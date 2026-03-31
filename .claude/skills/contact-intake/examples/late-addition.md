---
example: late-addition
scenario: 2 contacts added to closed conference batch 5 days late
source-type: conference (late addition)
contact-count: 2
tests: [batch-reopen-protocol, dedup-against-batch, multi-threaded-flag, csv-append, deadline-reset, event-reference-despite-delay]
success-criteria:
  - Closed batch reopened cleanly with audit trail
  - Both contacts added to existing batch CSV
  - Contact 2's company flagged multi-threaded (another contact already in batch)
  - Follow-up deadlines calculated from today (March 30) not event date (March 25)
  - Follow-up messages reference Datacloud naturally despite 5-day gap
  - Batch re-closed with updated completion gate
failure-indicators:
  - New batch created instead of reopening existing one
  - Deadlines calculated from event date (stale by 5 days)
  - Multi-threaded flag missed on Contact 2
  - Follow-up fails to reference the conference
  - Batch CSV not updated (contacts exist in HubSpot but not in batch tracking)
  - Original batch contacts disturbed or re-scored
grader: human (Carlos or team lead)
last-reviewed: 2026-03-30
---

# Worked Example: Late Addition -- 2 Contacts Added to Closed Datacloud Batch

> Pipeline walkthrough: 2 late contacts appended to a previously closed conference batch.
> Original batch: "Datacloud Europe 2026" -- 15 contacts, processed and closed March 26.
> Late additions discovered: March 30 (5 days after event, 4 days after batch close).
> Contacts: 1 from crumpled business card, 1 from LinkedIn connection request.

---

## Source Metadata

| Field | Value |
|-------|-------|
| original_batch_id | `CONF-2026-0325-DATACLOUD` |
| original_event | Datacloud Europe 2026, Monaco, March 24-25 |
| original_batch_status | CLOSED (March 26, 18:00) |
| original_contact_count | 15 (processed, scored, routed) |
| late_addition_date | 2026-03-30 |
| days_since_event | 5 |
| days_since_batch_close | 4 |
| late_contact_count | 2 |
| path | CSV append (conference source = always CSV, even for late additions) |

---

## Batch Reopen Protocol

**Trigger:** Carlos messages on March 30: "Found two more from Datacloud. Crumpled card in my jacket and a LinkedIn request I missed. Can you add them to the Datacloud batch?"

### Step 1: Locate and Validate Original Batch

Batch `CONF-2026-0325-DATACLOUD` located:
- **Status:** CLOSED
- **Close date:** 2026-03-26 18:00
- **Contacts:** 15 processed, all scored and routed
- **CSV:** `Datacloud_Europe_2026_contacts_review.csv` (Google Drive)
- **Completion gate:** All items checked off

### Step 2: Reopen Batch

Batch status changed: CLOSED -> **REOPENED (late addition)**

Audit trail entry:
```
[2026-03-30 10:15] Batch CONF-2026-0325-DATACLOUD reopened for late addition.
Reason: 2 additional contacts discovered post-close.
Reopened by: Carlos (via contact-intake skill).
Original close: 2026-03-26 18:00 (15 contacts).
Expected re-close: 2026-03-30 (same day, after processing).
```

### Step 3: Deadline Reset Rule

> CRITICAL: All follow-up deadlines for late additions are calculated from TODAY (March 30), not from the event date (March 25) or original batch close date (March 26).

Rationale: Contacts discovered 5 days late cannot meet original deadlines. Using stale deadlines would either (a) trigger immediate escalation alerts for already-missed deadlines or (b) create confusion about which contacts are genuinely overdue. Fresh deadlines from discovery date preserve the urgency framework's integrity.

| Tier | Standard Deadline | Late-Addition Deadline (from March 30) |
|------|-------------------|---------------------------------------|
| A | 24hr from event | March 31 (24hr from discovery) |
| B | 48-72hr from event | April 1-2 (48-72hr from discovery) |
| C | 1 week from event | April 6 (1 week from discovery) |

