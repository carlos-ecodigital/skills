# DE Domain Overlays

> Digital Energy domain-specific activation rules, source hierarchies, and post-synthesis comparison protocol.
> Loaded when a DE domain keyword is detected in the research question.

## Core Principle

Research finds fresh data independently. Ecosystem data is the benchmark, not the baseline.

The research engine does NOT pre-load `_shared/` reference files as starting knowledge. It searches for the best available data from scratch. After synthesis is complete, it compares its findings against ecosystem references — keeping the best/latest per data point and flagging stale ecosystem data for user-approved updates.

This makes research-engine a continuous improvement mechanism for DE institutional knowledge.

## Domain Activation

Scan the research question against these keyword triggers. If any match, activate that domain's overlay.

Multiple domains can activate simultaneously (e.g., "BESS financing in NL" activates both BESS and Project Finance).

### Domain 1: BESS / Energy Storage

**Trigger keywords:** BESS, battery storage, energy storage, LFP, NMC, inverter, cycling, degradation, SDE++, FCR, aFRR, arbitrage, battery park, grid-scale battery, utility-scale storage, batterijopslag, energieopslag

**During research (Phase 1-2):**
- Inject NL BESS source hierarchy into search agent prompts:
  - Tier 1 priority: TenneT (ancillary services data), ACM (market reports), RVO (SDE++ statistics), CBS (energy statistics), BNEF (global storage tracker)
  - Tier 2 priority: Rabobank Dutch Electricity Sector reports, Energy Storage News, CBRE European energy storage reports
- Add Dutch-language search agent for NL-specific BESS data
- Anti-keywords: "home battery", "EV battery", "consumer", "Tesla Powerwall", "portable battery"

**Post-synthesis (Phase 3):**
- Compare findings against: `_shared/market-data.md` (BESS section)
- Compare against: `energy-markets/references/` (ancillary services pricing)
- Flag stale data in Ecosystem Data Updates appendix

### Domain 2: Data Centers / AI Infrastructure

**Trigger keywords:** data center, data centre, hyperscale, colocation, AI factory, GPU, compute, PUE, WUE, immersion cooling, liquid cooling, moratorium, restwarmteplicht, edge, AI cluster

**During research (Phase 1-2):**
- Inject DC source hierarchy:
  - Tier 1 priority: CBS (ICT sector statistics), IEA (data center energy reports)
  - Tier 2 priority: CBRE NL data center market reports, Cushman & Wakefield, DCD (Datacenterdynamics), Turner & Townsend DCCI, Uptime Institute
- Anti-keywords: "gaming PC", "home server", "NAS", "Raspberry Pi"

**Post-synthesis (Phase 3):**
- Compare findings against: `_shared/market-data.md` (DC section)
- Compare against: `dc-engineering/references/` (technical specs)
- Compare against: `ai-infrastructure/references/` (GPU/compute data)
- Flag stale data

### Domain 3: Energy Markets NL

**Trigger keywords:** energy market, electricity price, day-ahead, imbalance, EPEX, APX, grid congestion, TenneT, cable pooling, curtailment, Energiewet, transportschaarste, net congestion, balancing

**During research (Phase 1-2):**
- Inject NL energy source hierarchy:
  - Tier 1 priority: TenneT (congestion maps, transport data), ACM (market monitoring reports), ENTSO-E (transparency platform), CBS (energy statistics), EPEX SPOT
  - Tier 2 priority: Energeia, Rabobank Dutch Electricity Sector, S&P Global Platts
- Activate Dutch-language searches (energy regulation content is often Dutch-only)
- Anti-keywords: "gas prices" (unless explicitly relevant), "oil market", "petrol"

**Post-synthesis (Phase 3):**
- Compare findings against: `energy-markets/references/` (all reference files)
- Compare against: `_shared/market-data.md` (energy markets section)
- Flag stale data

### Domain 4: Netherlands Regulatory / Permitting

**Trigger keywords:** Omgevingswet, Energiewet, vergunning, bestemmingsplan, stikstof, PAS, BOPA, MER, m.e.r., Wcw, warmtekavel, aardwarmte, Mijnbouwwet, PGS 37, Seveso, BRZO, Bal, Bbl, omgevingsplan, bezwaar, beroep

**During research (Phase 1-2):**
- Inject NL regulatory source hierarchy:
  - Tier 1 priority: wetten.overheid.nl (primary legislation), Staatscourant, RVO (permit guidance), Rijkswaterstaat (water permits), RIVM (environmental standards), ILT
  - Tier 2 priority: CMS, De Brauw, NautaDutilh, Stibbe, Pels Rijcken (law firm publications on NL regulatory changes)
- ALWAYS activate Dutch-language searches for regulatory topics
- Anti-keywords: "Belgium", "Germany" (unless comparative analysis requested)

**Post-synthesis (Phase 3):**
- Compare findings against: `netherlands-permitting/references/` (all reference files)
- Flag outdated statute references (legislation changes frequently)
- Note: Regulatory findings have high sensitivity to recency. Apply fast-moving recency factors.

### Domain 5: Project Finance

**Trigger keywords:** project finance, non-recourse, SPV, BV, DSCR, LLCR, PLCR, bankability, debt sizing, financial close, senior debt, mezzanine, equity bridge, cash waterfall, financial model, gearing

**During research (Phase 1-2):**
- Inject PF source hierarchy:
  - Tier 1 priority: EIB (project finance reports), DNB (banking sector data), BNEF (clean energy finance)
  - Tier 2 priority: Alantra, Rabobank, ING, ABN AMRO (NL infrastructure lending), Invest-NL, DLA Piper/CMS/NautaDutilh (PF legal publications)
- Anti-keywords: "personal finance", "consumer loan", "mortgage", "venture capital" (unless explicitly relevant)

**Post-synthesis (Phase 3):**
- Compare findings against: `_shared/equity-structures.md`
- Compare against: `_shared/investor-landscape.md`
- Compare against: `project-financing/references/` (deal structuring, benchmarks)
- Flag stale data

## Dutch-Language Search Activation

For Domains 3 (Energy Markets) and 4 (Regulatory): ALWAYS activate Dutch-language search.
For Domains 1 (BESS) and 5 (Project Finance): Activate Dutch search if the question is specifically about NL.
For Domain 2 (Data Centers): Activate Dutch search only if permitting or policy related.

**Implementation:** Include one Dutch-language search query per block alongside English queries. Use Dutch keyword equivalents from `keyword-engine.md`.

## Source Hierarchy Injection

Source hierarchies are injected into agent prompts as priority guidance, not as exclusive lists:

```
PRIORITY SOURCES for this topic (check these first):
- Tier 1: {list}
- Tier 2: {list}
Do not limit your search to these sources. They are starting points. Follow evidence wherever it leads.
```

This prevents the search from missing unexpected but valuable sources.

## Post-Synthesis Comparison Protocol

1. After synthesis: read relevant `_shared/` and skill reference files (identified per domain above)
2. For each data point in the brief with a counterpart in ecosystem files:
   - Which is more recent? Keep the most recent.
   - Which has a better source tier? Keep the best-sourced.
   - Are they consistent? If yes, corroboration bonus.
   - Are they inconsistent? Note in Contradictions section.
3. Produce the Ecosystem Data Updates appendix (see `output-formats.md`)
4. Updates to ecosystem files require explicit user approval — the brief recommends only

## When Overlay is Inactive

If no DE domain keywords match:
- No source hierarchy injection
- No geographic weighting
- No Dutch-language searches
- No post-synthesis ecosystem comparison
- No Ecosystem Data Updates appendix

The research engine works as a pure, domain-agnostic intelligence tool.
