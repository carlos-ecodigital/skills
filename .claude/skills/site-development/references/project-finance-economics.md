# Project Finance & Economics

## 1. Integrated Financial Model Structure

### Model Architecture

The DEC financial model must capture the full value stack — three revenue streams that together create a business case stronger than any standalone data center or greenhouse project:

```
REVENUE MODEL
  ├── Stream 1: Colocation Revenue
  │     ├── Power revenue (€/kW/month or €/kWh consumed)
  │     ├── Space revenue (€/m2 or €/cage/month) — often bundled into power
  │     ├── Cross-connect / connectivity fees
  │     └── Managed services (optional)
  │
  ├── Stream 2: Energy Revenue
  │     ├── BESS revenue (FCR + aFRR + arbitrage + congestion management)
  │     ├── Demand response revenue
  │     ├── Cable pooling savings (avoided transport tariff)
  │     ├── Imbalance optimization revenue
  │     └── SDE++ subsidy (heat delivery)
  │
  └── Stream 3: Heat Revenue
        ├── Heat supply to greenhouse (€/GJ or infrastructure fee)
        ├── SDE++ subsidy (if separate from Stream 2)
        └── Carbon credit value (if monetizable, typically not counted)

COST MODEL
  ├── CAPEX
  │     ├── Land acquisition / erfpacht (ground lease)
  │     ├── DC building construction
  │     ├── Electrical infrastructure (substation, MV/LV distribution)
  │     ├── Cooling infrastructure (CDU, dry coolers, piping)
  │     ├── Heat recovery infrastructure (heat pump, buffer tank, thermal bridge)
  │     ├── BESS system
  │     ├── Solar PV system
  │     ├── Grid connection (aansluitbijdrage)
  │     ├── Permitting and development costs
  │     └── Contingency (10-15%)
  │
  ├── OPEX
  │     ├── Electricity procurement (wholesale, PPA, network tariffs, EB, ODE)
  │     ├── Facility O&M (building, MEP, cooling, heat systems)
  │     ├── Insurance (property, liability, business interruption)
  │     ├── Property tax (onroerendezaakbelasting / OZB)
  │     ├── BRP/energy management fees
  │     ├── Staff / management costs
  │     ├── Backup fuel (gas for backup boiler)
  │     └── Compliance and reporting costs
  │
  └── FINANCING
        ├── Equity return requirement
        ├── Debt service (interest + principal)
        ├── Arrangement fees
        └── Reserve account funding
```

### Time Horizon

| Period | Financial Model Detail | Key Assumptions |
|---|---|---|
| Year -2 to 0 | Development phase (CAPEX spend, no revenue) | Land acquisition, permitting, construction |
| Year 1-3 | Ramp-up (partial occupancy, partial heat delivery) | Occupancy: 30% → 60% → 85% |
| Year 3-10 | Stabilized operation | Occupancy: 85-95%, full heat delivery |
| Year 10-20 | Mature operation + expansion | Equipment refresh cycles, Phase 2 CAPEX |
| Year 20-25 | Terminal value or exit | Residual asset value, contract renewals |

## 2. CAPEX Build-Up

### Phase 1 CAPEX (40 MW IT, indicative)

