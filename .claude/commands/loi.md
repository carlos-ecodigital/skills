---tier: 0

description: Generate a Letter of Intent via the legal-assistant skill (5 types — EU / DS / WS / SS / EP). Optional argument: counterparty name.
---
Load the `legal-assistant` skill: read `.claude/skills/legal-assistant/SKILL.md` in full (especially the **Phase 0–8 Intake SOP (v3.3)** section). Then invoke the Phase 0–8 flow to produce a Letter of Intent.

**Skill:** legal-assistant
**Purpose:** Colocation LOI v3.2 / v1.0 production — End User (EU), Distributor (DS, Mode A/B), Wholesale (WS), Strategic Supplier (SS), Ecosystem Partnership (EP).

## Invocation

- `/loi` — asks for counterparty name in Phase 1.
- `/loi [CounterpartyName]` — pre-fills the counterparty short name and proceeds to Phase 1 gap questions.

## Phase flow (canonical, v3.4)

0. **Trigger** — slash command or natural language.
1. **Triage** — one batched round: short name, website, HubSpot / ClickUp IDs, email / Fireflies / deck paths, relationship context, turnaround. Minimum-input floor: counterparty name + one source.
2. **Type classification** — 5-type decision tree; confidence flag; user confirms.
3. **Source capture** — autonomous; WebFetch website, HubSpot / ClickUp MCPs, LinkedIn, press search, KVK / Companies House. Every material claim source-tagged per `_shared/counterpart-description-framework.md` Tier Hierarchy Policy.
4. **Batched intake** — one round; only gaps from Phase 3. Type-specific required fields validated. `counterparty.source_map` required for material-claim LOIs.
5. **Recital B draft** — 5-pillar methodology per `_shared/counterpart-description-framework.md`; source map with tier-1 URLs; user accepts or edits.
6. **Confirmation gate** — single-screen summary of every intake value + choices + Recital B + source_map. User confirms.
7. **Generation + QA** — write YAML, run `python generate_loi.py`, interpret QA status (PASS / PASS_WITH_WARN / FAIL). R-23 fabrication gate enforces source_map attribution.
7.5. **Mandatory `legal-counsel` review (v3.4)** — non-bypassable; structured 4-point review: clause-type appropriateness, meta-commentary scan, cross-clause consistency, source-verification sample of 3 material claims. Returns PASS / FLAG-FOR-REVISION / REJECT. No override path.
8. **Delivery** — emit path + next-step menu (Word / PDF / DocuSign via `executive-comms` / HubSpot stage update). Only reached after Phase 7.5 PASS.

## Invariants

- Do not hallucinate. Every material claim in Recital B must be attributable to a tier-1 source (counterparty's own website, official registry, or direct-quoted press) in `counterparty.source_map`, marked `[TBC]`, or pass `--source-override` with reason.
- Tier-2 press (FT / Reuters / Bloomberg / DCD / etc.) is citable **only with "as publicly reported" qualifier**. Tier-3 (analyst commentary / blogs / AI-generated) is never citable.
- Linter is enforcing. `fail` rules block output unless `--override R-xx` with reason. R-23 (fabrication gate) catches material numeric claims without source_map.
- Confirmation gate in Phase 6 is non-negotiable.
- Phase 7.5 `legal-counsel` review is **mandatory on every LOI** (v3.4). No override.
- Closing line is hardcoded "We look forward to working with you." No bespoke closings. If near-signature operational content is needed, produce a companion cover letter via `executive-comms`.

## Escalation

- Counterparty returns redlines → stop, invoke `legal-counsel`.
- Below minimum-input floor (no name or zero sources) → list gaps, do not proceed.
- M&A, investment, CIA-CAP, generic commercial LOI outside the 5 types → use `legal-counsel` instead.
