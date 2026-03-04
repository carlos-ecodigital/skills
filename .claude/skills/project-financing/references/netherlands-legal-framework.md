# Nederlands Juridisch Kader / Netherlands Legal Framework for Project Finance

> **Laatst bijgewerkt / Last updated:** February 2026
> **Taal / Language:** Tweetalig Nederlands/Engels (Bilingual Dutch/English)
> **Werkwoordsvorm / Verb form:** Gebiedende wijs / Imperative-infinitive

---

## 1. Inleiding / Introduction

This reference file provides the Dutch legal framework applicable to infrastructure project finance, with emphasis on energy storage (BESS), data centres (DC), fibre, and renewable energy. Key principles governing Dutch project finance include:

- **Contractsvrijheid (freedom of contract):** Parties determine their own contractual terms, subject to mandatory law and public policy (openbare orde).
- **Redelijkheid en billijkheid (reasonableness and fairness, Art. 6:248 BW):** Overriding principle that supplements and may derogate from contractual provisions.
- **Notarieel stelsel (notarial system):** Security over shares, real property, and certain rights requires a notariele akte (notarial deed).
- **Kadaster (Land Registry):** Registration system for rights in rem over onroerend goed (immovable property) and zakelijke rechten (rights in rem).
- **Faillissementsbestendigheid (bankruptcy remoteness):** Structuring principle using stichtingen and limited-recourse mechanisms.

Refer to [financial-model-references.md](./financial-model-references.md) for financial modelling assumptions and to [grid-connection.md](./grid-connection.md) for grid-related legal and regulatory detail.

---

## 2. SPV-oprichting / SPV Formation

### 2.1 Besloten Vennootschap (BV / Private Limited Company)

Standard SPV vehicle for Dutch project finance. The Flex-BV regime entered into force on 1 October 2012 under the Wet vereenvoudiging en flexibilisering BV-recht.

**Kenmerken / Key Features:**

| Kenmerk | Detail |
|---|---|
| Minimumkapitaal (minimum capital) | EUR 0.01 -- no meaningful minimum capital requirement in practice [Source: Art. 2:178 BW] |
| Notariskosten (notary fees) | EUR 500--1,500 standard; spoedoprichting (express incorporation) 3 werkdagen @ EUR 999 [Source: Firm24] |
| KvK-registratie (Chamber of Commerce registration) | EUR 82.25 [Source: KvK.nl, 2025 tariff] |
| Kwaliteitsfonds bijdrage | EUR 8.22--9.95 [Source: OprichtenBV.nl] |
| Wwft-check (AML check) | ~EUR 20 per person [Source: OprichtenBV.nl] |
| Totale oprichtingskosten (total formation costs) | EUR 600--2,600 depending on complexity and urgency |

**Vereisten / Requirements:**

- Notariele akte van oprichting (notarial deed of incorporation) -- mandatory under Art. 2:175 BW.
- Statuten (articles of association) form the constitutional document; include: naam, zetel, doel, maatschappelijk kapitaal, bestuur, aandeelhoudersvergadering, winstbestemming.
- Bestuurder (director) appointment in the deed of incorporation; minimum 1 bestuurder required.
- Aandelenregister (share register) maintained by the company at its registered office.
- Register at KvK within 8 days of incorporation.

**Governance / Bestuursstructuur:**

- Aandeelhoudersvergadering (general meeting of shareholders, AVA): sovereign body; appoints/dismisses bestuurders.
- Bestuur (management board): manages day-to-day operations; fiduciary duties under Art. 2:239 BW.
- Raad van commissarissen (supervisory board, RvC): optional unless structuurregime applies.
- Besluitvorming buiten vergadering (resolution without meeting, Art. 2:238 BW): permitted unless statuten prohibit; requires unanimous written consent of all aandeelhouders with stemrecht.

### 2.2 Naamloze Vennootschap (NV / Public Limited Company)

Use for larger, listed, or bond-issuing project holding structures.

| Kenmerk | Detail |
|---|---|
| Minimumkapitaal (minimum capital) | EUR 45,000 -- must be fully subscribed; minimum 25% paid up on issuance [Source: Art. 2:67 BW] |
| Accountantsverklaring | Required for inbreng in natura (contribution in kind) [Source: Art. 2:94a BW] |
| Board structure | Two-tier: bestuur + raad van commissarissen (mandatory for structuurvennootschap under Art. 2:152 BW) |
| Bearer shares | Abolished since 1 July 2019 (Wet omzetting aan toonder) |
| Prospectusplicht | Applicable if offering securities to public (see Section 4.2) |

### 2.3 Commanditaire Vennootschap (CV / Limited Partnership)

Tax-transparent vehicle used in fund and cross-border structures.

| Kenmerk | Detail |
|---|---|
| Beherende vennoot (GP / general partner) | Unlimited liability for CV debts |
| Commanditaire vennoot (LP / limited partner) | Limited liability -- loses protection if takes part in management (bestuursverbod, Art. 20 WvK) |
| Open CV | Freely transferable interests; treated as fiscaal non-transparant (opaque) for VPB |
| Gesloten CV (closed CV) | Transfer requires consent of all vennoten; fiscaal transparant -- income attributed to vennoten |
| Formation | No notarial deed required; CV-overeenkomst (partnership agreement) suffices; register at KvK |
| Use case | Fund structures, cross-border JVs, layered holding structures above project BVs |

