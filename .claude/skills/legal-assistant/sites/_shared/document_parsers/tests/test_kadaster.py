"""Tests for KadasterParser — Phase B5."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_PARENT = Path(__file__).resolve().parents[2]
if str(_PARENT) not in sys.path:
    sys.path.insert(0, str(_PARENT))

from document_parsers.base import CorruptDocError, UnreadableScanError  # noqa: E402
from document_parsers.kadaster import KadasterParser  # noqa: E402


def _make_pdf(text: str, path: Path) -> None:
    import fitz
    doc = fitz.open()
    page = doc.new_page()
    for i, line in enumerate(text.split("\n")):
        page.insert_text((50, 50 + i * 15), line, fontsize=9)
    doc.save(str(path))
    doc.close()


def test_parcel_single_extraction(tmp_path):
    p = tmp_path / "kadaster.pdf"
    _make_pdf(
        "Kadastraal uittreksel\n"
        "Perceelgegevens\n"
        "gemeente Horst aan de Maas, sectie A, nummer 1234\n"
        "Eigendom: ja\n"
        "Omvang: 2,5 hectare",
        p,
    )
    r = KadasterParser(p).parse()
    parcels = r.fields_populated.get("D1_kadaster_parcels", [])
    assert len(parcels) == 1
    assert "sectie A" in parcels[0]
    assert "1234" in parcels[0]


def test_parcel_multiple_extraction(tmp_path):
    p = tmp_path / "kadaster.pdf"
    _make_pdf(
        "Kadaster\n"
        "gemeente Grubbenvorst, sectie B nummer 567\n"
        "gemeente Horst, sectie C, nummer 890\n"
        "Eigendom van Van Gog B.V.",
        p,
    )
    r = KadasterParser(p).parse()
    parcels = r.fields_populated.get("D1_kadaster_parcels", [])
    assert len(parcels) == 2


def test_title_type_recht_van_opstal_wins(tmp_path):
    p = tmp_path / "kadaster.pdf"
    _make_pdf(
        "Kadaster uittreksel\n"
        "gemeente Horst sectie A nummer 1\n"
        "Eigendom: Bedrijf X B.V.\n"
        "Tevens ingeschreven: recht van opstal ten behoeve van Y",
        p,
    )
    r = KadasterParser(p).parse()
    assert r.fields_populated["D2_title_type"] == "Recht van opstal"


def test_title_type_eigendom_default(tmp_path):
    p = tmp_path / "kadaster.pdf"
    _make_pdf(
        "Kadaster uittreksel\n"
        "gemeente Horst sectie A nummer 1\n"
        "Eigendom Bedrijf X B.V.\n"
        "Geen bijzondere rechten",
        p,
    )
    r = KadasterParser(p).parse()
    assert r.fields_populated["D2_title_type"] == "Eigendom"


def test_encumbrance_detected_hypotheek(tmp_path):
    p = tmp_path / "kadaster.pdf"
    _make_pdf(
        "Kadaster uittreksel\n"
        "gemeente Horst sectie A nummer 1\n"
        "Eigendom ja\n"
        "Hypotheek geregistreerd: EUR 500.000 ABN AMRO",
        p,
    )
    r = KadasterParser(p).parse()
    assert r.fields_populated["D3_encumbrances"] is True


def test_encumbrance_false_when_clean(tmp_path):
    p = tmp_path / "kadaster.pdf"
    _make_pdf(
        "Kadaster uittreksel\n"
        "gemeente Horst sectie A nummer 1\n"
        "Eigendom Bedrijf X B.V.\n"
        "Geen bijzondere rechten of lasten geregistreerd.",
        p,
    )
    r = KadasterParser(p).parse()
    assert r.fields_populated["D3_encumbrances"] is False


def test_corrupt_pdf_raises(tmp_path):
    p = tmp_path / "bad.pdf"
    p.write_bytes(b"not a PDF at all")
    with pytest.raises(CorruptDocError):
        KadasterParser(p).parse()


def test_unreadable_scan_raises(tmp_path):
    import fitz
    p = tmp_path / "empty.pdf"
    d = fitz.open()
    d.new_page()
    d.save(str(p))
    d.close()
    with pytest.raises(UnreadableScanError):
        KadasterParser(p).parse()


def test_parser_metadata():
    assert KadasterParser.doc_type == "kadaster_uittreksel"
    assert KadasterParser.parser_version == "0.1"
    assert "D1_kadaster_parcels" in KadasterParser.populates_fields
