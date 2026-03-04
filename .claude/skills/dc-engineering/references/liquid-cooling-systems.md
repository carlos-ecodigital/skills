# Liquid Cooling Systems for AI Data Centers

## 1. Why Liquid Cooling is Mandatory for AI

### The Physics
Air cooling hits a practical wall at ~25-30 kW/rack. Beyond that, the airflow velocity required creates:
- Unacceptable noise levels (>85 dB(A) at rack face)
- Hot spots despite containment
- Fan power consuming 30-40% of total rack power
- Physical impossibility of moving enough air through a 42U rack

GPU accelerators (NVIDIA H100/H200/B200/GB200, AMD MI300X/MI325X) dissipate 300-1000W per chip. A single NVIDIA GB200 NVL72 rack contains 72 GPUs + 36 CPUs at 120-130 kW total. Air cooling this is not engineering — it's fantasy.

### Liquid vs Air: Quantified

| Metric | Air-Cooled 15 kW/rack | Liquid-Cooled 100 kW/rack |
|---|---|---|
| Racks per MW IT | 67 | 10 |
| Floor space per MW IT | 400 m2 | 80 m2 |
| Cooling energy (PUE contribution) | 0.3-0.5 | 0.05-0.15 |
| Effective PUE | 1.4-1.6 | 1.05-1.15 |
| Heat recovery temperature | 25-35°C (low grade) | 40-50°C (medium grade) |
| Facility water temperature | 7-12°C chilled | 25-35°C warm |

## 2. Direct-to-Chip (DTC) Cooling

### How It Works
Cold plates mounted directly on GPU/CPU packages. Coolant (typically propylene glycol/water mix or treated water) circulates through cold plates, absorbing heat at source. Heated coolant returns to CDU (Coolant Distribution Unit) where heat is transferred to facility water loop.

### Key Vendors & Systems

**CoolIT Systems (Calgary, Canada)**
- Market leader in DTC for hyperscale and enterprise
- DCLC (Direct Contact Liquid Cooling) platform
- Deployed at Microsoft Azure, Meta, Dell/HPE server lines
- Strengths: production maturity, supply chain, server OEM integration
- Weaknesses: proprietary manifold design, limited heat recovery optimization
- Cold plate thermal resistance: <0.05°C/W

**ZutaCore (Israel)**
- HyperCool: direct-on-chip two-phase evaporative cooling
- Dielectric fluid evaporates on chip surface, condenses in overhead condenser
- Eliminates cold plates and facility water in the rack
- Strengths: highest thermal performance, no water in rack
- Weaknesses: young company, limited production scale, complex fluid handling
- Recently acquired by Vertiv (2024)

**Asetek (Denmark)**
- Pioneer in CPU liquid cooling (consumer/workstation origins)
- Enterprise DLC product line for server cooling
- Strengths: design maturity, European manufacturing
- Weaknesses: smaller scale than CoolIT for hyperscale deployments

**Motivair (USA)**
- ChilledDoor rear-door heat exchanger (RDHX) and CDU systems
- Dynamic cooling solutions for mixed-density environments
- Strengths: flexibility for colocation (different density per rack)
- Weaknesses: RDHX alone insufficient for AI density

### Fluid Chemistry

| Fluid | Composition | Thermal Performance | Corrosion Risk | Cost | DEC Suitability |
|---|---|---|---|---|---|
| Treated water | Demineralized + inhibitors | Excellent | Low with treatment | Low | Good if leak risk managed |
| Propylene glycol 25-30% | PG/water mix | Good (-15% vs water) | Very low | Low | Preferred — freeze protection + low toxicity |
| Propylene glycol 40-50% | PG/water mix | Fair (-25% vs water) | Very low | Low | Only if freeze protection critical |
| Dielectric (mineral oil) | Engineered mineral oil | Fair | None | Moderate | Immersion only |
| Dielectric (synthetic) | Engineered fluorocarbon | Good | None | High | Two-phase immersion |

