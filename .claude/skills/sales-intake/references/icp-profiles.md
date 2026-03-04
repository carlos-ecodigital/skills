# ICP Profiles

Per-ICP reference for collateral, objections, competitive positioning, deal economics, and messaging. Referenced during intake for positioning angle selection and post-intake for skill routing.

---

## C-NEO: Neocloud

### Key Messaging Pillars
1. **Speed to deployment** -- Grid connections that take others 5+ years, we access through existing site infrastructure
2. **Purpose-built for AI** -- High density, liquid cooling, designed for GPU workloads from day one
3. **EU market entry** -- Dutch location provides EU data sovereignty and access to EU customers
4. **Sustainability built in** -- Waste heat to growers = genuine sustainability story, not offsets

### Competitive Set & Positioning
| Competitor | Their Strength | DE Differentiator |
|-----------|---------------|-------------------|
| Nordic DCs (Iceland, Norway, Sweden) | Cheap power, cold climate | Closer to EU demand centers, better latency, established grid |
| Frankfurt/Amsterdam incumbents | Ecosystem, connectivity | Faster deployment via existing grid, lower contention, purpose-built for AI |
| Self-build | Full control | No 5-year grid wait, lower capex risk, faster time to revenue |
| US expansion (stay domestic) | Existing footprint | EU regulatory compliance (GDPR, EU AI Act), customer proximity |

### Objection Handling
| Objection | Response Framework |
|-----------|-------------------|
| "You're too small / only sub-25 MW" | "We're building purpose-built AI facilities with [X] MW in pipeline. Our scale matches neocloud unit economics -- you get a dedicated facility, not a cage in a multi-tenant hall." |
| "Nordics are cheaper on power" | "Power is one cost. Latency to EU users, regulatory compliance, and time-to-deploy are the others. Our grid access advantage means you're live 12-18 months sooner." |
| "We need Tier IV" | "GPU workloads don't need Tier IV -- they need power density, cooling, and fast recovery. We design for workload, not certification theater." |
| "Never heard of you" | "We're new, and that's the point. New facilities designed for 2025+ workloads, not retrofitted 2015 buildings." |

### Collateral References
- `collateral-studio` → Neocloud technical spec sheet
- `collateral-studio` → Facility capability brief
- `positioning-expert` → Neocloud sales narrative

### Typical Deal Economics
- Deal size: 1-50 MW
- Contract: 3-10 years
- Pricing model: per kW/month or per MW/year
- Decision cycle: 2-8 weeks (founder-led) to 3-6 months (institutional)

---

## C-ENT: Enterprise

### Key Messaging Pillars
1. **Digital sovereignty** -- EU-sovereign infrastructure, not a hyperscaler subsidiary
2. **TCO advantage** -- Cloud repatriation at 40-60% lower TCO for predictable workloads
3. **Compliance built in** -- Dutch jurisdiction, ISO/SOC-ready, sector-specific compliance
4. **Future-proof** -- Purpose-built for AI workloads with room to scale

### Competitive Set & Positioning
| Competitor | Their Strength | DE Differentiator |
|-----------|---------------|-------------------|
| AWS/Azure/GCP | Ecosystem, managed services, flexibility | True sovereignty, predictable pricing, no vendor lock-in |
| Equinix/Digital Realty | Brand, network density | Purpose-built for AI (not general colo), heat recovery story |
| On-premise / private DC | Full control | No capex, professional operations, better PUE |
| Other NL colo (NorthC, Interxion) | Local presence | AI-specific design, waste heat sustainability, newer facilities |

### Objection Handling
| Objection | Response Framework |
|-----------|-------------------|
| "We're on AWS/Azure and it works fine" | "For general workloads, yes. For dedicated AI infrastructure with data sovereignty requirements, cloud becomes expensive and non-compliant. We handle the dedicated capacity; you keep cloud for everything else." |
| "You're not Tier IV certified" | "We design to match or exceed Tier III+ reliability for AI workloads. Certification is a process we're pursuing, but the engineering is already there." |
| "Our procurement requires 3 references" | "We can arrange site visits and reference conversations with [available references]. Our infrastructure speaks for itself." |
| "Total cost still seems high vs cloud" | "Compare 3-year TCO including egress, reserved instance waste, and the sovereignty premium you'd pay for dedicated cloud regions." |

