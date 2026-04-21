"""Tests for SDEPlusParser — Phase B5."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_PARENT = Path(__file__).resolve().parents[2]
if str(_PARENT) not in sys.path:
    sys.path.insert(0, str(_PARENT))

from document_parsers.base import CorruptDocError, UnreadableScanError  # noqa: E402
from document_parsers.sde_plus import SDEPlusParser  # noqa: E402


def _make_pdf(text: str, path: Path) -> None:
    import fitz
    doc = fitz.open()
    page = doc.new_page()
    for i, line in enumerate(text.split("\n")):
        page.insert_text((50, 50 + i * 15), line, fontsize=9)
    doc.save(str(path))
    doc.close()


def test_sde_reference_extracted(tmp_path):
    p = tmp_path / "sde.pdf"
    _make_pdf(
        "RVO.nl Beschikking\n"
        "Subsidieregeling: SDE++ 2023-001234\n"
        "Categorie: Aquathermie\n"
        "Maximale subsidie: EUR 1.234.567,89\n"
        "Besluit: 14 april 2024\n"
        "Subsidieduur: 15 jaar",
        p,
    )
    r = SDEPlusParser(p).parse()
    assert "SDE++" in r.fields_populated.get("_sde_reference", "")


def test_sde_awarded_amount_dutch_format(tmp_path):
    p = tmp_path / "sde.pdf"
    # Use EUR (not €) to avoid fitz font-rendering quirks.
    # Use "Maximale subsidie:" label which matches parser AMOUNT_RE alternative.
    _make_pdf(
        "Maximale subsidie: EUR 1.234.567,89\n"
        "SDE++ kenmerk 2024-001122\n"
        "Categorie industriële restwarmte\n"
        "Datum besluit: 1 januari 2024\n"
        "Subsidieduur: 15 jaar",
        p,
    )
    r = SDEPlusParser(p).parse()
    assert r.fields_populated.get("_sde_awarded_eur") == 1234567.89


def test_sde_decision_date_dutch_months(tmp_path):
    p = tmp_path / "sde.pdf"
    # Parser DATE_RE matches "datum besluit" / "beschikkingsdatum" / "beschikt op" / "datum".
    _make_pdf(
        "SDE++ 2024-999888\n"
        "Maximale subsidie: EUR 500.000,00\n"
        "Datum besluit: 15 maart 2024\n"
        "Subsidieduur: 12 jaar",
        p,
    )
    r = SDEPlusParser(p).parse()
    date_str = r.fields_populated.get("_sde_decision_date", "")
    assert "2024" in date_str
    assert ("03" in date_str or "maart" in date_str)


def test_sde_duration_years_extracted(tmp_path):
    p = tmp_path / "sde.pdf"
    _make_pdf(
        "SDE++ 2024-111111\n"
        "Maximale subsidie: EUR 100.000,00\n"
        "Besluit: 1 januari 2024\n"
        "Subsidieduur: 12 jaar",
        p,
    )
    r = SDEPlusParser(p).parse()
    dur = r.fields_populated.get("_sde_duration_years")
    assert dur == 12 or dur == 12.0


def test_sde_raises_corrupt_on_bad_pdf(tmp_path):
    p = tmp_path / "not.pdf"
    p.write_bytes(b"not a real PDF")
    with pytest.raises(CorruptDocError):
        SDEPlusParser(p).parse()


def test_sde_raises_unreadable_scan_on_empty(tmp_path):
    import fitz
    p = tmp_path / "empty.pdf"
    doc = fitz.open()
    doc.new_page()
    doc.save(str(p))
    doc.close()
    with pytest.raises(UnreadableScanError):
        SDEPlusParser(p).parse()


def test_sde_parser_metadata():
    assert SDEPlusParser.doc_type == "sde_plus_plus"
    assert SDEPlusParser.parser_version == "0.1"
    assert "_sde_reference" in SDEPlusParser.populates_fields
    assert "_sde_awarded_eur" in SDEPlusParser.populates_fields


def test_sde_populates_meta_fields_not_registry_ids(tmp_path):
    """SDE parser populates _sde_* meta fields — no registry (A*, B*, ...) IDs."""
    p = tmp_path / "sde.pdf"
    _make_pdf(
        "SDE++ 2024-555\n"
        "Subsidiebedrag: € 100.000,00\n"
        "Besluit 5 mei 2024\n"
        "Duur 10 jaar",
        p,
    )
    r = SDEPlusParser(p).parse()
    non_meta = {k for k in r.fields_populated if not k.startswith("_")}
    assert non_meta == set()
