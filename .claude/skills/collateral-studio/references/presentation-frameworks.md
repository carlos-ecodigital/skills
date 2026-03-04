# Presentation Frameworks — Slide-by-Slide Guidance

Audience-specific deck structures for Digital Energy. Each framework defines slide order, content requirements, and key messaging per slide. Adapt to the specific opportunity — these are frameworks, not rigid templates.

---

## Universal Deck Principles

1. **Problem before solution.** Always open with the buyer's pain, never with DE's story.
2. **Numbers before claims.** Lead with a quantified fact, then explain what it means.
3. **One takeaway per slide.** If a slide needs more than 10 seconds to understand, split it.
4. **Comparison tables win.** Side-by-side comparisons accelerate decision-making.
5. **End with a concrete next step.** "Let's schedule a site visit on [date]" not "Contact us."
6. **No more than 20 words in a slide title.** Titles should be assertions, not labels ("DE reduces grower heating costs by 60-80%" not "Cost savings overview").

---

## Framework 1: Grower Deck (Teler Presentatie) — 12 Slides

**Language:** Dutch (technical/legal terms in English parenthetical)
**Tone:** Direct, practical, farmer-to-farmer. Numbers over theory. No tech jargon.
**Duration:** 15-20 minutes + Q&A

| Slide | Title Pattern | Content | Key Data |
|---|---|---|---|
| 1 | **Uw gasrekening stijgt structureel** | Open with gas cost trajectory. Show TTF price history and ETS2 impact timeline. Create urgency. | EUR 35-45/MWh gas; EUR 10-20/MWh ETS2 from 2027 |
| 2 | **De toekomst van verwarming in de glastuinbouw** | Three options: stay on gas (costs rise), geothermal (10-year wait, geological risk), waste heat (available now). Position waste heat as the practical choice. | Comparison table: gas vs. geothermal vs. DEC waste heat |
| 3 | **Wat is een Digital Energy Center?** | Visual: aerial view of greenhouse + DEC building (render). Explain in simple terms: AI computers generate heat, we capture it, deliver it to your greenhouse. | ~2,000 sqm building, 45-60°C heat, 97% recovery |
| 4 | **Uw besparing: 60-80% op verwarmingskosten** | Central slide. Show the economics table: current gas cost vs. DEC heat cost. Three scenarios (conservative/base/optimistic). | EUR 15/MWh vs. EUR 35-45/MWh; annual saving in EUR |
| 5 | **Hoe het werkt: stap voor stap** | Timeline visual: LOI (10 dagen) → HoT (6 weken) → Bouw (12-18 maanden) → Warmtelevering. Emphasize speed and simplicity. | 10-day LOI; zero investment from grower |
| 6 | **Geen investering van uw kant** | DE finances everything. Grower provides land access (recht van opstal). Grower receives heat + revenue share. No CAPEX, no operational responsibility. | Zero CAPEX; CPI-indexed heat price; 30-year partnership |
| 7 | **Uw netaansluiting is goud waard** | Explain cable pooling (Energiewet 2026). Their existing grid connection enables the DEC + BESS without new grid wait. Their underutilized asset becomes a revenue source. | 60 GW queue; up to 10-year wait; cable pooling for up to 4 parties |
| 8 | **Wat u ziet op uw terrein** | Site layout diagram. DEC building with dimensions. Noise levels. Visual impact. Access requirements. Address the "data center on my land" concern directly. | 2,000 sqm; <45 dB at property line; enclosed facility |
| 9 | **Zekerheid en bescherming** | Legal protections: Dutch law, Dutch BV, recht van opstal, 5-year non-renewal windows, heat supply transfer provisions. Address the "what if you go bankrupt" concern. | Dutch BV (ProjectBV); Dutch law; 5-year review periods |
| 10 | **Wat andere telers doen** | Social proof. Reference pipeline activity. Quote from an early grower (anonymized if needed). Network effect: early movers get priority. | [X] growers in discussion; LOIs signed |
| 11 | **De volgende stap** | Concrete ask: "Wilt u een vrijblijvend locatiebezoek inplannen?" or "Aanmelden via het portaal duurt 30 seconden." Give two date options. | Portal URL; contact name and phone |
| 12 | **Over Digital Energy** | Brief boilerplate. Zug HQ, Dutch operations, Lenovo/Nokia partnerships, pipeline. Keep short — they've already seen the substance. | See `de-brand-bible/examples/boilerplate-paragraphs.md` |

