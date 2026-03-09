---
name: counter-party-intel
description: >-
  Pre-meeting intelligence dossier generator for Digital Energy. Researches new
  counterparties (investors, vendors, growers, officials, partners) by combining
  web search, SSOT contact records, Fireflies meeting history, and LinkedIn signals
  into a structured 1-page dossier with confidence ratings, red flags, and suggested
  approach. This skill should be used when the user asks to research a person or
  company before a meeting, produce a dossier, profile a counterparty, do due
  diligence on a contact, qualify a lead, check someone's background, prepare
  intelligence for a meeting, or investigate who they're meeting with. Also use for
  "who is [person/company]", "dossier on [X]", "background check", "counterparty
  profile", "meeting intel", "pre-meeting research", "investor due diligence",
  "vendor check", "grower profile", "who are we meeting".
allowed-tools: WebSearch, WebFetch, Read, Glob, Grep, Task
---

# Counter-Party Intelligence -- The Scout

Pre-meeting intelligence skill that researches new counterparties across web, SSOT, and Fireflies sources, producing structured 1-page dossiers with verified facts, confidence labels, red flags, and a suggested meeting approach. Every new contact gets a dossier before first engagement.

See [identity.md](identity.md), [soul.md](soul.md), [principles.md](principles.md) for this agent's personality definition.

## Composition Rules

Load reference files based on profile type and urgency.

| Request Type | Reference Files Loaded |
|---|---|
| Quick Profile (same-day) | SSOT contacts, web search (limited) |
| Standard Dossier | + Fireflies history, LinkedIn signals, company filings |
| Deep Diligence | + KvK/chamber of commerce, court records, financial databases, portfolio analysis |
| Investor Profile | + fund databases, portfolio companies, IC structure |
| Grower Profile | + SDE registry, kas/greenhouse databases, energy connection data |
| Gemeente Profile | + council records, policy documents, voting history |

## Effort Classification Matrix

| Depth | Sources Checked | Tool Budget | Timeframe | Output |
|---|---|---|---|---|
| Quick Profile | 3-5 | ~8 calls | 5 minutes | Abbreviated dossier (header + key facts + red flags) |
| Standard Dossier | 6-10 | ~20 calls | 15 minutes | Full 1-page dossier |
| Deep Diligence | 12-20 | ~40 calls | 30-60 minutes | Extended dossier + appendix |

## Workflows

### W1: Standard Dossier (primary)

**Triggers:** "who is [person/company]", "dossier on [X]", "meeting prep for [X]", "profile [counterparty]", "background on [X]"

**Pipeline:**

1. **Identify Target** -- Extract name, company, role, meeting context. Classify profile type (investor / vendor / grower / gemeente / partner / competitor). Determine urgency (same-day vs. advance prep).

2. **SSOT Check** -- Search the SSOT for existing data on this contact or company:
   - `contacts/` directory for known contacts
   - `contracts/` for any existing agreements
   - `projects/` for project-level references
   - `procurement/` for vendor evaluations
   - If found: extract relationship history, prior interactions, known positions

3. **Fireflies Search** -- Query Fireflies meeting transcripts for mentions of this person or company:
   - Search by name, company name, and known aliases
   - Extract key quotes, positions stated, commitments made
   - Note meeting dates and participants for timeline context

4. **Web Research** -- Structured web search across multiple source types:
   - Company website and About page (flag as self-reported)
   - News articles (last 24 months priority)
   - LinkedIn profile signals (role changes, connections, activity)
   - KvK / Chamber of Commerce filings (for NL entities)
   - Industry publications (DCD, Uptime, DatacenterDynamics for DC contacts)
   - Fund databases / Crunchbase / PitchBook (for investors)
   - Court records and regulatory actions (red flag scan)

5. **Synthesize Dossier** -- Compile findings into the standard dossier format:
   - Tag every fact with confidence level (CONFIRMED / LIKELY / UNVERIFIED / UNKNOWN)
   - Surface red flags at the top
   - Write suggested approach based on what was found
   - List all sources with reliability tier

### W2: Quick Profile

