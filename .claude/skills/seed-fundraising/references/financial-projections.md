# Financial Projections Guide -- Seed Stage

## 1. Purpose

Seed-stage financial projections serve two audiences: investors evaluating your business sense, and your team planning resource allocation. At seed stage, the projections are a PLAN, not a forecast. Investors know the numbers will change. What they're evaluating is: does this founder understand the economics of their business?

**Key principle**: Keep it simple. A seed model should be built in 2-4 hours, not 2-4 weeks. The detailed PF model comes later (see `project-financing/references/financial-modeling.md` for that).

## 2. Seed-Stage Model Architecture

### What to Build

| Component | Include | Exclude at Seed |
|---|---|---|
| Revenue projections | 3-5 year by stream | Complex stochastic revenue models |
| Cost structure | Monthly for Year 1, quarterly Y2, annual Y3-5 | Full three-statement integrated model |
| Unit economics | Per-site / per-MW / per-customer | Monte Carlo simulations |
| Cash flow | Monthly burn rate and runway | Full cash flow waterfall |
| Key metrics | Growth rate, margins, breakeven | DSCR/LLCR/PLCR (that's PF territory) |
| Scenarios | Base, upside, downside | 20-variable sensitivity matrix |
| Cap table | Current + this round + Series A dilution | Full option pool waterfall |

### Model Structure (Spreadsheet)

| Tab | Contents |
|---|---|
| Assumptions | All inputs in one place, clearly labeled |
| Revenue | Revenue by stream, per period |
| Costs | OPEX by category, CAPEX phasing |
| P&L | Revenue - COGS - OPEX = EBITDA (keep it high-level) |
| Cash Flow | Operating CF, investing CF, financing CF, closing cash |
| Metrics | Key KPIs per period |
| Cap Table | Pre/post-money, option pool, dilution |
| Scenarios | Toggle between base/upside/downside |

## 3. Revenue Modeling for Infrastructure/Energy

### Revenue Streams for a DE-Type Company

| Stream | Model | Key Drivers | Year 1 | Year 3 | Year 5 |
|---|---|---|---|---|---|
| BESS Arbitrage | $/MW/year | MW deployed, spread capture, cycling | First site | Multi-site | Portfolio |
| BESS Ancillary (FCR/aFRR) | $/MW/year | MW deployed, auction prices, availability | First site | Multi-site | Portfolio |
| AI Colocation | $/kW/month | MW IT load, occupancy %, pricing | Pre-lease | Ramp-up | Stabilized |
| Heat Supply | EUR/MWh | MW thermal, hours, price, offtake % | First delivery | Multi-customer | Contracted base |
| Grid Services | $/MW/year | Congestion management contracts | Emerging | Growth | Established |

### Revenue Build-Up Approach

**Bottom-up per site**:
```
Site Revenue = (BESS MW x BESS Rev/MW/yr) + (DC MW x Occupancy% x $/kW/mo x 12) + (Heat MW x Hours x EUR/MWh)
```

**Portfolio roll-up**:
```
Total Revenue = Sum(Site Revenue) for each operational site, phased by construction timeline
```

### Phasing Assumptions

| Site | Construction Start | BESS COD | DC Phase 1 | DC Stabilized |
|---|---|---|---|---|
| Site 1 | Q1 2026 | Q3 2026 | Q1 2027 | Q3 2027 |
| Site 2 | Q3 2026 | Q1 2027 | Q3 2027 | Q1 2028 |
| Site 3 | Q1 2027 | Q3 2027 | Q1 2028 | Q3 2028 |

## 4. Cost Structure

### OPEX Categories

| Category | Typical Range | Notes |
|---|---|---|
| Team / Payroll | 40-60% of OPEX at seed | Largest cost; scale as you hire |
| O&M (BESS) | EUR 8-15K/MW/year | Contracted to O&M provider |
| O&M (DC) | 2-4% of DC CAPEX/year | Facilities management, maintenance |
| Energy costs | Pass-through with margin | Grid tariffs, commodity, ODE |
| Insurance | 0.3-0.5% of asset replacement cost | CAR/EAR during construction, operational after |
| Land lease | EUR 5-15K/MW/year | Recht van opstal or erfpacht |
| Professional services | EUR 100-300K/year | Legal, accounting, tax, advisory |
| Corporate overhead | EUR 50-150K/year | Office, travel, software, admin |

### CAPEX Phasing

| Item | Cost Range | Timing |
|---|---|---|
| BESS (per site) | EUR 330-700K/MW | 6-12 month construction |
| DC shell + core | EUR 8-12M/MW IT load | 18-24 month construction |
| DC fit-out | EUR 1-3M/MW incremental | Phased with customer take-up |
| Grid connection upgrade | EUR 0.5-2M | If needed beyond existing |
| Heat infrastructure | EUR 0.5-2M per site | Piping, heat exchangers |

**At seed stage**: Show CAPEX per site, phased by quarter. Don't model the full construction cost breakdown -- that's for the PF model.

## 5. Unit Economics

### Per-Site Economics (Illustrative)

| Metric | Value | Calculation |
|---|---|---|
| Total CAPEX | EUR X M | BESS + DC Phase 1 + Heat infra |
| Annual Revenue (stabilized) | EUR X M | Sum of all streams at full occupancy |
| Annual OPEX | EUR X M | O&M + energy + insurance + land |
| Gross Margin | X% | (Revenue - OPEX) / Revenue |
| EBITDA (stabilized) | EUR X M | Revenue - OPEX |
| Payback Period | X years | CAPEX / annual EBITDA |
| Unlevered Project IRR | X% | XIRR of project cash flows |

### Key Ratios Investors Care About

| Ratio | What It Tells Investors | Seed Target |
|---|---|---|
| Monthly burn rate | How fast you spend | EUR X K/month |
| Runway | Months of cash remaining | 18-24 months post-raise |
| Revenue growth (MoM/QoQ) | Trajectory | 15-30% QoQ for infrastructure |
| Gross margin | Business quality | 40-70% (infrastructure) |
| CAC | Customer acquisition efficiency | Varies by segment |
| LTV/CAC | Unit economics health | >3x |
| Capital efficiency | Revenue per dollar raised | Track from first revenue |

## 6. Scenario Analysis (Seed-Appropriate)

Three scenarios, clearly labeled:

| Scenario | Revenue Assumption | CAPEX | Timeline | Use |
|---|---|---|---|---|
| Base Case | P50 revenue, planned sites | Budget | On schedule | Primary case for valuation |
| Downside | P75 revenue, fewer sites, delays | +15% | +6 months | Stress test for investors |
| Upside | P25 revenue, accelerated rollout | On budget | Ahead of schedule | Shows potential |

**Present the delta**: "In our downside case, runway extends to X months and we still reach Y milestone before needing Series A."

## 7. Cash Flow and Runway

### Monthly Cash Flow Table (Year 1)

| Month | Revenue | OPEX | CAPEX | Net CF | Closing Cash |
|---|---|---|---|---|---|
| M1 | -- | (Team) | -- | (X) | Seed - X |
| M2 | -- | (Team) | (BESS deposit) | (Y) | ... |
| ... | ... | ... | ... | ... | ... |
| M12 | First BESS rev | (Team + O&M) | -- | +/- | Z |

### Runway Calculation
```
Runway (months) = Cash Balance / Monthly Burn Rate
Target: 18-24 months post-close
```

**Rule of thumb**: Raise enough for 18-24 months. Plan to start Series A fundraising at month 12-15 (fundraising takes 3-6 months).

## 8. Presentation Format

### For Pitch Deck (Slide 11)
- One summary chart: revenue trajectory, 3 years
- Key metrics table: 4-5 numbers that matter
- The ask: amount, milestones, runway

### For Executive Summary
- 2-3 sentences on unit economics
- High-level Year 1-3 revenue trajectory
- Burn rate and runway

### For Investment Memorandum
- Full 3-5 year P&L summary table
- Unit economics per site
- Scenario comparison table
- Key assumptions list
- Cross-reference to detailed model in data room

### For Data Room
- Full spreadsheet model (Excel/Google Sheets)
- Assumptions document (separate PDF explaining each input)
- Scenario analysis summary

## 9. Common Mistakes

| Mistake | Fix |
|---|---|
| Over-engineering at seed | Keep it to 4-6 tabs. Save complexity for PF model. |
| Hockey stick without basis | Every growth assumption needs a driver (sites, customers, MW) |
| Ignoring working capital | BTW recovery timing, construction deposits, payment terms |
| No scenario analysis | Always show base + downside minimum |
| Inconsistent with deck | The numbers in the model MUST match the pitch deck |
| Mixing startup and PF metrics | Seed model: burn, runway, growth. PF model: DSCR, LLCR. Keep them separate. |

---

## Cross-References

| Topic | Reference File |
|---|---|
| Project finance modeling (DSCR, debt sizing) | `project-financing/references/financial-modeling.md` |
| Market benchmarks | [references/sector-thesis.md](sector-thesis.md) |
| Cap table mechanics | [references/cap-table-guide.md](cap-table-guide.md) |
| Pitch deck financial slide | [references/pitch-deck-guide.md](pitch-deck-guide.md) |
| IM financial section | [references/investment-memo-guide.md](investment-memo-guide.md) |
