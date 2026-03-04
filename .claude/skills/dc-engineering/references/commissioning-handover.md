# Commissioning & Handover for AI Data Centers with Heat Recovery

## 1. Why Commissioning Fails

### The Pattern
Every experienced commissioning agent (Inbedrijfstellingscoördinator) has seen the same failure pattern:
1. Design team specifies systems independently (electrical, mechanical, cooling, fire)
2. Contractor installs each system per specification
3. Each system passes individual testing (FAT, SAT)
4. Systems are connected and turned on together for the first time
5. **Nothing works as designed** — interactions between systems create cascading failures that no individual specification anticipated

For DEC, this pattern is amplified because the system boundary extends BEYOND the DC building to include heat pumps, buffer tanks, piping, and the greenhouse heating system. Traditional DC commissioning stops at the facility boundary. DEC commissioning must verify an integrated thermal chain spanning two buildings and two operators (DC operator + grower).

### The Cost of Inadequate Commissioning
- Delayed COD (Commercial Operation Date): €50,000-€200,000 per week in lost revenue for a 10 MW colocation facility
- Equipment damage from untested failure modes: €100,000-€1,000,000+
- Warranty disputes: if commissioning doesn't document baseline performance, warranty claims are unenforceable
- Insurance: FM Global and other DC insurers require documented commissioning for policy validity

## 2. Commissioning Framework

### ASHRAE Guideline 0 / 1.1

**Guideline 0: The Commissioning Process**
- Defines commissioning (Cx) as quality-focused process from pre-design through operation
- Owner's Project Requirements (OPR) → Basis of Design (BOD) → Cx Plan → execution → handover
- Applies to ALL building systems, not just HVAC

**Guideline 1.1: HVAC&R Technical Requirements for the Commissioning Process**
- Specific technical requirements for HVAC, refrigeration, and controls Cx
- Test procedures, acceptance criteria, documentation requirements
- Particularly relevant for DEC's cooling and heat recovery systems

### Cx Phases for DEC

| Phase | Timing | Activities | DEC-Specific |
|---|---|---|---|
| **Phase 0: Pre-Design Cx** | Before design starts | Define OPR, identify Cx team, develop Cx Plan | Define heat recovery performance criteria in OPR |
| **Phase 1: Design Review** | During design | Review design for testability, identify Cx requirements in specifications | Verify heat recovery design supports IST testing |
| **Phase 2: Construction Cx** | During construction | Monitor installation quality, witness hold points, pre-functional testing | Verify pipe routing, insulation, heat pump placement |
| **Phase 3: FAT** | Factory (before delivery) | Factory Acceptance Test at manufacturer's facility | Heat pump FAT, CDU FAT, transformer FAT |
| **Phase 4: SAT** | On-site (after installation) | Site Acceptance Test — individual system startup and verification | Each system individually operational |
| **Phase 5: IST** | After all SATs complete | Integrated Systems Test — multiple systems operating together | **THE critical phase** — cross-system interaction |
| **Phase 6: Handover** | Post-IST | Documentation, training, O&M manual, warranty handover | DC + heat recovery + greenhouse thermal bridge handover |
| **Phase 7: Seasonal Cx** | 6-12 months post-COD | Verify performance across all seasons | Summer heat rejection, winter heat recovery, shoulder transition |

## 3. Factory Acceptance Testing (FAT)

### Critical FATs for DEC Facility

**Heat Pump FAT (at Oilon/GEA/Combitherm factory):**
- Refrigerant charge and leak test (R717 ammonia: zero tolerance for leaks)
- Compressor performance: COP at design point (source temp → delivery temp)
- Control system functional test: variable speed, capacity modulation, safety interlocks
- Ammonia gas detection system integrated test
- Vibration measurement at compressor (baseline for monitoring)
- **Witness:** DEC commissioning agent + DEC mechanical engineer + insurer representative

**CDU FAT (at CoolIT/vendor factory):**
- Hydraulic pressure test (1.5× design pressure)
- Flow rate vs pressure drop curve
- Leak detection system functional test
- Control valve operation and modulation
- Quick-disconnect coupling operation (dry-break verification)
- Heat exchange capacity at design temperatures

**Transformer FAT (at Siemens/Schneider/ABB factory):**
- Routine tests per IEC 60076: ratio, impedance, no-load loss, load loss, insulation resistance
- Type tests if first-of-type: temperature rise, impulse withstand, sound level
- Tap changer operation (if OLTC — On-Load Tap Changer)

