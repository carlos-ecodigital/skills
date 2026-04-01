---
name: m-market-research
description: "Market research intake module: 3-layer intake (screening 10 Qs, core 75 Qs across 7 categories with track filtering, cross-reference validation 9 tests) for Seed/Growth/Institutional tracks"
type: intake-module
version: 2.0
last_updated: 2026-03-31
depends_on:
  - market-research-framework.md
  - market-data.md
---

# Market Research Intake Module v2.0

> **Three-layer intake architecture for market research across all capital raise tracks.**
> Layer 1: Screening (10 Qs) → Layer 2: Core Intake (~75 Qs, track-filtered) → Layer 3: Cross-Reference Validation (9 tests)
>
> Methodology reference: `_shared/market-research-framework.md`
> Data output target: `_shared/market-data.md` (template) or project-specific data store

---

## How to Use

1. **Run Layer 1 screening** (10 Qs) to determine track and whether full intake is warranted
2. **Apply track assignment** based on screening answers
3. **Run Layer 2 core intake** (~75 Qs) filtered to the assigned track
4. **For each question the founder cannot answer**, use the "Help Me" fallback to guide research
5. **After intake completes**, run Layer 3 cross-reference validation (9 automated tests)
6. **Generate gap analysis report** showing completeness, failures, stale data, and priority actions

---

## Layer 1: Screening Questions

### Purpose
Gate whether full intake is warranted and determine which track applies. These 10 questions should take <10 minutes and provide enough context to calibrate the full intake.

### Questions

| # | Question | Purpose | Response Format |
|---|----------|---------|-----------------|
| SC.1 | What is the company/asset? (1 sentence) | Classification | Free text |
| SC.2 | What stage? | Track selection | Enum: Ideation / Development / Construction / Operating / Scale |
| SC.3 | What are you raising and how much? | Track selection | Type (Equity/Debt/Both) + quantum (currency + amount) |
| SC.4 | What's the target return profile? | Investor matching | IRR range, cash yield, or multiple target |
| SC.5 | What % of revenue is contracted? | Revenue certainty | Percentage (0-100%) |
| SC.6 | Who are your top 2 competitors? | Market awareness | Two company names (or "none identified") |
| SC.7 | What's the key regulatory dependency? | Regulatory risk | Free text (or "none") |
| SC.8 | What's the key risk? (1 sentence) | Risk awareness | Free text |
| SC.9 | What data do you already have? | Effort calibration | Enum: None / Internal only / Published sources / Commissioned study |
| SC.10 | What is the timeline for this raise? | Urgency | Date or timeframe |

### Track Assignment Logic

```
IF SC.3 quantum < $10M → SEED
IF SC.3 quantum $10M-$50M → SEED (with Growth-Infra depth on C4/C5)
IF SC.3 quantum $50M-$500M → GROWTH-INFRA
IF SC.3 quantum $500M+ → INSTITUTIONAL

Override triggers:
- IF investor is pension/sovereign regardless of size → INSTITUTIONAL
- IF SC.2 = Operating AND SC.3 type includes Debt → min GROWTH-INFRA
- IF SC.7 indicates pending regulatory approval → elevate C6 to top-2 priority
```

### Gate Logic (Proceed / Flag)

| Condition | Action |
|-----------|--------|
| SC.2 = Ideation AND SC.9 = None | FLAG: "Significant research needed before intake can be productive. Consider Research Engine brief first." |
| SC.5 = 0% AND SC.3 quantum > $100M | FLAG: "Revenue certainty mismatch — $100M+ raise with no contracted revenue requires strong C3/C4 evidence." |
| SC.6 = "none identified" | FLAG: "Every market has competitors — at minimum, the status quo is a competitor. Research before proceeding." |
| SC.10 < 4 weeks | FLAG: "Tight timeline — prioritize P0 categories only; skip Growth-Infra/Inst depth on lower-priority categories." |

---

## Layer 2: Core Intake

### How Track Filtering Works

