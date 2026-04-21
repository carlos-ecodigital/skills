# Recital B — 5-Pillar Framework for Site Partners (Sites Stream)

**Purpose:** Produce an institutional-grade, lender-readable counterparty description for Site LOIs and HoTs. Adapts the commercial-LOI framework (`_shared/counterpart-description-framework.md`) for **Site Partners** — parties whose commercial fit is measured by what assets they secure and the quality of the value-exchange they enable.

**Per-partner target output:** 3–5 sentences, 120–180 words, single paragraph, bilingual (English + Nederlands), no bullets, no jargon without gloss, no vanity metrics, every material claim source-attributable to either (a) a tier-1 source URL in `site_partners[].source_map`, (b) a parsed document (KvK, Kadaster, ATO), or (c) a `[TBC]` placeholder.

**Upper bound:** one Recital B paragraph per Site Partner. A deal with three distinct B.V.s (Van Gog pattern) renders three paragraphs, each under 180 words.

---

## The 3 lender questions (Sites variant)

Every Site-Partner Recital B implicitly answers, in order:

1. **Is this partner operationally serious and solvent?** — entity form, KvK active status, years operating, ownership structure, sector track record.
2. **Does their asset position make this DEC commercially viable?** — grid capacity held, hectares of greenhouse served, heat-demand profile, BESS co-investment appetite.
3. **What's the bankable value-exchange signal?** — existing ATO, parcel control, long-term offtake capability, prior successful co-development or financing.

A Dutch infrastructure lender reading the LOI/HoT in a data room asks: *"If this project reaches FID, will this Site Partner still be there, still hold the grid connection and land, and still want the heat?"* Everything in Recital B should answer that.

---

## The 5 pillars (Sites variant)

Pillars 1–4 are mandatory per Site Partner. Pillar 5 is conditional.

| # | Pillar | Content | Answers Q | Fed by `deal.yaml` fields |
|---|---|---|---|---|
| 1 | **Identity & Scale** | KvK registration, legal name, UBO or controlling shareholder, group structure when multiple linked B.V.s | 1 | `site_partners[].legal_name`, `.kvk`, `.registered_address`, `.group_structure[]` (optional) |
| 2 | **Core Business** | What the SP does operationally — crop type (grower), network scale (heat network), portfolio (BESS operator), estate size (industrial landlord) | 1, 2 | `site_partners[].sector`, plus contribution-derived facts: `contributions[asset: grid_interconnection].details.mva`, `contributions[asset: land].details.area_m2`, etc. |
| 3 | **Track Record** | Years operating, relevant prior projects, financial or operational indicators where known | 3 | `site_partners[].years_operating`, `.prior_projects[]`, optional financial snapshot |
| 4 | **Strategic Fit** | Why this SP is the right contributor for the assets they hold | 2 | Derived from `contributions[]` + `returns[]`: e.g., heat-demand complementarity for growers, grid-node value for BESS, network-scale reach for heating networks |
| 5 | **Forward Plans** | Expansion intent, decarbonization roadmap, co-investment appetite — only if material to motivating the Project | 2, 3 | `site_partners[].forward_plans[]` (optional) — greenhouse expansion from `A.9` → `A.10`, decarbonization intent |

**Structural test:** if you remove any of pillars 1–4 and the paragraph still answers the three lender questions, the pillar was redundant. Cut.

---

## Pillar 1 — Identity & Scale

### Purpose

Establish the SP as a verifiable Dutch (or Benelux) legal entity whose identity a lender can pull from the KVK registry independently. When multiple linked B.V.s appear in the deal, surface the group relationship so the lender reads them as one family rather than three random vendors.

### Signal examples (pass)

- "Van Gog Grubbenvorst B.V. is a private limited company (besloten vennootschap met beperkte aansprakelijkheid) registered with the Dutch Chamber of Commerce under KvK number [TBC], with its registered office at Vinkenpeelweg 10, 5971 NJ Grubbenvorst."
- "The Site Partner is one of three linked B.V.s under the Van Gog family holding structure: Van Gog Grubbenvorst B.V. (Grid Contributor), Van Gog Grubbenvorst Vastgoed B.V. (Landowner), and Van Gog kwekerijen Grubbenvorst B.V. (Heat Offtaker)."
- "Westland Infra B.V. is a regulated distribution system operator licensed under the Dutch Electricity Act 1998 (Elektriciteitswet 1998) and the Gas Act (Gaswet), with concession areas covering Westland and surrounding municipalities."