**DRUPS FAT (at Hitec/Piller factory):**
- Diesel engine start and load acceptance
- Flywheel energy storage verification
- Transfer time measurement (grid → flywheel → diesel)
- Load bank test at 100% rated load
- Vibration and noise measurement (baseline)

**Switchgear FAT (at manufacturer):**
- Insulation resistance and dielectric test
- Protection relay settings verification
- Interlocking operation
- Arc flash containment (if arc-rated design)

### FAT Documentation
Every FAT produces a signed test record (testrapport) including:
- Test procedure reference
- Equipment serial numbers
- Measurement data with instrument calibration certificates
- Pass/fail assessment against acceptance criteria
- Punch list (restpunten) items with resolution timeline
- Signatures: manufacturer, Cx agent, client representative

## 4. Site Acceptance Testing (SAT)

### Individual System SATs (in sequence)

**SAT Sequence for DEC:**

```
1. Electrical SAT (energize)
   → MV switchgear → transformers → LV distribution → UPS/DRUPS → busway → rack PDU

2. Mechanical SAT (pressurize + flow)
   → CDU piping → CDU startup → facility water loop → dry cooler → heat pump → buffer tank → greenhouse piping

3. Fire & Life Safety SAT
   → VESDA → point detectors → BMC → IG-541 system → sprinkler → emergency lighting → PA system

4. BMS/Controls SAT
   → Sensors → actuators → control loops → alarm routing → SCADA visualization

5. Security SAT
   → Access control → CCTV → perimeter detection → guard tour system
```

### Electrical SAT Details

**NETA (InterNational Electrical Testing Association) Acceptance Testing:**
- Standard: ANSI/NETA ATS (Acceptance Testing Specifications)
- While NETA is a US-based standard, it is widely used in international DC commissioning as THE reference for electrical acceptance testing
- NL equivalent: NEN 3140 (Bedrijfsvoering van Elektrische Installaties — Operation of Electrical Installations) covers operational safety, not commissioning depth
- **DEC recommendation:** Use NETA ATS for commissioning rigor, NEN 3140 for operational compliance

**Key Electrical Tests:**

| Test | Standard | Equipment | Purpose |
|---|---|---|---|
| Insulation resistance | IEEE 43, IEC 60204 | Megger/insulation tester | Verify cable and winding insulation integrity |
| Contact resistance | IEC 62271 | Micro-ohmmeter | Verify bus connections, circuit breaker contacts |
| Power factor / tan delta | IEEE 286 | Doble/Omicron test set | Transformer insulation condition |
| Primary injection | IEC 60255 | Primary injection test set | Protection relay operation with real current |
| Secondary injection | IEC 60255 | Relay test set (Omicron, Doble) | Protection relay settings verification |
| Harmonic analysis | IEEE 519 | Power quality analyzer | Baseline THDv/THDi at PCC |
| Infrared thermography | NETA | IR camera (Flir/Fluke) | Hot spot detection at connections under load |
| Arc flash study verification | IEEE 1584 | Calculated from measurements | Verify incident energy matches study labels |

**Grounding System Test:**
- Fall-of-potential test for earth electrode resistance (target: <1 Ω for DC facility)
- Equipotential bonding continuity: every bonding point measured with micro-ohmmeter
- CDU piping bonding: verify continuity across every joint and quick-disconnect coupling
- See [power-quality-grounding.md](power-quality-grounding.md) for detailed grounding requirements

### Mechanical SAT Details

**CDU and Cooling System:**
- Hydraulic pressure test (already done at FAT, repeated on-site after field piping)
- Leak test: pressurize to 1.5× design, hold for 24 hours, <0.5% pressure drop
- Flow balancing: commissioning valves adjusted to achieve design flow at each CDU/rack branch
- Temperature verification: supply and return at each CDU at design heat load
- Water quality: glycol concentration, pH, conductivity, bacteria count

**Heat Pump System:**
- Ammonia charge and leak test (PGS 13 compliance — gas detection must be operational before first charge)
- Compressor startup: vibration, bearing temperature, oil pressure, suction/discharge pressure
- COP verification at achievable operating point (may not match design point until full DC load available)
- Safety system test: high pressure cutout, low pressure cutout, ammonia gas detection → emergency ventilation → alarm → shutdown sequence
- **Veiligheidsregio notification:** Ammonia first charge requires notification to Veiligheidsregio in many regions

