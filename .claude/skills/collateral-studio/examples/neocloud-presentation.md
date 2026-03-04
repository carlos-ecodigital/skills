# Neocloud Presentation — Full 15-Slide Pitch Deck Outline

**Audience:** GPU cloud provider (neocloud) — CTO, VP Infrastructure, Head of Capacity
**Language:** English
**Duration:** 20-25 minutes + Q&A
**Classification:** External
**Filename:** `DE-DECK-Neocloud-Pitch-v[X]-[DATE].pptx`

---

## Slide 1: European GPU infrastructure has a power problem

**Title:** The bottleneck isn't silicon — it's megawatts

**Content:**
- 60 GW of grid connection applications queued in the Netherlands against 20 GW peak demand
- Amsterdam data center moratorium active until 2030+
- Average wait for new grid connection in congested areas: up to 10 years
- Visual: NL grid congestion map showing red zones

**Key data:** 60 GW queue; Amsterdam moratorium; up to 10-year wait
**Source footnote:** TenneT; NL Times Apr 2025

**Speaker notes:** Neoclouds understand power constraints. They live it. Open with the problem they already have and can't solve: "Where do I get European megawatts in 12-18 months, not 5-10 years?"

---

## Slide 2: The supply-demand gap

**Title:** European AI compute demand is outpacing available infrastructure

**Content:**
- NL colocation market: USD 11.25B, growing 9.67% CAGR through 2030
- DC vacancy in NL: 5% (down from 7% in 2024) — near full absorption
- Amsterdam controls 78% of NL DC capacity — concentration risk
- NL operators declined from 111 to 95 (2019-2023) — consolidating
- EU AI Act + GDPR = structural demand for European-hosted compute

**Key data:** USD 11.25B market; 9.67% CAGR; 5% vacancy; 78% Amsterdam concentration
**Source footnote:** Mordor Intelligence 2025; Cushman & Wakefield 2025; CBRE

**Speaker notes:** This isn't speculative demand. It's quantified and growing. The AI Act creates legal requirements for European enterprises to know where their models are trained. That drives demand to European infrastructure.

---

## Slide 3: Secured grid. Available now.

**Title:** DE has grid connections secured — deployment in 12-18 months, not 5-10 years

**Content:**
- DE's grid connections were secured before the congestion queue
- No new grid wait required — cable pooling (Energiewet 2026) enables co-location
- Map: site locations relative to AMS-IX, Frankfurt, London with latency markers
- Timeline: FID → 12-18 months → operational

**Key data:** Secured MW capacity; 12-18 month deployment; sub-2ms to major hubs
**Source footnote:** DE development pipeline; Energiewet 2026

**Speaker notes:** This is the slide where you differentiate. Everyone can build a data center — if they can find power. DE has power, now. That's the moat.

---

## Slide 4: Facility specifications

**Title:** Liquid-cooled, high-density AI infrastructure — built for GPU workloads

**Content:**
Technical specification table:

| Parameter | Specification |
|---|---|
| Rack density | 40-140 kW/rack (current); up to 240 kW next-gen |
| Cooling | Direct liquid cooling |
| PUE | 1.2 target |
| Power redundancy | [N+1 / 2N — per site design] |
| Network | Nokia infrastructure; AMS-IX proximity |
| Latency | Sub-2ms to Frankfurt and London |
| Security | Physical: manned + CCTV; Logical: per tenant isolation |
| Certifications | [ISO 27001 path — confirm status] |

**Source footnote:** DE engineering specification; Tom's Hardware 2025 (density ranges)

**Speaker notes:** This is the slide they'll screenshot and send to their engineering team. Make sure every number is accurate and specific. No vague "enterprise-grade" claims.

---

## Slide 5: Network and interconnect

**Title:** Sub-2ms to Frankfurt and London via Nokia infrastructure

**Content:**
- Nokia network partnership: high-bandwidth, low-latency interconnect
- AMS-IX proximity: peering access to Europe's largest internet exchange
- Latency comparison table:

| Destination | From DE NL site | From Nordic alternative |
|---|---|---|
| Frankfurt | <2ms | 10-15ms |
| London | <2ms | 15-20ms |
| Amsterdam (AMS-IX) | <1ms | 8-12ms |

- Relevance for inference workloads: every millisecond matters at scale

**Key data:** Sub-2ms to Frankfurt/London; Nokia partnership
**Source footnote:** Network design specification; Nokia partnership