### Noise examples (fail — do not include)

- "A family-owned leader in Dutch horticulture" — vanity; class-level; unverifiable.
- "One of the top growers in the Netherlands" — ranking without tier-1 source.
- "Part of the thriving Brabant glastuinbouw cluster" — geographic vanity.

### Bilingual template

**English:**
> `{legal_name}` is a `{entity_form_en}` registered with the Dutch Chamber of Commerce under KvK number `{kvk}`, with its registered office at `{registered_address}`.

**Nederlands:**
> `{legal_name}` is een `{entity_form_nl}`, ingeschreven bij de Kamer van Koophandel onder nummer `{kvk}`, met statutaire zetel aan `{registered_address}`.

### Anti-pattern enforcement (mirrors R-24/R-25 from loi-qa-gate)

- **No inline bracket citations** in the Recital prose (e.g., `[kvk.nl]`). Source attribution lives in `site_partners[].source_map`, never in the rendered paragraph. Enforced by **R-S24 (fail)**.
- **No vanity-financial patterns** (valuations of the family holding, turnover ranges picked up from press). Enforced by **R-S25 (fail)**.
- **Group-structure paragraph** appears only when more than one linked Site Partner exists in the deal; a single-SP deal omits it.

### Fed by

`site_partners[].legal_name`, `.kvk` (validated against `kvk_uittreksel` doc via cross-doc gate DataAcc-2), `.registered_address`, `.entity_form` (derived from legal_name suffix per registry A.1 validation), `.group_structure[]` (optional free-form list of sibling entities).

---

## Pillar 2 — Core Business

### Purpose

Describe what the SP *actually does* — not what they aspire to. For growers, crop type + scale (hectares). For heating networks, network reach + temperature regime. For BESS operators, deployed MW + chemistry. For industrial landlords, estate composition. Every material figure here must be sourceable.

### Signal examples (pass)

- **Grower:** "Van Gog kwekerijen Grubbenvorst B.V. operates a [18] hectare glasshouse complex at Vinkenpeelweg 10, Grubbenvorst, currently cultivating `[flowers / vegetables / plants — per registry A.11]`. Annual heat demand under the existing CHP infrastructure is approximately [TBC] MWh."
- **Heat network operator:** "Stadsverwarming Purmerend B.V. operates a district-heating network serving approximately 25,000 residential connections across Purmerend, with a contracted thermal throughput of circa 450 GWh per annum."
- **BESS operator / grid contributor:** "The Grid Contributor holds two active grid connections at the project site totalling 25.5 MVA (18.5 MW import / 7 MW export), provisioned by Enexis Netbeheer B.V. under ATO reference `{ato_reference}`, with a 70 MW expansion reservation earmarked for future phases."

### Noise examples (fail)

- "One of the Netherlands' most innovative greenhouse operators" — salesy adjective; R-14 equivalent.
- "Operates a state-of-the-art heat network" — salesy adjective; R-21 equivalent.
- "Renowned for operational excellence" — vanity.

### Bilingual template — Grower

**English:**
> `{legal_name}` operates a `{current_size_ha}` hectare glasshouse at `{greenhouse_location}`, cultivating `{cultivation_type}`. The existing heat supply is `{legacy_heat_source}`; anticipated annual heat demand is approximately `{mwh_per_year}` MWh per annum.

**Nederlands:**
> `{legal_name}` exploiteert een kas van `{current_size_ha}` hectare aan `{greenhouse_location}`, met teelt van `{cultivation_type_nl}`. De huidige warmtelevering is `{legacy_heat_source_nl}`; de verwachte jaarlijkse warmtevraag bedraagt circa `{mwh_per_year}` MWh per jaar.

### Bilingual template — Grid Contributor / BESS co-developer

**English:**
> The Grid Contributor holds `{mva}` MVA of active grid capacity at the project site via `{count}` connection(s) with `{dso}`, under ATO reference `{ato_reference}`. Existing contracted import / export capacity is `{import_mw}` MW / `{export_mw}` MW.

