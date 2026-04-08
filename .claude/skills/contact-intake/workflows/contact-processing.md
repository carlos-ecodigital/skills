---
workflow: contact-processing
version: 1.0.0
owner: contact-intake
trigger: "process these contacts", "new contacts", "conference dump", "just got back from [event]"
frequency: ad-hoc
estimated-duration: 30-90 minutes depending on volume
inputs:
  - Raw contact materials in any format (photos, notes, voice memos, WhatsApp screenshots, LinkedIn messages, text dumps, CSVs)
outputs:
  - HubSpot records created (contacts + companies)
  - Contacts scored and tiered (A/B/C/V/X/N/-)
  - Follow-ups initiated per tier cadence
  - Promises tracked with owners and deadlines
  - Review CSV saved to Google Drive (if applicable)
tools:
  - Claude vision (built-in, OCR + image parsing)
  - HubSpot MCP (via sales-intake)
  - ClickUp MCP (via delegation-engine)
  - Gmail MCP (via ops-outreachops)
  - Google Calendar MCP
  - WebSearch
  - Fireflies MCP (transcript cross-reference — manual workaround, see Step 6 note)
last-updated: 2026-03-26
---

# Contact Processing Pipeline (W1-W5)

## Purpose

Process raw contacts from any source into scored, tiered, CRM-resident records with active follow-up plans and promise tracking, ensuring zero contacts fall through the cracks.

## Prerequisites

- [ ] Raw contact materials available (photos, notes, text, CSV, screenshots, etc.)
- [ ] HubSpot MCP accessible via `sales-intake`
- [ ] ClickUp MCP accessible via `delegation-engine`
- [ ] Gmail MCP accessible via `ops-outreachops`
- [ ] Google Calendar MCP accessible
- [ ] Source context known or obtainable (event name, date, type)

---

## Steps

### Step 1: Capture Source Metadata

**Who:** contact-intake
**Tool:** Direct conversation with user
**Input:** User trigger phrase and any context provided
**Action:**
1. Identify the source type: `conference` | `event` | `meeting` | `referral` | `inbound` | `random` | `whatsapp`.
2. Capture event/source name (e.g., "Datacloud Europe 2026").
3. Capture date of encounter(s) in YYYY-MM-DD format.
4. Capture location if available (city, venue, or "virtual").
5. Ask for any introduction chain context ("Who introduced you?").
6. Determine if a W0 pre-conference activation was run (check for existing target list).
7. If source is `conference`, note: CSV path is mandatory regardless of contact count.

**Output:** Source metadata object: `{source_type, source_detail, source_date, location_met, introduction_chain, w0_target_list_exists}`.
**If blocked:** If user cannot specify source, default to `random` with today's date. Flag for later enrichment.

---

### Step 2: Accept and Process All Input Formats

**Who:** contact-intake
**Tool:** Claude vision (OCR), text parsing
**Input:** Raw materials from user + source metadata from Step 1
**Action:**
1. Inventory all inputs by format type (reference `references/input-format-handlers.md` for per-format extraction instructions).
2. For each input, apply the appropriate handler:
   - **Photos / business cards:** Claude vision OCR. Extract name, title, company, email, phone, LinkedIn. Note confidence per field.
   - **Handwritten notes:** Claude vision OCR. Extract names, companies, conversation context, promises. Flag illegible sections.
   - **WhatsApp screenshots:** Parse message threads. Extract contact info, conversation content, phone numbers.
   - **LinkedIn screenshots/messages:** Extract profile data, message content, connection context.
   - **Voice memo transcripts:** NLP extraction of names, companies, action items, promises.
   - **CSV/spreadsheet:** Map columns to schema fields. Validate and normalize.
   - **Free text / brain dump:** NLP extraction into structured fields. Flag ambiguous entries.
3. For each extracted contact, populate the intermediate record per `references/contact-record-schema.md`:
   - All Identity fields (name required; company required; others as available).
   - All Context fields (source_type, source_detail, source_date from Step 1).
   - Conversation fields (summary, quality, interest signal).
   - Classification fields (contact_type, icp_track).
   - Promise fields (promises_we_made, promises_they_made).
4. Assign per-field confidence: `high` | `medium` | `low`.
5. Populate `parse_notes` with any OCR issues, illegible text, or best guesses.
6. Populate `sources` list referencing the raw input file/type.

