# Grower FAQ Reference — Co Ten Wolde BD Support

> **Purpose:** Canonical FAQ answers for grower-facing BD conversations. Every answer is SSOT-sourced. Use this to ensure consistent, accurate messaging across all grower touchpoints.
> **Audience:** Co Ten Wolde (Grower Relations / BD) — intermediate user who needs guardrails on technical claims, SDE++ framing, and contract details.
> **Language default:** Dutch-first (answers include NL and EN). All grower conversations in Dutch unless explicitly requested otherwise.
> **Last updated:** 2026-03-07

---

## How To Use This FAQ

1. **Find the topic** in the category sections below
2. **Use the "Approved Answer"** — this is what Co should communicate
3. **Check "NEVER SAY"** — these are guardrails on common mistakes
4. **Check "Source"** — if challenged, you can look up the authoritative SSOT file
5. **When unsure** — route to the right skill (listed per topic)

---

## Category A: Over de Oplossing / About the Solution

### A1. Hoeveel energie wordt als warmte teruggewonnen? / How much energy is captured as heat?

**Approved Answer (NL):**
Het datacenter zet vrijwel alle elektrische energie om in warmte. We vangen die restwarmte op via ons koelsysteem en leveren het via een warmtewisselaar en warmteleiding aan uw kas. Afhankelijk van de configuratie (directe levering of met warmtepomp) leveren we 40-55°C direct, of tot 80°C met warmtepompopwaardering. De hoeveelheid warmte hangt af van het IT-vermogen van het datacenter.

**Approved Answer (EN):**
The data center converts virtually all electrical energy into heat. We capture this waste heat via our cooling system and deliver it through a heat exchanger and heat pipe to your greenhouse. Depending on configuration (direct or with heat pump uplift), we supply 40-55°C direct, or up to 80°C with heat pump. The heat volume depends on the DC's IT capacity.

**Key Facts:**
- Direct DC output: 40-55°C (matches buisrail base load, groeipijp, gewasverwarming)
- With R717 (ammonia) heat pump uplift: up to 70-80°C (matches luchtverhitter, winter peak)
- Annual weighted COP of heat pump: 4.5-5.0
- DC operates 24/7/365 — continuous heat source, more predictable than geothermal or biomass

**NEVER SAY:**
- "70°C or higher" without specifying this requires heat pump uplift (website inaccuracy)
- "Mining" — DE does AI/HPC compute, not cryptocurrency mining
- Specific MWth numbers without checking project-specific design

**Source:** `skills/site-development/references/grower-thermal-interface.md`, `skills/dc-engineering/references/heat-pumps-waste-heat.md`
**Route if challenged:** `dc-engineering`

---

### A2. Welke temperatuur leveren jullie? / What temperature do you provide?

**Approved Answer (NL):**
Dat hangt af van uw verwarmingssysteem en gewas. Direct uit het datacenter leveren we 40-55°C — dat dekt het basislast van buisrailverwarming en groeipijpen prima. Voor hogere temperaturen (winter-piek, luchtverhitters) plaatsen wij een warmtepomp die opwaardeert tot 70-80°C. We ontwerpen altijd maatwerk op uw situatie.

**Approved Answer (EN):**
That depends on your heating system and crop. Direct from the DC we supply 40-55°C — that covers base load for rail-pipe and growing pipes well. For higher temperatures (winter peak, air heaters), we install a heat pump that uplifts to 70-80°C. We always design a custom solution for your situation.

**Key Facts (by heating system):**
| Systeem | Temperatuurbereik | DC Direct Match |
|---------|-------------------|-----------------|
| Buisrailverwarming | 40-90°C | Ja, voor basislast (40-55°C) |
| Groeipijp | 35-60°C | Uitstekend |
| Gewasverwarming | 30-50°C | Uitstekend |
| Luchtverhitter | 60-80°C | Nee, warmtepomp nodig |

**Key Facts (by crop):**
| Gewas | Piektemperatuur | DC Direct (40-55°C) |
|-------|-----------------|---------------------|
| Tomaat | 40-70°C | Deels (basislast) |
| Paprika | 45-75°C | Deels (basislast) |
| Komkommer | 50-80°C | Beperkt (warmtepomp) |
| Sierteelt | 35-60°C | Goed |
| Potplanten | 40-65°C | Goed |

**NEVER SAY:**
- "We leveren 70°C+" zonder te vermelden dat dit een warmtepomp vereist
- "Alle warmte direct uit het datacenter" — dit is misleidend voor hoge-temp gewassen
- Specifieke COP-waarden aan de kweker noemen (te technisch, route naar dc-engineering)

**Source:** `skills/site-development/references/grower-thermal-interface.md`
**Route if challenged:** `dc-engineering`

---

### A3. Wat gebeurt er met de warmte als wij die niet nodig hebben? / What happens with the heat when you don't need it?

**Approved Answer (NL):**
Het datacenter draait het hele jaar door, maar uw kas heeft vooral in het stookseizoen (oktober-april) warmte nodig. Buiten het stookseizoen wordt de warmte afgevoerd via ons dissipatiessysteem — droge koelers op het dak van het datacenter. Dit heeft geen impact op uw bedrijfsvoering. We onderzoeken ook seizoensopslag (WKO/ATES) om overtollige zomerwarmte op te slaan voor de winter.

