# Site Selection Methodology

## 1. Fatal Flaw Screening

### Purpose
Before investing resources in detailed site evaluation, screen every candidate site against binary pass/fail criteria. A single fatal flaw eliminates the site regardless of other merits.

### Fatal Flaw Criteria

| # | Fatal Flaw | Test | Data Source | Threshold |
|---|---|---|---|---|
| 1 | **No grid capacity** | TenneT/DSO capacity available at nearest substation | DSO capacity map, preliminary inquiry | <10 MVA available AND >5 year connection timeline |
| 2 | **Hostile provincial policy** | Province prohibits or severely restricts new data centers | Omgevingsverordening, provincial coalition agreement | Explicit prohibition or de facto moratorium |
| 3 | **Incompatible zoning** | Current bestemmingsplan/omgevingsplan does not allow DC or greenhouse, and rezoning is politically infeasible | Ruimtelijkeplannen.nl, municipality consultation | No pathway to compatible zoning within 2-3 years |
| 4 | **Natura 2000 / stikstof** | Site within or directly adjacent to Natura 2000 area with nitrogen-sensitive habitat | AERIUS Calculator, Natura 2000 boundary maps | Significant stikstof impact with no mitigable pathway |
| 5 | **Severe soil contamination** | Known contamination requiring extensive bodemsanering (soil remediation) | Bodemloket, historisch bodemonderzoek | Category "serious" contamination with no remediation plan |
| 6 | **Flood zone** | Site in Buitendijks (unprotected) area or primary flood zone | Klimaateffectatlas, watertoets | Unprotectable flood risk |
| 7 | **No fiber connectivity** | No carrier fiber within economically reasonable distance | Carrier route maps, Glasvezel Buitengebied status | >5 km from nearest carrier POP with no build-out plan |
| 8 | **No greenhouse land** | No suitable agricultural land for greenhouse within heat pipe distance (~2-5 km) | Agricultural land classification (AHN/BRK), tuinbouw clusters | No glastuinbouw (greenhouse horticulture) potential within thermal delivery distance |

**Decision rule:** Any single fatal flaw → site eliminated. No exceptions. No "we can work around it."

### Provincial Data Center Policy Landscape

| Province | DC Policy Stance | Key Restriction | DEC Implication |
|---|---|---|---|
| **Noord-Holland** | Restrictive (hyperscale moratorium) | No new hyperscale DC in MRA (Metropoolregio Amsterdam), Haarlemmermeer restrictive | DEC must position as "non-hyperscale" (<40 MW) with heat reuse |
| **Zuid-Holland** | Moderate-supportive | Prefers DC with waste heat utilization (Westland glastuinbouw focus) | Strong match for DEC model — heat integration is policy goal |
| **Flevoland** | Restrictive-evolving | Recent restrictions on large DC, but agricultural diversification supported | DC-greenhouse co-location may pass if framed as agricultural innovation |
| **Noord-Brabant** | Moderate | Requires energy efficiency and heat reuse demonstration | DEC heat reuse is advantage; grid congestion is the constraint |
| **Groningen** | Supportive | Welcomes digital economy; earthquake-affected areas seeking new economic activity | Grid capacity available; fewer greenhouses than Westland but emerging |
| **Zeeland** | Supportive | Borssele energy hub, available grid capacity, province seeking diversification | Grid advantage; greenhouse sector smaller than Zuid-Holland |
| **Limburg** | Moderate | Provincial policy developing; Chemelot cluster potentially supportive | Industrial heat market, but greenhouse sector limited |
| **Gelderland** | Moderate-restrictive | Grid congestion severe; cautious on DC development | Grid congestion may be fatal flaw; limited greenhouse cluster |
| **Overijssel** | Moderate | Focus on energy transition projects with local benefit | DEC model could fit; grid capacity moderate |
| **Friesland** | Undeveloped | Limited DC policy; agricultural province | Greenhouse potential; grid capacity to be assessed |
| **Drenthe** | Undeveloped | Limited DC policy; rural province | Similar to Friesland |
| **Utrecht** | Restrictive | Urban province, limited industrial space, grid congested | Unlikely fit for DEC |

**DEC strategic regions (strongest policy + grid + greenhouse fit):**
1. Zuid-Holland / Westland corridor — policy match, greenhouse cluster, grid moderate
2. Zeeland / Borssele area — grid capacity, policy supportive, emerging greenhouse
3. Groningen — grid capacity, policy supportive, lower land cost

