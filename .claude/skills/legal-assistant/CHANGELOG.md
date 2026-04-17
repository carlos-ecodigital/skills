# Changelog — legal-assistant

All notable changes to the `legal-assistant` skill.
Versioning: skill release version, not per-document template version (each template carries its own version number inside its filename).

---

## v3.2 — 2026-04-16

LOI framework v3.2. Post-mortem on five LOIs produced in 2026-04 (Cerebro, Aldewereld, SAG, InfraPartners, Cudo) surfaced a cluster of template content issues, methodological gaps, and missing relationship types. This release addresses them.

### Added

- **Recital A variant library** (`_shared/loi-recital-a-library.md`) — three canonical variants (`default` / `sovereignty` / `integration`) plus `bespoke` escape hatch, all MPN v3.2-aligned. Generator resolves variants at build time.
- **Counterpart description framework** (`_shared/counterpart-description-framework.md`) — 5-pillar methodology mapped to 3 lender questions, source-capture protocol (website / HubSpot / ClickUp / LinkedIn / press / Fireflies / KVK / deck), per-type tuning, consortium/federation guidance, anti-pattern catalogue, worked examples from the reviewed LOIs.
- **QA gate** (`_shared/loi-qa-gate.md` + embedded linter in `generate_loi.py`) — 20 rules with severity levels (`fail` / `warn` / `info`) and override mechanism. Pre-save lint blocks output on `fail` unless `--override R-xx --override-reason "..."` is supplied. Generates `{output}_qa.txt` alongside every build.
- **Strategic Supplier LOI** (`DE-LOI-SS-v1.0`) — fourth LOI type for supply-chain partners (EPCs, modular vendors, key suppliers). Forced 1–2 strategic-purpose selector drives clause inclusion. Reference template + YAML intake example. **Generator engine: partial (cover + Recitals A/B only); full clause builders pending in v3.3.**
- **Ecosystem Partnership LOI** (`DE-LOI-EP-v1.0`) — fifth LOI type for no-commercial-flow relationships (standards bodies, universities, co-marketing alliances, research consortia). Reference template + YAML intake example. **Generator engine: partial (cover + Recitals A/B only); full clause builders pending in v3.3.**
- **CLI flags**: `--override` (comma-separated rule IDs) and `--override-reason` (freeform string) on `generate_loi.py`.

### Changed

- **Recital A**: no longer cites "14 identified sites" or "12 months of commercial commitment" or "positioning as one of the leading". Library-sourced variants replace inline recital strings. YAML now supports `programme.recital_a_variant`.
- **Capacity language**: Customer-facing clauses now express capacity in MW IT + Designated Sites. "DEC Block" terminology removed from Cl. 1 definitions, Cl. 3 capacity clauses, and Schedule 1 entries. "DEC Block" remains internal delivery-unit vocabulary elsewhere.
- **Term language**: "minimum commitment term of 5 years" replaced across Wholesale and End User templates with "approximately 5 (five) years, indicative only and subject to confirmation in the MSA".
- **Cl. 4.2 "Revenue Chain"** with Unicode arrows (`→`) replaced with "Contractual Sequence" — institutional prose + numbered list (a)–(d). Zero Unicode arrows anywhere in the document body.
- **Closing-line policy**: Default closing = single sentence "We look forward to working with you." Bespoke closing (via `choices.bespoke_closing`) replaces the default entirely. Generator strips leading "We look forward..." phrases from bespoke to prevent the duplicated-phrase bug. Bespoke containing banned patterns ("confident that", "combination of", "will deliver meaningful value", multi-sentence) is rejected and falls back to default.
- **Schedule titles**: `(NON-BINDING)` suffix removed from all schedule annex titles. Italic prefatory note on each schedule carries the non-binding signal. Authoritative binding/non-binding assignment lives in Cl. 5.1 only.
- **Clause headings**: `(NON-BINDING)` suffix removed from Cl. 3 and Cl. 4 headings across all types (Wholesale, Distributor, End User). Same rationale — Cl. 5.1 / Cl. 8.1 is authoritative.
- **Version footer**: `DE-LOI-{Type}-v3.2` (up from v3.0).

