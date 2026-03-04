# Power Quality & Grounding for Liquid-Cooled AI Data Centers

## 1. Why AI Density Changes Power Quality

### The Problem
Traditional data centers have diverse, mixed loads (servers, storage, networking, cooling) that produce partial harmonic cancellation. AI factories have hundreds of identical GPU racks drawing near-identical non-linear current waveforms. This creates:
- **Harmonic reinforcement** instead of cancellation — THDi accumulates rather than averages out
- **Flat-topped voltage waveforms** (voltage distortion from current distortion through source impedance)
- **Neutral conductor overloading** from triplen harmonics
- **Transformer overheating** from harmonic losses (eddy current and stray losses increase with frequency squared)

### Liquid Cooling Adds Complexity
Direct-to-chip (DTC) liquid cooling introduces metallic piping throughout the data hall — CDU manifolds, rack-level quick-disconnects, overhead distribution piping. This creates:
- **Parallel earth paths** through coolant piping (if piping contacts bonded metal)
- **Galvanic corrosion** at dissimilar metal junctions under stray current
- **EMC (Electromagnetic Compatibility) issues** if piping acts as antenna for radiated emissions
- **Touch voltage risk** if piping becomes live due to insulation fault

## 2. Harmonic Analysis

### Harmonic Spectrum of GPU Power Supplies

Modern GPU server PSUs (e.g., 3,000W 80 PLUS Titanium) with active PFC:

| Harmonic Order | Typical Magnitude (% of fundamental) | Notes |
|---|---|---|
| 1st (50 Hz) | 100% | Fundamental |
| 3rd (150 Hz) | 2-5% | Triplen — adds in neutral |
| 5th (250 Hz) | 8-15% | Dominant harmonic |
| 7th (350 Hz) | 5-10% | Second dominant |
| 11th (550 Hz) | 3-6% | Significant |
| 13th (650 Hz) | 2-4% | Significant |
| THDi | 15-25% | Total harmonic distortion (current) |

### Aggregation Effect
With N identical loads:
- **Triplen harmonics (3rd, 9th, 15th):** Add arithmetically in neutral conductor (phase-aligned)
- **Non-triplen odd harmonics (5th, 7th, 11th, 13th):** Partial cancellation due to phase diversity, but less than traditional mixed loads — diversity factor 0.7-0.9 at AI density (vs 0.4-0.6 for traditional DC)

### Voltage Distortion at PCC (Point of Common Coupling / Aansluitpunt)
NEN-EN 50160 (Voltage characteristics of electricity supplied by public networks):
- THDv ≤ 8% at MV (including up to 4th harmonic: ≤6.5%)
- Individual harmonic voltage: limits per harmonic order

If facility THDi causes THDv >8% at PCC, the DSO (netbeheerder) can require mitigation. This is a contractual obligation in the aansluitovereenkomst (connection agreement).

### IEEE 519-2022 Compliance
While NEN-EN 50160 is the Dutch legal standard, IEEE 519 provides more detailed guidance:
- Current distortion limits based on ISC/IL ratio (short-circuit current vs load current)
- At typical DC facility ISC/IL ratio of 20-50: THDi limit 5-8% at PCC
- Individual odd harmonics <4% (for 5th, 7th) at PCC

## 3. Harmonic Mitigation

### Strategy Hierarchy (Preferred Order)

**1. Source-Side Mitigation (Built into Equipment)**
- Multi-pulse transformers: 12-pulse (ΔΔ/ΔY) or 18-pulse UPS input eliminates 5th and 7th harmonics
- Active front-end (AFE) UPS: PWM rectifier maintains THDi <5% regardless of load
- DEC recommendation: specify UPS with AFE input — eliminates downstream harmonic problems at source
- Key vendors with AFE: Vertiv Liebert EXL S1 (AFE standard), Schneider Galaxy VX (AFE option), Eaton 93PM (12-pulse standard, AFE optional)

**2. Passive Harmonic Filters**
- Tuned LC filters at specific harmonic frequencies (5th, 7th, 11th)
- Simple, reliable, maintenance-free
- Disadvantage: fixed tuning, can create resonance with changing system impedance
- Application: supplement to multi-pulse transformers, not primary strategy

