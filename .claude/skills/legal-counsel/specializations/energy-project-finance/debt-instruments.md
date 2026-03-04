# Schuldfinanciering / Debt Instruments for Dutch Infrastructure Project Finance

> Reference file for Claude Code skill on Dutch project financing.
> Bilingual Dutch/English. All data sourced with [Source] tags.
> Last updated: February 2026

---

## 1. Overzicht / Overview

### 1.1 Kernprincipe / Core Principle

Non-recourse and limited-recourse project finance debt for Netherlands infrastructure
projects (BESS, data centres, AI factories). The fundamental principle: lenders look to
**project cash flows and assets** as their primary source of repayment and security,
**NOT** to sponsor balance sheets.

The Special Purpose Vehicle (SPV / Projectvennootschap) is the borrowing entity. All
debt is ring-fenced within the SPV. Sponsors provide equity and, in some cases,
limited completion support but are otherwise shielded from project-level debt
obligations post-completion.

### 1.2 Debt Structuring Principles

- **Cash flow waterfall**: all project revenues flow through a single controlled
  account structure; debt service is senior to distributions
- **Sculpted repayment**: principal repayment profiles are shaped to match projected
  cash flows, maintaining target DSCR throughout the debt tenor
- **Security package**: comprehensive first-priority security over all SPV assets,
  shares, accounts, contracts, insurance proceeds, and permits
- **Covenant framework**: financial, information, and restrictive covenants provide
  lender oversight and control triggers
- **Reserve accounts**: Debt Service Reserve Account (DSRA), Maintenance Reserve
  Account (MRA), and other reserves sized to project risk profile

### 1.3 Scope of This Reference

This document covers:
- Senior secured term loans, construction facilities, and revolving credit
- Market pricing and reference rates (EURIBOR, swaps, margins)
- Dutch bank and multilateral lender landscape
- Green bonds and sustainability-linked instruments
- Security package under Dutch law (zekerhedenstructuur)
- Loan covenants and conditions
- Refinancing considerations

---

## 2. Senior Secured Debt

### 2.1 Term Loan Facilities — Indicative Parameters

The table below summarises typical term loan parameters for the four primary asset
classes in Dutch infrastructure project finance. Parameters are indicative and vary
by project quality, sponsor, market conditions, and contracted vs. merchant exposure.

| Parameter | BESS (Contracted) | BESS (Merchant) | Colocation DC | AI Factory |
|---|---|---|---|---|
| **Gearing (D/D+E)** | 70–80% | 40–60% | 65–75% | 50–65% |
| **Tenor** | 10–15 years | 5–7 years | 7–15 years | 5–7 years |
| **Margin** | EURIBOR + 200–300 bps | EURIBOR + 300–400 bps | EURIBOR + 175–250 bps | EURIBOR + 250–400 bps |
| **Min DSCR** | 1.25x | 1.35–1.50x | 1.20–1.30x | 1.30x+ |
| **Lock-up DSCR** | 1.10–1.15x | 1.15–1.20x | 1.10–1.15x | 1.15–1.20x |
| **Default DSCR** | 1.05x | 1.05–1.10x | 1.05x | 1.05–1.10x |
| **Repayment Profile** | Sculpted to cash flow | Sculpted, faster amort | Sculpted / annuity | Sculpted, faster amort |
| **Commitment Fee** | 40–50% of margin | 40–50% of margin | 40–50% of margin | 40–50% of margin |
| **Typical Size** | EUR 50–350M | EUR 30–150M | EUR 100–500M+ | EUR 200–1,000M+ |
| **Currency** | EUR | EUR | EUR | EUR |

[Source: Market observation; Dentons Project Mufasa advisory; InfraVia Project Leopard; AEW infrastructure debt research 2025]

**Key distinctions by asset class:**

- **BESS (Contracted)**: Long-term tolling or capacity agreements provide revenue
  certainty; lenders comfortable with higher gearing and longer tenors. SDE++
  allocations further de-risk cash flow (see Section 5.4).
- **BESS (Merchant)**: Significant revenue uncertainty from trading exposure; lenders
  require lower gearing, shorter tenors, faster amortisation, and higher DSCR
  cushions. Cash sweep mechanisms are standard.
- **Colocation DC**: Blue-chip tenant base (hyperscalers) with long leases (10–15
  years) provides contracted cash flow. Lenders view favourably; terms approach
  investment-grade real estate finance. PUE and sustainability KPIs increasingly
  included.
- **AI Factory**: Nascent asset class with limited track record. Higher technology
  risk, customer concentration, and rapid obsolescence risk drive conservative
  structuring. Lender appetite growing but selective.

### 2.2 Construction Facilities

Construction-phase debt is a critical component of project finance for greenfield
developments. The facility funds CAPEX from financial close through to commercial
operation date (COD / Inbedrijfstelling).

**Structure:**
- **Delayed draw term loan**: drawn in tranches against verified construction
  milestones (mijlpalen)
- **Independent Engineer (IE)**: certification required for each drawdown; IE
  confirms milestone completion, budget tracking, and schedule adherence
- **Construction contingency**: 5–10% of total CAPEX held in reserve for cost
  overruns; drawn only with IE and lender approval
