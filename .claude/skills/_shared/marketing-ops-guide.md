# Marketing Operations Guide — Cross-Skill Coordination

Shared operational reference for all Digital Energy marketing skills. This file defines how skills work together, where files go, what tools to use, and how to maintain quality across the marketing stack.

**Referenced by:** `marketing-strategist/`, `positioning-expert/`, `content-engine/`, `collateral-studio/`, `de-brand-bible/`, `content-atomizer/`, `carlos-thought-leadership/`

---

## 1. Skill Invocation Map

### Quick Routing: "I need to..." → Use this skill

| Task | Primary Skill | Secondary Skill |
|---|---|---|
| Design a campaign / GTM plan | `marketing-strategist/` | — |
| Create an offer or value proposition | `marketing-strategist/` | `positioning-expert/` for framing |
| Define market positioning | `positioning-expert/` | — |
| Analyze competitive landscape | `positioning-expert/` | `de-brand-bible/references/competitive-positioning.md` |
| Write a LinkedIn post | `content-engine/` | — |
| Write a cold email sequence | `content-engine/` | `marketing-strategist/` for targeting strategy |
| Repurpose content across platforms | `content-atomizer/` | `content-engine/` for channel specs |
| Plan Carlos's weekly content (LinkedIn + X) | `carlos-thought-leadership/` | `content-engine/` for drafting |
| Brainstorm lead magnet concepts | `marketing-strategist/references/lead-magnet-ideation.md` | `collateral-studio/` for production |
| Create a newsletter | `content-engine/` + `references/newsletter-playbook.md` | `content-atomizer/` for section inserts |
| Create a pitch deck | `collateral-studio/` | — |
| Create a one-pager | `collateral-studio/` | — |
| Design a sales narrative | `positioning-expert/` | `collateral-studio/` for formatting |
| Plan an event | `marketing-strategist/references/events-speaking-playbook.md` | `content-engine/` for invitations |
| Design ABM campaign | `marketing-strategist/references/abm-playbook.md` | `positioning-expert/` for account messaging |
| Set pricing strategy | `marketing-strategist/references/pricing-strategy.md` | `de-brand-bible/references/deal-economics.md` |
| Measure marketing ROI | `marketing-strategist/references/marketing-analytics.md` | — |
| Run win-loss analysis | `positioning-expert/references/win-loss-analysis.md` | — |
| Handle a crisis | `marketing-strategist/references/crisis-management.md` | — |
| Launch a new product | `marketing-strategist/references/product-launch-playbook.md` | All execution skills |
| Check brand voice / terminology | `de-brand-bible/references/voice-rules.md`, `banned-phrases.md`, `terminology-standards.md` | — |
| Verify a proof point | `de-brand-bible/references/proof-points.md` | — |
| Get deal economics | `de-brand-bible/references/deal-economics.md` | `_shared/market-data.md` |

### Multi-Step Workflow Sequences

**New segment campaign (end-to-end):**
1. `positioning-expert/` → positioning canvas for the segment
2. `marketing-strategist/` → campaign brief + offer design + channel selection
3. `content-engine/` → LinkedIn posts, cold emails, ads, PR
4. `collateral-studio/` → pitch deck, one-pager, capability summary

**New deal collateral (fast turnaround):**
1. `collateral-studio/` → pitch deck from framework (select audience template)
2. `content-engine/` → follow-up email sequence
3. `marketing-strategist/references/objection-handling.md` → prep for likely pushback

**Event preparation:**
1. `marketing-strategist/references/events-speaking-playbook.md` → event strategy + targeting
2. `collateral-studio/` → event-specific deck + conference handout
3. `content-engine/` → pre-event LinkedIn + invitation email + post-event follow-up sequence

**Content calendar week:**
1. `marketing-strategist/references/smm-agent-pipeline-architecture.md` → Stage 1-4 (Scout → Approve)
2. `content-engine/` → draft posts per channel playbook
3. `de-brand-bible/references/proof-points.md` → verify all claims

