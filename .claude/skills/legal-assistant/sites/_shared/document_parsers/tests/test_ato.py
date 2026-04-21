"""Tests for ATOParser — Phase B5."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_PARENT = Path(__file__).resolve().parents[2]
if str(_PARENT) not in sys.path:
    sys.path.insert(0, str(_PARENT))

from document_parsers.ato import ATOParser  # noqa: E402
from document_parsers.base import CorruptDocError, UnreadableScanError  # noqa: E402


def _make_pdf(text: str, path: Path) -> None:
    import fitz
    doc = fitz.open()
    # Put more text per page so density check stays clean
    page = doc.new_page()
    # Multi-line insert_text uses \n
    for i, line in enumerate(text.split("\n")):
        page.insert_text((50, 50 + i * 15), line, fontsize=9)
    doc.save(str(path))
    doc.close()


def test_dso_enexis_detected(tmp_path):
    p = tmp_path / "ato.pdf"
    _make_pdf(
        "Aansluit- en Transportovereenkomst\n"
        "Netbeheerder: Enexis Netbeheer B.V.\n"
        "Aansluitadres: Paprikastraat 12\n"
        "EAN: 871694841000123456\n"
        "Gecontracteerde capaciteit: 16 MVA\n"
        "Afname: 10 MW\n"
        "Teruglevering: 5 MW",
        p,
    )
    r = ATOParser(p).parse()
    assert r.fields_populated["B1_dso"] == "Enexis"


def test_dso_liander_detected(tmp_path):
    p = tmp_path / "ato.pdf"
    _make_pdf(
        "Aansluit- en Transportovereenkomst\n"
        "Netbeheerder: Liander N.V.\n"
        "Klant: AgroCompany Greenhouses B.V.\n"
        "EAN: 871694841000777888",
        p,
    )
    r = ATOParser(p).parse()
    assert r.fields_populated["B1_dso"] == "Liander"


def test_ean_18_digit_extracted(tmp_path):
    p = tmp_path / "ato.pdf"
    _make_pdf(
        "Enexis ATO 2024-001234\n"
        "EAN 871694841000555666\n"
        "16 MVA\n"
        "Afname 10 MW",
        p,
    )
    r = ATOParser(p).parse()
    assert r.fields_populated["B2_ean_code"] == "871694841000555666"


def test_mva_max_when_multiple_mentioned(tmp_path):
    p = tmp_path / "ato.pdf"
    _make_pdf(
        "Enexis\n"
        "Subaansluiting A: 8 MVA\n"
        "Subaansluiting B: 10 MVA\n"
        "Totale aansluiting: 20 MVA\n"
        "Afname 12 MW",
        p,
    )
    r = ATOParser(p).parse()
    assert r.fields_populated["B4_total_connection_mva"] == 20.0


def test_import_export_dutch_labels(tmp_path):
    p = tmp_path / "ato.pdf"
    _make_pdf(
        "Netbeheerder: Liander\n"
        "EAN 871694841000111222\n"
        "Totale aansluiting 16 MVA\n"
        "Afname: 10 MW\n"
        "Teruglevering: 5 MW",
        p,
    )
    r = ATOParser(p).parse()
    assert r.fields_populated["B5_total_import_mw"] == 10.0
    assert r.fields_populated["B6_total_export_mw"] == 5.0


def test_dutch_decimal_comma(tmp_path):
    p = tmp_path / "ato.pdf"
    _make_pdf(
        "Stedin\n"
        "EAN 871694841000111333\n"
        "Aansluiting 16,5 MVA\n"
        "Afname 10,2 MW",
        p,
    )
    r = ATOParser(p).parse()
    assert r.fields_populated["B4_total_connection_mva"] == 16.5
    assert r.fields_populated["B5_total_import_mw"] == 10.2


def test_confidence_proportional_to_fields_populated(tmp_path):
    p = tmp_path / "ato.pdf"
    # Only DSO — low confidence.
    _make_pdf("Enexis some other unrelated text to exceed 50 char threshold please", p)
    r = ATOParser(p).parse()
    assert 0 < r.confidence < 0.3   # only 1/6 of populates_fields


def test_warns_when_no_dso_recognized(tmp_path):
    p = tmp_path / "ato.pdf"
    _make_pdf(
        "Some local utility (Fictieve Netbeheer) ATO 2024 content unlabeled MVA MW data",
        p,
    )
    r = ATOParser(p).parse()
    # B1_dso should be absent
    assert "B1_dso" not in r.fields_populated
    # Warning emitted
    assert any("B1_dso" in w for w in r.warnings)


def test_raises_corrupt_on_non_pdf_bytes(tmp_path):
    p = tmp_path / "not.pdf"
    p.write_bytes(b"this is not a PDF")
    with pytest.raises(CorruptDocError):
        ATOParser(p).parse()


def test_raises_unreadable_scan_on_empty_pdf(tmp_path):
    import fitz
    p = tmp_path / "empty.pdf"
    doc = fitz.open()
    doc.new_page()
    doc.save(str(p))
    doc.close()
    with pytest.raises(UnreadableScanError):
        ATOParser(p).parse()


def test_parser_metadata():
    assert ATOParser.doc_type == "ato_document"
    assert ATOParser.parser_version == "0.1"
    assert "B4_total_connection_mva" in ATOParser.populates_fields
