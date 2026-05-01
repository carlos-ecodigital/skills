"""v3.7.4 — HubSpot duplicate-check before company create.

Production concern (raised 2026-04-30): the current
`hubspot_upsert_company` builds an `operation: "upsert"` payload that
relies on HubSpot's domain-based dedup. Failure modes:
1. Counterparty domain missing/empty in intake → upsert creates new
   company even when one exists under a different name.
2. Counterparty domain typo → same as #1.
3. Parent + subsidiary share a domain → upsert clobbers one of them.
4. Multiple sales reps reach out to same prospect; each LOI session
   creates a fresh "duplicate" company.

Fix: search-first flow.
- `hubspot_search_company(intake)` returns a search payload (domain +
  name fuzzy).
- The orchestrator runs the search, gets candidates back, surfaces
  matches to the operator, and only THEN calls
  `hubspot_upsert_company(intake, ..., dedup_decision={"link_to": id} OR {"force_create": True, "reason": "..."})`.
- Bare `hubspot_upsert_company(intake, output_path)` without a
  `dedup_decision` returns a SEARCH payload (not an upsert), forcing
  the orchestrator to run the dedup check.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest


SKILL_ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture
def intake_with_domain():
    return {
        "type": "Wholesale",
        "counterparty": {
            "name": "Acme Corp",
            "domain": "acme.com",
            "description": "AI cloud services",
        },
        "dates": {"loi_date": "20 April 2026"},
    }


@pytest.fixture
def intake_no_domain():
    """Intake without domain — common when only LinkedIn / brochure
    sources are available. Failure mode #1 from the docstring."""
    return {
        "type": "Strategic Supplier",
        "counterparty": {
            "name": "Foo Industries B.V.",
            "description": "Legacy industrial supplier",
        },
        "dates": {"loi_date": "20 April 2026"},
    }


# ---------------------------------------------------------------------------
# Search-first flow
# ---------------------------------------------------------------------------


def test_search_payload_built_first(intake_with_domain):
    """Calling `hubspot_search_company` must produce a search payload
    targeting `search_crm_objects` (read-only), NOT `manage_crm_objects`.
    """
    sys.path.insert(0, str(SKILL_ROOT))
    from scripts import phase8_actions
    payload = phase8_actions.hubspot_search_company(intake_with_domain)
    assert payload["action"] == "hubspot_search_company"
    assert payload["tool"] == "search_crm_objects"
    # The search must include domain AND name as parallel queries
    queries = payload["dispatch"]
    assert isinstance(queries, list)
    assert any("domain" in q.get("filters", {}).get("propertyName", "") for q in queries), (
        "Search must query by domain"
    )
    assert any("name" in q.get("filters", {}).get("propertyName", "") for q in queries), (
        "Search must query by name (fuzzy fallback)"
    )


def test_search_payload_handles_missing_domain(intake_no_domain):
    """When domain is absent the search still runs — name-only — and the
    payload signals downstream that the operator MUST review candidates
    even if the search returns zero matches (because no-match could be
    a typo, not a true new company)."""
    sys.path.insert(0, str(SKILL_ROOT))
    from scripts import phase8_actions
    payload = phase8_actions.hubspot_search_company(intake_no_domain)
    assert payload["action"] == "hubspot_search_company"
    queries = payload["dispatch"]
    # No domain query when domain is empty
    assert all("domain" not in q.get("filters", {}).get("propertyName", "")
               for q in queries)
    # Name query still present
    assert any("name" in q.get("filters", {}).get("propertyName", "") for q in queries)
    # Operator-review-required flag explicit
    assert payload.get("requires_operator_review") is True


# ---------------------------------------------------------------------------
# Upsert refuses to fire without a dedup_decision
# ---------------------------------------------------------------------------