### 2.4 Stichting (Foundation)

Orphan entity for structured finance and bankruptcy-remote security structures.

- **No shareholders, no members, no equity** -- bestuur (board) is sole governing body.
- Creates **faillissementsbestendigheid (bankruptcy remoteness)**: assets held by stichting are not part of sponsor's estate.
- **Stichting administratiekantoor (STAK):** holds shares of SPV and issues certificaten van aandelen (depository receipts) to economic beneficiaries. Separates legal ownership from economic interest.
- **Security trustee role:** Stichting holds shares of project BV as zekerheidsagent (security agent) for lenders under credit agreement. On enforcement, stichting transfers shares to lenders or purchaser.
- **Governance:** Typically 1--3 independent bestuurders from trust companies (e.g., Intertrust, TMF, Vistra); governed by bestuursinstructie.
- **No uitkeringsverbod since Flex-BV:** Stichtingen may make distributions if statuten permit (Art. 2:285 lid 3 BW).

### 2.5 Cooperatie U.A. (Cooperative)

| Kenmerk | Detail |
|---|---|
| Dividendbelasting | No withholding tax on distributions to members (advantage over BV) [Source: Art. 1 lid 1 Wet DB] |
| Profit distribution | Flexible via ledenovereenkomst (membership agreement) |
| Liability | U.A. = uitsluiting van aansprakelijkheid (exclusion of liability for members) |
| Formation | Notariele akte required (Art. 2:53a jo. 2:27 BW); register at KvK |
| Use case | JV structures, fund vehicles, energy cooperatives (energiecooperaties) |
| Governance | Ledenvergadering (member meeting) + bestuur; optional RvC |

### 2.6 UBO-register

- **Registratieplicht (mandatory registration)** at KvK for all Dutch legal entities [Source: Implementatiewet registratie uiteindelijk belanghebbenden].
- **Public access restricted** since 15 July 2025 following CJEU privacy ruling (Case C-37/20 and C-601/20, Luxembourg Business Registers) [Source: KvK.nl].
- Only Wwft/Wtt-obligated entities (banks, notarissen, tax advisers) retain access.
- **Compliance rate:** ~80% of registered entities have filed UBO information [Source: Projective Group, 2024].
- **UBO definition:** Uiteindelijk belanghebbende (ultimate beneficial owner) = natural person with >25% ownership interest, >25% voting rights, or effective control [Source: Art. 10a Wwft].
- **Sancties (penalties):** Administrative fines up to EUR 22,500; criminal liability for non-compliance.

### 2.7 Substance Requirements

For treaty benefits, EU Directive compliance, and anti-abuse:

- **Adequate NL substance** required under ATAD/ATAD2 implementation (Wet implementatie eerste EU-richtlijn antibelastingontwijking, eff. 1 Jan 2019).
- **Minimum substance indicators:** NL-resident directors with relevant expertise, NL bank accounts, NL board meetings (at least 50% held in NL), decision-making in NL, adequate office space, bookkeeping in NL.
- **OECD MLI** impact on Dutch treaty network: PPT (principal purposes test) applies to most Dutch treaties.
- Relevant for holding structures above project SPVs to ensure deelnemingsvrijstelling and treaty WHT reductions are available.
- See [tax-structuring.md](./tax-structuring.md) for detailed substance checklists.

---

## 3. Burgerlijk Wetboek (BW) -- Relevante Bepalingen / Relevant Civil Code Provisions

### 3.1 Boek 2 BW -- Rechtspersonen (Legal Entities)

Key provisions for project finance structuring:

| Artikel | Onderwerp | Relevantie |
|---|---|---|
| Art. 2:175--283 BW | BV-bepalingen (BV provisions) | Full regulatory framework for project BVs |
| Art. 2:195 BW | Blokkeringsregeling (transfer restrictions) | Since Flex-BV, aanbiedingsregeling (right of first offer) is default; freely excludable in statuten; critical for sponsor change-of-control clauses |
| Art. 2:196 BW | Aandelenlevering (share transfer) | Must be by notariele akte; acquire shares in project SPV via notarial deed + registration in aandeelhoudersregister |
| Art. 2:207 BW | Verkrijging eigen aandelen (acquisition of own shares) | BV may acquire own shares if eigen vermogen minus verkrijgingsprijs exceeds reserves required by statuten; bestuurder must approve |
| Art. 2:216 BW | Uitkeringen (distributions) | Uitkeringstest = balanstest (balance sheet test) + liquiditeitstest (liquidity test); bestuurder approval required; bestuurder personally liable if knew or should have known company could not continue to pay debts after distribution |
| Art. 2:238 BW | Besluitvorming buiten vergadering (resolution without meeting) | Permitted unless statuten prohibit; requires unanimous written consent of all aandeelhouders met stemrecht |
| Art. 2:239 BW | Bestuurstaak (duty of directors) | Directors must act in interest of vennootschap and haar onderneming |
| Art. 2:244 BW | Ontslag bestuurder (dismissal of director) | AVA may dismiss at any time; no court intervention needed |
| Art. 2:256 BW | Tegenstrijdig belang (conflict of interest) | Director with personal conflict excluded from decision-making; note: no mandatory prohibition on transaction itself since Flex-BV |

### 3.2 Boek 3 & 5 BW -- Vermogensrecht / Zakelijke Rechten (Property Law / Rights in Rem)

