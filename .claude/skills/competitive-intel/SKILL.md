---
name: competitive-intel
description: >-
  Competitive landscape monitoring and intelligence for the Dutch and European
  data center market. Tracks competitor moves, pricing signals, site announcements,
  regulatory shifts, and market dynamics. Produces monthly landscape updates,
  competitor profiles, and ad-hoc intelligence alerts. This skill should be used
  when the user asks about competitors, competitive landscape, market dynamics,
  competitor pricing, market share, competitor announcements, regulatory changes
  affecting DC market, industry trends, or market intelligence. Also use for
  "what are competitors doing", "competitive landscape", "market update",
  "competitor profile", "pricing intelligence", "regulatory scan", "who else is
  building in NL", "market dynamics", "industry monitor", "competitive analysis",
  "landscape update", "competitor tracking".
allowed-tools: WebSearch, WebFetch, Read, Glob, Grep, Task
---

# Competitive Intelligence -- The Radar

Continuous competitive landscape monitoring for the Dutch and European data center market. Tracks competitor moves across seven signal types, classifies impact on DE, and produces structured intelligence outputs ranging from monthly landscape updates to ad-hoc competitor deep dives. The Radar ensures DE is never surprised by a market shift.

See [identity.md](identity.md), [soul.md](soul.md), [principles.md](principles.md) for this agent's personality definition.

## Composition Rules

Load reference files based on request type.

| Request Type | Reference Files Loaded |
|---|---|
| Quick Market Check | Known competitor profiles, recent signals |
| Monthly Update | + regulatory tracker, pricing database, market metrics |
| Competitor Deep Dive | + specific competitor profile, full signal history, portfolio analysis |
| Pricing Analysis | + all pricing data points, market benchmarks, contract structures |
| Regulatory Scan | + policy tracker, gemeente decisions, grid allocation rules |

## Effort Classification Matrix

| Depth | Sources | Tool Budget | Timeframe | Output |
|---|---|---|---|---|
| Quick Check | 3-5 web searches | ~8 calls | 10 minutes | 3-5 bullet summary |
| Monthly Update | 15-25 searches + SSOT review | ~35 calls | 30-45 minutes | Full monthly update |
| Competitor Deep Dive | 20-30 searches + SSOT + industry sources | ~50 calls | 45-60 minutes | Full competitor profile + signal history |
| Pricing Analysis | 10-20 searches + SSOT pricing records | ~25 calls | 20-30 minutes | Pricing intelligence brief |

## Workflows

### W1: Monthly Competitive Update (primary)

**Triggers:** "monthly update", "competitive landscape update", "what happened this month in the DC market", first week of each month (cadence-driven)

**Pipeline:**

1. **Scan** -- Structured web search across 8 signal types for the trailing 30 days:
   - Industry publications (DCD, Uptime Institute, DatacenterDynamics, BroadGroup)
   - Dutch business press (FD, Telegraaf tech section, Energeia)
   - Regulatory sources (gemeente websites, RVO, TenneT capacity maps)
   - Job boards (LinkedIn, Indeed NL) for leading indicators
   - Conference proceedings and presentations (if recent events)
   - Financial news (fundraising, M&A, refinancing)

2. **Classify** -- Tag each signal with type (SITE / PRICING / REGULATORY / PARTNERSHIP / FUNDING / EXECUTIVE / TECHNOLOGY / MARKET) and impact (HIGH / MEDIUM / LOW). Apply "Impact on DE" assessment to each.

3. **Cross-reference SSOT** -- Check findings against existing competitor profiles and prior intelligence. Flag new information, contradictions, and updated status.

4. **Synthesize** -- Produce the Monthly Competitive Update in the standard format: Executive Summary, HIGH-impact signals, MEDIUM-impact signals, Pricing Intelligence, Regulatory Tracker, Competitor Spotlight, Market Metrics, Next Month Watch List.

5. **Alert** -- If any HIGH-impact signal is identified, produce an immediate ad-hoc alert in addition to the monthly update.

### W2: Competitor Deep Dive

**Triggers:** "deep dive on [competitor]", "full profile of [company]", "what is [competitor] doing in NL"

**Pipeline:** Load existing SSOT profile -> Comprehensive web research on target competitor -> Update profile template (category, NL presence, capacity, pricing, technology, strategy, key people, recent moves) -> Assess DE relevance and competitive implications -> Write "DE Relevance" section with specific strategic recommendations.

### W3: Pricing Intelligence

**Triggers:** "competitor pricing", "what are colo fees in NL", "market pricing for [service]", "how does our pricing compare"

**Pipeline:** Collect all available pricing data points from web, SSOT, and Fireflies -> Organize by competitor, geography, date, and confidence level -> Compare against DE's base case (EUR 120/kW/m) -> Identify pricing trends and outliers -> Produce pricing intelligence brief with confidence-labeled data points and DE implications.

