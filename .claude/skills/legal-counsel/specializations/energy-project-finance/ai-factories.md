# AI Factory / GPU Compute Facility -- Projectfinanciering / Project Financing

Reference file for the `project-financing` skill. Provide detailed technical, financial, and regulatory context for AI compute infrastructure as an emerging project finance asset class in the Netherlands and the EU. All data sourced and attributed; verify against primary sources before reliance.

---

## 1. Definitie activaklasse / Asset Class Definition

### 1.1 Wat is een AI Factory? / What Constitutes an AI Factory?

Distinguish between three facility archetypes relevant to project finance structuring:

| Kenmerk (Characteristic) | Traditioneel datacenter (Traditional DC) | Colocatie datacenter (Colocation DC) | AI Factory / GPU Compute Facility |
|---|---|---|---|
| Primaire functie (primary function) | Enterprise IT, opslag (storage), netwerken | Ruimte, stroom, koeling verhuren aan derden (lease space/power/cooling to tenants) | Massaal parallelle GPU/accelerator-berekeningen (massively parallel GPU/accelerator compute) |
| Vermogensdichtheid (power density) | 6--15 kW/rack | 8--20 kW/rack | 40--140 kW/rack huidig; 240 kW/rack volgende generatie [Tom's Hardware 2025] |
| Koeling (cooling) | Luchtkoeling (air cooling) | Luchtkoeling; sommige DLC | Vloeistofkoeling verplicht (liquid cooling mandatory) |
| Inkomstenmodel (revenue model) | Interne kostenplaats (internal cost center) | Colocatie-vergoedingen (colocation fees, $/kW/month) | GPUaaS, training/inference contracts, managed AI infra |
| Huurder/klantrelatie (tenant relationship) | Eigen gebruik (captive) | Multi-tenant; wholesale/retail | Enkel-klant of multi-tenant compute; API-gebaseerd |
| Bouwperiode (construction) | 18--36 maanden | 18--36 maanden | 18--30 maanden (facility); 2--6 maanden GPU fit-out |
| Projectfinancieringsgeschiedenis (PF track record) | Beperkt (limited); corporate finance dominant | Gevestigd (established); REIT-structuren | Opkomend (emerging); beperkt track record |

### 1.2 GPU Compute Hardware Landscape

Identify the principal accelerator platforms relevant to lender technology due diligence:

| Platform | Fabrikant (Manufacturer) | Geheugen (Memory) | TDP per GPU | Typische clusterconfiguratie (Typical Cluster) | Status |
|---|---|---|---|---|---|
| H100 SXM | NVIDIA | 80 GB HBM3 | 700 W | DGX H100 (8 GPU, 10.2 kW) | Productie; breed ingezet (production; widely deployed) |
| H200 SXM | NVIDIA | 141 GB HBM3e | 700 W | DGX H200 (8 GPU) | Productie (production) |
| B200 | NVIDIA | 192 GB HBM3e | 1,000 W | DGX B200 (8 GPU, ~14.3 kW) | Productie 2025 |
| GB200 NVL72 | NVIDIA | 192 GB HBM3e per GPU | 1,200 W (GPU) + 600 W (CPU) | 72 GPU rack (~120 kW liquid-cooled) | Productie 2025; volledig vloeistofgekoeld |
| MI300X | AMD | 192 GB HBM3 | 750 W | OCP Accelerator Module (8 GPU) | Productie; alternatief voor H100 |
| TPU v5p / v6e | Google (custom ASIC) | Variabel | ~300--500 W per chip | Pods (6,144+ chips) | Google Cloud exclusief (captive) |
| Trainium2 | Amazon (custom ASIC) | Variabel | ~500 W per chip | UltraClusters (100K+ chips) | AWS exclusief (captive) |
| Gaudi 3 | Intel (Habana Labs) | 128 GB HBM2e | 900 W | Universal Baseboard (8 accelerator) | Productie; beperkte adoptie |

[NVIDIA product specs; AMD specs; Google Cloud TPU docs; AWS Trainium docs; Intel Gaudi docs]

### 1.3 Trainings- vs inferentiefaciliteiten / Training vs Inference Facilities

| Parameter | Trainingsfaciliteit (Training Facility) | Inferentiefaciliteit (Inference Facility) | Hybride (Hybrid) |
|---|---|---|---|
| Werklast (workload) | Grote batch; langlopend (large batch, long-duration) | Lage latentie; hoge doorvoer (low-latency, high-throughput) | Beide; dynamische toewijzing (both; dynamic allocation) |
| Typische duur per taak | Dagen tot maanden | Milliseconden tot seconden | Variabel |
| GPU-benuttingsgraad (utilization) | 70--95% tijdens training; clusters soms idle tussen taken | 40--80% gemiddeld; piekbelasting variabel | 60--85% (blended) |
| Netwerkvereisten (network) | Ultra-hoge bandbreedte inter-GPU (NVLink/NVSwitch, InfiniBand 400G/800G) | Lagere inter-GPU bandbreedte; hogere client-facing throughput | Beide topologieen noodzakelijk |
| Inkomstenprofiel (revenue profile) | Blokboekingen; langere contracten (block reservations; longer contracts) | Verbruiksgebaseerd; variabel (usage-based; variable) | Gemengd (blended) |
| Bankability voor financiers | Hoger (langere contracten, voorspelbaarder) | Lager (variabeler cashflow) | Middelhoog |

### 1.4 Vermogensdichtheid en koeling / Power Density and Cooling

Vermogensdichtheid (power density) is het onderscheidende kenmerk van AI factories:

| Generatie (Generation) | Dichtheid per rack (Density per rack) | Koelmethode (Cooling Method) | Bron (Source) |
|---|---|---|---|
| Traditioneel datacenter | 6--15 kW/rack | Luchtkoeling (air cooling) | Industrie standaard |
| AI huidig (H100/MI300X era) | 40--80 kW/rack | DLC + lucht hybride | NVIDIA DGX specs |
| AI high-density (B200/GB200) | 120--140 kW/rack | Directe vloeistofkoeling (DLC) verplicht | Tom's Hardware 2025 |
| AI next-gen (GB200 NVL72+) | Tot 240 kW/rack | Volledige vloeistofkoeling; immersiekoeling | Tom's Hardware 2025 |

Koelingsopties voor financiers:

| Koelmethode (Cooling Method) | Beschrijving (Description) | Rijpheid (Maturity) | CAPEX vs luchtkoeling | PUE impact |
|---|---|---|---|---|
| Directe vloeistofkoeling / Direct Liquid Cooling (DLC) | Koelplaten op CPU/GPU; warm water circuit | Volwassen (mature); voorkeur NVIDIA H100/B200 | +20--30% | 1.05--1.15 |
| Achterdeur-warmtewisselaars / Rear-Door Heat Exchangers (RDHx) | Warmtewisselaar op achterdeur van rack | Volwassen; retrofit-geschikt | +15--25% | 1.10--1.20 |
| Immersiekoeling / Immersion Cooling | Servers ondergedompeld in dielectrische vloeistof | Beperkt operationeel track record | +30--40% | 1.02--1.05 |
| Hybride (lucht + vloeistof) | Luchtkoeling voor netwerk/opslag; DLC voor GPU | Meest voorkomend in huidige deployments | +20--35% | 1.08--1.15 |

[Introl 2025; Schneider Electric White Papers; NVIDIA Design Guides]

---

## 2. Technologierisico / Technology Risk Assessment for Lenders

### 2.1 GPU Technologie-levenscyclus / GPU Technology Lifecycle

Beoordeel het technologierisico als materieel hoger dan traditioneel datacenter of BESS:

- **Snelle veroudering (rapid obsolescence):** Generatiecyclus van 18--36 maanden. NVIDIA: Hopper (2022) -> Blackwell (2024) -> Rubin (verwacht 2026). Elke generatie biedt 2--4x prestatieverbetering per watt.
- **Restwaarde (residual value):** Conservatieve aanname voor financiers: nul op Jaar 3--5. Tweedehands GPU-markt bestaat maar is volatiel en onzeker voor projectfinanciering.
- **GPU-vervangingsreserve (GPU refresh CAPEX reserve):** Verplicht door financiers; typisch 8--15% van GPU CAPEX per jaar gereserveerd uit kasstroom.
- **Padafhankelijkheid (path dependency):** CUDA-ecosysteem (NVIDIA) creëert software lock-in; overstap naar AMD ROCm of alternatieve platforms vereist significante investering.
- **Exportbeperkingen (export controls):** VS CHIPS Act en BIS export controls beinvloeden beschikbaarheid van cutting-edge GPUs in bepaalde markten.

### 2.2 Koelingsinfrastructuur / Cooling Infrastructure

| Risicofactor | Beoordeling (Assessment) | Mitigatie (Mitigation) |
|---|---|---|
| DLC lekrisico (leak risk) | Laag bij juiste installatie | Lekkagedetectie; drip trays; onderhoudsprotocol |
| Immersiekoeling track record | Beperkt; <5 jaar grootschalig | OEM garanties; pilotfase; onafhankelijk testen |
| Koelmiddel beschikbaarheid (coolant supply) | Medium; sommige koelmiddelen zijn gespecialiseerd | Langetermijnleveringscontracten; meerdere leveranciers |
| Koelsysteem single point of failure | Hoog risico bij uitval | N+1 redundantie; bypass systemen; noodkoeling |
| Retrofit risico | DLC kan worden geretrofit; immersie niet | Faciliteitontwerp met toekomstbestendige aansluitingen |

### 2.3 Stroomdistributie / Power Distribution

| Parameter | Minimumeis (Minimum Requirement) | Best practice | Toelichting (Notes) |
|---|---|---|---|
| Redundantie (redundancy) | N+1 voor alle kritieke systemen | 2N voor missiekritieke trainingsclusters | 2N vereist dubbele investering in UPS/generatoren |
| UPS autonomie | 5--10 minuten | 10--15 minuten | Overbrugging tot noodstroom (diesel/gas) |
| PUE luchtgekoeld (air-cooled) | 1.4--1.8 | <1.4 | Niet geschikt voor high-density AI |
| PUE vloeistofgekoeld (liquid-cooled) | 1.05--1.15 | 1.02--1.05 | Best-in-class: 1.02 [Introl 2025] |
| Stroomkwaliteit (power quality) | UPS met dubbele conversie | Flywheel + batterij UPS | GPU-clusters zijn gevoelig voor stroomonderbrekingen |

### 2.4 Bankbaarheid voor financiers / Lender Bankability Assessment

Financiers dienen de volgende technologiecriteria te beoordelen:

- **Onafhankelijke technische due diligence (IE assessment):** Verplicht; IE-rapport over koeling, stroomdistributie, GPU-configuratie, en faciliteitontwerp.
- **OEM-garantieovereenkomsten:** NVIDIA DGX/HGX Enterprise Support; AMD Instinct support; minimaal 3--5 jaar hardware garantie en onderhoudscontract.
- **Bewezen technologie (proven technology):** Voorkeur voor 2+ jaar operationele data; nieuwe koeltechnologieen vereisen aanvullende buffers.
- **GPU-vervangingsreserve (refresh reserve):** Gefinancierd uit kasstroom; opgenomen in financieel model als verplichte reserverekening.
- **Verzekeringsdekking (insurance):** Technologie-prestatiegarantie (technology performance warranty) -- beperkt beschikbaar; brandverzekering (fire); bedrijfsschadeverzekering (business interruption, BI). NB: immersiekoeling met brandbare koelmiddelen vereist aanvullende brandverzekering.

---

## 3. Inkomstenmodellen / Revenue Models

### 3.1 Cloud Compute / GPU-as-a-Service (GPUaaS)

GPU-uurtarieven zijn sterk gedaald sinds de lancering van H100 en vertonen verdere differentiatie naar generatie:

| GPU-model | Bereik (Range) | Gestabiliseerd tarief | Daling sinds lancering | Bron (Source) |
|---|---|---|---|---|
| H100 SXM | $1.49--$4.00/GPU-uur | $2.85--$3.50/GPU-uur | 64--75% | GMI Cloud 2025; IntuitionLabs |
| A100 SXM | $0.80--$1.89/GPU-uur | $1.00--$1.50/GPU-uur | 70--80% | Diverse cloud providers |
| B200 | $3.99--$18.53/GPU-uur | Nog niet gestabiliseerd | N.v.t. (te nieuw) | Northflank; Modal |
| GB200 NVL72 | Beperkte beschikbaarheid | Nog niet vastgesteld | N.v.t. | Vroege deployments |
| MI300X | $1.29--$3.49/GPU-uur | $2.00--$2.80/GPU-uur | 50--65% | Diverse cloud providers |

Prijsdifferentiatie:

| Contracttype (Contract Type) | Typische korting vs on-demand | Toelichting (Notes) |
|---|---|---|
| On-demand / spot | Basis (geen korting) | Hoogste prijs; geen commitment; variabele beschikbaarheid |
| Gereserveerde instanties (reserved) 1 maand | 10--25% korting | Gegarandeerde beschikbaarheid |
| Gereserveerde instanties 3--12 maanden | 25--50% korting | Vooruitbetaling gebruikelijk |
| Gereserveerde instanties 1--3 jaar | 40--65% korting | Meest bankbaar voor PF; vergelijkbaar met take-or-pay |
| Spot/preemptible | 60--80% korting vs on-demand | Onderbrekbaar; niet geschikt als basis voor schuldendienst |

### 3.2 AI Training-as-a-Service (TaaS)

- Grote taalmodel (LLM) trainingswerklast; klant levert data en modelarchitectuur.
- Multi-year contracten (1--5 jaar) met take-or-pay structuur meest bankbaar.
- Klantprofiel: hyperscalers (overstroom naar derden), AI-startups met VC-financiering, enterprises.
- Risico: klantconcentratie; creditwaardigheid van AI-startups is beperkt.
- Mitigatie: vooruitbetaling (prepayment); moederbedrijfgarantie (parent company guarantee); escrow.

### 3.3 Inference-as-a-Service (IaaS)

- Lagere marge per GPU-uur; hogere benuttingsgraad (24/7 productieverkeer).
- API-gebaseerde prijsstelling: per token (LLM), per verzoek (request), per seconde compute.
- Geschikt voor stabiele basisinkomsten; aanvulling op training-inkomsten.
- Inkomstenstabiliteit afhankelijk van eindgebruikersadoptie van AI-toepassingen.

### 3.4 Managed AI Infrastructure

- Full-stack aanbod: hardware + softwarestack + orkestratie (Kubernetes, Slurm) + ondersteuning.
- Premiumprijsstelling: 20--50% boven standaard GPUaaS.
- Langere contracttermijnen (2--5 jaar) gebruikelijk.
- Hogere operationele complexiteit; vereist specialistisch personeel.

### 3.5 Overzicht inkomstzekerheid / Revenue Certainty Spectrum

| Contracttype (Contract Type) | Looptijd (Term) | Bankbaarheid (Bankability) | Hefboom impact (Gearing Impact) | Toelichting (Notes) |
|---|---|---|---|---|
| Take-or-pay meerjarig (multi-year) | 3--7 jaar | Hoogste | Hogere hefboom mogelijk (60--65%) | Voorkeur van senior financiers; vergelijkbaar met PPA in energiesector |
| Gereserveerde instanties (reserved) | 1--3 jaar | Hoog | Gematigd hogere hefboom (55--60%) | Vooruitbetaalde kortingen gebruikelijk |
| Verbruiksgebaseerd met minimum commitment | 1--2 jaar | Middelhoog | Basis hefboom (50--55%) | Bodeminkomsten (floor revenue) + opwaarts potentieel |
| Spot / on-demand | Geen | Laagste | Laagste hefboom (40--50%) | Volledig merchant risico; vergelijkbaar met merchant BESS |

### 3.6 Omzet per MW / Revenue per MW

| Parameter | AI Factory | Traditioneel Datacenter | Verhouding (Ratio) | Bron (Source) |
|---|---|---|---|---|
| Indicatieve omzet per MW per jaar | ~$12.5M | ~$4.2M | ~3.0x | Alpha-Matica |
| EBITDA-marge (indicatief) | 40--60% | 45--55% | Vergelijkbaar | Sector gemiddelden |
| Indicatieve EBITDA per MW per jaar | ~$5.0--7.5M | ~$1.9--2.3M | ~2.6--3.3x | Berekend |

NB: Werkelijke omzet varieert sterk afhankelijk van GPU-dichtheid, benuttingsgraad, prijsmodel, type werklast, en contractmix. Bovenstaande cijfers zijn indicatief en gebaseerd op blended aannames.

---

## 4. Kengetallen / Key Metrics and Benchmarks

### 4.1 Technische kengetallen / Technical Metrics

| Kengetal (Metric) | Benchmark | Bron (Source) |
|---|---|---|
| GPU-dichtheid (GPU density) | 8--16 GPUs per rack (DGX/HGX configuratie) | NVIDIA productspecificaties |
| Vermogen per GPU (power per GPU) | 700 W (H100) -- 1,200 W (GB200) | NVIDIA productspecificaties |
| Vermogen per rack (power per rack) | 40--240 kW (generatie-afhankelijk) | Tom's Hardware 2025 |
| PUE vloeistofgekoeld (liquid-cooled PUE) | 1.05--1.15; best-in-class 1.02 | Introl 2025 |
| PUE luchtgekoeld (air-cooled PUE) | 1.4--1.8 | Industrie standaard |
| Benuttingsgraad doelstelling (utilization target) | 70--90% | Industrie benchmark |
| Netwerk bandbreedte per GPU | 400--800 Gbps InfiniBand/Ethernet | NVIDIA/Mellanox specs |
| Beschikbaarheid (availability) | 99.95--99.99% (Tier III/IV equivalent) | Uptime Institute |

### 4.2 Financiele kengetallen / Financial Metrics

| Kengetal (Metric) | Benchmark | Bron (Source) |
|---|---|---|
| CAPEX per MW excl. GPU | EUR 10--15M/MW | Turner & Townsend DCCI 2025-2026 |
| CAPEX per MW incl. GPU | Tot EUR 40M/MW | Turner & Townsend DCCI 2025-2026 |
| AI datacenter premium (facility only) | +7--10% vs traditioneel datacenter | Turner & Townsend DCCI 2025-2026 |
| Omzet per MW per jaar (revenue per MW/yr) | ~$12.5M (blended indicatief) | Alpha-Matica |
| GPU-vervangingscyclus (GPU refresh cycle) | 18--36 maanden per generatie | Industrie schatting |
| GPU CAPEX als % totaal CAPEX | 50--70% | Industrie schatting |
| O&M kosten (% van omzet) | 15--25% (excl. stroom) | Industrie benchmark |
| Stroomkosten als % opex | 40--60% | Industrie benchmark |
| Hefboompercentage (gearing) | 50--65% (gecontracteerd) | Sector gemiddelde |
| DSCR (minimum covenant) | 1.30x+ (hoger dan traditioneel DC) | Financierspraktijk |
| Looptijd schuld (debt tenor) | 5--7 jaar (vs 10--15 jaar traditioneel DC) | Financierspraktijk |

---

## 5. Nederlandse AI-infrastructuur / Netherlands AI Infrastructure Market

### 5.1 Huidig landschap / Current Landscape

- **SURF:** Nationale ICT-coöperatie voor onderwijs en onderzoek; Snellius-supercomputer (Lenovo/NVIDIA A100); nationale AI-computecapaciteit voor academisch gebruik.
- **Commerciele cloud providers:** Microsoft Azure (Amsterdam/Middenmeer regio's); AWS (Europe-West); Google Cloud (Eemshaven); Oracle Cloud.
- **Amsterdam/Schiphol-corridor:** Europese hub voor datacenters; AMS-IX (Amsterdam Internet Exchange) als aantrekkingsfactor; Science Park als AI-onderzoekscluster.
- **Opkomende locaties:** Groningen (nabij Eemshaven windparken); Zeeland (net capaciteit); Flevoland (grondprijs en ruimte).

### 5.2 Regelgevingscontext / Regulatory Context

| Regelgeving (Regulation) | Beschrijving (Description) | Impact op AI Factories | Bron (Source) |
|---|---|---|---|
| Nationaal moratorium | Hyperscaledatacenters >70 MW EN >100.000 m2 verboden, behalve Het Hogeland en Hollands Kroon | AI-trainingsfaciliteiten moeten onder drempel blijven OF naar aangewezen gebieden | CMS LawNow |
| Amsterdam verbod | ALLE nieuwe datacenters/uitbreidingen verboden tot ten minste 2030 | Geen nieuwe AI facilities in Amsterdam | NL Times Apr 2025 |
| NH datacenterstrategie | DCs >2.000 m2 / >5 MVA beperkt tot aangewezen industriegebieden | Beperkt locatieopties in Noord-Holland | NH Datacenterstrategie 2025--2027 |
| Omgevingswet | Zelfde vergunningenregime als colocatiedatacenters | Omgevingsvergunning; omgevingsplan; MER indien nodig | Stb. 2016, 156 |
| Stikstof (AERIUS) | Drempel >0.005 mol/ha bij Natura 2000 gebieden | Bouwfase-emissies en noodgeneratoren vereisen stikstofberekening | RIVM |

### 5.3 Nederlandse overheid AI-strategie / Dutch Government AI Strategy

- **Nationaal Groeifonds:** AI-gerelateerde toewijzingen voor onderzoek en innovatie.
- **EU AI Factories:** 19 faciliteiten verspreid over 16 EU-lidstaten; EUR 2.6B totale investering; combinatie van publiek en privaat kapitaal. Nederland nog geen toegewezen locatie per Q1 2025. [EIB]
- **EU AI Gigafactories:** EUR 20B doelstelling voor ~5 grootschalige faciliteiten in de EU; EIB-financiering; publiek-private partnerschappen. [EIB]
- **Coalitieakkoord 2024-2028:** Digitale infrastructuur als strategische prioriteit; balans tussen groei en ruimtelijke ordening.
- **SDE++ en EIA/KIA:** Geen directe subsidie voor GPU-compute; wel voor hernieuwbare energieopwekking die AI-faciliteiten voedt; Energie-investeringsaftrek (EIA) mogelijk voor energie-efficiënte koelsystemen.

### 5.4 Netaansluiting / Grid Connection

| Parameter | Specificatie | Toelichting (Notes) |
|---|---|---|
| Typisch vermogen groot trainingscluster | 50--200+ MW | Vergelijkbaar met middelgroot hyperscale datacenter |
| TenneT wachtlijsten (connection queues) | Gemiddeld tot 10 jaar in congestiegebieden | ~60 GW in wachtrij vs ~20 GW piekvraag [TenneT] |
| Transportschaarste (grid congestion) | Ernstig in Noord-Holland, Zuid-Holland, Noord-Brabant | Beperkt nieuwe aansluitingen; TDTR als alternatief |
| Cable pooling (Energiewet 2026) | Tot 4 partijen per aansluiting; min. 100 kVA | Combinatie met hernieuwbaar/BESS; kostenreductie [QGM Law] |
| Eigen opwekking (on-site generation) | Zonnepanelen, gasturbines (backup), BESS | Vermindert netafhankelijkheid; stikstofrisico bij gasturbines |
| TDTR (Tijdelijk Dataverkenning Transportrecht) | 6 GW capaciteit toegekend (85%+ uurbeschikbaarheid) | Beschikbaar voor flexibele afnemers [PV Magazine Oct 2025] |

### 5.5 EU AI Act (Verordening 2024/1689) / EU AI Act (Regulation 2024/1689)

Relevantie voor infrastructuurfinanciers:

- **Risicogebaseerde classificatie:** AI-systemen ingedeeld in verboden, hoog-risico, beperkt risico, en minimaal risico. Infrastructuurproviders zijn indirect betrokken als faciliteerders.
- **Verplichtingen voor aanbieders van AI-modellen voor algemeen gebruik (GPAI):** Transparantievereisten; technische documentatie; naleving auteursrecht. Relevant voor klanten die trainen op AI-factorycapaciteit.
- **Compliance-impact op contracten:** Offtake-overeenkomsten moeten AI Act compliance-clausules bevatten; aansprakelijkheidsverdeling; data governance-vereisten.
- **Energierapportage:** GPAI-modelaanbieders moeten energieverbruik tijdens training rapporteren; impact op transparantie in de waardeketen.

---

## 6. Mondiale investeringsschaal / Global Investment Scale

### 6.1 Hyperscaler en AI CAPEX

| Metriek (Metric) | 2025 | 2026 | 2030 | CAGR | Bron (Source) |
|---|---|---|---|---|---|
| Hyperscaler CAPEX (totaal) | ~$443B | ~$602B | -- | -- | CreditSights/IEEE ComSoc |
| Waarvan AI-gerelateerd (of which AI) | ~75% (~$332B) | ~75% (~$452B) | -- | -- | CreditSights/IEEE ComSoc |
| Mondiale AI CAPEX | $423B | $571B | $1.3T | ~25% | UBS |
| Totale DC-investering (cumulatief tot 2030) | -- | -- | $5.2T | -- | McKinsey |
| Wereldwijde DC-stroomvraag | -- | -- | 219 GW | -- | McKinsey |

### 6.2 EU-specifieke programma's

| Programma (Program) | Bedrag (Amount) | Beschrijving (Description) | Bron (Source) |
|---|---|---|---|
| EU AI Factories | EUR 2.6B | 19 faciliteiten in 16 lidstaten; publiek-privaat | EIB |
| EU AI Gigafactories | EUR 20B (doel) | ~5 grootschalige faciliteiten; EIB-gefinancierd | EIB |
| TechEU | EUR 70B (2025--2027) | Breed technologie-investeringsprogramma | EIB |
| EIB totaal plafond 2025 | EUR 100B | Waarvan >EUR 11B voor energienetwerken + opslag | EIB |
| InvestEU AI-component | Onderdeel InvestEU | EU-garantie voor AI-investeringen | Europese Commissie |

### 6.3 Toonaangevende transacties / Landmark Deals

| Transactie (Deal) | Omvang (Size) | Type | Locatie (Location) | Bron (Source) |
|---|---|---|---|---|
| Nscale Series B | $1.1B | Venture capital | VK (UK) / Europa | Nscale; grootste Europese Series B |
| Microsoft Portugal | $10B | Corporate investering; meerjarig | Portugal | Silicon Republic |
| Google Duitsland | EUR 5.5B | Corporate investering; tot 2029 | Duitsland (Germany) | Silicon Republic |
| Meta + Blue Owl | $27B | Private credit; DC joint venture | VS (US) | Norton Rose Fulbright |
| FluidStack + Macquarie | 1 GW | Infrastructuurfonds; AI compute | Frankrijk (France) | DCD |
| CoreWeave financiering | $7.5B + $12B | Schuldfinanciering + equity raises | VS (US) | Diverse bronnen |
| Blackstone DC portfolio | $70B+ pipeline | Infrastructuurfonds; DC/AI | Mondiaal (Global) | Blackstone |
| xAI Memphis Supercluster | 150 MW (fase 1) | Corporate; GPU mega-cluster | VS (US) | Diverse bronnen |

---

## 7. Kapitaalstructuur / Capital Structure

### 7.1 Vreemd vermogen / Debt

| Parameter | AI Factory | Traditioneel DC (ter vergelijking) | Toelichting (Notes) |
|---|---|---|---|
| Hefboompercentage (gearing) | 50--65% | 65--75% | Lager vanwege technologierisico |
| Looptijd (tenor) | 5--7 jaar | 10--15 jaar | Korter; afgestemd op GPU-levenscyclus |
| Prijsstelling (pricing) | EURIBOR + 250--400 bps | EURIBOR + 150--250 bps | Premie voor technologierisico |
| DSCR covenant (minimum) | 1.30x+ | 1.20x--1.25x | Hoger vanwege technologische onzekerheid |
| DSCR lock-up | 1.15x--1.20x | 1.10x--1.15x | Distributie-blokkade drempel |
| DSCR default | 1.05x--1.10x | 1.05x | Ingrijprecht crediteur (step-in) |
| Schuldendienstreserve (DSRA) | 6 maanden | 6 maanden | Standaard; soms 9 maanden voor AI |
| GPU-vervangingsreserve | Verplicht (8--15% GPU CAPEX/jr) | N.v.t. | Specifiek voor AI; uniek vereiste |
| Voorwaarden (key conditions) | Gecontracteerde omzet voor hogere hefboom | Bezettingsgraad; huurcontracten | Financier-voorkeur: take-or-pay |

### 7.2 Eigen vermogen / Equity

- **Hogere eigen-vermogenseis:** 35--50% (vs 25--35% voor traditioneel datacenter).
- **Typische sponsors:** Technologiebedrijven (NVIDIA, Microsoft, Google eigen faciliteiten); sovereign wealth funds (GIC, ADIA, MGX/UAE); specialistische AI-infrastructuurfondsen (Nscale, CoreWeave); private equity (Blackstone, KKR, Brookfield); pensioenfondsen (beperkt; opkomend).
- **Rendementsverwachting (return expectations):** 15--20%+ unlevered IRR (vs 10--14% voor traditioneel datacenter); hoger vanwege technologierisico en beperkt track record.
- **Exit-strategieen:** Verkoop aan hyperscaler; beursgang (IPO); verkoop aan infrastructuurfonds; data center REIT-opname.

### 7.3 Hybride / Mezzanine

| Structuur (Structure) | Beschrijving (Description) | Voordeel (Advantage) |
|---|---|---|
| GPU-leasing | Gescheiden financiering HW vs faciliteit; GPU als roerend goed | Scheidt technologierisico van vastgoedrisico |
| Tech refresh faciliteit | Aparte kredietlijn voor GPU-vervanging | Voorkomt herfinanciering van hoofdschuld |
| Leveranciersfinanciering (vendor financing) | NVIDIA en AMD financieringsprogramma's | Directe OEM-relatie; soms gunstiger voorwaarden |
| Mezzanine schuld | Achtergesteld (subordinated); hogere rente | Overbrugt equity-gap; flexibeler covenants |

### 7.4 Opkomende structuren / Emerging Structures

- **GPU-als-onderpand (GPU-as-collateral):** GPUs als roerend goed bezwaard via pandrecht (Art. 3:236 BW); waarderingsproblematiek vanwege snelle veroudering; registerpandrecht via Kadaster nodig.
- **Omzetgebaseerde financiering (revenue-based financing):** Aflossing gekoppeld aan benuttingsgraad; opwaarts- en neerwaarts-sharing; geschikt voor merchant component.
- **Private credit structuren:** Meta + Blue Owl $27B datacenter joint venture als landmark [Norton Rose Fulbright]. Groeiende belangstelling van private credit fondsen.
- **GPU compute financiering:** FluidStack + Macquarie 1 GW Franse AI-computefaciliteit als voorbeeld van infrastructuurfonds + compute-operator combinatie [DCD].
- **Securitisatie (securitization):** Toekomstige optie; verpakking van GPU-verhuurcontracten als ABS; markt nog niet ontwikkeld.

---

## 8. Due Diligence Focus Areas

Checklist specifiek voor AI factory/GPU compute projectfinanciering:

### 8.1 Technisch

- [ ] GPU OEM-overeenkomsten: garantie, ondersteuning, vervangingsvoorwaarden (NVIDIA DGX/HGX Enterprise contracten)
- [ ] Koelsysteemontwerp en -validatie: DLC vs immersie; OEM-certificering; redundantie
- [ ] Stroomdistributie en redundantie: N+1 of 2N; UPS-autonomie; noodstroomcapaciteit
- [ ] GPU-vervangingsschema en reservefinanciering: cyclus, kosten, logistiek
- [ ] Netwerkfabric en connectiviteit: InfiniBand/Ethernet topologie; internetconnectiviteit; latentie
- [ ] Onafhankelijk technisch advies (IE technology assessment): volledig IE-rapport verplicht

### 8.2 Commercieel

- [ ] Klantofftake-contracten: looptijd, take-or-pay, kredietwaardigheid tegenpartij
- [ ] Omzetmodel-analyse: mix gecontracteerd vs merchant; prijsgevoeligheidsanalyse
- [ ] Concurrentielandschap: pricing trends; overcapaciteitsrisico; hyperscaler eigen capaciteit
- [ ] Klantconcentratie: maximale blootstelling per tegenpartij; diversificatiestrategie

### 8.3 Juridisch en regelgevend

- [ ] EU AI Act (Verordening 2024/1689): compliance-vereisten voor infrastructuurproviders
- [ ] Gegevensbescherming (AVG/GDPR): dataverwerking door klanten op AI-infrastructuur
- [ ] Omgevingsvergunning en bestemmingsplan: conformiteit omgevingsplan; MER indien nodig
- [ ] Stikstof (AERIUS): bouwfase en operationeel (noodgeneratoren)
- [ ] Moratorium en lokale beperkingen: nationaal hyperscaleverbod; lokale datacenter strategieen

### 8.4 Financieel en verzekeringen

- [ ] Verzekeringsportefeuille: brand (fire); technologie (technology performance warranty -- beperkt beschikbaar); bedrijfsschade (BI); CAR/EAR (bouwfase)
- [ ] Financieel model: GPU-vervangingsreserve; DSCR-gevoeligheid voor benuttingsgraad en pricing
- [ ] Softwarestack afhankelijkheden en licenties: CUDA, orchestratiesoftware, monitoring
- [ ] Belastingstructuur: earningsstripping 24.5%; EIA voor koelsystemen; deelnemingsvrijstelling

---

## 9. Contractueel kader / Key Contractual Framework

### 9.1 Overzicht kerncontracten / Core Contract Overview

| Contract | Tegenpartij (Counterparty) | Typische looptijd (Typical Term) | Bankability | Kernrisico (Key Risk) |
|---|---|---|---|---|
| GPU OEM Supply Agreement | NVIDIA / AMD / Intel | 1--5 jaar; verlenging | Hoog (gevestigde OEMs) | Leveringstermijnen; allocatie bij schaarste |
| Klant offtake / compute contract | AI-bedrijven; enterprises; hyperscalers | 1--7 jaar | Varieert (afhankelijk van tegenpartij) | Kredietwaardigheid; volume commitment |
| EPC faciliteit (shell) | Bouwbedrijf | 18--30 maanden (bouwfase) | Standaard PF-structuur | Bouwtijd; kostenoverschrijding |
| GPU fit-out en commissioning | Systeemintegrator / OEM | 2--6 maanden | Medium | Technische complexiteit; tijdigheid |
| O&M faciliteit | Facilitair dienstverlener | 3--10 jaar | Hoog | KPI's; beschikbaarheid |
| O&M IT / GPU-stack | Specialist IT-dienstverlener | 1--5 jaar | Medium | Specialistische kennis; personeelsbeschikbaarheid |
| Koelingsonderhoud (cooling maintenance) | Koelsysteemfabrikant / specialist | 3--10 jaar | Hoog | OEM-afhankelijkheid; onderdelenvoorziening |
| PPA / Stroomlevering | Energieleverancier / ontwikkelaar | 5--15 jaar | Hoog | Prijsrisico; leveringszekerheid |
| Huur / Opstalrecht | Grondeigenaar | 15--30 jaar | Standaard | Huurzekerheid; waarde-impact |

### 9.2 Specifieke aandachtspunten voor AI-contracten

- **GPU OEM-contracten:** Allocatierechten bij schaarste; next-generation upgraderechten; service level agreements (SLAs) voor reparatie en vervanging; onderpandvestiging op GPUs (pandrecht).
- **Klantcontracten:** Take-or-pay clausules; minimum commitment levels; prijsherziening bij nieuwe GPU-generaties; data-eigendom en -vertrouwelijkheid; AI Act compliance-allocatie.
- **EPC-splitsing:** Faciliteitsschil (shell) apart van GPU fit-out; UAV-GC 2025 of FIDIC voor faciliteit; separaat GPU-installatiecontract met OEM of systeemintegrator.
- **O&M-splitsing:** Faciliteit O&M (koeling, stroom, beveiliging) apart van IT O&M (GPU-management, softwarestack, monitoring); verschillende specialismen en dienstverleningsniveaus.

---

## 10. Risicomatrix / Risk Matrix for AI Factory Project Finance

| Risico (Risk) | Categorie (Category) | Ernst (Severity) | Waarschijnlijkheid (Likelihood) | Mitigatie (Mitigation) |
|---|---|---|---|---|
| GPU-veroudering (obsolescence) | Technologie | Hoog | Hoog | Vervangingsreserve; korte schuldlooptijd; upgradecontracten |
| Koelsysteem uitval (failure) | Technologie | Hoog | Laag--Medium | N+1 redundantie; OEM-onderhoud; noodprotocollen |
| Prijsdruk GPUaaS-markt | Markt | Medium--Hoog | Hoog | Langetermijncontracten; diversificatie workloads |
| Klantconcentratie | Krediet | Medium--Hoog | Medium | Diversificatie; vooruitbetaling; moederbedrijfgaranties |
| Netcongestie / transportschaarste | Infrastructuur | Hoog | Hoog (NL) | Cable pooling; TDTR; eigen opwekking; BESS |
| Moratorium / regelgevingswijziging | Regelgeving | Medium | Medium | Locatiediversificatie; lobby; compliance-monitoring |
| Bouwvertraging | Constructie | Medium | Medium | EPC fixed-price; liquidated damages; buffers in planning |
| Stikstofproblematiek | Vergunning | Medium | Medium (bouwfase) | Elektrisch materieel; emissieberekening vooraf; saldering |
| EU AI Act compliance | Regelgeving | Laag--Medium | Medium | Contractuele allocatie; monitoring; juridisch advies |
| Brand (fire) | Fysiek | Hoog | Laag | Branddetectie; suppressie; verzekering; immersie-specifieke maatregelen |
| Cyberaanval | Operationeel | Hoog | Medium | Cybersecurity; verzekering; incident response plan |

---

## 11. Vergelijking met andere activaklassen / Comparison with Other Asset Classes

| Parameter | AI Factory | Colocatie DC | BESS | Windpark (ter referentie) |
|---|---|---|---|---|
| PF track record | Opkomend (<3 jaar) | Gevestigd (10+ jaar) | Groeiend (5+ jaar) | Volwassen (20+ jaar) |
| Technologierisico | Hoog (GPU-veroudering) | Laag--Medium | Medium (batterijdegradatie) | Laag |
| Inkomstenzekerheid | Variabel (contract-afhankelijk) | Hoog (langetermijnhuur) | Variabel (merchant/gecontracteerd) | Hoog (SDE++/PPA) |
| Typische hefboom | 50--65% | 65--75% | 40--80% | 70--85% |
| Typische schuldduur | 5--7 jaar | 10--15 jaar | 5--10 jaar | 15--18 jaar |
| DSCR covenant | 1.30x+ | 1.20x--1.25x | 1.20x--1.35x | 1.15x--1.25x |
| Equity IRR verwachting | 15--20%+ | 8--12% | 10--15% | 7--10% |
| CAPEX per MW | EUR 10--40M | EUR 8--12M | EUR 0.3--0.7M | EUR 1.2--2.5M |
| Bouwperiode | 18--30 maanden | 18--36 maanden | 6--12 maanden | 24--48 maanden |
| NL moratorium impact | Ja (>70 MW) | Ja (>70 MW; Amsterdam) | Nee | Nee |

---

## 12. Disclaimer / Disclaimer

AI-infrastructuur is een opkomende activaklasse met een beperkt projectfinancieringstrack record. Marktgegevens, GPU-prijzen, en omzetschattingen zijn indicatief en onderhevig aan snelle verandering. Technologierisico is materieel hoger dan bij traditionele datacenters of BESS-projecten.

- Alle tarieven, drempels, en regelgevingsverwijzingen zijn gebaseerd op 2025/2026 wetgeving en marktdata. Verifieer actuele gegevens bij primaire bronnen.
- GPU-prijzen (GPUaaS-tarieven) zijn volatiel en onderhevig aan snelle verandering door nieuwe generaties, capaciteitsuitbreiding, en concurrentiedruk.
- Dit bestand vormt geen juridisch advies (juridisch advies), belastingadvies (belastingadvies), of beleggingsadvies (beleggingsadvies). Raadpleeg gekwalificeerde Nederlandse juridische, fiscale, en financiele adviseurs voor specifieke transacties.

---

## 13. Kruisverwijzingen / Cross-References

| Onderwerp (Subject) | Referentiebestand (Reference File) |
|---|---|
| Colocatiedatacenters (Colocation DCs) | [references/colocation-data-centers.md](references/colocation-data-centers.md) |
| Schuldinstrumenten (Debt instruments) | [references/debt-instruments.md](references/debt-instruments.md) |
| Nederlands juridisch kader (Netherlands legal framework) | [references/netherlands-legal-framework.md](references/netherlands-legal-framework.md) |
| Risicoverdeling (Risk allocation) | [references/risk-allocation.md](references/risk-allocation.md) |
| BESS-projecten (Battery energy storage) | [references/bess-projects.md](references/bess-projects.md) |
| Eigen vermogen structuren (Equity structures) | [references/equity-structures.md](references/equity-structures.md) |
| Financiele modellering (Financial modeling) | [references/financial-modeling.md](references/financial-modeling.md) |
| Due diligence checklist | [references/due-diligence-checklist.md](references/due-diligence-checklist.md) |
| Bronnen en referenties (Sources and references) | [references/sources-and-references.md](references/sources-and-references.md) |

---

*Laatst bijgewerkt / Last updated: 2025-Q4. Verifieer alle gegevens tegen primaire bronnen voor transactiebeslissingen.*
