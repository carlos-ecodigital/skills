# Financiele Modellering / Financial Modeling for Dutch Infrastructure Projects

> **Skill Reference File** -- Project Financing for Dutch Digital Infrastructure
> Last updated: 2026-02-12 | Bilingual NL/EN terminology throughout
> Cross-references to sibling files at bottom

---

## 1. Modelarchitectuur / Model Architecture

### 1.1 Standard PF Model Structure

A Dutch project finance (PF) model for digital infrastructure follows the three-statement integrated approach: **income statement** (resultatenrekening), **balance sheet** (balans), and **cash flow statement** (kasstroomoverzicht). These three statements must reconcile fully in every projection period.

**Periodicity (periodiciteit):**

| Phase | Recommended Period | Rationale |
|---|---|---|
| Construction (bouwfase) | Monthly or quarterly | Captures drawdown timing, IDC accrual |
| Ramp-up (aanloopfase) | Quarterly | Revenue build-up monitoring |
| Operations (exploitatiefase) | Semi-annual or quarterly | Aligned with debt service dates |

**Projection horizon (projectieperiode):**

| Asset Class | Minimum Horizon | Typical Range | Driver |
|---|---|---|---|
| BESS (batterijopslag) | 20 years | 20-25 years | Battery warranty life, degradation tail |
| Colocation Data Center | 15 years | 15-20 years | Lease terms, asset useful life |
| AI Factory (AI-fabriek) | 7 years | 7-10 years | GPU obsolescence, technology risk |
| Hybrid (gemengd) | 15 years | 15-20 years | Weighted by dominant asset |

The model must cover the full loan tenor plus a tail period (staartperiode) of at least 12-24 months beyond final debt maturity. [Source: Forvis Mazars model audit guidance]

### 1.2 Key Model Sheets (Modelbladen)

| Sheet Name | Dutch Equivalent | Purpose |
|---|---|---|
| Timing & Flags | Timing & Schakelaars | Construction/operation toggles, period start/end dates, flag rows for conditional logic |
| Macro Assumptions | Macro-aannames | Inflation (CPI NL via CBS), EURIBOR forward curve, electricity price forecasts, FX if applicable |
| CAPEX | Investeringskosten | Construction costs by category, contingency (onvoorzien), interest during construction (IDC / rente tijdens bouw) |
| Revenue | Opbrengsten | Revenue build-up by stream: arbitrage, FCR, aFRR, colocation fees, GPUaaS, power pass-through |
| OPEX | Operationele kosten | Fixed/variable operating costs, O&M contracts, insurance (verzekering), land lease (erfpacht/huur), management fees |
| Debt | Schuld | Drawdown schedule (trekkingsschema), repayment profile (sculpted/annuity), interest calculation, commitment/arrangement fees |
| Equity | Eigen vermogen | Equity contributions (stortingen), distributions (uitkeringen), IRR calculation (pre-tax and post-tax) |
| Tax | Belasting | Dutch CIT computation (vennootschapsbelasting), earningsstripping test (renteaftrekbeperking), verliesverrekening, innovatiebox |
| Cash Flow Waterfall | Kasstroom waterval | Priority of payments, DSRA funding, maintenance reserve (onderhoudsreserve), distribution lock-up test |
| Returns | Rendement | Equity IRR (pre/post-tax), project IRR, cash-on-cash yield, MOIC |
| Ratios | Ratio's | DSCR, LLCR, PLCR, gearing, lock-up test threshold, default test threshold |
| Sensitivities | Gevoeligheden | Tornado charts, scenario toggles, breakeven analysis |
| Checks | Controles | Balance sheet balancing check, cash balance non-negative, circular reference flag, integrity checks |

### 1.3 Model Standards (Modelstandaarden)

**FAST Methodology** -- the prevailing standard in European PF modeling:

| Principle | Meaning | Application |
|---|---|---|
| **F**lexible | Easy to change assumptions | All inputs in dedicated assumption cells; no hard-coded numbers in formulas |
| **A**ppropriate | Fit for purpose | Level of detail matches decision needs; avoid over-engineering |
| **S**tructured | Logical layout | Consistent flow: left-to-right, top-to-bottom; one row per calculation |
| **T**ransparent | Easy to audit | Every formula readable without deconstruction; clear labels |

[Source: FAST Standard Organisation, www.fast-standard.org]

**Additional NL PF modeling conventions:**

