---
example: single-referral
scenario: 1 contact via WhatsApp referral from existing grower partner
source-type: referral
contact-count: 1
tests: [referral-modifier, single-contact-pipeline, no-email-handling, intro-chain-capture, trust-transfer-scoring]
success-criteria:
  - Julia has HubSpot record within 1 hour of intake
  - Referral modifier (+0.4) applied to score
  - Intro chain modifier (+0.5) applied (Henk is Tier A)
  - Follow-up via WhatsApp (no email available)
  - Henk's referrer role captured in intro chain
  - Promise to Henk ("I'll reach out to Julia") creates ClickUp task
  - HubSpot record created with phone-only (no email blocker)
failure-indicators:
  - Follow-up attempted via email (no email exists)
  - Referral modifier missed
  - Intro chain modifier missed (Henk is Tier A, should trigger +0.5)
  - Contact blocked or dropped due to missing email
  - Henk not notified that Carlos followed up
grader: human (Carlos or team lead)
last-reviewed: 2026-03-30
---

# Worked Example: Single Referral -- WhatsApp Intro from Grower Partner

> Full pipeline walkthrough: 1 referral contact from WhatsApp -> scored, routed, closed.
> Referrer: Henk Bakker, Director, Bakker Tuinbouw B.V. (signed grower partner, Tier A in HubSpot).
> Contact: Julia van den Berg, Head of Sustainability, VersFood Group B.V.
> Input: WhatsApp screenshot, phone number only. No email, no card, no LinkedIn.

---

## Source Metadata

| Field | Value |
|-------|-------|
| batch_id | `REF-2026-0328-BAKKER` |
| source_type | referral / WhatsApp |
| referrer_name | Henk Bakker |
| referrer_company | Bakker Tuinbouw B.V. |
| referrer_hubspot_id | `HS-CON-12450` |
| referrer_tier | A |
| referrer_relationship | Signed grower partner (HoT executed Dec 2025) |
| contact_count | 1 |
| path | direct-upload (count <= 5 AND source != conference) |
| overlay | referral: intro chain capture, referrer trust transfer bonus |

---

## W1: INGEST

**Trigger:** Carlos forwards a WhatsApp screenshot at 09:22 on March 28: "Henk just sent me this. Worth logging."

### Raw Input

| # | Format | Description |
|---|--------|-------------|
| 1 | WhatsApp screenshot | Chat thread between Henk Bakker and Carlos. Timestamp: March 28, 08:47. |

### WhatsApp Screenshot Extraction (Claude Vision OCR)

**Chat thread (Henk Bakker -> Carlos):**

> **Henk Bakker** (08:47):
> "Carlos, je moet met Julia van den Berg praten bij VersFood Group. Ze is Head of Sustainability daar. Ze zoeken een oplossing voor restwarmte voor hun productielocatie in het Westland. Ik heb verteld over jullie concept en ze was erg geinteresseerd. Hier is haar nummer: +31 6 4782 3190"
>
> **Carlos** (09:15):
> "Top, bedankt Henk! Ik neem contact met haar op. Ken je haar goed?"
>
> **Henk Bakker** (09:18):
> "Ja, we leveren al 8 jaar aan VersFood. Julia ken ik van de duurzaamheidsbijeenkomsten van Glastuinbouw Nederland. Goed mens, heel gedreven. Zeg maar dat ik je heb doorverwezen."

**Translation summary (for pipeline records -- all records stored in English):**
- Henk recommends Carlos talk to Julia van den Berg at VersFood Group
- Julia is Head of Sustainability
- VersFood is looking for a waste heat solution for their production facility in Westland
- Henk told Julia about DE's concept, she was interested
- Julia's phone: +31 6 4782 3190
- Henk has supplied VersFood for 8 years (existing commercial relationship)
- Henk knows Julia from Glastuinbouw Nederland sustainability meetings
- Henk says to mention his name in the introduction

### Extraction Results

#### Contact 1: Julia van den Berg

