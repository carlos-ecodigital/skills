# Compute FAQ — Canonical Answers Reference

> **Purpose:** Ready-to-use answers for customer-facing conversations about DE's AI colocation offering. Every answer is resolved from contractual sources (SLA v5.1, Pricing v5.1) cross-referenced with engineering specs.
> **Audience:** Yoni Fishman (sales), Carlos Reuven (CEO), Jelmer Ten Wolde (CPO) — anyone fielding compute customer questions.
> **Source hierarchy:** SLA/Pricing v5.1 (contractual) > DC engineering refs (design) > Presentation deck (marketing). When in doubt, quote the contract, not the deck.
> **Confidentiality:** Items marked [CONFIDENTIAL] are for internal use only. Items marked [SHAREABLE] can be discussed with customers.
> **Last updated:** 2026-03-07

---

## How To Use This Reference

1. **Find the topic** by section number (matches SKILL.md topic matrix)
2. **Use "Quote This"** — the exact claim you can make to customers
3. **Check "Don't Quote"** — numbers that exist in our docs but shouldn't be shared or are misleading out of context
4. **Check "Confidentiality"** — [SHAREABLE] or [CONFIDENTIAL]
5. **When in doubt** — say "I'll get back to you with the exact specification" and route to the right skill

---

## 1. Availability and Uptime

### Q1.1: What's your power SLA? [SHAREABLE]

**Quote This:**
"99.99% power availability in Steady State (Phase 2). That's measured per calendar month at the distribution board level."

**Key Facts:**
- 99.99% = ~4.4 minutes unplanned downtime per month
- Measurement: per distribution/board level (not per rack)
- Metering: MID-certified meters
- Applies ONLY in Phase 2 (Steady State)

**Don't Quote:**
- "Five nines" (99.999%) — we commit to four nines
- "Per-rack metering" — metering is at distribution/board level (v5.1 change)
- "99.95%" — that was the old design availability target, not the SLA

**Source:** SLA terms v5.1 (Phase 2 Steady State)

---

### Q1.2: What about cooling availability? [SHAREABLE]

**Quote This:**
"99.99% cooling availability in Steady State. We run N+1 cooling plant with dual-path direct liquid cooling distribution."

**Key Facts:**
- Cooling SLA is SEPARATE from power SLA (separate credit schedules in v5.1)
- N+1 plant redundancy
- Dual-path DLC distribution (was single-path in v5.0)
- Liquid cooling has inherent thermal mass buffer (more forgiving than air)

**Source:** SLA terms v5.1

---

### Q1.3: What about Early Access / Phase 1? [SHAREABLE — but handle carefully]

**Quote This:**
"Phase 1 is our Early Access period — approximately one month from Ready-for-Service. During Early Access, the facility operates on a best-effort basis. Full SLA commitments kick in at Phase 2."

**Key Facts:**
- Phase 1 (Early Access): ~1 month from RFS
- Best effort — NO SLA commitments
- NO credits during Phase 1
- Month 1 may be free (at provider discretion), then discounted kW fee
- Purpose: burn-in, commissioning, initial workload deployment

**NEVER SAY:**
- "Full SLA from day one" — Phase 1 has NO SLA
- "Credits apply during Early Access" — they don't
- "Early Access is just a formality" — it's a real operational period with reduced guarantees

**Why this matters:** A neocloud CTO who commits to a customer contract expecting four nines from day one, and then discovers a best-effort Phase 1, will lose trust permanently. Be upfront about the two-phase model.

**Source:** SLA terms v5.1 (Phase 1 Early Access)

---

### Q1.4: What's excluded from the SLA? [SHAREABLE]

**Quote This:**
"Standard exclusions apply: scheduled maintenance windows, force majeure, and customer-caused outages. We also exclude any downstream issues beyond the CDU demarcation point."

**Key Facts:**
- Scheduled maintenance: Tue/Wed 02:00-06:00 CET, max 2/month, max 4hrs each
- CDU demarcation: Provider controls to CDU level; downstream is customer responsibility
- Credits are NOT automatic — customer must request with proof within 60 days
- Grid-wide utility failure exclusion was REMOVED in v5.1 (important: we now own grid risk)