### Collateral References
- `collateral-studio` → TCO comparison deck (vs hyperscaler)
- `collateral-studio` → Enterprise capability brief
- `positioning-expert` → Enterprise sovereignty narrative

### Typical Deal Economics
- Deal size: 0.5-10 MW
- Contract: 3-7 years
- Pricing model: per kW/month, blended rate, may include managed services
- Decision cycle: 6-18 months (procurement-driven)

---

## C-INS: Institution

### Key Messaging Pillars
1. **Beyond SURF** -- Dedicated capacity without queue times, specific GPU access
2. **Academic-friendly pricing** -- Structured for grant budgets and reporting
3. **Data sovereignty** -- Dutch-hosted, suitable for sensitive research data
4. **Research partnership** -- Potential for collaboration, not just hosting

### Competitive Set & Positioning
| Competitor | Their Strength | DE Differentiator |
|-----------|---------------|-------------------|
| SURF | Free/subsidized, established, trusted | Dedicated capacity, no queue, specific hardware, more flexibility |
| Cloud (AWS/Azure/GCP) | On-demand, massive scale | Predictable pricing, no egress costs, data in NL, grant-compatible |
| Own cluster | Full control, on-campus | No capex, professional cooling, better GPU utilization |

### Objection Handling
| Objection | Response Framework |
|-----------|-------------------|
| "SURF is free" | "SURF is shared and oversubscribed. Your researchers wait weeks for GPU time. With us, you get dedicated capacity when you need it. The cost of delayed research exceeds the cost of dedicated compute." |
| "Our grant doesn't cover this" | "Most NWO/EU grants cover compute as eligible OPEX. We structure contracts to match grant reporting requirements. Happy to review the specific grant terms." |
| "We need to go through university procurement" | "Understood. We can support your procurement process with technical specs, references, and compliance documentation. How can we help prepare the internal case?" |

### Collateral References
- `collateral-studio` → Academic capability brief
- `collateral-studio` → Grant-compatible pricing sheet

### Typical Deal Economics
- Deal size: 0.2-5 MW
- Contract: 1-5 years (aligned with grant periods)
- Pricing model: per GPU-hour, reserved capacity blocks, or flat monthly
- Decision cycle: 3-12 months

---

## S-GRW: Grower (Greenhouse)

### Key Messaging Pillars (Dutch/English)
1. **Gratis warmte / Free heat** -- Uw gaskosten naar nul, zonder investering
2. **Uw grond, uw bedrijf / Your land, your business** -- U houdt volledige controle over uw teelt
3. **Aanvullende inkomsten / Additional income** -- Grondhuur voor het datacenter-perceel
4. **Toekomstbestendig / Future-proof** -- Klaar voor de warmtetransitie, zonder risico

### Competitive Set & Positioning
| Competitor | Their Strength | DE Differentiator |
|-----------|---------------|-------------------|
| Gas (status quo) | Known, reliable, existing infrastructure | Free heat, zero gas cost, future-proof against gas price rises |
| Geothermie / Geothermal | Sustainable, supported by subsidies | No boring risk, no CAPEX, proven technology, faster deployment |
| Biomassa / Biomass | Available, SDE++ eligible | No fuel cost, no emissions, no particulate matter |
| Warmtepomp / Heat pump | Electric, efficient | No electricity cost for heating, higher output |

### Objection Handling
| Objection | Response Framework |
|-----------|-------------------|
| "30 jaar is te lang / 30 years is too long" | "Het contract is 15-25 jaar, vergelijkbaar met geothermie. Maar anders dan geothermie investeert u niets en draagt u geen risico. (The contract is 15-25 years, similar to geothermal. But unlike geothermal, you invest nothing and carry no risk.)" |
| "Een datacenter op mijn land? / A DC on my land?" | "Het datacenter staat op een apart perceel met eigen toegang. Uw kas en teeltbedrijf worden niet gestoord. Veel kwekers merken er niets van. (The DC sits on a separate plot with its own access. Your greenhouse and cultivation are not disturbed.)" |
| "Ik wil eerst geothermie proberen" | "Geothermie kost EUR 15-25M investering met boorrisico. Wij leveren dezelfde warmte zonder investering, zonder risico, en sneller. (Geothermal costs EUR 15-25M with drilling risk. We deliver the same heat without investment, without risk, and faster.)" |
| "Wat als het datacenter stopt? / What if the DC shuts down?" | "Het contract garandeert warmtelevering voor de volledige looptijd. Bij ontbinding krijgt u compensatie en behoudt u de netaansluiting. (The contract guarantees heat supply for the full term. On termination you receive compensation and keep the grid connection.)" |

