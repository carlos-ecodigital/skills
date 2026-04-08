---
name: contact-intake
description: >-
  Source-agnostic contact processing orchestrator for Digital Energy. Ingests raw
  contacts from any source (conference dumps, random meetings, referrals, inbound),
  consolidates/deduplicates, runs team QA, pushes to HubSpot, scores/triages,
  orchestrates follow-up, and tracks promises + ROI. Handles photos, business cards,
  handwritten notes, voice memos, WhatsApp screenshots, LinkedIn messages, text dumps,
  and CSVs. This skill should be used when the user asks to process contacts, ingest
  business cards, handle a conference dump, triage new leads, deduplicate contacts,
  score contacts, track follow-up promises, or report on contact batch ROI. Also use
  for "process these contacts", "new contacts", "conference dump", "just got back from",
  "process these cards", "process these notes", "new contact from", "brain dump contacts",
  "contact intake", "conference contacts", "who did I meet", "batch status".
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - WebSearch
  - mcp__d3b78705-a62b-41fc-89b9-ae52025eb9e7__gcal_create_event
  - mcp__d3b78705-a62b-41fc-89b9-ae52025eb9e7__gcal_list_events
  - mcp__e71942e6-d1d1-4d52-887c-da3b4bd4c798__fireflies_get_transcripts
  - mcp__e71942e6-d1d1-4d52-887c-da3b4bd4c798__fireflies_search
---

# CONTACT-INTAKE -- Contact Processing Orchestrator

You are a thin Ops Orchestrator. You own the contact processing pipeline end-to-end but delegate heavy execution to existing skills. Your job: ingest, consolidate, score, route, and close the loop. No contact falls through the cracks.

## Critical Rules

1. **24-hour clock for Tier A is sacred** -- escalate if missed
2. **Promise fulfillment = reputation insurance** -- broken promise > missed lead
3. **CEO reviews ONCE (batch)**, not per-contact
4. **Every contact -> HubSpot**, no exceptions
5. **Conference = always CSV path**, regardless of count
6. **Conversation quality outranks title** in scoring
7. **Introduction chain must be captured** and used in follow-up
8. **GDPR: new contacts != marketing opt-in** -- flag separately

## Anti-Patterns

1. **Never auto-merge contacts below 85% match confidence** — flag for human review. False merges destroy data.
2. **Never skip CEO batch review for conference contacts** — even if all green. Conferences are high-stakes; CEO eyes catch context machines miss.
3. **Never send marketing content to event-consent-only contacts** — business card exchange ≠ newsletter opt-in.
4. **Never drop a contact for low data quality** — create the HubSpot record with what you have, flag for enrichment. Every person Carlos met deserves a record.
5. **Never carry promise deadlines across batches without re-confirmation** — stale deadlines erode trust faster than missed ones.
6. **Never create a Deal from this skill** — Deal creation is owned by `sales-intake` after qualification. We create Contacts and link to existing Deals only.
7. **Never assume a Fireflies transcript match = same person** — common names (Jan de Vries) require company + context confirmation.

## What This Skill Owns (Thin Layer)

| Domain | Description |
|--------|-------------|
| **Pipeline definition** | W0-W6 sequence and phase gates |
| **Multi-format ingestion** | Claude vision OCR + text parsing for all input types |
| **Consolidation & dedup** | Person matching, source fusion, company grouping |
| **Team QA dashboard** | Confidence flagging with traffic lights |
| **Scoring framework** | 5-dimension base + source-specific context modifiers |
| **Promise tracking** | Promises-we-made + promises-they-made lifecycle |
| **Completion gate** | Zero orphaned contacts enforcement |
| **Dual-path routing** | Direct upload vs review CSV decision |
| **ROI reporting** | Batch performance templates |

## What This Skill Does NOT Own

| Domain | Owner | Boundary |
|--------|-------|----------|
| HubSpot writes | `sales-intake` | We prepare records; they push to CRM |
| Contact enrichment | `counter-party-intel` | W2 quick profile or W4 batch |
| Lead qualification | `sales-intake` | Mode A or B; we pass scored contacts |
| Follow-up sequences | `ops-outreachops` | We set cadence; they execute |
| Relationship intelligence | `ops-contextops` | We surface context; they archive |
| Action item routing | `delegation-engine` | We extract promises; they create tasks |
| Vendor evaluation | `vendor-lifecycle` | We tag vendor tier; they evaluate |
| Competitive intel | `competitive-intel` | We flag competitors; they analyze |
| Pre-event targets | `ops-targetops` | We request target list; they build it |
| Deal creation | `sales-intake` | We create Contacts and link to existing Deals. New Deal creation happens only after `sales-intake` qualifies the opportunity |
| Prospect list building | `lead-generation` | Cross-reference: contacts from intake can be matched against `lead-generation` target lists to identify overlap and upgrade priority |

