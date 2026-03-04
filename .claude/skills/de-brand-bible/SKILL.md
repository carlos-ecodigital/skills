---
name: de-brand-bible
description: >-
  Shared brand foundation for all Digital Energy marketing skills. Contains
  brand identity, tone of voice, messaging pillars, six buyer personas (growers,
  district heating, industrial heat, neoclouds, enterprises, institutions),
  quantified proof points, competitive positioning, and sanitized deal economics.
  This skill is referenced by marketing-strategist, positioning-expert,
  content-engine, and collateral-studio. It is not typically invoked directly
  but provides the authoritative source of truth for all external-facing
  marketing content produced by any marketing skill.
---

# Digital Energy -- Brand Bible

## Personality

See [identity.md](identity.md), [soul.md](soul.md), [principles.md](principles.md) for this agent's personality definition.

Shared foundation referenced by all marketing skills. All external content must be consistent with this brand bible. When producing any marketing deliverable, read the relevant reference files below before drafting.

## Brand Overview

**Entity:** Digital Energy Group AG (Zug, Switzerland) operating through Dutch project BVs.

**One-sentence positioning:** Digital Energy co-locates Digital Energy Centers (DECs) on Dutch industrial and agricultural sites, recycling 100% of compute energy into usable heat and turning grid scarcity into competitive advantage.

**Category:** Vertically integrated sovereign AI infrastructure developer — digital cogeneration platform. Not a traditional data center operator, not an energy company, but the intersection.

## Messaging Pillars

Five operating principles — industrial logic, not marketing slogans. See `references/brand-identity.md` for full pillar detail and audience hierarchy.

| # | Pillar | Core Principle | Proof Domain |
|---|---|---|---|
| 1 | **Multi-use infrastructure** | Every resource serves multiple purposes simultaneously. Digital cogeneration (CHC): compute + heat from one energy input. Cable pooling: BESS + DC + heat on one connection. | Cable pooling (Energiewet 2026), 3 revenue streams per site, EUR 0 CAPEX/OPEX for grower, freed CHP/e-boiler assets for grid balancing |
| 2 | **Maximum utilization of underutilized assets** | Find stranded resources. Activate them. Oversized grower connections, retiring coal infrastructure, agricultural land zoning. | 14 sites secured (existing grid), 60 GW queue vs 20 GW peak, permitting by design (6-14 months), Amsterdam moratorium to 2030 |
| 3 | **Sovereign European AI** | European compute on European soil, by European partners. Sovereignty by architecture, not contract clause. | Dutch BV per project, Lenovo/Nokia consortium, NVIDIA-native, 14+ sovereign sites, EU AI Act compliance |
| 4 | **Flexible IT loads on an open grid** | DECs are active grid participants, not passive consumers. BESS + demand response + workload flexibility. "Energy maker, not taker." | BESS JV (25.5 MW / 51 MWh), revenue stacking (arbitrage + FCR + aFRR), 423 negative price hours H1 2025, BESS 12-15% equity IRR |
| 5 | **Decentralized energy infrastructure for distributed intelligence** | 4.2 MW modular blocks, deployable anywhere there's grid + thermal demand. The Super-Factory: a distributed network of DECs as unified AI infrastructure. | 4.2 MW modular block, 6-14 months deployment, 14 sites distributed, AMS-IX proximity (sub-2ms), "manufactured not constructed" |

## Tone of Voice

The brand voice is defined across focused reference files. See `_retrieval-rules.yaml` for task-specific loading rules.

| File | What It Covers |
|---|---|
| [references/brand-identity.md](references/brand-identity.md) | Mission, vision, values (brand foundation) |
| [references/voice-rules.md](references/voice-rules.md) | 5 general tone principles |
| [references/banned-phrases.md](references/banned-phrases.md) | 12 banned phrases with replacements |
| [references/channel-adaptations.md](references/channel-adaptations.md) | 8 channel-specific tone adjustments |
| [references/terminology-standards.md](references/terminology-standards.md) | 18 preferred terms, naming rules, framing rules, visual identity notes |
| [references/language-policy.md](references/language-policy.md) | Audience-language pairings (NL/EN) |

**In brief:**
- **Precise over promotional.** Use numbers, not adjectives. "25.5 MW utility grid connection" not "massive grid capacity."
- **Technical confidence.** We know Dutch energy regulation, project finance, and AI infrastructure. Show it through specificity.
- **Honest about uncertainty.** Use "indicative," "subject to," "base case" where appropriate. Sophisticated buyers respect intellectual honesty.
- **Bilingual where needed.** Dutch/English for grower-facing content. English-primary for institutional and neocloud audiences.
- **No buzzwords.** Ban: "game-changing," "revolutionary," "cutting-edge," "synergy," "leverage" (as verb), "unlock potential."

## Buyer Personas

Six buyer segments, each with distinct pain points, decision processes, and preferred channels. See [references/buyer-personas.md](references/buyer-personas.md) for full profiles.

| Persona | Who They Are | What They Want | How They Buy |
|---|---|---|---|
| **Grower** | Dutch greenhouse BV owner/director | Lower energy costs, heat security, future-proofing | Referral → LTO event → Portal signup → LOI → HoT |
| **District Heating Utility** | Municipal/regional warmtenet operator (e.g., Ennaturlijk) | Cost-based heat source, regulatory compliance (Wcw), volume | RFP/direct engagement → Technical assessment → Board approval |
| **Industrial Heat Buyer** | Manufacturing/food processing plant manager | Process heat, cost reduction, sustainability reporting | Direct BD → Site assessment → Procurement → Contract |
| **Neocloud** | GPU cloud provider (Lambda, CoreWeave, Crusoe type) | Affordable MW, low PUE, speed to deploy, European sovereign | Conference/referral → Technical due diligence → LOI → MSA |
| **Enterprise** | CTO/VP Infra at large corporate | Dedicated AI compute, data sovereignty, ESG alignment | Analyst report → RFP → Proof of concept → Contract |
| **Institution** | University/research center IT director | Research compute, sustainability goals, cost efficiency | Grant-funded → Procurement → Multi-year agreement |

## Proof Points

See [references/proof-points.md](references/proof-points.md) for the full library of quantified claims with sources.

## Competitive Positioning

See [references/competitive-positioning.md](references/competitive-positioning.md) for DE vs. alternatives analysis per buyer segment.

## Deal Economics

See [references/deal-economics.md](references/deal-economics.md) for sanitized economics suitable for external use.

## Cross-References

- For market data, regulatory context, and financial benchmarks: see `project-financing/` skill and its references
- For contract structures and terms: see `drafting-service-agreements/` skill
- For Dutch tax implications in marketing materials: see `project-financing/references/netherlands-legal-framework.md`

## Usage by Other Skills

When any marketing skill (marketing-strategist, content-engine, collateral-studio, positioning-expert) produces content:
1. **Consult `_retrieval-rules.yaml`** to identify which chunks to load for the task type
2. Load `always_load` chunks and evaluate `load_if_relevant` based on context
3. Stay within the `token_budget` for brand context
4. Read the relevant buyer persona from `references/buyer-personas.md`
5. Check proof points in `references/proof-points.md` before making quantified claims
6. Follow tone of voice rules from `references/voice-rules.md`
7. Check banned phrases in `references/banned-phrases.md`
8. Use competitive framing from `references/competitive-positioning.md`
9. Reference deal economics from `references/deal-economics.md` for financial claims

Never fabricate statistics. If a number isn't in the proof points library or the project-financing skill references, don't use it.