**Output:** Array of raw intermediate contact records with confidence flags and parse notes.
**If blocked:** If an input is completely unreadable, log it as a failed extraction with `row_review: needs_fix` and `parse_notes` describing the issue. Continue with remaining inputs.

---

### Step 3: Person-Level Dedup Matching

**Who:** contact-intake
**Tool:** Algorithmic matching (reference `references/dedup-matching-rules.md`)
**Input:** Array of raw contact records from Step 2
**Action:**
1. Run the matching cascade in priority order for every pair of records:
   - Priority 1: Exact email match (100% confidence).
   - Priority 2: LinkedIn URL match after normalization (95% confidence).
   - Priority 3: Name + company fuzzy match with normalization rules (90% confidence).
   - Priority 4: Phone number match after E.164 normalization (85% confidence).
   - Priority 5: Name + conversation context overlap (70% confidence). Flag for human review.
2. Apply all normalization rules:
   - Email: lowercase, trim whitespace.
   - LinkedIn: strip protocol, `www.`, trailing `/`, query params.
   - Names: strip diacritics, normalize prefixes (de/van/von/di/el/al), handle first-initial matches, name-order tolerance, hyphen normalization. Do NOT auto-match nicknames.
   - Company: strip legal suffixes (GmbH, AG, Inc., Ltd., etc.), normalize spacing, check known aliases.
   - Phone: remove non-digits, handle country codes, store E.164 format.
3. For each match found, assign a merge decision label:
   - `MERGED`: Two or more input sources combined.
   - `REVIEW`: 70-85% confidence match. Requires human confirmation.
   - `NEW`: No duplicates detected.

**Output:** Deduplicated contact set with merge decision labels and match confidence scores.
**If blocked:** If matching is ambiguous for a pair, label as `REVIEW` and present both records side-by-side in Step 8. Never auto-merge below 85% confidence.

---

### Step 4: Source Fusion (Merge Richest Data Per Field)

**Who:** contact-intake
**Tool:** Algorithmic merge per `references/dedup-matching-rules.md` merge protocol
**Input:** Deduplicated contact set from Step 3
**Action:**
1. For each `MERGED` set, apply per-field priority rules:
   - `name`: Business card > LinkedIn > other.
   - `title`: LinkedIn > business card > notes.
   - `company`: Business card > LinkedIn > notes.
   - `email`: Business card (work) > email forward > WhatsApp.
   - `phone`: WhatsApp > business card > notes.
   - `linkedin`: LinkedIn screenshot > business card > notes.
   - `conversation_summary`: MERGE ALL with `[source]` prefix per entry.
   - `conversation_quality`: Take highest.
   - `interest_signal`: Take highest.
   - `promises_we_made` / `promises_they_made`: MERGE ALL, deduplicate exact matches.
   - `source_type` / `source_detail`: List all.
   - `source_date`: Take earliest.
   - `confidence`: Take highest per field.
2. After merge, recalculate overall record confidence. If any required field is `low`, set `row_review: needs_fix`.

**Output:** Fused contact records with richest available data per field and updated confidence maps.
**If blocked:** If priority source is unclear (e.g., two business cards with conflicting data), flag the specific field as `medium` confidence and set `row_review: needs_fix`.

---

### Step 5: Company Grouping

**Who:** contact-intake
**Tool:** Algorithmic grouping
**Input:** Fused contact records from Step 4
**Action:**
1. Normalize all company names (strip legal suffixes, lowercase, trim).
2. Group contacts sharing the same normalized company name.
3. For groups with 2+ contacts, flag as "multi-threaded".
4. Generate a company summary per group:
   - Company name (normalized).
   - Contact count + names.
   - Roles covered (list of titles).
   - Aggregate conversation quality (highest across group).
   - Multi-threaded flag.
   - Account strategy note: "Multiple entry points at [Company]. Consider coordinated outreach."
5. Populate the `Company Group` column for the review CSV:
   - Single contact from company: leave blank.
   - Multiple: `"CompanyName (N)"` where N = count.

**Output:** Grouped contact set with company summaries and multi-threaded flags.
**If blocked:** If company name is missing or ambiguous, group under "Unknown Company" and flag for resolution in Step 8.

---

### Step 6: Cross-Reference HubSpot and Existing Records

