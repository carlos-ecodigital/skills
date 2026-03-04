# SMM Agent Pipeline Architecture for Digital Energy — v4

## Context

Digital Energy needs to scale its **LinkedIn + X (Twitter)** presence across company page and 5 co-founder accounts without proportionally scaling headcount. The solution: a seven-stage AI agent pipeline that scouts, drafts, filters, approves, publishes, engages, and learns — with human approval as a feature, not a bottleneck, that gracefully degrades as the system earns autonomy.

This is a **system design document**, not code. It defines every agent, every gate, every score, and every fallback so a team can build and operate it starting next week.

### Starting Conditions (validated)

| Factor | Reality |
|---|---|
| Combined LinkedIn followers (all 6 accounts) | <5,000 |
| Current posting cadence | Near zero (sporadic) |
| Co-founder LinkedIn time budget | 15-30 min/day each |
| Human review cadence | 2-3x per week (batched), not daily |
| HubSpot | Fully configured with pipeline stages, deal tracking, contact properties |
| Lead magnets | Existing assets available (to be mapped to CTA strategy) |
| Dedicated marketing hire | Not yet — reviewer role is shared |

These constraints fundamentally shape the design. The pipeline must be **low-burden for co-founders**, **batch-friendly for review**, and **realistic about reach from a small base**.

### What Changed in v4 (Critical Review + Reality Calibration)

v3 had the right architecture but wrong assumptions. v4 grounds everything in DE's actual starting conditions:

**From v2-v3 (retained):**
1. Stage 6: ENGAGE — comment monitoring, reply automation, comment-to-DM lead capture
2. Stage 7: ANALYZE — weekly performance analysis feeding back into all stages
3. Multi-format strategy — carousels outperform text on engagement (~5-8% vs ~3-4%, per Social Insider/van der Blom benchmarks)
4. LinkedIn algorithm awareness — company pages get 2-6% follower reach, personal profiles get 10-30%
5. Cross-engagement protocol — employee reshares reach 2-10x further than company page alone (MSLGroup found 561% in 2013; modern data shows wide variance)
6. Content repurposing chain — one brief → multiple formats/channels
7. Reactive fast lane — breaking news in under 2 hours
8. A/B testing framework — systematic variant testing
9. Tooling architecture — n8n + CrewAI + Buffer/Hootsuite + Shield (corrected from Taplio)
10. Anti-automation-bias — decoy posts, rotating review order, cold reads

**New in v4:**
11. **X (Twitter) as second channel** — lightweight cross-posting strategy starting month 2, with X-specific adaptations
12. **Virality Engine** — algorithm-aware post construction with corrected statistics (all claims now sourced or marked as directional)
13. **Growth Loops** — three self-reinforcing loops with recalibrated KPIs for <5K starting base
14. **Lead Generation Integration** — pipeline feeds into existing HubSpot CRM with lead scoring, using DE's existing assets as lead magnets
15. **Batched Approval Flow** — 2-3x/week review sessions replacing daily 20-min window
16. **Graduated Volume Ramp** — 4 posts/day weeks 1-4, scaling to 8 posts/day by month 2-3
17. **Statistics Audit** — every external claim validated, sourced, or marked as directional estimate

### Statistics Integrity Note

All statistics in this document are categorized:
- **[Sourced]** — traceable to a specific study with attribution
- **[Benchmark]** — consistent across multiple industry reports (Social Insider, van der Blom, Hootsuite, Buffer)
- **[Directional]** — the trend is well-established but the specific number is an estimate
- **[DE-specific]** — will be calibrated with DE's own data after 4-8 weeks of operation

---

## Pipeline Overview (7 Stages)

### Phase A: Ramp (Weeks 1-4) — 4 posts/day

```
Daily  SCOUT ──> DRAFT ──> FILTER ──> 2-3x/week APPROVE ──> PUBLISH ──> All Day ENGAGE ──> Weekly ANALYZE
 20 raw items   5 briefs    15-20 pieces    8-10 candidates     4 posts        replies + DMs      performance report
   ↓ score≥55  ↓ formats    ↓ 4 gates       ↓ batched review    ↓ 2 slots      ↓ lead capture     ↓ recalibrate
 10 briefs      15-20 pcs   8-10 survive     4-6 approved        4 published    engagement boost   scoring updates
```

### Phase B: Full Volume (Month 2+) — 8 posts/day

```
Daily  SCOUT ──> DRAFT ──> FILTER ──> 2-3x/week APPROVE ──> PUBLISH ──> All Day ENGAGE ──> Weekly ANALYZE
 40 raw items   10 briefs   30-40 pieces    20-25 candidates     8 posts        replies + DMs      performance report
   ↓ score≥55  ↓ formats    ↓ 4 gates       ↓ batched review     ↓ 3 slots      ↓ lead capture     ↓ recalibrate
 20 briefs      30-40 pcs   20-25 survive    12-16 approved       8 published    engagement boost   scoring updates
```

**Key design change from v3:** Human review happens 2-3x per week in batched sessions (~30-45 min each), not daily in a 20-min window. The pipeline produces and filters content continuously; approved posts are queued for scheduled publishing across the next 2-3 days.

**Phase A volume math (weeks 1-4, working backwards):**
- 4 posts needed per day = ~12-16 per review batch (covering 3-4 days)
- Reviewer sees 20-25 candidates per batch (target 60-70% approval)
- 20-25 candidates → 40-50 content pieces through 4-gate filter (~50% survival across batch)
- 40-50 pieces → 12-15 selected briefs × 3-4 formats each
- 12-15 briefs → from continuous daily scouting

**Phase B volume math (month 2+):**
- 8 posts/day = ~24-32 per review batch (covering 3-4 days)
- Reviewer sees 30-40 candidates per batch (target 65-80% approval)
- Rest of math same as before, scaled up

---

## Stage 1: SCOUT (05:00-06:00 CET)

**Agent:** Source Scout Agent
**Input:** RSS feeds, social monitoring, DE internal updates, LinkedIn trending topics
**Output:** Phase A: 10-15 scored source briefs / Phase B: 15-25 scored source briefs

### Source Categories (7 — added LinkedIn social listening)

| Category | What to Monitor | Signal Type |
|---|---|---|
| Dutch energy regulation | TenneT, ACM, RVO, Eerste/Tweede Kamer, municipal energy plans | Policy changes, grid data, subsidy rounds |
| AI infrastructure / DC industry | DCD, Data Center Knowledge, Capacity Media, hyperscaler earnings | Capacity announcements, pricing, build-outs |
| Dutch agriculture / horticulture | LTO, Glastuinbouw NL, Kas Magazine, Onder Glas, AGF.nl | Gas prices, heat demand, sustainability mandates |
| Energy markets | EPEX SPOT, TTF, BESS industry (ESS News, Energy Storage News), BNEF | Arbitrage spreads, FCR pricing, negative hours |
| Sovereign AI / EU policy | EU AI Act implementation, EC digital strategy, EIB, national AI strategies | Compute investments, data sovereignty, regulation |
| Competitor / peer activity | LinkedIn feeds of NorthC, Switch, QTS/Eurofiber, GPU cloud providers | Market positioning, partnerships, capacity claims |
| **LinkedIn social listening** | **Trending posts in DE's network, viral industry threads, audience questions** | **Engagement hooks, debate topics, audience pain signals** |

**Why LinkedIn social listening matters:** The best-performing posts respond to conversations already happening. A trending debate about Dutch grid congestion is a better hook than a static news article. The Scout should surface high-engagement posts from the network (>100 reactions, active comment threads) as source material.

### Scoring Rubric (0-100, pass threshold: 55)

| Dimension | Weight | Logic |
|---|---|---|
| Pillar alignment | 25% | Maps to one of 5 messaging pillars? +25 if yes, 0 if no |
| Persona relevance | 20% | +10 per persona it touches (max 20) |
| Timeliness | 20% | Today=+20, this week=+15, this month=+10, evergreen=+5 |
| Proof point density | 15% | 3+ matching proof points=+20, 2=+15, 1=+10, 0=+5 |
| **Format potential** | **10%** | **Can this become a carousel/video/thread? Multi-format=+10, text-only=+5** |
| Engagement potential | 10% | Controversial=+15, surprising data=+12, practical=+10, incremental=+5 |

*Changed from v1: Added "format potential" dimension, reduced proof point density and engagement potential weights slightly to make room.*

### Source Brief Output Format

```
ID:              SCOUT-2026-02-13-007
Source:          [Publication, date, URL]
Score:           76/100 (breakdown per dimension)
Matched pillars: Grid Scarcity as Moat
Matched personas: Grower, Neocloud
Matched proofs:  [PP-01: "~60 GW in queue vs ~20 GW peak demand"]
Key angles:      [2-3 possible post angles]
Suggested formats: [Text post, Carousel (5 slides: the grid queue visualized), Comment thread]
Suggested accounts: [CEO personal (narrative), Company (data graphic)]
Reactive flag:   [YES/NO — is this breaking/time-sensitive?]
```

---

## Post Type Taxonomy

Every piece of content in this pipeline is classified into one of 7 post types. This classification drives: which copywriting framework to use, which account(s) to post from, what tone to strike, which gates apply extra scrutiny, and how the content mixes across the week.

### The 7 Post Types

#### 1. Industry News Commentary

**What it is:** DE's take on external news — regulatory changes, market data, competitor moves, industry trends. The news is the hook; DE's perspective is the value.

| Attribute | Specification |
|---|---|
| **Source** | Scout Stage — categories 1-6 (external sources) |
| **Voice** | Analytical, authoritative. "Here's what this means for [persona]." |
| **Framework** | PAS (Problem-Agitate-Solve) or AIDA |
| **Account priority** | CEO (narrative take), Company (data-led summary), CTO/CFO (domain-specific angle) |
| **Best formats** | Text post, Carousel (data visualization), Comment thread (deeper analysis) |
| **Proof points** | Required — must connect news to DE's quantified claims |
| **CTA** | Question ("How is your organization preparing for this?") or link in first comment |
| **Risk level** | Medium — ensure DE's interpretation of regulation/policy is accurate. Product Accuracy gate enforced strictly. |
| **Weekly target** | 10-12 posts (25-30% of total) — the backbone of the content calendar |
| **DE example** | TenneT publishes new grid queue data → CEO post: "The Dutch grid queue just hit 65 GW. Here's why that number is both a problem and an opportunity..." |

#### 2. Company News & Updates

**What it is:** Internal developments — new hires, office/site updates, partnership announcements (non-milestone), event attendance, team activities. Humanizes the brand.

| Attribute | Specification |
|---|---|
| **Source** | Internal — team Slack, project updates, HR, events calendar |
| **Voice** | Warm, proud but not boastful. Show, don't tell. |
| **Framework** | 4Ps (Promise-Picture-Proof-Push) or BAB |
| **Account priority** | Company page (primary), relevant co-founder (secondary — "Excited to welcome [name]...") |
| **Best formats** | Text + photo, Video (behind-the-scenes), Carousel (event recap) |
| **Proof points** | Optional — not every company update needs quantified claims |
| **CTA** | Soft — "Welcome aboard!" / "See you at [event]?" / Tag people |
| **Risk level** | Low — but check: no confidential info, no premature announcements, HR-approved for hiring posts |
| **Weekly target** | 4-6 posts (10-15% of total) — enough to show life, not so much it crowds out substance |
| **DE example** | "Our operations team just completed the first cable pull at [site]. 3 months ahead of schedule." + site photo |

#### 3. Achievements, Milestones & Announcements

**What it is:** Significant company milestones — deals signed, permits obtained, MW milestones, partnership launches, funding rounds, award recognition. The "big moments."

