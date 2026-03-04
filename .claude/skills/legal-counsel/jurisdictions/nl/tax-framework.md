# Netherlands -- Tax Framework

## Vennootschapsbelasting (VPB / Corporate Income Tax)

### Rates (2025/2026)

| Parameter | Detail |
|---|---|
| Tarief (rate) | 19% on first EUR 200,000; 25.8% above EUR 200,000 |
| Financial sector surcharge | 25.8% on entire taxable profit (banks, insurers) |

### Earningsstripping (Renteaftrekbeperking, Art. 15b Wet VPB)

- Net interest expense deductible up to **24.5% of fiscale EBITDA** (increased from 20%, eff. 1 Jan 2025)
- **Franchise:** EUR 1M (net interest up to EUR 1M always deductible)
- Excess carried forward indefinitely
- Per-entity rule; no consolidation within fiscal unity for this purpose
- Interacts with specific anti-abuse rules (Art. 10a, 10b Wet VPB)

### Verliesverrekening (Loss Relief)

- **Carry-back:** 1 year
- **Carry-forward:** unlimited in time; capped at EUR 1M + 50% of taxable profit exceeding EUR 1M
- Applies per entity within fiscal unity

### Afschrijving (Depreciation)

- Gebouwen (buildings): max depreciation to WOZ-waarde (WOZ value); 100% own use; 100% belegging (investment property since 2024)
- Goodwill: max 10% per year
- Other assets: generally based on economic useful life

### Investeringsaftrek (Investment Deductions)

| Regeling | Rate | Qualifying Assets |
|---|---|---|
| KIA (Kleinschaligheidsinvesteringsaftrek) | Sliding scale, max 28% | Small-scale investments EUR 2,801--EUR 387,580 |
| EIA (Energie-investeringsaftrek) | 45.5% of qualifying investment | Energy-efficient assets (Energielijst RVO) -- BESS, heat pumps, efficient cooling |
| MIA (Milieu-investeringsaftrek) | 27% / 36% / 45% depending on category | Environmental assets (Milieulijst RVO) |
| VAMIL (Willekeurige afschrijving milieu-investeringen) | 75% arbitrary depreciation in year 1 | Same qualifying assets as MIA |

## Deelnemingsvrijstelling (Participation Exemption, Art. 13 Wet VPB)

- **0% CIT** on qualifying dividends and capital gains from holdings of 5% or more
- **Toetsen (tests):** must satisfy either:
  - Onderworpenheidstoets (subject-to-tax test): subsidiary subject to profit tax at reasonable rate
  - Bezittingstoets (asset test): <50% free portfolio investments (vrije beleggingen)
- Applies to both domestic and foreign subsidiaries
- **Liquidatieverliesregeling (Art. 13d):** deduction for losses on liquidation of qualifying subsidiary
- Critical for Dutch holding SPVs

## Fiscale eenheid (Fiscal Unity, Art. 15 Wet VPB)

- **95%+ ownership** (juridisch en economisch) required
- **Effect:** consolidated CIT return; intercompany transactions eliminated
- **Restrictions post-CJEU rulings:** per-element approach limits certain cross-border benefits
- Useful for: netting profits and losses across multiple project SPVs
- Both parties must be NL-resident or have NL permanent establishment

## Innovatiebox (Innovation Box, Art. 12b Wet VPB)

- **Effective rate:** 9% on qualifying profits from innovation
- **Vereisten:** WBSO-verklaring (R&D tax credit certificate) from RVO + qualifying intellectual property (self-developed intangible)
- Nexus approach: qualifying profit proportional to own R&D expenditure vs. total costs
- Relevant for: proprietary BESS software, DC cooling technology, energy management systems

## Dividendbelasting (Dividend Withholding Tax)

| Scenario | Rate | Basis |
|---|---|---|
| Standard BV/NV distribution | 15% | Art. 1 Wet DB |
| EU/EEA qualifying parent (>5% holding) | 0% (Parent-Subsidiary Directive) | Art. 4 Wet DB |
| Treaty-reduced rate | 0--10% depending on treaty | Applicable treaty |
| Conditional WHT to low-tax jurisdictions | 25.8% (since 2021) | Wet bronbelasting 2021 |
| Within fiscale eenheid | 0% (intercompany) | Art. 15 Wet VPB |
| Cooperatie U.A. to members | 0% | Art. 1 Wet DB |
| Inhoudingsvrijstelling (qualifying holding) | 0% | Art. 4 lid 2 Wet DB |

## Overdrachtsbelasting (Real Estate Transfer Tax, WBR)

| Scenario | Rate | Notes |
|---|---|---|
| Commercial property (niet-woning) | 10.4% | Art. 14 WBR, 2025 rate |
| Recht van opstal / erfpacht | 10.4% | Over de waarde van het recht |
| Share deal in vastgoedvennootschap | 10.4% | If >50% assets are NL real property held as belegging (Art. 4 WBR) |
| Woning (residential) | 2% (or 0% for starters <EUR 510K) | Not typically applicable to project finance |
| Reorganisatievrijstelling (Art. 5bis WBR) | 0% | Intragroup restructuring; conditions apply |

## BTW (Omzetbelasting / VAT)

| Scenario | Rate | Notes |
|---|---|---|
| Standard rate | 21% | Default for goods and services |
| Reduced rate | 9% | Food, hotels, cultural events, warmtelevering (heat supply) |
| Verleggingsregeling (reverse charge) | 0% supplier; buyer self-accounts | NL construction services (Art. 12 lid 4 Wet OB 1968) |
| Verhuur onroerend goed | Exempt | Optie belaste verhuur possible if >90% aftrekgerechtigd use by tenant |
| Import solar panels (residential) | 0% | Since 1 Jan 2023 |

## ATAD Implementation

### Interest Limitation (ATAD Art. 4)

Implemented via Art. 15b Wet VPB -- see earningsstripping above.

### CFC Rules (ATAD Art. 7--8)

- NL applies Model A (entity approach)
- Targets undistributed income of CFC in low-tax jurisdiction (<9% effective rate)
- Exemption if CFC has genuine economic activity (substance)

### Anti-Hybrid Rules (ATAD2)

- Wet implementatie ATAD 2 (eff. 1 Jan 2020/2022)
- Addresses deduction/no-inclusion mismatches, dual-residence mismatches, PE mismatches
- Reverse hybrid rule (Art. 2 lid 12 Wet VPB): certain transparent entities treated as opaque if >50% held by non-transparent entity in jurisdiction that treats hybrid as opaque

## Pillar Two (Global Minimum Tax)

- IIR (Income Inclusion Rule) and UTPR (Undertaxed Profits Rule): eff. 2024/2025
- Applies to groups with consolidated revenue > EUR 750M
- Minimum effective rate: 15%
- Wet minimumbelasting 2024 (Minimum Tax Act)
