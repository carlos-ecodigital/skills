# Skill Feedback, Lessons Learned & Improvement Plan

> **Source:** 10-agent stress test of the investment case intake plan
> **Date:** 2026-02-17
> **Purpose:** Capture every objective finding from the 10 specialist agent review, synthesized into actionable skill and workflow improvements.

---

## Part A: 10-Agent Review Synthesis

Each agent's findings are preserved in detail with specific missing items and structural lessons.

---

### Agent 1 — ING/Rabobank Debt Banker

**Missing items identified:** 68 questions

**Key gaps:**
- **Covenants:** DSCR lock-up (1.10-1.15x), DSCR default (1.05x), LLCR minimum (1.15-1.20x) — all absent from any skill
- **Reserve accounts:** DSRA (6 months coverage), MRA (maintenance reserve), cash sweep mechanism — not in project-financing intake or IM template
- **Construction financing:** Bridge-to-term structure, IDC funding, drawdown schedule — absent from all skills
- **Hedging:** Interest rate swap/cap/collar strategy and % of exposure hedged — not addressed anywhere
- **Security package:** Share pledge (pandrecht op aandelen), asset pledge, account pledge, assignment of contracts, direct agreements (tripartite) — not in DD checklist intake
- **Cash waterfall:** Revenue → OPEX → Senior debt service → DSRA → MRA → Tax → Equity distributions — not specified in any template

**Structural lesson:** project-financing has 293K lines of reference knowledge about all these topics but no structured way to surface them during IM production. The IM template was written as if equity is the only capital source. For an infrastructure company where 50-70% of capital structure is project debt, this is a fundamental omission.

**Resolution:** Intake Section 10 (Debt Structure & Bankability) now covers all 35 questions. IM guide restructured with S10.1-10.5 and S12A (Capital Structure).

---

### Agent 2 — PE Infrastructure Fund Partner

**Missing items identified:** 100+ questions (key subset selected)

**Key gaps:**
- **Equity waterfall:** Return of capital → preferred return → catch-up → carry split — not in any template
- **Anti-dilution:** Broad-based weighted average vs. full ratchet — not in seed-fundraising intake
- **Liquidation preferences:** Participating vs. non-participating preferred — not discussed anywhere
- **Swiss AG mechanics:** Share classes (registered vs. bearer), Vinkulierung transfer restrictions — not in jurisdiction guide
- **JV equity:** Co-investment at project SPV level — not contemplated in any skill
- **Dual economics:** Infrastructure investors have fundamentally different economics (yield + appreciation) vs. VC (appreciation only) — no skill distinguishes between them

**Structural lesson:** seed-fundraising treats all investors as identical. The intake and IM must serve both VC (growth equity, 10x MOIC, 5-8 year horizon) and infrastructure investors (6-8% cash yield, 3-5x MOIC, 7-12 year horizon). Every deliverable needs dual-audience framing.

**Resolution:** Intake Section 11 (Equity Structure & Investor Terms, 20 questions) and Section 17 (Investor Strategy, questions 9-14 on infra vs. VC decision).

---

### Agent 3 — APG/PGGM Pension Fund Risk Officer

**Missing items identified:** 60-80 questions

**Coverage assessment of original risk section:**
- Construction risk: **5% covered** — no P50/P75/P90 cost overrun distributions, no EPC failure scenario
- Technology risk: **5% covered** — no BESS degradation quantification, no GPU obsolescence scenario
- Revenue/market risk: **15% covered** — no merchant revenue P75/P90 downside
- Insurance risk: **10% covered** — no coverage gap analysis, no exclusion mapping
- Dutch regulatory risk: **20% covered** — no Wcw heat obligation impact quantified
- ESG/SFDR: **0% covered** — mandatory for EU institutional capital since 2024
- Operational risk: **0% covered** — no O&M failure, cybersecurity, workforce scenarios

**Structural lesson:** Risk assessment must be quantified, not narrated. "High likelihood, high impact" with a narrative mitigation is insufficient for institutional investors. Pension funds need: P50/P75/P90 distributions, Monte Carlo sensitivity, tornado charts, and DSCR impact quantification for each material risk. If your risk section doesn't survive their internal stress test, they reject.

