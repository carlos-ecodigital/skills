# Opportunity Brief: Voltage Park

**Date:** 2025-03-15 | **Score:** 4.55 / 5.0 | **Tier:** 1 (Hot)
**ICP:** C-NEO (Neocloud) | **Track:** Colocation | **Owner:** Christian

---

## 1. Company Profile

Voltage Park is a US-based GPU cloud provider (Series B, ~$120M raised) offering on-demand and reserved NVIDIA GPU capacity to AI startups, research labs, and enterprise inference customers. Founded 2023, headquartered in San Francisco. Currently operates out of US data centers and is actively expanding into Europe to serve EU customers and comply with emerging EU AI Act data residency preferences. ~50 employees, growing rapidly.

## 2. Key People

| Name | Role | Decision Authority | Notes |
|------|------|--------------------|-------|
| Jake Thompson | CTO | DM -- can sign facility agreements | Primary technical contact. Referred by [advisor]. Focused on power density and liquid cooling support. |
| Sarah Chen | VP Infrastructure | Influencer -- leads site selection | Running the EU expansion project. Evaluating NL, Nordics, Frankfurt. |
| Mark Rivera | CEO | Final sign-off on >$5M commitments | Not yet engaged. Jake indicated he has autonomy for initial facility deals. |

## 3. What They Need

10 MW of GPU-ready colocation capacity in the EU, deployable within 6 months. Specifically: high-density racks (30-60 kW/rack), rear-door or direct-to-chip liquid cooling, and reliable power with N+1 redundancy. Initial deployment 5 MW, scaling to 10 MW within 12 months. Primarily NVIDIA H100/B200 clusters for inference workloads.

## 4. Why Now (Trigger)

EU AI Act creating data residency demand from Voltage Park's enterprise customers. Three EU enterprise customers have explicitly requested EU-hosted GPU capacity. Additionally, Voltage Park's US capacity is nearing utilization limits and they need geographic diversification. Series B closed Q4 2024 -- capital available for expansion.

## 5. How We Fit

Strong fit. DE can offer:
- **Capacity:** 5-10 MW available at [Site Name] within the requested timeline
- **Density:** Facility designed for 30-60 kW/rack from day one, liquid cooling included
- **Speed:** Grid connection already secured -- no 5-year wait
- **Location:** Netherlands = EU jurisdiction, GDPR/EU AI Act compliant, AMS-IX proximity

Key gap: Voltage Park wants 10 MW; initial site may cap at 8 MW. Phasing discussion needed -- 5 MW Phase 1, remainder via adjacent capacity or second site.

## 6. Positioning Angle

Lead with **speed to deployment** + **purpose-built for AI**. Voltage Park's #1 pain is time-to-revenue in the EU market -- every month of delay means lost enterprise contracts. Secondary angle: sustainability story (waste heat to growers) supports their ESG narrative to institutional investors.

Avoid: price comparison with Nordics (they'll bring it up -- redirect to total cost including latency, compliance, and deployment speed).

## 7. Competitive Landscape

| Alternative | Status | DE Advantage |
|-------------|--------|--------------|
| Nordic DCs (Atria, Iceland) | Sarah visited Iceland site in January | NL is closer to EU demand centers. Lower latency to Frankfurt/AMS. No 5-year grid wait. |
| Frankfurt incumbent (Equinix FR) | Received pricing, availability Q4 2025 | DE delivers 6+ months sooner. Purpose-built for AI vs retrofitted general colo. |
| Self-build (lease land in NL) | Considered and rejected -- too slow | Validates our speed advantage. Reference this in discussions. |

Key differentiator vs all: DE has grid access now. Self-build and new Frankfurt builds face 3-5 year grid queues.

## 8. Obstacles & Risk

| Obstacle | Severity | Mitigation |
|----------|----------|------------|
| Scale concern ("only 8 MW at one site") | Medium | Present phasing plan: 5 MW Phase 1, 3 MW Phase 2. Show pipeline of additional sites for future scale. |
| "Never heard of DE" | Medium | Site visit invitation. Technical deep-dive with engineering team. Reference conversations with existing partners. |
| Nordic power cost comparison | Low | Prepare TCO comparison including latency cost, compliance cost, and time-to-revenue. Nordic is cheaper per kWh but slower and further. |

No red flags identified. Strong technical fit, funded, real EU demand driver.

## 9. Commercial Parameters

- **Expected deal size:** 5-10 MW (EUR 3-6M ARR at estimated pricing)
- **Pricing model:** per kW/month, wholesale colocation (shell + power + cooling)
- **Contract term:** 3-5 years initial, renewal options
- **Decision timeline:** 4-8 weeks (Jake has authority; Sarah drives evaluation)
- **Decision process:** Jake (CTO) evaluates and recommends → Mark (CEO) approves if >$5M → Legal review on contract terms

## 10. Recommended Next Actions

1. **Schedule site visit** -- Invite Jake + Sarah to [Site Name] within 2 weeks. Owner: Christian. Deadline: 2025-03-22.
   Route to: `ops-meetingops` (agenda prep)

2. **Prepare neocloud technical spec sheet** -- Power density, cooling specs, connectivity, redundancy, timeline.
   Route to: `collateral-studio` (neocloud spec sheet)

3. **TCO comparison: DE vs Nordics vs Frankfurt** -- 3-year total cost including latency, compliance, deployment speed.
   Route to: `collateral-studio` (TCO comparison) + `positioning-expert` (competitive framing)

4. **NDA execution** -- Jake mentioned willingness to sign NDA for detailed pricing and site specifics.
   Route to: `legal-counsel` (NDA)

5. **Research dossier on Voltage Park** -- Funding history, infrastructure partners, EU customer base, competitive positioning.
   Route to: `ops-targetops` (research dossier)

6. **CRM entry** -- Create Contact (Jake Thompson, Sarah Chen), Company (Voltage Park), Deal (Voltage Park - Neocloud Colocation, Sales pipeline, Lead stage, Tier 1).
   Route to: `ops-dealops` (HubSpot)
