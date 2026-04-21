# legal-assistant — Feature Matrix

This matrix compares document types across both streams:

- **Colocation Stream** — LOI/NCNDA v3.5 (5 sub-types). Sections below.
- **Site Sourcing Stream** — DE Site HoT v1.0. Final section.

## Clause Structure — Colocation LOI by Type

| Clause | End User (EU) | Distributor (DS) | Wholesale (WS) | Strategic Supplier (SS) | Ecosystem Partnership (EP) |
|--------|:---:|:---:|:---:|:---:|:---:|
| **Parties Preamble** (v3.5.2) | Legal identification block | Same | Same | Same | Same |
| **Recital A** | v3.4 single canonical body + EU tail | + DS tail | + WS tail | + SS tail | + EP tail |
| **Recital B** | Signal Test 3-gate (EU-tuned, v3.5.2) | 3-gate (DS-tuned) | 3-gate (WS-tuned) | 3-gate (SS-tuned) | 3-gate (EP-tuned) |
| **Cl. 1 Definitions** | 10 terms | 17 terms (+PBI, +AC, +Competitor, +Site ID, +SOF, +Transaction) | 15 terms (+AC, +Site ID, +SOF, +Services) | 13 terms (+AC, +Site ID, +Framework Agreement, optional +PBI) | 3 terms (CI, Collaboration, Representatives) |
| **Cl. 2 Purpose and Scope** | Standard | Standard | Standard | Standard (supply framing) | Non-commercial framing |
| **Cl. 3 Commercial / Scope** | Service Requirements | Partnership and Combined Offering | Indicative Capacity + Commercial Terms | Partnership Scope (purpose-driven) | Collaboration Scope |
| **Cl. 4 Next Steps / Structure** | Next Steps (simple) | Relationship Structure + Protection | Relationship Structure + Contractual Sequence | Pipeline Engagement + Contractual Sequence | Announcements and Branding |
| **Cl. 5** | Project Finance (lighter) | Project Finance | Project Finance (heaviest) | **Supply Chain and Delivery Commitment** (v3.4 — NOT revenue bankability) | **N/A — IP and Deliverables** (not Cl. 5 Finance) |
| **Cl. 6 Confidentiality** | Tier A (8 clauses) | Tier B (16 clauses) | Tier B (16 clauses) | Tier B (16 clauses) | Tier A (7 clauses, mutual; "will exchange" per v3.5.3 Scope J) |
| **Cl. 7 Non-Circumvention** | **OMITTED** | **FULL** (24mo, PBI 10yr) | **LIGHT** (supply-side only) | **LIGHT** (supply-side only) | **OMITTED** |
| **Cl. 8 / 7 General** | Cl. 7 (9 sub) | Cl. 8 (10 sub) | Cl. 8 (10 sub) | Cl. 8 (10 sub) | Cl. 7 (11 sub, non-commercial) |
| **Schedule 1** | Service Requirements (`schedule_1.technical.gpu_platform` from YAML, v3.5.1) | Partnership Details | **Capacity + Technical** (MW IT; `technical.gpu_platform` + `rack_density_kw` + `cooling` from YAML) | Scope and Capability Matrix | Joint Activity Plan (optional) |
| **Page count** | ~4 | ~7-8 | ~6-7 | ~7-8 (once fully wired) | ~4-5 |

**Commonalities across all 5 types (v3.5 state):**