**Resolution:** Intake Section 15 expanded from 20 to 35 questions with subsections for Construction Risk (15.16-20), ESG/SFDR (15.21-25), Operational Risk (15.26-30), and Dutch Regulatory Risk Specifics (15.31-35). All require quantified financial impact.

---

### Agent 4 — De Brauw/Stibbe NL Permitting Lawyer

**Missing items identified:** 50 questions across 8 regulatory domains

**Key gaps by domain:**
- **Omgevingswet pathway:** 8 additional questions — BOPA requirement, omgevingsplan conformity, bezwaar/beroep timeline, participatie vereiste
- **PGS 37 fire safety:** 4 questions — compliance plan, UL9540A, local fire department approval, container clearance distances
- **DC moratorium:** 3 questions — 70 MW IT load threshold, 100,000 m² floor area threshold, Amsterdam-specific ban until 2030
- **Wcw heat obligation:** 5 questions — municipal heat zone designation status, cost-based tariff obligation, revenue model impact
- **Noise impact:** 3 questions — geluidsonderzoek, BESS cooling fan noise at property boundary, residential proximity assessment
- **Cable pooling:** 4 questions — MLOEA status, allocation methodology, metering architecture, grid charge allocation
- **Soil contamination:** 4 questions — NEN 5725 desk study, NEN 5740 investigation, asbestos assessment, remediation cost estimate
- **Stakeholder participation:** 3 questions — omgevingsoverleg, gemeentelijke participatievereisten, social license

**Structural lesson:** netherlands-permitting skill has deep reference knowledge but no structured intake. The investment-case-intake now serves as the permitting intake too — every site must answer these regulatory questions. The expanded gates in Section 8 (Sites & Assets) integrate all permitting requirements.

**Resolution:** Section 8 gates expanded with Omgevingswet pathway detail, Wcw heat zone designation, PGS 37, soil contamination, stikstof/AERIUS, stakeholder participation, and noise impact per site.

---

### Agent 5 — Lazard/Rothschild IM Advisory

**Missing items identified:** 7 new sections, 6 appendices

**Key gaps:**
- **IM must serve dual audience:** VC (platform growth narrative) + infrastructure (per-site yield analysis) — currently written as single-audience
- **Section 10 restructure needed:** 10.1 Platform P&L → 10.2 Per-site unit economics → 10.3 Model audit → 10.4 Debt sizing → 10.5 Breakeven
- **New Section 12A:** Capital Structure & Financing Strategy — debt evolution, gearing trajectory, waterfall
- **Missing appendices:** G (asset portfolio summary), H (insurance programme), I (ESG/SFDR), J (tax structuring memo), K (bankability checklist), L (data room index)
- **Comparable transactions:** Must include infrastructure M&A multiples (EV/MW, EV/EBITDA), not just funding rounds
- **Sensitivity analysis:** Must use tornado charts (top 5 variables driving equity IRR), not just scenario tables

**Structural lesson:** The IM template was written for a SaaS seed round. Infrastructure IMs at Rothschild/Lazard/Macquarie advisory level require: asset-level detail, debt structure evolution across project lifecycle, dual-audience framing, and per-site DCF alongside platform-level P&L. The executive summary must be standalone-readable. Appendices must be cross-referenced from the body.

**Resolution:** IM guide restructured (S10.1-10.5, S12A, Appendices G-K). Template updated with corresponding sections and {{PLACEHOLDER}} variables.

---

### Agent 6 — a16z/Founders Fund Seed VC

**Missing items identified:** 90 questions across 7 categories

