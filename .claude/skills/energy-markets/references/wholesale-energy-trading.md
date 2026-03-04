# Wholesale Energy Trading for Data Centers

## 1. Dutch Wholesale Electricity Market Structure

### Market Overview

The Netherlands is part of the Northwest European coupled electricity market:

| Market | Operator | Trading Window | Products | Key Feature |
|---|---|---|---|---|
| **Day-Ahead** | EPEX SPOT | D-1, auction at 12:00 CET | Hourly blocks (24 per day) | Main price reference, coupled with BE/DE/FR/AT/NO |
| **Intraday Continuous** | EPEX SPOT | D-1 15:00 to D delivery | 15-min, 30-min, hourly | Continuous matching, cross-border |
| **Intraday Auction** | EPEX SPOT | Multiple auctions D-1 to D | 15-min blocks | Quarterly introduction for NL |
| **Futures** | ICE Endex | Months to years ahead | Baseload, peakload months/quarters/years | Financial settlement, physical delivery option |
| **Imbalance** | TenneT | Real-time | 15-min settlement periods | Single imbalance price (since 2021) |
| **OTC** | Bilateral | Any | Custom profiles | Broker-intermediated (ICAP, TFS, GFI) |

### Key NL Market Characteristics

**Price volatility is structural:**
- High renewable penetration (solar + wind approaching 50% of generation) creates structural price volatility
- Negative prices increasingly common (>100 hours/year) during high solar + wind + low demand
- Price spikes during low-wind winter evenings (€200-1,000+/MWh)
- This volatility is opportunity for flexible consumers (BESS, demand response)

**NL is a net importer:**
- Limited domestic thermal generation capacity post-coal exit (2030 target)
- Heavy reliance on interconnector flows (NorNed, BritNed, COBRAcable, Belgium)
- Import dependency creates exposure to neighboring market conditions

**Baseload price trend (recent):**
- 2020: ~€30/MWh (COVID depression)
- 2021-2022: €100-300/MWh (energy crisis)
- 2023-2024: €60-100/MWh (normalization)
- Forward curve (2025-2028): €60-90/MWh (consensus range, highly uncertain)

## 2. Data Center Energy Procurement Strategy

### The Layered Hedge Book

**Principle:** No single procurement instrument is optimal. A data center should construct a layered hedge book that combines multiple instruments:

```
Layer 4: SPOT / IMBALANCE (residual, unhedged)
  │  0-10% of volume
  │  Purpose: capture price upside, manage forecast errors
  │
Layer 3: SHORT-TERM FORWARDS (1-3 months ahead)
  │  10-20% of volume
  │  Purpose: seasonal adjustment, fine-tune hedge
  │
Layer 2: MEDIUM-TERM FUTURES (1-3 years ahead)
  │  30-50% of volume
  │  Purpose: budget certainty, core hedge
  │
Layer 1: LONG-TERM PPA (5-15 years)
     20-40% of volume
     Purpose: structural hedge, ESG compliance, price floor
```

### Procurement Volume Estimation

**Data center load profile characteristics:**

| Parameter | Training-Dominant DC | Inference-Dominant DC | Mixed DC |
|---|---|---|---|
| Load factor | 90-95% | 50-70% | 70-85% |
| Daily variability | ±5% | ±30-50% | ±15-25% |
| Seasonal variability | Minimal | Moderate | Low-moderate |
| Ramp rate | Slow (hours) | Fast (minutes) | Mixed |
| Annual consumption (40 MW) | ~315 GWh | ~220-280 GWh | ~250-300 GWh |

**Volume risk:** The difference between contracted and actual consumption must be settled in the imbalance market. For training DCs, volume risk is low (stable load). For inference DCs, volume risk is significant.

### Procurement Instruments Comparison

| Instrument | Price Certainty | Volume Flexibility | ESG Value | Complexity | Tenor |
|---|---|---|---|---|---|
| Futures (ICE Endex) | High (fixed) | Low (must nominate) | None | Low | 1-3 years |
| Physical PPA | Medium-High | Low-Medium | High (additionality) | High | 5-15 years |
| Virtual PPA (CfD) | Medium | High (no physical delivery) | Medium | Medium | 5-10 years |
| Day-Ahead spot | None | Full | None | Low | Daily |
| OTC bilateral | High (negotiable) | Negotiable | Possible | Medium | 1-5 years |

### DEC-Specific Procurement Considerations

**1. Greenhouse co-location changes the equation:**
- Heat recovery from DC displaces gas consumption at greenhouse
- If greenhouse operates WKK (CHP), DC heat may reduce WKK running hours → reduces greenhouse's own electricity generation
- The energy balance of DC + greenhouse must be modeled together, not separately
- Potential for cable pooling: DC + greenhouse + solar PV behind single grid connection

**2. SDE++ interaction:**
- If DEC receives SDE++ for heat delivery, the subsidy is based on avoided CO2 → energy procurement methodology matters
- Market-referenced PPA can affect SDE++ basisbedrag calculation

**3. Energiebelasting optimization:**
- Energiebelasting (energy tax) has declining rate per volume bracket
- Multi-tenant DC can structure metering to optimize tax position (see energy-risk-settlement.md)
- Zelflevering (self-supply) via MLOEA/cable pooling can reduce tax if structured correctly

