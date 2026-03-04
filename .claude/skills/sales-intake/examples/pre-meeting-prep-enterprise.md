# Pre-Meeting Prep: ABN AMRO

**Meeting:** 2025-04-10, 14:00, Microsoft Teams | **Attendees:** Thomas Kuijpers (CTO Office), Lisa Martens (Head of Cloud), Christian (DE)
**ICP:** C-ENT (Enterprise) | **Track:** Colocation

---

## Background (1 paragraph)

ABN AMRO is one of the three major Dutch banks (EUR 370B+ assets), headquartered in Amsterdam. Thomas Kuijpers from the CTO office reached out via LinkedIn after seeing a DE post about sovereign AI infrastructure. Lisa Martens, Head of Cloud Infrastructure, joined the conversation. ABN AMRO is running an internal evaluation of dedicated AI compute options as part of their "AI Factory" program -- an initiative to move from cloud-based ML experimentation to production AI workloads. They currently spend ~EUR 8M/year on Azure AI services and are evaluating whether dedicated infrastructure is more cost-effective and compliant for sensitive workloads (credit risk models, fraud detection, customer analytics). The bank has a board-level digital sovereignty policy adopted in 2024.

## Their Likely Priorities

1. **Data sovereignty and regulatory compliance** -- DNB (Dutch central bank) and ECB supervisory expectations around critical infrastructure. DORA (Digital Operational Resilience Act) compliance. They need to demonstrate control over AI infrastructure processing sensitive financial data.
2. **TCO vs Azure** -- The EUR 8M/year cloud spend is under scrutiny. Reserved instances are underutilized (~60% utilization). They want to understand if dedicated colo is cheaper for predictable, always-on workloads.
3. **Operational risk** -- They cannot afford downtime on production AI models (fraud detection runs 24/7). Will ask about redundancy, SLAs, and disaster recovery.

## Our Talking Points

1. **Lead with sovereignty:** "You've already decided data sovereignty matters -- your 2024 board policy confirms it. The question is execution. Dedicated AI infrastructure in the Netherlands gives you full control: your hardware, your jurisdiction, no third-party access. That's what DORA and DNB expect for critical workloads."

2. **TCO comparison:** "For always-on AI workloads, dedicated colo runs 40-60% below hyperscaler pricing over 3 years. Your EUR 8M Azure spend at 60% utilization means EUR 3-4M is wasted reserved capacity. We can model the exact savings for your workload profile."

3. **Operational reliability:** "Our facilities are designed for continuous AI operation -- redundant power, redundant cooling, N+1 on all critical systems. We can contractually guarantee [X]% uptime SLAs. Your fraud detection doesn't sleep, and neither does our infrastructure."

## Questions They Will Ask (and Our Answers)

| Likely Question | Prepared Answer |
|----------------|-----------------|
| "What's your Tier certification?" | "We design to Tier III+ reliability standards for AI workloads. Formal certification is in process, but the engineering is there. For banking, what matters is the contractual SLA and the redundancy architecture -- happy to walk through both." |
| "We're on Azure and it works. Why change?" | "Don't change everything. Keep Azure for general workloads and elastic demand. Move the predictable, sensitive AI workloads -- fraud detection, credit risk, customer analytics -- to dedicated infrastructure. Hybrid model, best of both." |
| "Our procurement requires references and a formal RFP." | "Understood. We can participate in your RFP process and provide technical documentation, site visits, and reference conversations. Happy to align with your procurement timeline." |
| "What about DORA compliance?" | "Dedicated infrastructure where you control the hardware and we provide the facility is simpler to evidence for DORA than public cloud. No multi-tenant risk, clear audit trail, Dutch jurisdiction throughout." |
| "Can you match Azure's managed services?" | "We provide the infrastructure layer: power, cooling, space, connectivity. For managed services (orchestration, monitoring), we can partner with managed service providers or your existing team manages it. This gives you more control, which aligns with your sovereignty goals." |

## Questions We Should Ask Them

1. **Workload specifics:** "Which AI workloads would you move first -- fraud detection, credit risk, customer analytics? What's the GPU/compute requirement for each?"
2. **Decision process:** "Beyond Thomas and Lisa, who else needs to sign off? Is this routed through group IT procurement or the CTO office directly?"
3. **Timeline:** "When does the AI Factory program need dedicated infrastructure operational? Are you in exploration or has budget been allocated?"
4. **Compliance specifics:** "Has DNB or your internal risk function expressed specific requirements about AI infrastructure hosting? Any specific certifications required?"
5. **Azure contract:** "When does your current Azure commitment renew? Is there flexibility to reduce the reserved instance commitment?"

## Collateral to Prepare

- [ ] TCO comparison deck: DE dedicated colo vs Azure reserved instances for AI workloads (`collateral-studio` -- enterprise TCO comparison)
- [ ] Enterprise capability brief: specs, SLAs, compliance features, connectivity (`collateral-studio` -- enterprise capability brief)
- [ ] DORA compliance positioning: one-pager on how dedicated colo supports DORA requirements (`collateral-studio` -- compliance brief)
- [ ] Facility overview: photos, layout, power architecture, cooling specs (if site visit isn't possible in first meeting)

## Meeting Objective

**Primary:** Get agreement to a technical deep-dive session with Lisa's infrastructure team + DE engineering, where we model the specific workloads and TCO.

**Fallback:** If they're earlier stage than expected, get clarity on their decision timeline and evaluation criteria, and agree on what information they need to advance internally.
