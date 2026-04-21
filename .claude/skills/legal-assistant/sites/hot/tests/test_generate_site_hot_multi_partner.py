"""Tests for generate_site_hot.py Wave 2 — multi-partner Annex A fill.

Exercises the section-to-partner disambiguation layer added in v0.2:

  - A.* / C.* / G.Grower_* → Heat Offtaker
  - B.*                     → Grid Contributor (largest MVA on ties)
  - D.* / G.Landowner_*     → Landowner (distinct from grower)
  - E.*                     → deal-level (partner-agnostic)

Fixture: Van Gog 3-partner (kwekerijen heat offtaker, Grubbenvorst B.V. grid
contributor, Vastgoed landowner) materialised from the embedded YAML in
``fixtures_embedded``. Single-partner regression is re-asserted with the
Moerman fixture that also drives ``test_generate_site_hot_v0_1.py``.
"""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml
from docx import Document

_HOT_DIR = Path(__file__).resolve().parents[1]
if str(_HOT_DIR) not in sys.path:
    sys.path.insert(0, str(_HOT_DIR))

import generate_site_hot as engine  # noqa: E402

_TESTS_DIR = Path(__file__).resolve().parent
if str(_TESTS_DIR) not in sys.path:
    sys.path.insert(0, str(_TESTS_DIR))

import fixtures_embedded  # noqa: E402


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def van_gog_deal(tmp_path):
    path = fixtures_embedded.write_van_gog_fixture(tmp_path)
    return engine.load_deal(path)


@pytest.fixture
def van_gog_deal_path(tmp_path):
    return fixtures_embedded.write_van_gog_fixture(tmp_path)


@pytest.fixture
def moerman_deal(tmp_path):
    path = fixtures_embedded.write_fixture(tmp_path)
    return engine.load_deal(path)


def _annex_flat_text(docx_path: Path) -> str:
    doc = Document(str(docx_path))
    return "\n".join(
        c.text for tbl in doc.tables for r in tbl.rows for c in r.cells
    )


def _partner_warnings(warnings: list[str]) -> list[str]:
    """Filter out enum_normaliser noise so partner-disambiguation tests
    only assert on the warnings they actually own."""
    return [w for w in warnings if not w.startswith("enum_normaliser:")]


# ---------------------------------------------------------------------------
# 1. Multi-partner section disambiguation
# ---------------------------------------------------------------------------


def test_van_gog_3_partner_fill_disambiguates_sections(van_gog_deal, tmp_path):
    """All three Van Gog partners' data must land in the right cells:

      - A.* / C.* / G.Grower_* pulled from the kwekerijen (heat offtaker)
      - B.* pulled from the Grubbenvorst B.V. (grid contributor)
      - D.* / G.Landowner_* pulled from the Vastgoed B.V. (landowner)
    """
    warnings: list[str] = []
    values = engine.build_field_values(van_gog_deal, warnings=warnings)

    # A.* ← kwekerijen (Heat Offtaker)
    assert values["A.1"] == "Van Gog kwekerijen Grubbenvorst B.V."
    assert values["A.2"] == "34567890"
    assert values["A.4"] == "Koen Saris"
    assert values["A.11"] == "Vegetables / Groenten"

    # B.* ← Grubbenvorst B.V. (Grid Contributor)
    assert values["B.1"] == "Enexis"
    assert values["B.2"] == "871687510000099999"
    assert float(values["B.4"]) == 16.0

    # C.* ← kwekerijen (Heat Offtaker returns)
    assert values["C.1"] == 55
    assert values["C.4"] == 22

    # D.* ← Vastgoed (Landowner)
    assert values["D.1"] == "Horst aan de Maas, Sectie G, Nr 8812"
    assert values["D.5"] == 300
    assert values["D.6"] == 30

    # D.8/D.9 fires because Landowner != Grower
    assert values["D.8"] == "Van Gog Grubbenvorst Vastgoed B.V."
    assert values["D.9"] == "Marion van Gog"

    # G.Grower_* ← kwekerijen
    assert values["G.Grower_email"] == "koen.saris@vangogkwekerijen.nl"
    # G.Landowner_* ← Vastgoed (notices override or partner fallback)
    assert values["G.Landowner_email"] == "marion@vangogvastgoed.nl"

    # No spurious partner-disambiguation warnings for the clean 3-partner
    # shape (enum_normaliser noise is orthogonal and ignored here).
    assert _partner_warnings(warnings) == [], warnings