**Source:** SLA terms v5.1

---

## 2. Power

### Q2.1: What's the maximum power density per rack? [SHAREABLE]

**Quote This:**
"Our facility supports 60-130 kW per rack depending on the GPU platform. For GB200 NVL72, that's 120-130 kW per liquid-cooled rack."

**Key Facts (by platform):**
| Platform | Power per Rack | Cooling | Racks per MW |
|----------|---------------|---------|-------------|
| H100 SXM (8-GPU node) | ~40-60 kW | DLC + air | ~17-25 |
| B200 SXM (8-GPU node) | ~80-90 kW | DLC + air | ~11-13 |
| GB200 NVL72 | 120-130 kW | Full liquid | ~8 |
| GB300 NVL72 (2026+) | ~140-150 kW | Full liquid | ~7 |

**Don't Quote:**
- "225 kW/rack" — this is the RANGE MAXIMUM from the pricing framework for future capacity, not current
- "40-140 kW" from the presentation deck — too wide a range, sounds uncertain
- Specific kW without asking which GPU platform they're deploying

**Source:** `skills/ai-infrastructure/references/gpu-accelerator-hardware.md`, `skills/dc-engineering/references/data-hall-design.md`

---

### Q2.2: What's the power chain architecture? [SHAREABLE]

**Quote This:**
"Grid connection → MV switchgear → transformers → UPS (N+1) → power distribution to rack-level demarcation. We also have BESS on-site for power quality and backup, plus N+1 gas backup generators."

**Key Facts:**
- Block Redundant architecture (independent blocks per tenant cluster, shared MV distribution)
- N+1 throughout — NOT 2N (deliberate design choice for AI workloads)
- BESS integrated via cable pooling (Energiewet 2026)
- UPS: N+1 configuration
- Backup generators: N+1 gas
- Power usage design: 80% nominal, peaks within 100%

**Why N+1 not 2N:**
Training workloads checkpoint and can resume after brief outages. The cost of 2N infrastructure (doubling everything) isn't justified when the workload tolerates restarts. This is a deliberate, defensible design choice — not a shortcut.

**NEVER SAY:**
- "2N redundancy" — unless the specific site design actually has it
- "No backup generators" — we have N+1 gas generators
- "UPS provides X minutes of runtime" — don't quote specific runtime without site-specific data

**Source:** `skills/dc-engineering/references/ai-factory-design.md`, Pricing framework v5.1 (Provider Scope)

---

### Q2.3: What's the minimum commitment? [CONFIDENTIAL pricing; SHAREABLE structure]

**Quote This (structure only):**
"Minimum block is 1.2 MW — that's one Superpod block of 24 racks. We can scale in 1.2 MW increments up to 3 blocks (4.1-6.2 MW IT) per building."

**Key Facts [CONFIDENTIAL]:**
- Minimum block: 1.2 MW (one Superpod block)
- 24 racks per block
- 3 blocks per building (4.1-6.2 MW IT)
- Base rate: EUR 150/kW/month [CONFIDENTIAL — share only in formal commercial discussions]
- Payment: monthly in advance, net 30
- Security deposit: 3 months (in MSA)

**Don't Quote:**
- Specific EUR/kW/month rate in casual conversations — this is for formal proposals
- "We can do less than 1.2 MW" — unless specifically designing a pilot/POC arrangement
- Old pricing: EUR 170/kW/month was v5.0, now EUR 150 in v5.1

**Source:** Pricing framework v5.1

---

## 3. Cooling

### Q3.1: What cooling technology do you use? [SHAREABLE]

**Quote This:**
"Direct liquid cooling is standard. We use CDUs (Coolant Distribution Units) delivering facility water at 30-35°C supply, returning at 42-45°C. The liquid handles approximately 80% of the heat load. The remaining 15-20% residual air cooling is handled by in-row cooling units."

**Key Facts:**
- CDU supply temperature: 30-35°C (warm water — NOT chilled water)
- CDU return temperature: 42-45°C (this feeds the heat recovery system)
- Liquid handles: ~80% of total heat
- Residual air cooling: 15-20% via in-row units (Schneider InRow, Vertiv Liebert CRV)
- No raised floor — slab-on-grade with overhead services (CDU piping, busway, cable tray)
- CDU demarcation: Provider controls to CDU level; everything downstream (manifolds, hoses to servers) is customer

