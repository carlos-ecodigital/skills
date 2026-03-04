# Colocation Datacenters -- Projectfinanciering Nederland / Project Financing Netherlands

---

## 1. Definitie en Marktoverzicht / Definition and Market Overview

### 1.1 Definitie / Definition

Colocation datacenters (colocatie datacentra): multi-tenant faciliteiten (multi-tenant facilities) die
ruimte (space), vermogen (power), koeling (cooling) en connectiviteit (connectivity) bieden.
Huurders (tenants) installeren eigen IT-apparatuur (IT equipment). Niet verwarren met
hyperscale datacenters die door een enkele operator voor eigen gebruik worden gebouwd.

**Modellen / Models:**

| Model | Beschrijving / Description | Typisch vermogen / Typical Power |
|---|---|---|
| Wholesale (grootschalig) | Volledige of gedeeltelijke hallen (full/partial halls), dedicated infrastructuur | >500 kW per klant |
| Retail (kleinschalig) | Per rek (rack), kooi (cage) of suite; gedeelde infrastructuur | <500 kW per klant |
| Powered shell | Casco met stroomvoorziening; huurder bouwt af | >1 MW per klant |
| Build-to-suit | Op maat gebouwd voor specifieke huurder | Variabel |

Kernactiviteiten omvatten: stroomvoorziening en -distributie (power supply and distribution),
koeling en klimaatbeheersing (cooling and climate control), fysieke beveiliging (physical security),
netwerkcross-connects (network cross-connects) en remote hands ondersteuning.

### 1.2 Nederlandse Marktomvang / NL Market Size

| Metric | Waarde / Value | Bron / Source |
|---|---|---|
| Marktomvang 2025 / Market size 2025 | USD 11.25 miljard (billion) | [Mordor Intelligence] |
| Verwachte marktomvang 2030 / Projected 2030 | USD 17.85 miljard (billion) | [Mordor Intelligence] |
| CAGR 2025-2030 | 9.67% | [Mordor Intelligence] |
| Amsterdam colocatie vermogen / colocation power | ~565-580 MW (2023-2024) | [Mordor Intelligence; CBRE] |
| Amsterdam marktaandeel / market share | 78.4% van NL markt | [CBRE] |
| Aantal colocatie DCs / Number of colocation DCs | 129 operationeel, 15 in aanbouw (upcoming) | [ResearchAndMarkets] |
| Aantal operators / Number of operators | 44 (R&M major operators; DDA telt 95 bredere definitie) | [ResearchAndMarkets; DDA] |
| Totaal racks / Total racks | ~159.000 | [ResearchAndMarkets] |
| Nieuwe capaciteit 2025-2030 / New capacity | ~784 MW (Arizton); R&M colo-only: 656 MW / 15 DCs | [Arizton; ResearchAndMarkets] |
| Leegstand / Vacancy | 5% (2025, gedaald van 7% in 2024) | [Cushman & Wakefield 2025] |

### 1.3 Nederlandse Marktstructuur / NL Market Structure

**Grote operators / Major operators:**

| Operator | NL Faciliteiten / Facilities | Focus |
|---|---|---|
| Equinix | 21 faciliteiten in Nederland | Retail + interconnectie (interconnection) |
| Digital Realty / Interxion | ~31 NL DCs (gecombineerd / combined) | Wholesale + retail |
| CyrusOne (nu Brookfield) | Amsterdam campus | Wholesale |
| NorthC | Meerdere locaties NL | Regional/edge |
| DataFoundry | Amsterdam | Wholesale |
| Iron Mountain | Amsterdam | Enterprise |

**Belangrijke infrastructuur / Key infrastructure:**

- Amsterdam Internet Exchange (AMS-IX): 's werelds grootste naar aantal leden (world's largest by
  member count); kritisch interconnectie-knooppunt (critical interconnection hub)
- Nabijelegen glasvezelroutes (nearby fiber routes) naar Frankfurt, London, Parijs
- Primaire corridors (primary corridors): Science Park, Sloterdijk, Schiphol-Rijk

---

## 2. Inkomstenmodellen / Revenue Models

### 2.1 Prijsstelling / Pricing

| Prijstype / Price Type | Indicatief / Indicative | Bron / Source |
|---|---|---|
| Wholesale globaal gemiddelde Q1 2025 / global avg | ~$217/kW/maand (month) | [CBRE / DataX Connect] |
| Amsterdam wholesale | Op of boven globaal gemiddelde (at or above) | [CBRE] |
| Retail: 48U rek / rack (excl. stroom / power) | Vanaf EUR 495/maand (month) | [HOSTKEY] |
| Cross-connect (per kabel / cable) | EUR 150-300/maand | [Marktdata / Market data] |
| Remote hands (per uur / hour) | EUR 75-150 | [Marktdata / Market data] |

