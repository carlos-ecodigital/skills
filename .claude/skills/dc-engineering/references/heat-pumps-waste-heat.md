# Industrial Heat Pumps for DC Waste Heat Upgrading

## 1. The Heat Pump's Role in DEC

### Core Function
The heat pump is the bridge between data center waste heat (35-50°C) and usable heat for greenhouses and district heating (55-90°C). Without it, DC waste heat is too cold for most heating applications. The heat pump upgrades low-grade thermal energy to medium/high-grade.

### DEC Thermal Chain Position
```
CDU facility water return (35-45°C)
    → Heat pump evaporator (source side)
        → Compressor (electricity input)
            → Heat pump condenser (output 55-80°C)
                → Buffer tank / warmtenet
                    → Greenhouse or district heating delivery
```

### Sizing for DEC
For a 40 MW IT facility with 80% liquid cooling capture:
- **Source heat available:** ~32 MWth at 35-45°C
- **Heat pump electrical input:** 32 / (COP - 1) = ~10.7 MWe (at COP 4.0)
- **Total heat output:** 32 + 10.7 = ~42.7 MWth at 55-80°C
- **This heat output must match greenhouse demand + warmtenet demand**
- **Summer surplus:** When heat demand < 42.7 MWth, excess rejected via dry coolers

## 2. Technology Selection

### Compression Heat Pumps (Preferred for DEC)

**Working Fluid Options:**

| Refrigerant | Type | Evap Temp Range | Cond Temp Range | COP at 40→70°C | GWP | NL Regulatory Status |
|---|---|---|---|---|---|---|
| R717 (Ammonia) | Natural | -40 to +50°C | +50 to +90°C | 3.8-4.5 | 0 | PGS 13 applies if charge >50 kg |
| R290 (Propane) | Natural | -40 to +45°C | +40 to +80°C | 3.5-4.2 | 3 | ATEX zone classification if charge >5 kg |
| R1234ze(E) | HFO | -30 to +45°C | +40 to +85°C | 3.3-3.8 | 7 | F-gas compliant, no additional NL restriction |
| R744 (CO2 transcritical) | Natural | -50 to +25°C | +60 to +120°C | 2.5-3.5 | 1 | No restriction but lower COP |
| R134a | HFC | -30 to +45°C | +40 to +80°C | 3.5-4.0 | 1430 | Phase-down under F-gas Regulation; avoid |
| R410A | HFC | -30 to +45°C | +40 to +65°C | 3.0-3.5 | 2088 | Phase-down; avoid for new installations |

### Absorption Heat Pumps
Use thermal energy (waste heat or gas) instead of electricity to drive the cycle. Absorption chillers are well-established; absorption heat pumps less so.

**DEC Assessment: NOT RECOMMENDED.** The source temperature from DC (35-45°C) is too low to drive an absorption cycle efficiently. Absorption heat pumps need driving heat at 80-150°C. The COP for absorption at DEC conditions would be <1.5, making compression heat pumps 2-3x more efficient.

### DEC Recommendation: R717 (Ammonia) for Primary System
- **Best COP** at the 40→70°C lift required (3.8-4.5)
- **Zero GWP** — aligns with sustainability narrative
- **Proven technology** for industrial heat pumps at 5-30 MWth scale
- **NL-specific:** PGS 13 (Ammonia Refrigeration) compliance required for charge >50 kg — adds safety measures (gas detection, ventilation, restricted access) but is well-established in NL food/cold storage industry
- **Trained operators available** in NL (cold storage, food processing heritage)
- **Alternative: R290 for smaller installations** (<5 MWth) where ammonia's toxicity and PGS 13 burden is disproportionate

## 3. Key Vendors

### Oilon (Finland)
- ChillHeat series: industrial heat pumps up to 25 MWth per unit
- R717 and R1234ze(E) models
- Source temperatures 30-60°C, output up to 90°C
- Strong track record in Nordic district heating and industrial waste heat
- DEC relevance: Oilon ChillHeat P300 series suitable for 5-15 MWth units

### Johnson Controls / York (USA/Global)
- YORK YVWA water-to-water heat pump
- Large capacity range (up to 20 MWth per unit)
- R1234ze(E) and R134a models
- Established global service network, NL office in Zoeterwoude
- DEC relevance: strong support infrastructure, moderate COP

### GEA (Germany)
- Grasso series: ammonia compressors and heat pumps
- Long Dutch heritage (Grasso is originally a Den Bosch company)
- Extremely reliable industrial equipment
- DEC relevance: if ammonia selected, GEA/Grasso compressors are the default choice in NL

### MAN Energy Solutions (Germany)
- ETES (Electro-Thermal Energy Storage): heat pump + thermal storage integrated system
- Very large scale (50+ MWth)
- CO2 transcritical cycles
- DEC relevance: potentially interesting for Phase 2+ expansion; overkill for Phase 1

### Combitherm (Netherlands)
- Dutch heat pump manufacturer/integrator
- Custom industrial heat pump solutions
- R717 and R290 expertise
- DEC relevance: local manufacturer, custom integration possible, NL regulatory knowledge

### Viessmann (Germany)
- Vitocal Pro: large commercial/industrial heat pumps
- R290 models for moderate capacity
- Strong NL service network through Viessmann Nederland
- DEC relevance: good for smaller supplementary heat pumps, less suitable for primary 10+ MWth units

## 4. COP Optimization

### Factors Affecting COP

