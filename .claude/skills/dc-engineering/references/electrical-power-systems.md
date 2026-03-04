# Electrical Power Systems for AI Data Centers

## 1. The Electrical Challenge of AI Density

### Power Demand at AI Scale
A single NVIDIA GB200 NVL72 rack draws 120-130 kW. A 40 MW IT facility contains 300-400 such racks. The electrical infrastructure must deliver reliable, clean power at densities 5-10x higher than traditional enterprise data centers.

### Power Chain Overview
```
Grid (150/50/20 kV)
    → MV Substation (10-20 kV) with transformers
        → MV Switchgear (SF6 or vacuum circuit breakers)
            → UPS (rotary or static)
                → LV Distribution (400/230V or 415/240V)
                    → PDU / Busway
                        → Rack PDU (per-rack power strip)
                            → PSU (server power supply unit)
                                → GPU / CPU
```

### Netherlands Grid Connection Context
- See companion skill `energy-markets` (Expert 6: Grid Connection & Network Tariff Strategist) for transportschaarste strategy
- See companion skill `netherlands-permitting` (Expert 9: Energie & Flexibiliteit Specialist) for regulatory procedure
- This file covers: facility-side electrical design from point of delivery (aansluitpunt) downstream

## 2. Medium Voltage (MV) Infrastructure

### Voltage Levels in NL
| Level | Typical Voltage | Application |
|---|---|---|
| EHV/HV (Hoogspanning) | 150 kV / 110 kV | TenneT transmission grid, direct connection for >100 MW |
| MV (Middenspanning) | 10 kV or 20 kV | DSO distribution, typical DC connection 10-50 MW |
| LV (Laagspanning) | 400/230V 3-phase | Building distribution, rack power |

### MV Substation Design
For DEC at 40-100 MW IT load (+ 10-15 MW cooling/heat pump):

**Transformer Configuration:**
- **N+1 redundancy** at MV/LV transformer level
- ONAN/ONAF dry-type (droogtype) preferred for indoor installation — no oil spill risk, no bodembescherming (soil protection) requirements for transformer containment
- Oil-filled (oliegevulde) transformers for outdoor installation — higher efficiency, lower cost, but require bunded enclosure (inkuiping) per PGS 15 or Bal bodembescherming
- **Sizing:** 2,500-3,150 kVA per transformer for LV distribution; 10-40 MVA for MV/MV step-down
- **DEC recommendation:** Dry-type for indoor CDU rooms and IT halls; oil-filled for main MV/MV outdoor substation

**MV Switchgear:**
- **SF6-free trend:** European regulators moving toward SF6 ban (EU F-gas Regulation revision). SF6 alternatives: vacuum (Siemens 8DJH), clean air (Schneider SM AirSeT, ABB AirPlus), solid insulation (Eaton Xiria)
- **DEC recommendation:** Specify SF6-free switchgear for new installations — future-proofs against regulatory change, aligns with ESG messaging, marginal cost premium
- **Key vendors (NL):** Siemens (strong NL presence, Zoetermeer), Schneider Electric (Den Bosch), ABB (Rotterdam), Eaton (Amsterdam), Ormazabal (Spanish, growing NL presence — Xiria platform popular with NL DSOs)

### MV Ring Main Unit (RMU)
DSO connection typically via RMU (ringkabelkast) with:
- Incoming/outgoing cable compartments (closed ring for redundancy)
- Transformer compartment with fuse/circuit breaker
- NL DSOs (Liander, Stedin, Enexis) have specific RMU specifications — verify with local netbeheerder (grid operator)

## 3. UPS Topology

### The AI Factory UPS Debate