- **Color coding (kleurcodering):** Blue font = hard-coded inputs; Black font = formulas; Green font = links to other sheets; Red font = check cells
- **No circular references** (geen kringverwijzingen): Use macro-based iterations only if unavoidable (e.g., interest-on-cash-balance feedback loops); clearly flag with a dedicated check cell
- **Audit trail (auditspoor):** Every assumption must be traceable to a source document (term sheet, market report, engineer's estimate)
- **Version control (versiebeheer):** Model version number on cover sheet; change log maintained
- **Units row:** Every calculation block includes a units row (EUR, %, MW, MWh, etc.)

---

## 2. Kerngegevens / Key Model Inputs

### 2.1 Macro Assumptions (Macro-aannames)

| Input | Dutch Term | Source | 2025-2026 Value | Update Frequency |
|---|---|---|---|---|
| CPI Netherlands | Consumentenprijsindex | CBS / CPB | 2.0-2.5% annual | Quarterly |
| 3-month EURIBOR | 3-maands EURIBOR | euribor-rates.eu / ECB | ~1.89% (Feb 2026) | Daily (use forward curve) |
| 12-month EURIBOR | 12-maands EURIBOR | euribor-rates.eu / ECB | ~1.92% (Feb 2026) | Daily (use forward curve) |
| 5-year EUR IRS | 5-jaars EUR swap | Bloomberg / Refinitiv | ~2.30% | Daily |
| 10-year EUR IRS | 10-jaars EUR swap | Bloomberg / Refinitiv | ~2.55% | Daily |
| Electricity base price (NL) | Elektriciteitsprijs (NL) | EPEX SPOT / ICE Endex forward | Project-specific; use forward curve | Monthly review |
| Corporate tax rate | Vpb-tarief | Belastingdienst | 19% (first EUR 200K) / 25.8% (excess) | Annual (Belastingplan) |
| Earningsstripping limit | Renteaftrekbeperking | Wet Vpb Art. 15b | 24.5% of fiscal EBITDA (EUR 1M franchise) | Annual |
| BTW standard rate | BTW-tarief | Wet OB 1968 | 21% | Legislative change only |
| Network tariffs (TenneT) | Nettarieven | ACM tariff decisions | Location-specific; EUR 15-50/kW/yr | Annual (ACM besluit) |

[Source: CBS StatLine for CPI; ECB Statistical Data Warehouse for EURIBOR; Belastingdienst.nl for tax rates; ACM.nl for network tariffs]

### 2.2 Asset-Specific Inputs (Activaspecifieke invoer)

#### BESS (Batterij-energieopslagsysteem)

| Parameter | Value Range | Source | Notes |
|---|---|---|---|
| Battery CAPEX (all-in) | EUR 330-700K/MW | BNEF 2025 | Varies by duration (2h vs 4h); includes BOS, EPC |
| EPC contingency | 5-10% of base CAPEX | Industry standard | Higher for novel configurations |
| Interest during construction (IDC) | Calculated | Model output | 12-18 month construction; capitalize at all-in rate |
| Degradation curve (P50) | 1-2% annual capacity loss | Clean Energy Reviews / manufacturer warranty data | LFP chemistry baseline |
| Degradation curve (P90) | 2-3% annual capacity loss | Independent engineer assessment | Used for debt sizing |
| Revenue stacking | Day-ahead spread + FCR + aFRR | EPEX SPOT, TenneT ancillary services data | See Section 8 for detailed methodology |
| Optimal cycling | 300-400 cycles/year | ScienceDirect (Oct 2025) | Balance revenue vs degradation |
| Augmentation CAPEX | 15-25% of initial battery CAPEX | Developer estimates | Triggered at ~80% nameplate capacity |
| Round-trip efficiency (RTE) | 85-90% (LFP, new) | Manufacturer specs | Declining ~0.5% p.a. with age |
| O&M cost | EUR 8-15K/MW/year | O&M contractor quotes | Escalated at CPI |
| Insurance | 0.3-0.5% of replacement cost | Insurance broker quotes | All-risk + liability |
| Land lease (erfpacht/huur) | EUR 5-15K/MW/year | Location-specific | Escalated at CPI; 20-30 year term |

[Source: BNEF Global Energy Storage Outlook 2025; ScienceDirect "Optimal Battery Storage Cycling" Oct 2025; Clean Energy Reviews degradation studies]

#### Colocation Data Center (Colocatie Datacentrum)

| Parameter | Value Range | Source | Notes |
|---|---|---|---|
| Facility CAPEX | EUR 8-12M/MW IT load | Turner & Townsend DC Cost Index | Shell + core; excludes land |
| Fit-out CAPEX (per cage/suite) | EUR 1-3M/MW incremental | Developer estimates | Customer-specific; phased |
| Land cost (grondkosten) | EUR 200-600/m2 | NVM / Funda Zakelijk | Amsterdam metro premium; Groningen/Limburg discount |
| Take-up curve (bezettingsgraad) | 50% Y1 / 75% Y2 / 90% Y3 | CBRE / JLL market data | Conservative; pre-lease reduces risk |
| Wholesale pricing | ~$217/kW/month | CBRE North America Data Center Report Q1 2025 | NL pricing at slight premium to EU avg |
| Retail pricing | $300-500/kW/month | Broker estimates | Higher margin, higher churn |
| Churn rate (verloop) | 5-10% retail; <5% wholesale | Industry benchmark | Model as annual % of occupied capacity |
| PUE (Power Usage Effectiveness) | 1.2-1.4 (air) / 1.05-1.15 (liquid) | Uptime Institute | Critical for power cost modeling |
| O&M cost | 2-4% of CAPEX/year | FM contractor quotes | Includes staffing, maintenance, consumables |
| Insurance | 0.15-0.25% of replacement cost | Broker quotes | Lower per-MW than BESS due to lower hazard profile |

[Source: Turner & Townsend International Construction Market Survey 2025; CBRE Global Data Centre Report Q1 2025; Uptime Institute Annual Survey]

#### AI Factory (AI-Fabriek)

| Parameter | Value Range | Source | Notes |
|---|---|---|---|
| Facility CAPEX (excl. GPU) | EUR 10-15M/MW | Turner & Townsend | Higher spec cooling (liquid), power density |
| GPU CAPEX | Up to EUR 25M/MW additional | NVIDIA pricing / broker market | H100/H200/B200 depending on vintage |
| Total CAPEX (facility + GPU) | EUR 35-40M/MW | Combined estimate | Significantly higher than standard DC |
| GPU refresh reserve | Full replacement every 3-5 years | Technology lifecycle analysis | Critical: model as periodic CAPEX injection |
| Revenue (GPUaaS) | $1.49-4.00/GPU-hr (H100) | GMI Cloud pricing survey | Declining over GPU generation life |
| Utilization target | 70-90% | Operator benchmarks | Higher utilization = better unit economics |
| Power consumption per GPU | 700W (H100) / 1000W+ (B200) | NVIDIA spec sheets | Determines MW-to-GPU ratio |
| O&M cost | 3-5% of facility CAPEX/year | Operator estimates | Higher than standard DC due to cooling complexity |
| Technology risk premium | +200-400 bps on required equity IRR | Investor feedback | Reflects obsolescence risk |

[Source: Turner & Townsend; GMI Cloud GPU Pricing Index; NVIDIA product specifications]

---

## 3. Nederlandse belastingmodellering / Dutch Tax Modeling

### 3.1 CIT Computation (Vpb-berekening)

The Dutch corporate income tax (vennootschapsbelasting, Vpb) computation in a PF model follows these steps:

| Step | Description (NL) | Description (EN) | Formula |
|---|---|---|---|
| 1 | Omzet - OPEX | Revenue - OPEX | = EBITDA |
| 2 | EBITDA - afschrijving | EBITDA - depreciation - amortization | = EBIT |
| 3 | EBIT - netto rente | EBIT - net interest (pre-earningsstripping) | = Pre-adjustment taxable income |
| 4 | Renteaftrekbeperking toets | Earningsstripping test (Art. 15b Wet Vpb) | Max deductible = MAX(EUR 1M, 24.5% x fiscal EBITDA) |
| 5 | Niet-aftrekbare rente | Disallowed interest add-back | Added to taxable income; carry-forward indefinitely |
| 6 | Verliesverrekening | Loss offset | EUR 1M + 50% of excess taxable profit offset against prior losses |
| 7 | Belastbaar bedrag | Taxable amount | After loss offset |
| 8 | Vpb berekening | CIT calculation | 19% on first EUR 200K + 25.8% on remainder |
| 9 | Innovatiebox toets | Innovation box check | 9% rate on qualifying IP income (if applicable) |
| 10 | Te betalen Vpb | CIT payable | Net of provisional assessments |

[Source: Belastingdienst.nl; Wet op de vennootschapsbelasting 1969; PwC Belastingplan 2025 analysis]

### 3.2 Earningsstripping Impact (Impact renteaftrekbeperking)

The earningsstripping rule (Art. 15b Wet Vpb) is **critical** for high-leverage project SPVs.

**Mechanism:**
- Maximum deductible net interest expense (saldo aan renten) = greater of EUR 1M or 24.5% of fiscal EBITDA
- **Fiscal EBITDA** for this purpose: taxable profit + net interest + depreciation + amortization (not identical to accounting EBITDA)
- Excess interest is added back to taxable income
- Disallowed interest carries forward indefinitely (onbeperkte voortwenteling)
- The EUR 1M franchise (drempel) means small projects with annual net interest below EUR 1M are unaffected

**Illustrative impact at typical leverage:**

| Scenario | Gearing (D/(D+E)) | All-in Interest Rate | Annual Interest (EUR M) | Fiscal EBITDA (EUR M) | 24.5% Threshold | Disallowed Interest | Effective Tax Uplift |
|---|---|---|---|---|---|---|---|
| BESS 100MW/4h contracted | 75% | 5.5% | 8.3 | 18.0 | 4.4 | 3.9 | ~EUR 1.0M additional Vpb |
| BESS 100MW/4h merchant | 50% | 6.5% | 4.9 | 14.0 | 3.4 | 1.5 | ~EUR 0.4M additional Vpb |
| DC 10MW wholesale | 70% | 5.0% | 7.0 | 22.0 | 5.4 | 1.6 | ~EUR 0.4M additional Vpb |
| AI Factory 5MW | 55% | 7.0% | 4.8 | 12.0 | 2.9 | 1.9 | ~EUR 0.5M additional Vpb |

**Rate history:** Increased from 20% to 24.5% effective 1 January 2025 as part of Belastingplan 2025 [Source: PwC Tax News, Belastingplan 2025]

**Modeling note:** The earningsstripping calculation must be performed on a per-entity basis. A fiscale eenheid (fiscal unity) computes this at the consolidated level, which may be advantageous if one entity has high EBITDA and another has high interest.

### 3.3 Fiscale Eenheid (Fiscal Unity)

A fiscale eenheid allows a parent company and its 95%+ owned Dutch subsidiaries to be treated as a single taxpayer for Vpb purposes.

| Feature | Implication for PF Model |
|---|---|
| Consolidated tax return (geconsolideerde aangifte) | Single Vpb computation for all entities in unity |
| Intercompany elimination (intercompany eliminatie) | Transactions between unity members ignored for Vpb |
| Loss offset between entities (verliesverrekening) | Profits of one entity offset against losses of another |
| Earningsstripping at group level | 24.5% test applied to consolidated fiscal EBITDA |
| Joint and several liability (hoofdelijke aansprakelijkheid) | All members liable for group Vpb -- lender concern |

**Modeling approach:**
- Model both scenarios: (a) separate entity Vpb computations, (b) fiscale eenheid consolidated
- Present delta to stakeholders
- Note: lenders may restrict fiscale eenheid formation to protect ring-fencing of project SPV

[Source: Wet Vpb 1969, Art. 15-15aj; Belastingdienst guidance on fiscale eenheid]

### 3.4 BTW Recovery (BTW-terugvordering)

| Item | Treatment | Notes |
|---|---|---|
| Construction CAPEX BTW (21%) | Fully recoverable | SPV must be BTW-registered (BTW-geregistreerd) |
| Verleggingsregeling (reverse charge) | No BTW cash outflow on NL construction services | Subcontractor invoices without BTW; SPV self-accounts |
| Imported equipment BTW | Recoverable via BTW return | May cause temporary cash flow impact |
| Pre-registration BTW | Recoverable if registration obtained within reasonable time | Ensure registration before first invoice; discuss with adviseur |
| Exempt supplies (vrijgestelde prestaties) | BTW on related costs NOT recoverable | Rare in digital infra; check if any revenue is BTW-exempt |
| Pro rata (evenredigheidsbeginsel) | Partial recovery if mixed taxable/exempt | Calculate recovery percentage annually |

**Cash flow timing:** BTW returns filed monthly or quarterly. Model the timing difference between BTW payment on supplier invoices and BTW recovery via returns. During construction, this can represent a significant working capital requirement (werkkapitaalbehoefte).

[Source: Wet op de omzetbelasting 1968; Belastingdienst BTW guidance]

---

## 4. Schuldberekening / Debt Sizing Methodology

### 4.1 DSCR-Based Sizing (Op basis van DSCR)

The Debt Service Coverage Ratio (DSCR) is the primary debt sizing tool in Dutch PF:

**Definition:**
```
DSCR = Cash Flow Available for Debt Service (CFADS) / Debt Service (interest + principal)
```

**Sizing process:**

| Step | Action | Detail |
|---|---|---|
| 1 | Set target minimum DSCR | E.g., 1.25x for contracted BESS; 1.40x for merchant |
| 2 | Project CFADS for each period | Revenue - OPEX - tax - working capital changes |
| 3 | Calculate maximum debt service per period | CFADS / target DSCR |
| 4 | Determine repayment profile | Sculpted (gemodelleerd) to match CFADS shape; or annuity (annuiteit) |
| 5 | Derive maximum debt | NPV of debt service stream discounted at all-in cost of debt |
| 6 | Cross-check against gearing cap | Ensure D/(D+E) does not exceed maximum allowed |
| 7 | Cross-check against LLCR | Ensure LLCR above minimum at all times |

**Sculpted repayment (gemodelleerde aflossing):** Principal repayment in each period is set so that DSCR equals the target in every period. This maximizes debt capacity but creates uneven amortization.

**Annuity repayment (annuiteitsaflossing):** Equal total debt service payments. Simpler but may under-utilize debt capacity in high-CFADS periods.

[Source: Standard PF modeling methodology; Forvis Mazars / BDO audit frameworks]

### 4.2 LLCR-Based Sizing (Op basis van LLCR)

**Loan Life Coverage Ratio (LLCR):**

```
LLCR = NPV(CFADS over remaining loan life) / Outstanding Debt Balance
```

| Parameter | Typical Minimum | Context |
|---|---|---|
| LLCR lock-up | 1.15x-1.20x | Distribution lock-up trigger |
| LLCR default | 1.05x-1.10x | Event of default trigger |
| LLCR sizing | 1.20x minimum | Debt sizing constraint |

The LLCR is a forward-looking measure that complements the period-by-period DSCR. It is more conservative for projects with lumpy or back-loaded cash flow profiles because it considers the entire remaining debt tenor.

### 4.3 PLCR (Project Life Coverage Ratio)

```
PLCR = NPV(CFADS over remaining project life) / Outstanding Debt Balance
```

The PLCR extends beyond loan maturity to capture the full economic life of the asset. It provides comfort that the project generates sufficient value to repay debt even if refinancing is required.

| Ratio | Horizon | Typical Minimum | Use |
|---|---|---|---|
| DSCR | Single period | 1.20x-1.40x | Period debt service adequacy |
| LLCR | Remaining loan life | 1.15x-1.25x | Loan life debt coverage |
| PLCR | Remaining project life | 1.30x-1.50x | Full project value coverage |

### 4.4 Gearing Cap (Maximale hefboom)

Maximum debt-to-total-capitalization ratio applied as an additional sizing constraint:

| Asset / Risk Profile | Maximum D/(D+E) | Rationale |
|---|---|---|
| BESS -- fully contracted (FCR/aFRR) | 70-80% | Predictable revenue stream |
| BESS -- merchant / hybrid | 40-60% | Revenue volatility |
| Colocation DC -- pre-let >70% | 65-75% | Contracted colocation revenue |
| Colocation DC -- speculative build | 50-60% | Take-up risk |
| AI Factory -- contracted GPUaaS | 55-65% | Technology risk despite contracts |
| AI Factory -- speculative | 40-50% | High technology + market risk |

[Source: Market practice per lender interviews; see also [references/debt-instruments.md](references/debt-instruments.md)]

### 4.5 Cash Flow Waterfall (Kasstroom waterval)

Standard priority of payments in a Dutch PF SPV:

| Priority | Payment | Dutch Term | Notes |
|---|---|---|---|
| 1 | Operating expenses | Operationele kosten | OPEX, O&M, insurance, land lease |
| 2 | Senior debt interest | Rente senior schuld | Per interest period |
| 3 | Senior debt principal | Aflossing senior schuld | Per amortization schedule |
| 4 | DSRA top-up | Aanvulling DSRA | Typically 6 months forward debt service |
| 5 | Maintenance reserve top-up | Aanvulling onderhoudsreserve | Per independent engineer schedule |
| 6 | Cash sweep (if applicable) | Versnelde aflossing | Excess cash applied to prepayment |
| 7 | Subordinated debt service | Achtergestelde schuld | If applicable (mezzanine, shareholder loans) |
| 8 | Tax payments | Belastingbetalingen | Vpb, BTW (net) |
| 9 | Working capital | Werkkapitaal | Seasonal fluctuations |
| 10 | Equity distributions | Uitkeringen eigen vermogen | Subject to lock-up DSCR test (e.g., 1.15x-1.20x) |

**Distribution lock-up test (uitkeringstoets):**
- Historical DSCR (trailing 12 months) must exceed lock-up threshold (e.g., 1.15x)
- Projected DSCR (forward 12 months) must exceed lock-up threshold
- No outstanding event of default or potential event of default
- All reserves fully funded
- All representations and warranties true

---

## 5. Rendementsanalyse / Returns Analysis

### 5.1 Equity Returns Metrics (Rendementsmaatstaven)

| Metric | Dutch Term | Definition | Typical Target Range | Notes |
|---|---|---|---|---|
| Pre-tax equity IRR | Rendement eigen vermogen (voor belasting) | IRR on equity cash flows before corporate tax | 10-15% (contracted); 15-20%+ (merchant/AI) | Primary negotiation metric |
| Post-tax equity IRR | Rendement eigen vermogen (na belasting) | IRR on equity cash flows after Dutch Vpb | 8-12% (contracted); 12-18% (merchant/AI) | Actual investor return |
| Cash-on-cash yield | Kasstroom rendement | Annual distribution / total equity invested | 8-12% stabilized | Relevant for income-focused investors |
| MOIC | Multiple on Invested Capital | Total distributions / total equity contributions | 1.8-2.5x over fund life | Key for PE/infrastructure funds |
| Payback period | Terugverdientijd | Years until cumulative distributions = equity invested | 5-8 years | Quick metric for investor committees |
| Project IRR (unlevered) | Project rendement (ongehefboomd) | IRR on total project cash flows (pre-debt, pre-tax) | 7-10% (contracted); 10-14% (merchant) | Measure of asset quality |

### 5.2 Blended Returns and Leverage Effect (Hefboomeffect)

The **leverage effect** (hefboomeffect) amplifies equity returns when the project IRR exceeds the cost of debt:

```
Equity IRR > Project IRR   when   Project IRR > Cost of Debt
Equity IRR < Project IRR   when   Project IRR < Cost of Debt
```

**Illustrative leverage impact (BESS 100MW/4h):**

| Gearing | Project IRR | Cost of Debt | Equity IRR (pre-tax) | Amplification |
|---|---|---|---|---|
| 0% (all equity) | 9.5% | n/a | 9.5% | 1.0x |
| 50% | 9.5% | 5.5% | 12.8% | 1.35x |
| 70% | 9.5% | 5.5% | 16.2% | 1.71x |
| 80% | 9.5% | 5.5% | 20.1% | 2.12x |

**Caution:** Higher gearing also amplifies downside risk. A 10% revenue shortfall at 80% gearing may eliminate equity distributions entirely, while at 50% gearing the impact is manageable.

### 5.3 IRR Computation Method

- **Timing:** Use XIRR (not IRR) to account for irregular cash flow dates
- **Equity cash flows:** Negative = equity contributions (stortingen); Positive = distributions (uitkeringen)
- **Terminal value:** If model horizon does not capture full asset life, include a terminal/residual value (restwaarde) -- typically conservative (e.g., 0-5x terminal EBITDA for BESS)
- **Tax treatment:** Post-tax IRR applies Dutch Vpb computed in the model (including earningsstripping impact)

---

## 6. Gevoeligheidsanalyse / Sensitivity Analysis

### 6.1 Standard Sensitivities (Standaard gevoeligheden)

| Variable | Dutch Term | Base Case | Downside | Upside | Impact Metric |
|---|---|---|---|---|---|
| Electricity price | Elektriciteitsprijs | Forward curve | -20% | +20% | Equity IRR, DSCR |
| CAPEX overrun | Kostenoverschrijding | Budget (EPC contract) | +10% | -5% | Equity IRR, gearing |
| OPEX increase | OPEX stijging | Budget | +15% | -10% | DSCR, equity IRR |
| Degradation (BESS) | Degradatie | P50 curve | P90 curve | P10 curve | Revenue, DSCR |
| Take-up rate (DC) | Bezettingsgraad | 50/75/90% Y1/Y2/Y3 | 30/50/75% | 70/90/95% | Revenue, DSCR |
| Utilization (AI) | Bezettingsgraad GPU | 80% | 60% | 90% | Revenue, equity IRR |
| Interest rate | Rente | Forward curve | +100 bps | -50 bps | Debt service, equity IRR |
| Inflation (CPI) | Inflatie | 2.0% | 1.0% | 3.5% | OPEX, revenue (if indexed) |
| Construction delay | Bouwvertraging | On schedule | +6 months | -- | IDC, delayed revenue |
| Currency (if applicable) | Wisselkoers | Spot | +/-10% | +/-10% | CAPEX (imported equipment) |
| Tax rate change | Vpb-tarief wijziging | Current (25.8%) | +2% (27.8%) | -2% (23.8%) | Post-tax equity IRR |

### 6.2 Scenario Analysis (Scenarioanalyse)

| Scenario | Description | Key Assumptions | Purpose |
|---|---|---|---|
| Base case (basisscenario) | Management's best estimate | P50 revenue, budget CAPEX/OPEX, forward rates | Primary valuation |
| Downside (neerwaarts) | Stressed but plausible | P75/P90 revenue, +10% CAPEX, +15% OPEX, +6mo delay | Risk assessment |
| Upside (opwaarts) | Favorable outcomes | P25 revenue, -5% CAPEX, -10% OPEX, faster take-up | Opportunity sizing |
| Banker's case (bankiersscenario) | Conservative for debt sizing | P90 revenue (BESS), P75 take-up (DC), higher OPEX | Debt capacity determination |
| Breakeven (break-even) | Minimum viable | Solve for min revenue at DSCR = 1.0x | Stress threshold |
| Refinancing | Debt repricing at maturity | +50-100 bps margin; shorter tenor | Mini-perm exit risk |

### 6.3 Advanced Sensitivity Techniques

- **Tornado chart (tornadodiagram):** Rank sensitivities by impact magnitude on equity IRR; identifies key value drivers
- **Spider chart (spindiagram):** Plot equity IRR against % change in each variable; shows linearity/convexity of sensitivities
- **Two-way data tables:** Electricity price x CAPEX; utilization x pricing; gearing x interest rate
- **Monte Carlo simulation:** For merchant revenue streams (BESS arbitrage, spot pricing); requires probability distributions for key inputs; output = distribution of equity IRR/DSCR with confidence intervals

---

## 7. Modelaudit / Model Audit

### 7.1 NL-Active Model Audit Firms

| Firm | Professionals / Track Record | Specialization | Notes |
|---|---|---|---|
| Forvis Mazars (Corality) | 120+ professionals, 1,000+ project audits | Energy, infrastructure, PPP | Global market leader; strong NL presence |
| Operis | Model Auditor of the Year (multiple awards); OAK software | Infrastructure, energy, transport | UK-headquartered; active across EU including NL |
| BDO | 25+ years experience, 2,500+ project audits | Broad infrastructure, renewables | Strong NL office; cost-competitive |
| Gridlines | 100+ audits since 2017 | Infrastructure, digital, energy storage | Specialist boutique; growing NL practice |
| Rebel Group | NL-headquartered | Transport, social infrastructure | Advisory + audit combined offering |

[Source: Firm websites and industry directories; Infrastructure Journal league tables]

### 7.2 Audit Process (Auditproces)

| Phase | Activity | Typical Duration |
|---|---|---|
| 1. Scoping | Define audit scope, agree on deliverables, sign engagement letter | 1-2 weeks |
| 2. Structural review | Check model architecture, layout, consistency with FAST principles | 1 week |
| 3. Logic review | Test every formula for logical integrity and accuracy | 2-4 weeks |
| 4. Assumption review | Verify assumptions against source documents (term sheet, reports) | 1-2 weeks |
| 5. Sensitivity testing | Run scenarios, check model behavior under stress | 1 week |
| 6. Reporting | Issue model audit report with findings and opinion | 1-2 weeks |
| **Total** | | **6-12 weeks** |

**Audit opinion types:**

| Opinion | Meaning |
|---|---|
| Clean (schoon) | No material issues; model fit for purpose |
| Qualified (met voorbehoud) | Material issues identified but limited in scope; model usable with caveats |
| Adverse (afkeurend) | Fundamental issues; model not fit for purpose; must be remediated |

**Cost:** EUR 25,000-75,000 depending on model complexity, number of scenarios, and asset class. BESS models typically at lower end; multi-asset portfolio models at upper end.

**Lender requirement:** All Dutch PF transactions require a model audit report from an independent firm acceptable to the lender group. The model audit report is a condition precedent (opschortende voorwaarde) to financial close.

[Source: Industry practice; lender term sheet requirements]

---

## 8. BESS Revenue Modeling Specifics (BESS Opbrengstenmodellering)

### 8.1 Revenue Stacking Model (Gestapeld opbrengstenmodel)

BESS revenue in the Netherlands is typically modeled as a stack of multiple revenue streams:

| Revenue Stream | Dutch Term | Mechanism | Typical Share of Revenue | Contracted/Merchant |
|---|---|---|---|---|
| Day-ahead arbitrage | Dagmarkt arbitrage | Buy low / sell high on EPEX SPOT | 30-50% | Merchant |
| FCR (Frequency Containment Reserve) | FCR | Capacity reservation for grid frequency | 20-35% | Semi-contracted (weekly/monthly auctions) |
| aFRR (Automatic Frequency Restoration Reserve) | aFRR | Capacity + energy for frequency restoration | 15-30% | Semi-contracted (daily auctions) |
| Intraday trading | Intraday handel | Continuous intraday market optimization | 5-15% | Merchant |
| Negative price avoidance | Negatieve prijzen vermijding | Charge during negative price hours | 5-10% | Merchant |
| Imbalance market | Onbalansenmarkt | Real-time imbalance settlement | 0-10% | Merchant |

**Negative price hours:** 423 hours recorded in Jan-Jul 2025 in the Netherlands, creating significant charging opportunities for BESS [Source: ComCam Energy analysis]

**Modeling approach:**
- Use historical price data (minimum 3 years) to calibrate spread distributions
- Apply P50/P90 methodology: P50 for equity case, P90 for banker's case
- Account for capture rate (vangstpercentage): BESS does not capture full theoretical spread
- Apply revenue cannibalization factor as BESS deployment increases
- Optimal dispatch: 300-400 cycles/year balances revenue maximization against battery degradation [Source: ScienceDirect, Oct 2025]

### 8.2 Degradation Curves (Degradatiecurves)

| Metric | P50 (Base Case) | P90 (Banker's Case) | P10 (Upside) |
|---|---|---|---|
| Annual capacity loss | 1-2% | 2-3% | 0.5-1% |
| Year 10 capacity (% of nameplate) | 82-90% | 73-82% | 90-95% |
| Year 15 capacity (% of nameplate) | 73-83% | 60-73% | 85-90% |
| Augmentation trigger | ~80% nameplate | ~80% nameplate | May not be needed |
| Augmentation timing | Year 8-12 | Year 6-9 | Year 12+ |

**Augmentation modeling:**
- Reserve CAPEX line for battery module replacement/addition
- Triggered when capacity drops below contractual minimum or economic threshold
- CAPEX: 15-25% of initial battery CAPEX (module cost only; BOS reused)
- Resets degradation curve for augmented portion
- Must be included in CFADS projection for debt sizing

[Source: Clean Energy Reviews; independent engineer reports; manufacturer warranty curves]

---

## 9. DC Revenue Modeling Specifics (DC Opbrengstenmodellering)

### 9.1 Take-up Model (Bezettingsmodel)

| Phase | Typical Occupancy | Duration | Revenue Recognition |
|---|---|---|---|
| Pre-lease (voorverhuur) | 0-30% at financial close | Before COD | Letters of intent / signed leases |
| Year 1 ramp-up | 50% average | 12 months | Phased move-in |
| Year 2 growth | 75% average | 12 months | Continued leasing |
| Year 3 stabilization | 90% target | 12 months | Near full occupancy |
| Steady state (stabiele fase) | 85-95% | Ongoing | Net of churn |

**Churn modeling (verloopmodellering):**

| Segment | Annual Churn Rate | Average Lease Term | Replacement Period |
|---|---|---|---|
| Wholesale (wholesale) | <5% | 5-15 years | 3-6 months |
| Retail (retail) | 5-10% | 1-3 years | 1-3 months |
| Enterprise (zakelijk) | 3-7% | 3-5 years | 2-4 months |

**Pricing:**
- Amsterdam wholesale colocation: approximately $217/kW/month [Source: CBRE North America Data Center Report Q1 2025, with NL adjustment]
- Pricing escalation: typically CPI-linked or fixed 2-3% annual escalator in lease agreements
- Power cost: typically passed through to customer at PUE-adjusted rate plus margin

### 9.2 Power Cost Modeling (Energiekostenmodellering)

| Component | Description | Typical Value (NL) |
|---|---|---|
| Commodity cost (grondstofkosten) | Wholesale electricity price | Per forward curve (EPEX SPOT / ICE Endex) |
| Network tariffs (nettarieven) | TenneT / regional DSO charges | EUR 15-50/kW/year [Source: ACM tariff decisions] |
| Renewable energy surcharge (ODE) | Opslag Duurzame Energie | Per kWh; varies annually |
| Energiebelasting | Energy tax | Degressive rate per kWh; reduced for large consumers |
| PUE multiplier | Total facility power / IT load power | 1.2-1.4x (air) / 1.05-1.15x (liquid) |
| Pass-through margin | Markup on power cost to customer | 5-15% or fixed per-kWh markup |
| PPA overlay | Corporate PPA for green sourcing | Fixed price or CfD structure; see [references/debt-instruments.md](references/debt-instruments.md) |

**Model calculation:**
```
Total power cost = IT Load (MW) x PUE x Hours x (Commodity + Network + ODE + EB) x (1 + margin)
Customer power revenue = IT Load (MW) x PUE x Hours x Customer rate
Power margin = Customer power revenue - Total power cost
```

---

## 10. Modelcontroles / Model Integrity Checks

### 10.1 Standard Check List

| Check | Formula Logic | Expected Result |
|---|---|---|
| Balance sheet balances | Total Assets - Total Liabilities - Equity = 0 | Zero in all periods |
| Cash balance non-negative | MIN(cash balance) >= 0 | True |
| Debt balance at maturity | Debt outstanding at final maturity date | Zero |
| DSRA funding | DSRA balance >= required level | True in all operational periods |
| Circular reference flag | Excel IFERROR check on iteration | No circulars (or controlled iteration) |
| Tax loss carry-forward | Losses correctly tracked and utilized | Reconciles with Vpb computation |
| BTW recovery | Construction BTW recovered within expected period | Reconciles with BTW return schedule |
| Equity IRR cross-check | XIRR of equity cash flows vs manual check | Consistent |
| Sum of parts | Sum of revenue streams = total revenue | True in all periods |
| Construction CAPEX | Total drawdown = total project cost | Reconciles at COD |

### 10.2 Error Handling

- Dedicate a "Checks" sheet (controlevel) summarizing all integrity checks
- Use conditional formatting: green = pass, red = fail
- Model should not be distributed or relied upon if any check fails
- Audit firms will flag unresolved check failures as qualifications

---

## 11. Modelsjabloon Structuur / Model Template Structure

### 11.1 Recommended File Organization

```
/Project_Name_Financial_Model_v[X.X].xlsx
  |-- Cover (Voorblad)           -- Project name, version, date, author, status
  |-- ToC (Inhoudsopgave)        -- Hyperlinked table of contents
  |-- Checks (Controles)         -- All integrity checks in one view
  |-- Timing (Timing)            -- Dates, flags, period counters
  |-- Macro (Macro-aannames)     -- Inflation, rates, prices
  |-- CAPEX (Investeringen)      -- Construction costs, contingency, IDC
  |-- Revenue (Opbrengsten)      -- Revenue by stream
  |-- OPEX (Bedrijfskosten)      -- Operating cost detail
  |-- Debt (Schuld)              -- Drawdown, repayment, interest, fees
  |-- Equity (Eigen vermogen)    -- Contributions, distributions
  |-- Tax (Belasting)            -- Vpb, earningsstripping, BTW
  |-- Waterfall (Waterval)       -- Cash flow priority of payments
  |-- IS (Resultatenrekening)    -- Income statement
  |-- BS (Balans)                -- Balance sheet
  |-- CF (Kasstroomoverzicht)    -- Cash flow statement
  |-- Returns (Rendement)        -- IRR, MOIC, payback
  |-- Ratios (Ratio's)           -- DSCR, LLCR, PLCR, gearing
  |-- Sensitivities (Gevoelig.)  -- Scenarios, tornado, data tables
  |-- Dashboard (Dashboard)      -- Summary charts and KPIs
```

---

## 12. Veelgebruikte Formules / Common PF Formulas

| Metric | Formula | Notes |
|---|---|---|
| DSCR | CFADS / (Interest + Principal) | Per period |
| LLCR | NPV(CFADS, remaining loan life) / Debt Outstanding | Discount at WACD |
| PLCR | NPV(CFADS, remaining project life) / Debt Outstanding | Discount at WACD |
| Gearing | Debt / (Debt + Equity) | At financial close |
| Equity IRR | XIRR(equity cash flows, dates) | Pre-tax and post-tax |
| Project IRR | XIRR(project cash flows, dates) | Unlevered, pre-tax |
| MOIC | Sum(distributions) / Sum(contributions) | Undiscounted |
| Cash-on-cash | Annual distribution / Total equity invested | Per year |
| Payback | First period where cumulative distributions >= equity | Years from first contribution |
| Sculpted principal | CFADS / Target DSCR - Interest | Per period |
| IDC | Cumulative drawn debt x interest rate x day count | During construction |
| Fiscal EBITDA | Taxable profit + net interest + depreciation + amortization | For earningsstripping test |

---

## 13. Disclaimer / Vrijwaring

Financial model outputs are **projections** (prognoses) based on assumptions that may not materialize. Actual results will vary, potentially materially, from modeled outcomes.

- All tax rates and rules per 2025/2026 legislation; subject to change via annual Belastingplan
- Market data (EURIBOR, electricity prices, CAPEX benchmarks) are point-in-time and will change
- This reference file does not constitute **beleggingsadvies** (investment advice), **juridisch advies** (legal advice), or **fiscaal advies** (tax advice)
- Consult qualified Dutch tax advisors (belastingadviseurs), legal counsel (advocaten), and financial advisors for project-specific guidance
- All sources cited should be independently verified for the most current data

---

## Cross-References (Kruisverwijzingen)

| Topic | Reference File |
|---|---|
| Debt instruments, term sheets, lender landscape | [references/debt-instruments.md](references/debt-instruments.md) |
| BESS technology, market, project specifics | [references/bess-projects.md](references/bess-projects.md) |
| Colocation data center operations and market | [references/colocation-data-centers.md](references/colocation-data-centers.md) |
| AI factory technology, GPU economics | [references/ai-factories.md](references/ai-factories.md) |
| Netherlands legal, regulatory, tax framework | [references/netherlands-legal-framework.md](references/netherlands-legal-framework.md) |

---

*This reference file is maintained as part of the DE Claude Project Financing skill. Updates should reflect current Dutch tax legislation, market rates, and industry benchmarks.*