| Category | Sub-Item | Cost (€M) | Notes |
|---|---|---|---|
| **Land & Site** | | **3-8** | |
| | Land purchase/erfpacht | 1-5 | Highly location-dependent |
| | Site preparation (grading, piling, sanering) | 1-3 | Dutch soil = piling needed almost everywhere |
| | Archaeology, ecology, site surveys | 0.1-0.3 | |
| **DC Building** | | **15-25** | |
| | Structure (steel frame, foundation, cladding, roof) | 8-15 | Purpose-built AI factory shell |
| | MEP fit-out (MV/LV rooms, cooling plant rooms) | 4-7 | |
| | Fire suppression system | 1-2 | |
| | Security, BMS, monitoring | 1-2 | |
| **Electrical** | | **8-15** | |
| | Grid connection (aansluitbijdrage) | 2-5 | 50 kV connection to nearest substation |
| | On-site substation + transformers | 3-5 | MV/LV transformation |
| | Busway/distribution to racks | 2-4 | |
| | Backup generators (if included) | 1-3 | Diesel generators for Tier III reliability |
| **Cooling** | | **6-12** | |
| | CDU (Coolant Distribution Units) | 2-4 | For liquid-cooled GPU racks |
| | Dry coolers (adiabatic) | 2-4 | Reject heat when not recovered |
| | Piping (primary + secondary loops) | 1-3 | |
| | Heat recovery HX and controls | 0.5-1 | |
| **Heat Infrastructure** | | **5-10** | |
| | Heat pump system (industrial, 2-5 MWth) | 2-5 | R717 ammonia or R744 CO2 |
| | Buffer tank (2,000-5,000 m3) | 1-2 | Steel or concrete |
| | Thermal bridge (pre-insulated pipe, 200-500 m) | 0.5-1.5 | Logstor/Isoplus below-ground |
| | Backup gas boiler | 0.3-0.6 | Grower confidence |
| | Metering, controls, SCADA | 0.2-0.4 | |
| **BESS** | | **8-15** | |
| | Battery system (20 MW / 40 MWh LFP) | 6-10 | Container-based, turnkey |
| | BMS/PCS (power conversion system) | 1-2 | |
| | BESS enclosure, fire suppression, grid connection | 1-3 | PGS 37 compliance |
| **Solar PV** | | **3-5** | |
| | 5 MWp rooftop + ground-mount | 3-5 | Cable pooling with DC and BESS |
| **Development Costs** | | **2-4** | |
| | Permitting (omgevingsvergunning, MER, advisors) | 0.5-1.5 | |
| | Engineering/design (architectural, MEP, structural) | 0.5-1.5 | |
| | Legal, financial advisory | 0.3-0.5 | |
| | Project management during development | 0.3-0.5 | |
| **Contingency** | | **5-10** | 10-15% of above |
| **TOTAL Phase 1 CAPEX** | | **€55-105M** | Wide range reflects location, specification, market conditions |

### Key CAPEX Benchmarks

| Metric | DEC Range | Market Comparison |
|---|---|---|
| €/kW IT capacity (total facility) | €1,375-2,625/kW | Standard DC: €1,000-1,500/kW; AI factory: €2,000-3,500/kW |
| Heat infrastructure as % of total | 9-15% | Unique to DEC (standard DC: 0%) |
| BESS as % of total | 12-18% | Growing trend, not standard for DC |
| Grid connection as % of total | 4-8% | Location-dependent; can be much higher |

**DEC cost advantage:** Heat infrastructure (€5-10M) adds cost but generates a new revenue stream (heat + SDE++) that standard DCs don't have. Net impact depends on heat revenue, which at scale covers the infrastructure cost within 3-5 years.

## 3. Revenue Model

### Stream 1: Colocation Revenue

| Item | Pricing Model | Typical Range | Annual Revenue (40 MW, 85% occupancy) |
|---|---|---|---|
| **Power** | €/kW/month (contracted) | €80-150/kW/month | €27-51M/year |
| **Space** | Often bundled with power | Included above | -- |
| **Cross-connects** | €/cross-connect/month | €200-500/month each | €0.2-0.5M/year |
| **Managed services** | Optional upcharge | Variable | €0-2M/year |
| **Total colocation** | | | **€27-54M/year** |

**Critical dependency:** Colocation revenue depends entirely on tenant occupancy and pricing power. DEC as a new entrant must offer competitive pricing to attract first tenants, potentially below market rates initially.

### Stream 2: Energy Revenue

| Item | Revenue Mechanism | Annual Revenue (40 MW DC + 20 MW BESS) |
|---|---|---|
| BESS FCR + aFRR | TenneT prequalification, daily auctions | €1.5-3M/year |
| BESS day-ahead + imbalance arbitrage | EPEX SPOT, TenneT imbalance | €0.5-1.5M/year |
| BESS congestion management | GOPACS platform | €0.1-0.5M/year |
| Cable pooling savings | Avoided transport tariff on self-consumption | €0.2-0.3M/year |
| DC demand response | aFRR/mFRR, GOPACS | €0.1-0.5M/year |
| **Total energy revenue** | | **€2.4-5.8M/year** |

### Stream 3: Heat Revenue

| Item | Revenue Mechanism | Annual Revenue (30 MWth recovery) |
|---|---|---|
| Heat supply (€/GJ to grower) | Heat supply agreement | €0.5-2M/year (at €5-12/GJ) |
| SDE++ subsidy | RVO subsidy for waste heat delivery | €1-4M/year (depends on basisbedrag and gas price) |
| **Total heat revenue** | | **€1.5-6M/year** |

