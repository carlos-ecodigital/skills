# Colocation Track -- Intake Questions (Demand Side)

ICP-specific question modules for buyers of AI colocation capacity. Each ICP module extends the shared base questions from `intake-questions-shared.md`.

**ICPs in this track:**
- **C-NEO** -- Neocloud (GPU cloud providers): Lambda, CoreWeave, Crusoe, Voltage Park, Together AI
- **C-ENT** -- Enterprise (corporate AI): banks, telcos, industrial corporates running AI/ML
- **C-INS** -- Institution (research/government): universities, TNO, KNMI, government agencies

---

## C-NEO: Neocloud Module

### Phase 1 -- Identity & Context (+2 questions)

#### Q1.4-NEO -- Funding & Growth Stage
**Text:** "Where are they in their growth? Recently funded? How much capacity are they running today?"
**Why:** Neoclouds are capital-intensive and growth-stage. A recently funded neocloud (Series B/C) with expansion pressure is the hottest lead type. Also reveals whether they can actually sign a contract.
**Feeds:** Lead Qualification Score (capacity need, decision authority), Opportunity Brief (section 1, 4)
**Auto-fill from:** Crunchbase, Dealroom, recent press

#### Q1.5-NEO -- Current Footprint
**Text:** "Where do they operate today? Own DCs, colo partners, which regions?"
**Why:** Reveals competitive set (who are we displacing), geographic strategy (are they expanding to EU?), and sophistication level.
**Feeds:** Opportunity Brief (section 7), Pre-Meeting Prep (competitive positioning), scoring

### Phase 2 -- Need & Problem (+3 questions)

#### Q2.5-NEO -- Workload Type
**Text:** "What workloads -- training, inference, or both? GPU type preference?"
**Why:** Training = dense power, long contracts, predictable load. Inference = latency-sensitive, variable demand, proximity matters. GPU type determines cooling requirements and power density.
**Feeds:** Opportunity Brief (section 3, 5), technical spec matching, Lead Qualification Score (technical fit)
**Conditional:** If inference → ask about latency requirements and end-user geography

#### Q2.6-NEO -- Power Density Requirements
**Text:** "What power density do they need? kW per rack, liquid cooling requirements?"
**Why:** DE's purpose-built facilities can handle high density (>30 kW/rack with liquid cooling). This is a key differentiator vs traditional colo. If they need <10 kW/rack, we may not be the right fit.
**Feeds:** Opportunity Brief (section 3, 5), technical feasibility, Lead Qualification Score (technical fit)

#### Q2.7-NEO -- EU Expansion Driver
**Text:** "Why EU / Netherlands specifically? Sovereignty, customer proximity, capacity constraints elsewhere?"
**Why:** The reason they want EU presence determines our positioning angle. Sovereignty → GDPR/EU AI Act. Customer proximity → latency. Capacity constraints → speed of deployment.
**Feeds:** Lead Qualification Score (strategic driver), Opportunity Brief (section 4, 6), positioning angle

### Phase 3 -- Technical / Ops (+4 questions)

#### Q3.4-NEO -- Deployment Model
**Text:** "Are they looking for wholesale/shell (they outfit the space) or fully fitted (turnkey)?"
**Why:** Determines DE's scope and pricing model. Wholesale = lower price, faster, less DE responsibility. Turnkey = higher margin, more control, longer lead time.
**Feeds:** Opportunity Brief (section 3, 9), commercial parameters, site matching

#### Q3.5-NEO -- Network Requirements
**Text:** "What connectivity do they need? Dark fiber, carrier-neutral, specific peering requirements?"
**Why:** Network is table stakes for neoclouds. Inadequate connectivity kills deals regardless of power/price.
**Feeds:** Opportunity Brief (section 3), technical feasibility check, site matching

#### Q3.6-NEO -- Redundancy & SLA
**Text:** "What availability do they require? N+1, 2N? What's their SLA expectation?"
**Why:** Neoclouds vary widely. Training workloads tolerate brief outages; inference serving customer-facing apps needs high availability.
**Feeds:** Opportunity Brief (section 3), technical design, Lead Qualification Score (technical fit)

