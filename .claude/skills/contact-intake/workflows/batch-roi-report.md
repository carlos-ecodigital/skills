---
workflow: batch-roi-report
version: 1.0.0
owner: contact-intake
trigger: "contact batch status", "how did [event] go", "conference ROI", "batch report"
frequency: ad-hoc
estimated-duration: 15-30 minutes
inputs:
  - Event/batch name or source tag
  - HubSpot pipeline data (via MCP read)
  - Promise tracker status (via ClickUp MCP read)
outputs:
  - ROI report (activity, pipeline, or revenue attribution depending on elapsed time)
tools:
  - HubSpot MCP (read)
  - ClickUp MCP (read)
last-updated: 2026-03-26
---

# W6: Batch Status & ROI Report

## Purpose

Measure the return on contact acquisition efforts by reporting on activity, pipeline progression, and revenue attribution for a specific event or contact batch, enabling data-driven decisions about future events and outreach investments.

## Prerequisites

- [ ] Event/batch name or source tag identified
- [ ] HubSpot MCP access (read) for contact and deal pipeline data
- [ ] ClickUp MCP access (read) for promise tracker status
- [ ] Contacts from the batch have been fully processed through W1-W5

## Steps

### Step 1: Identify Batch and Determine Report Tier

**Who:** contact-intake orchestrator
**Tool:** User input
**Input:** User request (event name, batch identifier, or source tag)
**Action:** Confirm which batch/event to report on. Calculate elapsed time since the event or batch processing date. Determine report tier:
- T+1 week: Activity report
- T+1 month: Pipeline report
- T+3 months: Revenue attribution report
If the user requests a specific report type regardless of timing, accommodate but flag if data may be premature.
**Output:** Batch identifier + report tier selection

### Step 2: Pull HubSpot Contacts for Batch

**Who:** contact-intake orchestrator
**Tool:** HubSpot MCP (read)
**Input:** Batch identifier / source tag from Step 1
**Action:** Search HubSpot for all contacts tagged with the event source tag (e.g., "source:ees2026", "source:dinner-munich-jan"). Pull contact records with: name, company, tier assignment, lifecycle stage, last activity date, associated deals.
**Output:** Full contact list from batch with current HubSpot status
**If blocked:** HubSpot tags inconsistent -- search by date range + source detail field as fallback. If still incomplete, ask user to confirm expected contact count.

### Step 3: Pull Deal Pipeline Data

**Who:** contact-intake orchestrator
**Tool:** HubSpot MCP (read)
**Input:** Contact list from Step 2
**Action:** For each contact, pull associated deal data: deal name, stage, amount, create date, close date (if won), last stage change. Aggregate by pipeline stage to build a conversion funnel. Calculate total pipeline value and weighted pipeline value.
**Output:** Deal pipeline summary (by stage, by tier, totals)
**If blocked:** Some contacts have no deals yet -- this is expected, especially at T+1 week. Report as "no pipeline activity" rather than treating as an error.

### Step 4: Pull Promise Tracker Status

**Who:** contact-intake orchestrator
**Tool:** ClickUp MCP (read)
**Input:** Batch identifier from Step 1
**Action:** Search ClickUp for all promise tasks linked to this batch/event. Pull status for both promise types:
- Promises WE made: task status, deadline, completion date, owner
- Promises THEY made: follow-up status, whether fulfilled
Calculate promise fulfillment rate for each type.
**Output:** Promise tracker summary (fulfilled / pending / overdue / broken)
**If blocked:** Promise tasks not consistently tagged -- search by date range and assignee as fallback

### Step 5: Compile Report by Tier

**Who:** contact-intake orchestrator
**Tool:** Manual composition
**Input:** All data from Steps 2-4 + report tier from Step 1
**Action:** Compile the appropriate report based on elapsed time:

**T+1 Week -- Activity Report:**
- Total contacts processed (by tier: A/B/C/V/X/N)
- Follow-ups sent vs. pending (by tier)
- Promise fulfillment status (we-made and they-made)
- Response rate (replies received / follow-ups sent)
- Any Tier A contacts still without follow-up (escalation flag)

