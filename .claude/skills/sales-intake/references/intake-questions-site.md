# Site Track -- Intake Questions (Supply Side)

ICP-specific question modules for partners enabling DE's infrastructure. Each ICP module extends the shared base questions from `intake-questions-shared.md`.

**Critical framing:** Site Track ICPs are PARTNERS, not customers. They provide land, grid access, and heat offtake. DE provides free heat and (indirectly) fast-tracks permits via the restwarmteplicht. Language must reflect partnership, zero-investment framing.

**ICPs in this track:**
- **S-GRW** -- Grower (greenhouse operators): tomato, pepper, flower, cannabis growers in NL
- **S-DHN** -- District Heating (warmtenet operators): municipal utilities, energy companies, housing corporations
- **S-IND** -- Industrial Heat (factories, food processors): process heat users with decarbonization mandates

---

## S-GRW: Grower Module

**Language default:** Dutch for questions, English in parentheses. Growers prefer Dutch communication.

### Phase 1 -- Identity & Context (+3 questions)

#### Q1.4-GRW -- Bedrijfsprofiel / Farm Profile
**Text:** "Wat voor bedrijf is het? Welk gewas, hoeveel hectare, welke regio? (What do they grow, how big, which region?)"
**Why:** Crop type determines heating profile (tomatoes year-round, flowers seasonal). Size determines scale viability. Region determines grid zone and congestion status.
**Feeds:** Opportunity Brief (section 1), Lead Qualification Score (capacity/grid value), site matching
**Auto-fill from:** KvK, Google Maps satellite, Glastuinbouw Nederland data

#### Q1.5-GRW -- Eigendomssituatie / Ownership
**Text:** "Is het eigen grond of huur? Wie is de eigenaar van de kaslocatie? (Owned or leased land? Who owns the greenhouse site?)"
**Why:** DE needs recht van opstal (right of superficies) for the DC plot. Leased land requires landlord consent and adds complexity. Owned = faster.
**Feeds:** Opportunity Brief (section 8), Lead Qualification Score (decision authority), legal routing
**Red flag:** If leased with no landlord contact → significant delay risk

#### Q1.6-GRW -- Vereniging / Association
**Text:** "Zijn ze lid van een telersvereniging of coöperatie? (Part of a grower association or cooperative?)"
**Why:** Association members often have collective energy contracts and may need association approval. Also a source for additional grower leads.
**Feeds:** Opportunity Brief (section 2, 8), stakeholder mapping, future lead sourcing

### Phase 2 -- Need & Problem (+3 questions)

#### Q2.5-GRW -- Gaskosten / Gas Costs
**Text:** "Wat betalen ze nu aan gas per jaar? Weten ze hun verbruik in m3 of MWh? (Annual gas spend? Consumption in m3 or MWh?)"
**Why:** Gas cost is THE pain point. DE replaces gas with free waste heat. The bigger the gas bill, the more compelling the proposition. Also validates scale viability.
**Feeds:** Lead Qualification Score (capacity/grid value, 30% weight), Opportunity Brief (section 3, 4, 9), Validation (benchmark: expect EUR 500K-5M/year for viable growers)
**Red flag:** Gas bill <EUR 200K/year → scale may be too small

#### Q2.6-GRW -- WKK Status / CHP Status
**Text:** "Hebben ze een WKK (warmtekrachtkoppeling)? Hoe oud, wanneer loopt het contract af? (Do they have a CHP? Age, contract expiry?)"
**Why:** Most Dutch growers use CHP (combined heat and power). CHP contract expiry is a critical trigger event. If the CHP is new, the deal timeline extends 5-10 years.
**Feeds:** Opportunity Brief (section 4, 7), Lead Qualification Score (timeline match), trigger assessment
**Conditional:** If WKK contract <3 years remaining → hot trigger; if >5 years → park for later

#### Q2.7-GRW -- Bestaande verduurzaming / Existing sustainability
**Text:** "Hebben ze al andere warmtebronnen onderzocht? Geothermie, biomassa, warmtepomp? (Have they explored other heat sources? Geothermal, biomass, heat pump?)"
**Why:** Competitive landscape. If they've explored and rejected geothermal (too expensive, no guarantee), DE's proposition is even stronger. If they're committed to another source, timing changes.
**Feeds:** Opportunity Brief (section 7), competitive positioning, Lead Qualification Score

### Phase 3 -- Technical / Ops (+5 questions)