**Heat Recovery Piping:**
- Pressure test: 1.5× design pressure, 24-hour hold
- Flow test: design flow rate achieved with acceptable pressure drop
- Insulation verification: thermal camera inspection of all above-ground piping (no hot spots indicating missing or damaged insulation)
- Expansion joints and loops: visual inspection of movement capability
- Valve operation: every valve (isolation, control, safety) operated and verified
- **Heat meter (GJ-teller):** Calibration verification with known flow and temperature differential. See [heat-recovery-integration.md](heat-recovery-integration.md) for Kamstrup MULTICAL 803 specification

## 5. Integrated Systems Test (IST)

### IST Level Classification

The IST is where commissioning becomes genuinely valuable — and where most projects fail. The industry uses 5 levels of increasing severity:

| IST Level | Test Scope | Simulated Condition | Typical Duration | What It Proves |
|---|---|---|---|---|
| **Level 1** | Individual component operation | Normal operation | 1-2 days | Each component works as installed |
| **Level 2** | System-level operation | Normal operation with load | 3-5 days | Each system (cooling, power, fire) works as a system |
| **Level 3** | Multi-system interaction | Normal operation, all systems together | 5-10 days | Systems work together without conflict |
| **Level 4** | Failure mode testing | Single failure conditions (N+1 event) | 5-10 days | Redundancy works — one component fails, system continues |
| **Level 5** | Cascading failure testing | Multiple failures, worst-case scenarios | 10-20 days | System degrades gracefully under extreme stress |

**DEC Minimum: IST Level 5.** Anything less is theater.

IST Level 5 is the only level that proves the facility can handle real-world failure scenarios. IST Level 3-4 proves that systems work under planned conditions — but real failures are never planned. Level 5 tests what happens when the plan fails.

### IST Level 5 Test Scenarios for DEC

**Scenario 1: Grid Failure (Netstoring)**
- Simulate grid loss (open main breaker)
- DRUPS flywheel engages → diesel engine starts within 10 seconds
- All IT load sustained without interruption or voltage excursion
- CDU pumps transfer to backup power (generator or DRUPS auxiliary)
- Dry cooler fans restart on backup power
- Heat pump: controlled shutdown (greenhouse switches to backup boiler)
- **Duration:** 4 hours continuous diesel operation + grid restoration sequence
- **Acceptance criteria:** Zero IT downtime, CDU temperature within ±2°C of setpoint within 5 minutes

**Scenario 2: Cooling System Failure**
- Simulate single CDU failure (close isolation valve or kill pump)
- Remaining CDUs redistribute load (N+1 design verification)
- GPU temperatures monitored: must remain below throttle threshold (see liquid-cooling-systems.md)
- Dry cooler N+1: simulate single dry cooler failure, verify remaining capacity maintains setpoint
- **Acceptance criteria:** No GPU thermal throttling, CDU return temperature <45°C within 10 minutes

**Scenario 3: Heat Recovery Chain Failure**
- Simulate heat pump trip (emergency stop)
- CDU facility water must bypass heat pump → direct to dry coolers (bypass valve operation)
- DC cooling continues uninterrupted — heat recovery is NOT on the critical cooling path
- Greenhouse receives alarm → activates backup boiler within 15 minutes
- **Critical verification:** DC cooling is NEVER dependent on heat recovery system availability. Heat pump failure = lost heat revenue, NOT lost cooling.
- **Acceptance criteria:** Zero impact on IT cooling, greenhouse notification within 60 seconds

**Scenario 4: Fire Alarm Activation**
- Simulate fire detection in data hall (VESDA alarm)
- BMC (brandmeldcentrale) activates: audible/visual alarm, notification to PAC
- IG-541 pre-discharge alarm → 30-second delay → discharge
- HVAC dampers close (prevent fresh air feeding fire)
- CDU continues operating (liquid cooling does not introduce oxygen — no conflict with gas suppression)
- IT equipment continues operating during and after gas discharge
- **Veiligheidsregio participation:** Invite brandweer for IST fire scenario observation — builds relationship and provides realistic response time data
- **Acceptance criteria:** Gas concentration reaches design hold for 10+ minutes, VESDA alarm <30 seconds from smoke introduction, BMC notification to PAC <60 seconds

**Scenario 5: Multiple Simultaneous Failures**
- Grid failure + CDU failure (worst case: power outage causes CDU pump trip)
- Verify: DRUPS sustains IT load, backup CDU pump starts on backup power, cooling maintained
- Generator failure during grid outage: DRUPS transfers to second generator
- Fire alarm during grid outage: IG-541 discharges, generators continue running
- **Acceptance criteria:** Cascading response, no single-point-of-failure causes IT outage