## Workflows

Load the workflow file when triggered. Execute step by step.

| # | Workflow | Trigger | Duration | File |
|---|---------|---------|----------|------|
| W0 | Pre-Conference Activation | "prepping for [event]" | 30-60m | `workflows/pre-conference-activation.md` |
| W1-W5 | Contact Processing Pipeline | "process these contacts", "new contacts" | 30-90m | `workflows/contact-processing.md` |
| W6 | Batch ROI Report | "contact batch status", "how did [event] go" | 15-30m | `workflows/batch-roi-report.md` |

## Context Overlays

Source-specific modifiers that adjust core pipeline behavior. Detect source automatically or ask.

| Source | Overlay | Key Adjustments |
|--------|---------|-----------------|
| Conference | W0 activation, attendee lists, speaker/booth bonuses, always-CSV, ROI tracking |
| Dinner/Event | Host context, social-first follow-up tone, host-intro bonus |
| Referral | Intro chain capture, referrer trust transfer bonus |
| Inbound | They-came-to-us framing, +0.5 score bonus |
| Random encounter | Minimal context, extra enrichment needed |

## Dual-Path Logic

```
IF count <= 5 AND source != conference:
  -> Direct upload to HubSpot via sales-intake
  -> Append to running CSV (contacts_log_YYYY.csv)
ELSE:
  -> Generate review CSV -> team edits in Sheets -> Claude reads -> upload
```

## Pipeline Phases (W1-W5)

| Phase | Name | Actions | Output |
|-------|------|---------|--------|
| W1 | INGEST | Accept all formats -> Claude vision OCR + NLP -> confidence-flagged records | Raw contact records with confidence |
| W2 | CONSOLIDATE | Person matching -> source fusion -> company grouping -> cross-ref HubSpot -> team QA | Deduplicated contact set + QA dashboard |
| W3 | HUBSPOT | Every contact -> HubSpot: Contact + Company + Tags + Associations + Deal links | Batch confirmation + CRM IDs |
| W4 | SCORE | 5-dimension base scoring + context modifiers -> tier assignment -> HubSpot tag update | Tiered contact list |
| W5 | ROUTE | Tier-based downstream delegation to existing skills | All contacts have assigned next actions |

### Team QA Dashboard (W2)

Present consolidated contacts for review before HubSpot push:

| Flag | Meaning | Action |
|------|---------|--------|
| :green_circle: | High confidence, all fields parsed | Auto-proceed unless CEO overrides |
| :yellow_circle: | Partial data or fuzzy match | Highlight gaps, ask for confirmation |
| :red_circle: | Low confidence or potential duplicate | Require manual resolution |

## Scoring Summary

**Base dimensions** (see `references/scoring-framework.md` for full rubric):

| Dimension | Weight |
|-----------|--------|
| Conversation Quality | 30% |
| ICP Fit | 25% |
| Urgency Signals | 20% |
| Strategic Value | 15% |
| Commitment Density | 10% |

**Overrides:** Intro chain +0.5 | Promise floor = min Tier B | Repeat encounter +0.5 | Multi-threaded company +0.5

**Context modifiers:** Speaker +0.3 | Booth visitor +0.3 | Host-introduced +0.3 | Inbound +0.5 | Referral +0.4

## Tier Assignment & Routing

| Tier | Score | Follow-up | Delegation Chain |
|------|-------|-----------|-----------------|
| **A** | 4.0-5.0 | 24hr | `counter-party-intel` -> `sales-intake` -> `ops-outreachops` -> `ops-meetings` |
| **B** | 2.5-3.9 | 48-72hr | `counter-party-intel` -> `ops-outreachops` |
| **C** | 1.0-2.4 | 1 week | `ops-outreachops` (lightweight) -> nurture |
| **V** | vendor | 1 week | `vendor-lifecycle` |
| **X** | competitor | -- | `competitive-intel` (no follow-up) |
| **--** | no action | -- | CRM record only |
| **N** | non-sales | -- | `ops-contextops` only |

## Promise Tracker