### Collateral References
- `collateral-studio` → Grower one-pager (NL)
- `collateral-studio` → Grower presentation (NL)

### Typical Deal Economics
- Site value: 5-25 MVA grid connection
- Contract: 15-25 years (land + heat)
- Grower receives: free heat + ground rent
- Decision cycle: days to weeks (owner-operator)

---

## S-DHN: District Heating

### Key Messaging Pillars
1. **Wcw compliance** -- DC waste heat counts as sustainable heat under Wcw obligations
2. **Reliable baseload** -- 24/7 continuous heat supply, not weather-dependent
3. **Competitive pricing** -- Below gas-equivalent, long-term price certainty
4. **Scalable with network growth** -- DC capacity can scale as the network expands

### Competitive Set & Positioning
| Competitor | Their Strength | DE Differentiator |
|-----------|---------------|-------------------|
| Gas boilers (status quo) | Known, reliable, flexible | Zero-carbon, Wcw compliant, long-term price certainty |
| Geothermal | Sustainable, high temp, SDE++ eligible | No drilling risk, no CAPEX, proven source, faster deployment |
| Biomass | Sustainable classification, existing capacity | No fuel cost volatility, no particulate emissions, more scalable |
| Other waste heat (industry) | May be higher temperature | More reliable (24/7 DC operation), purpose-designed for heat supply |

### Objection Handling
| Objection | Response Framework |
|-----------|-------------------|
| "DC heat is too low-grade (temperature)" | "Our systems supply 40-50C baseload, upgradeable with heat pumps to 70-90C. For low-temperature networks, we're ideal. For high-temp, we handle baseload and you peak with existing sources." |
| "What about supply reliability?" | "Data centers operate 24/7/365 with redundant systems. Our heat output is more predictable than any other renewable source. We contractually guarantee availability levels." |
| "We need to go through public tender" | "Understood. We can support your tender process with technical specifications, reference projects, and compliance documentation. We can also engage informally during the market exploration phase." |
| "Multiple stakeholders need to agree" | "We're experienced with municipal governance. Happy to present to the college, relevant committees, or do a technical briefing for your team." |

### Collateral References
- `collateral-studio` → DH compliance brief
- `collateral-studio` → Heat supply framework proposal

### Typical Deal Economics
- Deal size: 5-100 MWth
- Contract: 15-25 years
- Heat price: EUR 10-25/MWh
- Decision cycle: 6-18 months (municipal governance)

---

## S-IND: Industrial Heat

### Key Messaging Pillars
1. **Decarbonize without disrupting production** -- Replace gas incrementally, not all at once
2. **Energy cost certainty** -- Fixed heat price, immune to gas price volatility
3. **ESG reporting** -- Genuine Scope 1/2 emission reduction for sustainability reporting
4. **Process integration** -- Designed to match your specific temperature and load profile

### Competitive Set & Positioning
| Competitor | Their Strength | DE Differentiator |
|-----------|---------------|-------------------|
| Gas (status quo) | Known, reliable, any temperature | Zero-carbon, price certainty, ESG compliance |
| Electric heating | Direct, efficient for some processes | Lower cost, no grid capacity needed for heating |
| Geothermal | High temperature potential | No CAPEX, no drilling risk, more predictable |
| Heat pump | Efficient, controllable | Lower electricity demand, continuous output |

### Objection Handling
| Objection | Response Framework |
|-----------|-------------------|
| "Our process needs 150C, your heat is 50C" | "We can supply preheating stages (ambient to 50C) and reduce your gas consumption by 30-40%. You keep gas for the final temperature boost. That alone delivers significant ESG and cost impact." |
| "We can't risk production downtime" | "We don't propose replacing your primary heat source. We supplement it. Your existing backup stays in place. We add a low-cost, zero-carbon layer underneath." |
| "How does this work with our process?" | "We do a process integration study specific to your facility. It maps exactly how DC waste heat fits into your heat flows, what equipment is needed, and what savings you get." |

### Collateral References
- `collateral-studio` → Integration study template
- `collateral-studio` → Industrial heat capability brief

### Typical Deal Economics
- Deal size: 1-50 MWth
- Contract: 10-20 years
- Heat price: EUR 10-25/MWh
- Decision cycle: 3-12 months (plant management)
