# Workflow Automation

> Reusable multi-step automation chain patterns for the Digital Energy skill ecosystem.
> Each pattern: trigger → skill chain → tools → output → user confirmation points.
> Last updated: 2026-02-19

## Pipeline Patterns

### 1. Meeting Processing Pipeline

**Trigger:** "process this transcript", "meeting notes from [meeting]", post-meeting invocation
**Automation level:** L2 (Chrome-assisted) / L3 (HubSpot MCP for CRM updates)

```
Fireflies transcript (via MCP or paste)
    ↓
ops-meetingops
  → Extract: summary, action items, attendees, decisions, next steps
  → Output: structured meeting summary
    ↓
ops-contextops
  → Capture: decisions → decision journal, relationship intel → contact notes
    ↓
ops-dealops
  → Match attendees to HubSpot contacts (search_crm_objects)
  → Log meeting note on contact/deal records (manage_crm_objects)
  → Update deal stage if milestone was discussed
    ↓
ops-outreachops
  → Draft follow-up email per attendee
  → Route through content-engine for tone/structure
    ↓
humanizer
  → Strip AI patterns from email drafts
    ↓
OUTPUT: Follow-up emails ready to send
  → L2: Chrome opens Gmail, composes each email → USER CONFIRMS before send
  → L1: Output formatted email text for manual paste
```

**User confirmation points:** HubSpot record updates (table display), email sends
**Error handling:** If Fireflies MCP unavailable → accept pasted transcript. If HubSpot contact not found → create new contact (confirm with user first).
**Batch-friendly:** Yes — can process multiple meetings in one session.

---

### 2. Brain Dump Pipeline

**Trigger:** "brain dump", "here's what happened this week", WhatsApp export paste
**Automation level:** L1 (paste-and-process) → L3 (HubSpot updates if deal-related)

```
Raw input (voice note transcript, WhatsApp export, stream-of-consciousness)
    ↓
ops-contextops
  → Parse into structured categories:
    - Decisions → decision journal entries
    - People/relationships → relationship intel updates
    - Project updates → deal/project context
    - Ideas/priorities → action item candidates
    ↓
ops-chiefops
  → Extract action items with owners and deadlines
  → Flag blockers or escalations
  → Update priority list if new priorities mentioned
    ↓
ops-dealops (if deal-related content detected)
  → Update HubSpot contacts/deals with new intel (manage_crm_objects)
  → Log relationship context as notes
    ↓
OUTPUT:
  - Structured context capture (saved to context files)
  - Action items with owners (ready for ClickUp or weekly brief)
  - HubSpot updates (confirmed by user)
```

**User confirmation points:** HubSpot record updates, any action items assigned to others
**Error handling:** If input is too unstructured → ask user to clarify the key decisions/actions
**Batch-friendly:** Yes — designed for 1-2x weekly bulk processing

---

### 3. Content Publishing Pipeline

**Trigger:** "write a LinkedIn post about [topic]", "publish content on [channel]"
**Automation level:** L2 (Chrome-assisted for posting)

```
User request with topic/angle
    ↓
content-engine
  → Load de-brand-bible for tone, persona, proof points
  → Draft content per channel playbook (LinkedIn, blog, email, etc.)
  → Apply channel-specific formatting
    ↓
humanizer
  → Strip AI patterns
  → Verify natural voice
    ↓
USER REVIEW
  → Present draft for approval/edits
    ↓
OUTPUT:
  → L2: Chrome navigates to platform → paste content → USER CONFIRMS → post
  → L1: Output formatted content for manual posting
```

**User confirmation points:** Content approval (before posting), post confirmation (before clicking post)
**Error handling:** If brand-bible references unavailable → use general DE tone guidelines. If Chrome can't access platform → output formatted text.
**Batch-friendly:** Yes — can draft multiple pieces in one session, post sequentially

---

### 4. Investor Update Pipeline

**Trigger:** "monthly investor update", "write update for investors"
**Automation level:** L2 (Chrome for Gmail) / L3 (HubSpot for metrics)