- **IDC (Interest During Construction)**: interest accrued during construction is
  capitalised into the loan balance; no cash debt service until COD
- **Conversion mechanism**: construction facility converts to term loan at COD upon
  satisfaction of completion conditions (completion tests, final IE report,
  insurance confirmation, permit confirmation)

**Lender Requirements for Construction Drawdown:**
- Executed EPC contract with wrap (fixed price, fixed date, performance guarantees)
- Sponsor completion guarantee or equity bridge until COD
- Delay in Start-Up (DSU) / Advanced Loss of Profits (ALOP) insurance
- Construction All Risks (CAR) insurance
- Builder's lien waiver or subordination arrangements
- Grid connection agreement executed (or firm timeline with TenneT/DSO)
- All material permits in place (omgevingsvergunning, Rijksinpassingsplan if applicable)

**Construction Period Monitoring:**

| Reporting | Frequency | Content |
|---|---|---|
| IE progress report | Monthly | Physical progress, budget, schedule, risks |
| Drawdown certificate | Per drawdown | Milestone confirmation, cost breakdown |
| Insurance certificate | Quarterly | Coverage confirmation, premium payment |
| Permit status | Quarterly | Status of all required permits |
| Change order log | As required | Any EPC contract modifications |

[Source: Standard NL project finance practice; Allen & Overy project finance guides]

### 2.3 Revolving Credit Facilities (RCF)

Revolving credit facilities complement the term loan to address short-term liquidity
needs of the project SPV.

**Types:**
- **Working capital RCF**: 6–12 month facility for operational cash flow timing
  mismatches (e.g., quarterly revenue receipts vs. monthly operating costs)
- **DSRA letter of credit alternative**: standby L/C issued by relationship bank to
  fund DSRA, freeing cash for other purposes; typically cheaper than cash-funded
  reserve
- **Maintenance capex facility**: for periodic major maintenance expenditures

**Key Terms:**
- Typically **pari passu** (gelijkwaardig) with the term loan in security ranking
- Margin: in line with term loan margin or slightly lower
- Commitment fee: 35–50% of margin on undrawn amounts
- Clean-down period: typically required annually (facility fully repaid for 5–10
  consecutive business days)
- Subject to same financial covenant framework as term loan

---

## 3. Market Pricing and Reference Rates

### 3.1 Reference Rates — Current Indicative Levels

| Rate / Benchmark | Current Level | Notes | Source |
|---|---|---|---|
| 3-month EURIBOR | ~1.89% | As of early 2026 | [euribor-rates.eu] |
| 6-month EURIBOR | ~1.91% | Interbank benchmark | [euribor-rates.eu] |
| 12-month EURIBOR | ~1.92% | Most common PF reference | [euribor-rates.eu] |
| 5-year EUR mid-swap | ~2.30% | Swap rate for hedging | [Market data] |
| 10-year EUR mid-swap | ~2.55% | Longer-tenor hedging | [Market data] |
| ECB deposit facility rate | 2.75% | Policy rate | [ECB] |
| Infrastructure average margin | 200–250 bps | Range 40–600 bps depending on risk | [AEW Research 2025] |
| IG infrastructure debt total return (EUR) | 4.25–4.75% | Target for institutional investors | [Aviva Investors 2026] |
| Greenium (EUR market) | ~1 bp | Effectively vanished | [ABN AMRO Research] |
| Dutch 10-year government bond | ~2.65% | Risk-free benchmark | [DSTA / Market] |

**Note:** Rates are indicative and subject to daily market movement. Project-specific
all-in cost of debt = reference rate + credit margin + hedging cost + fees.

### 3.2 All-In Cost of Debt Illustration

| Component | BESS (Contracted) | Colocation DC | AI Factory |
|---|---|---|---|
| Reference rate (EURIBOR) | ~1.90% | ~1.90% | ~1.90% |
| Credit margin | +2.50% | +2.00% | +3.25% |
| Swap cost (indicative) | +0.40% | +0.40% | +0.40% |
| Upfront fees (amortised) | +0.15% | +0.15% | +0.20% |
| **Indicative all-in fixed** | **~4.95%** | **~4.45%** | **~5.75%** |

[Source: Author calculation based on market data, February 2026]

### 3.3 Interest Rate Hedging (Renterisicoafdekking)

Interest rate hedging is **mandatory** in virtually all project finance facilities.
Lenders require borrowers to hedge a substantial portion of floating-rate exposure.

**Hedging Requirements:**

| Parameter | Typical Requirement |
|---|---|
| Hedge ratio | 75–100% of outstanding debt |
| Instrument | Interest rate swap (IRS) |
| Tenor | Match to debt tenor, minimum 5–7 years |
| Counterparty | Facility lender or approved bank (min rating A-/A3) |
| Timing | Execute within 30–90 days of financial close |
| Documentation | ISDA Master Agreement + Schedule + CSA |

**Hedging Considerations:**
- **Pre-hedging risk**: manage exposure between signing and first drawdown; forward-
  starting swaps or swaptions may be used