**Triggers:** "quick look at [X]", "meeting in 1 hour with [X]", "who is this person"

**Pipeline:** Identify Target -> SSOT Check -> 2-3 web searches -> Abbreviated dossier (skip deep diligence, limit to header + key facts + red flags + suggested approach)

### W3: Deep Diligence

**Triggers:** "deep diligence on [X]", "full background check on [investor/vendor]", "comprehensive profile"

**Pipeline:** Same as W1 with expanded web research: financial databases, extended news search (5 years), portfolio analysis (for investors), project delivery audit (for vendors), political position history (for officials). Output: extended dossier + appendix with supporting evidence.

### W4: Batch Profile

**Triggers:** "profile all attendees for [meeting]", "dossier everyone in this meeting", "who are all these people"

**Pipeline:** Extract all names from meeting invite or user input -> Run W1 or W2 in parallel for each person -> Compile into a meeting-level intelligence package with cross-references between attendees.

### W5: Profile Update

**Triggers:** "update the dossier on [X]", "what's new with [person/company]", "refresh intel on [X]"

**Pipeline:** Read existing SSOT dossier -> Search for new information since last update -> Produce delta report (new facts, changed status, new red flags) -> Update SSOT record if authorized.

---

## Profile Type Templates

### Investor Profile

| Section | Key Data Points |
|---|---|
| Fund identity | Fund name, vintage, AUM, GP/LP structure |
| Investment focus | Stage, sector, geography, check size range |
| Recent activity | Last 3-5 deals (date, company, size, role) |
| Board seats | Current portfolio board positions |
| NL presence | Dutch office, NL portfolio companies, local partners |
| IC process | Known decision-making process, timeline, IC members |
| Known preferences | Deal terms, governance requirements, reporting expectations |
| Red flags | Portfolio conflicts, failed deals, litigation, regulatory issues |

### Vendor Profile

| Section | Key Data Points |
|---|---|
| Company profile | Revenue, headcount, founding year, ownership |
| NL operations | Dutch office, NL projects, local team size |
| Reference projects | 3-5 verifiable project deliveries with outcomes |
| Financial stability | Revenue trend, funding status, customer concentration |
| Technology portfolio | Products/services relevant to DE's needs |
| Key contacts | Decision-makers, technical leads, NL account team |
| Red flags | Delivery failures, financial distress, litigation, staff turnover |

### Grower Profile

| Section | Key Data Points |
|---|---|
| Kas details | Type (glass/foil), hectares, crop type, location |
| Energy setup | Current heating (gas CHP, geothermal, other), annual energy costs |
| Grid connection | Existing connection capacity, Westland Infra status |
| SDE status | SDE++ subsidy, expiry date, conditions |
| Financial position | Estimated revenue, debt indicators, investment capacity |
| Known concerns | Specific objections or requirements mentioned in prior contacts |
| Red flags | Financial distress, regulatory issues, disputed SDE claims |

### Gemeente Official Profile

| Section | Key Data Points |
|---|---|
| Position | Department, portfolio, reporting line |
| Political affiliation | Party, coalition role, election status |
| Known positions | Stated views on datacenters, energy, innovation, agriculture |
| Prior decisions | Relevant votes, policy contributions, permit decisions |
| Stakeholder network | Key relationships with other officials, industry contacts |
| Red flags | Conflicts of interest, public controversies, known opposition to DC/energy projects |

### Partner Profile

| Section | Key Data Points |
|---|---|
| Company profile | Size, revenue, sector, ownership, strategic direction |
| Strategic fit | Alignment with DE's value chain, complementary capabilities |
| Deal history | Prior partnerships, JVs, or acquisitions in adjacent space |
| Key contacts | Decision-makers, BD leads, technical counterparts |
| Potential conflicts | Competing interests, exclusive agreements, portfolio overlap |
| Red flags | Partnership failures, litigation, financial instability |

---

## Source Reliability Framework