**Scenario 6: Heat Recovery Seasonal Transition**
- Simulate summer condition: greenhouse heat demand = zero
- All heat rejected via dry coolers at full capacity
- CDU return temperature remains at setpoint (no heat pump to absorb heat)
- Simulate winter condition: maximum greenhouse heat demand
- Heat pump at full capacity, buffer tank drawdown, dry cooler load reduced
- **Acceptance criteria:** Smooth transition between operating modes without manual intervention

### Load Bank Testing

Before tenants install IT equipment, simulate IT heat load with electrical load banks:
- Resistive load banks in each data hall (generate heat equivalent to IT load)
- Ramp from 25% → 50% → 75% → 100% design load over 3-5 day period
- Verify cooling system performance at each load step
- Measure actual PUE at each load step (compare with design PUE)
- **Heat recovery verification:** At 50-100% load, verify heat pump COP, buffer tank temperature, and thermal delivery to greenhouse connection point
- **Load bank vendors:** Aggreko, Crestchic, Simplex

## 6. DEC-Specific: Greenhouse Thermal Bridge Commissioning

### The Integration Test That Nobody Plans

Traditional DC commissioning stops at the building boundary. DEC's thermal bridge extends to the greenhouse. This requires a dedicated Cx protocol:

**Test 1: Thermal Delivery Verification**
- Pump hot water from DC heat system to greenhouse connection point
- Measure: delivery temperature, return temperature, flow rate, thermal power (kW)
- Compare with warmteleveringsovereenkomst (heat supply agreement) specifications
- **Acceptance criteria:** Delivery temperature ≥ contractual minimum (e.g., ≥55°C), thermal power ≥ design capacity

**Test 2: Control Interface**
- Greenhouse heating controller sends demand signal to DC heat management system
- DC system responds: heat pump modulates, buffer tank valve opens, flow increases
- Verify response time: demand signal → temperature at greenhouse manifold
- **Acceptance criteria:** Response within 10-15 minutes for step change in demand

**Test 3: Emergency Isolation**
- Simulate leak in thermal bridge piping (close isolation valve, observe pressure drop)
- Automatic leak detection and isolation (pressure transmitters, flow comparison)
- Greenhouse alarm: backup boiler activates
- DC side: heat pump continues (divert to dry cooler bypass)
- **Acceptance criteria:** Isolation within 60 seconds of detected pressure drop, no contamination of either system

**Test 4: Heat Meter Accuracy**
- Cross-check DC-side heat meter against greenhouse-side heat meter
- Acceptable discrepancy: <2% at design flow (per MID requirements)
- This is the basis for commercial heat billing — meter disagreement = revenue dispute
- **Acceptance criteria:** <2% discrepancy at 50%, 75%, and 100% design flow

### Grower Participation in Commissioning
- Greenhouse operator (tuinder / grower) must witness thermal bridge testing
- Grower's heating system installer verifies compatibility at connection point
- Joint sign-off on thermal interface test record (testprotocol thermische koppeling)
- Documented in warmteleveringsovereenkomst as conditions precedent for heat delivery commencement

## 7. Veiligheidsregio Requirements

### Fire System Commissioning (Brandveiligheidssystemen Inbedrijfstelling)

Before facility can receive gebruiksvergunning / gebruiksmelding:

**Veiligheidsregio Inspections:**
1. **Brandmeldinstallatie (Fire Alarm):** NEN 2535 certified inspection by inspectie-instelling (CCV-certified inspection body: Kiwa, Efectis, LPCB/BRE NL)
2. **Blusinstallatie (Suppression):** NEN-EN 12845 (sprinkler) or NEN-EN 15004 (gaseous suppression) inspection
3. **Brandwerende doorvoeren (Penetration Seals):** Visual inspection + sampling test
4. **Vluchtwegen (Escape Routes):** Emergency lighting, exit signage, door operation, travel distance verification
5. **Brandweertoegang (Fire Brigade Access):** Opstelplaats (positioning area), sleutelkluis (key safe), brandweerpaneel (fire panel), bluswater (fire water supply)

**Documentation Required:**
- Brandveiligheidsinstallatie rapport (fire safety installation report)
- As-built drawings of all fire systems
- Maintenance contracts for all fire systems (brandveiligheidssystemen onderhoudscontracten)
- Ontruimingsplan (evacuation plan) with assembly points
- BHV-organisatie (Bedrijfshulpverlening — In-house Emergency Response) team roster and training records

### PGS 13 Ammonia Commissioning

