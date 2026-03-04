# PPA Structuring & Green Certificates

## 1. PPA Types for Data Centers

### Physical PPA (Fysieke Stroomafnameovereenkomst)

**Structure:** Direct physical delivery of electricity from renewable generator to data center.

```
Wind/Solar Farm ──[physical electricity]──→ Grid ──→ Data Center
       │                                              │
       └────────[PPA contract: fixed price €/MWh]─────┘
       └────────[GOs bundled with electricity]────────┘
```

**Key characteristics:**
- Electricity is physically nominated (E-programs) from generator to consumer
- GOs are bundled with physical delivery (strongest additionality claim)
- Generator and consumer must be in same bidding zone (NL) or connected market
- Requires BRP coordination (generator BRP and consumer BRP must align nominations)
- Profile risk: generator produces when wind blows/sun shines, not when DC needs power
- Typically 10-15 year tenor

**Profile Risk Management:**
The fundamental challenge of physical PPAs: renewable generation doesn't match DC load.

| Hour | Wind Generation | DC Load | Surplus/Deficit |
|---|---|---|---|
| 2:00 AM (windy) | 100% capacity | 90% load | +10% → sold to market |
| 2:00 PM (sunny, no wind) | 0% | 90% load | -90% → bought from market |
| 6:00 PM (peak, low wind) | 20% | 95% load | -75% → bought from market at peak price |

**Solutions to profile risk:**
1. **Baseload conversion (proxy revenue swap):** Third party converts intermittent PPA into baseload product → DC pays fixed baseload price, third party takes profile risk for a fee
2. **Portfolio approach:** Combine wind (produces more in winter/night) + solar (produces in summer/day) to flatten profile
3. **BESS integration:** Store excess PPA generation, discharge during deficit
4. **Residual market procurement:** Accept profile mismatch, buy/sell residual on EPEX SPOT

### Virtual PPA (Contract for Difference / CfD)

**Structure:** Financial contract — no physical electricity delivery. Generator and consumer settle the difference between PPA strike price and market price.

```
Wind/Solar Farm ──[sells to market at spot price]──→ Market
       │                                                │
       └────[CfD: if spot > strike, generator pays DC]──┘
       └────[CfD: if spot < strike, DC pays generator]──┘

Data Center ──[buys from market at spot price]──→ Utility/BRP
```

**Key characteristics:**
- No physical delivery — purely financial hedge
- Generator and consumer can be in different locations (even different countries)
- Simpler BRP coordination (DC buys normally from utility)
- GOs typically sold separately (weaker additionality claim)
- REMIT reporting may apply (financial instrument)
- Accounting treatment: may qualify as hedge under IFRS 9 (complex)

**Advantages over physical PPA:**
- No profile risk (DC buys baseload from market, CfD provides price hedge)
- No BRP coordination complexity
- Can be with generators in neighboring countries (cross-border CfD)
- Easier to scale (sign multiple small CfDs vs one large physical PPA)

**Disadvantages:**
- Weaker ESG/additionality claim (no bundled GOs)
- Basis risk: if generator is in different market zone, spot prices may diverge
- Accounting complexity (IFRS 9 hedge accounting)
- REMIT compliance burden

### Sleeved PPA

**Structure:** Utility or trading company acts as intermediary — buys from generator via PPA, supplies to DC with profile shaping.

```
Wind/Solar Farm ──[PPA]──→ Utility (sleeving party)
                              │
                              ├──[profile shaping, balancing]
                              │
                              └──[supply contract]──→ Data Center
```

**Key characteristics:**
- Simplest for DC to manage (looks like normal supply contract)
- Utility handles all profile risk, balancing, GO transfer
- Higher cost than direct PPA (utility margin for sleeving service: €2-5/MWh)
- Weaker additionality than direct physical PPA (intermediary complicates chain)
- Common in NL market (Vattenfall, Eneco, Statkraft offer sleeving)

### DEC PPA Recommendation