**Approved Answer (EN):**
The DC runs year-round, but your greenhouse mainly needs heat during the heating season (October-April). Outside the season, heat is dissipated via our cooling system — dry coolers on the DC roof. This has zero impact on your operations. We are also exploring seasonal storage (ATES) to store excess summer heat for winter use.

**Key Facts:**
- DC heat output is 24/7/365 — this is a fundamental mismatch with greenhouse seasonal demand
- ATES (Aquifer Thermal Energy Storage): round-trip efficiency 60-80%, cost EUR 1-3M for 5-10 MWth
- Buffer tank sizing: 4-hour buffer typical (60-80 m3 per MWth, EUR 50-80K per MWth)
- Backup gasketel investment: EUR 300-600K CAPEX for N+1 redundancy

**NEVER SAY:**
- "Geen energieverspilling" — some heat IS dissipated in summer; be honest
- Specific ATES costs without project-level design

**Source:** `skills/dc-engineering/references/heat-recovery-integration.md`, `skills/dc-engineering/references/heat-pumps-waste-heat.md`

---

### A4. Kan de infrastructuur hergebruikt worden als het concept niet werkt? / Can the infrastructure be repurposed?

**Approved Answer (NL):**
Ja. De warmte-infrastructuur (leidingen, warmtewisselaars, buffervaten) is standaard industrieel materiaal dat hergebruikt kan worden voor andere warmtebronnen — denk aan geothermie of industriele restwarmte. Het datacentergebouw is ook adapteerbaar voor andere functies. Maar het belangrijkste: het concept werkt al. We bouwen bewezen technologie, geen experiment. Datacenters draaien al tientallen jaren 24/7, en restwarmtebenutting is in Scandinavie al standaard.

**Approved Answer (EN):**
Yes. The heat infrastructure (pipes, heat exchangers, buffer tanks) is standard industrial equipment reusable for other heat sources — geothermal, industrial waste heat, etc. The DC building is also adaptable. But most importantly: this concept works. We build proven technology, not an experiment. Data centers have operated 24/7 for decades, and waste heat utilization is already standard in Scandinavia.

**NEVER SAY:**
- "Mining" or "minen" — DE does AI/HPC, not crypto mining
- "Als het niet werkt" — don't validate the premise; reframe to proven technology

**Source:** `skills/dc-engineering/references/heat-recovery-integration.md`

---

## Category B: Vereisten en Kosten / Requirements & Costs

### B1. Wat is de minimale elektrische capaciteit? / What is the minimum electrical capacity required?

**Approved Answer (NL):**
Wij zoeken locaties met minimaal 5 MVA netaansluiting. Grotere aansluitingen (10-25 MVA) zijn ideaal en geven meer warmtelevering. De netaansluiting is de #1 waarde-driver voor ons — een goede aansluiting zonder congestie maakt uw locatie bijzonder aantrekkelijk.

**Approved Answer (EN):**
We look for locations with at least 5 MVA grid connection. Larger connections (10-25 MVA) are ideal and enable more heat delivery. The grid connection is the #1 value driver for us — a good connection without congestion makes your site particularly attractive.

**Key Facts:**
- Minimum viable: 5 MVA grid connection
- Sweet spot: 10-25 MVA
- Grid connection = 30% of lead qualification score weight
- Red flag: no existing grid connection or heavily congested zone

**NEVER SAY:**
- Exact MW-to-warmte conversion without project-specific design
- "We gebruiken uw netaansluiting" — frame as "we coordineren" or "cable pooling"

**Source:** `skills/sales-intake/references/intake-questions-site.md` (Q3.4-GRW)

---

### B2. Kan het project kleiner beginnen dan 5 MW? / Can the project start smaller than 5 MW?

**Approved Answer (NL):**
In principe is 5 MW het minimum voor een rendabel project vanwege de vaste kosten (infrastructuur, vergunningen, aansluiting). Maar als u onderdeel bent van een cluster van kwekers, kan het individuele aandeel kleiner zijn. We bekijken altijd de locatie als geheel.

**Approved Answer (EN):**
In principle, 5 MW is the minimum for a viable project due to fixed costs (infrastructure, permits, connections). However, if you're part of a grower cluster, the individual share can be smaller. We always evaluate the location as a whole.

**Key Facts:**
- Gas bill < EUR 200K/year = red flag for scale viability
- Clustering: one anchor grower + neighboring growers can make smaller individual sites viable
- Telersvereniging/cooperatie membership can enable cluster deals

**Source:** `skills/sales-intake/references/intake-questions-site.md` (Q2.5-GRW), `skills/sales-intake/references/icp-profiles.md`

---

### B3. Wat zijn de verantwoordelijkheden van de kweker? / What are the customer's responsibilities?

**Approved Answer (NL):**
Uw verantwoordelijkheden zijn beperkt:
1. **Grond beschikbaar stellen** — via recht van opstal (zakelijk recht, geen eigendomsoverdracht)
2. **Warmteaansluiting** — de leiding van de warmte-koude-centrale (WKC) naar uw ketelruimte. Kosten: EUR 25.000-100.000 afhankelijk van afstand
3. **Meewerken aan vergunningen** — als mede-aanvrager of met verklaring warmteafnemer
4. **SDE++ ondersteuning** — tekenen van de verklaring warmteafnemer voor de SDE++-aanvraag

Wij (Digital Energy) bouwen, financieren en onderhouden het complete datacenter en de warmte-infrastructuur. Uw investering is nul.

