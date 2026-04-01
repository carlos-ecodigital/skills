---
name: market-research-framework
description: Canonical market research methodology for capital raises across Seed, Growth-Infra, and Institutional tracks. 7 categories, 4-tier credibility, 9 cross-reference tests.
type: reference
version: 2.0
last_updated: 2026-03-31
---

# Market Research Framework v2.0

> **Canonical reference architecture for market research across all capital raise tracks.**
> This document defines methodology, standards, and validation logic. Existing skills (`seed-fundraising`, `Intake_IM_institutional`, `research-engine`, `competitive-intel`, `project-financing`, `financial-model-interpreter`) keep their own lightweight question sets for UX flow but point here for methodology.

---

## Table of Contents

1. [Purpose, Scope & Architecture](#1-purpose-scope--architecture)
2. [Priority Ordering by Track & Investor Type](#2-priority-ordering-by-track--investor-type)
3. [Source Credibility Framework (4 Tiers)](#3-source-credibility-framework-4-tiers)
4. [C1: Market Sizing & Value Chain](#4-c1-market-sizing--value-chain)
5. [C2: Competitive Landscape & Positioning](#5-c2-competitive-landscape--positioning)
6. [C3: Pricing, Demand & Revenue Durability](#6-c3-pricing-demand--revenue-durability)
7. [C4: Comparable Transactions & Valuations](#7-c4-comparable-transactions--valuations)
8. [C5: FM Assumptions & Value Creation](#8-c5-fm-assumptions--value-creation)
9. [C6: Regulatory & Policy Risk](#9-c6-regulatory--policy-risk)
10. [C7: Downside, Distress & Asset Recovery](#10-c7-downside-distress--asset-recovery)
11. [Cross-Reference Validation Matrix](#11-cross-reference-validation-matrix)
12. [Anti-Patterns & Common Failures](#12-anti-patterns--common-failures)
13. [Presentation Standards by Deliverable](#13-presentation-standards-by-deliverable)
14. [Quality Gates by Stage](#14-quality-gates-by-stage)
15. [Handling Data-Poor / Nascent Markets](#15-handling-data-poor--nascent-markets)

---

## 1. Purpose, Scope & Architecture

### 1.1 Purpose

This framework is the single authoritative reference for market research methodology across all capital raise activities. It serves two audiences:

- **Founder-facing**: Guides intake conversations, structures what data is needed and why
- **Analyst/AI research guide**: Defines methodology, evidence standards, and quality gates for research execution

### 1.2 Scope

- **7 research categories** (C1-C7): Market Sizing, Competitive Landscape, Pricing & Demand, Comparable Transactions, FM Assumptions, Regulatory Risk, Downside & Recovery
- **3 fundraise tracks**: Seed (<$10M), Growth-Infra ($50M-$500M), Institutional ($500M-$5B+)
- **Sector-agnostic core**: No sector-specific content in this file. Sector depth is provided by overlays at `_shared/overlays/{sector}-{category}.md`

### 1.3 Architecture

```
market-research-framework.md (THIS FILE — methodology)
        │
        ├── market-data.md (field schema template — sector-agnostic)
        │       │
        │       └── overlays/{sector}-{category}.md (sector-specific benchmarks)
        │
        ├── intake-modules/m-market-research.md (intake questionnaire)
        │
        └── [Project-specific data stores]
            └── e.g., Market_Research_v3/ (populated research files)
```

### 1.4 How to Use

1. **Determine track** using screening questions (see intake module)
2. **Follow priority ordering** (§2) to allocate research effort
3. **Apply credibility standards** (§3) to every source
4. **Execute category methodologies** (§4-§10) at track-appropriate depth
5. **Run cross-reference validation** (§11) to ensure internal consistency
6. **Check quality gates** (§14) before declaring research complete
7. **Present findings** using deliverable-appropriate format (§13)

### 1.5 Stage-Appropriate Depth Ladder

| Aspect | Seed | Growth-Infra | Institutional |
|--------|------|-------------|---------------|
| Research depth | Directional | Validated | Auditable |
| Source tier | Tier 1b+ acceptable | Tier 1a required for key inputs | Tier 1a + Tier 0 for key inputs |
| Scenario analysis | Base + qualitative bear | Base / bull / bear quantified | Base / bull / bear + stress test |
| Third-party validation | Not required | Recommended | Required |
| Total research effort | 20-40 hours | 80-120 hours | 200-400 hours |

---

## 2. Priority Ordering by Track & Investor Type

### 2.1 Seed Track (<$10M)

| Rank | Category | Investor Signal |
|------|----------|-----------------|
| 1 | C1: Market Sizing & Value Chain | "Is this market big enough and where does value sit?" |
| 2 | C2: Competitive Landscape | "Why won't incumbents eat you?" |
| 3 | C3: Pricing & Demand | "Does the unit economics work?" |
| 4 | C6: Regulatory & Policy | "What tailwinds/headwinds exist?" |
| 5 | C4: Comparable Transactions | "What's this worth?" |
| 6 | C5: FM Assumptions | "Are the numbers grounded?" |
| 7 | C7: Downside & Recovery | Light touch at seed |

### 2.2 Growth-Infra Track ($50M-$500M)

| Rank | Category | Investor Signal |
|------|----------|-----------------|
| 1 | C4: Comparable Transactions | "What have similar platforms traded at?" |
| 2 | C1: Market Sizing & Value Chain | "Can this market support the growth plan?" |
| 3 | C3: Pricing & Demand | "What's contracted vs. merchant?" |
| 4 | C5: FM Assumptions & Value Creation | "Where does the return come from?" |
| 5 | C6: Regulatory & Policy | "What regulatory risk am I underwriting?" |
| 6 | C2: Competitive Landscape | "What's the barrier to replication?" |
| 7 | C7: Downside & Recovery | "What do I lose in the bear case?" |

### 2.3 Institutional Track ($500M+)

| Rank | Category | Investor Signal |
|------|----------|-----------------|
| 1 | C4: Comparable Transactions | "What have similar assets traded at?" |
| 2 | C7: Downside & Recovery | "What's the floor on my investment?" |
| 3 | C1: Market Sizing & Value Chain | "Can this market absorb $1B?" |
| 4 | C5: FM Assumptions & Value Creation | "Can we rebuild these numbers?" |
| 5 | C3: Pricing & Demand | "What's the revenue certainty?" |
| 6 | C6: Regulatory & Policy | "What political/regulatory risk exists?" |
| 7 | C2: Competitive Landscape | "What's the barrier to entry?" |

### 2.4 Investor-Type Calibration Matrix

Different investor types weight categories differently, regardless of raise size:

| Investor Type | Top 3 Categories | Evidence Expectation |
|--------------|-------------------|---------------------|
| Seed VC | C1, C2, C3 | Narrative with directional data; team > data |
| Growth Equity | C1, C4, C5 | Validated with operating history; auditable model |
| PE / Infra Fund | C4, C7, C5 | Independent market study; model audit; lender case |
| Pension / Sovereign | C4, C7, C6 | Full independent verification; regulatory comfort letter |
| Family Office | C1, C3, C4 | Strong narrative backed by data; thesis-driven |
| Strategic / Corporate | C2, C3, C1 | Synergy analysis; market overlap mapping |

### 2.5 Track Selection Decision Tree

```
Raise quantum?
├── <$10M → SEED
├── $10M-$50M → SEED (with Growth-Infra depth on C4/C5)
├── $50M-$500M → GROWTH-INFRA
├── $500M-$5B+ → INSTITUTIONAL
└── Unknown → Start with screening questions (see intake module)

Override triggers:
- If investor is pension/sovereign regardless of size → INSTITUTIONAL
- If asset is operating with debt financing → min GROWTH-INFRA
- If regulatory approval pending → elevate C6 to rank 1-2 regardless of track
```

---

## 3. Source Credibility Framework (4 Tiers)

### 3.1 Tier Definitions

| Tier | Name | Examples | Use |
|------|------|----------|-----|
| **0** | **Primary Research** | Expert network calls (GLG, AlphaSights, Guidepoint), proprietary surveys, management interviews, channel checks, site visits, customer interviews, industry conferences (direct notes) | Highest conviction; required for variant views and key assumptions at institutional track |
| **1a** | **Official / Factual** | Government statistics (CBS, Eurostat, BLS), central bank data (ECB, DNB), regulatory filings (ACM, AFM, RVO), court records, stock exchange filings (SEC, AFM), patent databases, land registry (Kadaster), grid operator data (TenneT, regional DSOs) | Factual basis; not disputable; anchors all other analysis |
| **1b** | **Institutional Analytical** | Big 4 reports (Deloitte, PwC, EY, KPMG), bulge bracket research (Goldman, JPM, MS, Citi), multilateral agency reports (IEA, IRENA, World Bank, IMF), Gartner/IDC/Forrester, BNEF, peer-reviewed academic research, rating agency reports (Moody's, S&P, Fitch) | Analytical estimates from reputable institutions; methodology transparent; debatable but high-quality |
| **2** | **Professional** | Trade publications (Datacenter Dynamics, Energy Storage News, Greentech Media), industry associations (NVDE, Holland Solar, Dutch Data Center Association), named analyst notes, conference presentations (public slides), consulting reports from mid-tier firms | Supporting evidence; require corroboration from Tier 1 for key findings |
| **3** | **Informal** | Blog posts, social media (LinkedIn, X), unnamed sources, founder estimates, AI-generated analysis (ChatGPT, Claude outputs without source verification), Wikipedia, press releases (company-issued), podcast transcripts | Use only with Tier 1-2 corroboration; must be explicitly flagged as Tier 3 |

### 3.2 Freshness Requirements

| Data Type | Maximum Age | Rationale |
|-----------|------------|-----------|
| Market sizing | 18 months | Market dynamics shift but TAM moves slowly |
| Pricing data | 12 months | Pricing changes with market conditions |
| Comparable transactions | 6 months | Deal multiples are highly time-sensitive |
| Regulatory status | Current (verify at time of use) | Regulations can change overnight |
| Primary research | 12 months | Expert opinions date quickly |
| Technology specs | 6 months | Tech generations refresh rapidly |
| Financial model inputs | 6 months | Rates, spreads, costs change with markets |

### 3.3 Consensus vs. Variant Perception (Goldman Standard)

Every market view must be tagged:

- **Consensus**: Aligned with mainstream analyst/report estimates
  - Lower burden of proof (Tier 1b sufficient)
  - Lower alpha — consensus is already priced in
  - Still requires sourcing and freshness compliance

- **Variant**: Differs materially from consensus
  - Higher burden of proof — must explain why consensus is wrong
  - Requires Tier 0 or Tier 1a evidence to support
  - Must articulate the specific mechanism by which consensus will shift
  - Variant views are where investment alpha lives — they are valuable but must be defended

### 3.4 Contradiction Protocol

When sources disagree:

1. **Present both**: Show the disagreement explicitly; do not hide it
2. **Assess credibility**: Compare tier, recency, methodology, sample size, geographic relevance
3. **Identify root cause**: Are they measuring different things? Different time periods? Different geographies?
4. **Recommend resolution**: State which source you weight more heavily and why
5. **Flag for human judgment**: If unresolvable after steps 1-4, escalate explicitly
6. **Document**: Record the contradiction, your analysis, and the resolution in the research file

### 3.5 Source Citation Standard

Every source citation must include:
- Author / organization
- Title
- Publication date
- URL (if available)
- Access date
- Tier classification
- Geographic scope
- Freshness status (current / approaching stale / stale)

---

## 4. C1: Market Sizing & Value Chain

### 4.1 Core Methodology

**TAM/SAM/SOM with derivation chain**: Each step must show explicit filters from the prior step. No gaps in logic. Every number must have a source.

**Dual methodology mandatory**:
- **Top-down**: Start from published market reports → apply geographic filters → apply segment filters → apply adoption curve → arrive at addressable market
- **Bottom-up**: Count addressable units × price per unit × penetration rate × capture rate → arrive at addressable market

**Reconciliation requirement**:
- If top-down and bottom-up differ by <30%: acceptable; average or explain preference
- If 30-50% gap: explain why; identify which methodology has weaker assumptions
- If >50% gap: one methodology is wrong; investigate and fix before proceeding

### 4.2 Value Chain & Margin Pool Analysis (JPM Standard)

Map the full value chain from raw input to end customer:
1. Identify every node in the value chain
2. Estimate gross margin at each node
3. Identify where the margin pool concentrates
4. Show where the company captures value
5. Flag if company is positioned in a low-margin node (red flag)

This analysis answers: "Even if the market is large, does value accrue to THIS part of the chain?"

### 4.3 Supply-Side Constraint Analysis (GIP Standard)

For any market involving physical assets, demand-side TAM is necessary but not sufficient. Analyze supply constraints:

- **Grid / infrastructure capacity**: Available grid connections, substation capacity, pipeline throughput
- **Permitting pipeline**: Permit approval rates, timeline, backlog
- **Labor / supply chain**: Skilled worker availability, equipment lead times, supply chain bottlenecks
- **Land / site availability**: Zoning, land prices, community acceptance
- **Capital availability**: Debt market capacity, equity appetite, crowding-out effects

**Constrained market size** = min(demand-side TAM, supply-side capacity)

This is often materially smaller than demand-side TAM for infrastructure assets.

### 4.4 Penetration Curve Modeling

- Use S-curve modeling based on analogues from adjacent markets
- Never use linear extrapolation for emerging markets
- Identify: current penetration %, inflection triggers, saturation level, timeline to maturity
- Reference adoption curves from analogous technologies (e.g., solar → BESS, mobile → IoT)

### 4.5 Market Structure

- **HHI (Herfindahl-Hirschman Index)**: <1,000 = fragmented, 1,000-2,500 = moderate, >2,500 = concentrated
- **Fragmentation trend**: Consolidating or fragmenting? Implications for new entrants.
- **CR4 / CR8**: Top 4/8 player market share concentration

### 4.6 Presentation by Track

| Track | Deliverable | Depth |
|-------|------------|-------|
| Seed | 1 slide (TAM/SAM/SOM funnel) + 1-2 IM pages | Top-down + bottom-up with reconciliation; margin pool insight |
| Growth-Infra | 2-3 IM pages + appendix | Full sizing with constraint analysis + value chain map + market structure |
| Institutional | 5-8 IM pages + appendix | Independent market study with scenario analysis, geographic decomposition, constraint modeling, penetration curves |

### 4.7 Red Flags

- TAM >$100B without granular breakdown or derivation chain
- SOM >10% of SAM without detailed GTM plan and competitive justification
- Single-source sizing (must have 2+ independent sources at minimum)
- Linear growth projection for emerging market
- No supply-side constraint analysis for physical asset businesses
- Margin pool analysis shows company in lowest-margin node without mitigation strategy
- Market sizing from company's own materials without independent verification

---

## 5. C2: Competitive Landscape & Positioning

### 5.1 Framework Stack

Layer competitive analysis using these frameworks in combination:

1. **Porter's Five Forces**: Threat of new entrants, supplier power, buyer power, threat of substitutes, competitive rivalry
2. **2x2 Positioning Matrix**: Define two axes that capture the key competitive dimensions; plot company + competitors
3. **Moat Taxonomy**: Classify the type(s) of competitive advantage
4. **Competitive Advantage Quantification**: Don't just name advantages — measure them

### 5.2 Competitor Taxonomy

- **Direct competitors**: Same product/service, same market, same customer
- **Indirect competitors**: Different product/service solving the same problem
- **Potential entrants**: Companies with capability/motivation to enter (especially well-funded adjacencies)
- **Substitutes**: Alternative approaches that eliminate the need for the product entirely

### 5.3 Moat Types & Quantification

| Moat Type | Definition | How to Quantify |
|-----------|-----------|-----------------|
| Network effects | Value increases with users | Users per unit value; growth rate; tipping point |
| Switching costs | Cost/effort to change providers | $/customer to switch; months to migrate; data lock-in |
| Regulatory | Government-granted barriers | Licenses, permits, tariff protection; years to replicate |
| IP / Patents | Legal protection of innovation | Patent portfolio count; litigation history; expiry dates |
| Scale economies | Cost per unit decreases with scale | Cost curve by volume; minimum efficient scale |
| Brand | Reputation and trust | NPS; organic traffic; pricing premium vs. generic |
| Data / Learning curves | Proprietary data or accumulated expertise | Data volume; iteration cycles; performance delta vs. new entrant |

**GIP Standard**: Don't just name the advantage — quantify it in bps of cost advantage, $/unit savings, months of timeline advantage, or % of locked-in demand. "We have a regulatory moat" is not sufficient. "We hold 3 of 7 permits issued in the province, each taking 18-24 months to obtain" is.

### 5.4 Operational Benchmarking (Brookfield Standard)

For infrastructure and operational businesses, benchmark against industry:

- Cost per unit vs. best-in-class operator
- Staffing ratios (headcount per MW, per unit, per $M revenue)
- Utilization rates vs. peer average
- Maintenance spend per unit vs. industry standard
- Downtime / availability vs. SLA benchmarks

### 5.5 Failed Competitor Analysis

Who tried this and failed? Why? What does that tell you about the market?

- Identify 2-3 failed or struggling competitors
- Analyze root cause of failure (market, execution, timing, funding, technology)
- Explain how your approach differs
- This builds credibility — acknowledging failures shows market awareness

### 5.6 Presentation by Track

| Track | Deliverable | Depth |
|-------|------------|-------|
| Seed | 1 slide (2x2 matrix) + 1 IM page | Top 5 competitors + 1-sentence differentiator + moat type |
| Growth-Infra | 2-3 IM pages | Full competitive analysis with quantified advantages + failed competitor analysis |
| Institutional | 3-5 IM pages + appendix | Market share data, strategy mapping, operational benchmarking, Porter's Five Forces, moat quantification |

### 5.7 Red Flags

- "No competitors" (every product has alternatives — at minimum, the status quo is a competitor)
- Ignoring indirect substitutes (especially if substitutes are cheaper/simpler)
- No barrier-to-entry analysis (especially for simple business models)
- Moat claimed without quantification ("we have strong network effects" — how strong?)
- Operational metrics worse than industry average without explanation or improvement plan
- Competitive analysis limited to direct competitors; no potential entrant analysis

---

## 6. C3: Pricing, Demand & Revenue Durability

### 6.1 Evidence Ladder

Rank demand evidence from strongest to weakest:

| Rank | Evidence Type | Weight | Example |
|------|-------------|--------|---------|
| 1 | Binding contracts | Highest | Signed PPAs, colocation agreements, capacity reservations |
| 2 | LOIs / Term sheets | High | Non-binding but negotiated terms with identified counterparties |
| 3 | Pilot revenue | High | Actual revenue from initial customers (even if small) |
| 4 | Customer interviews | Medium | Structured interviews with potential buyers confirming WTP |
| 5 | Surveys | Medium-Low | Broader market surveys (susceptible to hypothetical bias) |
| 6 | Market reports | Low | Third-party estimates of demand (no direct customer validation) |

### 6.2 Pricing Methodology

Identify which methodology is used and whether it's appropriate:

- **Cost-plus**: Floor pricing (ensures margin); risk of leaving money on table
- **Value-based**: Prices relative to customer value/savings; highest pricing power
- **Competitive benchmarking**: Prices relative to alternatives; market-driven
- **Willingness-to-pay (WTP)**: Direct customer research on price sensitivity
- **Auction / market-clearing**: Price discovered through bidding; volatile but transparent

### 6.3 Revenue Stacking (Morgan Stanley Standard)

For multi-stream businesses, analyze each revenue stream independently:

1. **Identify**: List every distinct revenue stream
2. **Size**: Quantify each stream's contribution (% and absolute)
3. **Classify certainty**: Regulated tariff > Contracted > Quasi-contracted > Merchant
4. **Assess correlation**: Are streams diversifying (one goes up when other goes down) or correlated (all move together)?
5. **Calculate revenue-at-risk**: What % of total revenue is merchant/uncontracted?
6. **Present the stack**: Visual showing the revenue build-up with certainty bands

### 6.4 Revenue Waterfall (ECP Standard)

**Mandatory for any asset with physical production.** Shows the haircut from theoretical maximum to net realizable revenue:

```
Gross Revenue Potential (100%)
├── Technology degradation           (-X%)  ← Panel degradation, battery fade, efficiency loss
├── Availability / downtime          (-X%)  ← Planned maintenance, unplanned outage
├── Curtailment / congestion         (-X%)  ← Grid curtailment, dispatch constraints
├── Price risk: contracted vs. merchant (-X%)  ← Merchant exposure, basis risk, shape risk
└── Counterparty credit risk         (-X%)  ← Customer default, payment delays
= Net Realizable Revenue             (Y%)
```

Track-specific requirements:
- Seed: Not required (qualitative mention of revenue risks sufficient)
- Growth-Infra: Required for infrastructure assets; quantify each haircut
- Institutional: Required with scenario analysis (base/bull/bear haircut ranges)

### 6.5 Demand Signals

- **Pipeline / backlog**: Value of identified opportunities at various stages
- **Waitlist**: Number of customers/projects waiting for capacity
- **Order book**: Confirmed orders not yet delivered
- **Market absorption rate**: How quickly the market consumes new supply
- **RFP/tender activity**: Volume and frequency of market requests

### 6.6 Customer Concentration Analysis

| Metric | Threshold | Red Flag Level |
|--------|-----------|----------------|
| Top 1 customer % of revenue | >30% | High concentration risk |
| Top 5 customers % of revenue | >60% | Moderate concentration risk |
| Customer HHI | >2,500 | Concentrated customer base |
| Single-sector exposure | >70% | Sector concentration risk |

### 6.7 Presentation by Track

| Track | Deliverable | Depth |
|-------|------------|-------|
| Seed | 1 slide (unit economics waterfall) + 1-2 IM pages | Pricing model, demand evidence, CAC/LTV |
| Growth-Infra | 2-3 IM pages | Revenue stacking + contracted/merchant split + pricing sensitivity |
| Institutional | 3-5 IM pages | Full revenue waterfall + demand scenario analysis + counterparty credit analysis |

### 6.8 Red Flags

- 100% merchant revenue at scale without volatility analysis
- Pricing >2x competitors without quantified value-based justification
- Single customer >30% of projected revenue
- No churn/renewal data at growth stage
- Revenue waterfall shows >40% gross-to-net haircut without mitigation strategy
- LTV:CAC ratio <3x (or unmeasured)
- No contracted revenue pipeline for next 12-24 months

---

## 7. C4: Comparable Transactions & Valuations

### 7.1 Four Comp Types (Stonepeak Standard)

Every comp analysis must consider all four types. Not all will be available for every company, but the absence of a type should be noted and explained.

| Type | What It Measures | Best For | Key Multiples |
|------|-----------------|----------|---------------|
| **Trading comps** | Public company market values (ongoing concern) | Establishing valuation floor/ceiling from liquid markets | EV/Revenue, EV/EBITDA, P/E |
| **Precedent M&A** | Company-level acquisition prices (including control premium) | Valuation including strategic value and control | EV/EBITDA, EV/Revenue |
| **Asset-level transactions** | Individual asset/project sales | Infrastructure, real estate, project finance | EV/MW, EV/kWh, $/sq ft, $/unit |
| **Funding rounds** | Private company valuations | Early-stage and growth companies | Pre-money, post-money, implied multiple |

### 7.2 Yield-Based Comparables (Macquarie Standard)

Infrastructure investors think in yields, not multiples:

- **Cost of equity (CoE)**: What equity return does the market demand?
- **Project IRR**: Unlevered project-level return
- **Dividend yield**: Cash distribution rate
- **Cash yield**: Free cash flow yield

Yield comps are especially important for:
- Operating infrastructure assets
- Any asset with contracted cash flows
- Comparison against risk-free rate + spread

### 7.3 Selection Criteria Discipline (JPM Standard)

Every comp table must include:
- **Rationale for inclusion**: Why is this a valid comparable?
- **Similarity dimensions**: Size, geography, stage, business model, asset class, vintage
- **Adjustments applied**: What normalizations were made?
- **Exclusion note**: What potential comps were excluded and why?

### 7.4 Technical Standards

**Calendarization**: LTM (Last Twelve Months) normalize across different fiscal years. Never compare FY2024 to FY2025 without adjustment.

**Pro forma adjustments**: Strip out:
- One-time items (restructuring charges, litigation)
- Acquisition synergies (announced but not yet realized)
- Non-recurring revenue (one-off contracts, project completions)
- Non-cash items (stock-based compensation — include/exclude consistently)

**Control premium treatment**: M&A comps include 20-40% control premium vs. trading comps. Never mix M&A and trading comps in the same range without adjusting for control premium.

**Development premium/discount (Macquarie)**:
- Development-stage assets trade at 20-40% discount to operating assets
- Construction-stage assets at 10-20% discount
- Premium applies at COD (Commercial Operation Date) — the "construction-to-operation" value step-up

### 7.5 Football Field Output

The deliverable from comp analysis is an **implied valuation range chart** (football field), not a raw table.

- Table = input (raw comp data with sources)
- Football field = output (visual showing valuation range from each methodology)
- Include: trading comps range, M&A comps range, asset comps range, DCF range, management/board target
- Show the overlap zone where multiple methodologies converge

### 7.6 Presentation by Track

| Track | Deliverable | Depth |
|-------|------------|-------|
| Seed | 5-8 funding round comps + 3-5 M&A comps in appendix table | Implied valuation range, key multiples |
| Growth-Infra | 2-3 IM pages + appendix | Full comp table with 4 types + implied range + football field |
| Institutional | 3-5 IM pages + appendix | 15+ comps, all 4 types, adjustments documented, football field, premium/discount analysis, yield comps |

### 7.7 Red Flags

- Only favorable comps shown (no negative precedents, no down-round comps)
- Mixing geographies without adjustment (US multiples applied to EU market)
- Stale data >6 months for recent transactions
- No control premium adjustment when mixing M&A and trading comps
- No development discount for pre-operating assets
- Implied valuation from model >30% above comp range without explanation
- Comps from fundamentally different business models (e.g., SaaS comps for hardware business)

---

## 8. C5: FM Assumptions & Value Creation

### 8.1 Core Principle

**Every financial model input needs a market research source.** Assumptions without sources are opinions, not analysis. At institutional track, 100% of key inputs must be sourced with Tier 1 evidence.

### 8.2 Assumption Categories

| Category | Key Inputs | Source Requirements |
|----------|-----------|-------------------|
| **Revenue** | Pricing × volume × growth rate × penetration | C3 pricing evidence + C1 market sizing |
| **Cost** | COGS, SGA, R&D, maintenance, insurance | Industry benchmarks + vendor quotes |
| **Capital** | CAPEX, working capital, debt terms, equity structure | C4 asset comps + lender term sheets |
| **Market** | Growth rates, penetration, pricing trends, competitive dynamics | C1 market data + C2 competitive intel |
| **Tax & regulatory** | Tax rates, incentives, regulatory costs | C6 regulatory analysis + tax advisor |
| **Technology** | Degradation, efficiency, useful life, replacement cycles | OEM warranties + industry data |

### 8.3 Value Creation Bridge (KKR Standard)

Where does the investor return come from? Break total return into 5 sources:

1. **Development / construction margin**: Buy/build at cost, value at completion → development spread
2. **Operational improvement**: Revenue enhancement (occupancy, pricing, new revenue streams) + cost reduction (efficiency, scale, procurement)
3. **Financial engineering**: Leverage optimization, refinancing at lower rates, securitization, structured finance
4. **Multiple expansion**: Market re-rating (sector rotation, de-risking through operating history, index inclusion)
5. **Exit premium**: Strategic buyer premium, portfolio premium, platform premium

Show the decomposition: "Of the target 15% IRR, 4% comes from development margin, 3% from operational improvement, 5% from leverage, 2% from multiple expansion, 1% from exit premium."

### 8.4 Lender Case vs. Management Case (Macquarie Standard)

Infrastructure models financed with debt must have two versions:

| Aspect | Management Case | Lender Case |
|--------|----------------|-------------|
| Revenue | Full pricing with merchant upside | Contracted revenue only; no merchant |
| Growth | Base case growth | Zero growth or minimal |
| OPEX | Optimized cost structure | Include contingency (typically 5-10%) |
| CAPEX | Planned CAPEX schedule | Include cost overrun buffer (10-20%) |
| Timing | On-schedule | 3-6 month delay assumption |
| Purpose | The pitch; shows full potential | The floor; shows debt serviceability |

### 8.5 DSCR Sensitivity (Macquarie Standard)

Debt Service Coverage Ratio sensitivity table is mandatory for any debt-financed asset:

- Show DSCR across a matrix of revenue and cost assumptions
- Identify the covenant break point (typically DSCR <1.10x or <1.20x)
- Show which assumption combinations trigger covenant breach
- Present as a heat-map table: green (comfortable) → yellow (tight) → red (breach)

### 8.6 Scenario Analysis

| Track | Requirement |
|-------|-------------|
| Seed | Base case + qualitative bear case narrative |
| Growth-Infra | Base / bull / bear with quantified driver changes |
| Institutional | Base / bull / bear + combined adverse stress test (multiple drivers moving adversely simultaneously) |

### 8.7 Cross-Reference Reconciliation

These checks ensure the financial model is grounded in market research:

- FM revenue = C1 SOM × C3 ASP (within 20% tolerance)
- FM revenue growth ≤ C1 market CAGR unless share-gain is justified with GTM plan
- FM CAPEX ≈ C4 asset-level comp CAPEX (within 25% tolerance)
- FM pricing matches C3 evidence (within competitive range)
- FM debt terms match C4/C5 market benchmarks
- FM regulatory assumptions match C6 timeline and approvals

### 8.8 Presentation by Track

| Track | Deliverable | Depth |
|-------|------------|-------|
| Seed | 1 IM page | Key assumptions table with sources |
| Growth-Infra | 2-3 IM pages | Assumptions + value creation bridge + base/bull/bear |
| Institutional | 5-8 IM pages | Full assumption book + lender case + DSCR sensitivity + stress test + value creation bridge |

### 8.9 Red Flags

- Revenue growth >50% CAGR without bottom-up justification
- Margin expansion without identified driver
- Cost of equity <15% for pre-revenue company
- No lender case for debt-financed assets
- Assumptions disconnected from C1-C4 market research findings
- Terminal value >50% of total NPV (sensitive to assumptions)
- Model not reviewed by third party at Growth-Infra+ track
- DSCR >2.0x across all scenarios (suggests under-leveraging or overly optimistic assumptions)

---

## 9. C6: Regulatory & Policy Risk

### 9.1 Regulatory Mapping

For every relevant jurisdiction, document:

| Element | Detail Required |
|---------|----------------|
| Regulation name | Official name + short description |
| Jurisdiction | Country / province / municipality |
| Status | Draft / enacted / effective / under review |
| Effective date | When it takes/took effect |
| Sunset clause | Does it expire? When? |
| Approval chain | Which agencies approve? In what order? |
| Timeline | Expected duration from application to approval |
| Cost | Application fees, compliance costs |
| Impact on company | Positive (tailwind) / negative (headwind) / neutral |

### 9.2 Regulatory Timeline

Create a timeline showing:
- Key decision dates (parliamentary votes, regulatory reviews)
- Implementation dates (when new rules take effect)
- Transition periods (phase-in, grandfathering clauses)
- Upcoming changes (announced but not yet effective)

### 9.3 Regulatory Risk Scenarios

For each major regulatory dependency, model:
- **Base case**: Current regulation continues as-is
- **Upside**: Regulation becomes more favorable (e.g., subsidy increase, streamlined permitting)
- **Downside**: Regulation becomes adverse (e.g., subsidy cuts, moratorium, new restrictions)
- **Quantify impact**: Revenue/cost impact per scenario in % and absolute terms

### 9.4 Regulatory Moat Assessment

Does regulation create barriers to entry (license requirements, permitting complexity, tariff protection) or remove them (deregulation, market opening, technology neutrality)?

- **Regulatory moat**: Permits, licenses, approvals that take time/capital to obtain and limit competitor entry
- **Regulatory risk**: Same regulations can change, be revoked, or be replicated by competitors over time
- Net assessment: Is regulation net-positive or net-negative for competitive position?

### 9.5 Subsidy & Incentive Analysis

For every subsidy/incentive the business model depends on:

| Element | Detail |
|---------|--------|
| Program name | Official name |
| Quantum | Amount per unit ($/kWh, $/MW, % of CAPEX) |
| Duration | How long the subsidy applies |
| Sunset date | When does the program expire or get reviewed? |
| Revenue dependency | What % of revenue depends on this subsidy? |
| Replacement risk | If subsidy disappears, is there a market price substitute? |
| Political risk | Likelihood of early termination or reduction |

### 9.6 Presentation by Track

| Track | Deliverable | Depth |
|-------|------------|-------|
| Seed | 0.5-1 IM page | Key regulatory tailwinds and headwinds named |
| Growth-Infra | 1-2 IM pages | Full regulatory mapping + scenario analysis + moat assessment |
| Institutional | 2-3 IM pages + appendix | Full analysis + legal opinion reference + compliance cost modeling + pending changes (3-year window) |

### 9.7 Red Flags

- Business model depends on a single subsidy with sunset clause
- No regulatory approval pathway identified for required permits
- Regulation actively hostile to business model (moratorium, ban, restrictive zoning)
- Compliance costs not reflected in financial model
- No legal counsel review at institutional track
- Regulatory timeline conflicts with financial model revenue start date

---

## 10. C7: Downside, Distress & Asset Recovery

### 10.1 Liquidation Value Analysis (Brookfield Standard)

What are the physical assets worth if the business fails? This sets the **floor** on investment loss.

- Identify all tangible assets (land, buildings, equipment, IP, contracts)
- Value each at: book value, market value (orderly liquidation), forced sale value (fire sale)
- Present as: total liquidation value as % of total investment
- Compare to outstanding debt: Does liquidation value cover senior debt? Mezzanine?

### 10.2 Replacement Cost Analysis

What would it cost to replicate the asset base from scratch?

- Calculate total replacement cost including: land acquisition, permitting (time + cost), construction, equipment, commissioning, ramp-up
- Replacement cost sets a **ceiling on competitive entry** (a competitor would need to spend this much)
- Replacement cost sets a **floor on strategic value** (an acquirer would pay at least this vs. building new)
- Compare: current valuation vs. replacement cost → premium or discount?

### 10.3 Distress Comparables

What have similar assets sold for in distressed situations?

- Find 3-5 distressed sales of comparable assets
- Typical fire sale discounts: 30-60% of going-concern value
- Identify drivers of discount: urgency, asset condition, market conditions, seller motivation
- Apply to current asset to estimate worst-case recovery

### 10.4 Technology Obsolescence Risk

| Element | Assessment |
|---------|-----------|
| Technology Readiness Level (TRL) | 1-9 scale; below TRL 7 is pre-commercial |
| Remaining useful life | Years of productive use remaining |
| Replacement cycle | Industry standard refresh period |
| Obsolescence risk | Low / medium / high with explanation |
| Technology hedge | Can asset be repurposed if primary technology becomes obsolete? |

### 10.5 Tail Risk Identification

Low-probability, high-impact events that could cause total or near-total loss:

| Category | Example Tail Risks |
|----------|-------------------|
| Regulatory | Complete moratorium, retroactive subsidy revocation, expropriation |
| Technology | Competing technology renders asset obsolete |
| Market | Sustained commodity price collapse, demand destruction |
| Counterparty | Key customer bankruptcy, key supplier failure |
| Force majeure | Natural disaster, war, pandemic |
| Environmental | Contamination, emissions liability, stranded asset designation |

For each: estimate probability, impact magnitude, insurance/mitigation status.

### 10.6 Recovery Waterfall

In insolvency, who gets paid first?

```
1. Secured creditors (senior secured debt)     ← First priority
2. Priority claims (employee wages, taxes)
3. Unsecured creditors (trade payables, unsecured debt)
4. Mezzanine / subordinated debt
5. Preferred equity
6. Common equity                                ← Last priority (residual)
```

Show what the recovery rate is at each level given the liquidation value estimate from §10.1.

### 10.7 Presentation by Track

| Track | Deliverable | Depth |
|-------|------------|-------|
| Seed | 0.5 IM page | Brief mention of downside scenario and pivot optionality |
| Growth-Infra | 1-2 IM pages | Liquidation value + replacement cost + bear case scenario |
| Institutional | 2-3 IM pages | Full distress analysis + recovery waterfall + tail risk quantification + insurance coverage review |

### 10.8 Red Flags

- No tangible asset recovery value (pure goodwill/IP business at institutional track)
- Technology at risk of obsolescence within financing tenor
- No insurance coverage for key operational risks
- Zero residual value at debt maturity in lender case
- Recovery waterfall shows <60% senior debt coverage in distress scenario
- Tail risks identified but no mitigation strategy documented

---

## 11. Cross-Reference Validation Matrix

### 11.1 The Evercore Standard

Every market research package must pass these 9 internal consistency tests. Run all 9 after completing research; failures must be investigated and resolved before declaring research complete.

| # | Cross-Reference | Test | Threshold | Red Flag If Fails |
|---|----------------|------|-----------|-------------------|
| 1 | C1 TAM × C1 SOM | SOM capture rate realistic? | Seed <5%, Growth <10%, Institutional <15% | Implies unrealistic market capture without GTM plan |
| 2 | C1 SOM × C3 ASP → C5 Revenue | SOM × average selling price = FM revenue for Year X | Within 20% | Financial model disconnected from market sizing |
| 3 | C4 comps × C5 FM → Valuation | Implied valuation from FM within comp range | Within 30% | Either model is too optimistic or comps are wrong |
| 4 | C5 growth vs. C1 CAGR | Company revenue growth > market growth? | If yes, must have share-gain plan | Unsupported growth assumption (growing faster than market without explanation) |
| 5 | C3 pricing vs. C2 comp pricing | Company pricing within competitive range | 50-150% of competitor pricing | Pricing not market-tested; too high or suspiciously low |
| 6 | C5 CAPEX vs. C4 asset comps | CAPEX per unit within comparable range | Within 25% | Cost assumptions unrealistic (too low = under-built; too high = over-paying) |
| 7 | C3 revenue waterfall → C5 net revenue | Gross-to-net haircut reflected in FM | Exact match | Revenue leakage not modeled; FM shows gross revenue as net |
| 8 | C6 regulatory timeline → C5 revenue start | Revenue doesn't precede regulatory approval | Timeline consistent | Revenue assumed before asset is legally permitted to operate |
| 9 | C7 distress value → C5 debt sizing | Distress recovery ≥ 60% of senior debt | Lender comfort threshold | Over-leveraged for asset quality; debt not supportable in distress |

### 11.2 Pass Requirements by Track

| Track | Minimum Passing | Notes |
|-------|----------------|-------|
| Seed | 5 of 9 | Tests 1, 2, 4, 5 are most critical at seed |
| Growth-Infra | 7 of 9 | All except 7 and 9 (which require detailed operational data) |
| Institutional | 9 of 9 | All must pass; failures require documented resolution |

### 11.3 Resolution Process

When a cross-reference test fails:

1. **Flag**: Document the failure with specific numbers
2. **Investigate**: Identify root cause — which input is wrong?
3. **Determine**: Is the market research wrong, or is the FM wrong?
4. **Fix**: Correct the wrong input with better evidence
5. **Re-run**: Execute the cross-reference test again
6. **Document**: Record the adjustment, rationale, and new result

---

## 12. Anti-Patterns & Common Failures

### 12.1 The Ten Recurring Errors

| # | Anti-Pattern | Description | How to Detect | How to Fix |
|---|-------------|-------------|---------------|------------|
| 1 | **Cherry-picked TAM** | Using the largest defensible number without honest filtering to SAM/SOM | SOM/TAM ratio >15%; no derivation chain; single methodology | Require dual methodology (top-down + bottom-up) with reconciliation |
| 2 | **Survivorship bias in comps** | Only showing successful exits, up-rounds, and favorable transactions | No failed comps; no down-round comps; all comps show growth | Require minimum 2 negative precedents (failures, down-rounds, distressed) |
| 3 | **Circular sourcing** | Source A cites Source B which cites Source A; no primary origin | Trace citation chains to primary source; check if sources reference each other | Require Tier 0 or Tier 1a evidence for key findings |
| 4 | **Vanity metrics** | Using impressive-sounding but irrelevant numbers (total downloads, registered users, gross bookings) | Metric doesn't connect to revenue or investor return | Every metric must map to a financial model input |
| 5 | **Stale data as current** | Using 2023/2024 data in a 2026 analysis without freshness caveat | Check publication date of every source against freshness requirements §3.2 | Enforce freshness requirements; flag stale data explicitly |
| 6 | **Consensus-as-conviction** | Presenting mainstream analyst estimates as if they were proprietary insight | No variant view; all sources agree; analysis adds no new perspective | Require consensus/variant tagging per §3.3; identify where YOUR view differs |
| 7 | **Assumption anchoring** | Building FM first, then finding market research to justify pre-determined assumptions | Key assumptions exactly match one convenient source; no range or sensitivity | Market research must precede or be provably independent of FM development |
| 8 | **Geographic mismatch** | Using US data for a European market, or national data for a local market | Check geography of every source vs. target market geography | Flag geographic mismatches; require local data for key assumptions; apply adjustments with documented methodology |
| 9 | **Denominator manipulation** | Narrowing SAM definition to inflate company's apparent market share | SAM suspiciously small relative to TAM; SAM definition excludes obvious market segments | Require explicit SAM derivation with each filter documented and justified |
| 10 | **Revenue without risk** | Showing revenue potential without degradation, curtailment, credit risk, or price risk | No revenue waterfall; no merchant risk analysis; revenue = gross theoretical maximum | Require C3 revenue waterfall for all physical/infrastructure assets |

---

## 13. Presentation Standards by Deliverable

### 13.1 Category-by-Deliverable Matrix

| Deliverable | C1 Sizing | C2 Competitive | C3 Pricing | C4 Comps | C5 FM | C6 Regulatory | C7 Downside |
|-------------|-----------|---------------|------------|---------|-------|--------------|------------|
| **Pitch Deck** | 1 slide: TAM/SAM/SOM funnel | 1 slide: 2x2 matrix | 1 slide: unit economics | — | 1 slide: projections | Embedded in "Why Now" slide | — |
| **Executive Summary** | 1 paragraph | 1 paragraph | 1 paragraph | — | 1 paragraph | 1 sentence | — |
| **Mgmt Presentation** (30-50pp) | 3-5 pages | 2-3 pages | 2-3 pages | 2-3 pages | 3-5 pages | 1-2 pages | 1 page |
| **IM (Seed)** | §5 (1-2pp) | §8 (1pp) | §6 (1-2pp) | Appendix F | §10 (1pp) | In §5 | Brief in §10 |
| **IM (Institutional)** | §4-5 (5-8pp) | §7 (3-5pp) | §6 (3-5pp) | §8 + Appendix (3-5pp) | §9-10 (5-8pp) | §11 (2-3pp) | §12 (2-3pp) |
| **Data Room** | 06.01 | 06.03 | 06.04 | 06.02 | 03_Model | 06.05 | 06.06 |

### 13.2 Data Room Sub-Folder Structure (Stonepeak Standard)

```
06_Market/
├── 06.01_Market_Study/         # Independent market study (if commissioned); else management analysis
├── 06.02_Comparable_Analysis/  # Comp tables, football fields, source data
├── 06.03_Competitor_Profiles/  # Individual file per major competitor
├── 06.04_Pricing_Evidence/     # Contracts, LOIs, benchmark data, WTP analysis
├── 06.05_Regulatory_Analysis/  # Permits, policy papers, legal opinions
├── 06.06_Downside_Analysis/    # Liquidation analysis, distress comps, tail risk
└── 06.07_Supply_Chain/         # Vendor quotes, lead times, supply constraint data
```

### 13.3 General Presentation Principles

- **Lead with "so what"**: Every section starts with the conclusion, then supporting evidence
- **Source everything**: No unsourced claims in any deliverable
- **Scenario range**: Present base/bull/bear, not a single point estimate
- **Visual hierarchy**: Tables for data, charts for trends, bullet points for analysis
- **Investor-readable**: External readers must understand without context from the author

---

## 14. Quality Gates by Stage

### 14.1 Gate Definitions

| # | Gate | Seed | Growth-Infra | Institutional |
|---|------|------|-------------|---------------|
| 1 | Market sizing sources | 2+ (Tier 1b+) | 4+ (Tier 1a or 1b) | 5+ (Tier 1a required for key inputs) |
| 2 | Evidence type | Hypotheses with directional data | Validated with operating evidence | Audited / independently verified |
| 3 | Competitor profiles | 5+ direct | 10+ (direct + indirect) | 20+ with market share data |
| 4 | Pricing evidence | LOIs / pilots / WTP survey | Multi-quarter revenue history | Multi-year contracted + sensitivity analysis |
| 5 | Comp transactions | 5+ (funding rounds ok) | 10+ (all 4 types attempted) | 15+ (all 4 types + yield comps) |
| 6 | FM assumption sourcing | 50%+ inputs sourced | 80%+ sourced | 100% sourced; Tier 1 for key inputs |
| 7 | Data freshness | <18 months | <12 months | <6 months |
| 8 | Cross-reference tests | 5/9 passing | 7/9 passing | 9/9 passing |
| 9 | Regulatory analysis | Key tailwinds named | Full mapping + timeline | Independent legal opinion obtained |
| 10 | Downside analysis | Qualitative bear case | Liquidation value + 1 scenario | Full distress analysis + recovery waterfall |
| 11 | Third-party validation | Not required | Recommended (advisor review) | Required (independent market study and/or model audit) |

### 14.2 Gate Interpretation

- **Must pass all gates for the applicable track** to declare market research "complete"
- Gates are cumulative: Institutional must pass all Seed and Growth-Infra gates PLUS its own
- Partially-met gates should be documented as "open items" with owner and deadline
- Gates are minimum standards, not targets — exceeding gates is always appropriate

---

## 15. Handling Data-Poor / Nascent Markets

### 15.1 When This Section Applies

Use these techniques when:
- Tier 1 sources don't exist for this specific market
- Market is genuinely new (no historical data)
- Adjacent market data is the best available proxy
- Total research yields <3 independent sources for key metrics

### 15.2 Six Strategies for Nascent Markets

1. **Analogue-based sizing**: Use adoption curves from analogous markets (e.g., smartphone adoption curve applied to VR headsets; solar adoption curve applied to BESS; cloud adoption applied to edge computing). Document the analogue, the mapping logic, and the limitations.

2. **Primary research escalation**: When published data doesn't exist, Tier 0 becomes the primary source. Commission expert network calls, run proprietary surveys, conduct customer interviews. Budget appropriately: 5-10 expert calls at $500-1,500/hour for institutional track.

3. **Triangulation requirement**: Minimum 3 independent estimation methodologies, even if each has low confidence individually. Convergence across independent methods increases confidence. Divergence requires investigation.

4. **Explicit uncertainty quantification**: Provide confidence intervals, not point estimates.
   - Bad: "TAM is $10B"
   - Good: "TAM is $5-15B (80% confidence interval); our base case is $10B"

5. **Scenario-weighted output**: Present base / bull / bear with explicit probability weights.
   - Example: Bull (20% probability, $15B TAM), Base (60%, $10B), Bear (20%, $5B)
   - Expected TAM = 0.2×15 + 0.6×10 + 0.2×5 = $10B (but the range is $5-15B)

6. **Explicit disclosure**: State that the market is nascent and that sizing is inherently uncertain. This builds credibility rather than undermining it. Investors respect honesty about uncertainty more than false precision.

### 15.3 Documentation Standard for Nascent Markets

Every metric in a nascent market must include:
- Methodology used (which of the 6 strategies above)
- Confidence level (Low / Medium with explanation — High is unlikely for nascent markets)
- Analogue referenced (if applicable)
- Range, not point estimate
- Key assumption that could invalidate the estimate
- Date of assessment (nascent market data dates quickly)

---

## Appendix A: Glossary

| Term | Definition |
|------|-----------|
| TAM | Total Addressable Market — total revenue opportunity |
| SAM | Serviceable Addressable Market — TAM filtered by geography, segment, capability |
| SOM | Serviceable Obtainable Market — realistic near-term capture |
| HHI | Herfindahl-Hirschman Index — market concentration measure |
| DSCR | Debt Service Coverage Ratio — cash available for debt service / debt service |
| LTV | Loan-to-Value (in finance context) or Lifetime Value (in customer context) |
| CAC | Customer Acquisition Cost |
| CoE | Cost of Equity |
| WACC | Weighted Average Cost of Capital |
| TRL | Technology Readiness Level (1-9 scale) |
| EV | Enterprise Value |
| IRR | Internal Rate of Return |
| NPV | Net Present Value |
| LTM | Last Twelve Months |
| COD | Commercial Operation Date |

## Appendix B: Related Files

| File | Location | Purpose |
|------|----------|---------|
| Market Data Template | `_shared/market-data.md` | Field schema for market research data (sector-agnostic) |
| Market Research Intake | `_shared/intake-modules/m-market-research.md` | 3-layer intake questionnaire |
| Overlay Specification | `_shared/overlays/README.md` | Sector overlay format and requirements |
| Seed Fundraising | `seed-fundraising/SKILL.md` | Phase 3 references this framework |
| IM Institutional Intake | `Intake_IM_institutional/SKILL.md` | Phase 2 + 12 reference this framework |
| Research Engine | `research-engine/SKILL.md` | Uses credibility framework §3 |
| Competitive Intel | `competitive-intel/SKILL.md` | Writes to C2/C3 data targets |
| Project Financing | `project-financing/SKILL.md` | Reads C4/C5/C6 for validation |
| FM Interpreter | `financial-model-interpreter/SKILL.md` | Reads C5 for assumption audit |

---

*Framework version 2.0 — Last updated 2026-03-31*
*Methodology sources: Goldman Sachs (consensus/variant), JPMorgan (margin pool, selection criteria), Stonepeak (4 comp types), Macquarie (yield comps, lender case, development discount), KKR (value creation bridge), Brookfield (operational benchmarking, liquidation value), GIP (supply-side constraints, moat quantification), ECP (revenue waterfall), Evercore (cross-reference validation)*