**Nederlands:**
> De Netbijdrager beschikt over `{mva}` MVA actieve netcapaciteit op de projectlocatie via `{count}` aansluiting(en) met `{dso_nl}`, onder ATO-referentie `{ato_reference}`. De bestaande gecontracteerde invoer- / uitvoercapaciteit bedraagt `{import_mw}` MW / `{export_mw}` MW.

### Fed by

`site_partners[].sector` (derived or provided), plus contribution-specific detail keys: `contributions[asset: land].details.area_m2`, `contributions[asset: grid_interconnection].details.mva / .import_mw / .export_mw / .dso`, `contributions[asset: equipment_bess].details.mw / .mwh`, legacy context from `deal_meta.legacy_heat_source`.

---

## Pillar 3 — Track Record

### Purpose

Concrete, verifiable operational history. Years operating, prior projects relevant to the Project (heat recovery, BESS co-development, grid-sharing agreements, SDE++ award history), financial indicators where public.

### Signal examples (pass)

- "Founded in 1972, the Van Gog group has operated continuously at the Vinkenpeelweg site for over fifty years and is registered as an active going concern in the KVK register."
- "The Grid Contributor has previously secured an SDE++ subsidy award for its CO₂ capture installation (reference [TBC])."
- "The Landowner previously executed a recht van opstal grant to [Third-Party] in 2018 for a 3-hectare adjacent parcel, demonstrating experience with the instrument."

### Noise examples (fail)

- "Trusted partner of many leading growers" — unsourced endorsement.
- "Top-tier reputation" — vanity.
- "Served 500+ clients" — unattributed count. Class-level.

### Bilingual template

**English:**
> Founded in `{year_founded}`, `{short_name}` has operated continuously at `{primary_site}` for `{years_operating}` years. `{prior_project_sentence_optional}`.

**Nederlands:**
> Opgericht in `{year_founded}` is `{short_name}` sinds `{years_operating}` jaar onafgebroken actief op `{primary_site}`. `{prior_project_sentence_nl_optional}`.

### Fed by

`site_partners[].years_operating` (derived from KvK `established_date` via parser), `.year_founded`, `.prior_projects[]` — a list of `{project_name, counterparty, instrument_type, year, source_doc_ref?}` entries. Each `prior_projects` entry must either link to a publicly verifiable source or be marked `[TBC]`.

### Tier 3 exclusion

Blog posts, analyst opinion, and AI-generated summaries are **never** citable as Track Record evidence for Site Partners. Same rule as commercial-LOI Recital B, inherited.

---

## Pillar 4 — Strategic Fit

### Purpose

One sentence — at most two — that explains *why this Site Partner is the right contributor for the assets they hold*. Rooted in the `contributions[] / returns[]` composition, not in rhetoric.

### Signal examples (pass)

- **Grower (Heat Offtaker):** "The `{current_size_ha}` hectare cultivation at Vinkenpeelweg generates a year-round thermal demand that aligns with the DEC's continuous waste-heat output, and the adjacency of the greenhouse to the DEC footprint permits direct-pipeline heat delivery without third-party transmission."
- **Grid Contributor:** "The Grid Contributor's `{mva}` MVA active connection at the site provides immediate access to grid capacity in a region where new ATO applications face 18–36 month DSO queue times, materially advancing DEC ready-for-service."
- **Landowner:** "The Landowner controls the freehold parcel adjacent to the Heat Offtaker's operations, enabling a single-site co-location of DEC, BESS, and heat-delivery infrastructure under one recht van opstal arrangement."
- **Heating network operator:** "As operator of the `{network_name}` district-heating network, the Heat Offtaker can absorb the DEC's thermal output into an existing distribution system without bespoke pipeline construction, shortening the heat-offtake development timeline."

### Noise examples (fail)

- "A natural partner for Digital Energy" — unsupported claim.
- "Shares our vision for sustainable infrastructure" — vision-language; not operational fit.
- "Strongly committed to decarbonization" — aspirational, not specific.

### Bilingual template

**English:**
> `{short_name}`'s `{key_contribution}` at `{site_location}` `{fit_rationale_active_verb}`, `{consequence_for_project}`.

**Nederlands:**
> `{short_name}`'s `{key_contribution_nl}` op `{site_location}` `{fit_rationale_active_verb_nl}`, `{consequence_for_project_nl}`.