- **v3.2**: library-sourced Recital A; no "DEC Block" in customer-facing text (SS/EP never use); no "minimum 5 years" (indicative language instead); no Unicode arrows in Cl. 4.2 (prose + numbered list); no "(NON-BINDING)" suffix in headings or schedule titles (italic prefatory note instead); single-sentence default closing with linter-checked bespoke override.
- **v3.4**: Recital A collapsed to single canonical body + 5 type-specific tails (3-variant library removed); meta-commentary stripped from Recital C/D + Cl. 5.1; SS Cl. 5 split into supply-chain framing; R-21/R-22/R-23 linter rules; source-attribution framework + `counterparty.source_map` field; Phase 7.5 `legal-counsel` review gate.
- **v3.5.1**: sig block cleaned (no KvK, no "ACKNOWLEDGED AND AGREED", [TBC] → fillable blanks; Place: field added per Dutch/EU execution convention); footer centre-aligned + entity derived from `provider.legal_name` (BV → nl, AG → ag); Cl. 3.2 rack density 40 → 130 kW default + DLC (GB-class reference); Cl. 3.4 expansion_mw template branches on non-numeric.
- **v3.5.2**: **Parties Preamble** in body between cover and Recital A; brand-name defined term `"Digital Energy"` (replaced `"the Provider"` 99×); Signal Test 3-gate methodology governs Recital B; R-24 (inline citations fail), R-25 (vanity-financial fail), R-27 (sig-block [TBC] fail), R-28 ([TBC] density warn); `config/entities.yaml` entities register; legal-counsel LOI review callee.
- **v3.5.3-cont**: Recital B multi-paragraph extraction; `type_defaults` auto-expansion (minimal intake → NL BV + Carlos/Director); R-22 narrowed; Phase 5/6 UX.
- **v3.5.6**: R-23 pillar diagnostic (permissive, names pillar attribution in QA report); sentence-boundary `[TBC]` proximity; hybrid override-reason (≥15 chars OR structured audit short-code); Phase 7.5 fail-closed enforcement (opt-in) + senior-counsel refinement pass (six-axis review, produces final envelope).

---

## Conditional Blocks by Type

| Conditional | End User | Distributor | Wholesale |
|-------------|:---:|:---:|:---:|
| IF: PRICING / NO_PRICING | Yes | Yes | Yes |
| IF: PHASING | No | No | Yes |
| IF: EXCLUSIVITY | No | Yes | No |
| ALT-A / ALT-B (NDA) | Yes | Yes | Yes |
| Service type selector | Yes (BM/Shared/Tokens) | No | No |
| Bespoke Cl. 3 narrative | No | **Yes** | No |
| MODE A / MODE B | No | **Yes** (Combined / Referral) | No |

---

## Distributor Mode A vs Mode B

| Feature | Mode A (Combined Offering) | Mode B (Introduction/Referral) |
|---------|:---:|:---:|
| Cl. 3.2 variant | Joint service delivery | Referral arrangement |
| Partner delivers services | **Yes** | No |
| Partner service scope defined | **Yes** ([PARTNER_SERVICE_SCOPE]) | No |
| Fee economics in LOI | Indicative partner rate | **Separate** Commercial Introduction Agreement |
| Governance (Cl. 4.4) | Joint steering committee | Simplified or omitted |
| Schedule 1 detail | Full partnership roadmap | Simplified (target segments, milestones only) |
| Companion agreement | None at LOI stage | Commercial Introduction Agreement (DE-CIA-COM) |

---

## Companion: Master Introduction Agreement (DE-MIA — separate workstream)

One agreement, two severable annexes:

| Component | Scope | Activated when |
|---|---|---|
| **Master Framework** | Parties, confidentiality, non-circumvention, term, governing law, severability | Always |
| **Annex A: Commercial** | Customer introductions. Residual % MRR (tiered) or one-time flat. | Partner introduces customers |
| **Annex B: Capital** | Investor introductions. **Capped %** (2% of Capital Committed, EUR 250k cap per intro). Named investor list (on-demand). Strict activity limitations. Regulatory representations. Auto-suspension clause. Enhanced severability. | Partner introduces investors |

Either or both annexes can be activated. Annex B is designed to stay outside the AFM/FCA/SEC regulatory perimeter through strict activity limitations, prohibition on solicitation/advice, and automatic suspension on regulatory change.

