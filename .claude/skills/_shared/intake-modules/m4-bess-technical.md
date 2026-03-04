# M4: BESS Technical Specifications

**Module metadata:**
- Questions: 45 (Q6.1-6.45)
- Priority: P1 (Q6.1-6.19) · P0 (Q6.20-6.35 for bankability) · P2 (Q6.36-6.45)
- Track: `[BOTH]` — PF loads full; Seed loads P0 questions only (~15 of 45)
- Feeds: `PF` `NP` `SF` `DR`
- Dependencies: M6 (site data needed for site-specific parameters)
- Parallel track: C (Site/Technical)
- Mini-deliverable trigger: After M4 + M5 + M6 → **Technical Asset Summary** (per-site one-pager)

**Seed mode note:** When loaded for seed track, only ask P0 questions (6.14-6.17, 6.20-6.21, 6.28). Skip all P1/P2 questions — seed investors need bankability headlines, not engineering depth.

**Critical insight:** A project finance lender will reject an investment case in the first technical DD phase if BESS technical specifications are incomplete. These questions are P0/P1 gating items for bankability.

---

## Battery Chemistry & Technology

### 6.1 Chemistry Selection
`ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `SF`

Battery chemistry selected and rationale:
- Chemistry: LFP (lithium iron phosphate) or NMC (nickel manganese cobalt)?
- Rationale for selection (safety, cycle life, cost, energy density, supply chain)
- If LFP: acceptance of lower energy density trade-off for longer cycle life
- If NMC: fire safety mitigation plan for higher thermal runaway risk

**Gate:** Chemistry must be explicitly selected with documented rationale. "To be determined" is not acceptable at P1.

---

### 6.2 Manufacturer & Track Record
`ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `DR`

Battery system manufacturer details:
- Manufacturer name and country of origin
- Specific model / product line selected
- Years in market for this specific product
- Global installed base (MW and MWh)
- Reference installations in your target market jurisdiction
- Manufacturer credit rating or financial stability assessment
- Lead time for delivery (weeks/months)

**Gate:** Manufacturer must have >3 years market track record with >500 MW installed globally. If selecting a newer manufacturer, justify the risk with enhanced warranty terms.

---

### 6.3 Supply Chain Sourcing
`ANS` | `P1` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF`

Supply chain risk assessment:
- Cathode material sourcing (geopolitical concentration risk?)
- Anode material sourcing
- Cell manufacturing location
- Container/rack assembly location
- Geopolitical risk: what happens if a major supplier restricts battery exports?
- Diversification strategy: second-source manufacturer identified?

**Gate:** Must identify concentration risk and have a documented mitigation strategy (dual sourcing, strategic inventory, or alternative technology).

---

### 6.4 Operating Temperature Range
`ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `NP`

Temperature specifications vs. site conditions:
- Manufacturer-specified operating range (min/max ambient °C)
- Local climate typical range and extremes
- Performance derating at temperature extremes
- HVAC system sizing to maintain battery within operating range
- Energy consumption of thermal management system (% of throughput)

**Gate:** Operating range must encompass local climate extremes. If derating occurs at common temperatures, quantify the revenue impact.

---

### 6.5 Degradation Curve Source
`DOC` | `P1` | `[DOC-REQUIRED]` | `[BOTH]` | Feeds: `PF`

Degradation data provenance:
- Source: manufacturer lab data, field data, or independent assessment?
- Duration of data: <5 years, 5-10 years, >10 years?
- Conditions: cycling rate, temperature, depth of discharge used in testing
- Applicability: do test conditions match your planned operating regime?
- Independent validation: has a third party (DNV, Wärtsilä) validated the curves?

**Gate:** Degradation curves must be based on real data (not extrapolated from <2 years). If only lab data exists, discount by standard engineering factor and disclose.

---

## Degradation Modeling

### 6.6 P50/P90 Degradation Curves
`CAL` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `SF`

Provide probabilistic degradation projections:
- P50 (median expected) degradation curve: % capacity retained at years 1, 3, 5, 7, 10, 15
- P90 (downside) degradation curve: same milestones
- Methodology: statistical analysis, Monte Carlo simulation, or engineering judgment?
- Variance drivers: what causes the P50-P90 spread?
- Source and validation of the curves

