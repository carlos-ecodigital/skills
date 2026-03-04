# Energy Procurement & Market Strategy Checklist — DEC Facility

## Purpose
Comprehensive checklist for energy procurement, grid connection, BESS revenue optimization, taxation, and ESG compliance for a DEC AI data center colocation facility with greenhouse heat integration in the Netherlands.

---

## A. Load Profile Characterization

### Facility Load Estimate

| Parameter | Value | Source |
|---|---|---|
| IT Load (contracted) | ___ MW | Tenant agreements |
| Facility Load (cooling, heat pumps, BMS) | ___ MW (~15-25% of IT) | dc-engineering estimate |
| **Total Facility Demand** | ___ MW | Sum |
| Annual Consumption Estimate | ___ GWh | Total MW × 8,760 hrs × load factor |
| Expected Load Factor | ___% (training: 90-95%, inference: 50-70%, mixed: 75-85%) | ai-infrastructure workload mix |

### Load Profile Characteristics

- [ ] Workload type confirmed: [ ] Training-dominant [ ] Inference-dominant [ ] Mixed
- [ ] Hourly load profile modeled (8,760 hours, 15-min resolution preferred)
- [ ] Ramp rate assessed (how fast does load change? minutes/hours/days)
- [ ] Seasonal variation quantified (summer vs winter, holiday periods)
- [ ] Phase-in schedule defined (Month 1: ___ MW, Month 6: ___ MW, Month 12: ___ MW, Year 2: ___ MW)
- [ ] Greenhouse heat pump load profiled separately (seasonal: high winter, low summer)

**DEC Cross-Reference:** → ai-infrastructure [training-workloads.md] for power profiles, dc-engineering [heat-pumps-waste-heat.md] for heat pump load

---

## B. Grid Connection Strategy

### Pre-Application Assessment

- [ ] Target location identified and grid congestion level checked (TenneT/DSO capacity map)
- [ ] Nearest substation identified with available capacity (MVA)
- [ ] Connection voltage level determined: [ ] 150 kV (TenneT) [ ] 50 kV (DSO) [ ] 10-20 kV (DSO)
- [ ] Regional DSO identified: [ ] Liander [ ] Stedin [ ] Enexis [ ] Westland Infra [ ] Other: ___
- [ ] Preliminary inquiry (vooronderzoek) submitted to netbeheerder
- [ ] Congestion level confirmed: [ ] None [ ] Low [ ] Moderate [ ] Severe [ ] Extreme
- [ ] Estimated connection timeline received: ___ years

### Phased Connection Strategy

| Phase | Capacity (MVA) | IT Load (MW) | Target Date | Status |
|---|---|---|---|---|
| Phase 1 | ___ | ___ | ___ | [ ] Applied [ ] Offered [ ] Accepted [ ] Under construction |
| Phase 2 | ___ | ___ | ___ | [ ] Applied [ ] Offered [ ] Accepted [ ] Under construction |
| Phase 3 | ___ | ___ | ___ | [ ] Applied [ ] Offered [ ] Accepted [ ] Under construction |

- [ ] Phase 1 sized for achievability (smaller = faster, target 1-3 years)
- [ ] Phase 2 application submitted during Phase 1 construction
- [ ] Expansion rights preserved in site selection / land agreement

### Flexible Connection Assessment

- [ ] Niet-vast transportrecht (non-firm transport capacity) evaluated
- [ ] Maximum curtailment hours acceptable: ___ hours/year
- [ ] Curtailment impact on tenants assessed (training can tolerate brief reductions)
- [ ] BESS can absorb curtailment: [ ] Yes (___MW/___MWh) [ ] No [ ] Partially
- [ ] Financial benefit of flexible vs firm connection quantified: €___ /year tariff saving + ___ years faster
- [ ] GOPACS participation assessed for congestion management revenue: €___K/year estimated

### MLOEA (Multi-Supplier Single Connection)

- [ ] MLOEA needed: [ ] Yes (multiple tenants/suppliers) [ ] No (single entity)
- [ ] MLOEA parties identified: DEC facility + ___ tenants + BESS + Solar PV
- [ ] Capacity allocation model defined: [ ] Fixed [ ] Dynamic sharing [ ] Hybrid
- [ ] Priority during curtailment defined (DEC facility = highest priority)
- [ ] Cost allocation agreed: [ ] Per allocated capacity [ ] Per actual use [ ] Hybrid
- [ ] MLOEA agreement drafted and submitted to netbeheerder

