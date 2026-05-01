---
title: "Shared Reference: HubSpot Pipeline Routing (Canonical)"
domain: SKILL
tier: 1
owner: "@jonathan"
status: active
confidentiality: internal
version: v2.2
created: 2026-04-29
updated: 2026-04-29
---

# DE HubSpot Pipeline Routing — Canonical (v2.2)

**Loaded by:** `de-sales-intake`, `de-ops-deals` (and any skill creating HubSpot deals)
**Last revision:** 2026-04-29 rev 3 — fixed P8 default stage to `Target Identified`, made the conference-organizer rule explicitly mandatory ("MUST create a deal, never contact-only"), made the activity-timeline note rule universal across ALL 8 pipelines (no exceptions for investor / press / channel / etc.)

---

## Core principle

**Classify on company ICP, not contact_type label.** A contact tagged `partner` who works at a neocloud (Nebius, Cudo, Core42) belongs in the demand pipeline because the *company* consumes capacity. The `contact_type` label only matters for true connectors — advisors/consultants/brokers with no operational stake in compute.

A "partner" tag is not a guarantee of channel-pipeline routing. Read the company.

---

## The 8 active pipelines

| # | Pipeline name | Default stage on intake | Default owner | Use when |
|---|---|---|---|---|
| 1 | `COMPUTE 1/2 - 2026 DC Colo Capacity Sale` | `Lead` | Jonathan | Company is a **demand-side capacity consumer** — neocloud (NEO), enterprise AI buyer (ENT), sovereign-AI tenant (TEN), DC operator buying colo (INFRA-DCO/INFRA-COLO) |
| 2 | `COMPUTE 2/2 - 2026 DC Colo Channel Partners` | `Identified` | Jonathan | Partner who **introduces or routes capacity buyers** to us — consultants, advisors, system integrators, builders, fuel-cell/energy infra partners, DC operators that act as channel |
| 3 | `INV - 1/4 - Program (Projects)` | `New Lead` | Carlos | **Project finance / debt** — banks, debt funds, infra credit, asset managers (fixed income / research analysts), structured lending, leasing |
| 4 | `INV - 2/4 - Equity (Platform)` | `New Lead` | Carlos | **Platform / corporate equity** — VC, PE, growth, family office, angel investors investing at the development entity |
| 5 | `INV - 4/4 - Investors Intro/Connect` | `Lead` | Carlos | **Investor connectors** — partners who can introduce us to investors but are not investing themselves (financial advisors, IR consultants, corporate-development liaisons) |
| 6 | `HEAT - 1/3 Greenhouses NL - Closing HoT` | `Lead` | Jonathan | **Heat offtake partners** — Dutch greenhouses, district heating, industrial heat buyers (HEAT-* ICP) |
| 7 | `Growth - Media/PR Pipeline` | `Pitched` | Jonathan | **Press, media, influencers, industry analysts** — journalists, podcasters, LinkedIn Top Voices, Forbes 30u30, paid newsletters (e.g. SemiAnalysis), TEDx speakers |
| 8 | `Growth - Conference Speaking` | `Target Identified` | Jonathan | **Conference / summit speaking opportunities** — conference organizers, summit Portfolio Directors / Programme Managers who might invite DE founders to keynote / panel / speak. **MANDATORY: must create a deal — never leave as contact-only.** Even a single conversation with a Portfolio Director at a Summit is enough to open a deal at `Target Identified` so the relationship is tracked and the speaking-slot follow-up is queued. |

---

## Decision tree (apply in order — first match wins)