**3. Active Harmonic Filters (AHF / Actieve Harmonische Filters)**
- Power electronics inject anti-phase harmonic currents to cancel harmonics
- Adaptive to changing load conditions
- Effective THDi reduction to <5% at PCC
- Key vendors: Schneider Electric (AccuSine), ABB (PQF), Siemens (SVC), Danfoss (VLT AAF)
- Disadvantage: adds complexity, power losses, maintenance of power electronics

**4. K-Rated Transformers**
- Not a mitigation strategy — a tolerance strategy
- K-factor rated transformers handle harmonic heating without derating
- K-13 or K-20 for AI density halls
- All AI facility MV/LV transformers should be K-rated regardless of other mitigation

### DEC Recommendation
1. **UPS with AFE input** (eliminates harmonic injection from UPS — largest single harmonic source)
2. **K-rated transformers** throughout (defensive measure — handles residual harmonics)
3. **Active harmonic filter** at MV/LV transformer secondary if THDi exceeds 8% at PCC (measured post-commissioning)
4. **Ongoing monitoring** via power quality analyzer at PCC (Dranetz, Fluke 1770, Hioki) — continuous, not spot-check

## 4. Neutral Conductor Design

### The Triplen Harmonic Problem
In a 3-phase 4-wire system (TN-S, standard in NL), triplen harmonics (3rd, 9th, 15th...) from all three phases are in-phase and add arithmetically in the neutral conductor.

For AI density with balanced 3-phase GPU loads:
- Phase current: I_phase
- Neutral current from 3rd harmonic: I_neutral = 3 × I_phase × %3rd_harmonic
- If 3rd harmonic = 5% of fundamental: I_neutral ≈ 0.15 × I_phase — manageable
- If 3rd harmonic = 15% of fundamental: I_neutral ≈ 0.45 × I_phase — neutral must be sized accordingly

### Design Rule
**Neutral conductor ≥ 100% of phase conductor cross-section** for all AI density distribution. Do NOT apply the NEN 1010 derating allowance for neutral in balanced 3-phase systems — that rule assumes minimal 3rd harmonic, which does not apply here.

For busway systems: specify full-sized neutral bar. Most busway manufacturers offer this as option (default is reduced neutral).

## 5. Grounding System Design

### TN-S System (NL Standard)
- **Separate N and PE** from main distribution board (MDB) throughout facility
- **Single N-PE bond** at MDB only (no downstream N-PE connections)
- If N and PE are connected at multiple points: circulating earth currents → interference, corrosion
- NEN 1010 Section 411 and NEN-EN-IEC 60364-4-41

### Equipotential Bonding (Potentiaalvereffening)

**Main Equipotential Bonding (Hoofdpotentiaalvereffening):**
- Main earthing terminal connects: PE conductor, water pipe, gas pipe (if present), structural steel, CDU piping main entry, cable tray system
- Located at MDB / main switchboard room

**Supplementary Equipotential Bonding (Bijkomende Potentiaalvereffening):**
- In data halls: bonding ring around perimeter connecting all metallic services
- Each rack bonded to ring via braided copper strap (minimum 16 mm² Cu)
- CDU piping bonded at every joint, manifold, and rack connection point
- Cable tray bonded at every joint and support

### Liquid Cooling-Specific Grounding

**CDU Piping as Parallel Earth Path:**
The metallic CDU piping system (typically stainless steel or copper manifolds) runs parallel to the PE conductor system. If the piping contacts grounded metal at any point, it becomes a parallel earth path.

**Risks:**
- Earth fault current flows through piping instead of PE conductor — violates NEN 1010 earth fault clearance assumptions
- Stray current causes electrochemical corrosion at dissimilar metal joints (e.g., stainless manifold to copper fitting)
- Touch voltage on piping if insulation fault occurs on nearby conductor

**Mitigation:**
1. **Bond all piping** to equipotential bonding system at regular intervals (every 15-20 m and at every branch point)
2. **Dielectric isolation** at CDU-to-facility interface if DC loop and facility loop must be electrically isolated (some CDU designs require this)
3. **Insulated pipe supports** where piping crosses cable tray or structural steel (prevents uncontrolled bonding)
4. **Stray current monitoring** on CDU piping — periodic measurement (annually minimum)
5. **Corrosion inspection** at dissimilar metal joints — ultrasonic thickness measurement

**Quick-Disconnect Couplings:**
- CoolIT, Asetek, and other DTC vendors use proprietary quick-disconnect (dry-break) couplings at each rack
- These couplings may or may not maintain electrical continuity across the joint
- **Verify with vendor** whether coupling maintains bonding — if not, install bonding jumper across each QD coupling
- This is a frequently missed detail in liquid-cooled DC commissioning

