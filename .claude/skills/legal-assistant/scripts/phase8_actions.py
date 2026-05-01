"""Phase 8 auto-action executor.

v3.7.0 scope — wires the SKILL.md Phase 8 action menu to actual tool calls
when the operator opts in via `--phase-8-auto-execute`.

Dispatch stubs here produce a structured payload describing the intended
action. Real MCP invocations happen in the orchestrator session (not here),
because MCP tool schemas are session-scoped and must be called from the
same runtime that loaded them. This module keeps the payload shape testable
and deterministic.

Default: `dry_run=True`. The caller must explicitly pass `dry_run=False`
(driven by the `--phase-8-auto-execute` CLI flag) to produce a real-write
payload.

v3.7.4 — HubSpot duplicate-check before company create. Calling
`hubspot_upsert_company` without a `dedup_decision` returns a SEARCH
payload, forcing the orchestrator to run dedup-check first and surface
candidates to the operator. Only after the operator passes back a
`dedup_decision` (link_to_id OR force_create with reason) does the
function emit the actual create/update payload. Eliminates the silent-
duplicate failure modes documented in `test_v3_7_4_hubspot_dedup.py`.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any


# Actions the operator can pick at Phase 8. Keep in sync with SKILL.md.
ACTION_KEYS = {
    "hubspot_upsert_company",
    "clickup_create_task",
    "artifact_storage_push",
    "domain_card_create",
    "cover_email_cross_check",
}


def _extract_domain(cp: dict) -> str:
    """Pull domain from `counterparty.domain` or fallback to `website`."""
    domain = cp.get("domain") or ""
    if not domain:
        website = cp.get("website") or ""
        domain = (
            website.replace("https://", "").replace("http://", "").rstrip("/")
        )
    return domain


# v3.7.7 — canonical HubSpot pipeline mapping per
# `_shared/hubspot-pipeline-routing.md` (Jonathan, PR #83 / #36).
#
# Source of truth: the routing doc. Update both this map AND the doc when
# pipeline names change. The canonicality test in
# `tests/test_v3_7_7_canonical_pipeline.py` blocks regressions where a
# stale name (e.g. v3.7.4's "Commercial") slips into the deal payload.
_LOI_TYPE_TO_PIPELINE: dict[str, tuple[str, str]] = {
    # type: (pipeline name, default stage on intake)
    "EndUser":               ("COMPUTE 1/2 - 2026 DC Colo Capacity Sale", "Lead"),
    "Wholesale":             ("COMPUTE 1/2 - 2026 DC Colo Capacity Sale", "Lead"),
    "Distributor":           ("COMPUTE 2/2 - 2026 DC Colo Channel Partners", "Identified"),
    "StrategicSupplier":     ("COMPUTE 2/2 - 2026 DC Colo Channel Partners", "Identified"),
    "EcosystemPartnership":  ("COMPUTE 2/2 - 2026 DC Colo Channel Partners", "Identified"),
}

# Safe default for unknown types — never silently emit a non-canonical
# name. P2 Channel is the most generic LOI-applicable pipeline.
_LOI_DEFAULT_PIPELINE = ("COMPUTE 2/2 - 2026 DC Colo Channel Partners", "Identified")


def _resolve_pipeline(loi_type: str) -> tuple[str, str]:
    """Map LOI type → (pipeline name, default stage)."""
    return _LOI_TYPE_TO_PIPELINE.get(loi_type, _LOI_DEFAULT_PIPELINE)


def hubspot_search_company(intake: dict) -> dict:
    """v3.7.4 — return a SEARCH payload for the orchestrator to run BEFORE
    creating a HubSpot company. Searches by domain (exact, when present)
    AND by name (fuzzy fallback for missing/typo'd domains).

    The orchestrator runs each query against `search_crm_objects`
    (read-only), aggregates candidates, and surfaces them to the
    operator. The operator decides — link to existing or force-create —
    and passes the decision back via `hubspot_upsert_company(...,
    dedup_decision=...)`.
    """
    cp = intake.get("counterparty", {})
    name = cp.get("name", "")
    domain = _extract_domain(cp)

    queries: list[dict] = []
    if domain:
        queries.append({
            "objectType": "companies",
            "filters": {"propertyName": "domain", "operator": "EQ", "value": domain},
            "properties": ["name", "domain", "lifecyclestage", "createdate"],
            "limit": 5,
        })
    if name:
        queries.append({
            "objectType": "companies",
            "filters": {"propertyName": "name", "operator": "CONTAINS_TOKEN",
                        "value": name},
            "properties": ["name", "domain", "lifecyclestage", "createdate"],
            "limit": 10,
        })

    return {
        "action": "hubspot_search_company",
        "tool": "search_crm_objects",
        "dispatch": queries,
        # When domain is missing, search may legitimately return zero
        # rows even when a duplicate exists under a misspelled name.
        # Force operator review either way.
        "requires_operator_review": True,
        "review_prompt": (
            f"HubSpot dedup-check for {name!r}: review the search "
            f"results. If a match is found, call hubspot_upsert_company "
            f"with dedup_decision={{'link_to_id': '<hubspot_id>', "
            f"'match_confidence': 'high|medium|low', 'match_property': "
            f"'<domain_exact|name_fuzzy|...>'}}. If no match (truly new "
            f"entity), call with dedup_decision={{'force_create': True, "
            f"'reason': '<≥15 chars>', 'search_run_at': '<ISO8601>'}}."
        ),
        "intake_signature": {
            "name": name,
            "domain": domain,
            "type": intake.get("type"),
        },
    }


def hubspot_upsert_company(
    intake: dict, output_path: str, dedup_decision: dict | None = None
) -> dict:
    """Build the payload to create/update a HubSpot company + deal.

    v3.7.4 — duplicate-check enforced. Without `dedup_decision`, returns
    a SEARCH payload (search-first); the orchestrator runs the search,
    surfaces candidates, and re-calls with a decision. With a decision
    the function emits either:
      - `dedup_decision={'link_to_id': '<id>', ...}` → UPDATE on the
        existing record + association by id (no duplicate created).
      - `dedup_decision={'force_create': True, 'reason': '...',
        'search_run_at': '<ISO8601>'}` → CREATE-only with audit trail
        recording that a search ran and no link was made.
    """
    if dedup_decision is None:
        # No decision yet — return the search payload. Caller must run
        # the search, surface results to the operator, and re-call.
        return hubspot_search_company(intake)

    cp = intake.get("counterparty", {})
    name = cp.get("name", "")
    domain = _extract_domain(cp)
    loi_type = intake.get("type", "Unknown")

    pipeline_name, default_stage = _resolve_pipeline(loi_type)

    if "link_to_id" in dedup_decision:
        company_id = dedup_decision["link_to_id"]
        company_payload = {
            "objectType": "companies",
            "operation": "update",
            "objectId": company_id,
            "properties": {
                # Conservative on UPDATE — only refresh LOI-relevant
                # properties; do NOT clobber name/domain/lifecyclestage.
                "loi_status": "LOI Sent — Draft",
                "loi_last_sent": intake.get("dates", {}).get("loi_date", ""),
            },
        }
        deal_payload = {
            "objectType": "deals",
            "operation": "create",
            "properties": {
                "dealname": f"LOI-{loi_type}-{name}",
                "dealstage": default_stage,
                "pipeline": pipeline_name,
            },
            "associations": [{"to": "companies", "match_by": "id",
                              "value": company_id}],
        }
        return {
            "action": "hubspot_link_company",
            "tool": "manage_crm_objects",
            "dispatch": [company_payload, deal_payload],
            "output_path": output_path,
            "dedup_audit": {
                "operation": "link",
                "linked_to_id": company_id,
                "match_confidence": dedup_decision.get("match_confidence"),
                "match_property": dedup_decision.get("match_property"),
            },
        }

    if dedup_decision.get("force_create"):
        reason = dedup_decision.get("reason", "")
        if len(reason) < 15:
            raise ValueError(
                "dedup_decision.force_create requires a reason ≥ 15 chars "
                "documenting why the search produced no usable match"
            )
        company_payload = {
            "objectType": "companies",
            "operation": "create",
            "properties": {
                "name": name,
                "domain": domain,
                "description": cp.get("description", ""),
                "lifecyclestage": "opportunity",
                "loi_status": "LOI Sent — Draft",
            },
        }
        deal_payload = {
            "objectType": "deals",
            "operation": "create",
            "properties": {
                "dealname": f"LOI-{loi_type}-{name}",
                "dealstage": default_stage,
                "pipeline": pipeline_name,
            },
            # Association by domain works because we just created the
            # company with this domain — no ambiguity on this run.
            "associations": [{"to": "companies", "match_by": "domain",
                              "value": domain}] if domain else [],
        }
        return {
            "action": "hubspot_upsert_company",
            "tool": "manage_crm_objects",
            "dispatch": [company_payload, deal_payload],
            "output_path": output_path,
            "dedup_audit": {
                "operation": "create",
                "force_create": True,
                "reason": reason,
                "search_run_at": dedup_decision.get("search_run_at", ""),
            },
        }

    raise ValueError(
        "dedup_decision must contain either 'link_to_id' or "
        "'force_create: True' (with reason). Got: "
        f"{sorted(dedup_decision)}"
    )


def clickup_create_task(intake: dict, output_path: str) -> dict:
    """Build the payload for `clickup_create_task`."""
    cp = intake.get("counterparty", {})
    name = cp.get("name", "")
    loi_type = intake.get("type", "Unknown")

    return {
        "action": "clickup_create_task",
        "tool": "clickup_create_task",
        "dispatch": {
            "name": f"LOI follow-up: {name} — {loi_type}",
            "description": (
                f"LOI sent on {intake.get('dates', {}).get('loi_date', '')}. "
                f"Follow-up required to resolve [TBC] items and progress to MSA. "
                f"Draft: {output_path}"
            ),
            "priority": 2,  # High
            "tags": ["loi", loi_type.lower()],
        },
        "output_path": output_path,
    }


def artifact_storage_push(output_path: str, intake: dict) -> dict:
    """Dispatch to `artifact_storage.upload_artifact`."""
    return {
        "action": "artifact_storage_push",
        "tool": "artifact_storage.upload_artifact",
        "dispatch": {
            "output_path": output_path,
            "intake": {
                "type": intake.get("type"),
                "counterparty": {
                    "name": intake.get("counterparty", {}).get("name", "")
                },
                "dates": {
                    "loi_date": intake.get("dates", {}).get("loi_date", "")
                },
            },
        },
    }


def domain_card_create(intake: dict, output_path: str) -> dict:
    """Scaffold the `/domains/counterparties/{slug}/overview.md` card."""
    from scripts.artifact_storage import _slugify  # local import — avoid cycle

    cp = intake.get("counterparty", {})
    slug = _slugify(cp.get("name", ""))
    card_path = f"/domains/counterparties/{slug}/overview.md"

    return {
        "action": "domain_card_create",
        "tool": "Write",
        "dispatch": {
            "file_path": card_path,
            "content_preview": (
                f"# {cp.get('name', '')}\n\n"
                f"- LOI: {output_path}\n"
                f"- HubSpot: [pending]\n"
                f"- ClickUp: [pending]\n"
                f"- Drive: [pending]\n"
            ),
        },
    }


def cover_email_cross_check(intake: dict, output_path: str) -> dict:
    """Extract headline terms from a drafted cover email + map to LOI clauses.

    v3.7.0 ships the dispatch stub; the actual extraction happens in the
    orchestrator session where the email text is available in context.
    """
    return {
        "action": "cover_email_cross_check",
        "tool": "inline",
        "dispatch": {
            "loi_path": output_path,
            "intake_counterparty": intake.get("counterparty", {}).get("name", ""),
            "note": (
                "Cover-email cross-check runs in the orchestrator session. "
                "This dispatch stub confirms the action is selected; the "
                "actual email → clause mapping happens after the cover "
                "email is drafted."
            ),
        },
    }


DISPATCHERS: dict[str, Any] = {
    "hubspot_upsert_company": hubspot_upsert_company,
    "clickup_create_task": clickup_create_task,
    "artifact_storage_push": lambda intake, output: artifact_storage_push(output, intake),
    "domain_card_create": domain_card_create,
    "cover_email_cross_check": cover_email_cross_check,
}


def run_phase_8_actions(
    intake: dict,
    output_path: str,
    actions: list[str],
    *,
    dry_run: bool = True,
) -> dict:
    """Orchestrator for Phase 8 actions.

    Args:
        intake: Parsed intake YAML.
        output_path: Path to the generated .docx.
        actions: List of action keys (subset of ACTION_KEYS).
        dry_run: When True (default), return payloads without invoking.
                 When False, calling code is responsible for executing
                 each payload against its MCP tool.

    Returns:
        {
            "dry_run": bool,
            "actions": [{action result dict}, ...],
            "errors": [...],
        }
    """
    unknown = set(actions) - ACTION_KEYS
    errors = [f"Unknown action: {a}" for a in unknown]

    results = []
    for action in actions:
        if action not in ACTION_KEYS:
            continue
        try:
            dispatcher = DISPATCHERS[action]
            payload = dispatcher(intake, output_path)
            payload["dry_run"] = dry_run
            results.append(payload)
        except Exception as exc:  # broad catch — report per-action, don't halt
            errors.append(f"{action}: {exc!r}")

    return {
        "dry_run": dry_run,
        "actions": results,
        "errors": errors,
    }