- **Basis risk**: mismatch between hedge reference rate and loan reference rate
  (e.g., 3-month EURIBOR vs. 6-month EURIBOR)
- **Break costs**: significant on early termination; size into financial model
- **Dutch pension fund / insurer alternatives**: fixed-rate lending by institutional
  investors eliminates hedging need; increasingly common for long-dated infrastructure
  debt (see Section 5.3 on NIA)
- **Hedge accounting**: IFRS 9 / NL GAAP hedge accounting to avoid P&L volatility

---

## 4. Nederlandse Banken / Dutch Banks Active in Infrastructure

### 4.1 Major Dutch Lenders

| Bank | Infrastructure Focus | AuM / Lending Volume | Notable Transactions | Source |
|---|---|---|---|---|
| **ABN AMRO** | Digital infrastructure, energy, sustainable | EUR 4.8B digital infra lending (5th largest European bank) | Acquired NIBC (infra lending expertise); BESS deals | [ION Analytics] |
| **Rabobank** | Agricultural infrastructure, energy transition | Major NL cooperative bank | Multi-bank BESS syndications; wind/solar PF | [Rabobank annual report] |
| **ING** | Energy transition, digital infra, global PF | Top-10 global PF bank | Project Mufasa lender; extensive DC financing | [ING / IJGlobal] |
| **Triodos Bank** | Sustainable / impact finance | EUR 6B+ balance sheet | BESS, renewable energy, community projects | [Triodos Annual Report] |
| **BNG Bank** | Public sector, municipal infrastructure | EUR 130B+ balance sheet | PPP projects, social housing, public infra | [BNG Bank] |
| **NWB Bank** | Water boards (waterschappen), public infra | EUR 100B+ balance sheet | Green bond issuer; water infrastructure | [NWB Bank] |
| **NIBC** (now ABN AMRO) | Infrastructure, real estate, shipping | Integrated into ABN AMRO | Historical DC and energy PF expertise | [ION Analytics] |
| **de Volksbank** | Limited PF activity | — | Indirect via green bond investments | — |

### 4.2 Multi-Bank Deal Examples (BESS)

| Project | Size | Lenders | Structure | Source |
|---|---|---|---|---|
| **Project Mufasa** | EUR 350M | 6 lenders (incl. ING, ABN AMRO) | Senior secured term + RCF | [Dentons] |
| **Project Leopard** | EUR 300M | 8 lenders | Senior secured, multi-tranche | [InfraVia] |
| **GIGA Storage Borssele** | EUR 100M+ (est.) | Dutch bank club + EIB (est.) | Construction + term | [Market intelligence] |

### 4.3 International Banks Active in NL Infrastructure

| Bank | Focus | Notable |
|---|---|---|
| **Societe Generale** | Energy, infrastructure PF | Active in NL BESS deals |
| **MUFG** | Global PF, digital infra | DC financing |
| **Sumitomo Mitsui (SMBC)** | Infrastructure, energy | NL market presence |
| **NatWest** | Infrastructure, renewables | NL deals via London desk |
| **KfW IPEX** | German export / infrastructure | Cross-border NL/DE projects |
| **Kommunalkredit** | Infrastructure specialist | BESS, renewable, digital |

---

## 5. Multilaterale en Publieke Financiering / Multilateral and Public Finance

### 5.1 Invest-NL

Invest-NL is the Dutch national promotional institution (nationale
investeringsinstelling), established in 2020 to mobilise private capital for
transitions that the market alone will not finance at sufficient scale.

| Parameter | Detail | Source |
|---|---|---|
| **Cumulative investments** | EUR 1.145B across 89 investments | [Invest-NL Annual Report 2024] |
| **Private capital mobilised** | EUR 3.2B alongside Invest-NL capital | [Invest-NL Annual Report 2024] |
| **Additional government funding** | EUR 900M announced (Prinsjesdag 2024) | [Rijksoverheid / Prinsjesdag] |
| **Products** | Equity, mezzanine, guarantees, co-investment | [Invest-NL] |
| **Focus areas** | Energy transition, deeptech, digitalization | [Invest-NL] |

**Portfolio Examples Relevant to Infrastructure:**
- **iwell**: energy storage / battery management (equity investment)
- **Battolyser**: hydrogen electrolysis / storage technology
- **Various BESS projects**: co-investment alongside institutional capital
- **Deep-tech**: AI infrastructure enabling technologies

**How Invest-NL Participates in Project Finance:**
- Mezzanine or subordinated debt tranches behind senior bank debt
- Equity co-investment alongside sponsors
- Guarantees to improve senior debt bankability
- First-loss positions to crowd in private lenders

### 5.2 EIB (European Investment Bank / Europese Investeringsbank)

The EIB is the largest multilateral lender for European infrastructure. Its 2025–2027
strategy substantially increases commitments to energy, digital, and AI infrastructure.

