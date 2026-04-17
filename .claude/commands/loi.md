---tier: 0

description: Generate a Letter of Intent via the legal-assistant skill (5 types — EU / DS / WS / SS / EP). Optional argument: counterparty name.
---
Load the `legal-assistant` skill: read `.claude/skills/legal-assistant/SKILL.md` in full (especially the **Phase 0–8 Intake SOP (v3.3)** section). Then invoke the Phase 0–8 flow to produce a Letter of Intent.

**Skill:** legal-assistant
**Purpose:** Colocation LOI v3.2 / v1.0 production — End User (EU), Distributor (DS, Mode A/B), Wholesale (WS), Strategic Supplier (SS), Ecosystem Partnership (EP).

## Invocation

- `/loi` — asks for counterparty name in Phase 1.
- `/loi [CounterpartyName]` — pre-fills the counterparty short name and proceeds to Phase 1 gap questions.

## Phase flow (canonical)

0. **Trigger** — slash command or natural language.
1. **Triage** — one batched round: short name, website, HubSpot / ClickUp IDs, email / Fireflies / deck paths, relationship context, turnaround. Minimum-input floor: counterparty name + one source.
2. **Type classification** — 5-type decision tree; confidence flag; user confirms.
3. **Source capture** — autonomous; WebFetch website, HubSpot / ClickUp MCPs, LinkedIn, press search, KVK / Companies House.
4. **Batched intake** — one round; only gaps from Phase 3. Type-specific required fields validated.
5. **Recital B draft** — 5-pillar methodology per `_shared/counterpart-description-framework.md`; source map; user accepts or edits.
6. **Confirmation gate** — single-screen summary of every intake value + choices + Recital A variant + Recital B. User confirms.
7. **Generation + QA** — write YAML, run `python generate_loi.py`, interpret QA status (PASS / PASS_WITH_WARN / FAIL).
8. **Delivery** — emit path + next-step menu (Word / PDF / DocuSign via `executive-comms` / HubSpot stage update).

## Invariants

- Do not hallucinate. If a fact is not sourced, ask or flag `[TO BE CONFIRMED]`.
- Source-attribute every material Recital B claim.
- Linter is enforcing. `fail` rules block output unless `--override R-xx` with reason.
- Confirmation gate in Phase 6 is non-negotiable.
- Closing line is hardcoded "We look forward to working with you." No bespoke closings. If near-signature operational content is needed, produce a companion cover letter via `executive-comms`.

## Escalation

- Counterparty returns redlines → stop, invoke `legal-counsel`.
- Below minimum-input floor (no name or zero sources) → list gaps, do not proceed.
- M&A, investment, CIA-CAP, generic commercial LOI outside the 5 types → use `legal-counsel` instead.
