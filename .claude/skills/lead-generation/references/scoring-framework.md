# Scoring Framework — Account Tiering, Confidence & Propensity

## Overview

This framework defines how to rank, tier, and score target accounts. v1 (active) uses revenue-based ranking with qualitative confidence levels. v2 (documented but not active) adds a Compute Propensity Score for future enhancement.

---

## v1: Revenue-Based Ranking (Active)

### Revenue as Primary Metric

Revenue is the primary ranking metric because:
- It correlates with IT budget (typically 3-7% of revenue for enterprises)
- It is the most consistently available financial metric across verticals
- It enables cross-vertical comparison
- It aligns with deal size potential

### Revenue Source Priority

When determining company revenue, use sources in this priority order:

1. **Published annual report** — Most authoritative; note fiscal year
2. **KVK/KBO/RCSL filed accounts** — Official filings; may be abbreviated for SMEs
3. **NZa open data (healthcare)** — Regulator-published financial data
4. **NBB Balanscentrale (Belgium)** — Central bank annual accounts database
5. **Industry rankings** — MT500, Trends Top 100.000 (may be 1-2 years old)
6. **DNB/CSSF registers (finance)** — Total assets for banks (not revenue, but sizing proxy)
7. **Company website / press releases** — Self-reported; may be selective
8. **News articles** — Third-party reporting; note date and context
9. **LinkedIn company page** — Rough employee count for proxy estimation
10. **Estimate from employee count** — Last resort proxy

### Employee Count as Revenue Proxy

When revenue data is unavailable, use employee count with sector-specific multipliers:

| Vertical | Revenue per Employee (EUR, approximate) |
|----------|----------------------------------------|
| Finance | 300,000 - 500,000 |
| Healthcare | 80,000 - 120,000 |
| Logistics | 100,000 - 200,000 |
| Agriculture (Cooperatives) | 500,000 - 1,500,000 |
| Horticulture | 150,000 - 300,000 |
| Defense contractors | 150,000 - 250,000 |

**Important**: Always flag proxy-based revenue estimates with `[PROXY]` in the Notes column and state the employee count used.

### Revenue Conversion
- All revenue figures in EUR
- For non-EUR sources, convert at the rate current on the date of the source
- Note original currency and conversion rate in Notes if applicable
- Most Benelux companies report in EUR natively

---

## Account Tiering

### Tier 1 — Strategic Accounts

**Criteria** (meet ANY of the following):
- Revenue > 500M EUR (or >50B total assets for banks)
- Top 10 in their sub-segment by revenue in their country
- Known brand name with strategic value for reference selling
- Existing relationship or warm introduction available
- Active in public procurement for compute/infrastructure services

**Expected Volume**: 5-15 per vertical per country (NL); 3-10 (BE); 1-5 (LU)

**Treatment**:
- Full buying committee mapping (3 contacts)
- Detailed research and rationale
- High-priority outreach
- Custom messaging per account
- Multi-threaded engagement

**Next Step Recommendation**: "Multi-thread outreach" or "Executive introduction"

### Tier 2 — Target Accounts

**Criteria** (meet ANY of the following):
- Revenue 100M-500M EUR (or 5-50B total assets for banks)
- Top 11-30 in their sub-segment by revenue
- Growth indicators (M&A activity, geographic expansion, digital transformation press)
- Moderate compute intensity in their operations

**Expected Volume**: 15-40 per vertical per country (NL); 10-25 (BE); 3-15 (LU)

**Treatment**:
- Champion + Economic Buyer mapping (2 contacts)
- Standard research and rationale
- Sequence-based outreach
- Segment-level messaging with light personalization

**Next Step Recommendation**: "Champion-first outreach" or "Warm-up sequence"

### Tier 3 — Opportunity Accounts

**Criteria**:
- Revenue 25M-100M EUR (or 1-5B total assets for banks)
- Identified but not yet deeply researched
- May become Tier 2 with additional intelligence
- Useful for pipeline volume and market coverage

**Expected Volume**: 20-100+ per vertical per country

**Treatment**:
- Champion identification only (1 contact)
- Light research
- Automated or semi-automated outreach
- Vertical-level messaging

**Next Step Recommendation**: "Research & nurture" or "Add to sequence"

### Special Cases

**Government / Defense Accounts**:
- Tiering is based on budget allocation and strategic importance rather than revenue
- Tier 1: Ministry of Defence, major defense primes (>100M EUR defense revenue)
- Tier 2: Mid-size defense contractors, government agencies with significant IT budgets
- Tier 3: Small defense suppliers, government entities with limited IT scope

**Financial Sector (Luxembourg)**:
- Use total assets under management (AUM) or total assets instead of revenue
- Tier 1: >50B EUR AUM or total assets
- Tier 2: 5-50B EUR
- Tier 3: 1-5B EUR

---

## Confidence Levels

### High Confidence

**Criteria** (ALL must be met):
- Revenue figure from authoritative source (annual report, regulator, official filing) dated within last 24 months
- At least Champion contact verified as current employee via LinkedIn
- Company website confirmed and active
- Sub-segment classification verified through multiple sources

**Implications**:
- Data can be used for immediate outreach
- HubSpot import without additional verification
- Suitable for Tier 1 account planning

### Medium Confidence

**Criteria** (MOST of the following):
- Revenue figure from secondary source (industry ranking, news) or dated 24-36 months
- OR revenue estimated from employee count proxy
- Contact identified but role currency not 100% confirmed
- Company data consistent across at least 2 sources
- Minor gaps in data (e.g., missing email, estimated employee count)

**Implications**:
- Data suitable for outreach with caveat
- HubSpot import acceptable; flag for enrichment cycle
- Brief verification recommended before Tier 1 outreach