### Grower Deck — Do's and Don'ts
- **Do:** Start with their gas bill, use Dutch, show the savings table early, offer a site visit
- **Don't:** Lead with AI/technology, use English acronyms without translation, show complex financial models, mention GPU pricing or compute economics

---

## Framework 2: Neocloud Deck (GPU Cloud Provider) — 15 Slides

**Language:** English
**Tone:** Technical, data-dense, infrastructure-focused. Speak their language: rack density, PUE, latency, interconnect.
**Duration:** 20-25 minutes + Q&A

| Slide | Title Pattern | Content | Key Data |
|---|---|---|---|
| 1 | **European GPU infrastructure has a power problem** | Grid scarcity in NL. Amsterdam moratorium. 5-10 year wait for new connections. The bottleneck isn't silicon — it's megawatts. | 60 GW queue; Amsterdam moratorium to 2030; 5% vacancy |
| 2 | **The supply-demand gap** | Demand for European GPU capacity (EU AI Act, GDPR, enterprise sovereignty requirements) vs. available supply. Show the gap visually. | NL DC market USD 11.25B; 9.67% CAGR; 5% vacancy |
| 3 | **Secured grid. Available now.** | DE has grid connections already secured. No 10-year wait. Deployment timeline: 12-18 months from FID. Map showing site locations relative to AMS-IX. | Secured MW; 12-18 month timeline; AMS-IX proximity |
| 4 | **Facility specifications** | Technical spec table: rack density, cooling type, PUE, power per rack, network, redundancy. This is the slide they'll screenshot. | 40-140 kW/rack; liquid cooling; PUE 1.2; redundancy levels |
| 5 | **Network and interconnect** | Nokia network infrastructure. AMS-IX peering proximity. Latency benchmarks vs. Nordic and Frankfurt alternatives. | Sub-2ms to Frankfurt/London; Nokia partnership |
| 6 | **Why NL beats the alternatives** | Comparison table: DE NL site vs. Nordic options vs. Frankfurt incumbents vs. self-build. Cover latency, timeline, cooling, grid certainty. | Comparison matrix: 5 parameters × 4 options |
| 7 | **Colocation models** | Three options: wholesale colocation, powered shell, GPUaaS. Pricing framework for each. Flexibility to match their business model. | Pricing ranges per model; contract flexibility |
| 8 | **Waste heat: your operating cost advantage** | DE's waste heat revenue subsidizes facility costs. Lower effective rental rate. Explain how this works without requiring anything from the neocloud. | 97% heat recovery; revenue offset; lower TCO |
| 9 | **Sovereign AI infrastructure** | European data sovereignty context. EU AI Act. GDPR. Why European enterprises need European compute. Position the neocloud as meeting this demand via DE infrastructure. | EU AI Act; GDPR; European enterprise demand |
| 10 | **Lenovo + Nokia partnership** | Hardware standardization. Pre-configured clusters. European supply chain. Not bespoke integration. Faster deployment, predictable quality. | Lenovo hardware; Nokia network; European supply chain |
| 11 | **BESS integration** | Battery storage on-site provides grid services and power quality. Revenue stacking benefits the site economics. Neocloud benefits from reliable power. | BESS capacity; FCR/aFRR revenue; power quality |
| 12 | **Scale roadmap** | Pilot site (1.2 MW), scale site (4.1 MW), European expansion (12+ sites). Show the growth trajectory. Early movers get capacity allocation priority. | Fonti 1.2 MW → Powergrow 4.1 MW → 12+ sites |
| 13 | **Commercial structure** | ProjectBV structure. Non-recourse finance. Contract terms overview. Occupancy timeline. What the neocloud commits to and what DE provides. | Dutch BV; non-recourse; contract term structure |
| 14 | **Current pipeline** | Who else is in discussion (anonymized or with permission). Creates urgency: capacity is finite, grid is scarce. | Number of neoclouds in discussion; capacity allocation status |
| 15 | **Next step: technical deep-dive** | Concrete ask: "Let's schedule a 45-minute technical review with our engineering team." Provide specific date options. Include contact and one-pager link. | Technical contact; date options; one-pager download |