#### Q3.7-NEO -- Phasing & Ramp
**Text:** "Do they want everything at once, or phased deployment? What's the ramp schedule?"
**Why:** Large deals (>10 MW) almost always phase. Understanding the ramp protects DE from building capacity that sits idle.
**Feeds:** Opportunity Brief (section 5, 9), commercial structuring, site capacity planning
**Conditional:** Only ask if capacity need >5 MW

### Phase 4 -- Commercial / Financial (+3 questions)

#### Q4.4-NEO -- Price Benchmarks
**Text:** "What are they paying in their current locations? Per kW, per MW, blended?"
**Why:** Neoclouds know their unit economics cold. Their current cost sets the reference price we must beat or justify.
**Feeds:** Lead Qualification Score (budget/price fit), Opportunity Brief (section 9), Validation (benchmark)

#### Q4.5-NEO -- Contract Structure Preference
**Text:** "What contract term and structure are they used to? Take-or-pay, flexible, reserved?"
**Why:** Neoclouds prefer flexibility; DE needs long-term commitments for project finance. Finding the middle ground is critical.
**Feeds:** Opportunity Brief (section 9), legal routing, commercial negotiation prep

#### Q4.6-NEO -- NDA Status
**Text:** "Have we signed an NDA? Do they require one before sharing specs?"
**Why:** Neoclouds often require NDAs before detailed technical/commercial discussions. Knowing this upfront prevents stalling.
**Feeds:** Recommended Next Actions (NDA as first step), legal routing

---

## C-ENT: Enterprise Module

### Phase 1 -- Identity & Context (+3 questions)

#### Q1.4-ENT -- AI/ML Maturity
**Text:** "How mature is their AI practice? Experimenting, scaling, or mission-critical production?"
**Why:** Determines the conversation level. Experimenters need education. Scalers need infrastructure. Production runners need reliability and compliance.
**Feeds:** Opportunity Brief (section 1, 3), positioning angle, Pre-Meeting Prep (conversation level)

#### Q1.5-ENT -- IT Decision Structure
**Text:** "Who owns infrastructure decisions? CTO, CIO, VP Infrastructure, procurement?"
**Why:** Enterprise decisions involve multiple stakeholders. Mapping the buying center early prevents wasted effort on the wrong person.
**Feeds:** Opportunity Brief (section 2), Lead Qualification Score (decision authority), stakeholder mapping

#### Q1.6-ENT -- Industry & Regulatory Context
**Text:** "What industry are they in? Any specific regulatory requirements for data hosting?"
**Why:** Financial services (DNB/ECB oversight), healthcare (NEN 7510), government (BIO) all have specific hosting requirements that DE's Dutch sovereign positioning addresses.
**Feeds:** Opportunity Brief (section 1, 6), Lead Qualification Score (strategic driver), compliance matching

### Phase 2 -- Need & Problem (+4 questions)

#### Q2.5-ENT -- Current Cloud Spend
**Text:** "What's their current cloud/infrastructure spend? Annual, growing, who are the vendors?"
**Why:** Cloud spend is the budget DE is competing for. Knowing the number and the incumbent shapes the TCO comparison.
**Feeds:** Lead Qualification Score (budget/price fit), Opportunity Brief (section 7, 9), TCO comparison prep

#### Q2.6-ENT -- Sovereignty / Data Residency
**Text:** "Is data sovereignty or EU data residency a factor? GDPR, EU AI Act, sector-specific rules?"
**Why:** Sovereignty is the #1 strategic driver for enterprise. If they need EU-sovereign infrastructure, DE wins vs hyperscalers on this axis.
**Feeds:** Lead Qualification Score (strategic driver, 20% weight), Opportunity Brief (section 4, 6), positioning

#### Q2.7-ENT -- Cloud Exit Pain
**Text:** "Are they trying to reduce dependency on a specific hyperscaler? Which one and why?"
**Why:** Cloud repatriation/hybrid strategies are a major enterprise trend. Understanding the exit motivation shapes our positioning.
**Feeds:** Opportunity Brief (section 4, 7), competitive positioning, Pre-Meeting Prep