## 2. Weighted Scoring Matrix

### Scoring Framework

After fatal flaw screening, evaluate surviving sites using a weighted scoring matrix:

| # | Criterion | Weight | Scoring Basis | Data Source |
|---|---|---|---|---|
| 1 | **Grid capacity & connection timeline** | 25% | MVA available, years to energization, voltage level | DSO preliminary inquiry |
| 2 | **Zoning & permitting pathway** | 15% | Current bestemmingsplan compatibility, rezoning probability, municipality attitude | Ruimtelijkeplannen.nl, municipality consultation |
| 3 | **Greenhouse land availability** | 15% | Agricultural land area, quality (bodem/water), existing grower interest, proximity | Agricultural land registry, grower network |
| 4 | **Heat demand proximity** | 10% | Greenhouse heat demand within thermal delivery distance, seasonal profile match | Glastuinbouw Nederland data, local grower survey |
| 5 | **Land availability & cost** | 10% | Site area (DC + greenhouse + expansion), €/m2, acquisition timeline | Kadaster, brokers, municipality industrial land office |
| 6 | **Fiber connectivity** | 8% | Carrier count, distance to AMS-IX, latency, carrier availability | Carrier route maps, peering exchange proximity |
| 7 | **Environmental constraints** | 7% | Natura 2000 proximity, stikstof exposure, geluid (noise) sensitivity, water table | AERIUS, Klimaateffectatlas, omgevingsverordening |
| 8 | **Soil & geotechnical conditions** | 5% | Soil type, bearing capacity, contamination status, pile foundation requirements | Bodemloket, DINOloket, geotechnical reports |
| 9 | **Transport & logistics** | 3% | Road access (heavy transport for construction and equipment), public transport for staff | Google Maps, province infrastructure plans |
| 10 | **Community acceptance** | 2% | Municipality attitude, neighbor sensitivity, existing industrial precedent | Municipal policy, stakeholder analysis |
| | **Total** | **100%** | | |

### Scoring Scale

| Score | Description |
|---|---|
| 5 | Excellent — best-in-class for this criterion |
| 4 | Good — strong position with minor limitations |
| 3 | Adequate — meets minimum requirements, no standout advantage |
| 2 | Below average — significant limitations requiring mitigation |
| 1 | Poor — barely acceptable, major mitigation required |
| 0 | Unacceptable — fatal for this criterion (should have been caught in fatal flaw screen) |

### DEC-Specific Scoring Adjustments

**Greenhouse co-location bonus (add to weighted score):**
- Site is within existing glastuinbouw cluster (Westland, Aalsmeer, Noordoostpolder, Venlo): +5% bonus
- Identified grower partner willing to engage: +3% bonus
- Existing warmtenet (district heating network) infrastructure within 5 km: +2% bonus

**DEC-specific disqualifiers (beyond fatal flaws):**
- Province requires restwarmteplicht (mandatory waste heat utilization) but no grower partner identified: site stalled
- Municipality opposes data centers but would support greenhouse expansion: reframe as greenhouse-led project

## 3. Due Diligence Checklist

### Phase 1: Desktop Due Diligence (2-4 weeks)

| # | Item | Source | Deliverable |
|---|---|---|---|
| 1 | **Title search (eigendomscheck)** | Kadaster (Land Registry) | Title report: owner, encumbrances, erfdienstbaarheden (easements), hypotheek (mortgage) |
| 2 | **Zoning verification** | Ruimtelijkeplannen.nl | Current bestemmingsplan/omgevingsplan, permitted uses, building envelope |
| 3 | **Soil contamination screening** | Bodemloket, historisch bodemonderzoek (HBo/historical soil investigation) | Contamination status, any known soil issues |
| 4 | **Archaeological screening** | Archeologische Monumentenkaart (AMK), ARCHIS | Archaeological expectation value (hoge/middelhoge/lage verwachting), required surveys |
| 5 | **Utility survey** | KLIC melding (Kabels en Leidingen Informatie Centrum) | Underground cables and pipelines crossing or adjacent to site |
| 6 | **Environmental baseline** | AERIUS Calculator, Natura 2000 map, Klimaateffectatlas | Stikstof depositie, flooding risk, noise zone, groundwater protection area |
| 7 | **Grid capacity inquiry** | DSO/TenneT preliminary inquiry | Available capacity (MVA), estimated connection timeline, voltage level |
| 8 | **Fiber connectivity survey** | Carrier inquiries (KPN, Eurofiber, Relined, Colt) | Fiber availability, distance, carrier count, indicative lead time |
| 9 | **Provincial/municipal policy review** | Omgevingsverordening, coalitieakkoord (coalition agreement), structuurvisie | DC policy stance, restrictions, opportunities |
| 10 | **Greenhouse land assessment** | Agricultural land classification, BRP (Basisregistratie Percelen/Parcel Registry), grower contacts | Available greenhouse land within 5 km, land quality, existing grower interest |

