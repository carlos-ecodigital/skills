# EPC Contracts and Energy-Specific Clauses

This reference provides clause guidance for EPC (Engineer, Procure, Construct) contracts and energy-specific supplementary clauses for BESS, data centre, and renewable energy projects. Load this reference when drafting EPC contracts or when a service agreement involves energy infrastructure. These clauses supplement -- and in some cases replace -- the standard sections in a Service Agreement (see `contract-drafting/sections-guide.md`).

For JV structuring provisions, see `corporate-ma/jv-structuring.md`.


## 1. EPC Terms (Engineer, Procure, Construct)

### 1.1 Purpose
EPC provisions allocate design, procurement, and construction responsibilities. The EPC contractor typically assumes single-point responsibility for delivering a complete, operational facility.

### 1.2 Key Clauses

**1.2(a) Scope of Works and Employer's Requirements**
- Detailed technical specification (Employer's Requirements / ER) annexed as a Schedule
- EPC Contractor's obligation to design, procure, manufacture, deliver, install, test, and commission the facility in accordance with the ER
- Contractor's Proposal annexed -- any deviations from ER to be expressly listed

**1.2(b) Turnkey vs Split Contract**
- Turnkey: single EPC contractor responsible for all works; lump sum price
- Split: separate contracts for engineering, procurement, and construction -- requires interface agreement
- Hybrid: turnkey with owner-furnished equipment (OFE) -- responsibility matrix required

**1.2(c) Design Responsibility**
- Contractor assumes full design responsibility (fitness for purpose or reasonable skill and care -- specify which)
- Fitness for purpose: strict standard -- design must achieve intended outcomes
- Reasonable skill and care: negligence standard -- appropriate for UK-law contracts where fitness for purpose is disproportionate
- Design review process: owner's right to review does not diminish contractor's responsibility

**1.2(d) Site Conditions**
- Responsibility for site conditions: owner provides site data; contractor responsible for interpretation
- Unforeseen ground conditions: risk allocation (contractor risk if site survey was available; shared risk if not)
- Access and interface with other contractors on site

**1.2(e) Permits and Approvals**
- Allocation of permit responsibility: owner typically obtains planning/environmental permits; contractor obtains construction-specific permits
- Permit risk: consequences of permit delay or refusal
- Change in law affecting permit requirements


## 2. Performance Guarantees

### 2.1 Purpose
Performance guarantees establish minimum technical performance that the facility must achieve. They are critical in energy/BESS contracts because revenue depends on performance.

### 2.2 Key Clauses

**2.2(a) Capacity Guarantee**
- Guaranteed capacity: {{GUARANTEED_CAPACITY_MW}} MW (or MWh for energy capacity)
- Measurement: standardised capacity test protocol (IEC 62933 for BESS; IEC 61724 for solar)
- Test conditions: reference ambient temperature, humidity, grid voltage
- Capacity shortfall: triggers performance liquidated damages

**2.2(b) Round-Trip Efficiency (RTE) Guarantee** (BESS-specific)
- Guaranteed RTE: {{GUARANTEED_RTE}}% at beginning of life (BOL)
- Measurement protocol: charge from empty to full, discharge from full to empty, measure AC-AC efficiency
- Adjustment for auxiliary loads (HVAC, BMS, fire suppression)
- RTE degradation: expected annual decline; guaranteed minimum at year milestones

**2.2(c) Availability Guarantee**
- Guaranteed availability: {{GUARANTEED_AVAILABILITY}}% (typically 95-98%)
- Calculation: (total hours - planned outage - forced outage) / (total hours - planned outage) x 100
- Planned maintenance windows excluded from calculation
- Measurement period: typically rolling 12 months after final acceptance

**2.2(d) Ramp Rate and Response Time** (BESS/frequency regulation)
- Guaranteed ramp rate: {{RAMP_RATE_MW_PER_SEC}} MW/s
- Response time from idle to full output: {{RESPONSE_TIME_MS}} ms
- Grid code compliance requirements
- Testing protocol and acceptance criteria

**2.2(e) Testing Protocols**
- Capacity test: demonstrate guaranteed capacity under reference conditions
- Performance test: sustained operation over defined period (typically 30-90 days)
- Reliability run: uninterrupted operation for defined duration (typically 240-720 hours)
- Re-test rights: contractor entitled to {{NUMBER_OF_RETESTS}} re-tests within cure period
- Independent engineer: role in witnessing and certifying tests


## 3. Liquidated Damages (LDs)

### 3.1 Purpose
LDs provide pre-agreed compensation for failure to meet guaranteed milestones or performance levels, avoiding the need to prove actual loss.

### 3.2 Key Clauses

**3.2(a) Delay LDs**
- Daily rate: {{DELAY_LD_DAILY_RATE}} (typically 0.05-0.10% of contract price per day)
- Cap: {{DELAY_LD_CAP}}% of contract price (typically 10-15%)
- Trigger: failure to achieve mechanical completion / provisional acceptance by the guaranteed date
- Interaction with extension of time (EOT) provisions

**3.2(b) Performance LDs**
- Capacity shortfall LDs: calculated per MW/MWh below guaranteed capacity
- RTE shortfall LDs: calculated per percentage point below guaranteed RTE
- Availability shortfall LDs: calculated per percentage point below guaranteed availability
- Formula: LD = shortfall x rate x remaining contract period (or NPV of lost revenue)
- One-time payment or annual payment during warranty period

**3.2(c) Aggregate LD Cap**
- Total aggregate LD cap (delay + performance): {{AGGREGATE_LD_CAP}}% of contract price (typically 20-25%)
- Once aggregate cap is reached: owner's remedy is termination for contractor default
- Delay LDs credited against performance LDs (or not -- specify)

**3.2(d) Enforceability**
- LDs must be a genuine pre-estimate of loss (English law) or not unconscionable
- Norwegian law: boeteklausule (penalty clause) subject to moderation under avtaleloven § 36 if unreasonable
- FIDIC approach: include both delay damages and performance damages schedules
- Cavendish Square v Makdessi [2015] UKSC 67 considerations for English law


## 4. Battery Degradation Warranty (BESS-specific)

### 4.1 Purpose
BESS batteries degrade over time. The degradation warranty guarantees minimum state of health (SOH) at defined milestones.

### 4.2 Key Clauses

**4.2(a) Guaranteed State of Health (SOH) Milestones**

| Milestone | Guaranteed SOH (% of nameplate) |
|---|---|
| Year 1 | {{SOH_YEAR_1}}% (typically 97-98%) |
| Year 5 | {{SOH_YEAR_5}}% (typically 88-92%) |
| Year 10 | {{SOH_YEAR_10}}% (typically 80-85%) |
| Year 15 | {{SOH_YEAR_15}}% (typically 70-75%) |
| Year 20 | {{SOH_YEAR_20}}% (typically 60-70%) |

**4.2(b) Degradation Curve**
- Expected degradation curve (non-linear; calendar ageing + cycle ageing)
- Guaranteed curve vs expected curve: guaranteed is the minimum; expected is the baseline
- Throughput limitation: guaranteed SOH assumes maximum annual throughput of {{MAX_THROUGHPUT}} MWh (or number of cycles)
- Exceeding throughput: accelerated degradation excluded from warranty claim

**4.2(c) SOH Testing**
- Annual SOH test protocol (capacity test at reference conditions)
- Independent engineer or manufacturer representative to witness
- Notice period for testing: {{SOH_TEST_NOTICE}} days
- Dispute resolution for disagreement on test results

**4.2(d) Remedies for Excessive Degradation**
- Augmentation: contractor supplies additional battery modules to restore guaranteed capacity
- Replacement: defective modules replaced at contractor's cost
- Credit: monetary compensation calculated as NPV of lost revenue from reduced capacity
- Remedy election: owner's choice or contractor's choice (specify)
- Timeframe for remedy: {{REMEDY_PERIOD}} days after SOH shortfall confirmed

**4.2(e) OEM Warranty Pass-Through**
- EPC contractor to assign or pass through OEM battery warranty to owner
- Back-to-back alignment: EPC warranty terms should be at least as favourable as OEM terms
- Direct agreement: owner may require direct contractual relationship with battery OEM


## 5. Grid Connection

### 5.1 Key Clauses

**5.1(a) Connection Responsibility**
- Allocation: owner responsible for grid connection works (up to point of common coupling / PCC), or contractor responsible for balance of plant (BOP) including grid connection -- specify clearly
- Grid connection agreement: owner to obtain from grid operator (e.g., Statnett, regional DSO)
- Interface point: define physical and electrical interface between facility and grid

**5.1(b) Grid Code Compliance**
- Facility must comply with applicable grid code (e.g., Norwegian FoS/RfG, UK Grid Code, ENTSO-E requirements)
- Reactive power capability, frequency response, fault ride-through
- Contractor's obligation to design for grid code compliance
- Grid code changes: change in law provisions apply

**5.1(c) Curtailment Risk**
- Definition: grid operator instruction to reduce or cease output
- Risk allocation: curtailment risk typically borne by owner (as it depends on grid conditions beyond contractor's control)
- Revenue loss from curtailment: excluded from availability calculations
- Compensation: owner bears curtailment risk unless caused by contractor's design fault

**5.1(d) Metering and Measurement**
- Revenue-grade metering at PCC (calibrated to applicable standards)
- Backup metering and data logging
- Metering disputes: reference to independent calibration
- Data ownership and access rights


## 6. Commissioning and Acceptance

### 6.1 Key Clauses

**6.1(a) Mechanical Completion**
- Definition: all works substantially complete, systems installed, ready for testing
- Mechanical completion certificate issued by contractor, confirmed by owner/independent engineer
- Punchlist/snagging: minor defects listed; must be rectified within agreed timeframe
- Mechanical completion triggers: start of testing period; potential start of delay LD relief

**6.1(b) Provisional Acceptance (PAC)**
- Triggers: successful completion of performance tests (capacity, RTE, availability)
- PAC certificate issued when all performance guarantees demonstrated
- Risk transfer: care, custody, and control transfers from contractor to owner at PAC
- Insurance transition: contractor's CAR/EAR policy to owner's operational insurance
- Commencement of warranty period (typically 2-5 years from PAC)

**6.1(c) Final Acceptance (FAC)**
- Triggers: expiry of defects notification period (DNP) + all defects rectified + all retentions released
- FAC certificate: final sign-off; releases retention monies and performance bonds
- Typically 12-24 months after PAC

**6.1(d) Deemed Acceptance**
- If owner fails to issue PAC/FAC certificate within {{DEEMED_ACCEPTANCE_DAYS}} days after contractor's application and no valid grounds for refusal: deemed accepted
- Protects contractor from unreasonable withholding of acceptance
- Owner's right to reject: must provide specific technical grounds in writing within the notice period


## 7. Decommissioning

### 7.1 Key Clauses

**7.1(a) Decommissioning Obligations**
- Party responsible for decommissioning at end of operational life or lease term
- Scope: removal of all above-ground structures, foundations (to specified depth), cables, restoration of land to original or agreed condition
- Compliance with environmental regulations and permit conditions
- Hazardous materials (battery cells, transformer oil): specialist disposal required

**7.1(b) Decommissioning Security**
- Bond, guarantee, or escrow fund to cover estimated decommissioning costs
- Amount: {{DECOMMISSIONING_SECURITY}} (updated periodically based on revised cost estimates)
- Mechanism for updating: independent cost estimate every {{DECOM_UPDATE_YEARS}} years
- Release: upon satisfactory completion of decommissioning and regulatory sign-off

**7.1(c) Environmental Remediation**
- Baseline environmental survey conducted before construction commencement
- Obligation to remediate contamination caused during construction or operation
- Standard: restore to baseline condition or agreed remediation standard
- Liability for pre-existing contamination: excluded from contractor's obligations

**7.1(d) Recycling and Disposal**
- Battery recycling: compliance with EU Battery Regulation (Regulation 2023/1542) and applicable national legislation
- Documentation: chain of custody for hazardous waste, recycling certificates
- Extended producer responsibility (EPR) allocation


## 8. Change in Law

### 8.1 Purpose
Allocates risk for legislative or regulatory changes that affect project economics after contract signing.

### 8.2 Key Clauses

**8.2(a) Definition of Change in Law**
- Any new law, regulation, or binding interpretation issued after the agreement date (or specified reference date)
- Includes: tax law changes, environmental regulations, grid code amendments, planning law, health and safety
- Excludes: changes that were published or reasonably foreseeable before the reference date

**8.2(b) Discriminatory vs General Change in Law**
- Discriminatory: affects only the project, the technology type, or a small class of entities -- higher risk allocation to owner/off-taker
- General: affects all businesses -- typically borne by the party impacted

**8.2(c) Allocation**
- Tax law changes affecting project revenue: typically owner's risk (compensated through tariff adjustment or indemnity)
- Subsidy regime changes (e.g., el-sertifikater, capacity market changes): specify whether risk sits with owner or shared
- Environmental compliance cost increases: shared or allocated to contractor if within scope of design
- Grid code changes requiring retrofitting: typically owner's risk if change is post-PAC; contractor's risk if pre-PAC

**8.2(d) Remedy**
- Cost pass-through: incremental costs resulting from change in law added to contract price
- Schedule relief: extension of time for delays caused by change in law
- Termination: right to terminate if change in law makes project economically unviable (compensation on defined basis)


## 9. Environmental and Permitting

### 9.1 Key Clauses

**9.1(a) Environmental Impact Assessment (EIA)**
- Owner's obligation to obtain EIA approval before construction commences
- Contractor's obligation to comply with EIA conditions during construction and commissioning
- Monitoring: ongoing environmental monitoring obligations during operation

**9.1(b) Permit Conditions**
- Compliance matrix: list all permits with conditions, responsible party, and compliance status
- Permit transfer: if permits held by contractor, mechanism to transfer to owner at PAC
- Permit renewal: responsibility for ongoing permit renewals during operational phase

**9.1(c) Environmental Compliance During Operation**
- Emissions monitoring (if applicable)
- Noise limits: compliance with permit conditions and applicable regulations
- Biodiversity: habitat management plans, bird/bat monitoring (for wind)
- Water discharge: permits for cooling water, surface water management

**9.1(d) Carbon Credits and Offsets**
- Ownership of carbon credits, guarantees of origin (GoO), or renewable energy certificates (RECs) generated by the facility
- Default: owner of the facility owns the credits unless expressly assigned
- Registration: owner to register with applicable registry (e.g., Norwegian GoO registry, EU ETS)

**9.1(e) BESS-Specific Environmental**
- Fire safety: compliance with NFPA 855, IEC 62933-5-2, or applicable national standards
- Thermal runaway propagation prevention
- Battery electrolyte containment
- Emergency response plan required before commissioning


## Drafting Notes

1. **Template integration**: these clauses supplement the standard sections. When generating an energy/BESS agreement, replace or augment the following standard sections:
   - Section 3 (Scope): incorporate EPC scope and employer's requirements
   - Section 4 (SLAs): replace with Performance Guarantees (section 2 above)
   - Section 12 (Warranties): add degradation warranty
   - Section 13 (Liability): adjust caps to reflect LD regime
   - Section 16 (Termination): add specific termination triggers (aggregate LD cap reached, prolonged force majeure, failure to achieve PAC)
   - Section 18 (Force Majeure): expand for energy-specific events (grid failure, curtailment)

2. **FIDIC alignment**: for international EPC projects, consider basing the agreement on FIDIC Silver Book (EPC/Turnkey) with bespoke amendments, rather than drafting from scratch.

3. **Norwegian-law considerations**: for Norwegian-law energy contracts, note that boeteklausule (penalty clauses including LDs) are subject to judicial moderation under avtaleloven § 36 if unreasonable. Draft LDs as genuine pre-estimates of loss with supporting calculations.

4. **Insurance**: energy/BESS projects require specialised insurance: Construction All Risks (CAR) / Erection All Risks (EAR) during construction; operational all risks, business interruption, third-party liability, and (for BESS) battery-specific cover during operation.

5. **Lender requirements**: if project-financed, the agreement must be reviewed for bankability. Lenders will require direct agreements (step-in rights), assignment of key contracts, and specific cure period provisions.
