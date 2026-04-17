# Changelog — legal-assistant

All notable changes to the `legal-assistant` skill.
Versioning: skill release version, not per-document template version (each template carries its own version number inside its filename).

---

## v3.3 — 2026-04-16

Full LOI engine for all five types. Ships on a single branch with v3.2, after reconciling `bespoke_closing` with OPEN-1 (commit `2097f52`).

### Added

- **Strategic Supplier (SS) full engine** — `clause3_ss()` with purpose-driven sub-clause inclusion (capacity_lock_in → 3.2/3.3; pricing_volume → 3.4/3.5; supply_chain_de_risking → 3.6; engineering_integration → 3.7 with joint_ip choice; pipeline_visibility → 3.8 ROFR with 20-BD window). `clause4_ss()` with 4.1 (conditional), 4.2 (always — Contractual Sequence: LOI → Framework Agreement → SOWs → deliverables), 4.3 (conditional on engineering_integration), 4.4 (always — CoC), 4.5 (conditional), 4.6 (always — roadmap). SS branches in `definitions`, `clause2`, `clause7_nc` (light supply-side, references Framework Agreement), `clause_general`, `schedule` (Scope and Capability Matrix), `recitals` (Recitals C and D). SS-specific `validate()` block (1–2 strategic_purposes required; lead_time_target / volume_indicative / joint_ip required conditionally).
- **Ecosystem Partnership (EP) full engine** — separate `_build_ep()` pipeline because EP has different structure (no Cl. 5 Project Finance; no Cl. 7 Non-Circumvention; Cl. 5 is IP & Deliverables; Cl. 6 is Tier A light mutual with 7 sub-clauses; Cl. 7 is General with 11 sub-clauses). New methods: `definitions_ep()` (3 terms: CI, Collaboration, Representatives), `clause2_ep()` (non-commercial framing, 4 sub-clauses), `clause3_ep()` (5 sub-clauses — Themes, Activity Categories, Governance, Working-Group Participation, Non-Exclusivity), `clause4_ep()` (Announcements and Branding — 4.1 conditional on `announcement_protocol`, 4.2 conditional on `logo_use`, 4.3 attribution), `clause5_ep()` (IP & Deliverables — 5.1 Background IP, 5.2 Joint Deliverables, 5.3 No Assignment, 5.4 Publication), `clause6_ep()` (Tier A light — 7 sub-clauses mutual), `clause7_ep_general()` (General — 11 sub-clauses with explicit "No Commercial Commitment" in 7.2), `schedule_ep()` (optional Joint Activity Plan — only rendered if `ecosystem.joint_activity_plan` provided). EP-specific `validate()` block.
- **Recital C/D branches** for SS and EP in `recitals()`.
- **SKILL.md Phase 0–8 SOP** — structured phases with prompt templates at executable-by-a-colleague detail. Covers trigger, triage (minimum-input floor), type classification, source capture (WebFetch / HubSpot / ClickUp / LinkedIn / press / KVK / Companies House), batched intake, Recital B draft with source map, assumption-confirmation gate, generation + QA, delivery with next-step menu. 300+ lines of new guidance.
- **SOP.md rewrite** — team-facing 9-step workflow aligned with Phase 0–8. Minimum-input floor documented. What Claude will NOT do spelled out.
- **`/loi` slash command** — `.claude/commands/loi.md`. Registered at tier-0. Optional counterparty-name argument pre-fills Phase 1.
- **Per-type version footer** — `DE-LOI-{Type}-v3.2` for EU/DS/WS; `DE-LOI-{Type}-v1.0` for SS/EP.
- **Regression report** — `regression-v3.3-report.md`. Cudo (WS) + SAG (DS Mode B) + InfraPartners (SS) regenerated against v3.3. 9 + 7 + 4 anti-pattern hits in originals → 0 + 0 + 0 in regenerations. Word-count reduction: Cudo flat (trimmed Recital B balanced by Cl. 4.2 expansion), SAG −576 (−14%, consortium rework), InfraPartners −421 (−11%, SS-native chassis).

### Changed

- **`bespoke_closing` removed from `signature()` per OPEN-1** — commit `2097f52` on main closed OPEN-1 by removing `choices.bespoke_closing` with the rationale that operational near-signature content belongs in the letter body, not the closing line. v3.2 re-added it with a dedupe handler to solve a v3.1 duplicate-phrase bug; v3.3 honors OPEN-1 by removing the dedupe handler entirely. Closing is hardcoded single-sentence "We look forward to working with you." The `choices.bespoke_closing` YAML field is silently ignored for backward compat (no error).
- **Framework Agreement vocabulary for SS** — SS Cl. 7 and Cl. 8 use "Framework Agreement" as the downstream binding document name, not "MSA". New definition entry for "Framework Agreement" in SS Cl. 1.
- **`build()` routing** — SS and EP now route through dedicated clause builders instead of falling through to `clause3_eu()` or the v3.2 partial engine.
- **`validate()`** — extended with type-specific blocks for SS (purpose validation, conditional field requirements) and EP (relationship_type enum, mandatory collaboration_themes and joint_activity_categories).

### Fixed

- **OPEN-1 reconciliation** — v3.2 `da8ad63` added `bespoke_closing` dedupe in conflict with main's `2097f52`. v3.3 removes the dedupe block, restoring main's simple `signature()` behaviour. The handover at `~/.claude/plans/sync-messages-2026-04-16.md` asked for this drop explicitly.
- **SS partial engine path (v3.2)** — v3.2 had SS and EP route through a placeholder "engine note" branch in `build()`. v3.3 replaces this with full clause execution.

### Verified

- All 6 intake examples (EU / DS Mode A / DS Mode B / WS / SS / EP) regenerate with QA `PASS` status.
- Body content audit across all 6 produced .docx confirms zero hits for: "14 identified sites", "12 months of commercial commitment", "DEC Block", "minimum commitment term of 5", "We are confident that", Unicode arrows, "Revenue Chain", "(NON-BINDING)" in schedule title, duplicated "We look forward", "(NON-BINDING)" in clause heading.
- Regression: 3 reviewed LOIs regenerated against v3.3 with anti-pattern hits eliminated (9→0, 7→0, 4→0).
- Deprecation error (R-18) fires on legacy YAML with `commercial.dec_block_count`.

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

### Unreleased

Everything from the v3.2 § Unreleased was shipped in v3.3 (see above). No open items for the legal-assistant skill beyond the pre-existing blockers noted below.

- `generate_site_hot.py` — Site HoT form-fill engine still pending Git LFS binary fetch. Tracked separately in `~/.claude/plans/temporal-dreaming-meerkat.md` Phase 1.5.
- SAR md cover bug in `document-factory/generate.py` — out of scope for this skill; diagnosed in a separate session's plan file. ~30 min of Python work.

---

## v3.1 — 2026-04-13

- Renamed skill from `loi-generator` to `legal-assistant`; added Site HoT stream.
- LOI/NCNDA v3.0 templates (EndUser, Distributor Mode A/B, Wholesale) stabilised.
- DE-MIA Master Introduction Agreement v1.0 built as parallel workstream.

## v3.0 — 2026-04-05

- LOI/NCNDA v3.0 — three-type modular system (End User / Distributor / Wholesale) with shared core chassis (Cl. 5–8) and type-specific modules (Cl. 3–4, Schedule 1). First production release of the YAML-to-.docx engine.
