# Output Schema — xlsx Column Specification

## Overview

All lead generation output is delivered as `.xlsx` files with a standardized column layout. This ensures consistency across batches, enables HubSpot import, and supports downstream automation.

---

## Column Layout

### Company Block (Columns A-H)

| Col | Header | Type | Required | Description |
|-----|--------|------|----------|-------------|
| A | Company Name | Text | Yes | Legal or trading name (use trading name if well-known) |
| B | Country | Text | Yes | NL, BE, or LU |
| C | Vertical | Text | Yes | One of: Healthcare, Agriculture, Horticulture, Finance, Logistics, Defense/Government |
| D | HQ City | Text | Yes | City of headquarters |
| E | Website | URL | Yes | Primary company website (https://) |
| F | Revenue EUR est | Number | Best effort | Estimated annual revenue in EUR; note year and source in Notes |
| G | Employee Count | Number | Best effort | Approximate headcount; note source |
| H | Sub-segment | Text | Yes | Per-vertical sub-segment (see vertical-playbooks.md) |

### Contact 1 — Champion (Columns I-N)

| Col | Header | Type | Required | Description |
|-----|--------|------|----------|-------------|
| I | C1 Name | Text | Yes (Tier 1-3) | Full name (First Last, include tussenvoegsel for NL) |
| J | C1 Title | Text | Yes | Current job title |
| K | C1 LinkedIn | URL | Yes | Full LinkedIn profile URL |
| L | C1 Email | Email | Best effort | Business email address; mark confidence |
| M | C1 Phone | Phone | Optional | Direct business phone if found |
| N | C1 Rationale | Text | Yes (Tier 1-2) | Why this person; evidence-based (see contact-targeting.md) |

### Contact 2 — Economic Buyer (Columns O-R)

| Col | Header | Type | Required | Description |
|-----|--------|------|----------|-------------|
| O | C2 Name | Text | Yes (Tier 1-2) | Full name |
| P | C2 Title | Text | Yes (Tier 1-2) | Current job title |
| Q | C2 LinkedIn | URL | Yes (Tier 1-2) | Full LinkedIn profile URL |
| R | C2 Rationale | Text | Yes (Tier 1) | Why this person; evidence-based |

### Contact 3 — Blocker (Columns S-U)

| Col | Header | Type | Required | Description |
|-----|--------|------|----------|-------------|
| S | C3 Name | Text | Yes (Tier 1) | Full name |
| T | C3 Title | Text | Yes (Tier 1) | Current job title |
| U | C3 LinkedIn | URL | Yes (Tier 1) | Full LinkedIn profile URL |

### Meta Block (Columns V-AA)

| Col | Header | Type | Required | Description |
|-----|--------|------|----------|-------------|
| V | Account Tier | Text | Yes | Tier 1, Tier 2, or Tier 3 |
| W | Confidence Level | Text | Yes | High, Medium, or Low (see scoring-framework.md) |
| X | Next Step | Text | Yes | Recommended action (see scoring-framework.md) |
| Y | HubSpot Status | Text | Yes | New, Existing, or Enriched |
| Z | Source | Text | Yes | Primary data source(s) used |
| AA | Notes | Text | Optional | Additional context, caveats, data freshness |

### v2 Reserved (Columns AB-AD) — Documented but Not Active

| Col | Header | Type | Required | Description |
|-----|--------|------|----------|-------------|
| AB | Cloud Stack | Text | Future | Known cloud/infra stack (AWS, Azure, on-prem, etc.) |
| AC | Intent Signals | Text | Future | Observed buying signals (job postings, tech blog posts, tenders) |
| AD | Compute Propensity Score | Number | Future | 0-100 score (see scoring-framework.md v2 section) |

---

## Quality Thresholds

### Minimum Viable Row
A row must have at minimum:
- Company Name, Country, Vertical, Website (columns A, B, C, E)
- At least one contact with Name, Title, and LinkedIn (columns I, J, K)
- Account Tier and Confidence Level (columns V, W)

### Target Quality by Tier

**Tier 1**: All columns A-AA populated. All 3 contacts identified. Revenue data from a named source. Rationale for Champion and Economic Buyer. Confidence = High or Medium.

**Tier 2**: Columns A-R populated. 2 contacts (Champion + Economic Buyer). Revenue data best effort. Rationale for Champion. Confidence = High or Medium.

**Tier 3**: Columns A-K and V-X populated. 1 contact (Champion). Revenue estimated or proxied by employee count. Confidence = any level acceptable.

---

## HubSpot CSV Field Mapping

When importing to HubSpot, map as follows:

| xlsx Column | HubSpot Property | HubSpot Object |
|-------------|-----------------|----------------|
| Company Name | Company name | Company |
| Country | Country/Region | Company |
| Website | Website URL | Company |
| Revenue EUR est | Annual revenue | Company |
| Employee Count | Number of employees | Company |
| Vertical | Industry | Company |
| Sub-segment | (Custom) Sub-segment | Company |
| HQ City | City | Company |
| C1 Name | First name + Last name | Contact |
| C1 Title | Job title | Contact |
| C1 Email | Email | Contact |
| C1 Phone | Phone number | Contact |
| C1 LinkedIn | (Custom) LinkedIn URL | Contact |
| Account Tier | (Custom) Account Tier | Company |
| Confidence Level | (Custom) Confidence Level | Company |
| Source | (Custom) Lead Source Detail | Company |

Note: HubSpot import requires separate Company and Contact imports with association. The xlsx is the master file; HubSpot import is a downstream step.

---

## Sample Rows

### Tier 1 Example
| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| Erasmus MC | NL | Healthcare | Rotterdam | https://www.erasmusmc.nl | 1,800,000,000 | 15,000 | University Medical Center |

| V | W | X | Y | Z | AA |
|---|---|---|---|---|---|
| Tier 1 | High | Multi-thread outreach | New | NZa jaarverslagen 2024, KVK | Revenue from 2024 annual report |

### Tier 2 Example
| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| Van Oord | NL | Logistics | Rotterdam | https://www.vanoord.com | 2,100,000,000 | 5,000 | Marine Transport |

| V | W | X | Y | Z | AA |
|---|---|---|---|---|---|
| Tier 2 | Medium | Champion-first outreach | New | KVK filing 2024, website | Revenue estimated from annual report |

### Tier 3 Example
| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| Koppert Cress | NL | Horticulture | Monster | https://www.koppertcress.com | 45,000,000 | 200 | Specialty Growers |

| V | W | X | Y | Z | AA |
|---|---|---|---|---|---|
| Tier 3 | Low | Research & nurture | Check HubSpot | Website, CBS | Revenue estimated from employee proxy |

---

## File Naming Convention

```
leads_{vertical}_{country}_{YYYY-MM-DD}_v{version}.xlsx
```

Examples:
- `leads_healthcare_NL_2026-03-25_v1.xlsx`
- `leads_finance_BENELUX_2026-03-25_v1.xlsx`
- `leads_horticulture_NL_2026-03-25_v2.xlsx` (v2 = revised batch)

### Batch Handoff Files
When work spans multiple sessions, use:
```
handoff_{vertical}_{country}_{YYYY-MM-DD}.md
```
This contains progress notes, completed rows, and remaining work items.

---

## Data Integrity Rules

1. **No empty required fields** — if data cannot be found, mark as "Not found" rather than leaving blank
2. **URLs must be valid** — include https:// prefix, verify domains resolve
3. **Revenue in EUR** — convert from other currencies at current rate; note original currency in Notes
4. **Names in native format** — "Jan van der Berg" not "Van Der Berg, Jan"
5. **One company per row** — subsidiaries get their own rows with parent noted
6. **No duplicate companies** — check within batch and against HubSpot export
7. **Source attribution** — every data point should be traceable to a source
