# Sample Output: Top 10 Healthcare Companies — Netherlands

This example shows the expected output format for a W1 (Full Vertical List Build) run. First 10 companies of a 100-company list, demonstrating all three tiers.

## Tier 1 (3 contacts each)

| Col | Company 1 | Company 2 |
|-----|-----------|-----------|
| A: Company Name | Philips (Koninklijke Philips N.V.) | Erasmus MC |
| B: Country | NL | NL |
| C: Vertical | Healthcare | Healthcare |
| D: HQ City | Amsterdam | Rotterdam |
| E: Website | philips.com | erasmusmc.nl |
| F: Revenue (EUR est.) | €18.2B | €2.1B |
| G: Employees (est.) | 69,000 | 17,000 |
| H: Sub-segment | Medtech / Health Technology | University Medical Center |
| I: Contact 1 Name | [researched name] | [researched name] |
| J: Contact 1 Title | VP IT Infrastructure & Cloud | CIO / Director ICT |
| K: Contact 1 LinkedIn | [verified URL] | [verified URL] |
| L: Contact 1 Email | [pattern: first.last@philips.com] | [pattern: initials@erasmusmc.nl] |
| M: Contact 1 Phone | [if available] | [if available] |
| N: Contact 1 Rationale | Champion — owns compute infrastructure decisions. Philips runs hybrid cloud (AWS + on-prem). Recent LinkedIn posts about AI workload scaling. | Champion — responsible for all ICT infrastructure across the MC. Erasmus MC is NL's largest academic hospital with significant research compute needs. |
| O: Contact 2 Name | [researched name] | [researched name] |
| P: Contact 2 Title | CIO | CFO |
| Q: Contact 2 LinkedIn | [verified URL] | [verified URL] |
| R: Contact 2 Rationale | Economic Buyer — budget authority for IT investments. Reports directly to CEO. | Economic Buyer — controls capex allocation. UMCs have centralized budget authority for infrastructure investments. |
| S: Contact 3 Name | [researched name] | [researched name] |
| T: Contact 3 Title | CISO / Head of Information Security | Head of Procurement |
| U: Contact 3 LinkedIn | [verified URL] | [verified URL] |
| V: Account Tier | 1 | 1 |
| W: Confidence | High | Medium |
| X: Next Step | Priority: direct outreach via warm intro or executive email | Priority: direct outreach via warm intro or executive email |
| Y: HubSpot Status | New | New |
| Z: Source | Annual Report 2024, LinkedIn, philips.com/about | erasmusmc.nl, LinkedIn, NZa registry |
| AA: Notes | NVIDIA DGX customer. Active AI/ML programs in imaging. | Part of NFU (Dutch Federation of University Medical Centres). Heavy research compute user. |

## Tier 2 (2 contacts each)

| Col | Company 3 | Company 4 |
|-----|-----------|-----------|
| A: Company Name | Zilveren Kruis (Achmea) | ASML Healthcare division |
| F: Revenue | €22B (Achmea group) | Part of €28B ASML |
| H: Sub-segment | Health Insurance | Medtech / Semiconductor Health |
| V: Account Tier | 2 | 2 |
| Contacts | 2 (Champion + Economic Buyer) | 2 (Champion + Economic Buyer) |

## Tier 3 (1 contact)

| Col | Company 5 |
|-----|-----------|
| A: Company Name | Lentis (GGZ) |
| F: Revenue | €450M est. |
| H: Sub-segment | Mental Healthcare Chain |
| V: Account Tier | 3 |
| Contacts | 1 (Best available IT/tech contact) |

## Notes on This Sample

- Revenue figures sourced from annual reports or MT500/CBS data
- Contact names replaced with [researched name] — in real output, actual names from web/LinkedIn research
- Email patterns noted when direct email unavailable: "pattern: first.last@domain.com"
- Confidence: High when verified on both company site and LinkedIn; Medium when LinkedIn only
- HubSpot Status: checked against existing CRM before output
