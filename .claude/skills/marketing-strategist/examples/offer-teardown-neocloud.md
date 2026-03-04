# Offer Teardown: Neocloud GPU Capacity — Value Equation Analysis

Applying the Hormozi Value Equation to DE's offer for GPU cloud providers seeking European capacity.

---

## The Offer

**One sentence:** "Liquid-cooled AI colocation in the Netherlands with secured grid, AMS-IX proximity, and heat-subsidized operating costs — available 12-18 months from commitment."

---

## Value Equation Breakdown

### Dream Outcome: 8/10

**What the neocloud CTO actually wants:**
1. Available megawatts in Europe (power is the bottleneck, not space)
2. Liquid cooling capability at 40-140 kW/rack (GPU workloads demand it)
3. Low latency to European enterprise customers (<5ms to major hubs)
4. Speed — every month without European capacity is lost enterprise revenue
5. Cost efficiency — GPU cloud margins depend on infrastructure cost

**How DE delivers:**
- Secured grid connections (not in a 10-year queue)
- New-build facility with liquid cooling native (DLC, not retrofitted air cooling)
- Netherlands: AMS-IX adjacency, sub-2ms to Frankfurt/London
- Fonti pilot: 4 months from FID. Scale sites: 12-18 months.
- Heat revenue offsets operating costs → lower all-in price to tenant

**Why 8, not 10:** Scale is currently limited. First sites are sub-25 MW. Neoclouds thinking 50+ MW need the expansion pipeline story.

### Perceived Likelihood: 6/10

**Why a neocloud would believe us:**
- Lenovo partnership (hardware credibility)
- Secured grid connections (not speculative)
- Active development pipeline (5 projects)
- Professional project finance structuring (institutional investor alignment)

**Why skepticism remains:**
- No operational facility yet (pilot in progress)
- New entrant in DC market (limited track record)
- Small initial scale vs. incumbent operators

**How to increase to 8/10:**
1. Get Fonti operational — nothing beats a working facility
2. Secure first neocloud LOI — social proof from one converts many
3. NVIDIA / Lenovo endorsement — "DE is a validated infrastructure partner"
4. Independent technical report on facility design and PUE

### Time Delay: 4/10 (lower is better — 4 is slow)

**Current state:**
- Fonti pilot: 4 months from FID (fast)
- Scale sites: 12-18 months from commitment (reasonable for DC, but slow vs. "I need GPUs now")
- Competition: Nordic builds take 2-3 years. Self-build: 3-5 years. But existing facilities (Equinix, NorthC) can deploy in weeks.

**How to reduce time delay:**
1. Pre-built powered shell option: customer brings hardware, we provide power/cooling/connectivity in existing or nearly-complete facility
2. Phase deployment: first rack operational in 4-6 months, full buildout in 12-18
3. Bridge capacity: partner with existing NL colocation for immediate needs while DEC builds

### Effort & Sacrifice: 7/10 (lower is better — 7 means low effort)

**What the neocloud has to do:**
- Ship/install their own hardware (standard for colocation — they expect this)
- Commit to minimum term and power reservation
- Wait for facility completion (the main "sacrifice")

**What DE eliminates:**
- Grid connection procurement (done)
- Permitting (DE handles Omgevingswet)
- Facility engineering and construction (DE's scope)
- Cooling system design (liquid cooling built-in)

**How to improve to 9/10:**
1. Offer turnkey option: DE procures and installs GPU hardware (GPUaaS model)
2. Handle logistics: coordinate hardware shipping, customs, installation
3. Provide pre-configured networking with AMS-IX connectivity included

---

## Current Value Score

**VALUE = (8 × 6) / (4 × 3) = 48 / 12 = 4.0**

Good but not compelling. The bottleneck is **perceived likelihood (6)** and **time delay (4)**.

---

## Grand Slam Offer Design

To make this offer irresistible, address the weak levers:

### Core Offer
"Liquid-cooled AI colocation on secured Dutch grid with AMS-IX proximity."

### Bonus 1 — Speed (reduces time delay)
"Phase 1 capacity available in 4-6 months. Reserve your power allocation now — we begin build-out immediately upon LOI."

### Bonus 2 — Proof (increases perceived likelihood)
"Site visit + live technical review with our engineering team. See the grid connection, review the cooling design, meet the Lenovo hardware team."

### Bonus 3 — Ease (reduces effort)
"Turnkey deployment option: we handle hardware procurement, logistics, and installation. You provide the workload, we provide everything else."

### Risk Reversal
"30-day exit clause in Year 1 if PUE exceeds 1.25 or uptime falls below 99.9%." (Sets a high bar that DE should meet — builds confidence without real risk.)

### Scarcity (real, not manufactured)
"We have [X] MW allocated across [Y] sites. Current pipeline interest exceeds available capacity. LOI priority is first-come-first-served."

### Revised Value Score (with Grand Slam additions)

| Lever | Before | After | Change |
|---|---|---|---|
| Dream Outcome | 8 | 8 | Same |
| Perceived Likelihood | 6 | 8 | Site visit + Lenovo credibility |
| Time Delay | 4 | 7 | Phase 1 in 4-6 months |
| Effort/Sacrifice | 7 → 3 effort | 9 → 1 effort | Turnkey option |

**NEW VALUE = (8 × 8) / (3 × 1) = 64 / 3 = 21.3** — 5x improvement

---

## Campaign Implications

### Target List
- 20-30 neocloud companies with European expansion interest
- Source: GTC/OCP attendee lists, Crunchbase (raised >$10M, AI/cloud infrastructure), LinkedIn (VP Infra at GPU cloud companies)

### Channels
1. **Direct BD** via Lenovo/NVIDIA introductions (warm outreach)
2. **LinkedIn ABM** targeting VP Infra / CTO at identified companies
3. **Conference presence** at GTC Europe, OCP, SC (speaking slot if possible)
4. **Cold email** to neocloud infrastructure leads (5-email sequence)

### Content Needed
1. Neocloud-specific pitch deck (collateral-studio)
2. Technical one-pager: facility specs, PUE, power density, connectivity (collateral-studio)
3. Cost comparison model: DE vs. Equinix vs. Nordic vs. hyperscaler (marketing-strategist + collateral-studio)
4. Cold email sequence: 5 emails, infrastructure-focused (content-engine)
5. LinkedIn content series: 5 posts on European AI infrastructure gap (content-engine)

### Timeline
| Week | Action |
|---|---|
| 1-2 | Build target list; create content |
| 3 | Launch cold email sequence to first batch (10 contacts) |
| 4-5 | Follow up; request site visits for warm leads |
| 6-8 | Site visits; technical deep dives |
| 8-10 | Proposal delivery; LOI negotiation |
| 10-12 | Target: 1-2 LOIs signed |

### Budget
| Item | Amount |
|---|---|
| Conference attendance (1 event) | EUR 3,000-5,000 |
| Email tooling | EUR 200/mo |
| LinkedIn Sales Navigator | EUR 100/mo |
| Travel for site visits | EUR 1,000 |
| **Total (Q2)** | **EUR 5,000-7,000** |

### Success Metrics
| KPI | Target |
|---|---|
| Qualified conversations | 8-10 |
| Site visits completed | 3-5 |
| Proposals delivered | 2-3 |
| LOIs signed | 1-2 |
| CPL | <EUR 700 |