**Key gaps:**
- **Founder-market fit:** 8 questions — domain credibility, technical depth, replacement scenario, burn tolerance
- **Valuation methodology:** 6 questions — comparable anchoring, WACC-implied, infrastructure fund vs. VC pricing mismatch
- **Competitive dynamics:** 10 questions — Crusoe/Lowercarbon response, grid access defensibility, first-mover disadvantage, incumbent timeline, unit economics parity
- **Network effects:** 8 questions — information advantage, shared infrastructure economics, switching costs, multi-homing risk, platform vs. portfolio distinction
- **Customer validation:** 12 questions — grower cohort binding, neocloud diligence results, price validation with NL data, LOI binding status, counterparty credit
- **Term sheet negotiation:** 10 questions — valuation floor, dilution ceiling, board seats, liquidation preference positions, drag-along
- **Metacognitive:** 5 questions — assumption brittleness, competitive insecurity, failure definition

**Structural lesson:** Seed VCs at Tier 1 firms assess the FOUNDER as much as the business. The original intake had zero questions testing founder self-awareness, assumption quality, or negotiation readiness. A founder who cannot name their most fragile assumption or their biggest competitive insecurity gets passed on. These are disqualifiers, not "nice to have" P2 items.

**Resolution:** Section 3 expanded with founder-market fit (19-24). Section 4 expanded with competitive dynamics (21-25). Section 14 expanded with customer validation depth (17-22). Section 18 (Term Sheet Negotiation Prep) created as new section. Section 20 includes metacognitive questions (9-16).

---

### Agent 7 — DNV BESS Independent Engineer

**Missing items identified:** 92 questions

**Key insight:** "The intake as drafted would produce an investment case that a project finance lender would reject in the first technical due diligence phase."

**Critical technical gaps:**
- **Degradation:** P50/P90 curves missing — without them, DSCR/LLCR calculations are meaningless
- **Cycling vs. warranty:** Revenue model assumes 420 cycles/year but warranty may limit to 365 — this single mismatch can break bankability
- **Revenue stacking:** Without TenneT FCR/aFRR prequalification status, revenue projections for ancillary services are unsubstantiated
- **BMS/EMS platform:** Unspecified integration risk delays COD 6-12 months
- **Grid code:** Compliance must be designed in, not retrofitted — LVRT/HVRT, reactive power, fault ride-through
- **Fire safety:** UL9540A testing is a prerequisite for insurance underwriting and PGS 37 compliance
- **Decommissioning:** EU Battery Regulation 2023/1542 requires battery passport by 2027

**Structural lesson:** BESS technical questions are not "nice to have for P2." They are P0/P1 gating items for bankability. A BESS project without validated degradation curves, confirmed prequalification status, and cycling/warranty alignment is not financeable.

**Resolution:** Section 6 (BESS Technical Specifications, 45 questions) covers all 8 subsections identified by the DNV agent.

---

### Agent 8 — DC/AI Infrastructure Engineer

**Missing items identified:** 99 questions

**Key insight:** "A founder could complete the proposed intake and still lack sufficient detail to pass independent engineer review for a DC facility."

**Critical technical gaps:**
- **Power density validation:** Requires engineering calculations, not datasheet references — 240 kW/rack for GB200 NVL72
- **SLA structure:** Neocloud customer SLA terms directly affect lender credit assessment — uptime, power density, temperature, seasonal derating
- **GPU refresh reserve:** 8-15% of operating cash flow annually must be funded in financial model or DSCR collapses at Year 5
- **Cooling design:** DLC vs. RDHx vs. immersion — loop redundancy, heat exchanger sizing, waste heat transfer to district heating
- **Network connectivity:** InfiniBand topology for multi-node AI training, carrier diversity, AMS-IX proximity
- **Moratorium compliance:** 70 MW IT load and 100,000 m² are legal blockers, not risk factors — confirmed by counsel or project stops

**Structural lesson:** DC/AI infrastructure investors read technical specifications like debt covenants — every number must be defensible with engineering calculations, not marketing materials. GPU refresh reserve is the DC equivalent of BESS augmentation reserve — if it's not funded, the asset depreciates faster than the debt amortizes.

**Resolution:** Section 7 (DC/AI Infrastructure Technical, 50 questions) covers all 7 subsections. GPU refresh reserve integrated into Section 12 financial model requirements.

---

### Agent 9 — Loyens & Loeff Tax Partner

**Missing items identified:** 55+ questions

**7 critical findings:**