**Static UPS (Traditioneel):**
- Double-conversion (online) topology: AC→DC→battery→DC→AC
- Battery: lithium-ion (Li-ion) replacing VRLA lead-acid
- Efficiency: 95-97% in double-conversion; 98-99% in eco-mode
- Response time: 0-5 ms transfer
- Key vendors: Vertiv (Liebert), Schneider Electric (Galaxy), Eaton (93PM), ABB (PowerLine DPA), Huawei (UPS5000)
- Strengths: proven, modular, scalable, silent
- Weaknesses: battery replacement every 7-10 years (Li-ion), battery room fire risk (PGS 37 applies if Li-ion), double-conversion losses at scale

**Rotary UPS (DRUPS — Diesel Rotary UPS):**
- Diesel engine + flywheel + alternator integrated unit
- No batteries — flywheel provides 10-15 seconds ride-through during engine start
- Efficiency: 95-97% (no double-conversion loss)
- Response time: <1 second (flywheel instant, engine start 5-10 sec)
- Key vendors: Hitec Power Protection (Almelo, NL — THE market leader), Piller (Germany), Hitzinger (Austria), Euro-Diesel (Belgium)
- Strengths: no battery fire risk, no battery replacement, proven in mission-critical (Shell, ASML, chip fabs), 25+ year equipment life
- Weaknesses: noise and vibration, diesel fuel storage (PGS 28), emissions during test runs, larger footprint, higher initial cost

### DEC Recommendation: Rotary UPS (DRUPS) for Training-Dominant Facilities

**Rationale:**
- AI training tolerates 1-second transfer — checkpoint recovery handles brief interruption
- No Li-ion battery fire risk (PGS 37-1 compliance eliminated for UPS function)
- No battery replacement CAPEX cycle — DRUPS lasts 25+ years with maintenance
- Hitec Power Protection is headquartered in Almelo, NL — supply chain advantage, service proximity
- Diesel fuel storage for DRUPS is smaller than generator fuel storage (already needed)
- NL regulatory: PGS 28 (diesel storage) is simpler than PGS 37 (Li-ion battery) for permitting

**Exception:** If facility includes significant inference serving (latency-critical, SLA-driven), a static UPS with Li-ion may be needed for those halls specifically. Hybrid approach: DRUPS for training halls, static UPS for inference halls.

**Named contrarians:** Microsoft and Meta are deploying DRUPS at scale for AI factories. Google and Amazon still favor static UPS with Li-ion — driven by their existing supply chain and battery-as-grid-asset strategy. Equinix uses mix depending on site.

## 4. Generator Systems

### Backup Generation
Even with DRUPS (which includes integrated diesel engine), separate backup generators may be needed for:
- Cooling systems (CDU pumps, dry cooler fans) — must run during grid outage to protect GPUs
- Heat pump systems — can be load-shed during grid outage (greenhouse switches to backup boiler)
- BMS, fire safety, security, lighting

### Generator Sizing
| Facility Load | Generator Configuration | Fuel Storage (24 hr runtime) |
|---|---|---|
| 10 MW IT | 4x 3.3 MVA gensets (N+1) | ~25,000 liters diesel |
| 40 MW IT | 8-10x 5 MVA gensets (N+1) | ~100,000 liters diesel |
| 100 MW IT | 16-20x 6.25 MVA gensets (N+1) | ~250,000 liters diesel |

### NL-Specific Generator Requirements
- **Activiteitenbesluit / Bal:** Noodstroomaggregaten (emergency generators) permitted up to 500 hours/year test running under Bal
- **Stikstof:** Generator test runs produce NOx → AERIUS calculation required if near Natura 2000
- **PGS 28 (Opslag van Vloeibare Brandstoffen):** Diesel storage >150 liters: spill containment, fire resistance, distance to property boundary
- **Geluid (noise):** Generators are major noise source during testing — typically 85-100 dB(A) at 1 m. Testing schedule restricted by Bal geluidhinder limits (especially nacht: 40 dB(A) at nearest woning)
- **Key vendors (NL):** Caterpillar / Pon Power (NL Cat dealer), Cummins, MTU / Rolls-Royce Power Systems, SDMO/Kohler, Volvo Penta. Pon Power has strong NL infrastructure with Rotterdam HQ.