#### 3.2.1 Recht van opstal (Right of Superficies, Art. 5:101--105 BW)

- Grants the opstaller the right to own gebouwen, werken, of beplantingen (buildings, works, or plantings) in, on, or above another party's onroerend goed.
- **Critical for BESS and DC projects** on third-party land: separates ownership of installation from land ownership.
- Created by **notariele akte** registered at **Kadaster** (Land Registry).
- Typical duration: 25--50 years with verlengingsoptie (renewal option).
- **Retributieplicht (ground rent obligation):** payment to grondeigenaar.
- Vestigingsakte (deed of establishment) must specify:
  - Duur (duration) and verlengingsvoorwaarden (renewal conditions)
  - Retributie (ground rent) amount and indexatie
  - Onderhoud (maintenance) obligations
  - Einde en gevolgen (termination and consequences)
  - Vergoedingsregeling (compensation arrangement) at end of term
  - Hypotheceerbaarheid (mortgageability) of the opstalrecht
- Opstalrecht can be hypothecated (Art. 3:227 BW) -- essential for lender security.
- Prefer opstal over huur (lease) for installations to avoid huurbescherming regime.

#### 3.2.2 Erfpacht (Long Lease, Art. 5:85--100 BW)

- Near-eigendom (near-ownership) usage rights over another's onroerend goed.
- **Canon (ground rent):** payable periodically or as afkoopsom (lump sum).
- Duration: 50--99 years or eeuwigdurend (perpetual).
- Erfpachter may hypothecate the erfpachtrecht (Art. 5:98 BW).
- Used by gemeenten (municipalities) for ground-lease structures on industrial sites.
- Erfpachtvoorwaarden (leasehold conditions) set by grondeigenaar; review for:
  - Bestemmingsbeperking (use restriction)
  - Toestemmingsvereiste (consent requirement) for transfer or sublease
  - Canon herziening (rent review) mechanism
  - Sancties on breach (verval erfpacht)

#### 3.2.3 Pandrecht (Pledge, Art. 3:236 BW)

Table of common pledge assets in project finance:

| Verpand object (pledged asset) | Vestigingswijze (creation method) | Bijzonderheden (specifics) |
|---|---|---|
| Aandelen (shares) in project BV | Notariele akte + registration in aandeelhoudersregister (Art. 2:196 BW) | Lender typically obtains stemrecht (voting rights) on enforcement; openbaar pandrecht preferred for control |
| Bankrekeningen (bank accounts) | Onderhandse akte (private deed) or notariele akte + notification to bank | Include verpandingsverbod waiver in account documentation |
| Vorderingen op afnemers (receivables from offtakers) | Stille cessie (silent assignment) by private deed; notification to debtor converts to openbare cessie on enforcement | Registratie bij Belastingdienst for date certainty (Art. 3:239 BW) |
| Contractuele rechten (contractual rights) | Pandakte referencing specific contracts (EPC, O&M, offtake) | Include medewerking (cooperation) clause in underlying contract |
| Verzekeringen (insurance proceeds) | Pandakte + notification to verzekeraar (insurer) | Bankersclausule standard in NL insurance market |
| Roerende installaties (movable equipment -- BESS, transformers) | Bezitloos pandrecht (non-possessory pledge) by private deed | Register at Belastingdienst for date certainty; bodemrecht risk for Belastingdienst |
| Intellectuele eigendom (IP rights) | Pandakte; for octrooien (patents): registration at OCNL | Relevant for proprietary software in DC/BESS |
| Huurvorderingen (rental claims) | Stille cessie by private deed | If project generates rental income |

#### 3.2.4 Hypotheek (Mortgage, Art. 3:260 BW)

- Security over onroerend goed (immovable property) and zakelijke rechten (opstal, erfpacht).
- **Must be created by notariele akte** registered at **Kadaster**.
- **Recht van parate executie (summary foreclosure, Art. 3:268 BW):** mortgagee may sell without court intervention upon default. Standard in project finance.
- **Priority:** determined by date and time of registration at Kadaster (Art. 3:21 BW).
- **Hypotheekakte** must specify: maximum bedrag (secured amount), interest rate reference, conditions of enforcement.
- Multiple hypotheken possible on same asset; priority by registration date.
- **Huurbeding (rental clause, Art. 3:264 BW):** hypotheekhouder may stipulate that property may not be leased without consent.

#### 3.2.5 Cessie (Assignment, Art. 3:94 BW)

| Type | Vereisten | Gebruik |
|---|---|---|
| Openbare cessie (disclosed assignment) | Akte van cessie + mededeling aan debiteur (notification to debtor) | Enforcement of silent pledges; outright transfer of receivables |
| Stille cessie (silent/undisclosed assignment, Art. 3:94 lid 3 BW) | Onderhandse akte (private deed) without notification; registered at Belastingdienst for date certainty | Security assignment in project finance; convert to openbaar on enforcement event |

### 3.3 Boek 6 BW -- Verbintenissen (Obligations)

#### 3.3.1 Ingebrekestelling (Notice of Default, Art. 6:82 BW)

- **Written notice** (schriftelijke aanmaning) with redelijke termijn (reasonable term) required before claiming schadevergoeding (damages) or ontbinding (termination).
- Exception under Art. 6:83 BW: no ingebrekestelling needed if:
  - Fatale termijn (fixed deadline) expired
  - Performance is blijvend onmogelijk (permanently impossible)
  - Debtor has declared it will not perform (mededeling)