**For DEC's first 40 MW facility:**
1. **Physical PPA (50% of volume):** Long-term (10-year) with NL onshore wind farm. Bundled GOs for strongest ESG claim. Baseload conversion via partner trading company.
2. **Sleeved PPA (30% of volume):** With major utility (Vattenfall/Eneco) for operational simplicity on remaining green volume.
3. **Spot/short-term (20% of volume):** Managed via BRP for flexibility and imbalance optimization.

## 2. Garanties van Oorsprong (Guarantees of Origin)

### GO Market Structure

**CertiQ:** Dutch issuing body for GOs. Part of AIB (Association of Issuing Bodies) European system.

**GO = proof of 1 MWh renewable generation.** Can be:
- **Bundled:** Sold together with physical electricity (strongest claim)
- **Unbundled:** Sold separately from electricity (certificate trading)

### GO Pricing (NL Market)

| GO Type | Typical Price Range | ESG Value |
|---|---|---|
| Nordic hydro (unbundled) | €0.20-1.00/MWh | Low (no additionality — hydro runs regardless) |
| NL wind (unbundled) | €0.50-2.00/MWh | Medium |
| NL solar (unbundled) | €0.50-2.00/MWh | Medium |
| NL wind (bundled with PPA) | Included in PPA price | High (additional) |
| New-build NL wind/solar | Included in PPA price | Highest (clearly additional) |

### Additionality

**The core question:** Does your GO purchase cause new renewable generation to be built?

**Additionality hierarchy:**
1. **Strongest:** PPA with new-build project (your contract enables the project to reach FID)
2. **Strong:** PPA with existing project that would otherwise sell merchant (your contract provides revenue certainty that extends project life)
3. **Moderate:** Bundled GOs from NL renewable generation
4. **Weak:** Unbundled NL GOs (certificate trading, no direct link to generation)
5. **Weakest:** Unbundled Nordic hydro GOs (purely accounting exercise)

**GHG Protocol Scope 2 Guidance:**
- Market-based method: GOs are valid instruments for Scope 2 claims
- BUT: quality criteria increasingly required (additionality, temporal matching, geographic proximity)
- RE100: requires GOs from same market as consumption (NL production for NL consumption)
- 24/7 Carbon-Free Energy (Google, Microsoft): requires hourly matching — GOs alone insufficient

### 24/7 Clean Energy (Emerging Standard)

**What it means:** Every hour of electricity consumption is matched with clean generation in the same hour and same grid region.

**Why it matters for DEC:**
- Google, Microsoft require 24/7 CFE from colo providers (increasingly)
- Annual GO matching ≠ hourly matching (a DC running 24/7 matched with solar GOs only covers daytime hours)
- DEC's combination of wind + solar + BESS + demand response could achieve high hourly match rate

**How to achieve 24/7 for DEC:**
1. Onshore wind PPA (generates night + winter → covers baseline)
2. Solar PPA (generates day → covers daytime peak)
3. BESS (shifts excess solar to evening hours)
4. Residual: grid electricity during low-wind/low-solar hours (certified renewable if available)
5. Target: 90%+ hourly match (100% is not yet economically feasible in NL)

**Tracking platforms:** EnergyTag (hourly matching standard), FlexiDAO, Google/Microsoft internal tools

## 3. SDE++ Interaction with PPA

### SDE++ Background

SDE++ (Stimulering Duurzame Energieproductie en Klimaattransitie/Stimulation of Sustainable Energy Production and Climate Transition) is the Dutch subsidy for renewable energy and CO2-reducing technologies.

**Relevant for DEC:**
- Heat delivery from DC to greenhouse may qualify for SDE++ under "industriële restwarmte" (industrial waste heat) category
- Heat pump electricity consumption may qualify under "elektrische boiler/warmtepomp" category
- Solar PV on DC/greenhouse roof may qualify (though increasingly competitive → lower subsidy)

### SDE++ and PPA Interaction

**Key issue:** SDE++ subsidy is calculated as: SDE++ payment = basisbedrag (basis amount) - correctiebedrag (correction amount)