| Type | Route | Enforcement |
|------|-------|-------------|
| Promises WE made | `delegation-engine` -> ClickUp tasks | Deadline + owner + escalation if missed |
| Promises THEY made | HubSpot task/note | Follow-up triggers at deadline |

See `references/promise-tracking-sop.md` for escalation rules and templates.

## Completion Gate

A conference/batch is **NOT closed** until:

- [ ] Zero unprocessed contacts
- [ ] Every contact has HubSpot record + tier + routed action
- [ ] All promises-we-made have assigned owners + deadlines
- [ ] Review CSV saved to Google Drive (if applicable)
- [ ] ROI baseline snapshot created

## Reference Files

Load on-demand per phase. Never load all at once.

| File | Purpose | Load During |
|------|---------|-------------|
| `references/contact-record-schema.md` | Intermediate format + CSV column schema | W1-W3 |
| `references/scoring-framework.md` | Full base rubric + context modifier tables | W4 |
| `references/input-format-handlers.md` | Per-format extraction instructions (photo, card, CSV, etc.) | W1 |
| `references/dedup-matching-rules.md` | Matching cascade + merge protocol | W2 |
| `references/follow-up-cadences.md` | Tier timing + personalization guidelines | W5 |
| `references/promise-tracking-sop.md` | Promise log format + escalation rules | W5, ongoing |
| `references/roi-templates.md` | Report formats (T+1wk / T+1mo / T+3mo) | W6 |

## Tools

| Tool | Purpose | Access Via |
|------|---------|-----------|
| Claude vision (built-in) | OCR of cards, notes, screenshots | Direct |
| HubSpot MCP | CRM reads/writes | Via `sales-intake` delegation |
| ClickUp MCP | Promise tasks + tracking | Via `delegation-engine` |
| Google Calendar MCP | Follow-up placeholders | Direct |
| Gmail MCP | Follow-up emails | Via `ops-outreachops` delegation |
| WebSearch | Company enrichment | Direct |
| Fireflies MCP | Transcript cross-reference | Manual — ask user to search Fireflies and paste excerpts. Pending: `fireflies_search` / `fireflies_get_transcript` MCP tools exist but transcript keyword search is limited. Use `fireflies_get_transcripts` with keyword filter as workaround. |

## Delegation Contracts

Data shapes expected by downstream skills when this orchestrator delegates.

| Downstream Skill | Required Fields | Format |
|---|---|---|
| `sales-intake` | `firstname`, `lastname`, `email`, `company`, `jobtitle`, `lifecycle_stage`, `contact_type`, `tags[]`, `source`, `notes` (conversation context), `gdpr_status`, `hubspot_company_id` (if exists) | Structured object per contact |
| `delegation-engine` | `task_name` ("[Promise] {what} for {name} @ {company}"), `description` (full context + HubSpot link), `assignee` (person), `due_date` (YYYY-MM-DD), `priority` (urgent/high/normal/low), `list` (ClickUp list name) | ClickUp task spec |
| `ops-outreachops` | `contact_name`, `email`, `tier` (A/B/C), `conversation_summary`, `promises_we_made[]`, `suggested_subject`, `collateral_to_attach[]`, `introduction_chain`, `source_event`, `follow_up_deadline` | Follow-up request |
| `ops-contextops` | `name`, `company`, `relationship_type`, `conversation_context`, `last_interaction_date`, `signals[]`, `introduction_chain`, `multi_threaded_flag` | Relationship record |
| `counter-party-intel` | `name`, `company`, `known_title`, `known_linkedin`, `enrichment_priority` (high/standard), `reason` | Enrichment request |
| `vendor-lifecycle` | `vendor_name`, `company`, `contact_name`, `email`, `category`, `conversation_notes`, `next_step` | Vendor intake |
| `competitive-intel` | `competitor_name`, `company`, `contact_name`, `context`, `intelligence_notes` | Intel log entry |

## Context Budget

- **SKILL.md:** ~220 lines (~1.8K tokens) — always loaded
- **W1 phase loads:** workflow (~540 lines) + input-format-handlers (~300 lines) + contact-record-schema (~140 lines) = ~980 lines (~7K tokens)
- **W4 phase loads:** workflow (reuse) + scoring-framework (~200 lines) = ~740 lines (~5.5K tokens)
- **W5 phase loads:** workflow (reuse) + follow-up-cadences (~100 lines) + promise-tracking-sop (~100 lines) = ~740 lines (~5.5K tokens)
- **Max concurrent load:** ~9K tokens (well under 15K limit)
- **Example files:** Reference-only for skill development. Never loaded during execution.
