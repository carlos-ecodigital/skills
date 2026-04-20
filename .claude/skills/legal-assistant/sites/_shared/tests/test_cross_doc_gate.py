"""Tests for cross_doc_gate.py — Phase B8."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_SHARED = Path(__file__).resolve().parents[1]
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

import cross_doc_gate as cdg  # noqa: E402


def _minimal_deal(**overrides) -> dict:
    base = {
        "deal_yaml_schema_version": "1.0",
        "slug": "test",
        "hubspot_deal_id": 1,
        "site_partners": [],
        "locations": [],
        "documents": [],
        "enrichment": {},
        "gate_overrides": [],
    }
    base.update(overrides)
    return base


# ---------------------------------------------------------------------------
# GateVerdict
# ---------------------------------------------------------------------------

def test_verdict_to_dict_roundtrip():
    v = cdg.GateVerdict(rule="Con-1", severity="fail", message="x", overridable=True)
    d = v.to_dict()
    assert d["rule"] == "Con-1"
    assert d["severity"] == "fail"
    assert d["overridable"] is True


# ---------------------------------------------------------------------------
# Contradiction rules
# ---------------------------------------------------------------------------

def test_con_1_pricing_drift_flags_fail():
    prior = _minimal_deal(site_partners=[
        {"returns": [{"value": "energy_heat", "details": {"price_eur_mwh": 20}}]}
    ])
    curr = _minimal_deal(site_partners=[
        {"returns": [{"value": "energy_heat", "details": {"price_eur_mwh": 25}}]}
    ])  # 25% drift
    verdicts = cdg.run(curr, stage="hot", prior_loi_deal=prior)
    assert any(v.rule == "Con-1" and v.severity == "fail" for v in verdicts)


def test_con_1_pricing_within_10_percent_clean():
    prior = _minimal_deal(site_partners=[
        {"returns": [{"value": "energy_heat", "details": {"price_eur_mwh": 20}}]}
    ])
    curr = _minimal_deal(site_partners=[
        {"returns": [{"value": "energy_heat", "details": {"price_eur_mwh": 21}}]}
    ])  # 5% drift
    verdicts = cdg.run(curr, stage="hot", prior_loi_deal=prior)
    assert not any(v.rule == "Con-1" for v in verdicts)


def test_con_3_site_location_differs_hard_fail():
    prior = _minimal_deal(locations=[{"parcel_id": "GRU A 1"}])
    curr = _minimal_deal(locations=[{"parcel_id": "GRU B 2"}])
    verdicts = cdg.run(curr, stage="hot", prior_loi_deal=prior)
    hits = [v for v in verdicts if v.rule == "Con-3"]
    assert hits and hits[0].severity == "fail"
    assert hits[0].overridable is False  # non-overridable


def test_con_3_overlap_clean():
    prior = _minimal_deal(locations=[{"parcel_id": "GRU A 1"}])
    curr = _minimal_deal(locations=[{"parcel_id": "GRU A 1"}])
    verdicts = cdg.run(curr, stage="hot", prior_loi_deal=prior)
    assert not any(v.rule == "Con-3" for v in verdicts)


def test_con_4_kvk_mismatch_flags_non_overridable():
    prior = _minimal_deal(site_partners=[
        {"legal_name": "X B.V.", "kvk": "11111111"}
    ])
    curr = _minimal_deal(site_partners=[
        {"legal_name": "X B.V.", "kvk": "22222222"}
    ])
    verdicts = cdg.run(curr, stage="hot", prior_loi_deal=prior)
    hits = [v for v in verdicts if v.rule == "Con-4"]
    assert hits and hits[0].severity == "fail"
    assert hits[0].overridable is False


# ---------------------------------------------------------------------------
# Contribution consistency
# ---------------------------------------------------------------------------

def test_contrib_2_partner_missing_in_current():
    prior = _minimal_deal(site_partners=[
        {"legal_name": "A B.V."},
        {"legal_name": "B B.V."},
    ])
    curr = _minimal_deal(site_partners=[{"legal_name": "A B.V."}])
    verdicts = cdg.run(curr, stage="hot", prior_loi_deal=prior)
    hits = [v for v in verdicts if v.rule == "Contrib-2"]
    assert any("B B.V." in h.message for h in hits)


def test_contrib_1_assets_differ_overridable_fail():
    prior = _minimal_deal(site_partners=[
        {"legal_name": "X", "contributions": [{"asset": "land"}]}
    ])
    curr = _minimal_deal(site_partners=[
        {"legal_name": "X", "contributions": [{"asset": "land"},
                                              {"asset": "grid_interconnection"}]}
    ])
    verdicts = cdg.run(curr, stage="hot", prior_loi_deal=prior)
    hits = [v for v in verdicts if v.rule == "Contrib-1"]
    assert hits and hits[0].severity == "fail"
    assert hits[0].overridable is True


# ---------------------------------------------------------------------------
# Gap rules
# ---------------------------------------------------------------------------

def test_gap_2_missing_legal_name_in_hot_stage():
    curr = _minimal_deal(site_partners=[{"legal_name": None}])
    verdicts = cdg.run(curr, stage="hot")
    assert any(v.rule == "Gap-2" for v in verdicts)


def test_gap_1_missing_kvk_in_hot_stage_non_overridable():
    curr = _minimal_deal(site_partners=[
        {"legal_name": "X", "kvk": None}
    ])
    verdicts = cdg.run(curr, stage="hot")
    hits = [v for v in verdicts if v.rule == "Gap-1"]
    assert hits and hits[0].overridable is False


def test_loi_stage_does_not_run_gap_1_2():
    curr = _minimal_deal(site_partners=[
        {"legal_name": None, "kvk": None}
    ])
    verdicts = cdg.run(curr, stage="loi")
    assert not any(v.rule in ("Gap-1", "Gap-2") for v in verdicts)


# ---------------------------------------------------------------------------
# Gap-4 (doc collection) + Gap-5 (validity)
# ---------------------------------------------------------------------------

def test_gap_4_landowner_missing_kadaster():
    curr = _minimal_deal(site_partners=[
        {"legal_name": "X", "kvk": "12345678",
         "contributions": [{"asset": "land"}]}
    ])
    verdicts = cdg.run(curr, stage="hot")
    # Kadaster + bestemmingsplan are required for land contributor
    hits = [v for v in verdicts if v.rule == "Gap-4"]
    assert any("kadaster_uittreksel" in v.message for v in hits)


def test_gap_4_not_run_in_loi_stage():
    curr = _minimal_deal(site_partners=[
        {"legal_name": "X", "contributions": [{"asset": "land"}]}
    ])
    verdicts = cdg.run(curr, stage="loi")
    assert not any(v.rule == "Gap-4" for v in verdicts)


def test_gap_5_stale_kvk_doc():
    # 60 days ago → past KVK 30-day validity
    curr = _minimal_deal(
        site_partners=[{"legal_name": "X", "kvk": "12345678", "entity_id": 1}],
        documents=[{"type": "kvk_uittreksel", "uploaded_at": "2026-01-01",
                    "partner_entity_idx": 0}],
    )
    verdicts = cdg.run(curr, stage="hot")
    assert any(v.rule == "Gap-5" for v in verdicts)


# ---------------------------------------------------------------------------
# Data accuracy
# ---------------------------------------------------------------------------

def test_dataacc_1_null_entity_id_fires():
    curr = _minimal_deal(site_partners=[
        {"legal_name": "X", "entity_id": None}
    ])
    verdicts = cdg.run(curr, stage="hot")
    hits = [v for v in verdicts if v.rule == "DataAcc-1"]
    assert hits and hits[0].overridable is False


def test_dataacc_2_pdok_false_fires():
    curr = _minimal_deal(enrichment={"pdok_parcel_confirmed": False})
    verdicts = cdg.run(curr, stage="hot")
    hits = [v for v in verdicts if v.rule == "DataAcc-2"]
    assert hits and hits[0].severity == "fail" and hits[0].overridable is False


def test_dataacc_3_dso_mismatch_warns():
    curr = _minimal_deal(enrichment={"dso_matches_postcode": False})
    verdicts = cdg.run(curr, stage="hot")
    hits = [v for v in verdicts if v.rule == "DataAcc-3"]
    assert hits and hits[0].severity == "warn"


# ---------------------------------------------------------------------------
# Registry escalation rules
# ---------------------------------------------------------------------------

def test_esc_1_non_standard_heat_split_triggers():
    curr = _minimal_deal(commercial={"heat_sales_split_pct": "70 : 30 %"})
    verdicts = cdg.run(curr, stage="hot")
    assert any(v.rule == "Esc-1" for v in verdicts)


def test_esc_1_default_50_50_does_not_trigger():
    curr = _minimal_deal(commercial={"heat_sales_split_pct": "50 : 50 %"})
    verdicts = cdg.run(curr, stage="hot")
    assert not any(v.rule == "Esc-1" for v in verdicts)


def test_esc_4_joint_signing_warns():
    curr = _minimal_deal(site_partners=[
        {"legal_name": "X", "entity_id": 1, "kvk": "12345678",
         "signatory": {"signing_authority": "joint"}}
    ])
    verdicts = cdg.run(curr, stage="hot")
    assert any(v.rule == "Esc-4" and v.severity == "warn" for v in verdicts)


# ---------------------------------------------------------------------------
# Override application
# ---------------------------------------------------------------------------

def test_override_downgrades_fail_to_warn_when_overridable():
    prior = _minimal_deal(site_partners=[
        {"returns": [{"value": "energy_heat", "details": {"price_eur_mwh": 20}}]}
    ])
    curr = _minimal_deal(
        site_partners=[
            {"returns": [{"value": "energy_heat", "details": {"price_eur_mwh": 25}}]}
        ],
        gate_overrides=[{"rule": "Con-1", "justification": "Ok", "approver": "SAL",
                         "timestamp": "2026-04-20"}],
    )
    verdicts = cdg.run(curr, stage="hot", prior_loi_deal=prior)
    con1 = [v for v in verdicts if v.rule == "Con-1"]
    assert con1 and con1[0].severity == "warn"
    assert "overridden" in con1[0].message


def test_override_does_not_downgrade_non_overridable_rule():
    curr = _minimal_deal(
        site_partners=[{"legal_name": "X", "entity_id": None}],
        gate_overrides=[{"rule": "DataAcc-1", "justification": "whatever",
                         "approver": "SAL", "timestamp": "2026-04-20"}],
    )
    verdicts = cdg.run(curr, stage="hot")
    hits = [v for v in verdicts if v.rule == "DataAcc-1"]
    assert hits and hits[0].severity == "fail"


# ---------------------------------------------------------------------------
# Summarise / serialise
# ---------------------------------------------------------------------------

def test_summarise_counts_severities():
    verdicts = [
        cdg.GateVerdict(rule="A", severity="fail", message=""),
        cdg.GateVerdict(rule="B", severity="fail", message=""),
        cdg.GateVerdict(rule="C", severity="warn", message=""),
    ]
    s = cdg.summarise(verdicts)
    assert s["total"] == 3
    assert s["by_severity"]["fail"] == 2
    assert s["by_severity"]["warn"] == 1
    assert s["blocking"] == 2


def test_to_dict_list_returns_serialisable_list():
    verdicts = [cdg.GateVerdict(rule="X", severity="fail", message="m")]
    out = cdg.to_dict_list(verdicts)
    import json
    json.dumps(out)  # must be JSON-serialisable


# ---------------------------------------------------------------------------
# Van Gog anchor: expected-gap fixture surfaces through gate cleanly
# ---------------------------------------------------------------------------

def test_van_gog_fixture_surfaces_dataacc_1_for_all_3_partners():
    """deal_van-gog.yaml has 3 partners with entity_id=null. Expected."""
    import yaml
    p = Path(__file__).resolve().parents[3] / "sites" / "loi" / "examples" / "deal_van-gog.yaml"
    deal = yaml.safe_load(p.read_text())
    verdicts = cdg.run(deal, stage="hot")
    dataacc_1 = [v for v in verdicts if v.rule == "DataAcc-1"]
    assert len(dataacc_1) == 3  # one per Site Partner