**T+1 Month -- Pipeline Report:**
- Everything from Activity Report (updated)
- Qualified opportunities generated (count + value)
- Meetings booked and held
- Deals created and current stages
- Conversion funnel: contacts -> responses -> meetings -> opportunities
- Tier accuracy check: did A-tier contacts actually convert better?

**T+3 Months -- Revenue Attribution Report:**
- Everything from Pipeline Report (updated)
- Total pipeline value attributed to this batch
- Closed-won revenue attributed to this batch
- ROI multiple (revenue / estimated event cost, if cost data available)
- Cost per qualified opportunity
- Cost per closed deal
- Top 3 wins from this batch (story format)
- Attend-again recommendation (for conference batches)

**Output:** Formatted report matching the appropriate tier

### Step 6: Add Conference-Specific Metrics (If Applicable)

**Who:** contact-intake orchestrator
**Tool:** Manual composition
**Input:** Report from Step 5 + event cost data (if available)
**Action:** If this batch is from a conference/event, add:
- Event cost breakdown (registration, travel, booth, sponsorship, entertainment)
- Cost per contact acquired
- Cost per qualified opportunity
- Attend-again recommendation: YES / MAYBE / NO with reasoning
- Suggestions for next time (better booth placement, different sessions, etc.)
If cost data is not available, ask user or flag as "cost data needed for full ROI calculation."
**Output:** Conference-enhanced report section
**If blocked:** No cost data available -- present pipeline metrics only and flag that ROI multiple requires cost input

### Step 7: Cross-Event Comparison (If Requested)

**Who:** contact-intake orchestrator
**Tool:** HubSpot MCP (read)
**Input:** Current report + prior event tags (if comparison requested)
**Action:** If user requests cross-event comparison, pull equivalent metrics from prior event batches. Present side-by-side: contacts acquired, conversion rates, pipeline generated, revenue closed, cost per opportunity. Highlight trends and outliers.
**Output:** Comparison table with prior events
**If blocked:** Prior event data incomplete or tags inconsistent -- present available data with caveats

### Step 8: Present Report

**Who:** contact-intake orchestrator
**Tool:** Direct delivery
**Input:** Complete report from Steps 5-7
**Action:** Present the report in a scannable format. Lead with the headline metric (e.g., "EES 2026: 47 contacts, 12 qualified opps, $340K pipeline at T+1 month"). Include a "next check-in" recommendation (when to run the next tier report). If any data quality issues were encountered, list them at the bottom.
**Output:** Final report delivered to user

## Quality Gate

- [ ] All contacts from batch accounted for (count matches expected total)
- [ ] Pipeline data is current (last HubSpot sync within 24 hours)
- [ ] Promise tracker status is up to date (no stale tasks)
- [ ] Report tier matches elapsed time (or deviation is acknowledged)
- [ ] Headline metric is clear and actionable
- [ ] Next check-in date recommended

## Handoffs

| Output | Destination | Skill/Person |
|--------|-------------|-------------|
| ROI report | CEO (Carlos) | Direct delivery |
| Stale promise alerts | delegation-engine | Escalation for overdue items |
| Attend-again recommendation | ops-targetops | Future event planning input |
| Tier accuracy insights | contact-intake (self) | Scoring framework calibration |

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| HubSpot source tags inconsistent | Contact count does not match expected batch size | Search by date range + source detail field as fallback; ask user to confirm expected count |
| Not enough time elapsed for meaningful pipeline data | T+1 week report requested but no follow-ups sent yet | Flag that data is premature; suggest checking back after follow-up window closes |
| Promise tracker tasks not tagged to batch | ClickUp search returns fewer tasks than expected | Search by date range and assignee; cross-reference with HubSpot notes |
| Event cost data unavailable | User cannot provide cost breakdown | Present pipeline metrics only; calculate ROI multiple as "pending cost input" |
| Prior event data incomplete for comparison | Tags or records missing from older batches | Present available data with caveats; recommend standardizing tags going forward |
| Deal data stale | Last HubSpot activity older than 7 days | Flag staleness; recommend pipeline review before finalizing report |
