# Changelog — legal-assistant

All notable changes to the `legal-assistant` skill.
Versioning: skill release version, not per-document template version (each template carries its own version number inside its filename).

---

## v3.7.0 — 2026-04-20

Consolidated release covering the full v3.6.1 + v3.6.2 + v3.6.3 + v3.7 roadmap from `~/.claude/plans/expressive-cooking-flamingo.md`. Three field retrospectives (Cerebro, Armada, InfraPartners) drove 29+ distinct improvement items across linter expansion, CLI tooling, phase-logic hardening, extensibility layer, and cross-skill ecosystem. Test baseline 307 → 368 passing. All additions backward-compatible — every new YAML field is optional with v3.6.0-matching defaults; all 10 goldens unchanged.

Template filename stays `DE-LOI-{Type}-v3.2` (skill release ≠ template version).

### Added — linter / CLI / session tooling (v3.6.1 scope)
- **R-29 (fail)** — URL content verification. Opt-in via `--verify-source-urls` CLI flag (default OFF in v3.7.0; default-on in v3.8). For each `source_map[pillar_N]` URL, fetches and checks Recital B claim keywords appear in ≥500 chars of content. If missing → downgrade to `[TBC — url_content_insufficient]`.
- **R-30 (fail)** — Double-period detector on rendered body. Excludes ellipsis and numbered-list prefixes.
- **R-31 (warn)** — `contact_name == signatory_name` fires on case-insensitive match; "confirm intentional single-point-of-contact."
- **R-27/R-28 normalization** — broadened to match bare `TBC` (not only `[TBC]`) for signatory detection + density counting.
- **R-11 helper** — `certifications_in_source(intake)` surfaces detected ISO/SOC/PCI certs in QA report so Phase 5 makes the include/omit decision explicitly.
- **R-21 narrowing** — `purpose-built` now allowed inside Clause 3 product-capability text; banned in Recital A/B/closing only.
- **R-24 (warn)** — brochure-sourced pillars require tier-1 corroboration before signing.
- **Brochure source_map token** — `source_map[pillar_N]` accepts `internal:brochure_{YYYYMMDD}_{slug}` tokens as tier-2 sources.
- **`--recital-b-only <path>`** — regenerate Recital B only; replace paragraph in existing .docx; write `_v{N}`.
- **`--audit-only`** — read `prior_loi_path`; run full linter; emit `{basename}_audit.txt` without regenerating.
- **`--verify-source-urls`** — activates R-29.
- **`--phase-8-auto-execute`** — CLI flag to activate real HubSpot + ClickUp writes (dry-run by default).
- **`choices.recital_b_density: terse|standard|verbose`** — word-count cue for Recital B generation.
- **`SESSION_LOG.md` artifact** — emitted alongside every `.docx` capturing decisions, CLI flags, QA summary, customizations.

### Added — phase logic / doc sync (v3.6.1 + v3.6.2 scope)
- **Recital A canonicalization** — deleted `sovereignty | integration | bespoke` variant options from SKILL.md, ASSEMBLY_GUIDE.md, and all 6 `intake_example_*.yaml`.
- **Bespoke Recital A checklist gate** — Phase 5 requires operator confirmation of (a) non-commercial counterparty OR (b) canonical tail materially incorrect; justification captured in `choices.recital_a_bespoke_justification`.
- **Categorical-vs-tactical descriptor table** added to `_shared/counterpart-description-framework.md`.
- **Phase 2.5 name disambiguation** — WebSearch check for counterparty-name collision.
- **Phase 3 systematic parallel source-capture** + prior-LOI `/extract`-first rule.
- **Phase 3.5 public-web-dark detection** — `dark_web_counterparty: true` flag; elevated Phase 7.5 review.
- **Phase 4.5 signatory-name cross-check** — Fireflies fuzzy match; domain-surname homonym escalation.
- **Phase 5 newest-fixture starting point** — `colocation/examples/README.md` points to newest `regression/v{X.Y}/*` first.
- **Phase 6 evidence-strength column** — per-pillar Tier-1/Tier-2/[TBC]; auto mode 10s non-blocking interrupt.
- **Phase 8 auto-actions** — HubSpot + ClickUp wired; dry-run default + `--phase-8-auto-execute`.
- **`allowed-tools` expanded** — `fireflies_search`, `fireflies_get_transcript`, `manage_crm_objects`, `clickup_create_task`.
- **LOI sizing framework** — new `_shared/loi-sizing-framework.md` (R1–R4 ratios).
- **`mark_chapter` hygiene rule** added.
- **`scripts/artifact_storage.py`** — implements v3.5.3 J13 Drive upload (deferred since v3.5.3).

### Added — extensibility schema (v3.6.3 scope)
- **`custom.definitions[]`** — arbitrary `{key, text}` injected at top of Cl. 2.
- **`custom.definitions_include[]`** — include-list resolves against new `_shared/loi-common-defined-terms.md` library (Super-Factory Initiative, Designated Site, Framework Agreement, DEC Block).
- **`custom.clauses[]` with `mode: append`** — append arbitrary clauses to document body.
- **`choices.confidentiality_opt_outs`** — suppress named §6 Tier B sub-clauses with auto-renumber.
- **`choices.include_schedule: bool`** — when false, suppresses Schedule 1 + scrubs §8.1(a) + §4.2(d).
- **`supplier.rofr`** — parameterizes §3.8 RoFR clause (styles: alignment | sole_discretion | hard_minimum | milestone).
- **`supplier.referral_rider: bool`** — adds §3.9 Mutual Referral Rider.
- **`counterparty.relationship_cluster` + `identity_map`** — structured metadata in QA report.
- **`dates.financing_context`** — validated + surfaced in QA.
- **`scripts/phase8_actions.py`** — dispatch payloads for Phase 8 actions.

### Added — cross-skill ecosystem (v3.7 scope)
- **`legal-assistant/_shared/fireflies-integration.md`** — call patterns for Phase 3 + 4.5.
- **`legal-assistant/docs/tooling/image-ingest.md`** — HEIC→JPG `sips` tooling.
- **`legal-assistant/docs/glossary.md`** — 20 DE acronyms.
- **New sibling skill `de-executive-comms`** — executive-voice drafting with Gmail MCP fallback + tone markers + LOI cover email template + tone audit grid.

### Changed
- `clause6()` Tier B refactored to declarative list honoring `confidentiality_opt_outs`. Backward-compatible when opt_outs is empty.
- `definitions()` now injects `custom.definitions[]` + `definitions_include[]` entries.
- `build()` respects `choices.include_schedule` and calls `_inject_custom_clauses()` after signature.
- `qa_lint()` emits new INFO lines for `relationship_cluster`, `identity_map`, `financing_context`, `certifications_detected`.

### Verified
- **368/368 pytest** tests pass (307 baseline + 25 specA linter + 36 specC extensibility).
- **10 goldens unchanged** — all additions backward-compatible.
- All schema additions validate on absence (default paths preserve v3.6.0 rendering).

### Deferred to v3.7.1 (explicit scope cut — flagged for user decision)
- **Joint Stocking Programme clause template** (InfraPartners §5.6) — parametric on `supplier.lead_time_target < 6 months`.
- **Co-Marketing clause template** (InfraPartners §5.7) — parametric on `supplier.co_marketing`.
- **84-item audit checklist generator** — `{output}_AUDIT.txt` emitter.
- **`custom.clauses` modes `replace` + `insert-after:N`** — validated but body injection supports `append` only.
- **Post-template renumbering pass** for arbitrary gap-closing (confidentiality opt-outs already auto-renumber via list approach).

---

## v3.6.0 — 2026-04-20

Seven production-blocking bug fixes surfaced by three field retrospectives: Cerebro Wholesale (Jonathan Glender, 2026-04-17), Armada Strategic Supplier (2026-04-19), InfraPartners Strategic Supplier (2026-04-19). Each fix written test-first per PRINCIPLES.md #4; 15 new tests in `tests/test_v3_6_0_bugs.py`. Plus three doc-only additions. Template filename version stays `DE-LOI-{Type}-v3.2` — skill release ≠ template version.

