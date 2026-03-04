# Grower Thermal Interface

## 1. Dutch Greenhouse Heating Systems

### Overview

Dutch greenhouses (glastuinbouw/greenhouse horticulture) are among the most energy-intensive agricultural operations in the world. Heating accounts for 40-60% of a typical greenhouse's operating cost in the Netherlands.

### Heating System Types

**Buisrailverwarming (Rail-Pipe Heating):**
- Primary heating system in Dutch greenhouses
- Steel pipes (51 mm diameter) run along crop rows at ground level, doubling as rails for trolleys
- Water temperature: 40-90°C depending on heating demand
- Provides base load heating and thermal mass (pipes store heat)
- **DEC relevance:** DC waste heat at 40-55°C can directly supply buisrailverwarming in mild conditions; heat pump needed for peak winter temperatures

**Groeipijp (Growing Pipe):**
- Smaller diameter pipes (28-32 mm) positioned near the crop canopy
- Higher temperature than buisrail during active growth periods
- Water temperature: 35-60°C
- Stimulates plant growth by directing heat at crop level
- **DEC relevance:** Well-matched to DC waste heat temperature range; can often be supplied directly without heat pump

**Gewasverwarming (Crop Heating):**
- Thin tube heating systems placed within or directly around the crop
- Common for vegetables (tomatoes, peppers, cucumbers)
- Water temperature: 30-50°C
- Used for dehumidification and microclimate control
- **DEC relevance:** Excellent match for DC waste heat — low temperature requirement

**Luchtverhitter (Air Heater / Unit Heater):**
- Fan-driven hot air circulation for rapid temperature response
- Water temperature: 60-80°C
- Used for peak heating and rapid temperature recovery
- **DEC relevance:** Requires heat pump uplift from DC waste heat; used only for peak demand

### Temperature Requirements by Crop

| Crop | Min Night Temp | Optimal Day Temp | Heating System Temp | Annual Heat Demand | DEC Direct Supply (40-55°C) |
|---|---|---|---|---|---|
| **Tomaat (tomato)** | 16-18°C | 20-25°C | 40-70°C | 30-40 m3 gas-eq/m2/yr | Partial (base load) |
| **Paprika (bell pepper)** | 17-20°C | 22-26°C | 45-75°C | 35-45 m3 gas-eq/m2/yr | Partial (base load) |
| **Komkommer (cucumber)** | 18-20°C | 22-28°C | 50-80°C | 40-55 m3 gas-eq/m2/yr | Limited (needs HP uplift) |
| **Sierteelt (ornamental plants)** | 12-18°C | 16-22°C | 35-60°C | 20-30 m3 gas-eq/m2/yr | Good (most of base load) |
| **Potplanten (potted plants)** | 14-20°C | 18-24°C | 40-65°C | 25-35 m3 gas-eq/m2/yr | Good |
| **Tropische planten (tropical)** | 20-24°C | 24-32°C | 50-85°C | 45-60 m3 gas-eq/m2/yr | Limited (needs HP uplift) |

**Gas equivalent conversion:** 1 m3 natural gas ≈ 31.65 MJ (bovenwaarde/gross calorific value). A 10 ha tomato greenhouse with 35 m3/m2/yr = 110,495 GJ/yr ≈ 3.5 MWth average.

### Current Greenhouse Heating Sources (Pre-DEC)

| Source | Market Share (NL) | Temperature | CO2 | DEC Displacement |
|---|---|---|---|---|
| **WKK / CHP (gas engine)** | ~60% | 80-90°C supply | CO2 from exhaust used for dosing | Primary target for DEC heat replacement |
| **Gasketel (gas boiler)** | ~25% | 60-90°C | No CO2 production | Easy to displace thermally; no CO2 impact |
| **Geothermie (geothermal)** | ~5-8% | 60-90°C (depends on well) | No CO2 production | DEC complements geothermal (backup, peak) |
| **Restwarmte (waste heat)** | ~3-5% | 40-70°C typically | No CO2 production | DEC IS restwarmte; competes with industrial waste heat |
| **Biomassa (biomass boiler)** | ~2-3% | 70-90°C | Some CO2 from stack (but biogenic) | DEC can displace; biomass has air quality concerns |

## 2. CO2 Dosing: The Hidden Deal-Killer

### Why CO2 Matters

Dutch greenhouses actively dose CO2 to enhance plant growth. Normal atmospheric CO2 is ~420 ppm; optimal greenhouse CO2 is 600-1,200 ppm depending on crop and light conditions.

**CO2 increases yield by 15-30%** — this is not optional for commercial growers. A grower who loses CO2 dosing loses 15-30% of revenue.

### The CO2 Gap Problem

When a grower's WKK (CHP) is replaced by DC waste heat:
- **Before DEC:** WKK runs for heat → produces electricity (sold to grid) + produces CO2 (used for dosing)
- **After DEC:** DC waste heat replaces WKK heat → WKK turns off → no CO2 production → crops suffer