## 3. BRP Operations

### What is a BRP (Programmaverantwoordelijke/Balance Responsible Party)?

Every grid connection in NL must have a BRP responsible for balancing supply and demand. The BRP:
- Submits day-ahead and intraday nominations (E-programs) to TenneT
- Is financially responsible for imbalance (difference between nominated and actual)
- Settles with TenneT based on single imbalance price per 15-min period

### BRP Options for DEC

| Option | Description | When to Choose |
|---|---|---|
| **Utility BRP** | Energy supplier acts as BRP (e.g., Vattenfall, Eneco) | Simple, small DC, no trading ambition |
| **Independent BRP** | Specialized BRP/aggregator (e.g., Flexitricity, Sympower, Next Kraftwerke) | Medium DC, want flexibility optimization |
| **Own BRP license** | DEC becomes its own BRP (ACM license required) | Large portfolio (>100 MW), trading capability |
| **BRP + trading desk** | Own BRP with active imbalance trading | Maximum value, highest complexity |

**DEC Recommendation:** Start with independent BRP (lower cost, access to imbalance optimization). Consider own BRP license only when portfolio exceeds 100 MW and DEC has energy trading competence.

### Imbalance Optimization

**The imbalance market is not just a penalty — it's a revenue opportunity:**

TenneT's single imbalance price (enkel onbalans) reflects real-time system need:
- System short (demand > supply): imbalance price > day-ahead price → short positions profit
- System long (supply > demand): imbalance price < day-ahead price → long positions profit

**Optimization strategies for data centers:**
1. **Passive optimization:** Accurate forecasting reduces imbalance exposure (±2-3% of volume × price spread)
2. **Active optimization:** Deliberately deviate from nomination when imbalance price is favorable
3. **BESS-enhanced:** Use co-located BESS to capture imbalance spread (buy low/sell high)

**Revenue potential:**
- Passive (good forecasting): €0.50-1.50/MWh savings vs poor forecasting
- Active (with BESS): €3-8/MWh additional revenue on BESS capacity

## 4. Energy Market Data Sources

### Price References

| Source | Data | Access | Cost |
|---|---|---|---|
| EPEX SPOT | Day-ahead, intraday prices | API subscription | €5,000-15,000/year |
| ICE Endex | Futures prices, curves | Terminal or API | €10,000-30,000/year |
| TenneT | Imbalance prices, system state | Open data (tennet.org) | Free |
| ENTSO-E Transparency | Cross-border flows, generation | Open data | Free |
| Montel | News, analysis, forecasts | Subscription | €5,000-20,000/year |

### Forecasting

**Price forecasting services for trading:**
- Montel Analytics, ICIS, Platts (market fundamentals)
- Energy Quantified, Energeia (NL-specific analytics)
- Proprietary models (weather → renewable generation → residual demand → price)

**Load forecasting for DEC:**
- Training workloads: highly predictable (known schedule, stable utilization)
- Inference workloads: requires integration with tenant API traffic forecasting
- Combined: DEC should provide 48-hour load forecast to BRP for nomination accuracy

## 5. Wholesale Market Access

### Trading Infrastructure

**For DEC (when own BRP or active trading):**

| Component | Purpose | Vendors |
|---|---|---|
| ETRM System | Trade capture, position management, P&L | Allegro, Brady (now ION), Openlink, Trayport |
| Market access | EPEX SPOT, ICE Endex trading | Direct membership or via broker |
| Metering | Real-time consumption data to BRP | Smart meter + telemetry to BRP |
| Forecasting | Load + price forecasting | In-house or external service |
| Risk management | VaR, limits, credit management | ETRM module or standalone |

**Cost of own trading capability:** €200,000-500,000/year (systems, data, personnel, memberships)
**Break-even point:** Generally above 100 MW portfolio

### Market Participants Relevant to DEC

| Category | Examples | Relevance |
|---|---|---|
| Utilities (leverancier) | Vattenfall, Eneco, Essent, Greenchoice | Standard energy supply, BRP services |
| Energy traders | Axpo, Statkraft, Shell Energy, Engie | Structured procurement, PPA counterparty |
| Aggregators | Next Kraftwerke, Sympower, Flexitricity | Flexibility monetization, BRP |
| PPA advisors | Pexapark, Emergy (NL), Re-Source | PPA origination and structuring |
| Brokers | ICAP, TFS/Tradition, GFI | OTC bilateral trading |

## Cross-References
- See [ppa-green-certificates.md](ppa-green-certificates.md) for PPA structuring and GO procurement (Layer 1 of hedge book)
- See [balancing-bess-revenue.md](balancing-bess-revenue.md) for imbalance trading with BESS and demand response
- See [energy-risk-settlement.md](energy-risk-settlement.md) for risk management and energiebelasting optimization
- See [grid-connection-strategy.md](grid-connection-strategy.md) for connection capacity impact on procurement volume
- See companion skill `dc-engineering` for load profiles and metering architecture
- See companion skill `ai-infrastructure` for GPU workload power profiles (training vs inference variability)
- See companion skill `netherlands-permitting` for Energiewet regulatory context
- See companion skill `site-development` for energy cost in financial model