**Gate:** Both P50 and P90 curves must exist. P90 must be used for lender DSCR calculations. P50 can be used for equity return projections. If curves don't exist, flag as critical bankability gap.

---

### 6.7 Calendar vs. Cycle Aging Decomposition
`CAL` | `P2` | `[RANGE]` | `[BOTH]` | Feeds: `PF`

Decompose degradation into calendar and cycle components:
- Calendar aging rate (% capacity loss per year at rest)
- Cycle aging rate (% capacity loss per equivalent full cycle)
- Temperature-dependent aging factors
- How decomposition affects augmentation planning

**Gate:** Decomposition must be technically defensible. If using manufacturer's combined curve without decomposition, note the limitation.

---

### 6.8 Augmentation Strategy
`ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

Battery augmentation plan:
- Trigger: at what % remaining capacity is augmentation triggered? (Typical: 70-80%)
- Timeline: expected augmentation year(s) based on P50 and P90
- Method: module replacement, new container, or parallel addition?
- Cost: per kWh of augmentation capacity (local currency)
- Funding mechanism: reserve fund, operating budget, or refinancing?

**Gate:** Augmentation must be planned and costed. "Replace at end of life" without year-by-year planning is insufficient for project finance.

---

### 6.9 Augmentation Reserve Fund
`CAL` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

Reserve fund for augmentation:
- Total reserve required
- Annual contribution to reserve
- Drawdown schedule (aligned with P50 augmentation timeline)
- Source of contributions: operating cash flow or pre-funded from equity/debt?
- Reserve adequacy under P90 scenario

**Gate:** Reserve must be funded in the financial model. Unfunded augmentation is a bankability blocker.

---

### 6.10 Warranty Degradation Guarantee
`DOC` | `P1` | `[DOC-REQUIRED]` | `[BOTH]` | Feeds: `PF` `DR`

Manufacturer warranty on degradation:
- Guaranteed minimum capacity retained: % at year 5, 10, 15
- Warranty exclusions (excessive cycling, temperature abuse, improper maintenance)
- Remedy: replacement, monetary compensation, or performance guarantee?
- Warranty provider credit quality (investment grade? parent guarantee?)
- Warranty transferable on asset sale?

**Gate:** Warranty must be documented. If warranty guarantees < P90 degradation assumption, the financial model is at risk.

---

### 6.11 Back-to-Back Warranty Chain
`ANS` | `P2` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF` `LC`

Warranty chain from manufacturer to lender:
- Manufacturer → Integrator/EPC warranty (terms, duration, coverage)
- EPC → SPV warranty (pass-through or independent?)
- SPV → Lender (assignment of warranty rights, direct agreement?)
- Gap analysis: are there any uncovered gaps in the warranty chain?

**Gate:** Must demonstrate unbroken warranty chain. Gaps between manufacturer warranty and lender requirements must be identified and addressed (warranty insurance or bridging arrangement).

---

### 6.12 Degradation-Adjusted Revenue
`CAL` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `SF`

Year-by-year revenue impact of degradation:
- Revenue at BOL (beginning of life): per year
- Revenue decline per year due to degradation
- Revenue recovery from augmentation
- 15-year cumulative revenue impact (P50 and P90)
- DSCR impact of degradation in years 5, 10, 15

**Gate:** Must show year-by-year revenue curves, not just BOL assumption. If DSCR drops below covenant in later years due to degradation, flag as structural risk.

---

### 6.13 Independent Degradation Assessment
`EXT` | `P2` | `[DOC-REQUIRED]` | `[BOTH]` | Feeds: `PF` `DR`

Independent engineer assessment of degradation:
- Engaged or planned? (DNV, Wärtsilä, or equivalent)
- Scope of assessment (review manufacturer data, independent testing, field data analysis)
- Timeline for report
- Status: completed? Draft? Not yet engaged?

**Gate:** Independent assessment is required for project finance. If not yet engaged, include in budget and timeline.

---

## Revenue Stacking Specifics

### 6.14 Ancillary Services Prequalification
`ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `SF`

Frequency containment and balancing services prequalification:
- FCR (Frequency Containment Reserve) prequalification: application submitted? Status? Qualified MW?
- Expected FCR revenue based on recent auction prices in your market
- Timeline to full prequalification if not yet complete

**Gate:** Prequalification status must be confirmed (not assumed). If revenue model relies on FCR and prequalification is incomplete, flag as revenue certainty risk.

---

### 6.15 Secondary Ancillary Services
`ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

