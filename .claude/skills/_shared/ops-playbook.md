# Digital Energy Operating System Playbook

> Shared reference for all ops-* skills. This is the operating rhythm, governance model, tool integration, and continuous improvement framework.

## 1. Skill Ecosystem Map

### Existing Skills (Domain Experts)
| Skill | Domain | Invoked By |
|-------|--------|-----------|
| `de-brand-bible` | Brand foundation, personas, proof points | All content/narrative skills |
| `seed-fundraising` | Fundraising strategy, materials, archetypes | ops-storyops, ops-dataroomops, ops-irops |
| `content-engine` | Content writing (all channels) | ops-outreachops, ops-storyops, ops-irops |
| `collateral-studio` | Presentations, decks, one-pagers | ops-storyops, ops-outreachops |
| `marketing-strategist` | GTM strategy, campaigns, offers | ops-storyops |
| `positioning-expert` | Positioning, competitive, messaging | ops-storyops |
| `legal-counsel` | Legal documents, advice | ops-dealops, ops-dataroomops |
| `netherlands-permitting` | Permits, environmental, regulatory | ops-dealops |
| `project-financing` | Financial modeling, deal structures | ops-dealops, ops-dataroomops |
| `humanizer` | Strip AI writing patterns | ops-outreachops, ops-irops (before sending) |
| `dc-engineering` | Data center engineering (15 specialists) | ops-dealops |
| `ai-infrastructure` | AI compute cluster design (6 specialists) | ops-dealops |
| `energy-markets` | Energy trading, PPA, BESS revenue (6 specialists) | ops-dealops |
| `sales-intake` | Lead qualification, ICP routing | ops-dealops, ops-targetops |
| `brand-book` | Visual design system, design tokens | All presentation/visual skills |
| `content-atomizer` | Repurpose 1 source → 10+ platform derivatives (LinkedIn, X, video, newsletter, email) | ops-storyops, content-engine |
| `carlos-thought-leadership` | CEO personal brand strategy for LinkedIn + X (topic selection, engagement, weekly briefs) | content-engine, content-atomizer |
| `site-development` | Site selection, co-location master planning | ops-dealops |

### Meta Skills
| Skill | Role | Primary Output |
|-------|------|---------------|
| `forge` | Skill ecosystem architect | New skills, audits, integrations, automation chains |

### Ops Skills (Orchestrators)
| Skill | Role | Primary Output |
|-------|------|---------------|
| `ops-chiefops` | Cross-functional coordination | Weekly brief, decision log, escalations |
| `ops-meetings` | Meeting lifecycle | Agendas, summaries, action items |
| `ops-contextops` | Institutional memory | Decision journal, relationship intel, tribal knowledge |
| `ops-dealops` | Deal/project lifecycle + HubSpot CRM | Deal dashboards, pipeline reviews, CRM hygiene |
| `ops-storyops` | Unified narrative (all audiences) | Narrative architecture, consistency checks, routing |
| `ops-targetops` | All-audience prospecting | Scored target lists, research dossiers, intro maps |
| `ops-outreachops` | All-audience outbound | Email sequences, intro requests, follow-ups |
| `ops-dataroomops` | Due diligence readiness | Data room, DD Q&A, readiness audits |
| `ops-irops` | Investor relations | Monthly updates, relationship tracking, ask management |

### Relationship: Ops Skills Orchestrate, Domain Skills Execute

```
User request
    ↓
Ops skill (decides WHAT to do, HOW to structure it)
    ↓
Domain skill (does the specialized work)
    ↓
Ops skill (checks quality, routes output, updates tracking)
```

Example: "Write investor update for this month"
1. `ops-irops` structures the update (pulls metrics, frames highlights/lowlights)
2. `content-engine` polishes the writing
3. `humanizer` strips AI patterns
4. `ops-irops` finalizes, tracks distribution

## 2. Operating Cadence