---

## W1: INGEST

### Raw Inputs Received

| # | Format | Description |
|---|--------|-------------|
| 1 | Business card photo | Crumpled card found in suit jacket pocket. Partially creased but legible. German text. |
| 2 | LinkedIn screenshot | Connection request from someone Carlos met at Datacloud conference bar on Day 2 evening. |

### Extraction Results

#### Late Contact 1: Thomas Krause (Crumpled business card)

**Source:** Business card photo (crumpled, creases across middle, but text legible)

| Field | Extracted Value | Confidence |
|-------|----------------|------------|
| first_name | Thomas | :green_circle: |
| last_name | Krause | :green_circle: |
| company | RheinData GmbH | :green_circle: |
| title | Geschaftsfuhrer (Managing Director) | :green_circle: |
| email | t.krause@rheindata.de | :green_circle: |
| phone | +49 221 9876 5400 | :green_circle: |
| address | Konrad-Adenauer-Ufer 11, 50668 Koln | :green_circle: |
| website | www.rheindata.de | :green_circle: |

**Carlos's verbal context (provided with the card):**
"Thomas runs a mid-sized colocation provider in Cologne. We talked for maybe 10 minutes at the networking lunch on Day 1. He's expanding their facility and looking at liquid cooling. I think he mentioned 5MW of new capacity. German guy, very technical, asked about our power density capabilities."

**Extracted context:**
- `conversation_topic`: Liquid cooling, power density, facility expansion (5MW new capacity)
- `conversation_duration`: ~10 minutes
- `promises_we_made`: None recalled
- `promises_they_made`: None recalled
- `urgency_signal`: Active expansion (5MW new capacity build)
- `contact_type`: prospect
- `track`: C-ENT (enterprise colocation operator)
- `acquisition_context`: Conference networking lunch, Day 1
- `late_addition_reason`: Card found in jacket pocket 5 days post-event

All fields :green_circle:. Good extraction despite crumpled card.

---

#### Late Contact 2: Erik Visser (LinkedIn connection request)

**Source:** LinkedIn connection request screenshot

**LinkedIn connection request content:**

> **Erik Visser** wants to connect
> Independent Energy Consultant | Grid Strategy & Renewables | Netherlands
> "Hi Carlos, great talking with you at the Datacloud bar on Tuesday evening. Your approach to integrating heat recovery with DC operations is very interesting. Would love to continue the conversation. I'm advising a few parties in the Dutch energy space who might benefit from what you're building."

| Field | Extracted Value | Confidence |
|-------|----------------|------------|
| first_name | Erik | :green_circle: |
| last_name | Visser | :green_circle: |
| company | Independent (self-employed consultant) | :green_circle: |
| title | Independent Energy Consultant | :green_circle: |
| email | [not on LinkedIn request] | :red_circle: |
| phone | [not on LinkedIn request] | :red_circle: |
| linkedin | /in/erikvisser-energy | :green_circle: (from connection request URL) |

**Extracted context:**
- `conversation_topic`: Heat recovery + DC operations integration. Erik advises parties in Dutch energy.
- `conversation_duration`: Unknown (bar conversation, likely 15-30 min given the "great talking" framing)
- `promises_we_made`: None
- `promises_they_made`: Implied offer to connect Carlos with his advisory clients
- `urgency_signal`: None explicit. Exploratory advisor interest.
- `contact_type`: advisor
- `track`: N/A (advisor, not a direct buyer)
- `acquisition_context`: Conference bar, Day 2 evening
- `late_addition_reason`: LinkedIn request accepted 5 days post-event

Name and company :green_circle:. LinkedIn :green_circle:. Email and phone :red_circle: -- to be captured via LinkedIn messaging.

---

### W1 Summary: 2 Late Inputs -> 2 Raw Contact Records

