# Changelog — legal-assistant

All notable changes to the `legal-assistant` skill.
Versioning: skill release version, not per-document template version (each template carries its own version number inside its filename).

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
