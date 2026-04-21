# legal-assistant — Assembly Guide

This guide covers two streams produced by `legal-assistant`:

- **Colocation Capacity** — LOI/NCNDA v3.0 (End User, Distributor, Wholesale). Sections 1–11 below.
- **Site Sourcing** — DE Site HoT v1.0 (grower Heads of Terms). Section 12 below.

A third, parallel stream — **Introducer Fees** (DE-MIA Master Introduction Agreement, Master + severable Annex A Commercial / Annex B Capital) — has its own operator guide at `mia/MIA_ASSEMBLY_GUIDE.md` and engine at `mia/generate_mia.py`. Not covered here. If a counterparty is an Introducer (customer or investor referrer), use that guide instead. **Annex B (capital) MUST be routed through the `legal-counsel` skill before first execution.**

Previously called `loi-generator/ASSEMBLY_GUIDE.md`.

---

## 1. LOI Type Selection (5 types, v3.5)

| If the counterparty... | Use | Template |
|---|---|---|
| Buys compute directly (enterprise, AI lab, startup) | **End User (EU)** | DE-LOI-EndUser-v3.5 |
| Packages DE capacity with their own services to sell to end users (SI, MSP, software company, sovereign AI builder) | **Distributor (DS)** | DE-LOI-Distributor-v3.5 |
| Buys capacity in bulk to resell to their own customers (neocloud, GPU cloud) | **Wholesale (WS)** | DE-LOI-Wholesale-v3.5 |
| Supplies equipment, services, or build capability (EPC, modular vendor, cooling/power OEM, key supplier) | **Strategic Supplier (SS)** | DE-LOI-SS-v1.0 |
| Ecosystem / co-positioning relationship with no commercial flow (standards body, university, research consortium, co-marketing alliance) | **Ecosystem Partnership (EP)** | DE-LOI-EP-v1.0 |

**Decision logic:**
- **If counterparty IS the end user** (buys to consume): End User.
- **If counterparty has its own end-user customers and adds value**: Distributor.
- **If counterparty resells raw capacity at scale**: Wholesale.
- **If counterparty supplies to DE** (goods/services/capability): Strategic Supplier.
- **If no commercial flow within 12 months** (co-positioning only): Ecosystem Partnership.

**Critical test for EP:** If commercial flow is contemplated, do NOT use EP. Use the commercial type that matches the direction of flow.

**Distributor vs Wholesale:** Distributors add value (integration, managed services, software). Wholesale customers resell raw capacity. The test: does the counterparty transform or bundle the capacity with their own services?

**Consortium / federation counterparty:** the coordinating entity signs. Describe it (not every member) per the consortium guidance in `_shared/counterpart-description-framework.md`.

---

## Distributor Mode Selection

The Distributor template (DE-LOI-Distributor) has two modes:

| If the partner... | Use | Cl. 3.2 variant |
|---|---|---|
| Delivers services jointly with DE to end users | **Mode A: Combined Offering** | Joint service scope, responsibility matrix |
| Introduces customers to DE but does not deliver services | **Mode B: Introduction/Referral** | Referral arrangement, fee economics in separate agreement |

**Mode B note:** When Mode B is selected, the economic terms (fees, qualifying introductions, payment schedule) are NOT in the LOI. They go in a separate **Commercial Introduction Agreement** signed alongside or after the LOI. The LOI captures the relationship intent; the fee agreement captures the economics.

---

## Strategic Supplier — Purpose Selector (v1.0)

SS intake requires **1–2** strategic purposes. Each drives which Cl. 3 / Cl. 4 sub-clauses fire in the template.

| Purpose | Cl. 3 blocks | Cl. 4 blocks | Always required YAML |
|---|---|---|---|
| `capacity_lock_in` | 3.2 Capacity Reservation, 3.3 Lead-Time Targets | optional 4.5 Exclusivity | `supplier.lead_time_target` |
| `pricing_volume` | 3.4 Pricing Framework, 3.5 Volume Tiers | — | `supplier.volume_indicative` |
| `supply_chain_de_risking` | 3.6 Dual-Source + Continuity | — | — |
| `engineering_integration` | 3.7 Design Integration + IP Allocation | 4.3 Joint-Development Governance | `choices.joint_ip` (none / background / foreground) |
| `pipeline_visibility` | 3.8 Preferred-Supplier / ROFR (20-BD window) | 4.1 Project Introduction Process | — |

**Always-on clauses** (regardless of purpose selection): Cl. 3.1 Capability Contribution; Cl. 4.2 Contractual Sequence; Cl. 4.4 Change of Control; Cl. 4.6 Implementation Roadmap; Cl. 5 Project Finance; Cl. 6 Confidentiality (Tier B); Cl. 7 Non-Circumvention (light supply-side); Cl. 8 General.