### Cable Pooling

- [ ] Co-located assets identified: [ ] Solar PV (___MWp) [ ] BESS (___MW/___MWh) [ ] Other
- [ ] All assets behind same allocatiepunt (grid connection point): [ ] Yes [ ] No
- [ ] Cable pooling savings estimated: €___K/year (avoided transporttarief, peak shaving)
- [ ] SDE++ compatibility confirmed for solar PV in cable pool configuration
- [ ] Energiewet 2026 expanded eligibility confirmed for configuration

### Connection Cost

| Item | Estimated Cost | Status |
|---|---|---|
| Connection fee (aansluitbijdrage) | €___M | [ ] Quoted [ ] Paid |
| Substation contribution (if new) | €___M | [ ] Quoted [ ] Paid |
| Annual transport tariff (transporttarief) | €___K/year | [ ] Estimated |
| Annual connection service (aansluitdienst) | €___K/year | [ ] Estimated |

**DEC Cross-Reference:** → energy-markets [grid-connection-strategy.md] for full strategy, netherlands-permitting [grid-connection.md] for regulatory procedure

---

## C. Energy Procurement Strategy

### Hedge Book Design

| Layer | Instrument | Volume (%) | Duration | Status |
|---|---|---|---|---|
| Layer 1 | PPA (physical/sleeved) | 20-40% | 10-12 years | [ ] In negotiation [ ] Signed |
| Layer 2 | Medium-term futures (ICE Endex) | 30-50% | 1-3 years | [ ] Executed |
| Layer 3 | Short-term forwards (EPEX/OTC) | 10-20% | 1-12 months | [ ] Ongoing |
| Layer 4 | Spot/imbalance | 0-10% | Real-time | [ ] BRP manages |
| **Total** | | **100%** | | |

### PPA Procurement Process

- [ ] PPA strategy defined: [ ] Physical (bundled GOs) [ ] Virtual (CfD) [ ] Sleeved [ ] Mix
- [ ] Target volume: ___ GWh/year (___ % of total consumption)
- [ ] Target strike price range: €___-___/MWh
- [ ] RFP issued to ___ counterparties
- [ ] Indicative pricing received from ___ counterparties
- [ ] Short-list: ___ counterparties in detailed negotiation
- [ ] Profile risk management approach: [ ] Baseload conversion [ ] Wind+Solar portfolio [ ] BESS [ ] Accept residual
- [ ] GO treatment confirmed: [ ] Bundled (strongest ESG) [ ] Unbundled [ ] Separate procurement
- [ ] Credit support arrangement: [ ] Parent guarantee [ ] Letter of credit [ ] Cash margin
- [ ] Contract framework: [ ] EFET [ ] ISDA [ ] Custom
- [ ] PPA signed: [ ] Yes [ ] No — target date: ___

### PPA Key Terms Checklist

| Term | DEC Position | Agreed Value |
|---|---|---|
| Strike price | €___/MWh | |
| Tenor | 10-12 years | |
| Volume | ___ GWh/year | |
| Profile | [ ] As-produced [ ] Baseload-shaped | |
| Settlement | [ ] Physical [ ] Financial CfD [ ] Sleeved | |
| Floor/cap | [ ] None [ ] Floor: €___ / Cap: €___ | |
| GO treatment | [ ] Bundled [ ] Separate | |
| Negative price risk | [ ] Generator bears [ ] Shared below €___/MWh | |
| Change of law | [ ] Shared [ ] Specific carve-outs | |
| Termination | Mark-to-market settlement | |

### BRP (Balans Responsible Party / Programmaverantwoordelijke) Selection

- [ ] BRP model selected: [ ] Utility BRP [ ] Independent BRP [ ] Own BRP license [ ] Own + trading desk
- [ ] BRP candidates evaluated: ___
- [ ] Imbalance optimization strategy agreed with BRP
- [ ] E-program nomination process defined
- [ ] Settlement and reporting cadence agreed (monthly reconciliation)
- [ ] BRP agreement signed: [ ] Yes [ ] No