**Prijsmodellen / Pricing models:**

- Stroom doorberekening (power pass-through): huurder betaalt werkelijk verbruik + opslag (margin)
- All-inclusive: vaste prijs per kW inclusief stroom, koeling en ruimte
- Hybride (hybrid): basisprijs + metered verbruik boven gecommitteerd vermogen (committed power)

### 2.2 Omzetcomponenten / Revenue Components

| Component | Beschrijving / Description | Typisch % van omzet / Typical % of Revenue |
|---|---|---|
| Ruimte/vermogen (space/power) | kW-gebaseerde of per-rack prijsstelling | 60-70% |
| Stroom (power) doorberekening + marge | Nutskosten (utility cost) + opslag (margin) | 15-25% |
| Interconnectie (interconnection) | Cross-connects, carrier-neutraal | 10-15% |
| Beheerde diensten (managed services) | Remote hands, monitoring, DCIM | 5-10% |

### 2.3 Contractstructuur / Contract Structure

**Master License Agreement (MLA) -- Wholesale:**

| Kenmerk / Feature | Typisch / Typical |
|---|---|
| Looptijd / Term | 3-10 jaar (years); hyperscaler MLAs tot 15 jaar |
| Opzegtermijn / Notice period | 12-24 maanden (months) |
| Take-or-pay | Gecommitteerd vermogen (committed power); betaling ongeacht gebruik |
| Prijsescalatie / Price escalation | CPI-gekoppeld (linked) of vast (fixed) jaarlijks 2-3% |
| Verlengingsoptie / Renewal option | 1-3 perioden van 3-5 jaar |
| Beeindiging / Termination | Beperkt tot wanprestatie (default) of faillissement (insolvency) |

**Colocation Agreement -- Retail:**

| Kenmerk / Feature | Typisch / Typical |
|---|---|
| Looptijd / Term | 1-5 jaar (years) |
| Opzegtermijn / Notice period | 3-12 maanden (months) |
| Take-or-pay | Basisruimte + minimaal vermogen (minimum power) |
| Prijsescalatie / Price escalation | CPI of vast 2-3% per jaar |
| Verlengingsoptie / Renewal option | Evergreen of vaste perioden |

**Klantenwaardigheid / Customer creditworthiness:**

- Enterprise / hyperscaler huurders met investment-grade (IG) rating: meest financierbaar (most bankable)
- Sub-IG huurders: hogere risicopremie, kortere looptijden
- Klantenverloop (churn): 5-10% jaarlijks retail; <5% wholesale

### 2.4 Bezettingsopbouw / Take-up Curve

| Jaar / Year | Standaard take-up | Pre-verhuurd / Pre-leased |
|---|---|---|
| Jaar 1 (Year 1) | 50% | 70-80% |
| Jaar 2 (Year 2) | 75% | 85-90% |
| Jaar 3 (Year 3) | 90% | 95%+ |
| Stabilisatie / Stabilization | 92-95% | 95-98% |

[Industriebenchmark / Industry benchmark]

Opmerking: dit zijn modelaannames (model assumptions), geen geverifieerde marktbenchmarks.
Werkelijke opbouwcurves variëren afhankelijk van voorverhuring, marktkrapte en
operatortrack record. Voorverhuurde faciliteiten hebben hogere initiële bezetting maar langere
ontwikkelperiode (pre-leased facilities have higher initial occupancy but longer development period).

---

## 3. CAPEX-benchmarks / CAPEX Benchmarks

### 3.1 Bouwkosten / Construction Costs

| Benchmark | Waarde / Value | Bron / Source |
|---|---|---|
| Amsterdam per Watt | US$10.8/W (~EUR 9.8-10.0/W) | [Turner & Townsend DCCI 2025-2026] |
| Europees gemiddelde per MW / European average | US$9.1M/MW (+6.5% j-o-j / YoY) | [Turner & Townsend DCCI] |
| AI datacenter toeslag / premium | +7-10% bovenop traditioneel (above traditional) | [Turner & Townsend] |
| Amsterdam per MW equivalent | ~EUR 10.8M/MW | [Afgeleid van T&T / Derived T&T] |
| Casco + kern / Shell + core (excl. afbouw) | 60-70% van totale CAPEX | [Industriebenchmark] |
| Huurdersafbouw / Tenant fit-out | 30-40% van totale CAPEX | [Industriebenchmark] |

