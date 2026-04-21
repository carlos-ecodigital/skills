"""Tests for site_doc_base.py — Phase B6."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_SHARED = Path(__file__).resolve().parents[1]
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

import site_doc_base as sdb  # noqa: E402


# ---------------------------------------------------------------------------
# Registry loading
# ---------------------------------------------------------------------------

def test_load_registry_succeeds():
    reg = sdb.load_registry()
    assert reg["version"] == "1.1"
    assert reg["total_fields"] == 58
    assert "sections" in reg
    assert "supporting_documents" in reg


def test_load_registry_rejects_missing_keys(tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text('{"version": "0.1"}')
    with pytest.raises(ValueError, match="missing required"):
        sdb.load_registry(bad)


def test_iter_fields_yields_58():
    reg = sdb.load_registry()
    count = sum(1 for _ in sdb.iter_fields(reg))
    assert count == 58


# ---------------------------------------------------------------------------
# Stage filtering
# ---------------------------------------------------------------------------

def test_fields_by_stage_loi_includes_both():
    reg = sdb.load_registry()
    loi_fields = sdb.fields_by_stage(reg, "loi")
    # Stage 'both' counts as LOI too. Registry has 15 'both' + 1 'loi' = 16.
    assert len(loi_fields) == 16


def test_fields_by_stage_hot_includes_both():
    reg = sdb.load_registry()
    hot_fields = sdb.fields_by_stage(reg, "hot")
    # 15 'both' + 42 'hot' = 57
    assert len(hot_fields) == 57


def test_fields_by_stage_rejects_invalid_stage():
    reg = sdb.load_registry()
    with pytest.raises(ValueError):
        sdb.fields_by_stage(reg, "msa")


# ---------------------------------------------------------------------------
# Asset filtering
# ---------------------------------------------------------------------------

def test_fields_by_asset_land_returns_14():
    reg = sdb.load_registry()
    # 14 land fields per registry post-B3
    assert len(sdb.fields_by_asset(reg, "land")) == 14


def test_fields_by_asset_identity_includes_A1():
    reg = sdb.load_registry()
    ids = [fid for _, fid, _ in sdb.fields_by_asset(reg, "identity")]
    assert "A1_legal_name" in ids


# ---------------------------------------------------------------------------
# Required field IDs
# ---------------------------------------------------------------------------

def test_required_field_ids_total():
    reg = sdb.load_registry()
    # Registry: required_fields = 44
    assert len(sdb.required_field_ids(reg)) == 44


def test_required_field_ids_filtered_by_loi_stage():
    reg = sdb.load_registry()
    loi_required = sdb.required_field_ids(reg, stage="loi")
    # At minimum all 'both'-tagged required fields appear; exact count
    # depends on required flags on 'both' + 'loi' rows.
    assert len(loi_required) >= 1
    assert len(loi_required) < len(sdb.required_field_ids(reg, stage="hot"))


# ---------------------------------------------------------------------------
# Role-label derivation
# ---------------------------------------------------------------------------

def test_derive_role_labels_grid_contributor():
    sp = {"contributions": [{"asset": "grid_interconnection"}], "returns": []}
    en, nl = sdb.derive_role_labels(sp)
    assert en == ["Grid Contributor"]
    assert nl == ["Netbijdrager"]


def test_derive_role_labels_landowner():
    sp = {"contributions": [{"asset": "land"}], "returns": []}
    en, nl = sdb.derive_role_labels(sp)
    assert en == ["Landowner"]
    assert nl == ["Grondeigenaar"]


def test_derive_role_labels_heat_offtaker():
    sp = {"contributions": [], "returns": [{"value": "energy_heat"}]}
    en, nl = sdb.derive_role_labels(sp)
    assert en == ["Heat Offtaker"]
    assert nl == ["Warmteafnemer"]


def test_derive_role_labels_van_gog_grid_partner_with_bess():
    """Van Gog Grubbenvorst B.V. contributes grid + BESS, receives equity."""
    sp = {
        "contributions": [
            {"asset": "grid_interconnection"},
            {"asset": "equipment_bess"},
        ],
        "returns": [{"value": "equity"}],
    }
    en, nl = sdb.derive_role_labels(sp)
    assert en == ["Grid Contributor", "Equipment Contributor", "Equity Partner"]
    assert nl == ["Netbijdrager", "Apparatuurbijdrager", "Aandelenpartner"]


def test_derive_role_labels_dedupes_identical_labels():
    # land + property both map to Landowner — must dedupe
    sp = {
        "contributions": [
            {"asset": "land"},
            {"asset": "property"},
        ],
        "returns": [],
    }
    en, nl = sdb.derive_role_labels(sp)
    assert en == ["Landowner"]
    assert nl == ["Grondeigenaar"]


def test_derive_role_labels_empty_partner():
    assert sdb.derive_role_labels({}) == ([], [])


# ---------------------------------------------------------------------------
# Addon flag derivation
# ---------------------------------------------------------------------------

def test_derive_addon_flags_bess_detected():
    deal = {"site_partners": [
        {"contributions": [{"asset": "equipment_bess"}]}
    ]}
    flags = sdb.derive_addon_flags(deal)
    assert flags["bess_co_development"] is True


def test_derive_addon_flags_btm_solar_pv_detected():
    deal = {"site_partners": [
        {"contributions": [{"asset": "equipment_solar_pv"}]}
    ]}
    flags = sdb.derive_addon_flags(deal)
    assert flags["btm_renewables"] is True


def test_derive_addon_flags_explicit_override_wins():
    deal = {
        "site_partners": [],
        "addons": {"bess_co_development": True},  # explicitly set
    }
    flags = sdb.derive_addon_flags(deal)
    assert flags["bess_co_development"] is True


# ---------------------------------------------------------------------------
# Partner-subset logic
# ---------------------------------------------------------------------------

def test_docs_required_for_grid_contributor_includes_ato():
    reg = sdb.load_registry()
    sp = {"contributions": [{"asset": "grid_interconnection"}]}
    required = sdb.docs_required_for_partner(reg, sp)
    assert "ato_document" in required
    assert "kvk_uittreksel" in required  # identity doc for every partner
    # Kadaster NOT required for a pure Grid Contributor
    assert "kadaster_uittreksel" not in required


def test_docs_required_for_pure_landowner_includes_kadaster():
    reg = sdb.load_registry()
    sp = {"contributions": [{"asset": "land"}]}
    required = sdb.docs_required_for_partner(reg, sp)
    assert "kadaster_uittreksel" in required
    assert "bestemmingsplan_excerpt" in required
    assert "ato_document" not in required


def test_docs_required_for_pure_heat_offtaker_only_identity():
    reg = sdb.load_registry()
    sp = {"contributions": [], "returns": [{"value": "energy_heat"}]}
    required = sdb.docs_required_for_partner(reg, sp)
    # Pure Heat Offtaker contributes nothing → only identity doc required
    assert required == ["kvk_uittreksel"]


def test_docs_required_for_bess_contributor():
    reg = sdb.load_registry()
    sp = {"contributions": [
        {"asset": "grid_interconnection"},
        {"asset": "equipment_bess"},
    ]}
    required = sdb.docs_required_for_partner(reg, sp)
    # ATO for grid + KVK identity. BESS grid-sharing agreement is
    # required=False so not in list.
    assert "ato_document" in required
    assert "kvk_uittreksel" in required


# ---------------------------------------------------------------------------
# Document validity windows
# ---------------------------------------------------------------------------

def test_doc_is_stale_kvk_past_30_days():
    reg = sdb.load_registry()
    entry = {"type": "kvk_uittreksel", "uploaded_at": "2026-01-01"}
    assert sdb.doc_is_stale(reg, entry, as_of_iso_date="2026-04-20") is True


def test_doc_is_stale_kvk_within_30_days():
    reg = sdb.load_registry()
    entry = {"type": "kvk_uittreksel", "uploaded_at": "2026-04-15"}
    assert sdb.doc_is_stale(reg, entry, as_of_iso_date="2026-04-20") is False


def test_doc_is_stale_null_validity_never_stale():
    reg = sdb.load_registry()
    entry = {"type": "site_plan", "uploaded_at": "2020-01-01"}
    # validity_days=null → no expiry
    assert sdb.doc_is_stale(reg, entry, as_of_iso_date="2026-04-20") is False


def test_doc_is_stale_missing_upload_date_returns_false():
    reg = sdb.load_registry()
    entry = {"type": "kvk_uittreksel"}
    assert sdb.doc_is_stale(reg, entry) is False


# ---------------------------------------------------------------------------
# SiteDocBase integration
# ---------------------------------------------------------------------------

def test_sitedocbase_decorates_deal_with_role_labels():
    deal = {
        "site_partners": [
            {
                "legal_name": "X",
                "contributions": [{"asset": "land"}],
                "returns": [],
            }
        ]
    }
    base = _ConcreteSite()
    base.decorate_deal(deal)
    sp = deal["site_partners"][0]
    assert sp["_role_labels_en"] == ["Landowner"]
    assert sp["_role_labels_nl"] == ["Grondeigenaar"]


def test_sitedocbase_decorates_deal_with_addon_flags():
    deal = {"site_partners": [
        {"contributions": [{"asset": "equipment_bess"}]}
    ]}
    base = _ConcreteSite()
    base.decorate_deal(deal)
    assert deal["_addons_effective"]["bess_co_development"] is True


def test_sitedocbase_stage_fields_for_loi():
    base = _ConcreteSite()
    base.stage = "loi"
    fields = base.stage_fields()
    assert len(fields) == 16  # 15 'both' + 1 'loi'


def test_sitedocbase_hydrate_from_hubspot_passthrough():
    base = _ConcreteSite()
    deal = {"x": 1}
    assert base.hydrate_from_hubspot(deal) is deal


def test_sitedocbase_run_cross_doc_gate_empty():
    base = _ConcreteSite()
    assert base.run_cross_doc_gate({}) == []


def test_sitedocbase_load_deal_rejects_wrong_schema(tmp_path):
    p = tmp_path / "d.yaml"
    p.write_text('deal_yaml_schema_version: "0.9"\n')
    with pytest.raises(ValueError, match="schema version"):
        sdb.SiteDocBase.load_deal(p)


def test_walk_for_tbc_finds_nulls_and_tbc_literal():
    deal = {
        "a": None,
        "b": {"c": "[TBC]", "d": "value"},
        "e": [1, None, "[TBC]"],
        "_internal": None,  # should be skipped
    }
    paths = sdb._walk_for_tbc(deal)
    assert "a" in paths
    assert "b.c" in paths
    assert "e[1]" in paths
    assert "e[2]" in paths
    assert "_internal" not in paths  # skipped
    assert "b.d" not in paths  # has a value


class _ConcreteSite(sdb.SiteDocBase):
    """Minimal concrete subclass for testing the abstract base."""
    stage = "loi"
    def render_document(self, deal):
        return None