| Programme / Target | Amount | Detail | Source |
|---|---|---|---|
| **2025 lending ceiling** | EUR 100B (record) | Highest in EIB history | [EIB] |
| **Power grids + storage** | >EUR 11B | Dedicated allocation | [EIB press release 2025] |
| **AI Gigafactories** | EUR 20B target | ~5 large-scale AI facilities across EU | [EIB / EC joint initiative] |
| **TechEU** | EUR 70B (2025–2027) | Broadest digital/tech umbrella | [EIB] |
| **OVHcloud** | EUR 200M | Landmark cloud DC financing | [EIB / OVHcloud] |
| **InvestEU guarantee** | EUR 26.2B budget | Backs EIB risk-taking | [EC / InvestEU] |

**EIB Relevance for Dutch Projects:**
- Can provide up to 50% of project cost (typically 25–35% in practice)
- Pricing: typically tighter than commercial bank debt (AAA-rated institution)
- Tenor: up to 20–30 years (longer than commercial banks)
- BESS and DC projects eligible under Climate and Digital mandates
- Due diligence: extensive environmental and social review (E&S standards)
- Procurement: EIB procurement guidelines apply to co-financed projects

### 5.3 NIA (Nationale Investeringsinstelling) / NII (National Investment Institution)

The NIA was established to bridge the gap between Dutch institutional capital
(pensioenfondsen, verzekeraars) and infrastructure investment opportunities.

**Key Role:**
- Mobilise institutional capital (pension funds, insurers) for Dutch infrastructure
- Bridge between long-term liability-matching needs of institutions and project
  developers seeking long-dated fixed-rate debt
- Pool smaller projects into investable ticket sizes
- Provide standardised due diligence and documentation frameworks

**Institutional Investors Active in NL Infrastructure Debt:**

| Investor Type | Examples | Typical Allocation |
|---|---|---|
| Pension funds (pensioenfondsen) | ABP, PFZW, PME, PMT, bpfBOUW | 2–8% of AuM to infrastructure |
| Insurance companies (verzekeraars) | Aegon, NN Group, ASR, Achmea | Infrastructure debt allocation |
| Asset managers | PGGM, APG, MN, Cardano | Manage infra debt mandates |

**Institutional Debt Characteristics:**
- Fixed rate (no hedging required)
- Long tenor: 15–30 years
- Private placement / bilateral
- Investment-grade equivalent credit quality required
- Documentation: lighter than bank facilities but robust covenants
- Minimum ticket size: EUR 25–50M+

### 5.4 SDE++ als Bankable Kasstroom / SDE++ as Bankable Cash Flow

The Stimulering Duurzame Energieproductie en Klimaattransitie (SDE++) subsidy scheme
is a critical cash flow component for lenders in renewable energy and storage projects.

**Mechanism:**
- **Basisbedrag** (base amount) minus **correctiebedrag** (correction amount) =
  operating subsidy per unit of output
- Subsidy tenor: 12–15 years depending on technology category
- Indexed to market reference prices (electricity, gas)
- Provides a revenue floor when market prices are below basisbedrag

**Bankability of SDE++:**
- Lenders treat SDE++ as **quasi-contracted revenue** providing a floor under cash flows
- SDE++ approval letter is a condition precedent to financial close
- Assignment of SDE++ proceeds to security agent is standard
- Lenders model both SDE++ and merchant scenarios

**BESS-Specific SDE++ Allocation:**
- Separate EUR 100M BESS allocation within SDE++ framework
  [Source: PV Magazine Netherlands]
- Technology-specific basisbedrag for battery storage systems
- Lenders increasingly familiar with SDE++ for BESS (beyond traditional wind/solar)

### 5.5 Other Public Financing Instruments

| Instrument | Provider | Relevance | Source |
|---|---|---|---|
| **DEI+ (Demonstratie Energie- en Klimaatinnovatie)** | RVO | Innovation subsidy for first-of-a-kind | [RVO] |
| **MOOI (Missiegedreven Onderzoek, Ontwikkeling en Innovatie)** | RVO | R&D collaboration subsidy | [RVO] |
| **Groeifonds (Nationaal Groeifonds)** | Ministry of Finance | Large-scale infrastructure investment | [Rijksoverheid] |
| **WBSO** | RVO | R&D wage tax credit | [RVO] |
| **EIA (Energie-Investeringsaftrek)** | Belastingdienst | Energy investment tax deduction | [RVO] |
| **MIA/VAMIL** | Belastingdienst | Environmental investment deductions | [RVO] |
| **Connecting Europe Facility (CEF)** | European Commission | Cross-border infrastructure | [EC] |

---

## 6. Green Bonds and Sustainability-Linked Loans

### 6.1 Dutch Green Bond Market (Groene Obligaties)

The Netherlands is one of the most active sovereign green bond issuers globally, and
the corporate/project green bond market is well-developed.

| Metric | Value | Source |
|---|---|---|
| **NL sovereign Green DSLs outstanding** | ~EUR 27B | [DSTA (Dutch State Treasury Agency)] |
| **Latest issuance** | 20-year EUR 4.98B Green DSL | [DSTA] |
| **EU Green Bond Standard (EU GBS)** | EUR 22B issued in first year market-wide | [EC / Market data] |
| **NL corporate green bond issuers** | TenneT, Alliander, NWB Bank, BNG Bank, others | [Market data] |

**Relevance for Project Finance:**
- Large BESS, DC, or AI factory projects may issue project bonds (green-labelled)
  in the capital markets as an alternative or complement to bank debt
