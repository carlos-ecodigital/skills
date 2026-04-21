"""Artifact storage — copy LOI .docx + QA/session/audit artifacts to Drive.

v3.5.3 scope J13 — deferred until v3.7.0.

Writes to:
    Fundraise DE/06_Shared_Collateral/_Drafts/{YYYYMMDD}_DEG_LOI-{Type}_{slug}/

Where `{slug}` is derived from `counterparty.name` via a simple slugify, and
`{Type}` is one of EndUser / Distributor / Wholesale / StrategicSupplier /
EcosystemPartnership.

Drive is mounted at `~/Library/CloudStorage/GoogleDrive-carlos@ecodigital.group/`
by default. If the mount is unavailable (e.g., CI environments, alternate
operator), `upload_artifact` logs a warning and returns the local output path
unchanged.
"""
from __future__ import annotations

import os
import re
import shutil
from datetime import datetime
from pathlib import Path


DEFAULT_DRIVE_ROOT = (
    "/Users/crmg/Library/CloudStorage/GoogleDrive-carlos@ecodigital.group"
    "/Fundraise DE/06_Shared_Collateral/_Drafts"
)


def _slugify(name: str) -> str:
    """Lowercase, strip non-alnum, collapse hyphens."""
    slug = re.sub(r"[^\w\s-]", "", name.lower())
    slug = re.sub(r"[\s_]+", "-", slug).strip("-")
    return slug or "counterparty"


def _dated_folder_name(intake: dict) -> str:
    """`{YYYYMMDD}_DEG_LOI-{Type}_{slug}` — matches existing Drive convention."""
    loi_date = intake.get("dates", {}).get("loi_date", "")
    # Accept both "17 April 2026" and "2026-04-17" formats.
    yyyymmdd = ""
    for fmt in ("%d %B %Y", "%Y-%m-%d"):
        try:
            yyyymmdd = datetime.strptime(loi_date, fmt).strftime("%Y%m%d")
            break
        except (ValueError, TypeError):
            continue
    if not yyyymmdd:
        yyyymmdd = datetime.now().strftime("%Y%m%d")

    loi_type = intake.get("type", "Unknown")
    slug = _slugify(intake.get("counterparty", {}).get("name", ""))
    return f"{yyyymmdd}_DEG_LOI-{loi_type}_{slug}"


def upload_artifact(
    output_path: str,
    intake: dict,
    *,
    drive_root: str | None = None,
    dry_run: bool = False,
) -> str:
    """Copy .docx + sibling artefacts (_qa, _SESSION_LOG, _AUDIT) to Drive.

    Args:
        output_path: Path to the primary .docx emitted by generate_loi.py.
        intake: Parsed intake YAML (must include `dates.loi_date`, `type`,
                `counterparty.name`).
        drive_root: Override the default Drive path for testing / alternate
                    operator use. Defaults to Carlos's Fundraise DE folder.
        dry_run: When True, compute the target path + report what would be
                 copied, but don't actually copy. Returns the intended Drive
                 path as a string.

    Returns:
        The Drive folder path as a string (target, whether or not copy
        actually ran). Returns the local output path unchanged if Drive is
        unreachable.
    """
    root = drive_root or DEFAULT_DRIVE_ROOT
    root_path = Path(root)

    # Drive unreachable → soft-fail, keep local
    if not dry_run and not root_path.parent.exists():
        print(
            f"[artifact_storage] WARN: Drive root unavailable ({root}). "
            f"Leaving artefact at {output_path}."
        )
        return output_path

    target_folder = root_path / _dated_folder_name(intake)

    if dry_run:
        return str(target_folder)

    target_folder.mkdir(parents=True, exist_ok=True)

    output = Path(output_path)
    stem = output.stem
    parent = output.parent

    # Primary .docx + sibling artefacts emitted alongside
    candidates = [
        output,
        parent / f"{stem}_qa.txt",
        parent / f"{stem}_SESSION_LOG.md",
        parent / f"{stem}_AUDIT.txt",
        parent / f"{stem}_audit.txt",  # --audit-only mode output
    ]

    copied = []
    for src in candidates:
        if src.exists():
            dst = target_folder / src.name
            shutil.copy2(src, dst)
            copied.append(str(dst))

    print(f"[artifact_storage] Copied {len(copied)} artefact(s) to {target_folder}")
    for p in copied:
        print(f"  - {p}")

    return str(target_folder)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: artifact_storage.py <output.docx> [--dry-run]")
        sys.exit(1)

    import yaml  # deferred import — tests shouldn't need it

    docx = sys.argv[1]
    dry = "--dry-run" in sys.argv
    # Assume caller passes intake YAML path via env var or uses defaults.
    intake_path = os.environ.get("INTAKE_PATH", "intake.yaml")
    with open(intake_path) as f:
        intake = yaml.safe_load(f)

    result = upload_artifact(docx, intake, dry_run=dry)
    print(result)
