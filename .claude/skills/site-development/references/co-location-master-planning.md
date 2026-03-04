# Co-Location Master Planning

## 1. Design Principle: Unified Thermodynamic System

### Core Philosophy

A DEC facility is not "a data center next to a greenhouse." It is a single thermodynamic system with two building types, connected by a thermal bridge that is the most critical piece of infrastructure on the site.

**Master planning sequence (opinionated):**
1. Define the thermal bridge (heat pipe routing, capacity, redundancy)
2. Position the heat exchanger / buffer tank (central to thermal system)
3. Orient the greenhouse (optimize for light, wind, heat delivery point)
4. Position the DC building (optimize for grid connection, cooling, tenant access)
5. Route shared utilities (substation, water, fiber, roads, fire water)
6. Plan expansion reserves
7. Integrate landscape requirements

**Common mistake:** Designing the DC first, then asking "where do we put the greenhouse?" This produces suboptimal thermal bridge routing, compromised greenhouse orientation, and expensive retrofit.

## 2. Site Layout Principles

### Spatial Relationships

```
                    ┌──────────────────────────────────────────────┐
                    │                  SITE BOUNDARY                │
                    │                                               │
                    │   ┌─────────┐  Thermal    ┌───────────────┐  │
                    │   │   DATA  │  Bridge     │  GREENHOUSE   │  │
                    │   │  CENTER │◄══════════►│   COMPLEX     │  │
                    │   │  40 MW  │  (heat pipe)│  10-20 ha     │  │
                    │   │         │             │               │  │
                    │   └────┬────┘             └───────┬───────┘  │
                    │        │                          │          │
                    │   ┌────┴────┐  ┌─────────┐  ┌───┴───────┐  │
                    │   │  SUB-   │  │ BUFFER  │  │   SOLAR   │  │
                    │   │ STATION │  │  TANK   │  │  PV FIELD │  │
                    │   │  +BESS  │  │ +HEAT   │  │  (5 MWp)  │  │
                    │   │         │  │  PUMP   │  │           │  │
                    │   └─────────┘  └─────────┘  └───────────┘  │
                    │                                               │
                    │   ═══ Utility corridor (power, water, fiber) │
                    │   ─── Road access                            │
                    │   ▓▓▓ Landscape buffer (geluidscherm, groen) │
                    └──────────────────────────────────────────────┘
```

### Key Spatial Constraints

| Constraint | Requirement | Source | DEC Impact |
|---|---|---|---|
| **Fire separation (brandoverslag)** | Minimum distance between DC and greenhouse depends on fire load and construction | Bbl, Veiligheidsregio | Typically 5-15 m depending on facade classification |
| **Greenhouse orientation** | Glass facades oriented for maximum light (typically east-west ridgeline in NL) | Horticultural best practice | Constrains greenhouse placement relative to DC |
| **Noise zone (geluidcontour)** | DC dry coolers, generators, transformers must meet noise limits at greenhouse boundary | Bal Art. 4.17-4.21, Bkl | May require geluidscherm (noise barrier) between DC and greenhouse |
| **Landscape buffer** | Green buffer zone between industrial (DC) and agricultural (greenhouse) use | Omgevingsplan, beeldkwaliteitsplan | 5-20 m landscape strip typical |
| **Water buffer (waterberging)** | On-site water storage for increased impervious surface | Watertoets requirement (waterschap) | Wadi system or retention basin, typically 10-15% of impervious area |
| **Expansion reserve** | Space for DC Phase 2+, additional greenhouses, BESS expansion | DEC growth plan | Reserve 50-100% of Phase 1 footprint |
| **Security perimeter** | DC requires physical security (CCTV, fencing, access control) | Tenant SLA, insurance | Separate security zones for DC and greenhouse |

### Adjacency Matrix

| Element | DC Building | Greenhouse | Substation | Buffer/HP | BESS | Solar PV | Parking/Office |
|---|---|---|---|---|---|---|---|
| **DC Building** | -- | 50-500 m (thermal bridge) | Adjacent (<50 m) | Adjacent (<100 m) | Adjacent (<50 m) | Flexible | Adjacent |
| **Greenhouse** | 50-500 m | -- | Flexible | Adjacent (<100 m) | Flexible | Flexible | Flexible |
| **Substation** | Adjacent | Flexible | -- | Adjacent | Adjacent | Adjacent | Separated |
| **Buffer/Heat Pump** | Adjacent | Adjacent | Adjacent | -- | Flexible | Flexible | Separated |
| **BESS** | Adjacent | Flexible | Adjacent | Flexible | -- | Adjacent (cable pooling) | Separated (safety) |
| **Solar PV** | Flexible | Flexible | Adjacent | Flexible | Adjacent | -- | Flexible |