### Fixed

- **Duplicated "We look forward to working with you"** — observed in Aldewereld and SAG bespoke closings where default + bespoke stacked. Generator now strips duplicate lead-phrases.
- **Recital A inconsistency** — Cerebro (2026-04-15) was missing the "14 identified sites" reference while Aldewereld had it; variant library ensures every LOI of a given type shares the same Recital A unless explicitly bespoke.
- **Schedule 1 redundant "(NON-BINDING)"** — previously both Cl. 5.1 body and annex title declared the schedule non-binding. Now single authoritative source in Cl. 5.1.
- **Sales-y adjectives in generated Recital A** — "leading sovereign AI infrastructure programmes" language removed from all variants; linter R-14 warns on regression.

### Deprecated

- `commercial.dec_block_count` — YAML field removed. Generator raises a migration error ([R-18]) pointing to this changelog. Capacity is now expressed exclusively via `commercial.indicative_mw`.
- `commercial.min_term` semantics — field kept, but now renders as "approximately N, indicative only", not "minimum commitment term of N".

### Migration

Old intake YAMLs with `commercial.dec_block_count` will fail validation with:

```
[R-18] commercial.dec_block_count is deprecated in v3.2. Use commercial.indicative_mw instead.
```

To migrate: delete the `dec_block_count` line. Keep `indicative_mw` as the single source of capacity. No auto-migration provided (clean cut).

Add `programme.recital_a_variant: default` (or `sovereignty` / `integration`) to every intake YAML. If omitted, generator uses `default` and emits info `[R-16]`.

### Verified

- All four existing intake examples (`intake_example_enduser`, `intake_example_distributor`, `intake_example_distributor_referral`, `intake_example_wholesale`) regenerate cleanly under v3.2 with QA `PASS` status.
- Body content audit confirms: zero hits for "14 identified sites", "12 months of commercial commitment", "DEC Block", "minimum commitment term of 5", "We are confident that", Unicode arrows, "Revenue Chain", "(NON-BINDING) in Schedule title", or duplicated "We look forward" across all four generated documents.

### Unreleased (pending in v3.3)

- Full clause builders for Strategic Supplier (Cl. 3.1–3.8 per-purpose + Cl. 4 engagement + Schedule 1 capability matrix).
- Full clause builders for Ecosystem Partnership (Cl. 1–7 + optional Schedule 1 joint-activity plan).
- `/loi` slash command registration as user-invocable entry point.
- SKILL.md Phase 0–8 end-to-end intake SOP (triage → classification → source capture → batched intake → Recital B → confirmation gate → generation + QA → delivery).
- ASSEMBLY_GUIDE.md 5-type decision tree; SS purpose selector matrix; EP variant guidance; consortium/federation descriptor pattern.
- FEATURE_MATRIX.md SS + EP columns.
- SOP.md team-facing workflow rewrite.
- Regression regeneration of the 5 reviewed LOIs (Cerebro, Aldewereld, SAG, InfraPartners, Cudo) against v3.2 with diff report.

---

## v3.1 — 2026-04-13

- Renamed skill from `loi-generator` to `legal-assistant`; added Site HoT stream.
- LOI/NCNDA v3.0 templates (EndUser, Distributor Mode A/B, Wholesale) stabilised.
- DE-MIA Master Introduction Agreement v1.0 built as parallel workstream.

## v3.0 — 2026-04-05

- LOI/NCNDA v3.0 — three-type modular system (End User / Distributor / Wholesale) with shared core chassis (Cl. 5–8) and type-specific modules (Cl. 3–4, Schedule 1). First production release of the YAML-to-.docx engine.