#### 3.3.2 Boeteclausule (Penalty / LD Clause, Art. 6:91 BW)

- **Enforceable** as agreed between parties.
- Subject to **rechterlijke matiging (judicial reduction, Art. 6:94 BW)** if penalty is buitensporig (disproportionate) compared to actual loss.
- Best practice: draft as genuine pre-estimate of loss with reasoning documented in negotiations.
- Cumulation with schadevergoeding only if expressly agreed (Art. 6:92 lid 2 BW is default: no cumulation).

#### 3.3.3 Overmacht (Force Majeure, Art. 6:75 BW)

- Narrow interpretation under Dutch law: tekortkoming (breach) must be **niet toerekenbaar** (not attributable) to the debtor.
- Not toerekenbaar if: not due to schuld (fault), and not krachtens wet, rechtshandeling, of verkeersopvattingen (by law, legal act, or common opinion) for debtor's account.
- **Transportschaarste (grid congestion):** widely foreseeable in NL; NOT likely to qualify as overmacht in new contracts [Source: CMS FM Guide NL; Taylor Wessing NL Grid Congestion Alert].
- **COVID-19 / pandemie:** no longer novel; unlikely FM after 2020 [Source: Hoge Raad guidance].
- **Best practice:** include explicit contractual force majeure definitions listing qualifying events and consequences.

#### 3.3.4 Redelijkheid en billijkheid (Good Faith, Art. 6:248 BW)

- **Aanvullende werking (supplementary function, lid 1):** fills gaps in contract.
- **Derogerende werking (derogating function, lid 2):** a contractual provision does not apply insofar as this would be onaanvaardbaar (unacceptable) under the circumstances.
- Even well-drafted, heavily negotiated contracts may be adjusted by courts.
- Particularly relevant for: hardship situations, changed circumstances (onvoorziene omstandigheden, Art. 6:258 BW), and long-term project contracts.

### 3.4 Boek 7 BW -- Bijzondere Overeenkomsten (Specific Contracts)

#### 3.4.1 Aanneming van werk (Contract for Work, Art. 7:750 BW)

- Governs EPC/construction contracts for BESS, DC, fibre, and renewable installations.
- **Oplevering (delivery/completion, Art. 7:758 BW):** triggers risk transfer from aannemer (contractor) to opdrachtgever (employer).
- After oplevering, aannemer is discharged from liability for gebreken (defects) that opdrachtgever knew or reasonably should have discovered at oplevering.
- **Verborgen gebreken (hidden defects):** 5-year verjaringstermijn (limitation period) from ontdekking (discovery); absolute limit 20 years from oplevering (Art. 7:761 BW).
- **Waarschuwingsplicht (duty to warn, Art. 7:754 BW):** aannemer must warn for onjuistheden (errors) in opdrachtgever's design/instructions.
- UAV 2012 / UAV-GC 2005 often incorporated for larger projects (standard conditions).

#### 3.4.2 Huur (Lease, Art. 7:201 BW)

- **Huurbescherming (tenant protection)** for bedrijfsruimte (commercial premises, Art. 7:290 BW): minimum 5+5 year terms, renewal rights.
- **Overige bedrijfsruimte (Art. 7:230a BW):** less protection; court may grant ontruimingsbescherming (eviction protection) up to 3 years.
- **Prefer recht van opstal over huur** for installations on third-party land to avoid huurbescherming regime and to create zakelijk recht (right in rem) rather than persoonlijk recht (personal right).

---

## 4. Wet op het financieel toezicht (Wft) / Financial Supervision Act

### 4.1 Fund Manager Licenses

| Regime | Drempelwaarde | Toezichthouder | Vereisten |
|---|---|---|---|
| Full AIFMD license (vergunning) | Above thresholds or voluntary | AFM | Full compliance: depositaris, risk management, reporting, remuneration policy |
| Light regime / registration (Art. 2:66a Wft) | <EUR 100M AuM (with leverage) or <EUR 500M AuM (no leverage, closed-end, no redemption within 5 years) | AFM registration | Simplified: registration, AIFMD Annex IV reporting, no depositary required |
| Exempt: single-asset SPV | N/A | N/A | Generally NOT a beleggingsinstelling (investment institution) if not pooling capital from multiple investors; assess structure-specific facts carefully [Source: AFM Guidance on Scope] |

### 4.2 Prospectus Requirements

| Scenario | Prospectusplicht (prospectus obligation) | Bevoegde autoriteit |
|---|---|---|
| Public offering of securities > EUR 8M | Verplicht (mandatory); AFM-approved prospectus | AFM |
| Offer exclusively to gekwalificeerde beleggers (qualified investors) | Vrijgesteld (exempt) | N/A |
| Offer to < 150 natural or legal persons per member state (other than qualified investors) | Vrijgesteld | N/A |
| Total consideration < EUR 8M in rolling 12 months | Vrijgesteld | N/A |
| Minimum denomination EUR 100,000 per unit | Vrijgesteld | N/A |
| Green bonds / sustainability-linked bonds | Prospectus required if public offer > EUR 8M; EU Green Bond Standard voluntary | AFM |

[Source: Verordening (EU) 2017/1129 (Prospectus Regulation); Art. 5:2 Wft]

