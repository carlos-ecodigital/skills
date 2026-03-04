# Data Hall Design for AI Colocation

## 1. Data Hall as Architectural Problem

### The Reframing
The data hall is NOT a room that happens to contain IT equipment. It is a precision-engineered volume whose geometry, adjacencies, and MEP coordination determine facility efficiency, tenant flexibility, and construction cost. The Data Hall Architect (Datahalontwerper) owns spatial decisions — not structural (→ Expert 11) or leak containment (→ Expert 2).

### DEC Context
DEC's multi-tenant AI colocation model adds constraints beyond single-tenant AI factories:
- Different tenants at different rack densities (60-130 kW/rack)
- Revenue-grade metering at hall/row/rack level
- Independent tenant access without crossing other tenants' space
- Shared MEP infrastructure with tenant-specific distribution
- Heat recovery aggregation from all tenants into unified thermal system

## 2. Space Programming

### Data Hall Sizing

**IT Floor Space per MW:**
| Rack Density | Racks per MW | Floor Area per MW | Notes |
|---|---|---|---|
| 20 kW/rack (enterprise) | 50 | 250 m² | Traditional — NOT DEC's market |
| 60 kW/rack (moderate AI) | 17 | 100-120 m² | DEC Phase 1 target range |
| 100 kW/rack (high AI) | 10 | 70-90 m² | NVIDIA DGX/HGX clusters |
| 130 kW/rack (ultra-high) | 8 | 55-70 m² | GB200 NVL72 racks |

**Auxiliary Space (per MW IT):**
| Function | Area per MW IT | Adjacency Requirement |
|---|---|---|
| CDU room | 15-25 m² | Directly adjacent to data hall, same level |
| Electrical room (LV switchgear, PDU) | 20-30 m² | Adjacent to data hall, separated by fire wall |
| UPS/DRUPS room | 25-40 m² | Adjacent to electrical room |
| MV switchgear room | 15-20 m² | Near building perimeter for cable entry |
| Generator yard | 30-50 m² (outdoor) | Near MV room, fuel storage access |
| Meet-me room (MMR) | 5-10 m² | Central, accessible to all data halls |
| NOC (Network Operations Center) | 3-5 m² | Near data halls, 24/7 access |
| Staging / loading dock | 10-20 m² | Ground floor, truck access, freight elevator access |
| Heat pump plant room | 20-35 m² | Between DC and greenhouse, near CDU rooms |

### Total Building Efficiency
Gross-to-net ratio (usable IT floor vs total building area):
- Single-tenant AI factory: 55-65% efficiency
- Multi-tenant colocation: 45-55% efficiency (more corridors, metering, tenant separation)
- DEC target: 50-55% (includes heat recovery infrastructure footprint)

## 3. Hall Geometry

### Clear Height
Minimum clear height (finished floor to underside of lowest obstruction):

| Configuration | Minimum Clear Height | Preferred | Driver |
|---|---|---|---|
| DTC liquid-cooled, overhead busway | 4.0 m | 4.5 m | Busway + CDU piping + cable tray stacking |
| DTC + overhead cable management | 3.5 m | 4.0 m | Reduced busway height |
| Immersion cooling (future) | 3.0 m | 3.5 m | Tanks lower than racks |

**DEC recommendation: 4.5 m minimum clear height.** Overhead stacking order (bottom to top):
1. Rack tops at 2.0-2.2 m
2. CDU piping with drip trays at 2.5-3.0 m
3. Busway with tap-off boxes at 3.0-3.5 m
4. Cable tray (structured cabling, fiber) at 3.5-4.0 m
5. Fire detection/suppression (VESDA sampling, IG-541 nozzles) at ceiling
6. Clearance to structure underside: 0.3-0.5 m for installation

### Hall Width
Determined by column grid and rack row configuration:

**Typical Row Configuration (6.0 m grid):**
```
[Wall/CDU room] | 1.2m hot aisle | rack | 1.5m cold aisle | rack | 1.2m hot aisle | [Wall/CDU room]
                                        ← 6.0 m bay →
```

Single bay = 2 rack rows with shared cold aisle
Double bay = 4 rack rows across 12.0 m width

