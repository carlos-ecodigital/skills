# Data Center Permitting in the Netherlands

## 1. National Policy Framework

### National Data Center Strategy
The Dutch government regulates data center development through the Nationale Omgevingsvisie (NOVI) and subsequent policy letters. Data centers are recognized as critical digital infrastructure but face increasing scrutiny regarding energy consumption, landscape impact, and resource use.

### Hyperscale Moratorium (February 2022)
The Cabinet issued a voorbereidingsbesluit (preparatory decision) imposing a nine-month moratorium on new hyperscale data centers nationwide.

**Definition of Hyperscale:**
- Floor area exceeding 10 hectares (100,000 m2)
- Electrical consumption exceeding 70 MW

**Scope:**
- Applied nationwide except municipalities of Hollands Kroon and Het Hogeland (pre-existing commitments)
- Building applications for hyperscale data centers postponed; permits could not be granted
- Duration: 9 months, allowing time for new zoning policy development

**Current Status (2025-2026):**
The moratorium's formal term expired, but its effects persist through provincial and municipal policy restrictions. The government continues developing permanent siting criteria. Controversy in January 2026 arose when Microsoft received permits in Amsterdam by splitting a hyperscale facility into three separate applications, circumventing the moratorium.

## 2. Provincial and Municipal Restrictions

### Noord-Holland Province
The province adopted its own datacenter strategy (Datacenterstrategie Noord-Holland) on 31 January 2022.

**Key Rules:**
- Applies to new data centers with area > 2,000 m2 AND electricity connection >= 5 MVA
- New data centers permitted only in designated industrial areas of:
  - Amsterdam
  - Haarlemmermeer
  - Hollands Kroon
- Provincial omgevingsverordening restricts data center development outside these areas
- Waste heat utilization required as condition for new permits

### Amsterdam Municipality
- 2019: One-year moratorium on new data centers (Amsterdam + Haarlemmermeer)
- Post-moratorium policy: data centers required to explore waste heat utilization for heating nearby homes
- Strict spatial planning: data centers only in designated areas within Westpoort and surrounding industrial zones
- Energy efficiency requirements exceed national minimums

### Other Provinces
Each province can impose its own restrictions through the provinciale omgevingsverordening. Check the specific provincial rules for:
- Zuid-Holland (Rotterdam port area, Drechtsteden)
- Groningen (Eemshaven area, seaport data centers)
- Flevoland (Zeewolde -- project controversially approved and later scaled back)

## 3. Required Permits and Procedures

### 3.1 Spatial Planning (Omgevingsplan)

**If data center fits within current omgevingsplan:**
- Binnenplanse omgevingsplanactiviteit
- Reguliere procedure (8 weeks + 6 weeks extension)
- Bevoegd gezag: gemeente (B&W)

**If data center does NOT fit within current omgevingsplan:**
- **Option A: Buitenplanse omgevingsplanactiviteit (bopa)**
  - Gemeente may choose reguliere or uitgebreide procedure
  - If uitgebreide: 26 weeks, mandatory participatie, no automatic grant
  - Often triggers plan-MER (see section 5)
- **Option B: Omgevingsplan amendment**
  - Gemeente changes the omgevingsplan to accommodate data centers
  - Triggers plan-MER if framework-setting for future m.e.r.-plichtige activities
  - Longer timeline (6-18 months)
  - Subject to provincial approval (reactieve aanwijzing possible)

### 3.2 Building Permit (Bbl)

**Gevolgklasse (consequence class):**
- Most data centers: gevolgklasse 2 or 3 (due to size, height, structural complexity)
- Gevolgklasse 3: requires omgevingsvergunning bouwtechnische activiteit
- Gevolgklasse 2: may require omgevingsvergunning depending on complexity
- Gevolgklasse 1: bouwmelding (notification) to gemeente + private kwaliteitsborger

**Key Bbl Requirements:**
- Brandveiligheid (fire safety): brandcompartimentering, vluchtwegen, sprinklers
- Constructieve veiligheid: structural integrity calculations
- Energieprestatie: BENG requirements for new construction (though data centers have specific energy profiles)
- GACS (Building Automation and Control System) mandatory from 1 January 2026 for installations > 290 kW capacity

### 3.3 Environmental Permit (Bal -- Milieubelastende Activiteit)

Data centers trigger multiple milieubelastende activiteiten under the Bal:

**Noise (Geluid):**
- Cooling systems, HVAC, emergency generators
- Bal general rules for geluid (Art. 4.17-4.21)
- Bkl omgevingswaarden for geluid at gevoelige gebouwen
- Night-time restrictions particularly relevant

**Air Quality (Luchtkwaliteit):**
- Emergency diesel generators: NOx, PM2.5, PM10 emissions
- Bal Chapter 3: stookinstallatie rules apply
- Depending on aggregate generator capacity, may need omgevingsvergunning for milieubelastende activiteit
- NOx emissions feed into AERIUS stikstof calculations

**Emergency Generators:**
- Diesel generators are classified as stookinstallaties under Bal
- Aggregate thermal capacity > 1 MW typically triggers additional rules
- Testing hours subject to restrictions (typically < 500 hours/year for emergency use)
- Emissions must be calculated and reported
- May require NOx-compensatie in areas with stikstofdepositie issues

### 3.4 Water Permits

**Cooling Water:**
- Open-loop cooling systems require watervergunning (Waterwet via Omgevingswet)
- Grondwateronttrekking (groundwater extraction): provincial permit (GS)
- Lozing op oppervlaktewater: waterschap permit for discharge of heated water
- Temperature differential limits apply (typically max 3°C increase at mixing zone boundary)