**This is the most common deal-killer for DC-greenhouse heat projects.** If DEC doesn't solve CO2 dosing, the grower's business case worsens despite receiving "free" heat.

### CO2 Dosing Solutions

| Solution | Cost | CO2 Quality | Scalability | DEC Role |
|---|---|---|---|---|
| **OCAP pipeline** | €1-5/m3 greenhouse area/yr (connection + usage) | Pure CO2, reliable | Limited geography (only Rijnmond/Westland region) | Facilitate OCAP connection as part of co-location |
| **Pure CO2 delivery** (Linde, Air Liquide) | €80-150/ton CO2 | Medical/food grade, reliable | Available everywhere, but expensive at scale | Include CO2 cost in heat supply economics |
| **Partial WKK retention** | Lower gas cost (reduced hours) | WKK-quality (cleaned exhaust) | Proven, existing infrastructure | DEC provides base heat; WKK runs only for CO2 + peak |
| **Biomass boiler CO2** | Biomass fuel cost | Variable quality, NOx concerns | Air quality permits needed | Less preferred — regulatory headwind |
| **Direct Air Capture (DAC)** | Currently €400-600/ton | Pure, unlimited | Emerging technology, not yet commercial | Future option; too expensive today |

**DEC recommendation:** The optimal solution depends on geography:
1. **Westland/Rijnmond area:** OCAP pipeline connection — solved, proven, cost-effective
2. **Outside OCAP area:** Partial WKK retention — grower keeps WKK for CO2 dosing during high-light hours, DEC provides base heat → WKK runs fewer hours, grower saves gas, CO2 maintained
3. **New greenhouse (no existing WKK):** Pure CO2 delivery — include cost in heat supply agreement, negotiate bulk supply contract with Linde/Air Liquide

### CO2 Dosing Quantification

| Parameter | Value | Notes |
|---|---|---|
| CO2 dosing requirement per m2 greenhouse | 30-50 kg CO2/m2/year | Varies by crop and light levels |
| 10 ha greenhouse | 300-500 ton CO2/year | |
| WKK CO2 production | ~500 g CO2/kWh(e) × operating hours | Depends on WKK capacity and run hours |
| Pure CO2 cost at 400 ton/yr | €32,000-60,000/year | At €80-150/ton |
| OCAP cost at 400 ton/yr | €10,000-50,000/year | Connection cost + usage, highly variable |

## 3. Heat Delivery Specification

### Technical Specification Template

| Parameter | Specification | DEC Guarantee | Negotiation Range |
|---|---|---|---|
| **Supply temperature** | ___°C at delivery point | Minimum ___°C, nominal ___°C | 40-55°C direct; 60-80°C with heat pump |
| **Return temperature** | ___°C at delivery point | Maximum ___°C | 25-40°C (lower return = more heat extracted) |
| **Thermal capacity** | ___ MWth at design conditions | Guaranteed minimum ___ MWth | Based on greenhouse area and crop type |
| **Annual heat delivery** | ___ GJ/year | Minimum annual quantity: ___GJ | Based on heating demand profile |
| **Availability** | ___% uptime during heating season (Oct-Apr) | ≥95% recommended; ≥99% with backup | Seasonal definition matters |
| **Response time** | Heat available within ___ hours of demand signal | 2-4 hours (buffer tank provides lag) | Buffer sizing drives response time |
| **Backup provision** | ___ MWth backup capacity | [ ] DEC backup boiler [ ] Grower backup [ ] Shared | Critical for grower confidence |
| **Water quality** | Closed loop, treated to ___ specification | No contamination of greenhouse circuit | Typically separate circuits with heat exchanger |
| **Metering** | GJ-teller (heat meter) at delivery point | Calibrated, accessible to both parties | MID Class 2 accuracy minimum |
| **Connection point** | Physical location on site | Defined in master plan | At greenhouse utility entrance |

### Backup and Redundancy

**Grower perspective:** A crop failure from heat loss can cost €50-200/m2 → a 10 ha greenhouse crop loss = €5-20M. No serious grower will accept a single point of failure.

**Redundancy options:**

| Option | Description | Cost | DEC Recommendation |
|---|---|---|---|
| **DEC backup gas boiler** | DEC installs and operates gas boiler at heat plant | €300-600K CAPEX + gas cost when used | Preferred — gives DEC full control of reliability narrative |
| **Grower retains existing boiler** | Grower keeps gas boiler as backup | No DEC CAPEX; grower bears gas cost | Acceptable for conversions (existing greenhouse) |
| **Buffer tank oversizing** | Buffer provides 12-24 hours of heating autonomy | €200-500K additional CAPEX | Supplements but doesn't replace backup heat source |
| **Redundant heat pump** | N+1 heat pump configuration | €500K-1M additional CAPEX | Engineering best practice; protects against single HP failure |
| **District heating connection** | Connect to warmtenet as backup source | Variable; depends on availability | Only if warmtenet exists near site |