**Source:** `skills/dc-engineering/references/ai-factory-design.md`, `skills/dc-engineering/references/data-hall-design.md`

---

### Q3.2: What's your PUE? [SHAREABLE — but handle the number carefully]

**Quote This:**
"Our billing PUE is fixed at 1.3 — that's what you pay on your energy bill. Our design target is lower. You benefit from a predictable energy cost regardless of actual facility efficiency."

**Key Facts — THE PUE RECONCILIATION:**
| Context | PUE Value | What It Means | Use When |
|---------|-----------|---------------|----------|
| **Billing PUE** | **1.3 fixed** | What customer pays: kWh x 1.3 x rate | Always — this is the contractual number |
| Design target | ~1.15-1.20 | What we engineer for | Internal only, or when asked specifically about design |
| PowerGrow calculated | 1.166 | Site-specific model output | Only for PowerGrow-specific discussions |
| Presentation claim | 1.2 | Marketing/deck number | Only in general capability discussions |

**Critical rule:** Energy optimization benefits (delta between 1.3 billing and actual PUE) are retained by Provider (per Pricing Framework v5.1). This means: if we achieve PUE 1.15 but bill at 1.3, the 0.15 delta is DE's margin. This is standard industry practice.

**NEVER SAY:**
- "PUE 1.15" as the customer's billing PUE — the billing PUE is 1.3
- "You'll see lower PUE on your bill" — the billing PUE is FIXED at 1.3
- "PUE 1.2" and then have the contract say 1.3 — this kills trust instantly
- Mix up design PUE with billing PUE — different audiences, different numbers

**Why 1.3 billing is GOOD for the customer:**
Predictability. The customer knows exactly what they'll pay. No seasonal PUE variation, no metering disputes, no "your PUE was 1.4 this winter" surprises. Fixed cost, simple math.

**Source:** Pricing framework v5.1 (energy formula), `skills/dc-engineering/references/ai-factory-design.md`

---

### Q3.3: What about heat recovery? [SHAREABLE]

**Quote This:**
"We recover approximately 97% of the waste heat and deliver it to adjacent greenhouses. This creates a second revenue stream for DE, which helps keep your colocation rate competitive. You have zero operational responsibility for heat recovery — it's fully our operation."

**Key Facts:**
- Heat recovery: ~97% of total waste heat
- CDU return water (42-45°C) → heat pump → 70-80°C → greenhouse delivery
- Heat pump COP target: 3.5-5.0 (depending on temperature lift)
- DC cooling takes absolute priority over heat delivery (SLA terms v5.1)
- No impact on customer operations — heat recovery is invisible to the compute tenant

**NEVER SAY:**
- "Heat recovery might affect your cooling" — DC cooling ALWAYS takes priority
- "You'll benefit from heat recovery revenue" — the revenue goes to DE, not the compute tenant
- "SDE++ subsidy" to compute customers — that's grower/DE internal economics

**Source:** SLA terms v5.1 (greenhouse thermal priority), `skills/dc-engineering/references/heat-recovery-integration.md`

---

## 4. Network

### Q4.1: Are you carrier neutral? [SHAREABLE]

**Quote This:**
"Yes, we're carrier neutral. We provide the physical fiber infrastructure, structured cabling, and meet-me room. You bring your own network equipment and choose your carriers. Cross-connects are a one-time fee."

**Key Facts:**
- DE provides: physical fiber, structured cabling, MMR, carrier cross-connects
- Customer provides: all active networking equipment (switches, NICs, firewalls)
- DE does NOT inspect or manage tenant traffic
- Cross-connects: one-time fee only (no monthly — changed in v5.1)
- Nokia partnership for interconnect infrastructure

**Source:** Pricing framework v5.1, `skills/ai-infrastructure/references/cluster-networking.md`

---

### Q4.2: What's the latency to major hubs? [SHAREABLE]

**Quote This:**
"Sub-2ms to Frankfurt and London, sub-1ms to AMS-IX. This matters particularly for inference workloads where every millisecond impacts user experience."

