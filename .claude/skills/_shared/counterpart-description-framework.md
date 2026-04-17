# Counterparty Description Framework — Recital B Methodology

**Purpose:** Produce an institutional-grade, lender-readable counterparty description (Recital B) in every LOI produced by `legal-assistant`.

**Shared across** all five LOI types: End User (EU), Distributor (DS), Wholesale (WS), Strategic Supplier (SS), Ecosystem Partnership (EP).

**Target output:** 3–5 sentences, 80–150 words, single paragraph, no bullet lists, no jargon without gloss, no salesy adjectives, every material claim source-attributable.

---

## The 3 lender / investor questions

Every Recital B must implicitly answer these, in order:

1. **Is this counterparty serious and solvent?** — identity, scale, track record
2. **Does the relationship make commercial sense?** — strategic fit, synergy logic
3. **What's the bankable signal?** — material proof points (revenue, deployed capacity, customer base, institutional credentials, pipeline)

When a bank or institutional investor reads the LOI in a data room, these are the three things they are asking. Everything else is decoration.

---

## The 5 content pillars

Every Recital B is built from these five pillars, in this order. Pillars 1–4 are mandatory. Pillar 5 is conditional.

| # | Pillar | Content | Answers Q |
|---|---|---|---|
| 1 | Identity & Scale | Legal entity, HQ, operating geography, years operating, ownership/funding status | 1 |
| 2 | Core business & positioning | What they do operationally, who their customers/users are | 1, 2 |
| 3 | Track record & proof points | Concrete, verifiable metrics: customers served, deployed capacity, revenue/ARR, partnerships, deployments | 3 |
| 4 | Strategic fit with Provider | One sentence on why this relationship exists commercially | 2 |
| 5 | Forward plans (optional) | Only if material to motivating the LOI: pipeline, expansion, strategic intent | 2, 3 |

**Structural test:** if you remove any of pillars 1–4 and the paragraph still answers the 3 lender questions, the pillar was redundant. Cut it.

---

## Source-capture protocol (Phase 3 of SOP)

Before drafting Recital B, gather facts from as many of these sources as are available. Sources are additive: use what exists, skip what doesn't. Do not hallucinate. If a pillar cannot be sourced, surface the gap to the user.

| # | Source | What to extract | Tool |
|---|---|---|---|
| 1 | **Website** | About, products/services, customers, leadership, news, technical specs | WebFetch |
| 2 | **HubSpot** | Company properties, associated deals, engagement log, deal description | MCP (HubSpot) |
| 3 | **ClickUp** | Associated tasks, project docs, relationship notes | MCP (ClickUp) |
| 4 | **LinkedIn** | Headcount band, HQ, description, recent posts | WebFetch |
| 5 | **Press / news** | Recent coverage, funding announcements, customer wins (last 18 months) | WebSearch |
| 6 | **Email threads / Fireflies** | User-specified threads or meetings | Read (user path) |
| 7 | **KVK / Companies House** | Legal entity form, registration number, registered address | WebFetch (for NL / UK) |
| 8 | **Deck / press kit** | User-provided file | Read |

**Source-attribution rule:** for every material claim in the draft Recital B, internally tag the source. Present the source map to the user at the Recital B review gate (Phase 5).

Example internal tagging:
```
Pillar 1: "Croatia-based GPU cloud, operating since 2023" → [website /about], [LinkedIn]
Pillar 3: "300,000+ GPUs deployed globally" → [website /capacity], [press: Reuters 2025-11]
```

---

## Per-type tuning

Different LOI types emphasise different facets of the 5 pillars.

### End User (EU)

Emphasise: customer base size, workload profile, compliance needs.

> [Counterparty] is a Netherlands-based AI startup developing compliance-focused large language models for the European legal and financial services markets. The company operates from Amsterdam, has raised Series A funding, and currently serves over 20 enterprise customers across banking, insurance, and legal sectors. Its inference workloads require high-density GPU capacity with EU data residency. The Counterparty is seeking sovereign AI colocation to support production deployment of its models and planned expansion across the Benelux.

### Distributor (DS)

Emphasise: channel reach, relationship network, pipeline-level commitment.

> [Counterparty] is a Netherlands-based independent datacenter brokerage and infrastructure consultancy, operating since 2014 under Aldewereld Consultancy. The firm maintains direct commercial relationships with CISOs across more than 150 Dutch enterprise customers, operates as an independent internet service provider (AS30409) with carrier-grade fibre procurement, and is positioning its service to originate wholesale GPU capacity demand for European cloud providers at the scale of Hetzner and OVHcloud. The relationship is intended to provide a qualified channel path to Dutch enterprise, cloud-provider, and sovereign end-user demand, delivered through the Provider's DEC platform.

### Wholesale (WS)