If signed alongside a Distributor LOI: LOI's confidentiality covers both. If standalone: MIA has its own embedded confidentiality.

**Status:** Built v1.0 on 2026-04-13. Engine at `mia/generate_mia.py`; templates at `mia/templates/`; intake examples at `mia/examples/`; operator guide at `mia/MIA_ASSEMBLY_GUIDE.md`. Annex B MUST route through `legal-counsel` skill before first execution. Tail period harmonised at 12 months. Defensive pipeline carve-out replaces upfront exclusion list.

---

## Protection Features by Type

| Feature | End User | Distributor | Wholesale |
|---------|:---:|:---:|:---:|
| Confidentiality (basic) | Yes | Yes | Yes |
| Purpose limitation | ALT-B only | Yes | Yes |
| Onward-sharing controls | No | Yes | Yes |
| Compliance confirmation | No | Yes | Yes |
| Breach notification (72hr) | No | Yes | Yes |
| Metadata protection | No | Yes | Yes |
| "As is" disclaimer | No | Yes | Yes |
| Non-circumvention | **No** | **Full** | **Light** |
| PBI anti-replication (10yr) | No | **Yes** | No |
| Change of control | No | **Yes** | No |
| Associated Counterparties | No | Yes (incl. EPCs, gov agencies) | Yes (excl. gov agencies) |
| Deemed introduction | No | Yes | Yes |
| Independent knowledge exception | No | Yes | Yes |

---

## Project Finance Features by Type

| Feature | End User | Distributor | Wholesale | Strategic Supplier | Ecosystem Partnership |
|---------|:---:|:---:|:---:|:---:|:---:|
| Revenue bankability signal (Cl. 5.1) | Yes | Yes | Yes | **N/A — supply-side bankability** (v3.4) | **N/A — no Cl. 5 Finance** |
| Assignment carve-out (Cl. 5.2) | Yes | Yes | Yes | Yes (supplier continuity) | N/A |
| Lender acknowledgment (Cl. 5.3) | Yes | Yes | Yes | Financing continuity (v3.4 SS Cl. 5.3) | N/A |
| Revenue chain articulation (Cl. 4.2) | No | No | **Yes** | No | No |
| Direct agreement willingness (Cl. 4.3) | No | No | **Yes** | No | No |
| Take-or-pay signal (Cl. 3.6) | No | No | **Yes** | No | No |
| Credit assessment (Cl. 3.7) | No | No | **Yes** | No | No |

---

## Commercial Features by Type

| Feature | End User | Distributor | Wholesale | Strategic Supplier | Ecosystem Partnership |
|---------|:---:|:---:|:---:|:---:|:---:|
| Capacity in **MW IT** (v3.2 — DEC Blocks deprecated) | Optional | Via partner estimate | **Yes** (`commercial.indicative_mw` required) | N/A (supply-side, not capacity-bought) | N/A |
| Service type selector (BM/Shared/Tokens) | **Yes** | No | No | No | No |
| Partnership type (bespoke) | No | **Yes** | No | No | No |
| Deployment phasing | No | No | **Yes** | No | No |
| Expansion rights | No | No | **Yes** (v3.5.1 J3 — branches on numeric vs non-numeric `expansion_mw`) | No | No |
| Minimum term signal | Yes | No | **Yes** | No | No |
| Indicative pricing table | Yes | Yes | **Yes** (detailed) | N/A | No |
| Implementation milestones | Yes (Cl. 4) | Yes (Cl. 4.5) | **Yes** (Cl. 4.5 + Sch. 1) | Yes (pipeline-engagement framing) | Optional joint-activity plan |
| Non-exclusivity / preferred partner | No | **Yes** (conditional) | No | **Yes** (supplier continuity) | N/A |
| Governance mechanism | No | Yes (Cl. 4.4) | No | No | **Yes** (Cl. 4 Announcements + Branding) |

---

## Audience Framing by Type