**DEC recommended approach:** DEC backup gas boiler + buffer tank (8-12 hours) + N+1 heat pump. Total backup CAPEX: €500K-1.5M. This is the cost of grower confidence.

### Seasonal Mismatch Management

**The fundamental challenge:** DC produces heat year-round; greenhouse needs heat mainly October-April.

| Month | DC Heat Available (MWth) | Greenhouse Demand (MWth) | Surplus/Deficit |
|---|---|---|---|
| January | 25-30 | 20-30 | Balanced to slight surplus |
| February | 25-30 | 18-25 | Slight surplus |
| March | 25-30 | 12-18 | Surplus |
| April | 25-30 | 5-10 | Significant surplus |
| May | 25-30 | 2-5 | Large surplus |
| June | 25-30 | 1-3 | Large surplus → reject |
| July | 25-30 | 1-2 | Large surplus → reject |
| August | 25-30 | 1-3 | Large surplus → reject |
| September | 25-30 | 3-8 | Surplus |
| October | 25-30 | 8-15 | Moderate surplus |
| November | 25-30 | 15-22 | Slight surplus |
| December | 25-30 | 20-28 | Balanced |

**Surplus management strategies:**
1. Reject via dry coolers (simplest, cheapest, energy waste)
2. ATES seasonal storage (expensive but recovers summer heat for winter)
3. District heating export (if warmtenet available)
4. Multiple greenhouse types with staggered demand
5. Additional heat users (other growers, swimming pools, residential)

## 4. Heat Supply Agreement Framework

### Commercial Terms

| Term | Description | DEC Recommended Position |
|---|---|---|
| **Heat price** | €/GJ at delivery point | €5-12/GJ (benchmark: gas equivalent at €8-15/GJ) |
| **Price indexation** | Annual adjustment mechanism | Index to gas price (partial) + CPI (partial) |
| **Minimum take-or-pay** | Grower must consume or pay for minimum GJ/year | 60-70% of estimated annual demand |
| **Maximum supply** | DEC's maximum obligation | 100% of agreed capacity at specified temperatures |
| **Contract duration** | Term and renewal | 15-20 years (matches SDE++ and DC lease) |
| **Availability guarantee** | Uptime commitment during heating season | 95-99% availability Oct-Apr |
| **Penalty for unavailability** | DEC pays if heat not available | Gas cost differential for backup period |
| **Force majeure** | Events excusing non-performance | Standard: natural disaster, grid failure, regulatory change |
| **CO2 responsibility** | Who provides/pays for CO2 dosing | Define explicitly: [ ] Grower [ ] DEC [ ] Shared |
| **Measurement** | Heat metering and dispute resolution | GJ-teller at delivery point; annual calibration; dispute → independent expert |
| **Termination** | Exit provisions | Mutual: 24-month notice; for cause: 6-month cure period |
| **Assignment** | Can agreement be transferred? | With consent (critical if grower sells greenhouse or DEC refinances) |

### Pricing Models

| Model | Structure | DEC Advantage | Grower Advantage | Risk Allocation |
|---|---|---|---|---|
| **Fixed price** | €X/GJ, escalated annually | Predictable revenue | Predictable cost | DEC bears input cost risk |
| **Gas-indexed** | €/GJ = f(TTF gas price) | Revenue tracks DEC's energy cost | Familiar to growers, tracks alternative | Shared; both benefit/suffer with gas |
| **Discount to gas** | Gas equivalent price × (1 - discount%) | Competitive pricing | Always cheaper than gas alternative | DEC bears cost risk; grower gets guaranteed savings |
| **Free heat + infrastructure fee** | €0/GJ + fixed monthly infrastructure charge | Simple narrative ("free heat") | Zero marginal cost for heat | DEC bears volume risk |
| **SDE++ pass-through** | Heat price linked to SDE++ subsidy received | Subsidy upside shared | Below-market heat price | Both share regulatory/subsidy risk |

**DEC positioning:** "Free heat" narrative is strongest for grower acquisition and media story. Implement as: heat at €0/GJ (or very low: €2-4/GJ) + infrastructure contribution from grower (one-time connection fee or annual service charge covering pipe maintenance, heat pump O&M, metering).

### SDE++ Integration with Heat Supply

**SDE++ for waste heat (industriele restwarmte/industrial waste heat):**
- Basisbedrag (basis amount): €8-12/GJ (set at SDE++ application)
- Correctiebedrag (correction amount): based on gas price → variable subsidy
- Net SDE++ payment: basisbedrag - correctiebedrag = subsidy per GJ
- Duration: 15 years from first production