### Daily Habits (3 minutes total)
| When | Habit | How |
|------|-------|-----|
| After any external meeting | Voice note: key takeaways (2 min) | WhatsApp voice note, later processed via `ops-contextops` |
| After any decision | Say it out loud with reasoning | WhatsApp message or voice note, processed by `ops-contextops` |

### Weekly Rhythm
| Day | Activity | Skill | Founder Time |
|-----|----------|-------|-------------|
| Sunday evening | 15-min voice note: this week's priorities | Processed by `ops-chiefops` | 15 min |
| Monday AM | Weekly brief delivered | `ops-chiefops` | 5 min read |
| Monday | Pipeline review (async) | `ops-dealops` | 10 min review |
| As needed | Meeting prep for external meetings | `ops-meetings` | 0 (auto) |
| As needed | Post-meeting processing | `ops-meetings` + `ops-contextops` | 2 min voice note |
| Friday PM | Action item reconciliation | `ops-chiefops` | 5 min review |

**Total founder ops time: <45 minutes/week**

### Monthly
| Activity | Skill | Founder Time |
|----------|-------|-------------|
| Investor update | `ops-irops` | 30 min input |
| CRM health check | `ops-dealops` | 10 min review |
| Narrative consistency check | `ops-storyops` | 15 min review |
| Complexity kill review | `ops-chiefops` | 15 min (what's not working? kill it.) |

### Quarterly
| Activity | Skill | Founder Time |
|----------|-------|-------------|
| OKR / priority reset | `ops-chiefops` | 2 hrs |
| Skill ecosystem review | All ops skills | 1 hr (which skills earn their keep?) |
| Strategy/narrative refresh | `ops-storyops` | 2 hrs |

## 3. Tool Integration

### Current Stack
| Tool | Used For | Integrated With | MCP Status |
|------|---------|----------------|------------|
| **Gmail** | External comms | `ops-outreachops`, `ops-meetings` | Google Workspace MCP (draft + send) |
| **Google Calendar** | Scheduling | `ops-meetings` (meeting prep triggers) | Google Workspace MCP (read events) |
| **Google Drive** | File storage | `ops-dataroomops`, all skills | Google Workspace MCP (create/list files) |
| **Google Sheets** | Financial models | `ops-dealops`, `project-financing` | Google Workspace MCP (read/write cells) |
| **Fireflies** | Meeting transcription | `ops-meetings` (post-meeting processing) | Fireflies MCP (search + pull transcripts) |
| **WhatsApp** | Founder comms, voice notes | `ops-contextops` (brain dump, WhatsApp harvest) | No MCP -- manual export only |
| **Claude Code** | Skill execution | All skills | N/A (host platform) |
| **HubSpot** | CRM | `ops-dealops`, `ops-targetops` | Connected via Claude plugin |
| **ClickUp** | Task management | `ops-chiefops`, `ops-meetings` | ClickUp MCP (create/update tasks) |
| **GitHub** | Code | Engineering (not ops-managed) | N/A |

### MCP Server Configuration

Skills declare MCP tools in their `allowed-tools` frontmatter. When connected, they pull data directly instead of requiring manual copy-paste.

| MCP Server | Skills That Use It | Key Capabilities |
|------------|-------------------|------------------|
| Google Workspace | `ops-meetings`, `ops-outreachops`, `ops-chiefops`, `ops-dataroomops`, `ops-dealops` | Gmail send/read, Calendar events, Drive files, Sheets data, Docs creation |
| Fireflies | `ops-meetings`, `ops-chiefops` | Search transcripts, pull full transcript, generate summary |
| ClickUp | `ops-meetings`, `ops-chiefops`, `ops-dealops` | Create tasks, update status, list tasks |
| HubSpot | `ops-dealops`, `ops-outreachops`, `ops-targetops`, `ops-dataroomops`, `ops-chiefops`, `ops-meetings` | Search/update contacts and deals, property discovery, pipeline queries |

**Setup:** See `_shared/mcp-setup-guide.md` for installation and configuration instructions.

### Data Flow

```
WhatsApp voice note / message
    ↓ (export or dictate to Claude -- no MCP available)
ops-contextops → Decision Journal / Relationship Intel / Tribal Knowledge
    ↓
ops-chiefops → Weekly Brief / Action Items → ClickUp (direct via MCP)
    ↓
ops-dealops → HubSpot (direct via MCP: contacts, deals, pipeline)

Fireflies transcript
    ↓ (pull directly via Fireflies MCP)
ops-meetings → Meeting Summary + Action Items
    ↓
ops-dealops → HubSpot update (direct via MCP)
    ↓
ops-outreachops → Follow-up email (draft via Gmail MCP, send after approval)
    ↓
ClickUp → Action items assigned (direct via MCP)

External meeting scheduled
    ↓ (detected via Calendar MCP)
ops-meetings → Agenda
    ↓
ops-targetops / seed-fundraising → Pre-meeting brief
```

### Workflow Friction Points

**Original problem:** Skills live in Claude Code; work happens in Gmail/WhatsApp/Drive.

**Solved by MCP (5 friction points eliminated):**
1. ~~Fireflies transcripts require manual paste~~ → Fireflies MCP pulls transcripts directly
2. ~~Meeting follow-ups require copy-paste to Gmail~~ → Gmail MCP drafts and sends (after approval)
3. ~~HubSpot updates require manual data entry~~ → HubSpot MCP reads/writes directly
4. ~~Calendar events require manual checking~~ → Calendar MCP lists upcoming meetings
5. ~~Data room documents require manual upload~~ → Drive MCP creates files directly

**Remaining friction (no MCP solution yet):**
1. **WhatsApp:** No safe MCP server. Continue manual export via `ops-contextops`.
2. **Voice notes:** WhatsApp voice notes require manual transcription or dictation. No automated path.
3. **Batch processing:** Some workflows still benefit from batching (1-2x/day) to reduce context switching.

**Fallback principle:** Every MCP-dependent workflow has a manual fallback. If an MCP server is disconnected, skills revert to paste-and-process or output-as-Markdown. No skill breaks without MCP.

## 4. Governance (Minimal)

### Decision-Making
| Decision Type | Who Decides | Process |
|--------------|-------------|---------|
| Day-to-day ops | Any founder, solo | Decide and log via `ops-contextops` |
| Spending >EUR 1K | Both founders agree | 24-hour consent: decide, share, proceed unless vetoed |
| External commitments | Both founders | Written agreement before committing |
| Strategy changes | Founders together | Dedicated strategy session |
| Legal/financial | Founders + advisor | Escalate via `ops-chiefops` |

### Information Access
| Sensitivity | Who Sees | Examples |
|------------|----------|---------|
| Open | Anyone | Product info, public content, general market data |
| Internal | Founders + team | Pipeline data, meeting notes, internal metrics |
| Restricted | Founders only | Cap table, financials, investor terms, legal strategy |
| Confidential | Named individuals only | Term sheets, sensitive negotiations |

### Written Over Verbal
If it's not written down, it didn't happen. But "written" includes:
- Voice notes (processed by `ops-contextops`)
- WhatsApp messages (harvested weekly)
- Claude Code outputs (automatically documented)

## 5. Activation Sequence

Not all skills at once. Phase in based on where you are:

### Phase 0: This Week (Skill Activation Sprint)
**Goal:** Test 3-5 existing skills with real tasks. Fix what's broken.

| Day | Test | Skill |
|-----|------|-------|
| 1 | "Write a LinkedIn post about grid congestion" | `content-engine` |
| 2 | "Help me outline our seed deck" | `seed-fundraising` |
| 3 | "Create a one-pager for neocloud buyers" | `collateral-studio` |
| 4 | "What's our positioning vs. hyperscalers?" | `positioning-expert` |
| 5 | "Brain dump: [paste recent WhatsApp thread]" | `ops-contextops` |

### Phase 1: Weeks 1-2 (Kill the Admin)
**Activate:** `ops-contextops` + `ops-meetings`
**Goal:** Process every meeting and capture every decision. Reduce admin burden.

**MCP setup:** Connect Google Workspace MCP and Fireflies MCP (see `_shared/mcp-setup-guide.md`). This eliminates the biggest friction point -- manual transcript paste and calendar checking.

Habit to build: After every meeting, invoke `ops-meetings` -- it pulls the Fireflies transcript directly via MCP. No paste needed.

### Phase 2: Weeks 2-4 (Build the Narrative)
**Activate:** `ops-storyops` + `ops-targetops`
**Goal:** Lock the narrative across investor and buyer audiences. Build target lists.

### Phase 3: Month 2 (Execute the Raise)
**Activate:** `ops-outreachops` + `ops-dataroomops` + `ops-irops`
**Goal:** Launch investor outreach. Data room ready. Update cadence established.

### Phase 4: Month 2-3 (Commercial Pipeline)
**Activate:** `ops-dealops` + full HubSpot integration + ClickUp MCP
**Goal:** Parallel commercial pipeline alongside raise. HubSpot MCP is already connected via Claude plugin -- `ops-dealops` can pull pipeline data directly from day one.

### Phase 5: Ongoing
**Activate:** `ops-chiefops` at full cadence
**Goal:** Weekly rhythm locked in. Reporting automated.

## 6. Continuous Improvement

### After Every Skill Use: Quick Rating (5 seconds)
Ask yourself: "Was that output useful enough that I'd invoke this skill again for the same task?"
- Yes -> skill is working
- Sort of -> note what was missing
- No -> flag for redesign

### Monthly: Complexity Kill Review
Ask: "What process, report, or skill output did nobody use this month?"
Kill it.

### Quarterly: Ecosystem Review
For each skill:
| Question | Answer |
|----------|--------|
| Did I invoke this skill this quarter? | Y/N |
| Was the output useful more often than not? | Y/N |
| Should it be merged with another skill? | Which? |
| Should it be killed? | Why? |
| What's missing that I wished it could do? | Feature request |

### Common Failure Modes
| Failure | Symptom | Fix |
|---------|---------|-----|
| Skill bloat | Too many skills, unclear which to use | Merge or kill. Max 20 total. |
| Stale processes | SOPs not updated | Review every skill quarterly |
| CRM rot | HubSpot data goes stale | Weekly stale check via `ops-dealops` |
| Narrative drift | Different materials tell different stories | Monthly consistency check via `ops-storyops` |
| Admin creep | Ops overhead grows instead of shrinks | Monthly complexity kill review |
| Tool sprawl | More tools than necessary | Quarterly tool audit. Max 8 core tools. |

## 7. Parked Questions (To Revisit)

These questions were deferred. Return to them as the system stabilizes:

1. **Ideal week structure:** What does the founder's ideal week look like? (Shapes skill priority)
2. **One-thing question:** If one skill worked perfectly, which would change everything? (Focuses investment)
3. **Co-founder roles:** Who owns what? (Shapes agent assignment per founder)
4. **Advisor inventory:** How many, what domains, how active? (Feeds `ops-targetops` advisor map)
5. **Raise details:** Amount, structure, timeline? (Configures `seed-fundraising`)
6. **ClickUp status:** Keep, simplify, or replace? (Affects action item routing)
7. **Voice-first comfort:** How much of input can be voice-driven? (Shapes entire input architecture)
8. **SIGNALOPS:** Proactive intelligence agent -- build after Phase 2 when commercial pipeline is active
9. **Deal structuring skill:** Commercial architecture (term sheets, value splits) -- build when closing first deal