| Dimension | End User | Distributor | Wholesale |
|-----------|----------|-------------|-----------|
| **Recital A framing** | Service delivery, sovereignty, multi-model access | Platform reach, channel partnership | Scale programme, energy security, speed to market |
| **Subject line** | "AI Compute Infrastructure Services" | "Strategic Infrastructure Partnership" | "Purpose-Built AI Colocation Capacity" |
| **Counterparty term** | "Customer" | "Partner" | "Customer" |
| **Decision-maker** | CTO, VP Infrastructure | CEO, BD Lead | Founder, CFO, VP Operations |
| **Closing line** | "We look forward to working with you." | "We look forward to working with you." | "We look forward to working with you." |

---

## v3.5.x Feature Additions — Cross-Type

Features introduced across v3.5.x; not type-specific.

| Feature | Where it lives | Introduced | Opt-in? |
|---|---|---|---|
| **Parties Preamble** (legal identification in body) | `parties()` method in `generate_loi.py`; rendered between cover and Recital A for all 5 types | v3.5.2 Scope A''' | No — applied unconditionally |
| **Brand-name defined term** (`"Digital Energy"` replaces `"the Provider"` 99×) | All clause templates + Recital A constants | v3.5.2 | No — body-wide rename |
| **Entities register** (`config/entities.yaml` with `de_nl` + `de_ag`) | Referenced via `provider.entity: "de_nl"` + `signatory_mode: "pre_msa"` in intake YAMLs | v3.5.2 Scope Q | Optional — explicit-fields intakes still supported |
| **Minimal intake auto-expansion** (`type: Wholesale` alone → NL BV + Carlos/Director via `type_defaults`) | `expand_provider_from_register()` | v3.5.3-cont J12 | Optional — only fires when no explicit identity fields |
| **Signal Test 3-gate methodology** (Attribution / Operational relevance / Freshness) | `_shared/counterpart-description-framework.md` | v3.5.2 Scope 0 | No — governs all Recital B drafts |
| **Footer entity derivation** (BV → nl, AG → ag from `provider.legal_name`) | `_derive_footer_entity()` + `_setup()` | v3.5.1 Scope A'''' | No — fixes v3.5.0 BV-shipping-AG-footer bug |
| **Schedule 1 technical parameters from YAML** (`gpu_platform` / `rack_density_kw` / `cooling`) | `schedule()` method (WS + EU branches) | v3.5.1 Scope N-subset | Optional fields — defaults to placeholders if absent |
| **Phase 7.5 fail-closed enforcement** | `_phase_7_5_enforce_enabled()` + sentinel file + `--phase-7-5-pass` consume | v3.5.6 Scope G | Opt-in via `--enforce-phase-7-5` flag OR `DE_LOI_ENFORCE_PHASE_7_5=1` env var. Default fail-open preserves v3.5.x behaviour. |
| **Two-pass review** (junior 4-point + senior six-axis refinement) | `legal-counsel/specializations/contract-review/loi-review-workflow.md` + `loi-senior-review-pass.md` | v3.5.6 Scope G-bis | No — both passes run when Phase 7.5 is invoked |
| **Hybrid `--override-reason` validation** (≥15 chars OR structured audit short-code; thin patterns rejected) | `_validate_override_reason()` | v3.5.6 Scope D.3 | No — enforced whenever `--override` is used |
| **R-23 pillar attribution diagnostic** (PASS path emits which pillar matched each claim) | `qa_lint()` + `_R23_PILLAR_DIAGNOSTIC` | v3.5.6 Scope D.1 | No — always-on diagnostic in QA report |
| **Sentence-boundary `[TBC]` proximity** (replaces v3.5.x wildcard) | `_claim_is_tbc_covered()` with `_split_recital_b_sentences()` | v3.5.6 Scope D.2 | No — tightens R-23 attribution rigor |
| **`--migrate-check` CLI flag** (legacy v3.3 YAML inspector, non-blocking) | `_migrate_check()` | v3.5.3 Scope K | Optional CLI usage |

