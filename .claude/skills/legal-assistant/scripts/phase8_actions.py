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


def hubspot_upsert_company(intake: dict, output_path: str) -> dict:
    """Build the payload to create/update a HubSpot company + deal.

    Does NOT invoke the MCP tool; returns a payload the orchestrator
    can pass to `manage_crm_objects`.
    """
    cp = intake.get("counterparty", {})
    name = cp.get("name", "")
    domain = cp.get("domain") or cp.get("website", "").replace("https://", "").replace(
        "http://", ""
    ).rstrip("/")

    company_payload = {
        "objectType": "companies",
        "operation": "upsert",
        "properties": {
            "name": name,
            "domain": domain,
            "description": cp.get("description", ""),
            "lifecyclestage": "opportunity",
            "loi_status": "LOI Sent — Draft",
        },
    }

    loi_type = intake.get("type", "Unknown")
    deal_payload = {
        "objectType": "deals",
        "operation": "upsert",
        "properties": {
            "dealname": f"LOI-{loi_type}-{name}",
            "dealstage": "loi_sent",
            "pipeline": "Commercial",
        },
        "associations": [{"to": "companies", "match_by": "domain", "value": domain}],
    }

    return {
        "action": "hubspot_upsert_company",
        "tool": "manage_crm_objects",
        "dispatch": [company_payload, deal_payload],
        "output_path": output_path,
    }


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
