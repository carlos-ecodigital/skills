"""Integration: LOI engine output → output_router → fake Drive."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

import generate_site_loi as engine
import output_router as router


@pytest.fixture
def van_gog_yaml_path():
    return Path(__file__).resolve().parents[1] / "loi" / "examples" / "deal_van-gog.yaml"


def _generate_loi(tmp_path, van_gog_yaml_path):
    rc = engine.main([str(van_gog_yaml_path), "--out-dir", str(tmp_path)])
    assert rc == 0
    docx = next(tmp_path.glob("*_DE_LOI_Site_van-gog-grubbenvorst_v1_*.docx"))
    qa = next(tmp_path.glob("*_DE_LOI_Site_van-gog-grubbenvorst_v1_qa.txt"))
    return docx, qa


def test_engine_to_router_pipeline(tmp_path, van_gog_yaml_path):
    fake_drive = tmp_path / "drive"
    fake_drive.mkdir()
    out_dir = tmp_path / "tmp"
    out_dir.mkdir()

    docx, qa = _generate_loi(out_dir, van_gog_yaml_path)

    # Route the LOI .docx
    artifact = router.OutputArtifact(
        src_path=docx,
        slug="van-gog-grubbenvorst",
        counterparty_folder_name="Van Gog Grubbenvorst_Project_Benelux_Ops",
        doc_kind="loi",
    )
    dest = router.route(artifact, drive_base=fake_drive)
    assert dest.exists()
    assert dest.parent.name == "drafts"
    assert dest.parent.parent.name == "Van Gog Grubbenvorst_Project_Benelux_Ops"
    # Manifest updated
    manifest = dest.parent / "_manifest.json"
    entries = json.loads(manifest.read_text())
    assert any(e["slug"] == "van-gog-grubbenvorst" for e in entries)


def test_engine_to_router_qa_and_docx_both_routed(tmp_path, van_gog_yaml_path):
    fake_drive = tmp_path / "drive"
    fake_drive.mkdir()
    out_dir = tmp_path / "tmp"
    out_dir.mkdir()

    docx, qa = _generate_loi(out_dir, van_gog_yaml_path)

    for src, kind in ((docx, "loi"), (qa, "loi_qa")):
        a = router.OutputArtifact(
            src_path=src,
            slug="van-gog-grubbenvorst",
            counterparty_folder_name="VanGogCoB",
            doc_kind=kind,
        )
        dest = router.route(a, drive_base=fake_drive)
        assert dest.exists()

    drafts = fake_drive / "VanGogCoB" / "drafts"
    # Must have both files
    files = list(drafts.iterdir())
    docx_count = sum(1 for f in files if f.suffix == ".docx")
    qa_count = sum(1 for f in files if f.name.endswith("_qa.txt"))
    assert docx_count >= 1
    assert qa_count >= 1


def test_router_dry_run_does_not_write_to_drive(
    tmp_path, van_gog_yaml_path, monkeypatch
):
    fake_drive = tmp_path / "drive"
    fake_drive.mkdir()
    out_dir = tmp_path / "tmp"
    out_dir.mkdir()

    docx, _ = _generate_loi(out_dir, van_gog_yaml_path)

    monkeypatch.setenv(router.DRY_RUN_ENV, "1")
    a = router.OutputArtifact(
        src_path=docx,
        slug="van-gog-grubbenvorst",
        counterparty_folder_name="DryRunCo",
        doc_kind="loi",
    )
    router.route(a, drive_base=fake_drive)
    # Dry-run: no files
    assert not (fake_drive / "DryRunCo").exists()


def test_router_drive_unavailable_clean_error(tmp_path, van_gog_yaml_path):
    out_dir = tmp_path / "tmp"
    out_dir.mkdir()
    docx, _ = _generate_loi(out_dir, van_gog_yaml_path)

    nonexistent = tmp_path / "not_mounted"
    a = router.OutputArtifact(
        src_path=docx,
        slug="x",
        counterparty_folder_name="y",
        doc_kind="loi",
    )
    with pytest.raises(router.DriveUnavailable):
        router.route(a, drive_base=nonexistent)