### Low Confidence

**Criteria** (ANY of the following):
- Revenue data unavailable or older than 36 months
- Revenue estimated with low basis (rough employee guess, sector average)
- Contact not fully verified (may have changed roles)
- Limited data from only one source
- Company may have undergone recent changes (M&A, restructuring)

**Implications**:
- Data requires enrichment before outreach
- Mark as "Needs Research" in HubSpot
- Not suitable for personalized outreach until upgraded
- Acceptable for Tier 3 list building and market mapping

---

## Next-Step Recommendation Matrix

| Tier | Confidence | Next Step |
|------|-----------|-----------|
| Tier 1 | High | Multi-thread outreach — engage Champion and Economic Buyer simultaneously |
| Tier 1 | Medium | Verify & enrich — confirm contact data, then multi-thread outreach |
| Tier 1 | Low | Deep research — upgrade data quality before any outreach |
| Tier 2 | High | Champion-first outreach — personalized sequence to Champion |
| Tier 2 | Medium | Champion-first outreach — standard sequence with personalization |
| Tier 2 | Low | Research & nurture — add to nurture sequence while enriching |
| Tier 3 | High | Add to sequence — automated outreach sequence |
| Tier 3 | Medium | Add to sequence — lower-touch automated sequence |
| Tier 3 | Low | Research & nurture — park for future enrichment cycle |

---

## v2 Enhancement: Compute Propensity Score (Documented, Not Active)

> This section documents a planned enhancement. The fields are reserved in the output schema (columns AB-AD) but should NOT be populated in v1 output.

### Concept

The Compute Propensity Score (CPS) estimates how likely a company is to have significant compute infrastructure needs. Score ranges from 0-100.

### Five Scoring Factors

#### Factor 1: Industry Compute Intensity (Weight: 25%)
How compute-intensive is the company's core business?

| Score | Criteria |
|-------|----------|
| 90-100 | Core business IS compute (data centers, cloud, HPC) |
| 70-89 | Heavy compute dependency (financial modeling, genomics, AI/ML) |
| 50-69 | Moderate compute (ERP-dependent, data analytics, IoT processing) |
| 30-49 | Standard IT (office productivity, basic applications) |
| 0-29 | Minimal IT (manual processes, basic operations) |

#### Factor 2: Digital Maturity Signals (Weight: 20%)
Evidence of technology investment and digital transformation.

| Score | Criteria |
|-------|----------|
| 90-100 | Published cloud/AI strategy; dedicated CTO/CDO; tech blog; innovation lab |
| 70-89 | Active digital transformation program; recent IT leadership hires |
| 50-69 | Standard IT department; some modernization efforts |
| 30-49 | Limited technology presence; legacy systems dominant |
| 0-29 | No visible technology investment signals |

#### Factor 3: Scale and Growth (Weight: 20%)
Company size and trajectory indicate future compute demand.

| Score | Criteria |
|-------|----------|
| 90-100 | Revenue >1B EUR AND growing >10% annually |
| 70-89 | Revenue >500M EUR OR rapid growth (>15%) |
| 50-69 | Revenue 100-500M EUR with stable operations |
| 30-49 | Revenue 25-100M EUR |
| 0-29 | Revenue <25M EUR with no growth signals |

#### Factor 4: Infrastructure Indicators (Weight: 20%)
Observable signs of current infrastructure investment.

| Score | Criteria |
|-------|----------|
| 90-100 | Operates own data centers; published infrastructure job postings |
| 70-89 | Known cloud migration project; infrastructure team on LinkedIn |
| 50-69 | Standard IT infrastructure; managed services likely |
| 30-49 | Basic infrastructure; likely hosted/SaaS-dependent |
| 0-29 | No infrastructure indicators visible |

#### Factor 5: Procurement Readiness (Weight: 15%)
Signals that the company is in or near a buying cycle.

| Score | Criteria |
|-------|----------|
| 90-100 | Active tender for compute/infrastructure services |
| 70-89 | RFI published or known evaluation in progress |
| 50-69 | Budget cycle alignment; contract renewal approaching (if known) |
| 30-49 | General interest signals (conference attendance, content downloads) |
| 0-29 | No procurement signals detected |

### CPS Calculation
```
CPS = (Factor1 * 0.25) + (Factor2 * 0.20) + (Factor3 * 0.20) + (Factor4 * 0.20) + (Factor5 * 0.15)
```

### CPS Interpretation
| CPS Range | Label | Action |
|-----------|-------|--------|
| 80-100 | Very High Propensity | Immediate priority; likely strong fit |
| 60-79 | High Propensity | Strong candidate; prioritize outreach |
| 40-59 | Medium Propensity | Worth pursuing; standard pipeline |
| 20-39 | Low Propensity | Long-term nurture; may not be ready |
| 0-19 | Very Low Propensity | Deprioritize; unlikely near-term opportunity |

### Intent Signal Detection (v2)
Signals to monitor for column AC:
- Job postings for cloud architects, DevOps engineers, data engineers
- Press releases about digital transformation or cloud migration
- Tender publications for infrastructure services
- Conference speaking on cloud/compute topics
- LinkedIn posts from IT leadership about technology strategy
- Technology partnership announcements
- Data center expansion or construction permits
- Sustainability/energy reports mentioning compute efficiency

### v2 Activation Criteria
Activate v2 scoring when:
1. v1 process is stable and producing consistent output
2. Sufficient data exists to populate at least 3 of 5 factors for >60% of accounts
3. Sales team provides feedback loop on score accuracy vs. actual deal progression
4. Tool infrastructure supports automated signal monitoring (e.g., Clay + 6sense)