def test_van_gog_cli_produces_annex_with_multi_partner_values(
    van_gog_deal_path, tmp_path
):
    """End-to-end CLI: Van Gog multi-partner fixture writes annex with
    the kwekerijen / Grubbenvorst B.V. / Vastgoed data in the right cells."""
    out_dir = tmp_path / "out"
    rc = engine.main([str(van_gog_deal_path), "--out-dir", str(out_dir)])
    assert rc == 0
    annex_paths = list(out_dir.glob("*_annex-a.docx"))
    assert len(annex_paths) == 1
    flat = _annex_flat_text(annex_paths[0])
    assert "Van Gog kwekerijen Grubbenvorst B.V." in flat  # A.1
    assert "Enexis" in flat                                 # B.1
    assert "Horst aan de Maas, Sectie G, Nr 8812" in flat   # D.1
    assert "Van Gog Grubbenvorst Vastgoed B.V." in flat     # D.8
    assert "koen.saris@vangogkwekerijen.nl" in flat         # G.Grower_email


# ---------------------------------------------------------------------------
# 2. Single-partner regression (v0.1 single-grower deals keep working)
# ---------------------------------------------------------------------------


def test_single_grower_as_all_roles_still_works(moerman_deal):
    """Moerman is a single partner wearing all three hats (heat offtaker,
    grid contributor, landowner). The v0.2 mapper must still resolve A/B/D
    from the same partner and NOT fire D.8/D.9 (landowner == grower)."""
    warnings: list[str] = []
    values = engine.build_field_values(moerman_deal, warnings=warnings)

    assert values["A.1"] == "Moerman Paprika B.V."
    assert values["B.1"] == "Westland Infra"
    assert values["D.1"] == "Naaldwijk, Sectie B, Nr 4521"
    # Landowner is the same entity as Grower → D.8/D.9 must be absent
    assert "D.8" not in values
    assert "D.9" not in values
    # No partner-selection warnings on a well-formed single-partner deal
    assert _partner_warnings(warnings) == [], warnings


# ---------------------------------------------------------------------------
# 3. Missing grid contributor → B.* flagged as [TBC]
# ---------------------------------------------------------------------------


def test_missing_grid_contributor_flags_B_section_as_tbc(van_gog_deal):
    """Strip the grid_interconnection contribution from the Van Gog
    Grubbenvorst B.V. partner — B.1/B.4 must fall back to "[TBC]" and a
    warning must surface."""
    d = copy.deepcopy(van_gog_deal)
    # Remove the grid contribution from partner 0; BESS stays so the
    # partner keeps the returns shape valid.
    p0 = d["site_partners"][0]
    p0["contributions"] = [
        c for c in p0["contributions"] if c["asset"] != "grid_interconnection"
    ]

    warnings: list[str] = []
    values = engine.build_field_values(d, warnings=warnings)

    assert values.get("B.1") == "[TBC]"
    assert values.get("B.4") == "[TBC]"
    assert any("Section B" in w and "no Grid Contributor" in w for w in warnings), (
        warnings
    )


# ---------------------------------------------------------------------------
# 4. Missing landowner → G.Grower_* used (no distinct G.Landowner)
# ---------------------------------------------------------------------------


def test_missing_landowner_uses_primary_grower_for_G_grower_fields(
    van_gog_deal,
):
    """Strip the Vastgoed (land) partner. D.1 must become "[TBC]",
    G.Landowner_* must NOT be emitted (no distinct landowner), and
    G.Grower_* must continue to resolve from the kwekerijen partner."""
    d = copy.deepcopy(van_gog_deal)
    d["site_partners"] = [
        p for p in d["site_partners"]
        if not any(
            c["asset"] in ("land", "property")
            for c in (p.get("contributions") or [])
        )
    ]
    # Sanity: we have 2 partners left (grid, heat offtaker)
    assert len(d["site_partners"]) == 2

    warnings: list[str] = []
    values = engine.build_field_values(d, warnings=warnings)

    # D.1 sentinel
    assert values.get("D.1") == "[TBC]"
    # G.Grower still resolves from heat offtaker
    assert values["G.Grower_email"] == "koen.saris@vangogkwekerijen.nl"
    # No G.Landowner_* because there is no distinct landowner
    assert "G.Landowner_address" not in values
    assert "G.Landowner_email" not in values
    # No D.8 (no landowner entity at all)
    assert "D.8" not in values
    # Warning surfaces
    assert any("Section D" in w and "no Landowner" in w for w in warnings), warnings


# ---------------------------------------------------------------------------
# 5. Partner ambiguity on Grid Contributor
# ---------------------------------------------------------------------------


