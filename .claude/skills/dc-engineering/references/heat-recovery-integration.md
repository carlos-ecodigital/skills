# Heat Recovery & Thermal Integration for DC-Greenhouse Co-Location

## 1. The Thermal Integration Challenge

### DEC's Unique Proposition
DEC's co-location model connects two systems that are rarely designed together:
- **Data center:** Constant heat generator (35-45°C), needs to reject heat 24/7/365
- **Greenhouse:** Variable heat consumer (40-80°C depending on crop), peak demand in winter, minimal in summer

The thermal integration system must bridge:
- **Temperature gap:** 35-45°C (DC output) → 55-80°C (greenhouse input) via heat pump
- **Temporal gap:** DC load is steady; greenhouse demand is seasonal and diurnal
- **Reliability gap:** DC cooling is life-safety (GPU thermal protection); greenhouse heating is production-critical but not life-safety
- **Ownership gap:** DC operator and greenhouse operator are different entities with different incentives

## 2. System Architecture

### Primary Components
```
[DC Data Halls] → [CDU Cluster] → [Facility Water Loop]
                                          ↓
                                   [Plate HX / Free Cooling] ← (for residual air cooling rejection)
                                          ↓
                                   [Heat Pump Evaporator]
                                          ↓
                                   [Heat Pump Compressor] ← (electricity)
                                          ↓
                                   [Heat Pump Condenser]
                                          ↓
                                   [Buffer Tank (short-term)]
                                          ↓
                              ┌─────────────┴─────────────┐
                              ↓                           ↓
                    [Greenhouse Delivery]         [Warmtenet Injection]
                              ↓                           ↓
                    [Greenhouse Return]           [Warmtenet Return]
                              ↓                           ↓
                              └─────────────┬─────────────┘
                                            ↓
                                   [Return to Heat Pump]
```

### Hydraulic Separation
Critical design principle: the DC facility water loop and the greenhouse/warmtenet loop must be hydraulically separated:
- **Plate heat exchanger** between DC loop and heat pump source side
- **Different pressures, different water chemistry, different ownership**
- If DC loop water enters greenhouse system (or vice versa), contamination risk
- Hydraulic separation also provides thermal decoupling — DC can operate independently of heat demand

## 3. Temperature Matching by Crop Type

### Greenhouse Heating Systems

| System | Supply Temperature | Return Temperature | Application |
|---|---|---|---|
| Buisrailverwarming (pipe rail heating) | 40-55°C | 30-40°C | Primary heating for most crops |
| Groeipijp (growing pipe) | 35-45°C | 25-35°C | Low-level crop heating, humidity control |
| Gewasverwarming (crop heating) | 30-40°C | 25-30°C | Direct crop zone heating |
| Luchtverwarming (air heater/unit heater) | 60-80°C | 40-50°C | Rapid heat-up, dehumidification |
| Schermverwarming (screen heating) | 50-70°C | 35-45°C | Above-screen heating, condensation prevention |

### Crop-Specific Temperature Requirements

| Crop | Day Temp (air) | Night Temp (air) | Max Heating Demand | Heat Pump Output Needed |
|---|---|---|---|---|
| Tomaat (tomato) | 19-23°C | 16-18°C | 250-350 W/m2 glass | 55-65°C (buisrail + groeipijp) |
| Paprika (bell pepper) | 20-24°C | 17-19°C | 250-350 W/m2 | 55-65°C |
| Komkommer (cucumber) | 21-25°C | 18-20°C | 300-400 W/m2 | 60-70°C |
| Roos (rose) | 18-22°C | 15-18°C | 200-300 W/m2 | 55-65°C |
| Chrysant (chrysanthemum) | 18-22°C | 16-18°C | 200-300 W/m2 | 55-60°C |
| Tropische planten (tropical) | 24-30°C | 20-24°C | 350-500 W/m2 | 70-80°C (higher temp needed) |

### DEC Design Implication
For most common Dutch greenhouse crops (tomaat, paprika, komkommer), a heat pump output of **55-65°C** is sufficient. This represents a 20-25°C lift from 40°C source — achievable at COP 4.5-5.5 with ammonia or propane heat pumps. Only tropical crops require 70-80°C output with correspondingly lower COP.

## 4. Buffer Tank Sizing

### Purpose
Buffer tanks decouple the DC's constant heat production from the greenhouse's variable demand pattern:
- **Diurnal buffer:** Greenhouse heating ramps up at night and reduces during daytime (solar gain). Buffer absorbs midday surplus, releases at night.
- **Demand response:** Heat pump can shift electrical load to off-peak hours (charging buffer during night tariff), reducing energy cost.