Full template: `colocation/templates/DE-LOI-StrategicSupplier-v1.0_TEMPLATE.md`.

---

## Ecosystem Partnership — Variant Guidance (v1.0)

EP has no purpose selector — the shape is fixed. Configuration via YAML:

| Field | Options | Default |
|---|---|---|
| `ecosystem.relationship_type` | standards_body / university / research_consortium / co_marketing / industry_association / policy_partner / other | — (required) |
| `ecosystem.collaboration_themes` | freeform list | — (required) |
| `ecosystem.joint_activity_categories` | publications / events / pilots / advocacy / working_groups (subset) | — (required) |
| `choices.announcement_protocol` | mutual_approval / notify_only | mutual_approval |
| `choices.logo_use` | reciprocal / one_way / none | reciprocal |
| `programme.recital_a_variant` | default (canonical, v3.4) | `default` — sovereignty/integration keys accepted but map to canonical body. Bespoke by exception only. |

Full template: `colocation/templates/DE-LOI-EcosystemPartnership-v1.0_TEMPLATE.md`.

---

## Recital A Variant Selection

Per `_shared/loi-recital-a-library.md` — same canonical body + per-type tail across all five types (v3.4).

**v3.7.0 note:** The three-variant model (default / sovereignty / integration) is deprecated. Use the single canonical body for all types. The `sovereignty` and `integration` legacy keys still resolve to the canonical body for backward compatibility — but do not prompt the operator to choose them.

| Recital A path | When to use |
|---|---|
| **Canonical body + per-type tail** (default) | All counterparties. Covers both sovereignty and integration framing — do not override to bespoke to blend them. |
| **Bespoke** (exception) | Only when (a) counterparty profile is genuinely non-commercial (sovereign regulator, academic institution), OR (b) per-type canonical tail is materially incorrect for the relationship. Requires justification in intake YAML — see Phase 5 bespoke gate. |

`bespoke` is the exception, not a blending convenience — linter-checked against R-2, R-3, R-14, R-15.

---

## Companion Agreements

The LOI system works alongside (but is separate from) two fee instruments:

| Agreement                                          | Scope                                                                              | Regulatory risk        | Relationship to LOI                                                  |
| -------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------- | -------------------------------------------------------------------- |
| **Commercial Introduction Agreement** (DE-CIA-COM) | Customer introductions — ongoing or one-off. Fee: residual % MRR or one-time flat. | Low                    | Signed alongside Distributor LOI (Mode B) or standalone. Any person can sign. |
| **Capital Introduction Agreement** (DE-CIA-CAP)    | Investor/financing introductions. Fee: % of capital committed.                     | **High** (AFM/FCA/SEC) | Always standalone. **Never** referenced in or connected to any LOI.  |

**Confidentiality dependency:** If a fee agreement is signed WITHOUT an accompanying LOI, the fee agreement must contain its own embedded confidentiality provisions. If signed alongside an LOI, the LOI's confidentiality clause covers both (the Distributor LOI's Purpose definition explicitly includes "companion agreements").

---

## Workflow

### Manual workflow (markdown template)

| Step | Action | Time |
|---|---|---|
| 1 | Select type + mode (Distributor only), open correct template, Save-As with naming convention | 1 min |
| 2 | Fill parameter table (page 1) | 5-10 min |
| 3 | **Distributor only:** Write bespoke Cl. 3.1. Choose Mode A or Mode B for Cl. 3.2. | 10-15 min |
| 4 | Choose conditional blocks (pricing, phasing, exclusivity, NDA alt, Distributor mode) — delete unused | 2-5 min |
| 5 | Find-and-replace all remaining [PLACEHOLDERS] | 2-3 min |
| 6 | Delete all shaded instruction blocks | 2 min |
| 7 | Search for `[` to verify no brackets remain | 1 min |
| 8 | Tone check: read Recital A aloud — institutional or promotional? | 2 min |
| 9 | CPO/CEO review (if required) | — |
| 10 | Export to PDF, send via DocuSign or wet signature | 2 min |

### Automated workflow (YAML intake → Python script)

| Step | Action | Time |
|---|---|---|
| 1 | Copy the example YAML file for the correct type | 1 min |
| 2 | Fill in all parameter values and choices | 5-15 min |
| 3 | Run `python generate_loi.py intake.yaml` | 10 sec |
| 4 | Review the output .docx — verify content, check formatting | 5 min |
| 5 | CPO/CEO review (if required) | — |
| 6 | Send via DocuSign or wet signature | 2 min |

**Total:** 15-30 min (Distributor), 10-20 min (Wholesale/End User).

---

## Naming Convention

**Template files:** `DE-LOI-{TYPE}-v3.0_TEMPLATE.md`

