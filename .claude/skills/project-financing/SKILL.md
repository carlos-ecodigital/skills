---
name: project-financing
description: >-
  Expert guidance on project financing for energy and digital infrastructure
  assets in the Netherlands. This skill should be used when the user asks about
  project finance structuring, SPV formation (BV/NV), non-recourse debt,
  capital structuring, DSCR/LLCR/PLCR debt sizing, AI factory financing,
  GPU compute facility investment, colocation data center financing,
  BESS (battery energy storage system) project finance, cable pooling, MLOEA,
  SDE++ subsidies, Dutch grid connection (netaansluiting), TenneT transportschaarste,
  DSO/netbeheerder (Liander/Stedin/Enexis), Omgevingswet permitting,
  recht van opstal, bestemmingsplan, omgevingsvergunning, KvK registration,
  UBO register, fiscal unity (fiscale eenheid), participation exemption
  (deelnemingsvrijstelling), innovation box (innovatiebox), Dutch WHT
  (dividendbelasting), InvestNL, NIA, EIB facilities, green bonds,
  sustainability-linked loans, Dutch pension fund infrastructure investment
  (APG/PGGM), EPC contracts, revenue stacking, energy arbitrage, FCR/aFRR
  ancillary services, waste heat recovery (warmteterugwinning), district heating
  (stadsverwarming), Wet collectieve warmtevoorziening (Wcw), EU ETS2,
  EU Battery Regulation 2023/1542, joint venture structuring, SHA terms,
  waterfall distributions, or any Netherlands-focused project finance question
  covering AI infrastructure, data centers, or battery storage assets.
version: "1.0.0"
---

# Projectfinanciering -- Nederland / Project Financing -- Netherlands

## Personality

See [identity.md](identity.md), [soul.md](soul.md), [principles.md](principles.md) for this agent's personality definition.

Provide authoritative, practical project finance guidance for energy and digital infrastructure assets in the Netherlands. All rates, thresholds, and regulatory references are current as of 2025/2026 and should be verified against primary sources before reliance. For authoritative source citations, see [references/sources-and-references.md](references/sources-and-references.md).

## Toepasselijke wetgeving / Primary Legislation

| Wet (Act) | Afkorting (Abbreviation) | Referentie (Reference) |
|---|---|---|
| Burgerlijk Wetboek (Civil Code) | BW | Boek 2 (Rechtspersonen), Boek 3 (Vermogensrecht), Boek 6 (Verbintenissen), Boek 7 (Bijzondere overeenkomsten) |
| Wet op het financieel toezicht (Financial Supervision Act) | Wft | Stb. 2006, 475 |
| Omgevingswet (Environment and Planning Act) | Ow | Stb. 2016, 156 (eff. 1 Jan 2024; replaces ~26 prior laws) |
| Energiewet (Energy Act) | -- | Eff. 1 Jan 2026 (replaces Elektriciteitswet 1998 + Gaswet) |
| Wet collectieve warmtevoorziening (Collective Heat Act) | Wcw | Adopted Eerste Kamer 9 Dec 2025; eff. mid-2026 to 1 Jan 2027 |
| Wet vennootschapsbelasting (Corporate Income Tax Act) | Wet Vpb | Stb. 1969, 445 |
| Wet dividendbelasting (Dividend WHT Act) | Wet DB | Stb. 1965, 621 |
| Handelsregisterwet (Trade Register Act) | Hrw | Stb. 2007, 153 |
| EU Battery Regulation | -- | Reg. 2023/1542 (battery passport eff. 2027) |
| EU AI Act | -- | Reg. 2024/1689 |

## Kernbegrippen projectfinanciering / Core PF Metrics Quick Reference

| Kengetal (Metric) | Definitie (Definition) | Typisch bereik (Typical Range) | Toelichting (Notes) |
|---|---|---|---|
| DSCR (Debt Service Coverage Ratio) | Netto kasstroom / schuldendienst (net cash flow / debt service) | 1.20x--1.40x senior | Minimum covenant level; lender sizing metric |
| LLCR (Loan Life Coverage Ratio) | NCW kasstromen over looptijd / uitstaande schuld (NPV cash flows over loan life / outstanding debt) | >1.20x | Primary lender sizing metric |
| PLCR (Project Life Coverage Ratio) | NCW kasstromen over projectlevensduur / uitstaande schuld | >1.30x | Tail risk comfort; longer horizon than LLCR |
| Hefboompercentage (Gearing / D:E) | Schuld / (Schuld + Eigen vermogen) | 50--80% | Varies by asset class and revenue certainty |
| Lock-up DSCR | Drempel waaronder uitkeringen geblokkeerd (threshold below which distributions blocked) | 1.10x--1.20x | Cash sweep trigger for equity distributions |
| Default DSCR | Drempel die ingrijprecht crediteur activeert (threshold triggering lender step-in) | 1.05x--1.10x | Event of default; triggers cure period |

