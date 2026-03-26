# Enrichment Methodology — Data Pipeline & Quality

## Overview

The enrichment pipeline transforms a raw list of target companies into a fully populated xlsx output. The process follows a strict sequence: Identify, Enrich, Verify, Normalize, Output.

---

## Pipeline Stages

### Stage 1: Identify

**Objective**: Build the initial target company list from registry and public sources.

Steps:
1. Define vertical and geography scope
2. Pull from primary registry (see geo-sources.md for per-country registries)
3. Apply size filters (revenue, employees, assets — per vertical thresholds)
4. Remove known exclusions (already in HubSpot, out of scope, dissolved entities)
5. Rank by size metric to assign preliminary tiers

**Output**: Raw company list with Name, Country, Vertical, and size indicator.

**Key Rule**: Filter BEFORE enriching. Do not spend enrichment effort on companies that will be filtered out.

### Stage 2: Enrich

**Objective**: Populate all company and contact fields in the output schema.

#### Company Enrichment Waterfall

Try sources in this order; stop when data point is found:

1. **Official registry** (KVK, KBO, CSSF) — Legal name, HQ city, registration number
2. **Company website** — Trading name, website URL, sub-segment indicators
3. **Annual report / financial filing** — Revenue, employee count, organizational structure
4. **CBS / statistics office** — Revenue estimates, sector averages (for sizing when company-specific data unavailable)
5. **Industry rankings** — MT500, Trends Top 100.000, sector-specific lists
6. **LinkedIn company page** — Employee count (approximate), HQ location, industry
7. **News / press** — Revenue announcements, M&A activity, growth indicators

#### Contact Enrichment Waterfall

For each required contact role (Champion, Economic Buyer, Blocker):

1. **Company website** — Leadership / team page, press releases
2. **LinkedIn** — People search filtered by company and title keywords
3. **Annual report** — Management board, organizational leadership
4. **KVK / KBO** — Registered directors and authorized signatories
5. **Conference / event records** — Speaker lists, panel participants
6. **Press / media** — Interviews, quotes, award mentions
7. **Industry association** — Board members, committee members

#### Email Discovery Waterfall