### Phase 2: Field Due Diligence (4-8 weeks)

| # | Item | Source | Deliverable |
|---|---|---|---|
| 1 | **Geotechnical investigation** | CPT (Cone Penetration Test) campaign, laboratory analysis | Soil profile, bearing capacity, pile length estimate, groundwater level |
| 2 | **Environmental soil survey** | NEN 5740 verkennend bodemonderzoek (exploratory soil investigation) | Soil and groundwater sample results, remediation need assessment |
| 3 | **Topographic survey** | Land surveyor (landmeter) | Site boundaries, elevations, existing structures, drainage |
| 4 | **Acoustic baseline** | Noise measurement (achtergrondgeluidniveau/background sound level) | Current noise levels at site boundary and nearest sensitive receptors |
| 5 | **Ecological survey (quickscan)** | Ecologist flora/fauna quickscan | Protected species presence, required surveys, seasonal constraints |
| 6 | **Flood risk assessment** | Watertoets (water assessment) | Flooding probability, drainage capacity, water storage requirement |
| 7 | **Unexploded ordnance screening** | OCE (Ontplofbare Conventionele Explosieven) desktop study | Risk zones, required field survey areas |
| 8 | **Municipality pre-consultation** | Vooroverleg (pre-application meeting) with gemeente | Municipality attitude, planning constraints, conditions, timeline expectations |
| 9 | **DSO/TenneT technical meeting** | In-person or detailed written exchange | Connection offer specifics, route, timeline, cost estimate |
| 10 | **Grower engagement** | Direct meetings with identified greenhouse operators | Grower interest level, heat demand specification, commercial terms framework |

### Phase 3: Confirmatory Due Diligence (4-6 weeks)

| # | Item | Source | Deliverable |
|---|---|---|---|
| 1 | **Full archaeological survey** (if required) | Inventariserend Veldonderzoek (IVO) / proefsleuven (trial trenches) | Archaeological report, impact on buildable area |
| 2 | **Detailed geotechnical design** | Pile foundation design based on CPT data | Foundation specification, cost estimate |
| 3 | **MER screening** | m.e.r.-beoordelingsnotitie or plan-MER if required | Environmental impact assessment determination |
| 4 | **Stikstof calculation** | AERIUS berekening (calculation) for construction and operation | Depositie values, mitigation requirements |
| 5 | **Grid connection offer** | Formal offerte from netbeheerder | Connection cost, timeline, route, conditions |
| 6 | **Land acquisition terms** | Heads of terms or koopovereenkomst (purchase agreement) draft | Price, conditions, timeline, erfpacht (ground lease) if applicable |
| 7 | **Grower LOI** | Letter of Intent with greenhouse partner | Heat demand, pricing framework, timeline alignment |

## 4. Site Comparison Template

### Comparison Matrix

