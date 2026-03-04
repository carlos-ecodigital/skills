# Grid Connection & Network Tariff Strategy

## 1. Dutch Grid Connection Landscape

### Transportschaarste Crisis

The Netherlands faces severe grid congestion (transportschaarste), the single biggest infrastructure challenge for data center development:

**Current situation:**
- 10,000+ businesses on waiting lists for new or expanded grid connections
- Average wait time: 3-7 years for connections >10 MVA in congested areas
- Most of Noord-Holland, Zuid-Holland, Noord-Brabant, and Gelderland severely congested
- TenneT and regional DSOs (Liander, Stedin, Enexis) cannot expand grid fast enough

**Congestion map (simplified):**
| Region | Congestion Level | Wait Time | DEC Implication |
|---|---|---|---|
| Amsterdam/Haarlemmermeer | Extreme | 5-10+ years | Effectively impossible for new large DC |
| Zuid-Holland (Westland) | Severe-Moderate | 3-7 years | Greenhouse area — cable pooling opportunity |
| Noord-Holland (north) | Moderate | 2-5 years | More feasible, fewer growers |
| Flevoland | Moderate-Low | 2-4 years | Agricultural land, good grid potential |
| Groningen | Low-Moderate | 1-3 years | Good grid capacity, earthquake risk |
| Zeeland | Low | 1-2 years | Borssele nuclear/wind, available capacity |

### Grid Connection Process

**Step-by-step for large connections (>10 MVA):**

| Step | Actor | Duration | Key Activity |
|---|---|---|---|
| 1. Preliminary inquiry | DEC → DSO/TenneT | 2-4 weeks | Capacity check at proposed location |
| 2. Connection request | DEC → netbeheerder | 4-8 weeks | Formal application (aanvraag aansluiting) |
| 3. Offer (offerte) | Netbeheerder → DEC | 8-18 weeks | Connection offer with cost estimate and timeline |
| 4. Acceptance | DEC → netbeheerder | 4 weeks | Sign connection agreement (aansluitovereenkomst) |
| 5. Design & engineering | Netbeheerder | 6-18 months | Grid reinforcement design (if needed) |
| 6. Construction | Netbeheerder + contractors | 12-36 months | Build substation, lay cables, install transformer |
| 7. Commissioning | Netbeheerder + DEC | 4-8 weeks | Testing, metering, energization |
| **Total** | | **2-5 years** | Longer in congested areas |

### Connection Voltage Levels

| Voltage | Typical Capacity | Netbeheerder | DEC Relevance |
|---|---|---|---|
| 150 kV (EHS/Extranet Hoogspanning) | 50-200+ MVA | TenneT | Full-scale facility (>50 MW IT) |
| 50 kV (HS/Hoogspanning) | 10-80 MVA | Regional DSO | Medium facility (10-50 MW IT) |
| 10-20 kV (MS/Middenspanning) | 1-10 MVA | Regional DSO | Small facility or Phase 1 |

**DEC first facility (40 MW IT + facility load ≈ 50 MVA):** Likely 50 kV or 150 kV connection depending on location and available infrastructure.

## 2. Grid Connection Strategy for DEC

### Phased Connection Strategy

**The biggest mistake data center developers make:** Applying for maximum capacity (100 MW+) upfront.

**Phased approach (recommended for DEC):**

```
Phase 1: 20-30 MVA connection (flexible terms)
  ├── IT load: 15-20 MW
  ├── Timeline: achievable in 1-3 years (smaller = faster)
  └── Revenue: start earning while waiting for expansion

Phase 2: Expansion to 50-80 MVA
  ├── IT load: 35-50 MW
  ├── Application submitted during Phase 1 construction
  └── Available by Year 3-5

Phase 3: Full capacity 100+ MVA
  ├── IT load: 80-100+ MW
  ├── Subject to grid reinforcement completion
  └── Long-term (Year 5+)
```

**Advantages of phased approach:**
1. **Faster first connection:** Smaller capacity = shorter queue, less grid reinforcement needed
2. **Revenue during wait:** Generate revenue from Phase 1 while Phase 2 is being built
3. **Flexibility:** Adjust Phase 2/3 capacity based on actual demand and grid conditions
4. **Lower upfront cost:** Smaller connection = lower connection fee

### Flexible Connection Contracts (Niet-Vast Transportrecht)

**What it means:** Accept connection with non-firm transport capacity — the netbeheerder can curtail you during congestion hours.

**How it works:**
- Standard connection: firm (vast) transport → guaranteed full capacity 24/7
- Flexible connection: non-firm (niet-vast) transport → full capacity most of the time, but netbeheerder can reduce your capacity during grid stress (typically <200 hours/year)

**Why this works for DEC:**
- AI training can tolerate brief reductions (reduce non-critical jobs for 1-2 hours)
- BESS can absorb the curtailment (discharge from BESS during grid stress)
- The capacity reduction is typically 10-30%, not full shutdown
- In exchange: faster connection (skip the queue for firm capacity) and lower transport tariff

