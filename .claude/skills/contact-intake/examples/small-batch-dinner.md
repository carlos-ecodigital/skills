---
example: small-batch-dinner
scenario: 3 contacts from hosted networking dinner
source-type: event
contact-count: 3
tests: [direct-upload-path, host-introduced-modifier, social-first-tone, non-sales-routing]
success-criteria:
  - All 3 contacts have HubSpot records within 2 hours
  - CTO contact merged with existing HubSpot record (not duplicated)
  - Journalist routed to Tier N (ops-contextops only, no sales follow-up)
  - Host-introduced modifier (+0.3) applied to all 3 scores
  - Promise to send specs creates ClickUp task with 48hr deadline
failure-indicators:
  - Journalist receives sales email
  - CTO duplicated in HubSpot instead of merged
  - Direct-upload path not used (should not generate CSV for 3 contacts)
  - Host-introduced modifier missed
grader: human (Carlos or team lead)
last-reviewed: 2026-03-30
---

# Worked Example: Small Batch Dinner -- Amsterdam VC Networking Dinner

> Full pipeline walkthrough: 3 contacts from a curated networking dinner -> scored, routed, closed.
> Event: Private dinner hosted by Pim de Graaf (Managing Partner, Windmill Ventures), March 25 2026.
> Location: Restaurant Bougainville, Herenstraat 28, Amsterdam.
> Context: 12-person dinner focused on "Energy Transition x Digital Infrastructure." Pim personally introduced all guests.
> DE presence: Carlos attended as invited guest. No speaking role, social setting.

---

## Source Metadata

| Field | Value |
|-------|-------|
| batch_id | `EVT-2026-0325-WINDMILL` |
| source_type | event / dinner |
| event_name | Windmill Ventures Energy-Infra Dinner |
| event_date | 2026-03-25 |
| host | Pim de Graaf, Managing Partner, Windmill Ventures |
| host_hubspot_id | `HS-CON-44821` (existing contact, Tier B) |
| location | Amsterdam |
| contact_count | 3 |
| path | direct-upload (count <= 5 AND source != conference) |
| overlay | dinner/event: social-first tone, host-introduced modifier |

---

## W1: INGEST

**Trigger:** Carlos messages at 23:15 on March 25: "Just got back from dinner at Pim de Graaf's thing. Three people worth logging. Dumping notes + cards now."

### Raw Inputs Received

| # | Format | Description |
|---|--------|-------------|
| 1 | Handwritten notes | 1 page, Carlos's handwriting. Dinner seating chart, conversation notes for all three contacts. |
| 2 | Business card photo | Kees van der Linden, Thermion B.V. |
| 3 | Business card photo | Marc Oosterbeek, Atlas Infrastructure Partners |

No card for the journalist -- Carlos noted her details in his handwritten notes only.

### Extraction Results

#### Contact 1: Kees van der Linden (Business card #2 + Handwritten notes)

**Source:** Business card (clear, good lighting) + extensive handwritten notes

| Field | Extracted Value | Confidence |
|-------|----------------|------------|
| first_name | Kees | :green_circle: |
| last_name | van der Linden | :green_circle: |
| company | Thermion B.V. | :green_circle: |
| title | Chief Technology Officer | :green_circle: |
| email | k.vanderlinden@thermion.nl | :green_circle: |
| phone | +31 6 2198 7340 | :green_circle: |
| linkedin | /in/keesvanderlinden | :green_circle: (printed on card) |

**Handwritten notes (relevant portion, OCR):**
> "Kees - Thermion - CTO. District heating company based in Delft. 20 min deep conversation about heat recovery from DC exhaust air. They run 4 networks in Zuid-Holland, struggling with source temperature -- currently on geothermal + industrial waste but temp is borderline for their grid. Our 55-60C reject heat is exactly what they need. He asked very specific questions about our thermal interface specs and year-round supply profile. Promised to send him our technical heat recovery datasheet + the Westland thermal integration case study. He said he'd share their network topology maps so we can model the fit. Very engaged. Pim introduced us specifically because of the heat angle."