**Approved Answer (EN):**
Your responsibilities are limited:
1. **Make land available** — via recht van opstal (superficies right, not ownership transfer)
2. **Heat connection** — the pipe from the WKC (heat-cold central) to your boiler room. Cost: EUR 25,000-100,000 depending on distance
3. **Permit cooperation** — as co-applicant or with heat buyer declaration
4. **SDE++ support** — signing the verklaring warmteafnemer for the SDE++ application

We (Digital Energy) build, finance, and maintain the complete data center and heat infrastructure. Your investment is zero.

**Key vocabulary:**
- WKC = Warmte-Koude Centrale (heat-cold central) — the building housing heat exchangers and heat pumps
- Recht van opstal = right of superficies — a registered property right (zakelijk recht) that separates land ownership from building ownership. The grower retains land ownership.
- Verklaring warmteafnemer = heat buyer declaration — mandatory document for SDE++ application

**NEVER SAY:**
- "Het kost u niets" als absoluut statement — de warmteaansluiting (EUR 25-100K) is voor rekening van de kweker
- Specifieke EUR bedragen voor de warmteaansluiting zonder site-specifiek ontwerp
- "Eigendomsoverdracht" — het is recht van opstal, niet verkoop van grond

**Source:** `skills/site-development/references/grower-thermal-interface.md`, `skills/grower-relationship-mgr/SKILL.md` (section 2)

---

### B4. Hoeveel ruimte heeft de WKC nodig? / How much space does the WKC require?

**Approved Answer (NL):**
De WKC (warmte-koude-centrale) beslaat circa 200 m2 per MW IT-vermogen. Het totale datacenter-perceel inclusief WKC, IT-hal, en buitenruimte is groter — reken op minimaal 2.000 m2 voor een basis-installatie. De exacte footprint hangt af van het ontwerp en het vermogen.

**Approved Answer (EN):**
The WKC (heat-cold central) covers approximately 200 m2 per MW of IT capacity. The total DC plot including WKC, IT hall, and outdoor space is larger — expect a minimum of 2,000 m2 for a basic installation. The exact footprint depends on design and capacity.

**Key Facts:**
- Minimum site area: ~2,000 m2 (from intake question Q3.5-GRW)
- Distance to greenhouse matters: affects heat pipe costs (DN 100-150 for 1 MWth up to 500m)
- Pipe costs: EUR 1-3M/km — short distance is critical
- Thermal losses: 2-8 W/m depending on depth and insulation

**Source:** `skills/sales-intake/references/intake-questions-site.md` (Q3.5-GRW), `skills/dc-engineering/references/heat-recovery-integration.md`

---

## Category C: Warmte en Voordelen / Heat & Benefits

### C1. Wat is de prijs van de warmte? / What is the price of the heat?

**Approved Answer (NL):**
De warmte is gratis voor u. Digital Energy investeert in het datacenter en de warmte-infrastructuur. De SDE++-subsidie maakt het voor ons mogelijk om warmte zonder kosten aan u te leveren. U betaalt alleen de vaste kosten voor uw eigen warmteaansluiting (eenmalig, EUR 25-100K).

**Approved Answer (EN):**
The heat is free for you. Digital Energy invests in the data center and heat infrastructure. The SDE++ subsidy makes it possible for us to deliver heat to you at no cost. You only pay the fixed costs for your own heat connection (one-time, EUR 25-100K).

**NEVER SAY:**
- "We splitsen de SDE++" — creates entitlement expectation
- "De SDE++ is EUR X/GJ waard" — gives grower leverage to negotiate a share
- "U krijgt een percentage van de subsidie" — regulatory and tax complications
- Specifieke EUR/GJ heat price benchmarks (EUR 12-18/GJ is internal; never share)

**Acceptable Framing:**
- "SDE++ maakt onze investering haalbaar, waardoor wij de warmte gratis kunnen leveren"
- "De subsidiestructuur maakt het mogelijk dat wij de hele infrastructuur bouwen zonder investering van uw kant"

**Exception criteria for revenue sharing (CEO + CFO approval only):**
- Anchor sites with exceptional strategic value (first reference project)
- Very large heat demand (>10 MWth)
- Grower cluster hubs (access to 3+ additional growers)
- Sites with unique grid access (>20 MVA immediately available)

**Source:** `skills/grower-relationship-mgr/SKILL.md` (section 5 — SDE++ Structuring Guidance)
**Route if challenged:** `ops-dealops`, `legal-counsel`

---

### C2. Is de gratis warmteprijs gekoppeld aan de SDE++ subsidie? / Is the free heat linked to the SDE++ subsidy?

**Approved Answer (NL):**
De SDE++-subsidie behoort aan Digital Energy als warmteproducent en investeerder. De subsidie maakt het voor ons mogelijk om de hele infrastructuur te bouwen en warmte gratis te leveren. Als de SDE++ er niet zou zijn, zouden wij een warmteprijs moeten berekenen. Maar dankzij de SDE++ kunt u rekenen op gratis warmte voor de volledige contractduur.

**Approved Answer (EN):**
The SDE++ subsidy belongs to Digital Energy as the heat producer and investor. The subsidy enables us to build the entire infrastructure and deliver heat for free. Without the SDE++, we would need to charge a heat price. But thanks to the SDE++, you can count on free heat for the full contract term.