**Who:** contact-intake
**Tool:** HubSpot MCP (via sales-intake), Fireflies MCP (manual workaround)
**Input:** Grouped contact set from Step 5
**Action:**
1. For each contact, run the cross-reference protocol in order:
   - Search HubSpot by email (exact).
   - Search HubSpot by name + company (fuzzy).
   - Search HubSpot by phone (normalized).
   - Search ops-contextops relationship records by name/company.
   - Fireflies cross-reference: Use `fireflies_get_transcripts` with `keyword` filter set to the person's name. If no results, try company name. If Fireflies MCP is unavailable or returns no useful results, ask the user: "Do you have any meeting recordings with [name]? Search Fireflies for '[name]' and paste any relevant excerpts." Do NOT block the pipeline on Fireflies results.
2. For each match found:
   - If HubSpot exact match: label `MERGED + EXISTING`. Do NOT create a new record in W3. Merge new data into existing record using per-field priority.
   - If HubSpot fuzzy match: label `REVIEW`. Present candidate match for human confirmation.
   - If Fireflies match: add to `parse_notes`: "X prior Fireflies transcripts found."
   - If ops-contextops match: enrich with relationship history.
3. For returning contacts, note the repeat encounter for scoring (+0.5 override in Step 11).
4. For multi-threaded companies, also pull existing HubSpot contacts at that company. Update Company Group to `"CompanyName (N) *"` if prior relationships exist.

**Output:** Fully cross-referenced contact set with merge labels (`NEW` | `MERGED` | `MERGED + EXISTING` | `REVIEW`), existing HubSpot IDs where applicable, and enrichment notes.
**If blocked:** If HubSpot MCP is unavailable, proceed with all contacts labeled `NEW` and add a prominent warning that CRM cross-reference was skipped. Re-run Step 6 when access is restored.

---

### Step 7: Team QA Review Dashboard

**Who:** contact-intake (presents) + Carlos (reviews)
**Tool:** Direct presentation in chat
**Input:** Cross-referenced contact set from Step 6
**Action:**
1. Assign traffic-light flags to each contact:
   - :green_circle: High confidence, all required fields parsed, no merge conflicts. Auto-proceed unless CEO overrides.
   - :yellow_circle: Partial data, fuzzy match found, or medium-confidence fields. Highlight gaps, ask for confirmation.
   - :red_circle: Low confidence, potential unresolved duplicate, missing required fields, or conflicting merge data. Require manual resolution.
2. Present the dashboard sorted by flag severity (red first, then yellow, then green):
   - Show contact name, company, merge status, flag color, and specific issues.
   - For `REVIEW` items, show side-by-side comparison of candidate matches.
   - For :red_circle: items, present specific questions for resolution.
3. Collect CEO decisions on all :red_circle: and :yellow_circle: items.
4. Apply corrections and confirmations.
5. Re-flag until zero :red_circle: items remain.

**Output:** QA-approved contact set with zero :red_circle: flags. All `REVIEW` items resolved to either `MERGED` or `NEW`.
**If blocked:** If CEO is unavailable for review, park :red_circle: items and proceed with :green_circle: and confirmed :yellow_circle: items only. Set a reminder to revisit within 24 hours.

---

### Step 8: Dual-Path Fork

**Who:** contact-intake
**Tool:** Decision logic
**Input:** QA-approved contact set from Step 7 + source metadata from Step 1
**Action:**
1. Evaluate the routing rule:
   ```
   IF count <= 5 AND source_type != conference:
     -> DIRECT PATH: proceed to Step 9 for immediate HubSpot upload.
     -> Append records to running CSV (contacts_log_YYYY.csv).
   ELSE:
     -> CSV PATH: generate review CSV per references/contact-record-schema.md CSV schema.
     -> Upload CSV to Google Drive as shared Sheet for team editing.
     -> Wait for team edits (or proceed immediately if CEO approves as-is).
     -> Read back edited CSV before proceeding to Step 9.
   ```
2. For CSV path: generate the CSV with all columns in schema order, company-grouped and sorted so same-company contacts are adjacent.
3. Include merge status columns: `Merge Status`, `Merge Sources`, `Existing HubSpot ID`, `Merge Confidence`.

**Output:** Either (a) approval to proceed directly, or (b) review CSV saved to Google Drive with share link.
**If blocked:** If Google Drive is unavailable for CSV upload, present the CSV content directly in chat and collect approval inline.

---

### Step 9: HubSpot Contact and Company Creation