**DEC recommendation: 2-bay wide data halls (12.0 m internal width).**
- 4 rack rows per hall width
- CDU rooms at row ends (accessible from corridor, not from data hall)
- Each row can be independently metered for different tenants

### Hall Length
Row length determines racks per row and operational efficiency:
- Minimum useful: 18 m (8-10 racks per row + CDU space)
- Optimal: 36-48 m (16-24 racks per row)
- Maximum practical: 60 m (beyond this, pipe run pressure drop and cable length become limiting)

### Fire Compartment Size
Bbl (Besluit bouwwerken leefomgeving / Building Decree):
- Standard maximum brandcompartiment (fire compartment): 2,500 m²
- Data halls typically >2,500 m² → requires gelijkwaardigheid (equivalence) assessment
- See [fire-safety-suppression.md](fire-safety-suppression.md) for fire compartment negotiation strategy
- DEC recommendation: design halls at ~2,000-2,400 m² each to stay under 2,500 m² limit where practical

## 4. Containment Strategy

### Hot Aisle Containment (HAC) vs Cold Aisle Containment (CAC)

For AI density with liquid cooling:
- **80% of heat** removed by liquid (DTC cold plates) — goes to CDU
- **20% of heat** removed by air — residual from memory, VRMs, NVLink switches, fans
- Air cooling is supplementary, not primary → containment strategy changes

**Hot Aisle Containment (Preferred for DEC):**
- Hot aisle enclosed with doors at row ends and ceiling panels
- Hot exhaust air captured and returned to CRAH/air handler
- Cold aisle open to room → room temperature = cold supply temperature
- Advantages: room is comfortable for humans (cold), hot air contained
- For AI density: hot aisle temperature 35-45°C (higher than traditional DC due to liquid handling 80%)

**Cold Aisle Containment (Alternative):**
- Cold aisle enclosed
- Room temperature = hot return temperature
- Disadvantages: room uncomfortable, hot air escapes from every opening

**DEC Recommendation: Hot Aisle Containment**
- Personnel comfort matters for 24/7 NOC and maintenance staff
- Hot aisle temperatures higher than traditional (liquid handles most heat) but contained
- CRAH/air handlers sized only for 20% residual heat — much smaller than traditional DC
- In-row cooling units (Schneider InRow, Vertiv Liebert CRV) preferred over perimeter CRAH for AI density

### Rack Dimensions

| Parameter | Traditional 42U | AI Rack (NVIDIA reference) |
|---|---|---|
| Height | 2,000 mm (42U) | 2,000-2,200 mm (42-48U) |
| Width | 600 mm | 600 mm |
| Depth | 1,000-1,070 mm | 1,200 mm (deeper for GPU servers) |
| Weight (loaded) | 500-800 kg | 1,500-2,500 kg |
| Floor loading | 4-6 kN/m² | 12-20 kN/m² |

**DEC consideration:** 1,200 mm deep racks require:
- Wider cold aisle (1.5 m minimum for rear access) or wider hot aisle (1.2 m minimum)
- Slab-on-grade with adequate floor loading capacity (see Expert 11 Structural)
- Door swing clearance in hot aisle containment

## 5. Adjacency Matrix

### Critical Adjacencies

| Space A | Space B | Relationship | Reason |
|---|---|---|---|
| Data hall | CDU room | Direct adjacent, same level | Piping length minimizes pressure drop and thermal loss |
| CDU room | Heat pump plant | Connected by pipe corridor | Thermal chain continuity |
| Data hall | Electrical room | Adjacent, fire-separated | Short busway/cable runs |
| Electrical room | UPS/DRUPS room | Adjacent | Power chain continuity |
| UPS/DRUPS room | Generator yard | Adjacent (indoor/outdoor interface) | Fuel line, exhaust, vibration isolation |
| MV switchgear | Building perimeter | At perimeter | DSO cable entry, transformer access |
| Meet-me room | All data halls | Central | Fiber/cabling equidistant to all halls |
| Staging area | Data hall | Same level, corridor access | Equipment delivery without external weather exposure |
| Heat pump plant | Buffer tank / ATES | Adjacent | Thermal chain continuity |
| Buffer tank | Greenhouse pipe exit | Direct path | Minimize transport pipe length |