**Key Facts:**
- SDE++ duration: 15 years from first heat production
- Basisbedrag: EUR 8-12/GJ (set at application, guaranteed)
- Correctiebedrag: variable based on gas market prices
- SDE++ flows to heat producer (DE/SPV), not the grower
- Verklaring warmteafnemer (heat buyer declaration) — grower must sign this

**NEVER SAY:**
- "We delen de SDE++" — NOOIT
- Specifieke EUR/GJ bedragen van het basisbedrag of correctiebedrag
- "De subsidie loopt af na 15 jaar, dan betaalt u" — frame unknown future positively

**Source:** `skills/grower-relationship-mgr/SKILL.md` (section 5), `skills/netherlands-permitting/references/sde-subsidies.md`

---

### C3. Ik heb al goedkope warmte. Wat brengen jullie? / I already have cheap heat. What do you bring?

**Approved Answer (NL):**
Vergelijk ons niet alleen op warmteprijs. Ons voorstel:
1. **Stabiliteit** — vaste, langetermijn warmteprijs (nul). Geen gasmarktrisico, geen CO2-heffing
2. **Nul investering** — u hoeft niets te bouwen of te financieren
3. **Aanvullende inkomsten** — grondhuur voor het datacenter-perceel (EUR 5-15/m2/jaar)
4. **Toekomstbestendig** — voldoet nu al aan komende CO2-wetgeving (CO2-heffing stijgt van EUR 9,50/ton in 2025 naar EUR 17,70+ in 2030)
5. **Verduurzaming** — echte CO2-reductie voor uw bedrijf, relevant voor supermarkten en retail

**Key Facts:**
- Current WKK gas cost: EUR 500K-5M/year for viable growers
- CO2-heffing trajectory: EUR 9.50/ton (2025) → EUR 17.70/ton (2030) → EU ETS-2 (higher)
- Energy = 20-30% of total operating costs for Dutch greenhouses
- Ground rent benchmark: EUR 5-15/m2/year for agricultural land in NL
- Competition from Spain has 9-17x lower heating cost per kg product

**Competitive positioning:**
| Alternatief | Nadeel t.o.v. DE |
|-------------|------------------|
| Gas (status quo) | EUR 500K-5M/jaar, stijgende CO2-heffing, prijsvolatiliteit |
| Geothermie | EUR 15-25M investering, boorrisico, geen garantie op warmte |
| Biomassa | EUR 2-5M + brandstofkosten + luchtkwaliteitsvergunning, politiek gevoelig |
| Warmtepomp | Hoge elektriciteitskosten, netcapaciteit nodig |
| DE | EUR 0 investering, gratis warmte, grondhuur als extra inkomen |

**Source:** `skills/sales-intake/references/icp-profiles.md` (S-GRW), `skills/grower-relationship-mgr/SKILL.md` (section 2)

---

### C4. Past het project bij onze duurzaamheidsdoelen? / Can the project integrate with our sustainability goals?

**Approved Answer (NL):**
Absoluut. Door gas te vervangen met restwarmte vermindert u uw CO2-uitstoot direct. Dit helpt bij:
- Sector-doelstelling klimaatneutraal 2040
- CO2-heffing compliance (EUR 9,50/ton nu, stijgt naar EUR 17,70+)
- Duurzaamheidsrapportage richting supermarkten en retail
- Vermindering gasafhankelijkheid
En het belangrijkste: dit is geen greenwashing. Het is daadwerkelijke CO2-reductie, meetbaar via de GJ-teller.

**Source:** `skills/grower-relationship-mgr/SKILL.md` (section 2, pillar 5)

---

## Category D: CO2 Dosering / CO2 Dosing — CRITICAL TOPIC

> **Dit is het #1 grower concern. Bereid je hier altijd goed op voor.**

### D1. Wat gebeurt er met mijn CO2 als ik mijn WKK vervang? / What happens to my CO2 when I replace my CHP?

**Approved Answer (NL):**
Dit is een terechte en belangrijke vraag. Uw WKK levert nu niet alleen warmte maar ook CO2 (rookgas) voor gewasdosering. CO2-dosering verhoogt uw opbrengst met 15-30% — dat willen we absoluut niet kwijtraken.

Wij hebben drie bewezen oplossingen, afhankelijk van uw locatie:

1. **OCAP-leiding** (Westland/Rijnmond): Bewezen, kosteneffectief (EUR 10-50K/jaar). De meeste Westland-kwekers gebruiken dit al of kunnen aansluiten.
2. **Gedeeltelijke WKK-behoud**: U houdt uw WKK aan voor CO2-productie, wij leveren de basislast warmte. U draait de WKK alleen voor CO2, niet meer voor warmte.
3. **Zuiver CO2-levering** (Linde/Air Liquide): EUR 80-150/ton. Duurder, maar geschikt voor locaties buiten het OCAP-gebied.

De CO2-oplossing wordt expliciet opgenomen in de overeenkomst. We lossen dit samen op voordat we beginnen.

**Approved Answer (EN):**
This is a valid and important question. Your CHP currently delivers not only heat but also CO2 (flue gas) for crop dosing. CO2 dosing increases your yield by 15-30% — we absolutely don't want to lose that.

We have three proven solutions, depending on your location:

1. **OCAP pipeline** (Westland/Rijnmond): Proven, cost-effective (EUR 10-50K/year). Most Westland growers already use this or can connect.
2. **Partial CHP retention**: You keep your CHP for CO2 production only, we supply base load heat. You run the CHP for CO2, not for heating anymore.
3. **Pure CO2 delivery** (Linde/Air Liquide): EUR 80-150/ton. More expensive, but suitable for locations outside the OCAP area.