**Who:** sales-intake (delegated)
**Tool:** HubSpot MCP (via sales-intake)
**Input:** Approved contact set from Step 8
**Action:**
1. Present a batch summary for CEO confirmation before any writes:
   - Total contacts to create/update.
   - Breakdown: N new contacts, M updates to existing, K new companies.
   - Any GDPR flags (new contacts default to `event-consent-only` or `business-relationship`).
2. Upon confirmation, delegate to `sales-intake` for execution:
   - For `NEW` contacts: create HubSpot contact + company records. Set associations.
   - For `MERGED + EXISTING` contacts: update existing HubSpot records with merged data. Append activity note: "Re-encountered at [event] on [date]."
   - For new companies with multi-threaded flag: create company record with account strategy note.
   - Set `contact_owner` per assignment rules.
   - Set `gdpr_status` on all records.
3. Capture all returned HubSpot IDs (`hubspot_contact_id`, `hubspot_company_id`).
4. Verify batch: confirm count of records created/updated matches expected count.

**Output:** Batch confirmation with HubSpot IDs for all contacts and companies. Updated contact records with CRM IDs populated.
**If blocked:** If HubSpot write fails for specific records, log failures, proceed with successful records, and retry failed records. If bulk failure, escalate to CEO with error details.

---

### Step 10: Score Contacts

**Who:** contact-intake
**Tool:** Scoring algorithm per `references/scoring-framework.md`
**Input:** HubSpot-synced contact set from Step 9
**Action:**
1. For each contact, score the 5 base dimensions (1-5 each):
   - Conversation Quality (30%): rate per rubric descriptors.
   - ICP Fit (25%): match against ICP tracks (C-NEO, C-ENT, C-INS, S-GRW, S-DHN, S-IND).
   - Urgency Signals (20%): detect timeline indicators, RFPs, budget references.
   - Strategic Value (15%): assess title seniority, network access, account potential.
   - Commitment Density (10%): count and qualify mutual promises.
2. Calculate base score:
   ```
   base_score = (conversation_quality * 0.30)
              + (icp_fit * 0.25)
              + (urgency_signals * 0.20)
              + (strategic_value * 0.15)
              + (commitment_density * 0.10)
   ```
3. Apply base score overrides (cumulative):
   - Introduction chain from Tier A contact: +0.5.
   - Promise floor: if `promises_we_made` has a specific named promise, score cannot drop below 2.5.
   - Repeat encounter (from Step 6 cross-reference): +0.5.
   - Multi-threaded company (from Step 5): +0.5.
4. Apply context modifiers (source-specific):
   - Conference speaker/panelist: +0.3.
   - Conference booth visitor: +0.3.
   - Conference sponsor: +0.2.
   - Event host-introduced: +0.3.
   - Inbound: +0.5.
   - Referral from partner: +0.4.
   - Referral from investor: +0.3.
   - WhatsApp first-contact: +0.1.
   - LinkedIn inbound: +0.2.
   - Random/serendipitous: +0.0.
5. Cap final score at 5.0.
6. Set `urgency` (1-5) and `relevance` (1-5) as standalone fields.

**Output:** Scored contact set with `score`, `urgency`, and `relevance` populated for every record.
**If blocked:** If insufficient conversation data to score a dimension, default that dimension to 1 and flag with `parse_notes`: "Scored with incomplete data -- [dimension] defaulted to 1."

---

### Step 11: Assign Tiers and Update HubSpot Tags

**Who:** contact-intake + sales-intake (for HubSpot writes)
**Tool:** Tier assignment logic + HubSpot MCP (via sales-intake)
**Input:** Scored contact set from Step 10
**Action:**
1. Apply tier thresholds:
   - **A** (4.0-5.0): Full pipeline. 24-hour follow-up deadline.
   - **B** (2.5-3.9): Structured follow-up. 48-72 hour deadline.
   - **C** (1.0-2.4): Lightweight. 1-week deadline.
   - **V**: `contact_type = vendor` regardless of score.
   - **X**: `contact_type = competitor` regardless of score.
   - **N**: `contact_type` in (press, personal, advisor) unless conversation_quality >= 4 AND strategic_value >= 4.
   - **-**: No action warranted.
2. Apply tier override rules:
   - Competitor always -> X.
   - Vendor always -> V.
   - Press -> N unless high-quality interaction.
   - Personal always -> N.
   - Promise floor: any contact with specific `promises_we_made` cannot be below Tier B.
3. Delegate to `sales-intake` to update HubSpot:
   - Set tier tag on each contact record.
   - Set score, urgency, relevance fields.
   - For Tier A contacts, add to "Hot Leads" pipeline stage.