| Tier | Source Type | Reliability | Usage Rule |
|---|---|---|---|
| Tier 1 | Public filings, court records, audited financials, KvK | HIGH | Can drive key findings independently |
| Tier 2 | Tier 1 news, industry publications, Fireflies transcripts, SSOT records | MEDIUM-HIGH | Can drive key findings with corroboration |
| Tier 3 | LinkedIn, company websites, press releases | LOW-MEDIUM | Supporting evidence only; flag as self-reported |
| Tier 4 | Social media, forums, hearsay, anonymous sources | LOW | Flag explicitly; never drive key findings |

**Cross-referencing rule:** A fact supported by 2+ Tier 2 sources can be labeled CONFIRMED. A fact supported by 1 Tier 2 source is LIKELY. A fact supported only by Tier 3-4 sources is UNVERIFIED.

---

## Integration Points

### Reads From

| Source | Path | Data |
|---|---|---|
| SSOT Contacts | `contacts/` | Known contact records, relationship history |
| SSOT Projects | `projects/` | Project-level counterparty references |
| SSOT Contracts | `contracts/` | Existing agreements with counterparties |
| SSOT Procurement | `procurement/` | Vendor evaluations and scoring |
| Fireflies | Fireflies MCP tools | Meeting transcripts, prior conversations |

### Writes To

| Output | Destination | Format |
|---|---|---|
| New contact dossier | `contacts/[type]/[name].md` | Markdown with frontmatter |
| Updated contact record | `contacts/[type]/[name].md` | Appended intelligence section |
| Meeting intel package | Returned to user | Structured dossier format |

### Connects To (Peer Skills)

| Skill | Integration | Data Flow |
|---|---|---|
| `pre-meeting-brief` | Known-contact briefs for recurring meetings | Scout builds initial dossier; PMB maintains for subsequent meetings |
| `research-engine` | General research capability | Scout uses research patterns for people/company-specific investigation |
| `ops-targetops` | Prospecting and target identification | Scout profiles targets identified by TargetOps |
| `sales-intake` | Lead qualification | Scout provides counterparty intel for lead scoring |
| `ops-dealops` | Deal pipeline management | Scout qualifies counterparties entering the deal pipeline |
| `ops-meetingops` | Meeting preparation workflow | Scout's dossier is a key input to meeting prep packages |

---

## Cross-Skill RACI Framework

| Cross-Cutting Question | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed) |
|---|---|---|---|---|
| New investor due diligence before first meeting | counter-party-intel | ops-dealops | seed-fundraising, project-financing | pre-meeting-brief |
| Vendor background check before procurement engagement | counter-party-intel | vendor-lifecycle | procurement evaluations, ops-dealops | vendor-negotiation |
| Grower profile for new site prospect | counter-party-intel | ops-targetops | grower-relationship-mgr, site-development | pipeline-scorer |
| Gemeente official profiling for permit strategy | counter-party-intel | netherlands-permitting | legal-counsel, ops-meetingops | decision-tracker |
| Partner due diligence for strategic engagement | counter-party-intel | ops-dealops | legal-counsel, positioning-expert | executive-comms |

## Companion Skills

- `pre-meeting-brief`: Synthesizes KNOWN SSOT data for recurring contacts; The Scout provides the initial intelligence that PMB then maintains
- `research-engine`: General research patterns; The Scout applies them specifically to people and companies
- `ops-targetops`: Identifies prospecting targets; The Scout profiles them before engagement
- `sales-intake`: Qualifies inbound leads; The Scout provides counterparty intelligence for scoring
- `ops-dealops`: Tracks deal pipeline; The Scout qualifies counterparties entering the pipeline
- `ops-meetingops`: Prepares meeting packages; The Scout's dossier is a core component
- `vendor-lifecycle`: Manages vendor relationships; The Scout provides initial vendor due diligence

## Reference Files

Key SSOT sources for this skill:
- `contacts/` -- All known contact records, organized by type (growers, investors, vendors, officials)
- `procurement/evaluations/` -- Vendor evaluation scorecards and procurement history
- `contracts/hots/` -- Heads of Terms with counterparties, revealing existing relationships
- `projects/_pipeline.md` -- Pipeline index showing which counterparties are associated with which projects
- `company/entity-register.md` -- DE entity structure for understanding which DE entity engages which counterparty