Additional balancing services (aFRR, mFRR, or equivalent):
- Registration status with TSO
- Platform integration timeline (e.g., PICASSO, MARI)
- Expected revenue contribution per MW/year
- Technical requirements met (activation time, ramp rate)?

**Gate:** Registration status must be stated. If not yet registered, include timeline in project schedule.

---

### 6.16 Arbitrage Strategy
`ANS` | `P0` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF` `SF`

Day-ahead and intraday arbitrage:
- Primary trading market
- Average daily price spread assumption (source: historical market data)
- Spread methodology: day-ahead only, or combined day-ahead + intraday?
- Seasonal variation in spreads
- Historical validation: backtested against actual local price data?

**Gate:** Spread assumptions must be validated with actual market data from your target geography. Extrapolation from adjacent markets must be disclosed and justified.

---

### 6.17 Contracted vs. Merchant Split
`ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `SF`

Revenue certainty breakdown:
- Contracted revenue: % of total (ancillary services contracts, tolling agreements, capacity payments)
- Merchant revenue: % of total (arbitrage, spot market, optimized dispatch)
- Target split at COD
- Target split at Year 3 (after contract ramp-up)
- Minimum contracted percentage required for bankability (lender expectation: typically ≥50%)

**Gate:** Must state the split explicitly. If merchant revenue >50%, flag as bankability risk requiring enhanced credit support or higher DSCR.

---

### 6.18 Dispatch Optimization
`ANS` | `P1` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF` `SF`

Dispatch and optimization platform:
- Optimization approach: rule-based, ML/AI-based, or third-party platform?
- If third-party: which platform?
- Competitive advantage in dispatch: what does your approach do better?
- Backtesting results: performance vs. simple rule-based benchmark?
- Latency and execution: direct market access or through aggregator?

**Gate:** Must specify the optimization approach. "We'll optimize" without specifics is insufficient.

---

### 6.19 Revenue Stacking Mutual Exclusions
`CAL` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

Which revenue streams can operate concurrently vs. are mutually exclusive?
- FCR + arbitrage: concurrent or sequential?
- aFRR + peak shaving: concurrent or sequential?
- Grid services + customer behind-the-meter services: compatible?
- Time allocation model: what percentage of hours assigned to each revenue stream?
- Conflict resolution: when two services call for opposite dispatch, which has priority?

**Gate:** Must document mutual exclusions. If revenue model assumes concurrent stacking of mutually exclusive services, it overstates revenue.

---

## BMS/EMS Platform

### 6.20 BMS Specifications
`ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `DR`

Battery Management System details:
- Manufacturer and model
- Software version and certification status
- Certifications held: IEC 62933 (safety), IEC 62443 (cybersecurity)
- Cell-level monitoring capability
- State of charge (SoC) and state of health (SoH) accuracy
- Alarm thresholds and automated protection actions

**Gate:** BMS must be specified with model number and certifications. "Standard BMS" is insufficient.

---

### 6.21 EMS Platform
`ANS` | `P1` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF` `SF`

Energy Management System details:
- Integrated stack or custom platform?
- Optimization algorithms for revenue stacking (describe approach)
- Real-time market data feed integration
- Forecasting capabilities (price, load, renewable generation)
- API integration with grid operator systems

**Gate:** EMS must be specified. If custom-built, describe development status and team capability.

---

### 6.22 Inverter/PCS Redundancy
`ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

Power Conversion System specifications:
- Manufacturer, model, rating (MW)
- Redundancy level: N+1 or single? Why?
- Revenue impact during maintenance: what capacity is lost?
- Maintenance schedule and downtime (hours/year)
- Round-trip efficiency of PCS (%)

**Gate:** If single PCS without redundancy, quantify the availability impact and maintenance downtime revenue loss.

---

### 6.23 Cybersecurity
`ANS` | `P2` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF` `DR`

Cybersecurity for BESS control systems:
- Penetration testing: conducted? By whom? Results?
- SOC 2 or ISO 27001 certification: planned?
- Network segmentation: BMS/EMS isolated from corporate IT?
- Cloud data encryption: at rest and in transit?
- Incident response plan: documented?

**Gate:** If BESS is grid-connected and remotely controlled, cybersecurity is a lender concern. At minimum: network segmentation and documented incident response plan.

---

### 6.24 DSO/TSO Integration
`ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `NP`