### 3.2 CAPEX Uitsplitsing / Breakdown

| Categorie / Category | % van Totaal / of Total | Toelichting / Notes |
|---|---|---|
| Grond en bouw / Land and construction | 25-35% | Inclusief fundering, structuur, gevel (facade) |
| Elektrisch / Electrical | 25-30% | HV/MV/LV, transformatoren, UPS, generatoren |
| Mechanisch / Mechanical | 15-20% | Koeling (cooling), HVAC, brandbeveiliging (fire protection) |
| IT-infrastructuur / IT infrastructure | 5-10% | Kabelbanen (cable trays), patchpanelen, netwerk backbone |
| Ontwerp en vergunningen / Design and permits | 5-8% | Architectuur, engineering, Omgevingswet vergunningen |
| Onvoorzien / Contingency | 5-10% | Hoger bij greenfield; lager bij bewezen design |

### 3.3 Bouwtijdlijnen / Construction Timelines

| Type | Looptijd / Duration | Toelichting / Notes |
|---|---|---|
| Greenfield (nieuwbouw) | 18-36 maanden (months) | Inclusief vergunningen en grondwerk |
| Uitbreiding / Expansion (bestaand terrein) | 12-18 maanden | Op reeds vergund terrein |
| Afbouw / Fit-out (bestaande hal) | 6-12 maanden | MEP installatie in bestaand casco |
| Powered shell conversie | 3-6 maanden | Huurderspecifieke afbouw (tenant-specific fit-out) |

---

## 4. Waardering / Valuation Multiples

### 4.1 Publieke Marktwaardering / Public Market Valuation

| Categorie / Category | Multiple | Bron / Source |
|---|---|---|
| Equinix (REIT) | ~26.6x EV/EBITDA LTM; Forward AFFO 18.4x | [Seeking Alpha, DCD Q3 2025] |
| Digital Realty (REIT) | Forward AFFO 22x | [DCD] |
| Europese genoteerde DC-bedrijven / European listed | 20-27x EV/EBITDA (2025 data) | [Bloomberg consensus; Yahoo Finance] |

### 4.2 Private Marktwaardering / Private Market Valuation

| Categorie / Category | Multiple | Bron / Source |
|---|---|---|
| Private platforms (Tier 1) | 25-30x EV/EBITDA | [CBRE Investment Management] |
| Europese M&A: Tier 1 | ~25x EV/EBITDA | [Alantra 2024 M&A Review] |
| Europese M&A: secundair / secondary | ~13x EV/EBITDA (beperkte transacties; bereik waarschijnlijk 10-18x) | [Alantra 2024] |
| DC obligatiepremie / bond premium | 100-150 basispunten (bps) boven hyperscaler bedrijfsobligatie | [Norton Rose Fulbright] |

### 4.3 Waarderingsdrijvers / Valuation Drivers

- Contractuele omzet met IG-huurders (contracted revenue with IG tenants): hogere multiples
- Interconnectie-dichtheid (interconnection density): premie voor carrier-neutrale faciliteiten
- Locatieschaarste (location scarcity): Amsterdam moratorium verhoogt bestaande asset-waarde
- Stroomcapaciteit (power capacity): beschikbaar vermogen als premium driver
- PUE en duurzaamheid (sustainability): lagere PUE leidt tot hogere operationele marges

---

## 5. Nederlandse Regelgeving / Netherlands Regulatory Framework

### 5.1 Amsterdam Moratorium (Vestigingsstop)

- Moratorium aanvang juli 2019 (initiele vestigingsstop / initial freeze); volledig verbod geformaliseerd/verlengd tot ten minste 2030
  (moratorium inception July 2019; full ban formalized/extended through at least 2030) [NL Times apr 2025]
- Microsoft/Pure DC 78 MW controverse: omzeild via 3 afzonderlijke vergunningen +
  <100.000 m2 (circumvented via 3 separate permits + <100K sqm) [NL Times jan 2026]
- Minister verklaarde onvermogen (inability) om dit onder huidig recht te voorkomen
- Impact: extreme schaarste (scarcity) drijft huurprijzen op; bestaande assets worden waardevoller
- Gemeenteraad Amsterdam overweegt strengere maatregelen (considering stricter measures)

