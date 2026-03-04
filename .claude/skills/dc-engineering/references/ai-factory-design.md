# AI Factory Concept Design

## 1. What Makes an AI Factory Different

### Definition
An AI factory is a purpose-built facility optimized for GPU/accelerator-dense workloads (training, fine-tuning, inference at scale) where the thermal, electrical, and physical infrastructure is designed around liquid cooling and ultra-high rack densities (40-130+ kW per rack) from day one.

### Key Differences from Traditional Data Center

| Dimension | Traditional Enterprise DC | AI Factory |
|---|---|---|
| Rack density | 5-15 kW/rack | 40-130+ kW/rack |
| Primary cooling | Air (CRAC/CRAH) | Liquid (DTC, immersion, CDU) |
| Power per rack | 1x 16A or 32A 3-phase | 4-8x 63A 3-phase |
| Floor loading | 8-12 kN/m2 | 15-25 kN/m2 |
| Network fabric | 10/25/100 GbE | 400/800G InfiniBand or RoCEv2 |
| Heat rejection | Chilled water, chillers | Warm water loop, dry coolers, heat recovery |
| Redundancy model | 2N everything | N+1 or distributed, workload-aware |
| Availability target | 99.999% (five 9s) | 99.95-99.99% (training tolerates restart) |
| Facility water temp | 7-12°C chilled water | 30-45°C warm water (enables heat recovery) |

### Design Paradigm Shift
The fundamental paradigm shift is: **AI factories are thermal management facilities that happen to contain compute**, not compute facilities that need cooling. The thermal chain drives every architectural decision.

## 2. Facility Typologies

### Single-Tenant AI Factory
- Purpose-built for one operator (neocloud, hyperscaler, or sovereign AI program)
- Optimized for specific GPU generation (e.g., NVIDIA GB200 NVL72)
- Homogeneous infrastructure: identical racks, identical power/cooling per row
- Advantages: design efficiency, operational simplicity, maximum density
- Disadvantages: inflexible if tenant requirements change, single customer risk

### Multi-Tenant AI Colocation (DEC Model)
- Purpose-built facility leased to multiple neocloud tenants
- Must accommodate varying rack densities (40-130 kW) across tenants
- Power and cooling modularity essential: some tenants want 60 kW/rack, others want 120 kW
- Revenue-grade metering at rack/row/hall level for billing
- Advantages: diversified revenue, higher utilization, shared infrastructure cost
- Disadvantages: more complex power/cooling design, metering overhead, SLA management
- DEC-specific: waste heat aggregated from all tenants feeds single thermal recovery system

### Hybrid (Phased)
- Phase 1: single anchor tenant at 50-80% capacity
- Phase 2+: additional tenants or anchor expansion
- Infrastructure designed for full build-out but deployed incrementally
- Critical: shared infrastructure (power, cooling, heat recovery) sized for full build; tenant-specific infrastructure modular

## 3. Redundancy Topology

### The AI Factory Redundancy Debate

**Traditional DC thinking:** 2N everything (dual power paths, dual cooling loops, dual UPS). Uptime Institute Tier III/IV.

**AI Factory reality:** GPU training workloads checkpoint every 5-30 minutes. If power is lost, the job restarts from last checkpoint. The cost of a 10-minute outage is 10 minutes of compute time, not data loss. This changes the redundancy calculus.

### Topology Options

| Topology | Description | Cost Premium | Use Case |
|---|---|---|---|
| 2N | Dual everything, concurrent maintenance | +80-100% infrastructure cost | Inference serving, latency-critical |
| N+1 | One spare per N units | +15-25% | Training, batch workloads |
| Distributed Redundant | Multiple smaller units, any subset sufficient | +30-50% | Mixed workloads |
| Block Redundant | Independent power blocks, shared cooling | +20-40% | Multi-tenant with varied SLA |

### DEC Recommendation
For DEC's multi-tenant AI colocation:
- **Power:** Block Redundant — independent power blocks per tenant cluster, shared MV distribution
- **Cooling:** N+1 on CDUs and dry coolers — liquid cooling has inherent thermal mass (minutes of buffer)
- **UPS:** Depends on workload mix — rotary UPS for training-dominant; static UPS only if inference SLA demands it
- **Heat recovery:** N+0 with backup boiler at greenhouse — heat recovery is not life-safety; if DC thermal system fails, greenhouse switches to backup

## 4. Column Grid: The Critical Decision

### Why Column Grid Matters
The structural column grid determines:
- Rack row length and number of racks per row
- CDU room placement and pipe routing
- Cable tray routing and bend radii
- Electrical busway/cable runs
- Fire compartment possibilities
- Future flexibility

### Grid Options

| Grid Pitch | Pros | Cons | Best For |
|---|---|---|---|
| 3.6 m x 3.6 m | Minimal structural cost | Cramped rows, limits rack depth, poor for 1200mm racks | Legacy enterprise, office conversion |
| 4.8 m x 9.6 m | Good compromise, fits 42U racks with hot aisle containment | MEP coordination tight | Medium-density (20-40 kW/rack) |
| 6.0 m x 12.0 m | Optimal for AI density, ample MEP space, accommodates 1200mm deep racks with rear-door access | Higher structural cost | AI factory, 40+ kW/rack, liquid cooled |
| 7.2 m x 14.4 m | Maximum flexibility, easy maintenance access | Significantly higher structural cost, large span beams | Hyperscale, 100+ kW/rack |