| Factor | Impact on COP | Optimization Action |
|---|---|---|
| Source temperature (evaporator) | +1°C source = +2-3% COP | Maximize CDU return temperature (design GPU cooling conservatively warm) |
| Sink temperature (condenser) | -1°C sink = +2-3% COP | Minimize greenhouse delivery temperature (lower-temp heating systems) |
| Part-load operation | +5-15% COP at 50% load vs full load | VSD compressors, multiple units staged |
| Heat exchanger sizing | Oversized = lower approach = better COP | Worth the capital premium for permanent COP improvement |
| Ambient conditions | Source temp varies with IT load and ambient | Design for worst case, operate at average |

### DEC-Specific COP Scenarios

| Scenario | Source Temp | Sink Temp | Lift | Expected COP (R717) |
|---|---|---|---|---|
| Winter peak (high greenhouse demand) | 42°C | 70°C | 28°C | 4.2-4.5 |
| Shoulder season (moderate demand) | 42°C | 55°C | 13°C | 5.5-6.5 |
| Summer (minimal demand, heat rejection) | 42°C | rejected | N/A | Heat pump OFF |
| Warmtenet injection (high temp) | 42°C | 85°C | 43°C | 3.0-3.5 |

### Annual Weighted COP
For DEC in NL with greenhouse primary off-taker:
- **Design COP:** 4.0 (conservative, used for equipment sizing)
- **Annual weighted COP:** 4.5-5.0 (reflects NL climate and demand profile — many hours at favorable conditions)
- **Heat pump electricity cost:** ~€0.15-0.25/kWhe × (1/COP) = €0.03-0.06/kWh_thermal produced

## 5. Thermal Storage Integration

### Buffer Tanks
- **Short-term buffer** (hours): 50-200 m3 hot water tank between heat pump and greenhouse
- Smooths demand fluctuations
- Allows heat pump to run at optimal steady-state COP
- Located between heat pump and greenhouse delivery point

### ATES (Aquifer Thermal Energy Storage)
- **Seasonal storage** (months): store summer surplus heat in aquifer, extract in winter
- NL has extensive ATES deployment experience (office buildings, hospitals)
- Requires Mijnbouwwet / provincial groundwater permit
- Typical efficiency: 60-80% seasonal round-trip
- DEC relevance: addresses the fundamental seasonal mismatch — DC produces heat year-round, greenhouse needs heat mostly in winter
- Capital cost: €1-3M for a 5-10 MWth ATES system
- Permitting timeline: 6-18 months

### ATES vs Oversized Dry Coolers
The DEC seasonal mismatch can be addressed two ways:
1. **Reject summer surplus heat** via dry coolers (simple, no permits, but wastes energy)
2. **Store summer surplus heat** in ATES for winter extraction (complex, permits, but recovers value)

**Economic assessment:** At current electricity prices and greenhouse heat value (~€15-25/GJ), ATES payback is 5-8 years. Worth the investment for Phase 1 if Mijnbouwwet permitting is started early.

## 6. PGS 13: Ammonia Safety (NL-Specific)

### When PGS 13 Applies
- Koelinstallatie (refrigeration installation) using ammonia (R717)
- Charge > 50 kg (virtually any industrial heat pump)
- Classified as milieubelastende activiteit under Bal

### Key Requirements
- **Veiligheidsafstanden (safety distances):** Ammonia room to property boundary and gevoelige gebouwen (sensitive buildings)
- **Gasdetectie (gas detection):** NH3 sensors with alarm at 25 ppm, evacuation at 300 ppm
- **Ventilatie (ventilation):** Mechanical ventilation in ammonia room, emergency extraction
- **Noodafsluiters (emergency shutoffs):** Remote-operated isolation valves
- **Toegangsbeperking (access restriction):** Ammonia room is restricted area
- **Onderhoud (maintenance):** Scheduled inspections per PGS 13 frequency table
- **Registratie (registration):** Installation registered with bevoegd gezag

### DEC Layout Implication
Ammonia heat pump plant room must be:
- Separated from DC and greenhouse by adequate distance
- Not underneath or directly adjacent to occupied spaces
- Equipped with emergency ventilation to safe discharge point
- Accessible for ammonia delivery and emergency services

## 7. Permitting Interactions

### Bal (Milieubelastende Activiteit)
- Koelinstallatie with ammonia: specific Bal rules apply (Ch. 3.2.5)
- Meldingsplicht (notification obligation) for installations below threshold
- Omgevingsvergunning for larger installations (depends on ammonia charge and capacity)

### PGS 13 Integration with Bbl
- Fire compartment requirements for ammonia plant room
- Veiligheidsregio consultation for emergency planning
- Aandachtsgebieden (attention areas) may apply if ammonia charge exceeds threshold

### SDE++ Subsidy Potential
- Warmtebenutting (heat utilization) from industrial processes is an SDE++ category
- DC waste heat upgraded by heat pump may qualify
- Haalbaarheidsstudie (feasibility study) required
- See companion skill `netherlands-permitting` for SDE++ permitting detail

## Cross-References
- See [liquid-cooling-systems.md](liquid-cooling-systems.md) for CDU output temperatures (heat pump source)
- See [heat-rejection-dry-coolers.md](heat-rejection-dry-coolers.md) for surplus heat rejection
- See [heat-recovery-integration.md](heat-recovery-integration.md) for downstream thermal integration
- See companion skill `netherlands-permitting` for PGS 13, Bal, and SDE++ permitting
- See companion skill `energy-markets` for heat pump electricity procurement and cost optimization
- See companion skill `site-development` for grower thermal interface specification