### DEC Recommendation: Propylene Glycol 25-30%
- Freeze protection for NL outdoor piping (heat rejection loop)
- Food-grade available (relevant for greenhouse proximity — no environmental contamination risk)
- Thermal penalty acceptable at 25% concentration
- Well-understood chemistry, established inhibitor packages
- Compatible with all major CDU manufacturers

## 3. Immersion Cooling

### Single-Phase Immersion
Servers submerged in dielectric fluid (engineered mineral oil or synthetic). Fluid circulates past components, heated fluid pumped to external heat exchanger.

**GRC (Green Revolution Cooling)**
- ElectroSafe dielectric fluid
- ICEraQ and ICEtank systems
- Largest installed base of single-phase immersion
- Strengths: proven technology, good thermal uniformity
- Weaknesses: fluid cost (€15-25/liter), maintenance complexity (must drain tank for hardware changes), supply chain bottleneck

**LiquidCool Solutions**
- LCS chassis: sealed liquid-cooled server chassis
- Strengths: no open tanks, server can be removed conventionally
- Weaknesses: limited production, niche player

### Two-Phase Immersion
Servers submerged in low-boiling-point dielectric. Fluid boils on hot surfaces, vapor rises to condenser, liquid drips back. Extremely efficient heat transfer.

**Current status:** Promising in lab/pilot; not production-ready at scale. Fluid cost (€80-200/liter for fluorocarbon dielectrics), vapor management in open data halls, and supply chain limitations prevent deployment at DEC scale in 2025-2027 timeframe.

### DEC Position on Immersion
**Not for Phase 1.** DTC is the pragmatic choice for 2025-2028 deployments. Immersion may be viable for Phase 2+ (2028+) if fluid costs decrease and two-phase systems mature. Design facility water infrastructure to be immersion-compatible (temperature, flow rate, pipe sizing) even if deploying DTC initially.

## 4. Coolant Distribution Unit (CDU)

### Function
The CDU is the interface between the rack-level cooling loop (server coolant) and the facility-level water loop. It contains:
- Heat exchanger (plate or shell-and-tube)
- Pumps (primary side: server coolant; secondary side: facility water)
- Expansion tank
- Filtration
- Monitoring/control

### CDU Sizing

| Parameter | Typical Range | Notes |
|---|---|---|
| Capacity per CDU | 200-500 kW | Serves 2-6 racks depending on density |
| Server-side flow | 30-80 LPM per rack | Depends on rack power and deltaT |
| Server-side deltaT | 10-15°C | Supply → return temperature difference |
| Facility-side deltaT | 8-12°C | CDU → facility water temperature difference |
| Approach temperature | 2-5°C | CDU HX efficiency — lower = more expensive HX |

### CDU-to-Facility Interface: THE Critical Parameter for Heat Recovery

The temperature at which the CDU delivers heat to the facility water loop determines everything downstream:
- **35°C facility return:** Heat pump needs 35°C lift to reach 70°C for greenhouse → COP ~4.0-4.5
- **40°C facility return:** Heat pump needs 30°C lift → COP ~4.5-5.0
- **45°C facility return:** Heat pump needs 25°C lift → COP ~5.0-5.5 (or direct use at low-temperature greenhouse)

**Every 1°C increase in CDU return temperature improves annual heat pump electricity cost by approximately 2-3%.**

### Placement Options
- **In-row CDU:** CDU sits in the rack row, takes one or two rack positions. Short pipe runs, easy maintenance. Preferred for DTC.
- **End-of-row CDU:** CDU at end of row in dedicated alcove. Slightly longer pipe runs, better for busway routing.
- **CDU room (centralized):** Dedicated room adjacent to data hall. Longer pipe runs, easier maintenance access, more flexible for different rack configurations. Preferred for multi-tenant colocation.

### DEC Recommendation: CDU Room
For multi-tenant colocation with varying rack densities, a dedicated CDU room per data hall provides:
- Isolation of wet infrastructure from IT space (leak containment)
- Flexibility to serve different rack configurations
- Centralized monitoring and maintenance access
- Clean interface for facility water connection to heat recovery system