| # | Name | Company | Source(s) | Confidence | Late Reason |
|---|------|---------|-----------|------------|-------------|
| L1 | Thomas Krause | RheinData GmbH | Crumpled card | :green_circle: | Card in jacket pocket |
| L2 | Erik Visser | Independent | LinkedIn request | :green_circle: / :red_circle: | LinkedIn request accepted late |

---

## W2: CONSOLIDATE & QA

### Dedup Check: HubSpot AND Existing Batch

Late additions require TWO dedup passes:
1. **HubSpot dedup:** Standard check against all HubSpot contacts
2. **Batch dedup:** Check against the 15 contacts already in `CONF-2026-0325-DATACLOUD`

#### Thomas Krause -- Dedup Results

| Check | Match? | Detail |
|-------|--------|--------|
| HubSpot | No match | No existing record for Thomas Krause or RheinData GmbH |
| Batch CSV | No match | RheinData not represented in the original 15 contacts |

Result: CREATE new. No dedup concerns.

#### Erik Visser -- Dedup Results

| Check | Match? | Detail |
|-------|--------|--------|
| HubSpot | No match | No existing record for Erik Visser |
| Batch CSV | **COMPANY OVERLAP** | Original batch contains **Dirk Mulder, Senior Grid Advisor, independent consultant** who also advises Dutch energy parties. However, different person, different company entity. False positive -- independent consultants are not the same "company." |

Wait -- let me recheck. The batch CSV also contains:

| Batch Contact #8 | Name | Company |
|---|---|---|
| 8 | Sanne de Vries | Liander N.V. |

And batch contact #12:

| Batch Contact #12 | Name | Company |
|---|---|---|
| 12 | Willem Hofstra | Hofstra Energy Advies |

Erik is independent, so "company" dedup doesn't trigger on name match. But let me check if Erik's *advisory clients* overlap with batch contacts. His LinkedIn says he advises "parties in the Dutch energy space." This is relevant context but NOT a dedup issue.

However, upon deeper check of the batch CSV:

| Batch Contact #5 | Name | Company |
|---|---|---|
| 5 | Pieter Groen | GreenPower Consultancy B.V. |

GreenPower Consultancy and Erik Visser are both independent energy consultants operating in the Dutch market. Carlos confirms: "Erik mentioned he sometimes works with Pieter Groen on grid projects. They're not the same firm but they collaborate."

**Multi-threaded flag decision:** Erik and Pieter are at different companies. Multi-threaded flag requires 2+ contacts at the SAME organization. However, the collaboration note is captured as a relationship signal for `ops-contextops`.

**Revised dedup conclusion:** Actually, reviewing the original batch more carefully -- batch contact #14 is:

| Batch Contact #14 | Name | Company |
|---|---|---|
| 14 | Anna Brinkmann | RheinData GmbH |

Wait -- Anna Brinkmann from RheinData GmbH is already in the batch. Thomas Krause is ALSO from RheinData GmbH.