1. **HEAT-* ICP** → P6 HEAT
2. **Company is a conference organizer or someone representing a conference** (title = Portfolio Director / Programme Director / Event Director / Conference Director at "*Summit / *Conference / *Forum / *Expo / *Days / *Week") OR notes mention "speaking opportunity / liked the pitch / invite to keynote / invite to panel / appearance / [Conference] [month]" → **P8 Conference Speaking @ stage `Target Identified`**. **This is MANDATORY** — never leave a conference-organizer contact as contact-only. The deal at `Target Identified` is what triggers the follow-up workflow to lock in a speaking slot. No exceptions, no "we'll decide later" — open the deal.
3. **`contact_type = press`** OR title contains `influencer / journalist / editor / Forbes / TED / Top Voice / podcast / paid-newsletter` → P7 Press/PR
4. **Company is a known media / research outlet** (SemiAnalysis, The Information, Stratechery, TechCrunch, Wired, PitchBook, etc.) → **P7 Press/PR (auto-route, do not need contact_type signal)** — the COMPANY determines routing, even if individual contact_type says `advisor`
5. **`ICP_primary ∈ {NEO, ENT, TEN, INFRA-DCO, INFRA-COLO}`** AND `ICP_secondary ∉ {ADV-CONSULT, ADV-ANALYST}` → **P1 Capacity Sale** (regardless of `contact_type`)
6. **`contact_type = customer`** → P1 (force, even with no/weird ICP)
7. **Big-tech compute consumer** (Meta, Microsoft, AWS, Google Cloud, Apple, Oracle) AND `contact_type ≠ advisor` → P1
8. **`ICP_primary starts with FIN-*`** AND notes describe them as the **financier directly** → P3 Program
9. **`ICP_primary starts with FIN-*`** AND notes describe them as a **connector/intro-maker** for project finance → P5 Connect
10. **`contact_type = investor`** → split:
    - Asset Mgmt / Wealth / Fixed Income / Sr. Research Analyst / debt-leaning → **P3 Program**
    - VC / PE / Family Office / Angel / Crypto-VC / Strategic Corporate Dev → **P4 Equity**
11. **`contact_type = partner`** AND has channel/intro/refer signal in notes OR ICP ∈ `{ADV-CONSULT, ADV-ANALYST, BLD, INFRA, VND, NRG}` → P2 Channel
12. **Partner with empty / unknown ICP but ENRICHED ParseNotes describing them as a DC operator / colo / GPU / data-center specialist** → **P2 Channel** (NOT no-deal). Always read `ParseNotes` ENRICHED section before defaulting to no-deal. Example: OPCORE (Plastennet R29 in GTC batch — ParseNotes said "European datacenter specialist 50MW current, 730MW secured").
13. **Vendor with channel signal** — vendors whose notes mention `European customers / resell / route customers / integrate compute for clients` → P2 Channel (NOT no-deal)
14. **Else** → no deal (still create contact record, just no deal record)

---

## Pre-classification enrichment checklist (DO NOT default to no-deal until you have done all of these)

- [ ] Read the contact's **`Title`** for press/influencer/conference signals (Influencer, Forbes 30u30, TED, Top Voice, Editor, Journalist, Podcaster, Analyst, **Portfolio Director at \*Summit**, Programme Director, Event Director)
- [ ] Read **`OrigNotes`, `ConvSummary`, `ParseNotes`** (especially the `ENRICHED:` / `ENRICHED (high):` / `ENRICHED (low):` section) for capacity / buyer / customer / AI-platform / oversubscription / "datacenter specialist" signals — `ParseNotes` often has the answer when the row otherwise looks unclassifiable
- [ ] **Look up the company website** when the name is unfamiliar (e.g. `opcore.eu` → "European datacenter specialist 50MW current 730MW secured"; `kisacoresearch.com` → conference organizer behind AI Infra Summit). The ENRICHED ParseNotes block usually has the result of this lookup already — read it.
- [ ] Check **`ICP_secondary`** — primary ENT with secondary ADV-CONSULT is channel, not demand. Primary NEO with secondary NEO is pure demand.
- [ ] Check the **email domain** for company hints (e.g. `@blackrock.com` → equity investor, `@semianalysis.com` → press, `@kisacoresearch.com` → conference org)
- [ ] Look at **`PromisesWe / PromisesThey`** — promises like "explore project finance" / "introduce to investors" signal connector role (P5); promises like "follow up re: [Conference] September appearance" / "speaking opportunity" signal P8 Conference Speaking
- [ ] Confirm with founder if the contact is borderline (advisor at media firm? researcher at conference org?) before defaulting to no-deal

---

## Known-company cheat sheet (seed; extend with each batch)