**Revenue from congestion management:**
- If DEC voluntarily reduces load during congestion → paid by netbeheerder via GOPACS
- Revenue: €50-200/MWh during congestion hours × volume × hours
- Turns a constraint into a revenue stream

### Congestion Management Participation

**GOPACS platform:**
- DSOs and TenneT post congestion management requests (redispatch)
- Flexible consumers (including DCs with BESS) bid to increase/decrease consumption
- Settlement at bid price × volume
- Growing rapidly: GOPACS transactions up 5× since 2022

**DEC can participate by:**
1. Reducing DC load during local congestion (demand response)
2. Discharging BESS during congestion (inject stored energy)
3. Increasing consumption during negative congestion (absorb excess generation)
4. Revenue: highly site-dependent, €50K-500K/year for 40 MW site in congested area

## 3. MLOEA (Multi-Supplier Single Connection)

### What is MLOEA?

MLOEA (Meervoudige Leveranciers Overeenkomst Eén Aansluiting / Multi-Supplier Agreement Single Connection) allows multiple parties to share a single grid connection, each with their own energy supplier.

### MLOEA Structure

```
Single Grid Connection (50 MVA)
  │
  ├── DEC Facility Load (5 MW) ──→ Supplier A
  │
  ├── Tenant 1 (20 MW) ──→ Supplier B (tenant's choice)
  │
  ├── Tenant 2 (15 MW) ──→ Supplier C (tenant's choice)
  │
  ├── BESS (10 MW/20 MWh) ──→ DEC/aggregator
  │
  └── Solar PV (5 MWp) ──→ DEC/PPA counterparty
```

### Energiewet 2026 and MLOEA Expansion

**Current (pre-Energiewet):**
- MLOEA possible but limited administrative support
- Requires agreement of all parties + netbeheerder
- Complex metering and settlement

**Under Energiewet 2026:**
- Cable pooling explicitly enabled and expanded
- MLOEA administrative burden reduced
- More flexible arrangements for shared connections
- Encourages efficient use of scarce grid capacity

### MLOEA Commercial Structuring

**Key commercial questions:**

| Issue | Options | DEC Recommendation |
|---|---|---|
| **Capacity allocation** | Fixed per party vs dynamic sharing | Dynamic sharing (maximize utilization) |
| **Priority during curtailment** | Equal reduction vs priority system | Priority by contract (DEC facility = highest priority) |
| **Cost allocation** | Per allocated capacity vs per actual use | Hybrid (fixed component + variable) |
| **Expansion rights** | Pro-rata vs first-come | Define in MLOEA agreement upfront |
| **Exit provisions** | Penalty vs notice period | 12-month notice + capacity reallocation |

## 4. Cable Pooling

### Cable Pooling Concept

Cable pooling = sharing a single grid connection between generation (solar PV, wind) and consumption (DC, BESS) to net production against consumption behind the meter.

```
Behind-the-Meter Cable Pooling:

Solar PV (5 MWp) ──┐
                    ├── Shared Connection (50 MVA) ──→ Grid
BESS (10 MW) ──────┤
                    │
Data Center (40 MW)─┘

When solar produces 5 MW and DC consumes 40 MW:
  → Grid supplies 35 MW (40 - 5 = 35 MW net import)
  → 5 MW never touches the grid → no transporttarief on those 5 MW

When solar produces 5 MW and DC consumes 30 MW + BESS charges 5 MW:
  → Grid supplies 30 MW
  → 10 MW consumed behind the meter → no grid charges on those 10 MW
```

### Cable Pooling Economics

**Annual savings from cable pooling (40 MW DC + 5 MWp solar + 10 MW BESS):**

| Savings Source | Calculation | Annual Value |
|---|---|---|
| Avoided transporttarief on solar self-consumption | 5 MWp × 1,050 kWh/kWp × ~€25/MWh transport | ~€131K |
| Avoided energiebelasting on self-consumption | 5.25 GWh × €0.05/kWh (top bracket) | ~€3K (minimal at top bracket) |
| Peak shaving via BESS | Reduce peak demand by 5 MW × transporttarief saving | ~€50-150K |
| Reduced connection capacity needed | 50 MW instead of 55 MW → lower connection fee | One-time saving |
| **Total annual savings** | | **€180-280K** |

**Cable pooling payback:**
- Additional investment: solar PV (€5-6M for 5 MWp), BESS (€8-12M for 10 MW/20 MWh)
- BESS has additional revenue from FCR/aFRR (see balancing-bess-revenue.md)
- Solar has PPA/SDE++ revenue
- Cable pooling savings are additional on top of standalone business cases

### Cable Pooling Regulatory Requirements