1. **Treaty benefits assumed but unexamined:** 0% WHT via Beteiligungsabzug requires confirmed qualification — ownership stability through fundraising rounds can break it
2. **Earningsstripping constrains project debt materially:** 24.5% fiscal EBITDA cap on interest deduction not modeled in any financial projection
3. **Transfer pricing compliance absent:** Intercompany management fees, IP licensing, loans between AG and BVs — zero documentation = major audit risk
4. **VAT timing mismatch not modeled:** 21% VAT on construction CAPEX creates significant working capital requirement during construction phase
5. **Exit taxation not addressed:** Deelnemingsvrijstelling scope on BV share sale, overdrachtsbelasting (10.4%) on shares containing real estate
6. **ATAD substance lacks teeth:** Binary Yes/No for substance without actionable checklist items
7. **Conditional WHT (WBB 2021) trap:** If Zug combined rate is deemed "low-tax" by Dutch standards, 25.8% override applies — hidden structural blocker

**Structural lesson:** Tax structuring is not a "P2 deep dive." Earningsstripping directly affects DSCR (limits deductible interest). Treaty benefits directly affect investor returns (WHT on dividends). Exit tax directly affects return multiples. These must be addressed before term sheet conversations, not during DD.

**Resolution:** Section 2 (Tax Structuring & Treaty Benefits, 25 questions) covers all 7 areas. Cross-cutting Validation Dimension 5 (Tax Structure Integrity) ensures consistency between S2, S10, and S16.

---

### Agent 10 — Anthropic CPO Cross-Skill Audit

**Integration rating:** 3-4/10

**Structural findings:**
- **Broken cross-references:** seed-fundraising → project-financing is one-way (no return reference)
- **Duplicated content:** Investor deck framework exists in both seed-fundraising and collateral-studio
- **Routing gaps:** "Help me build a financial model" has no clear intake path to any skill
- **No orchestration layer:** 20+ skills, user must know which to invoke — no single entry point
- **No gate enforcement:** Skills accept any input quality without validation
- **No end-to-end workflow:** No skill traces from intake → processing → deliverable output

**Structural lesson:** The skill ecosystem is a collection of reference documents, not a product. Each skill is a standalone knowledge base with weak cross-references. Mode C must create the orchestration layer that binds them into an integrated system.

**Resolution:** Mode C added to seed-fundraising SKILL.md as single entry point. Bidirectional cross-references added between seed-fundraising ↔ project-financing ↔ ops-dataroomops. Content ownership conflicts resolved (investor deck → seed-fundraising exclusively).

---

## Part B: Skill-by-Skill Improvement Actions

| # | Skill | Current State | Improvements | Priority |
|---|-------|--------------|-------------|----------|
| 1 | **seed-fundraising** | 30-question SaaS intake, 5 archetype modes | Add Mode C (full investment case intake), IM production workflow with PF routing, update archetype blending for infrastructure voice | P0 — this session |
| 2 | **project-financing** | 293K lines reference, zero intake | Add intake reference to investment-case-intake.md S6-10, add "Producing IM-Ready Outputs" section, add bidirectional reference to seed-fundraising | P0 — this session |
| 3 | **investment-memo-guide** | 14-section startup IM | Restructure S10 into 10.1-10.5, add S12A, add Appendices G-K, add dual-audience framing, comparable transactions, tornado charts | P0 — this session |
| 4 | **investment-memo-template** | {{PLACEHOLDER}} template for 14 sections | Add placeholders for new sections/appendices, per-site unit economics table, tornado chart format, bankability checklist | P0 — this session |
| 5 | **ops-dataroomops** | Data room with 03_Financial folder | Expand to 03a_Platform_Model / 03b_Project_Models / 03c_Debt_Sizing, add project-financing reference, add per-site document checklist | P0 — this session |
| 6 | **ops-storyops** | Narrative guidance, drift detection concept | Add structured narrative consistency checklist: map TAM, MW, pipeline, revenue, DSCR across all deliverables. Add trigger: after any deliverable, run consistency check | P1 — future session |
| 7 | **collateral-studio** | Grower/neocloud/district heating decks + incomplete investor deck | Remove incomplete investor deck framework. Add reference: "For investor deck, use seed-fundraising" | P1 — future session |
| 8 | **ops-chiefops** | Weekly briefs, blocker resolution | Add "Investment Case Readiness Audit" routing: coordinate readiness checks across seed-fundraising, project-financing, ops-dataroomops | P1 — future session |
| 9 | **netherlands-permitting** | Deep regulatory knowledge, no intake | Add reference to investment-case-intake.md S8 as per-site permitting intake | P1 — future session |
| 10 | **ops-dealops** | Multi-workstream deal tracking | Add trigger: when deal reaches "construction" workstream, reference project-financing for bankability assessment | P2 — future session |
| 11 | **ops-irops** | Monthly investor updates | Add trigger: after intake section completed, update investor pipeline status | P2 — future session |
| 12 | **ops-targetops** | Investor targeting and scoring | Add infrastructure fund vs. VC scoring criteria from intake S17 | P2 — future session |
| 13 | **legal-counsel** | Contract drafting, corporate/M&A | Add reference to investment-case-intake.md S2 as pre-investment legal checklist | P2 — future session |