4. Present tier summary to CEO:
   - Count per tier.
   - Tier A contacts listed by name with 24-hour deadline highlighted.

**Output:** Tiered contact set with HubSpot tags updated. Tier summary presented.
**If blocked:** If HubSpot tag update fails, log and retry. Tier assignments are not blocked by CRM sync -- proceed with routing using local tier data.

---

### Step 12: Route Per Tier

**Who:** contact-intake (orchestrates) + downstream skills (execute)
**Tool:** Delegation to downstream skills
**Input:** Tiered contact set from Step 11
**Action:**
1. Route each contact per tier delegation chain:

   **Tier A (4.0-5.0):**
   - Delegate to `counter-party-intel` for deep profile enrichment.
   - Delegate to `sales-intake` for lead qualification (Mode A).
   - Delegate to `ops-outreachops` for personalized follow-up email (24-hour deadline).
   - Delegate to `ops-meetings` for meeting scheduling.
   - Flag for Carlos review.

   **Tier B (2.5-3.9):**
   - Delegate to `counter-party-intel` for standard enrichment.
   - Delegate to `ops-outreachops` for warm follow-up email (48-72 hour deadline).
   - Add to nurture sequence if no response after initial follow-up.

   **Tier C (1.0-2.4):**
   - Delegate to `ops-outreachops` for brief acknowledgment email (1-week deadline).
   - Add to newsletter/nurture list.

   **Tier V (vendor):**
   - Delegate to `vendor-lifecycle` for vendor evaluation track.
   - 1-week follow-up deadline.

   **Tier X (competitor):**
   - Delegate to `competitive-intel` for intelligence logging.
   - No follow-up initiated.

   **Tier N (non-sales):**
   - Delegate to `ops-contextops` for relationship record only.
   - Follow-up varies by sub-type (press, advisor, personal).

   **Tier - (no action):**
   - CRM record exists. No further action. Log as "no action warranted."

2. For each routed contact, set `follow_up_type`, `follow_up_status: pending`, and `next_action_date` per tier deadlines.

**Output:** All contacts routed with assigned next actions. Follow-up types and deadlines set.
**If blocked:** If a downstream skill is unavailable, queue the delegation and set a reminder. Do not skip routing -- the contact must have an assigned action even if execution is deferred.

---

### Step 13: Promise Extraction and Task Routing

**Who:** contact-intake + delegation-engine (for ClickUp)
**Tool:** ClickUp MCP (via delegation-engine)
**Input:** Full contact set with promise fields populated
**Action:**
1. Extract all `promises_we_made` across the entire batch. For each:
   - Verify it has: `what` (specific action), `deadline` (date), `owner` (person responsible).
   - If `owner` is missing, default to Carlos and flag for reassignment.
   - If `deadline` is missing, assign default: Tier A = 24h, Tier B = 72h, Tier C = 1 week.
2. Delegate to `delegation-engine` to create ClickUp tasks for each promise:
   - Task name: "[Promise] [What] for [Contact Name] @ [Company]".
   - Due date: promise deadline.
   - Assignee: promise owner.
   - Description: full context including source, conversation summary, and contact HubSpot link.
3. Extract all `promises_they_made` across the batch. For each:
   - Create a HubSpot task/note on the contact record.
   - Set follow-up trigger at the expected deadline.
4. Log all promises in the batch promise tracker.

**Output:** ClickUp tasks created for all promises-we-made. HubSpot tasks created for all promises-they-made. Promise tracker updated.
**If blocked:** If ClickUp is unavailable, create promises as a structured list in chat and set a calendar reminder to create tasks when access is restored. Promises must never be lost.

---

### Step 14: Follow-Up Initiation

**Who:** ops-outreachops (delegated)
**Tool:** Gmail MCP (via ops-outreachops)
**Input:** Routed contacts from Step 12 with tier and follow-up details
**Action:**
1. Delegate to `ops-outreachops` to initiate follow-ups per tier cadence (reference `references/follow-up-cadences.md`):
   - Tier A: Personalized email within 24 hours. Reference specific conversation topics, promises made, and introduction chain.
   - Tier B: Warm follow-up within 48-72 hours. Reference conversation context. Include relevant collateral.
   - Tier C: Brief acknowledgment within 1 week. "Great meeting you at [event]" tone.
   - Tier V: Vendor acknowledgment with procurement next steps.
   - Tier N: Relationship-appropriate follow-up (if any).