The CO2 solution is explicitly included in the agreement. We solve this together before we start building.

**Key Facts:**
- Dutch greenhouses dose 30-50 kg CO2/m2/year
- CO2 dosing increases yield by 15-30% — losing it means losing 15-30% of revenue
- OCAP pipeline cost: EUR 1-5/m3, EUR 10-50K/year (Westland/Rijnmond area)
- Pure CO2 delivery: EUR 80-150/ton (Linde, Air Liquide)
- Direct air capture: EUR 400-600/ton (not yet viable at scale)
- CO2 solution assessment is Phase 2 of the partnership lifecycle

**NEVER SAY:**
- "Dat lossen we later op" — CO2 is een dealbreaker, niet een detail
- "U heeft OCAP niet nodig" — als ze buiten het OCAP-gebied zitten, is dat misleidend
- Specifieke CO2-kosten zonder locatie-specifieke check

**Source:** `skills/site-development/references/grower-thermal-interface.md` (CO2 Dosing Gap section), `skills/grower-relationship-mgr/SKILL.md` (section 8)
**Route if challenged:** `dc-engineering`

---

## Category E: Proces en Tijdlijn / Process & Timeline

### E1. Wat is de tijdlijn van het project? / What are the project timelines?

**Approved Answer (NL):**
De totale doorlooptijd van HoT-tekening tot warmtelevering is 18-36 maanden, afhankelijk van vergunningen en netaansluiting:

| Fase | Doorlooptijd |
|------|-------------|
| Site assessment + warmteprofiel | 2-4 maanden |
| Vergunningstraject | 6-18 maanden (gemeente-afhankelijk) |
| SDE++-aanvraag | Jaarlijks window (okt-nov), beschikking 3-6 maanden later |
| Bouw | 8-12 maanden |
| Commissioning | 1-2 maanden |

De vergunning is vaak de langste factor. In gemeenten die ervaring hebben met datacenters gaat het sneller. In nieuwe gemeenten kan een bestemmingsplanwijziging nodig zijn (+6 maanden).

**Key Facts:**
- SDE++ application window: October-November each year
- Haalbaarheidsstudie: prepare 3-6 months before SDE++ window
- Realisatietermijn after beschikking: typically 4 years
- Bankgarantie: EUR 10-25 per kW, forfeited if project not completed on time
- Currently 5 Westland projects blocked by TAM-IMRO voorbereidingsbesluit — realistic first permit: Q4 2026 / Q1 2027

**NEVER SAY:**
- "Over een jaar draait het" — onrealistisch voor de meeste locaties
- Specifieke vergunningsdata voor Westland-projecten (blokkade actief)
- "De vergunning is geen probleem" — dit verschilt sterk per gemeente

**Source:** `skills/grower-relationship-mgr/SKILL.md` (section 3 — Lifecycle), `skills/netherlands-permitting/references/sde-subsidies.md`
**Route if challenged:** `netherlands-permitting`

---

### E2. Hoe lang is de contractduur? / How long is the contract term?

**Approved Answer (NL):**
Het contract is typisch 15-25 jaar, vergelijkbaar met andere warmtebronnen zoals geothermie. Het verschil: bij ons investeert u niets en draagt u geen risico. Na de contractperiode zijn er opties voor verlenging of aanpassing.

De SDE++-subsidie loopt 15 jaar. Het grondgebruik (recht van opstal) kan een langere of gelijke looptijd hebben.

**Approved Answer (EN):**
The contract is typically 15-25 years, comparable to other heat sources like geothermal. The difference: with us, you invest nothing and carry no risk. After the contract period, there are options for extension or adjustment.

The SDE++ subsidy runs 15 years. The land use (recht van opstal) can have an equal or longer duration.

**Key Facts (current HoT durations):**
| Project | HoT Duur |
|---------|----------|
| PowerGrow | 1 jaar |
| EP Flora | 1 jaar |
| Schenkeveld | 15 jaar |
| ECW | 15 jaar |
| YoungGrow, Moerman, Knoppert, Senzaro, Richplant | 30 jaar |

**NEVER SAY:**
- "30 jaar is standaard" — HoT-duren varieren sterk per project
- Specifieke duur van een ander project tenzij de kweker er expliciet om vraagt
- "U zit vast voor 30 jaar" — frame als stabiliteit, niet als verplichting

**Source:** `contracts/hots/` (individual HoT documents), `financial/_INDEX.md`

---

### E3. Wie bepaalt de timing en hoeveelheid warmteproductie? / Who determines the timing and amount of heat production?

**Approved Answer (NL):**
Het datacenter draait op basis van de vraag van onze compute-klanten, niet op basis van uw warmtebehoefte. Dat klinkt misschien als een nadeel, maar in de praktijk betekent het dat u een continue, betrouwbare warmtebron heeft:

- Het datacenter draait ~7.000 uur/jaar (80% uptime target)
- De warmteproductie is voorspelbaar en constant
- Een buffervat vangt korte onderbrekingen op (4-8 uur buffer standaard)
- Een backup-gasketel is altijd beschikbaar voor piekmomenten en onderhoud

Uw teelt bepaalt hoeveel warmte u afneemt. U heeft volledige controle over uw verwarmingssysteem.