### Total Revenue Summary (Stabilized Year)

| Stream | Low Case | Base Case | High Case |
|---|---|---|---|
| Colocation | €27M | €38M | €54M |
| Energy | €2.4M | €4M | €5.8M |
| Heat | €1.5M | €3.5M | €6M |
| **Total** | **€31M** | **€45.5M** | **€65.8M** |
| Non-colo revenue as % of total | 13% | 16% | 18% |

**Investor narrative:** Non-colocation revenue represents 13-18% of total — enough to meaningfully improve economics and differentiate DEC, but not so high that the business case depends on it. This makes the heat/energy revenue a "bonus" that de-risks the overall investment.

## 4. Investment Metrics

### Key Metrics

| Metric | Target | Calculation | DEC Range |
|---|---|---|---|
| **IRR (project)** | 12-18% unlevered | NPV of project cashflows = 0 | 14-20% with heat + BESS revenue |
| **IRR (equity)** | 15-25% levered | NPV of equity cashflows = 0 | 18-28% with leverage |
| **NPV** | >0 at WACC | DCF of all cashflows | Highly dependent on assumptions |
| **DSCR (Debt Service Coverage Ratio)** | >1.3× minimum | Annual cashflow / annual debt service | 1.4-1.8× at stabilization |
| **LLCR (Loan Life Coverage Ratio)** | >1.2× minimum | NPV of cashflows over loan life / outstanding debt | 1.3-1.6× |
| **Payback (simple)** | <6 years | CAPEX / annual net cashflow | 4-7 years |
| **Cash yield (stabilized)** | >8% | Annual free cashflow / total CAPEX | 8-14% |

### DEC IRR Enhancement from Heat + Energy

**Without heat and energy revenue (standard DC):**
- CAPEX: €50-85M (no BESS, no heat infra, no solar)
- Revenue: colocation only = €27-54M/year
- Unlevered IRR: 12-16%

**With heat and energy revenue (DEC model):**
- CAPEX: €55-105M (includes BESS, heat infra, solar)
- Revenue: colocation + energy + heat = €31-66M/year
- Unlevered IRR: 14-20%

**IRR enhancement:** +2-4 percentage points from heat + energy revenue. This is significant — it can make the difference between "marginal investment" and "compelling investment" for infrastructure investors.

## 5. Financing Structure

### Capital Structure Options

| Structure | Equity / Debt | Typical for DEC | Considerations |
|---|---|---|---|
| **All equity** | 100% / 0% | Seed stage (pre-revenue) | No debt service, maximum flexibility; highest cost of capital |
| **Conservative leverage** | 60% / 40% | Early operation (partial occupancy) | Low debt = low risk; banks comfortable with limited track record |
| **Standard project finance** | 30-40% / 60-70% | Stabilized operation | Requires 1.3× DSCR; colocation contracts support debt |
| **Aggressive leverage** | 20% / 80% | Mature, contracted cashflows | Only with long-term tenant contracts; re-fi at COD or stabilization |

### Financing Phases

| Phase | Instrument | Source | Amount | Timing |
|---|---|---|---|---|
| **Seed equity** | Convertible note / SAFE / equity | Angels, family offices, strategic | €1-5M | Pre-development |
| **Development equity** | Series A / co-development | Infrastructure PE, strategic partner | €5-20M | Site acquisition through construction start |
| **Construction debt** | Facility agreement | Infrastructure bank (ING, ABN AMRO, Rabobank) | €30-60M | Construction period |
| **Equity bridge** | Draw-down facility | Same as development equity | €10-20M | To cover equity portion during construction |
| **Refinancing at COD** | Term loan / project bond | Infrastructure debt funds | €40-70M | At commercial operation date (COD) |

### Bankability Considerations

**What lenders want to see:**

| Requirement | DEC Response |
|---|---|
| Contracted revenue (off-take) | Colocation agreements with creditworthy tenants (neocloud, enterprise) |
| Proven technology | Standard DC technology + proven heat pump + standard BESS |
| Experienced management | DEC team + experienced EPC contractor + O&M partner |
| Construction risk mitigation | Fixed-price EPC, completion guarantee, liquidated damages |
| Revenue certainty | PPA for energy cost; SDE++ for heat subsidy; tenant contracts for colocation |
| Insurance | Builder's all-risk (CAR), operational property, business interruption |
| Grid connection certainty | Signed aansluitovereenkomst (connection agreement) with timeline |