1. **Company website** — Check for listed emails to detect pattern
2. **Pattern generation** — Apply detected pattern to contact name
3. **LinkedIn contact info** — If connected or via InMail
4. **Google search** — `"firstname.lastname@domain"` or `"@domain.nl"` in public documents
5. **GitHub / academic profiles** — For technical contacts
6. **Tool verification** — If using Apollo, Clay, or similar (verify, don't trust blindly)
7. **Mark as not found** — If no email can be confirmed, note LinkedIn as primary channel

### Stage 3: Verify

**Objective**: Validate data accuracy before output.

#### Company Verification
- Website URL resolves and matches the correct entity
- Revenue figure has a source and year noted
- Employee count is within plausible range for the revenue
- Company is still active (not dissolved, merged, or acquired)
- Sub-segment classification is accurate
- No duplicate with another row in the batch or HubSpot

#### Contact Verification
- Person is still at the company (LinkedIn shows current role)
- Title matches the assigned buying committee role
- LinkedIn URL is correct and active
- Name spelling is verified against multiple sources
- For NL: Dutch naming conventions respected (van, van de, van der, de, etc.)
- Email (if found) follows the correct company pattern

#### Cross-Verification
- Champion and Economic Buyer are different people
- Contacts are at the correct legal entity (not subsidiary/parent confusion)
- Account Tier aligns with company size data
- Confidence Level reflects actual data quality

### Stage 4: Normalize

**Objective**: Standardize all data for consistent output.

Rules:
- Country codes: NL, BE, LU (not "Netherlands," "Belgium," "Luxembourg")
- Revenue in EUR with no currency symbol in cell (number format)
- URLs with https:// prefix
- LinkedIn URLs in format: https://www.linkedin.com/in/username/
- Names in natural order: "Jan van der Berg" (not "van der Berg, Jan")
- Titles in original language if commonly used (e.g., "Directeur ICT" is acceptable)
- Phone numbers in international format: +31 6 1234 5678
- Dates in ISO format: YYYY-MM-DD
- No trailing spaces, no smart quotes, no special characters that break CSV

### Stage 5: Output

**Objective**: Generate the final xlsx file.

Steps:
1. Populate all columns per output-schema.md
2. Sort by Account Tier (Tier 1 first), then by Revenue descending
3. Apply conditional formatting (optional): Tier 1 = green, Tier 2 = yellow, Tier 3 = no fill
4. Name file per convention: `leads_{vertical}_{country}_{date}_v{version}.xlsx`
5. Generate summary statistics: Total rows, per-tier counts, confidence distribution
6. Save to agreed location

---

## Batch Processing Protocol

### Why Batches
- Context window limits require breaking large lists into manageable chunks
- Quality degrades when processing too many companies at once
- Allows for mid-process quality checks and course corrections

### Batch Size
- **Recommended**: 10 companies per batch
- **Maximum**: 15 companies per batch
- **Minimum**: 5 companies per batch (for very deep Tier 1 research)

### Context Reset Procedure
When a new session or context reset occurs mid-project:

1. **Before reset**: Create a handoff artifact containing:
   - Companies completed (with row numbers)
   - Companies in progress (with partial data)
   - Companies remaining
   - Any issues or blockers encountered
   - Current file version and location

2. **After reset**: Begin by:
   - Reading the handoff artifact
   - Loading the current xlsx file
   - Resuming from the first incomplete company
   - Re-verifying the last 2-3 completed rows (catch errors from context fatigue)

### Handoff Artifact Format
```markdown
# Handoff: {vertical} {country} {date}

## Completed (rows 2-12)
- Row 2: Company A — Tier 1 — Full
- Row 3: Company B — Tier 2 — Full
...

## In Progress
- Row 13: Company C — Company data done, contacts pending

## Remaining
- Company D, Company E, Company F...

## Issues
- Company X: Could not find revenue data; used employee proxy
- Company Y: CIO recently departed; need to re-check

## File
- Location: /path/to/file.xlsx
- Version: v1
- Last updated: 2026-03-25
```

---

## Data Decay

### Annual Decay Rates (Industry Benchmarks)
- **Email addresses**: 25-30% become invalid per year
- **Phone numbers**: 15-20% change per year
- **Job titles**: 20-25% change per year (people change roles/companies)
- **Company data**: 5-10% change per year (M&A, rebranding, closure)

### Implications
- Data older than 12 months should be flagged for re-verification
- Contact data older than 6 months benefits from a quick LinkedIn check
- Revenue data should always note the year of the figure
- Re-enrichment cycles should be planned quarterly for active pipeline

---

## Quality Metrics

### Per-Batch Quality Targets
- **Completion rate**: >95% of required fields populated
- **Contact hit rate**: >80% of companies have at least Champion identified
- **Email discovery rate**: >50% of Champions have email found
- **Revenue data rate**: >70% of companies have revenue figure
- **Verification pass rate**: >90% of contacts confirmed current at company

### Quality Flags
Mark rows with quality issues:
- `[VERIFY]` — Data point needs additional verification
- `[PROXY]` — Revenue estimated from employee count proxy
- `[STALE]` — Data source older than 18 months
- `[CONFLICT]` — Conflicting data from multiple sources (note both in Notes)

---

## What NOT to Do

1. **Do not fabricate data** — If you cannot find a revenue figure, leave it blank or mark as "Not found." Never estimate without basis.
2. **Do not guess email addresses** — Pattern-based emails must be flagged as unverified. Never present a guess as confirmed.
3. **Do not skip verification** — Every contact must have at least a LinkedIn check for currency.
4. **Do not enrich before filtering** — Size-filtering first saves significant effort.
5. **Do not ignore duplicates** — Always check against HubSpot export and within-batch.
6. **Do not mix entities** — A subsidiary is not its parent company. Keep them separate.
7. **Do not use personal email addresses** — Only business email addresses are appropriate.
8. **Do not scrape LinkedIn at scale** — Use LinkedIn for targeted research, not bulk scraping (ToS violation).
9. **Do not ignore data freshness** — Always note the year/date of revenue and employee data.
10. **Do not assume NL patterns apply to BE/LU** — Each country has distinct registries and business cultures.