**Content multiplication (from a blog post, press release, or whitepaper):**
1. `content-atomizer/` → generate all platform derivatives (LinkedIn, X, video scripts, newsletter section, email snippets)
2. `humanizer` → strip AI patterns from all derivatives
3. Carlos review → approve, add personal touches
4. Schedule per atomizer's posting calendar

**Carlos's weekly thought leadership:**
1. `carlos-thought-leadership/` → weekly content brief (triggers, topics, angles, hooks)
2. Carlos approves topics → `content-engine/` drafts posts per channel playbook
3. If atomizing from existing content → `content-atomizer/` for derivatives
4. `humanizer` → clean all output
5. Carlos final voice check → publish

**Monthly newsletter:**
1. `content-engine/references/newsletter-playbook.md` → run content curation checklist
2. `content-atomizer/` → generate newsletter sections from recent long-form content (if applicable)
3. `content-engine/` → draft full newsletter (5 sections per playbook structure)
4. Generate 3 subject line variants + preview text
5. `humanizer` → strip AI patterns
6. Carlos review → send

**Lead magnet campaign:**
1. `marketing-strategist/references/lead-magnet-ideation.md` → brainstorm + score concepts
2. `marketing-strategist/` → campaign brief for lead magnet distribution
3. `collateral-studio/` → produce the lead magnet deliverable
4. `content-engine/` → landing page copy, LinkedIn promos, email integration
5. `content-atomizer/` → repurpose lead magnet content into social derivatives

**Quarterly strategy review:**
1. `positioning-expert/references/win-loss-analysis.md` → deal analysis
2. `marketing-strategist/references/marketing-analytics.md` → channel/segment ROI review
3. `positioning-expert/` → positioning refresh if data warrants
4. All execution skills → update templates and examples with new positioning

### When to Chain vs. Invoke Standalone

**Standalone (single skill):** Quick tasks with clear format — "write a LinkedIn post," "create a one-pager," "handle this objection." The skill has enough brand bible context to operate independently.

**Chain (multiple skills):** Strategic tasks that require both thinking and producing — "design and execute a grower acquisition campaign," "prepare for the DCD conference," "launch our enterprise colocation offering."

**Rule of thumb:** If the task involves both *what to say* AND *how to format it*, chain strategy → execution.

---

## 2. Directory Structure & File Output

### Where to Save What

```
/Users/crmg/Documents/DE Claude/
├── [Project Name]/                    ← Per-deal/per-partner working directory
│   ├── Marketing/                     ← All marketing outputs for this deal
│   │   ├── DECK/                      ← Presentations
│   │   ├── 1PGR/                      ← One-pagers
│   │   ├── EMAIL/                     ← Email sequences and templates
│   │   ├── CONTENT/                   ← LinkedIn posts, blog drafts, ad copy
│   │   └── _draft/                    ← Working drafts (move to parent when approved)
│   └── [other project files]
├── .claude/skills/                    ← Skill definitions (templates, not outputs)
│   ├── _shared/                       ← Cross-skill shared references
│   └── [skill directories]
```

### Standard Directory Template for New Projects

When starting marketing work for a new project/deal:
```bash
mkdir -p "[Project]/Marketing/{DECK,1PGR,EMAIL,CONTENT,_draft}"
```

### Draft vs. Final Protocol
- **Drafts:** Save in `_draft/` subfolder with `DRAFT-` prefix
- **Approved finals:** Move to category folder, remove `DRAFT-` prefix, convert to PDF
- **Source files:** Keep `.md` source alongside `.pdf` final (editable source retained)

---

## 3. Naming Conventions

### Formal Deliverables (from `data-room-standards.md`)
```
[DE]-[Category]-[Topic]-[Version]-[Date].[ext]
```