2. For each follow-up, ensure:
   - Introduction chain is referenced in the email if applicable.
   - Any promises-we-made are acknowledged or fulfilled in the email.
   - GDPR status is respected (no marketing content for `event-consent-only`).
3. Update `follow_up_status` to `sent` as each email is dispatched (or `pending` if queued).

**Output:** Follow-up emails initiated or queued for all contacts with a follow-up action. Status updated per contact.
**If blocked:** If Gmail MCP is unavailable, draft all emails in a structured list for manual sending. Set calendar reminders for each deadline.

---

### Step 15: Relationship Intelligence Routing

**Who:** ops-contextops (delegated)
**Tool:** Delegation to ops-contextops
**Input:** Tier A and Tier B contacts from Step 12
**Action:**
1. For each Tier A and Tier B contact, delegate to `ops-contextops`:
   - Full conversation summary with source attribution.
   - Introduction chain details.
   - Company context and multi-threaded status.
   - Any prior relationship history found in Step 6.
   - Relevant Fireflies transcript references.
2. For multi-threaded companies, provide the full company summary from Step 5.
3. Request `ops-contextops` to create or update relationship records for future reference.

**Output:** Relationship intelligence archived for all Tier A and B contacts. Company relationship maps updated for multi-threaded accounts.
**If blocked:** If ops-contextops is unavailable, store the intelligence package locally and queue for later delivery. Context must not be lost.

---

### Step 16: Completion Gate Check

**Who:** contact-intake
**Tool:** Internal verification
**Input:** All outputs from Steps 1-15
**Action:**
1. Run the completion checklist:
   - [ ] Zero unprocessed contacts (every input yielded a record or a documented failure).
   - [ ] Zero :red_circle: items remaining after QA (Step 7 resolved all).
   - [ ] Every contact has a HubSpot record (verify `hubspot_contact_id` is populated for all).
   - [ ] Every contact has a tier assignment (`tier` field is not null for any record).
   - [ ] Every contact has a routed action (even if "no action" for Tier - or Tier X).
   - [ ] All `promises_we_made` have assigned owners + deadlines + ClickUp tasks.
   - [ ] All `promises_they_made` have HubSpot tasks with follow-up triggers.
   - [ ] Review CSV saved to Google Drive (if CSV path was taken in Step 8).
   - [ ] ROI baseline snapshot created (contact count, tier distribution, promise count, source breakdown).
2. If any item fails:
   - Identify the gap.
   - Execute the minimum steps needed to close it.
   - Re-run the checklist.
3. Present the final batch summary to CEO:
   - Total contacts processed.
   - Tier distribution (A: N, B: N, C: N, V: N, X: N, N: N, -: N).
   - Promises tracked (we-made: N, they-made: N).
   - Follow-ups initiated: N.
   - Notable flags or items requiring CEO attention.
4. Mark the batch as CLOSED.

**Output:** Batch completion confirmation. Summary report. Batch status set to CLOSED.
**If blocked:** If a gap cannot be closed immediately, document it as an open item with an owner and deadline. The batch remains OPEN until all items are resolved.

---

### Late Addition Protocol

**Trigger:** "add more contacts to [batch]", "found more cards", "late addition", "forgot about this one"
**When:** After a batch is CLOSED (Step 16 complete) but new contacts surface (common 2-7 days after an event)

**Who:** contact-intake
**Tool:** Same pipeline tools
**Input:** New raw contact materials + reference to the closed batch

**Action:**
1. Identify the target batch by event name or date. Confirm with user: "Adding to the [Event Name] batch from [date]?"
2. Run W1 (Steps 2-3) on new contacts only — extract, parse, confidence-flag.
3. Run W2 (Steps 3-6) with special attention to dedup against the EXISTING batch contacts (not just HubSpot). Load the batch CSV or HubSpot records from the original run.
4. Run W3 (Step 9) for HubSpot creation — append to same event tags.
5. Run W4 (Steps 10-11) — score and tier. Apply same context modifiers as the original batch source.
6. Run W5 (Steps 12-14) — route, create promise tasks, initiate follow-ups. Note: follow-up deadlines reset from TODAY, not from original event date.
7. Update the batch CSV if one exists: append new rows, update batch summary row counts.
8. Update the batch ROI baseline to reflect the expanded contact set.
9. Re-close the batch with updated completion gate.