### Fed by

Derived from the composition of `contributions[]` and `returns[]` on the SP; the writer identifies the single most material asset/value pair and articulates the fit in one sentence. No separate YAML field — this pillar is generated from data, not hand-authored content.

---

## Pillar 5 — Forward Plans (conditional)

### Purpose

Cover expansion intent, decarbonization roadmap, and co-investment appetite **only when** such plans are material to motivating the LOI/HoT. For a static grower with no expansion plans, omit.

### Signal examples (pass)

- "The Heat Offtaker has announced a phased expansion from `{current_size_ha}` to `{planned_size_ha}` hectares by `{expansion_timeline}`, which would proportionally increase contracted heat offtake."
- "The Grid Contributor has indicated an appetite for up to 50% co-investment in the BESS SPV, subject to HoT-stage financing terms."
- "The Site Partner has stated an intent to decommission its existing gas-fired CHP (`{kw_e}` kW electrical) on a schedule tied to DEC heat-supply ready-for-service."

### Noise examples (fail)

- "Plans to become a sustainability leader" — aspirational.
- "Exploring further partnerships" — vague; no operational substance.
- "Growing rapidly" — vanity without figure.

### Bilingual template

**English:**
> `{short_name}` has indicated `{forward_plan_specific}`, subject to `{contingency_optional}`.

**Nederlands:**
> `{short_name}` heeft aangegeven voornemens te zijn `{forward_plan_specific_nl}`, onder voorbehoud van `{contingency_optional_nl}`.

### Fed by

`site_partners[].forward_plans[]` — list of `{plan_type, figure?, timeline?, contingency?}` entries. Where a figure is stated (e.g., `planned_size_ha`), it must either link to a KvK filing, a municipal bestemmingsplan amendment, or the SP's own communication (tier-1). Otherwise marked `[TBC]`.

---

## Signal Test (Sites variant)

For each Site Partner Recital B paragraph, ask:

1. Does it name the **legal entity, KvK, and registered address** in the first sentence? (Pillar 1)
2. Does it describe **what the SP does operationally + the material asset(s) they hold**, with figures where available? (Pillar 2)
3. Does it establish **years operating or relevant prior projects**? (Pillar 3)
4. Does it explain **asset-specific fit** in one sentence with active verbs, not rhetoric? (Pillar 4)
5. If forward plans are material, does it state them with figures + timelines? (Pillar 5)
6. Is the paragraph under **180 words per partner**?
7. Are **all material claims** either (a) traceable to `source_map`, (b) parsed from a supporting document, or (c) marked `[TBC]`?

If all seven pass — signal. If any fail — noise; rewrite before presenting to user.

---

## YAML intake shape

```yaml
site_partners:
  - entity_id: 12345678901
    legal_name: "Van Gog Grubbenvorst B.V."
    kvk: "[TBC]"
    registered_address: "Vinkenpeelweg 10, 5971 NJ Grubbenvorst"
    entity_form: "besloten vennootschap met beperkte aansprakelijkheid"
    signatory: { ... }
    sector: "grid_contributor"        # free-form hint for Pillar 2
    year_founded: 1972
    years_operating: 54
    group_structure:
      - "Van Gog Grubbenvorst Vastgoed B.V. (Landowner)"
      - "Van Gog kwekerijen Grubbenvorst B.V. (Heat Offtaker)"
    prior_projects:
      - { name: "CO2 capture SDE++ award", instrument: "sde_subsidy", year: 2021, source_doc_ref: "[TBC]" }
    forward_plans:
      - { plan_type: "greenhouse_expansion", figure: "18 → 24 ha", timeline: "2027", contingency: "bestemmingsplan amendment" }
    contributions: [ ... ]
    returns: [ ... ]
    source_map:
      pillar_1:
        - "https://www.kvk.nl/handelsregister/[TBC]"
      pillar_2:
        - "documents/ato_enexis_8716…pdf"       # parsed-doc reference
      pillar_3:
        - "https://www.vangogkwekerijen.nl/over-ons"
      pillar_4: "derived from contributions + returns composition"
      pillar_5: "[TBC]"
```

### Tier-2 qualifier pattern