**Critical adjacency:** Buffer tank / heat pump plant must be centrally positioned between DC and greenhouse to minimize pipe runs in both directions.

## 3. Thermal Bridge Design

### Heat Pipe Routing

The thermal bridge connects the DC heat recovery system to the greenhouse heating system via pre-insulated pipes carrying hot water.

**Key design parameters:**

| Parameter | Value Range | Design Driver |
|---|---|---|
| Pipe distance (DC to greenhouse) | 50-2,000 m (target <500 m) | Cost, heat loss, pump energy |
| Supply temperature | 40-55°C (from DC CDU) or 60-90°C (from heat pump) | Greenhouse crop requirement |
| Return temperature | 25-40°C | DC CDU inlet requirement |
| Flow rate | 100-500 m3/h (depends on thermal capacity) | Pipe diameter, pump sizing |
| Pipe diameter | DN200-DN500 (depends on capacity and distance) | Cost vs pressure drop |
| Insulation | Pre-insulated bonded pipe (Logstor, Isoplus, Thermaflex) | Heat loss target <1°C/km |
| Routing | Above-ground (pipe rack) or below-ground (direct burial) | Cost, aesthetics, maintenance |

### Above-Ground vs Below-Ground Routing

| Factor | Above-Ground (Pipe Rack) | Below-Ground (Direct Burial) |
|---|---|---|
| **Cost** | Lower installation cost | Higher installation (excavation, backfill) |
| **Maintenance** | Easy inspection, leak detection, repair | Difficult access, leak detection harder |
| **Aesthetics** | Visible — may require visual screening | Invisible — preferred by municipalities |
| **Heat loss** | Slightly higher (exposed to air) | Lower (ground insulation) |
| **Permits** | May require omgevingsvergunning for visual impact | May require ontgrondingsvergunning for excavation |
| **Frost risk** | Freeze protection required | Ground temperature provides some protection |
| **Flexibility** | Easy to modify/extend | Expensive to modify |

**DEC recommendation:** Below-ground for public-facing routes (between DC and greenhouse), above-ground within the DC secure perimeter. Use pre-insulated bonded pipe (Logstor Duo or similar) for below-ground sections.

### Buffer Tank Sizing

**Purpose:** Decouple DC heat production (steady) from greenhouse heat demand (variable/seasonal).

**Sizing methodology:**

```
Buffer volume = Peak hourly mismatch × buffer hours

Example: 40 MW DC, 30 MW thermal recovery, greenhouse peak demand 25 MW
  Peak mismatch scenarios:
  1. DC at full load, greenhouse demand zero (summer day): 30 MW excess → buffer or reject
  2. DC at reduced load (maintenance), greenhouse at peak (winter night): 20 MW deficit → buffer + backup
  3. Normal operation: steady supply, variable demand → buffer smooths 2-6 hours

  Buffer sizing: 25 MWth × 4 hours × 3.6 GJ/MWh ÷ (ΔT × 4.18 kJ/kg·K × 1000 kg/m3)
    At ΔT = 20°C: 360 GJ ÷ (20 × 4.18 × 1000 / 1,000,000) = ~4,300 m3

  Practical range: 2,000-10,000 m3 depending on buffer hours and temperature range
```

**Buffer tank types:**
- Steel tank (above-ground): 100-5,000 m3, proven, visible, requires foundation
- Concrete tank (partially buried): 1,000-20,000 m3, cost-effective at large size, can be landscaped
- ATES (Aquifer Thermal Energy Storage / Warmte-Koude Opslag): seasonal storage, requires hydrogeological suitability, permits from province

### Seasonal Mismatch Strategy

| Season | DC Heat Production | Greenhouse Demand | Strategy |
|---|---|---|---|
| **Winter peak** (Dec-Feb) | 25-30 MWth (steady) | 20-30 MWth (peak) | Heat pump uplift to meet peak; buffer for hourly variation |
| **Spring/Autumn** (Mar-May, Sep-Nov) | 25-30 MWth | 10-20 MWth | Partial utilization; excess to buffer or reject |
| **Summer** (Jun-Aug) | 25-30 MWth | 2-5 MWth (screens, dehumidification only) | Significant excess → reject via dry coolers or store (ATES) |

**DEC challenge:** Year-round heat production, seasonal demand. Solutions:
1. **Size heat recovery for winter peak** → accept summer excess rejection (simplest)
2. **ATES seasonal storage** → store summer excess, use in winter (capital-intensive, permitting complex)
3. **District heating connection** → sell summer excess to warmtenet (if available)
4. **Multiple greenhouse types** → tropical crops for higher summer demand