---

## QA Linter Rules (R-1 → R-28) — coverage by type

All 5 types run the same linter; rule applicability varies by clause scope. Every rule is evaluated on every rendered doc.

| Rule | Severity | Scope | Introduced | Notes |
|---|---|---|---|---|
| R-1 | FAIL | body | v3.2 | `"minimum commitment term of 5 years"` banned |
| R-2 | FAIL | Recital A | v3.2 | Fixed site-count language |
| R-3 | FAIL | Recital A | v3.2 | `"12 months of commercial commitment"` banned |
| R-5 | FAIL | closing | v3.2 | `"We are confident that"` banned |
| R-7 | FAIL | body | v3.2 | Unicode arrows detected |
| R-8 | FAIL | schedule-title | v3.2 | `"(NON-BINDING)"` in schedule title |
| R-10 | FAIL | Cl. 4.2 | v3.2 | Heading must be `"Contractual Sequence"`, not `"Revenue Chain"` |
| R-11 | WARN | Recital B | v3.2 | ISO certification reference |
| R-14 | WARN | body | v3.2 (scope broadened v3.4) | Salesy adjectives (`leading` / `innovative` / `world-class`) |
| R-15 | WARN | body | v3.2 | `"positioning (its|itself) as"` formulaic |
| R-17 | INFO | YAML | v3.2 | No `bespoke_closing` — default closing used |
| R-18 | FAIL | intake | v3.2 | Deprecated `commercial.dec_block_count` |
| R-19 | WARN | heading | v3.2 | `"(NON-BINDING)"` in clause heading |
| R-20 | FAIL | Recital A | v3.2 | `"programme spans N..."` language |
| R-21 | WARN | body | v3.4 | `"purpose-built"` / `"state-of-the-art"` marketing adjectives |
| R-22 | WARN | body | v3.4 (narrowed v3.5.3-cont E) | Meta-commentary patterns (narrowed to verb-context) |
| R-23 | FAIL | Recital B | v3.4 (refined v3.5.6 D) | Fabrication gate — permissive any-pillar URL match, sentence-scoped `[TBC]`, attribution diagnostic on PASS |
| R-24 | FAIL | Recital B | v3.5.2 | Inline bracket citation in `counterparty.description` |
| R-25 | FAIL | Recital B | v3.5.2 | Vanity-financial pattern (valuation / generic VC label / unattributed raise). Named-endorser financing allowed. |
| R-27 | FAIL | sig-block | v3.5.2 | `[TBC]` rendered literally in Name / Title |
| R-28 | WARN | body | v3.5.2 | `[TBC]` density count > 5 body-wide |

---

## Site Sourcing Stream — DE Site HoT v1.0

| Dimension | DE Site HoT |
|---|---|
| **Counterparty** | Dutch greenhouse grower (B.V., V.O.F., C.V., N.V., Coöperatie U.A.) |
| **Structure** | Two-part: locked bilingual Body (EN/NL, never modified) + populated Annex A (form-filled) |
| **Intake method** | 7-phase conversational (Identification → Signatory/Greenhouse → Electrical → Heat → Land → Commercial → Optional + Notices) |
| **Field count** | 58 (44 required + 12 conditional) per registry v1.1, tagged with `stage` ∈ {loi, hot, both} and `asset` ∈ enum |
| **Template version** | Body 1.0 (2026-03-13, locked bilingual); Annex A 1.0; DE-HoT-Site-v1.0 master template (1,360 lines) derived from body for LOI→HoT composition |
| **Engine** | `generate_site_hot.py` v0.1 — **LIVE** (3-pass XML form-fill; byte-exact body copy with SHA-256 verification) |
| **Validators** | KVK 8-digit, EAN `^871\d{15}$`, capacity base≤total, heat ΔT ≥15°C, co-investment ≤50%, entity suffix whitelist |
| **Conditional blocks** | Grower ≠ landowner (D.8–11, G.Landowner); mortgaged land (D.10–11, G.Financier); CHP lease (F.1a); co-investment (F.2a) |
| **Escalations** | Non-50:50 heat split → Carlos; co-investment → Jelmer; missing consent → Carlos + legal-counsel; body modification → REFUSE |
| **Policy reference** | `_shared/nda-policy-positions.md` applies to body confidentiality (Cl. 7 — not editable) |
| **Output artifacts** | `annex-a-data.json`, `DE-Site-HoT_Annex_A_{Company}.docx`, `DE-Site-HoT_Body_{Company}.docx` (copy), `intake-log.md`, `status.md` |
| **Output location** | SSOT `contracts/hots/active/{grower-slug}/` |
| **Post-gen action** | Git commit + push to SSOT (when working dir is a git checkout) |
| **Companion agreements** | None at HoT stage — future MSA/SOF are post-HoT lifecycle (see `grower-relationship-mgr`) |

