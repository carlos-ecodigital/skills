# legal-assistant — Assembly Guide

This guide covers two streams produced by `legal-assistant`:

- **Colocation Capacity** — LOI/NCNDA v3.0 (End User, Distributor, Wholesale). Sections 1–11 below.
- **Site Sourcing** — DE Site HoT v1.0 (grower Heads of Terms). Section 12 below.

A third, parallel stream — **Introducer Fees** (DE-MIA Master Introduction Agreement, Master + severable Annex A Commercial / Annex B Capital) — has its own operator guide at `mia/MIA_ASSEMBLY_GUIDE.md` and engine at `mia/generate_mia.py`. Not covered here. If a counterparty is an Introducer (customer or investor referrer), use that guide instead. **Annex B (capital) MUST be routed through the `legal-counsel` skill before first execution.**

Previously called `loi-generator/ASSEMBLY_GUIDE.md`.

---

## 1. LOI Type Selection

| If the counterparty... | Use | Template |
|---|---|---|
| Buys compute directly (enterprise, AI lab, startup) | **End User** | DE-LOI-EndUser-v3.0 |
| Packages DE capacity with their own services to sell to end users (SI, MSP, software company, sovereign AI builder) | **Distributor** | DE-LOI-Distributor-v3.0 |
| Buys capacity in bulk to resell to their own customers (neocloud, GPU cloud) | **Wholesale** | DE-LOI-Wholesale-v3.0 |

**When in doubt:** If the counterparty has its own end-user customers → Distributor or Wholesale. If the counterparty IS the end user → End User.

**Distributor vs Wholesale:** Distributors add value (integration, managed services, software). Wholesale customers resell raw capacity. The test: does the counterparty transform or bundle the capacity with their own services?

---

## Distributor Mode Selection

The Distributor template (DE-LOI-Distributor) has two modes:

| If the partner... | Use | Cl. 3.2 variant |
|---|---|---|
| Delivers services jointly with DE to end users | **Mode A: Combined Offering** | Joint service scope, responsibility matrix |
| Introduces customers to DE but does not deliver services | **Mode B: Introduction/Referral** | Referral arrangement, fee economics in separate agreement |

**Mode B note:** When Mode B is selected, the economic terms (fees, qualifying introductions, payment schedule) are NOT in the LOI. They go in a separate **Commercial Introduction Agreement** signed alongside or after the LOI. The LOI captures the relationship intent; the fee agreement captures the economics.

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

**Digital Energy Netherlands B.V.** signs all types.

- Dutch entity = jurisdictional alignment (Dutch law LOI)
- Closest to revenue-generating assets (lender-preferred)
- Clean SPV assignment chain (intra-jurisdictional)
- If credit enhancement needed: reference Digital Energy Group AG (Swiss parent) as guarantor in the credit assessment clause — not as signatory

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
> [PARTNER_SHORT] provides AI system integration services, including the design, deployment, and management of GPU compute infrastructure for enterprise and institutional clients. The Provider develops and operates purpose-built AI colocation facilities with secured energy and grid access, liquid cooling, and full energy recovery infrastructure.
>
> The Parties intend to combine the Partner's enterprise customer relationships, solution architecture capability, and implementation expertise with the Provider's colocation platform to deliver integrated AI infrastructure solutions — from workload assessment and hardware specification through facility deployment, system commissioning, and ongoing managed operations — as a unified end-to-end offering to enterprise and institutional end users.

**Cl. 3.2(b):**
> the Partner would contribute solution architecture and workload assessment, hardware specification and procurement, rack-level deployment and commissioning, operating system and orchestration layer configuration, application integration and performance tuning, ongoing infrastructure management including monitoring, patching, and capacity planning, and first-line technical support for end-user customers

### Example 2: Sovereign AI / Defence Partner (Mode A)

*Archetype: A company like FrontierOne, Palantir's infrastructure arm, or a national defence contractor — enables government and critical infrastructure clients to access AI compute within classification and sovereignty constraints.*

**Cl. 3.1:**
> [PARTNER_SHORT] provides sovereign AI infrastructure and security-classified computing services to government, defence, and critical national infrastructure institutions. The Provider develops and operates purpose-built AI colocation facilities with secured energy and grid access, liquid cooling, and full energy recovery infrastructure.
>
> The Parties intend to combine the Partner's security architecture capability, government procurement expertise, and institutional relationships with the Provider's colocation platform to deliver sovereign, classification-compliant AI infrastructure — enabling government and defence end users to access high-density compute capacity within the security, provenance, and data sovereignty frameworks their mandates require.

