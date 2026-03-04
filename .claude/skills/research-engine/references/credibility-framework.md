# Credibility Framework

> Source evaluation, confidence scoring, and conflict resolution rules.
> Referenced by all agent templates. Load for every research workflow.

## Source Tier Definitions

### Tier 1 — Institutional Authority (Weight: 1.0)

Sources with institutional accountability, peer review, or regulatory mandate.

| Source Type | Examples |
|---|---|
| Government / regulatory bodies | ACM, RVO, TenneT, European Commission, IEA, IRENA, CBS, Eurostat |
| Academic publications | Peer-reviewed journals, university research departments |
| Official statistics | CBS (NL), Eurostat, BNEF, IHS Markit |
| Industry standards bodies | ENTSO-E, ACER, DNV, TUV |
| Central / development banks | DNB, EIB, Invest-NL, World Bank |
| Audited financial reports | Annual reports, 10-K/20-F filings, regulated disclosures |
| Primary legislation | Staatsblad, Official Journal of the EU, wetten.overheid.nl |

### Tier 2 — Professional Authority (Weight: 0.7)

Sources with editorial standards or professional reputation, but without the institutional mandate of Tier 1.

| Source Type | Examples |
|---|---|
| Major financial media | FT, Bloomberg, Reuters, Het Financieele Dagblad, Energeia |
| Established consultancies | McKinsey, BCG, Deloitte, PwC, KPMG, EY (branded reports) |
| Law firm publications | CMS, Allen & Overy, De Brauw, NautaDutilh, Stibbe, Loyens & Loeff |
| Industry associations | DDA, Holland Solar, NWEA, NLdigital |
| Real estate / infra analysts | CBRE, JLL, Cushman & Wakefield, Alantra |
| Specialized trade media | Datacenterdynamics, Energy Storage News, PV Magazine, S&P Global |

### Tier 3 — Informal / Promotional (Weight: 0.4)

Sources without editorial review or institutional accountability. Useful for leads but not for key findings without corroboration.

| Source Type | Examples |
|---|---|
| Company press releases | Self-serving claims, product announcements |
| Blogs and opinion pieces | LinkedIn articles, Medium posts, personal blogs |
| Forums and social media | Reddit, Twitter/X threads, LinkedIn comments |
| Unverified aggregator sites | News aggregators without original reporting |
| Promotional white papers | Vendor-funded "research" with obvious bias |
| Wikipedia | Useful for orientation but not citable as primary source |

### Special Handling Rules

- **Vendor claims about own products:** Always Tier 3 regardless of publication venue.
- **Self-published research:** Tier 2 at best, even from reputable companies (no peer review).
- **Paywalled content:** If summary is visible but full report is behind a paywall, note in knowledge gaps. Do not fabricate data from partial glimpses.
- **Pre-print papers (arXiv):** Tier 2 (not peer-reviewed but often from credible researchers).

## Composite Confidence Score

Each individual finding gets a composite score from 5 factors:

```
Confidence = Tier_Weight x Recency x Geo_Relevance x Corroboration x Specificity
```

### Factor Tables

**Recency Factor:**

| Age of Source | Standard Fields | Fast-Moving Fields (AI, energy prices) | Slow-Moving Fields (geology, legislation) |
|---|---|---|---|
| < 6 months | 1.0 | 1.0 | 1.0 |
| 6-12 months | 0.9 | 0.7 | 1.0 |
| 1-2 years | 0.7 | 0.4 | 0.9 |
| 2-3 years | 0.5 | 0.2 | 0.7 |
| 3+ years | 0.3 | 0.1 | 0.5 |

**Geographic Relevance Factor (DE topics only — defaults to 1.0 for non-DE):**

| Scope | Factor |
|---|---|
| Netherlands-specific source | 1.0 |
| EU / EEA source | 0.8 |
| Comparable markets (Nordics, Germany, UK) | 0.7 |
| Global / US-centric source | 0.5 |

**Corroboration Factor:**

| Corroboration Level | Factor |
|---|---|
| 3+ independent sources agree | 1.2 (bonus) |
| 2 independent sources agree | 1.0 |
| Single source only | 0.7 |
| Sources conflict on this point | 0.5 (flag for resolution) |

**Specificity Factor:**

| Specificity | Factor |
|---|---|
| Exact number with methodology disclosed | 1.0 |
| Exact number without methodology | 0.8 |
| Range or estimate | 0.7 |
| Qualitative claim only | 0.5 |

### Mapping Scores to Labels

| Composite Score | Label | Meaning |
|---|---|---|
| >= 0.7 | **HIGH** | Well-supported by multiple quality sources |
| 0.4 – 0.69 | **MEDIUM** | Supported but with caveats (single source, older data, or geographic mismatch) |
| 0.2 – 0.39 | **LOW** | Weakly supported, should be verified before reliance |
| < 0.2 | **PRELIMINARY** | Signal only, not evidence. Use with explicit warning. |

## Conflict Resolution Rules

### Cross-Tier Conflicts (e.g., Tier 1 says X, Tier 2 says Y)

Default: Tier 1 wins. Exception: If the Tier 2 source is significantly more recent AND the field is fast-moving, the Tier 2 finding takes precedence. Always present both claims with sources and note the conflict.

### Same-Tier Conflicts

Present both claims. Note the discrepancy. Hypothesize why the sources differ:

- Different methodology (e.g., different market definitions)
- Different time periods (Q1 vs Q4 data)
- Different geographic scope (NL vs EU averages)
- Different sample sizes or data sources

Never silently pick one side.

### High-Stakes Contradictions

When a contradiction would change a recommendation AND evidence is balanced between the two sides, trigger adversarial debate. Two agents each marshal evidence for their position. A judge agent evaluates which is better supported.

Trigger criteria (ALL must be true):

1. The contradiction affects a Key Finding (not just the evidence table).
2. Both claims come from Tier 1-2 sources.
3. Corroboration is similar for both claims.
4. The resolution would change the brief's recommendation or conclusion.