### Neocloud Deck — Do's and Don'ts
- **Do:** Lead with infrastructure specs, use comparison tables, reference latency/PUE/density, show pricing models
- **Don't:** Over-explain waste heat to growers (they don't care), use marketing language, hide behind vague "premium infrastructure" claims

---

## Framework 3: District Heating Deck (Warmtenet Presentatie) — 14 Slides

**Language:** Dutch (with English for international operators)
**Tone:** Professional, regulatory-aware, evidence-based. Speak to engineering directors and board members.
**Duration:** 20-25 minutes + Q&A

| Slide | Title Pattern | Content | Key Data |
|---|---|---|---|
| 1 | **De Wcw verandert de warmtemarkt** | Open with regulatory context. Cost-based tariffs, public ownership requirements, designated heat company model. What this means for heat source economics. | Wcw effective 2026-2027; cost-based tariffs; >50% public ownership |
| 2 | **Uw bronnenportfolio onder druk** | Heat source diversification imperative. Over-reliance on gas or single sources creates regulatory and financial risk. | Gas cost trajectory; ETS2 impact; source reliability comparison |
| 3 | **Datacenter-warmte: 24/7 baseload** | AI data centers run 8,760 hours/year. Unlike intermittent sources, DEC heat is continuous, predictable, and non-seasonal. | 8,760 hr/yr; 45-60°C direct; 80-90°C with heat pump |
| 4 | **Warmteprijs: CPI, niet gas** | Central slide. Price comparison: DEC heat vs. gas vs. geothermal vs. biomass. Show CPI indexation vs. TTF volatility. Wcw-compliant cost-based structure. | EUR 10-15/MWh CPI-indexed vs. EUR 35-45/MWh gas |
| 5 | **Technische specificaties** | Heat output per MW IT, temperature grades, recovery efficiency, connection points, seasonal modulation capability. | 97% recovery; 45-60°C; scalable output |
| 6 | **Integratie met uw netwerk** | How DEC heat connects to existing district heating infrastructure. 4th/5th generation compatibility. Heat pump boosting if needed. Schematic diagram. | Connection schematic; temperature grades; flow rates |
| 7 | **Betrouwbaarheid en redundantie** | Uptime track record for DC infrastructure. Diversified tenant base means no single-point failure. Backup provisions in contract. | >99% availability target; backup heat source provisions |
| 8 | **Geen investeringskosten** | DE finances and builds the DEC. Utility pays only for consumed heat at contracted price. No CAPEX, no construction risk, no technology risk. | Zero CAPEX; consumption-based payment; CPI-indexed |
| 9 | **Vergelijking met alternatieven** | Comparison table: DEC heat vs. gas boiler vs. geothermal vs. biomass vs. industrial waste heat. Score on: price, reliability, availability timeline, carbon, risk. | 5-alternative comparison matrix |
| 10 | **Wcw-conformiteit** | How DE's model aligns with Wcw requirements. Cost-based pricing (not gas-linked). Transparent cost structure. Compatible with municipal ownership models. | Wcw compliance checklist |
| 11 | **Projectstructuur** | Dutch BV (ProjectBV). Non-recourse finance. Contract hierarchy. Roles and responsibilities. What the utility sees and what DE handles. | Organizational diagram |
| 12 | **Referenties en pipeline** | DE's project pipeline. Relevant comparable projects (if available). Partnership credentials (Lenovo, Nokia). | Active projects; pipeline MW; partnership names |
| 13 | **Haalbaarheidsvoorstel** | Concrete offer: DE prepares a technical feasibility assessment for the utility's specific network. No cost, no obligation. 4-week timeline. | Free feasibility assessment; 4-week delivery |
| 14 | **Over Digital Energy** | Boilerplate. Keep brief. | See `de-brand-bible/examples/boilerplate-paragraphs.md` |

