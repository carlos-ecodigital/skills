# Objection Handling — Top Objections by Buyer Segment

Framework: Acknowledge → Reframe → Evidence → Next Step

For each objection: acknowledge the concern (never dismiss), reframe to show the real trade-off, provide specific evidence, then move forward.

---

## Grower Objections

### 1. "30 years is too long a commitment"
- **Acknowledge:** "30 years sounds like a long time. That's a fair concern."
- **Reframe:** "Your greenhouse heating infrastructure lasts 25-30 years too. This replaces your heating source with a better one, on the same timeline. And you have non-renewal windows every 5 years with 5-year notice."
- **Evidence:** Natural gas boiler replacement cycle: 20-30 years. CHP WKK lifecycle: 15-25 years. Our term matches what you'd commit to anyway.
- **Next step:** "Would seeing the specific withdrawal and non-renewal provisions address your concern?"

### 2. "I don't want a data center on my property"
- **Acknowledge:** "Completely understandable — the word 'data center' conjures images of massive warehouses."
- **Reframe:** "A DEC is roughly 2,000 sqm — smaller than one greenhouse bay. It's enclosed, no external noise above 45 dB at the property line (quieter than your existing WKK). It uses your existing grid connection, so no new overhead lines."
- **Evidence:** Specific DEC footprint dimensions; noise specifications; visual rendering.
- **Next step:** "Can I show you what a DEC looks like on a site similar to yours?"

### 3. "What if Digital Energy goes bankrupt?"
- **Acknowledge:** "That's exactly the right question to ask about any long-term partner."
- **Reframe:** "Each DEC is owned by a separate Dutch BV (ProjectBV). The physical infrastructure stays on your land secured by recht van opstal. The heat supply contract transfers to any successor operator. Your land rights are registered at the Kadaster — they don't disappear with us."
- **Evidence:** ProjectBV structure, recht van opstal registration, non-recourse project finance (lenders also need the project to survive).
- **Next step:** "Would it help if our legal team walked through the structural protections with your advisor?"

### 4. "My gas bill isn't that high"
- **Acknowledge:** "If gas costs are manageable today, there's less urgency."
- **Reframe:** "EU ETS2 starts in 2027. That adds EUR 10-20/MWh to your gas cost. Your gas bill isn't just today's price — it's today's price plus carbon. And gas prices are fundamentally volatile (TTF went from EUR 20 to EUR 300 and back). DEC heat is CPI-indexed: stable, predictable."
- **Evidence:** TTF price history chart. ETS2 projected cost. 10-year gas cost scenario vs. DEC heat cost scenario.
- **Next step:** "If I run a 10-year cost comparison with your actual gas consumption, would that be useful?"

### 5. "I need to discuss with my accountant / advisor first"
- **Acknowledge:** "Absolutely — your advisors should review this."
- **Reframe:** This isn't an objection. This is a buying signal. They're taking it seriously enough to involve their advisor.
- **Evidence:** Provide a one-page summary designed for financial advisors: key economics, contract structure, tax implications (9% BTW on heat).
- **Next step:** "I have a one-page advisor brief. Can I send that over? And would it be helpful if I joined a call with your accountant to answer technical questions?"

---

## Neocloud Objections

### 6. "We need more than 25 MW — you're too small"
- **Acknowledge:** "Scale matters for GPU cloud economics. You're right to think about growth."
- **Reframe:** "Our Fonti pilot is 1.2 MW — that's intentional. Prove the model fast, then scale. Powergrow is 4.1 MW. We have 70 MW expansion pipeline at the Lodewijk site alone, and we're developing multiple sites. Start small, prove reliability, scale with us."
- **Evidence:** Fonti timeline (4 months from FID), 70 MW expansion reservation, multi-site development pipeline.
- **Next step:** "What's your 12-month capacity roadmap? Let me show you how our pipeline aligns."

### 7. "Nordic power is cheaper"
- **Acknowledge:** "Nordics have some of the cheapest electricity in Europe. That's real."
- **Reframe:** "Power cost isn't the only variable. NL gives you AMS-IX proximity (world's largest internet exchange), sub-2ms latency to Frankfurt and London, and immediate grid access. Nordic builds take 2-3 years and latency to major European customers is 10-20ms higher. For inference workloads, latency matters. For enterprise customers, Netherlands is a trust jurisdiction."
- **Evidence:** NL vs. Nordic latency comparison. AMS-IX connectivity. NL grid timeline vs. Nordic build timeline.
- **Next step:** "What's your customer distribution? If inference is >30% of workload, NL may actually be cheaper on total cost when you factor in latency impact on utilization."