## Vergelijking activaklassen / Asset Class Comparison

| Parameter | AI Factories | Colocation DC | BESS |
|---|---|---|---|
| Typische CAPEX (NL) | EUR 10--15M/MW excl. GPUs; up to EUR 40M/MW incl. GPUs [Turner & Townsend DCCI 2025-2026] | EUR 8--12M/MW [T&T DCCI: Amsterdam US$10.8/W] | EUR 330--700K/MW (2--4hr LFP) [BNEF 2025: global avg $117/kWh; Europe ~$177/kWh] |
| Hefboompercentage (gearing) | 50--65% | 65--75% (gecontracteerd / contracted) | 70--80% (gecontracteerd); 40--60% (merchant) [ESS News BBDF 2025] |
| Inkomstenmodel (revenue) | GPUaaS ($1.49--4.00/GPU-hr H100) [GMI Cloud 2025]; training/inference contracts | Colocation ~$217/kW/month wholesale [CBRE Q1 2025]; interconnection | Arbitrage (EPEX SPOT NL spread 83--121 EUR/MWh [Synertics 2025]); FCR (~EUR 13/MW/h [Rabobank 2023]); aFRR |
| EV/EBITDA multiple | 25--30x (platform); emerging | 19--26x (publieke REITs) [Equinix ~26.6x LTM; Alantra 2024: 13--25x private M&A] | N.v.t. -- omzetgebaseerd (N/A -- revenue-based) |
| NL-specifiek | Moratorium >70MW/>100K sqm; EU AI Gigafactory program (EUR 20B) [EIB] | Amsterdam ban tot 2030 [NL Times Apr 2025]; NH strategie; leegstand 5% [C&W 2025] | Energiewet cable pooling; SDE++ EUR 100M BESS [PV Magazine]; TenneT 6 GW TDTR |
| Bouwperiode (construction) | 18--30 maanden | 18--36 maanden | 6--12 maanden |
| Referentiebestand (reference file) | [references/ai-factories.md](references/ai-factories.md) | [references/colocation-data-centers.md](references/colocation-data-centers.md) | [references/bess-projects.md](references/bess-projects.md) |

## Nederlandse SPV-structuren / Dutch SPV Structures -- Overzicht

- **Besloten Vennootschap (BV):** Standard SPV vehicle for Dutch project finance. Flex-BV since 1 Oct 2012; minimum kapitaal (capital) EUR 0.01; oprichtingskosten (incorporation cost) EUR 500--1,500 notaris + EUR 82.25 KvK [Firm24/KvK.nl]. Notariele akte van oprichting (notarial deed) required. UBO-registratie verplicht (mandatory); public access restricted since 15 Jul 2025 (CJEU privacy ruling) [Projective Group]. Fiscale eenheid (fiscal unity) possible with 95%+ ownership.
- **Naamloze Vennootschap (NV):** Used for listed/larger structures. Minimum kapitaal EUR 45,000; accountantsverklaring required for inbreng in natura (contribution in kind).
- **Commanditaire Vennootschap (CV):** Tax-transparent; beherende vennoot (GP) / commanditaire vennoot (LP). Used in fund structures.
- **Stichting (Foundation):** Used as orphan entity (stichting administratiekantoor) for structured finance. No shareholders; governance by bestuur (board) only. Creates bankruptcy remoteness for lender security packages.
- **Cooperatie U.A.:** Flexible profit distribution; no dividendbelasting on distributions to members. Used in certain fund and JV structures.

For full Dutch legal framework, SPV formation procedures, and BW provisions, see [references/netherlands-legal-framework.md](references/netherlands-legal-framework.md).

## Belastingen / Tax Overview for Project SPVs