---

## Part C: Workflow Improvement Actions

### 1. Orchestration Layer (Mode C)

**Problem:** 20+ skills exist but the user doesn't know which to invoke for a given task.

**Solution:** Mode C in seed-fundraising acts as single entry point. "Help me build my investment case" triggers 20-section intake → routes answers to consuming skills → produces deliverables. User never needs to know about skill architecture.

**Implementation:** Added to seed-fundraising/SKILL.md with explicit routing table.

---

### 2. Progressive Input Acceptance

**Problem:** Intake assumes structured, precise answers. Founders have messy, fragmented data.

**Solution:** Each question accepts multiple input types:
- Voice note transcript → extract key data points, ask clarifying questions
- WhatsApp message dump → parse for relevant information
- Rough spreadsheet → validate structure, flag missing fields
- "I don't know yet" → mark as gap, log suggested action to fill it

**Integration:** ops-contextops activates as pre-processor for messy input before routing to the intake question.

---

### 3. Phase-Aligned Delivery

**Problem:** Founder completes sections but receives nothing until everything is done. Motivation drops.

**Solution:** After each section cluster, produce a mini-deliverable:

| After completing... | Mini-deliverable produced |
|---------------------|--------------------------|
| S1 + S2 | Corporate Structure Summary (2 pages) — shareable with lawyers |
| S3 + S4 + S5 | Pitch Narrative Draft (5 pages) — test with advisors |
| S6 + S7 + S8 | Technical Asset Summary (per-site one-pager) — shareable with EPC/engineers |
| S9 + S10 + S11 | Financial Overview Draft (5 pages) — shareable with financial advisors |
| S12 + S13 | Investment Materials Package (deck + exec summary draft) |
| S14-S20 | Complete Investment Case (all deliverables, data room ready) |

Each mini-deliverable uses P0 answers only; P1/P2 answers enhance iteratively.

---

### 4. Dependency-Aware Parallel Paths

**Problem:** Plan implies linear completion (S1 → S2 → S3...) but many sections are independent.

**Solution:** 5 parallel tracks:

| Track | Sections | Dependencies |
|-------|----------|-------------|
| **A** (Immediate) | S3, S4, S5, S20 | None — narrative + founder story |
| **B** (Entity info) | S1, S2 | Needs basic entity details only |
| **C** (Site data) | S6, S7, S8, S9, S10 | Needs site details + technical specs |
| **D** (Financial model) | S12, S13 | Depends on Track C outputs |
| **E** (Synthesis) | S11, S14, S15, S16, S17, S18, S19 | Partially depends on A-D |

Founder can work Track A + Track B simultaneously, then move to Track C, etc.

---

### 5. Quality Gate Enforcement

**Problem:** No skill validates answer quality. Generic or evasive answers pass through.

