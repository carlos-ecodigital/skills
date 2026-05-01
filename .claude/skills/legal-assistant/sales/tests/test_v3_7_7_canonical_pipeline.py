"""v3.7.7 — canonical HubSpot pipeline mapping.

Surfaced by 2026-04-30 audit: v3.7.4 hardcoded `pipeline: "Commercial"`
+ `dealstage: "loi_sent"` in `phase8_actions.hubspot_upsert_company`.
Neither name exists in `_shared/hubspot-pipeline-routing.md` (Jonathan's
canonical 8-pipeline list, merged in PR #83).

Real impact: Phase 8 auto-create produced HubSpot deal payloads that
either reject on the API or silently land in a default catchall pipeline,
defeating the purpose of routing.

Fix: map intake.type → canonical pipeline + use the canonical default
stage from the routing doc.

Type → pipeline mapping per `_shared/hubspot-pipeline-routing.md`:

| intake.type            | Pipeline                                          | Default stage |
|------------------------|---------------------------------------------------|---------------|
| EndUser                | COMPUTE 1/2 - 2026 DC Colo Capacity Sale          | Lead          |
| Wholesale              | COMPUTE 1/2 - 2026 DC Colo Capacity Sale          | Lead          |
| Distributor            | COMPUTE 2/2 - 2026 DC Colo Channel Partners       | Identified    |
| StrategicSupplier      | COMPUTE 2/2 - 2026 DC Colo Channel Partners       | Identified    |
| EcosystemPartnership   | (operator decision; default to P2 Channel)        | Identified    |
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest


SKILL_ROOT = Path(__file__).resolve().parents[2]


CANONICAL_PIPELINES = {
    "COMPUTE 1/2 - 2026 DC Colo Capacity Sale",
    "COMPUTE 2/2 - 2026 DC Colo Channel Partners",
    "INV - 1/4 - Program (Projects)",
    "INV - 2/4 - Equity (Platform)",
    "INV - 4/4 - Investors Intro/Connect",
    "HEAT - 1/3 Greenhouses NL - Closing HoT",
    "Growth - Media/PR Pipeline",
    "Growth - Conference Speaking",
}

EXPECTED_TYPE_MAP = [
    ("EndUser", "COMPUTE 1/2 - 2026 DC Colo Capacity Sale", "Lead"),
    ("Wholesale", "COMPUTE 1/2 - 2026 DC Colo Capacity Sale", "Lead"),
    ("Distributor", "COMPUTE 2/2 - 2026 DC Colo Channel Partners", "Identified"),
    ("StrategicSupplier", "COMPUTE 2/2 - 2026 DC Colo Channel Partners", "Identified"),
    ("EcosystemPartnership", "COMPUTE 2/2 - 2026 DC Colo Channel Partners", "Identified"),
]


def _intake(loi_type: str) -> dict:
    return {
        "type": loi_type,
        "counterparty": {"name": "Acme Corp", "domain": "acme.com"},
        "dates": {"loi_date": "20 April 2026"},
    }


@pytest.mark.parametrize("loi_type,expected_pipeline,expected_stage", EXPECTED_TYPE_MAP)
def test_force_create_emits_canonical_pipeline_per_type(
    loi_type, expected_pipeline, expected_stage
):
    """Each LOI type maps to a specific canonical pipeline + default stage."""
    sys.path.insert(0, str(SKILL_ROOT))
    from scripts import phase8_actions
    payload = phase8_actions.hubspot_upsert_company(
        _intake(loi_type),
        "/tmp/out.docx",
        dedup_decision={
            "force_create": True,
            "reason": f"test fixture: type={loi_type}",
            "search_run_at": "2026-04-30T10:00:00Z",
        },
    )
    deal = payload["dispatch"][1]
    assert deal["properties"]["pipeline"] == expected_pipeline, (
        f"{loi_type}: pipeline mismatch — expected {expected_pipeline!r}, "
        f"got {deal['properties']['pipeline']!r}"
    )
    assert deal["properties"]["dealstage"] == expected_stage, (
        f"{loi_type}: dealstage mismatch — expected {expected_stage!r}, "
        f"got {deal['properties']['dealstage']!r}"
    )


def test_pipeline_is_always_canonical():
    """For every supported LOI type, emitted pipeline is in the canonical
    8-pipeline set per `_shared/hubspot-pipeline-routing.md`. Defends
    against future regressions like the v3.7.4 'Commercial' staleness."""
    sys.path.insert(0, str(SKILL_ROOT))
    from scripts import phase8_actions
    for loi_type, _, _ in EXPECTED_TYPE_MAP:
        payload = phase8_actions.hubspot_upsert_company(
            _intake(loi_type),
            "/tmp/out.docx",
            dedup_decision={
                "force_create": True,
                "reason": "canonicality regression test",
                "search_run_at": "2026-04-30T10:00:00Z",
            },
        )
        pipeline = payload["dispatch"][1]["properties"]["pipeline"]
        assert pipeline in CANONICAL_PIPELINES, (
            f"{loi_type} produced non-canonical pipeline {pipeline!r}; "
            f"must be one of {sorted(CANONICAL_PIPELINES)}"
        )


def test_link_to_existing_does_not_clobber_pipeline():
    """When linking to an existing HubSpot company, the company UPDATE
    payload must NOT include `pipeline` (lifecyclestage clobber risk).
    Pipeline only appears on the deal CREATE payload."""
    sys.path.insert(0, str(SKILL_ROOT))
    from scripts import phase8_actions
    payload = phase8_actions.hubspot_upsert_company(
        _intake("Wholesale"),
        "/tmp/out.docx",
        dedup_decision={
            "link_to_id": "12345678",
            "match_confidence": "high",
            "match_property": "domain_exact",
        },
    )
    company_update, deal_create = payload["dispatch"]
    # Company UPDATE: no pipeline (stays whatever HubSpot has it as)
    assert "pipeline" not in company_update["properties"]
    assert "lifecyclestage" not in company_update["properties"]
    # Deal CREATE: pipeline IS canonical
    assert deal_create["properties"]["pipeline"] in CANONICAL_PIPELINES


def test_canonical_doc_is_present():
    """Sanity — the canonical pipeline routing doc must exist in
    _shared/. If it's missing, the type→pipeline mapping has lost its
    source of truth."""
    doc = SKILL_ROOT.parent / "_shared" / "hubspot-pipeline-routing.md"
    assert doc.exists(), (
        f"Canonical pipeline routing doc not found at {doc}. "
        f"phase8_actions.py depends on it as the source of truth for "
        f"pipeline names."
    )


def test_unknown_type_defaults_safely():
    """If an unrecognized type is supplied, the code must NOT silently
    emit a stale 'Commercial' string. Either map to a sensible default
    (P2 Channel as the most generic) or raise — but never produce a
    non-canonical name."""
    sys.path.insert(0, str(SKILL_ROOT))
    from scripts import phase8_actions
    payload = phase8_actions.hubspot_upsert_company(
        {
            "type": "TotallyUnknownType",
            "counterparty": {"name": "X", "domain": "x.com"},
            "dates": {"loi_date": "20 April 2026"},
        },
        "/tmp/out.docx",
        dedup_decision={
            "force_create": True,
            "reason": "test fixture: unknown type",
            "search_run_at": "2026-04-30T10:00:00Z",
        },
    )
    pipeline = payload["dispatch"][1]["properties"]["pipeline"]
    assert pipeline in CANONICAL_PIPELINES, (
        f"Unknown LOI type produced non-canonical pipeline {pipeline!r}"
    )
