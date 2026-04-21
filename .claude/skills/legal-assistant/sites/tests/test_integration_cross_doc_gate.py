"""Integration tests: cross_doc_gate interplay with LOI engine + Van Gog
fixture + override flow."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml

import cross_doc_gate as cdg
import generate_site_loi as engine


@pytest.fixture
def van_gog_deal():
    p = Path(__file__).resolve().parents[1] / "loi" / "examples" / "deal_van-gog.yaml"
    return yaml.safe_load(p.read_text())


def test_van_gog_surfaces_3x_dataacc1_unoverridable(van_gog_deal):
    """Van Gog has 3 partners with entity_id=null → DataAcc-1 × 3, all
    non-overridable regardless of gate_overrides entries."""
    deal = copy.deepcopy(van_gog_deal)
    # Attempt to override — must be ignored for non-overridable rule.
    deal["gate_overrides"] = [
        {"rule": "DataAcc-1", "justification": "ignore me",
         "approver": "SAL", "timestamp": "2026-04-20"}
    ]
    verdicts = cdg.run(deal, stage="hot")
    dataacc1 = [v for v in verdicts if v.rule == "DataAcc-1"]
    assert len(dataacc1) == 3
    for v in dataacc1:
        assert v.severity == "fail"
        assert v.overridable is False


def test_van_gog_esc2_co_investment_warning_fires(van_gog_deal):
    verdicts = cdg.run(van_gog_deal, stage="hot")
    esc2 = [v for v in verdicts if v.rule == "Esc-2"]
    assert esc2 and esc2[0].severity == "warn"


def test_gate_downgrades_overridable_con1_to_warn():
    prior = {
        "deal_yaml_schema_version": "1.0", "slug": "x", "hubspot_deal_id": 1,
        "site_partners": [
            {"returns": [{"value": "energy_heat",
                          "details": {"price_eur_mwh": 20}}]}
        ],
        "locations": [], "documents": [], "enrichment": {},
        "gate_overrides": [],
    }
    curr = copy.deepcopy(prior)
    curr["site_partners"][0]["returns"][0]["details"]["price_eur_mwh"] = 25  # 25% drift
    curr["gate_overrides"] = [
        {"rule": "Con-1", "justification": "updated ATO quote came in higher",
         "approver": "SAL", "timestamp": "2026-04-20"}
    ]
    verdicts = cdg.run(curr, stage="hot", prior_loi_deal=prior)
    con1 = [v for v in verdicts if v.rule == "Con-1"]
    assert con1 and con1[0].severity == "warn"
    assert "overridden" in con1[0].message


def test_gate_loi_stage_skips_hot_only_rules(van_gog_deal):
    verdicts = cdg.run(van_gog_deal, stage="loi")
    # Gap-4 / Gap-5 and most DataAcc are LOI-irrelevant
    assert not any(v.rule == "Gap-4" for v in verdicts)
    assert not any(v.rule == "Gap-5" for v in verdicts)


def test_gate_report_serialises_via_to_dict_list(van_gog_deal):
    """Engine-emitted gate verdicts must round-trip through to_dict_list
    for persistence in cross-doc-gate-report.json."""
    verdicts = cdg.run(van_gog_deal, stage="hot")
    serialised = cdg.to_dict_list(verdicts)
    import json
    # Round-trip through JSON
    js = json.dumps(serialised)
    back = json.loads(js)
    assert len(back) == len(verdicts)
    assert all("rule" in v and "severity" in v for v in back)


def test_gate_summarise_matches_verdict_count(van_gog_deal):
    verdicts = cdg.run(van_gog_deal, stage="hot")
    summary = cdg.summarise(verdicts)
    assert summary["total"] == len(verdicts)
    assert summary["blocking"] == sum(1 for v in verdicts if v.severity == "fail")


def test_loi_engine_emits_gate_verdicts_in_qa_report(tmp_path):
    """End-to-end: LOI engine → QA report includes gate verdicts."""
    p = Path(__file__).resolve().parents[1] / "loi" / "examples" / "deal_van-gog.yaml"
    rc = engine.main([str(p), "--out-dir", str(tmp_path)])
    assert rc == 0
    qa = next(tmp_path.glob("*qa.txt"))
    text = qa.read_text()
    assert "Cross-doc gate verdicts:" in text
    # Should include at least the DataAcc-1 and Esc-2 rules
    assert "DataAcc-1" in text