---

## Framework 4: Enterprise Deck (AI Sovereignty) — 15 Slides

**Language:** English
**Tone:** Consultative, compliance-aware, executive-level. Speak to CTOs, CISOs, and procurement.
**Duration:** 20-25 minutes

| Slide | Title Pattern | Content | Key Data |
|---|---|---|---|
| 1 | **Where is your AI being trained?** | Most European enterprises can't answer this. Data leaves Europe. Jurisdiction unclear. Compliance risk grows. | EU AI Act; GDPR; data sovereignty requirements |
| 2 | **The sovereignty imperative** | EU AI Act transparency requirements. GDPR data processing location obligations. Board-level liability for non-compliance. | Regulatory framework overview |
| 3 | **The European compute gap** | US hyperscalers control majority of GPU cloud. European alternatives are scarce, small, or Nordic (latency). | US vs. European GPU capacity comparison |
| 4 | **Sovereign AI infrastructure in NL** | DE builds and operates European-owned AI infrastructure on Dutch soil. European hardware (Lenovo), European network (Nokia), Dutch jurisdiction. | NL location; European supply chain; Dutch BV |
| 5 | **Facility specifications** | Technical spec table adapted for enterprise concerns: security, redundancy, cooling, power, compliance certifications. | ISO 27001 path; PUE 1.2; redundancy levels |
| 6 | **Deployment models** | Private cloud, dedicated cluster, shared colocation. Map to enterprise procurement models. Show how existing cloud workloads can migrate. | Three deployment models with specifications |
| 7 | **Compliance framework** | How DE's infrastructure supports: GDPR (data localization), EU AI Act (transparency), NIS2 (critical infrastructure), industry-specific regulation. | Compliance mapping table |
| 8 | **Network and connectivity** | AMS-IX proximity. Nokia infrastructure. Latency to major European business centers. Hybrid cloud connectivity options. | Sub-2ms to Frankfurt/London; AMS-IX |
| 9 | **Total cost of ownership** | TCO comparison: DE sovereign infrastructure vs. US hyperscaler with sovereignty premium vs. Nordic alternatives. | TCO comparison table |
| 10 | **Waste heat: sustainability credentials** | 97% heat recovery. ESG reporting benefit. Carbon reduction quantified. Aligns with corporate sustainability commitments. | Heat recovery %; ESG impact metrics |
| 11 | **Partnership ecosystem** | Lenovo, Nokia, and the broader European sovereign AI initiative. Enterprise-grade hardware and support. | Partnership logos and credentials |
| 12 | **Case for early adoption** | Grid scarcity means capacity is finite. Early commitments secure allocation. Capacity reservation model. | Grid scarcity context; allocation model |
| 13 | **Implementation timeline** | From contract to operational: what happens, when, and what the enterprise needs to do (answer: minimal). | Milestone timeline; enterprise responsibilities |
| 14 | **Reference and credentials** | DE track record, pipeline, and any referenceable enterprise relationships. | Project pipeline; relevant credentials |
| 15 | **Proposal: dedicated capacity assessment** | Concrete next step: DE's technical team assesses the enterprise's compute requirements and proposes a tailored solution. 2-week turnaround. | Free assessment; 2-week timeline |

---

## Framework 5: Investor / Energy Partner Deck — 16 Slides

**Language:** English
**Tone:** Infrastructure investor language. Risk-return framing. Non-recourse project finance terminology. No marketing hyperbole.
**Duration:** 25-30 minutes