| Attribute | Specification |
|---|---|
| **Source** | Internal — BD pipeline, project milestones, legal/commercial closings |
| **Voice** | Confident, specific, factual. Let the numbers speak. No "game-changing" or "thrilled to announce." |
| **Framework** | 4Ps (Promise-Picture-Proof-Push) or AIDA |
| **Account priority** | Company page (official announcement) + CEO (personal narrative behind the milestone) + relevant co-founder (domain angle) |
| **Best formats** | Text post (company), Text + Comment thread (CEO — story behind the milestone), Carousel (visual timeline of progress) |
| **Proof points** | Required — the milestone IS a proof point. Add it to the library. |
| **CTA** | Depends: investor-facing = "DM for details." Grower-facing = "Want to be next? Link in first comment." Partner-facing = tag partner. |
| **Risk level** | **HIGH** — always human-reviewed regardless of graduation. Verify: is the milestone real and closeable? Is the partner okay with being named? Is legal cleared? |
| **Weekly target** | 1-3 posts (5-8% of total) — only when there's genuine news. Never manufacture milestones. |
| **DE example** | "Digital Energy has secured 25.5 MW of grid capacity across 3 sites in South Holland. Here's what that means for our heat and compute customers..." |
| **Special rules** | - Always coordinated with partner (if naming them) — send draft for approval before publishing. - Embargo rules: if under NDA or pre-announcement, DO NOT post. - Cross-post: company page first, then CEO reacts/comments within 15 min, then co-founders engage. |

#### 4. Thought Leadership & Opinion

**What it is:** Original insights, contrarian takes, industry predictions, lessons learned, frameworks, mental models. This is where founders build personal brand equity. The most valuable post type for long-term positioning.

| Attribute | Specification |
|---|---|
| **Source** | Scout Stage (inspired by news but with original angle), internal expertise, founder experience |
| **Voice** | First-person, opinionated, specific. "I think X because Y. Here's the data." Not hedged, not both-sides. |
| **Framework** | PAS (if arguing against status quo), AIDA (if presenting new framework), BAB (if sharing transformation) |
| **Account priority** | Co-founder accounts (primary — this is personal brand territory). Company page only if the take is institutional. |
| **Best formats** | Text post (strongest for thought leadership — raw, direct), Comment thread (layered argument), Carousel (if presenting a framework/model) |
| **Proof points** | Helpful but not mandatory — opinion posts can lead with reasoning, not just data. However, if numbers are cited, they must be verified. |
| **CTA** | Question to drive debate: "Agree or disagree?" / "What am I missing?" / "Hot take or common sense?" |
| **Risk level** | Medium — opinions represent the company. Gate B (Marketing QA) checks: is this opinion aligned with DE's positioning? Could it alienate a buyer persona? Gate D (Humanizer) critical here — thought leadership must feel genuinely human, not AI-generated. |
| **Weekly target** | 8-10 posts (20-25% of total) — the highest-value content; prioritize quality over quantity |
| **DE example** | CEO: "Everyone talks about the Dutch grid queue. Nobody talks about what happens when the queue clears. Here's the scenario nobody's modeling..." |
| **Special rules** | - CEO gets first right of refusal on the best thought leadership angles. - Each co-founder should have 2-3 "signature topics" they return to repeatedly (builds recognition). - Thought leadership should NEVER be a company pitch disguised as opinion. If the post ends with "...and that's why you should work with Digital Energy," it fails Gate B. |

#### 5. Promotional / Product / CTA-Heavy

**What it is:** Direct promotion of DE's offerings — heat supply, colocation capacity, BESS services, portal signup, event registration. The "ask."

| Attribute | Specification |
|---|---|
| **Source** | Internal — marketing calendar, product launches, event schedule, portal updates |
| **Voice** | Direct, benefit-first, specific. "X MW available. Y EUR/MWh. Z months to delivery." Not salesy. |
| **Framework** | 4Ps (Promise-Picture-Proof-Push) — strongest for promotional. AIDA also works. |
| **Account priority** | Company page (primary). Co-founders only if it's a personal invitation ("I'm speaking at [event], come say hi"). |
| **Best formats** | Text + visual (product specs), Carousel (before/after economics), Video (walkthrough/demo) |
| **Proof points** | **Required** — promotional posts without data are just noise. Every claim quantified. |
| **CTA** | Single, specific, measurable: "Register here" / "DM me 'HEAT' for the economics model" / "Link in first comment" |
| **Risk level** | **HIGH for compliance** — financial claims need "indicative" qualifiers. Capacity claims must be current. Never promise delivery timelines that aren't confirmed. |
| **Weekly target** | 3-5 posts (8-12% of total) — the smallest bucket deliberately. Earn the right to promote by leading with value (80% non-promotional). |
| **DE example** | "We have 10 MW of liquid-cooled colocation capacity available in South Holland. PUE < 1.15. First racks live in 4 months. Interested? DM me or link in first comment." |
| **Special rules** | - **80/20 rule**: max 20% of weekly posts can be promotional. If you exceed this, audience trust erodes. - Never post promotional content from co-founder personal accounts more than 1x/week each. - Promotional posts should still teach something — wrap the CTA in an insight. - External links in first comment only (60% reach penalty if in post body). |

#### 6. Educational / How-To / Explainer

**What it is:** Teaching the audience something useful — how BESS revenue stacking works, what the Omgevingswet means for your project, how to calculate heat economics. Builds trust and positions DE as the expert.

| Attribute | Specification |
|---|---|
| **Source** | Internal expertise, project-financing skill references, permitting skill references, DE's existing skill files |
| **Voice** | Clear, patient, authoritative. Assume the reader is smart but not specialist. Define terms. Use examples. |
| **Framework** | AIDA (hook with the question → explain → show DE's answer → CTA) or BAB (before you knew this → now you know → here's what to do) |
| **Account priority** | CTO (technical explainers), CFO (financial explainers), BD (market/commercial explainers), Company (institutional how-to) |
| **Best formats** | **Carousel (strongest — step-by-step, visual, high dwell time)**, Comment thread, Text post |
| **Proof points** | Required — educational content must be grounded in real numbers, not abstract advice |
| **CTA** | "Save this for later" / "Want the full model? DM 'BESS'" / "Share with someone who needs this" |
| **Risk level** | Medium — accuracy is everything. If the "how-to" is wrong, DE loses credibility. Gate C (Product Accuracy) enforced strictly. |
| **Weekly target** | 6-8 posts (15-20% of total) — high-value, evergreen, shareable. Second most important type after thought leadership. |
| **DE example** | Carousel: "BESS Revenue Stacking in the Netherlands: A 5-Slide Primer" — Slide 1: Hook ("Your BESS can earn from 4 revenue streams simultaneously"), Slides 2-5: FCR, aFRR, arbitrage, capacity payments explained with numbers, Slide 6: "Want the full model? DM 'STACK'" |

#### 7. Engagement / Community / Conversational

**What it is:** Questions, polls, congratulations to others, reshares with commentary, replies to trending debates, "unpopular opinion" posts. Purely for building community and algorithmic engagement.

| Attribute | Specification |
|---|---|
| **Source** | Scout Stage (LinkedIn social listening category), trending topics, community events, peer achievements |
| **Voice** | Casual, curious, generous. Celebrate others. Ask genuine questions. Don't make it about DE. |
| **Framework** | None specific — these are freeform. But every post should still have a clear purpose. |
| **Account priority** | Co-founder accounts (primary). Company page only for reshares with commentary. |
| **Best formats** | Text post (question), Poll (sparingly), Reshare + comment |
| **Proof points** | Not required — this is about conversation, not claims |
| **CTA** | Implicit — the question IS the CTA. Or: "Tag someone who should see this." |
| **Risk level** | Low — but avoid: commenting on politics, religion, or non-industry controversies. Don't engage in pile-ons. Don't congratulate competitors in a way that undermines DE's positioning. |
| **Weekly target** | 4-6 posts (10-15% of total) — enough to stay social, not so much it dilutes the brand |
| **DE example** | CEO: "Question for the Dutch energy crowd: if you could add 50 MW of grid capacity anywhere in the Netherlands tomorrow, where would you put it and why?" |

### Weekly Content Mix Summary

| Post Type | Weekly Target | % of 40 posts | Primary Account |
|---|---|---|---|
| Industry News Commentary | 10-12 | 27% | CEO + Company + domain co-founders |
| Company News & Updates | 4-5 | 11% | Company page |
| Achievements/Milestones | 1-2 | 5% | Company + CEO |
| Thought Leadership | 8-10 | 22% | Co-founder accounts |
| Promotional / CTA-Heavy | 3-4 | 9% | Company page |
| Educational / How-To | 6-8 | 17% | CTO + CFO + Company carousel |
| Engagement / Community | 3-5 | 9% | Co-founder accounts |
| **Total** | **35-46** | **100%** | — |

*Note: Weekly targets are ranges because content mix flexes based on what's happening (news-heavy weeks shift toward Industry News; milestone weeks shift toward Achievements). The midpoint of all ranges sums to 40. The compliance check ensures no single type exceeds its upper bound or falls below its lower bound for 2+ consecutive days.*

**Compliance check the Writer Agent runs daily:** Does today's 8-post slate violate the mix? If 3+ posts are promotional, kill the weakest promotional and replace with thought leadership or educational. If 0 educational posts in 2 consecutive days, flag for rebalancing.

### Post Type × Gate Severity Matrix

Not all gates apply equally to all post types:

| Post Type | Gate A (Brand) | Gate B (Marketing QA) | Gate C (Product Accuracy) | Gate D (Humanizer) |
|---|---|---|---|---|
| Industry News | Standard | Standard | **Strict** (regulatory claims) | Standard |
| Company News | Standard | Relaxed (lower hook bar) | Relaxed (fewer claims to verify) | Standard |
| Achievements/Milestones | Standard | Standard | **Strict** (milestone must be verifiable) | Standard |
| Thought Leadership | Standard | **Strict** (hook + insight density) | Standard (fewer hard claims) | **Strict** (must feel human) |
| Promotional | **Strict** (compliance language) | Standard | **Strict** (all claims verified) | Standard |
| Educational | Standard | Standard | **Strict** (accuracy is the value) | **Strict** (carousel text, explainer tone) |
| Engagement/Community | Relaxed (informal tone OK) | Relaxed (no hook formula needed) | Relaxed (no hard claims) | **Strict** (must feel genuinely casual) |

---

## Stage 2: DRAFT (06:00-07:00 CET)

**Agent:** SMM Writer Agent
**Input:** Top 8-10 scored briefs + content calendar + proof points + format guidance
**Output:** 30-40 content pieces (3-4 formats per selected brief)

### Selection Rules
- Top 8-10 by score
- Max 3 briefs from same pillar per day
- At least 2 different personas represented
- At least 3 suitable for company page, 5 for co-founder accounts
- **At least 2 briefs must produce non-text formats (carousel, video script, document)**

### Content Formats (not just text variants)

For each selected brief, generate **3-4 pieces from this menu:**