| Criterion | Weight | Site A: ___ | Site B: ___ | Site C: ___ |
|---|---|---|---|---|
| Grid capacity & timeline | 25% | Score: __ × 25% = __ | Score: __ × 25% = __ | Score: __ × 25% = __ |
| Zoning & permitting | 15% | Score: __ × 15% = __ | Score: __ × 15% = __ | Score: __ × 15% = __ |
| Greenhouse land | 15% | Score: __ × 15% = __ | Score: __ × 15% = __ | Score: __ × 15% = __ |
| Heat demand proximity | 10% | Score: __ × 10% = __ | Score: __ × 10% = __ | Score: __ × 10% = __ |
| Land availability & cost | 10% | Score: __ × 10% = __ | Score: __ × 10% = __ | Score: __ × 10% = __ |
| Fiber connectivity | 8% | Score: __ × 8% = __ | Score: __ × 8% = __ | Score: __ × 8% = __ |
| Environmental constraints | 7% | Score: __ × 7% = __ | Score: __ × 7% = __ | Score: __ × 7% = __ |
| Soil & geotech | 5% | Score: __ × 5% = __ | Score: __ × 5% = __ | Score: __ × 5% = __ |
| Transport & logistics | 3% | Score: __ × 3% = __ | Score: __ × 3% = __ | Score: __ × 3% = __ |
| Community acceptance | 2% | Score: __ × 2% = __ | Score: __ × 2% = __ | Score: __ × 2% = __ |
| **Raw weighted score** | **100%** | **___** | **___** | **___** |
| Co-location bonus | +0-10% | +___% | +___% | +___% |
| **Final score** | | **___** | **___** | **___** |

### Sensitivity Check

After scoring, test robustness by varying the top-3 weighted criteria by ±5% weight each. If ranking changes → decision is sensitive to assumptions → deeper investigation of the swinging criterion before committing.

## 5. Land Acquisition Considerations

### Acquisition Structures

| Structure | Description | DEC Advantage | DEC Risk |
|---|---|---|---|
| **Koop (purchase)** | Outright purchase of land | Full control, no ongoing lease cost | High upfront capital, less flexibility |
| **Erfpacht (ground lease)** | Long-term lease (typically 30-99 years) from municipality or private landowner | Lower upfront cost, municipality alignment | Annual canon (lease payment), renewal risk |
| **Recht van opstal (right of superficies)** | Right to own buildings on another's land | Separate DC and greenhouse land ownership possible | Complex legal structure, limited lender familiarity |
| **Huurovereenkomst (lease agreement)** | Standard commercial lease (shorter term) | Lowest commitment, fastest to arrange | Least control, lease renewal risk, lender concerns |

**DEC recommendation:** Erfpacht from municipality or agricultural landowner for greenhouse land; koop or erfpacht for DC land. This structure allows the grower to own/lease the greenhouse land separately while DEC controls the DC parcel and heat infrastructure easement.

### Land Cost Benchmarks (NL, indicative)

| Location Type | €/m2 (excl BTW) | Notes |
|---|---|---|
| Premium industrial (Haarlemmermeer, Schiphol corridor) | €250-500 | If available; mostly unavailable for new DC |
| Standard industrial (provincial bedrijventerrein) | €100-250 | Typical for smaller cities/towns |
| Agricultural (glastuinbouw area) | €30-80 | Zuid-Holland Westland area toward higher end |
| Agricultural (general arable) | €5-15 | Rural areas, conversion needed |
| Municipality erfpacht canon | €5-20/m2/year | Depends on municipality and use |

### Key Land Agreement Provisions (DEC-specific)

| Provision | Purpose | DEC Position |
|---|---|---|
| **Heat infrastructure easement** | Right to install heat pipes across greenhouse land | Essential — must survive land transfer |
| **Co-development obligation** | Both DC and greenhouse built per agreed phasing | Protects against stranded heat infrastructure |
| **Expansion reserves** | Right of first refusal on adjacent land for Phase 2+ | Critical for long-term growth |
| **Rezoning cooperation** | Seller/municipality cooperates on bestemmingsplanwijziging | De-risks permitting timeline |
| **Environmental indemnity** | Seller indemnifies for pre-existing soil contamination | Standard DD protection |

## Cross-References
- See [co-location-master-planning.md](co-location-master-planning.md) for site layout once selected
- See [grower-thermal-interface.md](grower-thermal-interface.md) for greenhouse-specific site requirements
- See [project-finance-economics.md](project-finance-economics.md) for land cost in financial model
- See companion skill `netherlands-permitting`:
  - [province-specific files] for provincial DC policy detail
  - [municipality-specific files] for local planning requirements
  - Omgevingsplanexpert for zoning/bestemmingsplan analysis
  - Stikstof/Natuur expert for Natura 2000 and AERIUS assessment
- See companion skill `energy-markets`:
  - [grid-connection-strategy.md] for grid connection as site criterion
- See companion skill `dc-engineering`:
  - [civil-works-netherlands.md] for geotechnical site requirements