| Slide | Title Pattern | Content | Key Data |
|---|---|---|---|
| 1 | **European AI infrastructure meets project finance** | Thesis: AI compute demand is structural. Grid is the bottleneck. DE converts grid scarcity into infrastructure assets with contracted cash flows. | Market opportunity framing |
| 2 | **The grid scarcity moat** | 60 GW queue. 10-year wait. Existing grid = unfair advantage. Barrier to entry for competitors. | 60 GW; 12,000+ companies waiting; up to 10-year wait |
| 3 | **The DE model: integrated infrastructure** | Three revenue streams: AI colocation, waste heat, BESS. Each de-risks the others. Cable pooling enables co-location on one grid connection. | Three-stream revenue model diagram |
| 4 | **Revenue stacking economics** | How the three streams combine. Show illustrative revenue waterfall for a reference project. Conservative / base / optimistic. | Revenue waterfall; three scenarios |
| 5 | **Heat supply: contracted, CPI-indexed** | 30-year heat supply contracts. CPI-indexed (not commodity-linked). Baseload demand from greenhouses/district heating. | EUR 10-15/MWh; 30-year terms; CPI indexation |
| 6 | **AI colocation: structural demand** | NL DC market data. Vacancy rates. Demand drivers (EU AI Act, sovereign cloud, neocloud expansion). Pricing benchmarks. | USD 11.25B market; 5% vacancy; pricing range |
| 7 | **BESS: early cash flow bridge** | BESS deploys first (6-12 months). Generates immediate returns (arbitrage + FCR). De-risks the development period. Equity converts to DC equity. | BESS IRR 12-15%; 6-12 month COD; revenue stack |
| 8 | **Project structure** | Each project is a Dutch BV. Non-recourse project finance. SPV isolation. Recht van opstal. Clear risk allocation. | SPV diagram; stakeholder map |
| 9 | **Risk framework** | Risk register: construction, technology, offtake, regulatory, counterparty. Mitigation for each. Insurance coverage. | Risk matrix with mitigants |
| 10 | **Regulatory tailwinds** | Energiewet cable pooling, Omgevingswet permitting, Wcw heat regulation, SDE++ eligibility, EU ETS2. All push toward DE's model. | Regulatory timeline; impact per regulation |
| 11 | **Partnership de-risking** | Lenovo (hardware), Nokia (network), Ampower (BESS JV), grower network. Each partnership reduces execution risk. | Partnership map with risk reduction |
| 12 | **Pipeline overview** | Current projects: Fonti (1.2 MW), Powergrow (4.1 MW), Lodewijk (25.5 MW + expansion), Ampower BESS JV. Status and timeline for each. | Pipeline table: project / MW / status / timeline |
| 13 | **Financial summary** | Indicative project economics. CAPEX ranges. Revenue composition. DSCR targets. Equity IRR ranges (with appropriate disclaimers). | Financial summary table; three scenarios |
| 14 | **Capital structure** | How projects are financed. Debt (infrastructure lenders), equity (DE + co-investors), and potential for institutional capital at scale. | Capital stack diagram; target gearing |
| 15 | **Management team** | Key team members with relevant credentials. Infrastructure, energy, and technology experience. | Team bios (3-4 key people) |
| 16 | **Investment proposition** | Concrete ask: what DE is looking for (capital, partnership, or specific collaboration). Next step: detailed project memorandum or site visit. | Specific ask; timeline; contact |

---

## Appendix: Slide Design Principles

### Title Rules
- Titles are **assertions**, not labels
- Good: "DEC waste heat reduces grower heating costs by 60-80%"
- Bad: "Cost savings overview"
- Good: "60 GW of grid applications are waiting — we're already connected"
- Bad: "Grid scarcity in the Netherlands"

### Data Visualization
- **Comparison tables:** Use for any claim that involves alternatives (gas vs. heat, Nordic vs. NL, self-build vs. DE)
- **Timeline diagrams:** Use for project milestones and regulatory timelines
- **Waterfall charts:** Use for revenue stacking and cost buildup
- **Maps:** Use for site locations, grid congestion zones, and AMS-IX proximity

### Source Footnotes
- In investor and technical decks: include source footnotes on data slides
- In marketing and grower decks: numbers alone are sufficient (source available on request)
- Format: "Source: [Source Name], [Year]" in 8pt at slide bottom
