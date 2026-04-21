"""Tests for BestemmingsplanParser — Phase B5."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_PARENT = Path(__file__).resolve().parents[2]
if str(_PARENT) not in sys.path:
    sys.path.insert(0, str(_PARENT))

from document_parsers.base import CorruptDocError, UnreadableScanError  # noqa: E402
from document_parsers.bestemmingsplan import BestemmingsplanParser  # noqa: E402


def _make_pdf(text: str, path: Path) -> None:
    import fitz
    doc = fitz.open()
    page = doc.new_page()
    for i, line in enumerate(text.split("\n")):
        page.insert_text((50, 50 + i * 15), line, fontsize=9)
    doc.save(str(path))
    doc.close()


def test_glastuinbouw_detected(tmp_path):
    p = tmp_path / "bestemming.pdf"
    _make_pdf(
        "Bestemmingsplan Buitengebied Horst aan de Maas\n"
        "Perceel A.1234\n"
        "Bestemming: Agrarisch - Glastuinbouw\n"
        "Toegestaan: kassencomplex, glastuinbouwbedrijf",
        p,
    )
    r = BestemmingsplanParser(p).parse()
    assert r.fields_populated["D4_zoning_designation"] == "Agrarisch - Glastuinbouw"


def test_bedrijventerrein_detected(tmp_path):
    p = tmp_path / "bestemming.pdf"
    _make_pdf(
        "Bestemmingsplan gemeente Venlo\n"
        "Perceel B.456\n"
        "Bestemming: Bedrijventerrein\n"
        "Bouwhoogte max 12 m",
        p,
    )
    r = BestemmingsplanParser(p).parse()
    assert r.fields_populated["D4_zoning_designation"] == "Bedrijventerrein"


def test_priority_glastuinbouw_over_bare_agrarisch(tmp_path):
    p = tmp_path / "bestemming.pdf"
    _make_pdf(
        "Bestemmingsplan Buitengebied\n"
        "Hoofdbestemming: Agrarisch\n"
        "Sub-bestemming: Agrarisch - Glastuinbouw\n"
        "Specifieke functie: glastuinbouw",
        p,
    )
    r = BestemmingsplanParser(p).parse()
    # Priority: glastuinbouw wins over bare "Agrarisch"
    assert r.fields_populated["D4_zoning_designation"] == "Agrarisch - Glastuinbouw"


def test_no_zoning_found_warns(tmp_path):
    p = tmp_path / "bestemming.pdf"
    _make_pdf(
        "Bestemmingsplan Voorbeeld\n"
        "Specifieke regeling voor dit perceel\n"
        "Gemeentelijk monument categorie 2\n"
        "Additional planning regulation reference text placeholder",
        p,
    )
    r = BestemmingsplanParser(p).parse()
    assert "D4_zoning_designation" not in r.fields_populated
    assert any("no recognised zoning" in w for w in r.warnings)


def test_corrupt_pdf_raises(tmp_path):
    p = tmp_path / "bad.pdf"
    p.write_bytes(b"not a pdf")
    with pytest.raises(CorruptDocError):
        BestemmingsplanParser(p).parse()


def test_parser_metadata():
    assert BestemmingsplanParser.doc_type == "bestemmingsplan_excerpt"
    assert BestemmingsplanParser.parser_version == "0.1"
    assert BestemmingsplanParser.populates_fields == ["D4_zoning_designation"]
