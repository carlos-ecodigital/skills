# Due Diligence Checklist / Zorgvuldigheidschecklist voor Nederlandse Projectfinanciering

Comprehensive due diligence checklist for BESS, data center, and AI factory project finance transactions in the Netherlands. Organized by workstream. Use as a starting framework; adapt to project-specific requirements.

## 1. Corporate DD / Vennootschapsrechtelijk

- [ ] KvK (Kamer van Koophandel) uittreksel -- current extract confirming registration, directors, authorized signatories
- [ ] Statuten (articles of association) -- latest version; review governance, share transfer restrictions, reserved matters
- [ ] Aandeelhoudersregister (share register) -- confirm shareholdings, encumbrances, classes
- [ ] UBO-registratie -- confirm UBO register compliance at KvK
- [ ] Bestuursbesluit (board resolution) authorizing the transaction
- [ ] Aandeelhoudersbesluit (shareholder resolution) for material transactions
- [ ] Existing aandeelhoudersovereenkomsten (SHAs) -- review restrictions, consents required
- [ ] Existing pandrechten (pledges) or hypotheken (mortgages) on shares or assets
- [ ] Group structure chart with all entities, ownership percentages, jurisdictions
- [ ] ATAD substance requirements -- confirm NL substance (directors, bank accounts, decision-making)
- [ ] Wft compliance -- confirm no AIFM license required or registration completed
- [ ] Litigation overview -- pending or threatened proceedings

## 2. Projectovereenkomsten / Project Agreements DD

- [ ] EPC contract -- review scope, price, program, LDs, defects liability, guarantees, force majeure, governing law
- [ ] O&M agreement -- review scope, KPIs, availability guarantees, penalty/bonus, term, termination
- [ ] Equipment supply agreements -- manufacturer warranties (battery: capacity + availability; GPU: OEM warranty)
- [ ] Technology license agreements -- software, BMS, EMS, orchestration platform
- [ ] Offtake/revenue contracts -- PPA, tolling, GPUaaS, colocation MLA/SLA terms
- [ ] Land agreements -- eigendom (freehold), erfpacht, huur, recht van opstal deed
- [ ] Cable pooling agreement -- parties, allocation, cost-sharing, MLOEA
- [ ] Grid connection agreement (aansluit- en transportovereenkomst, ATO) with DSO/TSO
- [ ] Interconnection agreements (DC: carrier/peering; AI: network fabric)
- [ ] Insurance broker appointment and broker's report
- [ ] Route-to-market / trading agreements (BESS: aggregator, energy management)
- [ ] Waste heat offtake agreement (if applicable; Wcw context)
- [ ] Subcontractor agreements (if not covered by EPC wrap)
- [ ] Direct agreements (tripartite: SPV, counterparty, lenders) -- confirm step-in rights for each material contract

## 3. Vergunningen / Permits and Regulatory DD

- [ ] Omgevingsvergunning -- granted, unconditional, not subject to appeal (onherroepelijk)
- [ ] Omgevingsplan conformity -- confirm zoning (bestemming) permits the project use
- [ ] MER (Environmental Impact Assessment) -- screening decision or full MER completed
- [ ] Stikstof/AERIUS -- calculation completed; below threshold or naturvergunning obtained
- [ ] Bouwvergunning (building permit) -- technical compliance with Besluit bouwwerken leefomgeving (BBL)
- [ ] Brandveiligheid (fire safety) -- compliance with BBL; BESS: UL9540A, NFPA 855
- [ ] Watervergunning (if applicable)
- [ ] Grid connection confirmation -- TenneT/DSO transportindicatie or formal connection agreement
- [ ] SDE++ beschikking (if applicable) -- granted, conditions, monitoring requirements
- [ ] EU Battery Regulation compliance plan (BESS: battery passport timeline)
- [ ] EU AI Act compliance assessment (AI factory)
- [ ] Gemeentelijke voorwaarden (municipal conditions) -- participatie requirements met
- [ ] Bezwaar/beroep status -- confirm no pending appeals against permits

## 4. Technische DD / Technical Due Diligence

### 4.1 Independent Engineer (IE) Assessment
- [ ] IE appointment and scope of work
- [ ] Construction progress report (if under construction)
- [ ] Design review -- compliance with specifications, codes, standards
- [ ] Equipment review -- manufacturer track record, warranty terms, spare parts availability

### 4.2 BESS-Specific Technical DD
- [ ] Battery technology assessment (LFP/NMC; manufacturer: CATL, BYD, Samsung SDI, etc.)
- [ ] Degradation modeling -- P50/P90 curves; augmentation strategy
- [ ] BMS and PCS compatibility and redundancy
- [ ] Thermal management system design and adequacy
- [ ] Fire suppression system -- UL9540A compliance
- [ ] Round-trip efficiency assumptions and validation
- [ ] Cycling strategy alignment with revenue model (300-400 cycles/year)

### 4.3 DC-Specific Technical DD
- [ ] Tier certification (Uptime Institute Tier III/IV) or equivalent
- [ ] Power distribution architecture -- redundancy level (N+1, 2N)
- [ ] Cooling system capacity and expandability
- [ ] PUE measurement and targets
- [ ] Network connectivity and carrier diversity
- [ ] Physical security and access control