### 4.3 DNB Prudential Oversight

- **Bankvergunning (banking license):** required for entities accepting opvorderbare gelden (repayable funds) from the public (Art. 2:11 Wft) [Source: DNB.nl].
- **SPV lending:** ensure no banking license trigger -- assess whether SPV is accepting deposits or merely issuing bonds to professional investors.
- **Securitisation Regulation (EU 2017/2402):** applies to securitisation SPVs; STS (simple, transparent, standardised) securitisation framework for favourable treatment.
- **DORA (Digital Operational Resilience Act, eff. 17 Jan 2025):** applies to financial entities and their ICT third-party service providers; relevant if DC serves financial sector clients.

---

## 5. Omgevingswet / Environment and Planning Act (eff. 1 Jan 2024)

### 5.1 Structure

The Omgevingswet replaces 26 previous laws (including Wro, Wabo, Wet milieubeheer) into a single integrated framework [Source: rijksoverheid.nl].

| Instrument | Niveau | Functie |
|---|---|---|
| Omgevingsvisie (environmental vision) | Rijk, provincie, gemeente | Strategic long-term vision for the physical environment |
| Omgevingsplan (environment plan) | Gemeente | Replaces bestemmingsplan; all municipal rules for the physical environment in one plan |
| Omgevingsverordening | Provincie | Provincial rules and instructieregels for gemeenten |
| AMvB (Besluit activiteiten leefomgeving, Bal; Besluit kwaliteit leefomgeving, Bkl; Besluit bouwwerken leefomgeving, Bbl; Omgevingsbesluit, Ob) | Rijk | Detailed national rules |
| Omgevingsvergunning | Gemeente (or provincie/Rijk for specific activities) | Permit for specific activities |

**DSO (Digitaal Stelsel Omgevingswet):** digital system for submitting applications and checking rules; accessible via omgevingsloket.nl [Source: DSO, Aan de Slag met de Omgevingswet].

### 5.2 Omgevingsvergunning (Environmental Permit)

| Activiteit | Omschrijving | Procedure |
|---|---|---|
| Bouwactiviteit (building activity) | Constructing, modifying, or demolishing a building | Regulier (8 weken) for technical assessment; meldingsplicht for gevolgklasse 1 |
| Omgevingsplanactiviteit (OPA) | Activity deviating from omgevingsplan rules | Regulier or uitgebreid depending on complexity |
| Milieubelastende activiteit (environmentally impactful activity) | Activities in Bal (e.g., large BESS, industrial DC cooling) | Regulier or uitgebreid; MER may be required |
| Wateractiviteit | Discharge, extraction, or works affecting water system | Waterschap or Rijkswaterstaat |
| Natuuractiviteit (nature activity) | Impact on Natura 2000, protected species | Provincie; may require passende beoordeling |
| Monumentenactiviteit | Works on protected monuments | Gemeente or Rijksdienst voor Cultureel Erfgoed |

**Procedures:**

| Procedure | Termijn | Kenmerken |
|---|---|---|
| Reguliere procedure | 8 weken + 6 weken verlenging | Default procedure; van rechtswege verleend (deemed granted) if not decided in time |
| Uitgebreide procedure (afd. 3.4 Awb) | 26 weken + 6 weken verlenging | For complex activities; mandatory participation; no deemed grant |

**Participatie (participation):** mandatory for omgevingsvergunning applications; applicant must indicate how stakeholders have been involved (Art. 16.55 lid 6 Omgevingswet).

### 5.3 Bestemmingsplan Transition

- Existing bestemmingsplannen automatically became part of the transitional omgevingsplan (bruidsschat) on 1 Jan 2024.
- Deadline for gemeenten to adopt a complete omgevingsplan: **1 January 2032** [Source: Invoeringswet Omgevingswet].
- **BOPA (buitenplanse omgevingsplanactiviteit):** permit for activities not conforming to the omgevingsplan; replaces old buitenplanse afwijking.
- During transition period: old rules remain in force as part of the omgevingsplan until replaced.

### 5.4 MER (Milieueffectrapportage / Environmental Impact Assessment)

- **Verplichte MER (mandatory EIA):** for activities listed in Bijlage V of the Omgevingsbesluit.
- **Beoordelingsplicht (screening obligation):** for activities in Bijlage V below threshold values -- bevoegd gezag (competent authority) determines if full MER is required.
- **Commissie m.e.r. (EIA Commission):** independent advisory body; mandatory advice for plan-MER; optional for project-MER.
- Larger BESS installations (>50 MW or significant spatial impact) and large DCs may trigger screening or full MER obligation.

### 5.5 DC and BESS Specific Permitting

| Jurisdictie | Maatregel | Status / Bron |
|---|---|---|
| Amsterdam | Moratorium on all new data centre construction | Until at least 2030; extended from original 2024 pause [Source: NL Times, April 2025] |
| Nationaal | Hyperscale ban: DCs >70 MW + >100,000 m2 prohibited | Except in designated gebieden (areas) identified by Rijk [Source: CMS LawNow, 2025] |
| Noord-Holland | Restriction on DCs >2,000 m2 or >5 MVA | Provinciale Datacenterstrategie 2025--2027 [Source: Provincie Noord-Holland] |
| Haarlemmermeer | Voorbereidingsbesluit limiting new DC development | Effective 2024; protecting Schiphol area grid capacity [Source: Gemeente Haarlemmermeer] |
| Microsoft / Pure DC (Agriport A7) | 78 MW approved via 3 separate permits | [Source: NL Times, January 2026] |
| Zeewolde (Meta) | Hyperscale DC project cancelled after political debate | 2022; led to national policy tightening |