#### Q3.4-GRW -- Netaansluiting / Grid Connection
**Text:** "Wat is hun huidige netaansluiting? Hoeveel MVA? Is er ruimte voor uitbreiding? (Current grid connection? MVA capacity? Room for expansion?)"
**Why:** Grid connection is the #1 value driver (30% scoring weight). DE's model depends on using the existing grid connection. A large grid connection (>10 MVA) at a site with low congestion is the ideal.
**Feeds:** Lead Qualification Score (capacity/grid value, 30%), Opportunity Brief (section 3, 5), site feasibility
**Red flag:** No existing grid connection or heavily congested zone → major blocker

#### Q3.5-GRW -- Locatie en ruimte / Location and Space
**Text:** "Is er ruimte op het terrein voor een datacenter? Hoeveel m2/hectare beschikbaar? Afstand tot de kas? (Space on site for a DC? How much? Distance to greenhouse?)"
**Why:** DE places the DC adjacent to the greenhouse. Need minimum ~2,000 m2 for a viable installation. Distance affects heat pipe costs.
**Feeds:** Opportunity Brief (section 5), site feasibility, technical design, Validation (geography)
**Auto-fill from:** Google Maps satellite imagery, kadaster

#### Q3.6-GRW -- Warmteprofiel / Heat Profile
**Text:** "Wat is hun warmtebehoefte door het jaar? Piekmaanden? Nachttemperaturen? (Heat demand profile through the year? Peak months? Night temperatures?)"
**Why:** DE's waste heat output must match the grower's heating profile. Year-round growers (tomatoes) are ideal. Seasonal growers (flowers) create off-season heat disposal challenges.
**Feeds:** Opportunity Brief (section 3, 5), technical matching, heat balance design

#### Q3.7-GRW -- Bestemmingsplan / Zoning
**Text:** "Wat is de huidige bestemming van het terrein? Weten ze of datacenter past in het bestemmingsplan? (Current zoning? Any idea if a DC fits the zoning plan?)"
**Why:** Dutch zoning (bestemmingsplan / omgevingsplan under Omgevingswet) often doesn't permit data centers in agricultural zones. The restwarmteplicht can facilitate an exception if the DC supplies waste heat to the grower.
**Feeds:** Opportunity Brief (section 8), permitting assessment, Lead Qualification Score, legal routing
**Route to:** `netherlands-permitting` for detailed assessment

#### Q3.8-GRW -- Glasvezel / Fiber
**Text:** "Is er glasvezel op de locatie of in de buurt? (Is there fiber at or near the site?)"
**Why:** A DC needs fiber connectivity. Rural greenhouse locations may lack fiber, requiring a build-out that adds cost and time.
**Feeds:** Opportunity Brief (section 5, 8), site feasibility, cost estimation
**Red flag:** No fiber within 5 km → significant additional cost

### Phase 4 -- Commercial / Financial (+2 questions)

#### Q4.4-GRW -- Grondhuur verwachting / Land Lease Expectation
**Text:** "Wat verwachten ze voor grondhuur? Hebben ze een idee van marktwaarde? (Land lease expectation? Any sense of market value?)"
**Why:** DE pays ground rent for the DC plot. Grower expectations must align with DE's project economics. Overpriced land kills the business case.
**Feeds:** Opportunity Brief (section 9), Validation (benchmark: EUR 5-15/m2/year for agricultural land in NL), commercial negotiation

#### Q4.5-GRW -- Bereidheid samenwerking / Partnership Willingness
**Text:** "Staan ze open voor een langetermijnpartnerschap (15-25 jaar)? Of zoeken ze iets korter? (Open to long-term partnership 15-25 years? Or looking for shorter?)"
**Why:** DE's project finance model requires long-term land agreements. Grower willingness to commit long-term is a deal qualifier.
**Feeds:** Lead Qualification Score (decision authority, timeline match), Opportunity Brief (section 9), contract approach

---

## S-DHN: District Heating Module

### Phase 1 -- Identity & Context (+3 questions)

#### Q1.4-DHN -- Network Profile
**Text:** "What network do they operate? Scale (connected households/buildings), age, geography."
**Why:** Network size determines heat demand volume. New networks are expanding and need new sources. Old networks may have locked-in supply contracts.
**Feeds:** Opportunity Brief (section 1, 3), Lead Qualification Score (baseload demand), site matching