**Source:** WhatsApp screenshot (referral message from Henk Bakker)

| Field | Extracted Value | Confidence |
|-------|----------------|------------|
| first_name | Julia | :green_circle: |
| last_name | van den Berg | :green_circle: |
| company | VersFood Group B.V. | :green_circle: |
| title | Head of Sustainability | :green_circle: |
| email | [not available] | :red_circle: Not provided. WhatsApp-only intro. |
| phone | +31 6 4782 3190 | :green_circle: |
| linkedin | [not available] | :red_circle: Not provided. |

**Extracted context:**
- `conversation_topic`: Waste heat solution for VersFood production facility in Westland
- `conversation_duration`: N/A (referral, no direct conversation yet)
- `promises_we_made`: Carlos told Henk "I'll reach out to Julia" (implied commitment to referrer)
- `promises_they_made`: None yet (no direct contact)
- `urgency_signal`: Active need -- "looking for a waste heat solution" (Henk's characterization)
- `contact_type`: prospect
- `track`: S-IND (industrial heat user -- food processing)
- `acquisition_context`: WhatsApp referral from signed grower partner
- `introduction_chain`: Henk Bakker (Bakker Tuinbouw, Tier A grower) -> Julia van den Berg
- `referrer_context`: Henk has 8-year commercial relationship with VersFood. Knows Julia personally from industry sustainability events. Strong trust transfer.
- `gdpr_note`: No direct consent from Julia yet. First contact must include how we got her number.

Name and company :green_circle:. Phone :green_circle:. Title :green_circle:. Email and LinkedIn :red_circle: -- acceptable for referral intake, not blocking.

---

### W1 Summary: 1 Input -> 1 Raw Contact Record

| # | Name | Company | Source(s) | Confidence |
|---|------|---------|-----------|------------|
| 1 | Julia van den Berg | VersFood Group B.V. | WhatsApp referral | :green_circle: / :red_circle: (identity clear, email missing) |

---

## W2: CONSOLIDATE & QA

### Dedup Check Against HubSpot

| # | Name | Company | HubSpot Match? | Action |
|---|------|---------|----------------|--------|
| 1 | Julia van den Berg | VersFood Group B.V. | No match on name. No match on phone. VersFood Group exists as company (`HS-COMP-7834`) but no contacts on file. | Create new contact, link to existing company. |

**Company record note:** VersFood Group B.V. (`HS-COMP-7834`) was created during Bakker Tuinbouw onboarding as a "grower ecosystem" company. Has a note: "Major buyer of Bakker's tomatoes. Potential heat offtake partner if Bakker site proceeds." This pre-existing context strengthens the referral signal.

### Team QA Dashboard

**Batch: Henk Bakker Referral March 2026 | Raw: 1 | Deduplicated: 1 | Parked: 0**

| # | Name | Company | :green_circle: | :yellow_circle: | :red_circle: | Action Needed |
|---|------|---------|------|------|------|---------------|
| 1 | Julia van den Berg | VersFood Group B.V. | 4/7 | 0 | 3 | Accept phone-only. Email/LinkedIn to be captured on first contact. |

**Dashboard decision:** Identity is clear. Missing email is non-blocking -- WhatsApp follow-up path handles this. Proceed.

### Path Decision

```
count = 1
source = referral (NOT conference)
-> 1 <= 5 AND source != conference
-> DIRECT UPLOAD PATH
-> No review CSV generated
-> Append to running contacts_log_2026.csv after upload
```

---

## W3: HUBSPOT PUSH

Delegated to `sales-intake` for CRM writes.

| # | Name | HubSpot Action | Record ID | Tags Applied |
|---|------|---------------|-----------|-------------|
| 1 | Julia van den Berg | CREATE new | `HS-CON-52340` (new) | `referral-henk-bakker`, `S-IND`, `grower-ecosystem`, `phone-only`, `needs-email` |

**HubSpot record details:**
- Contact: Julia van den Berg, Head of Sustainability, VersFood Group B.V.
- Phone: +31 6 4782 3190
- Email: [blank -- flagged `needs-email` for enrichment on first contact]
- Company association: Linked to `HS-COMP-7834` (VersFood Group B.V.)
- Source: Referral (Henk Bakker, Bakker Tuinbouw)
- Introduction chain: `Henk Bakker (HS-CON-12450) -> Julia van den Berg`
- Notes: "Referred by Henk Bakker (signed grower partner). VersFood looking for waste heat for Westland production facility. Julia interested per Henk. Phone-only contact -- no email yet."

---

## W4: SCORING

### Contact 1: Julia van den Berg (VersFood Group B.V.)

**Base Dimensions:**

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| Conversation Quality | 30% | 1 | No direct conversation yet. Referral only. Scored on referrer's characterization. Meets "Card-swap / None" -- we haven't spoken to Julia at all. |
| ICP Fit | 25% | 3 | S-IND track (industrial heat user). Food processing in Westland aligns with DE's heat offtake model. Not a primary track buyer but strong adjacent fit. |
| Urgency Signals | 20% | 3 | "Looking for a waste heat solution" per Henk. Active need but secondhand information. Medium-term until confirmed directly. |
| Strategic Value | 15% | 3 | Head of Sustainability at a major food processor. Could unlock VersFood as a reference industrial heat client. Westland location = DE's core geography. |
| Commitment Density | 10% | 2 | Soft intent via proxy. Julia expressed interest to Henk. No direct commitments yet. "Soft intent" level. |

**Base score calculation:**

```
base = (1 * 0.30) + (3 * 0.25) + (3 * 0.20) + (3 * 0.15) + (2 * 0.10)
     = 0.30 + 0.75 + 0.60 + 0.45 + 0.20
     = 2.30
```

**Overrides:**
- Introduction chain: APPLIES -- Henk Bakker is a current Tier A contact. +0.5.
- Promise floor: APPLIES -- Carlos told Henk "I'll reach out to Julia." We made a promise to a Tier A partner to follow up. Floor = min 2.5. After intro chain override, score will be 2.80, already above floor.
- Repeat encounter: N/A -- no prior record for Julia.
- Multi-threaded company: N/A -- only 1 contact from VersFood.

```
after_overrides = 2.30 + 0.50 = 2.80
```

**Context modifier:**
- Referral from partner: +0.4

```
final_score = 2.80 + 0.40 = 3.20
```

**Cap check:** 3.20 <= 5.0. No cap applied.

**Tier assignment:** 3.20 -> **Tier B** (2.5-3.9)

**Score narrative:** Julia scores Tier B despite no direct conversation, driven by the Tier A intro chain override (+0.5) and referral modifier (+0.4). The base score of 2.30 alone would have been Tier C, but the trust transfer from Henk -- a signed grower partner with 8 years of commercial relationship with VersFood -- appropriately lifts the score. This is exactly what the trust transfer modifiers are designed for.

---

### Scoring Summary Table

| # | Name | Base | Overrides | Modifier | Final | Tier |
|---|------|------|-----------|----------|-------|------|
| 1 | Julia van den Berg | 2.30 | +0.50 (Tier A intro chain) | +0.40 (referral) | **3.20** | **B** |

---

## W5: ROUTE & FOLLOW-UP

### Tier B: Julia van den Berg -- 48-72hr follow-up deadline

**Delegation chain:** `counter-party-intel` -> `ops-outreachops`

**Step 1: Enrichment** (delegated to `counter-party-intel`)
- Quick profile on VersFood Group B.V.: revenue, headcount, Westland facility details, sustainability strategy
- Quick profile on Julia van den Berg: LinkedIn lookup, prior roles, publications
- Enrichment priority: STANDARD (Tier B)
- **Side benefit:** Enrichment should capture Julia's email and LinkedIn for CRM update

**Step 2: Follow-up via WhatsApp** (delegated to `ops-outreachops`)

> CRITICAL: No email exists. Follow-up MUST be via WhatsApp. This is the only channel available.

**WhatsApp message guidance:**

Tone: Warm, referral-anchored. Mention Henk by name (he authorized this). Brief, respectful of the channel (WhatsApp is informal).

Draft structure:
- Opening: "Hoi Julia, Carlos Reuven hier van Digital Energy. Henk Bakker gaf me je nummer -- hij vertelde dat jullie bij VersFood kijken naar een restwarmte-oplossing voor de locatie in het Westland."
- Bridge: Reference Henk's context. Keep it conversational.
- Ask: Suggest a brief call or coffee to explore the fit. Low-pressure.
- Language note: Henk's referral was in Dutch. Follow-up should match -- start in Dutch. Switch to English only if Julia signals preference.

**WhatsApp message timing:**
- Send within 48 hours of Henk's referral (by March 30)
- Ideal: same business day if possible (March 28 afternoon)
- Rationale: Henk told Julia he was connecting them. Delay makes Henk look bad.

**Step 3: Promise tracking** (delegated to `delegation-engine`)

| Promise | Type | Owner | Deadline | Task |
|---------|------|-------|----------|------|
| Reach out to Julia (promise to Henk) | We made (to referrer) | Carlos | 2026-03-30 (48hr) | ClickUp: "[Promise] Reach out to Julia van den Berg per Henk Bakker referral" |
| Close the loop with Henk | We made (to referrer) | Carlos | 2026-04-01 (after Julia contact) | ClickUp: "[Promise] Update Henk Bakker on Julia outreach result" |

> NOTE: Closing the loop with Henk is critical. He vouched for us. If we don't follow up with Julia, or don't tell Henk we did, it damages the grower relationship. This is a Tier A partner -- the 24hr grower relationship clock applies to the referrer promise even though Julia herself is Tier B.

**Step 4: Email capture plan**

Once Julia responds to WhatsApp:
1. During the conversation, naturally ask for her email for follow-up materials
2. Update HubSpot record with email when captured
3. Remove `phone-only` and `needs-email` tags
4. Future follow-up can shift to email for formal materials, WhatsApp for scheduling

---

## Completion Gate

- [x] Zero unprocessed contacts (1/1 processed)
- [x] Contact has HubSpot record + tier + routed action
  - Julia: HS-CON-52340 (new), Tier B, WhatsApp follow-up
- [x] All promises-we-made have assigned owners + deadlines
  - Reach out to Julia: ClickUp task, 48hr deadline
  - Close loop with Henk: ClickUp task, after Julia contact
- [x] Appended to `contacts_log_2026.csv` (direct-upload path)
- [x] ROI baseline snapshot: 1 contact, 1 Tier B (referral-boosted)
- [x] Introduction chain captured: Henk Bakker -> Julia van den Berg

**Batch status: CLOSED**

---

## Key Test Validations

| Test | Expected | Actual | Pass? |
|------|----------|--------|-------|
| Referral modifier (+0.4) applied | +0.4 in context modifier step | +0.4 applied to final score | PASS |
| Intro chain modifier (+0.5) for Tier A referrer | Henk is Tier A, triggers +0.5 override | +0.5 applied after base score | PASS |
| Single-contact direct-upload path | 1 contact, non-conference -> direct | Direct upload, no CSV review | PASS |
| No-email handling | Follow-up via WhatsApp, not email | WhatsApp message drafted, no email sent | PASS |
| Intro chain captured | Henk -> Julia recorded in HubSpot | Introduction chain field populated | PASS |
| Phone-only HubSpot record | Contact created despite no email | HS-CON-52340 created with phone only | PASS |
| Referrer loop-close tracked | Promise to update Henk | ClickUp task created for Henk follow-up | PASS |
| Trust transfer scoring | Base 2.30 (Tier C) lifted to 3.20 (Tier B) | Modifiers correctly elevated tier | PASS |
| Dutch language follow-up | Referral in Dutch -> follow-up in Dutch | WhatsApp draft in Dutch | PASS |