Emphasise: deployed capacity, buyer base, geographic operations.

> [Counterparty] is a GPU cloud infrastructure provider, operating under CUDO Ventures Ltd (UK Company No. 11065412), and is an NVIDIA Preferred Partner with Enterprise Reference Architecture validation. The company designs, commissions, and operates production AI infrastructure for enterprise and neocloud customers, with a deployed base in excess of 300,000 GPUs across facilities in the United Kingdom, European Union, North America, Asia-Pacific, and the Middle East. The Counterparty targets over 250 MW of contracted capacity by end of 2026, with a stated pipeline exceeding 750 MW by end of 2027 across exclusive European sites.

### Strategic Supplier (SS)

Emphasise: manufacturing / engineering track record, delivered projects, capability scale.

> [Counterparty] is a global digital-infrastructure company specialising in the design, off-site manufacturing, and rapid deployment of modular data-centre solutions for high-density AI and accelerated compute workloads. The company operates from London, Dublin, Cluj, and Houston, with an active project portfolio exceeding 60 MW of delivered and contracted capacity. Its modular design targets 80% off-site completion and a Ready-for-Service target of 90 days or less from site-preparation completion. The relationship is intended to integrate modular DEC delivery capability with the Provider's site portfolio, reducing time-to-capacity on the Provider's active development pipeline.

### Ecosystem Partnership (EP)

Emphasise: mission, constituency, track record of published / convened work.

> [Counterparty] is a European research consortium operating under [governance form] and hosted by [institution], convening [N] institutions across [N] member states on AI infrastructure sovereignty, energy-efficient compute, and sustainable datacentre design. The consortium has published [N] peer-reviewed papers and convened [N] working groups on federated AI infrastructure since [year]. The relationship is intended to support joint thought-leadership on sovereign AI infrastructure in the European Union and co-ordinated contribution to emerging EU compute-infrastructure standards.

---

## Consortium / federation special case

When the counterparty is a consortium, federation, alliance, or similarly composite entity (e.g., SAG Sovereign AI-Grid Consortium), **do not try to describe every participant**. Apply these rules:

1. **Describe the coordinating entity** (the legal entity that is signing), not every member.
2. **Name the consortium's commercial purpose** in one sentence.
3. **Anchor credibility to the lead's track record** — the track record of the coordinating entity and its principal(s), not the sum of every member's credentials.
4. **List member categories if helpful** ("across 8 utility companies and 3 research institutions"), not member names.
5. **Include governance form briefly** if it affects signing authority (steward-ownership, cooperative, SPV). Do not embed the governance model as prose unless legally relevant.
6. **Avoid jargon without gloss**: translate Dutch / EU governance terms into English approximations on first use, e.g., `centrale knooppunt` → "coordinating entity", `Article 12b` → "EuroHPC hosting framework under Article 12b of Regulation (EU) 2021/1173".

**Before / after example (SAG Man-of-Solutions):**

❌ **Before** (current v3.1 output):
> "Man of Solutions (the 'Partner') is the coordinating entity (centrale knooppunt) of the Sovereign AI-Grid Consortium, a federated sovereign AI infrastructure initiative operating within the EuroHPC AI Gigafactory ecosystem across the Netherlands, Belgium, and Germany under a steward-ownership public-good governance model, structured as a multi-site Article 12b architecture with an ecosystem of energy, supply-chain, and engineering partners, and pursued through private-capital and programme funding pathways. The Consortium has identified Digital Energy Group AG on its public consortium roster as the strategic compute-infrastructure partner of the initiative. The Partner's Managing Director holds active institutional relationships across the Dutch Ministry of Economic Affairs and Climate Policy, the Netherlands Enterprise Agency, and the EuroHPC Joint Undertaking in the Netherlands, Belgium, and Germany; direct commercial relationships with CISOs across the Dutch top 500 enterprise market; deep roots in the European Linux and open-source infrastructure community built over years of direct technical engagement; independent internet service provider operations; and a demonstrated track record of successful datacentre capacity fulfilment for enterprise customers across European markets through targeted digital acquisition and performance marketing."
> (194 words, jargon-heavy, demand-side and supply-side credentials conflated, no sourcing anchor.)

✅ **After** (v3.2 framework applied):
> "Man of Solutions B.V. (the 'Partner') is the coordinating entity of the Sovereign AI-Grid Consortium, a Netherlands-Belgium-Germany federation convened under the EuroHPC hosting framework to coordinate sovereign AI infrastructure for European institutional and public-sector users. The consortium brings together energy, supply-chain, and engineering partners under a steward-ownership governance model, with the Provider named as strategic compute-infrastructure partner on the consortium's public roster. The Partner's Managing Director has established relationships across the Dutch Ministry of Economic Affairs and Climate Policy, the Netherlands Enterprise Agency, and the EuroHPC Joint Undertaking, and a track record of datacentre capacity origination across the European enterprise market. The relationship is intended to provide a federated institutional pathway to sovereign AI capacity on the Provider's platform."
> (125 words, pillar structure applied, jargon glossed, demand side only — supply-side credentials moved out.)

