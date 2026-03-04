# Jurisdiction Guide -- Seed Round Structuring

## 1. Overview

Seed-round structuring must consider where the holding company sits, where operations occur, and where investors are located. This guide covers the two primary jurisdictions for Digital Energy: Switzerland (holding) and Netherlands (operations), with extension points for other structures.

## 2. Switzerland -- AG and GmbH

### 2.1 Entity Comparison

| Feature | Aktiengesellschaft (AG) | Gesellschaft mit beschrankter Haftung (GmbH) |
|---|---|---|
| Governing law | Swiss Code of Obligations (OR), Art. 620 ff. | OR Art. 772 ff. |
| Minimum capital | CHF 100,000 | CHF 20,000 |
| Capital paid-in at formation | 20% (min CHF 50,000) | 100% |
| Share types | Bearer (Inhaberaktien) or registered (Namenaktien) | Stammanteile (registered only) |
| Par value minimum | CHF 0.01 | CHF 100 |
| Shareholder register | Required for Namenaktien; Inhaberaktien since 2020 | Always required; public at Handelsregister |
| Transfer restrictions | Vinkulierung possible (board approval) | Requires GM approval by default |
| Auditing | Required if >10 employees or 2 of: CHF 20M revenue, CHF 10M assets, 50 employees | Same thresholds; opting-out possible if <10 employees |
| VC preference | Strongly preferred for fundraising | Less common for institutional capital |

**Recommendation for seed fundraise**: AG. It's the standard vehicle for Swiss startups raising institutional capital. GmbH's public shareholder register and mandatory GM transfer approval create friction for investors.

### 2.2 Swiss AG Capital Mechanics for Fundraising

| Mechanism | Description | Use in Fundraise |
|---|---|---|
| Ordinary capital increase | GM resolution (2/3 majority), notarized | Standard for priced rounds |
| Authorized capital (genehmigtes Kapital) | Board can issue shares up to 50% of existing, 2-year limit | Flexibility for tranched closes |
| Conditional capital (bedingtes Kapital) | Reserved for options/warrants, up to 50% of existing | ESOP, convertible instruments |
| SAFE/convertible | Not a Swiss law instrument; contractual obligation | Legal under freedom of contract (OR Art. 19) |
| Capital band (new, 2023 reform) | Board can increase/decrease capital within band for 5 years | New flexibility; useful for serial rounds |

### 2.3 Swiss Tax Considerations

| Tax | Rate / Rule | Notes |
|---|---|---|
| Federal CIT | 8.5% on net profit | Applied after cantonal/communal |
| Cantonal/communal CIT | Varies by canton | Zug: ~11.9% effective combined; Zurich: ~19% |
| Capital tax | 0.001-0.5% of equity capital | Canton-specific |
| Dividend WHT | 35% on distributions | Reclaimable under treaties for qualifying shareholders |
| Beteiligungsabzug | Participation deduction on dividends from qualifying holdings | Applies to dividends from Dutch BVs |
| Stamp duty (Emissionsabgabe) | 1% on equity issuance >CHF 1M | Applies at capital increase |
| SAFE/convertible treatment | Not subject to stamp duty until conversion | Tax-efficient bridge instrument |
| Innovation deduction | Canton-specific patent box regimes | Zug, Nidwalden, Schaffhausen most favorable |

### 2.4 Zug-Specific Advantages

| Advantage | Detail |
|---|---|
| Effective CIT rate | ~11.9% (one of lowest in CH) |
| Crypto Valley ecosystem | Established startup/fintech ecosystem |
| Holding company benefits | Beteiligungsabzug + low cantonal rate |
| International treaties | 100+ DTAs; EU bilateral agreements |
| Talent pool | Multilingual workforce; proximity to Zurich |
| Formation speed | AG can be formed in 1-2 weeks via notary |

## 3. Netherlands -- BV

### 3.1 Quick Reference (Flex-BV)

| Feature | Detail | Source |
|---|---|---|
| Minimum capital | EUR 0.01 | Art. 2:178 BW |
| Formation | Notariele akte (notarial deed) required | Art. 2:175 BW |
| Cost | EUR 500-1,500 notaris + EUR 82.25 KvK | Firm24/KvK.nl |
| UBO register | Mandatory; restricted public access since Jul 2025 | Handelsregisterwet |
| Share classes | Letteraandelen (A/B/C) permitted | Art. 2:178 BW |
| Transfer | Notariele akte required | Art. 2:196 BW |
| Pre-emption | Statutory voorkeursrecht (Art. 2:206a BW) | 4-week exercise period |
| Distribution | Balanstest + liquiditeitstest | Art. 2:216 BW |

### 3.2 Why Dutch BVs for Operations