- Minimum issuance size for public green bond: typically EUR 250M+
- Private placement green bonds: smaller ticket sizes possible (EUR 50M+)
- Green bond framework required: alignment with ICMA Green Bond Principles or
  EU Green Bond Standard
- Use of proceeds: clearly defined eligible green expenditures

### 6.2 Sustainability-Linked Loans (SLLs / Duurzaamheidsgekoppelde Leningen)

SLLs tie the loan margin to achievement of pre-agreed sustainability Key Performance
Indicators (KPIs). Unlike green bonds/loans, SLLs do not restrict use of proceeds
but incentivise sustainability performance.

**Common KPIs for Infrastructure SLLs:**

| KPI Category | Metric | Target Example |
|---|---|---|
| **Energy efficiency** | PUE (Power Usage Effectiveness) for DC | PUE < 1.20 by year 3 |
| **Renewable energy** | % of energy from renewable sources | 100% renewable by COD |
| **Carbon intensity** | kg CO2e per MWh stored/delivered | Annual reduction trajectory |
| **Waste heat recovery** | % of waste heat productively reused | >40% recovery within 5 years |
| **Water usage** | WUE (Water Usage Effectiveness) for DC | WUE < 0.50 |
| **Circular economy** | % recycled materials in construction | >30% recycled content |

**Margin Ratchet Mechanism:**
- Margin adjustment: +/- 5–10 bps depending on KPI achievement
- Typically symmetric: margin increases if KPIs missed, decreases if met
- Annual testing against agreed SPT (Sustainability Performance Targets)
- Third-party verification of KPI achievement required

**Documentation Standards:**
- LMA (Loan Market Association) Sustainability-Linked Loan Principles
- Sustainability coordinator role (typically one of the arranging banks)
- Annual sustainability compliance certificate

### 6.3 Greenium Analysis

The "greenium" — the pricing advantage of green-labelled debt over conventional
equivalents — has effectively vanished in the EUR market.

| Market Segment | Greenium Estimate | Trend | Source |
|---|---|---|---|
| EUR IG corporate green bonds | ~1 bp | Converged to near-zero | [ABN AMRO Research] |
| EUR sovereign green bonds | 1–3 bps | Narrowing | [DSTA / Market data] |
| Green project finance loans | Negligible | No material advantage | [Market observation] |

**Implications:**
- "Green" label provides **investor diversification benefit** rather than material
  pricing advantage — access to ESG-mandated capital pools
- Certification costs (Second Party Opinion, annual reporting) must be weighed against
  marginal or zero pricing benefit
- Green structuring still valuable for: marketing, ESG compliance, regulatory
  positioning, access to specific investors (pension funds with ESG mandates)

**Certification and Verification:**

| Provider | Product | Use |
|---|---|---|
| Climate Bonds Initiative (CBI) | Climate Bonds Certification | Green bond certification |
| Sustainalytics (Morningstar) | Second Party Opinion (SPO) | Framework assessment |
| ISS ESG | SPO / Verification | Framework + annual verification |
| S&P Global Ratings | Green Evaluation | Scoring (0–100) |
| CICERO (now part of S&P) | Shades of Green | Framework assessment |

---

## 7. Zekerhedenstructuur / Security Package

### 7.1 Standard Security Package

Under Dutch law (Nederlands recht), the security package for project finance
transactions comprises the following elements, each created by specific legal
instruments (akten).

| Security Type | Dutch Term | Method of Creation | Registration | Priority |
|---|---|---|---|---|
| **Share pledge** | Pandrecht op aandelen | Notariele akte + registration in aandeelhoudersregister | Company register | First priority |
| **Account pledge** | Pandrecht op bankrekeningen | Onderhandse or notariele akte | Account bank notification | First priority |
| **Receivables assignment** | Cessie van vorderingen (stille cessie) | Registered deed (geregistreerde akte) | Belastingdienst registration for date certainty | First priority |
| **Mortgage on real property rights** | Hypotheek op recht van opstal / erfpacht | Notariele akte | Kadaster (Land Registry) | First priority |
| **Pledge on project contracts** | Pandrecht op contractuele rechten | Pandakte per contract | Notification to counterparty (on enforcement) | First priority |
| **Pledge on insurance proceeds** | Pandrecht op verzekeringspenningen | Pandakte + notification to insurer | Insurer acknowledgement | First priority |
| **Pledge on movables** | Bezitloos pandrecht op roerende zaken | Notariele akte or geregistreerde akte | Belastingdienst for date certainty | First priority |
| **Pledge on IP/permits** | Pandrecht op IE-rechten / vergunningen | Assignment deed / pandakte | Where applicable | First priority |
| **Direct agreements** | Directe overeenkomsten (step-in rechten) | Tripartite agreement | Between lender, SPV, and counterparty | Per agreement |

### 7.2 Key Security and Finance Documents

The following documents form the standard documentation package for a Dutch
project finance transaction:

**Finance Documents (Financieringsdocumenten):**