### Sizing Guidelines

| Buffer Duration | Tank Volume (per MWth) | Capital Cost | Use Case |
|---|---|---|---|
| 1 hour | 15-20 m3 | €15-25K | Minimum — smooths short transients |
| 4 hours | 60-80 m3 | €50-80K | Typical — covers diurnal variation |
| 8 hours | 120-160 m3 | €90-140K | Extended — enables demand response |

For DEC at 10 MWth heat pump output: 4-hour buffer = 600-800 m3 tank
- Typically above-ground insulated steel tank
- Location: between DC and greenhouse, near heat pump plant
- Temperature stratification maintained for optimal efficiency

### ATES as Seasonal Buffer
For seasonal storage (summer surplus → winter extraction):
- See [heat-pumps-waste-heat.md](heat-pumps-waste-heat.md) section 5 for ATES details
- ATES provides months of storage; buffer tank provides hours
- Both are typically needed in an optimized DEC system

## 5. Piping & Distribution

### Warmtetransportleiding (Heat Transport Pipeline)

**Above-Ground:**
- Pre-insulated steel or PE pipes (Thermaflex, Logstor, Isoplus)
- Thermal losses: 2-5 W/m depending on pipe diameter and insulation
- Advantages: easy maintenance, visible leak detection
- Disadvantages: landscape impact, frost exposure (mitigated by insulation), physical obstacle

**Below-Ground (Typical for DC-to-Greenhouse):**
- Pre-insulated bonded pipe systems (Logstor CasaFlex, Thermaflex Flexalen)
- Trench installation: 0.8-1.2 m depth, sand bed
- Thermal losses: 3-8 W/m depending on diameter and soil conditions
- Advantages: no landscape impact, protected from weather
- Disadvantages: higher installation cost, leak detection more complex, requires graafvergunning (excavation permit) if crossing public land

### Pipe Sizing

| Heat Transport Capacity | Flow Rate (ΔT=20°C) | Pipe Diameter | Typical Distance |
|---|---|---|---|
| 1 MWth | ~12 l/s | DN 100-150 | Up to 500 m |
| 5 MWth | ~60 l/s | DN 200-250 | Up to 1 km |
| 10 MWth | ~120 l/s | DN 300-350 | Up to 2 km |
| 20 MWth | ~240 l/s | DN 400-450 | Up to 3 km |

### DEC Pipe Run
Typical DC-to-greenhouse distance at co-location site: 100-500 m
- Short distance is a major advantage of co-location vs centralized warmtenet
- Lower pumping energy, lower thermal losses, lower capital cost
- DN 200-300 sufficient for most DEC Phase 1 projects

## 6. Metering & SLA

### Revenue-Grade Heat Metering

**GJ-teller (Heat Meter / Energy Meter):**
- Measures thermal energy delivered (flow × ΔT × time)
- MID-certified (Measuring Instruments Directive) for billing purposes
- NEN-EN 1434 (heat meters) compliant
- Typical accuracy: Class 2 (±3-5%) or Class 1 (±1-2%)

**Key Vendors:**
- **Kamstrup:** MULTICAL 803 — market leader in NL district heating
- **Itron (Actaris):** CF Echo II — established alternative
- **Siemens:** SITRANS F — industrial applications

**Meter Placement:**
- At delivery point (eigendomsgrens / ownership boundary between DC and greenhouse)
- BOTH supply and return temperature measured
- Flow measured on one pipe (typically return — lower temperature, less measurement error)
- Data logging: 15-minute intervals minimum for billing and dispute resolution

### Heat Supply Agreement (Warmteleveringsovereenkomst)

**Key Terms:**
| Parameter | Typical Value | Negotiation Point |
|---|---|---|
| Delivery temperature | ≥55°C (guaranteed minimum) | Higher = more expensive; lower = less greenhouse flexibility |
| Return temperature | ≤35°C (maximum) | Grower must maintain low return for system efficiency |
| Availability | ≥95% annual (measured monthly) | Lower for Phase 1; increase to 98%+ over time |
| Capacity | X MWth contracted | Take-or-pay vs variable; affects heat pump sizing |
| Price | €X/GJ (indexed) | Reference: €10-25/GJ depending on market; must beat gas alternative |
| Measurement | Per GJ-teller at delivery point | Meter ownership, calibration responsibility |
| Backup | Grower provides own backup boiler | DC not responsible for 100% greenhouse heating |
| Force majeure | DC maintenance, unplanned outage | Define what constitutes force majeure |
| Term | 10-15 years minimum | Long-term needed for investment payback |