| Code | Category | Example |
|---|---|---|
| PROP | Proposal | `DE-PROP-Lodewijk-Partnership-v3-20260215.pdf` |
| DECK | Presentation | `DE-DECK-Grower-Pitch-v2-20260201.pptx` |
| 1PGR | One-Pager | `DE-1PGR-Investor-Overview-v1-20260210.pdf` |
| WPPR | Whitepaper | `DE-WPPR-Grid-Scarcity-Analysis-v1-20260301.pdf` |
| CASE | Case Study | `DE-CASE-Fonti-Pilot-v1-20260401.pdf` |
| RESP | RFP Response | `DE-RESP-Municipality-Heat-v1-20260315.pdf` |
| FACT | Fact Sheet | `DE-FACT-BESS-Economics-v1-20260201.pdf` |
| BRCH | Brochure | `DE-BRCH-Capability-Summary-v2-20260115.pdf` |

### Working Documents
| Type | Pattern | Example |
|---|---|---|
| Draft deliverable | `DRAFT-[DE]-[Category]-[Topic]-[Version].[ext]` | `DRAFT-DE-DECK-Neocloud-Pitch-v1.md` |
| Research note | `RESEARCH-[Topic]-[Date].md` | `RESEARCH-Nordic-DC-Pricing-20260213.md` |
| Internal note | `NOTE-[Topic]-[Date].md` | `NOTE-Grower-Campaign-Retro-20260301.md` |
| Email sequence | `DE-EMAIL-[Segment]-[Sequence]-v[X].md` | `DE-EMAIL-Grower-Cold-5step-v2.md` |
| LinkedIn content | `DE-LI-[Theme]-[Account]-[Date].md` | `DE-LI-GridScarcity-CEO-20260213.md` |

### Version Control
- **Major:** v1, v2, v3 (structural changes, new sections)
- **Minor:** v1.1, v1.2 (corrections, data updates)
- **Draft:** v0.1, v0.2 (internal review only)
- Keep: current + previous version. Archive older versions in `_archive/` subfolder.

---

## 4. Tool & Integration Matrix

### Document Creation Pipeline
| Step | Tool | When |
|---|---|---|
| Draft content | Claude Write tool (`.md`) | Always start in markdown |
| Review & iterate | Claude Edit tool | Refinement loop |
| Convert to docx | `pandoc` via Bash (or `convert_to_docx.py` pattern from Stelia) | When Word format needed |
| Convert to PDF | `pandoc` with PDF engine or manual export | Final distribution format |
| Apply formatting | Reference `data-room-standards.md` | For formal deliverables |

### Research & Intelligence
| Tool | Use Case | Access |
|---|---|---|
| WebFetch | Market data from approved domains (see `settings.local.json`) | Whitelisted domains only |
| WebSearch | Current events, competitor news, regulatory updates | General web |
| `_shared/market-data.md` | NL DC market, BESS economics, pricing benchmarks | Local reference |
| `_shared/investor-landscape.md` | Investor profiles, fund mandates | Local reference |
| `project-financing/` skill references | Technical market data, regulatory frameworks | Local reference |

### CRM & Lead Management
| Tool | Use Case | Integration Point |
|---|---|---|
| HubSpot | Lead tracking, pipeline, deal attribution | `marketing-analytics.md` for metrics framework |
| HubSpot | Contact/company data for ABM | `abm-playbook.md` for account research |
| HubSpot | Email sequence tracking | `content-engine/` for sequence design |

### Social Media Management (SMM Pipeline)
| Tool | Use Case | Reference |
|---|---|---|
| n8n (self-hosted) | Orchestration — AI agent pipeline for 8 posts/day | `smm-agent-pipeline-architecture.md` |
| CrewAI | Agent framework for Scout/Writer/Filter stages | `smm-agent-pipeline-architecture.md` |
| Taplio / Buffer | LinkedIn scheduling (multi-account) | Stage 5: PUBLISH |
| Shield Analytics | Cross-account performance tracking | Stage 7: ANALYZE |
| Notion → Retool | Review queue (week 1-4 → month 2+) | Stage 4: APPROVE |
| Brand24 / Mention | Real-time mention monitoring | `crisis-management.md` |