Each question has a track tag:
- **ALL** = asked in all tracks (Seed, Growth-Infra, Institutional)
- **GRO+INST** = asked in Growth-Infra and Institutional tracks only
- **INST** = asked in Institutional track only

Question counts per track:
| Section | Total Qs | Seed | Growth-Infra | Institutional |
|---------|----------|------|-------------|---------------|
| S1: Market Sizing | 14 | 10 | 12 | 14 |
| S2: Competitive | 14 | 9 | 12 | 14 |
| S3: Pricing/Demand | 15 | 9 | 12 | 15 |
| S4: Comps/Valuation | 14 | 7 | 10 | 14 |
| S5: FM Assumptions | 16 | 8 | 12 | 16 |
| S6: Regulatory | 10 | 4 | 7 | 10 |
| S7: Downside/Recovery | 8 | 2 | 5 | 8 |
| **Total** | **91** | **49** | **70** | **91** |

---

### S1: Market Sizing & Value Chain (14 Qs)

| # | Track | Question | Evidence Expected | Maps To | Help Me Fallback |
|---|-------|----------|-------------------|---------|------------------|
| S1.1 | ALL | What is your target market? (geography, customer segment, use case) | Clear definition | IM §5, Deck Slide 4 | N/A — must be answered by founder |
| S1.2 | ALL | What is the total addressable market (TAM)? Provide number + source. | Tier 1b source + number | IM §5 | Locate 2+ published market reports; triangulate top-down estimates |
| S1.3 | ALL | Walk through your top-down sizing chain: total market → filters → TAM | Step-by-step derivation with sources at each step | IM §5 | Build derivation from Tier 1 reports using explicit geographic + segment filters |
| S1.4 | ALL | Walk through your bottom-up sizing: units × price × penetration × capture | Unit-level calculation | IM §5 | Construct from public data: company counts, average pricing, adoption rates |
| S1.5 | ALL | Do your top-down and bottom-up reconcile? If gap >30%, explain why. | Reconciliation analysis | IM §5 | Flag gap; investigate which methodology has weaker assumptions; recommend resolution |
| S1.6 | ALL | What is your SAM? What explicit filters did you apply to TAM? | SAM with derivation | IM §5 | Apply standard filters: geography served, customer segments targeted, product scope |
| S1.7 | ALL | What is your SOM? What capture rate and why? | SOM with GTM justification | IM §5 | Benchmark against analogues; require GTM plan that justifies capture rate |
| S1.8 | ALL | What is the market growth rate? (CAGR, historical + projected) | Tier 1b source + period | IM §5 | Locate CAGR from 2+ industry reports; specify measurement period |
| S1.9 | ALL | What are the key risks to market growth? | Risk description + probability | IM §5 | Research bear cases from analyst reports; identify technology/regulatory/macro threats |
| S1.10 | ALL | What market inflection or catalyst is driving growth NOW? | Current event/data point | Deck "Why Now" | Research recent regulatory shifts, technology breakthroughs, policy changes |
| S1.11 | GRO+INST | Where in the value chain do margins sit? Map the full value chain and identify the margin pool. | JPM-standard margin pool map | IM §5 | Analyze public company margins by value chain position; identify high-margin vs low-margin nodes |
| S1.12 | GRO+INST | What supply-side constraints limit market access? (grid, permits, labor, land, capital) | Quantified constraint list | IM §5 | Research infrastructure capacity, permitting backlogs, labor market data, land/site availability |
| S1.13 | INST | What is the constrained market size? (min of demand-side TAM, supply-side capacity) | Quantified + derived | IM §5 | Calculate based on S1.2 (demand) and S1.12 (supply constraints); take the smaller number |
| S1.14 | INST | Geographic breakdown of addressable market (per country/region) | Per-geography sizing | IM §5 Appendix | Decompose Tier 1 reports by geography; provide country-level TAM where available |

**Output**: Populated C1 fields in market-data; IM §5 market sizing draft; Deck Slide 4 data

---

### S2: Competitive Landscape & Positioning (14 Qs)

