# Carbon & ESG Compliance

## 1. Carbon Accounting for Data Centers

### GHG Protocol Framework

The GHG Protocol (WRI/WBCSD) is the global standard for corporate carbon accounting:

**Scope 1 — Direct Emissions:**
- Backup generators (diesel combustion during grid outages and testing)
- Refrigerant leaks from cooling systems (if applicable)
- Company vehicles
- For DEC: heat pump refrigerant (R717 ammonia = zero GWP; if R410A or R134a, significant GWP)
- Typical DC Scope 1: 1-5% of total emissions

**Scope 2 — Indirect Energy Emissions:**
- Purchased electricity for IT and facility loads
- This is the dominant emission source for data centers (70-90% of total)
- Two reporting methods:
  - **Location-based:** Uses average grid emission factor for NL (currently ~350-400 gCO2/kWh)
  - **Market-based:** Uses emission factor of actual procurement (PPA with GOs can be 0 gCO2/kWh)
- DEC MUST report both methods (GHG Protocol requires dual reporting)

**Scope 3 — Value Chain Emissions:**
- Upstream: embodied carbon in servers, networking equipment, building materials, construction
- Downstream: tenant operations (if DEC is a service provider)
- Business travel, employee commuting, waste
- Scope 3 is the largest category (potentially 50-80% of lifecycle emissions) but hardest to measure
- Key Scope 3 category for DC: **embodied carbon of IT equipment** (GPU manufacturing is carbon-intensive)

### DEC-Specific Carbon Accounting

**Unique considerations for DEC's model:**

1. **Heat recovery as avoided emissions:**
   - DC waste heat displaces gas combustion at greenhouse
   - Greenhouse would otherwise burn natural gas (0.056 kgCO2/MJ = 201 gCO2/kWh thermal)
   - 30 MW thermal recovery = ~950 TJ/year = ~53,000 tCO2/year avoided
   - This is NOT a Scope 1/2/3 reduction for DEC — it's an avoided emission
   - CSRD framework: report as "downstream positive impact" or under ESRS E1-7 (GHG removals and carbon credits)
   - SBTi: does not count avoided emissions toward target — but can report separately

2. **PUE and carbon intensity:**
   - PUE <1.10 achievable with liquid cooling (see dc-engineering)
   - Carbon intensity per kWh IT: depends on Scope 2 method
   - Market-based with 100% renewable PPA: near-zero Scope 2
   - Location-based: reflects NL grid average (~350-400 gCO2/kWh)

3. **Tenant allocation:**
   - Multi-tenant DC: allocate Scope 2 emissions per tenant based on power consumption
   - Tenants report DEC's electricity as THEIR Scope 2 (purchased energy at leased facility)
   - DEC must provide tenant-specific emission data (per GHG Protocol, Scope 2 guidance for leased assets)

### Carbon Accounting Methodology

**Annual Carbon Footprint Calculation (simplified):**

```
Scope 1:
  Generator fuel: liters diesel × emission factor (2.68 kgCO2/liter)
  + Refrigerant leaks: kg refrigerant × GWP (ammonia = 0)
  = Total Scope 1

Scope 2 (location-based):
  Total electricity (kWh) × NL grid factor (gCO2/kWh)
  = Total Scope 2 location-based

Scope 2 (market-based):
  PPA electricity (kWh) × 0 (if bundled GOs)
  + Grid electricity (kWh) × residual mix factor (gCO2/kWh)
  = Total Scope 2 market-based

Scope 3 (key categories):
  Cat 1: Purchased goods (embodied carbon of IT equipment, construction)
  Cat 2: Capital goods (same, for major assets)
  Cat 3: Fuel/energy not in Scope 1/2 (upstream of electricity)
  Cat 5: Waste
  Cat 6: Business travel
  Cat 13: Downstream leased assets (tenant operations, if applicable)
  = Total Scope 3

Avoided emissions (reported separately):
  Heat delivered to greenhouse (GJ) × displaced gas emission factor
  = Total avoided emissions
```

