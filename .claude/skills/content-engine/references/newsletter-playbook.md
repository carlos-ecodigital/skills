# Newsletter Playbook — Dedicated Workflow for Digital Energy Newsletters

> Elevates the newsletter from "just another channel" to a first-class recurring workflow with its own architecture, curation process, and optimization framework.

---

## 1. Newsletter Architecture

### Section-by-Section Framework

Every Digital Energy newsletter follows this 5-section structure:

| # | Section | Length | Purpose | Source |
|---|---|---|---|---|
| 1 | **Lead Insight** | 200-300 words | One original thought leadership piece — not a recap, an opinion or analysis | CEO/founder perspective, new data, contrarian take |
| 2 | **Proof Point Spotlight** | 100-150 words | One concrete milestone, deal, or metric that demonstrates progress | Recent deals, milestones, project updates from `de-brand-bible/references/proof-points.md` |
| 3 | **Curated Links** | 3 items × 50 words each | Industry news relevant to the reader with DE's angle on why it matters | Energy transition news, AI infrastructure developments, regulatory changes |
| 4 | **Upcoming** | 50-75 words | Events, webinars, conferences where DE will be present or content is publishing | Calendar, event marketing from `marketing-strategist/references/events-speaking-playbook.md` |
| 5 | **CTA** | 1 sentence | Single action — portal signup, resource download, event registration, or meeting request | Aligned with current campaign from `marketing-strategist` |

**Total length:** 500-800 words (3-4 minute read)

### Section Rules

- **Lead Insight must be original.** Not a summary of someone else's article. The reader should get value they can't find elsewhere. Frame as: "Here's what we're seeing / learning / thinking about [topic]."
- **Proof Point must be specific.** "[X] MW secured" or "First heat delivery to [partner]" — not "We're making great progress."
- **Curated Links must have a DE angle.** Don't just share a link — add 1 sentence: "Why this matters for [our readers / the energy transition / AI infrastructure]."
- **CTA must be singular.** One ask per newsletter. Rotate between campaign goals month by month.

---

## 2. Audience Segmentation

### Segment-Specific Variants

| Segment | Lead Insight Focus | Proof Point Frame | Curated Links Lens | CTA Type |
|---|---|---|---|---|
| **Growers / Heat Buyers** | Energy cost reduction, sustainability mandate, heat transition | Heat delivery milestones, cost savings data | NL energy policy, gas prices, LTO news | Portal signup, site visit invite |
| **Neoclouds / Compute Buyers** | AI infrastructure demand, European sovereignty, power availability | Capacity milestones, grid connection progress, partnership announcements | GPU/AI market, European DC demand, sovereignty regulation | Technical briefing call |
| **Investors** | Market thesis, infrastructure returns, deal pipeline | Pipeline value, LOIs signed, project financing progress | Infra fund activity, energy transition investment, regulatory tailwinds | Deck request, meeting |
| **General / Multi-segment** | Industry-level insight (grid scarcity, heat-compute convergence) | Biggest recent milestone | Broad energy/tech crossover news | Website visit, LinkedIn follow |

**Default:** If no segment specified, produce the General variant. Always ask user which segment(s) before writing.

---

## 3. Subject Line Framework

### Generate 3 Variants Per Send

For every newsletter, produce 3 subject line options with A/B rationale:

| Variant | Formula | Example |
|---|---|---|
| **A: Data-Led** | [Number] + [implication] | "60 GW queued + why your grid connection just became worth millions" |
| **B: Curiosity** | [Topic] + incomplete loop | "The part of AI infrastructure nobody's building" |
| **C: Benefit-Direct** | [What you'll learn/get] | "3 things shaping NL energy infrastructure this month" |

### Subject Line Rules
- Under 50 characters (mobile preview)
- No ALL CAPS, no exclamation marks, no emoji
- No "Monthly Update" or "Newsletter #X" — these kill open rates
- Preview text (preheader): extends the subject line, does not repeat it. 40-90 characters.
  - Subject: "60 GW queued + why your grid connection matters"
  - Preview: "Plus: our first heat delivery milestone and 3 links worth your time"

---

## 4. Content Curation Checklist

Before writing each newsletter, gather content from these sources:

### Internal Sources
- [ ] Recent deals closed or progressed (check with `ops-dealops` / HubSpot)
- [ ] Project milestones (grid connections, construction, heat delivery)
- [ ] New partnerships or LOIs
- [ ] Content published since last newsletter (LinkedIn posts, blog articles, press releases)
- [ ] Upcoming events or conferences
- [ ] Regulatory developments affecting DE's business
- [ ] Any updated proof points in `de-brand-bible/references/proof-points.md`

### External Sources (for Curated Links)
- [ ] NL energy policy news (Rijksoverheid, RVO, ACM decisions)
- [ ] European AI infrastructure news (DC construction, GPU capacity)
- [ ] Grid congestion updates (TenneT, regional TSO announcements)
- [ ] Competitor or market developments
- [ ] Relevant industry reports (BNEF, CBRE, IEA)

### Angle Selection
After gathering, choose the Lead Insight topic based on:
1. **Timeliness:** Is there a current event we can provide unique perspective on?
2. **Proof:** Do we have a new proof point that strengthens our narrative?
3. **Contrarian:** Can we challenge something the industry assumes?
4. **Original data:** Do we have numbers or insights nobody else has shared?

---

## 5. Send Cadence & Timing

### Recommended Frequency

| Segment | Frequency | Rationale |
|---|---|---|
| General | Monthly | Enough to maintain awareness without fatigue |
| Investors | Monthly (aligned with `ops-irops` update cycle) | Investors expect regular cadence |
| Growers | Bi-monthly or event-triggered | Growers are less digital; over-emailing causes unsubscribes |
| Neoclouds | Monthly | Fast-moving market; monthly keeps us relevant |

### Optimal Send Times
- **NL audience (growers, NL investors):** Tuesday or Wednesday, 09:00-10:00 CET
- **International (neoclouds, global investors):** Tuesday or Thursday, 14:00-15:00 CET
- **Avoid:** Monday morning (inbox overload), Friday afternoon (weekend mode)

---

## 6. Performance Tracking

### Metrics to Monitor Per Send

| Metric | Target | Action if Below |
|---|---|---|
| **Open rate** | >25% | Test subject lines; clean inactive subscribers |
| **Click-through rate** | >3% | Improve CTA clarity; test link placement |
| **Unsubscribe rate** | <0.5% | Check frequency; review content relevance |
| **Reply rate** | >0.5% | Good sign — means content is engaging; route replies to `ops-outreachops` |

### A/B Testing Protocol
- Test ONE variable per send (subject line OR CTA OR section order)
- Split list 50/50
- Declare winner after 24 hours (90% of opens happen within 24h)
- Apply winning pattern to next 3 sends, then test again

---

## 7. Newsletter Production Workflow

### Timeline (5 business days before send)

| Day | Step | Who |
|---|---|---|
| T-5 | Run content curation checklist; select Lead Insight topic | Content atomizer or content-engine |
| T-4 | Draft all 5 sections | `content-engine` (invoke this playbook) |
| T-3 | Generate 3 subject line variants + preview text | `content-engine` |
| T-2 | Run through `humanizer` to strip AI patterns | `humanizer` |
| T-1 | Carlos review + final edits | Founder |
| T-0 | Send; track metrics | Marketing team |

---

## 8. Integration with Content Atomizer

When the `content-atomizer` processes a source piece, the **newsletter section** derivative should follow this playbook's Section framework. The atomizer produces a single newsletter insert; this playbook governs the full newsletter that insert goes into.

**Flow:**
1. `content-atomizer` produces newsletter section from source content
2. This playbook assembles the full newsletter (Lead Insight may come from atomized content, or may be original)
3. `content-engine` writes the complete newsletter following this structure
4. `humanizer` cleans the output