### 8. "We're already in talks with [Equinix / Digital Realty / NorthC]"
- **Acknowledge:** "Those are good operators."
- **Reframe:** "They're colocation. We're infrastructure + heat economics. Our waste heat revenue subsidizes operating costs — that flows through to your pricing. And we build liquid cooling native from Day 1 — most incumbents are retrofitting air-cooled facilities. Ask them what their PUE is at 100+ kW/rack."
- **Evidence:** PUE comparison: DE target 1.2 vs. typical incumbent 1.4-1.6 at AI density. Cost comparison model.
- **Next step:** "Let me run a side-by-side cost model with your actual workload profile. No obligation."

---

## Enterprise Objections

### 9. "We're committed to AWS / Azure / GCP"
- **Acknowledge:** "Hyperscaler platforms are powerful and deeply integrated into enterprise workflows."
- **Reframe:** "We're not asking you to leave cloud. Most enterprises run 60-80% predictable workloads and 20-40% burst. Dedicated infrastructure for the predictable portion saves 30-50% while cloud handles burst. Hybrid is the smart play."
- **Evidence:** Cost comparison: hyperscaler GPU-hour vs. dedicated. Enterprise case studies of hybrid approaches.
- **Next step:** "What percentage of your AI workload is predictable vs. burst? That's the number that tells us if dedicated makes sense."

### 10. "Our procurement process takes 12-18 months"
- **Acknowledge:** "Enterprise procurement timelines are real. We respect the process."
- **Reframe:** "DEC development takes 18-30 months. Starting procurement now means the facility is ready when you need it. If you wait, you're adding 18-30 months to your 12-18 month timeline."
- **Evidence:** DC development timeline: permitting → engineering → construction → commissioning.
- **Next step:** "Can we start with a technical assessment to give your procurement team the data they need?"

---

## District Heating Objections

### 11. "Data center heat is low-temperature / low-grade"
- **Acknowledge:** "Temperature is a critical parameter for heat networks."
- **Reframe:** "DEC waste heat is 45-60°C direct from servers. This is ideal for 4th/5th generation low-temperature district heating networks — which is where the industry is heading (Wcw alignment). For existing high-temp networks, heat pumps can boost to 80-90°C. The Wcw reform is pushing toward lower temperatures anyway."
- **Evidence:** 4th gen district heating literature. Wcw cost-based tariff framework (favors lower-temp sources). Heat pump boost economics.
- **Next step:** "What's your current network temperature? Let me model the integration for your specific system."

### 12. "We need board / municipal approval"
- **Acknowledge:** "Municipal governance is part of your decision process."
- **Reframe:** "We've prepared documentation specifically designed for board-level presentations: technical feasibility, financial model, regulatory compliance analysis, and environmental impact. We can also present directly to the board if that's helpful."
- **Evidence:** Pre-packaged board presentation materials.
- **Next step:** "When is your next board meeting? Let me prepare a board-ready briefing document tailored to your network."

---

## Energy Partner / Investor Objections

### 13. "How do I know my equity stake won't be diluted?"
- **Acknowledge:** "Dilution protection is a standard concern in any equity structure."
- **Reframe:** "This is exactly what the Definitive Agreements are for. The HoT/framework agreement sets the equity allocation principles. Definitive Agreements will include standard anti-dilution provisions. We're at framework stage now — detailed protections come in the legal documentation."
- **Evidence:** Standard PE/infra anti-dilution mechanisms: weighted-average ratchet, preemptive rights, tag-along.
- **Next step:** "Would you like to involve your legal advisor in the framework discussion? We can schedule a joint session."

### 14. "The returns seem too good to be true"
- **Acknowledge:** "Skepticism about projections is healthy. We respect that."
- **Reframe:** "That's why we present three scenarios — conservative, base, and optimistic. The conservative scenario honestly shows below-CAPEX returns. Base case is built on independently sourced assumptions (CBRE pricing, BNEF BESS costs, Alantra multiples). Every number has a footnote."
- **Evidence:** Three-scenario framework with source citations. Walk through each assumption individually.
- **Next step:** "Which specific assumption would you like to stress-test? Let me walk you through the sensitivity analysis."

---

## Universal Response Principles

1. **Never argue.** Acknowledge, reframe, evidence. Arguments create defensiveness.
2. **Never oversell.** The conservative scenario exists for a reason. Intellectual honesty builds trust faster than enthusiasm.
3. **Always advance.** Every objection response ends with a next step. Standing still = losing momentum.
4. **Use their language.** If they say "risico" (risk), use "risico." If they say "IRR," use "IRR." Mirror their vocabulary.
5. **Know when to walk away.** If a prospect isn't a fit (wrong geography, wrong scale, wrong timeline), say so honestly. Disqualifying non-fits fast protects DE's time and builds reputation.