**BESS-specific:**

- **Nutsvoorziening ruling:** Rechtbank Midden-Nederland (24 April 2025) ruled that a BESS qualifies as nutsvoorziening (utility facility) under certain omgevingsplan classifications [Source: NewGroundLaw.nl].
- **RVO Handreiking elektriciteitsopslagsystemen (guidance on electricity storage systems):** published July 2024; addresses permitting, safety (PGS 37), and spatial planning for BESS [Source: RVO.nl].
- **PGS 37 (Publicatiereeks Gevaarlijke Stoffen):** safety distances and requirements for lithium-ion battery storage; applies to BESS >50 kWh.
- **Brandveiligheid (fire safety):** Bbl requirements; consult Veiligheidsregio for larger installations.

### 5.6 Stikstof (Nitrogen)

- **AERIUS Calculator 2025:** mandatory calculation tool for nitrogen deposition [Source: RIVM].
- **Threshold:** >0.005 mol N/ha/jaar on Natura 2000 area triggers vergunningplicht.
- **Bouwvrijstelling (construction phase exemption):** abolished by Raad van State ruling 2 November 2022 (ECLI:NL:RVS:2022:3159).
- **Intern salderen (internal offsetting):** no longer permit-free following Raad van State ruling December 2024; now requires naturvergunning [Source: Raad van State, ECLI:NL:RVS:2024:5093].
- **Extern salderen (external offsetting):** possible under provincial beleidsregels (policy rules); requires 30% afroming (clipping) in most provinces.
- **Proposed reform:** raise drempelwaarde (threshold) to 1 mol N/ha/jaar [Source: Bouwend Nederland position paper, 2025].
- **ADC-toets:** alternative assessment if significant effects cannot be excluded (Alternatief, Dwingende redenen, Compensatie).
- Impact on project timeline: nitrogen assessment adds 3--12 months to permitting process.

---

## 6. Energiewet / Energy Act (eff. 1 Jan 2026)

Replaces Elektriciteitswet 1998 and Gaswet. Official text: wetten.overheid.nl/BWBR0050714 [Source: Overheid.nl].

### 6.1 Key Changes

| Onderwerp | Oude situatie | Nieuwe situatie onder Energiewet |
|---|---|---|
| Cable pooling (gedeelde aansluiting) | Limited to production; min 2 MVA; max 2 parties | All types of users (production + consumption); min 100 kVA (from 2 MVA); up to 4 parties; BESS explicitly included [Source: QGM Law] |
| ACM anticipatory approval | N/A | ACM may already grant approvals for grid operator investments ahead of formal demand [Source: ACM.nl] |
| Energiegemeenschappen (energy communities) | No formal framework | Right to share energy within community; legal basis for cooperatieve energiegemeenschappen and burgergemeenschappen |
| Grid operator obligations | Limited transparency | Enhanced transparency on connection timelines (aansluitplicht within 18 weeks where feasible); publication of available capacity |
| Prosumer rights | Basic teruglevering (feed-in) | Expanded rights for kleinverbruikers (small consumers) including dynamic tariffs, data access, and energy sharing |
| Leveringsvergunning (supply license) | Separate E and G licenses | Single integrated vergunning |
| Meetverantwoordelijkheid (metering responsibility) | Varied | Clearer framework: netbeheerder or erkende meetverantwoordelijke |
| Systeemintegratie | Ad hoc | Explicit provisions for flexibility services and storage |

### 6.2 Grid Connection Under Energiewet

- See [grid-connection.md](./grid-connection.md) for full treatment of grid connection procedures, transportschaarste, and congestion management.
- **Aansluitplicht (connection obligation):** netbeheerder must connect within redelijke termijn; Energiewet provides clearer framework.
- **Non-firm aansluiting:** contractual arrangement for connection subject to curtailment during congestion; not yet formal under Energiewet but developing in practice.

---

## 7. Belastingen voor SPVs / Tax for Project SPVs

### 7.1 Vennootschapsbelasting (VPB / Corporate Income Tax)

| Parameter | Detail |
|---|---|
| Tarief (rate) | 19% on first EUR 200,000; 25.8% above EUR 200,000 [Source: Belastingdienst.nl, 2025] |
| Earningsstripping (renteaftrekbeperking) | 24.5% of fiscale EBITDA (increased from 20%, eff. 1 Jan 2025) [Source: PwC Belastingplan 2025]; EUR 1M franchise; excess carried forward indefinitely |
| Verliesverrekening (loss relief) | 1 year carry-back; unlimited carry-forward (EUR 1M + 50% of taxable profit exceeding EUR 1M) |
| Afschrijving (depreciation) | Gebouwen (buildings): max to WOZ-waarde (100% for own use); goodwill: max 10% per year |
| Investeringsaftrek (investment deduction) | KIA: small-scale investment deduction; EIA: energy investment deduction (45.5% of qualifying investment); MIA: environmental investment deduction (27%/36%/45%) [Source: RVO.nl] |

### 7.2 Innovatiebox (Innovation Box)