If DEC uses ammonia heat pumps:
- Ammonia system commissioning per PGS 13 requirements
- Gas detection system calibration verification
- Emergency ventilation operational test (designed airflow rate achieved)
- Emergency shower and eye wash station test
- Communication with Veiligheidsregio: ammonia incident response plan filed
- **Annual drill:** PGS 13 recommends annual ammonia release response exercise

## 8. Handover Documentation

### Minimum Handover Package

| Document | Content | Recipient |
|---|---|---|
| **As-Built Drawings** | All disciplines, reflecting actual installation (not design intent) | Owner/operator |
| **O&M Manuals** | Every piece of equipment: maintenance schedule, spare parts list, troubleshooting | Facility management team |
| **Cx Test Reports** | All FAT, SAT, IST records with data and sign-offs | Owner, insurer |
| **Punch List (Restpuntenlijst)** | Outstanding items with severity, responsibility, deadline | Contractor (for resolution) |
| **Warranty Certificates** | Equipment warranties with start date (typically COD or SAT date) | Owner |
| **Calibration Certificates** | All instruments (temperature, pressure, flow, power meters) | Facility management |
| **BIM Model (as-built)** | Updated BIM model reflecting actual installation | Owner/operator |
| **Fire Safety Dossier** | Brandveiligheidsdossier per Bbl, including all inspection reports | Gemeente/Veiligheidsregio |
| **Geluidrapport** | Post-construction noise measurement report per HMRI | Gemeente/omgevingsdienst |
| **Heat Recovery Cx Report** | Thermal bridge test records, heat meter calibration, grower sign-off | DEC operations + grower |

### Training

Before handover to operations team:
- **Operations training:** 40-80 hours for facility management team (CDU, heat pump, electrical, BMS, fire)
- **Emergency response training:** DRUPS failover, ammonia release, fire response, IT evacuation
- **Grower interface training:** heat system controls, demand management, emergency isolation
- Manufacturer training: specific OEM training for heat pump, CDU, DRUPS, BMS
- **BHV training:** Bedrijfshulpverlening training for designated emergency response team per Arbowet

## 9. Seasonal Commissioning (Post-COD)

### 12-Month Performance Verification

Not all operating conditions can be tested during IST (which typically occurs in one season). Seasonal Cx verifies:

| Season | Verification | Key Metrics |
|---|---|---|
| **Summer** (Jun-Aug) | Maximum cooling load, dry cooler performance, PUE at peak | CDU temperatures, dry cooler approach, water consumption (adiabatic) |
| **Winter** (Dec-Feb) | Maximum heat recovery, free cooling hours, heat pump COP | Greenhouse delivery temperature, COP at design source/sink, buffer utilization |
| **Shoulder** (Mar-May, Sep-Nov) | Transition between modes, partial cooling/heating | Mode switching, BMS stability, energy optimization |
| **All seasons** | Continuous PUE/ERE tracking, energy metering reconciliation | Monthly PUE trend, heat recovered (GJ), energy cost per kWth delivered |

### Performance Guarantee Verification
After 12 months of operation:
- Compare actual PUE with design PUE at equivalent load
- Compare actual COP with design COP at equivalent temperatures
- Compare actual heat delivery (GJ) with warmteleveringsovereenkomst targets
- Reconcile energy meters: grid import vs IT load + cooling + heat pump + losses
- This data feeds into contractor performance guarantee claims and SDE++ subsidy verification (if applicable)

## Cross-References
- See [ai-factory-design.md](ai-factory-design.md) for design redundancy requirements that IST must verify
- See [liquid-cooling-systems.md](liquid-cooling-systems.md) for CDU testing and thermal specifications
- See [heat-pumps-waste-heat.md](heat-pumps-waste-heat.md) for ammonia heat pump FAT/SAT and PGS 13 requirements
- See [heat-recovery-integration.md](heat-recovery-integration.md) for heat meter specifications and thermal delivery criteria
- See [heat-rejection-dry-coolers.md](heat-rejection-dry-coolers.md) for dry cooler performance testing
- See [electrical-power-systems.md](electrical-power-systems.md) for UPS/DRUPS and generator testing
- See [power-quality-grounding.md](power-quality-grounding.md) for electrical acceptance testing and grounding verification
- See [fire-safety-suppression.md](fire-safety-suppression.md) for fire system Cx and Veiligheidsregio requirements
- See [acoustic-engineering.md](acoustic-engineering.md) for post-construction noise measurement
- See companion skill `netherlands-permitting` for gebruiksmelding, brandveiligheidsinspectie, Wkb opleverdossier
- See companion skill `site-development` for COD definition and phase gate criteria
