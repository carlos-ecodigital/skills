---
workflow: pre-conference-activation
version: 1.0.0
owner: contact-intake
trigger: "prepping for [event]", "conference next week", "pre-conference", "who should I meet at [event]"
frequency: ad-hoc
estimated-duration: 30-60 minutes
inputs:
  - Event name, dates, location, DE presence type (booth/speaking/attendee)
  - Attendee/speaker list (from event website, app export, or user-provided)
  - DE priority targets (from ops-targetops)
outputs:
  - CEO briefing document with top 10-15 priority contacts
  - Google Calendar reminders for key sessions and networking windows
  - Collateral pack checklist
tools:
  - WebSearch
  - HubSpot MCP (read)
  - Google Calendar MCP
  - counter-party-intel
  - ops-targetops
last-updated: 2026-03-26
---

# W0: Pre-Conference Activation

## Purpose

Prepare the CEO with a prioritized target list and briefing before a conference or event, so every conversation is intentional and no high-value contact is missed.

## Prerequisites

- [ ] Event name and dates confirmed
- [ ] DE presence type known (booth, speaking slot, attendee-only)
- [ ] ops-targetops priority target list available or requestable
- [ ] HubSpot MCP access (read) for existing contact cross-reference
- [ ] Google Calendar MCP access for reminder creation

## Steps

### Step 1: Gather Event Details

**Who:** contact-intake orchestrator
**Tool:** User input + WebSearch
**Input:** Event name from user
**Action:** Confirm event name, dates, location, and DE presence type (booth / speaking / attendee-only). Search the event website for agenda, speaker list, exhibitor list, and any published attendee directory. Capture event hashtags and relevant social handles.
**Output:** Event fact sheet (name, dates, location, presence type, key URLs)
**If blocked:** Ask user to provide missing details directly

### Step 2: Obtain Attendee and Speaker List

**Who:** contact-intake orchestrator
**Tool:** WebSearch + user-provided data
**Input:** Event fact sheet from Step 1
**Action:** Pull speaker list and exhibitor/sponsor list from the event website. If an attendee list or event app export is available, ingest it. Accept any format: CSV, screenshot, PDF, or text dump. Parse all names, titles, companies into a working list.
**Output:** Raw attendee/speaker/exhibitor list (name, title, company)
**If blocked:** No attendee list available -- fall back to speaker list + sponsor/exhibitor list from event website. If event website is behind paywall, ask user for manual list, screenshots, or app export.

### Step 3: Cross-Reference Against Priority Targets

**Who:** contact-intake orchestrator
**Tool:** ops-targetops
**Input:** Raw attendee list from Step 2
**Action:** Request current priority target list from ops-targetops. Match attendees against target companies and individuals. Flag any direct matches (target person attending) and indirect matches (someone from a target company attending).
**Output:** Annotated list with target match flags

### Step 4: Cross-Reference Against Existing HubSpot Contacts

**Who:** contact-intake orchestrator
**Tool:** HubSpot MCP (read)
**Input:** Annotated list from Step 3
**Action:** Search HubSpot for each attendee by name and company. Flag existing contacts (mark relationship status: active deal, past conversation, cold). Note any prior interaction context or open deals. Identify warm re-engagement opportunities.
**Output:** Annotated list with HubSpot relationship status + prior context

### Step 5: Score and Rank Top 10-15 Priority Conversations

**Who:** contact-intake orchestrator
**Tool:** Manual scoring (ICP fit + strategic value framework)
**Input:** Fully annotated list from Steps 3-4
**Action:** Score each attendee on ICP fit (company size, sector, geography, pain alignment) and strategic value (partnership potential, multiplier effect, market access). Apply bonuses: +0.3 for speakers, +0.5 for target list matches, +0.3 for existing warm contacts. Rank and select top 10-15.
**Output:** Prioritized target list with scores and selection rationale

### Step 6: Generate Quick Profiles for Priority Targets

**Who:** counter-party-intel (delegation)
**Tool:** counter-party-intel W2 quick profile
**Input:** Top 10-15 names + companies from Step 5
**Action:** Delegate to counter-party-intel for quick profiles on each priority target. Request: current role, company overview, recent news, potential pain points, any DE connection points.
**Output:** Quick profile pack (1-paragraph per target)

### Step 7: Produce CEO Briefing Document

**Who:** contact-intake orchestrator
**Tool:** Manual composition
**Input:** Prioritized list from Step 5 + quick profiles from Step 6
**Action:** Compose a CEO briefing document with:
- Event overview (dates, location, DE presence type)
- Top 10-15 priority contacts, each with: name, title, company, 1-line reason to meet, suggested talking point, HubSpot status (new/existing)
- Grouped by priority tier (must-meet / should-meet / opportunistic)
- Any existing relationships to leverage for warm intros
**Output:** CEO briefing document (structured for quick scanning)

### Step 8: Create Google Calendar Reminders

**Who:** contact-intake orchestrator
**Tool:** Google Calendar MCP
**Input:** Event dates + briefing from Step 7
**Action:** Create calendar reminders for:
- Key sessions where priority targets are speaking
- Designated networking windows (coffee breaks, receptions, dinners)
- Pre-event prep reminder (day before: review briefing)
- Post-event processing reminder (day after: trigger W1 contact intake)
**Output:** Calendar events created with links back to briefing

### Step 9: Prepare Collateral Pack Checklist

**Who:** contact-intake orchestrator
**Tool:** Manual composition
**Input:** Priority target profiles + DE product/service alignment
**Action:** Based on the priority targets and their likely pain points, compile a checklist of collateral to have ready:
- [ ] Technical specifications (relevant product lines)
- [ ] Case studies (industry-matched to top targets)
- [ ] Pitch deck (current version)
- [ ] One-pagers (product-specific)
- [ ] Business cards (sufficient quantity)
- [ ] Demo environment (if applicable)
- [ ] NDA templates (if needed for technical discussions)
Flag any missing or outdated collateral that needs updating before the event.
**Output:** Collateral pack checklist with status (ready / needs update / missing)

## Quality Gate

- [ ] At least 10 priority contacts identified and profiled
- [ ] Each priority contact has a 1-line reason to meet and suggested talking point
- [ ] Collateral pack checklist complete with status for each item
- [ ] CEO briefing document is scannable in under 5 minutes
- [ ] Calendar reminders created for key networking windows
- [ ] Post-event W1 trigger reminder scheduled

## Handoffs

| Output | Destination | Skill/Person |
|--------|-------------|-------------|
| CEO briefing document | CEO (Carlos) | Direct delivery |
| Quick profile requests | counter-party-intel | W2 delegation |
| Target list request | ops-targetops | Priority target pull |
| Calendar reminders | Google Calendar | Automated |
| Collateral gaps identified | Relevant team member | Manual follow-up |

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| No attendee list available | Event website has no directory or app | Fall back to speaker list + sponsor/exhibitor list from event website |
| Event website behind paywall | HTTP 403 or login wall encountered | Ask user for manual list, screenshots, or event app export |
| ops-targetops target list unavailable | Skill not responding or list empty | Use ICP fit scoring alone without target overlay |
| HubSpot MCP read fails | API error or timeout | Proceed without CRM cross-reference; flag contacts for manual HubSpot check |
| Fewer than 10 relevant attendees | Small or niche event | Lower threshold to 5; supplement with "companies to watch for" list |
| Counter-party-intel overloaded | Profile generation delayed | Deliver briefing with basic profiles; enrich incrementally as profiles complete |
