"""Tests for KvKParser — Phase B5."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_PARENT = Path(__file__).resolve().parents[2]
if str(_PARENT) not in sys.path:
    sys.path.insert(0, str(_PARENT))

from document_parsers.base import CorruptDocError, UnreadableScanError  # noqa: E402
from document_parsers.kvk import KvKParser  # noqa: E402


def _make_pdf(text: str, path: Path) -> None:
    import fitz
    doc = fitz.open()
    page = doc.new_page()
    for i, line in enumerate(text.split("\n")):
        page.insert_text((50, 50 + i * 15), line, fontsize=9)
    doc.save(str(path))
    doc.close()


def test_kvk_labelled_match(tmp_path):
    p = tmp_path / "kvk.pdf"
    _make_pdf(
        "Uittreksel Handelsregister Kamer van Koophandel\n"
        "KvK-nummer 12345678\n"
        "Statutaire naam: Van Gog Grubbenvorst B.V.\n"
        "Vestigingsadres: Kasteelstraat 12, 5971 AB Grubbenvorst",
        p,
    )
    r = KvKParser(p).parse()
    assert r.fields_populated["A2_kvk_number"] == "12345678"


def test_statutaire_naam_extracted(tmp_path):
    p = tmp_path / "kvk.pdf"
    _make_pdf(
        "Uittreksel Handelsregister\n"
        "KvK-nummer 87654321\n"
        "Statutaire naam: Moerman Lilium B.V.\n"
        "Vestigingsadres: Greenhouse Weg 5",
        p,
    )
    r = KvKParser(p).parse()
    assert r.fields_populated["A1_legal_name"].startswith("Moerman Lilium")


def test_address_extracted(tmp_path):
    p = tmp_path / "kvk.pdf"
    _make_pdf(
        "Handelsregister Uittreksel\n"
        "KvK-nummer 11223344\n"
        "Statutaire naam: Test B.V.\n"
        "Vestigingsadres: Voorbeeldstraat 42, 1234 AB Teststad",
        p,
    )
    r = KvKParser(p).parse()
    addr = r.fields_populated.get("A3_registered_address", "")
    assert "Voorbeeldstraat" in addr
    assert "1234 AB" in addr


def test_signing_authority_sole(tmp_path):
    p = tmp_path / "kvk.pdf"
    _make_pdf(
        "Uittreksel Handelsregister\n"
        "KvK-nummer 12345678\n"
        "Statutaire naam: X B.V.\n"
        "Vestigingsadres: Y-straat 1\n"
        "Bestuurder: Marion van Gog\n"
        "Bevoegdheid: Zelfstandig bevoegd",
        p,
    )
    r = KvKParser(p).parse()
    assert r.fields_populated["A6_signing_authority"] == "Sole"


def test_signing_authority_joint(tmp_path):
    p = tmp_path / "kvk.pdf"
    _make_pdf(
        "Uittreksel Handelsregister\n"
        "KvK-nummer 12345678\n"
        "Statutaire naam: X B.V.\n"
        "Vestigingsadres: Y-straat 1\n"
        "Bestuurder: Jan Jansen\n"
        "Bestuurder: Piet Pietersen\n"
        "Bevoegdheid: Gezamenlijk bevoegd",
        p,
    )
    r = KvKParser(p).parse()
    assert r.fields_populated["A6_signing_authority"] == "Joint"


def test_signatory_first_bestuurder(tmp_path):
    p = tmp_path / "kvk.pdf"
    _make_pdf(
        "Uittreksel Handelsregister\n"
        "KvK-nummer 12345678\n"
        "Statutaire naam: Van Gog B.V.\n"
        "Vestigingsadres: Kasteelstraat 1\n"
        "Bestuurder: Marion van Gog\n"
        "Bevoegdheid: Zelfstandig bevoegd",
        p,
    )
    r = KvKParser(p).parse()
    sig = r.fields_populated.get("A4_signatory_name", "")
    assert "Marion" in sig
    assert "Gog" in sig


def test_corrupt_pdf_raises(tmp_path):
    p = tmp_path / "bad.pdf"
    p.write_bytes(b"nope")
    with pytest.raises(CorruptDocError):
        KvKParser(p).parse()


def test_unreadable_scan_raises(tmp_path):
    import fitz
    p = tmp_path / "empty.pdf"
    d = fitz.open()
    d.new_page()
    d.save(str(p))
    d.close()
    with pytest.raises(UnreadableScanError):
        KvKParser(p).parse()


def test_parser_metadata():
    assert KvKParser.doc_type == "kvk_uittreksel"
    assert KvKParser.parser_version == "0.1"
    assert "A2_kvk_number" in KvKParser.populates_fields