**DEC Cross-Reference:** → energy-markets [wholesale-energy-trading.md] for hedge book, [ppa-green-certificates.md] for PPA structuring

---

## D. BESS Revenue Optimization

### BESS Configuration

| Parameter | Value |
|---|---|
| BESS capacity | ___ MW / ___ MWh |
| Chemistry | [ ] LFP (recommended) [ ] NMC [ ] Other |
| Configuration | [ ] Behind-the-meter (cable pooling) [ ] Front-of-meter [ ] Hybrid |
| Supplier/platform | [ ] Tesla Autobidder [ ] Wärtsilä GEMS [ ] Fluence IQ [ ] Other |
| Expected cycle life | ___ cycles (LFP: 6,000-8,000) |

### Revenue Stack

| Revenue Stream | Priority | Estimated Revenue | Status |
|---|---|---|---|
| FCR (frequency containment) | 1 | €___K/year | [ ] Prequalified [ ] Active |
| aFRR (automatic frequency restoration) | 2 | €___K/year | [ ] Prequalified [ ] Active |
| Day-ahead arbitrage | 3 | €___K/year | [ ] Active |
| Imbalance optimization | 4 | €___K/year | [ ] Active |
| Congestion management (GOPACS) | 5 | €___K/year | [ ] Registered [ ] Active |
| Peak shaving (transporttarief reduction) | 6 | €___K/year | [ ] Active |
| PPA profile management | 7 | €___K/year | [ ] Active |
| **Total BESS revenue** | | **€___K/year** | |

### BESS Prequalification

- [ ] TenneT FCR prequalification test passed
- [ ] TenneT aFRR prequalification completed
- [ ] GOPACS registration completed
- [ ] BESS management platform operational
- [ ] Revenue optimization algorithm tuned

### Data Center Demand Response

- [ ] Flexible load identified: ___ MW from ___ MW total (___ %)
- [ ] Flexibility sources: [ ] Training job scheduling [ ] GPU clock throttling [ ] Cooling pre-cooling [ ] BESS [ ] Heat pump shifting
- [ ] aFRR/mFRR demand response participation evaluated
- [ ] GOPACS demand response registration
- [ ] Aggregator selected (if not self-managing): ___
- [ ] Estimated demand response revenue: €___K/year

**DEC Cross-Reference:** → energy-markets [balancing-bess-revenue.md] for revenue stacking, dc-engineering [heat-recovery-integration.md] for thermal storage

---

## E. Energy Taxation & Metering

### Energiebelasting (EB) & ODE Optimization

- [ ] Total facility consumption estimated: ___ GWh/year
- [ ] EB bracket identified: [ ] >10 GWh (laagste tarief, ~€0.05ct/kWh) [ ] Other
- [ ] ODE bracket identified: [ ] >10 GWh (laagste tarief) [ ] Other
- [ ] Total EB + ODE estimated: €___K/year

### Metering Architecture

- [ ] Metering option selected:
  - [ ] Option 1: Single connection, DEC as leverancier (lowest EB/ODE, requires leveranciersvergunning)
  - [ ] Option 2: Separate connections per tenant (highest EB/ODE but simplest)
  - [ ] Option 3: MLOEA with separate allocatiepunten (recommended for multi-tenant, no leveranciersvergunning)
- [ ] Estimated annual saving from optimal structuring vs worst case: €___K/year
- [ ] Revenue-grade metering (MID Class 0.5S) specified for all allocatiepunten
- [ ] Sub-metering for tenant billing: [ ] Per rack [ ] Per cage [ ] Per data hall
- [ ] 15-minute interval metering confirmed (ACM Meetcode requirement)
- [ ] Metering data collection system (MDMS) specified
- [ ] Settlement process documented (monthly reconciliation with netbeheerder)

### BTW (VAT) Treatment

- [ ] Electricity supply BTW rate confirmed (21% standard)
- [ ] Heat supply BTW rate confirmed (9% laag tarief for warmtelevering to greenhouse)
- [ ] BTW registration and filing process established
- [ ] Reverse charge mechanism for cross-border energy purchases (if applicable)