Grid operator integration:
- Congestion management platform registration: status?
- TSO balancing portal registration: status?
- DSO smart meter and data exchange: configured?
- Congestion management participation: agreed? Revenue terms?

**Gate:** Grid operator integration must be confirmed or in progress. Without it, grid services revenue is not achievable.

---

### 6.25 Remote Monitoring & Spare Parts
`ANS` | `P2` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF`

Operational support infrastructure:
- Remote monitoring capability (24/7 NOC or business hours?)
- Spare parts strategy: on-site inventory, regional warehouse, manufacturer?
- Critical spare parts lead time (inverter modules, BMS boards, contactors)
- O&M partner identified? Contract terms?
- Performance monitoring: what KPIs are tracked daily?

**Gate:** Critical spare parts lead time must be <72 hours. If longer, quantify the revenue loss from extended outages.

---

## Thermal Management & Fire Safety

### 6.26 HVAC System
`ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `NP`

Cooling system for BESS containers:
- HVAC capacity (kW cooling per container)
- Ambient design conditions (maximum outdoor temp for full capacity)
- N+1 redundancy on cooling? If not, derating at HVAC failure?
- Annual energy consumption for cooling (MWh)
- Noise level at property boundary (dB(A))

**Gate:** HVAC must be sized for local climate extremes. If no N+1 redundancy, quantify the capacity derating risk.

---

### 6.27 Fire Suppression System
`ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `NP` `DR`

Fire safety for BESS:
- System type: gaseous agent (FM-200, Novec 1230) or liquid (water mist)?
- Capacity: sufficient for containment of single-container thermal runaway?
- Auto-activation: detection method (temperature, smoke, gas)?
- Manual override capability
- Compliance with applicable fire safety standards (e.g., PGS 37-1 in Netherlands)

**Gate:** Fire suppression must be specified and comply with applicable local fire safety standards. "Standard fire suppression" without specification is insufficient for permitting.

---

### 6.28 UL9540A Testing
`EXT` | `P0` | `[BINARY]` | `[BOTH]` | Feeds: `PF` `NP` `DR`

UL9540A large-scale fire testing:
- Testing completed? By whom? Date?
- Test results available for insurance underwriters?
- If not completed: scheduled? Timeline? Budget?
- If using manufacturer's UL9540A results: applicable to your specific configuration?

**Gate:** UL9540A testing must be completed or credibly scheduled. Insurance underwriters require this; without it, insurance coverage may be unavailable or prohibitively expensive.

---

### 6.29 Container Layout
`DOC` | `P1` | `[DOC-REQUIRED]` | `[BOTH]` | Feeds: `NP` `PF`

Site layout for fire safety:
- Container spacing: minimum clearance between containers (typically 2.5-3m)?
- Distance to buildings, property boundaries, and public areas
- Fire access roads: adequate for fire department vehicles?
- Containment: bunds/berms for fire water runoff?
- Site plan signed off by fire safety consultant?

**Gate:** Layout must comply with applicable clearance requirements. Site plan must be reviewed by a qualified fire consultant.

---

### 6.30 Fire Response Plan
`DOC` | `P1` | `[DOC-REQUIRED]` | `[BOTH]` | Feeds: `NP` `DR`

Emergency response:
- Fire response plan documented?
- Approved by local fire department?
- Training schedule for on-site personnel
- Coordination with local emergency services
- Evacuation plan for adjacent facilities

**Gate:** Fire response plan must be documented and submitted to local fire department. Approval timeline should align with construction schedule.

---

## Grid Code & Prequalification

### 6.31 Grid Code Compliance
`EXT` | `P1` | `[BINARY]` | `[BOTH]` | Feeds: `PF` `NP`

Grid code compliance certification:
- Applicable electrical safety standards: compliance confirmed?
- Generation and storage connection requirements (e.g., VDE 4110 / EN 50549): applicable? Compliant?
- Grid operator-specific requirements: identified? Met?
- Compliance certificate obtained or planned?

**Gate:** Grid code compliance must be engineered into the design, not retrofitted. Compliance certificate must be planned before COD.

---

### 6.32 Fault Ride-Through Capability
`ANS` | `P2` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

System behavior during grid faults:
- Low Voltage Ride-Through (LVRT) capability: duration, voltage threshold
- High Voltage Ride-Through (HVRT) capability: duration, voltage threshold
- Reactive power injection during faults: capability?
- Protection system coordination with grid operator requirements

**Gate:** LVRT/HVRT must be designed in per grid code requirements. Non-compliance risks grid disconnection.

---

### 6.33-6.35 Additional Grid Questions

**6.33** Reactive power capabilities and TSO requirements: can the BESS provide reactive power support? At what cost to active power throughput? `ANS` | `P2` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**6.34** Symmetry testing for FCR: has upward and downward response symmetry been validated? TSOs typically require symmetric response for FCR prequalification. `ANS` | `P1` | `[BINARY]` | `[BOTH]` | Feeds: `PF`

**6.35** Short-circuit strength and grid interaction modeling: has power system analysis been conducted for the connection point? Results? `EXT` | `P2` | `[BINARY]` | `[BOTH]` | Feeds: `PF` `NP`

---

## Cycling Strategy & Warranty

### 6.36 Planned Cycling Frequency
`CAL` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

Annual cycling plan:
- Planned equivalent full cycles per year
- Basis: revenue model optimization or TSO schedule?
- Daily cycling pattern (peak/off-peak, seasonal variation)
- Total lifetime cycles planned

**Gate:** Must be stated explicitly with source of assumption.

---

### 6.37-6.40 Warranty Alignment

**6.37** C-rate limits and depth-of-discharge constraints: manufacturer-specified vs. planned operating regime. `ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**6.38** Warranty cycling budget alignment: does the planned cycling regime fit within the manufacturer's warranty cycling budget? Surplus or deficit cycles? `CAL` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**6.39** Warranty exclusions: what specific events void or reduce the warranty? (Excessive cycling, temperature abuse, unauthorized modifications, natural disasters) `DOC` | `P2` | `[DOC-REQUIRED]` | `[BOTH]` | Feeds: `PF` `LC`

