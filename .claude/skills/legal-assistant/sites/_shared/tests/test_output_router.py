"""Tests for output_router.py — Phase B10."""

from __future__ import annotations

import os
import sys
from datetime import date
from pathlib import Path

import pytest

_SHARED = Path(__file__).resolve().parents[1]
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

import output_router as router  # noqa: E402


@pytest.fixture
def fake_drive(tmp_path):
    """Simulated Drive base with a per-counterparty project folder."""
    base = tmp_path / "drive"
    base.mkdir()
    return base


@pytest.fixture
def fake_artifact(tmp_path):
    src = tmp_path / "source.docx"
    src.write_bytes(b"PK\x03\x04" + b"fake docx content ABC")
    return router.OutputArtifact(
        src_path=src,
        slug="van-gog-grubbenvorst",
        counterparty_folder_name="VanGog_Project_Benelux_Ops",
        doc_kind="loi",
        version_label="v1",
        generated_date="2026-04-20",
    )


# ---------------------------------------------------------------------------
# Filename construction
# ---------------------------------------------------------------------------

def test_filename_loi_docx(fake_artifact):
    assert fake_artifact.filename == \
        "20260420_DE_LOI_Site_van-gog-grubbenvorst_v1_(DRAFT).docx"


def test_filename_loi_qa_txt(fake_artifact):
    fake_artifact.doc_kind = "loi_qa"
    assert fake_artifact.filename == \
        "20260420_DE_LOI_Site_van-gog-grubbenvorst_v1_qa.txt"


def test_filename_gate_report_json(fake_artifact):
    fake_artifact.doc_kind = "gate_report"
    assert fake_artifact.filename == \
        "20260420_DE_gate-report_van-gog-grubbenvorst_v1.json"


def test_invalid_doc_kind_raises(tmp_path):
    src = tmp_path / "s"
    src.write_text("x")
    with pytest.raises(ValueError, match="unknown doc_kind"):
        router.OutputArtifact(
            src_path=src,
            slug="x",
            counterparty_folder_name="y",
            doc_kind="whatever",
        )


# ---------------------------------------------------------------------------
# route() happy path
# ---------------------------------------------------------------------------

def test_route_copies_to_drive(fake_drive, fake_artifact):
    dest = router.route(fake_artifact, drive_base=fake_drive)
    assert dest.exists()
    assert dest.parent.name == "drafts"
    assert dest.parent.parent.name == "VanGog_Project_Benelux_Ops"
    # content matches source
    assert dest.read_bytes() == fake_artifact.src_path.read_bytes()


def test_route_creates_subfolders(fake_drive, fake_artifact):
    router.route(fake_artifact, drive_base=fake_drive)
    project = fake_drive / "VanGog_Project_Benelux_Ops"
    assert (project / "drafts").exists()
    assert (project / "documents").exists()
    assert (project / "signed").exists()


def test_route_idempotent_same_hash(fake_drive, fake_artifact):
    d1 = router.route(fake_artifact, drive_base=fake_drive)
    d2 = router.route(fake_artifact, drive_base=fake_drive)
    assert d1 == d2
    # No version bump — same hash → no-op
    assert d1.name == "20260420_DE_LOI_Site_van-gog-grubbenvorst_v1_(DRAFT).docx"


def test_route_same_day_collision_bumps_to_v1b(fake_drive, fake_artifact):
    # First routing
    d1 = router.route(fake_artifact, drive_base=fake_drive)
    # Mutate source content (→ different hash) but same filename target
    fake_artifact.src_path.write_bytes(b"PK\x03\x04different content")
    # Fresh artifact with same initial version_label, same day
    new_artifact = router.OutputArtifact(
        src_path=fake_artifact.src_path,
        slug=fake_artifact.slug,
        counterparty_folder_name=fake_artifact.counterparty_folder_name,
        doc_kind=fake_artifact.doc_kind,
        version_label="v1",
        generated_date=fake_artifact.generated_date,
    )
    d2 = router.route(new_artifact, drive_base=fake_drive)
    assert d1 != d2
    assert "_v1b_" in d2.name


