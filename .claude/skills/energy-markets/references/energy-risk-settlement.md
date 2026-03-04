# Energy Risk Management & Settlement

## 1. Energy Risk Categories for Data Centers

### Risk Taxonomy

| Risk Type | Description | Magnitude (40 MW DC) | Mitigation |
|---|---|---|---|
| **Market price risk** | Wholesale price moves against hedged position | €1-5M/year exposure on unhedged portion | Layered hedge book, PPA |
| **Volume risk** | Actual consumption differs from contracted | €0.5-2M/year at ±10% utilization variance | Flexible contracts, tolerance bands |
| **Profile risk** | PPA production doesn't match DC load shape | €0.5-1.5M/year profile cost | Baseload conversion, BESS, portfolio |
| **Counterparty credit risk** | PPA/supply counterparty defaults | Up to full replacement cost of contract | Credit limits, parent guarantees, diversification |
| **Regulatory risk** | Tax/levy/tariff changes | €0.5-4M/year (energiebelasting changes) | Contract change-of-law clauses, monitoring |
| **Grid connection risk** | Connection delayed or capacity reduced | Project delay cost (€M) | Phased application, flexible contracts |
| **Imbalance risk** | Poor nomination accuracy | €0.2-1M/year | Forecasting, BRP optimization |
| **BESS revenue risk** | FCR/aFRR revenue below business case | €0.5-2M/year for 20 MW BESS | Revenue diversification, stacking |
| **Carbon price risk** | EU ETS price change affects competitiveness | Indirect (affects fossil alternative cost) | Monitor, position as advantage |

### Risk Quantification Methodology

**Value at Risk (VaR) for energy portfolio:**
- 95% VaR: maximum loss over defined period with 95% confidence
- For DC energy portfolio: calculate VaR on open (unhedged) position
- Include: spot price exposure, volume variance, PPA mark-to-market, BESS revenue variance

**Stress testing:**
- Energy crisis scenario (2021-2022 replay): spot prices 3-5× normal
- Renewable drought: low wind + low solar for 2 weeks → PPA shortfall + high spot prices
- Grid emergency: forced curtailment, penalty charges
- Regulatory shock: energiebelasting increase, ODE structure change

## 2. Dutch Energy Taxation

### Energiebelasting (EB / Energy Tax)

The most significant non-commodity energy cost for data centers:

**2025 Rate Structure (electricity):**

| Volume Bracket (kWh/year) | Rate (€ct/kWh) | Annual Cost at 40 MW (315 GWh) |
|---|---|---|
| 0 - 10,000 | ~12.7 | Negligible (tiny bracket) |
| 10,001 - 50,000 | ~5.5 | Negligible |
| 50,001 - 10,000,000 | ~2.2 | ~€220K (for first 10 GWh) |
| >10,000,000 | ~0.05 | ~€153K (for remaining 305 GWh) |
| **Total EB** | | **~€373K/year** |

*Rates are approximate and subject to annual government budget (Belastingplan). The declining rate structure means large consumers pay very low marginal EB.*

### ODE (Opslag Duurzame Energie / Sustainable Energy Surcharge)

ODE funds SDE++ subsidies. Structure mirrors EB brackets:

| Volume Bracket (kWh/year) | Rate (€ct/kWh) | Annual Cost at 40 MW |
|---|---|---|
| 0 - 10,000 | ~4.2 | Negligible |
| 10,001 - 50,000 | ~5.6 | Negligible |
| 50,001 - 10,000,000 | ~2.6 | ~€260K |
| >10,000,000 | ~0.01 | ~€30K |
| **Total ODE** | | **~€290K/year** |

### Multi-Tenant Metering Optimization

**The metering architecture determines the tax bracket:**

**Option 1: Single connection, single meter (DEC as consumer):**
- Total 315 GWh measured at one point
- Most volume in lowest bracket → lowest EB/ODE per kWh
- DEC bills tenants for energy (DEC is leverancier/energy supplier to tenants)
- **Requires DEC to have leveranciersvergunning (energy supply license) from ACM**

**Option 2: Single connection, sub-metering per tenant (DEC passes through):**
- Each tenant measured separately → may fall in higher brackets per tenant
- Higher aggregate EB/ODE cost
- Simpler for DEC (no leveranciersvergunning needed)
- Tenants can choose own energy supplier via MLOEA

**Option 3: MLOEA (Multi-supplier, single connection):**
- Single grid connection, but each tenant has own supply contract with own leverancier
- Energiewet 2026 expands MLOEA eligibility
- Each tenant in own EB/ODE bracket (based on their volume)
- DEC provides physical infrastructure; tenants manage own energy

