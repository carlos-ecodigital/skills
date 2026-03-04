# Energy Project Finance -- Overview

## Scope

Project finance structuring for energy and digital infrastructure assets: Battery Energy Storage Systems (BESS), colocation data centers, AI factories / GPU compute facilities, and hybrid configurations. Covers non-recourse debt, equity structuring, risk allocation, financial modeling, and transaction execution.

For jurisdiction-specific legal frameworks, tax treatment, permitting, and regulatory bodies, see `jurisdictions/nl/` and `jurisdictions/no/` (or UK/US when available).

---

## Core PF Metrics Quick Reference

| Metric | Definition | Typical Range | Notes |
|---|---|---|---|
| DSCR (Debt Service Coverage Ratio) | Net cash flow / debt service | 1.20x--1.40x senior | Minimum covenant level; lender sizing metric |
| LLCR (Loan Life Coverage Ratio) | NPV cash flows over loan life / outstanding debt | >1.20x | Primary lender sizing metric |
| PLCR (Project Life Coverage Ratio) | NPV cash flows over project life / outstanding debt | >1.30x | Tail risk comfort; longer horizon than LLCR |
| Gearing (D:E) | Debt / (Debt + Equity) | 50--80% | Varies by asset class and revenue certainty |
| Lock-up DSCR | Threshold below which distributions blocked | 1.10x--1.20x | Cash sweep trigger for equity distributions |
| Default DSCR | Threshold triggering lender step-in | 1.05x--1.10x | Event of default; triggers cure period |

---

## Asset Class Comparison

| Parameter | AI Factories | Colocation DC | BESS |
|---|---|---|---|
| Typical CAPEX | EUR 10--15M/MW excl. GPUs; up to EUR 40M/MW incl. GPUs | EUR 8--12M/MW | EUR 330--700K/MW (2--4hr LFP) |
| Gearing | 50--65% | 65--75% (contracted) | 70--80% (contracted); 40--60% (merchant) |
| Revenue model | GPUaaS ($1.49--4.00/GPU-hr H100); training/inference contracts | Colocation ~$217/kW/month wholesale; interconnection | Arbitrage (EPEX SPOT NL spread 83--121 EUR/MWh); FCR (~EUR 13/MW/h); aFRR |
| EV/EBITDA multiple | 25--30x (platform); emerging | 19--26x (public REITs) | N/A -- revenue-based |
| Construction period | 18--30 months | 18--36 months | 6--12 months |
| PF track record | Emerging (<3 years) | Established (10+ years) | Growing (5+ years) |
| Technology risk | High (GPU obsolescence) | Low (mature) | Medium (battery degradation) |
| Typical debt tenor | 5--7 years | 7--15 years | 5--15 years |

Sources: Turner & Townsend DCCI 2025-2026; BNEF 2025; CBRE Q1 2025; GMI Cloud 2025; Synertics 2025.

---

## Financing Instruments Overview

- **Senior secured non-recourse debt:** EURIBOR + 200--250 bps average (range 40--600 bps); IG infra debt total return ~4.25--4.75% EUR
- **Green bonds / Sustainability-linked loans:** Greenium effectively ~1 bp in EUR market; EU Green Bond Standard operational
- **Public development banks:** Invest-NL (EUR 1.145B cumulative, 89 investments); EIB (EUR 100B 2025 ceiling; >EUR 11B for power grids + storage; AI Gigafactories EUR 20B target)
- **Institutional investors:** Dutch pension funds (APG/ABP, PGGM/PFZW) and insurers (a.s.r., NN Group, Aegon AM) increasingly active in infrastructure debt and equity

For detailed debt structuring, see `debt-instruments.md`.
For equity structures and distribution waterfalls, see `equity-structures.md`.

---

## Risk Framework Overview

Key risk categories for infrastructure project finance:

| Category | Key Considerations |
|---|---|
| Construction | EPC wrap (UAV 2012 / UAV-GC 2025 / FIDIC); delay LDs; performance guarantees; DSU insurance |
| Technology | Per asset class -- degradation (BESS), obsolescence (AI), maturity (DC) |
| Revenue / Market | Contracted vs merchant; ancillary service market changes; price erosion (GPU) |
| Regulatory / Political | Permitting regime; moratoriums; energy law changes; subsidy policy |
| Grid connection | Congestion (transportschaarste in NL); cable pooling; TDTR; queue management |
| Force majeure | Contractual definition critical; grid congestion is foreseeable (not FM in NL post-2020) |
| Insurance | CAR/EAR, PAR/ISR, BI, cyber; BESS-specific fire/thermal; degradation NOT covered |
| Environmental | Soil investigation (NEN standards); nitrogen deposition (AERIUS); Natura 2000 |

For detailed risk allocation matrix, see `risk-allocation.md`.

---

## Financial Modeling Overview

Standard PF model architecture: three-statement integrated model (income statement, balance sheet, cash flow). FAST methodology as prevailing standard.

Key components:
- Periodicity: monthly/quarterly (construction) → semi-annual/quarterly (operations)
- Debt sizing: DSCR sculpting as primary method; LLCR/PLCR as secondary checks; gearing cap
- Cash flow waterfall: OPEX → senior debt interest → principal → DSRA → maintenance reserve → cash sweep → subordinated debt → tax → working capital → equity distributions
- Sensitivity analysis: tornado charts, scenario analysis (base/downside/upside/banker's case), breakeven
- Model audit: required as condition precedent to financial close

For detailed modeling methodology, see `financial-modeling.md`.

---

## Due Diligence Overview

Workstreams: corporate, project agreements, permits/regulatory, technical, financial, environmental, insurance, jurisdiction-specific items.

Key bankability thresholds:
- EPC: lump-sum turnkey; IG contractor or parent guarantee
- Revenue: 50%+ contracted or quasi-contracted
- Technology: proven (2+ years operational data); LFP preferred for BESS
- Grid: confirmed connection or formal agreement
- Permits: final and binding (onherroepelijk); no pending appeals
- Insurance: comprehensive programme; A-rated insurers
- Model: clean audit opinion from recognized firm
- Sponsor: credible track record; adequate equity commitment

For detailed DD checklist, see `due-diligence-checklist.md`.

---

## Reference File Index

| File | Content |
|---|---|
| `overview.md` | This file -- PF metrics, asset comparison, framework summaries |
| `financial-modeling.md` | Model architecture, inputs, tax modeling, debt sizing, sensitivity analysis |
| `debt-instruments.md` | Senior debt, construction facilities, pricing, bank landscape, green bonds, security package, covenants |
| `equity-structures.md` | BV share structure, SHA provisions, JV structures, distribution waterfalls, institutional investors |
| `risk-allocation.md` | Construction, technology, market, regulatory, environmental risk matrices |
| `epc-contracts.md` | EPC/construction contract terms, performance guarantees, LDs, battery degradation, grid, commissioning |
| `bess-specific.md` | BESS revenue models, energy market, technology risk, SDE++, cable pooling, capital structure |
| `ai-factories.md` | GPU compute, technology risk, revenue models, capital structure, EU AI Act |
| `colocation-data-centers.md` | DC market, revenue models, CAPEX, regulation, waste heat, technology risk |
| `due-diligence-checklist.md` | Comprehensive DD checklist by workstream |
| `sources-and-references.md` | Bibliography and source index |
| `examples/term-sheet-template.md` | Indicative term sheet template with placeholders |

---

## Disclaimers

- All rates, thresholds, and regulatory references are based on 2025/2026 legislation and market data. Verify current rates at primary sources before reliance.
- Market metrics (CAPEX, revenue, multiples, spreads) are sourced from published reports and are indicative. Obtain independent valuations for transaction-specific pricing.
- This specialization does not constitute legal advice, tax advice, or investment advice. Consult qualified advisers for specific transactions.
- For jurisdiction-specific legal frameworks, consult the relevant jurisdiction files under `jurisdictions/`.