**Key Facts:**
- DC target uptime: ~80% = ~7,000 hrs/year
- Buffer tank: 4-hour standard (60-80 m3 per MWth)
- Backup gasketel: EUR 300-600K CAPEX (part of redundancy design)
- SLA priority: DC cooling takes priority over heat delivery (MSA terms v5.1)

**NEVER SAY:**
- "De warmte is 100% beschikbaar" — de SLA prioriteert DC koeling boven warmtelevering
- "U bepaalt wanneer het datacenter draait" — dat is niet zo
- Specifieke uptime-garanties zonder contractuele basis

**Source:** `contracts/msas/sla-terms-v5.1.md`, `skills/dc-engineering/references/heat-recovery-integration.md`

---

## Category F: Risicobeheer / Risk Management

### F1. Wat als Digital Energy failliet gaat? / What are the risks if Digital Energy goes bankrupt?

**Approved Answer (NL):**
Dit is een terechte zorg. Wij hebben dit juridisch gestructureerd om u te beschermen:

1. **Gescheiden SPV** — elk project zit in een aparte vennootschap (SPV). Een probleem bij een ander project raakt uw project niet.
2. **Backup-gasketel** — uw bestaande of nieuwe gasketel blijft beschikbaar. Uw teelt loopt nooit gevaar.
3. **Recht van opstal** — als DE het recht van opstal niet meer uitoefent, vervalt het gebouw aan u als grondeigenaar (natrekking).
4. **Contractuele bescherming** — het contract bevat boeteclausules bij niet-levering en overdraagbaarheidsbepalingen.
5. **Netaansluiting** — u behoudt het recht om de netaansluiting te gebruiken of over te nemen.

**Key Facts:**
- Total SPVs: 12 DEC BVs + 12 Thermal BVs (separate legal entities per project)
- Holding entity: Eco-Digital AG (Switzerland)
- NL operating entity: DE Netherlands BV
- Recht van opstal is a registered property right (zakelijk recht) at the kadaster

**NEVER SAY:**
- "Dat kan niet gebeuren" — niet geloofwaardig
- Details over de Zwitserse holdingstructuur tenzij specifiek gevraagd
- "Wij zijn te groot om failliet te gaan" — we zijn een startup

**Source:** `company/entity-register.md`, `contracts/msas/sla-terms-v5.1.md`
**Route if challenged:** `legal-counsel`

---

### F2. Wat gebeurt er met de netaansluiting bij een faillissement? / What happens with the grid connection in case of default?

**Approved Answer (NL):**
Bij beeindiging van het contract of faillissement heeft u het recht om de netaansluiting te gebruiken of over te nemen. Dit is contractueel vastgelegd. De netaansluiting is op uw grond geinstalleerd en gekoppeld aan uw locatie — die kan niet worden 'meegenomen'.

**NEVER SAY:**
- Specifieke juridische clausules zonder contract-review door legal-counsel
- "De netaansluiting is van u" — het eigendom hangt af van de contractuele structuur

**Source:** `contracts/msas/sla-terms-v5.1.md`
**Route if challenged:** `legal-counsel`

---

### F3. Kunnen bestaande ketels als backup dienen? / Can existing assets (e.g., boilers) be used for backup?

**Approved Answer (NL):**
Ja, absoluut. Uw bestaande gasketel wordt onderdeel van het backup-systeem. De standaard configuratie:

1. **Primair**: Datacenter-restwarmte (+ warmtepomp indien nodig)
2. **Buffer**: Buffervat voor 4-8 uur
3. **Backup**: Uw bestaande gasketel voor piek en onderhoudsmomenten

U gooit uw oude ketel dus niet weg — die wordt uw verzekering. De exploitatiekosten van de ketel dalen dramatisch omdat die alleen nog als backup draait.

**Key Facts:**
- Backup investment total: EUR 500K-1.5M (DEC backup boiler + buffer tank + N+1 heat pump)
- DEC backup boiler: EUR 300-600K CAPEX (part of DE's investment, not grower's)
- Grower's existing boiler: stays as secondary backup (grower's responsibility to maintain)
- Buffer tank standard: 4-hour buffer (60-80 m3 per MWth)

**Source:** `skills/site-development/references/grower-thermal-interface.md`, `skills/dc-engineering/references/heat-recovery-integration.md`

---

## Category G: Juridisch en Grond / Legal & Land — MISSING FROM WEBSITE

### G1. Wat is recht van opstal? / What is the right of superficies?

**Approved Answer (NL):**
Recht van opstal is een zakelijk recht — geregistreerd bij het kadaster — dat Digital Energy het recht geeft om een gebouw (het datacenter) te plaatsen op uw grond. U blijft eigenaar van de grond. Het gebouw is eigendom van Digital Energy. Dit is vergelijkbaar met hoe zendmasten of transformatorhuisjes op agrarische grond staan.

Belangrijke punten:
- U verkoopt geen grond
- U behoudt volledige controle over de rest van uw perceel
- Het recht is tijdelijk (gekoppeld aan de contractduur)
- Bij beeindiging: het gebouw kan worden verwijderd of valt toe aan u (natrekking)

**Key vocabulary:**
- Recht van opstal = right of superficies (Book 5, Article 101 Dutch Civil Code)
- Zakelijk recht = real property right (registered at kadaster)
- Natrekking = accession (building becomes part of the land when the right expires)
- Notaris = required for registration