def test_route_raises_drive_unavailable_if_base_missing(fake_artifact, tmp_path):
    nonexistent = tmp_path / "not_there"
    with pytest.raises(router.DriveUnavailable):
        router.route(fake_artifact, drive_base=nonexistent)


def test_route_raises_filenotfound_if_source_missing(fake_drive, tmp_path):
    a = router.OutputArtifact(
        src_path=tmp_path / "nope.docx",
        slug="x",
        counterparty_folder_name="y",
        doc_kind="loi",
    )
    # Create the destination folder first so DriveUnavailable doesn't mask
    # the file-not-found check.
    fake_drive.mkdir(exist_ok=True)
    with pytest.raises(FileNotFoundError):
        router.route(a, drive_base=fake_drive)


# ---------------------------------------------------------------------------
# Dry-run
# ---------------------------------------------------------------------------

def test_dry_run_mode_no_filesystem_writes(fake_drive, fake_artifact, monkeypatch):
    monkeypatch.setenv(router.DRY_RUN_ENV, "1")
    dest = router.route(fake_artifact, drive_base=fake_drive)
    # Dest was reported but not actually copied
    assert not dest.exists()
    # No subfolders created either
    assert not (fake_drive / "VanGog_Project_Benelux_Ops").exists()


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------

def test_manifest_created_on_first_route(fake_drive, fake_artifact):
    router.route(fake_artifact, drive_base=fake_drive)
    manifest = fake_drive / "VanGog_Project_Benelux_Ops" / "drafts" / "_manifest.json"
    assert manifest.exists()
    import json
    entries = json.loads(manifest.read_text())
    assert len(entries) == 1
    assert entries[0]["slug"] == "van-gog-grubbenvorst"
    assert entries[0]["doc_kind"] == "loi"
    assert entries[0]["hash"]


def test_manifest_appends_on_subsequent_routes(fake_drive, fake_artifact, tmp_path):
    router.route(fake_artifact, drive_base=fake_drive)
    # Different artifact: QA txt
    qa_src = tmp_path / "qa.txt"
    qa_src.write_text("QA report content")
    qa_artifact = router.OutputArtifact(
        src_path=qa_src,
        slug="van-gog-grubbenvorst",
        counterparty_folder_name="VanGog_Project_Benelux_Ops",
        doc_kind="loi_qa",
        version_label="v1",
        generated_date="2026-04-20",
    )
    router.route(qa_artifact, drive_base=fake_drive)
    manifest = fake_drive / "VanGog_Project_Benelux_Ops" / "drafts" / "_manifest.json"
    import json
    entries = json.loads(manifest.read_text())
    assert len(entries) == 2


# ---------------------------------------------------------------------------
# Suffix bumping unit tests
# ---------------------------------------------------------------------------

def test_bump_same_day_v1_to_v1b():
    assert router._bump_same_day_suffix("v1") == "v1b"


def test_bump_same_day_v1b_to_v1c():
    assert router._bump_same_day_suffix("v1b") == "v1c"


def test_bump_same_day_v1z_to_v1aa():
    assert router._bump_same_day_suffix("v1z") == "v1aa"


def test_bump_major_v1_to_v2():
    assert router._bump_major_version("v1") == "v2"


def test_bump_major_v1b_drops_suffix_and_bumps():
    assert router._bump_major_version("v1b") == "v2"


# ---------------------------------------------------------------------------
# SHA helper
# ---------------------------------------------------------------------------

def test_sha256_matches_reference_digest(tmp_path):
    p = tmp_path / "a.bin"
    p.write_bytes(b"abc")
    import hashlib
    expected = hashlib.sha256(b"abc").hexdigest()
    assert router._sha256(p) == expected