| Belastingtype (Tax Type) | Tarief 2025/2026 (Rate) | Bron (Source) |
|---|---|---|
| Vennootschapsbelasting (CIT) | 19% (eerste EUR 200K) / 25.8% | Wet Vpb; verified PwC/Rabobank/AAFF |
| Earningsstripping (renteaftrekbeperking) | 24.5% of fiscal EBITDA (EUR 1M franchise) | Increased from 20% per 1 Jan 2025 [PwC Belastingplan 2025] |
| Dividendbelasting (Dividend WHT) | 15% standard; 25.8% conditional WHT (low-tax jurisdictions, since 2021) | Wet DB; PwC Tax Summaries |
| Deelnemingsvrijstelling (Participation exemption) | 0% on qualifying holdings (5%+) | Wet Vpb Art. 13 |
| Innovatiebox (Innovation box) | 9% effective rate on qualifying IP income | Business.gov.nl |
| Overdrachtsbelasting (Real estate transfer tax) | 10.4% commercial property | Unchanged 2025/2026 |
| BTW (VAT) | 21% standard; 9% reduced (incl. warmtelevering / heat supply) | Wet OB |
| Verliesverrekening (Loss carry-forward) | Unlimited forward (capped EUR 1M + 50% excess); 1 year back | Wet Vpb |

For complete tax structuring details and treaty network, see [references/netherlands-legal-framework.md](references/netherlands-legal-framework.md).

## Financiering / Financing Instruments -- Overzicht

- **Senior secured non-recourse debt:** EURIBOR + 200--250 bps average (range 40--600 bps) [AEW 2025]; IG infra debt total return ~4.25--4.75% EUR [Aviva Investors 2026]; 3-month EURIBOR ~1.89% [euribor-rates.eu]
- **Green bonds / Sustainability-linked loans:** NL Green DSLs outstanding ~EUR 27B [DSTA]; greenium effectively ~1 bp in EUR market [ABN AMRO Research]; EU Green Bond Standard: EUR 22B issued in first year
- **Invest-NL:** EUR 1.145B cumulative across 89 investments; mobilized EUR 3.2B private capital; additional EUR 900M government funding at Prinsjesdag; focus: energy transition, deeptech [Invest-NL Annual Report 2024]
- **EIB:** EUR 100B 2025 ceiling; >EUR 11B for power grids + storage; AI Gigafactories EUR 20B target (~5 facilities); TechEU EUR 70B (2025--2027) [EIB]
- **Nederlandse pensioenfondsen (Pension funds):** APG/ABP (EUR 552B AUM) target 10% infra allocation by 2030 [IPE]; PGGM/PFZW (EUR 251B AUM) EUR 15B infra portfolio; EUR 19M in Sympower BESS [PGGM]; PMT/PME EUR 2.5B infrastructure debt [IPE Real Assets]
- **Nederlandse verzekeraars (Insurers):** a.s.r. invested in Project Pollux (NL BESS); NN Group EUR 300M Rivage fund + EUR 350M Macquarie partnership [NN Group]; Aegon AM Renewable Infrastructure Debt (Article 9 SFDR) [Aegon AM]

For full debt instrument details, see [references/debt-instruments.md](references/debt-instruments.md).
For equity structures, see [references/equity-structures.md](references/equity-structures.md).
For shared equity structure summaries used across skills, see `_shared/equity-structures.md`.
For institutional investor landscape data, see `_shared/investor-landscape.md`.

## Vergunningen en net / Permitting and Grid -- Overzicht

- **Omgevingswet (eff. 1 Jan 2024):** Replaces ~26 prior laws (Wro, Wabo, Wet milieubeheer). Framework: omgevingsvisie -- omgevingsplan -- omgevingsvergunning. Applications via DSO (Digitaal Stelsel Omgevingswet).
- **Amsterdam:** ALL new DCs/expansions banned until at least 2030 [NL Times Apr 2025]. Microsoft/Pure DC 78 MW controversy: circumvented via 3 separate permits [NL Times Jan 2026].
- **Nationaal:** Hyperscale ban >70 MW AND >100,000 sqm except Het Hogeland and Hollands Kroon [CMS LawNow].
- **Noord-Holland provinciale strategie:** DCs >2,000 m2 / >5 MVA restricted to designated industrial zones in Amsterdam, Haarlemmermeer, Hollands Kroon [NH Datacenterstrategie 2025--2027].
- **TenneT transportschaarste (grid congestion):** ~60 GW battery storage in connection queue vs ~20 GW peak demand; average wait up to 10 years in congested areas [TenneT]; 6 GW TDTR capacity granted (85%+ hour availability) [PV Magazine Oct 2025]; over 12,000 companies waiting [Taylor Wessing].
- **Energiewet (eff. 1 Jan 2026):** Expands cable pooling to all installation types; minimum 100 kVA (was 2 MVA); up to 4 parties per connection; BESS/electrolysers explicitly included [QGM Law]. ACM granting anticipatory approval [ACM.nl].
- **BESS als nutsvoorziening:** Rechtbank Midden-Nederland ruled (24 Apr 2025) BESS can be classified as utility, potentially exempting from zoning restrictions [NewGroundLaw].
- **Stikstof (Nitrogen):** AERIUS Calculator 2025 mandatory for projects near Natura 2000 [RIVM]; threshold >0.005 mol/ha; bouwvrijstelling abolished; intern salderen no longer permit-free (Dec court ruling) [Bouwend Nederland].
- **Wcw (Collective Heat Act):** Municipalities get regierol; designated heat companies >50% publicly owned (7-year transition); cost-based tariff replaces gas-price-linked; existing networks 14--30 year transition [VNG Jul 2025; Dirkzwager Dec 2025].