**Key Facts (from presentation deck — verify per site):**
| Destination | From DE NL site | From Nordic alternative |
|-------------|----------------|----------------------|
| Frankfurt | <2ms | 10-15ms |
| London | <2ms | 15-20ms |
| Amsterdam (AMS-IX) | <1ms | 8-12ms |

**NEVER SAY:**
- Specific sub-millisecond latency numbers without site-specific measurement
- "Better than Frankfurt" — Frankfurt incumbents have <1ms to AMS-IX
- "Guaranteed latency" — latency is network-dependent, not SLA-covered

**Source:** Neocloud presentation (slide 5)

---

### Q4.3: What networking do you recommend for AI training? [SHAREABLE]

**Quote This:**
"For training clusters, InfiniBand NDR/XDR is the recommended compute fabric — the SHARP in-network reduction gives 2-3x improvement in AllReduce operations. For inference-focused deployments, RoCEv2 Ethernet at 400G/800G is a cost-effective alternative. We provide the physical cabling; you bring the switches."

**Key Facts:**
| Use Case | Recommended Fabric | Why |
|----------|-------------------|-----|
| LLM training (large scale) | InfiniBand NDR 400G / XDR 800G | SHARP, lossless by design, proven at scale |
| Inference (high batch) | RoCEv2 Ethernet 400G/800G | Lower cost, larger talent pool |
| Storage/management | Ethernet 100-400 GbE | Standard, multi-vendor |

**Multi-tenant isolation:**
- Compute fabric: physically separate IB switches per tenant (no shared InfiniBand)
- Frontend/storage: shared Ethernet with VRF + VLAN separation

**Cabling density warning:**
- 1,024 GPU H100 cluster = ~1,300+ cables
- 2-3x cable tray density vs. traditional enterprise DC
- Cable tray fill: max 50% (allows future expansion)

**Source:** `skills/ai-infrastructure/references/cluster-networking.md`

---

## 5. Physical Security

### Q5.1: What physical security measures are in place? [SHAREABLE]

**Quote This:**
"Biometric and badge access control, 24/7 CCTV monitoring, and per-tenant isolation. Specific security posture details are covered in the MSA."

**Key Facts:**
- Physical security section was removed from SLA in v5.1 (moved to MSA language)
- On-site security was removed from base package in v5.1
- Access control: biometric + badge (planned)
- CCTV: 24/7 monitoring
- Staffing model: TBD per site

**NEVER SAY:**
- "24/7 on-site manned security" — this was removed from the base package in v5.1
- "SOC-monitored" without confirming the monitoring arrangement
- Detailed security architecture to non-customers (OpSec)