#### Q2.8-ENT -- Workload Description
**Text:** "What AI/ML workloads specifically? Training, fine-tuning, inference, RAG, other?"
**Why:** Enterprise workloads are often more specialized than neocloud. Understanding the workload determines technical requirements and pricing model.
**Feeds:** Opportunity Brief (section 3), technical matching, Lead Qualification Score (technical fit)

### Phase 3 -- Technical / Ops (+3 questions)

#### Q3.4-ENT -- Hybrid Architecture
**Text:** "Will this be standalone or connected to their existing cloud/on-prem? What integration is needed?"
**Why:** Enterprises rarely go all-in on a single provider. Understanding the hybrid architecture determines connectivity, latency, and integration requirements.
**Feeds:** Opportunity Brief (section 3), technical feasibility, Pre-Meeting Prep

#### Q3.5-ENT -- Security & Compliance
**Text:** "What security certifications do they need? ISO 27001, SOC 2, sector-specific?"
**Why:** Enterprise procurement often has hard compliance requirements. Knowing these upfront prevents late-stage deal death.
**Feeds:** Opportunity Brief (section 3, 8), Lead Qualification Score (technical fit), compliance gap assessment

#### Q3.6-ENT -- Managed Services
**Text:** "Do they want bare metal only, or managed services (monitoring, patching, support)?"
**Why:** Determines DE's service scope and pricing. Also indicates the enterprise's in-house capability level.
**Feeds:** Opportunity Brief (section 3, 9), commercial structuring, staffing requirements

### Phase 4 -- Commercial / Financial (+4 questions)

#### Q4.4-ENT -- Budget Authority
**Text:** "Is there an approved budget for this, or is it still in planning?"
**Why:** Enterprise without budget approval = 6-12 month delay minimum. Affects deal timeline scoring.
**Feeds:** Lead Qualification Score (decision authority, timeline match), Opportunity Brief (section 9)

#### Q4.5-ENT -- Procurement Process
**Text:** "Is this going through formal procurement? RFP/RFI? What's the process and timeline?"
**Why:** Enterprise procurement processes are the #1 timeline determinant. An RFP means competitive bidding; informal means faster but less structured.
**Feeds:** Lead Qualification Score (timeline match), Opportunity Brief (section 9), Recommended Next Actions

#### Q4.6-ENT -- TCO Comparison Frame
**Text:** "What's their comparison baseline? Are they benchmarking us against cloud pricing, existing colo, or internal DC costs?"
**Why:** The comparison frame determines how we build the business case. Cloud repatriation TCO is different from colo-vs-colo comparison.
**Feeds:** Opportunity Brief (section 7, 9), collateral routing (TCO comparison deck), Pre-Meeting Prep

#### Q4.7-ENT -- Sustainability Requirements
**Text:** "Is sustainability / ESG reporting a factor in their infrastructure decisions?"
**Why:** DE's waste heat model is a genuine sustainability differentiator. If ESG reporting matters, this becomes a major selling point.
**Feeds:** Opportunity Brief (section 6), positioning angle, Lead Qualification Score (strategic driver)

---

## C-INS: Institution Module

### Phase 1 -- Identity & Context (+2 questions)

#### Q1.4-INS -- Institution Type
**Text:** "What type of institution? University, research institute, government agency, hospital?"
**Why:** Determines funding model, procurement rules, and competitive alternatives. Universities have different buying patterns than government agencies.
**Feeds:** Opportunity Brief (section 1), procurement approach, pricing model

#### Q1.5-INS -- Current Compute Access
**Text:** "How are they getting compute today? SURF, own cluster, cloud, nothing?"
**Why:** SURF (Dutch national compute provider) is the default competitor. If they're on SURF and hitting limits, that's the trigger. If they've never used SURF, that's unusual and worth understanding.
**Feeds:** Opportunity Brief (section 7), competitive positioning, Lead Qualification Score

### Phase 2 -- Need & Problem (+3 questions)

#### Q2.5-INS -- Research Focus
**Text:** "What research domain? NLP, computer vision, climate modeling, genomics, other?"
**Why:** Research domain determines compute profile (GPU type, memory, storage) and potential for long-term collaboration.
**Feeds:** Opportunity Brief (section 3), technical matching, positioning angle