### 5.2 Nationaal Hyperscale Verbod / National Hyperscale Ban

- Datacenters >70 MW EN >100.000 m2 landelijk verboden sinds 2022
  (banned nationally since 2022) [CMS LawNow]
- Uitzonderingen (exceptions): aangewezen gebieden (designated areas) in:
  - Het Hogeland (Groningen)
  - Hollands Kroon (Noord-Holland)
- Toetsing (assessment): vermogen (power) EN oppervlakte (floor area) moeten beiden de drempel overschrijden
- Colocation DCs onder deze drempels vallen buiten het verbod maar onder lokale regels

### 5.3 Noord-Holland Provinciale Strategie / Provincial Strategy

- Datacenters >2.000 m2 of >5 MVA beperkt tot aangewezen industrieterreinen
  (restricted to designated industrial zones) [NH Datacenterstrategie 2025-2027]
- Aangewezen zones (designated zones):
  - Amsterdam (bestaande locaties / existing locations only)
  - Haarlemmermeer (Schiphol-corridor)
  - Hollands Kroon (voor hyperscale)
- Verplichting (obligation) restwarmtebenutting voor nieuwe DCs >1 MW
- Energieprestatie-eisen (energy performance requirements): PUE, WUE rapportage

### 5.4 Omgevingswet Vergunningen / Permitting

Standaard vergunningsvereisten (standard permit requirements) voor colocatie DC:

| Vergunning / Permit | Beschrijving / Description | Procedure |
|---|---|---|
| Bouwactiviteit (building activity) | Technische bouweisen (BBL) | Reguliere procedure: 8 weken + 6 verlenging |
| Omgevingsplanactiviteit (spatial plan activity) | Bestemmingsplan (zoning) toetsing | Regulier of uitgebreid (extended) |
| Milieubelastende activiteit (environmental) | Emissies, geluid, koelmiddelen (coolants) | Melding (notification) of vergunning |
| MER-screening (EIA screening) | Voor grotere installaties (larger installations) | Drempels afhankelijk van omvang |
| Brandveiligheid (fire safety) | BBL eisen voor IT-faciliteiten | Onderdeel van bouwvergunning |

Proceduretermijnen / Procedure timelines:
- Reguliere procedure (regular): 8 weken (weeks) + 6 weken verlenging (extension)
- Uitgebreide procedure (extended): 6 maanden (months) + 6 weken verlenging
- Bezwaar en beroep (objection and appeal): 6 weken + Rechtbank + Raad van State
- Totale projectdoorlooptijd (total project delivery, incl. net + vergunningen + bouw): 18-36 maanden typisch; langer bij bezwaar/beroep

### 5.5 Netaansluiting / Grid Connection

| Aspect | Details |
|---|---|
| Transportschaarste (transmission congestion) | TenneT: TSO 38 GW (212 verzoeken) + DSO 9 GW (14.044 verzoeken) = ~47 GW formele wachtrij vs 20 GW piekvraag |
| Typische aansluit termijn / connection timeline | 2-10 jaar afhankelijk van locatie en capaciteit |
| Cable pooling met BESS | Toegestaan onder Energiewet (eff. 1 jan 2026) |
| Flexibele contracten (flexible contracts) | ATR85, TBTR beschikbaar |
| Prioritering (prioritization) | Maatschappelijke functies (societal functions) krijgen voorrang |
| Netbeheerder Amsterdam / Grid operator | Liander (onderdeel Alliander) |
| Netbeheerder transport / Transmission | TenneT TSO |

---

## 6. Restwarmte / Waste Heat Recovery

### 6.1 Wcw (Wet collectieve warmtevoorziening / Collective Heat Supply Act)

| Aspect | Details | Bron / Source |
|---|---|---|
| Aanname Eerste Kamer / Senate adoption | 9 december 2025 | [Dirkzwager] |
| Inwerkingtreding / Effective date | Mid-2026 tot 1 jan 2027 | [Dirkzwager] |
| Regierol gemeenten / Municipal directing role | Gemeenten wijzen warmtekavels aan (designate heat zones) | [Wcw] |
| Aangewezen warmtebedrijven / Designated heat companies | >50% publiek eigendom (publicly owned); 7 jaar overgangsperiode (transition) | [Wcw] |
| Tariefstelling / Tariff setting | Kostengebaseerd tarief vervangt gasprijs-gekoppeld (cost-based replaces gas-linked) | [Wcw] |
| Bestaande netten / Existing networks | 14-30 jaar overgangsperiode (transition period) | [Wcw] |
| Leveringsplicht / Supply obligation | Warmtebedrijf moet leveren aan aangeslotenen (must supply connected customers) | [Wcw] |