- **Effective rate:** 9% on qualifying profits from innovation [Source: Art. 12b Wet VPB].
- **Vereisten:** WBSO-verklaring (R&D tax credit certificate) from RVO + qualifying intellectual property (self-developed intangible asset).
- Relevant for proprietary BESS software, DC cooling technology, or energy management systems.
- Nexus approach: qualifying profit proportional to own R&D expenditure vs. total costs.

### 7.3 Fiscale eenheid (Fiscal Unity)

- **95%+ ownership** (juridisch en economisch) required [Source: Art. 15 Wet VPB].
- **Effect:** consolidated CIT return; intercompany transactions eliminated for VPB purposes.
- **Restrictions post-CJEU rulings:** per-element approach limits certain cross-border benefits.
- Useful for: netting profits and losses across multiple project SPVs within a group.

### 7.4 Deelnemingsvrijstelling (Participation Exemption)

- **0% CIT** on qualifying dividends and capital gains from holdings of 5% or more [Source: Art. 13 Wet VPB].
- **Toetsen (tests):** must satisfy either onderworpenheidstoets (subject-to-tax test: subsidiary subject to profit tax of reasonable rate) or bezittingstoets (asset test: <50% free portfolio investments).
- **Liquidatieverliesregeling (Art. 13d):** deduction for losses on liquidation of qualifying subsidiary.
- Critical for: Dutch holding SPVs holding project company shares.

### 7.5 Dividendbelasting (Dividend Withholding Tax)

| Scenario | Tarief (rate) | Bron |
|---|---|---|
| Standard BV/NV distribution to shareholder | 15% | Art. 1 Wet DB |
| EU/EEA qualifying parent (>5% holding) | 0% (Parent-Subsidiary Directive) | Art. 4 Wet DB |
| Treaty-reduced rate | 0--10% depending on treaty | Applicable treaty |
| Conditional WHT on payments to low-tax jurisdictions | 25.8% (since 2021) | Wet bronbelasting 2021 |
| Within fiscale eenheid | 0% (intercompany) | Art. 15 Wet VPB |
| Cooperatie U.A. to members | 0% (no dividend withholding on cooperative distributions) | Art. 1 Wet DB |
| Inhoudingsvrijstelling (exemption) | 0% for qualifying holding cooperatives and BVs meeting substance requirements | Art. 4 lid 2 Wet DB |

### 7.6 Overdrachtsbelasting (Real Estate Transfer Tax)

| Scenario | Tarief | Toelichting |
|---|---|---|
| Commercial property (niet-woning) | 10.4% | [Source: Art. 14 WBR, 2025 rate] |
| Recht van opstal / erfpacht | 10.4% | Over de waarde van het recht (on value of the right) |
| Share deal in vastgoedvennootschap | 10.4% | If >50% assets consist of NL onroerende zaken (real property) and held primarily as belegging (investment); Art. 4 WBR |
| Woning (residential) | 2% (or 0% for starters <EUR 510K) | Not typically applicable to project finance |
| Reorganisatievrijstelling (Art. 5bis WBR) | 0% | Intragroup restructuring; conditions apply |

### 7.7 BTW (Omzetbelasting / VAT)

| Scenario | Tarief | Toelichting |
|---|---|---|
| Standard rate | 21% | Default rate for goods and services |
| Warmtelevering (heat supply) | 9% | Verlaagd tarief (reduced rate) |
| Levering elektriciteit | 21% | Standard rate |
| Verleggingsregeling (reverse charge) | 0% supplier / buyer accounts | NL construction services (Art. 12 lid 4 Wet OB 1968); subcontractor charges 0%, hoofdaannemer self-accounts for BTW |
| Verhuur onroerend goed (leasing real property) | Exempt (optie belaste verhuur possible) | Art. 11 lid 1 sub b Wet OB; optie requires >90% aftrekgerechtigd use by huurder |
| Invoer zonnepanelen (solar panel import) | 0% | Since 1 Jan 2023 for residential installations |

### 7.8 Treaty Network

Major treaty partners with dividend WHT rates (excluding conditional WHT):

| Verdragsstaat (treaty state) | Dividend WHT -- portfolio | Dividend WHT -- substantial holding (>= threshold) | Interest WHT | Royalty WHT |
|---|---|---|---|---|
| United Kingdom | 15% | 0% (>=10% capital) | 0% | 0% |
| United States | 15% | 5% (>=10% voting) | 0% | 0% |
| Germany | 15% | 5% (>=25% capital) | 0% | 0% |
| Luxembourg | 15% | 2.5% (>=25% capital) | 0% | 0% |
| Singapore | 15% | 0% (>=25% capital) | 0% | 0% |
| United Arab Emirates | 10% | 5% (>=10% capital) | 0% | 0% |
| Japan | 15% | 5% (>=50% for 6 months) | 0% (10% for certain) | 0% |
| Ireland | 15% | 0% (>=10% voting) | 0% | 0% |

[Source: Belastingdienst Treaty Overview; subject to MLI modifications and LOB clauses]

---

## 8. Toezichthouders / Regulatory Authorities -- Expanded