### Isolated Grounding (IT Loads)
Some GPU systems (particularly NVIDIA DGX/HGX platforms) specify isolated ground for IT equipment:
- Dedicated insulated ground conductor (IG) from rack to MDB panel
- Separate from building ground / structural steel ground
- Purpose: reduce ground noise for sensitive high-speed signaling
- NEN 1010 allows isolated grounding as supplementary measure (does NOT replace safety PE)

## 6. Lightning Protection (Bliksembeveiliging)

### Risk Assessment per NEN-EN-IEC 62305-2
For AI facility with high-value equipment:
- **Tolerable risk** for loss of economic value: very low → requires LPL I or LPL II
- Building dimensions, local thunderstorm days (keraunisch niveau — NL average: 15-25 days/year), and equipment value drive protection level

### External Lightning Protection System (LPS)
- **Air termination:** Mesh method (20 m × 20 m for LPL I) on roof, or rolling sphere method (R=20 m for LPL I)
- **Down conductors:** Minimum 2, spaced per LPL (every 10 m perimeter for LPL I)
- **Earth termination:** Type B (ring earth) preferred — surrounds entire building, minimum 0.5 m depth, 80% contact with soil
- **Material:** Hot-dip galvanized steel or copper for NL soil conditions (saline groundwater corrosion risk in western NL)

### Surge Protection Devices (SPD / Overspanningsbeveiliging)
Cascaded SPD system:
| Location | SPD Type | Iimp/Imax | Coordination |
|---|---|---|---|
| Main LV switchboard | Type 1 (T1) | 12.5 kA (10/350 µs) | Lightning current diverter |
| Sub-distribution | Type 2 (T2) | 40 kA (8/20 µs) | Surge limiter |
| Rack PDU / IT equipment | Type 3 (T3) | 10 kA (8/20 µs) | Fine protection |

**CDU piping SPD:** If metallic piping enters from outdoor plant, SPD on piping at building entry (bonding to earth at entry point — also satisfies equipotential bonding requirement).

### DEC Co-Location Consideration
DC and greenhouse are separate buildings with different LPS designs:
- DC: steel structure, flat roof → mesh air termination, multiple down conductors
- Greenhouse: glass/aluminum structure, peaked roof → separate LPS (greenhouse often unprotected due to low equipment value, but DC proximity changes risk calculation)
- Shared services (heat pipeline, electrical, fiber): bond at building entry on both ends
- Coordinate LPS design between DC and greenhouse design teams

## 7. Power Monitoring & Analytics

### Continuous Power Quality Monitoring
Install permanent power quality analyzer at PCC (grid connection point):
- **Dranetz HDPQ** or **Fluke 1760** for Class A (IEC 61000-4-30) measurement
- Continuous recording: voltage, current, THDv, THDi, power factor, flicker, unbalance
- Alarm thresholds: THDv >5% (warning), >8% (critical); PF <0.90 (warning)
- Data retention: 12 months minimum for contractual compliance with DSO

### Per-Distribution Monitoring
At each MV/LV transformer and major distribution board:
- Power meter with harmonic analysis: Schneider ION9000, Siemens SENTRON PAC5200
- Revenue-grade accuracy for tenant billing (see [electrical-power-systems.md](electrical-power-systems.md))
- MODBUS/BACnet integration to BMS for centralized monitoring

### Arc Flash Monitoring
- Arc flash detection relay (AFD) at all MV and LV distribution panels
- Detection time: <1 ms optical + <10 ms trip — limits arc energy
- Key vendors: Littelfuse (AF series), ABB (REA arc protection), Schneider (Okken arc-monitored)
- NEN-EN-IEC 61936-1 for arc flash protection in MV installations
- NFPA 70E (US standard) widely used as reference for arc flash risk assessment methodology even in NL

## Cross-References
- See [electrical-power-systems.md](electrical-power-systems.md) for overall power distribution architecture
- See [liquid-cooling-systems.md](liquid-cooling-systems.md) for CDU piping materials and cooling system grounding interface
- See [data-hall-design.md](data-hall-design.md) for cable tray and bonding ring layout
- See [commissioning-handover.md](commissioning-handover.md) for power quality verification during IST
- See companion skill `netherlands-permitting` for NEN 1010 compliance and DSO connection requirements