### 6.2 Actieve Restwarmteprojecten in NL / Live Waste Heat Projects

| Project | Operator(en) | Details | Bron / Source |
|---|---|---|---|
| Amsterdam warmtenet | Vattenfall + SilverFalcon DC | 25 MW; ~15.000 huishoudens (households) tegen 2027 | [Euroheat] |
| Leeuwarden | Penta Infra | Eind 2026 operationeel | [DCD] |
| Groningen | QTS/Bytesnet + WarmteStad | Integratie met stadsverwarming (district heating) | [WarmteStad] |
| DDA-leden / members | Diverse operators | Gratis restwarmte sinds 2017 (free waste heat since 2017) | [Dutch Data Center Association] |
| Almere (gepland / planned) | Nader te bepalen | Onderdeel van Floriade-ontwikkeling | [Gemeente Almere] |

### 6.3 Omzetimpact / Revenue Impact

| Aspect | Details |
|---|---|
| Aanvullende omzet / Additional revenue | Warmteafnamecontract (heat offtake agreement) met warmtebedrijf |
| BTW tarief / VAT rate | 9% (verlaagd tarief / reduced rate) op warmtelevering (heat supply) |
| Kapitaalinvestering / Capital investment | Warmtewisselaar (heat exchanger), leidingen (piping) naar warmtenet |
| Typische investering / Typical investment | EUR 500K-2M afhankelijk van schaal en afstand |
| Terugverdientijd / Payback period | 5-8 jaar (years) afhankelijk van warmteprijs en volume |
| ESG voordeel / benefit | Vermindert scope 2 emissie-toerekening (reduces emissions attribution) |
| Vergunningsimpact / Permitting impact | Restwarmtebenutting kan vergunningverlening versoepelen (can ease permitting) |

---

## 7. Kapitaalstructuur / Capital Structure

### 7.1 Typische DC Projectfinancieringsstructuur / Typical DC Project Finance Structure

| Parameter | Gecontracteerd / Contracted | Speculatief / Speculative |
|---|---|---|
| Hefboom / Gearing | 65-75% | 50-60% |
| Eigen vermogen / Equity | 25-35% | 40-50% |
| Looptijd / Tenor | 7-15 jaar (years) | 5-7 jaar |
| Min DSCR | 1.20-1.30x | 1.35-1.50x |
| Min LLCR | 1.25-1.40x | 1.40-1.60x |
| Prijsstelling / Pricing | EURIBOR + 175-250 bps | EURIBOR + 250-350 bps |
| Voorverhuureis / Pre-lease requirement | 50-70% voor bouwuitkering (construction drawdown) | Lager; hoger eigenvermogenbuffer |
| Lock-up DSCR | 1.10-1.15x | 1.20-1.25x |
| Default DSCR | 1.05x | 1.10x |

### 7.2 Bouwfinanciering / Construction Finance

| Instrument | Beschrijving / Description |
|---|---|
| Uitgestelde trekkingslening (delayed draw term loan) | Getrokken naarmate bouw vordert (drawn as construction progresses) |
| Eigen vermogen eerst (equity first) | Sponsor investeert eerst; bank trekt later |
| Pro rata | Bank en sponsor trekken gelijktijdig (simultaneously) |
| Pari passu | Gelijke betalingsrechten (equal payment rights) |
| Bouwgarantie (construction guarantee) | Aanneemsom vaste prijs of GMP (guaranteed maximum price) |
| Onafhankelijk ingenieur (independent engineer) | Mijlpaalgoedkeuring (milestone sign-off) voor uitkeringen |
| Conversie bij COD | Omzetting naar termijnlening bij Commercial Operation Date / substantiele oplevering |

### 7.3 Omzetafdekking / Revenue Hedging

| Instrument | Beschrijving / Description |
|---|---|
| Langlopende MLAs met IG-huurders | Primaire bankbare afnameovereenkomst (primary bankable offtake) |
| PPA (Power Purchase Agreement) | Stroomprijs afdekking (power price hedging) voor 5-15 jaar |
| Nutshedging (utility hedging) | Via energieleverancier prijsafspraak |
| CPI-gekoppelde escalatie | Inflatiebescherming (inflation protection) ingebouwd in huurcontracten |
| Valuta-afdekking (currency hedging) | Indien omzet in USD; kosten in EUR |