## 2. EU ETS (Emissions Trading System)

### Applicability to Data Centers

**Current status:** Most data centers are NOT directly covered by EU ETS:
- EU ETS covers installations >20 MW thermal combustion capacity
- Backup generators typically <20 MW aggregate → below threshold
- If DEC has >20 MW of generator capacity AND they run significant hours → potentially covered
- Heat pump electricity consumption: NOT a direct emission → not ETS-covered

**Indirect ETS impact:**
- Electricity price includes EU ETS carbon cost (power generators pass through ETS cost)
- NL carbon cost in power: ~€5-15/MWh embedded in wholesale price (at €50-80/tCO2 ETS price)
- This cost already exists in DEC's energy procurement — no additional action needed

### CBAM (Carbon Border Adjustment Mechanism)

**Relevance for DEC:** Minimal direct impact, but:
- CBAM covers imported steel, aluminum, cement, electricity, hydrogen, fertilizers
- Construction materials (steel) may have CBAM surcharge if imported from non-EU → marginal cost increase
- Electricity imports from non-EU: not currently relevant for NL (connected to EU neighbors)

## 3. CSRD (Corporate Sustainability Reporting Directive)

### Applicability

**CSRD applies to DEC if:**
- Large company: >250 employees, >€50M revenue, >€25M assets (2 of 3 criteria)
- Or: listed on EU regulated market (any size)
- DEC likely falls below threshold at startup → CSRD voluntary initially
- But: tenants (large tech companies) may require CSRD-like reporting from DEC as part of their Scope 3

**Timeline:**
- 2024: Large listed companies (>500 employees)
- 2025: Other large companies
- 2026: Listed SMEs (with opt-out until 2028)
- DEC should prepare now for tenant and investor demand, even if not legally required yet

### ESRS (European Sustainability Reporting Standards)

**Key standards for DEC:**

| Standard | Topic | DEC Relevance |
|---|---|---|
| ESRS E1 | Climate Change | Core: Scope 1/2/3, transition plan, temperature alignment |
| ESRS E2 | Pollution | Generator emissions, noise (see acoustic-engineering.md) |
| ESRS E3 | Water & Marine Resources | Cooling water consumption (adiabatic dry coolers) |
| ESRS E4 | Biodiversity & Ecosystems | Site impact (Natura 2000, stikstof) |
| ESRS E5 | Circular Economy | IT equipment lifecycle, construction waste |
| ESRS S1 | Own Workforce | Standard employment reporting |
| ESRS G1 | Governance | ESG governance structure |

### ESRS E1 Deep Dive — Climate Change

**Required disclosures for DEC:**
1. Transition plan for climate change mitigation
2. GHG emission targets (absolute and intensity)
3. GHG emissions (Scope 1, 2, 3 — dual reporting)
4. Internal carbon pricing (if used)
5. Anticipated financial effects of climate risks
6. Energy consumption and mix (renewable vs fossil)
7. GHG removals and mitigation projects (where to report heat recovery avoided emissions)

## 4. SBTi (Science Based Targets Initiative)

### SBTi for Data Centers

**Target-setting methodology:**
- SBTi requires companies to set emission reduction targets consistent with Paris Agreement (1.5°C or well-below 2°C)
- For data centers: Scope 2 (electricity) is dominant → target focuses on renewable electricity procurement
- SBTi FLAG (Forest, Land and Agriculture) guidance: not applicable to DC directly

**Typical DC SBTi target:**
- Scope 1+2: reduce absolute emissions 42% by 2030 (1.5°C aligned)
- Scope 3: reduce absolute emissions 25% by 2030
- Or: 100% renewable electricity by 2030 (Scope 2)

**DEC advantage:** Heat recovery is a compelling SBTi narrative element, even though avoided emissions don't count toward Scope 1/2/3 targets directly.

### RE100

**RE100 commitment:** Source 100% of electricity from renewable sources
- DEC can commit to RE100 and achieve it through PPA + GO procurement
- RE100 requires: credible (market-based) procurement, annual reporting, third-party verification
- DEC's neocloud tenants may already be RE100 members → DEC must provide compliant procurement