**Speaker notes:** For inference workloads (which most neoclouds are building for), latency is non-negotiable. Nordic sites offer cheap power but 10-20ms more latency. For production AI inference, that's a deal-breaker.

---

## Slide 6: Why NL beats the alternatives

**Title:** Comparison: DE Netherlands vs. Nordic vs. Frankfurt vs. self-build

**Content:**
Comparison matrix:

| Factor | DE (Netherlands) | Nordic (Sweden/Finland) | Frankfurt (incumbents) | Self-Build (NL) |
|---|---|---|---|---|
| Grid availability | Secured | Available | Constrained | 5-10 year wait |
| Timeline to operational | 12-18 months | 12-24 months | Waiting list | 3-5+ years |
| Latency to W. Europe | Sub-2ms | 10-20ms | Sub-1ms | Sub-2ms |
| Cooling | Liquid (purpose-built) | Air (free cooling) | Mixed (retrofitted) | Varies |
| Power cost | Moderate | Low | High | Moderate |
| AI rack density | 40-140+ kW/rack | Limited by cooling | Legacy constraints | Clean-sheet |
| Waste heat subsidy | Yes (heat revenue) | Limited market | No | Depends on site |

**Speaker notes:** Every alternative has a trade-off. Nordic = cheap power but high latency. Frankfurt = low latency but no capacity. Self-build = control but years of waiting. DE = secured power, low latency, purpose-built, available now.

---

## Slide 7: Colocation models

**Title:** Three engagement models — matched to your business

**Content:**
| Model | What DE Provides | What You Provide | Pricing Basis |
|---|---|---|---|
| **Wholesale colocation** | Power, cooling, physical security, connectivity | Your hardware, your operations | $/kW/month |
| **Powered shell** | Shell building, power, cooling infrastructure | Interior buildout, hardware, operations | $/sqm/month + power |
| **GPUaaS** | Full stack: facility + hardware + management | Workloads | $/GPU-hour |

- Contract flexibility: 1-5 year terms with options
- Scaling provisions: reserved capacity for future expansion

**Key data:** Indicative pricing ranges per model (from `de-brand-bible/references/deal-economics.md`)
**Source footnote:** Market benchmarks; CBRE / DataX Connect Q1 2025

**Speaker notes:** Match the model to the neocloud's business. If they sell GPU-hours, they want wholesale colocation (they own hardware). If they want to test a market, GPUaaS reduces their commitment.

---

## Slide 8: Waste heat — your operating cost advantage

**Title:** Waste heat revenue offsets facility costs — lowering your effective rack rate

**Content:**
- Every MW of IT load generates ~1 MW of thermal energy
- DE recovers 97% and sells it to adjacent greenhouses / district heating
- Revenue from heat sales subsidizes facility operating costs
- Result: lower effective colocation rate vs. competitors who dump heat
- Neocloud responsibility: zero — heat recovery is fully DE's operation

**Key data:** 97% heat recovery; heat revenue subsidizes opex
**Source footnote:** DE engineering specification

**Speaker notes:** Neoclouds don't care about growers. They care about their cost per GPU-hour. Frame waste heat purely as: "This makes your rack rate lower because we have a second revenue stream."

---

## Slide 9: Sovereign AI infrastructure

**Title:** European enterprises need European compute — you can provide it from DE infrastructure

**Content:**
- EU AI Act: requires transparency about where AI models are processed
- GDPR: data processing location matters for European enterprise buyers
- Growing enterprise demand for "sovereign cloud" — compute on European soil, European jurisdiction
- DE infrastructure: Dutch BV, Dutch soil, European hardware (Lenovo), European network (Nokia)
- Your opportunity: sell "sovereign GPU cloud" to European enterprises who can't use US hyperscalers

**Key data:** EU AI Act; GDPR data localization requirements
**Source footnote:** EU AI Act framework; GDPR Art. 44-49

**Speaker notes:** Position this as a commercial opportunity for the neocloud, not a compliance burden. They can charge a premium for sovereign European compute. DE's infrastructure enables that premium positioning.

---

## Slide 10: Lenovo + Nokia partnership

**Title:** Enterprise-grade hardware — standardized, European supply chain

**Content:**
- Lenovo: pre-configured GPU clusters for AI workloads; not bespoke integration
- Nokia: high-bandwidth network infrastructure; telecom-grade reliability
- European supply chain: not dependent on US/APAC logistics for ongoing operations
- Standardized deployment: same stack across multiple DE sites = operational consistency