### W4: Regulatory Scan

**Triggers:** "regulatory update", "what's changed with the moratorium", "new DC regulations", "grid policy changes"

**Pipeline:** Scan Dutch regulatory sources (gemeente websites, RVO, TenneT, Energiewet updates) -> Check EU-level regulatory developments (CSRD, energy efficiency directive, data sovereignty) -> Classify changes by impact on DE -> Update regulatory tracker -> Produce regulatory intelligence brief.

### W5: Ad-Hoc Alert

**Triggers:** HIGH-impact signal detected during any workflow, user flags a specific event ("did you see that [competitor] announced X")

**Pipeline:** Verify signal across 2+ sources -> Classify impact -> Assess DE implications -> Produce 1-paragraph alert with recommended response -> Flag for positioning-expert and relevant project skills.

---

## Competitive Landscape Framework

### Tier 1: Direct Competitors

Companies building or planning DC capacity in the Netherlands with potential overlap in DE's market position (edge/distributed, sustainability-focused, or greenhouse-adjacent).

| Competitor | Category | NL Presence | Capacity (est.) | DE Relevance |
|---|---|---|---|---|
| NorthC | Retail/Edge Colo | Yes -- multiple NL sites | ~100 MW operational | Closest competitor in edge/distributed segment; sustainability messaging overlap |
| Switch | Wholesale Colo | Exploring NL | TBD | Sustainability angle similar to DE; potential entrant |

### Tier 2: Indirect Competitors

Hyperscalers building own facilities and traditional wholesale/retail colo expanding in NL.

| Competitor | Category | NL Presence | Capacity (est.) | DE Relevance |
|---|---|---|---|---|
| QTS | Wholesale | Yes -- Eemshaven | ~200 MW planned | Grid capacity competition in Groningen region |
| Vantage | Wholesale | Yes -- Amsterdam | ~100 MW | Amsterdam-focused; moratorium impact |
| Equinix | Retail Colo | Yes -- Amsterdam (dominant) | ~250 MW operational | Market pricing benchmark; moratorium constrained |
| Microsoft | Hyperscale | Yes -- multiple sites | 500+ MW planned | Grid capacity competition; political influence |
| Google | Hyperscale | Yes -- Eemshaven | ~200 MW | Grid capacity competition in Groningen |
| Amazon (AWS) | Hyperscale | Yes -- various | 300+ MW planned | Grid capacity competition; potential customer |

### Tier 3: Emerging / DE-Like Competitors

Companies exploring similar models: industrial heat recovery, greenhouse integration, edge/distributed DC, or agricultural-energy-compute convergence.

| Competitor | Category | NL Presence | Status | DE Relevance |
|---|---|---|---|---|
| (Monitor for entrants) | DE-like | TBD | Scanning | Direct threat to differentiation if model is replicated |
| Windcloud | Sustainable DC | Germany | Operational | Wind-powered DC model; different approach, similar narrative |
| Bytesnet | Regional Colo | NL (Groningen) | Operational | Regional NL player; potential partner or competitor |

---

## Dutch Market Dynamics

### Amsterdam Moratorium
- **Status:** Active through at least 2030
- **Scope:** No new DC development permits in Amsterdam
- **Haarlemmermeer:** Separate restrictions in place
- **Impact on DE:** Neutral-to-positive. DE does not target Amsterdam. Moratorium drives competitors to alternative locations where DE has site optionality.
- **Watch:** Any signals of moratorium extension, relaxation, or expansion to other municipalities.

### Grid Congestion
- **Status:** Severe. TenneT reports ~60 GW queue vs ~20 GW peak demand.
- **Impact on DE:** HIGH. Grid connection is the critical path for every DE project. DE's strategy of securing existing greenhouse connections (already energized) is a key differentiator.
- **Watch:** TenneT capacity allocation policy changes, Westland Infra connection decisions, cable pooling regulatory framework updates.

### Alternative Locations Gaining Traction
- **Groningen:** QTS and Google present. Grid capacity exists but filling fast.
- **Zeeland:** Emerging interest from wholesale operators. Nuclear proximity.
- **Limburg:** Some activity; cross-border (Germany/Belgium) grid access.
- **Flevoland:** Wind energy proximity; emerging DC interest.
- **Impact on DE:** DE's greenhouse-adjacent sites are spread across multiple regions. Monitor competitor entry into each.

### Energy Pricing
- **Day-ahead:** Track EPEX NL spot prices (trend and volatility)
- **PPAs:** Track corporate PPA rates for wind/solar in NL
- **Grid fees:** Track TenneT/DNO tariff changes
- **Impact on DE:** Energy cost is a pass-through in DE's model, but pricing trends affect grower economics and BESS revenue.

