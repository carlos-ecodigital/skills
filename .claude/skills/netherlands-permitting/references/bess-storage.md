# BESS (Battery Energy Storage System) Permitting in the Netherlands

## 1. Regulatory Framework Overview

BESS/EOS (Energieopslagsysteem) permitting in the Netherlands is governed by an evolving framework. As of February 2026, dedicated legislation for EOS is still being developed. The current regime relies on:

- **Omgevingswet** (general framework)
- **Bal** (milieubelastende activiteiten -- amendment expected ~2027 to include EOS)
- **PGS 37-1** (guideline for energy storage systems)
- **PGS 37-2** (guideline for lithium-ion battery storage)
- **Bevi** (Besluit externe veiligheid inrichtingen -- external safety, threshold at 10,000 kg)
- **Bbl** (building rules for enclosures and transformer stations)
- **EU Battery Regulation 2023/1542** (lifecycle, sustainability, labeling)

## 2. PGS 37-1: Energy Storage Systems (EOS/BESS)

### Scope
PGS 37-1 covers the safe operation of large coupled lithium battery systems used for:
- Grid-scale energy storage (utility-scale BESS)
- Neighborhood batteries (buurtbatterijen) for solar storage
- Wind farm co-located storage
- Grid stabilization and frequency regulation

**Applicability threshold:** Systems with capacity above 20 kWh

### Key Risks Addressed
- **Thermal runaway** (onbeheersbare brand): cascading cell failure producing extreme heat
- **Toxic gas release**: pyrolysis products include HF, HCl, CO, SO2
- **Explosive atmosphere**: vented gases may form explosive mixtures
- **Firefighting water contamination**: corrosive, poisonous runoff
- **Electrical hazards**: high DC voltage even during failure

### PGS 37-1 Typicals (Installation Configurations)

| Typical | Description | Key Requirements |
|---|---|---|
| **Typical 1** | Indoor EOS in accessible building | Fire compartmentalization, ventilation, detection |
| **Typical 2** | Indoor EOS in non-accessible enclosure within building | Enclosure integrity, suppression, monitoring |
| **Typical 3** | Outdoor EOS park with non-accessible enclosures | Safety distances between units and to environment |
| **Typical 4** | Mobile/temporary EOS | Temporary measures, fire water alternative |

### Safety Measures (Key Requirements)

**Fire Prevention:**
- Battery Management System (BMS) with cell-level monitoring
- Temperature, voltage, current monitoring per module
- Automatic disconnect at threshold breach
- Climate control (HVAC) for temperature regulation

**Fire Detection and Suppression:**
- Gas detection (off-gas detection for early thermal runaway warning)
- Smoke detection in enclosures
- Fire suppression system (water mist, inert gas, or combination)
- Bluswatervoorziening (fire water supply): minimum 1,000 L/min (M56)

**Safety Distances (Veiligheidsafstanden):**
- Between individual EOS units within a cluster
- Between EOS clusters
- Between EOS park boundary and external objects (kwetsbare objecten, beperkt kwetsbare objecten)
- Specific distances depend on capacity, configuration, and RIVM risk calculation

**Containment:**
- Opvang van bluswater (fire water containment) to prevent environmental contamination
- Lekbakken (spill containment) for cooling fluids and electrolyte
- Drainage to separate collection system (not into riolering or oppervlaktewater)

### Legal Status of PGS 37-1

**Current (pre-Bal amendment):**
- Established December 2023 by Bestuurlijk Omgevingsberaad (BOb)
- Not yet directly legally binding as Bal general rules
- Used as "working documents" and best practice guidance
- Enforceable through:
  - Permit conditions (vergunningvoorschriften) if EOS supports a licensed activity
  - Zorgplicht (duty of care) under Bal Art. 2.11-2.13
  - Bruidsschat (transitional rules) via omgevingsplan (Art. 22.44 Invoeringsbesluit)