### Spaces That Must Be SEPARATED

| Space A | Space B | Minimum Separation | Reason |
|---|---|---|---|
| Ammonia heat pump room | Occupied spaces | Per PGS 13 veiligheidsafstand | Ammonia toxicity |
| Generator fuel storage | Buildings | Per PGS 28 afstandstabel | Fire/explosion risk |
| Dry coolers | Property boundary | Per Bal geluidhinder | Noise at nearest woning |
| BESS containers | Buildings | Per PGS 37-1 afstandstabel | Li-ion fire/thermal runaway |
| Data hall | Greenhouse | Fire separation distance | Different occupancy, different fire load |

## 6. Structured Cabling & Connectivity

### Fiber Infrastructure

**Intra-Building (Structured Cabling):**
- **Backbone:** OS2 single-mode fiber (9/125 µm), 24-144 fiber count per cable
- **Horizontal (to rack):** OM4 or OM5 multimode fiber for 400G/800G short-reach (SR4/SR8)
- **Connector standard:** MPO-12 or MPO-16 for 400G+ (transitioning from LC duplex)
- **Cable class:** Euroclass Cca-s1,d2,a1 minimum per Bbl brandveiligheid (CPR — Construction Products Regulation) — halogen-free, low smoke
- **Key vendors:** Corning (market leader), CommScope/SYSTIMAX, Belden, Nexans (French, strong NL presence), Prysmian (Italian, strong NL cable manufacturing)

**External Connectivity:**
- **Dark fiber:** Multiple diverse fiber entries from different carriers
- **NL peering:** AMS-IX (Amsterdam Internet Exchange) and NL-ix proximity — DEC facility should have direct peering capability
- **Meet-Me Room (MMR):** Carrier-neutral room where external fiber terminates, with cross-connect to data halls
- **Fiber path diversity:** Minimum 2 physically diverse fiber routes to facility (different streets, different cable trenches)
- **KLIC/WIBON:** Before any excavation for fiber entry, KLIC-melding (underground utility survey) mandatory

**GPU Cluster Networking (Tenant-Provided):**
- NVIDIA InfiniBand (NDR 400G, XDR 800G) or Ethernet (RoCEv2 400G/800G)
- Fat-tree or rail-optimized topology — tenant designs, landlord provides physical infrastructure
- DEC provides: structured cabling, fiber pathway, meet-me room, power — NOT the network switches/fabric
- Cable management: AI clusters use massive fiber bundles (1,000+ fibers for large GPU clusters) — allocate dedicated cable tray capacity

### Cable Tray Design

**Overhead Cable Tray Hierarchy (top to bottom):**
1. Fiber backbone (top — least weight, most sensitive)
2. Copper data cabling (if any)
3. Power cables (heaviest — bottom tray)

**Separation:** NEN 1010 requires physical separation between power and data cables — separate trays or dividers within shared tray. Maintain 150 mm minimum separation for EMC.

**Sizing:** For AI density, cable tray fill should not exceed 50% (allows future cables without re-traying). AI clusters generate exceptional fiber density — allocate 2x traditional capacity.

## 7. Environmental Control

### Air Temperature & Humidity

ASHRAE TC 9.9 Thermal Guidelines for AI density with DTC liquid cooling:
- **Recommended range (A1):** 18-27°C inlet, 20-80% RH (non-condensing)
- **Allowable range (A2):** 10-35°C inlet, 20-80% RH
- Since liquid cooling handles 80% of heat, air temperature control is less critical than traditional DC
- **DEC target:** 23-27°C room temperature (energy-efficient — no overcooling)

### Residual Air Cooling Options

| Technology | Capacity | Footprint | Suitability |
|---|---|---|---|
| In-row cooler (InRow) | 20-80 kW/unit | 300 mm rack width | Best for row-level control |
| Rear-door heat exchanger (RDHX) | 30-60 kW/rack | Replaces rack rear door | Good supplement to DTC |
| Perimeter CRAH | 50-150 kW/unit | Dedicated floor space | Only if supplementary to DTC |
| Overhead fan-coil | 20-50 kW/unit | Ceiling mounted | Space-efficient but maintenance access difficult |