### Design & Formatting
| Standard | Reference |
|---|---|
| A4 page layout, margins, fonts | `collateral-studio/references/data-room-standards.md` Section 3 |
| Classification labels | `data-room-standards.md` Section 1 |
| Confidentiality notices (EN/NL) | `data-room-standards.md` Section 7 |
| Table formatting, source footnotes | `data-room-standards.md` Section 4 |

---

## 5. Cross-Skill Workflows (Standard Operating Procedures)

### SOP 1: Campaign Launch (4-6 weeks)

```
Week 1:  positioning-expert → positioning canvas for target segment
Week 1:  marketing-strategist → campaign brief (segment, offer, channels, budget, KPIs)
Week 2:  content-engine → draft content per channel (LinkedIn, email, ads, PR)
Week 2:  collateral-studio → pitch deck + one-pager + event handout
Week 3:  Review all content against de-brand-bible (proof points, terminology, tone)
Week 3:  Load email sequences into HubSpot; schedule LinkedIn via Taplio
Week 4:  Launch + Stage 6 ENGAGE (monitor, respond, DM leads)
Week 6:  marketing-analytics → measure results, report ROI, recommend adjustments
```

### SOP 2: Deal Collateral (48 hours)

```
Hour 0:   Identify buyer persona + decision stage
Hour 0-4: collateral-studio → select presentation framework, customize for this deal
Hour 4-8: content-engine → write follow-up email (sent after deck delivery)
Hour 8:   Verify all proof points against brand bible
Hour 8:   Apply data-room-standards (naming, classification, formatting)
Hour 8-12: CEO/BD review
Hour 12-48: Iterate based on feedback; finalize PDF
```

### SOP 3: Quarterly Review (half-day)

```
Morning:
1. positioning-expert/win-loss-analysis → review last quarter's deals
2. marketing-strategist/marketing-analytics → channel + segment ROI analysis
3. Identify: what positioning worked? what messaging fell flat? which channels delivered?

Afternoon:
4. positioning-expert → refresh positioning if win-loss data warrants
5. Update proof-points.md with new project milestones
6. Update buyer-personas.md if new objections or pain points emerged
7. marketing-strategist → adjust campaign architecture and lead scoring
8. Queue content-engine and collateral-studio updates for next quarter
```

---

## 6. Quality Handoff Checklist

### Before Invoking collateral-studio/
- [ ] Audience identified (which of 6 buyer personas?)
- [ ] Format selected (DECK, 1PGR, WPPR, CASE, RESP, BRCH?)
- [ ] Classification level assigned (PUBLIC, EXTERNAL, CONFIDENTIAL, INTERNAL)
- [ ] Proof points verified in `de-brand-bible/references/proof-points.md`
- [ ] Deal economics confirmed in `de-brand-bible/references/deal-economics.md`

### Before Invoking content-engine/
- [ ] Channel identified (LinkedIn, email, blog, ads, PR, events?)
- [ ] Language confirmed (NL for growers/district heat; EN for neocloud/enterprise/investor)
- [ ] Buyer persona selected
- [ ] CTA defined (one CTA per piece)
- [ ] Approval status clear (who reviews before publishing?)

### Before Invoking marketing-strategist/
- [ ] Segment identified (which of 6?)
- [ ] Budget available or estimated
- [ ] Timeline defined (launch date, campaign duration)
- [ ] Success metrics agreed (CPL, CPA, pipeline target)
- [ ] Strategic context checked (any recent positioning changes from positioning-expert?)

### Before Invoking positioning-expert/
- [ ] Segment identified
- [ ] Competitive context current (any new competitor moves, regulatory changes?)
- [ ] Recent win-loss data available?
- [ ] Market data in `_shared/market-data.md` up to date?

---

## 7. File Retention & Archiving

| File Type | Retain | Archive After | Delete |
|---|---|---|---|
| Final deliverables (PDF + source) | Indefinitely | Never | Never |
| Working drafts (v0.x) | Until final approved | Move to `_archive/` | After 6 months in archive |
| Previous versions (v1 when v2 exists) | 6 months | Move to `_archive/` | After 12 months in archive |
| Research notes | 12 months | Review at 12 months | If no longer relevant |
| SMM content (published posts) | 90 days active | Auto-archive | Evergreen → buffer (180-day cooldown) |
| Campaign reports | Indefinitely | Never | Never |
| Win-loss interview notes | Indefinitely | Never | Never (anonymize after 24 months) |

