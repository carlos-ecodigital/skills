---
chunk_id: "deal-economics"
domain: "economics"
category: "deal-metrics"
tags: ["economics", "deal", "revenue", "costs", "heat-price", "BESS", "investor"]
depends_on: []
token_count_approx: 600
version: "2.0"
last_updated: "2026-02-24"
status: "active"
summary: >-
  Sanitized deal economics for external use. Indicative figures for energy recycling
  pricing, AI colocation revenue, BESS economics, and integrated platform value.
  Includes WCK grower cost structure (EUR 0 CAPEX/OPEX model). Suitable for
  marketing and presentations. No internal-only assumptions or negotiation positions.
---

# Digital Energy -- Deal Economics (Sanitized for External Use)

Economics suitable for marketing materials, presentations, and general external communications. All figures are indicative and derived from published market data, project-level analysis, or partner indications.

**Classification:** Suitable for external use. No internal-only financial assumptions, counterparty-specific terms, or negotiation positions.

---

## 1. Energy Recycling Economics

### Revenue Model
- DE builds, owns, and operates the DEC on partner land
- Recycled thermal energy is sold to adjacent users (growers, district heating, industry)
- Partner (grower/grid-rights holder) receives agreed share of heat revenues
- DE funds all infrastructure CAPEX

### Grower Cost Structure (WCK Model)
- **EUR 0 CAPEX** — DE finances and builds all DEC infrastructure. Grower invests nothing.
- **EUR 0 OPEX** — Grower pays nothing for heat. DE's revenue comes from AI colocation + SDE++ thermal subsidy + grid flexibility, not from the grower.
- **Net position: potentially positive** — Grower's existing CHP/e-boiler assets are freed from heat duty, becoming available for grid balancing (mFRR, aFRR) and generating new flexibility revenue. The grower's net energy cost position can turn negative (earning rather than spending).
- **The "<EUR 0/MWh" in superiority tables** refers to this net position after accounting for freed flexibility revenue from CHP/e-boiler assets.

### Indicative Heat Economics

| Parameter | Conservative | Base Case | Optimistic |
|---|---|---|---|
| Heat price | EUR 10/MWh | EUR 15/MWh + CPI | EUR 20-25/MWh + CPI |
| Utilization rate | 50% | 70% | 85% |
| Energy recycling efficiency | 97% | 97% | 97% |
| Delivered temperature | 70-80°C (via heat pump upgrade from 50-65°C server output) | 70-80°C | 70-80°C |
| Annual heat revenue per MW IT | ~EUR 42K | ~EUR 89K | ~EUR 181K |

### Comparison to Natural Gas
| Parameter | Natural Gas (2025) | DEC Recycled Thermal Energy |
|---|---|---|
| Commodity cost | EUR 35-45/MWh (TTF-linked, volatile) | EUR 10-15/MWh (CPI-indexed, stable) |
| Carbon cost (from 2027) | EUR 45-65/tonne CO2 (EU ETS2 projected) | Zero — recycled energy, no combustion |
| Price volatility | High (TTF spot; geopolitical exposure) | Low (CPI-indexed, contractual) |
| CAPEX required from buyer | Maintenance/replacement of existing boilers | Zero — DE funds heat infrastructure |
| Estimated cost saving | — | 60-80% reduction in heating cost |

### Regulatory Price Context
- EU ETS2 (2027): Adds EUR 10-20/MWh to gas-fired heating cost
- Wcw (2026-2027): Forces cost-based tariffs for district heating; eliminates gas-linked pricing
- Dutch VAT on heat supply: 9% reduced rate (vs. 21% standard)

---

## 2. AI Colocation Economics

### Revenue Model
- Colocation: customer places own hardware in DE facility
- GPUaaS: DE owns hardware, sells compute-as-a-service
- Powered shell: customer builds out interior, DE provides power + cooling + connectivity

### Indicative Colocation Pricing (NL Market)

| Model | Indicative Price Range | Source Context |
|---|---|---|
| DE wholesale colocation (target) | EUR 150/kW/month | DE commercial positioning |
| Annual revenue per 4.2 MW DEC block (colo only) | EUR 7.56M/year | 4,200 kW × EUR 150 × 12 months |
| Wholesale colocation (market avg) | $200-250/kW/month | CBRE global avg $217; Amsterdam at/above average |
| Retail colocation | EUR 495+/month per 48U rack (excl. power) | NL market data |
| Cross-connect | EUR 150-300/month per cable | NL market data |
| GPU-as-a-Service (H100) | $1.49-4.00/GPU-hour | GMI Cloud 2025 pricing |