def test_partner_ambiguity_warns_on_multiple_grid_contributors(van_gog_deal):
    """Duplicate the grid contribution onto the Vastgoed partner — two
    Grid Contributors exist. The engine must pick the one with the
    larger MVA and warn that it chose among multiple."""
    d = copy.deepcopy(van_gog_deal)
    # Give the Vastgoed (landowner) partner a SMALLER grid connection
    # so the MVA tiebreaker is exercised deterministically.
    d["site_partners"][1]["contributions"].append({
        "asset": "grid_interconnection",
        "instrument": "ato_sharing",
        "details": {
            "dso": "Liander",
            "total_connection_mva": 4.0,
            "sap_configuration": "MLOEA",
        },
        "stage_tag": "hot",
    })

    warnings: list[str] = []
    values = engine.build_field_values(d, warnings=warnings)

    # Larger MVA (16.0) wins → Grubbenvorst B.V., DSO = Enexis
    assert values["B.1"] == "Enexis"
    assert float(values["B.4"]) == 16.0
    # Warning lists both partners
    assert any(
        "Section B" in w and "Grid Contributors" in w for w in warnings
    ), warnings


def test_partner_ambiguity_warns_on_tied_grid_mva(van_gog_deal):
    """When two Grid Contributors are tied on MVA, the engine still
    picks the first (insertion-order stable) and warns."""
    d = copy.deepcopy(van_gog_deal)
    d["site_partners"][1]["contributions"].append({
        "asset": "grid_interconnection",
        "details": {
            "dso": "Liander",
            "total_connection_mva": 16.0,  # same as partner[0]
        },
    })

    warnings: list[str] = []
    values = engine.build_field_values(d, warnings=warnings)

    # Tie → first in insertion order wins
    assert values["B.1"] == "Enexis"
    assert any(
        "Section B" in w and "Grid Contributors" in w for w in warnings
    ), warnings


# ---------------------------------------------------------------------------
# 6. Generated annex opens cleanly for multi-partner
# ---------------------------------------------------------------------------


def test_generated_annex_a_opens_cleanly_for_multi_partner(
    van_gog_deal, tmp_path
):
    """The populated .docx must be readable by python-docx and the
    injected multi-partner values must be present in the table text."""
    warnings: list[str] = []
    values = engine.build_field_values(van_gog_deal, warnings=warnings)
    assert _partner_warnings(warnings) == [], warnings

    dst = tmp_path / "annex_van_gog.docx"
    registry = engine.sdb.load_registry()
    stats = engine.populate_annex_a(
        engine.ANNEX_A_TEMPLATE, dst, values, registry
    )
    # XML form-fill warnings come from layout issues, unrelated to our
    # disambiguation layer — we assert cleanliness of the fill itself.
    assert stats.warnings == [], stats.warnings

    flat = _annex_flat_text(dst)
    # All three partners represented
    assert "Van Gog kwekerijen Grubbenvorst B.V." in flat
    assert "Enexis" in flat
    assert "Van Gog Grubbenvorst Vastgoed B.V." in flat
    assert "871687510000099999" in flat  # EAN from B.2
    assert "Koen Saris" in flat           # A.4


# ---------------------------------------------------------------------------
# 7. _select_partner_for_section — direct unit coverage
# ---------------------------------------------------------------------------


def test_select_partner_routes_each_section_to_right_partner(van_gog_deal):
    """Direct invocation of the helper: each section resolves to the
    partner whose contributions/returns match that role."""
    partners = van_gog_deal["site_partners"]
    warnings: list[str] = []

    a = engine._select_partner_for_section("A", partners, warnings)
    b = engine._select_partner_for_section("B", partners, warnings)
    c = engine._select_partner_for_section("C", partners, warnings)
    d = engine._select_partner_for_section("D", partners, warnings)
    g_grower = engine._select_partner_for_section("G.Grower", partners, warnings)
    g_lo = engine._select_partner_for_section("G.Landowner", partners, warnings)

    assert a["legal_name"] == "Van Gog kwekerijen Grubbenvorst B.V."
    assert b["legal_name"] == "Van Gog Grubbenvorst B.V."
    assert c is a
    assert d["legal_name"] == "Van Gog Grubbenvorst Vastgoed B.V."
    assert g_grower is a
    assert g_lo is d
    assert warnings == [], warnings


def test_select_partner_empty_list_returns_none():
    warnings: list[str] = []
    assert engine._select_partner_for_section("A", [], warnings) is None
    assert engine._select_partner_for_section("B", [], warnings) is None
    assert warnings == []