| Company | Pipeline | Why |
|---|---|---|
| Vontobel Asset Mgmt | P3 Program | Swiss bank, asset mgmt = fixed income / research, debt-side |
| Bloom Energy | P2 Channel | Fuel cell maker, complementary DC backup power |
| BlackRock | P4 Equity | Asset manager + private markets, treats DE as equity opportunity |
| SemiAnalysis | P7 Press/PR | Industry research / paid newsletter (Dylan Patel) |
| The Information | P7 Press/PR | Tech media |
| Stratechery | P7 Press/PR | Tech newsletter |
| Microway | P2 Channel | HPC system integrator, resells compute to EU clients |
| Nebius, Lablup, Cudo, TrueFoundry, Hut 8, Core42, Crusoe, CoreWeave, FluidStack, Together AI, Mistral | P1 Capacity Sale | Neoclouds (consumers) regardless of contact label |
| Marvik AI, FrontierOne, Cloudthrill, Hamilton Barnes, Ornn | P2 Channel | AI / DC consultancies that introduce customers |
| Newmark, CIBC, Digital Alpha Advisors, KfW, EIB | P3 Program | Project finance / infra debt |
| Boost VC, OVNI Capital, Encoded VC, DN Capital, Primary VC, Outpost | P4 Equity | Venture capital |
| Garrison FO, Sarofim, family offices generally | P4 Equity | Family office equity |
| Bloom Energy, Antora, Type One Energy | P2 Channel (energy adjacents) | Energy infra partners that bundle with compute |
| Agranom, Cooperatie Hoogstraten | P6 HEAT | NL greenhouse heat offtake |
| SKCI | P4 Equity | Angel investor network |
| **OPCORE** | **P2 Channel** | **European datacenter specialist (Iliad Group + InfraVia), 50 MW current + 730 MW secured. DC operator that can act as channel/integration partner.** |
| **KISA Core Research / AI Infra Summit** | **P8 Conference Speaking** | **Conference organizer behind AI Infra Summit (annual September event). Portfolio Directors invite founders to speak.** |
| **Firglas (Henrik Piper)** | **P5 Investors Intro/Connect** | **Board Member, ex-CFO Silverstream Technologies, ex-Goldman/UBS/Brunswick. Connector for infra financing, not direct financier.** |

---

## Deal naming convention (v2.0)

| Pipeline | Deal name format | Notes |
|---|---|---|
| P1 Capacity Sale | `{Company} — TBD MW` | If company is `[bracketed placeholder]` or empty → `{Contact} — TBD MW` |
| P2 Channel | `{Company} — TBD MW` | Same fallback rule |
| P3 Program | `{Company}` | Plain. Fallback: `{Contact}` |
| P4 Equity | `{Company}` | Plain. Fallback: `{Contact}` |
| P5 Connect | `{Company}` | Plain. Fallback: `{Contact}` |
| P6 HEAT | `{Company} — TBD MW` | Same fallback |
| P7 Press/PR | `{Company} — Press/PR` | If company is `Self-employed` or empty → `{Contact} — Press/PR` |
| P8 Conference Speaking | `{Company} — Speaking Opp` | Or `{Event} — Speaking Opp` if event name is more specific (e.g. `AI Infra Summit — Speaking Opp`) |

The MW placeholder is intentional — it signals to Jonathan that capacity sizing is still TBD and prompts the conversation. Replace once we have a real number.

---

## Owner assignment

- **P1, P2, P6, P7, P8** → Jonathan (BD / sales / heat / comms / speaking)
- **P3, P4, P5** → Carlos (all capital formation, all investor-track)

If `Met By` field shows a different DE founder (e.g. Yoni met someone), still apply the standard assignment — the deal owner manages the pipeline, not the original meeter.

---

## Notes on the activity timeline — UNIVERSAL RULE FOR EVERY DEAL

**Every single deal we create — across all 8 pipelines, no exceptions — gets at least one Note engagement attached to its activity timeline.** This applies equally to:

- ✅ P1 Capacity Sale deals (sales)
- ✅ P2 Channel Partners deals (channel)
- ✅ P3 Program (Projects) deals (project finance investors)
- ✅ P4 Equity (Platform) deals (equity investors)
- ✅ P5 Investors Intro/Connect deals (investor connectors)
- ✅ P6 HEAT deals (heat partners)
- ✅ P7 Media/PR deals (press)
- ✅ P8 Conference Speaking deals (conference organizers)

A deal without a meeting note is incomplete. When anyone (Jonathan, Carlos, future operator) opens the deal in HubSpot, the activity timeline must immediately show: who met, when, where, what was discussed, what was promised, and what's next. No clicking around, no hunting through emails — the note is RIGHT THERE on the timeline.

**There is no "this pipeline doesn't need notes" exception.** Investor deals get notes. Press deals get notes. Conference-speaking deals get notes. If you create a deal record, you create a note record and attach it. Period.

Meeting context goes on the deal as a **HubSpot Note engagement** (object type `notes` / `engagements`) — NOT in the deal `description` field. The `description` field is not visible on the timeline; the Note engagement is.