### Data Center CAPEX Benchmarks (NL)

| Component | Range | Source |
|---|---|---|
| Facility CAPEX (excl. GPUs) | EUR 8-15M/MW IT | Turner & Townsend DCCI; Alantra |
| Fully loaded (incl. land, grid, permitting) | EUR 12-16M/MW IT | T&T Amsterdam 2025 |
| GPU hardware (per MW equivalent) | EUR 25-30M/MW additional | Based on H100/B200 cluster pricing |
| PUE target | 1.2 | DE design specification |

### Market Dynamics
- NL DC vacancy: 5% (2025) — near full absorption
- Amsterdam moratorium: no new builds until 2030+
- National hyperscale restriction: >70 MW and >100K sqm requires central approval
- DE operates below hyperscale threshold: sub-70 MW facilities on existing grid connections

---

## 3. BESS Economics

### Revenue Model
- Joint venture structure: 50/50 equity split with Energy Partner
- Non-recourse project finance: 70-80% debt gearing (contracted revenue)
- Revenue stacking: energy arbitrage + FCR + aFRR + congestion management
- Grid connection shared with future DC under cable pooling

### Indicative BESS Economics

| Parameter | Conservative | Base Case | Optimistic |
|---|---|---|---|
| CAPEX per kWh (LFP) | EUR 250/kWh | EUR 180-200/kWh | EUR 150/kWh |
| Project equity IRR | 8-10% | 12-15% | 17-20%+ |
| Debt gearing | 60-65% (merchant) | 70-75% (partial contract) | 75-80% (contracted) |
| Revenue per MW/month | EUR 7,600 | EUR 10,000 | EUR 14,500 |
| Construction timeline | 6-12 months | 6-12 months | 6-12 months |

### Revenue Stack Contribution
| Source | Typical Share | Bankability |
|---|---|---|
| Day-ahead arbitrage | 40-60% | Medium (merchant) |
| FCR (frequency containment) | 15-25% | High (contracted) |
| aFRR (automatic restoration) | 10-20% | High (capacity contract) |
| Intraday trading | 5-15% | Low (fully merchant) |
| Congestion management | 5-10% | Medium (emerging) |

### Strategic Value Beyond Standalone Returns
- BESS generates standalone returns during DC development period (2-3 years before heat revenue)
- BESS equity converts to DC SPV equity at DC financial close (no additional cash required)
- Cable pooling under Energiewet enables grid-sharing between BESS and DC
- BESS demonstrates operational capability to institutional investors during DC fundraise

---

## 4. Integrated Platform Economics

### The Full Stack Value

| Revenue Stream | Source | Timing | Risk Profile |
|---|---|---|---|
| BESS returns | Arbitrage + ancillary services | Year 1-2 (standalone) | Medium (merchant/contracted mix) |
| Heat revenue | Recycled thermal energy sales | Year 3+ (DC operations) | Low (identified buyers, CPI-indexed) |
| Colocation revenue | Rent + power pass-through | Year 3+ (DC operations) | Low-medium (contracted) |
| Grid value appreciation | Scarcity premium on secured capacity | Ongoing | Low (structural) |

### Why Integration Beats Point Solutions

| Standalone | Integrated (DE Model) |
|---|---|
| BESS: single revenue stream, one asset class | BESS + DC + heat: three revenue streams, risk diversification |
| DC: cooling is pure cost (chiller OPEX) | DC cooling cost partially/fully offset by heat revenue — digital cogeneration |
| Heat supply: requires dedicated heat source (gas, geothermal) | Heat supply: recycled energy from compute operations — no fuel input |
| Grid connection: single-use capacity allocation | Grid connection: multi-use via cable pooling (BESS + DC) |

---

## 5. Usage in Marketing Materials

### What You Can Say
- Market-level economics with source attribution (CBRE, BNEF, T&T, etc.)
- Three-scenario frameworks (conservative/base/optimistic)
- Comparison to alternatives using published benchmarks
- General DE economics with "indicative" qualifier

### What Requires Caution
- Project-specific financial projections (only with "subject to definitive agreements" qualifier)
- Partner-specific revenue shares (only in materials for that specific partner)
- Internal financial model outputs (never in external materials)
- Forward-looking return projections (use "indicative" and "base case" qualifiers)

### What You Must Not Say
- Guaranteed returns or specific IRR promises
- Exact counterparty terms from active negotiations
- Internal valuations or equity allocation details
- Comparison that names specific competitors with pricing claims (use "market range" instead)