**Key data:** Lenovo hardware; Nokia network; European supply chain; 12+ planned sites
**Source footnote:** Stelia proposal V5

**Speaker notes:** For neoclouds expanding across Europe, standardization matters. Same hardware, same network stack, same operational procedures at every DE site. Scale without re-engineering.

---

## Slide 11: BESS integration

**Title:** On-site battery storage provides power quality and grid services

**Content:**
- BESS deployed alongside DEC on shared grid connection (cable pooling)
- Grid services: FCR, aFRR, congestion management
- Power quality: BESS smooths grid fluctuations for sensitive GPU workloads
- Revenue: BESS generates independent revenue stream, improving overall site economics
- Neocloud impact: reliable power; no BESS capex or operational burden from your side

**Key data:** BESS integrated via cable pooling; FCR + aFRR revenue
**Source footnote:** Energiewet cable pooling; DE/Ampower analysis

**Speaker notes:** BESS is a background benefit for neoclouds. They get better power quality. DE gets an additional revenue stream. Win-win, no action required from the neocloud.

---

## Slide 12: Scale roadmap

**Title:** From 1.2 MW pilot to 12+ European sites — early movers get capacity priority

**Content:**
Pipeline table:

| Project | Capacity (MW IT) | Timeline | Status |
|---|---|---|---|
| Fonti (pilot) | 1.2 | 4 months from FID | [Current status] |
| Powergrow (scale) | 4.1 | 12 months from FID | [Current status] |
| European expansion | 12+ sites | [Timeline] | Development pipeline |

- Capacity allocation: early commitments secure priority allocation
- Growth path: start at one site, expand across DE's European portfolio

**Key data:** 1.2 MW → 4.1 MW → 12+ sites; EUR 360-600M+ hardware deployment
**Source footnote:** Stelia proposal V5

**Speaker notes:** Create controlled urgency. Grid connections are finite. Capacity at each site is limited. Early movers get first allocation. This isn't artificial scarcity — it's physics (grid capacity is real and measurable).

---

## Slide 13: Commercial structure

**Title:** Dutch BV, non-recourse project finance, clear risk allocation

**Content:**
- Each site: separate Dutch BV (ProjectBV)
- Non-recourse project finance: site-level risk, not cross-collateralized
- Contract structure: colocation agreement with ProjectBV
- Flexibility: 1-5 year initial terms with expansion options
- Organizational chart: DE Group → ProjectBV → colocation agreement

**Speaker notes:** For sophisticated neoclouds, the legal structure matters. Non-recourse means one site's issues don't affect others. Dutch BV means European jurisdiction. Clear, bankable structure.

---

## Slide 14: Current discussions

**Title:** Multiple GPU cloud providers are in technical evaluation

**Content:**
- [X] neoclouds in active technical discussions
- Capacity allocation conversations underway for first sites
- Anonymized interest indicators (if available — e.g., "3 neoclouds evaluating for H2 2026 capacity")
- Reference: Lenovo and Nokia are engaged across the pipeline

**Speaker notes:** Social proof, even anonymized, helps. If you can name a category ("two EU-based GPU cloud providers"), that's more credible than "multiple companies." Keep it vague enough to be true, specific enough to be credible.

---

## Slide 15: Next step — technical deep-dive

**Title:** Let's schedule a 45-minute technical review

**Content:**
Concrete next step:

**What:** 45-minute technical session with DE's engineering team
**Who:** Your infrastructure lead + DE's CTO / lead engineer
**Agenda:**
1. Your capacity requirements (MW, rack density, timeline)
2. DE facility walkthrough (technical specs, cooling architecture, network)
3. Commercial model discussion (which engagement model fits)
4. Site selection (if multiple sites available)

**When:** [Date option 1] or [Date option 2]
**Contact:** [Name], [Email], [Phone]
**One-pager download:** [Link to DE-1PGR-Neocloud-Overview]

**Speaker notes:** Don't ask "are you interested?" — ask "does Tuesday or Thursday work for the technical call?" Assume interest, lower friction, be specific.

---

## Appendix Slides (optional)

### A1: Detailed facility floor plan
### A2: Network architecture diagram
### A3: Colocation pricing framework (detailed)
### A4: Regulatory overview (EU AI Act, GDPR, NIS2)
### A5: BESS technical specifications