For complete permitting pathways, see [references/colocation-data-centers.md](references/colocation-data-centers.md) and [references/bess-projects.md](references/bess-projects.md).

## Risicokader / Risk Framework -- Overzicht

Key risk categories for Dutch infrastructure project finance: construction risk (EPC; UAV 2012 / UAV-GC 2025 / FIDIC), technology risk (per asset class), revenue/market risk, regulatory/political risk (Omgevingswet, moratorium, Energiewet, stikstof), force majeure (overmacht Art. 6:75 BW -- note: transportschaarste is foreseeable in NL and should be addressed contractually [Taylor Wessing/CMS]), insurance (CAR/EAR, operational PAR/ISR, BESS-specific fire/thermal; key players: Marsh, GCube/TMGX, Solarif), and environmental/permitting risk (MER, bezwaar/beroep, bodemverontreiniging).

For complete risk allocation framework, see [references/risk-allocation.md](references/risk-allocation.md).

## Financiele modellering / Financial Modeling -- Overzicht

Standard project finance model architecture. Key model audit firms active in NL: Forvis Mazars (Corality), Operis, BDO, Gridlines. Debt sizing via DSCR, LLCR, PLCR. Dutch tax modeling requires attention to: earningsstripping at 24.5% (not 20%), fiscale eenheid, innovatiebox, verliesverrekening.

For model structure, inputs, and methodologies, see [references/financial-modeling.md](references/financial-modeling.md).

## Due Diligence

For comprehensive Dutch project finance DD checklists (corporate, project agreements, permits, technical, financial, environmental, insurance, Dutch-specific items), see [references/due-diligence-checklist.md](references/due-diligence-checklist.md).

## Toezichthouders en instellingen / Key Authorities

| Instantie (Authority) | Rol (Role) |
|---|---|
| AFM (Autoriteit Financiele Markten) | Financial markets supervision; fund regulation; prospectus requirements |
| DNB (De Nederlandsche Bank) | Prudential supervision; banking licenses |
| ACM (Autoriteit Consument & Markt) | Competition; energy market regulation; heat tariffs; cable pooling approval |
| RVO (Rijksdienst voor Ondernemend Nederland) | SDE++ administration; energy permits; subsidies; EIA/KIA |
| TenneT | TSO (Transmission System Operator); grid connection >10 MW; ancillary services procurement (FCR/aFRR/mFRR) |
| Liander / Stedin / Enexis | Regional DSOs (Distribution System Operators) |
| KvK (Kamer van Koophandel) | Commercial register; company registration; UBO register |
| Kadaster | Land registry; recht van opstal registration; hypotheek registration |
| ILT (Inspectie Leefomgeving en Transport) | Environmental enforcement |
| PBL (Planbureau voor de Leefomgeving) | Energy transition analysis; policy advice |
| Invest-NL | National development bank; equity/mezzanine/guarantees for energy transition and digitalization |

## Referentiemateriaal / Authoritative Sources

Core textbooks: Yescombe, *Principles of Project Finance* (2nd ed., Elsevier, 2013); Gatti, *Project Finance in Theory and Practice* (4th ed., Academic Press, 2024); Hoffman, *The Law and Business of International Project Finance* (3rd ed., Cambridge UP, 2007). Key Dutch market reports: DDA *State of the Dutch Data Centers 2025*; CBRE NL Market Outlook 2025; Rabobank Dutch Electricity Sector series (6 parts); BNEF ESS Cost Survey 2025.

For the complete bibliography with source citations, see [references/sources-and-references.md](references/sources-and-references.md).

## Investment Case Intake Integration

This skill receives structured input data from the **modular intake system** (`_shared/intake-modules/`), specifically:

| Intake Module | File | Data Received | PF Output |
|---|---|---|---|
| M4: BESS Technical | [m4-bess-technical.md](../../_shared/intake-modules/m4-bess-technical.md) | Degradation curves, cycling strategy, BMS/EMS, fire safety, grid code (45 Qs) | BESS bankability assessment, technology risk quantification |
| M5: DC/AI Technical | [m5-dc-ai-technical.md](../../_shared/intake-modules/m5-dc-ai-technical.md) | Power density, cooling, SLA, GPU refresh, moratorium compliance (50 Qs) | DC bankability assessment, SLA credit analysis |
| M6: Sites & Assets | [m6-sites-assets.md](../../_shared/intake-modules/m6-sites-assets.md) | Per-site details, grid connection, permits, land agreements (22 Qs/site) | Site-level feasibility, construction timeline |
| M7: Revenue & Debt | [m7-revenue-debt.md](../../_shared/intake-modules/m7-revenue-debt.md) | Revenue stacking, pricing, contracted vs. merchant, covenants, cash waterfall, security, insurance (55 Qs) | Revenue certainty assessment, debt sizing, DSCR sensitivity, covenant compliance |
| M1: Entity & Tax | [m1-entity-tax.md](../../_shared/intake-modules/m1-entity-tax.md) | SPV structure, tax structuring, earningsstripping (37 Qs) | SPV structure validation, tax modeling |

**Track-aware loading:** When the intake router (`_shared/intake-modules/intake-router.md`) selects "Project Finance" track, M4-M7 load at full depth. M1 is always full. M2 (Founder/Team) loads only 4 sponsor-credibility questions. M8 (Equity/Capital) loads only 4 questions. See the router's module loading matrix for complete track logic.

### Producing IM-Ready Outputs

When `seed-fundraising` Mode C triggers IM production, this skill produces:

1. **IM Section 10.1-10.5** (Project-Level Financials):
   - 10.1 Platform P&L (consolidated)
   - 10.2 Per-site unit economics (site-level DCF)
   - 10.3 Financial model audit status
   - 10.4 Debt sizing and DSCR analysis (incorporating earningsstripping from M1 S2)
   - 10.5 Breakeven analysis

2. **IM Section 12A** (Capital Structure & Financing Strategy):
   - Debt evolution across project lifecycle
   - Gearing trajectory
   - Cash waterfall specification

3. **IM Appendix G** (Asset Portfolio Summary): Per-site one-pager with key metrics from M6
4. **IM Appendix K** (Bankability Checklist): 8-category assessment per `due-diligence-checklist.md` Section 9

**Data room output:** Financial models go to `ops-dataroomops` folders 03a_Platform_Model, 03b_Project_Models, 03c_Debt_Sizing.

---

## Gerelateerde vaardigheden / Related Skills

| Skill | Use When |
|---|---|
| `seed-fundraising` | Seed-round fundraising: pitch decks, executive summaries, investment memos, investor targeting, cap table, financial projections. **Bidirectional: seed-fundraising Mode C loads `_shared/intake-modules/` → this skill reads M1, M4-M7 intake data → produces IM project finance sections.** |
| `_shared/equity-structures.md` | Consolidated equity structuring reference (BV + AG) used by both PF and fundraising |
| `_shared/investor-landscape.md` | Investor database: sector-focused VCs, infrastructure funds, pension funds, sovereigns |
| `_shared/market-data.md` | Sector benchmarks, cost curves, comparable transactions, regulatory landscape |
| `legal-counsel` | Contract drafting, SHA, SPA, corporate/M&A, multi-jurisdictional legal advice |
| `drafting-service-agreements` | Service agreements, EPC contracts, O&M agreements |
| `netherlands-permitting` | Omgevingswet, DC permitting, BESS safety (PGS 37), grid connection, MER |
| `de-brand-bible` | Brand voice, messaging pillars, buyer personas for Digital Energy external materials |

## Belangrijke disclaimers / Important Disclaimers

- All rates, thresholds, and regulatory references are based on 2025/2026 legislation (Belastingplan 2025/2026, Energiewet, Omgevingswet, Wcw) as adopted. Verify current rates at belastingdienst.nl, rvo.nl, and tennet.eu.
- Market metrics (CAPEX, revenue, multiples, spreads) are sourced from published reports and are indicative. Obtain independent valuations and market quotes for transaction-specific pricing.
- This skill does not constitute juridisch advies (legal advice), belastingadvies (tax advice), or beleggingsadvies (investment advice). Consult qualified Dutch legal, tax, and financial advisers for specific transactions.
- Dutch infrastructure regulation changes frequently through parliamentary processes, ministerial decrees, and case law. Review and update this skill after significant legislative or market developments.
- Landmark transaction references (Project Mufasa, Leopard, etc.) are for benchmarking purposes; terms of individual transactions vary.