The correctiebedrag for heat production is linked to the gas price. If DEC has a PPA for electricity (to run heat pump), this doesn't directly affect the SDE++ calculation — the SDE++ for heat is corrected against gas, not electricity.

**However:** If DEC generates its own renewable electricity (rooftop solar) and uses it for heat pump → the avoided electricity cost is an additional benefit on top of SDE++ for heat delivery.

### PPA Structuring with SDE++ in Mind

**Principle:** Keep PPA and SDE++ streams separate and non-interfering:
1. PPA covers DC electricity consumption (Scope 2 decarbonization)
2. SDE++ covers heat delivery to greenhouse (revenue stream)
3. Electricity for heat pump: can be from PPA or grid — doesn't affect SDE++ calculation
4. GOs from PPA: used for DC Scope 2 reporting, not for SDE++

## 4. PPA Negotiation Framework

### Key Commercial Terms

| Term | Description | DEC Position |
|---|---|---|
| **Strike price** | Fixed €/MWh | Negotiate against forward curve + risk premium |
| **Tenor** | Contract duration | 10-12 years (matches typical DC lease/financing) |
| **Volume** | Annual MWh contracted | 40-60% of expected consumption |
| **Profile** | Flat, baseload, as-produced, shaped | Prefer baseload-shaped (pay premium for shaping) |
| **Settlement** | Physical delivery, financial CfD, sleeved | Depends on PPA type |
| **Floor/cap** | Minimum/maximum settlement price | Consider collar structure for risk sharing |
| **GO treatment** | Bundled, separate, transferred | Bundled preferred (strongest ESG claim) |
| **Curtailment** | Who bears negative price risk | Generator bears (standard); DC bears below €X (negotiate) |
| **Credit support** | Parent guarantee, letter of credit, margin | DEC as startup → may need credit support from investor/lender |
| **Change of law** | Who bears regulatory risk | Shared (specific carve-outs for SDE++, energiebelasting changes) |
| **Termination** | Events and consequences | Mark-to-market settlement on early termination |

### PPA Counterparty Landscape (NL)

| Category | Examples | Strengths | Considerations |
|---|---|---|---|
| Project developers | Vattenfall, RWE, Eneco, BayWa r.e. | Direct access to new projects | May require credit support from DEC |
| Trading companies | Statkraft, Axpo, Shell Energy | Strong shaping/balancing capability | Less additionality (trading, not developing) |
| Platforms | Pexapark, LevelTen, Zeigo | Market access, standardized terms | Transaction fee, less customization |
| Local developers | Groene Energie Michiel Wiggers, Windunie | Community wind, strong local story | Smaller volumes, less sophisticated counterparty |

### PPA Process Timeline

| Phase | Duration | Key Activities |
|---|---|---|
| Strategy & screening | 2-4 weeks | Load profile analysis, volume determination, counterparty long-list |
| RFP/indication round | 4-8 weeks | Indicative pricing from 3-5 counterparties |
| Short-list negotiation | 6-12 weeks | Detailed term sheet, credit assessment |
| Contract execution | 4-8 weeks | Legal review, EFET/ISDA master agreement, side letters |
| **Total** | **4-8 months** | Including board/investor approval |

## Cross-References
- See [wholesale-energy-trading.md](wholesale-energy-trading.md) for PPA as Layer 1 of hedge book, market price references
- See [balancing-bess-revenue.md](balancing-bess-revenue.md) for BESS role in PPA profile management and 24/7 matching
- See [energy-risk-settlement.md](energy-risk-settlement.md) for PPA risk assessment (counterparty credit, volume, price)
- See [carbon-esg-compliance.md](carbon-esg-compliance.md) for GO/additionality assessment, Scope 2 reporting methodology
- See [grid-connection-strategy.md](grid-connection-strategy.md) for cable pooling with co-located solar + PPA
- See companion skill `netherlands-permitting` for SDE++ application process, GO regulatory framework
- See companion skill `site-development` for PPA impact on financial model and investor narrative