**DEC Tax Optimization Strategy:**
- For Phase 1 (single large tenant): Option 1 is simplest and most tax-efficient
- For multi-tenant: Option 3 (MLOEA) preferred → avoids DEC needing leveranciersvergunning while giving tenants flexibility
- **Annual savings from optimal structuring: €200K-1M+ depending on tenant mix**
- Engage energy tax specialist early (this is Expert 4's core competence)

### BTW (VAT) on Energy

- Standard 21% BTW on energy supply to business customers
- Fully recoverable for B2B tenants (VAT-registered)
- DEC must ensure correct BTW treatment in energy billing (if DEC supplies)
- Heat delivery to grower: 21% BTW (not reduced rate — heat is not gas)

## 3. Settlement & Reconciliation

### Dutch Settlement Process

**Allocation (allocatie):**
- Every 15 minutes, consumption is allocated to responsible parties
- Based on smart meter data (telemetrie for large connections, slimme meter for small)
- Allocation to leverancier (supplier) and BRP
- Reconciliation (reconciliatie): correction after actual metering data available (T+10 business days)

### Multi-Tenant Settlement Architecture

```
Grid Connection (DEC site)
  │
  ├── Main Meter (fiscal meter, allocatiepunt) ──→ Netbeheerder
  │
  ├── Tenant A Sub-Meter ──→ DEC billing system (or MLOEA allocatiepunt)
  │
  ├── Tenant B Sub-Meter ──→ DEC billing system (or MLOEA allocatiepunt)
  │
  ├── BESS Meter ──→ BESS management system
  │
  └── Facility Load Meter ──→ DEC facility management
       (cooling, lighting, security, etc.)
```

**Key settlement challenges:**
1. **Sub-metering accuracy:** Revenue-grade (Class 0.2S or 0.5S) sub-meters required for tenant billing
2. **Facility load allocation:** Common area power (cooling, lighting) must be allocated fairly across tenants
3. **PUE allocation:** PUE varies by hall, season, cooling load — must be metered, not estimated
4. **BESS revenue attribution:** If BESS serves multiple revenue streams, clear allocation methodology needed
5. **Time-of-use billing:** If DEC passes through wholesale price to tenants, 15-min resolution required

### Metering Standards

| Standard | Scope | Requirement |
|---|---|---|
| MID (Measuring Instruments Directive) | Fiscal meters | Mandatory for billing-grade meters in EU |
| NEN-EN 50600-99-1 | PUE measurement | Industry standard for DC efficiency metrics |
| ACM Meetcode | Grid metering | Dutch code for grid-connected metering |
| IEC 62052/62053 | Meter accuracy | Class 0.2S for revenue-grade, 0.5S acceptable |

## 4. Risk Management Framework

### Hedging Policy

**Minimum hedge ratios for DEC energy portfolio:**

| Time Horizon | Minimum Hedge | Maximum Hedge | Instruments |
|---|---|---|---|
| 0-3 months | 80% | 100% | Spot + short-term forward |
| 3-12 months | 60% | 90% | Futures + PPA |
| 1-3 years | 40% | 70% | Futures + PPA |
| 3-10 years | 20% | 50% | PPA only |
| >10 years | 0% | 30% | Long-term PPA (if available) |

### Credit Risk Management

**Counterparty limits:**
- No single counterparty >30% of total energy procurement volume
- PPA counterparty: require investment-grade credit rating or parent guarantee
- Utility supply: standard terms with reputable NL utility
- BESS revenue: diversify across FCR, aFRR, and arbitrage (not dependent on single market)

**Credit support instruments:**
- Parent company guarantee (most common for PPA)
- Letter of credit (bank-backed, expensive)
- Margin/collateral posting (ISDA CSA framework)
- Insurance (energy counterparty default insurance, emerging product)

### Regulatory Risk Monitoring

**Key regulatory changes to monitor:**

| Risk | Source | Impact | Monitoring |
|---|---|---|---|
| EB/ODE rate changes | Belastingplan (annual) | Direct cost impact | Annual, September budget day |
| Energiewet implementation | ACM, Ministry EZK | MLOEA rules, cable pooling | Ongoing, industry associations |
| SDE++ rule changes | RVO | Heat revenue eligibility/terms | Annual SDE++ opening |
| Grid tariff restructuring | ACM | Transporttarief impact | ACM consultation process |
| EU ETS reform (CBAM) | EU Commission | Indirect competitiveness impact | EU policy cycle |
| CSRD implementation | EU/NL | Reporting requirements | ESRS timeline |

## 5. Financial Reporting of Energy Contracts

### IFRS 9 Hedge Accounting

**PPA as hedge instrument:**
- Physical PPA: generally qualifies for "own use" exemption (IFRS 9 scope exclusion) → not a financial instrument
- Virtual PPA (CfD): IS a financial instrument → must be accounted for at fair value unless hedge accounting applied
- Hedge accounting: CfD designated as cash flow hedge of forecast electricity purchase → P&L volatility reduction
- **Complexity warning:** IFRS 9 hedge documentation requires demonstration of hedge effectiveness, prospective and retrospective testing

**For DEC (startup stage):**
- Physical PPAs preferred (simpler accounting treatment)
- If virtual PPA: engage IFRS 9 specialist early
- Investor reporting: show energy cost as range (base case + sensitivities) not single number

### Energy Cost Reporting

**For tenant billing:**
- Transparent cost build-up: commodity + network + EB + ODE + facility margin
- Pass-through vs fixed: tenants may prefer fixed €/MWh or pass-through of actual costs
- Reconciliation: monthly actual vs estimated, quarterly true-up

**For investor reporting:**
- Energy cost per GPU-hour or per kW-month
- PUE trend (improving over time as utilization increases)
- Hedge ratio and mark-to-market of energy contracts
- BESS revenue vs business case
- Heat revenue (€/GJ delivered, availability %)

## Cross-References
- See [wholesale-energy-trading.md](wholesale-energy-trading.md) for hedge book construction and BRP selection
- See [ppa-green-certificates.md](ppa-green-certificates.md) for PPA risk assessment (counterparty, volume, profile)
- See [balancing-bess-revenue.md](balancing-bess-revenue.md) for BESS revenue risk quantification
- See [grid-connection-strategy.md](grid-connection-strategy.md) for grid tariff optimization and MLOEA metering
- See [carbon-esg-compliance.md](carbon-esg-compliance.md) for carbon price risk and ESG reporting
- See companion skill `netherlands-permitting` for energiebelasting regulatory framework, leveranciersvergunning
- See companion skill `dc-engineering` for metering hardware (rack PDU, revenue-grade meters)
- See companion skill `site-development` for energy costs in financial model, investor reporting