| Requirement | Status | Notes |
|---|---|---|
| Same grid connection point | Required | All assets behind same allocatiepunt |
| MLOEA agreement | Required if multiple suppliers | See MLOEA section above |
| Energiewet 2026 eligibility | Expanded (effective Jan 2026) | Broader definitions, more flexibility |
| SDE++ compatibility | Must verify | Solar with SDE++ behind cable pool may have special rules |
| ACM approval | Not required (standard MLOEA) | But netbeheerder must accept configuration |

## 5. Network Tariff Optimization

### Dutch Network Tariff Structure

**Transporttarief (transport tariff) components:**

| Component | Basis | Typical Cost (50 kV connection) | Optimization Lever |
|---|---|---|---|
| **Aansluitdienst** (connection service) | Fixed per connection | €50-200K/year | Minimize connection capacity |
| **Transportdienst** (transport service) | kW contracted + kWh consumed | €15-30/kW/year + €3-8/MWh | Peak shaving, load factor |
| **Systeemdienst** (system service) | kWh consumed | €1-3/MWh | Cannot optimize |
| **Meetdienst** (metering service) | Per meter | €500-2,000/year | Minimize meter count |

### Peak Demand Management

**Transporttarief is based partly on peak demand (kW):**
- Measured as highest average demand in a 15-minute period during the month
- Even one 15-minute peak in the month sets the tariff for that month
- BESS peak shaving: cap peak demand by discharging BESS during anticipated peaks

**Example:**
- Without BESS: peak demand 50 MW → transporttarief based on 50 MW
- With 10 MW BESS peak shaving: peak demand 40 MW → transporttarief based on 40 MW
- Saving: 10 MW × €20/kW/year = €200K/year

### Aansluitcategorie Selection

The connection category (aansluitcategorie) determines tariff structure:
- Higher voltage = lower per-kWh tariff but higher fixed cost
- For 40-50 MW: 50 kV connection is typically optimal
- For >80 MW: 150 kV connection may be more cost-effective
- Analyze total cost (fixed + variable) at expected load profile

## 6. Grid Connection as Site Selection Criterion

### Grid Connection Scoring Matrix

When evaluating DEC sites, grid connection is typically the #1 weighted criterion:

| Factor | Weight | Scoring | Data Source |
|---|---|---|---|
| Available capacity at nearest substation | 25% | MVA available, congestion level | TenneT/DSO capacity map |
| Connection timeline | 25% | Years to energization | DSO preliminary inquiry response |
| Connection cost | 15% | €M for connection | DSO offer (offerte) |
| Voltage level | 10% | 150 kV / 50 kV / 10 kV | Based on available infrastructure |
| Grid reinforcement required | 10% | None / minor / major | DSO assessment |
| Fiber connectivity | 10% | Carrier proximity, AMS-IX distance | Carrier availability |
| Congestion management opportunity | 5% | Revenue potential from GOPACS | Congestion level analysis |

**Fatal flaw:** If no grid capacity is available and timeline exceeds 5 years → site rejected regardless of other criteria.

### Grid Connection Cost Estimate

| Connection Type | Typical Cost Range | Who Pays |
|---|---|---|
| 150 kV connection (new substation) | €5-20M | Shared (DEC + netbeheerder) |
| 50 kV connection (from existing substation) | €1-5M | DEC (aansluitbijdrage) |
| 10 kV connection (from existing transformer) | €100-500K | DEC |
| Grid reinforcement (if triggered by DEC) | €0-50M+ | Socialized (all grid users) or DEC contribution |

**Key principle:** Under Dutch law, grid reinforcement costs are socialized across all grid users (not charged to the individual connectee). However, the connection itself (kabel/leiding to your site) is at DEC's cost.

**DEC advantage with cable pooling:** If DEC's solar PV + BESS reduce net grid demand, the required connection capacity is lower → lower connection cost.

## Cross-References
- See [wholesale-energy-trading.md](wholesale-energy-trading.md) for grid connection capacity impact on procurement volume
- See [ppa-green-certificates.md](ppa-green-certificates.md) for cable pooling with co-located solar PV and PPA
- See [balancing-bess-revenue.md](balancing-bess-revenue.md) for BESS congestion management and peak shaving revenue
- See [energy-risk-settlement.md](energy-risk-settlement.md) for grid connection delay risk and tariff change risk
- See [carbon-esg-compliance.md](carbon-esg-compliance.md) for cable pooling renewable integration for ESG
- See companion skill `netherlands-permitting`:
  - [grid-connection.md] for Energiewet regulatory procedure, MLOEA permitting
  - Energie & Flexibiliteit expert for regulatory/procedural aspects (this file covers commercial/strategic)
- See companion skill `dc-engineering`:
  - [electrical-power-systems.md] for MV/LV design downstream of grid connection point
- See companion skill `site-development`:
  - [site-selection-methodology.md] for grid connection in site evaluation scoring
  - [project-finance-economics.md] for grid connection cost in financial model