#### Q1.5-DHN -- Ownership & Governance
**Text:** "Who owns the network? Municipal, private, mixed? Who makes decisions?"
**Why:** Municipal ownership means political governance, longer timelines, public procurement rules. Private = faster but possibly tighter margins. Mixed = complex stakeholder mapping.
**Feeds:** Opportunity Brief (section 2), Lead Qualification Score (decision authority, 20% weight), stakeholder mapping

#### Q1.6-DHN -- Regulatory Status
**Text:** "Where are they with the Wcw (Wet collectieve warmtevoorziening)? Do they have a warmtekavel designation?"
**Why:** The Wcw is reshaping Dutch district heating governance. Warmtekavel designation gives them exclusive rights in a zone but also obligations (including using available waste heat -- which benefits DE).
**Feeds:** Lead Qualification Score (strategic driver, 15%), Opportunity Brief (section 4, 6), competitive positioning
**Conditional:** If warmtekavel designated → ask about zone boundaries and heat source commitments

### Phase 2 -- Need & Problem (+4 questions)

#### Q2.5-DHN -- Current Heat Sources
**Text:** "What's their current heat supply portfolio? Gas boilers, geothermal, biomass, other waste heat?"
**Why:** Maps the competitive landscape and identifies where DE fits in the heat stack. DE is most valuable as baseload (40-60C continuous supply).
**Feeds:** Opportunity Brief (section 7), portfolio positioning, Lead Qualification Score

#### Q2.6-DHN -- Wcw Compliance Gap
**Text:** "Do they have a compliance gap under the Wcw? Specifically around sustainable heat supply obligations?"
**Why:** Wcw mandates increasing proportions of sustainable heat. DC waste heat qualifies. A compliance gap = urgent regulatory driver to work with DE.
**Feeds:** Lead Qualification Score (strategic driver, 15%), Opportunity Brief (section 4), positioning angle

#### Q2.7-DHN -- Network Expansion Plans
**Text:** "Are they expanding the network? New neighborhoods, commercial zones, existing building connections?"
**Why:** Expanding networks actively seek new heat sources. A network adding 5,000 homes needs 15-25 MWth additional supply -- perfect for DE.
**Feeds:** Opportunity Brief (section 3, 5), capacity matching, Lead Qualification Score (baseload demand)

#### Q2.8-DHN -- Heat Price Structure
**Text:** "What's their current heat supply cost? Gas equivalent pricing? Marginal cost per MWth?"
**Why:** DE must price waste heat competitively vs their existing sources. Understanding their cost stack reveals where DE fits economically.
**Feeds:** Opportunity Brief (section 9), Validation (benchmark: EUR 10-25/MWh for waste heat in NL), Lead Qualification Score (budget/price fit)

### Phase 3 -- Technical / Ops (+5 questions)

#### Q3.4-DHN -- Supply Temperature Requirements
**Text:** "What supply temperature does their network run at? High temperature (>70C), mid (40-70C), low (<40C)?"
**Why:** DC waste heat is typically 30-50C. If the network requires >70C, a heat pump is needed to boost temperature, adding cost and complexity. Low-temperature networks are ideal.
**Feeds:** Opportunity Brief (section 3, 5), technical feasibility, cost estimation, Lead Qualification Score (technical fit)

#### Q3.5-DHN -- Baseload Demand
**Text:** "What's their baseload heat demand (minimum year-round, before peak)? MWth?"
**Why:** DE supplies continuous baseload heat. The baseload demand determines the minimum DC size needed to make the supply worthwhile.
**Feeds:** Lead Qualification Score (baseload demand, 20%), Opportunity Brief (section 3), sizing

#### Q3.6-DHN -- Connection Point
**Text:** "Where would the connection point be? Is there existing infrastructure (pipes, substations) nearby?"
**Why:** Heat pipe distance and connection infrastructure determine capex. A connection point >5 km from a viable DE site may kill the economics.
**Feeds:** Opportunity Brief (section 5, 8), site matching, cost estimation

#### Q3.7-DHN -- Grid Access Near Network
**Text:** "Is there sufficient electrical grid capacity near the network area for a DC site?"
**Why:** DE needs both the heat offtaker AND a viable DC site with grid access nearby. Sometimes the heat demand exists but the grid doesn't support a DC in the area.
**Feeds:** Opportunity Brief (section 5), site feasibility, Lead Qualification Score (technical fit)