**DEC Cross-Reference:** → energy-markets [energy-risk-settlement.md] for tax optimization, netherlands-permitting for regulatory requirements

---

## F. Carbon & ESG Compliance

### Carbon Accounting Setup

- [ ] GHG Protocol reporting boundary defined (operational control / financial control)
- [ ] Scope 1 sources identified: [ ] Backup generators [ ] Refrigerant [ ] Vehicles
- [ ] Scope 2 methodology: [ ] Location-based + Market-based (both required by GHG Protocol)
- [ ] Scope 2 emission factor: location-based ___gCO2/kWh (NL grid), market-based ___gCO2/kWh (PPA/GO)
- [ ] Scope 3 categories assessed: [ ] Embodied carbon (IT equipment) [ ] Construction [ ] Business travel

### Green Certificates (GOs)

- [ ] GO procurement aligned with PPA strategy
- [ ] Additionality level: [ ] New-build PPA (strongest) [ ] Existing project PPA [ ] Bundled GOs [ ] Unbundled GOs
- [ ] CertiQ account opened for GO registration
- [ ] Annual GO volume matches or exceeds consumption: ___ GWh GOs vs ___ GWh consumption
- [ ] RE100 compliance: GOs from same market as consumption (NL): [ ] Yes [ ] N/A
- [ ] 24/7 clean energy hourly matching assessed: [ ] Not yet [ ] Target ___% hourly match

### Heat Recovery ESG Value

- [ ] Heat recovery volume estimated: ___ MW thermal, ___ GWh/year
- [ ] Avoided emissions calculated: ___ tCO2/year (at NL gas emission factor ~56.6 kgCO2/GJ)
- [ ] Reporting methodology: [ ] ESRS E1-7 avoided emissions [ ] Separate section (NOT counted toward SBTi target)
- [ ] ERF (Energy Reuse Factor) calculated: ___ (target <0.70 for strong ESG story)
- [ ] PUE calculated including heat recovery credit: ___

### CSRD / ESRS Readiness

- [ ] CSRD applicability assessed: [ ] In scope (large company) [ ] Below threshold (SME) [ ] Voluntary reporting
- [ ] ESRS E1 (Climate) reporting framework prepared
- [ ] Double materiality assessment scheduled: [ ] Yes [ ] N/A
- [ ] Third-party verification plan: [ ] Limited assurance [ ] Reasonable assurance [ ] Not yet

### SBTi Alignment

- [ ] SBTi applicability assessed (1.5°C or well-below 2°C pathway)
- [ ] Near-term target: 42% Scope 1+2 reduction by 2030 (from base year ___)
- [ ] Scope 3 screening completed for material categories
- [ ] FLAG sector guidance reviewed (if land-use relevant through greenhouse)

**DEC Cross-Reference:** → energy-markets [carbon-esg-compliance.md] for methodology, [ppa-green-certificates.md] for GO strategy

---

## G. Risk Management

### Energy Risk Register

| Risk | Current Exposure | Mitigation | Residual Risk | Owner |
|---|---|---|---|---|
| Market price risk (unhedged volume) | €___M | Hedge book layers 1-3 | €___M | Trading Expert |
| Volume risk (utilization variance) | €___M | Flexible contracts, tolerance bands | €___M | Risk Expert |
| PPA profile risk | €___M | Baseload conversion, BESS | €___M | PPA Expert |
| Counterparty credit risk | €___M | Credit limits, diversification | €___M | Risk Expert |
| Regulatory risk (EB/ODE changes) | €___M | Change-of-law clauses, monitoring | €___M | Risk Expert |
| Grid connection delay risk | €___M | Phased approach, flexible contract | €___M | Grid Expert |
| BESS revenue risk | €___M | Revenue diversification, stacking | €___M | BESS Expert |
| Carbon price risk | €___M | Monitor, position as advantage | €___M | Carbon Expert |

### Hedging Policy

| Time Horizon | Minimum Hedge | Maximum Hedge | Instruments |
|---|---|---|---|
| Year 3+ | 20% | 50% | PPA, long-term futures |
| Year 2 | 40% | 70% | Futures, forwards |
| Year 1 | 60% | 90% | Forwards, shaped products |
| Quarter ahead | 70% | 95% | Short-term forwards |
| Month ahead | 80% | 100% | Intraday, day-ahead |