### Fixed
- **Bug 1 — Cl. 8.2 `tthe` typo (all non-EndUser types)** (Armada §2.1). Non-EU path concatenated `"...t" + "t"` producing `"tthe good faith"`. `clause_general` line 1583 — dropped redundant `t` from the first ternary fragment.
- **Bug 2 — §8.1(b) "Project Finance and Assignment" leak in SS** (InfraPartners §4.1). Binding-provisions list hardcoded the Wholesale/Distributor Cl. 5 label; SS Cl. 5 is "Supply Chain and Delivery Commitment" and EP Cl. 5 is "IP and Deliverables". `clause_general` line 1577 — branch on `self.t` to emit the correct label per type.
- **Bug 3 — §8.9 "(ALT-A)" drafting marker leak** (InfraPartners §4.2). Entire-Agreement clause referenced "any NDA referenced in Clause 6 (ALT-A)" regardless of `choices.existing_nda`. Line 1600 — gate on `self.choice("existing_nda")`: with NDA → "the NDA referenced in Clause 6"; without → no NDA reference at all.
- **Bug 4 — Cl. 4.2 meta-commentary trailer (SS + WS)** (Armada §2.2). Template emitted "Each stage is designed to provide increasing commercial certainty and to support Digital Energy's project finance activities." — explains the LOI rather than creating obligation; R-22 class. Removed from both `clause4_ss` (line 1312) and `clause4_ws` (line 1384).
- **Bug 5 — double-period on Recital B** (Armada §2.3, InfraPartners §4.3). Engine appended literal `.` to `counterparty.description` without stripping existing trailing period. `recitals()` line 696 — `desc.rstrip().rstrip(".")` before concat.
- **Bug 6 — double-period on SS Cl. 3.1(b) `core_capability`** — same class as bug 5. `clause3_ss` line 1177 — `_cc.rstrip().rstrip(".")` before concat.
- **Bug 7 — preamble missing company number for Party 2** (InfraPartners §4.4). Party 2 conditional required BOTH `cp_reg_type` AND `cp_reg_number` to render, silently dropping the number when `reg_type` was unset. Party 1 has a KvK fallback; Party 2 now has a "company number" generic fallback when `reg_type` is absent. `parties_preamble` lines 717-722.

### Added
- `tests/test_v3_6_0_bugs.py` — 15 new regression tests, one or more per bug, exercising the exact field-observed failure modes. RED-first per PRINCIPLES.md #4.
- **Auto-version output filenames** (v3.6.0 item b). `generate_loi.py main()` — when target `.docx` exists, append `_v{N}` and increment until unique. Surfaces `[auto-version]` stderr note. Addresses file-confusion observed in all three retrospective sessions.
- **SS strategic-purpose → commercial-intent cross-reference table** (v3.6.0 item k, InfraPartners §4.5). New section in SKILL.md Step 3 SS subsection. Clarifies RoFR → `pipeline_visibility` mapping (not `capacity_lock_in` as InfraPartners session initially attempted).
- **DE signatory-title memo** (v3.6.0 item m). HTML comment block in SKILL.md Phase 6 summary template — notes Carlos Reuven holds CEO (Group AG) + Director (NL BV) titles; both legally valid; default is Director for NL BV pre-MSA; override via `provider.signatory_title` when CEO-signed variant needed.

### Verified
- 307/307 pytest tests pass (baseline 250 + 7 v3.5.6 scope G retained + 15 new v3.6.0 + v3.5.8 tripwires retained — full regression green).
- 10 goldens regenerated; diff reviewed — only expected content changes (no `tthe`, no Cl. 4.2 meta-trailer, §8.1(b) per-type labels correct, no `(ALT-A)` marker, no double-period on forced trailing-period inputs, Party 2 reg_number appears without reg_type when provided).
- All six `intake_example_*.yaml` regens QA PASS.
- All four `regression/v3.5/*_intake.yaml` regens QA PASS.

### Not in scope (future releases — see `~/.claude/plans/expressive-cooking-flamingo.md`)
- **v3.6.1**: linter expansion (R-29 URL-content verify, R-30 double-period, R-31 contact==signatory), `--recital-b-only` flag, density profile, Recital A doc canonicalization, `--audit-only`, `SESSION_LOG.md` artifact.
- **v3.6.2**: Phase 2.5/3.5/4.5/6/8 workflow additions, Fireflies MCP, HubSpot + ClickUp write auto-execution.
- **v3.6.3**: `custom.*` YAML extension layer, `supplier.rofr` structured block, Joint Stocking + Co-Marketing clause templates.

---

## v3.5.8 — 2026-04-19