#### Q2.6-INS -- Grant Constraints
**Text:** "Is this funded by a specific grant? What are the spending constraints?"
**Why:** Grant-funded compute has strict OPEX/CAPEX rules, time boundaries, and audit requirements. This shapes the commercial model entirely.
**Feeds:** Lead Qualification Score (budget fit, 20% weight), Opportunity Brief (section 9), pricing model
**Conditional:** If grant-funded → ask about grant period, eligible expenses, reporting requirements

#### Q2.7-INS -- SURF Limitations
**Text:** "What's not working about their current setup? Capacity limits, wait times, specific hardware needs?"
**Why:** Understanding why SURF isn't enough is the direct value proposition. Specific pain (wait times, GPU shortages, data restrictions) shapes our pitch.
**Feeds:** Opportunity Brief (section 4, 7), Pre-Meeting Prep, positioning vs SURF

### Phase 3 -- Technical / Ops (+2 questions)

#### Q3.4-INS -- Data Sensitivity
**Text:** "How sensitive is their research data? Any specific classification or handling requirements?"
**Why:** Some institutional data (medical, defense, personal data) has strict handling requirements that affect facility design and access controls.
**Feeds:** Opportunity Brief (section 3, 8), technical requirements, compliance matching

#### Q3.5-INS -- Multi-Tenancy Tolerance
**Text:** "Do they need dedicated hardware or is shared/multi-tenant acceptable?"
**Why:** Budget-constrained institutions often accept shared infrastructure. Dedicated = higher cost but simpler compliance. Shared = cost-effective but more complex isolation.
**Feeds:** Opportunity Brief (section 3, 9), pricing model, technical design

### Phase 4 -- Commercial / Financial (+3 questions)

#### Q4.4-INS -- Budget Model
**Text:** "How are they funding this? Departmental budget, research grant, multi-year program, consortium?"
**Why:** Funding source determines contract flexibility, term length, payment structure, and approval process.
**Feeds:** Lead Qualification Score (budget fit), Opportunity Brief (section 9), commercial structuring

#### Q4.5-INS -- Pricing Sensitivity
**Text:** "What pricing model works for them? Per-GPU-hour, reserved capacity, flat monthly?"
**Why:** Institutions are highly price-sensitive and used to academic pricing. The model must be simple and auditable for grant reporting.
**Feeds:** Opportunity Brief (section 9), pricing strategy, Lead Qualification Score (budget fit)

#### Q4.6-INS -- Multi-Year Appetite
**Text:** "Are they looking for a one-off allocation or ongoing capacity over multiple years?"
**Why:** Multi-year commitments require different approval processes (university board, ministry approval) but are more valuable to DE.
**Feeds:** Lead Qualification Score (timeline match), Opportunity Brief (section 9), decision process mapping
**Conditional:** If multi-year → ask about approval authority and budget cycle

---

## Secondary Conditionals (Within ICP Modules)

These are triggered by specific answers within the ICP modules above.

### C-NEO Conditionals
- **If capacity >10 MW:** Trigger Q3.7-NEO (phasing). Also: "Have they done deployments of this scale before?"
- **If inference workload:** "What latency requirements? Where are their end users?"
- **If currently in US only:** "Is this their first EU deployment? Do they have EU legal entity?"
- **If wholesale model:** "Do they bring their own ops team, or do they need on-site support?"

### C-ENT Conditionals
- **If on hyperscaler:** Trigger Q2.7-ENT (cloud exit). "What's driving the change -- cost, control, compliance?"
- **If RFP process:** "When does the RFP go out? Can we influence the spec?"
- **If multi-stakeholder:** "Who has final sign-off? What's the committee structure?"
- **If financial services:** "DNB/ECB outsourcing requirements -- are they aware of the regulatory framework?"

### C-INS Conditionals
- **If grant-funded:** Trigger Q2.6-INS follow-up. "What's the grant period? What expenses are eligible?"
- **If SURF user:** "What's their SURF allocation? When does it renew?"
- **If consortium:** "How many institutions? Who leads procurement?"
- **If sensitive data:** "Is there a DPIA (Data Protection Impact Assessment) in place?"