| Document | Dutch Term | Purpose |
|---|---|---|
| Facility Agreement | Leningovereenkomst | Master loan agreement; terms, conditions, covenants |
| Security Trust Deed | Trustakte / Parallel debt overeenkomst | Appoints security agent; creates parallel debt |
| Account Agreement | Rekeningenovereenkomst | Governs project accounts and cash waterfall |
| Intercreditor Agreement | Intercrediteurenovereenkomst | Priority and voting among creditor classes |
| Hedging Agreement | ISDA Master Agreement + Schedule | Interest rate swap documentation |
| Fee Letters | Vergoedingsbrieven | Arrangement, commitment, agency fees |
| Common Terms Agreement | Gemeenschappelijke voorwaardenovereenkomst | Shared definitions and mechanics (multi-tranche) |

**Security Documents (Zekerheidsdocumenten):**

| Document | Dutch Term | Purpose |
|---|---|---|
| Share Pledge Agreement | Pandakte op aandelen | Pledge of SPV shares to security agent |
| Mortgage Deed | Hypotheekakte | Mortgage on recht van opstal / erfpacht |
| Receivables Assignment | Cessieakte | Assignment of receivables (silent) |
| Account Pledge | Pandakte op bankrekeningen | Pledge of project bank accounts |
| Movables Pledge | Pandakte op roerende zaken | Non-possessory pledge on equipment/installations |
| Insurance Pledge | Pandakte op verzekeringen | Pledge of insurance proceeds |
| Contract Pledge | Pandakte op contracten | Pledge of rights under project contracts |

**Project Documents Subject to Direct Agreements:**

| Contract | Counterparty | Direct Agreement Purpose |
|---|---|---|
| EPC Contract | EPC Contractor | Step-in rights; cure rights; assignment on enforcement |
| O&M Agreement | O&M Provider | Continuity of operations; step-in |
| Offtake / PPA / Tolling Agreement | Offtaker | Revenue continuity; step-in |
| Lease / Opstalrecht Agreement | Landowner / Lessor | Site access continuity |
| Grid Connection Agreement | TenneT / DSO | Grid access preservation |
| Insurance Policies | Insurers | Loss payee; notification of cancellation |

### 7.3 Key Dutch Law Considerations (Bijzonderheden Nederlands Recht)

**Parallel Debt Structure (Parallelle Schuld):**
- Standard in Dutch syndicated lending and project finance
- Security agent (zekerheidsagent) holds all security on behalf of the lender group
- Parallel debt: the borrower owes an independent payment obligation to the security
  agent equal in amount to the facility obligations
- This structure allows the security agent to enforce all security for the benefit of
  all lenders, avoiding the complexity of individual security holdings
- Required because Dutch law does not have a statutory trust concept equivalent to
  English/common law trusts
- Legal basis: contractual; upheld in Dutch case law and market practice

**Bezitloos Pandrecht (Non-Possessory Pledge):**
- Pledge on movable assets (e.g., batteries, inverters, transformers, servers)
  without transferring physical possession to the pledgee
- Created by: notariele akte (automatically date-certain) OR onderhandse akte
  registered with the Belastingdienst (for date certainty / vaste dagtekening)
- Date certainty is critical: determines priority ranking among competing pledgees
- On enforcement: pledgee may sell assets through public auction or private sale
  with court permission

**Recht van Parate Executie (Right of Summary Execution):**
- Mortgage holder (hypotheekhouder) can sell the mortgaged property without court
  intervention upon default
- Provides significant enforcement advantage vs. pledge enforcement
- Standard notification and waiting periods apply
- Auction via notaris (public sale) or private sale with voorzieningenrechter approval

**Stille Cessie (Silent Assignment):**
- Standard method for assigning receivables as security
- "Silent" means the debtor (e.g., offtaker) is not notified at the time of assignment
- Upon enforcement event: convert to openbare cessie (disclosed assignment) by
  notifying the debtor; debtor then pays directly to the security agent
- Created by geregistreerde akte (registered deed) for date certainty

**No Floating Charge:**
- **Dutch law does NOT recognise the floating charge concept** known in English law
- Lenders must take **fixed security on each individual asset category** (shares,
  accounts, receivables, movables, real property, contracts, IP, insurance)
- This makes the Dutch security package more document-intensive but provides
  greater certainty of enforcement
- After-acquired property clauses are possible for pandrecht on movables and
  receivables (toekomstige goederen), but must be sufficiently determinable

---

## 8. Leningvoorwaarden / Key Loan Covenants

### 8.1 Financial Covenants (Financiele Ratio's)

Financial covenants are the primary monitoring and control mechanism for lenders in
project finance. Breach triggers remedial actions, distribution lock-up, or default.