### 7.4 Nederlandse Institutionele Investeerders / NL Institutional Investors

| Investeerder / Investor | Details | Bron / Source |
|---|---|---|
| APG (pensioenfonds) | EUR 552 miljard AUM; 10% infrastructuurdoelstelling (infra target) | [IPE] |
| PGGM | EUR 15 miljard in infrastructuur | [IPE] |
| NN Group (verzekeraar / insurer) | EUR 300M via Rivage fonds | [NN Group] |
| a.s.r. | Infrastructuurschuld (infrastructure debt) allocatie | [a.s.r.] |
| InvestNL | Eigen vermogen / mezzanine voor digitale infrastructuur | [Invest-NL] |
| EIB | OVHcloud EUR 200M voor cloud DC; AI Gigafactories programma | [EIB] |
| NIA (Nationale Investeringsinstelling) | Co-investering met pensioenfondsen in NL infra | [NIA] |

---

## 8. Technologierisico / Technology Risk for Lenders

### 8.1 Vermogen en Koeling / Power and Cooling

| Parameter | Traditioneel / Traditional | Hoge dichtheid / High-density | AI/GPU (H100/MI300X) | AI/GPU (B200/GB200+) |
|---|---|---|---|---|
| Vermogensdichtheid per rek / Power density per rack | 6-15 kW (gem. ~8 kW, 2024) | 30-50 kW | 40-80 kW | 120-240 kW |
| Koeling / Cooling | Lucht (air): CRAH/CRAC | Direct liquid (DLC) | DLC + lucht hybride | Volledige DLC / immersie |
| PUE doelstelling / target | 1.2-1.4 | 1.1-1.2 | 1.05-1.15 | 1.02-1.05 |
| WUE doelstelling / target | 0.5-1.5 L/kWh | 0.2-0.5 L/kWh | <0.2 L/kWh | <0.2 L/kWh |
| CAPEX per kW | Lager (lower) | +20-30% | +40-60% | +50-70% |

### 8.2 Redundantie en Uptime / Redundancy and Uptime

| Tier (Uptime Institute) | Redundantie / Redundancy | Beschikbaarheid / Availability | Geschiktheid PF / PF Suitability |
|---|---|---|---|
| Tier II | N+1 (gedeeltelijk / partial) | 99.741% | Onvoldoende voor PF (insufficient) |
| Tier III | N+1 gelijktijdig onderhoudbaar (concurrently maintainable) | 99.982% | Minimum voor projectfinanciering |
| Tier IV | 2N fouttolerant (fault-tolerant) | 99.995% | Premium; hoogste financierbaarheid |

**SLA-boetes (penalties) bij uitval (downtime):**
- Typisch: krediet op maandelijkse huur (credit on monthly fee) van 5-30% per incident
- Ernstige uitval (>24 uur): contractuele beeindigingsrecht (termination right) voor huurder
- Verzekeringsoverwegingen (insurance considerations): BI (bedrijfsonderbrekingsverzekering / business interruption)

### 8.3 Technologie Vernieuwingscyclus / Technology Refresh

| Component | Levensduur / Lifecycle | Verantwoordelijk / Responsible |
|---|---|---|
| Casco en kern / Shell and core | 20-30 jaar (years) | Eigenaar / verhuurder (owner/landlord) |
| MEP (mechanisch, elektrisch, loodgieterswerk) | 10-15 jaar | Eigenaar (CAPEX reserve planning) |
| Koelsystemen / Cooling systems | 10-15 jaar | Eigenaar |
| Noodstroomaggregaten / Emergency generators | 15-20 jaar | Eigenaar |
| UPS-systemen | 8-12 jaar | Eigenaar |
| IT-apparatuur / IT equipment | 3-5 jaar | Huurder (tenant responsibility) |
| Bekabeling / Cabling | 10-15 jaar | Eigenaar (backbone); huurder (within cage) |

Kredietverstrekkers (lenders) richten zich op casco/kernlevensduur voor bepaling looptijd schuld
(focus on shell/core asset life for debt tenor sizing). CAPEX-reserverekening (reserve account)
vereist voor MEP-vernieuwing.

---

## 9. Due Diligence Aandachtspunten / Due Diligence Focus Areas

### 9.1 Checklist

**Commercieel / Commercial:**
- [ ] Klantenconcentratierisico (customer concentration risk): top 5 huurders als % van omzet
- [ ] Contractvoorwaarden: resterende looptijd, verlengingsopties, beeindigingsbepalingen
      (term remaining, renewal options, termination provisions)