**Output:** Expanded batch with new contacts fully processed. Updated CSV and ROI baseline.

**Key rules:**
- Late additions get the SAME quality of processing as original batch contacts — no shortcuts.
- Follow-up deadlines are based on today's date, but email content should still reference the original event: "We met at [event] last week..."
- If the batch ROI report (W6) has already been generated, flag that it needs refresh.
- Maximum 2 late-addition rounds per batch. After that, new contacts go into a fresh batch to prevent scope creep.

---

## Quality Gate

- [ ] Zero :red_circle: items remaining after QA review
- [ ] Every contact has a HubSpot record (`hubspot_contact_id` populated)
- [ ] Every contact has a tier assignment (A/B/C/V/X/N/-)
- [ ] Every contact has a routed action (follow-up, intel log, nurture, or documented "no action")
- [ ] All `promises_we_made` have owners + deadlines + ClickUp tasks
- [ ] All `promises_they_made` have HubSpot tasks with follow-up triggers
- [ ] Review CSV saved to Google Drive (if CSV path was taken)
- [ ] ROI baseline snapshot captured (counts, tier distribution, source breakdown)
- [ ] GDPR status set on all contact records
- [ ] Tier A contacts have 24-hour follow-up deadlines confirmed

---

## Handoffs

| Output | Destination | Skill/Person |
|--------|-------------|--------------|
| HubSpot contact/company records | HubSpot CRM | `sales-intake` |
| Tier A leads (qualified) | Sales pipeline | `sales-intake` (Mode A) |
| Tier B leads (warm) | Nurture pipeline | `ops-outreachops` |
| Tier C contacts | Newsletter/nurture | `ops-outreachops` (lightweight) |
| Vendor contacts | Procurement track | `vendor-lifecycle` |
| Competitor contacts | Intelligence log | `competitive-intel` |
| Promises-we-made tasks | ClickUp | `delegation-engine` |
| Follow-up emails | Gmail | `ops-outreachops` |
| Relationship intelligence (A/B) | Context archive | `ops-contextops` |
| Deep enrichment requests (A/B) | Intel profiles | `counter-party-intel` |
| Meeting scheduling (A) | Calendar | `ops-meetings` |
| Review CSV | Google Drive | Team / Carlos |
| Batch ROI baseline | ROI tracking | `contact-intake` (W6 input) |

---

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| **HubSpot MCP unavailable or write failure** | API errors returned during Step 9 or Step 11. Contact records missing `hubspot_contact_id` at completion gate. | Queue all CRM writes locally. Proceed with scoring and routing using local data. Set a calendar reminder to retry HubSpot sync within 4 hours. Do not block the pipeline -- follow-ups can begin from local data. Re-run Steps 9 and 11 when access is restored. |
| **OCR extraction failure (unreadable input)** | Claude vision returns low-confidence or empty results for a photo/card/note. Multiple fields marked `low` confidence. `parse_notes` describes illegible content. | Log the failed input with full context. Set `row_review: needs_fix` and present in QA dashboard (Step 7) with the original image for manual data entry. If the user can re-photograph or re-provide the input, re-run extraction. Never silently drop a contact. |
| **Downstream skill unavailable (ops-outreachops, delegation-engine, etc.)** | Delegation call fails or times out. Follow-up emails not sent. ClickUp tasks not created. | Queue all delegations as structured action items with full context. Create calendar reminders at each follow-up deadline. Present the queue to CEO with "manual execution needed" flag. Re-attempt delegation when the skill is restored. For time-sensitive Tier A follow-ups, draft the email directly in chat for CEO to send manually. |
| **Duplicate conflict unresolvable** | Two records have 70-85% match confidence with conflicting data that cannot be resolved algorithmically. Presented in QA but CEO is unsure. | Keep both records as separate contacts in HubSpot. Add a note on each: "Potential duplicate of [other record]. Confirm identity at next interaction." Score and route both independently. Set a reminder to revisit after the first follow-up response clarifies identity. |
| **Tier A 24-hour deadline at risk** | More than 12 hours elapsed since batch processing started and Tier A follow-ups have not been initiated. | Escalate immediately to CEO. If ops-outreachops is blocked, draft the Tier A follow-up emails directly in chat for immediate manual sending. The 24-hour clock is sacred and overrides all other pipeline steps -- Tier A follow-ups can be initiated before the full batch completes if needed. |