**DEC bankability challenge:** Heat revenue and BESS revenue are newer asset classes for infrastructure lenders. Strategy: underwrite debt on colocation revenue alone, treat heat/energy as upside.

## 6. Dutch Fiscal Incentives

### EIA (Energie-investeringsaftrek / Energy Investment Allowance)

**What it is:** Additional tax deduction for investments in energy-efficient or renewable energy equipment. The investment is deducted from taxable profit ON TOP of normal depreciation.

| Parameter | Value |
|---|---|
| Deduction rate | 45.5% of qualifying investment (2025 rate) |
| Corporate tax rate (vpb) | 25.8% (above €200K profit) |
| Effective CAPEX reduction | 45.5% × 25.8% = ~11.7% of qualifying investment |
| Qualifying equipment | Heat pumps, heat recovery systems, BESS, energy-efficient cooling, LED grow lights |
| Maximum per project | €150M investment per project |
| Application | RVO (Rijksdienst voor Ondernemend Nederland) via Energielijst |
| Deadline | Apply within 3 months of purchase commitment |

### MIA (Milieu-investeringsaftrek / Environmental Investment Allowance)

**What it is:** Additional tax deduction for investments in environmentally beneficial equipment.

| Parameter | Value |
|---|---|
| Deduction rate | 27% or 36% or 45% depending on equipment category |
| Corporate tax rate | 25.8% |
| Effective CAPEX reduction | 7-11.6% of qualifying investment |
| Qualifying equipment | Heat recovery for third-party use, sustainable building materials, water recycling |
| Application | RVO via Milieulijst |

### VAMIL (Willekeurige Afschrijving Milieu-investeringen / Arbitrary Depreciation of Environmental Investments)

**What it is:** Accelerated depreciation for qualifying environmental investments — depreciate 75% in year 1 instead of normal linear depreciation.

| Parameter | Value |
|---|---|
| Accelerated depreciation | Up to 75% in year 1 |
| Tax benefit | Time value of money (deferral, not permanent benefit) |
| Qualifying equipment | Same as MIA list |
| Combined with MIA | Yes — MIA + VAMIL stack |

### Combined Fiscal Impact (DEC Heat Infrastructure)

**Example: €8M heat infrastructure (heat pump + buffer + thermal bridge + backup)**

| Incentive | Calculation | Benefit |
|---|---|---|
| EIA (45.5% × 25.8%) | €8M × 11.7% | €936K |
| MIA (36% × 25.8%) | €8M × 9.3% | €744K |
| VAMIL (accelerated depreciation) | NPV of acceleration on €6M (75% in Y1) | ~€200-400K |
| **Total fiscal benefit** | | **€1.9-2.1M** |
| **Effective CAPEX reduction** | | **24-26%** |

**Impact on IRR:** Fiscal incentives improve project IRR by 1-2 percentage points. This is material — can move a borderline project to investable.

### Innovatiebox (Innovation Box)

If DEC develops proprietary heat integration technology or software:
- Qualifying profit taxed at 9% instead of 25.8%
- Requires S&O-verklaring (R&D statement) from RVO
- Potentially applicable to DEC's integrated control systems or thermal optimization software

## 7. Unit Economics

### Key Unit Metrics

| Metric | Formula | DEC Range | Market Benchmark |
|---|---|---|---|
| **Revenue per MW IT** | Total revenue / contracted MW | €0.8-1.6M/MW/year | Standard colo: €0.8-1.2M/MW/year |
| **Cost per MW IT** | Total OPEX / contracted MW | €0.4-0.8M/MW/year | Standard colo: €0.3-0.6M/MW/year |
| **Margin per MW IT** | Revenue - cost per MW | €0.4-0.8M/MW/year | Standard colo: €0.3-0.6M/MW/year |
| **CAPEX per MW IT** | Total Phase 1 CAPEX / IT capacity | €1.4-2.6M/MW | Standard colo: €1.0-1.5M/MW |
| **Heat revenue per MW thermal** | Heat revenue / thermal recovery capacity | €50-200K/MWth/year | Novel — no standard benchmark |
| **BESS revenue per MWh** | BESS revenue / BESS capacity | €100-205/kWh/year | Market: €80-180/kWh/year |

### Sensitivity Analysis

**Key sensitivities (impact on project IRR):**