---

## Intelligence Gathering Sources

| Source Category | Specific Sources | Signal Types | Frequency |
|---|---|---|---|
| Industry Publications | DCD, Uptime Institute, DatacenterDynamics, BroadGroup | All types | Weekly scan |
| Dutch Business Press | FD, Telegraaf, Energeia, Duurzaam Bedrijfsleven | Site, Regulatory, Funding | Daily scan |
| Regulatory / Government | RVO, TenneT, gemeente websites, Omgevingsloket | Regulatory | Weekly scan |
| Financial | Crunchbase, PitchBook, annual reports, SEC filings | Funding, M&A | Monthly |
| Job Boards | LinkedIn, Indeed NL | Leading indicators | Monthly |
| Conferences | DCD events, Dutch Datacenter Association, FEDA | All types | Per event |
| Social Media / Forums | LinkedIn activity, Reddit r/datacenter | Early signals | Opportunistic |

---

## Integration Points

### Reads From

| Source | Path | Data |
|---|---|---|
| Existing competitor profiles | `_shared/competitive-positioning.md` or similar | Baseline competitor data |
| Pipeline index | `projects/_pipeline.md` | Which DE projects are in which regions (for geographic overlap analysis) |
| Pricing data | `financial/scenarios/base-case.md` | DE's base case pricing for comparison |
| Regulatory tracker | `_shared/regulatory-tracker.md` or similar | Current regulatory status |

### Writes To

| Output | Destination | Format |
|---|---|---|
| Monthly landscape update | Returned to user / stored in SSOT | Structured monthly format |
| Competitor profiles | SSOT reference files | Markdown with frontmatter |
| Pricing intelligence | SSOT reference files | Data table with confidence labels |
| Ad-hoc alerts | Returned to user + flagged for relevant skills | 1-paragraph alert |

### Connects To (Peer Skills)

| Skill | Integration | Data Flow |
|---|---|---|
| `positioning-expert` | Competitive positioning strategy | Radar provides intelligence; Dunford Brain translates into positioning |
| `marketing-strategist` | Competitive messaging for campaigns | Radar provides competitor claims to counter |
| `sales-intake` | Competitive objection handling | Radar provides competitor strengths/weaknesses for sales prep |
| `investor-memo-writer` | Market context for investment memoranda | Radar provides competitive landscape section |
| `seed-fundraising` | Competitive landscape slides for pitch decks | Radar provides data; SF formats for investors |
| `research-engine` | Deep research on specific competitors or markets | Radar triggers deep dives via research-engine patterns |
| `pipeline-scorer` | Geographic and competitive risk factors for pipeline scoring | Radar flags competitor activity near DE pipeline sites |

---

## Cross-Skill RACI Framework

| Cross-Cutting Question | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed) |
|---|---|---|---|---|
| Monthly competitive landscape update for leadership | competitive-intel | ops-chiefops | positioning-expert, marketing-strategist | seed-fundraising, sales-intake |
| Competitor pricing benchmarking for deal negotiations | competitive-intel | financial-model-interpreter | vendor-negotiation, project-financing | ops-dealops |
| Regulatory change impact assessment on DE pipeline | competitive-intel | netherlands-permitting | legal-counsel, grid-connection-strategy | pipeline-scorer, decision-tracker |
| Competitive landscape section for investor materials | competitive-intel | investor-memo-writer | positioning-expert, seed-fundraising | collateral-studio |
| Competitor site announcement near DE pipeline site | competitive-intel | pipeline-scorer | site-development, grid-connection-strategy | ops-dealops, decision-tracker |

## Companion Skills

- `positioning-expert`: Translates competitive intelligence into positioning strategy and messaging architecture
- `marketing-strategist`: Uses competitive intelligence for campaign messaging and competitive differentiation in market communications
- `sales-intake`: Uses competitor profiles and pricing data for competitive objection handling during sales engagements
- `investor-memo-writer`: Embeds competitive landscape intelligence into investment memoranda and investor Q&A preparation
- `seed-fundraising`: Uses competitive landscape data for pitch deck market context slides
- `research-engine`: Provides deep research capability for specific competitor or market investigations
- `pipeline-scorer`: Incorporates competitive proximity risk into pipeline project scoring and gate assessments
- `financial-model-interpreter`: Provides DE's base case financial parameters for competitive pricing comparison

## Reference Files

Key SSOT sources for this skill:
- `projects/_pipeline.md` -- Pipeline index for geographic overlap analysis with competitor site announcements
- `financial/scenarios/base-case.md` -- DE base case pricing and economics for competitive comparison
- `company/entity-register.md` -- DE entity structure for understanding competitive positioning per business line
