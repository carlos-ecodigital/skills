# DC Design Checklist — DEC AI Colocation with Heat Recovery

## Purpose
Comprehensive design review checklist for DEC's purpose-built AI colocation facility in the Netherlands with greenhouse waste heat integration. Covers all 15 expert domains. Use at each design phase gate.

---

## Phase Gate Reference

| Gate | Design Phase | Key Deliverable | Checklist Sections to Complete |
|---|---|---|---|
| G0 | Concept / Haalbaarheidsstudie | Feasibility study | A, B (partial), I (partial), N |
| G1 | Voorlopig Ontwerp (VO) | Preliminary design | A through H |
| G2 | Definitief Ontwerp (DO) | Detailed design | All sections A through O |
| G3 | Uitvoeringsgereed Ontwerp (UO) | Construction-ready design | Verification of all items |
| G4 | Oplevering (COD) | Commercial Operation Date | O (commissioning) confirmed complete |

---

## A. Facility Concept (Expert 1: AI Factory Concept Designer)

- [ ] IT load capacity defined (MW IT)
- [ ] Rack density target defined (kW/rack range)
- [ ] Tenancy model confirmed (single-tenant / multi-tenant colocation / hybrid)
- [ ] Redundancy topology selected and justified (N+1 / 2N / block redundant)
- [ ] NEN-EN 50600 availability class selected (power class / cooling class)
- [ ] Column grid dimensions confirmed (recommended: 6.0 m × 12.0 m for AI density)
- [ ] Slab-on-grade confirmed (raised floor rejected for AI density)
- [ ] Temperature cascade documented (GPU junction → CDU supply/return → heat pump → greenhouse)
- [ ] Phasing strategy documented (Phase 1 capacity, expansion reserves, future halls)
- [ ] Design basis document (DBD) issued and approved by DEC

## B. Liquid Cooling (Expert 2: Liquid Cooling Systems Engineer)

- [ ] Cooling technology selected (DTC / immersion / hybrid) with justification
- [ ] CDU vendor selected with performance data at DEC operating temperatures
- [ ] CDU placement decision (in-row / end-of-row / adjacent room) confirmed
- [ ] Facility interface temperature specified: supply ___°C, return ___°C
- [ ] Coolant chemistry specified (propylene glycol ___%, pH range, inhibitor package)
- [ ] Pipe material and sizing documented (manifold material, branch sizing)
- [ ] Quick-disconnect coupling type confirmed with bonding continuity verification
- [ ] Leak detection hierarchy documented (spot / cable / zone / CDU monitoring)
- [ ] Redundancy: N+1 CDU capacity confirmed
- [ ] GPU thermal throttle risk assessed at maximum CDU supply temperature

## C. Heat Rejection (Expert 3: Heat Rejection & Dry Cooler Specialist)

- [ ] Technology selected (adiabatic dry cooler / cooling tower / plate HX) with justification
- [ ] Vendor and model selected (e.g., Güntner GFD V-shape with Hydrospray)
- [ ] Free cooling hours calculated for NL climate data (target location)
- [ ] Water consumption estimated for adiabatic operation (m³/year)
- [ ] Legionella risk assessment completed (ISSO 55.3 compliance confirmed)
- [ ] Noise assessment at nearest woning: source Lw ___dB(A), predicted level at receptor ___dB(A)
- [ ] Night mode fan speed reduction strategy documented
- [ ] N+1 redundancy confirmed
- [ ] PUE contribution from cooling calculated: ___

## D. Heat Pump & Heat Recovery (Experts 4-5)

### Heat Pump
- [ ] Refrigerant selected with justification (R717 ammonia recommended)
- [ ] Capacity sized: ___MWth at source ___°C → delivery ___°C
- [ ] COP at design point: ___ (target: 3.8-4.5)
- [ ] Vendor selected with reference projects
- [ ] PGS 13 ammonia safety requirements documented
- [ ] Plant room location and ventilation design completed
- [ ] Thermal storage (ATES / buffer tank) sizing: ___ m³, ___ hour capacity