#### Q3.8-DHN -- Redundancy & Backup
**Text:** "What backup heat supply do they need? What happens if the DC goes offline for maintenance?"
**Why:** District heating has reliability obligations to connected households. DE cannot be the sole heat source without redundancy arrangements.
**Feeds:** Opportunity Brief (section 3, 8), technical design, commercial terms (availability guarantees)

### Phase 4 -- Commercial / Financial (+3 questions)

#### Q4.4-DHN -- Procurement Framework
**Text:** "Is there a formal procurement framework for heat supply? Public tender required?"
**Why:** Municipal-owned networks often require public procurement, adding 6-12 months. Private networks can move faster. Understanding the process sets realistic timelines.
**Feeds:** Lead Qualification Score (decision authority, timeline match), Opportunity Brief (section 9)

#### Q4.5-DHN -- Contract Duration Appetite
**Text:** "What contract duration are they considering for heat supply? 10, 15, 20+ years?"
**Why:** DE's project finance requires long-term offtake commitments. Matching contract duration to project economics is essential.
**Feeds:** Opportunity Brief (section 9), Lead Qualification Score (timeline match), commercial structuring

#### Q4.6-DHN -- Subsidy Landscape
**Text:** "Are they pursuing any subsidies for sustainable heat? SDE++, ISDE, other?"
**Why:** Subsidies can make the economics work for borderline cases. Also reveals sophistication and timeline (SDE++ applications have specific windows).
**Feeds:** Opportunity Brief (section 9), commercial structuring, Lead Qualification Score (budget fit)

---

## S-IND: Industrial Heat Module

### Phase 1 -- Identity & Context (+2 questions)

#### Q1.4-IND -- Industry & Process
**Text:** "What industry? What's their core process that requires heat?"
**Why:** Industry determines process temperature, load profile, uptime criticality, and decarbonization pressure. Food processing, pharma, and chemicals each have different requirements.
**Feeds:** Opportunity Brief (section 1, 3), technical matching, Lead Qualification Score

#### Q1.5-IND -- ESG & Decarbonization
**Text:** "Do they have public decarbonization targets or ESG commitments? Specific deadlines?"
**Why:** Regulatory and investor pressure on industrial decarbonization is accelerating. Companies with 2030 targets and no clear path are hot leads.
**Feeds:** Lead Qualification Score (strategic driver, 15%), Opportunity Brief (section 4, 6)

### Phase 2 -- Need & Problem (+3 questions)

#### Q2.5-IND -- Current Energy Mix
**Text:** "What's their current energy setup? Gas, electric, steam, other? Annual consumption?"
**Why:** Maps the energy baseline. DE replaces a portion of gas/steam with waste heat. The larger the thermal energy bill, the more compelling the business case.
**Feeds:** Lead Qualification Score (capacity/grid value), Opportunity Brief (section 3, 7), Validation (benchmark)

#### Q2.6-IND -- Process Temperature Profile
**Text:** "What temperature do they need for their process? Inlet, outlet, peaks?"
**Why:** DC waste heat is 30-50C base. Industrial processes often need higher temperatures. If >120C, DE can only provide partial supply (preheating). If <60C, direct use is possible.
**Feeds:** Lead Qualification Score (technical fit, 20%), Opportunity Brief (section 3, 5), technical feasibility
**Red flag:** Process temp >120C → partial supply only, reduced value proposition

#### Q2.7-IND -- Energy Cost Pressure
**Text:** "How has energy cost volatility affected them? Is energy cost reduction a board-level priority?"
**Why:** Energy cost pain determines urgency and budget willingness. Board-level attention means faster decision cycles and more budget flexibility.
**Feeds:** Lead Qualification Score (strategic driver), Opportunity Brief (section 4), positioning angle

### Phase 3 -- Technical / Ops (+4 questions)

#### Q3.4-IND -- Load Profile
**Text:** "What's their heat consumption pattern? 24/7, shift-based, seasonal, batch?"
**Why:** DC waste heat is continuous (24/7). Ideal match is continuous process heat demand. Batch or shift-based demand creates heat disposal challenges during off-periods.
**Feeds:** Opportunity Brief (section 3, 5), technical matching, Lead Qualification Score (technical fit)

#### Q3.5-IND -- Process Integration Risk
**Text:** "How critical is uninterrupted heat supply to their process? What happens if heat supply drops for an hour?"
**Why:** Some industrial processes (pharma, chemicals) cannot tolerate supply interruptions. This determines redundancy requirements and contractual obligations.
**Feeds:** Opportunity Brief (section 3, 8), technical design, commercial terms (availability guarantees)
**Red flag:** Zero-tolerance interruption + no backup → high risk for DE

