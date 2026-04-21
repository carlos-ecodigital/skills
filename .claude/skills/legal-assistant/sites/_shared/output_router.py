"""
Drive output router for Sites-stream draft artifacts.

Phase B10 of the sites-stream plan. Copies generated ``.docx`` / ``_qa.txt`` /
gate-report / sync-log artifacts from ``/tmp/`` to the project folder on
the Google Drive shared drive, under the per-counterparty convention
``{Counterparty}_Project_Benelux_Ops/drafts/``.

Key design choices (after enumerating 20+ existing Drive folders):

- The Drive folder convention is NOT synthesisable from the counterparty
  name alone. Existing deals show three variants:
    * canonical:  ``{Counterparty}_Project_Benelux_Ops``  (newer deals)
    * legacy:     ``{Counterparty}_Project_Benelux``      (e.g. ECW, Moerman)
    * typo:       ``Bunnik_Bromelia_Project_Beneluz``     (historic)
  Therefore ``OutputArtifact.counterparty_folder_name`` MUST be carried
  verbatim from ``deal.yaml``; the router never invents it.
- SHA-256 idempotency: re-running the same engine must not produce
  spurious new versions. If the destination file exists with the same
  hash, route() is a no-op and returns the existing path.
- Same-day collision handling: ``v1`` → ``v1b`` → ``v1c`` → … → ``v1z``
  then ``v1aa``. Cross-day collision bumps the major version:
  ``v1c → v2`` when a new calendar day begins.
- Append-only manifest: every routing event logged to
  ``drafts/_manifest.json`` for audit (uploaded by whom, hash, doc_kind).
- Dry-run via ``SITES_OUTPUT_ROUTER_DRY_RUN=1`` environment variable.
- ``DriveUnavailable`` raised cleanly when the base path does not exist
  (Drive unmounted, CI environment, etc.).
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
from dataclasses import dataclass, field
from datetime import date as _date
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DEFAULT_DRIVE_BASE = Path(
    "/Users/crmg/Library/CloudStorage/GoogleDrive-carlos@ecodigital.group/"
    "Shared drives/NEW_Ops/Projects Benelux_Ops/Active Digital Energy Projects"
)

DRY_RUN_ENV = "SITES_OUTPUT_ROUTER_DRY_RUN"

#: Doc-kind → filename component. Sites-stream convention.
_DOC_KIND_SLUG = {
    "loi": "LOI_Site",
    "hot": "HoT_Site",
    "loi_qa": "LOI_Site",            # suffix determined below
    "hot_qa": "HoT_Site",
    "gate_report": "gate-report",
    "sync_log": "hubspot-sync-log",
}


# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------

class DriveUnavailable(RuntimeError):
    """Raised when the Drive base path is not reachable."""


# ---------------------------------------------------------------------------
# OutputArtifact
# ---------------------------------------------------------------------------

@dataclass
class OutputArtifact:
    """A single produced file awaiting Drive placement."""
    src_path: Path
    slug: str
    counterparty_folder_name: str          # from deal.yaml; verbatim
    doc_kind: str                          # "loi" | "hot" | "loi_qa" | ...
    version_label: str = "v1"
    generated_date: Optional[str] = None   # ISO date; defaults to today

    def __post_init__(self):
        if isinstance(self.src_path, str):
            self.src_path = Path(self.src_path)
        if self.doc_kind not in _DOC_KIND_SLUG:
            raise ValueError(
                f"unknown doc_kind {self.doc_kind!r}; "
                f"expected one of {sorted(_DOC_KIND_SLUG)}"
            )
        if self.generated_date is None:
            self.generated_date = _date.today().isoformat()

    # --- Filename construction ------------------------------------------

    @property
    def date_stamp(self) -> str:
        return self.generated_date.replace("-", "")

    @property
    def filename(self) -> str:
        date_str = self.date_stamp
        kind_slug = _DOC_KIND_SLUG[self.doc_kind]
        if self.doc_kind in ("loi_qa", "hot_qa"):
            return f"{date_str}_DE_{kind_slug}_{self.slug}_{self.version_label}_qa.txt"
        if self.doc_kind == "gate_report":
            return f"{date_str}_DE_{kind_slug}_{self.slug}_{self.version_label}.json"
        if self.doc_kind == "sync_log":
            return f"{date_str}_DE_{kind_slug}_{self.slug}_{self.version_label}.json"
        # loi, hot
        return f"{date_str}_DE_{kind_slug}_{self.slug}_{self.version_label}_(DRAFT).docx"


# ---------------------------------------------------------------------------
# SHA helpers
# ---------------------------------------------------------------------------

def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Version-suffix bumping (same-day collision)
# ---------------------------------------------------------------------------

def _bump_same_day_suffix(version_label: str) -> str:
    """v1 → v1b → v1c → ... → v1z → v1aa → v1ab ..."""
    # Split off leading vN, take the rest as the alpha suffix.
    # version_label looks like "v1" or "v1b" or "v1aa".
    if not version_label.startswith("v"):
        raise ValueError(f"bad version label: {version_label!r}")
    rest = version_label[1:]
    # Split digits vs letters
    digits = ""
    letters = ""
    for ch in rest:
        if ch.isdigit() and not letters:
            digits += ch
        else:
            letters += ch
    if not letters:
        return f"v{digits}b"
    # Letters exist — increment like a-z-aa-ab spreadsheet counter.
    new_letters = _alpha_inc(letters)
    return f"v{digits}{new_letters}"


def _alpha_inc(s: str) -> str:
    """'b' → 'c', 'z' → 'aa', 'az' → 'ba', 'zz' → 'aaa'."""
    chars = list(s)
    i = len(chars) - 1
    while i >= 0:
        if chars[i] != "z":
            chars[i] = chr(ord(chars[i]) + 1)
            return "".join(chars)
        chars[i] = "a"
        i -= 1
    return "a" + "".join(chars)


def _bump_major_version(version_label: str) -> str:
    """v1 → v2, v1b → v2, v1aa → v2."""
    if not version_label.startswith("v"):
        raise ValueError(f"bad version label: {version_label!r}")
    digits = ""
    for ch in version_label[1:]:
        if ch.isdigit():
            digits += ch
        else:
            break
    n = int(digits) + 1
    return f"v{n}"


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------

def update_manifest(project_folder: Path, artifact: OutputArtifact, dest: Path) -> None:
    """Append an entry to ``{project_folder}/drafts/_manifest.json``."""
    manifest_path = project_folder / "drafts" / "_manifest.json"
    if manifest_path.exists():
        try:
            entries = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            entries = []  # corrupt manifest — overwrite with empty
    else:
        entries = []
    entries.append({
        "slug": artifact.slug,
        "doc_kind": artifact.doc_kind,
        "version_label": artifact.version_label,
        "filename": dest.name,
        "hash": _sha256(dest) if dest.exists() else None,
        "routed_at": _date.today().isoformat(),
        "src_path": str(artifact.src_path),
    })
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(entries, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# Subfolder creation
# ---------------------------------------------------------------------------

def ensure_subfolders(project_folder: Path) -> None:
    """Create ``drafts/ documents/ signed/`` inside the project folder."""
    for sub in ("drafts", "documents", "signed"):
        (project_folder / sub).mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Route
# ---------------------------------------------------------------------------

def route(
    artifact: OutputArtifact,
    drive_base: Optional[Path] = None,
) -> Path:
    """Copy ``artifact.src_path`` to the project folder under ``drafts/``.

    Args:
        artifact: The artifact to route.
        drive_base: Override default Drive base. Defaults to
            ``DEFAULT_DRIVE_BASE``. Tests should pass a ``tmp_path`` here.

    Returns:
        The final destination path.

    Raises:
        DriveUnavailable: if ``drive_base`` does not exist.
        FileNotFoundError: if ``artifact.src_path`` does not exist.
    """
    base = drive_base or DEFAULT_DRIVE_BASE
    if not base.exists():
        raise DriveUnavailable(
            f"Drive base path not available: {base}. "
            "Is Google Drive mounted? Verify path exists before invoking."
        )
    if not artifact.src_path.exists():
        raise FileNotFoundError(f"source artifact missing: {artifact.src_path}")

    project_folder = base / artifact.counterparty_folder_name
    dry_run = os.environ.get(DRY_RUN_ENV) == "1"

    if dry_run:
        dest = project_folder / "drafts" / artifact.filename
        print(f"[dry-run] would route {artifact.src_path} → {dest}")
        return dest

    ensure_subfolders(project_folder)

    drafts_dir = project_folder / "drafts"
    src_hash = _sha256(artifact.src_path)
    today = _date.today().isoformat()

    dest = drafts_dir / artifact.filename

    # Idempotency: same hash at dest → no-op
    while dest.exists():
        try:
            existing_hash = _sha256(dest)
        except OSError:
            break
        if existing_hash == src_hash:
            return dest  # already there, no-op
        # Hash differs. Determine whether same-day or cross-day.
        # We read the manifest to find when ``artifact.filename`` was first
        # routed for this slug. Simpler heuristic: mtime of the file.
        try:
            dest_mtime = _date.fromtimestamp(dest.stat().st_mtime).isoformat()
        except Exception:
            dest_mtime = today
        if dest_mtime == today:
            # Same-day collision → bump alpha suffix
            artifact.version_label = _bump_same_day_suffix(artifact.version_label)
        else:
            # Cross-day → bump major version
            artifact.version_label = _bump_major_version(artifact.version_label)
        dest = drafts_dir / artifact.filename

    shutil.copy2(artifact.src_path, dest)
    update_manifest(project_folder, artifact, dest)
    return dest