**Note body must include (same template across all pipelines):**
- Met where & when, met by which DE founder
- Contact details (title, email, phone, LinkedIn)
- ICP primary/secondary + contact type
- Conversation summary
- Original notes (raw in-person)
- LinkedIn notes (post-meeting LI activity)
- Interest signal + conversation quality
- **Promises we made** (action items for us, with due dates)
- **Promises they made** (expectations on them)

**One note per meeting.** If a deal is merged from multiple contacts (same company, multiple meetings), each meeting gets its own note attached to the deal — they all show on the timeline in chronological order. Every meeting is a separate note, even if they all attach to the same deal.

---

## Same-company merging rule

If multiple contacts at the same company classify into the **same pipeline**, merge to ONE deal record:
- One deal name (`{Company} — TBD MW` or pipeline default)
- All contacts associated to the deal
- Each contact's meeting note attached to the deal (multiple notes on one timeline)
- One set of stage progression

**Merge key:** normalized company name (lowercase, alphanumeric only) + pipeline.

**Cross-pipeline same-company stays as separate deals.** A company can legitimately be both a customer in P1 AND an investor in P4 — that's a real, useful distinction. Track separately.

---

## Required HubSpot scopes for write operations

The MCP connector must have these scopes for full deal creation:
- `crm.objects.contacts.write`
- `crm.objects.companies.write`
- `crm.objects.deals.write`
- `crm.objects.notes.write` (for activity-timeline notes)
- `crm.lists.write` (if using tier-based lists)
- Read counterparts of the above

Without `notes.write`, fall back to putting context in `description` field (degraded experience — won't show on activity timeline).

---

## Anti-patterns (mistakes from GTC 2026 batch — don't repeat)

❌ **Routing on `contact_type` instead of company ICP.** A "partner" at Nebius is still a P1 capacity-sale lead — the company consumes compute.

❌ **Defaulting unknowns to no-deal without enriching.** Many "unknown" contacts had clear classification clues in `Title`, `ParseNotes`, or domain. Always check.

❌ **Treating all FIN ICPs as direct project finance.** A FIN-tagged partner who "introduces" or "supports" project finance ≠ the direct financier. Use P5 Connect, not P3 Program.

❌ **Treating all Asset Mgmt as equity (P4).** Sr. Research Analysts at Asset Mgmt firms (Vontobel-class) are debt/fixed-income. Default to P3 Program unless notes explicitly indicate equity-side.

❌ **Treating all vendors as no-deal.** Vendors who resell to/integrate for end customers (system integrators like Microway) are channel partners, not pure no-deal vendors.

❌ **Missing the Press pipeline entirely.** Influencers, paid-newsletter operators, journalists, analysts are deal-pipeline-worthy in P7 Pitched stage.

❌ **Forgetting the `[BlackRock?]`-style placeholder check.** Bracketed company names mean "we don't know yet" — don't push these as deal names. Use the contact's name as the placeholder until the company is enriched.

❌ **Putting meeting notes in `description`.** They belong on the activity timeline as Note engagements.

❌ **Skipping the company-website lookup for unfamiliar names.** A 5-second domain check (or reading the ENRICHED ParseNotes section) reveals OPCORE = DC operator, KISA = conference organizer, Bloom Energy = fuel cell maker. Default to "look it up before classifying as no-deal."

❌ **Treating media/research firms as advisors-no-deal.** SemiAnalysis (Dylan Patel's paid newsletter), The Information, Stratechery — all are press/PR even when the contact's `contact_type` field says `advisor`. The COMPANY determines the routing.

❌ **Missing conference-organizer signals.** Title "Portfolio Director" at "AI Infra Summit / *Summit / *Conference / *Forum" + "speaking opportunity" / "liked the pitch" in notes = P8 Conference Speaking, not no-deal.

❌ **Leaving conference organizers / speaking opportunities as contact-only with no deal.** Conference organizers ALWAYS get a deal in P8 Conference Speaking at stage `Target Identified` — never just a contact. The deal record is what triggers the follow-up workflow to lock in the speaking slot. If a conference organizer ends up as contact-only, the relationship dies because nobody owns the follow-up.

❌ **Skipping the activity-timeline note on non-sales deals.** Investor deals, press deals, conference deals, channel deals — every single deal type gets a Note attached. There is no "this pipeline doesn't need notes" exception. If you create a deal, you create a note. Period.