**DEC recommendation:** In-row coolers (1 per 4-6 AI racks) for residual air cooling. Connected to same facility water loop as CDUs for simplicity. Schneider InRow RD and Vertiv Liebert CRV are market standards.

### Humidity Control
At AI density with liquid cooling, humidity control is less critical than traditional DC:
- No raised floor plenum → no underfloor moisture risk
- Contained hot aisle → moisture doesn't migrate freely
- NL climate: outdoor humidity 70-90% average — dehumidification rarely needed
- Humidification: rarely needed in NL (not the dry winter problem of continental climates)

## 8. Multi-Tenant Considerations

### Tenant Demarcation
For DEC's colocation model, each tenant needs:
- **Physical separation:** Cage or wall between tenant spaces (wire mesh cage for visibility/airflow, or solid wall for higher security)
- **Independent access:** Biometric/card access per tenant space without traversing other tenants
- **Metered power:** Revenue-grade metering at tenant boundary (see Expert 8)
- **Metered cooling:** Heat allocated per tenant for PUE/ERE reporting
- **Independent network:** Separate fiber pathways and cross-connects per tenant

### Hall Subdivision Options

| Approach | Flexibility | Cost | Security |
|---|---|---|---|
| Open hall, cage subdivision | High — cages can be reconfigured | Low | Moderate (visual) |
| Semi-permanent walls (metal stud) | Moderate — walls relocatable | Moderate | High |
| Permanent fire-rated walls | Low — structural modification to change | High | Very high (fire separation) |

**DEC recommendation:** Open hall with cage subdivision for Phase 1 (maximize flexibility while tenant mix stabilizes). Transition to semi-permanent walls for long-term tenants with security requirements.

### Shared Infrastructure vs Tenant Infrastructure
| Component | Shared (DEC provides) | Tenant-Specific |
|---|---|---|
| MV/LV power distribution | To tenant distribution board | From distribution board to rack |
| Cooling (facility water) | CDU and facility water loop | Rack-level liquid connections |
| Fire suppression | Building-wide system | — |
| Physical security | Perimeter, hall access | Cage-level access |
| Structured cabling | Backbone to MMR, tray infrastructure | Horizontal cabling within cage |
| Network switches | — | All networking is tenant-provided |
| Heat recovery | Aggregated from all CDUs | — |

## 9. DEC-Specific Design Considerations

### Heat Recovery Access
- CDU rooms must be accessible to DEC heat recovery operations team (not just tenant IT staff)
- Temperature sensors on CDU facility-water return are DEC instrumentation (not tenant)
- Heat pump operational data feeds DEC's heat supply SLA monitoring
- Design CDU room access as SHARED: tenant accesses CDU for IT cooling; DEC accesses CDU facility-water interface for heat recovery

### Greenhouse Interface
- Heat pipe penetration through building envelope: sealed, insulated, expansion loop
- Control system interface: BMS signal to heat pump for demand coordination
- Emergency shutdown: if greenhouse heat rejection fails, DC cooling must continue independently (dry cooler fallback)

### Noise-Sensitive Location
If DC is near greenhouse or residential area:
- Data hall walls: minimum Rw 45 dB sound insulation (masonry or insulated metal panel)
- Penetrations (pipe, cable, duct) sealed with acoustic sealant
- See [acoustic-engineering.md](acoustic-engineering.md) for detailed noise budget allocation

## Cross-References
- See [ai-factory-design.md](ai-factory-design.md) for column grid selection and redundancy topology
- See [liquid-cooling-systems.md](liquid-cooling-systems.md) for CDU placement options and piping design
- See [electrical-power-systems.md](electrical-power-systems.md) for busway routing and LV distribution
- See [power-quality-grounding.md](power-quality-grounding.md) for cable tray bonding and EMC separation
- See [civil-works-netherlands.md](civil-works-netherlands.md) for floor loading capacity and structural grid
- See [fire-safety-suppression.md](fire-safety-suppression.md) for fire compartment sizing and suppression integration
- See [acoustic-engineering.md](acoustic-engineering.md) for wall insulation and penetration sealing
- See companion skill `ai-infrastructure` for GPU cluster networking requirements and rack specifications
- See companion skill `site-development` for master plan integration and tenant commercial model