**MULTI-THREADED FLAG TRIGGERED on Thomas Krause:**
- Thomas Krause (Late Contact 1): Managing Director, RheinData GmbH
- Anna Brinkmann (Batch Contact #14): Head of Business Development, RheinData GmbH

Two contacts from the same organization in this batch -> `multi_threaded = true` for Thomas Krause. Multi-threaded bonus (+0.5) applies at scoring.

Carlos confirms: "Oh right, Anna from RheinData was at the booth on Day 2. Thomas is her boss -- I met him separately at lunch on Day 1. They probably don't know I talked to both of them."

> NOTE: Multi-threaded insight is valuable. Follow-up to Thomas should subtly acknowledge awareness of RheinData's broader engagement without name-dropping Anna (she may not have told Thomas she visited our booth). Let `ops-outreachops` handle the nuance.

### Team QA Dashboard (Late Additions Only)

**Batch: Datacloud Europe 2026 (REOPENED) | Late additions: 2 | New total: 17**

| # | Name | Company | :green_circle: | :yellow_circle: | :red_circle: | Action Needed |
|---|------|---------|------|------|------|---------------|
| L1 | Thomas Krause | RheinData GmbH | 8/8 | 0 | 0 | Multi-threaded flag (Anna Brinkmann in batch) |
| L2 | Erik Visser | Independent | 4/8 | 0 | 4 | Email/phone via LinkedIn. Accept gaps for now. |

### Path Decision

```
source = conference -> ALWAYS CSV PATH
action = APPEND to existing CSV (not generate new)
```

Late additions are appended to the existing review CSV, not processed through a separate CSV. This maintains the single-batch-single-CSV principle.

---

## W3: HUBSPOT PUSH

Delegated to `sales-intake` for CRM writes.

| # | Name | HubSpot Action | Record ID | Tags Applied |
|---|------|---------------|-----------|-------------|
| L1 | Thomas Krause | CREATE new | `HS-CON-52415` (new) | `datacloud-europe-2026`, `C-ENT`, `late-addition`, `multi-threaded-rheindata` |
| L2 | Erik Visser | CREATE new | `HS-CON-52416` (new) | `datacloud-europe-2026`, `advisor`, `late-addition`, `needs-email` |

Company records:
- RheinData GmbH: EXISTS (`HS-COMP-11203`, created during original batch for Anna Brinkmann). Thomas linked to same company.
- Erik Visser (Independent): CREATE new company record `HS-COMP-14405` ("Erik Visser Energy Consulting" -- placeholder for independent consultant).

---

## W4: SCORING

### Late Contact 1: Thomas Krause (RheinData GmbH)

**Base Dimensions:**

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| Conversation Quality | 30% | 3 | ~10 min substantive discussion. Explored power density and liquid cooling. Asked technical questions. Meets "Substantive" criteria. |
| ICP Fit | 25% | 4 | C-ENT track. Mid-sized colocation operator expanding capacity. Right industry, right role (MD = decision-maker), plausible buyer. Strong fit. |
| Urgency Signals | 20% | 4 | Active 5MW expansion. Near-term: building new capacity implies vendor selection within 6 months. |
| Strategic Value | 15% | 3 | Managing Director of a mid-sized German colo. German market entry reference case potential. Useful but not transformative. |
| Commitment Density | 10% | 1 | No commitments from either side. Card exchange + conversation. |

**Base score calculation:**

```
base = (3 * 0.30) + (4 * 0.25) + (4 * 0.20) + (3 * 0.15) + (1 * 0.10)
     = 0.90 + 1.00 + 0.80 + 0.45 + 0.10
     = 3.25
```

**Overrides:**
- Introduction chain: N/A -- no introduction, met at networking lunch.
- Promise floor: N/A -- no promises made.
- Repeat encounter: N/A -- no prior HubSpot record.
- Multi-threaded company: APPLIES -- Anna Brinkmann (RheinData) already in batch. +0.5.

```
after_overrides = 3.25 + 0.50 = 3.75
```

**Context modifier:**
- Conference (no specific sub-modifier): Thomas was neither a speaker, booth visitor, nor sponsor. He was a general conference attendee met at a networking lunch. No conference sub-modifier applies. +0.0.

```
final_score = 3.75 + 0.00 = 3.75
```

**Cap check:** 3.75 <= 5.0. No cap applied.

**Tier assignment:** 3.75 -> **Tier B** (2.5-3.9)

---

### Late Contact 2: Erik Visser (Independent Consultant)

**Base Dimensions:**

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| Conversation Quality | 30% | 3 | Bar conversation, likely 15-30 min based on "great talking" framing. Discussed heat recovery + DC ops in enough detail for Erik to reference it specifically. Substantive. |
| ICP Fit | 25% | 2 | Independent consultant. Not a buyer. Tangential -- could be a channel to buyers, but he himself is not ICP. |
| Urgency Signals | 20% | 2 | Exploratory. "Would love to continue the conversation." No timeline, no active process. His clients may have urgency, but that's indirect. |
| Strategic Value | 15% | 3 | Advisor to multiple Dutch energy parties. Potential multiplier -- if he recommends DE to clients, could generate warm introductions. Useful network. |
| Commitment Density | 10% | 2 | Soft intent. LinkedIn connection request + offer to continue conversation. No specifics. |

**Base score calculation:**

```
base = (3 * 0.30) + (2 * 0.25) + (2 * 0.20) + (3 * 0.15) + (2 * 0.10)
     = 0.90 + 0.50 + 0.40 + 0.45 + 0.20
     = 2.45
```

**Overrides:**
- Introduction chain: N/A.
- Promise floor: N/A.
- Repeat encounter: N/A.
- Multi-threaded company: N/A (independent consultant, no company overlap).

```
after_overrides = 2.45
```

**Context modifier:**
- Conference, no sub-modifier: +0.0.

```
final_score = 2.45 + 0.00 = 2.45
```

**Cap check:** 2.45 <= 5.0. No cap applied.

**Tier assignment:** 2.45 -> **Tier C** (1.0-2.4)

---

### Scoring Summary Table (Late Additions Only)

| # | Name | Base | Overrides | Modifier | Final | Tier |
|---|------|------|-----------|----------|-------|------|
| L1 | Thomas Krause | 3.25 | +0.50 (multi-threaded) | +0.00 | **3.75** | **B** |
| L2 | Erik Visser | 2.45 | -- | +0.00 | **2.45** | **C** |

---

## W5: ROUTE & FOLLOW-UP

### Tier B: Thomas Krause -- 48-72hr deadline (from March 30)

**Follow-up deadline:** April 1-2 (NOT March 27-28 which would be the deadline from event date)

**Delegation chain:** `counter-party-intel` -> `ops-outreachops`

**Step 1: Enrichment** (delegated to `counter-party-intel`)
- Quick profile on RheinData GmbH: facility size, customer base, expansion plans
- Cross-reference with Anna Brinkmann's existing intel from original batch
- Enrichment priority: STANDARD (Tier B)

**Step 2: Follow-up email** (delegated to `ops-outreachops`)

Tone: Conference follow-up, acknowledging the delay honestly.

> CRITICAL: Follow-up must reference Datacloud naturally despite the 5-day gap. Do NOT pretend it just happened. Acknowledge the delay lightly.

Follow-up template guidance:
- Subject: "Following up from Datacloud -- our power density conversation"
- Opening: "Thomas, I've been meaning to follow up since our conversation at the Datacloud networking lunch last week..."
- Body: Reference the specific conversation about liquid cooling and 5MW expansion. Show recall of his technical questions.
- Close: Suggest a call to explore how DE's power density approach could support RheinData's expansion.
- Tone: Professional, slightly apologetic about delay without over-explaining. Technical credibility.

> NOTE on multi-threaded awareness: The email to Thomas should NOT mention Anna Brinkmann. The follow-up team (`ops-outreachops`) is briefed that RheinData has two contacts, but the initial outreach to Thomas is direct. The multi-threaded strategy (coordinated engagement with both contacts) is planned after Thomas responds. `ops-outreachops` owns this coordination.

**No promises to track.** No commitments were made at the conference.

---

### Tier C: Erik Visser -- 1 week deadline (from March 30)

**Follow-up deadline:** April 6 (NOT April 1 from event date)

**Delegation chain:** `ops-outreachops` (lightweight) -> nurture

**Step 1: Accept LinkedIn connection** (if not already done)

Carlos should accept Erik's LinkedIn connection request. This is the primary channel since no email exists.

**Step 2: LinkedIn message** (delegated to `ops-outreachops`)

Tone: Warm conference follow-up, advisor-appropriate. Not a sales pitch -- Erik is an advisor, not a buyer.

Follow-up template guidance:
- "Erik, thanks for connecting. Really enjoyed our conversation at Datacloud last week -- your perspective on grid strategy for DC operations was very insightful."
- "Would be great to continue the conversation. If any of your advisory clients are exploring waste heat integration or high-density colocation, I'd welcome an introduction."
- Timing: Within 1 week of discovery (by April 6).
- Channel: LinkedIn message (no email available).

**No promises to track.**

---

## CSV Append

### Update to Batch CSV

**File:** `Datacloud_Europe_2026_contacts_review.csv`

Two rows appended to the existing 15-row CSV:

| Row | first_name | last_name | company | title | email | phone | source | conversation_topic | contact_type | late_addition | discovery_date | confidence |
|-----|------------|-----------|---------|-------|-------|-------|--------|-------------------|--------------|---------------|---------------|------------|
| 16 | Thomas | Krause | RheinData GmbH | Managing Director | t.krause@rheindata.de | +49 221 9876 5400 | Card (late) | Liquid cooling, 5MW expansion | prospect | Yes | 2026-03-30 | green |
| 17 | Erik | Visser | Independent | Energy Consultant | -- | -- | LinkedIn (late) | Heat recovery, DC ops, advisor | advisor | Yes | 2026-03-30 | yellow |

`late_addition` column added to flag these rows. Original 15 rows have `late_addition = No`.

CSV saved back to Google Drive. Version note: "v2 -- 2 late additions appended (Thomas Krause, Erik Visser). March 30."

---

## Batch Re-Close

### Updated Completion Gate

- [x] Zero unprocessed contacts (17/17 processed -- original 15 + 2 late)
- [x] Every contact has HubSpot record + tier + routed action
  - Thomas Krause: HS-CON-52415, Tier B, email follow-up
  - Erik Visser: HS-CON-52416, Tier C, LinkedIn follow-up
- [x] All promises-we-made have assigned owners + deadlines (no new promises from late additions)
- [x] Review CSV updated and saved to Google Drive (v2, 17 rows)
- [x] ROI baseline snapshot updated: 17 contacts (was 15), +1 Tier B, +1 Tier C

### Batch Status Change

```
REOPENED (late addition) -> CLOSED (v2)

[2026-03-30 11:45] Batch CONF-2026-0325-DATACLOUD re-closed.
Late additions processed: 2 (Thomas Krause, Erik Visser).
Total contacts: 17 (was 15).
Re-closed by: contact-intake skill.
Note: If further late contacts surface, batch can be reopened again.
```

**Batch status: CLOSED (v2)**

---

## Key Test Validations

| Test | Expected | Actual | Pass? |
|------|----------|--------|-------|
| Batch reopen protocol | Existing batch reopened, not new batch created | CONF-2026-0325-DATACLOUD reopened with audit trail | PASS |
| Dedup against existing batch | Thomas checked against 15 batch contacts | Anna Brinkmann (RheinData) found in batch | PASS |
| Multi-threaded flag | Thomas + Anna = 2 contacts at RheinData | multi_threaded flag set, +0.5 override applied | PASS |
| CSV append (not replace) | 2 rows added to existing 15-row CSV | Rows 16-17 appended, v2 saved | PASS |
| Deadline reset from today | Deadlines from March 30, not March 25 | Thomas: Apr 1-2, Erik: Apr 6 | PASS |
| Event reference despite delay | Follow-up mentions Datacloud naturally | "since our conversation at Datacloud last week" | PASS |
| Original contacts undisturbed | 15 original contacts not re-scored or re-routed | Original rows untouched in CSV | PASS |
| Late-addition tagging | Both contacts marked as late additions | `late-addition` tag in HubSpot, `late_addition=Yes` in CSV | PASS |
| Batch version tracking | Re-close creates v2 with updated counts | Batch closed as v2, count updated to 17 | PASS |