PRINCIPLES.md tripwire closure. Five principles (#1 / #4 / #5 / #6 / #12) moved from "pending v3.6" to implemented. Closes the items Jonathan + Carlos flagged as "house-of-cards" risk after the v3.5.5 post-mortem. Test harness grows from 139 → 250 passing checks in both repos. No render-logic change; no intake YAML change; no sibling docs change beyond PRINCIPLES.md.

### Added — #5 Golden-file integration tests
- `tests/_fingerprint.py` — deterministic .docx digest (paragraph count + per-paragraph text hash + space_before/after + alignment; table shape + cells; section margins in mm; footer alignment + text). Skips volatile fields (timestamps, absolute paths, UUIDs).
- `tests/test_golden_files.py` — parametrised across 10 intakes (6 examples + 4 regression fixtures). For each, regenerates .docx, fingerprints it, diffs against committed `tests/goldens/<slug>.json`. Mismatch = test fails with human-readable paragraph-level diff.
- `tests/conftest.py` — registers `--update-goldens` pytest flag. Workflow: edit render logic → `pytest --update-goldens` → review `git diff tests/goldens/` → commit alongside code. CI default (no flag) fails on any unexplained diff.
- 10 goldens seeded in `tests/goldens/` per repo. Staging goldens were seeded from staging's own generator output (not mirrored from upstream) because the two generators have legitimate cosmetic divergence (`document-factory` vs `de-document-factory` import path).

### Added — #6 Visual layout invariant tests
- `tests/test_visual_layout.py` — module-scoped fixture generates one Polarise Wholesale LOI reference doc; 15 tests assert concrete `paragraph_format.space_after`, `alignment`, and section geometry values. Direct guard against the v3.5.5 Parties Preamble spacing bug (blank-paragraph spacers → ~15pt gap, vs 6pt via `space_after`).
- Coverage: section geometry (A4 / margins 20-35-25-20 mm / `different_first_page_header_footer`), footer (CENTER alignment + NL entity + no Swiss AG leak), Parties Preamble (4 paragraphs, intro + 2 parties at 6pt `space_after`, opener/closing text), signature block (no KvK: label, no ACKNOWLEDGED AND AGREED, Place: field present twice), brand rename (zero `the Provider`, Digital Energy ≥ 20 occurrences).

### Added — #12 Intake structural-shape linter
- `tests/test_intake_structural_shape.py` — 79 tests asserting all 6 `intake_example_*.yaml` files share the consistent top-level contract (type / provider / counterparty / dates / programme / protection / choices) plus per-type additions (commercial / schedule_1 / partnership_mode / supplier / ecosystem).
- Second-level shape checks: `provider` must carry the required identity fields; `counterparty` must carry `source_map`; dates + programme + recital_a_variant enum validated; source_map pillar keys + value types enforced. Regression guard against v3.5.2-era bug where one intake shipped with a missing sub-field and the generator tolerated it silently for one type only.
- Positive-band checks: provider addresses must NOT contain "Zug" (v3.5.1 A'' — Swiss AG parent address leak guard); provider signatory_name must NOT be "Jelmer ten Wolde" (v3.5.1 A — default NL-BV pre-MSA signer is Carlos Reuven / Director).

### Added — #4 Branch-specific test enforcement (CI)
- Both repos' `legal-assistant-tests.yml` now carry an `Enforce test-changes-with-generator-changes` step that runs on every PR. Compares `git diff --name-only origin/<base>...HEAD`; if `generate_loi.py` appears in the diff but no file under `tests/` does, fails the job.
- Escape hatch for documentation-only or pure-comment generator edits: include the literal marker `[skip-test-check]` in any commit message on the branch. Rationale: rare but real case (e.g., docstring-only edits), and the marker forces explicit acknowledgement of test skip.
- CI checkout now uses `fetch-depth: 0` to make the merge-base diff reliable.

### Added — #1 Mirror-edit discipline sentinel
- `tests/mirror-manifest.txt` — sha256sum manifest of the test-harness files that must be byte-identical across upstream + staging. Committed verbatim in both repos.
- `tests/test_mirror_integrity.py` — 7 tests verifying each manifest-listed file hashes to the expected value. Mismatch = silent drift caught in CI.
- `tests/regen-mirror-manifest.sh` — upstream-only regeneration script. Workflow: mirror-edit upstream → regen → copy manifest to staging → commit to both.
- **Scope decision:** `generate_loi.py` is intentionally excluded from the manifest because staging uses `de-document-factory/` import path (legitimate DEGitOS divergence); byte-level hashing would false-positive. Tripwire targets the silent-drift class — test-harness files that don't get the same PR-review scrutiny as generator edits. Generator drift is covered by the standard review process plus the new golden-file tests.

### Changed — `docs/PRINCIPLES.md`
- Status table updated: items 1 / 4 / 5 / 6 / 12 flipped from ⏳/🟡 to ✅. Only items 3 (additive-first) and 10 (layer contracts) remain at partial/pending — both are review-discipline items where automation is lower-leverage than checklist rigor.
- "Priority for v3.6" sentence replaced with "Remaining work" pointing at items 3 and 10.

### Verified
- Upstream: 250/250 pytest tests pass (139 baseline + 10 goldens + 15 visual + 79 shape + 7 mirror-integrity).
- Staging: 250/250 pytest tests pass (same split).
- All 10 intake regens still QA PASS; regression fixtures unchanged.
- Golden mismatch detection verified end-to-end by tampering a golden entry (set `n_paragraphs` 151 → 152): test failed with "paragraph count: expected 152 got 151". Restored → green. Replayed the same loop with a visual-layout assertion (changed expected margin): failed as expected. Restored → green.
- Mirror-integrity drift detection verified: initial mirror exposed pre-existing cosmetic drift between upstream and staging `generate_loi.py` (~121 diff lines, all comment/wording plus the legitimate document-factory path). The drift is being tracked separately; mirror-manifest scope was narrowed to tests/ only for v3.5.8 to avoid false positives on legitimate generator-import divergence.

### Not in scope
- **#3 additive-first** — review-discipline; no automated tripwire proposed yet.
- **#10 layer contracts** — versioning-rigor; partially covered by existing commit-message convention.
- **Generator drift reconciliation** between upstream and staging `generate_loi.py` — surfaced by the mirror-integrity work; scheduled as a separate targeted PR so v3.5.8 stays additive-only.

---

## v3.5.7 — 2026-04-17

Sibling docs sync — brings `ASSEMBLY_GUIDE.md`, `FEATURE_MATRIX.md`, and `SOP.md` to v3.5.6 state. Documentation-only change; no code change; all 139 pytest tests remain passing; all 10 intakes regenerate QA PASS.

Executes the scoped edit plan in `~/.claude/plans/v3.5.4-sibling-docs-sync.md` (originally ~51 edits targeted), consolidated into coherent new sections rather than mechanical line-by-line patches.

### Changed — ASSEMBLY_GUIDE.md
- Section 1 heading: "LOI Type Selection (5 types, v3.2)" → "(5 types, v3.5)"; template versions DE-LOI-*-v3.2 → -v3.5
- Bespoke-language examples (Distributor Cl. 3, 6 sub-examples): removed all `the Provider` / `The Provider` (brand rename — 6 occurrences replaced with `Digital Energy`); stripped `purpose-built AI colocation facilities` (7 occurrences; v3.4 banned body-wide)
- "Signing Entity" section expanded with v3.5.1 canonical entity data table (NL BV + AG) and v3.5.2 entities-register pattern (A: explicit fields / B: `provider.entity` lookup / C: minimal `type:` only auto-expansion)
- New section: **Parties Preamble** (v3.5.2 Scope A''') — structure, output format, brand-name defined term, v3.5.5 spacing fix
- New section: **Recital B — Signal Test methodology** (v3.5.2 Scope 0) — 3-gate test, writer discipline, R-24/R-25/R-27/R-28 rules, v3.5.6 Scope D refinements (pillar diagnostic + sentence-boundary `[TBC]`)
- New section: **Phase 7.5 — Mandatory legal-counsel two-pass review** (v3.4 + v3.5.6) — junior 4-point + senior six-axis; enforcement opt-in; sentinel hash mechanics
- "Version Control" section: all five template rows bumped to v3.5 / 2026-04-17; `**v3.2 changes:**` one-line note replaced with **full changelog summary v3.2 → v3.5.7** covering every interim release

### Changed — FEATURE_MATRIX.md
- Stream header: "LOI/NCNDA v3.2 (5 sub-types)" → "v3.5 (5 sub-types)"
- Clause Structure matrix: added **Parties Preamble** row (v3.5.2); **Recital B** row annotated with Signal Test 3-gate reference; **Cl. 5** row updated for SS (now "Supply Chain and Delivery Commitment", not revenue bankability) and EP (now "N/A — IP and Deliverables"); **Cl. 6** row annotated with EP "will exchange" (v3.5.3); **Schedule 1** row annotated with v3.5.1 `technical.gpu_platform` read from YAML
- "v3.2 commonalities" section expanded to **per-release commonalities** (v3.2 / v3.4 / v3.5.1 / v3.5.2 / v3.5.3-cont / v3.5.6)
- "Project Finance Features by Type" matrix: added SS + EP columns (was EU/DS/WS only); SS Cl. 5.1 marked "N/A — supply-side bankability (v3.4)"; EP marked "N/A — no Cl. 5 Finance"
- "Commercial Features by Type" matrix: "Capacity in DEC Blocks" row → "Capacity in MW IT (v3.2 — DEC Blocks deprecated)"; all rows extended to SS + EP columns; expansion rights row annotated with v3.5.1 J3 non-numeric branch
- New section: **v3.5.x Feature Additions — Cross-Type** — tabular summary of every new cross-type feature (Parties Preamble / brand term / entities register / minimal intake auto-expansion / Signal Test / footer entity derivation / Schedule 1 from YAML / Phase 7.5 enforcement / two-pass review / hybrid override-reason / R-23 pillar diagnostic / sentence-boundary `[TBC]` / `--migrate-check`) with "where it lives / introduced in / opt-in" columns
- New section: **QA Linter Rules (R-1 → R-28) — coverage by type** — full catalogue table with severity / scope / version / notes

### Changed — SOP.md
- "v3.2 (v1.0 for SS/EP)" → "v3.5 engine (v1.0 for SS/EP)"
- "Requesting a Colocation LOI (v3.3 flow)" → "(v3.5 flow)"
- Recital A variant legacy-keys note added (v3.4 collapsed 3 variants to single canonical body + 5 tails; legacy keys accepted for backward-compat)
- "What Claude will NOT do" section expanded with v3.4/v3.5.2/v3.5.6 anti-patterns (fabrication, inline citations, vanity financials, sig-block `[TBC]`) cross-referenced to R-23/R-24/R-25/R-27 + Signal Test writer discipline
- New section: **Phase 7.5 — Mandatory legal-counsel two-pass review** (v3.4 + v3.5.6) — full workflow + enforcement opt-in + hash-bound sentinel
- New section: **CLI reference** — exhaustive command list (standard run / `--migrate-check` / `--override` with hybrid reason formats / `--enforce-phase-7-5` / `--phase-7-5-pass`) + exit codes
- "Questions?" section: single-line reference expanded to full skill-directory table with per-file purpose (SKILL.md / ASSEMBLY_GUIDE / FEATURE_MATRIX / CHANGELOG / PRINCIPLES / jonathan-memo delivery map / entities register / Recital A library / framework / QA gate / junior + senior review callees / regression fixtures)

### Verified
- 139/139 pytest tests pass in both repos (no code change)
- All 10 intakes regenerate with QA PASS (6 examples + 4 regression fixtures)
- Sibling docs pass staleness scan: zero remaining `the Provider` / `purpose-built` in active prose; zero stale `v3.2` / `v3.3` active version references; Phase 7.5 / Signal Test / Parties Preamble / entities register all surfaced consistently across all three files

### Not in scope (deferred by design)
- **Tripwire implementations** for PRINCIPLES.md #1 (mirror-hash pre-commit), #4 (branch-specific tests), #5 (golden-file integration), #6 (visual-layout tests), #12 (structural-shape linter for intakes) — carry to v3.6.
- **HoT stream documentation** (DE Site HoT §12 in ASSEMBLY_GUIDE) — v3.5.x did not touch HoT; left unchanged.

---

## v3.5.6 scope G + G-bis — 2026-04-17

Phase 7.5 fail-closed enforcement (Scope G) + senior-counsel refinement pass (Scope G-bis, added during execution per user request). Three design decisions from `~/.claude/plans/v3.5.6-design-decisions.md` plus the senior-pass addition.

### G.1 — sentinel file with SHA-256 hash
- `_write_phase_7_5_sentinel(docx_path)` writes `<docx>.phase_7_5_required` with SHA-256 of the .docx, ISO timestamp, and a HOW TO RESOLVE block naming both callee workflows (junior + senior).
- `_consume_phase_7_5_sentinel(docx_path)` verifies hash matches current .docx, then consumes. Prevents replay (consumption) + post-approval tampering (hash check).
- Helpers: `_docx_sha256()`, `_phase_7_5_sentinel_path()`.

### G.2 — opt-in: CLI flag OR env var
- `_phase_7_5_enforce_enabled()` checks `--enforce-phase-7-5` OR `DE_LOI_ENFORCE_PHASE_7_5=1/true/yes/on`. Either activates.
- Default fail-open preserves v3.5.x behaviour.

### G.3 — exit code 3
- Distinct from 1 (validation) and 2 (QA FAIL). Self-documenting HOW TO RESOLVE prints on activation.

### G-bis — senior-counsel refinement pass (new file)
- `legal-counsel/specializations/contract-review/loi-senior-review-pass.md` created. Six-axis senior review (commercial posture, precedent consistency, counterparty-reading, Signal-Test deep check, identity/execution hygiene, deliverability/aftermath) reviewing the junior 4-point envelope. Verdict-reconciliation table governs how the senior upgrades/downgrades/consolidates the junior's output. The senior's envelope is the **final** envelope `legal-assistant` consumes.
- Junior workflow (`loi-review-workflow.md`) updated with two-pass framing.
- `legal-counsel/SKILL.md` router row names both files.
- `legal-assistant/SKILL.md` Phase 7.5 section carries the two-pass callout and the v3.5.6 enforcement opt-in documentation.

### Added
- `colocation/tests/test_v3_5_6_scope_g.py` — 19 new tests
- **Total: 139 pytest tests all passing**

### Verified
- 139/139 tests pass both repos
- All 10 intakes regenerate QA PASS under default fail-open
- Enforcement end-to-end: first-run exit 3 + sentinel write; --phase-7-5-pass exit 0 + sentinel consumed

---

## v3.5.6 scope D — 2026-04-17

R-23 fabrication-gate upgrades per v3.5.6 design decisions (`~/.claude/plans/v3.5.6-design-decisions.md`). Three sub-decisions implemented:

### D.1 — permissive any-pillar match with attribution diagnostic
- Don't tighten the gate; tighten the signal. R-23 still passes if ANY pillar has URLs (v3.5.x behaviour preserved).
- New: QA report emits `[INFO] R-23 attribution diagnostic` line on PASS naming which pillar matched each claim (or `TBC-covered` for sentence-scoped `[TBC]` claims). Reviewer gets visibility without the gate over-rejecting.
- Module-level `_R23_PILLAR_DIAGNOSTIC` list carries (claim, pillar) tuples; `qa_lint()` renders them.

### D.2 — sentence-boundary `[TBC]` proximity
- Prior: `[TBC]` anywhere in Recital B suppressed R-23 for all claims (wildcard).
- New: `[TBC]` only covers claims in the same sentence-boundary segment. Special case: trailing-`[TBC]` covers final-segment claims (common drafting pattern).
- New helpers: `_split_recital_b_sentences()`, `_claim_is_tbc_covered()`, `_pillar_with_urls()`.

### D.3 — hybrid override-reason validation
- Prior: `--override-reason` accepted any string (even `"ok"`).
- New: `_validate_override_reason()` enforces hybrid rule — free-text ≥15 chars OR structured audit short-code `<STATUS>-<YYYY-MM-DD> <INITIALS>` (STATUS in OK/FINE/APPROVED/PREAPPROVED). Thin patterns (`ok`, `fine`, `yes`, `done`, `sure`, `good`, `n/a`, `tbd`) rejected unconditionally.
- `main()` validates before proceeding; prints both acceptable forms on rejection and exits 1.
- QA report: `[INFO] R-override meta` line logs active overrides + reason + ISO timestamp.

### Added
- `colocation/tests/test_v3_5_6_scope_d.py` — 40 new unit tests. **Total: 160 tests all passing.**

### Verified
- 160/160 tests pass both repos
- All 10 intakes regenerate QA PASS
- CLI smoke verified: thin reason rejected; verbose + structured short-code both accepted

---

## v3.5.6 scope I — 2026-04-17

Framework worked-examples tier-1 / tier-2 URL re-verification. Documentation-only change; no code change; all 120 pytest tests remain passing.

### Changed
- `_shared/counterpart-description-framework.md` Worked Examples section: re-fetched every tier-1 / tier-2 URL across the four verified counterparties (Polarise, Civo, InfraPartners, SAG/Man of Solutions) on 2026-04-17.
- Added a v3.5.6 verification-status table at the top of the Worked Examples section.
- **Polarise Pillar 1**: companyhouse.de 403 → online-handelsregister.de HRB 17714 canonical; added polarise.eu/imprint.
- **Polarise Pillar 3**: /newsroom deep-link 404 → newsroom index; swi.com → swi.com/announcements/.
- **Polarise Pillar 5**: /sites/augsburg 404 → /newsroom.
- **InfraPartners Pillar 2 + 3**: GlobeNewswire + Nscale shorthand paths → canonical full URLs.
- **SAG Pillar 3**: /partners + /geography 404 → root (single-page site).
- **Civo**: all URLs unchanged.

### Material-fact surfaces
- Polarise HRB 17714 Paderborn now framework-anchored; retires the `[Companyhouse.de placeholder]` pattern.
- No claim text corrections required.

### Verified
- 120/120 pytest tests pass (no code change).
- 19 URLs re-verified: 10 unchanged, 8 updated, 0 blocked, 0 pillar_4 (inferred).
- No counterparty has all tier-1 sources gated.

---

## v3.5.3-cont — 2026-04-17

Continuation of v3.5.3 — implements the scopes that v3.5.3 deferred because they needed v3.5.2-context to be landed first. Six of the nine originally-deferred scopes ship here (F / J12 / E / J8 / J9 / H); three (D / G / I) remain deferred pending explicit design decisions documented below.

### Added
- **Scope H — tier-2 qualifier worked-example pattern** in `_shared/counterpart-description-framework.md`. Documents the prose form ("as publicly reported by [Publisher]" / "according to [Publisher]" / "reportedly (as reported by [Publisher])"), the YAML dict-form `source_map` schema (`tier: 2` + `qualifier` fields alongside tier-1 URLs), and the rule that tier-2-only claims without tier-1 corroboration must be omitted. Reference pattern only (no live counterparty — inventing one would introduce fabrication risk).
- **30 new unit tests** in `colocation/tests/test_v3_5_3_cont.py` (6 for Scope F + 5 for J12 + 8 for E + 4 for J9 + 3 for J8 + 4 for H). **Total: 120 pytest tests all passing.**

### Changed
- **Scope F — Recital B multi-paragraph extraction** (`qa_lint()`): prior regex stopped at `\n\n`. Legitimate multi-paragraph Recital B (consortium / holdco-subsidiary disclosure) was partially scanned. New regex extracts until `(C)` / `(D)` / `\n## ` / EOF.
- **Scope J12 — type_defaults auto-expansion** (`expand_provider_from_register()`): `config/entities.yaml::type_defaults` now wired. Minimal intake (no explicit identity fields) → auto-populates from per-type default; backward-compat preserved for explicit-fields intakes.
- **Scope E — R-22 regex narrowing + allowlist comment**: prior patterns caught bare phrases (`Provider's ability to`, `will require the exchange of`) that legitimately appear in operative clauses. Narrowed to meta-commentary verb contexts only. Allowlist comment documents known-legitimate non-firing phrases.
- **Scope J8 — Phase 6 full Recital B** (`SKILL.md`): prior prompt truncated Recital B to 60 chars — user couldn't audit inline citations / `[TBC]` markers. New prompt surfaces full paragraph verbatim + word/sentence count + full source_map pillars.
- **Scope J9 — Phase 5 redraft-as-first-class** (`SKILL.md`): three-option prompt replaces "Accept, or request edits?" binary. (a) Accept; (b) Redraft with notes; (c) Paste replacement text — R-24/R-25/R-27/R-28 run against the paste before confirmation.

### Deferred (need design decision before implementation)
- **Scope D** — R-23 pillar-specific granularity + override reason validation. Open: claim→pillar heuristic completeness; `[TBC]` proximity-window definition (char vs sentence-boundary); override reason threshold.
- **Scope G** — Phase 7.5 fail-closed code-level spec. Open: sentinel-file replay behaviour; opt-in mechanism (env var vs flag); exit code.
- **Scope I** — Framework worked-examples direct WebFetch re-verification. Needs allocated time + retry budget for JS-gated URLs (polarise.com still gated per v3.5.5 attempts).

### Verified
- 120/120 pytest tests pass in both repos
- All 10 intakes regenerate with QA PASS (6 examples + 4 regression fixtures)
- R-22 false-positive fix: `"Digital Energy's ability to deliver the Services"` no longer fires; `"...ability to secure financing"` still fires
- J12 backward-compat: explicit-fields intakes unchanged; minimal intakes auto-expand

---

## v3.5.5 — 2026-04-17

Regression fixture completion + Polarise tier-1 re-verification + **engineering principles doc** + Parties Preamble spacing fix. Sibling-docs sync (~51 edits) remains deferred.

### Added
- **`colocation/regression/v3.5/infrapartners_supplier_intake.yaml`** — 4th regression fixture. Tier-1 verified: Nscale Glomfjord 60 MW partnership (nscale.com 25 Mar 2025); Caddis Cloud Solutions 100+ MW EMEA+NA pipeline (GlobeNewswire 5 Mar 2025); CEO Michalis Grigoratos. v3.4 correction applied (no "90-day RFS", no unqualified "80% off-site").
- **`docs/PRINCIPLES.md`** — 12 engineering principles for the skill with per-principle tripwires. Written in response to the "house of cards" observation — codifies the rules that prevent the recurring failure modes seen across v3.4 → v3.5.5. Status table of tripwires: 5 implemented, 3 partial, 4 pending (v3.6 target).

### Changed
- **`polarise_wholesale_intake.yaml`** tier-1 upgraded:
  - Legal name `"Polarise GmbH"` → `"Polarise. GmbH"` (verified via Handelsregister)
  - `reg_type` `"Handelsregister"` → `"HRB (Amtsgericht Paderborn)"`, `reg_number` `"[TBC]"` → `"17714"`
  - Signatory pool documented: Michel Boutouil or Tirat Demir (Geschäftsführer Einzelvertretung)
  - `source_map.pillar_1` now cites online-handelsregister.de (tier-1 official registry)
  - `source_map.pillar_2` + `pillar_3` cite swi.com direct investor release (tier-1; Deutsche Telekom + NVIDIA Cloud Preferred Partner status confirmed)
  - `pillar_5` remains `[TBC]` — polarise.com JS-gated across 5 paths
- **Parties Preamble spacing fix** (v3.5.2 Scope A''' follow-up): prior implementation used explicit `self.p("")` blank paragraphs between party blocks, doubling vertical gap. Now uses `space_after=6` on intro + party paragraphs. Proportional to rest of body.
- **`README.md`** updated to list 4 fixtures with per-fixture verification status

### Corporate-structure finding (Polarise)
Handelsregister lookup confirmed Polarise is legally **three GmbHs**:
- `Polarise. GmbH` (Paderborn, HRB 17714) — holdco; v3.5 regression fixture counterparty
- `Polarise MUC DC GmbH` — Munich facility operator
- `Polarise AUG DC GmbH` (Düsseldorf, HRB 112190) — Augsburg facility operator
- Holdco founded 6 Mar 2025; Geschäftsführer Michel Boutouil + Tirat Demir

### Scope deferred to v3.5.6
- **Scope B sibling docs sync** (ASSEMBLY_GUIDE / FEATURE_MATRIX / SOP, ~51 discrete edits per `~/.claude/plans/v3.5.4-sibling-docs-sync.md`). Requires focused 4h session.
- **Polish principle tripwires**: golden-file tests (principle #5), visual-layout tests (#6), mirror-hash pre-commit check (#1), structural-shape linter for intake examples (#12) — v3.6 priority.
- **Polarise.com direct tier-1** — site JS-gated; awaiting future access.
- **InfraPartners jurisdiction / reg_number** — US LLC State-level lookup pending.

### Verified
- 90/90 pytest tests pass in both repos
- All 9 intakes regenerate with QA PASS (6 examples + 4 regression fixtures)
- Parties Preamble spacing verified: 6pt between blocks (was ~15pt); proportional to rest of body
- Polarise fixture renders HRB 17714 in Parties Preamble

---

## v3.5 (consolidated release) — 2026-04-17

Consolidation of v3.5.1 + v3.5.2 + v3.5.3 + v3.5.4 into a single shippable release, plus polish items knocked out during consolidation. See per-version entries below for full scope detail; summary of v3.5 polish additions:

### v3.5 polish (added during consolidation)
- **SKILL.md Phase 7.5 → callee link** — Phase 7.5 section now explicitly points at `legal-counsel/specializations/contract-review/loi-review-workflow.md` (the Scope C callee file) so a reader of the SKILL.md Phase 7.5 section immediately knows which workflow file to load.
- **`self.provider_term`** now derives from `data["provider"]["short_name"]` with `"Digital Energy"` fallback. Was hardcoded to `"Digital Energy"`. Preserves brand when AG signs (short_name still "Digital Energy") and supports future subsidiary/JV instruments without another body-wide rename.
- **`validate()` fails fast on unknown `provider.entity` key** — e.g. `entity: "de_nnl"` (typo) now prints `ERROR: provider.entity 'de_nnl' not found in config/entities.yaml. Available keys: de_ag, de_nl` and exits 1 before rendering. Previously fell through silently to backward-compat path and the user only noticed at document-render time.
- **CI workflow** — `.github/workflows/legal-assistant-tests.yml` gates PRs on pytest (88 → 90 tests). Triggers on any PR touching `legal-assistant/**` or `_shared/counterpart-description-framework.md` or `_shared/loi-*.md` or `document-factory/generate.py`. Runs full test suite + smokes all 6 intake examples + all 3 regression fixtures.
- **`docs/jonathan-memo-v3.5-delivery-map.md`** — closes the loop on Jonathan's 2026-04-17 memo with a table mapping each J-item (E1-E7 + W1-W8 + J17-J19) to the specific v3.5.x delivery commit / PR / scope.
- **Test harness additions** — 2 new tests (v3.5 polish section in `test_v3_5_2.py`): provider_term derives from short_name; provider_term fallback when short_name missing. **Total: 90 tests, all passing.**

---

## v3.5.4 — 2026-04-17

Regression-regen anchor. Ships a reproducible Wholesale-type regression fixture for the Polarise use case that triggered the whole v3.5.x cycle, so any future v3.5.x change can be regressed against the known-good baseline. Sibling-docs-sync (Scope B) and full consolidated CHANGELOG (Scope M extension) deferred to a dedicated session — better to ship the regression anchor now than hold it behind docs.

### Added
- **Regression fixture directory**: `colocation/regression/v3.5/` with `README.md` explaining purpose, regen command, and non-goals.
- **`polarise_wholesale_intake.yaml`** — synthetic-but-realistic intake reconstructed from Jonathan's 2026-04-17 memo. Exercises:
  - v3.5.1 Scope J5 (`[TBC]` handling in counterparty sig block)
  - v3.5.1 Scope J3 (Cl. 3.4 non-numeric `expansion_mw: "to be discussed"` → fallback clause)
  - v3.5.1 Scope J1 (Cl. 3.2 rack density default — 130 kW + DLC)
  - v3.5.1 Scope N-subset (Schedule 1 `technical.gpu_platform: "NVIDIA GB200 NVL72 (2× SU, ~1,152 GPUs total)"` renders from YAML)
  - v3.5.2 Scope A''' (Parties Preamble)
  - v3.5.2 brand rename (Digital Energy throughout; no "the Provider")
  - v3.5.2 Scope 0 Signal Test: Recital B names SWI Stoneweg Icona (Euronext-listed controlling owner), Macquarie (infra-credit third-party DD), NVIDIA Cloud Partner (credentialled partnership), Deutsche Telekom Industrial AI Cloud (named marquee customer). **Zero inline citations. Zero fundraising-vanity. Augsburg forward pipeline omitted from Recital B** (fails Signal Test gate 1 — no named endorser — moved to Cl. 3 commercial context where self-reported sizing belongs).

### Scope deferred to v3.5.5 / sibling-docs session
- **L (remaining 3 fixtures)** — Cudo Compute (Wholesale), Sovereign AI Grid / Man of Solutions B.V. (Distributor Mode B), InfraPartners LLC (Strategic Supplier). Each requires tier-1 source verification + v3.4-corrected language application before fixture lands.
- **B** (sibling docs sync — ASSEMBLY_GUIDE / FEATURE_MATRIX / SOP) — 17+ discrete v3.4→v3.5 language updates across 694 lines of sibling docs. Scoped mapping doc and edit sprint carry to dedicated session.
- **M** (full consolidated CHANGELOG) — this file currently has four separate v3.5.x entries; a final consolidation pass aligning all entries with forward/backward navigation anchors carries to when all v3.5.x PRs merge.

### Verified
- Polarise regression regen: QA PASS, 0 warnings, 0 failures
- Rendered `.docx` verified end-to-end:
  - Parties Preamble renders with Polarise GmbH + `(1) Digital Energy Netherlands B.V.` + Macquarie / SWI Stoneweg named in Recital B
  - Schedule 1 renders `NVIDIA GB200 NVL72 (2× SU, ~1,152 GPUs total)` from intake YAML (not hardcoded TBC)
  - Cl. 3.4 fires non-numeric fallback for `expansion_mw: "to be discussed"`
  - Zero `[polarise.eu]` / `[swi.com]` / `[companyhouse.de]` inline citations (R-24 OK)
  - Zero `raised` / `valuation` vanity (R-25 OK)
  - Zero `the Provider` in body; `Digital Energy` appears 43× (brand rename OK)
- 88/88 pytest tests still pass

---

## v3.5.3 — 2026-04-17

Workflow + governance increment. Ships the independent portions of the v3.5.3 plan — Scope J (EP Recital D polish), Scope K (legacy YAML migration pre-flight), Scope J14 (Gmail MCP fallback), Scope J13 (Drive routing — doc-only, deferred until `artifact_storage.py` lands). Dependent scopes (D/E/F linter refinements, G Phase 7.5 fail-closed code spec, J8/J9 Phase-5/6 UX, J12 per-type defaults matrix) carry forward to v3.5.3 continuation.

### Added
- **Scope K — `--migrate-check` CLI flag** in `generate_loi.py::main()`. Inspects intake YAML for missing `counterparty.source_map` (v3.4 R-23 requirement); if absent, emits a ready-to-paste snippet with all 5 pillars marked `[TBC]`; exits 0 (non-blocking). Uses `yaml.safe_load` directly so legacy YAMLs that would fail full `validate()` can still be migration-checked. Covered by `test_v3_5_3.py::TestMigrateCheck` (3 tests).
- **Scope J14 — Gmail MCP fallback paragraph** in `SKILL.md` Phase 3: documents schema-error detection (`"False is not of type 'array'"`) and the PDF-export / thread-paste fallback. Explicit note that silent omission is NOT acceptable — email threads often carry technical commitments (GPU platform, rack density, RFS) that must reach Schedule 1.
- **Scope J13 — Drive-routing spec** in `SKILL.md` Phase 8: documents the `scripts/artifact_storage.py::upload_artifact()` integration pattern with CLAUDE.md §4 rationale. Status: deferred — script does not yet exist. Wire-up occurs when `artifact_storage.py` lands.
- **8 new unit tests** in `tests/test_v3_5_3.py` (EP Recital D polish + --migrate-check + v3.5.2 regression). Total harness: **88 tests all passing**.

### Changed
- **Scope J — EP Recital D**: `"The Parties may exchange..."` → `"The Parties will exchange..."` (consistency with other-type confidentiality framing; EP now matches EU/DS/WS/SS).

### Deferred to v3.5.3 continuation (needs v3.5.2-dependent context)
- **D**: R-23 pillar-specific granularity + override reason validation
- **E**: R-22 regex refinement (narrow to clause-context; allowlist for false positives)
- **F**: Recital B multi-paragraph extraction regex fix
- **G**: Phase 7.5 fail-closed operational spec (beyond the contract already documented in v3.5.2's `loi-review-workflow.md`)
- **J8 / J9**: Phase 6 full-Recital-B display + Phase 5 redraft-as-first-class UX
- **J12**: Per-type defaults matrix (depends on Scope Q entities register already landed in v3.5.2)
- **H / I**: Tier-2 qualifier worked examples + direct WebFetch re-verification of 4 framework examples

### Verified
- 88/88 pytest tests pass in both repos
- EP Recital D renders `"will exchange"` in generated .docx
- `--migrate-check` verified with legacy-style YAML (emits snippet) and v3.4-style YAML (reports OK)
- All 6 intake examples regenerate with QA PASS

---

## v3.5.2 — 2026-04-17

Foundations layer: the architectural scopes v3.5.1 deferred. Four big pieces — entities register, Parties Preamble + brand-name defined term, Signal Test methodology + new linter rules, legal-counsel Phase 7.5 callee — plus continued test-harness expansion.

### Added
- **Scope Q — entities register (`config/entities.yaml`)**: single source of truth for DE's legal entities. `de_nl` (Digital Energy Netherlands B.V., KvK 98580086) + `de_ag` (Digital Energy Group AG, CHE-408.639.320). Contains legal_name / short_name / abbreviation / legal_form / jurisdiction / address / reg_type / reg_number / RSIN / parent / footer_key / default signatories (pre_msa / post_msa for BV; ceo for AG) + per-type defaults matrix.
- **`load_entities_register()` + `expand_provider_from_register()`** helpers in `generate_loi.py`. Intake YAMLs can now use `provider.entity: "de_nl"` + `provider.signatory_mode: "pre_msa"` and the loader expands the full record at runtime. Explicit intake field values override register defaults (intake wins). Backward-compat with v3.5.1 explicit-fields pattern preserved.
- **Scope A''' — `parties()` method**: renders Parties Preamble legal-identification block in document body between cover page and Recital A. Pattern: `THIS LETTER OF INTENT (the "LOI") is dated [Date] and entered into between: (1) [Provider legal name], [form] incorporated under the laws of [jurisdiction], with registered office at [address] and registered with [registry] under number [reg_number] ("Digital Energy"); and (2) [Counterparty], [...] (the "[Customer/Partner/Supplier]"). (each a "Party" and together the "Parties")`. Invoked in `build()` and `_build_ep()`.
- **Scope C — legal-counsel LOI review workflow callee** (`legal-counsel/specializations/contract-review/loi-review-workflow.md`): single-phase 4-point structured review matching `legal-assistant` Phase 7.5 caller contract. Reference-only markdown (per codebase cross-skill convention — zero runtime coupling). Returns strict `PASS` / `FLAG-FOR-REVISION` / `REJECT` envelopes parseable by the caller. Fail-closed on incomplete review. `legal-counsel/SKILL.md` router updated.
- **Scope 0 — Signal Test methodology section** in `_shared/counterpart-description-framework.md`: 3-gate test (Attribution / Operational relevance / Freshness-health) supersedes v3.4 topic-based filtering. Writer discipline rule (named third parties must be tier-1-attributed before draft enters Phase 5). Fundraising-specific rule (corrects v3.4 crude exclusion — named-endorser financings pass; unattributed vanity fails). Customer / ownership specific rules.
- **Scope 0 — four new linter rules** (`generate_loi.py` `_FAIL_RULES` + `_WARN_RULES`):
  - **R-24 (fail)**: inline bracket citation in Recital B (`[polarise.eu]` pattern) — source attribution lives in YAML, never in prose
  - **R-25 (fail)**: vanity-financial pattern in Recital B (valuation-of / raised $X / generic Series-X) — does NOT match named-endorser financing like "backed by Macquarie"
  - **R-27 (fail)**: `[TBC]` rendered literally in sig-block Name/Title (`Name: [TBC]`) — must route through `_render_placeholder`
  - **R-28 (warn, count-based)**: `[TBC]` count exceeds 5 body-wide — intake likely incomplete
- **Scope T expansion** — `tests/test_v3_5_2.py` with 33 additional unit tests covering: entities-register contents, provider expansion (de_nl/de_ag + override wins + backward-compat), Parties Preamble output contract, brand rename invariants, R-24/25/27 pattern matching, and v3.5.1 regression checks. Total harness: 80 tests, all passing.

### Changed
- **Brand-name defined term — body-wide rename**: `"the Provider"` / `"The Provider"` → `"Digital Energy"` across all 99 occurrences in `generate_loi.py` (Recital A constants, type-specific tails, clause templates, meta-commentary regex). Recital A no longer opens with `'{prov} (the "Provider") develops...'`; now opens with `'{prov} develops...'`. Parties Preamble establishes `"Digital Energy"` as the defined short-name used throughout.
- **`self.party` for Strategic Supplier**: changed from `"Partner"` to `"Supplier"` — semantically correct (counterparty in SS LOI IS the supplier; DE is the buying principal).
- **Parties Preamble grammar**: `legal_form` auto-prefixed with "a" if missing article (renders as "a Besloten Vennootschap (B.V.)" when YAML has "Besloten Vennootschap (B.V.)").
- **`intake_example_wholesale.yaml`**: fleshed out Provider block with `jurisdiction`, `legal_form`, `reg_type`, `reg_number` for the explicit-fields pattern; comment block documenting both patterns (explicit + entities-register).

### Fixed
- (no corrective fixes — v3.5.2 is architectural additions; v3.5.1 shipped the correctness fixes)

### Scope still deferred (per 4-way split)
- **v3.5.3**: linter refinements D/E/F (R-22 narrow, R-23 pillar-specific, Recital B multi-paragraph extraction) + Phase 7.5 fail-closed spec (G) + J8/J9/J12/J13/J14 (workflow UX, Drive routing, Gmail fallback) + H/I/J/K (tier-2 qualifier, re-verification, EP polish, migration pre-flight). v3.5.3-prep agent has drafted the independent items.
- **v3.5.4**: Scope B (sibling docs sync — ASSEMBLY_GUIDE / FEATURE_MATRIX / SOP) + Scope L (regression regen of Cudo / SAG / InfraPartners / Polarise) + Scope M (full CHANGELOG consolidation). v3.5.4-prep agent has drafted regression intake YAMLs and sibling-docs-sync mapping.

### Verified
- 80/80 pytest unit tests pass in both repos (47 v3.5.1 + 33 v3.5.2)
- All 6 intake examples regenerate with QA PASS (0 warn, 0 fail) under v3.5.2
- Parties Preamble renders correctly between cover and Recital A (structural verify: `THIS LETTER OF INTENT` present, `(1) (2)` party enumeration present, `each a "Party"` defined-term block present)
- Brand rename end-to-end: zero `the Provider` / `The Provider` in rendered body; `Digital Energy` appears ~43× per Wholesale LOI
- Entities register backward-compat: intake YAMLs without `provider.entity` key unchanged; YAMLs with `entity: "de_nl"` expand correctly; override mechanism verified

---

## v3.5.1 — 2026-04-17

First production use of v3.4 on the Polarise Wholesale LOI (Jonathan memo 2026-04-17) surfaced 19 concrete field findings. v3.5.1 is the correctness critical-path sprint — makes the next-run LOI sendable without post-gen manual editing. Architectural scopes (entities register, full test harness, Recital B methodology rewrite, Parties Preamble + brand-name rename, legal-counsel callee, workflow UX) defer to v3.5.2 / v3.5.3 / v3.5.4 per the 4-way PR split in `plans/expressive-cooking-flamingo.md`.

### Added
- **Scope T seed**: `colocation/tests/` pytest harness with 47 unit tests for every v3.5.1 code path — `_is_tbc`, `_render_placeholder`, `_derive_footer_entity`, Cl. 3.4 numeric detection, signature-block output contract (no KvK, no "ACKNOWLEDGED AND AGREED", Place field present, placeholder helper used). Discipline rule for all subsequent PRs: no render-logic change ships without a unit test exercising the new branch.
- **`_is_tbc(value)`** static helper — detects placeholder sentinels: `None`, empty, `[TBC]`, `[TO BE CONFIRMED]`, `TBC`, `XXXXXXXX`.
- **`_render_placeholder(value, context)`** helper — context-scoped rendering; `sig_block_name` / `sig_block_title` render `____________________________` for placeholder values; `body_clause` preserves `[TBC]` as visible draft marker.
- **`_derive_footer_entity(legal_name)`** static helper — maps `provider.legal_name` to document-factory footer entity key (`"nl"` for B.V. / Netherlands; `"ag"` default).
- **Scope N-subset**: Schedule 1 now reads `schedule_1.technical.gpu_platform` / `rack_density_kw` / `cooling` / `designated_sites` from intake YAML (Wholesale + End User). Prior behaviour hardcoded `[To be confirmed]` regardless of intake content.
- **Place: field** in both provider + counterparty sig blocks (Dutch/EU execution convention, jurisdictional + eIDAS relevance).

### Changed
- **Scope A (signatory default)**: NL BV default signatory changed from `Jelmer ten Wolde` / `Chief Platform Officer` to `Carlos Reuven` / `Director` across 5 intake YAMLs + `SKILL.md:323`. Statutory capacity ("Director") — legally authoritative to bind Digital Energy Netherlands B.V. under Dutch corporate law; CEO is a functional title, not statutory.
- **Scope A'' (NL BV address + KvK)**: all 6 intake YAMLs updated from `Baarerstrasse 43, 6300 Zug, Switzerland` (the Swiss AG parent's address) to `Mijnsherenweg 33 A, 1433 AP Kudelstaart, the Netherlands` + `kvk: "98580086"` (was placeholder `"XXXXXXXX"`). Confirmed NL B.V. registered seat.
- **Scope A' (signature block cleanup)**: `DocBuilder.signature()` stripped (i) unconditional `KvK:` line (duplicate of Parties clause / cover page), (ii) `ACKNOWLEDGED AND AGREED:` header (unnecessary on bilateral instruments — signing = agreement), (iii) counterparty `{reg_type}: {reg_number}` block. Signatory `Name` and `Title` lines now route through `_render_placeholder(..., "sig_block_name"|"sig_block_title")` so `[TBC]` renders as fillable blank.
- **Scope A'''' (footer)**: `document-factory/generate.py::setup_footer` now CENTER-aligned (was default left). `generate_loi.py::_setup` derives entity from `provider.legal_name` via `_derive_footer_entity()` and passes to `setup_first_footer(entity=...)` / `setup_cont_footer(entity=...)`. Prior behaviour defaulted to `"ag"` causing BV-signed LOIs to ship with Swiss parent's entity in the footer.
- **Scope J1 (Cl. 3.2 rack density + cooling)**: Wholesale Cl. 3.2 Technical Specification default updated from `"40 kW and above"` (obsolete for AI compute) to `"approximately 130 kW and above"` + `"direct-to-chip liquid cooling (consistent with NVIDIA GB200 NVL72 and GB300 NVL72 reference architectures, which target approximately 120–140 kW per rack at full configuration)"`. Both parametrized via `commercial.rack_density_kw` + `commercial.cooling_topology` for non-GB workloads.
- **Scope J3 (Cl. 3.4 Expansion branching)**: template now detects numeric vs non-numeric `expansion_mw` values. Numeric → original sentence. Empty / `[TBC]` / `"to be discussed"` / non-numeric → fallback sentence: *"The Customer has expressed interest in future expansion beyond the initial deployment, with scale to be determined following technical scoping and subject to availability, commercial agreement, and the terms of the MSA."* Prior behaviour interpolated non-numeric values verbatim, producing ungrammatical output (*"approximately to be discussed MW IT"*).
- **Scope J7 (source_map format documentation)**: `intake_example_wholesale.yaml` updated with comment block documenting R-23 URL-list requirement + schedule_1.technical block showing GPU platform pattern.

### Fixed
- **NL B.V. LOIs no longer ship with Swiss AG address** on cover / footer (root cause: YAML defaults + footer entity default — both fixed).
- **Sig block no longer displays `Title: [TBC]`** as literal string on external-facing drafts (root cause: no placeholder hygiene — fixed via `_render_placeholder` helper).
- **Cl. 3.4 no longer produces ungrammatical output** when `expansion_mw` is non-numeric.
- **Cl. 3.2 no longer ships obsolete 40 kW rack density** for AI-compute LOIs.
- **Schedule 1 now renders GPU platform from intake** instead of hardcoded `[To be confirmed]`.

### Scope deferred to later v3.5.x PRs (per plan `expressive-cooking-flamingo.md`)
- **v3.5.2**: Scope Q (entities register — `config/entities.yaml`); full Scope T (golden-file integration tests + CI hook); Scope 0 (Recital B methodology + Signal Test + R-24/25/27/28); Scope A''' (Parties Preamble + body-wide `"the Provider"` → `"Digital Energy"` rename); Scope C (legal-counsel Phase 7.5 callee).
- **v3.5.3**: Scope D/E/F/G (linter refinements + Phase 7.5 fallback); J8/J9/J12/J13/J14 (workflow UX + Drive routing + MCP fallback); H/I/J/K (tier-2 + re-verification + EP polish + migration).
- **v3.5.4**: Scope B (sibling docs sync); Scope L (regression regen); full CHANGELOG.

### Verified
- All 6 intake example YAMLs regenerate with QA PASS, 0 warnings, 0 failures
- Rendered .docx verified: sig block clean; footer centred + NL entity; Cl. 3.2 + 3.4 correct; no `KvK:` in body; no `ACKNOWLEDGED AND AGREED` in body
- 47/47 pytest unit tests pass in both repos

---

## v3.4 — 2026-04-17

Post-v3.3-merge review surfaced five gaps. v3.4 closes all five.

### Added

- **Fabrication Gate (QA rule R-23)** — hard gate on material factual claims in Recital B. Regex targets numeric-metric patterns (MW / GW / customers / clients / sites / deployments / GPUs / operations / offices / countries / years / employees / %). Every triggered claim must be backed by (a) a tier-1 source URL in `counterparty.source_map`, (b) a `[TBC]` marker, or (c) an explicit `--source-override PILLAR_N "reason"` CLI flag. Build fails otherwise. Prevents fabrication regressions like the v3.3 InfraPartners "90-day RFS" and "80% off-site" claims that were not attributable to any tier-1 source.
- **Tier Hierarchy Policy** in `_shared/counterpart-description-framework.md` — formal definition of Tier 1 (counterparty's own site + official registry + direct-quoted press, citable without qualifier), Tier 2 (third-party financial press, citable with "as publicly reported" qualifier), Tier 3 (analyst / blog / AI-generated / unattributed, not citable). Supersedes the v3.3 "don't hallucinate" advisory with enforceable source-attribution rules.
- **QA rule R-21** (warn, body-wide): flags `"purpose-built"` and `"state-of-the-art"` marketing adjectives anywhere in the document.
- **QA rule R-22** (warn, body-wide): flags meta-commentary patterns. Catches `"Provider's ability to"`, `"depends in part on"`, `"is intended to evidence"`, `"while non-binding in its commercial terms"`, `"to support the Provider's financing"`, `"will require the exchange of"`, `"The Parties acknowledge that the Provider intends"`, `"is intended to form the basis"`.
- **`clause5_ss()` method** — Strategic Supplier gets dedicated Cl. 5 ("Supply Chain and Delivery Commitment"): 5.1 Delivery Intent (Partner reserves capacity for Provider pipeline), 5.2 Assignment (supplier-scoped, not unreasonably withheld), 5.3 Financing Continuity Acknowledgment (Partner cooperates with Provider's Financing Parties on supply confirmation for financed projects). Replaces the revenue-bankability-shaped `clause5()` that SS was inheriting from EU/DS/WS (type-mismatch: a supplier is not a revenue counterparty).
- **Phase 7.5 (mandatory `legal-counsel` handoff)** in `SKILL.md` — every LOI after automated QA passes routes through `legal-counsel` with a structured 4-point review question set: (1) clause-type appropriateness, (2) meta-commentary scan, (3) cross-clause consistency, (4) source-verification sample of 3 random material claims. `legal-counsel` returns pass / flag-for-revision / reject. Previously `legal-counsel` was mandatory only for MIA Annex B and HoT body modifications.
- **Real verified worked examples** in `counterpart-description-framework.md` — replaced synthetic v3.3 examples with four verified real counterparties: Polarise GmbH (Wholesale), Civo LTD (End User), InfraPartners LLC (Strategic Supplier, corrected), Man of Solutions B.V. / SAG Consortium (Distributor Mode B, corrected). Every example has source_map citations per pillar.
- **`counterparty.source_map` YAML schema** — dict keyed by pillar (1–5), values = list of source URLs (or `"[TBC]"` for acknowledged-unverified). Required for material-claim LOIs; enforced by R-23.
- **`--source-override` CLI flag** on generator — records override + reason in QA report for auditability.

### Changed

- **Recital A: single canonical body + 5 per-type tails** (replaces v3.3's 3-variant library). User-authored wording approved 2026-04-17:
  > "Digital Energy (the 'Provider') develops and operates Digital Energy Centers ('DECs'), distributed energy hubs for liquid-cooled AI colocation, integrating accelerated compute with heat recycling and behind-the-meter (BTM) power production, engineered as one integrated system. The Provider is building an integrated sovereign AI infrastructure platform for enterprise and institutional customers, designed for edge inference."
  Per-type tails now cover all 5 types (v3.3 had tails only for DS/SS/EP). EU + WS use "The Provider's integrated platform [verb]" subject (procurement pattern); DS / SS / EP use "The Provider [verb]" subject (relationship pattern).
- **`clause5()`** (EU/DS/WS) — Cl. 5.1 stripped of 5 meta-commentary phrases. New 5.1 reads operatively: "Project Finance Context. The Provider is developing the DEC programme under a combination of equity investment and non-recourse project finance. This LOI is binding in Clauses 5, 6, 7, and 8 to support that financing structure."
- **Recitals C/D** — 7 meta-commentary instances stripped across all 5 types. Replacement patterns: "is intended to form the basis for further..." → "precedes a [definitive agreement]"; "will require the exchange of..." → "will exchange... in connection with this LOI, and agree to binding confidentiality and non-circumvention provisions set out in Clauses 6 and 7".
- **`_SUBJECT_BY_LOI["Wholesale"]`**: "Purpose-Built AI Colocation Capacity" → "AI Colocation Capacity".
- **"purpose-built" stripped** from Cl. 1 DEC definition, Cl. 3 DS bespoke-template hint, Cl. 3.1 Wholesale indicative capacity clause.
- **"colocation" → "AI colocation"** in 2 active-clause locations (DS Cl. 3.1, WS Cl. 7.4). Definitions unchanged.
- **Cl. 4.3 Wholesale** — stripped "Provider's ability to deliver" meta-commentary.
- **QA rule R-14 scope** — broadened from "Recital B" to body-wide.

### Fixed

- **InfraPartners worked example** — fabrications removed: "Ready-for-Service within 90 days of site-preparation completion" (unsourced) and "80% off-site completion as Counterparty-asserted fact" (tier-2 only). Jurisdiction now marked `[TBC]` until counterparty confirms.
- **SAG worked example** — "centrale knooppunt" removed (not quoted from sovereignaigrid.nl). EuroHPC AI Gigafactory designation now framed as Consortium self-assertion. KVK + MD identity marked `[TBC]`.

### Deprecated

- `programme.recital_a_variant` values `"sovereignty"` and `"integration"` — accepted in YAML for backward compat but silently resolve to the single canonical body.

### Migration

Existing v3.2 / v3.3 intake YAMLs render correctly without modification for Recital A. Will **fail R-23 at build time** if Recital B contains numeric-metric claims (regex-matched) but no `counterparty.source_map`. Fix: add `counterparty.source_map` with tier-1 URLs per pillar, or mark claims `[TBC]`, or pass `--source-override` at generation.

### Verified

- All 6 intake examples regenerate with QA PASS.
- Body audit across all 6 produced .docx: zero hits on 9 v3.4 anti-patterns.
- Body audit confirms all 4 v3.4 mandatory phrases present in Recital A.
- SS Cl. 5 = "Supply Chain and Delivery Commitment", zero Revenue Bankability.
- WS subject = "AI Colocation Capacity".

### Ships as

- `carlos-ecodigital/skills` PR #7 (branch `legal-assistant-loi-v3.4`)
- `EcoDigital-Software/degitos-staging` PR #46 (branch `de-legal-assistant-v3.4`, mirror with `document-factory` → `de-document-factory` path transform)

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