#### Q3.6-IND -- Site Proximity
**Text:** "Where is their facility? Is there land nearby suitable for a DC?"
**Why:** Heat pipes are expensive (EUR 1-3M/km). The industrial facility must be within reasonable distance of a viable DC site with grid access.
**Feeds:** Opportunity Brief (section 5), site matching, cost estimation

#### Q3.7-IND -- Grid Access Near Facility
**Text:** "Is there sufficient grid capacity in their area for a DC installation?"
**Why:** Same as DHN -- need both heat demand AND grid access. Industrial zones often have better grid than residential, but not always.
**Feeds:** Opportunity Brief (section 5), site feasibility, Lead Qualification Score

### Phase 4 -- Commercial / Financial (+2 questions)

#### Q4.4-IND -- Energy Budget
**Text:** "What's their annual energy spend? Do they have a specific budget for heat supply alternatives?"
**Why:** Industrial energy budgets are large but allocated. Understanding the budget envelope determines pricing flexibility and project economics.
**Feeds:** Lead Qualification Score (budget/price fit), Opportunity Brief (section 9), Validation (benchmark)

#### Q4.5-IND -- Contract & Procurement
**Text:** "How do they procure energy today? Direct contracts, brokers, procurement tenders?"
**Why:** Procurement sophistication varies. Some industrials have dedicated energy teams; others use brokers. This determines the sales approach and who we need to convince.
**Feeds:** Opportunity Brief (section 2, 9), Lead Qualification Score (decision authority), sales approach

---

## Secondary Conditionals (Within ICP Modules)

### S-GRW Conditionals
- **If gas bill <EUR 200K/year:** "Hoeveel hectare kas? Zijn er buurkwekers die mee willen doen? (How many ha? Neighboring growers interested?)" -- scale viability check
- **If congested grid zone:** "Is er een transportbeperking? Kennen ze de netbeheerder contactpersoon? (Transport restriction? Do they know the DSO contact?)" -- grid feasibility
- **If no fiber within 5 km:** "Zijn er plannen voor glasvezeluitrol in de regio? (Are there fiber rollout plans?)" -- connectivity assessment
- **If WKK contract >5 years remaining:** "Wanneer loopt het WKK contract af? We kunnen alvast plannen. (When does CHP contract expire? We can plan ahead.)" -- park for later
- **If leased land:** "Wie is de grondeigenaar? Staan zij ook open voor gesprek? (Who owns the land? Are they open to discussion?)" -- landlord engagement

### S-DHN Conditionals
- **If warmtekavel designated:** "Wat zijn de grenzen? Welke warmtebronnen zijn al gecommitteerd? (Zone boundaries? Which heat sources committed?)" -- exclusivity assessment
- **If multiple heat sources:** "Hoe ziet hun warmtemix eruit? Waar past DC-restwarmte het best? (Heat portfolio? Where does DC waste heat fit best?)" -- portfolio positioning
- **If municipal ownership:** "Wie in de gemeente moet akkoord geven? College, raad, ambtenaren? (Who needs to approve? Executive, council, officials?)" -- stakeholder mapping
- **If public tender required:** "Wanneer is de volgende aanbestedingsronde? (When is the next tender round?)" -- timeline planning
- **If supply temp >70C:** "Overwegen ze een warmtepomp in het netwerk? (Considering a heat pump in the network?)" -- temperature bridging

### S-IND Conditionals
- **If process temp >120C:** "Welk deel van het proces kan met lagere temperatuur? Voorverwarming? (Which part of the process works at lower temp? Preheating?)" -- partial supply scoping
- **If 24/7 uptime critical:** "Welke back-up hebben ze nu? Kunnen we aanvullend leveren in plaats van vervanging? (Current backup? Can we supplement rather than replace?)" -- risk mitigation
- **If ETS/ETS2 exposed:** "Wat is hun CO2-uitstoot? Hebben ze al scenario's doorgerekend voor hogere CO2-prijzen? (CO2 emissions? Modeled scenarios for higher CO2 prices?)" -- decarbonization business case
- **If multiple facilities:** "Welke locatie heeft de beste combinatie van warmtevraag en netcapaciteit? (Which location has best combo of heat demand and grid capacity?)" -- site prioritization