**NEVER SAY:**
- "Wij kopen uw grond" — nooit, het is recht van opstal
- "Het is net als huur" — het is een zakelijk recht, juridisch sterker dan huur
- Specifieke notariskosten of juridische details zonder legal-counsel review

**Source:** `skills/grower-relationship-mgr/SKILL.md` (section 1 — Infrastructure Vocabulary)
**Route if challenged:** `legal-counsel`

---

### G2. Wat is de grondhuur? / What is the land lease/ground rent?

**Approved Answer (NL):**
Digital Energy betaalt een jaarlijkse grondhuur voor het perceel waarop het datacenter staat. Dit is een extra inkomstenbron voor u, bovenop de gratis warmte.

De grondhuur is marktconform voor agrarische grond in uw regio.

**NEVER SAY:**
- Specifieke EUR/m2/jaar bedragen aan nieuwe prospects (benchmark EUR 5-15/m2/yr is intern)
- "U wordt rijk van de grondhuur" — het is een solide bijverdienste, geen fortuin
- Grondhuur van andere projecten delen (concurrentiegevoelig)

**Source:** `skills/sales-intake/references/intake-questions-site.md` (Q4.4-GRW)
**Route if challenged:** `ops-dealops`

---

### G3. Wat als ik mijn kas verkoop? / What if I sell my greenhouse?

**Approved Answer (NL):**
De overeenkomst is overdraagbaar aan de nieuwe eigenaar. Sterker nog: het maakt uw bedrijf aantrekkelijker voor kopers. Een koper krijgt gesubsidieerde, gratis warmte — dat is een verkoopargument.

Het recht van opstal is een zakelijk recht dat met de grond meeloopt, niet met de eigenaar. Een nieuwe eigenaar neemt de rechten en plichten over.

**Source:** `skills/grower-relationship-mgr/SKILL.md` (section 9 — Common Concerns)

---

## Category H: Buren en Omgeving / Neighbors & Environment — MISSING FROM WEBSITE

### H1. Mijn buren gaan bezwaar maken / My neighbors will object

**Approved Answer (NL):**
Begrijpelijk. We hebben hier ervaring mee en pakken het proactief aan:

1. **Landschappelijke inpassing** — het datacenter wordt ontworpen passend bij de omgeving. Denk aan groene gevels, beperkte bouwhoogte, passend bij kassenbouw.
2. **Geluid** — moderne datacenters met vloeistofkoeling zijn significant stiller dan traditionele luchtgekoelde installaties. We houden ons aan geluidsnormen.
3. **Economisch voordeel** — het datacenter versterkt de lokale tuinbouw (gratis warmte, werkgelegenheid, verduurzaming). Dat is een verhaal voor de hele regio.
4. **Omgevingsdialoog** — wij initiëren het gesprek met omwonenden en gemeente, samen met u.

Framing-regel: altijd "tuinbouwversterking", nooit "datacenter-toelating".

**NEVER SAY:**
- "Daar merken ze niets van" — ongeloofwaardig en oneerlijk
- "Datacenter" in publieke communicatie zonder context van tuinbouwversterking
- Vergelijkingen met grote hyperscale datacenters (wij zijn 5-25 MW, niet 100+ MW)

**Source:** `skills/grower-relationship-mgr/SKILL.md` (section 9), `permitting/westland/strategy.md`

---

### H2. Wat is het geluid en de visuele impact? / What about noise and visual impact?

**Approved Answer (NL):**
Onze datacenters gebruiken vloeistofkoeling voor de servers. Dat betekent significant minder mechanische koeling en dus minder geluid dan traditionele datacenters. De WKC (warmte-koude-centrale) heeft wel koelers, maar die voldoen aan de Nederlandse geluidsnormen.

Visueel: het gebouw is compact (200 m2/MW), maximaal 8-10 meter hoog, en kan worden ingepast met groene gevels. Het past qua schaal en uiterlijk bij kasseninfrastructuur.

**NEVER SAY:**
- "Het is net zo stil als een koelkast" — ongefundeerd
- Specifieke dB-waarden zonder site-specifieke geluidsberekening
- "Het is onzichtbaar" — een gebouw is zichtbaar, maar past bij de omgeving

**Source:** `skills/dc-engineering/references/heat-recovery-integration.md`
**Route if challenged:** `dc-engineering`, `netherlands-permitting`

---

## Category I: Het Concept / The Concept — MISSING FROM WEBSITE

### I1. Wat is een "digitale brander"? / What is a "digital burner"?

**Approved Answer (NL):**
De digitale brander is ons concept: een datacenter als warmtebron voor uw kas, als vervanging van uw gasbrander of WKK. Net zoals uw WKK aardgas omzet in warmte en elektriciteit, zet ons datacenter elektriciteit om in rekenkracht en warmte. De warmte gaat naar u, de rekenkracht verkopen wij aan AI-bedrijven.

Simpel gezegd: wij vervangen uw gasbrander door een digitale brander. Dezelfde warmte, maar dan zonder gas, zonder CO2-uitstoot, en zonder kosten.

**NEVER SAY:**
- "Bitcoin-miner" of "cryptominer" — wij doen AI/HPC, geen crypto
- "Server-farm" — te simplistisch
- Technische details over GPU's of AI-workloads (niet relevant voor de kweker)

---

### I2. Wat is het verschil met een gewoon datacenter? / How is this different from a regular data center?

