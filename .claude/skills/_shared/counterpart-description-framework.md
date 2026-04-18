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

## The Signal Test (v3.5.2 — supersedes topic-based filtering)

**Why this supersedes v3.4 topic filtering**: topic-based allow/deny lists over-exclude valid signal (a NeoCloud with a named hyperscaler as strategic investor — fundraising content that IS signal) and under-exclude noise (a Fortune-500 customer count "serves 500+ enterprises" — customer content that is NOT signal because it's unattributed). The real filter is on **signal quality**, not topic.

### Definition

A **signal** is a third-party-testable operational fact whose attached identity carries endorsement weight. A signal passes ALL THREE gates below. Claims that fail any gate are noise — strip.

### Gate 1 — Attribution

> Is the claim attached to a named, verifiable third party whose identity a lender would recognize as operationally endorsing?

| Passes gate 1 | Fails gate 1 |
|---|---|
| "majority-owned by Euronext-listed SWI Stoneweg Icona" | "EUR 0.5bn valuation" (no endorsing 3rd party) |
| "backed by senior infrastructure financing from Macquarie" | "raised $150M in Series C" (generic, no endorsing investor named) |
| "supports Microsoft Azure's enterprise cloud" | "serves Fortune 500 clients" (class-level, untestable) |
| "NVIDIA Cloud Partner deploying GB200 NVL72" | "industry-leading AI platform" (self-slogan) |
| "co-developed with BMW, Bosch, and Siemens" | "150+ enterprise customers" (unattributed count) |

### Gate 2 — Operational relevance

> Does the attached identity speak to solvency/seriousness (Q1), commercial-fit logic (Q2), or bankable third-party validation (Q3)?

| Passes gate 2 | Fails gate 2 |
|---|---|
| "Macquarie senior debt" → Macquarie ran operational DD | "Twitter-followed by 20k" (social metric, not operational) |
| "OpenAI customer" → marquee platform vetting | "won 2023 AI Startup of the Year" (awards — reputational not operational) |
| "EuroHPC JU framework participant" → public-sector credentialling | "listed in Gartner Magic Quadrant" (analyst placement — tier-3) |

### Gate 3 — Freshness / health

> Is the attached third party currently operational, solvent, and in an undistressed relationship with the counterparty?

**Gate 3 fires only when:**
1. The **primary counterparty itself** is in distress (bankruptcy, regulatory enforcement, dissolution proceedings) — disclose factually or drop the claim; or
2. An **attached third party's distress is operationally material to the counterparty** (wholly-dependent financing where parent is in default; currently-relied-upon credentials that have been revoked; active litigation between counterparty and named endorser)
3. Signals > 24 months old without public continuation (stale contracts without renewal)

**Gate 3 does NOT fire** when an attached party is merely undergoing unrelated restructuring / management change / stock-price decline / quarterly miss. Arm's-length attached-party distress = no commentary. Recital B is a factual introduction, not a risk memo; lender DD reaches attached parties independently; volunteering distress commentary undermines the LOI.

### Writer discipline rule (runs BEFORE the signal test)

For every named third party in the draft, the writer must point to a specific tier-1 source in `counterparty.source_map` establishing the current relationship. If the name "feels right" but can't be tier-1-attributed, it is a **fabrication — even if the named party is real and plausible**. Brand recognition compounds fabrication cost; it does not reduce it.

**Real failure pattern** (v3.5 development): "Cohere" proposed as a CoreWeave customer from memory without tier-1 source — Cohere's public compute partnerships are GCP/Oracle, not CoreWeave. Fix: only name what you can attribute.

### Fundraising-specific rule (corrects v3.4 crude exclusion)

| Financial claim | Signal? | Reasoning |
|---|---|---|
| "EUR 117m senior financing from Macquarie" | **Signal** (gates 1+2 pass) | Macquarie's infra-credit team ran operational DD; third-party credit validation |
| "strategic investment from NVIDIA" | **Signal** | Platform-partner endorsement |
| "backed by SWI Stoneweg Icona (Euronext-listed)" | **Signal** | Listed-entity control + implicit credit backstop |
| "EUR 0.5bn valuation" | Noise | No endorsing 3rd party attached; investor-pitch vanity |
| "Series B from Accel" | Noise | Generic VC-round label; Accel identity does not carry operational endorsement for DE's colocation relationship |
| "raised $150M" | Noise | Unattributed; no investor named |

**Rule**: fundraising content passes the signal test only when a named endorsing third party is attached (strategic investor identity, infra-credit lender). "Raised at valuation X" alone is vanity; "backed by Macquarie" is signal. Same capital, different signal attribution.

### Customer-specific rule

| Customer claim | Signal? |
|---|---|
| "supports Microsoft Azure" | **Signal** — named hyperscaler |
| "supports Deutsche Telekom Industrial AI Cloud" | **Signal** — named marquee enterprise customer |
| "serves Fortune 500 clients" | Noise — class-level, untestable |
| "150+ customers" | Noise — unattributed count |
| "supports a leading US hyperscaler" | Noise — anonymized; un-nameable = un-signal-able |

**NDA-bound customers**: if the best customer cannot be named due to NDA, **do not anonymize — omit**. The value-prop goes in Cl. 3 as a Customer statement, not Recital B as an endorsement.

### Ownership-specific rule

Name the controlling shareholder in one clause in S1 only when at least one trigger fires:
- (a) publicly listed
- (b) sovereign fund or state-owned
- (c) acquired within past 24 months (continuity/CoC risk)
- (d) materially relevant to LOI positioning (sovereignty, FDI review, regulated sector)

Valuation, debt facility size, and growth-commitment numbers do NOT go in Recital B — those are investor-pitch metrics, not operational evidence.

### Enforcement

- **R-24 (fail)**: inline bracket citation (`[polarise.eu]`) in `counterparty.description` field. Source attribution lives in `source_map` YAML; NEVER in prose.
- **R-25 (fail)**: vanity-financial pattern (valuation of / raised $X at $Y / generic Series-X labels) in Recital B. Named-endorser financing (e.g. "backed by Macquarie") passes because the regex requires vanity patterns.
- **R-27 (fail)**: `[TBC]` rendered literally in sig-block Name/Title — must route through `_render_placeholder` so the line becomes a fillable blank.
- **R-28 (warn)**: `[TBC]` count exceeds 5 body-wide — intake likely incomplete; consider Phase 4/5 revision before external delivery.

---

## Tier Hierarchy Policy (v3.4)

Every material factual claim in Recital B must be grounded in a source of an appropriate tier. Source tier determines whether the claim can be cited directly, requires a qualifier, or must be excluded.

### Tier 1 — citable without qualifier

- Counterparty's **own website** (company-controlled domain, not re-hosted content)
- **Official registry** — KVK (NL), Companies House (UK/IE), SEC EDGAR (US), Handelsregister (DE), Registre du Commerce (FR/CH), Crunchbase company self-entries on paid tier
- **Direct-quoted press** in which the counterparty is the named speaker (CEO quote, official company statement on counterparty's own press release)
- Counterparty's **own press releases** hosted on counterparty's domain or a co-branded joint release (Provider + counterparty)

Tier-1 sources can be cited in Recital B as if the counterparty itself said it — because, in substance, the counterparty did.

### Tier 2 — citable only with "as publicly reported" qualifier

- **Third-party financial press**: FT, Reuters, Bloomberg, WSJ, DCD (Data Center Dynamics), Structure Research, TechCrunch, The Register, Business Insider
- **Industry research reports**: Gartner, Forrester, Omdia, IDC, 451 Research
- **Investor-facing databases**: Crunchbase free tier, PitchBook, Preqin non-paywall summaries

Any tier-2-sourced claim must be framed in Recital B with a qualifier: *"as publicly reported by [source]"* or *"reportedly"* or *"according to [source]"*. The Provider is not asserting the fact; the Provider is recording that a third-party source publicly reported it. This is a material legal distinction — lender relies on the counterparty's own statements, not on Provider's judgement of third-party accuracy.

### Tier 3 — NOT citable in Recital B

- **Analyst commentary** (single analyst's opinion on counterparty, unattributed industry speculation)
- **Blog posts** (including technical blogs, think pieces, Medium articles)
- **AI-generated content** (LLM summaries, AI-synthesised reports, auto-generated company profiles)
- **Unattributed industry gossip** ("I heard X", "people say X")

Tier-3 material must never appear in Recital B, even with qualifier. If the only source for a claim is tier-3, treat the claim as unsourced and mark `[TBC]` or omit.

### Tier application rule

**If a claim cannot be supported by a tier-1 or tier-2 source, it must be (a) omitted, or (b) marked `[TBC]` (to be confirmed by counterparty in follow-up correspondence).** Recital B is for verifiable facts only. The Provider does not make up facts about the counterparty, even plausible-sounding ones.

---

## Fabrication Gate (v3.4 — enforced by QA linter R-23)

### Rule

Every material factual claim in Recital B — specifically, claims containing numeric scale / metric language — must be backed by:

- a **tier-1 source URL** attached in the intake YAML via `counterparty.source_map`, pillar-keyed; OR
- an explicit `[TBC]` marker indicating the fact is to be confirmed before execution; OR
- an explicit `--source-override "PILLAR_N '[reason]'"` CLI flag invoked at generation time (recorded in the QA report for audit)

### What counts as a material numeric claim (triggers R-23)

The QA linter enforces on any Recital B substring matching: `\b\d+\s*(MW|GW|customers|clients|sites|deployments|GPUs|operations|offices|countries|years|employees|%)\b`

Examples that trigger the gate:
- "300,000 GPUs deployed"
- "150+ customers"
- "60 MW pipeline"
- "operations across 4 countries"
- "80% off-site completion"

### YAML intake shape

```yaml
counterparty:
  description: "..."  # the Recital B prose
  source_map:
    pillar_1:  # identity & scale
      - "https://counterparty.com/about"
      - "https://companyhouse.de/..."
    pillar_2:  # core business
      - "https://counterparty.com/products"
    pillar_3:  # track record / proof points
      - "https://counterparty.com/customers"
      - "https://reuters.com/2025-11/counterparty-funding"  # tier-2, add as publicly reported qualifier in prose
    pillar_4: "inferred from Phase 1 context"  # strategic fit is usually inferred
    pillar_5: "[TBC]"  # forward plans; ok to defer
```

### Override path

If user obtained a fact from a private source (e.g., in-meeting statement from counterparty not yet published), pass `--source-override "pillar_3 'Counterparty CTO confirmed in meeting 2026-04-16; to be re-confirmed in Definitive Documentation'"` at generation time. Override + reason is recorded in the QA report for audit.

### Tier-2 mandatory qualifier

If a source_map entry points to a tier-2 URL (e.g., Reuters, DCD, TechCrunch), the corresponding claim in Recital B **must** include an "as publicly reported" / "reportedly" / "according to" qualifier. Linter R-23 doesn't differentiate tier-1 from tier-2 at URL level (both are "URL present"), so this is enforced by reviewer in Phase 7.5 legal-counsel handoff.

### Critical anti-pattern — tier-2 treated as tier-1

A common failure (observed in the v3.3 InfraPartners and SAG worked examples before correction): cite tier-2 press coverage as if it were the counterparty's own statement. Example:

❌ **BAD** (v3.3 InfraPartners draft): "InfraPartners delivers 80% off-site completion" — claim sourced from AInvest article, not from infrapartners.llc.
✅ **GOOD** (v3.4 corrected): "InfraPartners, as publicly reported, targets 80% off-site completion [AInvest, 2025-06]" — qualifier reflects the actual source quality.

This distinction is material: a lender reading an LOI expects the counterparty to have said what the Recital B claims; if the claim came from a third-party analyst article, the lender has a different risk assessment.

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

## Worked examples — verified real counterparties (v3.4)

v3.4 replaces synthetic / partially-verified v3.2–v3.3 examples with four verified real counterparties. Every claim below is traceable to a tier-1 source (counterparty's own website + official registry + direct-quoted press). Corrections marked where v3.3 drafts contained fabrication.

### Tier-2 qualifier pattern (v3.5.3-cont scope H — reference pattern, no live counterparty)

When a material claim is only verifiable via tier-2 press (FT / Reuters / Bloomberg / DCD / Structure Research / etc.) and is **not** corroborated on the counterparty's own tier-1 channels, the claim is still citable — but the Recital B wording must carry a publisher-attributed qualifier, and the `source_map` entry must encode the tier explicitly so QA can validate the pairing.

**Pattern in Recital B prose** (always the counterparty + "as publicly reported by [Publisher]" or "according to [Publisher]"):

> *"As publicly reported by [Structure Research], [Counterparty] has deployed more than 8,000 GPUs across its Nordic facilities."*

> *"According to [Financial Times], [Counterparty] has signed framework agreements with two European sovereign funds."*

> *"[Counterparty] has reportedly secured 40 MW of grid capacity in Dublin (as reported by [Data Center Dynamics])."*

**Pattern in `source_map` YAML** (new v3.5.x schema — when a pillar value is a dict rather than a bare URL, the entry carries `tier` + `qualifier` fields so the QA linter can validate that the Recital B prose contains the matching qualifier phrase next to the claim):

```yaml
counterparty:
  source_map:
    pillar_3:
      # Tier-1 primary: counterparty's own newsroom confirmation
      - "https://counterparty.example/newsroom/partnership-announcement"
      # Tier-2 supplementary: third-party press, only citable with qualifier
      - url: "https://www.structureresearch.net/2025/11/counterparty-nordic-expansion/"
        tier: 2
        qualifier: "as publicly reported by Structure Research"
```

**Rule** (enforced by the Signal Test, documented in v3.5.x plan; future v3.6 tier-qualifier QA rule will grep Recital B prose for the qualifier phrase adjacent to the claim):

- Tier-1 claim → bare URL in `source_map` pillar; Recital B wording asserts the fact directly.
- Tier-2 claim → dict entry with `tier: 2` + `qualifier` string; Recital B wording prepends / embeds the publisher-attributed qualifier. Provider never asserts tier-2 content as its own judgement.
- Tier-2-only claims that **cannot** be corroborated with at least one tier-1 source in the same pillar must be **omitted** — tier-2 press is supplementary to tier-1, never a substitute.
- Publisher identity matters: reputable tier-2 outlets (FT, Reuters, Bloomberg, DCD, Structure Research) carry different weight than aggregators or paywalled summaries — the qualifier names the outlet so the lender can apply their own weighting.

**Why a reference pattern instead of a live counterparty**: the four live examples below are all tier-1-fully-verified. Inventing a tier-2 example against a real entity would introduce fabrication risk. The pattern is shown abstractly so writers recognize the shape; when a real counterparty requires tier-2 citation, the writer substitutes the real URL + publisher into the pattern.

---

### ✅ Polarise GmbH (Wholesale — fully verified)

**Source map (tier-1 unless noted):**
- Pillar 1: [polarise.eu/about](https://polarise.eu/about), [Companyhouse.de Polarise GmbH Paderborn](https://www.companyhouse.de/en/Polarise-GmbH-Paderborn)
- Pillar 2: [polarise.eu](https://polarise.eu) (product taxonomy: AI Factories, bare-metal GPU, Virtual AI Cloud Core, Dedicated Private Cloud, AI Studio Drive)
- Pillar 3: [polarise.eu/newsroom/deutsche-telekom-industrial-ai-cloud](https://polarise.eu/newsroom) (Deutsche Telekom Munich anchor customer), [polarise.eu NVIDIA Cloud Partner page](https://polarise.eu) (GB200 NVL72, GB300 NVL72), [swi.com press release](https://swi.com) (SWI Stoneweg Icona majority investment, EUR 0.5bn valuation, EUR 1.0bn growth commitment — tier-1: investor-facing direct-quoted release)
- Pillar 4: inferred from Phase 1 context (European sovereign AI wholesale demand)
- Pillar 5: [polarise.eu/sites/augsburg](https://polarise.eu) (announced 30 MW, scalable to 120 MW Augsburg expansion)

**Draft Recital B (146 words):**
> Polarise GmbH is a German limited liability company with its registered seat at Technologiepark 12, 33100 Paderborn, Germany [Companyhouse.de]. Polarise operates AI-ready data centers and a sovereign GPU cloud platform under the "Europe's Gateway for Sovereign AI" positioning, with sites in Munich, Oslo, and Frankfurt and an announced expansion of 30 MW (scalable to 120 MW) in the Augsburg area [polarise.eu]. Polarise is a Preferred NVIDIA Partner and NVIDIA Cloud Partner deploying GB200/GB300 NVL72 platforms, and supports Deutsche Telekom's Industrial AI Cloud in Munich [polarise.eu/newsroom]. In 2026 SWI Stoneweg Icona Group (Euronext Amsterdam) acquired a majority stake at a EUR 0.5bn valuation with a EUR 1.0bn growth commitment, and Macquarie has committed up to EUR 117m in senior financing [swi.com; polarise.eu/newsroom].

**Why this example works:** every material claim has a tier-1 URL. Scale signals (funding, partnerships, deployed platforms) are attributed to direct-quoted press from Polarise's own newsroom or the investor's own release. Forward plans (Augsburg 30 MW → 120 MW) are on Polarise's own site. Registration number placeholder is [Companyhouse.de]; full HRB can be pulled on demand if required at signing.

### ✅ Civo LTD (End User — fully verified)

**Source map (all tier-1):**
- Pillar 1: [civo.com/about](https://www.civo.com/about) (Civo LTD, UK Company 09568551, VAT GB213975206, London EC2A 4AW, founded 30 April 2015)
- Pillar 2: [civo.com](https://www.civo.com), [civo.com/uk-sovereign-cloud](https://www.civo.com/uk-sovereign-cloud) (Kubernetes-native sovereign cloud, K3s-based, Civo Stack, Konstruct)
- Pillar 3: [civo.com/about](https://www.civo.com/about) (ISO 27001, SOC 2, Cyber Essentials PLUS, Crown Commercial Service G-Cloud, named customers: Mercedes-Benz, Oxford, Orbital, THG)
- Pillar 4: inferred from Phase 1 (sovereign EU inference demand)
- Pillar 5: [TBC] (specific expansion plans not disclosed publicly)

**Draft Recital B (128 words):**
> Civo LTD is a company incorporated in England and Wales under company number 09568551, with its registered office at First Floor, 32–37 Cowper Street, London EC2A 4AW [civo.com/about]. Founded in April 2015 by Mark Boost, Civo operates a Kubernetes-native sovereign cloud and AI platform, with cloud regions in London, Frankfurt, Mumbai, New York, and Phoenix, and offices in London, Bengaluru, Austin, and Hamburg [civo.com/about]. Civo is certified to ISO 27001, SOC 2, and Cyber Essentials PLUS, and is listed on the UK Government's Crown Commercial Service G-Cloud framework [civo.com/about]. Public-sector and enterprise customers referenced by Civo include the University of Oxford, Mercedes-Benz, Orbital, and THG [civo.com/about].

**Why this example works:** everything sourced to a single tier-1 page (civo.com/about). Low fabrication risk. Fifth pillar (forward plans) is honestly marked `[TBC]` rather than invented.

### ✅ InfraPartners LLC (Strategic Supplier — CORRECTED from v3.3)

**⚠️ Prior v3.3 draft contained two fabrications:** "Ready-for-Service within 90 days of site-preparation completion" (no tier-1 source — not on infrapartners.llc, not on LinkedIn, not in Nscale or Caddis press releases) and "80% off-site completion" presented as a Counterparty-asserted fact (the figure is in tier-2 press at ainvest.com, but infrapartners.llc itself is effectively a placeholder page with no such claim). Both must be removed or reframed.

**Source map (v3.4 corrected):**
- Pillar 1: [linkedin.com/company/infrapartnersllc](https://www.linkedin.com/company/infrapartnersllc) (HQ London, offices London/Dublin/Cluj/Houston, founded 2018, 51–200 employees)
- Pillar 2: [globenewswire.com/news-release/infrapartners-caddis 2025-03-05](https://www.globenewswire.com) (quote from Michalis Grigoratos, CEO: "modular data centre solutions for AI workloads" — tier-1 direct-quoted press)
- Pillar 3: [nscale.com/press-releases/nscale-and-infrapartners](https://www.nscale.com) (60 MW Glomfjord Norway AI data centre partnership, Nscale x InfraPartners — tier-1 joint-release); [globenewswire/Caddis press release](https://www.globenewswire.com) (targeted 100 MW combined pipeline with Caddis Cloud Solutions across EMEA + North America — tier-1, joint release from Caddis quoting InfraPartners CEO)
- Pillar 4: inferred from Phase 1 (Provider supply-chain de-risking)
- Pillar 5: [TBC] (jurisdiction of Infrapartners LLC not public; combined pipeline target split between Caddis + Nscale named projects)

**Draft Recital B (v3.4 corrected, 135 words):**
> Infrapartners LLC ("InfraPartners") is a digital-infrastructure company founded in 2018, headquartered in London with offices in Dublin, Cluj, and Houston [LinkedIn]. InfraPartners designs and delivers prefabricated, modular data-centre solutions for AI workloads, with manufacturing operations in the United States and Romania [Caddis Cloud press release, 5 March 2025]. InfraPartners' announced pipeline includes a 60 MW AI data centre in Glomfjord, Norway in partnership with Nscale [Nscale press release, 25 March 2025], and a combined target of "over 100 MW of AI data center projects across EMEA and North America" in partnership with Caddis Cloud Solutions [Caddis press release]. The Counterparty's leadership includes Michalis Grigoratos (CEO) and Harqs Singh (CTO). The jurisdiction of incorporation and registration number of Infrapartners LLC shall be confirmed in the Definitive Documentation [TBC].

**What changed vs v3.3:**
- ❌ REMOVED: "Ready-for-Service within 90 days of site-preparation completion" (unsourced)
- ❌ REMOVED: "80% off-site completion" as Counterparty-asserted fact (tier-2 only; can be reintroduced in a subsequent draft with "as publicly reported" qualifier if desired, but not without)
- ❌ REMOVED: ">60 MW active project portfolio" as solo figure (60 MW is the Glomfjord single project; 100 MW is combined pipeline with Caddis — both now correctly attributed)
- ✅ ADDED: jurisdiction marked `[TBC]` — Infrapartners LLC's state of formation is not public; flagged honestly for signing-stage counsel confirmation

### ✅ Man of Solutions B.V. / SAG Consortium (Distributor Mode B — CORRECTED from v3.3)

**⚠️ Prior v3.3 draft contained Dutch-language jargon not matching actual site:** "centrale knooppunt" was used as if quoted from sovereignaigrid.nl, but the site actually uses "Consortium coördinatie & governance" — paraphrased closer to "consortium coordination & governance entity" in English. Additionally, "operating within the EuroHPC AI Gigafactory ecosystem" was presented as confirmed, but the EuroHPC JU has not independently designated SAG as a Gigafactory recipient — the consortium self-identifies that way. Corrections required.

**Source map (v3.4 corrected):**
- Pillar 1: [sovereignaigrid.nl](https://sovereignaigrid.nl) (consortium roster names Man of Solutions B.V. as parentOrganization / coordination entity), KVK registry = [TBC] (Man of Solutions B.V.'s own KVK number not embedded on consortium site)
- Pillar 2: [sovereignaigrid.nl](https://sovereignaigrid.nl) ("Consortium coördinatie & governance" — actual Dutch label; translates cleanly to "consortium coordination and governance entity")
- Pillar 3: [sovereignaigrid.nl/partners](https://sovereignaigrid.nl) (public partner roster: Easy Solar Group, Digital Energy Group AG, SourceParts.eu, Desert.Solutions), [sovereignaigrid.nl/geography](https://sovereignaigrid.nl) (Velsen-Noord NL primary, Verviers BE, Germany in development)
- Pillar 4: inferred from Phase 1 (federated institutional sovereign-AI pathway on Provider platform)
- Pillar 5: self-described as "first consortium implementing Article 12b multi-site regulation under the EuroHPC AI Gigafactory programme" — self-assertion, attribute accordingly; not independently verified from EuroHPC JU designation

**Draft Recital B (v3.4 corrected, 156 words):**
> Man of Solutions B.V. is a Netherlands private limited company publicly identified as the coordination and governance entity of the Sovereign AI-Grid Consortium (the "Consortium") [sovereignaigrid.nl]. The Consortium is a cross-border network operating across the Netherlands (Velsen-Noord), Belgium (Verviers), and Germany (in development), publicly positioned as a distributed federated network rather than a centralised facility [sovereignaigrid.nl]. The Consortium's announced partner roster includes Man of Solutions B.V., Easy Solar Group, Digital Energy Group AG, SourceParts.eu, and Desert.Solutions [sovereignaigrid.nl]. The Consortium self-identifies as "the first consortium implementing Article 12b multi-site regulation" within the EuroHPC AI Gigafactory programme framework, and states that it operates under steward-ownership governance [sovereignaigrid.nl]. The registered KVK number, registered office, and statutory director(s) of Man of Solutions B.V. shall be confirmed in the Definitive Documentation [TBC].

**What changed vs v3.3:**
- ❌ REMOVED: `"centrale knooppunt"` — not a quoted site phrase; site uses "Consortium coördinatie & governance"
- ✅ CHANGED: `"operating within the EuroHPC AI Gigafactory ecosystem"` → `"self-identifies as ... within the EuroHPC AI Gigafactory programme framework"` — reflects that the EuroHPC JU has not independently designated the Consortium; this is the Counterparty's own framing
- ✅ ADDED: `Article 12b multi-site regulation` attributed to "Consortium self-identifies as..." (not asserted as framework DE endorses)
- ✅ ADDED: KVK + MD identity marked `[TBC]` — not on sovereignaigrid.nl; require direct registry lookup before execution

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