When a Pillar 3 figure (e.g., years operating, prior project size) is only available via tier-2 press rather than KvK registry or SP's own site, use the same tier-2 qualifier pattern as the commercial framework: name the publisher in the Recital prose with *"as publicly reported by [Publisher]"* or *"according to [Publisher]"*, and tag the `source_map` entry with `tier: 2` + `qualifier: "..."`. If no tier-1 corroboration exists, omit the claim.

---

## Anti-patterns (enforced by `site_qa_gate.md`)

Mirrors and extends the commercial Recital B rules (R-11 through R-28). Site-specific additions:

| ID | Severity | Scope | Rule | Mirrors |
|---|---|---|---|---|
| **R-S11** | warn | Recital B | `ISO \d{4,5}` pattern present, unless `choices.cert_relevant: true` | R-11 |
| **R-S12** | warn | Recital B | Per-partner word count outside 80–200 (Sites target: 120–180) | R-12 |
| **R-S13** | warn | Recital B | More than 1 parenthetical per sentence | R-13 |
| **R-S14** | warn | Body (Sites-wide) | Salesy adjectives `\b(leading\|innovative\|cutting-edge\|world-class\|best-in-class\|state-of-the-art\|purpose-built)\b` | R-14 + R-21 |
| **R-S15** | warn | Whole document | `positioning (its\|itself) as` | R-15 |
| **R-S22** | warn | Body | Meta-commentary patterns (sentences explaining the LOI's purpose rather than asserting facts) | R-22 |
| **R-S23** | **fail** | Recital B | Material numeric-metric claims (regex: `\b\d+[\d,]*\s*(ha\|MVA\|MW\|MWh\|m²\|customers\|connections\|years\|%)\b`) MUST be backed by (a) a tier-1 URL in `source_map`, (b) a parsed-document reference, or (c) a `[TBC]` placeholder | R-23 |
| **R-S24** | fail | Recital B | No inline bracket citations in prose (`[kvk.nl]`, `[website.com]`) — source attribution lives in `source_map` | R-24 |
| **R-S25** | fail | Recital B | No vanity-financial patterns (family-holding valuations, revenue ranges picked up from press) | R-25 |
| **R-S27** | fail | Signature block | `[TBC]` rendered literally in signature Name/Title — must route through `_render_placeholder` | R-27 |
| **R-S28** | warn | Whole document | `[TBC]` count exceeds 5 body-wide — intake likely incomplete | R-28 |

Full catalogue in `site_qa_gate.md`.

---

## Worked example — Van Gog anchor deal (three linked B.V.s)

### Van Gog Grubbenvorst B.V. (Grid Contributor)

**Draft Recital B (142 words, bilingual pair):**

> **EN:** Van Gog Grubbenvorst B.V. is a private limited company (besloten vennootschap met beperkte aansprakelijkheid) registered with the Dutch Chamber of Commerce under KvK number [TBC], with its registered office at Vinkenpeelweg 10, 5971 NJ Grubbenvorst. The Site Partner is one of three linked B.V.s under the Van Gog family holding structure; the other entities — Van Gog Grubbenvorst Vastgoed B.V. (Landowner) and Van Gog kwekerijen Grubbenvorst B.V. (Heat Offtaker) — are counterparties to this LOI under their respective roles. The Grid Contributor holds two active grid connections at the project site totalling 25.5 MVA (18.5 MW import / 7 MW export), provisioned by Enexis Netbeheer B.V., with a 70 MW expansion reservation earmarked for future phases. The existing grid position materially advances DEC ready-for-service in a congestion zone where new ATO applications face 18–36 month DSO queues.

> **NL:** Van Gog Grubbenvorst B.V. is een besloten vennootschap met beperkte aansprakelijkheid, ingeschreven bij de Kamer van Koophandel onder nummer [TBC], met statutaire zetel aan Vinkenpeelweg 10, 5971 NJ Grubbenvorst. De Locatiepartner is één van drie verbonden B.V.'s binnen de familieholdingstructuur Van Gog; de overige entiteiten — Van Gog Grubbenvorst Vastgoed B.V. (Grondeigenaar) en Van Gog kwekerijen Grubbenvorst B.V. (Warmteafnemer) — zijn wederpartij bij deze LOI in hun respectieve rollen. De Netbijdrager beschikt over twee actieve netaansluitingen op de projectlocatie met in totaal 25,5 MVA (18,5 MW invoer / 7 MW uitvoer), geleverd door Enexis Netbeheer B.V., met een reserveringsoptie van 70 MW voor toekomstige fasen. De bestaande netpositie versnelt de DEC-realisatie op een locatie waar nieuwe ATO-aanvragen te kampen hebben met DSO-wachttijden van 18 tot 36 maanden.

**Why this works.** Pillar 1 (identity + group structure) in sentences 1–2. Pillar 2 (core asset held: grid capacity) in sentence 3, with figures from `contributions[grid_interconnection].details` and the Van Gog LOI Section L data. Pillar 4 (strategic fit: grid-queue bypass) in sentence 4. Pillar 3 (track record) implicit in "existing" and omitted to respect word budget. Pillar 5 (forward: 70 MW reservation) embedded in Pillar 2 sentence. `[TBC]` on KvK pending DataAcc-1 resolution. All material figures map to parsed-document sources or `[TBC]`.

### Van Gog Grubbenvorst Vastgoed B.V. (Landowner) — illustrative

> **EN:** Van Gog Grubbenvorst Vastgoed B.V. is a private limited company registered with the Dutch Chamber of Commerce under KvK number [TBC], with its registered office at Vinkenpeelweg 10, 5971 NJ Grubbenvorst, and serves as the property-holding vehicle within the Van Gog family group. The Landowner holds freehold title to Kadaster parcel [TBC] at Vinkenpeelweg 10, zoned Agrarisch under the Grubbenvorst bestemmingsplan. The parcel is adjacent to the Heat Offtaker's glasshouse operations, enabling single-site co-location of DEC, BESS, and heat-delivery infrastructure under a single recht van opstal arrangement.

> **NL:** Van Gog Grubbenvorst Vastgoed B.V. is een besloten vennootschap ingeschreven bij de Kamer van Koophandel onder nummer [TBC], met statutaire zetel aan Vinkenpeelweg 10, 5971 NJ Grubbenvorst, en fungeert als de vastgoedhoudende entiteit binnen de familiegroep Van Gog. De Grondeigenaar heeft vol eigendomsrecht op Kadaster-perceel [TBC] aan Vinkenpeelweg 10, met bestemming Agrarisch volgens het bestemmingsplan Grubbenvorst. Het perceel grenst aan de kasactiviteiten van de Warmteafnemer, waardoor een gecombineerde locatie van DEC, BESS en warmtelevering onder één recht van opstal mogelijk is.

### Van Gog kwekerijen Grubbenvorst B.V. (Heat Offtaker) — illustrative

TODO(SAL): complete Pillar 2 figures for greenhouse size (registry A.8 value) and current heat source (gas-fired CHP? boiler?) once `kvk_uittreksel` is collected. Draft Pillar 4: "year-round cultivation generates continuous thermal demand aligned with DEC waste-heat output; adjacent siting permits direct-pipeline delivery without third-party transmission". Word budget 120–180 after gaps are filled.

---

## Workflow integration

In the Site HoT SOP (future) + SAL Runbook:

1. SAL runs source capture: website (grower + group), KVK extract, Kadaster extract for parcels, ATO from the Grid Contributor.
2. Engine drafts one Recital B per Site Partner using the 5-pillar structure + bilingual template.
3. Engine applies the signal test + anti-pattern linter before presenting.
4. SAL reviews each paragraph + source map at the Recital B review gate.
5. SAL accepts, requests edits, or rewrites. Iterate until accepted.
6. Accepted paragraphs are embedded in `deal.yaml` under `site_partners[].recital_b.en` + `.nl`.
7. Generator re-runs anti-pattern linter at build time; failures block the .docx.

---

## What this framework does NOT do

- Does not write Recitals A, C, or D (template-fixed: Background, Non-Binding Nature, Binding Provisions — identical across Site Partners).
- Does not do legal due diligence on Site Partner solvency. It documents what is public + parsed; it does not verify. Escalate to `legal-counsel` for solvency analysis.
- Does not write Section R parties table or Section L locations table (those are data-driven, separate renderer in `loi/loi-template-body-v1.docx`).
- Does not cover commercial-stream LOIs — use `_shared/counterpart-description-framework.md` for those.