**Source:** SLA terms v5.1 (v5.1 change #6, #11)

---

## 6. Compliance & Certifications

### Q6.1: Do you have SOC2? ISO 27001? [SHAREABLE — be honest]

**Quote This:**
"SOC2 and ISO 27001 are on our certification roadmap. We're building to those standards from the ground up, which is actually easier than retrofitting compliance onto legacy infrastructure. We're happy to share our roadmap and current posture documentation."

**Key Facts:**
- SOC2: NOT yet obtained — planned (state roadmap)
- ISO 27001: NOT yet obtained — planned (state roadmap)
- Data sovereignty: Netherlands, EU jurisdiction — documented
- NIS2: apply to critical infrastructure — assess applicability per site

**NEVER SAY:**
- "We have SOC2" or "ISO 27001 certified" — we don't yet
- "We're SOC2 compliant" — compliance ≠ certification
- "Certification isn't important" — for enterprise buyers, it's often a procurement gate

**Acceptable framing:**
- "Building to SOC2/ISO 27001 standards from inception"
- "Clean-sheet advantage: no legacy technical debt to remediate"
- "Happy to provide our current security posture documentation"

**Source:** compute-faq SKILL.md (topic 6), soul.md ("Not Yet Documented" Protocol)

---

## 7. Pricing

### Q7.1: What's your pricing structure? [CONFIDENTIAL — formal discussions only]

**Quote This (in formal commercial context only):**
"We price on a per-kW/month basis with a fixed billing PUE. The all-in facility rate covers power, cooling, physical security, and basic connectivity. Energy is metered and billed separately."

**Key Facts [CONFIDENTIAL]:**
| Parameter | Value |
|-----------|-------|
| Base rate | EUR 150/kW/month (all-in facility rate) |
| PUE (billing) | 1.3 fixed |
| Energy formula | Metered IT Load (kWh) x 1.3 x Energy Rate |
| Target energy rate | ~EUR 0.070/kWh (range 0.060-0.100) |
| Minimum block | 1.2 MW |
| Escalation | 3% fixed OR CPI + 0.5% (floor 2%, cap 4%) |
| Payment | Monthly in advance, net 30 |
| Late payment | 1.5% monthly or Dutch statutory rate |
| Security deposit | 3 months (in MSA) |
| Add-on pricing | Cost + 10% |
| Fit-out milestones | 50% / 35% / 15% |
| Cross-connects | One-time fee only (no monthly) |

**Provider Scope (what's INCLUDED in the kW rate):**
1. Grid connection, MV infrastructure, transport
2. Transformers and main switchgear
3. UPS systems (N+1) and BESS
4. Backup generators (N+1 gas)
5. Power distribution to rack-level demarcation
6. Facility cooling plant (N+1) and primary distribution
7. CDU operational control
8. Building shell and structural systems
9. Fire detection and suppression
10. BMS and facility monitoring (24/7)
11. Heat recovery infrastructure
12. Energy procurement and PUE management
13. Facility operations staff (24/7)

**What's NOT included / metered separately:**
- Energy consumption (metered x 1.3 x rate)
- Remote hands (pricing TBD with vendor)
- Custom fit-out (cost + 10%)
- Tenant networking equipment
- GPU hardware (unless GPUaaS model)

**NEVER SAY:**
- "EUR 170/kW/month" — that was v5.0, now EUR 150 in v5.1
- Specific discount amounts — discount schedules removed from v5.1 (internal only)
- "We can do less than EUR 150" — route to sales-intake for custom pricing
- "PPA available" — PPA is only for whole-site/triple-net customers
- "Energy rate is EUR 0.070" as a firm commitment — it's a target range (0.060-0.100)

**Source:** Pricing framework v5.1

---

### Q7.2: What engagement models do you offer? [SHAREABLE]

**Quote This:**
"Three models: wholesale colocation (you bring hardware, we provide facility), powered shell (you build out the interior), or GPUaaS (full stack, you bring workloads). Most neocloud conversations start with wholesale colocation."

**Key Facts:**
| Model | DE Provides | Customer Provides | Pricing |
|-------|------------|-------------------|---------|
| Wholesale colocation | Power, cooling, security, connectivity | Hardware, operations | EUR/kW/month |
| Powered shell | Shell, power, cooling infrastructure | Interior buildout, hardware, ops | EUR/sqm/month + power |
| GPUaaS | Full stack: facility + hardware + mgmt | Workloads | EUR/GPU-hour |

**Source:** Neocloud presentation (slide 7)

---

## 8. SLA Credits

### Q8.1: How do credits work? [SHAREABLE]

**Quote This:**
"If we fall below 99.99% availability in a given month, you're entitled to service credits. Power and cooling have separate credit schedules. Credits are not automatic — you need to submit a claim with supporting evidence within 60 days."

**Key Facts (v5.1 changes):**
- Separate credit schedules for power vs. cooling (new in v5.1)
- Credits NOT automatic — customer must request with proof within 60 days
- 15% monthly credit cap was REMOVED in v5.1 (credits can now be larger)
- Phase 1 (Early Access): NO credits at all

**NEVER SAY:**
- "Automatic credits" — they're not; customer must request
- "Unlimited credits" — there are still reasonable limits, just no 15% cap
- Credit percentages or formulas without the actual SLA document in front of you

**Source:** SLA terms v5.1

---

## 9. Maintenance

### Q9.1: When are maintenance windows? [SHAREABLE]

**Quote This:**
"Scheduled maintenance is Tuesday and Wednesday, 02:00-06:00 CET. Maximum two windows per month, maximum four hours each. We provide advance notification for all scheduled work."

**Key Facts:**
- Windows: Tue/Wed 02:00-06:00 CET
- Max frequency: 2 per month
- Max duration: 4 hours per window
- Excluded from SLA calculations
- Emergency maintenance: separate procedure with immediate notification

**Source:** SLA terms v5.1

---

## 10. Onboarding

### Q10.1: What's the onboarding process? [SHAREABLE — high level]

**Quote This:**
"From contract signing, you're looking at 12-18 months to operational facility. The first month after Ready-for-Service is Early Access (Phase 1) — a commissioning period where we run best-effort while you deploy initial workloads. After that, full SLA kicks in."

**Key Facts:**
| Milestone | Timeline |
|-----------|----------|
| Contract → FID | Varies (negotiation) |
| FID → construction complete | 8-12 months |
| RFS → Phase 1 (Early Access) | ~1 month |
| Phase 1 → Phase 2 (Steady State) | After Early Access period |

- Acceptance testing procedure: TBD (to be documented)
- Customer telemetry portal: best effort (removed from SLA guarantee in v5.1)

**NEVER SAY:**
- "Live in 6 months" — 12-18 months is realistic from FID
- "Full SLA from day one" — Phase 1 is best effort
- Specific dates without project-specific timeline confirmation

**Source:** SLA terms v5.1, Pricing framework v5.1 (Early Access terms)

---

## 11. Scalability

### Q11.1: How do I expand? [SHAREABLE]

**Quote This:**
"Each building supports up to 3 blocks of 1.2 MW (total 4.1-6.2 MW IT). Beyond that, we have 16 projects in our pipeline across the Netherlands, with the same standardized design at each site. Start at one site, scale across the portfolio."

**Key Facts:**
- Block size: 1.2 MW (one Superpod, 24 racks)
- Building capacity: 3 blocks (4.1-6.2 MW IT)
- Pipeline: 16 projects, 13 signed HoTs
- Standardized design: same Lenovo hardware, Nokia networking, same operational procedures
- Contract flexibility: 1-5 year initial terms with expansion options

**Source:** Neocloud presentation (slide 12), `projects/_pipeline.md`

---

## 12. Technical Facility Specifications (Deep Dive)

### Q12.1: What are the structural specs? [SHAREABLE]

**Quote This:**
"Purpose-built for AI density. No raised floor — slab-on-grade with overhead services. Floor loading rated for 15-25 kN/m2, which handles the heaviest GPU racks (GB200 NVL72 at ~2,500 kg loaded). Minimum 4.5 m clear height."

**Key Facts:**
| Parameter | Specification |
|-----------|--------------|
| Floor type | Slab-on-grade (post-tensioned/reinforced concrete) |
| Floor loading | 15-25 kN/m2 |
| Clear height | 4.5 m minimum |
| Column grid | 6.0 m x 12.0 m optimal |
| Hall width | 12 m internal (2-bay, 4 rack rows) |
| Hall length | 18-60 m (8-24 racks per row) |
| Building efficiency | 50-55% gross-to-net (multi-tenant) |
| Fire compartment | ~2,000-2,400 m2 (under NL 2,500 m2 limit) |

**Source:** `skills/dc-engineering/references/data-hall-design.md`

---

### Q12.2: What GPU platforms do you support? [SHAREABLE]

**Quote This:**
"We're designed for current and next-gen NVIDIA platforms — H100, H200, B200, GB200 NVL72, and the upcoming GB300. Our liquid cooling infrastructure supports 120-130+ kW per rack. We also support AMD MI300X and future MI400 series."

**Key Facts:**
| Platform | Memory | TDP | Rack Power | Cooling |
|----------|--------|-----|-----------|---------|
| H100 SXM | 80 GB HBM3 | 700W | ~40-60 kW | DLC + air |
| H200 SXM | 141 GB HBM3e | 700W | ~40-60 kW | DLC + air |
| B200 SXM | 192 GB HBM3e | 1,000W | ~80-90 kW | DLC + air |
| GB200 NVL72 | 192 GB HBM3e/GPU | ~1,200W/GPU | 120-130 kW | Full liquid |
| GB300 NVL72 | 288 GB HBM3e/GPU | ~1,400W/GPU | ~140-150 kW | Full liquid |

**GB200 NVL72 — The Facility-Defining Platform:**
- 72 Blackwell GPUs + 36 Grace CPUs in single rack
- All 72 GPUs interconnected at 1,800 GB/s (NVLink 5.0)
- Rack dimensions: 2,200 mm H x 600 mm W x 1,200 mm D
- Loaded weight: ~2,500 kg
- CDU supply: 32-35°C; return: 42-45°C

**Supply Chain Lead Times (2025):**
| Platform | Lead Time | Availability |
|----------|-----------|-------------|
| H100 SXM | 4-8 weeks | Readily available |
| H200 SXM | 8-16 weeks | Moderate |
| B200 SXM | 12-24 weeks | Constrained |
| GB200 NVL72 | 16-30+ weeks | Very constrained |

**Source:** `skills/ai-infrastructure/references/gpu-accelerator-hardware.md`

---

### Q12.3: What cabling infrastructure do you provide? [SHAREABLE]

**Quote This:**
"We provide the full structured cabling infrastructure: OS2 single-mode fiber backbone (24-144 fiber count), OM4/OM5 multimode horizontal to racks, all Euroclass Cca-s1,d2,a1 rated. Cable trays are designed at 50% fill to allow future expansion. You bring your active networking equipment."

**Key Facts:**
| Cable Type | Standard | Distance | Application |
|-----------|---------|----------|-------------|
| OS2 single-mode | 9 um | up to 10 km | Backbone, inter-building |
| OM4 multimode | 50 um | up to 100 m | Horizontal to racks (400G SR4) |
| OM5 multimode | 50 um | up to 150 m | Extended intra-building |
| DAC (copper) | — | up to 3 m | Within rack |
| AOC (active optical) | — | 7-100 m | Intra-hall inter-rack |

**NEN 1010 compliance:** 150 mm minimum separation between power and data cables (EMC)

**Source:** `skills/ai-infrastructure/references/cluster-networking.md`, `skills/dc-engineering/references/data-hall-design.md`

---

## 13. Data Sovereignty [SHAREABLE]

### Q13.1: Where is the data processed? What jurisdiction?

**Quote This:**
"Netherlands, EU jurisdiction. Each site operates through a separate Dutch BV (private limited company). Dutch law governs all contracts. This gives your customers full GDPR compliance and EU AI Act alignment for data processed on our infrastructure."

**Key Facts:**
- Entity structure: Eco-Digital AG (CH holding) → DE Netherlands BV → ProjectBV per site
- Non-recourse project finance: site-level risk, not cross-collateralized
- Hardware: Lenovo (European supply chain)
- Network: Nokia (European)
- EU AI Act: requires transparency about where AI models are processed
- GDPR: data processing location matters for European enterprise buyers

**Source:** Neocloud presentation (slide 9, 13), `company/entity-register.md`

---

## 14. Competitive Positioning [SHAREABLE]

### Q14.1: Why DE vs. Nordic data centers?

**Quote This:**
"Three words: latency, latency, latency. Our sites are sub-2ms to Frankfurt and London. Nordic sites are 10-20ms. For production AI inference, that latency difference is the difference between usable and unusable for European end users."

**Full positioning matrix:**
| Factor | DE (Netherlands) | Nordic (Sweden/Finland) | Frankfurt (incumbents) | Self-Build (NL) |
|--------|-----------------|----------------------|---------------------|----------------|
| Grid | Secured | Available | Constrained | 5-10 year wait |
| Timeline | 12-18 months | 12-24 months | Waiting list | 3-5+ years |
| Latency | Sub-2ms W. Europe | 10-20ms | Sub-1ms | Sub-2ms |
| Cooling | Liquid (purpose-built) | Air (free cooling) | Mixed (retrofitted) | Varies |
| Power cost | Moderate | Low | High | Moderate |
| AI rack density | 60-130+ kW/rack | Limited by cooling | Legacy constraints | Clean-sheet |
| Heat recovery | Yes (heat revenue) | Limited market | No | Depends |

**NEVER SAY:**
- "Cheaper than Nordics on power" — we're not; our differentiator is latency and time-to-deploy
- Specific competitor pricing
- "Better than Equinix" — different product (they're multi-tenant enterprise; we're AI-purpose-built)

**Source:** Neocloud presentation (slide 6)

---

## Project-Specific Data — Dynamic Loading

When a customer asks about a **specific project**, load the project overview file:

```
projects/[project-name]/overview.md
```

**Key fields to surface per project:**
- IT capacity (MW)
- Grid connection (MVA, DSO, congestion status)
- PUE (calculated, site-specific)
- Heat recovery capacity (MWth)
- Permit status
- Timeline to RFS
- Municipality and zoning status

**Example (PowerGrow):**
- Location: De Kwakel, Uithoorn
- IT capacity: 4.3 MW
- Grid: 4.8 MVA transformer (Liander)
- PUE: 1.166
- Heat recovery: 4,880 kWth
- Permit: filed (buitenplanse afwijking)

**Route to:** `project-faq` for detailed project-specific queries.

---

## Discrepancies & Flags for Resolution

| # | Issue | Where It Appears | Resolution Needed |
|---|-------|-----------------|-------------------|
| 1 | PUE inconsistency | 1.3 (pricing) vs 1.2 (deck) vs 1.166 (PowerGrow) | Align: billing = 1.3, design = 1.15-1.20, site-specific varies. Deck should say "billing PUE 1.3, design target lower" |
| 2 | Rack density ranges | 100-225 kW (pricing) vs 40-140 kW (deck) vs 60-130 kW (engineering) | Use platform-specific numbers, not ranges. Lead with "60-130 kW depending on GPU platform" |
| 3 | On-site security | Removed from base package in v5.1 | Don't promise 24/7 manned security as standard. Clarify if add-on |
| 4 | Customer telemetry portal | Removed from SLA guarantee in v5.1 | Don't promise portal access; offer "best effort" |
| 5 | Technical hard requirements | xlsx not yet extracted to markdown | Extract and cross-reference (TODO) |

---

## Quick Reference: Communication Guardrails

### The Three Numbers That Will Get You in Trouble

1. **PUE:** Say "1.3 billing PUE" (contractual). NEVER say "1.15" to a customer.
2. **SLA:** Say "99.99% in Steady State (Phase 2)." NEVER say "from day one."
3. **Price:** Say "EUR 150/kW/month" ONLY in formal commercial discussions. NEVER in casual conversations.

### Always Do
- Lead with "purpose-built for AI" — not "generic colocation"
- Mention heat recovery as YOUR cost advantage (lower effective rate), not as a sustainability lecture
- Be upfront about Phase 1 (Early Access) — no SLA, best effort
- Be upfront about certifications — on roadmap, not yet obtained
- Quote platform-specific density (not vague ranges)
- Reference the SLA/pricing version number ("per our v5.1 terms")

### Never Do
- Promise certifications we don't have (SOC2, ISO 27001)
- Quote specific discount levels (removed from v5.1 — internal only)
- Mix up billing PUE (1.3) with design PUE (1.15-1.20)
- Promise features removed in v5.1 (on-site security, telemetry portal, per-rack metering)
- Share competitor pricing or make direct competitor claims
- Use "enterprise-grade" or "world-class" — our buyers see through marketing speak
- Quote "2N redundancy" — our design is N+1 (block redundant), and that's defensible

### Escalation Triggers
| Situation | Route To | Timeframe |
|-----------|---------|-----------|
| Custom pricing request | sales-intake → Carlos/Jelmer | Before next customer call |
| Deep GPU/network spec question | technical-analyst / ai-infrastructure | Within 24 hours |
| Security/compliance deep dive | legal-counsel + dc-engineering | Within 48 hours |
| Contract redline questions | legal-counsel | Within 48 hours |
| "Can you match [competitor] pricing?" | sales-intake → Carlos | Before responding |
| Project-specific site question | project-faq | Immediate (load project overview) |

---

*This reference is sourced from SLA v5.1, Pricing Framework v5.1, dc-engineering references, ai-infrastructure references, and the neocloud presentation deck. Contractual sources always take precedence over marketing materials.*

*Last updated: 2026-03-07*