**Closed-Loop Systems:**
- Reduced permit burden but may still require lozing of treatment chemicals
- Anti-legionella treatment wastewater discharge

### 3.5 Fire Safety

- Veiligheidsregio consultation mandatory for large data centers
- Gebruiksmelding or omgevingsvergunning voor brandveilig gebruik (depending on size/use)
- UPS battery rooms: PGS 37 applies if lithium-ion batteries used
- Diesel fuel storage: PGS 30 (liquid fuels) applies

## 4. Waste Heat Obligation (Restwarmteplicht)

### Under Wcw (Wet collectieve warmte -- effective mid-2026)
- Data centers generating significant waste heat may be designated as warmtebron (heat source)
- Gemeente can include waste heat supply obligations in warmtekavel conditions
- Data center operators may be required to make waste heat available at reasonable cost

### Under EU Energy Efficiency Directive (EED) Recast
- EU-wide requirements for data centers to report on energy efficiency
- PUE (Power Usage Effectiveness) reporting becoming mandatory
- Heat recovery plans required for new data centers above certain thresholds
- Netherlands implementing EED recast provisions into national law

### Practical Heat Recovery
- Waste heat temperature from data centers: typically 25-35°C (low grade)
- Requires heat pump for district heating integration (temperature uplift to 70°C+)
- Amsterdam's Westpoort Warmte (Vattenfall/Municipality JV) accepting data center waste heat
- Business case depends on proximity to heat demand and heat pump costs

## 5. Environmental Impact Assessment (MER)

### When MER is Triggered
Data centers are not separately listed in Ob Bijlage V. Triggers include:

**Category J10 (Industrieterrein):**
- Aanleg of wijziging of uitbreiding of inrichting of bedrijventerrein
- If omgevingsplan change creates space for industrial development

**Category J11 (Stedelijk ontwikkelingsproject):**
- Bouw of uitbreiding of wijziging of stedelijk ontwikkelingsproject
- Large data centers in urban/suburban areas often qualify
- No fixed threshold; m.e.r.-beoordeling required if project is listed

**Plan-MER:**
- Required when omgevingsplan change is framework-setting (kaderstellend)
- Almost always applies when gemeente rezones land for data center use

### Typical MER Scope for Data Centers
- Energy consumption and CO2 footprint
- Noise impact on surrounding area
- Air quality (NOx/PM from generators)
- Water use and thermal discharge
- Visual/landscape impact
- Traffic generation during construction and operation
- Ecological impact (Natura 2000, soortenbescherming)
- Alternatives assessment (location, scale, technology)

## 6. Sustainability and Reporting

### CSRD (Corporate Sustainability Reporting Directive)
- Large data center operators subject to CSRD from 2025 reporting year
- Double materiality assessment required
- Energy, water, waste heat metrics must be disclosed
- EU Taxonomy alignment reporting

### EU Energy Efficiency Directive Data Center Provisions
- Reporting obligations for data centers > 500 kW IT capacity
- PUE, WUE (Water Usage Effectiveness), renewable energy share
- First reports due 2024 (for 2023 data), ongoing annual reporting
- Member state reporting to European Commission database

## 7. Typical Permitting Timeline

| Phase | Duration | Activities |
|---|---|---|
| **Pre-development** | 3-6 months | Site selection, feasibility, pre-consultation (vooroverleg) with gemeente |
| **Spatial planning** | 6-18 months | Omgevingsplan amendment or bopa application; plan-MER if needed |
| **Building permit** | 3-8 months | Omgevingsvergunning bouwtechnische activiteit |
| **Environmental permits** | 3-6 months | Milieubelastende activiteiten; watervergunning |
| **Grid connection** | 12-120 months | TenneT/DSO application; depends on transportschaarste |
| **Nature permits** | 3-12 months | AERIUS calculation; ontheffing if needed |
| **Total critical path** | 18-36 months | Excluding grid connection (parallel track) |

**Critical Path Risk Factors:**
- Grid congestion (transportschaarste) can add years to timeline
- Stikstof issues can block permits entirely
- Political opposition may delay omgevingsplan changes
- MER procedure adds 6-12 months if triggered
- Bezwaar/beroep by objectors can add 12-24 months

## 8. Stakeholder Management

### Key Stakeholders
- Gemeente (B&W and gemeenteraad)
- Provincie (GS, provincial council)
- Omgevingsdienst (environmental service executing Bal enforcement)
- Veiligheidsregio (fire/safety authority)
- Waterschap (water authority)
- Netbeheerder (TenneT, Liander/Stedin/Enexis)
- Omwonenden (neighbors/local residents)
- Milieuorganisaties (environmental groups)
- Commissie m.e.r. (EIA commission, if MER triggered)

### Participatie Strategy
Under the Omgevingswet, participatie is structurally encouraged (reguliere procedure) or mandatory (uitgebreide procedure). For large data centers:
- Early engagement with gemeente (principeverzoek or vooroverleg)
- Neighborhood information sessions (informatieavonden)
- Environmental group consultation
- Business community alignment
- Document participatie process for permit application (verplichte participatieparagraaf)

## Sources and References

- rijksoverheid.nl/onderwerpen/datacenters
- iplo.nl (Informatiepunt Leefomgeving)
- Omgevingswet, Bal, Bbl, Bkl, Ob (wetten.nl)
- Datacenterstrategie Noord-Holland (2022)
- EU Energy Efficiency Directive 2023/1791 (recast)
- Wet collectieve warmte (Wcw) -- Stb. 2025