## 4. Shared Utilities

### Electrical Substation

**Shared vs separate substations:**
- **Shared substation** (recommended): single grid connection point for DC + greenhouse + BESS + solar PV → MLOEA/cable pooling benefits, lower connection cost, faster connection
- **Separate substations:** simpler commercially but wastes grid capacity, higher total cost

**Substation placement:** Adjacent to DC building (shortest MV cable run to data hall), with MV cable run to greenhouse for their supply.

### Water System

| Water Use | Volume | Quality | Source |
|---|---|---|---|
| DC cooling (adiabatic dry coolers) | 50-200 m3/day | Softened, Legionella-treated | Municipal water + treatment |
| Greenhouse irrigation | 100-1,000 m3/day | Rainwater + supplemental | On-site rainwater collection (kaswater) + municipal |
| Fire water | 200-500 m3 reserve | Untreated | Dedicated fire water tank or surface water |
| Domestic (office/sanitary) | 5-20 m3/day | Potable | Municipal |

**Water sharing opportunity:** Greenhouse rainwater collection (verplicht voor glastuinbouw / mandatory for greenhouse horticulture in many regions) can serve as supplemental cooling water for DC. Conversely, DC treated water discharge (if any) may be suitable for greenhouse use after quality check.

### Fiber Connectivity

**Fiber routing:**
- Carrier fiber enters site at meet-me room / entrance facility
- Fiber distribution from meet-me room to DC data halls (short runs, diverse paths)
- Fiber to greenhouse for climate control, monitoring, data exchange (low bandwidth, but connectivity needed)
- Minimum 2 diverse carrier entries from different directions

### Road Access

- Heavy vehicle access for DC equipment delivery (transformers: 50-100 ton, generators: 20-40 ton)
- Regular truck access for greenhouse logistics (produce transport, supplies)
- Separate access points for DC (security-controlled) and greenhouse (agricultural traffic)
- Construction vehicle access for phased build-out without disrupting operations

## 5. Construction Phasing

### Phase Strategy

```
Phase 0: Site Acquisition & Permitting (Year 0-1)
  ├── Land acquisition / erfpacht agreement
  ├── Omgevingsvergunning(en) applied for and obtained
  ├── Grid connection application submitted and offer accepted
  ├── Grower LOI / heat supply framework agreement signed
  └── Detailed design completed (DC + greenhouse + thermal bridge)

Phase 1A: DC Construction (Year 1-2)
  ├── Site preparation (bodemsanering if needed, grading, piling)
  ├── DC building shell (steel frame, cladding, roof)
  ├── Electrical infrastructure (substation, MV distribution)
  ├── Cooling infrastructure (CDU, dry coolers, piping)
  ├── Heat recovery infrastructure (heat pump, buffer tank, pipe stubs)
  ├── BESS installation (if Phase 1)
  └── DC commissioning (IST Level 1-5)

Phase 1B: Greenhouse & Thermal Bridge (Year 1.5-2.5)
  ├── Greenhouse construction (typically faster than DC: 6-12 months)
  ├── Thermal bridge pipe installation (DC to buffer to greenhouse)
  ├── Greenhouse heating system connection to DEC heat supply
  ├── CO2 dosing system installation (if WKK replaced)
  ├── Greenhouse commissioning
  └── First heat delivery (commissioning → steady state: 2-4 weeks)

Phase 1C: First Tenants & Operations (Year 2-3)
  ├── First neocloud tenant onboarded
  ├── IT load ramps up → heat production begins
  ├── Greenhouse receives heat → grower validates temperature/reliability
  └── Revenue generation starts (colocation + heat + BESS)

Phase 2: Expansion (Year 3-5)
  ├── Additional DC data halls
  ├── Additional greenhouse area
  ├── Expanded thermal bridge capacity
  ├── Grid connection Phase 2 energization
  └── Additional tenants onboarded
```

### Construction Sequencing Constraints

| Constraint | Requirement | Mitigation |
|---|---|---|
| **Grid connection must be live before DC commissioning** | Substation energized at least 3-6 months before tenant move-in | Start grid connection application at earliest possible date |
| **Heat infrastructure must be ready before greenhouse crop planting** | Grower plans crop cycle around heat availability | Coordinate Phase 1B completion with grower planting season (typically Sep-Nov for winter crops) |
| **Piling must precede all building construction** | Typical NL requirement: driven/pressed piles for all structures | Coordinate pile driving across DC and greenhouse to minimize mobilization |
| **Bodemsanering blocks site preparation** | No construction on contaminated areas until remediation complete or approved plan | Remediation concurrent with design/permitting phase |
| **Archaeology may delay site preparation** | If IVO finds significant remains, opgraving (excavation) required before construction | Front-load archaeological surveys in Phase 0 |