### Opinionated View
For DEC's 40-100 MW AI factory at 60-130 kW/rack: **6.0 m x 12.0 m is the optimal grid**. 3.6 m is undersized; 7.2 m is overbuilt for the scale. The 6.0 m bay accommodates two rack rows with 1.2 m hot aisle, rear maintenance access, and overhead busway/CDU piping routing. The 12.0 m span allows CDU rooms at row ends without splitting the data hall.

## 5. Slab-on-Grade vs Raised Floor

### The Verdict
Raised floor is dead for AI density. Period.

**Why:**
- Floor loading: raised floor stringers rated for 12-15 kN/m2; AI racks need 15-25 kN/m2
- Liquid cooling: coolant piping under raised floor creates leak containment nightmare
- Airflow: at 80+ kW/rack with liquid cooling, residual air cooling is 10-20% of total heat — doesn't justify underfloor plenum
- Cost: raised floor adds €100-150/m2 for no benefit
- Maintenance: overhead services (cable tray, busway, CDU piping) are accessible from below via mobile platforms; underfloor services require tile pulling

**What replaces it:**
- Slab-on-grade with post-tensioned or reinforced concrete (structural engineer specifies)
- Overhead cable tray (structured cabling, fiber)
- Overhead or wall-mounted busway (power)
- CDU piping: overhead with drip trays and leak detection, OR below-slab in trenches (for heat recovery main lines)

## 6. Thermal Architecture

### Temperature Cascade: The DEC Design Principle
Every component in the thermal chain is designed to MAXIMIZE return water temperature from the facility, because higher temperatures improve downstream heat pump COP.

```
GPU junction (85-95°C)
    → Cold plate (DTC coolant supply 30-35°C, return 40-50°C)
        → CDU (facility water supply 25-30°C, return 35-45°C)
            → Heat pump evaporator (source 35-45°C)
                → Heat pump condenser (output 65-80°C)
                    → Buffer tank / ATES
                        → Greenhouse delivery (40-80°C depending on crop)
                        → OR warmtenet injection (70-90°C)
```

### Design Parameters

| Parameter | Typical Range | DEC Target | Why |
|---|---|---|---|
| CDU facility water supply | 25-35°C | 30-32°C | Higher = better heat pump COP; limited by GPU thermal headroom |
| CDU facility water return | 35-50°C | 42-45°C | Higher = less heat pump work needed |
| Residual air cooling | 10-30% of total heat | 15-20% | Cannot be fully eliminated; dry coolers reject this portion |
| Heat pump COP at design | 3.0-5.0 | 3.5-4.0 | Conservative target for 42→70°C lift |
| Greenhouse delivery | 40-90°C | 55-70°C | Crop-dependent; tomaat/paprika need less than sierteelt |

## 7. NEN-EN 50600 Application

### Relevant Parts
- **50600-1:** General concepts and terminology
- **50600-2-1:** Building construction (space, structure, fire)
- **50600-2-2:** Power distribution
- **50600-2-3:** Environmental control (thermal, humidity)
- **50600-2-4:** Telecommunications cabling
- **50600-2-5:** Security systems
- **50600-2-6:** Management and operation
- **50600-99-1 through 99-3:** KPIs (PUE, REF, WUE)

### Availability Classes
NEN-EN 50600 defines 4 availability classes (roughly analogous to Uptime Tier I-IV):
- **Class 1:** Basic site infrastructure — single path, no redundancy
- **Class 2:** Redundant site infrastructure — N+1 components
- **Class 3:** Concurrently maintainable — maintenance without downtime
- **Class 4:** Fault tolerant — automatic failover

### DEC Targeting
For AI colocation with mixed training/inference workloads:
- **Power:** Class 3 (concurrently maintainable) for shared infrastructure; Class 2 (N+1) for tenant-specific
- **Cooling:** Class 2 (N+1) — liquid cooling's thermal mass provides inherent ride-through
- **This is NOT a cost-cutting choice** — it reflects the workload reality: AI training tolerates restart; 2N cooling for training workloads is waste

## 8. Key Reference Standards

| Standard | Scope |
|---|---|
| NEN-EN 50600 series | European DC infrastructure standard |
| ASHRAE TC 9.9 | Thermal guidelines for data processing environments |
| TIA-942-B | Telecommunications infrastructure for data centers |
| Uptime Institute Tier Standard | Availability classification |
| IEEE 3006 series | Power systems reliability |
| FM Global DS 5-32 | Data center fire protection |
| ASHRAE Guideline 36 | High-performance HVAC sequences (adapted for DC) |

## Cross-References
- See [liquid-cooling-systems.md](liquid-cooling-systems.md) for CDU and cooling technology detail
- See [data-hall-design.md](data-hall-design.md) for space programming and layout
- See [electrical-power-systems.md](electrical-power-systems.md) for power architecture
- See companion skill `ai-infrastructure` for GPU thermal profiles and workload characteristics
