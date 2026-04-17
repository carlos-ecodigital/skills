# legal-assistant — Feature Matrix

This matrix compares document types across both streams:

- **Colocation Stream** — LOI/NCNDA v3.0 (3 sub-types). Sections below.
- **Site Sourcing Stream** — DE Site HoT v1.0. Final section.

## Clause Structure — Colocation LOI by Type

| Clause | End User | Distributor | Wholesale |
|--------|:---:|:---:|:---:|
| **Recitals** | Service platform | Integration platform | Scale infrastructure |
| **Cl. 1 Definitions** | 10 terms | 17 terms (+PBI, +AC, +Competitor, +Site ID, +Whitespace, +SOF, +Transaction) | 15 terms (+AC, +Site ID, +SOF, +Services, +Whitespace) |
| **Cl. 2 Purpose and Scope** | Standard | Standard | Standard |
| **Cl. 3 Commercial Terms** | Service Requirements | Partnership and Combined Offering | Capacity and Commercial Terms |
| **Cl. 4 Next Steps / Structure** | Next Steps (simple) | Relationship Structure + Protection | Relationship Structure + Next Steps |
| **Cl. 5 Project Finance** | Standard (lighter touch) | Standard | Standard (heaviest context) |
| **Cl. 6 Confidentiality** | Tier A (8 clauses) | Tier B (16 clauses) | Tier B (16 clauses) |
| **Cl. 7 Non-Circumvention** | **OMITTED** | **FULL** (24mo, PBI 10yr) | **LIGHT** (supply-side only) |
| **Cl. 8 / 7 General** | Cl. 7 (9 sub-clauses) | Cl. 8 (10 sub-clauses) | Cl. 8 (10 sub-clauses) |
| **Schedule 1** | None | Partnership Details | Capacity + Technical Spec |
| **Page count** | ~4 | ~7-8 | ~6-7 |

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

| Feature | End User | Distributor | Wholesale |
|---------|:---:|:---:|:---:|
| Revenue bankability signal (Cl. 5.1) | Yes | Yes | Yes |
| Assignment carve-out (Cl. 5.2) | Yes | Yes | Yes |
| Lender acknowledgment (Cl. 5.3) | Yes | Yes | Yes |
| Revenue chain articulation (Cl. 4.2) | No | No | **Yes** |
| Direct agreement willingness (Cl. 4.3) | No | No | **Yes** |
| Take-or-pay signal (Cl. 3.6) | No | No | **Yes** |
| Credit assessment (Cl. 3.7) | No | No | **Yes** |

---

## Commercial Features by Type

| Feature | End User | Distributor | Wholesale |
|---------|:---:|:---:|:---:|
| Capacity in DEC Blocks | Optional | Via partner estimate | **Yes** |
| Service type selector (BM/Shared/Tokens) | **Yes** | No | No |
| Partnership type (bespoke) | No | **Yes** | No |
| Deployment phasing | No | No | **Yes** |
| Expansion rights | No | No | **Yes** |
| Minimum term signal | Yes | No | **Yes** |
| Indicative pricing table | Yes | Yes | **Yes** (detailed) |
| Implementation milestones | Yes (Cl. 4) | Yes (Cl. 4.5) | **Yes** (Cl. 4.5 + Sch. 1) |
| Non-exclusivity / preferred partner | No | **Yes** (conditional) | No |
| Governance mechanism | No | Yes (Cl. 4.4) | No |

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

## Site Sourcing Stream — DE Site HoT v1.0

| Dimension | DE Site HoT |
|---|---|
| **Counterparty** | Dutch greenhouse grower (B.V., V.O.F., C.V., N.V., Coöperatie U.A.) |
| **Structure** | Two-part: locked bilingual Body (EN/NL, never modified) + populated Annex A (form-filled) |
| **Intake method** | 7-phase conversational (Identification → Signatory/Greenhouse → Electrical → Heat → Land → Commercial → Optional + Notices) |
| **Field count** | 48 (35 required yellow-shaded + 13 conditional green-shaded) |
| **Template version** | 1.0 (2026-03-13); bilingual; locked body |
| **Engine** | `generate_site_hot.py` (NOT YET BUILT — blocked on LFS template fetch) |
| **Validators** | KVK 8-digit, EAN `^871\d{15}$`, capacity base≤total, heat ΔT ≥15°C, co-investment ≤50%, entity suffix whitelist |
| **Conditional blocks** | Grower ≠ landowner (D.8–11, G.Landowner); mortgaged land (D.10–11, G.Financier); CHP lease (F.1a); co-investment (F.2a) |
| **Escalations** | Non-50:50 heat split → Carlos; co-investment → Jelmer; missing consent → Carlos + legal-counsel; body modification → REFUSE |
| **Policy reference** | `_shared/nda-policy-positions.md` applies to body confidentiality (Cl. 7 — not editable) |
| **Output artifacts** | `annex-a-data.json`, `DE-Site-HoT_Annex_A_{Company}.docx`, `DE-Site-HoT_Body_{Company}.docx` (copy), `intake-log.md`, `status.md` |
| **Output location** | SSOT `contracts/hots/active/{grower-slug}/` |
| **Post-gen action** | Git commit + push to SSOT (when working dir is a git checkout) |
| **Companion agreements** | None at HoT stage — future MSA/SOF are post-HoT lifecycle (see `grower-relationship-mgr`) |

### Engine asymmetry (vs. Colocation LOI)

| | Colocation LOI | Site HoT |
|---|---|---|
| Intake format | YAML file | Conversational (7 phases) |
| Engine status | Deterministic Python (`generate_loi.py`), shipping | NOT BUILT — blocked on LFS fetch |
| Template storage | Markdown reference (not consumed by script) + Python-built .docx from scratch | Locked binary .docx, form-filled in place via zipfile + xml.etree |
| Brand layer | Via `document-factory` (cover page, headers, footers) | Self-contained (pre-formatted bilingual template) |
| Body mutability | Full (script builds from scratch) | Locked; REFUSE body modification |
| Output name pattern | `YYYYMMDD_DEG_LOI-{Type}_{Company}_(STATUS).docx` | `DE-Site-HoT_Annex_A_{Company}.docx` + body copy |