## v3.7.x Extensibility Layer — Colocation LOI

Additions in v3.7.0 + v3.7.1 + v3.7.2 that extend the engine without
changing clause defaults. All fields are optional; absence preserves
v3.6.0 rendering.

| Feature | Field | Applies to | Release |
|---|---|---|---|
| **Recital B density advisory** | `choices.recital_b_density: terse\|standard\|verbose` | All types | v3.7.0 (advisory v3.7.2) |
| **Brochure source_map token** | `source_map[pillar_N]: ["internal:brochure_{YYYYMMDD}_{slug}"]` | All types | v3.7.0 |
| **Schedule 1 suppression** | `choices.include_schedule: bool` | All types (except EP) | v3.7.0 |
| **Confidentiality opt-outs** | `choices.confidentiality_opt_outs: [...]` — suppresses §6.9 / §6.10 / §6.13 with auto-renumber | Tier B types (DS / WS / SS) | v3.7.0 |
| **Structured RoFR** | `supplier.rofr: {site_scope, response_window, lock_out_style, continues_on_remaining}` — 4 lock-out styles | SS | v3.7.0 |
| **Mutual Referral Rider** | `supplier.referral_rider: bool` — §3.9 bidirectional | SS | v3.7.0 |
| **Joint Stocking Programme** | auto-fires when `supplier.lead_time_target < 6 months` — §3.10 | SS | v3.7.1 |
| **Co-Marketing parameterized** | `supplier.co_marketing: {framing, logo_use, site_naming_approval_sla, press_at_loi}` — §3.11 with 6 sub-clauses | SS | v3.7.1 |
| **Relationship cluster metadata** | `counterparty.relationship_cluster`, `counterparty.identity_map` — QA-report only, not body | All types | v3.7.0 |
| **Financing context** | `dates.financing_context: {linked_to_fundraise, fundraise_close_target, buffer_months_post_close}` | All types | v3.7.0 |
| **Inline custom definitions** | `custom.definitions: [{key, text}, ...]` — injected at top of Cl. 2 | All types | v3.7.0 |
| **Library-sourced definitions** | `custom.definitions_include: [...]` — pulls from `_shared/loi-common-defined-terms.md` | All types | v3.7.0 |
| **Custom clauses** | `custom.clauses: [{number, mode, heading, text, sub_clauses}]` — modes: `append` / `replace` / `insert-after:N` | All types | v3.7.0 (append) / v3.7.1 (replace + insert-after) |
| **Opt-in renumbering** | `choices.auto_renumber: bool` — closes N.M gaps post-build | All types | v3.7.1 |

### v3.7.x Linter additions