**Solution:** After each section, run automated gate check:
- **[EXACT]** answers: verify number/date format, flag "approximately" or "TBD" as incomplete
- **[DOC-REQUIRED]** answers: verify document reference exists
- **[CAL]** answers: verify calculation is internally consistent
- **[NARRATIVE]** answers: flag if < 3 sentences or contains generic phrases ("we believe," "significant opportunity," "best-in-class")
- Gate pass → unlock next section's mini-deliverable
- Gate fail → list specific deficiencies with suggested actions to fix

---

### 6. Memory & Learning System

**Problem:** Each conversation starts fresh. Lessons from answering questions are lost.

**Solution:** After each section is completed:
- Log quality of answers (which questions were easy/hard for founder)
- Log gaps discovered (which questions revealed missing data)
- Store in persistent memory for future sessions
- Build cumulative "Investment Case Readiness Score" (0-100%) visible to founder
- Example memory entry: "Founder struggled with S2 (tax) — suggest engaging Loyens & Loeff before next session"

---

## Part D: Lessons for Future Skill Development

### Lesson 1: Every domain skill needs an intake mechanism

Reference knowledge without structured input is inert. project-financing proved this — 293K lines of deep infrastructure knowledge and zero user-facing utility until an intake was created. The intake transforms passive knowledge into an active workflow.

### Lesson 2: Cross-references must be bidirectional

One-way references (seed-fundraising → project-financing) create dead ends when the user enters from the other direction. Both SKILL.md files must point to each other with explicit routing instructions.

### Lesson 3: Infrastructure is not SaaS

Every skill originally designed for SaaS fundraising (MRR/ARR, burn rate, runway, LTV/CAC) needs an infrastructure extension (DSCR, gearing, bankability, site-level DCF, construction risk). The languages are fundamentally different. Using SaaS frameworks for infrastructure fundraising signals to investors that the team doesn't understand their own business model.

### Lesson 4: Dual audience is the norm

Digital Energy serves VCs AND infrastructure funds. Every deliverable must work for both audiences, with the IM explicitly structured as dual-model (platform narrative for VCs + per-site yield analysis for infrastructure investors). This is not unique to DE — most hybrid infrastructure/tech companies face the same challenge.

### Lesson 5: Tax structuring is structural, not cosmetic

Earningsstripping (24.5% fiscal EBITDA cap) directly constrains how much project debt can be sized. Conditional WHT can override treaty benefits that were assumed in the financial model. These are not "tax optimization nice-to-haves" — they are structural constraints that affect DSCR, investor returns, and exit economics. Must be modeled before approaching lenders.

### Lesson 6: Technical DD questions are lender gating items

BESS degradation curves, FCR prequalification, DC PUE validation, GPU refresh reserves — these are not "deep dive" questions for P2. They are P0/P1 blockers for project finance. A lender's independent engineer will reject the credit paper if these items are missing. They must be addressed before the debt process begins.

### Lesson 7: Risk must be quantified, not narrated

"High likelihood, high impact" with a narrative mitigation is a checkbox exercise. Institutional investors (APG, PGGM, EIB) run their own stress tests. If your risk section doesn't include P50/P75/P90 distributions, Monte Carlo sensitivity, and DSCR impact quantification, it will be replaced by their internal assessment — which you have no control over. Better to provide the quantified analysis yourself.

### Lesson 8: The founder experience matters

500 questions over 4 weeks requires sustained motivation. The design must provide continuous return value: mini-deliverables after each section cluster, dependency-aware parallel paths so founders can work on what they know best first, progressive input acceptance for messy data, and visible progress tracking. Without these, founders abandon the process after Section 3.

---

## Time Estimates

| Scope | Questions | Founder Time | Recommended Cadence |
|-------|-----------|-------------|-------------------|
| **P0 only (MVP — Conversation-Ready)** | ~120 | 6-8 hours | Week 1-2 |
| **P0 + P1 (Materials-Ready)** | ~300 | 16-20 hours | Weeks 1-3 |
| **Full (P0+P1+P2 — Institutional-Grade)** | ~500 | 30-35 hours | Weeks 1-4 |

---

*Version: 1.0 — Created 2026-02-17*