### Heat Recovery Integration
- [ ] System architecture diagram completed (full thermal cascade)
- [ ] Crop-specific temperature requirements confirmed with grower
- [ ] Buffer tank sizing: ___ m³ (target: 4-hour at ___ MWth)
- [ ] Piping route between DC and greenhouse documented (distance: ___ m)
- [ ] Heat meter specified (Kamstrup MULTICAL 803 or equivalent, MID-certified)
- [ ] Warmteleveringsovereenkomst terms agreed: delivery temp ≥___°C, availability ≥___%, price €___/GJ
- [ ] Three operating modes documented: full recovery / partial / full rejection
- [ ] Wcw (Warmtewet/Collectieve Warmtevoorziening) applicability assessed
- [ ] SDE++ eligibility assessed and application timeline planned (if applicable)

## E. Electrical Power (Experts 6-8)

### MV/LV Distribution
- [ ] Grid connection voltage and capacity confirmed with DSO: ___kV, ___MVA
- [ ] MV switchgear type: SF6-free confirmed (vendor: ___)
- [ ] Transformer configuration: N+1 confirmed, type (dry/oil), K-factor ___
- [ ] UPS/DRUPS topology selected with justification
- [ ] Generator configuration: ___× ___MVA gensets (N+1), fuel storage ___ liters
- [ ] LV distribution: busway vendor and routing documented
- [ ] Rack PDU specification and metering accuracy class confirmed

### Power Quality & Grounding
- [ ] Harmonic analysis completed: predicted THDi ___% at PCC
- [ ] Mitigation strategy documented (AFE UPS / active filter / K-rated transformers)
- [ ] Neutral conductor sized ≥100% of phase conductor (confirmed)
- [ ] TN-S grounding system documented
- [ ] CDU piping equipotential bonding plan documented
- [ ] Quick-disconnect bonding continuity verified in specification
- [ ] Lightning protection level: LPL ___ (per NEN-EN-IEC 62305-2 risk assessment)
- [ ] SPD cascade documented (T1/T2/T3 coordination)

### Metering
- [ ] Revenue-grade metering plan for multi-tenant billing documented
- [ ] PUE/ERE/ERF measurement points defined per NEN-EN 50600-99-1/99-3
- [ ] Power quality analyzer specified for continuous PCC monitoring

## F. Data Hall Design (Expert 9: Data Hall Architect)

- [ ] Hall dimensions: ___ m × ___ m × ___ m (clear height ≥4.5 m confirmed)
- [ ] Rack rows per hall: ___, racks per row: ___
- [ ] Containment strategy selected (hot aisle / cold aisle) with justification
- [ ] Fire compartment size: ___ m² (≤2,500 m² or gelijkwaardigheid submitted)
- [ ] Adjacency matrix completed: CDU room / electrical room / UPS room / MMR / staging
- [ ] Multi-tenant demarcation documented (cage / wall / fire separation)
- [ ] Shared vs tenant infrastructure clearly delineated
- [ ] Overhead stacking order documented (racks → CDU piping → busway → cable tray → fire)
- [ ] Residual air cooling sized for 20% air-cooled heat load

## G. Structured Cabling & Connectivity (Expert 10)

- [ ] Backbone fiber: OS2 single-mode, ___-fiber count per cable
- [ ] Horizontal fiber: OM4/OM5 multimode, connector type: MPO-___
- [ ] Cable class: Euroclass Cca-s1,d2,a1 minimum (B2ca preferred for data halls)
- [ ] External connectivity: ___ diverse fiber routes from ___ carriers
- [ ] Meet-Me Room location and design documented
- [ ] Cable tray capacity: ≥50% spare for future cables
- [ ] EMC separation between power and data cables: ≥150 mm (NEN 1010)
- [ ] AMS-IX / NL-ix peering connectivity path documented