```
ops-irops (orchestrates)
  → Structure update: highlights, lowlights, metrics, asks, next milestones
    ↓
ops-dealops
  → Pull pipeline metrics from HubSpot (search_crm_objects: deals)
  → Pull recent activity: new contacts, deal movements, meeting count
    ↓
content-engine
  → Polish writing, apply investor communication tone
  → Format per investor update template
    ↓
humanizer
  → Strip AI patterns from final draft
    ↓
USER REVIEW + EDIT
  → Founder reviews/edits before distribution
    ↓
OUTPUT:
  → L2: Chrome opens Gmail → compose to investor list → USER CONFIRMS → send
  → L1: Output formatted email for manual send
  → ops-irops: Log update in investor engagement tracking
```

**User confirmation points:** Content approval, recipient list confirmation, send confirmation
**Error handling:** If HubSpot metrics unavailable → ask user for manual metrics input. If investor email list not available → output email for manual addressing.
**Batch-friendly:** Typically one update per month, but can generate multiple versions (per investor tier)

---

### 5. Prospect Research Pipeline

**Trigger:** "research [company/person]", "build a target list for [audience]"
**Automation level:** L3 (HubSpot for CRM) / L1 (WebSearch for research)

```
User request with target specification
    ↓
ops-targetops
  → Define search criteria, scoring rubric for this audience type
  → WebSearch for company/person intelligence
  → Cross-reference with existing HubSpot contacts (search_crm_objects)
    ↓
ops-contextops (if existing relationship context exists)
  → Pull prior interactions, relationship intel, tribal knowledge
    ↓
ops-targetops
  → Score target against rubric
  → Map intro paths (advisor network, mutual connections)
  → Produce research dossier
    ↓
ops-dealops (if target is actionable)
  → Create/update HubSpot contact (manage_crm_objects)
  → Associate with appropriate deal/pipeline
    ↓
OUTPUT:
  - Research dossier (formatted Markdown)
  - HubSpot contact created/updated
  - Intro path recommendations
  - Ready for ops-outreachops to draft outreach
```

**User confirmation points:** HubSpot contact creation/update
**Error handling:** If WebSearch yields limited results → note gaps, suggest manual research. If existing contact found with different data → present conflict for user resolution.
**Batch-friendly:** Yes — can research multiple targets in one session

---

### 6. Skill Build Pipeline (Forge Internal)

**Trigger:** forge W1 (build) invoked
**Automation level:** L1 (all local file operations)

```
User brief for new skill
    ↓
forge W1
  → Intake questions → design decisions
  → Read ecosystem-registry.md → overlap check
  → Run anti-patterns.md checklist
  → Select composition pattern
  → Read gold-standard exemplar skill
    ↓
forge (build)
  → Draft SKILL.md using template
  → Write reference files (75/25 rule)
  → Generate eval scenarios (eval-scaffolding.md)
    ↓
forge (quality)
  → Self-critique (cooperative refinement)
  → Score against quality-rubric.md
  → Must score ≥75 to ship
    ↓
OUTPUT:
  - Complete skill directory
  - Updated ecosystem-registry.md
  - forge-learnings.md entry
```

**User confirmation points:** Skill design approval (before building), final review (before shipping)
**Error handling:** If score <75 → iterate on weakest categories. If overlap detected → present merge options.

## Cross-Pipeline Chaining

Pipelines can chain into each other:

| After This Pipeline... | Can Trigger... |
|----------------------|---------------|
| Meeting Processing | → Prospect Research (if new contact discussed) |
| Meeting Processing | → Content Publishing (if follow-up content promised) |
| Brain Dump | → Investor Update (if investor-related context captured) |
| Prospect Research | → Outreach (ops-outreachops drafts initial contact) |
| Investor Update | → Meeting Processing (if investor meeting followed) |

## Pipeline Design Checklist

When creating a new automation pipeline:

- [ ] Trigger is clear and unambiguous
- [ ] Each step identifies the responsible skill
- [ ] Tool calls are specified (MCP tool names or Chrome sequences)
- [ ] User confirmation points are marked for all external actions
- [ ] Error handling covers tool unavailability
- [ ] Fallback path documented for each automation level
- [ ] Output is formatted for the target destination
- [ ] Batch-friendly design (can process multiple items)