**Cl. 3.2(b):**
> the Partner would contribute security architecture design and threat modelling, facility clearance and classification-compliant operational procedures, secure supply chain management and hardware provenance verification, government procurement navigation including tender preparation and compliance documentation, data sovereignty assurance including encryption key management and access control frameworks, and ongoing security operations including incident response and audit support

### Example 3: GPU / Hardware Solutions Provider (Mode A)

*Archetype: A company like Lambda (hardware division), Penguin Solutions, or a regional GPU reseller — procures, configures, and manages GPU hardware but doesn't operate facilities.*

**Cl. 3.1:**
> [PARTNER_SHORT] provides GPU and accelerator hardware solutions, including procurement, configuration, and lifecycle management of high-density compute infrastructure for AI workloads. The Provider develops and operates purpose-built AI colocation facilities with secured energy and grid access, liquid cooling, and full energy recovery infrastructure.
>
> The Parties intend to combine the Partner's hardware procurement capability, vendor relationships, and technical configuration expertise with the Provider's colocation platform to deliver turnkey AI compute infrastructure — from hardware sourcing and rack integration through facility deployment and ongoing hardware lifecycle management — to enterprise, research, and neocloud customers.

**Cl. 3.2(b):**
> the Partner would contribute GPU and accelerator procurement including vendor relationship management and volume pricing negotiation, hardware configuration and validation against workload requirements, rack integration and cabling, firmware and driver lifecycle management, warranty administration and RMA coordination, and capacity planning for hardware refresh cycles

### Example 4: Managed Service Provider (Mode A)

*Archetype: A company like OVHcloud, Leaseweb, or a regional MSP — packages infrastructure as a service with platform management, billing, and customer success.*

**Cl. 3.1:**
> [PARTNER_SHORT] provides managed infrastructure services, packaging compute, storage, and networking as turnkey cloud offerings for enterprise and mid-market customers. The Provider develops and operates purpose-built AI colocation facilities with secured energy and grid access, liquid cooling, and full energy recovery infrastructure.
>
> The Parties intend to combine the Partner's service packaging capability, customer management infrastructure, and established client base with the Provider's colocation platform to deliver managed AI compute services — enabling the Partner's customers to access sovereign, high-density GPU infrastructure through the Partner's existing service relationship and billing framework.

**Cl. 3.2(b):**
> the Partner would contribute infrastructure-as-a-service packaging including compute, storage, and networking, customer onboarding and environment provisioning, platform management including orchestration, monitoring, and autoscaling, SLA management and service reporting, billing and usage metering, and customer success management including technical account management and escalation handling

### Example 5: Software / AI Platform Company (Mode A)

*Archetype: A company like Weights & Biases, Anyscale, or a vertical AI platform — provides software that runs on GPU compute and needs infrastructure underneath.*

**Cl. 3.1:**
> [PARTNER_SHORT] develops and operates an AI [training / inference / MLOps] platform used by [enterprise / research / developer] customers to [deploy, train, and manage AI workloads at scale]. The Provider develops and operates purpose-built AI colocation facilities with secured energy and grid access, liquid cooling, and full energy recovery infrastructure.
>
> The Parties intend to combine the Partner's software platform and customer ecosystem with the Provider's colocation infrastructure to offer an integrated solution — enabling the Partner's customers to run their AI workloads on sovereign, purpose-built European infrastructure through the Partner's platform interface, without managing the underlying facility, hardware, or cooling systems directly.

**Cl. 3.2(b):**
> the Partner would contribute its software platform including workload submission APIs and SDKs, scheduling and resource allocation optimisation, usage tracking and billing integration, customer-facing dashboard and self-service tooling, and ongoing platform development and feature delivery

### Example 6: Referral Partner (Mode B)

*Archetype: An advisory firm, consultant, or well-connected intermediary who introduces customers but doesn't deliver services. Fee economics in a separate Referral Agreement.*

**Cl. 3.1:**
> [PARTNER_SHORT] provides [strategic advisory / technology consulting / market access] services to enterprise and institutional clients across [territory]. The Provider develops and operates purpose-built AI colocation facilities with secured energy and grid access, liquid cooling, and full energy recovery infrastructure.
>
> The Parties intend to establish a referral arrangement under which the Partner would identify and introduce qualified end-user customers to the Provider's DEC platform, leveraging the Partner's established client relationships, domain credibility, and market presence in [territory/vertical]. The economic terms of the referral arrangement will be set out in a separate agreement between the Parties.

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
| DE-LOI-Distributor-v3.0 | 3.0 | 2026-04-05 |
| DE-LOI-Wholesale-v3.0 | 3.0 | 2026-04-05 |
| DE-LOI-EndUser-v3.0 | 3.0 | 2026-04-05 |
| DE-Site-HoT (grower body + Annex A) | 1.0 | 2026-03-13 (see `de-site-hot/templates/template-version.md`) |

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