## 6. Landscape Integration

### Dutch Landscape Requirements

| Requirement | Typical Obligation | DEC Approach |
|---|---|---|
| **Groencompensatie (green compensation)** | Replace lost greenery: trees, hedges, ecological zone | Perimeter planting, ecological corridor between DC and greenhouse |
| **Waterberging (water storage)** | On-site retention for increased impervious surface: 40-60 mm per m2 | Wadi system, retention pond, green roof on office/administration building |
| **Beeldkwaliteitsplan (visual quality plan)** | Municipality sets architectural/landscape standards | Integrate DC facade with agricultural context; green screening of dry coolers and BESS |
| **Welstandsnota (aesthetics policy)** | Local architectural review committee (welstandscommissie) approval | Design DC with materials and colors compatible with agricultural landscape |
| **Geluidscherm (noise barrier)** | If noise at sensitive receptor exceeds limits | Earth berm or acoustic fence between DC dry coolers and greenhouse / neighbors |

### Visual Impact Mitigation

**DEC facilities near greenhouses must address visual impact:**
- DC building height: typically 12-18 m → visible above greenhouse roofline (4-6 m)
- Dry coolers on DC roof: visible and industrial-looking
- BESS containers: industrial appearance
- Substation: functional, not attractive

**Mitigation approaches:**
1. **Green screening:** Fast-growing hedges (beuk/beech, haagbeuk/hornbeam) around DC perimeter
2. **Earth berms:** 2-3 m height berms between DC and public areas, doubles as noise barrier
3. **Facade treatment:** Use colors and materials that blend with agricultural context (green/brown tones, timber-effect cladding)
4. **Solar PV integration:** Solar panels on DC roof improve visual appearance (technology rather than industrial)
5. **Greenhouse framing:** Position greenhouse between DC and public road → greenhouse is the visible face of the site

## 7. Expansion Reserve Planning

### Reserve Requirements

| Element | Phase 1 | Expansion Reserve | Total Site Need |
|---|---|---|---|
| DC building footprint | 3,000-5,000 m2 | 3,000-5,000 m2 (100% expansion) | 6,000-10,000 m2 |
| Greenhouse area | 5-10 ha | 5-10 ha (100% expansion) | 10-20 ha |
| Substation footprint | 500-1,000 m2 | 500 m2 (for additional transformer) | 1,000-1,500 m2 |
| BESS footprint | 500-1,000 m2 | 500-1,000 m2 | 1,000-2,000 m2 |
| Buffer tank | 1 tank (2,000-5,000 m3) | Space for 2nd tank | Add 500-1,000 m2 |
| Utility corridors | Sized for Phase 1 | Designed for full build-out from day one | No additional land |
| Landscape/water | Per Phase 1 impervious area | Must accommodate full build-out | 15-20% of total site |
| Roads/parking | Phase 1 access | Expandable | 5-10% of total site |
| **Total site area** | **8-15 ha** | **8-15 ha reserve** | **15-30 ha total** |

**Critical principle:** Utility corridors (power cable trenches, heat pipes, fiber ducts, water mains) must be designed and partially installed for full build-out during Phase 1 construction. Retrofitting underground utilities under operational infrastructure is extremely expensive and disruptive.

## Cross-References
- See [site-selection-methodology.md](site-selection-methodology.md) for site evaluation prior to master planning
- See [grower-thermal-interface.md](grower-thermal-interface.md) for greenhouse-side thermal requirements that drive master plan
- See [project-finance-economics.md](project-finance-economics.md) for phasing economics and CAPEX allocation
- See companion skill `dc-engineering`:
  - [ai-factory-design.md] for DC building concept and layout
  - [heat-recovery-integration.md] for thermal cascade design
  - [heat-pumps-waste-heat.md] for heat pump plant sizing and placement
  - [acoustic-engineering.md] for noise impact on master plan layout
  - [civil-works-netherlands.md] for geotechnical and construction constraints
  - [commissioning-handover.md] for integrated DC-greenhouse commissioning sequence
- See companion skill `netherlands-permitting`:
  - Omgevingsplanexpert for zoning/bestemmingsplan compliance
  - Milieu Specialist for environmental integration requirements
  - Water & Bodem Expert for watertoets and water storage
  - Bouw & Kwaliteitsborging for building permit requirements
- See companion skill `energy-markets`:
  - [grid-connection-strategy.md] for substation and MLOEA/cable pooling layout