| Variable | Base Case | Downside (-20%) | Upside (+20%) | IRR Impact |
|---|---|---|---|---|
| Colocation price (€/kW/month) | €110 | €88 | €132 | ±3-4% IRR |
| Occupancy rate | 85% | 68% | 95% | ±2-3% IRR |
| Electricity price (€/MWh) | €70 | €56 | €84 | ±1-2% IRR |
| BESS revenue (€/kWh/yr) | €150 | €120 | €180 | ±0.5-1% IRR |
| Heat revenue (€M/yr) | €3.5 | €2.8 | €4.2 | ±0.3-0.5% IRR |
| Construction cost overrun | 0% | +20% | -10% | ±1-2% IRR |
| Grid connection delay (years) | 0 | +1 year | -6 months | ±1-3% IRR |

**Key insight:** Colocation pricing and occupancy dominate the economics. Heat and energy revenue improve the base case but don't save a project with poor colocation fundamentals. This reinforces the strategy: underwrite on colocation economics, present heat/energy as differentiation and upside.

### Breakeven Analysis

| Scenario | Breakeven Occupancy | Breakeven Timeline |
|---|---|---|
| Colocation only (no heat, no BESS) | 55-65% | Month 18-24 |
| Colocation + BESS revenue | 50-60% | Month 15-21 |
| Colocation + BESS + heat revenue | 45-55% | Month 12-18 |
| Full stack (colo + BESS + heat + SDE++) | 40-50% | Month 10-15 |

**DEC advantage:** Heat and energy revenue lower breakeven occupancy by 10-15 percentage points — critical for a new entrant that needs time to fill capacity.

## 8. Investor-Facing Financial Story

### Seed Round Financials

**What seed investors need to see:**

| Item | Content | Level of Detail |
|---|---|---|
| Unit economics | €/MW revenue, cost, margin | High — must be credible |
| Market sizing | TAM/SAM/SOM for NL AI colocation | Top-down and bottom-up |
| CAPEX estimate | Phase 1 total with major line items | Indicative (±30%) is acceptable |
| Revenue projection | 5-year P&L at portfolio level | Conservative base case + upside |
| Use of proceeds | How seed money gets to next milestone | Very specific |
| Key risks | Top 5 with mitigation | Honest — investors respect transparency |
| Exit pathway | Strategic sale, IPO, portfolio growth | Plausible, not fantastical |

### Financial Model Best Practices (DEC-specific)

1. **Conservative heat revenue:** Model heat at €0-4/GJ (not the full €8-12/GJ potential) — shows differentiation without depending on it
2. **Conservative BESS revenue:** Use bottom quartile of historical FCR/aFRR prices, not recent peaks
3. **SDE++ as upside:** If SDE++ awarded, show as scenario upside, not base case (subsidy is competitive and not guaranteed)
4. **Grid connection timeline risk:** Model 6-12 month delay as base case; on-time as upside
5. **Occupancy ramp:** 3-year ramp to stabilization is standard; faster is upside
6. **Energy price:** Use forward curve for years 1-3, long-term fundamental forecast for years 4+
7. **Fiscal incentives:** Include EIA/MIA in base case (high certainty) but show sensitivity without them

## Cross-References
- See [site-selection-methodology.md](site-selection-methodology.md) for land cost and development timeline inputs
- See [co-location-master-planning.md](co-location-master-planning.md) for phasing economics and expansion CAPEX
- See [grower-thermal-interface.md](grower-thermal-interface.md) for heat revenue model inputs and pricing
- See companion skill `energy-markets`:
  - [wholesale-energy-trading.md] for electricity cost inputs
  - [balancing-bess-revenue.md] for BESS revenue inputs
  - [energy-risk-settlement.md] for tax (EB/ODE) inputs
  - [carbon-esg-compliance.md] for carbon/ESG value
  - [grid-connection-strategy.md] for connection cost and cable pooling economics
- See companion skill `dc-engineering`:
  - [ai-factory-design.md] for CAPEX benchmarks
  - [heat-recovery-integration.md] for heat infrastructure CAPEX
- See companion skill `ai-infrastructure`:
  - [inference-serving.md] for colocation pricing benchmarks
  - [gpu-accelerator-hardware.md] for IT equipment cost trends
- See companion skill `netherlands-permitting`:
  - SDE++ Expert for subsidy valuation
  - Grid connection for connection cost and timeline risk