## H. Geotechnical & Structural (Expert 11)

- [ ] Geotechnical investigation completed: CPT at ___ m spacing, boreholes at ___
- [ ] Soil profile documented: bearing layer at ___ m depth
- [ ] Foundation type selected: ___ (driven prefab concrete piles recommended for western NL)
- [ ] Pile design: diameter/section ___, capacity ___ kN, spacing ___ m c/c
- [ ] Floor slab loading capacity: ___ kN/m² in AI zones (target: 15-25 kN/m²)
- [ ] Floor flatness: FM2 or better per TR 34
- [ ] Structural system: steel portal frame / concrete tilt-up / hybrid
- [ ] Roof design: PV array loading accommodated (___ kN/m² additional)
- [ ] NPR 9998 seismic assessment: required / not required (Groningen zone check)
- [ ] Watertoets completed with waterschap: water storage ___ m³ required

## I. Construction Management (Expert 12)

- [ ] Contract form selected: UAV 2012 / UAV-GC 2005 / FIDIC (with justification)
- [ ] NEN 5725/5740 soil investigation: contamination status confirmed
- [ ] NGE/OCE investigation: completed / not required (with justification)
- [ ] KLIC-melding submitted and utility locations received
- [ ] Bouwveiligheidsplan (V&G-plan) prepared
- [ ] Construction stikstof AERIUS calculation completed: ___ mol/ha/yr
- [ ] Bodemsanering required: yes / no (if yes: status and timeline)
- [ ] Bronbemaling permit: required / not required (waterschap: ___)
- [ ] PFAS groundwater test: completed (results: ___)
- [ ] Construction timeline: ___ months to COD
- [ ] Critical path items identified: grid connection (___months), transformers (___months), DRUPS (___months)

## J. Fire Safety & Suppression (Expert 13)

- [ ] Fire threat hierarchy documented for this facility
- [ ] Brandcompartiment sizing: ___ m² per hall
- [ ] Gelijkwaardigheid package: required / not required (if >2,500 m²: package documented)
- [ ] Detection system: VESDA + point detectors + linear heat detection (where applicable)
- [ ] Suppression system per zone:
  - Data halls: IG-541 (IG-100 alternative assessed: yes / no)
  - Electrical rooms: IG-541 / CO2
  - Generator rooms: pre-action sprinkler
  - Offices/common: wet sprinkler
- [ ] Cable rating specified: Euroclass B2ca-s1,d0,a1 for data hall power cables
- [ ] Brandwerende doorvoeren: system specified, tested per NEN-EN 1366-3
- [ ] Veiligheidsregio pre-application consultation completed
- [ ] FM Global / insurer review completed (fire strategy accepted)
- [ ] PGS 37-1 applicable (BESS): yes / no
- [ ] PGS 37-2 applicable (Li-ion UPS): yes / no (DRUPS eliminates: ___)
- [ ] PGS 13 applicable (ammonia heat pump): yes / no

## K. Acoustic Engineering (Expert 14)

- [ ] Noise sources inventoried with Lw per octave band
- [ ] Nearest gevoelig gebouw identified: distance ___ m, direction ___
- [ ] Noise model completed (software: SoundPLAN / iNoise / CadnaA)
- [ ] Predicted levels at receptor: dag ___dB(A), avond ___dB(A), nacht ___dB(A)
- [ ] Comparison with Bal limits: dag ≤50, avond ≤45, nacht ≤40 — compliant: yes / no
- [ ] Piekgeluid from generator start: predicted LAmax ___dB(A) at receptor
- [ ] Tonality correction (Kt) assessed: applicable / not applicable
- [ ] Mitigation measures documented:
  - [ ] Low-noise dry cooler specification
  - [ ] Generator acoustic enclosure (grade: ___)
  - [ ] Heat pump plant room Rw ___dB
  - [ ] Geluidscherm: required / not required (if yes: height ___m, length ___m)
  - [ ] Building orientation optimized for noise