- [ ] Kredietwaardigheid klanten (customer creditworthiness): IG-rating of equivalent
- [ ] Bezettingsaannames (take-up curve assumptions) vs markvraag (market demand)
- [ ] Historisch klantenverloop (historical churn) en retentiepercentage (retention rate)
- [ ] Concurrentiepositie (competitive position) en marktverzadiging (market saturation)

**Technisch / Technical:**
- [ ] Stroomcapaciteit (power capacity) en netaansluiting zekerheid (grid connection security)
- [ ] Koelsysteemcapaciteit (cooling system capacity) en uitbreidbaarheid (expandability)
- [ ] Redundantieniveau (redundancy level) en Tier-certificering
- [ ] PUE, WUE en energieprestatie (energy performance) historisch en verwacht
- [ ] Staat van onderhoud (maintenance condition) van bestaande MEP

**Juridisch en Vergunningen / Legal and Permits:**
- [ ] Omgevingswet naleving (compliance) en vergunningsvoorwaarden (permit conditions)
- [ ] Stikstof / AERIUS beoordeling (assessment): depositie op Natura 2000
- [ ] Brandveiligheidscompliance (fire safety): BBL, NEN normen, NFPA (indien van toepassing)
- [ ] Eigendomsstructuur (ownership structure): erfpacht (leasehold) vs vol eigendom (freehold)
- [ ] Huurovereenkomsten review (lease agreements review)

**Milieu en Verzekering / Environmental and Insurance:**
- [ ] Bodemonderzoek (soil investigation): NEN 5725 (vooronderzoek) -> NEN 5740 (verkennend) -> NTA 5755
- [ ] Asbest onderzoek (asbestos survey) voor bestaande gebouwen
- [ ] Verzekerings toereikendheid (insurance adequacy): PAR, BI, cyber, aansprakelijkheid (liability)
- [ ] Restwarmte monetisatie potentieel (waste heat monetization potential) en Wcw compliance

### 9.2 Bankability Criteria

| Criterium / Criterion | Minimum voor PF / Minimum for PF |
|---|---|
| Voorverhuurpercentage / Pre-lease rate | 50-70% van capaciteit bij financial close |
| Gemiddelde huurderrating / Average tenant rating | Investment grade of equivalent |
| WALT (gewogen gemiddelde huurlooptijd / weighted average lease term) | >5 jaar bij stabilisatie |
| Netaansluiting (grid connection) | Bevestigd en gecontracteerd (confirmed and contracted) |
| Bouwcontract | EPC vaste prijs of GMP met creditwaardige aannemer |
| Vergunningen / Permits | Onherroepelijk (irrevocable) of condition precedent |

---

## 10. EU Taxonomie en ESG / EU Taxonomy and ESG

### 10.1 EU Taxonomie Classificatie / Taxonomy Classification

| Aspect | Details |
|---|---|
| Activiteit / Activity | 8.1: Gegevensverwerking, hosting en aanverwante activiteiten (data processing, hosting) |
| PUE drempel / threshold | <= 1.5 voor nieuwe DCs (EU Gedelegeerde Verordening / Delegated Act) |
| WUE verwachting / expectation | Best practices rapportage vereist |
| Restwarmte bijdrage / Waste heat contribution | Draagt bij aan circulaire economie doelstelling (circular economy objective) |
| Klimaatadaptatie / Climate adaptation | Kwetsbaarheids- en risicobeoordeling (vulnerability and risk assessment) vereist |
| DNSH (Do No Significant Harm) | Toetsing op alle zes milieudoelstellingen (six environmental objectives) |

### 10.2 Duurzaamheidsverslaggeving / Sustainability Reporting

| Kader / Framework | Toepasselijkheid / Applicability |
|---|---|
| CSRD (Corporate Sustainability Reporting Directive) | Rapportageverplichting voor grotere entiteiten (larger entities) |
| SFDR (Sustainable Finance Disclosure Regulation) | Classificatie beinvloedt institutionele beleggersbereidheid (impacts investor appetite) |
| EED (Energy Efficiency Directive) | Rapportage over energieverbruik voor DCs >500 kW |
| European Code of Conduct for DC | Vrijwillige best practices |
| Science Based Targets initiative (SBTi) | Scope 1, 2 en 3 emissiereductiedoelen |

### 10.3 ESG Waarderingspremie / ESG Valuation Premium