### Risk Monitoring

- [ ] VaR/CVaR calculated for energy portfolio: weekly update
- [ ] Stress test scenarios defined and run quarterly
- [ ] Counterparty credit limits set and monitored
- [ ] Regulatory change monitoring in place (ACM, RVO, Belastingdienst)
- [ ] BESS revenue vs business case tracked monthly
- [ ] Grid connection milestone tracking in place

**DEC Cross-Reference:** → energy-markets [energy-risk-settlement.md] for risk framework

---

## H. Regulatory & Compliance

### Energy Market Registrations

- [ ] EECS/CertiQ account (GO registry)
- [ ] EPEX SPOT membership (if direct trading)
- [ ] ICE Endex membership (if direct futures trading)
- [ ] TenneT BSP (Balancing Service Provider) registration (for BESS)
- [ ] GOPACS registration (for congestion management)
- [ ] REMIT registration (ACER, if trading financial energy products)
- [ ] ACM registration (if leveranciersvergunning needed)

### Key Regulatory Milestones

| Regulation | Effective | DEC Impact | Status |
|---|---|---|---|
| Energiewet 2026 | January 2026 | Expanded MLOEA/cable pooling, new grid tariff structure | [ ] Monitoring [ ] Preparing |
| CSRD (large companies) | FY 2025 | Sustainability reporting if above thresholds | [ ] In scope [ ] Below threshold |
| EU Energy Efficiency Directive | Ongoing | DC energy efficiency reporting >500 kW | [ ] Compliant [ ] Preparing |
| SDE++ (if applicable) | Annual rounds | Heat delivery subsidy, solar PV subsidy | [ ] Applied [ ] Awarded [ ] N/A |

**DEC Cross-Reference:** → netherlands-permitting for all regulatory procedure detail

---

## I. Commercial Summary

### Annual Energy Cost Estimate (40 MW IT Facility)

| Item | Annual Cost | % of Total |
|---|---|---|
| Electricity procurement (wholesale + PPA) | €___M | ___% |
| Transport tariff (transporttarief) | €___K | ___% |
| Connection service (aansluitdienst) | €___K | ___% |
| Energiebelasting | €___K | ___% |
| ODE | €___K | ___% |
| BTW (non-recoverable portion) | €___K | ___% |
| BRP/balancing costs | €___K | ___% |
| GO procurement (unbundled, if needed) | €___K | ___% |
| **Total energy cost** | **€___M** | **100%** |

### Annual Energy Revenue/Savings Estimate

| Item | Annual Revenue | Source |
|---|---|---|
| BESS revenue (FCR + aFRR + arbitrage + congestion) | €___M | BESS Expert |
| Demand response revenue | €___K | BESS Expert |
| Cable pooling savings (avoided transport on self-consumption) | €___K | Grid Expert |
| Peak shaving savings (BESS reduces peak transporttarief) | €___K | Grid Expert |
| Heat revenue from greenhouse (SDE++ + bilateral) | €___M | PPA/BESS Expert |
| Imbalance optimization revenue | €___K | Trading Expert |
| **Total energy revenue/savings** | **€___M** | |

### Net Energy Cost

| | Value |
|---|---|
| Gross energy cost | €___M/year |
| Less: energy revenue/savings | (€___M/year) |
| **Net energy cost** | **€___M/year** |
| **Net energy cost per MW IT** | **€___K/MW/year** |
| **Net energy cost per kWh IT** | **€___ct/kWh** |

---

## J. Key Decision Log

| # | Decision | Date | Rationale | Decision Maker |
|---|---|---|---|---|
| 1 | Grid connection voltage level | | | |
| 2 | Phased vs full capacity application | | | |
| 3 | Flexible vs firm transport contract | | | |
| 4 | PPA type and counterparty | | | |
| 5 | BRP selection | | | |
| 6 | BESS size and configuration | | | |
| 7 | Metering architecture (EB optimization) | | | |
| 8 | GO procurement approach (additionality level) | | | |
| 9 | 24/7 clean energy target | | | |
| 10 | CSRD reporting scope | | | |

---

## Revision History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | | | Initial checklist |