### Archiving Protocol
1. Create `_archive/` subfolder in the project's Marketing directory
2. Move file with original name (don't rename)
3. Add `ARCHIVED-[Date]` prefix if needed for clarity
4. Archive trigger: when a new major version replaces the file, or at retention deadline

---

## 8. Classification Quick Reference

| Level | Label | Who Sees | Examples |
|---|---|---|---|
| **PUBLIC** | None required | Anyone | Website copy, press releases, published LinkedIn posts |
| **EXTERNAL** | "External — [Recipient]" | Named recipients + DE | Pitch decks, one-pagers, proposals, email sequences |
| **CONFIDENTIAL** | "Confidential" | Under NDA only | Financial models, term sheets, pricing specifics, project details |
| **INTERNAL** | "Internal Only" | DE team | Strategy documents, war room memos, win-loss reports, campaign retrospectives |

**Default classification by deliverable type:**

| Deliverable | Default Classification |
|---|---|
| Pitch deck | EXTERNAL |
| One-pager | EXTERNAL |
| Capability summary | PUBLIC |
| Press release | PUBLIC |
| LinkedIn post | PUBLIC |
| Cold email | EXTERNAL |
| Campaign brief | INTERNAL |
| Pricing strategy | CONFIDENTIAL |
| Win-loss report | INTERNAL |
| Financial projections | CONFIDENTIAL |
| ABM account plan | INTERNAL |
| Crisis response plan | INTERNAL |

---

## 9. Ecosystem Narrative — How to Explain the Marketing Stack

When explaining DE's AI marketing capabilities externally (to partners, advisors, or team members), lead with **10 capability buckets** — not skill counts or architecture tiers.

### The 10 Capabilities

| # | Capability | What It Does | Powered By |
|---|---|---|---|
| 1 | **Brand Voice & Identity** | Defines and enforces consistent brand voice across all channels, 6 personas, bilingual EN/NL | `de-brand-bible`, `brand-book`, `humanizer` |
| 2 | **Content Creation** | Writes all content types: LinkedIn, email, blog, ads, press releases, event invitations | `content-engine` |
| 3 | **Content Repurposing** | Takes 1 piece of content → 10+ platform-specific derivatives (LinkedIn, X, video, newsletter, email) | `content-atomizer` |
| 4 | **CEO Thought Leadership** | Proactive content strategy for Carlos on LinkedIn + X: topic selection, engagement, weekly briefs | `carlos-thought-leadership` |
| 5 | **Email & Outreach Sequences** | All-audience outbound: investor, neocloud, grower, advisor, event-based — with CRM integration | `ops-outreachops`, `content-engine` |
| 6 | **Positioning & Messaging** | Framework-driven competitive positioning (Dunford) and messaging architecture per segment | `positioning-expert` |
| 7 | **Lead Generation Strategy** | Campaign design, offer creation, lead magnet ideation, funnel architecture (Hormozi) | `marketing-strategist` |
| 8 | **Sales Collateral** | Pitch decks, one-pagers, capability summaries, proposals — audience-specific templates | `collateral-studio` |
| 9 | **Narrative Consistency** | Ensures all materials tell the same story to different audiences; detects narrative drift | `ops-storyops` |
| 10 | **Growth Operations** | Pipeline tracking, CRM hygiene, meeting processing, investor relations, target prospecting | `ops-dealops`, `ops-targetops`, `ops-irops`, `ops-meetingops` |

### How to Use This Framing

- **In conversations:** "We have 10 AI-powered marketing capabilities covering the full funnel from brand to close."
- **In presentations:** Use the 10 rows above as a single slide.
- **For team onboarding:** Start with this table, then point to the Quick Routing section (§1) for specific tasks.

**Principle:** Sophistication is an advantage when building. Simplicity is an advantage when explaining.