| Reason | Detail |
|---|---|
| Grid connections | Dutch grid; TenneT/DSO contracts must be NL entity |
| Permits | Omgevingsvergunning requires NL legal person |
| Project finance | Lenders require ring-fenced NL SPV |
| Customer contracts | Dutch counterparties prefer NL entity |
| Tax efficiency | Deelnemingsvrijstelling on AG->BV dividends (via treaty) |

### 3.3 NL Tax Summary for Project BVs

See `project-financing` SKILL.md for comprehensive Dutch tax framework. Key items:

| Tax | Rate | Notes |
|---|---|---|
| CIT | 19% first EUR 200K / 25.8% excess | |
| Dividend WHT | 15% | Reduced to 0% under CH-NL treaty (Art. 10(2)(a)) for 25%+ holdings |
| BTW | 21% standard / 9% heat supply | |
| Earningsstripping | 24.5% of fiscal EBITDA (EUR 1M franchise) | Critical for leveraged SPVs |
| Deelnemingsvrijstelling | 0% on qualifying holdings (5%+) | AG benefits on BV distributions |

## 4. CH-NL Holding Structure

### 4.1 Structure Diagram

```
Investors (seed)
     |
     v
Digital Energy Group AG (Zug, CH)  <-- Holding / fundraise entity
  |  |  |
  v  v  v
BV 1  BV 2  BV 3   <-- Operating entities (NL)
(Site 1) (Site 2) (Site 3)
```

### 4.2 Tax Flow

| Flow | Treatment |
|---|---|
| BV profit -> BV | NL CIT at 19%/25.8% |
| BV dividend -> AG | NL WHT 0% (CH-NL treaty, Art. 10(2)(a), 25%+ holding) |
| AG receives BV dividend | CH Beteiligungsabzug: effective 0% federal CIT |
| AG dividend -> Investors | CH WHT 35%; reclaimable under treaty |
| AG distributes to CH individuals | 35% WHT; partially reclaimable (effective ~20-25% tax) |
| AG distributes to NL individuals | 35% WHT; treaty reduces to 15%; excess reclaimable |
| AG distributes to US entities | 35% WHT; treaty reduces to 5-15%; excess reclaimable |

### 4.3 Key Structuring Considerations

| Consideration | Guidance |
|---|---|
| Substance | AG must have genuine Swiss substance (board meetings, management, bank account) |
| Transfer pricing | Arm's length for intra-group services/loans |
| BEPS compliance | Swiss-NL structures well-established; treaty regularly updated |
| Conditional WHT (NL) | 25.8% applies to low-tax jurisdictions; CH does NOT qualify (rate >9%) |
| Earningsstripping | Apply at BV level; AG level if relevant |
| ATAD infra exemption | NL BV project debt may qualify for ATAD infrastructure exemption |

## 5. Alternative Structures

### 5.1 US Delaware C-Corp (If Needed for US Investors)

| Feature | Detail |
|---|---|
| When to consider | If majority of investors are US-based VCs |
| Structure | DE C-Corp as holding above CH AG, or flip AG to C-Corp |
| SAFE compatibility | Standard YC SAFE designed for DE C-Corp |
| Tax | US CIT 21%; state taxes vary; complex international tax planning |
| Recommendation | Only pursue if US investor mandate requires it; adds complexity |

### 5.2 Luxembourg (If Needed for Institutional)

| Feature | Detail |
|---|---|
| When to consider | Large institutional fund structures |
| Vehicle | RAIF, SCSp, or SICAV-RAIF |
| Tax | Favorable regime for investment vehicles |
| Recommendation | Unnecessary at seed; consider for Series B+ institutional co-investment vehicles |

## 6. Investor Preferences by Geography

| Investor Geography | Preferred Vehicle | Notes |
|---|---|---|
| Swiss | AG | Most familiar; stamp duty understood |
| Dutch | BV or AG | NL investors comfortable with either |
| German | AG or GmbH | German-speaking familiarity |
| UK | AG or C-Corp | Comfortable with both |
| US (VC) | C-Corp preferred; AG acceptable | May need education on AG mechanics |
| Middle East (SWF) | AG | International holding company standard |
| Asian | AG | Neutral; focus on terms not jurisdiction |

---

## Cross-References

| Topic | Reference |
|---|---|
| Dutch legal framework (detailed) | `project-financing/references/netherlands-legal-framework.md` |
| Dutch equity structures | `_shared/equity-structures.md` |
| Norwegian tax | `norwegian-tax-law` skill |
| Cap table mechanics | [references/cap-table-guide.md](cap-table-guide.md) |
| Investment structure section (IM) | [references/investment-memo-guide.md](investment-memo-guide.md) |