| Format | When to Use | Specs | Engagement Benchmark |
|---|---|---|---|
| **Text post** | Always (baseline) | ≤1,300 chars, hook-first | ~3-4% engagement [Benchmark] |
| **Carousel / document** | Data-rich topics, step-by-step, comparisons | 5-10 slides, PDF upload, high dwell time | ~5-8% engagement [Benchmark — Social Insider, van der Blom] |
| **Video script** | Founder commentary, behind-the-scenes, explainers | ≤30 sec for highest completion; 1-2 min for deep-dive | Higher impressions than text, but engagement rate varies [Directional — the "5x" claim from LinkedIn's 2017 promo materials is outdated; carousels now often outperform video on engagement rate] |
| **Comment thread** | "Thread" continuation of a text post for deeper dive | 3-5 follow-up comments, each adding a layer | Extends dwell time |
| **Poll** | Opinion-gathering, audience research, engagement bait (used sparingly) | 2-4 options, text context above | High engagement but low quality leads |

**Format assignment per account:**

| Account | Primary Format | Secondary | Avoid |
|---|---|---|---|
| Company page | Carousel + Text | Video (company updates) | Polls (brand dilution) |
| CEO | Text + Video script | Comment thread | Too many carousels (feels corporate) |
| COO | Text + Carousel (process/timeline visuals) | Video (site visits) | — |
| CFO | Text + Carousel (deal structure visuals) | — | Video (unless confident on camera) |
| BD | Text + Video (grower testimonials, site visits) | Carousel | — |
| CTO | Text + Carousel (architecture diagrams) | Video (tech deep-dives) | — |

### Account Assignment & Voice (unchanged from v1 but with format layer)

| Co-founder | Domain | Posts About | Persona Focus |
|---|---|---|---|
| CEO | Strategy, vision, market | Grid scarcity, sovereign AI, partnerships | All |
| COO/Ops | Operations, engineering | BESS deployment, DEC construction, timelines | Neocloud, Enterprise |
| CFO/Finance | Project finance, economics | Deal structures, BESS economics, investor context | Institutions |
| BD/Commercial | Partnerships, growers | Grower deals, heat economics, commercial wins | Growers, District Heating |
| CTO/Technical | Technology, power density | GPU architecture, PUE, liquid cooling, grid tech | Neocloud, Enterprise |

### Framework Assignment

| Content Type | Framework |
|---|---|
| Breaking news / regulatory | PAS |
| Market data / statistics | AIDA |
| Case study / deal learning | BAB |
| Partner / milestone | 4Ps |
| Thought leadership / opinion | PAS or AIDA |
| **Carousel / educational** | **AIDA (slide 1 = hook, slides 2-8 = build interest, last slide = CTA)** |
| **Video script** | **BAB (before state → after state → how DE bridges)** |

### Format Rules
- Company page: third person, 3 hashtags, CTA = link/resource. **No external links in text (60% reach penalty) — put links in first comment instead.**
- CEO: first person, max 2 hashtags, CTA = question or "comment [X]"
- Co-founders: first person, domain-specific voice, max 2 hashtags
- All text: max 1,300 chars, Oxford comma, EUR prefix, no banned phrases
- **Carousels: first slide = hook (acts as thumbnail), last slide = CTA + company mention. Max 10 slides.**
- **Video: vertical format preferred, subtitles required, first 3 seconds = hook, no logo intros**

### Content Repurposing Chain

One high-scoring brief (score ≥80) should produce a **full repurposing chain:**

```
1 Source Brief (score ≥80)
  ├── CEO text post (Monday AM)
  ├── Company carousel (Monday PM)
  ├── CTO comment thread deepening the technical angle (Tuesday AM)
  ├── Newsletter snippet (Friday)
  └── BD text post adapting for grower audience (Wednesday)
```

This means 1 great source can fill 5 of the 8 daily slots across different accounts and days. Not every brief gets this treatment — only the top 1-2 per week.

---

## Stage 3: FILTER (07:00-08:30 CET — 4 Sequential Gates)

### Gate A: Brand Compliance Agent (binary pass/fail)

| Check | Pass | Fail Action |
|---|---|---|
| Banned phrases | Zero detected | Auto-fix → recheck |
| Terminology | Correct DE terms | Auto-fix → recheck |
| Currency/format | EUR prefix, Oxford comma | Auto-fix |
| Character count | ≤1,300 (text) / ≤10 slides (carousel) | Send to Writer for rewrite |
| Hashtag count | ≤3 | Auto-trim |
| **External link in post body** | **No external links (company/CEO posts)** | **Auto-move link to "first comment" instruction** |
| **Proof point verification** | **Every number traceable to proof-points.md** | **KILL (non-negotiable)** |
| Confidential data | None detected | KILL |

Pass rate: ~90%

### Gate B: Marketing QA Agent (scored 0-100, pass ≥65)

| Criterion | Weight |
|---|---|
| Hook strength | 25% (surprising number=25, counterintuitive=22, question=20, generic=5) |
| Insight density | 20% (teaches something=20, reports fact=10, restates known=5) |
| CTA quality | 15% (single clear CTA=15, multiple=5, none=0) |
| Persona-message fit | 15% (exact=20, partial=10, mismatch=0) |
| Content calendar fit | 10% (on-calendar=10, adjacent=7, off=3) |
| **Format-channel fit** | **10% (right format for the account and topic=10, suboptimal=5, mismatch=0)** |
| Engagement predictor | 5% (debate-provoking=10, like-worthy=7, ignorable=3) |

*Changed from v1: Added format-channel fit, reduced persona-message and engagement predictor weights.*

Actions: 80-100=PROMOTE, 65-79=PASS, 50-64=RECYCLE (1 rewrite), <50=KILL
Pass rate: ~65%

### Gate C: Product Accuracy Agent (pass/fail per check)

- Technical claims → cross-reference proof-points.md. Inaccurate = KILL
- Regulatory citations → verify dates/implications. Wrong = KILL
- Financial claims → "indicative"/"base case" qualifiers present. Missing = RECYCLE
- Competitive claims → no named competitor pricing. Auto-fix to "market range"
- Project status → verify against current documentation. Overstated = KILL
- **Carousel/video claims → every slide/frame fact-checked individually, not just the summary**

Pass rate: ~85%

### Gate D: Humanizer Agent (rewrite pass)

Detects and fixes AI patterns: generic openings ("In today's rapidly evolving landscape"), filler transitions ("Let's dive in"), excessive hedging ("It's worth noting"), perfect parallel structure, transparent pitch lead-ins ("This is why..."), emoji overuse, generic CTAs ("Feel free to reach out").

**Additional v2 checks:**
- **Carousel slide text**: each slide must read naturally, not like bullet-pointed AI output
- **Video scripts**: conversational cadence, not essay-read-aloud
- **Comment threads**: each comment should feel like a spontaneous follow-up, not a pre-planned series

Max 20% of post altered. If >20% needs rewriting → RECYCLE to Writer.
Pass rate: ~80%

### Cumulative: 30-40 pieces → ~12-15 survivors → top 12-15 to human review

---

## Stage 4: APPROVE (Batched — 2-3x per week, 30-45 min per session)

### Batched Review Design

Human review happens **2-3 times per week** (e.g., Monday, Wednesday, Friday mornings), not daily. Each session reviews 20-30 candidates covering the next 2-3 days of content.

**Why batched works better for DE:**
- Co-founders have 15-30 min/day LinkedIn time — daily approval isn't sustainable
- Batching allows deeper review per post (~2 min each vs ~90 sec in daily model)
- The pipeline produces content continuously; approved posts queue for scheduled publishing
- If a review session is missed, the evergreen buffer fills the gap automatically

**Session structure (30-45 min):**
1. Open review queue sorted by publish date priority (5 min scan)
2. Review each candidate — ~2 min per post for text, ~3 min for carousels (20-30 min)
3. Mark A/B test pairs if applicable (2 min)
4. Quick scan of previous batch's engagement results (5 min)

### Queue Presentation (per post)

| Field | Content |
|---|---|
| Rank | By composite quality score |
| Target account | Company / CEO / [Co-founder] |
| **Format** | **Text / Carousel / Video script / Thread** |
| Full post text/preview | Rendered as LinkedIn preview; carousel slides shown as thumbnails |
| Source + link | Original article that inspired it |
| Pillar + persona | Which messaging pillar and buyer segment |
| Quality scores | Marketing QA score, Gate C/D status |
| Proof points used | Library IDs |
| Suggested publish date + time | Slot from daily schedule, covering next 2-3 days |
| **First comment** | **Pre-written first comment (for link placement, engagement boost)** |
| **Engagement instructions** | **Which 1-2 co-founders should like/comment? (simplified from "all 5")** |

### Reviewer Actions
- **APPROVE** — goes to publish queue for scheduled date/time
- **APPROVE WITH EDIT** — reviewer edits inline, goes to publish queue
- **REJECT** — killed; reviewer selects reason category + optional detail
- **HOLD** — parked for future use (added to evergreen buffer if applicable)
- **A/B TEST** — reviewer marks 2 similar posts for split testing (different days or different accounts)

### Anti-Automation-Bias Measures

Research shows reviewers start rubber-stamping AI output after a few weeks. Countermeasures:

1. **Decoy posts.** 1 in 10 candidates is a deliberately flawed post (subtle inaccuracy, wrong tone, off-brand phrasing). If the reviewer approves it, flag it and remind them to read carefully. This is a calibration tool, not a gotcha.
2. **Rotating review order.** Don't always show highest-scored first. Randomize order to prevent top-of-list bias.
3. **Monthly "cold read."** Once a month, the reviewer sees 5 posts without quality scores or agent recommendations. Forces independent judgment. (Reduced from weekly — batched review means fewer but deeper sessions.)
4. **Rejection rate monitoring.** If the reviewer approves >95% across 3 consecutive sessions, surface a prompt: "Approval rate is very high. Are the posts genuinely that good, or should you calibrate?"

### Feedback Capture (feeds learning loop)
Every decision logged: reason category, detail text, diff of edits, time spent per post. Categories: hook too weak, tone wrong, off-pillar, too promotional, inaccurate, already posted similar, bad timing, wrong format, wrong account.

### Buffer Management Between Review Sessions

| Situation | Action |
|---|---|
| Approved queue runs out before next review | Deploy from evergreen buffer (20-post reserve) |
| Reactive/breaking news between reviews | Fast lane protocol: CEO/reviewer approves single post via Slack/WhatsApp (not a full session) |
| Low-quality batch (>50% rejected) | Reduce to company page posts only until next review; investigate pipeline quality |

---

## Stage 5: PUBLISH (3 time slots)

### Daily Schedule

| Slot | Time | Account | Content Type | Format Priority |
|---|---|---|---|---|
| 1 | 07:00-07:30 | CEO personal | Thought leadership | Text or video |
| 2 | 08:00-08:30 | Company page | Industry data | **Carousel or document** |
| 3 | 08:30-09:00 | Co-founder 2 (COO) | Ops/technical | Text |
| 4 | 14:00-14:30 | Company page | News/event/team | Text or video |
| 5 | 14:30-15:00 | Co-founder 3 (CFO) | Finance/economics | Text or carousel |
| 6 | 15:00-15:30 | Co-founder 4 (BD) | Commercial/grower | Text or video |
| 7 | 15:30-16:00 | Company page | Thought leadership | **Carousel** |
| 8 | 16:00-16:30 | Co-founder 5 (CTO) | Technical/infra | Text or carousel |

**Weekly format targets:** Of 40 posts/week, at least 8 should be non-text (carousels, videos, document posts). Target: 20% non-text minimum.

### Cross-Engagement Protocol (Simplified for 15-30 min/co-founder/day)

The v3 protocol required 40+ engagement actions per co-founder per day. That's impossible in a 15-30 minute budget. Simplified version:

**Automated (zero co-founder effort):**
- Scheduled tool auto-likes each new post from all 5 other accounts (immediate)
- First comment with link auto-posted by scheduling tool 15 min after publish

**1-2 co-founders per post (pre-assigned, 2-3 min effort each):**
- The most relevant 1-2 co-founders leave a substantive comment on each post within 1-2 hours of publishing
- This is their primary daily LinkedIn task — ~3-4 comments per day, taking 10-15 min total

**Company page reshare:**
- Company page reshares 1 co-founder post per day with brief commentary (automated with pre-written text from the review batch)

**Why this still works:** Employee reshares reach significantly further than company page alone — [Sourced] MSLGroup (2013) found 561% amplification, though modern estimates are 2-10x [Directional]. Early substantive comments from co-founders still trigger algorithmic amplification. [Directional] The key signal is conversation quality, not the number of accounts engaging. 1-2 thoughtful comments from domain experts > 5 forced generic interactions.

**Comment templates per co-founder (for cross-engagement):**
- CEO on CTO post: strategic implication ("This is exactly why we chose liquid cooling for [project]...")
- CTO on CEO post: technical depth ("To add context: the 60 GW queue means...")
- CFO on BD post: economics angle ("The unit economics on this are compelling because...")
- BD on CFO post: market reality ("We're seeing this exact pattern with 3 growers this quarter...")

These should feel genuine, not scripted. The Humanizer Agent reviews cross-engagement comments too.

**Co-founder daily LinkedIn time budget (15-30 min):**

| Activity | Time | Frequency |
|---|---|---|
| Review & approve 1-2 posts from their account (in batched session) | 5-10 min | 2-3x/week |
| Write 2-3 cross-engagement comments on others' posts | 10-15 min | Daily |
| Reply to comments on their own posts | 5-10 min | Daily |
| **Total daily** | **15-25 min** | — |

### Overlap Prevention
- No same-source posts within 4 hours
- No same-pillar back-to-back on any account
- Same source brief → max 2 accounts per day (different angles and formats)
- Weekly: each of 5 pillars appears in ≥3 posts, none exceeds 40%
- **No more than 1 company reshare of co-founder content per day**

### Fallback Protocol

| Gap | Action |
|---|---|
| 1-2 short | Pull from HOLD queue |
| 3-4 short | Reduce to 6 posts; drop lowest-priority co-founder slots |
| 5+ short | Reduce to 4 posts (2 company + 2 CEO); investigate pipeline |
| Source drought | Deploy from 20-post evergreen buffer (90-day reuse cooldown) |

---

## Stage 6: ENGAGE (All Day — NEW)

**Agent:** Engagement Monitor Agent
**Runs:** Continuously from 07:00-18:00 CET

This is the biggest gap v1 had. Publishing without engaging is like throwing a party and leaving.

### Comment Monitoring

| Trigger | Action | Agent/Human |
|---|---|---|
| Any comment within 60 min of posting | Draft reply, send to poster's queue for approval | Agent drafts, human approves (initially) |
| Comment with buying signal ("How much?", "Do you work with [sector]?", "We're looking for...") | **Alert BD/CEO immediately + draft DM** | Agent flags, human sends DM |
| Comment with objection or criticism | Draft measured response, flag for human review | Agent drafts, human must approve |
| Comment from high-value account (>10K followers, C-suite at target company) | **Priority alert + suggested reply + DM suggestion** | Human handles personally |
| Negative/hostile comment | Flag but do NOT auto-reply. Human decides response strategy. | Human only |
| Generic praise ("Great post!", emoji-only) | Auto-like the comment. No reply needed. | Agent auto-responds |

### Comment-to-DM Pipeline

Warm DMs (sent after someone has already engaged with your content) achieve significantly higher response rates than cold outreach — [Directional] 25-45% response rate for warm DMs vs. 5-15% for cold. Comment-triggered DMs (where the person showed buying intent) can reach 50-75% response rates. When a comment shows buying intent:

```
1. Comment detected with buying signal keywords
2. Agent classifies: [Hot lead / Warm interest / Info request / Noise]
3. For Hot/Warm: Agent drafts personalized DM referencing the comment
4. DM sent 5-15 min after comment (not instantly — feels more natural)
5. DM format: acknowledge their comment → offer specific value → single CTA
6. All DMs logged in CRM with source attribution (which post, which comment)
```

**DM template example:**
> Thanks for your comment on [topic]. We actually just completed a similar analysis for [relevant context]. Happy to share the data — want me to send over the one-pager?

**Rules:**
- Keep automated DM volume conservative — LinkedIn prohibits automated messaging per ToS, so all DMs should be human-sent or human-approved. [Corrected: there is no official "3 per day" LinkedIn limit. The actual risk is behavioral pattern detection. Conservative recommendation: max 10-15 manual DMs per account per day, spread across the day.]
- Never pitch in first DM — always offer value
- If no response to DM, no follow-up. One shot.
- All DMs human-approved until graduation (same criteria as posts)
- **Lead magnet delivery:** When someone DMs a keyword (e.g., "HEAT"), the response + asset attachment must be sent manually or via a pre-configured auto-response. Budget 15-20 min/day for lead magnet fulfillment as volume grows.

### Reply Tone Rules
- Match the commenter's energy level
- If they're casual, be casual. If they're technical, go deep.
- Never defensive. Acknowledge valid criticism directly.
- Keep replies ≤3 sentences unless the question demands more
- Always end with either a question (to continue the thread) or a clear answer (to close it)

---

## Stage 7: ANALYZE (Weekly — NEW)

**Agent:** Performance Analyst Agent
**Runs:** Every Monday 06:00 CET
**Output:** Weekly performance report + scoring recalibration recommendations

### Metrics Tracked (per post, per account, per pillar, per format)

| Metric | Source | Why It Matters |
|---|---|---|
| Impressions | LinkedIn Analytics | Raw reach |
| Engagement rate | (Likes + Comments + Shares) / Impressions | Quality of reach |
| Dwell time proxy | Engagement rate + comment length | LinkedIn's #1 ranking signal |
| Click-through rate | Link clicks / Impressions | Action conversion |
| Comment quality | Substantive (>20 words) vs generic | Algorithm favors conversation quality |
| Follower growth (net) | LinkedIn Analytics | Audience building |
| Profile visits | LinkedIn Analytics | Interest signal |
| DM conversion rate | DMs sent / Leads generated | Stage 6 effectiveness |
| **Post-to-meeting rate** | Meetings booked attributable to LinkedIn | Ultimate ROI metric |

### Weekly Report Structure

```
WEEKLY SMM PERFORMANCE — Week of [Date]
=========================================

HEADLINE METRICS
  Posts published: 40 (target: 40)
  Total impressions: [X]
  Avg engagement rate: [X]% (target: >3%)
  Comments: [X] (of which [X] substantive, [X] buying signals)
  DMs sent: [X] → Leads: [X] → Meetings: [X]
  Follower growth: +[X] (company), +[X] (CEO), etc.

TOP 5 POSTS (by engagement rate)
  1. [Post ID, account, format, pillar, engagement rate, why it worked]
  ...

BOTTOM 5 POSTS (by engagement rate)
  1. [Post ID, account, format, pillar, engagement rate, diagnosis]
  ...

FORMAT PERFORMANCE
  Text: [avg engagement]  |  Carousel: [avg engagement]  |  Video: [avg engagement]

PILLAR PERFORMANCE
  Grid Scarcity: [X]%  |  Waste Heat: [X]%  |  Sovereign AI: [X]%  |  Speed: [X]%  |  Finance: [X]%

SCORING RECALIBRATION RECOMMENDATIONS
  [Specific adjustments to Scout scoring, Marketing QA weights, or format allocation]

NEXT WEEK PRIORITIES
  [Suggested pillar emphasis, format experiments, A/B tests to run]
```

### A/B Testing Framework

Each week, run 2-3 controlled experiments:

| Test Type | Method | Measure |
|---|---|---|
| Hook A vs Hook B | Same content, different opening line, posted on different days from same account | Engagement rate |
| Format A vs Format B | Same topic as text post vs carousel, different accounts or days | Engagement + dwell |
| Framework A vs B | Same source, PAS version vs AIDA version | Approval rate + engagement |
| Time slot A vs B | Same post type, morning vs afternoon | Impressions + engagement |

**Rules:**
- Only 1 variable changes per test
- Minimum 5 posts per variant before drawing conclusions
- Results feed directly into scoring recalibration
- Reviewer marks A/B pairs at Stage 4 (APPROVE) — this is intentional, not random

---

## Reactive Fast Lane (NEW)

Breaking news can't wait until tomorrow's 05:00 scout cycle. The fast lane operates on demand:

```
TRIGGER: Team member spots breaking news relevant to DE
  ↓
FAST SCOUT: 10-minute scoring (abbreviated rubric: pillar match? timely? proof points available?)
  ↓
FAST DRAFT: Writer Agent generates 2 variants (CEO + Company) within 15 min
  ↓
FAST FILTER: Gate A (brand compliance) + Gate C (product accuracy) only. Skip Marketing QA and Humanizer.
  ↓
FAST APPROVE: CEO/marketing lead approves via mobile (Slack/WhatsApp notification)
  ↓
PUBLISH: Within 1-2 hours of the news breaking
```

**Rules:**
- Max 2 reactive posts per day (protect the scheduled calendar)
- Reactive posts replace the lowest-priority scheduled post for that slot
- Reactive posts still get logged for learning loop analysis
- If CEO is unavailable for fast approval, the post waits — never auto-publish reactive content

---

## X (Twitter) Channel Strategy

### Philosophy: LinkedIn First, X Second

X is not a separate content engine — it's a **distribution amplifier** for content already produced by the LinkedIn pipeline. Starting from near-zero on both platforms, splitting focus equally would dilute both. Instead:

- **Month 1:** LinkedIn only. Build the pipeline, prove the content quality, establish posting cadence.
- **Month 2+:** Begin X cross-posting for top-performing LinkedIn content (see implementation sequence).
- **Month 4+:** If X shows traction, develop X-native content (not just cross-posts).

### Volume Targets

| Phase | LinkedIn | X | X Source |
|---|---|---|---|
| Phase A (Weeks 1-4) | 4 posts/day | 0 | — |
| Phase B (Month 2-3) | 8 posts/day | 3-5 posts/day | Adapted from top LinkedIn content |
| Phase C (Month 4+) | 8 posts/day | 5-8 posts/day | Mix of cross-posts + X-native threads |

### X Format Adaptations

LinkedIn content does NOT copy-paste to X. Key differences:

| LinkedIn | X Adaptation |
|---|---|
| 1,300-char text post | Break into 3-5 tweet thread (280 chars per tweet) |
| Carousel (PDF) | Thread with images, or link to carousel hosted on LinkedIn/website |
| Video (vertical, 30s-2min) | Clip to <60 sec, horizontal/square format, auto-play optimized |
| Comment thread (self-replies) | Natural fit — becomes an X thread |
| Poll | X polls (native) — actually work better on X than LinkedIn |
| First comment with link | Link in last tweet of thread, or pinned reply |

### X-Specific Tone Adjustments

| LinkedIn Voice | X Voice |
|---|---|
| Professional, measured, detailed | Sharper, punchier, more direct |
| "Here's what this means for your business" | "This changes everything. Here's why →" |
| Paragraphs with white space | Single-line punchy statements |
| Industry jargon with context | Jargon-light, accessible to broader audience |
| 3 hashtags max | 1-2 hashtags or none (X penalizes hashtag overuse) |
| Oxford comma, formal | Can be more casual, emoji-light |

### Account Strategy for X

| Account | X Presence | Why |
|---|---|---|
| Company (@DigitalEnergyNL or similar) | Active from Month 2 | Brand presence, retweets co-founder content |
| CEO | Active from Month 2 | X rewards opinionated voices more than LinkedIn does |
| Other co-founders | Optional, Month 4+ | Only if they show interest; don't force 5 X accounts |

### Cross-Posting Rules

1. **Never copy-paste LinkedIn text to X** — always adapt format and tone
2. **Wait 2-4 hours** after LinkedIn publish before posting X version (avoid appearing robotic)
3. **Only cross-post top performers** — posts scoring >75 in Marketing QA, not everything
4. **X-first for breaking news** — X's real-time nature means reactive content should hit X first, then LinkedIn (reverse the normal flow)
5. **Track separately** — X engagement metrics feed into Stage 7 ANALYZE but don't influence LinkedIn scoring rubrics

### X Safety Limits

| Limit | Threshold | Notes |
|---|---|---|
| Tweets per day per account | Max 5-8 | X is more permissive than LinkedIn on volume |
| Threads per day | Max 1-2 | Threads = X's equivalent of long-form content |
| No automated follows/unfollows | Zero | X aggressively detects and bans automation |
| Direct messages | Conservative, same as LinkedIn approach | Human-sent, value-first |

### What This Section Doesn't Cover Yet

- X Ads / paid amplification strategy (add when organic shows traction)
- X Spaces (live audio) — potential equivalent of LinkedIn Live
- X Lists for community monitoring
- Integration with X API for automated posting (Buffer supports X scheduling)

---

## Learning Loop & Graduated Autonomy

### Phase 1: Data Collection (Weeks 1-8)
Log every approve/reject/edit + LinkedIn engagement (impressions, engagement rate, CTR) at 48 hours post-publish. Log every cross-engagement action and its effect on post performance.

### Phase 2: Pattern Extraction (Weeks 4-12)
After 160+ approved posts:
- Which hooks, pillars, frameworks, proof points win?
- Which co-founder voices need recalibration?
- **Which formats outperform on which accounts?**
- **Which cross-engagement combinations amplify most?**
- **What comment-to-DM conversion rate are we achieving?**

### Phase 3: Scoring Recalibration (Weeks 8-16)
Adjust Marketing QA rubric based on actual approval/engagement correlation. Target: r > 0.6 by week 12.

**Specific recalibration mechanisms:**
- If carousels consistently outperform text but the Marketing QA agent scores them lower → increase format-channel fit weight
- If certain hook types that score low actually drive high engagement → update hook strength scoring
- If a specific co-founder's posts get edited >30% of the time → voice model needs retraining with the edited versions as new ground truth

### Phase 4: Graduation Criteria

| Metric | Threshold | Result |
|---|---|---|
| Approval rate >90% for 4 weeks | 90%+ | Reviewer switches to exception-only review |
| QA-engagement correlation >0.65 | r>0.65 | Marketing QA trusted for go/no-go |
| Zero fabricated numbers for 8 weeks | 0 incidents | Product checks run async |
| Edit rate <10% for 4 weeks | <10% | Humanizer calibrated |
| Engagement within 20% of predicted, 80%+ of posts | 80%+ | Company page can auto-publish |
| **Comment reply approval rate >95% for 4 weeks** | **95%+** | **Comment replies can auto-publish (non-buying-signal only)** |

**Hard rules:**
- Company page: auto-publish possible at 4-6 months
- CEO account: **NEVER** auto-publish (always human-reviewed)
- Other co-founders: auto-publish only after company page graduates AND their individual approval rate hits 95% for 8 weeks
- **DMs: NEVER auto-send without human approval. Too high-risk.**
- **Reactive posts: NEVER auto-publish. Always fast-approve.**

---

## Risk Controls

### Always Require Human Review (regardless of graduation)
- Financial projections (IRR, returns, investment amounts)
- Named partners/customers (Lenovo, Nokia, specific growers)
- Future regulatory claims ("Wcw WILL require...")
- Competitive comparisons
- Hiring/team announcements
- Project milestone claims
- Crisis/incident responses
- **All DMs (buying-signal or otherwise)**
- **All reactive/breaking news posts**
- **Any post referencing a specific person or company not in the pre-approved list**

### Compliance Guardrails (embedded in agents)
- No guaranteed returns language → KILL
- "Indicative"/"base case" qualifiers required on forward-looking claims
- Three-scenario discipline (conservative/base/optimistic)
- **No fabrication = hardest kill rule in the pipeline**

### LinkedIn Safety Limits (Corrected)

| Limit | Threshold | Source | Consequence of Exceeding |
|---|---|---|---|
| Posts per account per day | Max 2 (co-founders), Max 3 (company) | [Benchmark — widely confirmed] | Account throttling, reduced reach |
| Connection requests per day | 20-25 max (LinkedIn's own limit as of 2022+) | [Sourced — LinkedIn reduced from ~100 to ~20-25/week] | Account restriction |
| DMs per day per account | Max 10-15 manual (no automated DMs per ToS) | [Corrected — "Max 3" was false. LinkedIn has no official per-day limit but detects automated patterns. 10-15 manual DMs is conservative-safe.] | Account restriction if automated patterns detected |
| Comments per day per account | No hard limit, but vary content and pacing | [Corrected — "Max 20" was unverifiable. Power users post 30+ comments/day without restriction. Spam detection is pattern-based (repetitive/generic), not count-based.] | Spam detection if comments are generic/repetitive |
| **No activity between 23:00-05:00 CET** | Zero automated actions overnight | [Best practice — reduces bot detection risk] | Bot detection avoidance |

### Crisis Safeguards
- Negative press about DE → ALL posts PAUSED, human reviews within 1 hour
- Industry crisis → ALL posts PAUSED for review
- Regulatory surprise → affected-regulation posts HELD
- Engagement blow-up → no auto-response, flag to CEO
- **LinkedIn account restriction on any account → ALL automation paused for that account for 48 hours, human-only posting**

### Content Staleness Rules
- Proof points audited quarterly; >12 months without verification = flagged
- Regulatory date references checked against current date
- Market data (CBRE, BNEF) tagged with report date; >12 months = "stale"
- Evergreen buffer: 90-day reuse cooldown, 180-day accuracy re-review

---

## Tooling Architecture (NEW)

### Recommended Stack

| Layer | Tool | Why | Cost Estimate |
|---|---|---|---|
| **Orchestration** | **n8n (self-hosted)** | Source-available (Sustainable Use License, not OSI open source), ~50-60 LangChain integration nodes [Directional], no per-execution pricing on self-hosted. Requires custom integration work to call CrewAI/LangGraph as external services via HTTP or Execute Command nodes — no native first-class integration. | Free (self-hosted) + server costs |
| Agent framework | **CrewAI** | Role-based sequential pipeline is literally its core design. Has short-term, long-term, and entity memory systems — useful for context retention across executions, though not a true ML-based "learning loop" (it's retrieval of past context, not adaptive learning). Manual prompt tuning still needed. | Free (open source) |
| LinkedIn scheduling | **Buffer** (recommended) or **Hootsuite** | Buffer supports multi-account LinkedIn management with API access, team collaboration, and approval workflows. ~$36-72/month for 6 accounts. **NOT Taplio** — Taplio is a single-user tool at $49-149/month PER account with no multi-account dashboard. | ~$50-70/month |
| Analytics | **Shield Analytics** + LinkedIn native | Shield tracks all 6 accounts in one dashboard (~$150/month for 6 profiles on Team plan). **Important limitation:** Shield provides standard metrics only (impressions, engagement rate, follower growth). It does NOT provide dwell time data, comment quality scoring, or sentiment analysis. Any advanced analytics (dwell time proxies, comment quality classification) must be built as a custom layer in the n8n/CrewAI pipeline. | ~$150/month |
| Review queue | **Notion database** (week 1-4) → **Custom Retool app** (month 2+) | Notion is fast to set up for batched review. Retool (~$20-30/month) is better for the structured approval workflow with RBAC, A/B marking, and feedback capture. | Free → ~$25/month |
| CRM integration | **HubSpot** (existing, fully configured) | Comment-to-DM leads flow into existing pipeline. Source attribution from post ID. Lead scoring properties to be added. | Existing |
| Content storage | **Airtable** or **Notion** | Post library, evergreen buffer, hold queue, A/B test log. | Free tier likely sufficient |
| Attribution | **Fibbler** (~$89-149/month, verify current pricing) or **Dealfront/Leadfeeder** | Fibbler syncs LinkedIn *paid ad* data to HubSpot contacts. **Critical correction:** there is no "LinkedIn Company Intelligence API" — Fibbler uses the LinkedIn Marketing API. For *organic* post attribution, Fibbler has limitations; you need UTM tracking + website visitor identification (Dealfront) as supplements. | ~$100-200/month |
| Crisis monitoring | **Brand24** (~$119-399/month) or **Mention** (~$49-179/month) | Adequate for general brand monitoring. **Limitation:** neither specializes in energy industry sources (regulatory filings, trade publications). Consider supplementing with Google Alerts for specific Dutch energy regulatory terms. | ~$100-200/month |

**Total estimated monthly tooling cost:** ~$500-850/month (excluding n8n server costs)

### Alternative: Full n8n stack

If budget is tight, n8n can handle orchestration + scheduling + review queue + analytics aggregation in one platform. The trade-off is more setup time but lower ongoing cost and no per-seat SaaS fees. Buffer for scheduling ($50-70/month) + Shield for analytics ($150/month) are the hardest to replace with n8n alone.

---

## Implementation Sequence

### Week 1: Foundation
1. Finalize 5 co-founder voice profiles (3 example posts each, 1 carousel example each)
2. Build source feed list (RSS, monitoring queries per 7 categories, LinkedIn social listening setup)
3. Write 20 evergreen buffer posts (4 per pillar) — include 5 carousels
4. Set up n8n instance + Buffer (multi-account scheduling) + Shield Analytics
5. Set up review queue in Notion (Kanban: Scout → Draft → Filter → Approve → Publish → Analyze)
6. **Audit existing DE assets → map 2-3 as lead magnets with DM keyword triggers**
7. Write cross-engagement comment templates per co-founder pair (10-15 templates — simplified from 20)
8. Configure HubSpot: add LinkedIn source attribution properties, lead scoring rules, UTM tracking

### Week 2: Pilot (Phase A launch — 4 posts/day)
1. Run full pipeline manually once — humans play each agent role
2. Calibrate Scout scoring and Marketing QA weights
3. **Launch at Phase A volume: 4 posts/day (2 company + 1 CEO + 1 rotating co-founder)**
4. First batched review session: reviewer approves 12-15 posts covering the week
5. Test cross-engagement protocol: 1-2 co-founders comment per post (within 15-30 min budget)

### Weeks 3-4: Phase A Stabilization
1. Maintain 4 posts/day, refine based on first 2 weeks of data
2. Activate Stage 6 (Engage) with human-approved replies
3. Begin learning loop data collection
4. First weekly Stage 7 report (even with limited data — establish the habit)
5. **Test 1 lead magnet CTA post per week — measure DM volume**
6. **Activate reactive fast lane (CEO fast-approves via Slack)**

### Month 2: Scale to Phase B (8 posts/day)
1. If Phase A approval rate >70% and co-founders report sustainable workload → scale to 8 posts/day
2. All 6 accounts now active daily
3. Increase review batch size to 25-30 posts per session
4. Begin A/B testing (1 experiment per week to start)
5. Evaluate first month's engagement data: which pillars/formats/accounts perform?
6. **Launch X (Twitter) cross-posting for top-performing LinkedIn content (see X Channel section)**

### Month 3: Optimization
1. First pattern report: which hooks/pillars/frameworks/formats win?
2. Recalibrate scoring rubrics based on engagement data
3. Expand source feeds based on brief quality data
4. **Migrate review queue from Notion to Retool**
5. Scale A/B testing to 2-3 experiments per week
6. Evaluate comment-to-DM conversion rate; adjust DM templates and lead magnet CTAs
7. **First lead gen report: DMs → HubSpot → meetings attribution**

### Month 4-6: Graduation
1. Evaluate graduation criteria for company page
2. Graduate company page to auto-publish with exception review
3. Graduate non-buying-signal comment replies to auto-publish
4. Maintain human review for all personal accounts and DMs
5. **Produce first quarterly report comparing AI pipeline performance vs manual baseline**
6. **If LinkedIn pipeline is producing: evaluate expanding X volume**

---

## Virality Engine

The pipeline produces content. The Virality Engine ensures that content reaches the maximum possible audience. This is not about "going viral" — it's about systematically engineering every post for maximum algorithmic amplification and organic spread.

### The Viral Coefficient (K-Factor)

Every post has a measurable viral coefficient:

**K = Impressions per Follower x Engagement Rate x Share Rate x Follower Conversion Rate**

| K Value | What It Means | DE Target |
|---|---|---|
| K < 0.1 | Linear growth. Treadmill — reach dies when you stop posting. | Avoid |
| K = 0.1-0.4 | Moderate amplification. Posts reach beyond immediate network. | Acceptable (most posts) |
| K = 0.5-0.7 | Strong compounding. Posts reach 2nd and 3rd degree connections. | Target (top 20% of posts) |
| K > 0.7 | Exponential flywheel. Self-sustaining reach. | Rare — celebrate and reverse-engineer when it happens |

**Track K-factor per post type, per account, per format.** The Stage 7 ANALYZE report should include K-factor analysis weekly. Double down on whatever produces K > 0.5.

### 5 Virality Archetypes

Every post should be designed using one of these archetypes. Each triggers different psychological sharing mechanisms:

#### 1. Framework Loop (Target: 3-5% save rate)

**Pattern:** Problem → Systematic solution → Application template
**Why it spreads:** Saves = algorithmic gold (LinkedIn weights saves heavily). People save frameworks to reference later and share with teams.
**DE application:** "The 4-Stack BESS Revenue Model" carousel. "The Grid Queue Decision Matrix." "3 Questions Every Grower Should Ask Before Signing a Heat Contract."
**Weekly allocation:** 35% of posts — the workhorse

#### 2. Contrarian Loop (Target: 3-5% share rate, high debate)

**Pattern:** Challenge conventional wisdom with data → Defend position → Invite counterargument
**Why it spreads:** Disagreement drives comments. Comments drive impressions. People share to say "see, I told you!" or "this is wrong because..."
**DE application:** "Everyone says the Dutch grid is broken. I think it's working exactly as designed — and here's why that's worse." / "Waste heat isn't free energy. It's better than free energy. Here's the math."
**Weekly allocation:** 10% — use sparingly, but these are the posts that break out

#### 3. Credibility Loop (Target: 1-2% DM rate from qualified prospects)

**Pattern:** Milestone + Transparency about how + Lessons learned
**Why it spreads:** Demonstrates competence without bragging. Attracts inbound from people who want similar results.
**DE application:** "We just secured our third grid connection in Zuid-Holland. Here's what we learned about the process that nobody tells you." / "Our first BESS unit hit 95% availability in month 1. Here's what almost went wrong."
**Weekly allocation:** 10% — only when there's a real milestone

#### 4. Relatability Loop (Target: 8-12% engagement rate)

**Pattern:** Personal struggle → Insight → Validation of audience's unspoken frustration
**Why it spreads:** People engage when they feel seen. Comments like "This is exactly my experience" drive algorithmic amplification.
**DE application:** CEO: "I spent 18 months trying to get a grid connection. Here's what that process actually looks like." / BD: "A grower told me last week: 'I've heard this pitch before.' Here's what we said that was different."
**Weekly allocation:** 25% — second most common, especially on co-founder accounts

#### 5. Community Loop (Target: 10-15% comment rate)

**Pattern:** Expert question drawing network wisdom → Curate responses → Follow-up post
**Why it spreads:** Low-risk way for people to participate visibly. Commenting positions the reader as knowledgeable.
**DE application:** "What's the biggest bottleneck in Dutch energy infrastructure right now? I'll compile the top answers into a follow-up post." / "CTO friends: what PUE are you actually achieving in liquid-cooled deployments? (Not the spec sheet — the real number.)"
**Weekly allocation:** 20% — drives the most comments per post

**Archetype assignment in Stage 2 (DRAFT):** The Writer Agent tags each draft with its virality archetype. The Marketing QA Agent (Gate B) evaluates whether the archetype was executed correctly — a Framework Loop post that doesn't include a saveable framework fails the gate.

### How Post Types and Virality Archetypes Interact

The 7 Post Types (Stage 2) define **what** the content is about. The 5 Virality Archetypes define **how** the content is constructed for maximum spread. They are two independent classification layers — every post has both a Type and an Archetype.

**Mapping: which archetypes work best for which post types:**

| Post Type | Natural Archetype(s) | Avoid |
|---|---|---|
| Industry News Commentary | Contrarian Loop, Framework Loop | Relatability Loop (news isn't personal) |
| Company News & Updates | Relatability Loop, Credibility Loop | Contrarian Loop (don't debate your own news) |
| Achievements/Milestones | Credibility Loop | Community Loop (milestone ≠ question) |
| Thought Leadership | Contrarian Loop, Framework Loop, Relatability Loop | — (most flexible type) |
| Promotional / CTA-Heavy | Framework Loop (wrap CTA in useful framework) | Community Loop, Contrarian Loop |
| Educational / How-To | Framework Loop (primary), Community Loop | Contrarian Loop (educators shouldn't provoke) |
| Engagement / Community | Community Loop (primary), Relatability Loop | Framework Loop (too structured for casual tone) |

**The Writer Agent assigns both tags.** The weekly mix compliance check validates both dimensions: "Do we have enough Post Type diversity?" AND "Do we have enough Archetype diversity?" If 80% of posts this week are Framework Loops, the mix is stale regardless of Type distribution.

### Golden Hour Orchestration (First 60 Minutes)

LinkedIn's algorithm tests content with 2-5% of your network first. If early engagement is weak, the post dies. If strong, it amplifies to 20-40% of network, then beyond.

**The DE Golden Hour Protocol (simplified for 15-30 min/co-founder/day):**

| Minute | Action | Who | Effort |
|---|---|---|---|
| 0 | Post goes live | Automated (scheduling tool) | Zero |
| 0-5 | Auto-like the post | All other DE accounts (automated) | Zero |
| 15 | Post first comment with link (if applicable) | Automated (pre-written in review batch) | Zero |
| Within 1-2 hours | 1-2 most relevant co-founders post substantive comment | Pre-assigned during review session | 2-3 min each |
| Within 2 hours | Author replies to co-founder comments | Author account | 2-3 min |
| Same day | Company page reshares 1 co-founder post (1x/day max) | Automated with pre-written commentary | Zero |
| Ongoing | Monitor for external comments, reply within 2-4 hours | Engagement Monitor Agent (Stage 6) drafts, human approves | 5 min/day |

**What changed from v3:** The v3 protocol demanded 5 co-founders engaging within 15 minutes of every post — physically impossible with 15-30 min daily budgets across 8 posts. The v4 protocol automates the low-effort actions (likes, first comments) and requires only 1-2 co-founders to comment per post, spread across the first 1-2 hours rather than the first 15 minutes.

**The algorithm still benefits because:** [Directional] LinkedIn's algorithm favors early engagement, but the exact time window is not confirmed. Quick replies to comments and substantive conversation matter more than speed-of-first-like. The author reply rate within the first few hours is a strong signal — not necessarily within 15 minutes (the "90% boost for 15-min reply" claim has no traceable source).

**Rules:**
- Cross-engagement comments must pass Gate D (Humanizer) — no generic "Great post!" patterns
- Each co-founder has 2-3 pre-written comment templates per other co-founder, refreshed monthly
- If a post gets organic traction (>50 reactions in first 2 hours), alert team to prioritize engagement on that post

### Dwell Time Optimization

Dwell time — how long someone spends on your post before scrolling — is a significant LinkedIn ranking signal. [Sourced — LinkedIn Engineering Blog, 2020, confirmed dwell time as an important feed ranking factor. Note: LinkedIn has never confirmed it as THE #1 signal; it's one of many factors including relevance, connection strength, engagement velocity, and content type preferences.]

**Tactics embedded in Stage 2 (DRAFT) instructions:**

| Tactic | How | Impact |
|---|---|---|
| **Hook + space** | First line = hook. Then blank line. Forces "see more" click = dwell time counted. | Significantly more impressions [Directional — widely reported by practitioners but no rigorous study quantifies the exact lift] |
| **Micro-paragraphs** | 1-2 sentences per paragraph. White space slows reading = more dwell. | Higher dwell per impression [Directional] |
| **Numbered lists** | People read lists to completion. 5-7 items optimal. | Extends reading time [Directional] |
| **Embedded question mid-post** | Ask a question in the middle, not just at the end. Reader pauses to think = dwell. | Higher comment rate [Directional] |
| **Carousel length** | 7-10 slides optimal. Each slide swipe = engagement signal + dwell. | Carousels avg 5-8% engagement vs 3-4% text [Benchmark — Social Insider, van der Blom] |
| **Video first 3 sec** | Surprising visual or text overlay. No logo intros. Silent-first (subtitles). | Higher completion rate for short videos [Directional — specific "200%" claim is unverified] |
| **Comment thread depth** | Post + 3-5 self-replies with escalating insight. Each click to expand = dwell. | Extends total engagement window [Directional] |

### Save-Trigger Patterns

Saves are the most underrated engagement metric. LinkedIn's algorithm weights saves heavily because they indicate long-term value.

**Content patterns that trigger saves:**

| Pattern | Example | Post Type |
|---|---|---|
| **Reference data** | "BESS economics in NL: the numbers you need" with specific EUR/MWh, IRR ranges | Educational |
| **Checklists** | "10-point due diligence checklist for grid connection contracts" | Educational |
| **Comparison tables** | "Gas vs. waste heat: total cost over 15 years for a 10-ha greenhouse" | Industry News |
| **Frameworks with blanks** | "The [X] Stack Revenue Model — fill in your own numbers" | Thought Leadership |
| **Unpopular truth + data** | "Why 90% of Dutch BESS projects will fail (and the 3 things that prevent it)" | Contrarian Loop |

**Writer Agent instruction:** For every Educational and Thought Leadership post, include at least one "save-worthy" element — a number, a framework, a checklist, or a comparison that the reader would want to reference later. If the post has nothing worth saving, it's not worth posting.

### Comment Depth Tactics

Comments are the second most powerful engagement signal. But not all comments are equal — LinkedIn's algorithm distinguishes substantive (>20 words) from generic ("Great post!").

**Tactics to drive substantive comments:**

| Tactic | How | When to Use |
|---|---|---|
| **Binary choice** | "Which is a bigger risk: grid congestion or permitting delays? Comment A or B." | Community Loop posts |
| **Fill-in-the-blank** | "The most underestimated challenge in Dutch energy transition is ___." | Community Loop |
| **Specific experience ask** | "If you've deployed BESS in NL, what was your actual vs. projected availability?" | Community Loop (CTO account) |
| **Mild controversy** | "I think the Netherlands should stop building gas plants entirely. Here's why." + data | Contrarian Loop |
| **Tag invitation** | "Tag someone building energy infrastructure in NL who should see this." | Any post type, use sparingly (max 1x/week) |
| **Promise a follow-up** | "I'll compile the best answers into a follow-up post next week with attribution." | Community Loop — this is a growth loop in itself |

---

## Growth Loops

The pipeline in Stages 1-7 is a production engine. Growth loops turn that engine into a flywheel that compounds over time. The difference: a production engine stops when you stop feeding it. A flywheel accelerates.

### Why Loops, Not Funnels

A funnel is linear: impressions → engagement → followers → leads → customers. Every stage loses people. You need constant top-of-funnel investment to maintain output.

A growth loop is circular: the output of one cycle becomes the input of the next, with amplification at each turn. Three loops power DE's SMM system:

### Loop 1: Content Flywheel

```
Post high-value content
  → Audience engages (comments, shares, saves)
    → Algorithm amplifies to 2nd/3rd degree connections
      → New followers discovered DE
        → Larger audience for next post
          → More engagement per post
            → Stronger algorithmic signal
              → Even broader amplification
                → [loops back with compound growth]
```

**Acceleration levers:**
- Every 100 new followers = ~5-15% more baseline impressions per post
- Cross-engagement from 6 accounts multiplies this by 3-5x (561% employee reshare amplification)
- Save-worthy content gets resurfaced by LinkedIn algorithm days/weeks later (second-life amplification)

**Measurement:** Track impressions-per-follower ratio weekly. A healthy flywheel shows this ratio stable or increasing. If it's declining, content quality or algorithmic fit is degrading.

**KPI target:** Impressions-per-follower > 2.0 combined across all accounts [Directional — reasonable for combined personal+company, but set separate targets: personal accounts > 3.0, company page > 1.0. Note: this metric is more useful as a trend indicator than an absolute number. If it's declining week-over-week, content quality or audience fit is degrading.]

### Loop 2: Employee Advocacy Multiplier

```
Co-founder posts from personal account
  → Reaches personal network (65% of feed = personal profiles)
    → Network engages with co-founder
      → Some visit DE company page / other co-founder profiles
        → Company page gains followers who now see company posts
          → Company posts get higher baseline engagement
            → Company reshares of co-founder content reach larger audience
              → Co-founder gains new followers from company audience
                → [loops back — co-founder reach grows, company reach grows]
```

**The employee advocacy effect:** [Directional] Multiple studies confirm that employee sharing dramatically amplifies brand reach — LinkedIn's own data shows employee networks have 10x more connections than company page followers. The commonly cited "3% of employees → 30% of engagement" and "20% revenue growth" originate from separate studies (LinkedIn/Hinge Marketing and Social Media Today respectively) and were later conflated into a single claim. The directional truth: even a small percentage of employees actively sharing drives outsized results. With 5 co-founders actively posting, DE has stronger advocacy coverage than most B2B companies.

**Acceleration levers:**
- **Strategic resharing:** Company page reshares co-founder posts 1-2x/day with added commentary. Co-founders engage on company posts. Creates bidirectional growth.
- **Tag strategy:** Co-founders tag each other in posts (not every post — 2-3x/week). Tags send notifications that trigger engagement.
- **Guest mentions:** When co-founders mention specific industry contacts (with permission), those people's networks see the post. Warm introduction at scale.

**KPI target:** Combined follower growth across all 6 accounts > 5% MoM months 1-3 (achievable from <5K base with high-volume posting), decelerating to 3-4% MoM months 4-6 as base grows. [Benchmark — 2-4% MoM is "good" for B2B company pages; 5% is above average but achievable for niche content in an underserved audience. Sustained 5% beyond month 3 likely requires paid amplification.]

### Loop 3: Lead Magnet Compounding

```
Post educational content (carousel, how-to, framework)
  → Includes DM-triggered lead magnet ("DM 'BESS' for the full model")
    → Prospect DMs for magnet
      → Lead captured in HubSpot with source attribution
        → Lead receives magnet + enters nurture sequence
          → Lead engages with future content (now warm, more likely to comment/share)
            → Lead's engagement amplifies next post
              → More prospects see the lead magnet CTA
                → [loops back with growing lead base AND growing audience]
```

**Why this compounds:** Every lead magnet interaction creates a follower who is pre-qualified AND engaged. They comment on future posts, which amplifies reach, which drives more lead magnet requests. The lead database and the content audience grow simultaneously.

**Acceleration levers:**
- Create 3-5 signature lead magnets (see Lead Generation section below)
- Rotate lead magnet CTAs across posts — don't use the same one every day
- Track which lead magnets drive highest DM volume AND highest downstream conversion
- Repurpose best-performing lead magnets into carousel posts (the lead magnet itself becomes content)

**KPI target:** Lead magnet DM requests — Base: >25/month by month 3, Stretch: >50/month. Scale to >100/month by month 6. [DE-specific — from <5K combined followers, 50 DMs/month by month 3 is the 75th-90th percentile of execution quality. 25-30 is more realistic as a planning assumption. The key variable is lead magnet quality — a genuinely useful calculator or model will dramatically outperform a generic PDF.]

### Loop Measurement Dashboard

The Stage 7 ANALYZE report should include a **Growth Loops Health Check:**

```
GROWTH LOOPS HEALTH — Week of [Date]
=====================================

LOOP 1: CONTENT FLYWHEEL
  Impressions-per-follower: [X] (target: >2.0)
  Week-over-week impression growth: [X]%
  Save rate (avg): [X]% (target: >2%)
  Second-life posts (resurfaced by algorithm): [X]
  Status: [Accelerating / Stable / Decelerating]

LOOP 2: EMPLOYEE ADVOCACY
  Cross-account follower growth: +[X] total across 6 accounts
  Company→Personal follower flow: [X] (people who followed co-founders after seeing company posts)
  Personal→Company follower flow: [X]
  Reshare amplification factor: [X]x
  Status: [Accelerating / Stable / Decelerating]

LOOP 3: LEAD MAGNET COMPOUNDING
  Lead magnet DM requests this week: [X]
  Unique lead magnets active: [X]
  Highest-performing magnet: [Name] ([X] requests)
  DM-to-HubSpot conversion rate: [X]%
  Lead-to-meeting conversion from magnets: [X]%
  Status: [Accelerating / Stable / Decelerating]
```

---

## Lead Generation Integration

Content without conversion is a hobby. The entire SMM pipeline exists to generate qualified leads that enter DE's BD pipeline and ultimately become signed HoTs and LOIs.

### The LinkedIn Lead Generation Funnel (with benchmarks)

| Stage | Metric | DE Target | Industry Benchmark |
|---|---|---|---|
| Impressions | Posts seen | Phase A: 10-15K/week, Phase B: 25-40K/week | [DE-specific — from <5K combined followers, 50K/week is unrealistic until month 4-6] |
| Engagement | Likes + comments + shares / impressions | >3% average | 2-6% organic [Benchmark] |
| Profile visits | People who click through to profile | >100/week (Phase A), >300/week (Phase B) | [Scaled for <5K base] |
| **DM conversations** | **People who DM after seeing content** | **>8/week by month 3, >15/week by month 6** | [DE-specific — scaled from base] |
| **Lead magnet requests** | **DMs requesting specific content** | **Base: >25/month by month 3, Stretch: >50/month. >100/month by month 6** | [DE-specific] |
| **MQLs (Marketing Qualified Leads)** | **Score >60 in lead scoring** | **>8/month by month 3, >20/month by month 6** | [Scaled — MQL rate from DMs typically 30-50%] |
| **SQLs (Sales Qualified Leads)** | **BD-confirmed, meeting booked** | **>3/month by month 3, >8/month by month 6** | [Scaled] |
| **Meetings booked** | **Discovery calls from LinkedIn-sourced leads** | **>2/month by month 3, >5/month by month 6** | [Scaled] |
| **Pipeline created** | **EUR value in active pipeline** | **Track from month 1** | Organic LinkedIn CPL equivalent: EUR 100-300 for mature programs [Benchmark range — EUR 164 is mid-range but assumes mature audience, not month-one DE] |

### Lead Magnet Strategy

DE has existing assets that can be mapped to the DM-trigger CTA strategy. The table below shows the **ideal** lead magnets per persona — map existing assets to these slots first, then identify gaps to fill.

| Magnet Concept | Target Persona | Keyword | Ideal Format | What to Use |
|---|---|---|---|---|
| **BESS Revenue Stacking Model** | Energy partners, Institutions | "STACK" | Excel model + 2-page PDF | **Map existing asset** — if a BESS economics model exists internally, package it for external sharing with "indicative" disclaimers |
| **Greenhouse Heat Economics Calculator** | Growers | "HEAT" or "WARMTE" | Interactive PDF or Excel | **Map existing asset** — gas cost comparison, heat economics materials |
| **Grid Connection Timeline Map** | Neoclouds, Enterprise | "GRID" | PDF infographic | **Map existing asset** — grid connection process documentation |
| **Sovereign AI Briefing** | Enterprise, Institutions | "SOVEREIGN" | 4-page PDF | **Map existing asset** — EU AI Act / data sovereignty materials |
| **Project Finance Term Sheet Template** | Institutions, Energy partners | "FINANCE" | Template PDF | **Map existing asset** — project finance structure documentation |

**Week 1 action:** Audit existing DE assets and map at least 2-3 to these keyword triggers. Start with whichever magnets are closest to "ready to share" — don't wait for all 5 to be perfect before launching. A single high-quality lead magnet is better than 5 mediocre ones.

**Rules:**
- Lead magnets must pass Gate C (Product Accuracy) before distribution — they contain numbers
- Every lead magnet includes "indicative" disclaimers where required
- Lead magnets are refreshed quarterly (data staleness rules apply)
- Track which magnet drives highest downstream conversion, not just highest DM volume
- **Quality over quantity:** The difference between 10 DMs/month and 50 DMs/month is usually the quality and specificity of the lead magnet, not the frequency of the CTA

### Comment-to-Lead Scoring (enhanced from Stage 6)

Not every comment is a lead. The Engagement Monitor Agent classifies comments into lead tiers:

| Signal | Classification | Lead Score Impact | Action |
|---|---|---|---|
| "How much does this cost?" / "What's the pricing?" | **Hot lead** | +40 points | Alert BD immediately. Draft DM within 5 min. |
| "We're looking for [capacity/heat/colocation]" | **Hot lead** | +40 points | Alert BD. Draft DM referencing their specific need. |
| "Do you work with [specific sector/geography]?" | **Warm lead** | +25 points | Draft DM with relevant case study or proof point. |
| "Interesting, can you share more?" | **Warm lead** | +20 points | Draft DM with lead magnet relevant to the post topic. |
| Tags a colleague: "@[name] this is relevant for us" | **Warm lead** | +25 points (both people) | Follow both. Draft DM to the tagger. |
| Profile matches ICP (C-suite at target company, >10K followers) | **High-value** | +15 points | Priority alert. Human-crafted response. |
| Asks technical question | **Info request** | +10 points | Reply publicly with expertise (demonstrates knowledge to other readers). Offer DM follow-up. |
| "Great post!" / emoji only | **Noise** | +0 points | Auto-like. No further action. |
| Negative/critical comment | **Not a lead** | -5 points | Human review. Respond thoughtfully. May become a lead if handled well. |

### Lead Scoring Model (0-100, integrated with HubSpot)

| Score Range | Classification | Pipeline Action |
|---|---|---|
| 0-30 | Cold | Nurture with content. Do not outreach. |
| 31-60 | Warm | Trigger: follow on LinkedIn + add to HubSpot. Content nurture. |
| 61-80 | MQL (Marketing Qualified) | Trigger: BD receives alert with full context. BD qualifies within 48 hours. |
| 81-100 | SQL (Sales Qualified) | Trigger: Book discovery call within 24 hours. Priority for CEO/relevant co-founder to handle personally. |

**Score accumulation:**

| Action | Points |
|---|---|
| Engaged with 1 post | +5 |
| Engaged with 3+ posts in 30 days | +15 |
| Requested lead magnet | +20 |
| Visited DE website (tracked via UTM) | +10 |
| Clicked link in first comment | +10 |
| Matches ICP persona profile | +15 |
| C-suite or decision-maker title | +10 |
| Company size matches DE target | +10 |
| Dutch / NL-based | +5 |
| Buying signal comment (see above) | +25 to +40 |
| Attended DE event/webinar | +20 |

### Attribution Model (LinkedIn → Pipeline)

Biggest problem in B2B social: a large majority of sharing is "dark social" — untraceable in standard analytics. [Directional — the commonly cited "84%" figure originates from RadiumOne (2016) and measured all web sharing via private channels, not B2B social specifically. The directional insight is well-established: most B2B influence happens offline, in private messages, and in conversations that analytics can't track.] Someone sees a post, tells a colleague, colleague emails you. LinkedIn gets zero credit.

**DE's Attribution Stack:**

| Layer | Method | Tool |
|---|---|---|
| **First-touch (software)** | UTM parameters on all links in first comments. Track which post drove the click. | HubSpot + Google Analytics |
| **Multi-touch (software)** | Fibbler (~$89-149/month, verify current pricing) syncs LinkedIn Marketing API data to HubSpot contacts. [Corrected: there is no "LinkedIn Company Intelligence API" — Fibbler uses the LinkedIn Marketing API. Works primarily with paid ad impression data. For organic attribution, supplement with Dealfront/Leadfeeder for website visitor identification.] | Fibbler + Dealfront → HubSpot |
| **Self-reported (human)** | "How did you hear about us?" free text field on all high-intent forms (demo requests, portal signup, contact form). Required field, not optional. | HubSpot form |
| **Engagement history (CRM)** | For every SQL, pull their full LinkedIn engagement history: which posts they liked/commented on, which lead magnets they requested, which co-founder they engaged with. | Shield + HubSpot |
| **Dark social proxy** | Monthly survey of pipeline: "Before you contacted us, had you seen our LinkedIn content?" Captures influence that never shows in UTMs. | Manual + HubSpot |

**Rules:**
- Every link in every first comment must have UTM parameters: `?utm_source=linkedin&utm_medium=organic&utm_campaign=[post-id]&utm_content=[account-name]`
- Every DM that converts to a meeting gets tagged with the originating post ID in HubSpot
- Monthly attribution reconciliation: compare software attribution vs. self-reported. Industry data shows self-reported captures ~90% more LinkedIn influence than software alone.

**KPI target:** By month 6, be able to answer: "LinkedIn-sourced leads generated EUR [X] in active pipeline with EUR [Y] closed."

### Multi-Account Lead Routing

Leads come in through 6 accounts. They need to reach the right BD person:

| Lead Source Account | Lead Type | Route To | Timeline |
|---|---|---|---|
| Company page | Any | Marketing team triages → routes by persona | Within 24 hours |
| CEO | Hot lead / high-value | CEO handles personally or delegates to BD | Within 4 hours |
| COO | Technical inquiry about deployment | CTO or COO handles directly | Within 24 hours |
| CFO | Finance/investment question | CFO handles directly | Within 24 hours |
| BD | Grower/heat inquiry | BD handles directly | Within 4 hours |
| CTO | Technical inquiry about infrastructure | CTO handles directly | Within 24 hours |

**Rules:**
- Every DM conversation is logged in HubSpot within 24 hours with: source post, lead score, conversation summary, next action
- If a co-founder receives a lead outside their domain, they warm-intro to the right co-founder in-DM: "Great question — my colleague [Name] leads this for us. Let me connect you."
- No lead sits in a DM inbox for >48 hours without response. Stage 6 (ENGAGE) monitors for this.

### Weekly Lead Gen Metrics (added to Stage 7 ANALYZE)

```
LEAD GENERATION — Week of [Date]
=================================

FUNNEL METRICS
  Total engaged audience: [X] (comments + likes + shares across all accounts)
  DM conversations initiated: [X]
  Lead magnet requests: [X] (breakdown by magnet: STACK=[X], HEAT=[X], GRID=[X], SOVEREIGN=[X], FINANCE=[X])
  New HubSpot contacts from LinkedIn: [X]

SCORING
  New MQLs (score >60): [X]
  New SQLs (score >80): [X]
  Meetings booked from LinkedIn leads: [X]

ATTRIBUTION
  Pipeline influenced (multi-touch): EUR [X]
  Pipeline sourced (first-touch LinkedIn): EUR [X]
  Self-reported LinkedIn attribution rate: [X]%

POST-TO-LEAD PERFORMANCE
  Top 3 posts by lead generation:
    1. [Post ID, account, type, leads generated]
    2. ...
    3. ...
  Top lead magnet this week: [Name] ([X] requests, [X]% conversion to meeting)

BOTTLENECKS
  DMs with >48hr response time: [X] (names, accounts)
  MQLs not yet contacted by BD: [X]
  Leads stuck at warm for >30 days: [X]
```

---

## What's Still Missing (Self-Critique)

Honest assessment of what this plan doesn't solve yet:

### 1. LinkedIn Live / Webinar Growth Loop
Webinars consistently show strong B2B lead conversion — [Benchmark] typical B2B webinar-to-MQL conversion rates are 20-40%, with CPLs of EUR 50-200 (significantly lower than trade show CPLs of EUR 500-1,500+). Note: the commonly cited "73% conversion" figure uses ON24's platform-specific engagement score definition, not traditional MQL conversion. The plan doesn't include a webinar/LinkedIn Live strategy. **Recommendation:** Add a monthly LinkedIn Live event (CEO-hosted, 30 min, one topic from the top-performing pillar that month). The recording becomes 5+ content pieces the following week. This is a growth loop: event → content → audience → next event registrations.

### 2. Video Production Workflow
The plan specifies video as a format option but doesn't define how videos get produced. AI-generated text is one thing; video requires filming, editing, subtitles, thumbnails. **Recommendation:** Define a lightweight video production process — even if it's just "co-founder records 30-second Loom on their phone, subtitles added automatically."

### 3. Newsletter Integration
The content repurposing chain mentions "newsletter snippet" but there's no newsletter strategy. **Recommendation:** Weekly newsletter (Friday) compiling the week's best content + one exclusive insight not posted on social. This captures email addresses from the LinkedIn audience (another growth loop: social → email → deeper relationship → more engagement on social).

### 4. SEO/Blog Cross-Pollination
Blog posts mentioned in the content-engine skill but not integrated into the SMM pipeline. **Recommendation:** Top-performing LinkedIn posts (K > 0.5) should be expanded into blog articles. Blog articles should be teased on LinkedIn with a "link in first comment" CTA. This creates an SEO growth loop alongside the social loop.

### 5. Paid Amplification Layer
The plan is 100% organic. [Directional] LinkedIn thought leadership ads (boosting organic posts that already performed well) consistently show strong B2B ROI because they combine social proof (visible engagement) with targeted distribution. Typical B2B LinkedIn ad CPLs range EUR 50-200 [Benchmark]; thought leadership ads often outperform standard ads because the content is pre-validated by organic engagement. The "EUR 81 → EUR 83K pipeline" case study circulated widely but is a cherry-picked outlier, not a benchmark — treat it as aspirational, not expected. **Recommendation:** Allocate a small budget (EUR 500-1,000/month) to boost the top 2-3 performing posts per week as thought leadership ads. Target by job title and company size matching DE's ICP. This is the fastest way to accelerate Loop 1 (Content Flywheel). Start after month 2, once organic content quality is proven.

### 6. Community Building Beyond LinkedIn
The plan treats LinkedIn as the entire universe. But leads discuss DE in places we can't see — WhatsApp groups, Slack communities, industry events, email threads. **Recommendation:** Track indirect signals (website traffic spikes correlated with posting schedule, self-reported attribution, Google Search Console brand queries). These are the "dark social" indicators that the pipeline is working beyond what LinkedIn metrics show.

### 7. Co-Founder Burnout Risk
8 posts/day across 5 personal accounts is ambitious. If co-founders feel they're "performing" rather than genuinely sharing, the content quality will degrade. **Recommendation:** Each co-founder commits to 1 fully original post per week (their own idea, their own angle). The pipeline fills the other 4. This preserves authenticity while maintaining volume. Monthly 1:1 with each co-founder: "Is this still working for you? What would you change?"

### 8. Competitor Response Monitoring
The Scout monitors competitor posts for content inspiration, but there's no protocol for when a competitor directly targets DE or copies DE's positioning. **Recommendation:** Add a competitor alert trigger in Stage 6 (ENGAGE): if a competitor post mentions DE's positioning pillars or makes claims about similar capabilities, flag for CEO review and consider a response post.

### 9. International Expansion Readiness
The plan is NL-focused with English as primary language. When DE expands to other EU markets, the pipeline needs language variants (German, French) and market-specific proof points. **Recommendation:** Not needed now, but design the source brief format and lead scoring to accommodate market tags from the start.

### 10. Content Fatigue Detection
Posting 40x/week is a lot. If the audience starts tuning out (declining engagement per impression), the pipeline needs to detect this and reduce volume before forcing low-quality content. **Recommendation:** If engagement rate drops >20% week-over-week for 2 consecutive weeks AND follower growth stalls, automatically reduce to 6 posts/day and investigate. Quality always beats quantity.

---

## Key Reference Files

| File | Used By |
|---|---|
| `de-brand-bible/references/proof-points.md` | Brand Compliance Agent (Gate A), Product Accuracy Agent (Gate C) |
| `de-brand-bible/references/brand-identity.md` | Brand Compliance Agent (Gate A) — tone, banned phrases, terminology |
| `content-engine/SKILL.md` | Writer Agent — channel specs, writing rules |
| `content-engine/references/copywriting-frameworks.md` | Writer Agent — PAS, AIDA, BAB, 4Ps |
| `content-engine/references/content-calendar-framework.md` | Writer Agent + Scheduling Agent — cadence, pillar rotation |
| `content-engine/references/tone-and-style-guide.md` | Humanizer Agent (Gate D) — style standards |
| `content-engine/examples/linkedin-post-series.md` | Evergreen buffer seed content |

---

## Verification

To validate this architecture works before building:

### Pipeline Tests
1. **Paper test:** Take 5 real news items from today. Score them using the Scout rubric. Do the top 2-3 match what you'd actually post about? Can at least 1 become a carousel?
2. **Draft test:** For the top-scoring item, write 4 pieces (text, carousel outline, CEO variant, co-founder variant). Run them through the 4 gates mentally. Publishable?
3. **Volume test:** Can you find 40 relevant items in one morning's scan of the 7 source categories? If not, expand the source list.
4. **Fallback test:** Do you have 20 evergreen posts (including 5 carousels) ready? If the pipeline fails on day 1, can you still publish 4-8 posts?

### Virality & Engagement Tests
5. **Golden Hour test:** Post a CEO text post. Execute the full Golden Hour Protocol (5 co-founders engage within 15 min). Measure reach vs. a post without orchestrated engagement. Is the 561% amplification real for DE?
6. **Archetype test:** Write 5 posts — one for each virality archetype (Framework, Contrarian, Credibility, Relatability, Community). Post over 5 days. Which archetype produces the highest K-factor for DE's audience?
7. **Dwell time test:** Post the same insight as (a) a short text post, (b) a carousel, and (c) a comment thread. Compare impressions and engagement rate. Which format drives the most dwell time for DE's content?
8. **Anti-bias test:** Show a reviewer 10 posts, 2 of which have deliberate flaws. Do they catch both?

### Lead Generation Tests
9. **Lead magnet test:** Post 3 educational posts over 1 week, each with a different lead magnet CTA ("DM STACK", "DM HEAT", "DM GRID"). How many DMs does each generate? How many convert to a HubSpot contact?
10. **Attribution test:** Set up UTM tracking on first-comment links for 1 week. Cross-reference with self-reported attribution on any inbound inquiries that week. Does the data align?
11. **Lead scoring test:** Take 10 real LinkedIn engagements from the past month. Score them using the lead scoring model. Does the scoring match your gut feeling about which are real opportunities?

### Growth Loop Tests
12. **Flywheel test:** Track impressions-per-follower for 4 consecutive weeks. Is it stable, increasing, or decreasing? If decreasing, content quality or audience fit is the problem.
13. **Fast lane test:** Can you go from "breaking news spotted" to "post published" in under 2 hours with the abbreviated pipeline?
14. **Co-founder sustainability test:** Ask each co-founder after 2 weeks: "Is this cadence sustainable? What would you change?" If 2+ co-founders say it's too much, reduce personal account targets before quality degrades.