## 5. Leak Detection & Containment

### The #1 Operational Risk of Liquid Cooling
Liquid near electronics is inherently risky. A leak in a 100 kW/rack environment can cause millions in hardware damage in minutes.

### Detection Hierarchy
1. **Spot sensors:** At every potential leak point (CDU connections, manifold joints, rack quick-disconnects)
2. **Cable sensors:** Continuous rope sensor under pipe runs and in drip trays
3. **Zone sensors:** Floor-level detection in data hall and CDU rooms
4. **CDU monitoring:** Flow rate deviation, pressure drop anomaly, fluid level in expansion tank

### Containment Design
- **Drip trays:** Under all overhead piping (mandatory)
- **CDU room:** Waterproof floor with containment lip, floor drain to holding tank (NOT to sewer)
- **Rack-level:** Quick-disconnect (dry-break) couplings at every rack connection — vendor-specific (CoolIT, Asetek)
- **Automatic isolation:** CDU shuts down and isolates rack loop within seconds of confirmed leak

### NL-Specific: Bodembescherming (Soil Protection)
Under the Bal, any liquid storage or handling with potential for bodemverontreiniging (soil contamination) requires preventive measures. While propylene glycol is low-toxicity, a large spill in a non-contained area could still trigger bodembeschermingsvereisten (soil protection requirements). Design containment to exceed regulatory minimum.

## 6. Heat Recovery Integration Point

### CDU as Heat Source
From the heat recovery perspective, the CDU cluster is the "heat source plant" of the facility:
- Total heat output = IT load (MW) × (1 - residual air fraction)
- For 80% liquid cooling capture: 40 MW IT → 32 MW thermal at 40-45°C
- This 32 MW thermal feeds the heat pump system
- Remaining 8 MW rejected via dry coolers (air-side cooling of residual heat)

### Temperature Optimization for DEC
Design decision: run GPUs slightly warmer (within ASHRAE A1/A2 envelope) to maximize CDU return temperature.

**ASHRAE A1 recommended:** 15-32°C inlet air temperature
**ASHRAE A2 allowable:** 10-35°C inlet air temperature

Higher coolant supply temperature → higher return temperature → better heat pump COP. The optimal operating point balances GPU thermal headroom against heat recovery value.

For NVIDIA GB200 NVL72 (T_junction_max = 83°C for sustained operation):
- Cold plate supply at 32°C → return ~45°C → facility water return ~42°C
- Cold plate supply at 35°C → return ~48°C → facility water return ~45°C
- Cold plate supply at 38°C → return ~51°C → BUT approaching GPU throttle zone

**DEC target: 32-35°C supply, 42-45°C return** — conservative enough for GPU headroom, warm enough for good heat pump COP.

## 7. Vendor Comparison Summary

| Vendor | Technology | Production Scale | Heat Recovery Suitability | NL Support |
|---|---|---|---|---|
| CoolIT | DTC cold plate | High (hyperscale proven) | Good (warm water DTC) | Via Dell/HPE channel |
| ZutaCore/Vertiv | Two-phase evaporative | Medium (growing) | Excellent (high return temp) | Vertiv NL office |
| Asetek | DTC cold plate | Medium | Good | European HQ in Denmark |
| GRC | Single-phase immersion | Medium | Good | Limited NL presence |
| Motivair | RDHX + CDU | Medium | Moderate (lower return temp with RDHX) | USA-based, distributor model |

## Cross-References
- See [ai-factory-design.md](ai-factory-design.md) for facility concept and thermal architecture
- See [heat-rejection-dry-coolers.md](heat-rejection-dry-coolers.md) for residual heat rejection
- See [heat-pumps-waste-heat.md](heat-pumps-waste-heat.md) for heat pump selection at CDU output temperatures
- See [heat-recovery-integration.md](heat-recovery-integration.md) for thermal integration with greenhouse/warmtenet
- See companion skill `ai-infrastructure` for GPU thermal profiles by accelerator generation