**6.40** Revenue impact if cycling limited to warranty budget: if planned cycling exceeds warranty, what revenue is lost by constraining to warranty limits? `CAL` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `SF`

**Gate:** If planned cycling exceeds warranty budget, this is a **critical risk**. Either reduce cycling (accept lower revenue) or negotiate enhanced warranty (accept higher cost).

---

## Efficiency & End-of-Life

### 6.41-6.45 Efficiency and Decommissioning

**6.41** Round-trip efficiency (RTE): nameplate at BOL, conservative model assumption, degradation of RTE over time. `ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**6.42** Auxiliary power consumption: BMS, cooling, standby, and building loads — total annual kWh and as % of throughput. `CAL` | `P2` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**6.43** Decommissioning cost estimate: per kWh, reserve fund mechanism, trigger for decommissioning. `CAL` | `P2` | `[RANGE]` | `[BOTH]` | Feeds: `PF`

**6.44** EU Battery Regulation 2023/1542 compliance: battery passport requirement by 2027 — compliance plan? `ANS` | `P2` | `[BINARY]` | `[BOTH]` | Feeds: `PF` `NP`

**6.45** Recycling partner: identified? Pre-contractual arrangement? Estimated recycling value (positive or negative)? `ANS` | `P2` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF`

---

## Section 6 Gate Summary

| Criterion | Required For | Status |
|-----------|-------------|--------|
| UL9540A testing completed or scheduled | P0 | [ ] |
| FCR prequalification status confirmed | P0 | [ ] |
| Contracted vs. merchant revenue split stated | P0 | [ ] |
| Arbitrage spreads validated with local market data | P0 | [ ] |
| P50/P90 degradation curves exist | P1 | [ ] |
| Chemistry selected with rationale | P1 | [ ] |
| Manufacturer with >3yr / >500MW track record | P1 | [ ] |
| Augmentation reserve funded in model | P1 | [ ] |
| Grid code compliance designed in | P1 | [ ] |
| Cycling plan within warranty budget (or risk flagged) | P1 | [ ] |
| Fire suppression compliant with local standards | P1 | [ ] |