**Future (post-Bal amendment, expected ~2027):**
- EOS storage of electricity will be designated as milieubelastende activiteit in Bal
- PGS 37-1 requirements become directly binding general rules
- Competent authority: primarily gemeente (B&W)

### Implementation Timeline (Appendix J)
For existing installations, PGS 37-1 provides graduated implementation timelines:
- Immediate: BMS monitoring, emergency procedures
- 2 years: bluswatervoorziening (fire water connection)
- 3-5 years: fire detection/suppression upgrades
- Up to 10 years: full compliance for certain structural measures

**Temporary alternative for mobile EOS (pre-PGS adoption):**
Water cutting system as "last line of defense" in lieu of full 1,000 L/min fire water connection, applicable only to systems that entered the market before final PGS 37-1 adoption.

## 3. PGS 37-2: Lithium Battery Storage

### Scope
PGS 37-2 covers the storage of lithium-containing energy carriers (batteries and accumulators) as products, not as operational energy storage systems. Applies to:
- Warehousing of batteries (e-bike, EV, laptop, power tool batteries)
- Distribution centers handling lithium batteries
- Retail storage of lithium products

### Storage Categories

| Category | Weight | Requirements |
|---|---|---|
| Small scale | < 500 kg | Cabinet storage, basic fire detection |
| Medium scale | 500 - 10,000 kg | Dedicated storage area, sprinkler system, containment |
| Large scale | > 10,000 kg | Full external safety assessment, Bevi applies |

## 4. External Safety (Externe Veiligheid)

### Bevi Threshold
When lithium-ion battery storage exceeds **10,000 kg**, the Besluit externe veiligheid inrichtingen (Bevi) applies, requiring:

- **Externe Veiligheidsrapportage (EVR)** or **Quantitative Risk Assessment (QRA)**
- Plaatsgebonden risico (location-specific risk): max 10^-6/year at boundary of kwetsbaar object
- Groepsrisico (societal risk): assessment against orientation value; verantwoordingsplicht
- Minimum distances to:
  - Kwetsbare objecten (vulnerable objects: homes, schools, hospitals)
  - Beperkt kwetsbare objecten (limited vulnerable objects: offices, shops)

### RIVM Risk Calculation Method (April 2025)
RIVM published a standardized calculation method for:
- Environmental safety risks of EOS/BESS
- Large battery storage facilities
- Inputs: capacity (kWh/MWh), chemistry, configuration, enclosure type
- Outputs: risk contours for plaatsgebonden risico and groepsrisico
- Required for external safety assessment in permit applications

### Seveso III / BRZO 2015
Large-scale BESS may trigger Seveso/BRZO classification depending on:
- Quantity of hazardous substances (electrolyte, cooling fluids)
- Lithium-ion batteries above certain thresholds
- If triggered: BRZO inspection regime, Veiligheidsrapport (VR), preventiebeleid
- Competent authority shifts to provincie (GS) for Seveso establishments

## 5. Building Permits (Bbl)

### BESS Enclosures and Containers
- Standalone BESS containers: typically gevolgklasse 1 (bouwmelding + kwaliteitsborger)
- Transformer stations: gevolgklasse 1 or 2 depending on size/height
- Grid connection infrastructure (kabel- en leidingentracé): may be vergunningsvrij if underground

### Fire Compartmentalization
- BESS buildings/enclosures must meet brandcompartimentering requirements
- Maximum brandcompartiment size depends on risk classification
- WBDBO (weerstand tegen branddoorslag en brandoverslag) requirements per Bbl

## 6. Environmental Permits

### Noise (Geluid)
- BESS inverters and cooling systems generate noise
- Bal general rules for geluid apply at nearest geluidgevoelig gebouw
- Night-time limits more restrictive (typically LAr,LT <= 40 dB(A))
- Acoustic study (akoestisch onderzoek) typically required for permit application

### Emissions to Air
- Minimal during normal operation
- Thermal runaway event: toxic gas release (HF, CO, particulates)
- Emergency ventilation systems must be designed for worst-case scenario
- No routine emission permit needed; covered by safety measures