---

## Anti-patterns (enforced by linter)

| Anti-pattern | Why | Rule |
|---|---|---|
| Certification checklists unless materially relevant | ISO 27001 etc. are rarely material to a DE LOI; they clutter and dilute real signal | R-11 (warn) |
| Untranslated jargon without gloss (`centrale knooppunt`, `Article 12b architecture`) | Reader-hostile; undermines credibility | — (reviewer gate) |
| Salesy adjectives (`leading`, `innovative`, `cutting-edge`, `world-class`, `best-in-class`) | Lender discount factor | R-14 (warn) |
| `positioning (its\|itself) as` | Formulaic, weak | R-15 (warn) |
| Unsourced scale claims (`150+ customers` with no source pattern) | Not verifiable, not bankable | — (reviewer gate) |
| Stacked sub-clauses | Reads as pitch deck, not institutional prose | R-13 (warn: >1 parenthetical per sentence) |
| Mixing demand-side and supply-side credentials when only one is relevant | Indicates the writer didn't decide what story to tell | — (reviewer gate) |
| Word count outside 60–180 | Too short = unfinished; too long = unfiltered | R-12 (warn) |

Full rule catalogue: `_shared/loi-qa-gate.md`.

---

## Worked examples from the 2026-04 LOI review

### ✅ Good — Aldewereld (Distributor)

The Aldewereld Recital B is the reference standard: structured, credentialed, lender-anchored. Opens with identity, moves to operational facts (AS30409, carrier-grade fibre), scales to credibility signal (150+ CISOs, VU Amsterdam StartHub ambassador role), and closes with strategic intent (Hetzner / OVHcloud-scale wholesale originator). Each claim is source-attributable.

One edit for v3.2: trim the second half. The ~350-word paragraph can be compressed to ~150 without losing any signal by consolidating the credential list and removing the restatement of target segments (which belong in Cl. 3).

### ❌ Bad → ✅ Fixed — SAG Man-of-Solutions (Distributor, consortium)

See "Consortium / federation special case" above for the before/after.

### ✅ Good — InfraPartners (Strategic Supplier)

The InfraPartners Recital B is a clean one-sentence supply-side executive summary: "global digital infrastructure company specialising in the design, off-site manufacturing, and rapid deployment of fully modular data centre solutions … with operations spanning London, Dublin, Cluj, and Houston, and an active project portfolio including engagements exceeding 60 MW." Strategic fit statement can be added explicitly (pillar 4) to make the commercial logic fully explicit.

### ✅ Good-but-trim — Cudo Compute (Wholesale)

The Cudo Recital B has the right structure but is padded. Strip:
- ISO 27001 facility list (not material to a DE colocation LOI)
- Full OEM partner list (Dell, Lenovo, Supermicro, HPE, CBRE, NetApp, Red Hat — one sentence summary is enough)
- Repetition between "operating across [regions]" and "United Kingdom, European Union, North America, Asia-Pacific, and the Middle East"

Keep:
- NVIDIA Preferred Partner + Enterprise Reference Architecture validation (lender-relevant signal)
- 300,000+ GPUs deployed (scale proof point)
- 250 MW contracted / 750 MW pipeline target (forward plan, material to motivating the LOI)

Target word count after trim: ~110 words.

---

## Workflow integration

In `SKILL.md` Phase 3 (Source Capture) and Phase 5 (Recital B Draft):

1. Skill runs source-capture protocol (Phase 3 sources 1–8), tagging each fact to its source.
2. Skill drafts Recital B using the 5-pillar structure, type-tuned for the LOI type.
3. Skill applies anti-pattern linter to the draft before presenting.
4. Skill presents draft + source map to user (Phase 5).
5. User accepts, requests specific edits, or rewrites. Iterate until accepted.
6. Accepted Recital B is embedded in YAML intake under `counterparty.description`.
7. Generator re-runs anti-pattern linter at build time.

---

## What this framework does NOT do

- Does not write Recitals C or D (template-fixed per LOI type).
- Does not write bespoke Cl. 3.1 / 3.2 for Distributor Mode A (see `ASSEMBLY_GUIDE.md` § Bespoke Language Guide).
- Does not write counterparty description for non-LOI documents (MSAs, SOWs, MIAs) — those have separate guidance.
- Does not do legal due diligence on counterparty solvency. It documents what is public; it does not verify. If verification is needed, escalate to `legal-counsel`.
