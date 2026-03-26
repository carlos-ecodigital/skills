---
name: Batch Research SOP
version: 1.0
last_updated: 2026-03-25
---

# Batch Research Standard Operating Procedure

Step-by-step procedure for researching a batch of 10 companies as part of W1 (Full Vertical List Build).

## Pre-Batch Setup

1. **Confirm parameters from handoff artifact:**
   - Vertical: [e.g., Healthcare]
   - Country: [e.g., NL]
   - Batch number: [e.g., 3 of 10]
   - Companies to research: ranked [21-30] by revenue
   - Completed rows so far: [20]
   - Schema: output-schema.md

2. **Load only relevant references:**
   - `vertical-playbooks.md` — only the section for this vertical
   - `geo-sources.md` — only the section for this country
   - `contact-targeting.md` — full file (needed for every batch)
   - Do NOT load: tool-landscape.md, gdpr-compliance.md, scoring-framework.md (unless needed)

## Step 1: Company Identification (10 companies)

**Goal:** Identify the next 10 companies ranked by revenue for this vertical + country.

1. Web search: "[vertical] largest companies [country] revenue ranking 2025 2026"
2. Cross-reference with industry-specific registries from geo-sources.md
3. For each company, collect:
   - Company name (legal entity name)
   - HQ city
   - Website
   - Revenue estimate (EUR) — source from annual report, industry ranking, or web search
   - Employee count estimate
   - Industry sub-segment

**Quality gate:** All 10 companies must have: name, country, HQ city, website, and at least a revenue estimate or employee count for tiering. If a company cannot be verified as real/operational, replace it with the next-ranked company.

## Step 2: Account Tiering

Based on the overall list position (not just this batch):
- Positions 1-20: Tier 1
- Positions 21-50: Tier 2
- Positions 51-100: Tier 3

This batch's companies inherit their tier from their revenue rank in the full list.

## Step 3: Buying Committee Research

For each company in the batch, research contacts per tier depth:

### Tier 1 companies (3 contacts)

**Contact 1 — Champion (technical advocate):**
1. Check company website → leadership/management/team page
2. Search LinkedIn: "[company name]" + ("VP Infrastructure" OR "CTO" OR "VP Cloud" OR "Director IT")
3. Check press releases for recent CTO/CIO appointments
4. Verify: title shows as "current" on LinkedIn, dated within 12 months

**Contact 2 — Economic Buyer (budget authority):**
1. Search for: CIO, CFO, VP IT Procurement, Head of Sourcing
2. Verify via company website or annual report management board section

**Contact 3 — Blocker (gatekeeper):**
1. Search for: CISO, Head of Procurement, Chief Privacy Officer
2. May require LinkedIn search with broader title keywords

### Tier 2 companies (2 contacts)
- Contact 1 (Champion) + Contact 2 (Economic Buyer) only
- Same research methodology as Tier 1

### Tier 3 companies (1 contact)
- Best available senior IT/tech contact
- Typically: CTO, CIO, IT Director, Head of IT
- For small companies (<500 employees): owner/managing director may be the IT decision-maker

## Step 4: Email Discovery

For each contact:
1. Check company website contact/team page for direct email
2. If any company email is visible, detect the pattern (first.last@, f.last@, firstlast@)
3. Apply detected pattern to target contact name
4. If no pattern detectable, record "email unavailable"
5. **Never guess** — only record emails that are verified or pattern-based with flag

## Step 5: Confidence Rating

Rate each company-contact combination:
- **High:** Contact verified on company website + LinkedIn, title current (<12 months), company data from official registry/annual report
- **Medium:** Contact found on LinkedIn only, or from annual report, company data from web search
- **Low:** Contact from press release >12 months old, or inferred from job postings, company data estimated

## Step 6: Next-Step Recommendation

Apply the matrix:
- Tier 1 → "Priority: direct outreach via warm intro or executive email"
- Tier 2 → "Standard: cold outreach with case study"
- Tier 3 → "Passive: add to database, re-assess quarterly"

## Step 7: Compile Batch Output

Format all 10 companies per output-schema.md columns (A through AA).

## Step 8: QA Review

Before handing off:
1. **Row count:** Confirm exactly 10 rows (or fewer if vertical is exhausted)
2. **Required fields:** Every row has: Company Name, Country, Vertical, HQ City, Website, Sub-segment, at least 1 contact with name + title + LinkedIn + rationale
3. **Tier assignment:** Every row has Account Tier (1/2/3)
4. **Confidence:** Every row has Confidence Level (High/Med/Low)
5. **Next step:** Every row has a recommendation
6. **No duplicates:** No company appears twice within this batch or in previous batches
7. **No fabrication:** No guessed emails, no invented revenue figures, no unverified contacts presented as verified

## Step 9: Handoff Artifact

Create the handoff artifact for the next batch:

```
BATCH HANDOFF — Batch [N+1] of [M]
Vertical: [vertical] | Country: [country] | Target: [total count]
Completed rows: [previous + this batch] | Schema: output-schema.md
Next batch: companies ranked [N*10+1] to [(N+1)*10] by revenue
Rows completed in this batch: [10]
Cumulative row count: [verified total]

[This batch's data as structured table]
```

## Timing

- Company identification: ~5 min per batch of 10
- Contact research: ~2-3 min per company (varies by tier)
- Total batch time: ~30-40 min for 10 companies with Tier 1+2 depth
- Tier 3 batches are faster: ~20 min

## Common Issues

| Issue | Resolution |
|-------|-----------|
| Company website has no leadership page | Use LinkedIn + annual report |
| LinkedIn profile is private | Note "LinkedIn private — title from [source]" |
| Revenue data unavailable | Use employee count as proxy; note "revenue estimated from headcount" |
| Company was recently acquired | Note M&A status; flag whether IT decisions are now centralized |
| Multiple entities with same name | Use KVK/KBO number to disambiguate; note legal entity |
| Contact appears to have left | Mark as Low confidence; note "may have left — verify before outreach" |
| Country too small for 100 companies | Ask user to confirm adjusted target; never pad |
