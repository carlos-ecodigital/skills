"""Tests for EquipmentOEMParser - Phase B5."""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

import pytest

_PARENT = Path(__file__).resolve().parents[2]
if str(_PARENT) not in sys.path:
    sys.path.insert(0, str(_PARENT))

from document_parsers.base import CorruptDocError  # noqa: E402
from document_parsers.equipment_oem import EquipmentOEMParser  # noqa: E402


def _make_pdf(text: str, path: Path) -> None:
    import fitz
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((72, 72), text, fontsize=10)
    doc.save(str(path))
    doc.close()


# ----------------------------------------------------------------------
# Fixtures

CHP_SAMPLE = (
    "CHP Commissioning Certificate / WKK-inbedrijfstellingscertificaat\n"
    "Unit: Combined Heat and Power engine\n"
    "Electric output: 450 kWe\n"
    "Thermal output: 600 kWth\n"
    "Commissioning date: 15-06-2019\n"
    "Certified by: OEM GmbH\n"
)

BESS_SAMPLE = (
    "Battery Energy Storage System (BESS) grid-sharing agreement\n"
    "Installed power: 10 MW\n"
    "Rated capacity: 20 MWh\n"
    "Cell chemistry: LFP (LiFePO4)\n"
    "Configuration: containerised modular units\n"
    "Reference: BESS-2025-001\n"
)

PV_SAMPLE = (
    "Opbrengstrapport zonnepanelen\n"
    "Nominaal vermogen: 1500 kWp\n"
    "Verwachte jaarlijkse opbrengst: 1.425.000 kWh\n"
    "Meetperiode 10 jaar; P50 scenario.\n"
    "Locatie: Westland, gemeente Maasdijk.\n"
)

AMBIGUOUS_SAMPLE = (
    "Technical dossier containing CHP commissioning certificate details\n"
    "and Battery Energy Storage System specifications for combined site.\n"
    "CHP: 500 kWe / 700 kWth. BESS: 5 MW / 10 MWh, NMC chemistry.\n"
    "Commissioning: 10-01-2020.\n"
)

NO_EQUIPMENT_SAMPLE = (
    "General commercial letter regarding warehouse lease terms only.\n"
    "This letter makes no reference to any energy equipment whatsoever.\n"
    "Party A and party B agree to renew the warehouse occupancy terms.\n"
)

# ----------------------------------------------------------------------


def test_equipment_oem_detects_chp(tmp_path):
    p = tmp_path / "chp.pdf"
    _make_pdf(CHP_SAMPLE, p)
    r = EquipmentOEMParser(p).parse()
    assert r.fields_populated["_equipment_type"] == "chp"


def test_equipment_oem_chp_kwe_kwth(tmp_path):
    p = tmp_path / "chp.pdf"
    _make_pdf(CHP_SAMPLE, p)
    r = EquipmentOEMParser(p).parse()
    assert r.fields_populated["_chp_kw_e"] == 450.0
    assert r.fields_populated["_chp_kw_th"] == 600.0


def test_equipment_oem_chp_age_years(tmp_path):
    p = tmp_path / "chp.pdf"
    _make_pdf(CHP_SAMPLE, p)
    r = EquipmentOEMParser(p).parse()
    # Commissioned 15-06-2019; reference date is today.
    today = date.today()
    expected = today.year - 2019 - (0 if (today.month, today.day) >= (6, 15) else 1)
    assert r.fields_populated["_chp_age_years"] == expected


def test_equipment_oem_detects_bess(tmp_path):
    p = tmp_path / "bess.pdf"
    _make_pdf(BESS_SAMPLE, p)
    r = EquipmentOEMParser(p).parse()
    assert r.fields_populated["_equipment_type"] == "bess"


def test_equipment_oem_bess_mw_mwh_chemistry(tmp_path):
    p = tmp_path / "bess.pdf"
    _make_pdf(BESS_SAMPLE, p)
    r = EquipmentOEMParser(p).parse()
    assert r.fields_populated["_bess_mw"] == 10.0
    assert r.fields_populated["_bess_mwh"] == 20.0
    assert r.fields_populated["_bess_chemistry"] == "LFP"


def test_equipment_oem_detects_pv(tmp_path):
    p = tmp_path / "pv.pdf"
    _make_pdf(PV_SAMPLE, p)
    r = EquipmentOEMParser(p).parse()
    assert r.fields_populated["_equipment_type"] == "solar_pv"


def test_equipment_oem_pv_kwp(tmp_path):
    p = tmp_path / "pv.pdf"
    _make_pdf(PV_SAMPLE, p)
    r = EquipmentOEMParser(p).parse()
    assert r.fields_populated["_pv_kwp"] == 1500.0


def test_equipment_oem_pv_annual_kwh(tmp_path):
    p = tmp_path / "pv.pdf"
    _make_pdf(PV_SAMPLE, p)
    r = EquipmentOEMParser(p).parse()
    # 1.425.000 kWh (Dutch thousand separator).
    assert r.fields_populated["_pv_annual_kwh"] == 1425000.0


def test_equipment_oem_ambiguous_doc_runs_all(tmp_path):
    p = tmp_path / "mixed.pdf"
    _make_pdf(AMBIGUOUS_SAMPLE, p)
    r = EquipmentOEMParser(p).parse()
    assert any("ambiguous" in w for w in r.warnings)
    # Both CHP and BESS fields should be populated when ambiguous.
    assert "_chp_kw_e" in r.fields_populated
    assert "_bess_mw" in r.fields_populated


def test_equipment_oem_no_type_detected(tmp_path):
    p = tmp_path / "nothing.pdf"
    _make_pdf(NO_EQUIPMENT_SAMPLE, p)
    r = EquipmentOEMParser(p).parse()
    assert r.fields_populated["_equipment_type"] is None
    assert r.confidence == 0.1


def test_equipment_oem_corrupt_pdf(tmp_path):
    p = tmp_path / "broken.pdf"
    p.write_bytes(b"definitely not a PDF -- just bytes that cannot open")
    with pytest.raises(CorruptDocError):
        EquipmentOEMParser(p).parse()


def test_equipment_oem_unreadable_scan(tmp_path):
    # An empty PDF simulates an image-only scan (no extractable text).
    import fitz
    p = tmp_path / "scan.pdf"
    doc = fitz.open(); doc.new_page(); doc.save(str(p)); doc.close()
    from document_parsers.base import UnreadableScanError
    with pytest.raises(UnreadableScanError):
        EquipmentOEMParser(p).parse()


def test_equipment_oem_confidence_proportional(tmp_path):
    """Confidence should track (populated / expected) for runner types."""
    p_full = tmp_path / "full_bess.pdf"
    _make_pdf(BESS_SAMPLE, p_full)
    r_full = EquipmentOEMParser(p_full).parse()
    # All 3 BESS fields found: confidence == 1.0
    assert r_full.confidence == 1.0

    p_thin = tmp_path / "thin_bess.pdf"
    _make_pdf(
        "Battery Energy Storage System only -- no numeric specs here. "
        "Deliberately missing MW, MWh, chemistry labels entirely in body.",
        p_thin,
    )
    r_thin = EquipmentOEMParser(p_thin).parse()
    # 0 of 3 BESS fields should be populated.
    assert r_thin.confidence == 0.0


def test_equipment_oem_parser_metadata():
    assert EquipmentOEMParser.doc_type == "equipment_oem"
    assert EquipmentOEMParser.parser_version == "0.1"
    for f in ("_chp_kw_e", "_bess_mw", "_pv_kwp", "_equipment_type"):
        assert f in EquipmentOEMParser.populates_fields