**Approved Answer (NL):**
Drie fundamentele verschillen:

1. **Co-locatie** — ons datacenter staat naast uw kas, niet op een bedrijventerrein. Dat maakt directe warmtelevering mogelijk.
2. **Warmtebenutting** — gewone datacenters blazen hun warmte de lucht in. Wij leveren die warmte aan u.
3. **Schaal** — wij bouwen 5-25 MW installaties, niet de mega-datacenters van 100+ MW die in het nieuws komen. Ons datacenter past in de tuinbouwomgeving.

---

## Category J: SDE++ Specifiek / SDE++ Specific — CRITICAL GUARDRAILS

### J1. Wat is de SDE++ en wat betekent het voor mij? / What is SDE++ and what does it mean for me?

**Approved Answer (NL):**
De SDE++ (Stimulering Duurzame Energieproductie en Klimaattransitie) is een overheidssubsidie die de productie van duurzame energie en warmte stimuleert. Restwarmte van datacenters valt onder de categorie "LT-warmte" (lage-temperatuur warmte).

Wat het voor u betekent:
- De SDE++ maakt het voor ons financieel mogelijk om de infrastructuur te bouwen
- Daardoor kunnen wij warmte gratis aan u leveren
- U tekent een verklaring warmteafnemer — dat bevestigt dat u de warmte gaat afnemen

Wat u NIET hoeft te doen:
- De SDE++ aanvragen (dat doen wij)
- De subsidie administreren
- Financieel risico dragen

**NEVER SAY:**
- "We splitsen de SDE++"
- "De SDE++ is EUR X/GJ waard"
- "U krijgt een percentage van de subsidie"
- "De SDE++ is gegarandeerd" — het is een aanvraag die goedgekeurd moet worden

**Critical SDE++ timeline awareness:**
- Application window: October-November each year
- Haalbaarheidsstudie: must be prepared 3-6 months before window
- Verklaring warmteafnemer: grower must sign (Co coordinates this)
- Realisatietermijn: heat delivery must start within ~4 years of beschikking
- Bankgarantie: EUR 10-25/kW — forfeited if project not completed

**Source:** `skills/netherlands-permitting/references/sde-subsidies.md`, `skills/grower-relationship-mgr/SKILL.md` (section 5)

---

## Website FAQ Discrepancies — FLAGS FOR REVIEW

> **These are inaccuracies on https://digital-energy.group/resources#faq that should be corrected.**

| # | Issue | Website Says | SSOT Says | Action |
|---|-------|-------------|-----------|--------|
| 1 | Temperature claim | "70°C or higher" | 40-55°C direct, up to 80°C with heat pump uplift | Update website to clarify HP uplift requirement |
| 2 | "Mining" reference | "Can the infrastructure be repurposed if mining becomes unfeasible?" | DE does AI/HPC, not mining | Replace "mining" with "AI computing" or "HPC" |
| 3 | Missing CO2 topic | Not mentioned | #1 grower concern (15-30% yield impact) | Add CO2 dosing FAQ section |
| 4 | Missing noise/visual FAQ | Not mentioned | Common neighbor concern | Add environmental impact section |
| 5 | Missing recht van opstal | Not mentioned | Critical legal concept for growers | Add legal/land section |
| 6 | WKC undefined | "WCK" used without definition | Should be "WKC" (Warmte-Koude Centrale) and defined | Define on first use |
| 7 | Missing "digitale brander" | Not mentioned | Core concept for grower understanding | Add concept explanation |
| 8 | Missing Dutch FAQ | English only | Growers prefer Dutch communication | Add Dutch FAQ version |
| 9 | Several empty answers | ~8 of 18 questions have no visible answer | Full answers available in this reference | Populate from this FAQ reference |

---

## Quick Reference: Communication Guardrails for Co

### Always Do
- Speak Dutch first (je/jij, not u)
- Lead with "gratis warmte" and "nul investering"
- Reference "Wat doet de buurman?" — peer adoption is the #1 decision driver
- Address CO2 proactively — never wait for the grower to bring it up
- Bring an engineer to the first meeting
- Give concrete next steps with dates
- Reference the grower's specific crop and heating system

### Never Do
- Share SDE++ EUR/GJ values or suggest splitting the subsidy
- Promise specific timelines for Westland permits (TAM-IMRO blokkade)
- Use "datacenter" without "tuinbouwversterking" context in public/gemeente settings
- Quote financial model numbers (FM v3.51 data is internal only)
- Say "mining" or "crypto" — it's AI/HPC
- Claim "70°C" without mentioning heat pump uplift
- Guarantee uptime percentages without contractual basis
- Share one project's HoT terms or ground rent with another grower

### Escalation Triggers
| Situation | Escalate To | Timeframe |
|-----------|------------|-----------|
| Grower asks for SDE++ revenue share | CEO + CFO (Carlos + Jelmer) | Before next meeting |
| Grower raises contract concerns | Legal counsel + Co | Within 48 hours |
| Grower hears negative info about DE | Carlos + Co | Within 24 hours |
| Competitor approaches grower | Carlos + Co + Jelmer | Within 48 hours |
| Municipality blocks permit | Netherlands-permitting + Co | Same day |

---

*This FAQ reference is sourced entirely from the SSOT. For updates, modify the source files and regenerate. Never hard-code financial data — all financial claims route through FM v3.51 via the financial-model-interpreter skill.*

*Last updated: 2026-03-07*