### 4.4 AI Factory-Specific Technical DD
- [ ] GPU specifications and OEM agreements (NVIDIA DGX/HGX)
- [ ] Liquid cooling system design and performance validation
- [ ] GPU refresh schedule and reserve adequacy
- [ ] Network fabric design (InfiniBand/Ethernet)
- [ ] Software stack assessment (CUDA, orchestration)

## 5. Financieel / Financial DD

- [ ] Financial model review -- structure, assumptions, formulas, integrity checks
- [ ] Model audit report -- clean opinion from recognized auditor (Forvis Mazars, Operis, BDO, Gridlines)
- [ ] Revenue assumptions -- market study from independent adviser
- [ ] CAPEX budget -- reconciliation with EPC contract price; contingency adequacy (5-10%)
- [ ] OPEX budget -- benchmarking against comparable projects
- [ ] Debt sizing -- DSCR, LLCR, PLCR within acceptable ranges
- [ ] Sensitivity analysis -- tornado charts; breakeven; scenario analysis
- [ ] Tax structuring review -- earningsstripping impact (24.5%); innovatiebox; verliesverrekening; fiscale eenheid
- [ ] BTW recovery plan -- pre-registration timing; verleggingsregeling
- [ ] Working capital requirements
- [ ] Construction contingency adequacy
- [ ] IDC (interest during construction) calculations

## 6. Milieu / Environmental DD

- [ ] NEN 5725 vooronderzoek (desk study) -- site history, potential contamination
- [ ] NEN 5740:2023 verkennend bodemonderzoek (exploratory soil investigation) -- if desk study indicates risk
- [ ] NTA 5755 nader onderzoek (further investigation) -- if exploratory investigation indicates contamination
- [ ] NEN 5707 asbestonderzoek (asbestos) -- for existing structures
- [ ] AERIUS berekening (nitrogen calculation) -- deposit on Natura 2000 sites
- [ ] Flora/fauna assessment -- protect species survey
- [ ] Noise impact assessment (geluidsonderzoek)
- [ ] Landscape/visual impact (beeldkwaliteitsplan if required)

Key environmental consultancies: RSK, Ekwadraat (stikstof/AERIUS specialist)

## 7. Verzekeringen / Insurance DD

- [ ] Insurance programme review -- broker's report on adequacy
- [ ] Construction: CAR/EAR, DSU, third-party liability, environmental
- [ ] Operational: PAR/ISR, BI, machinery breakdown, environmental, third-party, cyber (DC/AI)
- [ ] BESS-specific: thermal runaway coverage; UL9540A test results provided to insurer
- [ ] Key broker: Marsh; Specialist: GCube/TMGX ($100M Lloyd's), Solarif
- [ ] Degradation: confirm NOT covered; assess augmentation reserve as alternative
- [ ] Force majeure events: confirm alignment between insurance and FM clause
- [ ] Insurer financial strength rating (A.M. Best A- minimum)

## 8. NL-Specifiek / Netherlands-Specific DD Items

- [ ] Transportschaarste assessment -- grid availability at project location; TenneT/DSO confirmation
- [ ] Cable pooling eligibility -- Energiewet readiness; ACM anticipatory approval
- [ ] Recht van opstal deed -- registered at Kadaster; terms reviewed (duration, retributie, termination, compensation)
- [ ] Erfpacht voorwaarden -- reviewed for lender-unfriendly provisions
- [ ] Amsterdam/NH moratorium check -- confirm project NOT in restricted zone
- [ ] Hyperscale ban check -- confirm project <70 MW and <100,000 sqm (if applicable)
- [ ] Wcw assessment -- waste heat recovery potential; municipal heat planning
- [ ] Omgevingswet transition -- status of local omgevingsplan; BOPA required?
- [ ] Stikstof strategy -- extern salderen availability; elektisch materieel commitment
- [ ] BV structuur -- Flex-BV compliance; UBO registration; ATAD substance
- [ ] SDE++ conditionaliteit -- review conditions, monitoring, clawback provisions

## 9. Bankbaarheid samenvatting / Bankability Summary Checklist

| Category | Minimum Threshold for Lender Comfort |
|---|---|
| EPC | Lump-sum turnkey; IG contractor or parent guarantee |
| Revenue | 50%+ contracted or quasi-contracted (SDE++, MLA) |
| Technology | Proven (2+ years operational data); LFP preferred for BESS |
| Grid | Confirmed connection or formal agreement |
| Permits | Onherroepelijk (final and binding); no pending appeals |
| Insurance | Comprehensive programme; A-rated insurers |
| Model | Clean audit opinion from recognized firm |
| Sponsor | Credible track record; adequate equity commitment |

## 10. Disclaimer

This checklist is a framework. Adapt to project-specific circumstances. Not juridisch advies. Engage qualified Dutch legal, tax, technical, and environmental advisers.

## Cross-References
- Netherlands legal: [references/netherlands-legal-framework.md](references/netherlands-legal-framework.md)
- Risk allocation: [references/risk-allocation.md](references/risk-allocation.md)
- Debt instruments: [references/debt-instruments.md](references/debt-instruments.md)
- Financial modeling: [references/financial-modeling.md](references/financial-modeling.md)