### Price Benchmarking
| Heat Source | Delivered Cost (€/GJ) | Notes |
|---|---|---|
| Aardgas WKK (natural gas CHP) | €20-35/GJ | Includes gas cost + maintenance + CO2 |
| Aardwarmte (geothermal) | €8-15/GJ | After SDE++ subsidy |
| Restwarmte (industrial waste heat) | €5-15/GJ | Depends on transport distance |
| DC waste heat via heat pump | €10-20/GJ | Depends on electricity price and COP |
| Biomassa (biomass) | €15-25/GJ | Declining due to sustainability concerns |

DEC pricing target: **€12-18/GJ** — competitive with geothermal, cheaper than gas WKK, provides price certainty through indexation.

## 7. Reliability & Redundancy

### Heat Recovery is NOT Life-Safety
Critical design principle: the heat recovery system is production-critical for the greenhouse but NOT life-safety for the data center. The DC thermal system must function independently:

- **If heat pump fails:** DC cooling continues via dry coolers (heat rejected to atmosphere). Greenhouse activates backup boiler.
- **If greenhouse stops accepting heat:** DC cooling continues via dry coolers. No DC operational impact.
- **If DC IT load drops:** Heat available to greenhouse decreases. Greenhouse supplements with backup.

### Redundancy Architecture
| Component | Redundancy | Rationale |
|---|---|---|
| Heat pump | N+1 (e.g., 3+1 units of 5 MWth each) | Maintenance without losing capacity |
| Buffer tank | N+0 | Failure mode is slow (tank leak); manual intervention possible |
| Transport pipeline | N+0 with isolation valves per section | Leak isolation without full shutdown |
| Circulation pumps | N+1 per loop | Standard practice |
| Control system | Redundant controllers | Avoids single point of failure |
| Backup heat source | Grower's gas boiler | Grower must maintain own backup — DC cannot guarantee 100% |

## 8. Control Strategy

### Operating Modes

**Mode 1: Full Heat Recovery (Winter)**
- All DC waste heat captured by heat pump
- Heat pump runs at full capacity
- Buffer tank fully charged
- Greenhouse receives all available heat
- Dry coolers for residual air cooling only

**Mode 2: Partial Heat Recovery (Shoulder Season)**
- Greenhouse demand < available heat
- Heat pump part-loaded (VSD compressor)
- Excess heat rejected via dry coolers
- Buffer tank manages diurnal swing

**Mode 3: Heat Rejection (Summer)**
- Greenhouse demand near zero (solar gain sufficient)
- Heat pump OFF or at minimum (ATES charging if available)
- All DC waste heat rejected via dry coolers and adiabatic systems
- DC cooling PUE at its best (warmest ambient but no heat pump electricity)

### Temperature Setpoint Optimization
The control system must balance:
- GPU thermal headroom (maximum CDU supply temperature)
- Heat pump COP (higher source temperature = better COP)
- Free cooling hours (lower facility water temperature = more free cooling)

Optimal strategy: run CDU supply at 32-35°C when heat recovery is active (maximizing COP); reduce to 25-28°C in summer when heat rejection dominates (maximizing free cooling hours).

## 9. Wcw (Wet Collectieve Warmte) Implications

### From mid-2026
If DEC supplies heat to multiple off-takers (multiple greenhouses, or greenhouse + residential), the warmtekavel (heat concession zone) system under Wcw may apply:
- Gemeente designates warmtekavels
- Warmtebedrijf (heat company) selected per kavel
- >50% public ownership requirement for warmtebedrijf
- DEC as heat SOURCE does not need to be the warmtebedrijf — can supply to public utility

### DEC Structure Options
1. **Direct supply to single grower:** Likely NOT Wcw-regulated (bilateral, not "collectief")
2. **Supply to multiple growers:** May be Wcw-regulated depending on gemeente interpretation
3. **Supply to warmtebedrijf:** DEC sells heat wholesale to municipal heat company; warmtebedrijf delivers to end users

Option 1 is simplest for Phase 1. See companion skill `netherlands-permitting` for Wcw analysis.

## Cross-References
- See [liquid-cooling-systems.md](liquid-cooling-systems.md) for CDU output temperatures
- See [heat-pumps-waste-heat.md](heat-pumps-waste-heat.md) for heat pump technology and COP
- See [heat-rejection-dry-coolers.md](heat-rejection-dry-coolers.md) for surplus heat rejection
- See companion skill `netherlands-permitting` for Wcw warmtekavel and warmtenet permits
- See companion skill `site-development` for grower thermal interface specification and master planning
- See companion skill `energy-markets` for heat pump electricity cost optimization
