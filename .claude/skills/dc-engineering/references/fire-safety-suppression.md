# Fire Safety & Suppression for AI Data Centers in the Netherlands

## 1. Fire Risk in AI Data Centers

### The Realistic Threat Hierarchy
Fire safety engineers who have spent 25+ years in mission-critical facilities know that the actual fire threat hierarchy is:

1. **Cable fires (#1 realistic threat):** Overloaded or damaged power cables in cable trays. At AI density (120 kW/rack), cable loading is extreme. A single cable fault can ignite adjacent cables via flame propagation. Cable fires produce toxic smoke (HCl from PVC, HCN from polyamide) that damages electronics across entire halls long before flames reach equipment.

2. **Electrical equipment faults (#2):** Transformer, UPS/DRUPS, switchgear, PDU failures. Arc flash at MV level produces plasma temperatures >10,000°C. At LV level, loose connections in busway tap-offs under high AI loads create hot spots.

3. **Li-ion battery thermal runaway (#3 if Li-ion UPS or BESS present):** Self-propagating thermal runaway with toxic gas (HF) and potential explosion. PGS 37-1 addresses this specifically. If DEC uses DRUPS instead of static Li-ion UPS, this risk is eliminated for the UPS function (but may remain if on-site BESS exists).

4. **Construction-phase fires (#4):** Hot works (welding, cutting) during construction or modification. Most DC fires historically occur during construction, not operation.

5. **Liquid cooling leaks + electrical (#5 for DTC facilities):** Coolant (propylene glycol solution) leak onto live electrical equipment. Propylene glycol is combustible (flash point ~107°C for pure PG, higher when diluted) but not readily ignitable. Risk is indirect: coolant leak → short circuit → arc → fire.

**What is NOT a realistic primary threat:** Server spontaneous combustion, GPU catching fire, deliberate sabotage. These make headlines but are not what kills facilities.

## 2. Dutch Regulatory Framework

### Bbl (Besluit bouwwerken leefomgeving — Building Works Decree)

**Brandveiligheid (Fire Safety) Requirements:**
- **Gebruiksfunctie (Occupancy Function):** Data center = industriefunctie (industrial function) per Bbl Chapter 6
- **Brandcompartiment (Fire Compartment):** Maximum 2,500 m² for industriefunctie, maximum 1,000 m² if brandgevaarlijke stoffen (hazardous substances) present
- **WBDBO (Weerstand tegen Branddoorslag en Brandoverslag — Resistance to Fire Penetration and Fire Spread):** 60 minutes standard for compartment boundaries; 120 minutes if >2,500 m² with gelijkwaardigheid
- **Vluchtwegen (Escape Routes):** Maximum 30 m travel distance to exit in industriefunctie. Multiple exits required if >150 m² compartment with >1 person
- **Brandwerendheid (Fire Resistance):** Load-bearing structure (hoofddraagconstructie): 60-120 minutes depending on building height and compartment size. Compartment walls/floors: equal to WBDBO requirement

### Gelijkwaardigheid (Equivalence) for >2,500 m² Data Halls

Most AI data halls exceed 2,500 m². The standard Bbl compartment limit would force fire walls through data halls — impractical for cable tray continuity, busway routing, and cooling distribution.

**Gelijkwaardigheidsbeginsel (Equivalence Principle — Bbl Art. 2.4):**
The applicant may propose alternative measures that provide equivalent safety to the standard requirement. For DC fire compartments >2,500 m²:

**Typical Equivalence Package:**
1. Very early warning smoke detection (VESDA or equivalent) — detection time <30 seconds
2. Gaseous suppression system (IG-541 or clean agent) — suppression within 60 seconds of detection
3. Enhanced cable fire resistance (Euroclass Cca or B2ca rated cables)
4. Reduced fire load (no combustible storage, no raised floor with concealed combustible cable mass)
5. 24/7 fire alarm monitoring by gecertificeerde brandmeldcentrale (certified fire alarm panel) connected to brandweer (fire brigade)
6. Fire brigade access and intervention plan (inzetplan brandweer) agreed with Veiligheidsregio

**Process:**
- Submit as part of omgevingsvergunning bouwtechnische activiteit
- Bevoegd gezag (gemeente/omgevingsdienst) consults Veiligheidsregio (fire service region) for advice
- Veiligheidsregio fire prevention department (Afdeling Risicobeheersing) reviews and advises
- Approval is case-by-case — no guaranteed outcome
- **DEC recommendation:** Engage Veiligheidsregio early (pre-application consultation / vooroverleg) to build relationship and understand local expectations. Each Veiligheidsregio has different attitudes toward DC gelijkwaardigheid

### PGS 37-1 / PGS 37-2 (Lithium-Ion Battery Safety)

If DEC has on-site BESS or Li-ion UPS batteries:

**PGS 37-1:** BESS (Battery Energy Storage System) outdoor containers
- Safety distances (veiligheidsafstanden) based on energy capacity
- Explosion protection (explosiebeveiliging)
- Gas detection (thermal runaway off-gassing: HF, CO, H2)
- Fire suppression (water-based — gas suppression ineffective against thermal runaway)
- No standard suppressant stops Li-ion thermal runaway — cooling with water is only proven method
- Ventilation requirements for container

**PGS 37-2:** Li-ion batteries inside buildings (UPS batteries in UPS room)
- Maximum energy per fire compartment
- Ventilation rate calculation for off-gas dilution
- Detection: gas detection (CO, H2) + smoke detection + temperature monitoring
- Suppression: water mist or sprinkler (not gas — gas does not address thermal runaway)
- Fire resistance of UPS room: 60 minutes minimum

**DEC DRUPS Strategy Advantage:** If DRUPS eliminates Li-ion UPS batteries, PGS 37-2 does not apply to UPS rooms. This simplifies fire compartment design and removes the most complex fire safety regulatory burden. PGS 37-1 still applies if separate BESS containers are co-located on site.

### PGS 15 (Opslag van Verpakte Gevaarlijke Stoffen — Storage of Packaged Dangerous Goods)
Applies if facility stores:
- Diesel fuel for generators (PGS 28 primarily, but PGS 15 if packaged/in containers >150 L)
- Glycol coolant in drums (classified as combustible liquid)
- Ammonia refrigerant for heat pumps → PGS 13 (Ammoniak als Koudemiddel)
- Fire suppressant gas cylinders (IG-541 in pressurized cylinders — classified as compressed gas)

## 3. Fire Detection

### VESDA (Very Early Smoke Detection Apparatus)
- Aspirating smoke detection — continuously samples air through pipe network
- Detection time: <30 seconds (vs 3-5 minutes for point detectors)
- THE standard for mission-critical facilities — no credible alternative for early warning
- Vendor: Honeywell/Xtralis VESDA-E VEA/VEP/VES (Xtralis is now Honeywell)
- **Mounting:** Sampling pipes in ceiling void, CDU rooms, under-floor (if any), electrical rooms
- **Sensitivity:** Pre-alarm (Alert) at 0.005% obs/m, Action at 0.02% obs/m, Fire 1 at 0.06% obs/m
- **DEC-specific:** Sample pipes in CDU rooms to detect glycol vapor from leaks (glycol thermal decomposition produces smoke-like particles)

### Point Smoke Detectors (Puntdetectoren)
- Conventional photoelectric or ionization detectors
- Required per NEN 2535 (Brandmeldinstallaties — Fire Alarm Systems) as supplement to VESDA
- Provide individual zone identification and comply with insurance/certification requirements
- Key vendors: Siemens (Cerberus), Honeywell (Notifier), Bosch, Hochiki

### Linear Heat Detection (Lijnvormige Warmtedetectie)
- Heat-sensing cable along cable trays and busway routes
- Detects localized hot spots before they become fires
- Key vendors: Protectowire, Kidde (Fenwal), nVent/Raychem
- **DEC recommendation:** Install on all major cable tray runs and busway in AI halls — provides specific location of overheating

### Fire Alarm Panel (Brandmeldcentrale — BMC)
- NEN 2535 certified (Kiwa/Efectis certified per CCV scheme)
- Connected to Veiligheidsregio alarm center (PAC — Particuliere Alarmcentrale) via certified connection
- Alarm response time to brandweer: 8-15 minutes depending on Veiligheidsregio location
- **Mandatory:** Brandmeldinstallatie (fire alarm installation) for industriefunctie >2,500 m² per Bbl

## 4. Fire Suppression

### The Clean Agent Landscape (2025+)

**Novec 1230 (FK-5-1-12) — EFFECTIVELY DEAD:**
- 3M exited fluorochemical production (2025) — Novec 1230 is a fluoroketone
- PFAS regulation (EU REACH restriction proposal) threatens long-term availability
- Existing systems can be maintained with remaining stock, but new installations are increasingly difficult to source
- **DEC should NOT specify Novec 1230 for new facilities** — supply chain risk too high

**FM-200 (HFC-227ea) — PHASE-DOWN:**
- EU F-gas Regulation (Regulation 2024/573) phases down HFC production
- Not banned outright (fire suppression has exemption) but prices rising and availability declining
- GWP = 3,220 — highest among clean agents — ESG liability
- **Not recommended for new DEC facilities**

**IG-541 (Inergen) — RECOMMENDED:**
- Natural gas blend: 52% nitrogen, 40% argon, 8% CO2
- Zero GWP, zero ODP, no PFAS, no supply chain risk — components are atmospheric gases
- Stored at high pressure (200-300 bar) in large cylinder banks
- **Disadvantage:** Large cylinder storage footprint (5-10x more floor space than Novec/FM-200)
- **Disadvantage:** Higher installation cost (piping, nozzles, cylinder room)
- **Advantage:** Zero regulatory risk, zero environmental liability, proven track record
- Key vendors: Tyco/Johnson Controls (INERGEN), Kidde/Carrier (ARGONITE — similar blend), Siemens (Sinorix), Fike
- **DEC recommendation: IG-541 for all new data halls.** Accept the larger cylinder room footprint as trade-off for zero supply chain/regulatory risk

**Nitrogen (IG-100) — ALTERNATIVE:**
- Pure nitrogen inerting
- Even simpler than IG-541 — single-gas system
- Can be supplied via nitrogen generator (PSA/membrane) — eliminates cylinder replacement
- Maintained atmosphere: 15% O2 (fire cannot sustain, humans can work briefly with safety precautions)
- **Emerging approach:** "Oxygen reduction" / hypoxic fire prevention — continuous low-O2 atmosphere in unmanned data halls. Vendors: Wagner (OxyReduct), Isolcell
- **DEC consideration:** Oxygen reduction viable for unmanned AI training halls (no routine human occupancy). Not suitable for staffed colocation areas. Regulatory acceptance in NL still developing — consult Veiligheidsregio

### Pre-Action Sprinkler Systems

**The Uncomfortable Truth:**
Pre-action sprinklers are installed in many data centers primarily for insurance compliance (FM Global, insurer requirement), not because they are the best fire suppression for electronics. Water + energized electronics = massive secondary damage. A single sprinkler discharge in a €50M GPU cluster destroys more value than most fires would.

**When Sprinklers Make Sense:**
- Generator rooms (diesel fuel fire → water is appropriate)
- Transformer rooms (oil-filled transformer fire → water or foam)
- Cable tunnels and risers (cable fire propagation → water effective)
- Storage areas (combustible materials → sprinkler is the right answer)
- Offices, corridors, common areas (standard occupancy → Bbl required)

**When Sprinklers Do NOT Make Sense:**
- Data halls with gaseous suppression — redundant and contradictory
- CDU rooms with active liquid cooling — water-on-water adds no value
- UPS rooms with Li-ion — sprinkler alone cannot stop thermal runaway; dedicated suppression needed

**DEC Recommendation:**
- Data halls: IG-541 gaseous suppression (primary), NO sprinklers
- Generator rooms: pre-action sprinkler (single-interlock)
- Electrical/MV rooms: IG-541 or CO2 (CO2 for unmanned MV rooms — lethal concentration but no human occupancy)
- Cable risers/tunnels: pre-action sprinkler
- Offices/common: standard wet sprinkler per Bbl
- Present this as part of gelijkwaardigheid package to Veiligheidsregio

### FM Global / Insurance Requirements
- FM Global Data Sheet 5-32 (Data Centers and Related Facilities): reference standard for DC fire protection
- DS 5-32 generally requires pre-action sprinklers in data halls — BUT allows gaseous suppression as alternative with conditions
- If DEC's insurer is FM Global: negotiate early. Present IG-541 + VESDA + enhanced cable + compartmentation as equivalent to sprinkler
- Other insurers (Allianz AGCS, AXA XL, Zurich): generally less prescriptive than FM Global
- **Key principle:** Discuss fire protection strategy with insurer BEFORE design freeze — insurer requirements can drive major design changes

## 5. Cable Fire Performance

### The Most Important Fire Safety Decision Nobody Talks About

At AI density with busway + thousands of power/data cables, cable fire performance is THE most important passive fire safety measure.

### Euroclass Cable Ratings (NEN-EN 13501-6)

| Euroclass | Fire Performance | NL Requirement | DEC Recommendation |
|---|---|---|---|
| **B2ca-s1,d0,a1** | Non-flame-propagating, low smoke, no droplets, no acid gas | Optional (premium) | YES — for main cable tray runs in data halls |
| **Cca-s1,d2,a1** | Limited flame propagation, low smoke | **Bbl minimum for escape routes** | Minimum for all data hall cables |
| Dca-s2,d2,a2 | Some flame contribution | Legacy common | NOT acceptable for AI halls |
| Eca | Little performance | — | NOT for any indoor DC use |

**Bbl/Bal Requirement:** Cca minimum for cables in escape routes. Bbl does not mandate Cca for all building cables, but gelijkwaardigheid package for >2,500 m² compartment typically includes Cca or B2ca throughout data hall.

**DEC Recommendation: B2ca-s1,d0,a1 for power cables in data halls.**
- Premium over Cca: ~15-25% cable cost increase
- Benefit: massively reduced fire load in cable tray, near-zero flame propagation
- Combined with VESDA and IG-541: provides defense-in-depth where the actual fire risk is highest

**Key cable vendors (Euroclass certified):** Nexans (strong NL manufacturing — Delfzijl plant), Prysmian (NL production), Draka (now Prysmian), TKF (NL — Haaksbergen), Leoni

### Cable Penetration Sealing (Brandwerende Doorvoeren)

Every cable penetration through fire-rated wall or floor must be sealed to maintain fire compartment integrity:
- **Brandwerende afdichtingen (fire-rated seals):** intumescent putty, mortar, or pillow systems
- Must match WBDBO rating of the wall/floor (60 or 120 minutes)
- **Certified systems:** Hilti (CFS-S), Promat (PROMASEAL), Beele Engineering (NL — Aalten), Stopaq (NL)
- Tested per NEN-EN 1366-3 (Penetration Seals)
- **Critical for AI density:** High cable density means many penetrations per wall. Pre-plan penetration locations and sizes in design — retrofitting fire seals around packed cable trays is expensive and unreliable
- **Inspection:** Veiligheidsregio inspects penetration seals during gebruiksmelding / ingebruikname (commissioning)

## 6. Smoke Management (Rookbeheersing)

### Smoke Damage vs Fire Damage
In modern DC fires, smoke damage typically exceeds direct fire damage by 10-100x:
- Smoke (HCl, HCN from cable fires) corrodes copper traces on PCBs
- Smoke particles cause short circuits in electronics
- Smoke contamination requires complete replacement of affected IT hardware
- A contained cable fire in one rack can produce smoke that damages an entire data hall

### Smoke Management Strategy
1. **VESDA early detection** — detect before visible smoke production
2. **Gaseous suppression** — extinguish before smoke mass production
3. **Compartmentation** — contain smoke to affected zone if detection/suppression fails
4. **Smoke extraction** — mechanical smoke extraction per NEN 6093 (Brandveiligheid van gebouwen — Berekening van de rookdoorlatendheid) for large compartments
5. **Positive pressure** — maintain slight positive pressure in adjacent compartments to prevent smoke migration through door gaps and cable penetrations

### DEC-Specific: Smoke and Heat Recovery System
CDU piping penetrates fire compartment boundaries (data hall ↔ CDU room ↔ heat pump plant):
- Fire dampers (brandkleppen) on HVAC ductwork per NEN 6076
- CDU piping: water-filled piping is itself fire-resistant (water absorbs heat) — but pipe INSULATION may be combustible → specify non-combustible pipe insulation (mineral wool, not elastomeric foam) for all piping that crosses fire compartment boundaries
- Automatic CDU pump shutdown on fire alarm in affected zone — prevents coolant supply to fire zone

## 7. Li-Ion Battery Fire (BESS/UPS)

### If DEC Has On-Site Li-Ion (BESS Containers)

**Thermal Runaway Sequence:**
1. Cell internal short circuit → cell temperature rises
2. Cell venting → flammable gas release (electrolyte vapor, CO, H2)
3. Cell ignition → thermal runaway of single cell
4. Propagation → adjacent cells in module overheat from radiant/conducted heat
5. Module thermal runaway → cascade to adjacent modules
6. System fire → container fully involved, toxic gas release (HF)

**Suppression:**
- Gaseous agents (IG-541, Novec, FM-200) **DO NOT STOP thermal runaway** — they extinguish flame but cells continue thermal decomposition
- Only proven method: **water cooling** — massive water application to cool cells below self-heating threshold
- BESS containers: external water deluge or internal water mist + external fire brigade water application
- PGS 37-1 requires water supply calculation for BESS fire scenario

**Gas Detection:**
- Off-gas detection (CO, H2, VOC) BEFORE thermal runaway reaches ignition → allows evacuation and pre-emptive suppression
- Sensor vendors: Li-ion Tamer (Honeywell), Nexceris, Hanon Systems

**DEC BESS Fire Strategy:**
- BESS containers at safe distance per PGS 37-1 (minimum distance depends on energy content — typically 5-10 m from buildings)
- Water deluge system on BESS containers (separate from building sprinkler)
- Gas detection with automatic shutdown and ventilation
- Fire brigade liaison: provide Veiligheidsregio with BESS fire response plan
- **Drill:** Annual exercise with Veiligheidsregio for BESS fire scenario (builds relationship and identifies gaps)

## 8. Fire Brigade Interface (Brandweer Interface)

### Veiligheidsregio Engagement
NL has 25 Veiligheidsregio's (Safety Regions) managing fire brigade response:

**Pre-Application:**
- Contact Afdeling Risicobeheersing (Risk Management Department) of local Veiligheidsregio
- Present concept design including fire safety strategy
- Discuss gelijkwaardigheid approach for >2,500 m² compartments
- Identify concerns early — Veiligheidsregio feedback can be deal-breaker if ignored

**Design Phase:**
- Bereikbaarheid (accessibility): fire truck access to all building faces within 40 m (opstelplaats brandweervoertuig — fire truck positioning area)
- Bluswatervoorziening (fire water supply): minimum 60 m³/h for 4 hours (NEN 1006 + regional requirements) — typically from dedicated brandwatervoorziening (fire hydrants on water main or dedicated fire water tank)
- Brandweeringang (fire brigade entry): dedicated entry point with fire alarm panel replica (brandweerpaneel)
- Sleutelkluis (key safe): coded key box at fire brigade entry for after-hours access

**DEC-Specific Considerations:**
- Two buildings (DC + greenhouse) = two fire scenarios with different characteristics
- Greenhouse fire: large open space, glass structure, low fire load (plants), but WKK (CHP) and CO2 systems add complexity
- DC fire: high value, gaseous suppression, restricted access
- Fire brigade must understand BOTH building types and the interconnecting heat infrastructure
- Ammonia heat pump room: PGS 13 requires emergency response plan for ammonia release → coordinate with Veiligheidsregio hazmat (OGS — Officier van Dienst Gevaarlijke Stoffen) team

## 9. Passive Fire Protection

### Fire Compartment Walls (Brandscheidingen)
- **Concrete block (beton of kalkzandsteen):** 150-200 mm → 60-120 min fire resistance (Bbl Table 2.81)
- **Insulated metal panel:** fire-rated sandwich panel (mineral wool core) → 30-120 min depending on system. Key vendors: Kingspan (KS1150 FR), ArcelorMittal (Isodeck FR), Tata Steel (Trisobuild FR)
- **Gypsum stud wall (gipsplaatsysteem):** Siniat, Knauf, Gyproc — 60-120 min with appropriate stud/board configuration
- **DEC recommendation:** Concrete block for DC fire compartment walls (best acoustic performance — see acoustic-engineering.md, most robust for penetration sealing)

### Fire Doors (Branddeuren)
- Self-closing fire doors per NEN 6068 (Bepaling van de weerstand tegen branddoorslag en brandoverslag)
- 30-60 minute rating matching compartment wall
- Hold-open magnets released by fire alarm (electromagnet released on BMC signal)
- Key vendors: Hörmann, ASSA ABLOY, Novoferm (NL — strong market position), Daloc

### Structural Fire Protection
- Steel structure fire protection if bare steel doesn't meet Bbl fire resistance requirement
- Intumescent coating: thin film applied to steel, expands in fire to provide insulation (Sherwin-Williams Firetex, AkzoNobel International Interchar, Nullifire)
- Board protection: calcium silicate or vermiculite board wrapped around steel (Promat PROMATECT, Etex)
- Spray-applied: cementitious or mineral fiber spray (Cafco, Isolatek)
- **DEC recommendation:** Intumescent coating for exposed structural steel in data halls (clean appearance, no maintenance access interference). Board or spray for concealed areas

## Cross-References
- See [electrical-power-systems.md](electrical-power-systems.md) for generator fuel storage fire protection and UPS topology impact
- See [civil-works-netherlands.md](civil-works-netherlands.md) for fire compartment wall construction
- See [data-hall-design.md](data-hall-design.md) for compartment sizing and hall geometry
- See [liquid-cooling-systems.md](liquid-cooling-systems.md) for coolant flammability and leak detection
- See [power-quality-grounding.md](power-quality-grounding.md) for arc flash protection
- See [acoustic-engineering.md](acoustic-engineering.md) for acoustic performance of fire-rated walls
- See [commissioning-handover.md](commissioning-handover.md) for fire system Cx and Veiligheidsregio acceptance
- See companion skill `netherlands-permitting` for omgevingsvergunning brandveilig gebruik, PGS 37 permitting, gelijkwaardigheid procedure
- See companion skill `energy-markets` for BESS revenue stacking (PGS 37-1 fire safety impacts BESS siting)