**Extracted context:**
- `conversation_topic`: Heat recovery from DC exhaust, source temperature challenges, thermal interface specs
- `conversation_duration`: ~20 minutes (Carlos's estimate)
- `promises_we_made`: Send technical heat recovery datasheet + Westland thermal integration case study
- `promises_they_made`: Share network topology maps for fit modeling
- `urgency_signal`: Active source temperature problem on existing networks
- `contact_type`: prospect
- `track`: S-DHN (district heating network)
- `acquisition_context`: Dinner, host-introduced (Pim specifically matched them on heat angle)
- `introduction_chain`: Pim de Graaf (Windmill Ventures) -> Kees van der Linden

All fields :green_circle:. Deep technical conversation with mutual commitments.

---

#### Contact 2: Marc Oosterbeek (Business card #3 + Handwritten notes)

**Source:** Business card (clear) + brief handwritten notes

| Field | Extracted Value | Confidence |
|-------|----------------|------------|
| first_name | Marc | :green_circle: |
| last_name | Oosterbeek | :green_circle: |
| company | Atlas Infrastructure Partners | :green_circle: |
| title | Partner | :green_circle: |
| email | m.oosterbeek@atlasinfra.com | :green_circle: |
| phone | +31 20 573 8200 | :green_circle: |
| linkedin | /in/marcoosterbeek | :green_circle: (printed on card) |

**Handwritten notes (relevant portion, OCR):**
> "Marc O. - Atlas Infra Partners. Investment fund, infra focus. Brief chat, maybe 3 min at the bar after dinner. Exchanged cards. He said they're looking at energy transition assets in NL but wasn't specific. Polite, not much substance. Card says Partner."

**Extracted context:**
- `conversation_topic`: Energy transition infrastructure investment (generic)
- `conversation_duration`: ~3 minutes
- `promises_we_made`: None
- `promises_they_made`: None
- `urgency_signal`: None
- `contact_type`: investor
- `track`: N/A (investor, not a track buyer)
- `acquisition_context`: Dinner, host-introduced (general introduction at start of evening)
- `introduction_chain`: Pim de Graaf (Windmill Ventures) -> Marc Oosterbeek

All fields :green_circle:. Minimal conversation context.

---

#### Contact 3: Sophie Jansen (Handwritten notes only -- no business card)

**Source:** Handwritten notes only

| Field | Extracted Value | Confidence |
|-------|----------------|------------|
| first_name | Sophie | :green_circle: |
| last_name | Jansen | :green_circle: |
| company | Energeia | :green_circle: |
| title | Senior Reporter | :yellow_circle: (Carlos wrote "reporter" -- title may differ) |
| email | s.jansen@energeia.nl | :yellow_circle: (Carlos wrote from memory, not verified) |
| phone | [not captured] | :red_circle: |
| linkedin | [not captured] | :red_circle: |

**Handwritten notes (relevant portion, OCR):**
> "Sophie Jansen - Energeia (FD energy publication). Senior reporter. Taking notes for an article about the dinner / energy-infra ecosystem in NL. We chatted briefly about DE but she was in journalist mode. She asked about the heat reuse angle -- I gave her the high-level version. She might write something. Email I think is s.jansen@energeia.nl but not 100%. No card."

**Extracted context:**
- `conversation_topic`: DE's heat reuse model (high-level, on the record)
- `conversation_duration`: ~5 minutes
- `promises_we_made`: None
- `promises_they_made`: None (may write an article, but no commitment)
- `urgency_signal`: None
- `contact_type`: press
- `track`: N/A (non-sales)
- `acquisition_context`: Dinner, host-introduced (part of general guest introductions)
- `introduction_chain`: Pim de Graaf (Windmill Ventures) -> Sophie Jansen

Name and company :green_circle:. Email :yellow_circle: -- needs verification. Phone/LinkedIn :red_circle: -- not blocking (press contact, not sales).

---

### W1 Summary: 3 Inputs -> 3 Raw Contact Records

| # | Name | Company | Source(s) | Confidence |
|---|------|---------|-----------|------------|
| 1 | Kees van der Linden | Thermion B.V. | Card + Notes | :green_circle: |
| 2 | Marc Oosterbeek | Atlas Infrastructure Partners | Card + Notes | :green_circle: |
| 3 | Sophie Jansen | Energeia | Notes only | :yellow_circle: |

---

## W2: CONSOLIDATE & QA

### Dedup Check Against HubSpot

| # | Name | Company | HubSpot Match? | Action |
|---|------|---------|----------------|--------|
| 1 | Kees van der Linden | Thermion B.V. | **YES** -- `HS-CON-31204`, created 2025-11-12, lifecycle: lead, last activity 2025-12-03 | **MERGE** -- update existing record, do not create duplicate |
| 2 | Marc Oosterbeek | Atlas Infrastructure Partners | No match | Create new record |
| 3 | Sophie Jansen | Energeia | No match | Create new record |

**Merge Detail: Kees van der Linden (Contact 1)**

Existing HubSpot record `HS-CON-31204`:
- Created from a webinar attendee list (Nov 2025)
- Has email + company + title. No phone number on file.
- Last activity: Downloaded DE whitepaper on waste heat recovery (Dec 3 2025)
- Lifecycle: Lead. No deal associated.

Merge strategy:
- Phone number: ADD (new data from card, not in HubSpot)
- LinkedIn: ADD (new data from card, not in HubSpot)
- Title: KEEP existing (both say CTO, no conflict)
- Notes: APPEND dinner conversation context to existing timeline
- Lifecycle: UPDATE from "Lead" to "Sales Qualified Lead" (conversation quality warrants upgrade)
- Tags: ADD `windmill-dinner-2026`, `S-DHN`
- Match confidence: 98% (exact name + exact company + same email domain)

> Merge confidence > 85% threshold. Auto-merge permitted per dedup-matching-rules.md.

### Team QA Dashboard

**Batch: Windmill Dinner March 2026 | Raw: 3 | Deduplicated: 3 (1 merge) | Parked: 0**

| # | Name | Company | :green_circle: | :yellow_circle: | :red_circle: | Action Needed |
|---|------|---------|------|------|------|---------------|
| 1 | Kees van der Linden | Thermion B.V. | 7/7 | 0 | 0 | Merge with HS-CON-31204 |
| 2 | Marc Oosterbeek | Atlas Infra Partners | 7/7 | 0 | 0 | None -- create new |
| 3 | Sophie Jansen | Energeia | 3/7 | 2 | 2 | Verify email, accept gaps (press) |

**Dashboard decision:** All :green_circle: or acceptable :yellow_circle:. Sophie's gaps are non-blocking for a press contact. Proceed to HubSpot.

### Path Decision

```
count = 3
source = dinner (NOT conference)
-> 3 <= 5 AND source != conference
-> DIRECT UPLOAD PATH
-> No review CSV generated
-> Append to running contacts_log_2026.csv after upload
```

---

## W3: HUBSPOT PUSH

Delegated to `sales-intake` for CRM writes.

| # | Name | HubSpot Action | Record ID | Tags Applied |
|---|------|---------------|-----------|-------------|
| 1 | Kees van der Linden | MERGE with HS-CON-31204 | `HS-CON-31204` (updated) | `windmill-dinner-2026`, `S-DHN`, `host-introduced`, `has-promises` |
| 2 | Marc Oosterbeek | CREATE new | `HS-CON-52107` (new) | `windmill-dinner-2026`, `investor`, `host-introduced` |
| 3 | Sophie Jansen | CREATE new | `HS-CON-52108` (new) | `windmill-dinner-2026`, `press`, `host-introduced`, `non-sales` |

Company records:
- Thermion B.V.: Existing (`HS-COMP-8891`). Contact linked.
- Atlas Infrastructure Partners: CREATE new (`HS-COMP-14320`). Contact linked.
- Energeia: CREATE new (`HS-COMP-14321`). Contact linked. Marked as `press_outlet`.

---

## W4: SCORING

### Contact 1: Kees van der Linden (Thermion B.V.)

**Base Dimensions:**

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| Conversation Quality | 30% | 4 | 20-min deep dive on specific use case (heat recovery), asked technical specs, discussed internal network challenges. Meets "Deep" criteria. |
| ICP Fit | 25% | 3 | Matches S-DHN strategic track (district heating). Not a primary track (C-NEO/C-ENT/C-INS) but strong adjacent fit. |
| Urgency Signals | 20% | 4 | Active source temperature problem on existing networks. Near-term need, evaluating solutions. |
| Strategic Value | 15% | 3 | CTO of a regional DHN operator. 4 networks = meaningful scale. Could become reference case for S-DHN track. |
| Commitment Density | 10% | 5 | Mutual locked: we send specs, they send topology maps. Both sides committed to specific deliverables. |

**Base score calculation:**

```
base = (4 * 0.30) + (3 * 0.25) + (4 * 0.20) + (3 * 0.15) + (5 * 0.10)
     = 1.20 + 0.75 + 0.80 + 0.45 + 0.50
     = 3.70
```

**Overrides:**
- Introduction chain: N/A -- Pim is Tier B, not Tier A. Intro chain override (+0.5) requires Tier A introducer. Not applied.
- Promise floor: APPLIES -- we made a specific named promise (send specs). Floor = min 2.5. Already above. No effect.
- Repeat encounter: APPLIES -- existing HubSpot record (webinar attendee Nov 2025). +0.5.
- Multi-threaded company: N/A -- only 1 contact from Thermion.

```
after_overrides = 3.70 + 0.50 = 4.20
```

**Context modifier:**
- Event host-introduced: +0.3

```
final_score = 4.20 + 0.30 = 4.50
```

**Cap check:** 4.50 <= 5.0. No cap applied.

**Tier assignment:** 4.50 -> **Tier A** (4.0-5.0)

---

### Contact 2: Marc Oosterbeek (Atlas Infrastructure Partners)

**Base Dimensions:**

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| Conversation Quality | 30% | 1 | ~3 min card swap at the bar. No substance. Meets "Card-swap / None" criteria. |
| ICP Fit | 25% | 2 | Infrastructure investor but no specificity. Energy transition broadly relevant but no DC/heat focus articulated. Tangential. |
| Urgency Signals | 20% | 1 | None. Generic "looking at energy transition assets." No timeline, no active process. |
| Strategic Value | 15% | 3 | Partner at an infra fund. Useful network access if fund is relevant. Could facilitate portfolio intros. |
| Commitment Density | 10% | 1 | None. Card exchange only. |

**Base score calculation:**

```
base = (1 * 0.30) + (2 * 0.25) + (1 * 0.20) + (3 * 0.15) + (1 * 0.10)
     = 0.30 + 0.50 + 0.20 + 0.45 + 0.10
     = 1.55
```

**Overrides:**
- Introduction chain: N/A -- Pim is Tier B.
- Promise floor: N/A -- no promises made.
- Repeat encounter: N/A -- no prior HubSpot record.
- Multi-threaded company: N/A.

```
after_overrides = 1.55
```

**Context modifier:**
- Event host-introduced: +0.3

```
final_score = 1.55 + 0.30 = 1.85
```

**Cap check:** 1.85 <= 5.0. No cap applied.

**Tier assignment:** 1.85 -> **Tier C** (1.0-2.4)

---

### Contact 3: Sophie Jansen (Energeia)

**Non-sales contact. Tier N assigned directly.**

Sophie is a journalist. She is not a buyer, partner, vendor, investor, or competitor. She falls into the `press` contact type.

Per SKILL.md tier table: non-sales contacts -> **Tier N** (ops-contextops only, no sales follow-up).

Scoring is recorded for completeness but does not drive routing:

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| Conversation Quality | 30% | 2 | ~5 min conversation. She asked about heat reuse -- but in journalist mode, gathering info for her article. |
| ICP Fit | 25% | 1 | Press. Completely outside DE's target market as a buyer. |
| Urgency Signals | 20% | 1 | None. May write an article but no commercial urgency. |
| Strategic Value | 15% | 2 | Energeia is a respected Dutch energy publication. Positive coverage has brand value. Not sales value. |
| Commitment Density | 10% | 1 | None. |

```
base = (2 * 0.30) + (1 * 0.25) + (1 * 0.20) + (2 * 0.15) + (1 * 0.10)
     = 0.60 + 0.25 + 0.20 + 0.30 + 0.10
     = 1.45
```

Context modifier (host-introduced): +0.3 -> **1.75**

Tier override: **Tier N** (press contact type overrides score-based tier assignment).

---

### Scoring Summary Table

| # | Name | Base | Overrides | Modifier | Final | Tier |
|---|------|------|-----------|----------|-------|------|
| 1 | Kees van der Linden | 3.70 | +0.50 (repeat) | +0.30 (host) | **4.50** | **A** |
| 2 | Marc Oosterbeek | 1.55 | -- | +0.30 (host) | **1.85** | **C** |
| 3 | Sophie Jansen | 1.45 | -- | +0.30 (host) | **1.75** | **N** |

---

## W5: ROUTE & FOLLOW-UP

### Tier A: Kees van der Linden -- 24hr follow-up deadline

**Delegation chain:** `counter-party-intel` -> `sales-intake` -> `ops-outreachops` -> `ops-meetingops`

**Step 1: Enrichment** (delegated to `counter-party-intel`)
- Quick profile on Thermion B.V.: network coverage, MW capacity, ownership, key personnel
- Enrichment priority: HIGH (Tier A, 24hr clock)

**Step 2: Follow-up email** (delegated to `ops-outreachops`)

Tone: **Social-first** (dinner overlay). Not a cold sales email. Reference the social setting, Pim's introduction, and the specific conversation.

Follow-up template guidance:
- Subject: Reference the dinner, not a sales pitch
- Opening: "It was great meeting you at Pim's dinner last night..."
- Body: Reference the specific heat recovery conversation, the source temperature challenge he described
- Attachment: Technical heat recovery datasheet + Westland thermal integration case study (as promised)
- Close: Suggest a follow-up call to discuss the topology maps he offered to share
- Tone: Warm, peer-to-peer, technically curious. Not salesy.

**Step 3: Promise tracking** (delegated to `delegation-engine`)

| Promise | Type | Owner | Deadline | ClickUp Task |
|---------|------|-------|----------|-------------|
| Send technical heat recovery datasheet | We made | Carlos (or delegate) | 2026-03-27 (48hr) | CREATE: "[Promise] Send heat recovery datasheet to Kees @ Thermion" |
| Send Westland thermal integration case study | We made | Carlos (or delegate) | 2026-03-27 (48hr) | Same task as above (bundled) |
| Share network topology maps | They made | Kees van der Linden | 2026-04-01 (soft, 1 week) | HubSpot task: follow up if not received by April 1 |

**Step 4: Meeting scheduling** (delegated to `ops-meetingops`)
- Placeholder: 30-min call within 1 week of specs delivery
- Attendees: Carlos + Kees (+ possibly Kees's team member if he brings one)

---

### Tier C: Marc Oosterbeek -- 1 week follow-up

**Delegation chain:** `ops-outreachops` (lightweight) -> nurture

**Follow-up email** (delegated to `ops-outreachops`)

Tone: **Social-first, low-pressure.** Brief note acknowledging the dinner. No pitch.

Follow-up template guidance:
- Subject: "Good to meet you at Pim's dinner"
- Body: 2-3 sentences. "Enjoyed the evening. If energy-infra investments cross your desk that touch data centers or heat networks, happy to be a sounding board."
- No attachment. No ask. Plant the seed.
- Timing: Send within 1 week.

No promises to track. No enrichment needed. CRM record exists for future reference.

---

### Tier N: Sophie Jansen -- NO sales follow-up

**Delegation chain:** `ops-contextops` only

**Actions:**
1. Log relationship record in `ops-contextops`: journalist, Energeia, met at Windmill dinner
2. Tag in HubSpot: `press`, `non-sales`, `energeia`
3. **Do NOT send any follow-up email.** No sales outreach. No nurture sequence.
4. If she publishes an article mentioning DE or the dinner, `ops-contextops` captures it as a media mention.
5. If Carlos wants to proactively offer a quote or interview for her article, that's a manual CEO decision -- not an automated pipeline action.

> CRITICAL: Sophie must never enter any sales or marketing automation. Tier N contacts are CRM-record-only with contextops routing.

---

## Completion Gate

- [x] Zero unprocessed contacts (3/3 processed)
- [x] Every contact has HubSpot record + tier + routed action
  - Kees: HS-CON-31204 (merged), Tier A, follow-up + promises tracked
  - Marc: HS-CON-52107 (new), Tier C, lightweight follow-up
  - Sophie: HS-CON-52108 (new), Tier N, contextops only
- [x] All promises-we-made have assigned owners + deadlines
  - Send specs to Kees: ClickUp task, 48hr deadline, assigned to Carlos
- [x] Appended to `contacts_log_2026.csv` (direct-upload path, no review CSV)
- [x] ROI baseline snapshot: 3 contacts, 1 Tier A, 1 Tier C, 1 Tier N

**Batch status: CLOSED**

---

## Key Test Validations

| Test | Expected | Actual | Pass? |
|------|----------|--------|-------|
| Direct-upload path used (no CSV review) | Yes -- 3 contacts, non-conference | Direct upload executed | PASS |
| Host-introduced modifier (+0.3) | Applied to all 3 | +0.3 on all 3 final scores | PASS |
| Social-first follow-up tone | Dinner overlay, not cold-email | Follow-up references dinner, Pim, conversation | PASS |
| Journalist -> Tier N | Sophie classified as non-sales | Tier N, ops-contextops only routing | PASS |
| No sales email to journalist | Sophie excluded from outreach | No follow-up email delegated | PASS |
| CTO dedup / merge | Kees matched to HS-CON-31204 | Merged, not duplicated. 98% confidence. | PASS |
| Promise creates ClickUp task | Specs promise -> task with 48hr deadline | Task created: due 2026-03-27 | PASS |
| Repeat encounter override | Kees has prior HubSpot record | +0.5 override applied | PASS |