| Covenant | Definition | Typical Level | Testing |
|---|---|---|---|
| **Minimum DSCR** | Net Cash Flow Available for Debt Service / Scheduled Debt Service | Per asset class (see Section 2.1) | Semi-annual (actual) |
| **Projected DSCR** | Forward-looking DSCR over remaining debt life | Same as minimum DSCR | Annual (projected) |
| **Lock-up DSCR** | Distribution lock-up threshold | 1.10–1.20x | Semi-annual |
| **Default DSCR** | Event of default trigger | 1.05–1.10x | Semi-annual |
| **Loan Life Cover Ratio (LLCR)** | NPV of cash flows to maturity / outstanding debt | 1.20–1.40x | Annual |
| **Project Life Cover Ratio (PLCR)** | NPV of cash flows to end of project / outstanding debt | 1.30–1.50x | Annual |
| **Gearing ratio** | Debt / (Debt + Equity) | Per asset class | Semi-annual |
| **Reserve accounts** | DSRA fully funded | 6 months of debt service | Continuous |

**Cash Flow Waterfall and DSCR Calculation:**

```
Revenue (omzet)
  - Operating expenses (bedrijfskosten)
  - Tax (belasting)
  - Maintenance reserve contribution
  = Cash Flow Available for Debt Service (CFADS)

CFADS / Debt Service = DSCR

Debt Service = Principal repayment + Interest payment
```

**Distribution Conditions (Uitkeringsvoorwaarden):**
Distributions to equity holders (sponsors) are permitted only when ALL of the
following conditions are met:
1. DSCR above lock-up level (both historical and projected)
2. No Event of Default or Potential Event of Default outstanding
3. All reserve accounts fully funded
4. All insurance in place
5. All financial reporting up to date
6. Compliance certificate delivered

### 8.2 Information Covenants (Informatieconvenanten)

| Reporting Obligation | Frequency | Content | Deadline |
|---|---|---|---|
| Management accounts | Quarterly | P&L, balance sheet, cash flow, DSCR calc | 45 days after quarter-end |
| Audited annual accounts | Annual | Full financial statements (NL GAAP or IFRS) | 120 days after year-end |
| Compliance certificate | Semi-annual | Director certification of covenant compliance | With financial reporting |
| Insurance certificates | Annual + on renewal | Confirmation of all required coverages | 30 days before expiry |
| Technical / operational report | Semi-annual | Performance data, availability, incidents | With financial reporting |
| Environmental compliance | Annual | Permit compliance, emissions data | With annual accounts |
| Material adverse change | Promptly | Notification of any MAC event | As soon as aware |
| Litigation / claims | Promptly | Material litigation or claims | As soon as aware |
| Permit status | Annual | Status of all material permits | With annual accounts |
| Budget / business plan | Annual | Updated forward projections | 30 days before year-end |

### 8.3 Restrictive Covenants (Beperkende Convenanten)

Restrictive covenants limit the SPV's ability to take actions that could prejudice
the lenders' position.

| Restriction | Scope | Lender Consent |
|---|---|---|
| **No additional debt** | No borrowing beyond permitted facilities | Required for any additional debt |
| **No asset disposal** | No sale of material project assets | Required (except ordinary course) |
| **No change of control** | No transfer of SPV shares above threshold | Required (typically >50% threshold) |
| **No material contract amendment** | No change to EPC, O&M, offtake, lease | Required for material amendments |
| **No new business** | SPV restricted to single project activity | Absolute prohibition |
| **No merger/reorganisation** | No structural changes to SPV | Required |
| **No related-party transactions** | Transactions at arm's length only | Required above threshold |
| **Mandatory prepayment** | Insurance proceeds, asset disposal proceeds | Automatic (with reinvestment right) |
| **Cash sweep** | Excess cash applied to debt reduction | Triggered when DSCR above sweep threshold |
| **Permitted investments** | SPV cash invested only in permitted instruments | Specified in facility agreement |
| **Permitted hedging** | Only approved hedging transactions | Specified (matching principle) |

---

## 9. Herfinanciering / Refinancing Considerations

### 9.1 Refinancing Risk Analysis

Refinancing risk arises when the debt tenor is shorter than the economic life of the
project, creating exposure to market conditions at the time of refinancing.

| Risk Factor | Mitigation | Consideration |
|---|---|---|
| **Debt maturity vs. project life** | Align tenor to project life where possible | BESS: 15–20 year asset life; DC: 20+ years |
| **Balloon payment risk** | Avoid or size conservatively; cash sweep to reduce | Model residual debt at maturity |
| **Interest rate environment** | Pre-hedge or fix-rate portion of refinancing | Forward-starting swaps possible |
| **Market appetite** | Maintain lender relationships; diversify sources | Bank market vs. institutional vs. bond |
| **Regulatory changes** | Monitor SDE++, permit regime, grid policy | Subsidy expiry may affect refinancing |
| **Technology obsolescence** | Conservative residual value assumptions | Particularly relevant for BESS and AI |

### 9.2 Refinancing Mechanics

**Key Issues at Refinancing:**
- **Make-whole provisions**: existing facility agreements typically include prepayment
  premiums calculated as NPV of remaining interest margin; size into project economics
- **Swap break costs**: termination of existing interest rate swaps at mark-to-market;
  can be material (positive or negative depending on rate movements)
- **Consent requirements**: existing lender consent may be needed depending on
  facility agreement terms
- **Security release and re-take**: existing security must be released and new
  security granted to refinancing lenders; requires coordination with Kadaster,
  account banks, counterparties
- **Direct agreement novation**: all direct agreements must be novated to new lenders
- **Rating impact**: if rated debt, refinancing may trigger rating review