| Toezichthouder / Authority | Rol / Role | PF Relevantie / PF Relevance |
|---|---|---|
| **AFM** (Autoriteit Financiele Markten) | Securities supervision, market conduct, prospectus approval | Fund structuring, bond issuance, AIFMD registration/license |
| **DNB** (De Nederlandsche Bank) | Prudential supervision, banking license, insurance supervision | Banking license assessment for SPV lending; depositary oversight |
| **ACM** (Autoriteit Consument en Markt) | Competition, energy regulation, tariff approval | Grid tariffs, cable pooling approval, merger clearance, energy market conduct |
| **RVO** (Rijksdienst voor Ondernemend Nederland) | Subsidies, EIA/MIA/WBSO, SDE++ | Subsidy applications, tax deduction certificates, energy project support |
| **TenneT** | Transmission system operator (TSO) -- hoogspanningsnet (>110 kV) | High-voltage grid connections, congestion management, balancing market |
| **Liander / Stedin / Enexis** | Regional distribution system operators (DSOs) | Medium/low-voltage grid connections, transportcapaciteit, cable pooling |
| **KvK** (Kamer van Koophandel) | Commercial register, UBO register | SPV registration, UBO filings, annual account deposits |
| **Kadaster** (Land Registry) | Registration of real property rights and hypotheken | Registration of hypotheek, opstalrecht, erfpacht; title searches |
| **ILT** (Inspectie Leefomgeving en Transport) | Environmental enforcement, building quality | BESS safety enforcement, environmental compliance inspections |
| **Belastingdienst** (Tax and Customs Administration) | Tax collection, VPB/BTW/DB/OB | Tax filings, rulings, registration of stille cessie for date certainty |
| **Notaris** (civil-law notary) | Authentication of deeds, identity verification | Oprichting SPV, share transfers, hypotheek creation, security package execution |
| **Rijkswaterstaat** | National water and road infrastructure management | Watervergunningen for projects near rijkswateren or rijkswegen |
| **Provinciale Staten / Gedeputeerde Staten** | Provincial policy, omgevingsverordening, nature permits | Natura 2000 vergunning, stikstof, provincial spatial policy, extern salderen |
| **Gemeente** (Municipality) | Local omgevingsplan, omgevingsvergunning, local enforcement | Building permits, OPA, fire safety, local spatial integration, participatie |
| **Veiligheidsregio** | Fire safety, disaster response | BESS fire safety assessment, PGS 37 compliance advice |
| **Commissie m.e.r.** | Independent EIA advisory body | Mandatory advice on plan-MER; advisory role on project-MER |
| **OCNL** (Octrooicentrum Nederland) | Patent registration | Registration of pandrecht on octrooien (patents) |
| **Autoriteit Persoonsgegevens** | Data protection (GDPR/AVG enforcement) | DC operators handling personal data; DPIA requirements for large-scale processing |

---

## 9. Cross-Reference Index

| Onderwerp / Topic | Verwijzing / Reference File | Sectie / Section |
|---|---|---|
| Financial model assumptions and WACC | [financial-model-references.md](./financial-model-references.md) | All sections |
| Grid connection procedures and congestion | [grid-connection.md](./grid-connection.md) | Sections 5, 6 |
| Tax structuring and optimization | [tax-structuring.md](./tax-structuring.md) | Section 7 |
| SDE++ and subsidy frameworks | [subsidies-incentives.md](./subsidies-incentives.md) | Sections 5.4, 7.1 |
| EPC and construction contract structures | [contract-structures.md](./contract-structures.md) | Sections 3.4, 5 |
| Insurance requirements (CAR, CEAR, BI) | [insurance-requirements.md](./insurance-requirements.md) | Sections 3.2.3, 5.5 |
| BESS technology and safety standards | [bess-technical.md](./bess-technical.md) | Sections 5.5, 8 |
| Data centre market and permitting | [dc-market.md](./dc-market.md) | Sections 5.5, 8 |
| Due diligence checklists | [due-diligence.md](./due-diligence.md) | All sections |
| Lender security package templates | [security-package.md](./security-package.md) | Sections 3.2, 4 |
| ESG and sustainability compliance | [esg-framework.md](./esg-framework.md) | Sections 5, 7.7 |
| Dutch case law and precedents | [case-law.md](./case-law.md) | Sections 3, 5.6 |

---

## 10. Disclaimer

> **Disclaimer / Voorbehoud**
>
> All rates, thresholds, tariffs, and regulatory information in this document are current as of **February 2026** and are subject to change. Rates quoted for 2025 or 2026 fiscal years reflect the most recent published information at the time of writing.
>
> Always verify current information at authoritative sources:
>
> | Bron / Source | URL |
> |---|---|
> | Wetgeving (legislation) | wetten.overheid.nl |
> | Belastingdienst (tax authority) | belastingdienst.nl |
> | KvK (Chamber of Commerce) | kvk.nl |
> | AFM (financial markets authority) | afm.nl |
> | DNB (central bank) | dnb.nl |
> | ACM (competition/energy regulator) | acm.nl |
> | RVO (enterprise agency) | rvo.nl |
> | Kadaster (land registry) | kadaster.nl |
> | DSO Omgevingsloket | omgevingsloket.nl |
>
> This document does not constitute **juridisch advies (legal advice)** or **belastingadvies (tax advice)**. Engage qualified Dutch legal counsel (advocaat) and tax adviser (belastingadviseur) for transaction-specific guidance.
>
> Cross-references to sibling files assume those files exist in the same directory. If a referenced file is not yet created, treat the reference as a placeholder for future content.