| # | Track | Question | Evidence Expected | Maps To | Help Me Fallback |
|---|-------|----------|-------------------|---------|------------------|
| S2.1 | ALL | Name your top 3-5 direct competitors. For each: name, HQ, funding, estimated revenue, key differentiator. | Competitor profiles | IM §8, Deck Slide 8 | Search Crunchbase, PitchBook, press for competitors; build profiles from public data |
| S2.2 | ALL | Name 3-5 indirect competitors or substitutes (different product, same problem). | Indirect competition | IM §8 | Analyze what customers use TODAY to solve this problem; what they'd switch TO |
| S2.3 | ALL | What is your primary differentiator vs. the strongest competitor? (1 sentence) | Clear statement | Deck Slide 8 | Compare product/price/speed/quality on each dimension; identify largest delta |
| S2.4 | ALL | Define a 2x2 positioning matrix (name both axes) and place yourself + competitors. | Visual positioning | IM §8, Deck | Define axes based on most differentiating dimensions; plot companies |
| S2.5 | ALL | What is your moat? Name the type AND quantify the advantage (bps, $/unit, months, %). | Quantified moat | IM §8 | Use moat taxonomy from framework §5.3; find quantifiable data for each moat type claimed |
| S2.6 | ALL | What is the barrier to entry for a new competitor? Time, capital, and expertise required. | Barrier quantification | IM §8 | Research minimum capital, permitting time, technical requirements for market entry |
| S2.7 | ALL | What is the risk of a large incumbent entering your market? Which ones? | Incumbent threat assessment | IM §8 | Identify 2-3 large companies with capability and potential motivation to enter |
| S2.8 | ALL | What publicly available data exists on competitors? (databases, filings, reports) | Data source list | Research | Identify Capital IQ, PitchBook, SEC/AFM filings, industry reports with competitor data |
| S2.9 | ALL | Why does competition validate the market? (Competition = demand exists) | Market validation argument | Deck | Frame competition as market validation; more competitors = more demand evidence |
| S2.10 | GRO+INST | Market share breakdown: who has what %? Source? | Market share data with source | IM §8 | Research from Tier 1b reports; if unavailable, estimate from revenue proxies |
| S2.11 | GRO+INST | Competitive pricing analysis: your price vs. market range | Price benchmarking | IM §8 | Gather competitor pricing from public sources, customer interviews, RFP responses |
| S2.12 | GRO+INST | Have competitors failed? Which ones and why? (Name 2-3) | Failed competitor analysis | IM §8 | Research shutdowns, pivots, down-rounds in the space; analyze root causes |
| S2.13 | INST | Provide a Porter's Five Forces assessment for this market. | Full 5-forces analysis | IM §8 Appendix | Analyze each force: new entrants, supplier power, buyer power, substitutes, rivalry |
| S2.14 | INST | Operational benchmarking: your cost/unit, utilization, staffing vs. industry best-in-class. | Benchmark data | IM §8 Appendix | Gather industry benchmarks from reports and public company data; compare |

**Output**: Populated C2 fields; IM §8 competitive section draft; Deck Slide 8 data

---

### S3: Pricing, Demand & Revenue Durability (15 Qs)