**Executed documents:** `YYYYMMDD_DEG_LOI-{TYPE}_{Counterparty Name}_(STATUS).pdf`

Status values: `DRAFT` → `SENT` → `SIGNED` → `LAPSED` → `SUPERSEDED`

Examples:
- `20260415_DEG_LOI-Wholesale_Lambda Inc_(SIGNED).pdf`
- `20260420_DEG_LOI-Distributor_FrontierOne_(SENT).pdf`
- `20260501_DEG_LOI-EndUser_Acme AI Labs_(DRAFT).pdf`

---

## Signing Entity

**Digital Energy Netherlands B.V.** signs all types by default.

- Dutch entity = jurisdictional alignment (Dutch law LOI)
- Closest to revenue-generating assets (lender-preferred)
- Clean SPV assignment chain (intra-jurisdictional)
- If credit enhancement needed: reference Digital Energy Group AG (Swiss parent) as guarantor in the credit assessment clause — not as signatory

**v3.5.1 canonical entity data** (baked into defaults; see `config/entities.yaml` from v3.5.2):

| Field | NL BV (signing) | AG (parent / guarantor ref) |
|---|---|---|
| Legal name | Digital Energy Netherlands B.V. | Digital Energy Group AG |
| Address | Mijnsherenweg 33 A, 1433 AP Kudelstaart, the Netherlands | Baarerstrasse 43, 6300 Zug, Switzerland |
| Registration | KvK 98580086 | CHE-408.639.320 |
| Jurisdiction | the Netherlands | Switzerland |
| Legal form | Besloten Vennootschap (B.V.) | Aktiengesellschaft (AG) |
| Default pre-MSA signatory | Carlos Reuven, Director | Carlos Reuven, CEO |

**v3.5.2 entities-register pattern**: intake YAMLs can reference the entity by key instead of duplicating these fields. Both patterns are supported:

```yaml
# Pattern A — explicit fields (v3.5.1-compatible):
provider:
  legal_name: "Digital Energy Netherlands B.V."
  address: "Mijnsherenweg 33 A, 1433 AP Kudelstaart, the Netherlands"
  kvk: "98580086"
  signatory_name: "Carlos Reuven"
  signatory_title: "Director"

# Pattern B — entities-register lookup (cleaner, recommended):
provider:
  entity: "de_nl"              # key in legal-assistant/config/entities.yaml
  signatory_mode: "pre_msa"    # pre_msa | post_msa (BV) | ceo (AG)

# Pattern C — v3.5.3-cont J12 minimal: just `type:` set; generator auto-fills
#           from type_defaults in config/entities.yaml
type: Wholesale
# provider: <not specified> → auto-populates de_nl + pre_msa per type_defaults matrix
```

---

## Parties Preamble (v3.5.2 Scope A''')

Prior to v3.5.2 the legal identification of both parties lived only on the **cover page**. v3.5.2 added a **Parties Preamble** block in the document body between the cover and Recital A — a lender's counsel reading the body alone can now verify both parties' legal identification without flipping back to the cover.

Rendered structurally by `parties()` method in `generate_loi.py`. Consumes `provider.legal_name / legal_form / jurisdiction / address / reg_type / reg_number` and `counterparty.name / legal_form / jurisdiction / address / reg_type / reg_number`. Output:

```
THIS LETTER OF INTENT (the "LOI") is dated [Date] and entered into between:

(1) [Provider legal name], a [legal form] incorporated under the laws of [jurisdiction],
    with registered office at [address] and registered with the [reg_type] under number
    [reg_number] ("Digital Energy"); and

(2) [Counterparty legal name], an entity incorporated under the laws of [jurisdiction],
    with registered office at [address] and registered with the [reg_type] under number
    [reg_number] (the "[Customer / Partner / Supplier]").

(each a "Party" and together the "Parties")
```

**Brand-name defined term (v3.5.2)**: Provider is defined as `"Digital Energy"` (brand name) across all 5 types — replaced prior `"the Provider"` in every clause template. Counterparty defined-term varies by type: `"the Customer"` (EU/WS), `"the Partner"` (DS/EP), `"the Supplier"` (SS).

**Spacing (v3.5.5)**: party blocks use `space_after=6` (not blank-paragraph spacers) — keeps preamble proportional to body cadence.

---

## Recital B — Signal Test methodology (v3.5.2 Scope 0) + source_map (v3.4 R-23)

Recital B is the counterparty description. It is governed by the **Signal Test 3-gate** in `_shared/counterpart-description-framework.md` (not any freeform paragraph):