- Hoge ESG-score faciliteiten (high ESG-score facilities): potentieel lagere financieringskosten (lower financing costs)
- Groene obligaties (green bonds): spread voordeel (advantage) van 10-30 bps
- Institutionele investeerders: toenemende ESG-vereisten voor beleggingsbeleid (investment policy)
- Restwarmteprojecten: versterken (enhance) ESG-narratief en vergunningspositie

---

## 11. Risicomatrix / Risk Matrix

| Risico / Risk | Kans / Likelihood | Impact | Mitigatie / Mitigation |
|---|---|---|---|
| Netcongestie (grid congestion) | Hoog (High) | Hoog | Cable pooling, BESS, eigen opwekking (on-site generation) |
| Regulatoire wijziging (regulatory change) | Gemiddeld (Medium) | Hoog | Vergunningsstrategie, locatiediversificatie |
| Technologische veroudering (obsolescence) | Laag (Low) | Gemiddeld | Modulair ontwerp (modular design), CAPEX reserves |
| Klantenverloop (customer churn) | Gemiddeld | Gemiddeld | Langlopende contracten, interconnectie lock-in |
| Stroomprijs volatiliteit (power price volatility) | Hoog | Gemiddeld | PPAs, hedging, pass-through contracten |
| Bouwkostenoverschrijding (construction cost overrun) | Gemiddeld | Hoog | EPC vaste prijs, onvoorzien buffer, IE monitoring |
| Natuurrampen / klimaat (natural disasters / climate) | Laag | Hoog | Locatiekeuze, verzekering, redundantie |
| Cyberrisico / cyber risk | Gemiddeld | Hoog | ISO 27001, SOC 2, fysieke beveiliging, cyberverzekering |

---

## 12. Vergelijking Colocatie vs Hyperscale / Colocation vs Hyperscale Comparison

| Kenmerk / Feature | Colocatie / Colocation | Hyperscale |
|---|---|---|
| Huurderstructuur / Tenant structure | Multi-tenant | Enkele gebruiker (single user) |
| Typisch vermogen / Typical power | 1-50 MW | 50-500+ MW |
| Omzetmodel / Revenue model | Recurring huur + interconnectie | Intern gebruik (internal use) of cloud verkoop |
| Financierbaarheid / Bankability | Hoog bij diversificatie en IG-huurders | Hoog bij creditwaardige operator |
| NL regulatoir / NL regulatory | Onder lokale beperkingen; geen nationaal verbod (<70MW/<100Km2) | Nationaal verbod >70MW + >100Km2 |
| Waardering / Valuation | 13-30x EV/EBITDA | Onderdeel van platform/bedrijfswaardering |
| Interconnectie waarde / Interconnection value | Kernwaardedrijver (core value driver) | Minder relevant |
| Locatie flexibiliteit / Location flexibility | Beperkt door connectivity en klantproximiteit | Meer flexibel; kan naar periferie |

---

## 13. Disclaimer

Marktgegevens (market data), prijsindicaties (pricing indications) en waarderingsmultiples
(valuation multiples) zijn indicatief en afkomstig uit gepubliceerde rapporten (published reports).
Verkrijg onafhankelijke waarderingen (obtain independent valuations) en marktanalyses voor
transactiespecifieke doeleinden (transaction-specific purposes).

Regelgevingsverwijzingen (regulatory references) actueel per 2025/2026.

Dit document is geen beleggingsadvies (not investment advice) of juridisch advies (not legal advice).
Raadpleeg gekwalificeerde adviseurs (consult qualified advisors) voor specifieke transacties.

---

## 14. Kruisverwijzingen / Cross-References

Gerelateerde referentiebestanden (related reference files) in deze skill:

| Onderwerp / Topic | Bestand / File |
|---|---|
| AI-fabrieken / AI factories | [references/ai-factories.md](references/ai-factories.md) |
| BESS projecten / BESS projects | [references/bess-projects.md](references/bess-projects.md) |
| Schuldinstrumenten / Debt instruments | [references/debt-instruments.md](references/debt-instruments.md) |
| Eigen vermogen structuren / Equity structures | [references/equity-structures.md](references/equity-structures.md) |
| Risicoallocatie / Risk allocation | [references/risk-allocation.md](references/risk-allocation.md) |
| Nederlands juridisch kader / Netherlands legal framework | [references/netherlands-legal-framework.md](references/netherlands-legal-framework.md) |

---

*Laatst bijgewerkt / Last updated: maart 2026 (ecosystem sync vanuit Compute Market Size fact-check)*