| # | Track | Question | Evidence Expected | Maps To | Help Me Fallback |
|---|-------|----------|-------------------|---------|------------------|
| S3.1 | ALL | What is your pricing model? (subscription, usage, per-unit, hybrid, PPA, tariff, auction) | Model identification | IM §6 | Categorize current pricing; benchmark against competitor models |
| S3.2 | ALL | What is your current price point and how was it determined? | Price + methodology | IM §6 | Document current pricing; identify methodology (cost-plus, value-based, competitive, WTP) |
| S3.3 | ALL | What is your strongest evidence of demand? Where on the evidence ladder? | Highest-tier evidence | IM §6, Deck | Rank: binding contracts > LOIs > pilot revenue > interviews > surveys > reports |
| S3.4 | ALL | What is your customer acquisition cost (CAC)? How measured? | CAC with methodology | IM §6 | Calculate: total sales+marketing spend / new customers acquired in period |
| S3.5 | ALL | What is customer lifetime value (LTV)? What is LTV:CAC ratio? | LTV + ratio | IM §6 | Calculate: avg revenue per customer × avg customer lifetime; target >3x CAC |
| S3.6 | ALL | What % of revenue is contracted vs. merchant/spot? | Contracted/merchant split | IM §6 | Categorize each revenue stream; calculate % under binding contract |
| S3.7 | ALL | Customer concentration: top customer as % of revenue? Top 5? | Concentration metrics | IM §6 | Calculate from customer revenue data; flag if top 1 >30% or top 5 >60% |
| S3.8 | ALL | What would make customers switch to a competitor? | Switching trigger analysis | IM §6 | Identify: price threshold, feature gap, service failure, contract expiry |
| S3.9 | ALL | What market clearing price or WTP evidence exists? | WTP data or market price | IM §6 | Research: auction results, RFP pricing, customer survey data, published benchmarks |
| S3.10 | GRO+INST | List each revenue stream with sizing (% of total and absolute) | Revenue stream inventory | IM §6 | Enumerate all revenue sources; calculate contribution of each |
| S3.11 | GRO+INST | Are your revenue streams diversifying or correlated? What happens if one drops 50%? | Correlation analysis | IM §6 | Analyze: when market moves adversely, do all streams decline or do some offset? |
| S3.12 | GRO+INST | Contract durations, renewal rates, churn data for existing customers. | Operational metrics | IM §6 | Pull from CRM/billing data; benchmark against industry standards |
| S3.13 | INST | **Revenue waterfall**: Walk through gross potential → each haircut → net realizable. Mandatory for physical assets. | Full waterfall with % | IM §6 | Build: degradation, downtime, curtailment, price risk, credit risk → net. Source each haircut. |
| S3.14 | INST | Pricing sensitivity: if you raise/lower price by 20%, what happens to demand? | Elasticity estimate | IM §6 | Research price elasticity from academic studies, customer interviews, competitor behavior |
| S3.15 | INST | Revenue visibility: how far ahead can you see demand with confidence? | Visibility horizon | IM §6 | Analyze: contracted backlog, recurring revenue, pipeline conversion rates |

**Output**: Populated C3 fields; IM §6 revenue section draft; revenue waterfall; Deck unit economics

---

### S4: Comparable Transactions & Valuations (14 Qs)

| # | Track | Question | Evidence Expected | Maps To | Help Me Fallback |
|---|-------|----------|-------------------|---------|------------------|
| S4.1 | ALL | Comparable funding rounds (last 3 years): company, date, amount, valuation, multiple | Funding comp table | IM Appendix F | Search PitchBook, Crunchbase, press for recent rounds in the space |
| S4.2 | ALL | Comparable M&A transactions (last 3 years): target, acquirer, value, multiple | M&A comp table | IM Appendix F | Search Capital IQ, press, industry databases for relevant acquisitions |
| S4.3 | ALL | What valuation multiples are most relevant? (EV/Rev, EV/EBITDA, EV/unit) | Multiple selection | IM §12 | Identify which multiples are standard for this asset class/sector |
| S4.4 | ALL | How does your proposed valuation compare to these comps? | Valuation positioning | IM §12 | Calculate implied multiples at proposed valuation; compare to comp ranges |
| S4.5 | ALL | Are there negative precedents? (failures, down rounds, distressed sales) | Min 2 negative comps | IM §12 | Research shutdowns, down-rounds, fire sales; document at least 2 |
| S4.6 | ALL | What is the source of your comp data? (Capital IQ, PitchBook, press, other) | Data provenance | — | Identify available databases and public sources for this sector |
| S4.7 | ALL | What is the implied valuation range from your comp set? | Range (low-high) | IM §12 | Calculate: apply comp multiples to company's metrics; derive range |
| S4.8 | GRO+INST | Public company trading multiples (LTM normalized): list companies with EV/EBITDA, EV/Rev | Trading comp table | IM §12 | Pull from Capital IQ, Bloomberg, or public filings; LTM normalize |
| S4.9 | GRO+INST | Asset-level transaction multiples (EV/MW, EV/kWh, $/sq ft — whatever is relevant) | Asset comp table | IM §12 | Research project/asset-level sales; calculate per-unit metrics |
| S4.10 | GRO+INST | Multiple trend over last 2-3 years: expanding, stable, or compressing? | Trend analysis | IM §12 | Plot multiples over time; identify direction and drivers |
| S4.11 | INST | Development premium/discount: what discount do pre-operating assets trade at vs. operating? | Macquarie-standard discount | IM §12 | Research: development 20-40% discount, construction 10-20%; apply to current stage |
| S4.12 | INST | Geography/stage/scale adjustments: what normalizations did you apply to comp set? | Adjustment documentation | IM §12 | Document each adjustment: geography premium/discount, scale factor, stage adjustment |
| S4.13 | INST | Yield-based comparables: cost of equity, project IRR, dividend yield for similar assets | Yield comp table | IM §12 | Research from public infra companies, project finance databases, industry reports |
| S4.14 | INST | Control premium analysis: what premium do M&A transactions include vs. trading comps? | Premium quantification | IM §12 | Calculate: M&A EV/EBITDA vs. trading EV/EBITDA; typical 20-40% premium |

