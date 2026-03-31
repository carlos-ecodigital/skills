# Contact Record Schema

> The intermediate format that standardizes all inputs from W1 (extraction) through W3 (CRM sync).
> Every contact passes through this schema regardless of source format.

## Per-Contact Record Fields

### Identity

| Field | Required | Type | Notes |
|-------|----------|------|-------|
| `name` | Yes | string | Full name as captured. Normalize to "First Last" in W2. |
| `company` | Yes | string | Legal or common company name. |
| `title` | No | string | Job title / role. |
| `email` | No | string | Primary work email. |
| `secondary_email` | No | string | Personal or alternate email. |
| `phone` | No | string | Primary phone. E.164 format after normalization. |
| `secondary_phone` | No | string | Alternate phone. |
| `linkedin` | No | string | Full LinkedIn profile URL. |

### Context

| Field | Required | Type | Values / Notes |
|-------|----------|------|----------------|
| `source_type` | Yes | enum | `conference` \| `event` \| `meeting` \| `referral` \| `inbound` \| `random` \| `whatsapp` |
| `source_detail` | Yes | string | Event name, meeting context, referrer name. |
| `source_date` | Yes | date | YYYY-MM-DD. Date of encounter. |
| `location_met` | No | string | City, venue, or "virtual". |
| `introduction_chain` | No | list | Who introduced whom, or `["direct"]`. |

### Conversation

| Field | Required | Type | Values / Notes |
|-------|----------|------|----------------|
| `conversation_summary` | No | string | Free-text summary of what was discussed. |
| `conversation_quality` | No | enum | `deep` \| `substantive` \| `brief` \| `card-swap` \| `none` |
| `interest_signal` | No | enum | `high` \| `medium` \| `low` |

### Classification

| Field | Required | Type | Values / Notes |
|-------|----------|------|----------------|
| `contact_type` | Yes | enum | `investor` \| `customer` \| `partner` \| `vendor` \| `advisor` \| `press` \| `competitor` \| `personal` |
| `icp_track` | No | enum | `C-NEO` \| `C-ENT` \| `C-INS` \| `S-GRW` \| `S-DHN` \| `S-IND` \| `N/A` |
| `classification_notes` | No | string | Free-text rationale for classification choices. |

### ICP Track Definitions

| Track | Segment | Description |
|-------|---------|-------------|
| `C-NEO` | Customer - Neocloud | Hyperscaler alternatives, GPU cloud, AI infra |
| `C-ENT` | Customer - Enterprise | Traditional enterprise data center / corporate IT |
| `C-INS` | Customer - Infrastructure | Colo, wholesale DC, edge, tower |
| `S-GRW` | Strategic - Growth | VCs, growth equity, strategic investors |
| `S-DHN` | Strategic - DHN | District heating network operators, municipalities |
| `S-IND` | Strategic - Industrial | Industrial heat offtakers, process heat buyers |
| `N/A` | Not applicable | Non-sales contacts (press, personal, etc.) |

### Promises

| Field | Required | Type | Structure |
|-------|----------|------|-----------|
| `promises_we_made` | No | list | `[{what: string, deadline: date, owner: string}]` |
| `promises_they_made` | No | list | `[{what: string, expected_by: date, follow_up_action: string}]` |

### Scoring (populated in W4)

| Field | Type | Values |
|-------|------|--------|
| `tier` | enum | `A` \| `B` \| `C` \| `V` \| `X` \| `-` \| `N` |
| `score` | float | 0.0 - 5.0 |
| `urgency` | int | 1 - 5 |
| `relevance` | int | 1 - 5 |

### Follow-up (populated in W5)

| Field | Type | Values |
|-------|------|--------|
| `follow_up_type` | enum | `email` \| `call` \| `meeting` \| `intro` \| `send_collateral` \| `none` |
| `follow_up_status` | enum | `pending` \| `sent` \| `response_received` \| `meeting_booked` \| `completed` |
| `next_action_date` | date | YYYY-MM-DD |

### HubSpot (populated in W3)

| Field | Type | Notes |
|-------|------|-------|
| `hubspot_contact_id` | string | HubSpot record ID. |
| `hubspot_company_id` | string | HubSpot company record ID. |
| `hubspot_deal_id` | string | If linked to existing deal. |
| `contact_owner` | string | HubSpot owner ID for assignment. |
| `gdpr_status` | enum | `event-consent-only` \| `business-relationship` |

### QA

| Field | Type | Notes |
|-------|------|-------|
| `confidence` | object | Per-field map: `{field_name: "high" \| "medium" \| "low"}` |
| `row_review` | enum | `OK` \| `needs_fix` |
| `parse_notes` | string | OCR issues, illegible text, best guesses. |
| `sources` | list | References to raw inputs: `["card_photo_003.jpg", "notes_page_2"]` |

---

## Review CSV Schema

The review CSV is the human-facing output for W2 review. Column headers map to the record fields above, with additions for grouping and review workflow.

### Column Headers (in order)

```
Row,Row Review,Tier,Score,Name,Title,Company,Company Group,
Contact Type,ICP Track,Email,Phone,LinkedIn,
Source Type,Source Detail,Source Date,Location Met,Introduction Chain,
Conversation Summary,Conversation Quality,Interest Signal,
Promises We Made,Promises They Made,
Follow-up Type,Next Action Date,
Urgency,Relevance,Classification Notes,
Confidence Flags,Parse Notes,Sources,
HubSpot Contact ID,HubSpot Company ID,GDPR Status
```

### Company Group Column

The `Company Group` column flags multi-threaded opportunities:

| Value | Meaning |
|-------|---------|
| (blank) | Only one contact from this company in the batch. |
| `Vattenfall (3)` | 3 contacts from Vattenfall in this batch. |
| `Google (2) *` | 2 contacts + existing HubSpot contacts from Google. `*` = prior relationship. |

**Grouping rules:**
- Normalize company names before grouping (strip "Inc.", "GmbH", "AG", "Ltd.", "B.V.", etc.)
- Sort CSV so same-company contacts are adjacent.
- First row of each group gets the Company Group label; subsequent rows get `"`.
- Companies with 2+ contacts are auto-flagged for multi-threaded review in W4.