1. **Gate 1 — Attribution**: named, verifiable third party whose identity a lender would recognize as operationally endorsing
2. **Gate 2 — Operational relevance**: the attached identity speaks to solvency (Q1), commercial-fit (Q2), or bankable third-party validation (Q3)
3. **Gate 3 — Freshness / Health**: attached third party is currently operational, solvent, and in an undistressed relationship (narrow — fires only when distress is operationally material; arm's-length parent distress does NOT fire)

Every material numeric claim in Recital B must be attributed in `counterparty.source_map` (R-23 fabrication gate, v3.4). **v3.5.6 Scope D** refined:

- R-23 remains **permissive any-pillar match** (don't tighten the gate; tighten the signal). QA report now emits `[INFO] R-23 attribution diagnostic` on PASS naming which pillar matched each claim (or `TBC-covered` for sentence-scoped `[TBC]`).
- `[TBC]` proximity is **sentence-boundary-scoped** (v3.5.6 D.2) — a `[TBC]` marker covers claims only in the same sentence segment. Trailing-`[TBC]` special case covers final-segment claims.

**v3.5.2 QA rules** (Phase D of methodology):
- **R-24** (fail): inline bracket citation `[polarise.eu]` in `counterparty.description` field. Source attribution lives in `source_map` YAML, NEVER in prose.
- **R-25** (fail): vanity-financial pattern (valuation numbers / generic VC labels / unattributed capital-raise). Named-endorser financing ("backed by Macquarie") is signal and remains allowed.
- **R-27** (fail): `[TBC]` rendered literally in sig-block Name or Title — routes through `_render_placeholder` instead.
- **R-28** (warn, count-based): `[TBC]` count exceeds 5 body-wide — intake likely incomplete.

**Writer discipline rule (Phase A)**: every named third party requires a tier-1 `source_map` entry before draft enters Phase 5. Brand recognition compounds fabrication cost; it does not reduce it.

See `_shared/counterpart-description-framework.md` for the full methodology + tier hierarchy policy + tier-2 qualifier pattern (v3.5.3-cont Scope H) + worked examples (Polarise / Civo / InfraPartners / SAG — v3.5.6 Scope I re-verified 2026-04-17).

---

## Phase 7.5 — Mandatory legal-counsel two-pass review (v3.4 + v3.5.6 Scope G)

Phase 7.5 sits between automated QA (Phase 7) and delivery (Phase 8). It is **non-bypassable by contract** and (from v3.5.6) **enforceable by code** when opt-in.

**Two-pass review** (v3.5.6 Scope G-bis):
1. **Junior** — `legal-counsel/specializations/contract-review/loi-review-workflow.md` — 4-point structured review (clause-type appropriateness / meta-commentary scan / cross-clause consistency / source-verification sample). Produces draft envelope `PASS` / `FLAG-FOR-REVISION` / `REJECT`.
2. **Senior** — `legal-counsel/specializations/contract-review/loi-senior-review-pass.md` — six-axis refinement pass (commercial posture & proportionality / precedent consistency / counterparty-reading / Signal-Test deep check / identity/execution hygiene / deliverability/aftermath). Reviews the junior's envelope, catches what the junior missed, **upgrades or downgrades** the verdict where warranted, produces the **final** envelope.

The senior's envelope is what `legal-assistant` consumes. The junior envelope is an intermediate artefact.

**Enforcement (v3.5.6 Scope G)** — opt-in via CLI flag `--enforce-phase-7-5` OR env var `DE_LOI_ENFORCE_PHASE_7_5=1/true/yes/on`:
1. First run: writes `<docx>.phase_7_5_required` sentinel with SHA-256 of .docx, exits **3**.
2. Operator runs the two-pass review.
3. Second run with `--phase-7-5-pass`: consumes sentinel after verifying hash matches current .docx (prevents replay + post-approval tampering); if match, proceeds to delivery (exit 0). If mismatch: exit 3 with specific diagnostic.

**Default is fail-open** (no flag / no env var): v3.5.x behaviour preserved; Phase 7.5 is social-contract only. Enforcement is recommended for production LOI runs.

---

## Default Values

| Parameter | Default | Override when |
|---|---|---|
| Confidentiality survival | 3 years | Rarely — 3yr is standard. Negotiate in 2-5yr range if counterparty pushes. |
| NC duration | 24 months | 18-36 month range acceptable per DE policy. |
| PBI survival (Distributor only) | 10 years | Defend this. 10yr reflects long development cycles. |
| LOI validity | 12 months | Shorten to 6 months if faster conversion expected. |
| Milestone gates | 30/60/90 days | Adjust per deal complexity. Large Wholesale deals may need 45/90/120. |

---

## Bespoke Language Guide (Distributor Cl. 3 only)

The Distributor template requires bespoke text in Cl. 3.1 and 3.2. Do not copy template language. Write fresh for each partner.

### Example 1: System Integrator (Mode A)

*Archetype: A company like Atos, Computacenter, or Insight — deploys and manages enterprise IT infrastructure. Has existing enterprise customers who need compute but don't want to manage facilities themselves.*

**Cl. 3.1:**
> [PARTNER_SHORT] provides AI system integration services, including the design, deployment, and management of GPU compute infrastructure for enterprise and institutional clients. Digital Energy develops and operates AI-ready Digital Energy Centers ("DECs") with secured energy and grid access, direct liquid cooling, and full energy-recovery infrastructure.
>
> The Parties intend to combine the Partner's enterprise customer relationships, solution architecture capability, and implementation expertise with Digital Energy's integrated DEC platform to deliver integrated AI infrastructure solutions — from workload assessment and hardware specification through facility deployment, system commissioning, and ongoing managed operations — as a unified end-to-end offering to enterprise and institutional end users.

**Cl. 3.2(b):**
> the Partner would contribute solution architecture and workload assessment, hardware specification and procurement, rack-level deployment and commissioning, operating system and orchestration layer configuration, application integration and performance tuning, ongoing infrastructure management including monitoring, patching, and capacity planning, and first-line technical support for end-user customers

### Example 2: Sovereign AI / Defence Partner (Mode A)

*Archetype: A company like FrontierOne, Palantir's infrastructure arm, or a national defence contractor — enables government and critical infrastructure clients to access AI compute within classification and sovereignty constraints.*

**Cl. 3.1:**
> [PARTNER_SHORT] provides sovereign AI infrastructure and security-classified computing services to government, defence, and critical national infrastructure institutions. Digital Energy develops and operates AI-ready Digital Energy Centers ("DECs") with secured energy and grid access, direct liquid cooling, and full energy-recovery infrastructure.
>
> The Parties intend to combine the Partner's security architecture capability, government procurement expertise, and institutional relationships with Digital Energy's integrated DEC platform to deliver sovereign, classification-compliant AI infrastructure — enabling government and defence end users to access high-density compute capacity within the security, provenance, and data sovereignty frameworks their mandates require.

**Cl. 3.2(b):**
> the Partner would contribute security architecture design and threat modelling, facility clearance and classification-compliant operational procedures, secure supply chain management and hardware provenance verification, government procurement navigation including tender preparation and compliance documentation, data sovereignty assurance including encryption key management and access control frameworks, and ongoing security operations including incident response and audit support

### Example 3: GPU / Hardware Solutions Provider (Mode A)

*Archetype: A company like Lambda (hardware division), Penguin Solutions, or a regional GPU reseller — procures, configures, and manages GPU hardware but doesn't operate facilities.*

**Cl. 3.1:**
> [PARTNER_SHORT] provides GPU and accelerator hardware solutions, including procurement, configuration, and lifecycle management of high-density compute infrastructure for AI workloads. Digital Energy develops and operates AI-ready Digital Energy Centers ("DECs") with secured energy and grid access, direct liquid cooling, and full energy-recovery infrastructure.
>
> The Parties intend to combine the Partner's hardware procurement capability, vendor relationships, and technical configuration expertise with Digital Energy's integrated DEC platform to deliver turnkey AI compute infrastructure — from hardware sourcing and rack integration through facility deployment and ongoing hardware lifecycle management — to enterprise, research, and neocloud customers.

**Cl. 3.2(b):**
> the Partner would contribute GPU and accelerator procurement including vendor relationship management and volume pricing negotiation, hardware configuration and validation against workload requirements, rack integration and cabling, firmware and driver lifecycle management, warranty administration and RMA coordination, and capacity planning for hardware refresh cycles

### Example 4: Managed Service Provider (Mode A)

*Archetype: A company like OVHcloud, Leaseweb, or a regional MSP — packages infrastructure as a service with platform management, billing, and customer success.*

**Cl. 3.1:**
> [PARTNER_SHORT] provides managed infrastructure services, packaging compute, storage, and networking as turnkey cloud offerings for enterprise and mid-market customers. Digital Energy develops and operates AI-ready Digital Energy Centers ("DECs") with secured energy and grid access, direct liquid cooling, and full energy-recovery infrastructure.
>
> The Parties intend to combine the Partner's service packaging capability, customer management infrastructure, and established client base with Digital Energy's integrated DEC platform to deliver managed AI compute services — enabling the Partner's customers to access sovereign, high-density GPU infrastructure through the Partner's existing service relationship and billing framework.

**Cl. 3.2(b):**
> the Partner would contribute infrastructure-as-a-service packaging including compute, storage, and networking, customer onboarding and environment provisioning, platform management including orchestration, monitoring, and autoscaling, SLA management and service reporting, billing and usage metering, and customer success management including technical account management and escalation handling

### Example 5: Software / AI Platform Company (Mode A)

*Archetype: A company like Weights & Biases, Anyscale, or a vertical AI platform — provides software that runs on GPU compute and needs infrastructure underneath.*

**Cl. 3.1:**
> [PARTNER_SHORT] develops and operates an AI [training / inference / MLOps] platform used by [enterprise / research / developer] customers to [deploy, train, and manage AI workloads at scale]. Digital Energy develops and operates AI-ready Digital Energy Centers ("DECs") with secured energy and grid access, direct liquid cooling, and full energy-recovery infrastructure.
>
> The Parties intend to combine the Partner's software platform and customer ecosystem with Digital Energy's colocation infrastructure to offer an integrated solution — enabling the Partner's customers to run their AI workloads on sovereign, AI-ready European infrastructure through the Partner's platform interface, without managing the underlying facility, hardware, or cooling systems directly.

**Cl. 3.2(b):**
> the Partner would contribute its software platform including workload submission APIs and SDKs, scheduling and resource allocation optimisation, usage tracking and billing integration, customer-facing dashboard and self-service tooling, and ongoing platform development and feature delivery

### Example 6: Referral Partner (Mode B)

*Archetype: An advisory firm, consultant, or well-connected intermediary who introduces customers but doesn't deliver services. Fee economics in a separate Referral Agreement.*

**Cl. 3.1:**
> [PARTNER_SHORT] provides [strategic advisory / technology consulting / market access] services to enterprise and institutional clients across [territory]. Digital Energy develops and operates AI-ready Digital Energy Centers ("DECs") with secured energy and grid access, direct liquid cooling, and full energy-recovery infrastructure.
>
> The Parties intend to establish a referral arrangement under which the Partner would identify and introduce qualified end-user customers to Digital Energy's integrated DEC platform, leveraging the Partner's established client relationships, domain credibility, and market presence in [territory/vertical]. The economic terms of the referral arrangement will be set out in a separate agreement between the Parties.

**Cl. 3.2 (Mode B):** Uses the standard Mode B referral text — no bespoke needed for 3.2(b).

---

## Red-Line Protocol

When a counterparty marks up the LOI, apply these postures:

| Clause | Posture | Notes |
|---|---|---|
| Cl. 1-4 (non-binding) | **Flexible** | Negotiate freely. These clauses capture intent, not obligations. |
| Cl. 5 (Project Finance) | **Defend** | Lender signals are non-negotiable. Assignment carve-out and lender acknowledgment must remain. |
| Cl. 6 (Confidentiality) | **Negotiate** | Within DE policy bands (see `_shared/nda-policy-positions.md`). Standard adjustments: survival period, return/destruction timeline, compliance confirmation frequency. |
| Cl. 7 (Non-Circumvention) | **Negotiate** | Duration (18-36 month range acceptable), scope of Associated Counterparties, independent knowledge evidence standard. |
| Cl. 8 (General) | **Defend** | Governing law (Dutch), jurisdiction (Amsterdam), eIDAS, good faith — these are standard and non-negotiable. |

**Golden rule:** If the counterparty's redline email has more than 3-4 points on the binding clauses, either the LOI is genuinely problematic (escalate to legal) or the counterparty is over-lawyering (accept more).

---

## Conditional Blocks Reference

| Block | Applicable Types | Default |
|---|---|---|
| IF: PRICING / IF: NO_PRICING | All | NO_PRICING (defer to MSA stage) |
| IF: PHASING | Wholesale only | Omit unless customer specifies phasing |
| IF: EXCLUSIVITY | Distributor only | Non-exclusive (default) |
| MODE A / MODE B | Distributor only | Mode A (Combined Offering) |
| ALT-A: EXISTING NDA | All | Use if NDA already signed |
| ALT-B: EMBEDDED NCNDA | All | Use if no NDA exists (default for new relationships) |
| Service type selector | End User only | Select one or combine (Bare Metal / Shared Cloud / Tokens) |

---

## HubSpot Integration

After LOI execution:
1. Update the HubSpot deal to "LOI Signed" stage
2. Attach the signed PDF to the deal record
3. Set "MSA Target Date" to LOI date + 90 days
4. Log the LOI type (End User/Distributor/Wholesale) and mode (Distributor: A/B) in the deal custom fields

---

## Version Control

All three templates share identical binding clauses (Cl. 5, 6 ALT-B, 8). If a binding clause is updated in one template, it **must** be updated in all three simultaneously.

| Template | Version | Last Updated |
|---|---|---|
| DE-LOI-Distributor | 3.5 | 2026-04-17 |
| DE-LOI-Wholesale | 3.5 | 2026-04-17 |
| DE-LOI-EndUser | 3.5 | 2026-04-17 |
| DE-LOI-StrategicSupplier | 1.0 | 2026-04-17 |
| DE-LOI-EcosystemPartnership | 1.0 | 2026-04-17 |
| DE-Site-HoT (grower body + Annex A) | 1.0 | 2026-03-13 (see `de-site-hot/templates/template-version.md`) |

### Changelog summary (v3.2 → v3.5.6)

Full detail in `CHANGELOG.md`. High-level sweep for assembly purposes:

- **v3.2** — library-sourced Recital A (`_shared/loi-recital-a-library.md`); "DEC Block" dropped from customer-facing clauses; "minimum 5 years" → "approximately 5 years, indicative only"; Cl. 4.2 arrows → prose; "(NON-BINDING)" suffix stripped from schedule titles; QA linter embedded (`_shared/loi-qa-gate.md`); deprecated `commercial.dec_block_count`.
- **v3.3** — full SS + EP engines; Phase 0–8 SOP; `/loi` slash command; QA gate.
- **v3.4** — Recital A single canonical body + 5 type-specific tails (3-variant library collapsed); meta-commentary strip from Recital C/D and Cl. 5.1; SS Cl. 5 split into `clause5_ss` ("Supply Chain and Delivery Commitment", NOT revenue-bankability); R-21 + R-22 + R-23 linter rules; Phase 7.5 `legal-counsel` review gate; source-attribution framework (`_shared/counterpart-description-framework.md`); `counterparty.source_map` field (enforced by R-23 fabrication gate).
- **v3.5.1** — NL BV default signatory Jelmer/CPO → Carlos/Director (5 intake YAMLs + SKILL.md); NL BV address Zug (AG) → Mijnsherenweg/Kudelstaart + KvK 98580086 (6 YAMLs); sig-block cleanup (no KvK, no "ACKNOWLEDGED AND AGREED", [TBC] → fillable blanks via `_render_placeholder`); footer centre-aligned + entity derived from `provider.legal_name` (BV → nl, AG → ag); Cl. 3.2 rack density 40 kW → 130 kW + DLC (GB200/GB300 NVL72 reference); Cl. 3.4 branches on non-numeric `expansion_mw`; Schedule 1 `technical.gpu_platform` structured field; `docs/PRINCIPLES.md` (12 engineering principles).
- **v3.5.2** — `config/entities.yaml` entities register (de_nl + de_ag); intake `provider.entity: "de_nl"` + `signatory_mode: "pre_msa"` expansion (backward-compat for explicit-fields intakes); **Parties Preamble** in document body (`parties()` method between cover and Recital A); brand rename body-wide `"the Provider"` → `"Digital Energy"` (99 occurrences) + Recital A defined-term cleanup; `self.party` for SS now "Supplier" (was "Partner"); Signal Test methodology (3-gate: Attribution / Operational relevance / Freshness) in framework; **R-24** (inline citations `[polarise.eu]`), **R-25** (vanity-financial: valuation / generic VC labels / unattributed capital-raise), **R-27** (sig-block `[TBC]`), **R-28** (TBC density warn); `legal-counsel/specializations/contract-review/loi-review-workflow.md` callee for Phase 7.5.
- **v3.5.3** — EP Recital D "may exchange" → "will exchange"; `--migrate-check` CLI flag (legacy YAML inspector, non-blocking); Gmail MCP fallback in Phase 3 (request PDF/paste of thread on schema error); Drive-routing spec in Phase 8 (`scripts/artifact_storage.py::upload_artifact()` — pending the script landing).
- **v3.5.3-cont** — **Scope F**: Recital B multi-paragraph extraction regex (`\(B\)` … `(?=\(C\)\s|\(D\)\s|\n##\s|\Z)` — fixes `\n\n` early-stop bug); **J12**: `type_defaults` auto-expansion (minimal `type: Wholesale` intake → NL BV/Carlos/Director; backward-compat for explicit-fields); **Scope E**: R-22 regex narrowed to meta-commentary verb contexts (e.g. `ability to (secure|obtain|access)`) + allowlist comment; **J8**: Phase 6 prompt shows full Recital B verbatim (60-char truncation removed); **J9**: Phase 5 three-option redraft prompt (accept / redraft-with-notes / paste-replacement); **Scope H**: tier-2 qualifier worked-example pattern in framework (prose + `source_map` YAML dict schema with `tier: 2` + `qualifier`).
- **v3.5.4** — Polarise regression fixture anchor (`colocation/regression/v3.5/polarise_wholesale_intake.yaml`) exercising every v3.5.x fix path.
- **v3.5.5** — Parties Preamble spacing fix (`space_after=6` between party blocks; was `self.p("")` blank paragraphs doubling the gap); InfraPartners regression fixture (4th tier-1-verified fixture); Polarise fixture tier-1 upgrade (HRB 17714 Amtsgericht Paderborn verified); `docs/PRINCIPLES.md` engineering principles doc with per-principle tripwires.
- **v3.5.6 scope D** — R-23 pillar diagnostic (permissive any-pillar gate unchanged; QA report emits `[INFO] R-23 attribution diagnostic` naming which pillar matched each claim); sentence-boundary `[TBC]` proximity (replaces wildcard v3.5.x; trailing-`[TBC]` special case); hybrid override-reason validation (free-text ≥15 chars OR structured audit short-code `<STATUS>-<YYYY-MM-DD> <INITIALS>`; thin patterns rejected unconditionally).
- **v3.5.6 scope G + G-bis** — Phase 7.5 fail-closed code-level enforcement (opt-in via `--enforce-phase-7-5` flag OR `DE_LOI_ENFORCE_PHASE_7_5=1` env var; default fail-open preserves v3.5.x); sentinel file `<docx>.phase_7_5_required` with SHA-256 of .docx (prevents replay via consumption + post-approval tampering via hash check); distinct exit code 3. **Senior-counsel refinement pass** (`loi-senior-review-pass.md`) — two-pass Phase 7.5 review: junior 4-point + senior six-axis (commercial posture, precedent consistency, counterparty-reading, Signal-Test deep check, identity/execution hygiene, deliverability/aftermath); senior envelope is the **final** envelope `legal-assistant` consumes.
- **v3.5.6 scope I** — framework worked-examples tier-1/tier-2 URL re-verification (19 URLs across 4 counterparties; 8 updated — canonicalisation, single-page collapse, broken-deep-link → index). Polarise HRB 17714 Paderborn now framework-anchored via `online-handelsregister.de` (retires `[Companyhouse.de placeholder]` pattern).
- **v3.5.7** — this update: sibling docs sync (ASSEMBLY_GUIDE / FEATURE_MATRIX / SOP brought to v3.5.6 state).

---

## 12. Site Sourcing Stream — DE Site HoT

This section covers assembly rules specific to the DE Site HoT (grower Heads of Terms, v1.0). Detailed workflow is in `SKILL.md` § Site Sourcing Stream Workflow.

### 12.1 Two-part structure

| Artefact | Source | Modification allowed? |
|---|---|---|
| **Body** (`hot-grower-body-v1.docx`) | `de-site-hot/templates/` | **NEVER**. Legally reviewed bilingual (EN/NL) body. Variable references point to Annex A items. If a request implies body modification, REFUSE and escalate to `legal-counsel`. |
| **Annex A** (`hot-grower-annex-a-v1.docx`) | `de-site-hot/templates/` | Only via form-fill of yellow (FFFF99, required) and green (CCFFCC, conditional) shaded cells per `field-registry.json`. No structural edits. |

### 12.2 Intake discipline

- Ask questions in conversational batches per phase. Never dump all 48 fields at once.
- Validate each phase before proceeding.
- Use `field-registry.json` as the single source of truth for field IDs, validators, conditionals, and phase assignments.

### 12.3 Validator escalations

See `SKILL.md` §"Site HoT Escalation Matrix" (canonical). That table governs all validator-triggered routing. ASSEMBLY_GUIDE adds no rules of its own.

### 12.4 Bilingual handling

- Populate both EN and NL columns simultaneously per `field-registry.json`.
- Preserve native Dutch terms where the field-registry specifies them (`opstalrecht`, `tekenbevoegdheid`, `energiebelasting`, `bestemmingsplan`, `erfpacht`, `hypotheek`).
- Do not translate Dutch legal terms into English approximations.

### 12.5 Conditional sections

| Section | Trigger | Action |
|---|---|---|
| D.8–D.11, G.Landowner | `grower_is_not_landowner = true` | Populate; include landowner in signatory block |
| D.10–D.11, G.Financier | `has_land_financier = true` | Populate; include financier in signatory block |
| F.1a | F.1 CHP lease included | Populate CHP fee and period |
| F.2a | F.2 co-investment included | Populate % (max 50); escalate to Jelmer |

If a conditional trigger is false, strip the dependent cells entirely; do not leave empty yellow-shaded cells in the final Annex A.

### 12.6 Policy reference

The NDA/confidentiality policy in `_shared/nda-policy-positions.md` applies to the HoT's confidentiality clause (body Cl. 7 — not editable at this stage). If a grower proposes alternative confidentiality terms, that is a **body modification** request and must be escalated to `legal-counsel`.

### 12.7 Generation caveat (2026-04-13)

The form-fill engine `generate_site_hot.py` is **not yet built**. The versioned .docx templates in `de-site-hot/templates/` are Git LFS pointer stubs (130 B each); the real binaries must be fetched before the engine can be written. See `de-site-hot/templates/README.md` for fetch instructions. Until resolved: the intake runs to completion, `annex-a-data.json` is written, the Annex A docx step writes a `PENDING_ENGINE.md` placeholder, and the body is copied (also a stub until fetch).