### Water and Soil
- Opvangvoorziening for contaminated fire water (mandatory under PGS 37-1)
- Bodembescherming: spill containment for coolant and electrolyte
- Grondwatermonitoring if located near drinkwaterwingebied

## 7. Grid Connection for BESS

### TenneT (High Voltage / Extra High Voltage)
- Utility-scale BESS (typically > 10 MW) connects at HV/EHV level
- Application via TenneT's aansluitproces
- Current wait times: varies by location; heavily impacted by transportschaarste
- TenneT April 2025: 9.1 GW off-peak capacity allocated via flexible contracts (TBTR)
- BESS applications dominated the 70+ GW of demand for these contracts

### DSO (Regional Grid)
- Smaller BESS (< 10 MW) connects via regional netbeheerder
- Same transportschaarste issues at regional level
- Cable pooling: BESS can share connection with solar/wind under Energiewet

### Cable Pooling for BESS
- Under Energiewet (effective 2026): storage installations explicitly included in cable pooling
- ACM already permitting cable pooling with batteries (since November 2024)
- Minimum shared connection capacity: 2 MVA
- Maximum 4 parties per shared connection
- Reduces grid connection waiting time and cost

## 8. SDE++ for BESS
As of 2025-2026, standalone BESS is **not directly eligible** for SDE++ subsidy. However:
- BESS co-located with SDE++-subsidized renewable generation may optimize subsidy value
- BESS revenue stacking: FCR, aFRR, energy arbitrage, imbalance market
- Future SDE++ rounds may include storage categories (policy under development)

## 9. MER/m.e.r. for BESS

### Direct MER Obligation
- No specific BESS/EOS category in Ob Bijlage V
- Large BESS (> 100 MW) may trigger via energy industry categories

### m.e.r.-Beoordeling
- May be triggered via:
  - Hazardous substance storage categories (if > Bevi threshold)
  - Industrial area development (J10) if omgevingsplan change needed
  - Provincial discretion for large projects

### Plan-MER
- Required when gemeente changes omgevingsplan to accommodate BESS
- Particularly if plan is kaderstellend for future MER-plichtige activities

## 10. Typical BESS Permitting Timeline

| Phase | Duration | Activities |
|---|---|---|
| **Feasibility** | 2-4 months | Site selection, grid pre-assessment, PGS 37-1 gap analysis |
| **Pre-application** | 1-3 months | Vooroverleg with gemeente, Veiligheidsregio consultation |
| **Spatial planning** | 3-12 months | Omgevingsplan check; bopa if needed |
| **Permits** | 3-8 months | Omgevingsvergunning (milieu + bouwen), external safety |
| **Grid connection** | 6-60+ months | Application to TenneT/DSO; cable pooling assessment |
| **Construction** | 6-12 months | EPC, commissioning, energiekeuring |
| **Total** | 12-24 months | Excluding grid (parallel track) |

## 11. Market Context (2025-2026)

- ~250 MW BESS installed in Netherlands
- ~840 MW permitted or under construction
- ~690 MW announced
- TenneT projects 5 GW standalone BESS + 1 GW colocated by 2030
- Scale of projects growing: first 4-hour BESS operational February 2025
- 300+ MW projects in development
- Land scarcity and agricultural zoning are significant siting challenges

## Sources and References

- PGS 37-1 (publicatiereeksgevaarlijkestoffen.nl)
- PGS 37-2 (publicatiereeksgevaarlijkestoffen.nl)
- IPLO: iplo.nl/thema/externe-veiligheid/publicatiereeks-gevaarlijke-stoffen-pgs/pgs-37-1-37-2/
- RIVM: Risk calculation method for EOS (April 2025)
- Rabobank: Dutch BESS market analysis (2025)
- TenneT: tennet.eu/nl-en/battery-energy-storage-systems-bess
- Energy Storage NL: energystoragenl.nl
- EU Battery Regulation 2023/1542
