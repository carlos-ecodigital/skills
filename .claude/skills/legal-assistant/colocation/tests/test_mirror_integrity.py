"""Mirror-integrity check — v3.5.8 PRINCIPLES.md tripwire #1.

The upstream skills repo (`carlos-ecodigital/skills`) is the source of
truth; the staging repo (`EcoDigital-Software/degitos-staging`) maintains
byte-identical mirror copies of the key generator + test files under a
different path layout. The failure mode this guards against:

  1. Engineer edits staging copy of `generate_loi.py` directly
  2. Change is never mirrored to upstream
  3. Next mirror update from upstream overwrites the staging fix silently

`tests/mirror-manifest.txt` is the contract: a sha256 list generated from
upstream and committed verbatim in both repos. This test computes the
current hashes and diffs against the manifest. Mismatch => drift.

**Scope:** tests/ files only. `generate_loi.py` is excluded because
staging imports from `de-document-factory/` (DEGitOS naming) while
upstream imports from `document-factory/`, so a byte-level hash would
false-positive on a legitimate divergence. The drift class this tripwire
targets is the silent one — test-harness edits that slip past PR review
because nobody reads test diffs as carefully as they read generator
diffs. Generator drift is handled by the standard review process plus
the new v3.5.8 golden-file tests.

The manifest regen script lives in upstream at
`tests/regen-mirror-manifest.sh`. Staging never regenerates; it only
checks.

Rationale: golden-file tests exercise render paths per upstream's
intakes; they cannot catch a one-character edit to `generate_loi.py` in
staging that changes output only for fixtures staging doesn't have. An
integrity sentinel catches that class in O(ms).
"""
from __future__ import annotations

import hashlib
from pathlib import Path

import pytest


_TESTS_DIR = Path(__file__).resolve().parent
_COLOCATION_DIR = _TESTS_DIR.parent
_MANIFEST = _TESTS_DIR / "mirror-manifest.txt"


def _parse_manifest(path: Path) -> list[tuple[str, str]]:
    """Return list of (sha256, relative_path) from a sha256sum-format file.

    Comment lines (starting with '#') and blank lines are skipped."""
    out: list[tuple[str, str]] = []
    with open(path) as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            # sha256sum default format: "<hex>  <path>" (two spaces)
            parts = line.split(None, 1)
            if len(parts) != 2:
                continue
            sha, rel = parts
            out.append((sha, rel))
    return out


def _sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _manifest_entries():
    if not _MANIFEST.exists():
        return []
    return _parse_manifest(_MANIFEST)


class TestMirrorIntegrity:
    """Each mirrored file's current SHA-256 must match the manifest entry.

    If you intentionally edit a mirrored file upstream:
      1. Edit the file
      2. Run `bash tests/regen-mirror-manifest.sh` (upstream only)
      3. Copy the regenerated manifest verbatim to staging
      4. Commit the manifest change in BOTH repos

    Any other path (direct staging edit, skipping the regen script) will
    fail this test."""

    def test_manifest_exists(self):
        assert _MANIFEST.exists(), (
            f"mirror-manifest.txt missing at {_MANIFEST}. "
            f"Regenerate with tests/regen-mirror-manifest.sh in upstream."
        )

    def test_manifest_non_empty(self):
        entries = _manifest_entries()
        assert len(entries) > 0, "mirror-manifest.txt parsed to zero entries"

    @pytest.mark.parametrize(
        "entry",
        _manifest_entries(),
        ids=[rel for _, rel in _manifest_entries()],
    )
    def test_file_hash_matches_manifest(self, entry):
        expected_sha, rel_path = entry
        full = _COLOCATION_DIR / rel_path
        assert full.exists(), (
            f"Manifest lists {rel_path} but file is absent at {full}. "
            f"Mirror is incomplete."
        )
        actual_sha = _sha256_of(full)
        assert actual_sha == expected_sha, (
            f"Mirror drift detected: {rel_path}\n"
            f"  expected sha256: {expected_sha}\n"
            f"  actual sha256:   {actual_sha}\n"
            f"If this change is intentional: regen manifest in upstream\n"
            f"(bash tests/regen-mirror-manifest.sh) and copy to staging."
        )