### 9.3 Mini-Perm Structures

For asset classes with shorter initial debt tenors (merchant BESS, AI factories),
mini-perm structures are increasingly common:

| Feature | Detail |
|---|---|
| **Initial tenor** | 5–7 years |
| **Cash sweep** | Aggressive (70–100% of excess cash) |
| **Margin step-up** | +50–100 bps if not refinanced by target date |
| **Refinancing obligation** | Best-efforts or mandatory refinancing by year 5–7 |
| **Tail period** | 1–2 years after target refinancing date |
| **Balloon** | Sized at 30–50% of original principal |

---

## 10. Debt Sizing Methodology

### 10.1 Sizing Approaches

| Method | Application | Description |
|---|---|---|
| **DSCR sculpting** | Primary method for all PF | Size debt service to maintain target DSCR in each period |
| **LLCR constraint** | Secondary check | NPV of CFADS over debt life / debt must exceed threshold |
| **PLCR constraint** | Secondary check | NPV of CFADS over project life / debt must exceed threshold |
| **Gearing constraint** | Binding for some asset classes | Maximum D/(D+E) ratio |
| **Debt quantum** | Lender credit appetite | Maximum absolute debt amount per lender/project |

### 10.2 Base Case vs. Downside Scenarios

| Scenario | Purpose | Typical Assumptions |
|---|---|---|
| **Base case** | Primary sizing basis | P50 revenue, expected costs, contracted terms |
| **Downside / banking case** | Lender stress test | P90 revenue, higher costs, delay scenarios |
| **Extreme downside** | Default analysis | P99 revenue, equipment failure, contract loss |
| **Upside** | Equity return analysis | P10 revenue, optimised costs |

See: [references/financial-modeling.md](references/financial-modeling.md) for detailed
financial model methodology.

---

## 11. Disclaimer

Debt terms, pricing, and market data presented in this reference document are
**indicative** and derived from published reports, market observation, and
publicly available sources as of February 2026.

**Actual terms** depend on:
- Project-specific characteristics (technology, size, location, counterparties)
- Market conditions and lender appetite at the time of transaction
- Sponsor track record and creditworthiness
- Legal and regulatory environment

This document does **not** constitute:
- Beleggingsadvies (investment advice)
- Juridisch advies (legal advice)
- Financieringsadvies (financing advice)
- A binding indication of terms from any lender or institution

Professional advisors (financial, legal, tax, technical) should be engaged for any
specific transaction.

---

## 12. Cross-References

| Topic | Reference File |
|---|---|
| Security package (Dutch law detail) | [references/netherlands-legal-framework.md](references/netherlands-legal-framework.md) |
| BESS deal terms and case studies | [references/bess-projects.md](references/bess-projects.md) |
| Data centre deal terms and case studies | [references/colocation-data-centers.md](references/colocation-data-centers.md) |
| Financial modelling methodology | [references/financial-modeling.md](references/financial-modeling.md) |
| Risk allocation frameworks | [references/risk-allocation.md](references/risk-allocation.md) |
| Equity structures and returns | [references/equity-structures.md](references/equity-structures.md) |
| SDE++ subsidy details | [references/dutch-subsidy-schemes.md](references/dutch-subsidy-schemes.md) |
| Grid connection and TenneT | [references/grid-connection.md](references/grid-connection.md) |
| Insurance requirements | [references/insurance-requirements.md](references/insurance-requirements.md) |

---

## Sources Index

| Source | Description | Section(s) |
|---|---|---|
| [euribor-rates.eu] | EURIBOR benchmark rates | 3.1 |
| [ECB] | European Central Bank policy rates | 3.1 |
| [AEW Research 2025] | Infrastructure debt margin research | 2.1, 3.1 |
| [Aviva Investors 2026] | Infrastructure debt return targets | 3.1 |
| [ABN AMRO Research] | Greenium analysis EUR market | 3.1, 6.3 |
| [ION Analytics] | ABN AMRO digital infra lending; NIBC acquisition | 4.1 |
| [Dentons] | Project Mufasa legal advisory | 2.1, 4.2 |
| [InfraVia] | Project Leopard capital advisory | 2.1, 4.2 |
| [Invest-NL Annual Report 2024] | Invest-NL portfolio and mobilisation data | 5.1 |
| [Rijksoverheid / Prinsjesdag] | Additional Invest-NL funding announcement | 5.1 |
| [EIB] | EIB lending programmes and targets | 5.2 |
| [EIB / OVHcloud] | OVHcloud financing announcement | 5.2 |
| [EC / InvestEU] | InvestEU guarantee programme | 5.2 |
| [DSTA] | Dutch State Treasury Agency green bond data | 6.1 |
| [PV Magazine Netherlands] | SDE++ BESS allocation | 5.4 |
| [RVO] | Netherlands Enterprise Agency subsidy programmes | 5.5 |
| [LMA] | Loan Market Association SLL Principles | 6.2 |
| [Allen & Overy] | Project finance documentation guides | 2.2 |
| [Market data / observation] | Author market intelligence | Various |

---

*End of reference file — debt-instruments.md*