**Output**: Populated C4 fields; comp tables; football field chart data; IM Appendix F

---

### S5: FM Assumptions & Value Creation (16 Qs)

| # | Track | Question | Evidence Expected | Maps To | Help Me Fallback |
|---|-------|----------|-------------------|---------|------------------|
| S5.1 | ALL | Revenue growth rate projection (years 1-5) and what source/logic supports it. | Growth rate + source | IM §10 | Benchmark against C1 market CAGR; require bottom-up justification if above CAGR |
| S5.2 | ALL | Gross margin projection and what drives margin at this level. | Margin + driver | IM §10 | Benchmark against public company peers; identify scale/efficiency drivers |
| S5.3 | ALL | CAPEX schedule and cost basis. Source for unit costs ($/MW, $/kWh, $/sq ft). | CAPEX with source | IM §10 | Cross-reference against C4 asset-level comps and vendor quotes |
| S5.4 | ALL | OPEX assumptions: team, infrastructure, SGA, maintenance. | OPEX breakdown | IM §10 | Benchmark against operational peers; identify fixed vs. variable components |
| S5.5 | ALL | What are the top 3 most sensitive assumptions? (What breaks the model?) | Sensitivity identification | IM §10 | Run: +/- 20% on each key input; rank by impact on IRR/NPV |
| S5.6 | ALL | Do your revenue assumptions reconcile with C1 SOM × C3 ASP? (Cross-ref test #2) | Reconciliation check | — | Calculate: SOM × average selling price; compare to FM year-X revenue; flag if >20% gap |
| S5.7 | ALL | Do your pricing assumptions reconcile with C3 evidence? | Pricing consistency | — | Compare FM pricing to C3 evidence ladder; flag if FM uses higher price than highest evidence |
| S5.8 | ALL | Has the model been reviewed by a third party? | Review status | IM §10 | If no: note as open item; recommend advisor/audit per track requirements |
| S5.9 | GRO+INST | Discount rate / WACC derivation. Show component build-up. | WACC with components | IM §10 | Build: risk-free rate + equity risk premium + size premium + company-specific; debt cost + tax shield |
| S5.10 | GRO+INST | Terminal value methodology (exit multiple vs. perpetuity growth) and assumptions. | TV methodology + assumptions | IM §10 | Choose method based on asset type; flag if TV >50% of total NPV |
| S5.11 | GRO+INST | Scenario analysis: base / bull / bear with specific driver changes. | Three scenarios quantified | IM §10 | Vary top 3 sensitivities (S5.5): base = current assumptions; bull = favorable; bear = adverse |
| S5.12 | GRO+INST | Value creation bridge: where does the return come from? (KKR 5-source decomposition) | Return decomposition | IM §10 | Decompose target IRR into: dev margin, op improvement, financial engineering, multiple expansion, exit |
| S5.13 | INST | Lender case vs. management case: what's the floor? Show both. | Dual-case model | IM §10 | Build lender case: contracted revenue only, no growth, +10% OPEX contingency, +3-6mo delay |
| S5.14 | INST | DSCR sensitivity: at what assumptions does covenant break? Show the table. | DSCR sensitivity matrix | IM §10 | Build matrix: vary revenue (±10%, ±20%) × costs (±10%, ±20%); highlight covenant breach cells |
| S5.15 | INST | Inflation / escalation assumptions and how they flow through the model. | Inflation methodology | IM §10 | Document: which line items escalate with inflation, which are fixed, what inflation rate assumed |
| S5.16 | INST | Refinancing assumptions at debt maturity. | Refi terms + risk | IM §10 | Document: assumed refi rate, term, conditions; stress test with higher rates |

**Output**: Populated C5 fields; value creation bridge; lender case; IM §10 financials draft

---

### S6: Regulatory & Policy Risk (10 Qs)

| # | Track | Question | Evidence Expected | Maps To | Help Me Fallback |
|---|-------|----------|-------------------|---------|------------------|
| S6.1 | ALL | Which regulations apply to your business? List with jurisdiction. | Regulation inventory | IM §11 | Research applicable regulations by jurisdiction; create inventory table |
| S6.2 | ALL | What are the key regulatory tailwinds driving your market? | Tailwind identification | IM §11 | Research recent favorable regulatory changes, subsidies, mandates |
| S6.3 | ALL | What are the key regulatory headwinds or risks? | Headwind identification | IM §11 | Research restrictive regulations, moratoriums, compliance burdens |
| S6.4 | ALL | Does your business model depend on any subsidy or incentive? What's the sunset date? | Subsidy dependency + sunset | IM §11 | Identify all subsidies; check sunset clauses; calculate revenue dependency % |
| S6.5 | GRO+INST | Regulatory approval pathway: what approvals needed, expected timeline, success probability? | Pathway + timeline + probability | IM §11 | Map full approval chain; research typical timelines; estimate probability from precedent |
| S6.6 | GRO+INST | Regulatory risk scenario: what if the key regulation changes? Quantify revenue/cost impact. | Scenario quantification | IM §11 | Model: current regulation → change → revenue impact in % and absolute terms |
| S6.7 | GRO+INST | Does regulation create a moat (permits, licenses) or remove one (deregulation, new entrants)? | Moat assessment | IM §11 | Analyze: do regulations advantage or disadvantage the company vs. competitors? |
| S6.8 | INST | What is the annual compliance cost / burden? | Compliance cost | IM §11 | Estimate: staff, systems, reporting, legal, audit costs attributable to compliance |
| S6.9 | INST | What regulatory changes are pending that could affect the business in the next 3 years? | Pending change inventory | IM §11 | Research legislative calendars, regulatory review schedules, public consultations |
| S6.10 | INST | Has legal counsel reviewed regulatory risk? Is a legal opinion available? | Legal review status | IM §11 | If no: flag as open item; recommend engaging regulatory counsel per track requirements |

**Output**: Populated C6 fields; IM §11 regulatory section draft

---

### S7: Downside, Distress & Asset Recovery (8 Qs)

| # | Track | Question | Evidence Expected | Maps To | Help Me Fallback |
|---|-------|----------|-------------------|---------|------------------|
| S7.1 | ALL | What is the single biggest risk to this investment? | Risk identification | IM §12 | Review all categories (market, competitive, regulatory, technology, execution) and rank |
| S7.2 | ALL | In the bear case, what happens? Describe the narrative. | Bear case scenario | IM §12 | Build: adverse trigger → cascading effects → financial impact → recovery scenario |
| S7.3 | GRO+INST | What are the physical assets worth in liquidation? (orderly + forced sale) | Liquidation values | IM §12 | Value: land at market, equipment at resale, contracts at transfer value, IP at license value |
| S7.4 | GRO+INST | What would it cost to replicate the asset base from scratch? | Replacement cost | IM §12 | Calculate: land + permits + construction + equipment + commissioning + ramp-up time value |
| S7.5 | GRO+INST | What is the technology obsolescence risk? Remaining useful life? | TRL + remaining life | IM §12 | Research: technology replacement cycle, next-generation timeline, useful life of current assets |
| S7.6 | INST | Recovery waterfall in insolvency: who gets paid first? Show the stack with recovery rates. | Recovery waterfall | IM §12 | Build: senior secured → priority claims → unsecured → mezz → preferred → common equity |
| S7.7 | INST | Distress comps: what have similar assets sold for under duress? (Find 3-5 examples) | Distress comp table | IM §12 | Research distressed sales in sector; document: asset, sale price, going-concern value, discount % |
| S7.8 | INST | Tail risk inventory: list low-probability, high-impact events with mitigation status. | Tail risk register | IM §12 | Categorize: regulatory, technology, market, counterparty, force majeure, environmental |

**Output**: Populated C7 fields; downside analysis; IM §12 risk section input

---

## Layer 3: Cross-Reference Validation

### Purpose
After intake completes, run 9 automated cross-reference tests to verify internal consistency of the research package. Generate a gap analysis report.

### The 9 Tests

| # | Cross-Reference | Test | Threshold | How to Check |
|---|----------------|------|-----------|-------------|
| 1 | C1 SOM capture rate | SOM / SAM percentage | Seed <5%, Growth <10%, Inst <15% | `c1_som_capture_rate` field |
| 2 | Revenue match | C1 SOM × C3 ASP ≈ C5 Revenue Year X | Within 20% | `c1_som_value` × `c3_current_price` vs `c5_revenue_growth_yr1` implied revenue |
| 3 | Valuation match | Implied FM valuation within C4 comp range | Within 30% | FM implied valuation vs `c4_implied_valuation_low` / `c4_implied_valuation_high` |
| 4 | Growth match | C5 revenue growth > C1 market CAGR? | If yes, share-gain plan required | `c5_revenue_growth_yr1` vs `c1_market_cagr` |
| 5 | Pricing match | C3 pricing within C2 competitor range | 50-150% of competitor pricing | `c3_current_price` vs competitor price range from S2.11 |
| 6 | CAPEX match | C5 CAPEX within C4 asset comps | Within 25% | `c5_capex_per_unit` vs `c4_comp_ev_unit_range` |
| 7 | Waterfall match | C3 revenue waterfall → C5 net revenue | Exact match | `c3_net_revenue` = C5 FM net revenue |
| 8 | Timeline match | C6 regulatory timeline → C5 revenue start | Revenue doesn't precede approval | `c6_approval_timeline_months` vs FM first revenue date |
| 9 | Distress match | C7 distress recovery ≥ 60% of senior debt | Lender comfort threshold | `c7_liquidation_value` / total senior debt ≥ 60% |

### Pass Requirements

| Track | Minimum Passing | Notes |
|-------|----------------|-------|
| Seed | 5 of 9 | Tests 1, 2, 4, 5 most critical at seed |
| Growth-Infra | 7 of 9 | All except 7 and 9 |
| Institutional | 9 of 9 | All must pass |

---

## Gap Analysis Report Output Format

After running all 3 layers, generate this report:

```
═══════════════════════════════════════════════════════════════
MARKET RESEARCH GAP ANALYSIS
═══════════════════════════════════════════════════════════════

TRACK: [SEED / GROWTH-INFRA / INSTITUTIONAL]
COMPANY: [from SC.1]
RAISE: [from SC.3]
DATE: [YYYY-MM-DD]

───────────────────────────────────────────────────────────────
CATEGORY COMPLETENESS
───────────────────────────────────────────────────────────────
  C1 Market Sizing:     ██████████░░ 85%  [gaps: supply-side constraints, margin pool]
  C2 Competitive:       ████████░░░░ 70%  [gaps: market share data, op benchmarking, Porter's]
  C3 Pricing/Demand:    █████████░░░ 80%  [gaps: revenue waterfall, pricing sensitivity]
  C4 Comps:             ██████░░░░░░ 55%  [gaps: yield comps, dev discount, control premium, calendarization]
  C5 FM Assumptions:    ███████████░ 95%  [gaps: lender case]
  C6 Regulatory:        ████████████ 100%
  C7 Downside:          ████░░░░░░░░ 35%  [gaps: liquidation, replacement cost, distress comps, recovery, tail risk]

  OVERALL: [X]% complete for [TRACK] track

───────────────────────────────────────────────────────────────
CROSS-REFERENCE TESTS
───────────────────────────────────────────────────────────────
  [✓/✗] Test 1: SOM capture rate = [X]% (threshold: <[Y]%)
  [✓/✗] Test 2: SOM × ASP = [A], FM Revenue = [B] (delta: [C]%, threshold: <20%)
  [✓/✗] Test 3: FM valuation = [A], comp range = [B-C] (delta: [D]%, threshold: <30%)
  [✓/✗] Test 4: Revenue growth = [X]%, market CAGR = [Y]% (share gain: [yes/no])
  [✓/✗] Test 5: Company price = [A], competitor range = [B-C] (ratio: [D]%)
  [✓/✗] Test 6: FM CAPEX/unit = [A], comp CAPEX = [B] (delta: [C]%, threshold: <25%)
  [✓/✗] Test 7: C3 net revenue = [A], C5 net revenue = [B] (match: [yes/no])
  [✓/✗] Test 8: Regulatory approval in [X] months, first revenue in [Y] months (consistent: [yes/no])
  [✓/✗] Test 9: Distress recovery = [X]%, senior debt = [Y] (coverage: [Z]%, threshold: ≥60%)

  RESULT: [X]/9 passing ([TRACK] requires [Y]/9)
  STATUS: [PASS / FAIL — N tests below threshold]

───────────────────────────────────────────────────────────────
STALE DATA FLAGS
───────────────────────────────────────────────────────────────
  ⚠ [field_name]: Source dated [date] — [X months] old (freshness req: <[Y months])
  ⚠ [field_name]: Source dated [date] — [X months] old (freshness req: <[Y months])

───────────────────────────────────────────────────────────────
PRIORITY ACTIONS
───────────────────────────────────────────────────────────────
  1. [CRITICAL] [Action description] — Blocking [which deliverable/gate]
  2. [HIGH] [Action description] — Required for [track] track
  3. [MEDIUM] [Action description] — Would strengthen [category]
  4. [LOW] [Action description] — Nice to have

───────────────────────────────────────────────────────────────
QUALITY GATE STATUS
───────────────────────────────────────────────────────────────
  [✓/✗] Gate 1: Market sizing sources ([X] found, [Y] required)
  [✓/✗] Gate 2: Evidence type ([current type] vs [required type])
  [✓/✗] Gate 3: Competitor profiles ([X] found, [Y] required)
  [✓/✗] Gate 4: Pricing evidence ([type] vs [required])
  [✓/✗] Gate 5: Comp transactions ([X] found, [Y] required)
  [✓/✗] Gate 6: FM assumption sourcing ([X]% sourced, [Y]% required)
  [✓/✗] Gate 7: Data freshness (oldest source: [X months], max: [Y months])
  [✓/✗] Gate 8: Cross-reference tests ([X]/9 passing, [Y]/9 required)
  [✓/✗] Gate 9: Regulatory analysis ([status] vs [required])
  [✓/✗] Gate 10: Downside analysis ([depth] vs [required])
  [✓/✗] Gate 11: Third-party validation ([status] vs [required])

  RESULT: [X]/11 gates met ([TRACK] requires [Y]/11)

═══════════════════════════════════════════════════════════════
```

---

## Related Files

| File | Location | Purpose |
|------|----------|---------|
| Framework | `_shared/market-research-framework.md` | Methodology reference (§1-§15) |
| Data Template | `_shared/market-data.md` | Field schema this intake populates |
| Overlay Spec | `_shared/overlays/README.md` | Sector overlay format |

---

*Intake module version 2.0 — Last updated 2026-03-31*
*91 total questions across 7 categories with 3-track filtering*
*9 cross-reference validation tests with automated gap analysis*