### DEC Generator Strategy
- Phase 1: N+1 diesel generators for IT + cooling critical load only
- Heat pump and greenhouse systems: NOT backed by generator — greenhouse has own backup boiler
- Generator fuel storage sized for 24-48 hours (longer outages not credible on NL grid)
- AERIUS calculation for stikstof includes generator test run emissions — may be marginal but must be calculated

## 5. LV Distribution

### 400V vs 415V
NL standard is 400/230V 3-phase (50 Hz). Some server manufacturers design for 415/240V (US data center practice). Confirm with IT tenant — most modern PSUs are auto-ranging (200-240V) so 400V is fine.

### Busway (Bus Duct / Stroomrail) vs Cable
For AI density distribution from transformer to rack row:

**Busway:**
- Prefabricated bus duct with tap-off boxes at each rack position
- Tap-off boxes provide connection point for individual rack feeds
- Advantages: fast deployment, modular, easy reconfiguration, high density (up to 6,300A per run)
- Disadvantages: higher unit cost, vendor lock-in on tap-off boxes, overhead routing required
- Key vendors: Schneider Electric (Canalis), Siemens (LDA/LDB), Legrand (Zucchini Masterclad), Starline (Track Busway — OPEN tap-off standard), E+I Engineering (Ireland — growing DC market share)

**Cable (Kabeltrace):**
- Traditional cable tray with individual power cables per rack/row
- Advantages: lower unit cost, flexible routing, any electrician can install
- Disadvantages: slower deployment, cable tray congestion at AI density, difficult to reconfigure
- At 120 kW/rack: need 4-8x 63A feeds per rack → cable tray becomes massive

**DEC Recommendation: Busway for AI Density Halls**
- At 60+ kW/rack, cable volume becomes impractical
- Starline Track Busway offers open-standard tap-offs (avoids vendor lock-in)
- Schneider Canalis widely available in NL with local support
- Overhead busway routing coordinates well with overhead CDU piping (both above rack row)
- See Expert 9 (Data Hall Architect) for ceiling height requirements: minimum 4.5 m clear to underside of structure for busway + CDU piping + cable tray stacking

### Power Distribution Unit (PDU) / Rack PDU
- See Expert 8 (Rack Power & Metering) for detailed rack-level power distribution
- For multi-tenant colocation: revenue-grade metering at PDU level for tenant billing
- Key vendors: Vertiv (Geist), Raritan (Legrand), Server Technology (Legrand), Schneider Electric (APC)
- NL-specific: energy billing per Meetcode Elektriciteit requirements if direct supply to tenant

## 6. Power Quality

### Harmonics
GPU power supplies are switched-mode (SMPS) and generate significant harmonic currents:
- **5th and 7th harmonics** dominant (THDi 25-35% for typical server PSU)
- At AI density with hundreds of identical non-linear loads, harmonic currents aggregate
- **Neutral conductor loading:** 3rd harmonic (triplen) currents add in neutral — neutral must be sized ≥ phase conductor (not reduced as in traditional installations)
- **Transformer K-factor:** Specify K-13 or K-20 transformers for AI density halls — standard transformers (K-1) will overheat

### Power Factor
- Modern server PSUs with active PFC: power factor 0.95-0.99
- GPU training loads: highly consistent power factor (less variation than enterprise mixed loads)
- NL DSOs (netbeheerders) require power factor >0.85 to avoid reactive power surcharge (blindstroomvergoeding)
- Active harmonic filters (AHF) recommended if THDi >8% at point of common coupling (PCC)

### Grounding (Aarding)
**TN-S System (NL Standard):**
- Separate neutral (N) and protective earth (PE) conductors throughout
- Single point of connection between N and PE at main distribution board
- CRITICAL for liquid-cooled facilities: CDU piping creates parallel earth paths if not properly bonded