- [ ] Maatwerkvoorschrift required: yes / no
- [ ] Geluidrapport prepared for omgevingsvergunning submission
- [ ] Acoustic consultant engaged: firm name ___

## L. Commissioning (Expert 15)

- [ ] Commissioning Plan (Cx Plan) prepared per ASHRAE Guideline 0
- [ ] Owner's Project Requirements (OPR) documented (including heat recovery criteria)
- [ ] Cx team appointed: Cx agent / Cx authority identified
- [ ] FAT schedule: heat pump / CDU / transformer / DRUPS / switchgear
- [ ] SAT sequence documented: electrical → mechanical → fire → BMS → security
- [ ] IST Level 5 test scenarios documented:
  - [ ] Grid failure (netstoring)
  - [ ] Cooling system failure (CDU N+1)
  - [ ] Heat recovery chain failure (heat pump trip)
  - [ ] Fire alarm activation
  - [ ] Multiple simultaneous failures
  - [ ] Seasonal transition
- [ ] Load bank testing planned: ramp 25% → 50% → 75% → 100%
- [ ] Greenhouse thermal bridge Cx protocol documented:
  - [ ] Thermal delivery verification
  - [ ] Control interface test
  - [ ] Emergency isolation test
  - [ ] Heat meter accuracy cross-check
- [ ] Grower participation in thermal bridge Cx confirmed
- [ ] Veiligheidsregio invited to IST fire scenario
- [ ] Handover documentation list agreed with DEC operations team
- [ ] Seasonal Cx plan: 12-month post-COD verification schedule

## M. BESS (if applicable)

- [ ] BESS capacity: ___MWh / ___MW
- [ ] Location: outdoor containers at ___m from nearest building (PGS 37-1 distance)
- [ ] Safety systems: gas detection, ventilation, water deluge, fire brigade response plan
- [ ] Electrical integration: separate MV feeder, protection coordination study completed
- [ ] Revenue stacking strategy documented (see energy-markets skill)
- [ ] PGS 37-1 compliance assessment completed
- [ ] Seveso/BRZO threshold check: below threshold / applicable (see netherlands-permitting skill)

## N. Permitting Status Tracker

| Permit / Approval | Status | Submission Date | Expected Decision | Notes |
|---|---|---|---|---|
| Omgevingsvergunning bouwtechnisch (Bbl) | | | | Gevolgklasse ___ |
| Omgevingsvergunning milieu (Bal) | | | | Geluidrapport attached |
| Watervergunning (waterschap) | | | | Bronbemaling + waterberging |
| Netaansluiting (DSO) | | | | Critical path: ___month lead time |
| Brandveiligheid (Veiligheidsregio) | | | | Gelijkwaardigheid if >2,500 m² |
| Stikstof/AERIUS | | | | Construction + operation phases |
| SDE++ (RVO) | | | | If heat recovery eligible |
| Wkb kwaliteitsborger | | | | Appointed: ___ |

## O. Cross-Skill Verification

- [ ] All cross-references between dc-engineering reference files verified
- [ ] Companion skill handoffs documented:
  - [ ] → netherlands-permitting: permit applications, geluidrapport, AERIUS, brandveiligheid
  - [ ] → energy-markets: grid connection strategy, BESS revenue, PPA structure
  - [ ] → ai-infrastructure: tenant IT specifications, rack density, networking requirements
  - [ ] → site-development: site selection scoring, master plan integration, grower interface, financial model
- [ ] RACI matrix reviewed: no unassigned cross-cutting questions

---

## Sign-Off

| Role | Name | Date | Signature |
|---|---|---|---|
| DEC Project Director | | | |
| DC Engineering Lead | | | |
| Commissioning Agent | | | |
| Acoustic Consultant | | | |
| Fire Safety Engineer | | | |
| Grower Representative | | | |