## 5. Carbon Credits & Offset Markets

### DEC Position on Offsets

**Hierarchy of decarbonization:**
1. **Avoid emissions** (renewable electricity, efficient design, heat recovery)
2. **Reduce emissions** (PUE improvement, efficient operations)
3. **Remove emissions** (direct air capture, biochar — emerging)
4. **Offset remaining emissions** (carbon credits — last resort)

**Carbon credit quality:**
- Voluntary Carbon Market (VCM) quality varies enormously
- Gold Standard, Verra VCS: established registries but quality varies by project
- Avoid: cheap forestry offsets with permanence and additionality questions
- Prefer: engineered removal credits (DAC, biochar) — more expensive but more credible

**DEC Strategy:** Prioritize avoidance and reduction. Use heat recovery as primary ESG differentiator. Purchase high-quality removal credits for residual emissions (Scope 1 from generators, Scope 3).

## 6. ESG Reporting for DEC

### ESG Metrics Dashboard

**Environmental:**
| Metric | Unit | Target | Source |
|---|---|---|---|
| PUE (Power Usage Effectiveness) | Ratio | <1.10 | Facility metering |
| WUE (Water Usage Effectiveness) | L/kWh | <0.5 | Water metering |
| ERF (Energy Reuse Factor) | Fraction | >0.40 | Heat meter |
| Scope 2 (market-based) | tCO2e | 0 (100% renewable) | PPA/GO documentation |
| Scope 2 (location-based) | tCO2e | Report actual | NL grid factor |
| Avoided emissions (heat recovery) | tCO2e | Report actual | Heat meter + gas displacement |
| Renewable electricity % | % | 100% | PPA/GO documentation |

**Social:**
| Metric | Unit | Notes |
|---|---|---|
| Jobs created (direct) | FTE | Construction + operations |
| Local employment % | % | NL-based workforce |
| Safety record | LTIFR | Construction and operations |
| Community engagement | Qualitative | Greenhouse partnership, local heat supply |

**Governance:**
| Metric | Unit | Notes |
|---|---|---|
| Board ESG oversight | Yes/No | Board committee or designated director |
| Climate risk assessment | TCFD-aligned | Physical and transition risks |
| Stakeholder engagement | Qualitative | Grower, municipality, neighbors |

### Investor ESG Narrative

**DEC's ESG story (unique in the data center industry):**

1. **Waste heat recovery:** Not just "efficient" — DEC's model is the only DC model that produces a positive externality (greenhouse heat supply, CO2 displacement)
2. **Circular economy:** Waste product of computing becomes input for food production
3. **100% renewable electricity:** Achievable through NL PPA market
4. **Avoided gas consumption:** Quantifiable, verifiable, material (50,000+ tCO2/year for a 40 MW DC)
5. **Local community benefit:** Heat for local growers = direct local economic value
6. **SDE++ eligibility:** Government-validated environmental contribution

**This is DEC's single strongest differentiator for ESG-conscious investors.** See site-development [project-finance-economics.md] for how to quantify and present.

## Cross-References
- See [wholesale-energy-trading.md](wholesale-energy-trading.md) for carbon cost embedded in wholesale electricity price
- See [ppa-green-certificates.md](ppa-green-certificates.md) for GO procurement, additionality assessment, Scope 2 methodology
- See [balancing-bess-revenue.md](balancing-bess-revenue.md) for BESS carbon impact
- See [energy-risk-settlement.md](energy-risk-settlement.md) for carbon price risk in risk framework
- See [grid-connection-strategy.md](grid-connection-strategy.md) for renewable integration through cable pooling
- See companion skill `netherlands-permitting` for CSRD regulatory timeline, SDE++ as environmental validation
- See companion skill `dc-engineering` for PUE/WUE/ERF measurement methodology
- See companion skill `site-development` for ESG narrative in investor presentation, financial model