**Equipotential Bonding for Liquid Cooling:**
- All metallic CDU piping must be bonded to the equipotential bonding system
- Rack-to-CDU quick-disconnect couplings create potential bond breaks — verify bonding continuity
- Stray current through coolant piping can cause galvanic corrosion at dissimilar metal joints
- Bonding standard: NEN 1010 (Low Voltage Installations), NEN-EN-IEC 60364 series

### Lightning Protection (Bliksembeveiliging)
- NEN-EN-IEC 62305 (Lightning Protection) applies
- AI facility with high-value equipment: LPL I or LPL II (Lightning Protection Level)
- External LPS (Lightning Protection System): air termination, down conductors, earth termination
- Internal LPS: SPD (Surge Protective Device / overspanningsbeveiliging) at each distribution level
- DEC consideration: greenhouse glass structures have different lightning exposure than steel DC buildings — coordinate LPS design across co-located facilities

## 7. Energy Metering & Monitoring

### Revenue-Grade Metering (Multi-Tenant Colocation)
For DEC's multi-tenant model, accurate energy metering is essential for billing:

| Metering Point | Accuracy Class | Standard | Purpose |
|---|---|---|---|
| Grid connection (main meter) | 0.2S or 0.5S | IEC 62053-22 | DSO billing, fiscal metering |
| Per-tenant (hall/row) | 0.5S or 1.0 | IEC 62053-21/22 | Tenant energy billing |
| Per-rack (PDU meter) | 1.0 or 2.0 | IEC 62053-21 | Rack-level allocation, PUE tracking |
| Heat pump electricity | 1.0 | IEC 62053-21 | Heat cost allocation |
| Common area / infrastructure | 1.0 | IEC 62053-21 | PUE calculation, OPEX allocation |

### PUE Measurement
Power Usage Effectiveness = Total Facility Power / IT Load Power

For DEC, PUE accounting must handle heat recovery:
- **Standard PUE:** Includes heat pump electricity in facility overhead → PUE 1.15-1.25
- **ERE (Energy Reuse Effectiveness):** Credits heat recovered → ERE = PUE - (Energy Reused / IT Load) → ERE 0.85-1.05
- **ERF (Energy Reuse Factor):** ERF = Energy Reused / Total Facility Energy → ERF 0.10-0.40 depending on season

DEC should report ERE alongside PUE to demonstrate the value of waste heat recovery. NEN-EN 50600-99-1 (PUE) and NEN-EN 50600-99-3 (REF/ERF) provide the standard methodology.

## 8. BESS Integration (Electrical Perspective)

### BESS as Behind-the-Meter Asset
If DEC co-locates BESS with DC (see companion skill `energy-markets` for revenue stacking):
- BESS connects at MV level (typically 10-20 kV)
- Separate MV feeder from DC IT load (not series — BESS failure must not affect DC)
- Bidirectional inverter connects BESS to grid
- Control system coordinates: grid import, BESS charge/discharge, DC load, heat pump load

### Electrical Protection Coordination
- BESS adds complexity to protection coordination study
- Short-circuit contribution from BESS inverters during fault conditions
- Arc flash hazard analysis must include BESS contribution
- NEN 1010 and IEC 60909 (short-circuit currents) apply

See companion skill `netherlands-permitting` (Expert 6: BESS Expert) for PGS 37 and Bal permitting.

## Cross-References
- See [power-quality-grounding.md](power-quality-grounding.md) for detailed harmonic analysis and grounding design
- See [data-hall-design.md](data-hall-design.md) for busway routing and ceiling height requirements
- See [ai-factory-design.md](ai-factory-design.md) for redundancy topology and availability class selection
- See [fire-safety-suppression.md](fire-safety-suppression.md) for generator fuel storage fire protection
- See companion skill `energy-markets` for grid connection strategy, BESS revenue, and energy procurement
- See companion skill `netherlands-permitting` for grid connection procedure, BESS permitting, generator stikstof