| Rule | Severity | Condition | Release |
|---|---|---|---|
| **R-24** (second definition) | warn | `source_map` uses brochure tokens; tier-1 corroboration still needed before signing | v3.7.0 |
| **R-29** | warn | URL content verification — fetch fails to confirm Recital B keyword; pillar downgraded to `[TBC]` + R-23 re-asserted | v3.7.0 (wired default-on v3.7.2) |
| **R-30** | fail | Double-period in rendered body (excluding ellipsis + numbered lists) | v3.7.0 |
| **R-31** | warn | `contact_name == signatory_name` — confirm intentional single-POC | v3.7.0 |
| **R-21 (narrowed)** | warn | "purpose-built" permitted in Cl. 3 product-capability; still banned in Recital A / B / closing | v3.7.0 |
| **R-density** | info | Recital B word count out of band for chosen `recital_b_density` | v3.7.2 |
| **R-lead-time** | warn | `supplier.lead_time_target` non-empty but unparseable as days/weeks/months | v3.7.2 |
| **R-custom-mut** | warn | `custom.clauses` replace/insert-after target number not found in rendered body | v3.7.2 |

### v3.7.x CLI additions

| Flag | Purpose | Release |
|---|---|---|
| `--recital-b-only <path>` | Regenerate Recital B + QA only; replace paragraph in existing .docx | v3.7.0 |
| `--audit-only` | Read `prior_loi_path`; run full linter; emit `{basename}_audit.txt` without regenerating | v3.7.0 |
| `--verify-source-urls` | Force R-29 on (redundant when default-on) | v3.7.0 |
| `--no-network` | Disable R-29 fetching (CI escape) | v3.7.2 |
| `--phase-8-auto-execute` | Flip Phase 8 dispatch from dry-run to real writes | v3.7.0 (wired v3.7.2) |
| `--phase-8-actions=a,b,c` | Select specific Phase 8 actions to run | v3.7.2 |
| `LOI_NO_NETWORK=1` (env) | Same as `--no-network` (for CI environments) | v3.7.2 |

### v3.7.x Artifacts emitted alongside .docx

| File | Content | Release |
|---|---|---|
| `{stem}_SESSION_LOG.md` | Intake decisions, CLI flags, QA summary, customization counts | v3.7.0 |
| `{stem}_AUDIT.txt` | 20+ core assertions + per-customization probes (PASS/FAIL) | v3.7.1 |
| `{stem}_PHASE8_DISPATCH.json` | Action payloads for orchestrator to invoke (MCP tools) | v3.7.2 |
| `/domains/counterparties/{slug}/overview.md` | Domain card (HubSpot/ClickUp/Drive links, relationship cluster, identity map) | v3.7.2 |

### v3.7.x Canonical examples

- `examples/intake_example_strategic_supplier_v37_full.yaml` — **kitchen sink** demonstrating every v3.7.x field in one fixture. Recommended starting point for operators adopting the extensibility layer.
- `regression/v3.7/*.yaml` — 8 retrospective-derived fixtures (Cerebro, Armada, InfraPartners, name-homonym, dual-role, dark-web, brochure, prior-LOI regen) serving as both canonical audit records and regression tests.

### Engine asymmetry (vs. Colocation LOI)

| | Colocation LOI | Site HoT |
|---|---|---|
| Intake format | YAML file | Conversational (7 phases) |
| Engine status | Deterministic Python (`sales/generate_loi.py`), shipping | Deterministic Python (`sites/hot/generate_site_hot.py` v0.1), shipping |
| Template storage | Markdown reference (not consumed by script) + Python-built .docx from scratch | Locked binary .docx, form-filled in place via zipfile + xml.etree |
| Brand layer | Via `document-factory` (cover page, headers, footers) | Self-contained (pre-formatted bilingual template) |
| Body mutability | Full (script builds from scratch) | Locked; REFUSE body modification |
| Output name pattern | `YYYYMMDD_DEG_LOI-{Type}_{Company}_(STATUS).docx` | `DE-Site-HoT_Annex_A_{Company}.docx` + body copy |