**Key interaction:** SDE++ subsidy goes to the heat producer (DEC, or heat supply SPV), not the grower. The heat price to the grower should reflect the SDE++ benefit but the subsidy is DEC's revenue.

**SDE++ and heat supply agreement alignment:**
- SDE++ application requires a haalbaarheidsstudie (feasibility study) including identified heat user
- Heat supply agreement (or LOI) strengthens SDE++ application
- SDE++ realisatietermijn (realization deadline): heat delivery must start within specified period
- Bankgarantie (bank guarantee) required for SDE++: €10-25 per GJ/year committed

## 5. Grower Engagement Process

### Engagement Sequence

| Phase | Duration | Activities | Deliverable |
|---|---|---|---|
| **1. Identification** | 2-4 weeks | Identify growers within thermal delivery distance of site; assess crop type, greenhouse age, current heating system, expansion plans | Target grower list with thermal profiles |
| **2. Introduction** | 2-4 weeks | Initial meeting: present DEC concept, heat supply proposition, "free heat" narrative; assess grower interest and concerns | Grower interest indication (warm/cold) |
| **3. Technical assessment** | 4-8 weeks | Assess grower's heating system, temperature requirements, CO2 situation, annual consumption, seasonal profile; identify retrofit needs | Technical feasibility report |
| **4. Commercial framework** | 4-8 weeks | Negotiate heat supply terms: price, volume, availability, CO2, backup, contract duration | Heads of Terms / LOI signed |
| **5. Detailed design** | 8-16 weeks | Engineering of thermal bridge, heat exchanger, connection to greenhouse heating system | Design specification, cost estimate |
| **6. Contract execution** | 4-8 weeks | Final heat supply agreement, SDE++ application support, construction coordination | Signed agreement |

### Common Grower Concerns and Responses

| Concern | Grower Thinking | DEC Response |
|---|---|---|
| **"What if your DC shuts down?"** | Crop loss risk, livelihood at stake | Backup boiler + buffer tank + contractual penalty for unavailability |
| **"The temperature is too low"** | Buisrailverwarming needs 70-90°C in winter | Heat pump uplift to required temperature; direct supply sufficient for 60-70% of hours |
| **"What about my CO2?"** | WKK displacement means no CO2 for dosing | OCAP connection / pure CO2 / partial WKK retention — explicitly addressed in agreement |
| **"I'm locked into a long contract"** | Fear of dependency on unknown technology provider | Flexibility: 24-month exit notice; grower retains backup boiler capability |
| **"My neighbors will object to a data center"** | Social pressure, visual impact concerns | Landscape integration, economic benefits (jobs, grower competitiveness), community engagement |
| **"What happens when I sell my greenhouse?"** | Business succession, transferability | Agreement assignable with consent; attractive to buyer (subsidized heat) |
| **"The heat price will go up"** | Cost escalation fear | Fixed or gas-indexed pricing with caps; SDE++ provides long-term price stability |

### Grower Segments for DEC

| Segment | Characteristics | DEC Attractiveness | Engagement Priority |
|---|---|---|---|
| **Large grower (>10 ha), gas-WKK** | High heat demand, existing CO2 from WKK, sophisticated operator | Highest: large volume, clear savings, complex but viable | Priority 1 |
| **Large grower, gas boiler only** | High heat demand, no WKK CO2 dependency, simpler conversion | High: easier conversion, no CO2 gap | Priority 1 |
| **Medium grower (3-10 ha)** | Moderate demand, may have WKK or boiler | Medium: volume may require aggregating multiple growers | Priority 2 |
| **New greenhouse developer** | Building new greenhouse, flexible on heating system | Very high: design-in from scratch, no retrofit | Priority 1 (if timing aligns) |
| **Grower cooperative** | Multiple growers sharing infrastructure | High: single negotiation covers large volume | Priority 2 |

## Cross-References
- See [site-selection-methodology.md](site-selection-methodology.md) for greenhouse land availability as site criterion
- See [co-location-master-planning.md](co-location-master-planning.md) for thermal bridge design and buffer tank placement
- See [project-finance-economics.md](project-finance-economics.md) for heat revenue in financial model
- See companion skill `dc-engineering`:
  - [heat-recovery-integration.md] for thermal cascade from DC CDU to heat pump to greenhouse
  - [heat-pumps-waste-heat.md] for heat pump sizing and COP at required temperature
  - [commissioning-handover.md] for DC-greenhouse integrated commissioning
- See companion skill `energy-markets`:
  - [balancing-bess-revenue.md] for heat market valuation
  - [carbon-esg-compliance.md] for heat recovery as avoided emissions
- See companion skill `netherlands-permitting`:
  - Glastuinbouw Expert for greenhouse-specific permitting
  - SDE++ Expert for subsidy application process
  - Warmte Expert for Wcw/Warmtewet heat supply regulation