def test_upsert_without_dedup_decision_returns_search_payload(intake_with_domain):
    """Bare `hubspot_upsert_company(intake, output_path)` without a
    `dedup_decision` argument must return a SEARCH payload (forcing the
    orchestrator to run dedup first), NOT an upsert payload.

    This is the safety guarantee — silent duplicates are impossible
    because the upsert can't run without explicit operator decision."""
    sys.path.insert(0, str(SKILL_ROOT))
    from scripts import phase8_actions
    payload = phase8_actions.hubspot_upsert_company(intake_with_domain, "/tmp/out.docx")
    assert payload["action"] == "hubspot_search_company", (
        "hubspot_upsert_company without dedup_decision must return a "
        "search payload, not an upsert"
    )
    assert payload["tool"] == "search_crm_objects"


def test_upsert_with_force_create_after_search(intake_with_domain):
    """After running the search and finding NO matches (or matches the
    operator rejected as separate entities), `force_create` proceeds
    with create-only — and records the reason for audit."""
    sys.path.insert(0, str(SKILL_ROOT))
    from scripts import phase8_actions
    payload = phase8_actions.hubspot_upsert_company(
        intake_with_domain,
        "/tmp/out.docx",
        dedup_decision={
            "force_create": True,
            "reason": "Operator confirmed: no matches in search; new entity.",
            "search_run_at": "2026-04-30T10:00:00Z",
        },
    )
    assert payload["action"] == "hubspot_upsert_company"
    assert payload["tool"] == "manage_crm_objects"
    # Operation must be CREATE (not upsert) because dedup ran already
    assert all(
        d["operation"] == "create" for d in payload["dispatch"]
    ), "Post-dedup operation must be 'create', not 'upsert'"
    # Dedup audit trail captured in payload
    assert "dedup_audit" in payload
    assert payload["dedup_audit"]["force_create"] is True
    assert "reason" in payload["dedup_audit"]
    assert payload["dedup_audit"]["search_run_at"]


def test_upsert_with_link_to_existing(intake_with_domain):
    """When the orchestrator finds a match and the operator confirms
    it's the same entity, link_to_id triggers an UPDATE on the existing
    record + association (not a create)."""
    sys.path.insert(0, str(SKILL_ROOT))
    from scripts import phase8_actions
    payload = phase8_actions.hubspot_upsert_company(
        intake_with_domain,
        "/tmp/out.docx",
        dedup_decision={
            "link_to_id": "12345678",
            "match_confidence": "high",
            "match_property": "domain_exact",
        },
    )
    assert payload["action"] == "hubspot_link_company"
    assert payload["tool"] == "manage_crm_objects"
    # Operation must be UPDATE on the linked id
    assert payload["dispatch"][0]["operation"] == "update"
    assert payload["dispatch"][0]["objectId"] == "12345678"
    # Deal payload should associate with the linked company id, not by domain
    deal = payload["dispatch"][1]
    assert deal["associations"][0]["match_by"] == "id"
    assert deal["associations"][0]["value"] == "12345678"


def test_upsert_invalid_dedup_decision_raises(intake_with_domain):
    """A malformed dedup_decision (neither force_create nor link_to_id)
    must raise — operator gets a clear error rather than a silent
    fallback to create-by-domain."""
    sys.path.insert(0, str(SKILL_ROOT))
    from scripts import phase8_actions
    with pytest.raises(ValueError, match="dedup_decision"):
        phase8_actions.hubspot_upsert_company(
            intake_with_domain,
            "/tmp/out.docx",
            dedup_decision={"random_key": True},
        )


# ---------------------------------------------------------------------------
# run_phase_8_actions integration
# ---------------------------------------------------------------------------


def test_run_phase_8_includes_search_for_hubspot(intake_with_domain):
    """When `hubspot_upsert_company` is in the action list and no
    dedup_decision is provided, run_phase_8_actions must return a
    payload signalling a search-first step is required, and must NOT
    produce an upsert payload by itself."""
    sys.path.insert(0, str(SKILL_ROOT))
    from scripts import phase8_actions
    result = phase8_actions.run_phase_8_actions(
        intake_with_domain,
        "/tmp/out.docx",
        actions=["hubspot_upsert_company"],
    )
    assert result["dry_run"] is True
    hubspot_action = next(
        a for a in result["actions"]
        if a.get("action") in ("hubspot_search_company", "hubspot_upsert_company")
    )
    # Must be the search step, not the upsert
    assert hubspot_action["action"] == "hubspot_search_company"
