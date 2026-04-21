# Site Clause Library — LOI + HoT (bilingual, verbatim)

> **Status:** v1.0 shared — consumed by both the Site LOI engine and the Site HoT engine.
> **Owners:** legal-assistant/sites (Carlos + Jelmer + Yoni + SAL).
> **Last sourced:** 2026-04-20 from Van Gog LOI `DEC_LOI_Lodewijk_VanGog_DRAFT_v1.pdf` and HoT body `hot-grower-body-v1.docx`.

---

## 1. Preamble + usage notes

### 1.1 Why this file exists

The Site LOI and the Site HoT share ~40% of their clause text verbatim (Parties, Background, Governing Law, Misc, Information Right). Maintaining two parallel copies of the text in two template engines is a drift hazard: a single wording update has to be made twice, reviewed twice, and version-bumped twice — and experience shows one side lags.

This library is the single source of truth for all bilingual (EN + NL) clause text used by site-stage documents. The Site LOI engine and Site HoT engine both pull from this file at render time; neither engine owns its own copy of the clause text.

### 1.2 Engine consumption pattern

Both engines consume clauses through a single helper:

```python
from site_clause_library import get_clause

# Render §1.2 (Parties — counterparty definition) in English
en_text = get_clause(section_id="1.2", language="en")

# Render the matching Dutch text
nl_text = get_clause(section_id="1.2", language="nl")
```

`get_clause` returns the raw clause text with `{{placeholder}}` tokens unresolved. Placeholder resolution is the caller's responsibility (see §1.3).

Section IDs follow the published LOI numbering (`1.1`, `1.2`, `3.2`, `6.1.6` etc.). HoT-only clauses are addressed under their HoT numbering (`3.1`, `5.4(e)`, `8.13` etc.). Shared clauses are addressed under LOI numbering and marked **[SHARED]** in this file; the HoT engine looks them up under LOI IDs and re-numbers for HoT output if needed.

### 1.3 Variable placeholder convention

Clauses reference deal-specific data via Mustache-style tokens that resolve against the deal YAML (see `deal_yaml_schema.md`):

| Token | Resolves to | Source |
|---|---|---|
| `{{slug}}` | Deal slug (e.g. `van-gog-grubbenvorst`) | deal YAML root |
| `{{site_partner.legal_name}}` | Counterparty entity name | `site_partners[i].legal_name` |
| `{{site_partner.kvk}}` | Dutch CoC number | `site_partners[i].kvk` |
| `{{site_partner.address}}` | Registered seat | `site_partners[i].address` |
| `{{site_partner.signatory.name}}` | Signatory full name | `site_partners[i].signatory.name` |
| `{{site_partner.signatory.title}}` | Signatory title | `site_partners[i].signatory.title` |
| `{{contribs_bess.mw}}` | BESS nameplate MW | asset taxonomy `contributions[].bess.mw` |
| `{{contribs_bess.mwh}}` | BESS energy capacity | asset taxonomy `contributions[].bess.mwh` |
| `{{returns_heat.mw_th}}` | Heat return thermal MW | asset taxonomy `returns[].heat.mw_th` |
| `{{grid.connection_mva}}` | Grid connection capacity | `locations[i].grid.connection_mva` |
| `{{grid.dso}}` | DSO name | `locations[i].grid.dso` |
| `{{land.area_m2_per_mw}}` | Land per MW (default 300) | `locations[i].land.m2_per_mw` |
| `{{term.initial_years}}` | Initial term years (default 30) | deal YAML |
| `{{loi.date}}` | LOI execution date | deal YAML |

All tokens are **required to be resolved** before the document is rendered. Unresolved tokens are a Fatal in `cross_doc_gate.py`.

### 1.4 Canonical role-label derivation

Role labels are not free text. They are derived from the Site Partner's contributions + returns via `ROLE_LABEL_MAP` in `site_doc_base.py`:

```
grid_interconnection → ("Grid Contributor", "Netbijdrager")
land                 → ("Landowner",        "Grondeigenaar")
property             → ("Landowner",        "Grondeigenaar")
energy_heat (return) → ("Heat Offtaker",    "Warmteafnemer")
```

Where a Site Partner fills multiple roles (the Van Gog common case — same counterparty is Grid Contributor, Landowner, and Heat Offtaker), all applicable labels appear in the role list, deduplicated and ordered Grid > Land > Heat for consistency.

**Never** introduce ad-hoc role labels (e.g. "Host", "Site Owner", "Counterparty") in clause text. The only canonical EN labels are:

- **Digital Energy** (the DEC developer)
- **Site Partner / Site Partners** (generic plural — used when role is not yet assigned)
- **Grid Contributor**
- **Landowner**
- **Heat Offtaker**
- **ProjectBV** (the SPV to be incorporated)
- **Grower** (HoT-specific — used when the Site Partner is also a greenhouse operator and the HoT archetype is grower)

The Dutch equivalents are:

- **Digital Energy**
- **Locatiepartner / Locatiepartners**
- **Netbijdrager**
- **Grondeigenaar**
- **Warmteafnemer**
- **ProjectBV**
- **Teler**

### 1.5 "Site Partner" / "Locatiepartner" vocabulary standardisation

Earlier drafts used "Counterparty", "Host Party", and "Grower" inconsistently. The LOI settles this:

- **"Site Partner"** = the LOI-stage generic label for any counterparty, assigned one or more roles in the LOI Schedule Section R.
- **"Grower"** = HoT-stage archetype label, used only when the counterparty is a horticultural operator. The HoT uses "Grower" for brevity; downstream greenhouse-specific HoT templates retain this.
- **"Locatiepartner"** is the Dutch canonical equivalent of "Site Partner" and is used uniformly in LOI NL text.
- **"Teler"** is the Dutch equivalent of "Grower" in HoT text.

Engines must **not** mix vocabularies. A document rendered as LOI uses Site Partner / Locatiepartner; a document rendered as grower HoT uses Grower / Teler. The shared clauses in this library are authored in Site Partner / Locatiepartner form; the HoT engine substitutes at render time.

---

## 2. Shared clauses (both LOI + HoT use verbatim)

These clauses are textually identical (or near-identical up to Party label substitution) in both LOI and HoT. Any edit must be version-bumped on **both** templates per `version-bump.md`.

### §1.1 Parties — Digital Energy **[SHARED]**

**Source:** Van Gog LOI §1.1 (p.2) — matches HoT §1.1 with the entity swap noted below.

**Engine note:** LOI uses `Digital Energy Netherlands B.V.` (the Dutch ProjectBV-feeder entity; KVK 98580086). HoT uses `Digital Energy Group AG` (the Swiss holdco; CHE-408.639.320). The entity is a variable (`{{digital_energy.entity}}`) resolved per document-type.

**English (verbatim, LOI form):**

> 1.1 Digital Energy Netherlands B.V., a private limited company (besloten vennootschap met beperkte aansprakelijkheid) incorporated under Dutch law, registered with the Dutch Chamber of Commerce under number 98580086, with its registered office at Mijnsherenweg 33 A, 1433 AP Kudelstaart, the Netherlands, including its permitted successors and assigns ("Digital Energy").

**Nederlands (verbatim, LOI form):**

> 1.1 Digital Energy Netherlands B.V., een besloten vennootschap met beperkte aansprakelijkheid opgericht naar Nederlands recht, geregistreerd bij de Kamer van Koophandel onder nummer 98580086, met statutaire zetel aan Mijnsherenweg 33 A, 1433 AP Kudelstaart, Nederland, met inbegrip van haar toegestane rechtsopvolgers en rechtverkrijgenden ("Digital Energy").

### §1.2 Parties — Site Partner(s) **[SHARED]**

**Source:** Van Gog LOI §1.2 (p.2).

**English:**

> 1.2 The counterparty or counterparties identified in the LOI Schedule (Section R), with the registered particulars specified therein, including its or their permitted successors and assigns (each a "Site Partner" and, if more than one, collectively the "Site Partners").

**Nederlands:**

> 1.2 De wederpartij of wederpartijen vermeld in de Bijlage (Sectie R), met de statutaire gegevens daarin vermeld, met inbegrip van haar of hun toegestane rechtsopvolgers en rechtverkrijgenden (elk een "Locatiepartner" en, indien meer dan een, gezamenlijk de "Locatiepartners").

**HoT substitution:** in HoT rendering, "LOI Schedule (Section R)" → "Annex A, Item A.1–A.3" and "Site Partner" → "Grower" (when grower archetype).

### §1.3 Parties — collective term **[SHARED]**

**Source:** Van Gog LOI §1.3 (p.2).

**English:**

> 1.3 Digital Energy and each Site Partner are each referred to as a "Party" and together as the "Parties".

**Nederlands:**

> 1.3 Digital Energy en elke Locatiepartner worden afzonderlijk aangeduid als "Partij" en gezamenlijk als "Partijen".

### §1.4 Parties — role assignment **[SHARED, LOI-primary]**

**Source:** Van Gog LOI §1.4 (p.2). HoT does not include this clause verbatim because role assignment in the HoT is implicit in the archetype (the grower HoT assumes Grower = Grid Contributor + Landowner + Heat Offtaker). This clause is therefore retained **LOI-only** in the shared library but lives here because it anchors role vocabulary.

**English:**

> 1.4 The LOI Schedule assigns each Site Partner one or more roles: Grid Contributor (the party providing or applying for the electrical grid connection), Landowner (the party providing land for the DEC), and Heat Offtaker (the party receiving the waste heat). Where this LOI refers to a specific role, the obligation applies only to the Site Partner designated for that role in Section R.

**Nederlands:**

> 1.4 De Bijlage wijst aan elke Locatiepartner een of meer rollen toe: Netbijdrager (de partij die de elektrische netaansluiting verschaft of aanvraagt), Grondeigenaar (de partij die grond beschikbaar stelt voor het DEC), en Warmteafnemer (de partij die de restwarmte ontvangt). Waar deze LOI verwijst naar een specifieke rol, geldt de verplichting uitsluitend voor de Locatiepartner die voor die rol is aangewezen in Sectie R.

### §2.1 Background — DEC description **[SHARED]**

**Source:** Van Gog LOI §2.1 (p.2); matches HoT §2.2.

**English:**

> 2.1 Digital Energy has developed the Digital Energy Center ("DEC"), which captures and reuses waste heat from AI-computing data centers.

**Nederlands:**

> 2.1 Digital Energy heeft het Digital Energy Center ("DEC") ontwikkeld, dat restwarmte van AI-datacenters opvangt en hergebruikt.

### §2.2 Background — Purpose (Project definition) **[SHARED, LOI-primary]**

**Source:** Van Gog LOI §2.2 (p.2-3). HoT frames this differently via Recital B; see `recital_b_pillars.md`.

**English:**

> 2.2 The Parties wish to explore the development of a DEC project (the "Project") at the location(s) specified in the LOI Schedule (Section L). The roles and asset contributions are as set out in Section R.

**Nederlands:**

> 2.2 De Partijen wensen de ontwikkeling van een DEC-project (het "Project") te verkennen op de locatie(s) vermeld in de Bijlage (Sectie L). De rollen en bijdragen zijn zoals vastgelegd in Sectie R.

### §2.3 Background — LOI purpose + ProjectBV reference **[LOI-only]**

**Source:** Van Gog LOI §2.3 (p.3).

**English:**

> 2.3 This Letter of Intent ("LOI") expresses the Parties' mutual interest and sets out the basis for entering into binding Heads of Terms ("HoT") and subsequent definitive agreements ("Agreements") between a Dutch private limited company (besloten vennootschap met beperkte aansprakelijkheid) to be incorporated by Digital Energy as the special-purpose vehicle for the Project ("ProjectBV") and the Site Partner(s).

**Nederlands:**

> 2.3 Deze Intentieverklaring ("LOI") drukt de wederzijdse interesse van de Partijen uit en beschrijft de basis voor het aangaan van bindende Contractvoorwaarden ("HoT") en daaropvolgende definitieve overeenkomsten ("Overeenkomsten") tussen een door Digital Energy op te richten Nederlandse besloten vennootschap als special purpose vehicle voor het Project ("ProjectBV") en de Locatiepartner(s).

### §6.2 Governing Law and Jurisdiction **[SHARED]**

**Source:** Van Gog LOI §6.2 (p.7); matches HoT §§8.3-8.4.

**English:**

> 6.2.1 This LOI is governed by Dutch law.
>
> 6.2.2 Any dispute arising from this LOI shall be submitted exclusively to the District Court of Amsterdam (Rechtbank Amsterdam).

**Nederlands:**

> 6.2.1 Op deze LOI is Nederlands recht van toepassing.
>
> 6.2.2 Geschillen voortvloeiend uit deze LOI worden exclusief voorgelegd aan de Rechtbank Amsterdam.

**HoT engine note:** substitute "LOI" → "HoT and the Agreements" and renumber as 8.3 / 8.4 per HoT §8.3 and §8.4 (see §4 below).

### §6.4 General (Misc) **[SHARED]**

**Source:** Van Gog LOI §6.4.1–6.4.6 (p.8-9). HoT §§8.6–8.13 cover the same ground with additional provisions.

#### §6.4.1 Waiver

**English:**

> 6.4.1 No failure or delay in exercising any right under this LOI shall operate as a waiver thereof.

**Nederlands:**

> 6.4.1 Het niet of vertraagd uitoefenen van enig recht uit hoofde van deze LOI houdt geen afstand daarvan in.

#### §6.4.2 Severability

**English:**

> 6.4.2 If any provision of this LOI is held invalid or unenforceable, the remaining provisions continue in full force and effect.

**Nederlands:**

> 6.4.2 Indien enige bepaling van deze LOI ongeldig of niet-afdwingbaar wordt geacht, blijven de overige bepalingen volledig van kracht.

#### §6.4.3 Amendments

**English:**

> 6.4.3 Amendments to the binding provisions of this LOI require written agreement signed by all Parties.

**Nederlands:**

> 6.4.3 Wijzigingen van de bindende bepalingen van deze LOI vereisen schriftelijke overeenstemming ondertekend door alle Partijen.

#### §6.4.4 Personal data (GDPR)

**English:**

> 6.4.4 Each Party shall process any personal data received in connection with this LOI in accordance with applicable data protection legislation, including Regulation (EU) 2016/679 (GDPR).

**Nederlands:**

> 6.4.4 Elke Partij verwerkt persoonsgegevens die in verband met deze LOI worden ontvangen in overeenstemming met de toepasselijke wetgeving inzake gegevensbescherming, waaronder Verordening (EU) 2016/679 (AVG).

#### §6.4.5 Intellectual property

**English:**

> 6.4.5 Nothing in this LOI grants any Party any rights to any other Party's intellectual property.

**Nederlands:**

> 6.4.5 Niets in deze LOI verleent een Partij enig recht op het intellectuele eigendom van enige andere Partij.

#### §6.4.6 Language — English prevails

**English:**

> 6.4.6 In the event of any discrepancy between the English and Dutch text of this LOI, the English text shall prevail.

**Nederlands:**

> 6.4.6 In geval van discrepantie tussen de Engelse en Nederlandse tekst van deze LOI, prevaleert de Engelse tekst.

---

## 3. LOI-only clauses (non-binding pre-HoT)

These clauses are specific to the LOI stage and are either superseded or re-written for the HoT.

### §3 Project Overview

#### §3.1 DEC Development **[LOI-only]**

**Source:** Van Gog LOI §3.1 (p.3).

**English:**

> 3.1 DEC Development. Digital Energy intends to design, build, finance, and operate a DEC at the Project location(s). Digital Energy expects to bear the cost and risk of the DEC, including, at the end of the term, removal and site restoration. The DEC is expected to be owned and operated by the ProjectBV.

**Nederlands:**

> 3.1 DEC-ontwikkeling. Digital Energy is voornemens een DEC te ontwerpen, bouwen, financieren en exploiteren op de projectlocatie(s). Digital Energy verwacht de kosten en het risico van het DEC te dragen, met inbegrip van verwijdering en locatieherstel aan het einde van de looptijd. Het DEC zal naar verwachting eigendom zijn van en worden geëxploiteerd door de ProjectBV.

#### §3.2 BESS Co-Development **[LOI-only, asset-gated: contribs_bess]**

**Gate:** render only if `contributions[].bess` is present in deal YAML for this Site Partner.

**Source:** Van Gog LOI §3.2 (p.3-4).

**English:**

> 3.2 BESS Co-Development. The Parties anticipate that the Project will include the co-development of a Battery Energy Storage System ("BESS") as an initial development phase. The BESS is intended to utilise the Grid Contributor's electrical connections as described in the LOI Schedule (Section L) and to be located on the Landowner's property. The anticipated configuration is approximately {{contribs_bess.mw}} MW / {{contribs_bess.mwh}} MWh utilising lithium iron phosphate (LFP) technology, subject to detailed engineering and procurement.
>
> The BESS is intended as a joint investment between Digital Energy and the Grid Contributor. The Parties anticipate a 50/50 equity joint venture structure, with the BESS to be owned and operated by a dedicated BESS SPV. The BESS is expected to generate revenue from energy arbitrage, frequency containment reserve (FCR), and other ancillary services on the Dutch electricity balancing market.
>
> The BESS is intended to be operational prior to the DEC, providing the Grid Contributor with standalone investment returns before the DEC development phase commences. At DC financial close, the Parties anticipate that the Grid Contributor's BESS equity interest will convert to an equity interest in the ProjectBV, with the conversion terms to be agreed in the HoT.
>
> All BESS terms, including final capacity, total investment, equity and debt structure, revenue arrangements, grid-sharing with the DEC, operational management, and equity conversion mechanics, are to be agreed in the HoT.

**Nederlands:**

> 3.2 BESS Co-Ontwikkeling. De Partijen voorzien dat het Project de gezamenlijke ontwikkeling van een Batterij Energieopslagsysteem ("BESS") zal omvatten als initiële ontwikkelfase. De BESS is beoogd gebruik te maken van de elektrische aansluitingen van de Netbijdrager zoals beschreven in de Bijlage (Sectie L) en te worden geplaatst op het terrein van de Grondeigenaar. De beoogde configuratie betreft circa {{contribs_bess.mw}} MW / {{contribs_bess.mwh}} MWh met lithiumijzerfosfaat (LFP)-technologie, onder voorbehoud van nadere engineering en inkoop.
>
> De BESS is beoogd als gezamenlijke investering van Digital Energy en de Netbijdrager. De Partijen voorzien een 50/50 aandelenstructuur in joint venture-verband, waarbij de BESS eigendom zal zijn van en wordt geëxploiteerd door een daartoe opgericht BESS SPV. De BESS zal naar verwachting opbrengsten genereren uit energiearbitrage, frequency containment reserve (FCR), en overige hulpdiensten op de Nederlandse balanceringsmarkt.
>
> De BESS is beoogd operationeel te zijn voorafgaand aan het DEC, waardoor de Netbijdrager reeds standalone investeringsrendement ontvangt voordat de DEC-ontwikkelfase aanvangt. Bij de financiële afsluiting van het DC voorzien de Partijen dat het BESS-aandelenbelang van de Netbijdrager wordt omgezet in een aandelenbelang in de ProjectBV, waarbij de conversievoorwaarden worden overeengekomen in de HoT.
>
> Alle BESS-voorwaarden, waaronder definitieve capaciteit, totale investering, eigen vermogen- en schuldstructuur, opbrengstregelingen, netdeling met het DEC, operationeel beheer en conversievoorwaarden, zijn overeen te komen in de HoT.

#### §3.3 Heat Supply **[LOI-only, asset-gated: returns_heat]**

**Gate:** render only if `returns[].heat` is present for this Site Partner.

**Source:** Van Gog LOI §3.3 (p.4).

**English:**

> 3.3 Heat Supply. The Project's objective includes recovering and supplying waste heat from the DEC to the Heat Offtaker designated in Section R. The DEC converts electricity into compute capacity and, as a by-product, generates thermal energy. The facility is designed to capture this heat and deliver it to the adjacent Heat Offtaker's agricultural operations via a direct pipeline connection, replacing conventional gas-fired heating.
>
> The Parties anticipate that the heat supply will be formalised through a long-term heat offtake agreement between the ProjectBV and the Heat Offtaker, with pricing indexed to inflation (CPI). The specific heat supply terms, including price per MWh, volume commitments, delivery specifications, indexation mechanism, minimum offtake obligations, credit support, and contract duration, are to be agreed in the HoT.
>
> The Parties anticipate that the economic benefit of the heat revenue will be shared between Digital Energy and the Grid Contributor, in recognition of the Grid Contributor's contribution of the electrical grid connections that enable the DEC's operations. The terms of such revenue sharing are to be agreed in the HoT.

**Nederlands:**

> 3.3 Warmtelevering. Het Project heeft mede tot doel restwarmte van het DEC terug te winnen en te leveren aan de Warmteafnemer aangewezen in Sectie R. Het DEC zet elektriciteit om in rekencapaciteit en genereert als bijproduct thermische energie. De installatie is ontworpen om deze warmte op te vangen en via een directe pijpleidingverbinding te leveren aan de aangrenzende agrarische activiteiten van de Warmteafnemer, ter vervanging van conventionele gasgestookte verwarming.
>
> De Partijen voorzien dat de warmtelevering wordt geformaliseerd door middel van een langlopende warmteafnameovereenkomst tussen de ProjectBV en de Warmteafnemer, met prijsindexatie aan inflatie (CPI). De specifieke warmteleveringsvoorwaarden, waaronder prijs per MWh, volumeverplichtingen, leveringsspecificaties, indexatiemechanisme, minimale afnameverplichtingen, kredietondersteuning en contractduur, zijn overeen te komen in de HoT.
>
> De Partijen voorzien dat het economisch voordeel van de warmteopbrengsten wordt gedeeld tussen Digital Energy en de Netbijdrager, als erkenning van de bijdrage van de Netbijdrager in de vorm van de elektrische netaansluitingen die de exploitatie van het DEC mogelijk maken. De voorwaarden van deze opbrengstdeling zijn overeen te komen in de HoT.

#### §3.4 Electrical Connection **[LOI-only, asset-gated: grid_interconnection]**

**Gate:** render only if `contributions[].grid_interconnection` is present.

**Source:** Van Gog LOI §3.4 (p.4-5).

**English:**

> 3.4 Electrical Connection. The Project is expected to use the electrical grid connection as described in the LOI Schedule (Section L), including connection capacity (aansluitcapaciteit) and transport capacity (transportcapaciteit). Where the Grid Contributor provides an existing connection, the indicative details are set out in Section L. Where the Grid Contributor will apply for new or additional connections, the anticipated applications are described in Section L. Detailed capacity allocation and connection arrangements are to be determined in the HoT.

**Nederlands:**

> 3.4 Elektrische Aansluiting. Het Project zal naar verwachting gebruik maken van de elektrische netaansluiting zoals beschreven in de Bijlage (Sectie L), met inbegrip van aansluitcapaciteit en transportcapaciteit. Waar de Netbijdrager een bestaande aansluiting beschikbaar stelt, zijn de indicatieve gegevens opgenomen in Sectie L. Waar de Netbijdrager nieuwe of aanvullende aansluitingen zal aanvragen, zijn de beoogde aanvragen beschreven in Sectie L. De gedetailleerde capaciteitsverdeling en aansluitingsregelingen zijn te bepalen in de HoT.

#### §3.5 Land **[LOI-only, asset-gated: land|property]**

**Gate:** render only if `contributions[].land` or `contributions[].property` is present.

**Source:** Van Gog LOI §3.5 (p.5).

**English:**

> 3.5 Land. Where a Site Partner provides land, the Parties contemplate that the Landowner would make land available for the DEC, to be secured by a right of superficies (recht van opstal) or similar arrangement under Dutch law. The anticipated land area for a DEC is approximately {{land.area_m2_per_mw}} m² per MW of electrical capacity. The terms and conditions of any such land arrangement, including any fee or compensation, are to be determined in the HoT.

**Nederlands:**

> 3.5 Grond. Waar een Locatiepartner grond beschikbaar stelt, beogen de Partijen dat de Grondeigenaar grond ter beschikking stelt voor het DEC, te verzekeren door een recht van opstal of vergelijkbare regeling naar Nederlands recht. De verwachte grondoppervlakte voor een DEC bedraagt circa {{land.area_m2_per_mw}} m² per MW elektrisch vermogen. De voorwaarden van een dergelijke grondregeling, met inbegrip van eventuele vergoeding of compensatie, worden vastgelegd in de HoT.

#### §3.6 Multiple Locations **[LOI-only]**

**Source:** Van Gog LOI §3.6 (p.5).

**English:**

> 3.6 Multiple Locations. The Project may comprise one or more locations as listed in Section L of the LOI Schedule. Digital Energy will assess each location and the Parties will agree in the HoT which locations (if any) proceed to development.

**Nederlands:**

> 3.6 Meerdere Locaties. Het Project kan een of meer locaties omvatten zoals vermeld in Sectie L van de Bijlage. Digital Energy zal elke locatie beoordelen en de Partijen zullen in de HoT overeenkomen welke locaties (indien van toepassing) tot ontwikkeling overgaan.

#### §3.7 Separate Contributions **[LOI-only]**

**Source:** Van Gog LOI §3.7 (p.5).

**English:**

> 3.7 Separate Contributions. Where different Site Partners fill different roles as designated in Section R, Digital Energy shall coordinate the integration of the respective contributions.

**Nederlands:**

> 3.7 Afzonderlijke Bijdragen. Waar verschillende Locatiepartners verschillende rollen vervullen zoals aangewezen in Sectie R, zal Digital Energy de integratie van de respectieve bijdragen coördineren.

#### §3.8 Term **[LOI-only]**

**Source:** Van Gog LOI §3.8 (p.5).

**English:**

> 3.8 Term. The Parties contemplate an initial term of {{term.initial_years}} ({{term.initial_years_words}}) years with automatic renewal periods.

**Nederlands:**

> 3.8 Looptijd. De Partijen beogen een initiële looptijd van {{term.initial_years}} ({{term.initial_years_words_nl}}) jaar met automatische verlengingsperioden.

#### §3.9 Costs **[LOI-only]**

**Source:** Van Gog LOI §3.9 (p.5).

**English:**

> 3.9 Costs. Each Party bears its own costs in connection with this LOI and the pre-feasibility assessment. For the avoidance of doubt, neither Party is entitled to reimbursement of any costs from any other Party in connection with this LOI or the pre-feasibility assessment. Digital Energy expects to finance the DEC and the ProjectBV.

**Nederlands:**

> 3.9 Kosten. Elke Partij draagt haar eigen kosten in verband met deze LOI en het pre-haalbaarheidsonderzoek. Voor de duidelijkheid: geen van de Partijen heeft recht op vergoeding van kosten van enige andere Partij in verband met deze LOI of het pre-haalbaarheidsonderzoek. Digital Energy verwacht het DEC en de ProjectBV te financieren.

### §4 Next Steps (Pre-Feasibility + 90-day HoT timeline) **[LOI-only]**

**Source:** Van Gog LOI §§4.1–4.4 (p.5-6).

#### §4.1 Pre-feasibility assessment

**English:**

> 4.1 Following execution of this LOI, Digital Energy intends to conduct a pre-feasibility assessment of the Project, including technical evaluation of the electrical connection(s), heat demand analysis, site survey(s), and any location-specific assessments.

**Nederlands:**

> 4.1 Na ondertekening van deze LOI is Digital Energy voornemens een pre-haalbaarheidsonderzoek van het Project uit te voeren, waaronder een technische beoordeling van de elektrische aansluiting(en), warmtevraaganalyse, locatieonderzoek(en) en eventuele locatiespecifieke beoordelingen.

#### §4.2 Invitation to HoT

**English:**

> 4.2 If the pre-feasibility assessment is positive, Digital Energy expects to invite the Site Partner(s) to enter into binding HoT. It is anticipated that the HoT would include an exclusivity period during which the relevant Site Partner(s) would be expected to refrain from entering into arrangements that would conflict with the Project. The HoT is also expected to include a Variable Schedule specifying site-specific and deal-specific parameters. Data provided in the LOI Schedule carries forward to the HoT where applicable. The HoT is expected to address, among other matters, the BESS co-development terms, heat supply arrangements, grid connection allocation, development fee structure, and land access conditions.

**Nederlands:**

> 4.2 Indien het pre-haalbaarheidsonderzoek positief is, verwacht Digital Energy de Locatiepartner(s) uit te nodigen om bindende HoT aan te gaan. Het wordt verwacht dat de HoT een exclusiviteitsperiode bevatten gedurende welke van de betreffende Locatiepartner(s) verwacht zou worden af te zien van het aangaan van regelingen die in strijd zouden zijn met het Project. De HoT zullen naar verwachting tevens een Variabelenoverzicht met locatiespecifieke en dealspecifieke parameters bevatten. Gegevens verstrekt in de Bijlage worden waar van toepassing overgenomen in de HoT. De HoT zullen naar verwachting onder meer de BESS co-ontwikkelingsvoorwaarden, warmteleveringsregelingen, netaansluitingsverdeling, ontwikkelingsvergoedingsstructuur en grondtoegangscondities behandelen.

#### §4.3 Target timeline — 90 days

**English:**

> 4.3 Target timeline: execution of the HoT within ninety (90) days of this LOI, subject to satisfactory pre-feasibility assessment, Digital Energy's timely completion thereof, and the Site Partner(s)' reasonable cooperation.

**Nederlands:**

> 4.3 Streeftijdlijn: ondertekening van de HoT binnen negentig (90) dagen na deze LOI, onder voorbehoud van een bevredigend pre-haalbaarheidsonderzoek, tijdige afronding daarvan door Digital Energy, en redelijke medewerking van de Locatiepartner(s).

#### §4.4 Site access for pre-feasibility

**English:**

> 4.4 Each Site Partner intends, subject to reasonable advance notice and its operational requirements, to provide Digital Energy and its advisors access to the relevant site(s) and technical documentation relevant to the assets described in the LOI Schedule during normal business hours, to support the pre-feasibility assessment.

**Nederlands:**

> 4.4 Elke Locatiepartner is voornemens, met inachtneming van redelijke voorafgaande kennisgeving en haar operationele vereisten, Digital Energy en haar adviseurs toegang te verlenen tot de relevante locatie(s) en technische documentatie met betrekking tot de in de Bijlage beschreven activa tijdens normale kantooruren, ter ondersteuning van het pre-haalbaarheidsonderzoek.

### §5 Non-Binding Nature **[LOI-only]**

**Source:** Van Gog LOI §§5.1–5.3 (p.6-7).

**English:**

> 5.1 This LOI is not legally binding, except for Sections 6 (Binding Provisions) and 7 (Execution), which are binding upon signature.
>
> 5.2 No Party shall have any obligation to enter into the HoT or any further agreement, and any Party may withdraw from discussions at any time, subject to Section 6.
>
> 5.3 This LOI shall expire on the earlier of (a) six (6) months after the date hereof or (b) execution of the HoT. Upon expiry, all obligations cease except Section 6.1 (Confidentiality) and Section 6.2 (Governing Law and Jurisdiction), which survive in accordance with their terms.

**Nederlands:**

> 5.1 Deze LOI is niet juridisch bindend, met uitzondering van Artikel 6 (Bindende Bepalingen) en Artikel 7 (Ondertekening), die bindend zijn na ondertekening.
>
> 5.2 Geen van de Partijen is verplicht de HoT of enige verdere overeenkomst aan te gaan, en elke Partij kan zich te allen tijde terugtrekken uit besprekingen, met inachtneming van Artikel 6.
>
> 5.3 Deze LOI vervalt op de vroegste van (a) zes (6) maanden na de datum hiervan of (b) ondertekening van de HoT. Na het vervallen eindigen alle verplichtingen, met uitzondering van Artikel 6.1 (Vertrouwelijkheid) en Artikel 6.2 (Toepasselijk Recht en Bevoegde Rechter), die van kracht blijven overeenkomstig hun voorwaarden.

### §6.1 Confidentiality (LOI version — **superseded on HoT signature**)

**Source:** Van Gog LOI §6.1.1–6.1.6 (p.7-8).

> **CRITICAL — self-supersession mechanic.** §6.1.6 is the clause that makes the LOI confidentiality obligation automatically give way to the HoT confidentiality regime on HoT signature. Without §6.1.6, parties could have two conflicting confidentiality regimes running in parallel during the HoT period. This is the structural reason the LOI and HoT have *different* confidentiality clauses and why the HoT's §7 is not merely a copy.

#### §6.1.1 Obligation

**English:**

> 6.1.1 Each Party shall keep strictly confidential the existence, content, and terms of this LOI and all information exchanged in connection with the Project ("Confidential Information").

**Nederlands:**

> 6.1.1 Elke Partij houdt het bestaan, de inhoud en de voorwaarden van deze LOI en alle in verband met het Project uitgewisselde informatie ("Vertrouwelijke Informatie") strikt vertrouwelijk.

#### §6.1.2 Permitted disclosures

**English:**

> 6.1.2 Disclosure of Confidential Information is permitted: (a) to professional advisors, financiers, affiliates, investors or potential investors, and any special-purpose vehicle incorporated by Digital Energy for the Project, in each case on a need-to-know basis and bound by confidentiality obligations no less protective than this Section 6.1; and (b) as required by law, court order, or regulatory authority. Each disclosing Party shall ensure that any such recipient is bound by obligations no less protective than this Section 6.1.

**Nederlands:**

> 6.1.2 Openbaarmaking van Vertrouwelijke Informatie is toegestaan: (a) aan professionele adviseurs, financiers, gelieerde ondernemingen, investeerders of potentiële investeerders, en elke door Digital Energy voor het Project opgerichte special purpose vehicle, in elk geval op need-to-know basis en gebonden door geheimhoudingsverplichtingen die niet minder beschermend zijn dan dit Artikel 6.1; en (b) indien vereist door wet, rechterlijk bevel, of toezichthoudende instantie. Elke openbaarmakende Partij draagt er zorg voor dat elke dergelijke ontvanger gebonden is door verplichtingen die niet minder beschermend zijn dan dit Artikel 6.1.

#### §6.1.3 Exclusions

**English:**

> 6.1.3 Confidential Information does not include information that: (a) is or becomes part of the public domain other than through breach by the receiving Party; (b) was known to the receiving Party before disclosure by the disclosing Party; (c) is independently developed by the receiving Party without use of the disclosing Party's Confidential Information; or (d) is received from a third party without breach of any confidentiality obligation owed to the disclosing Party.

**Nederlands:**

> 6.1.3 Vertrouwelijke Informatie omvat niet informatie die: (a) deel uitmaakt van of deel gaat uitmaken van het publieke domein anders dan door schending door de ontvangende Partij; (b) de ontvangende Partij reeds bekend was voor openbaarmaking door de verstrekkende Partij; (c) zelfstandig is ontwikkeld door de ontvangende Partij zonder gebruik van de Vertrouwelijke Informatie van de verstrekkende Partij; of (d) is ontvangen van een derde zonder schending van enige geheimhoudingsverplichting jegens de verstrekkende Partij.

#### §6.1.4 Compelled disclosure

**English:**

> 6.1.4 If a Party is compelled by law, court order, or regulatory authority to disclose Confidential Information, such Party shall, to the extent legally permitted, promptly notify the other Parties before making such disclosure and cooperate in any effort to obtain confidential treatment.

**Nederlands:**

> 6.1.4 Indien een Partij door wet, rechterlijk bevel of toezichthoudende instantie verplicht wordt Vertrouwelijke Informatie openbaar te maken, stelt die Partij, voor zover wettelijk toegestaan, de andere Partijen onverwijld in kennis voorafgaand aan een dergelijke openbaarmaking en werkt zij mee aan pogingen om vertrouwelijke behandeling te verkrijgen.

#### §6.1.5 Return or destruction

**English:**

> 6.1.5 Upon expiry or termination of this LOI, each Party shall, at another Party's request, return or destroy all Confidential Information received from such Party, except to the extent retention is required by applicable law or for bona fide record-keeping purposes.

**Nederlands:**

> 6.1.5 Bij het vervallen of beëindiging van deze LOI zal elke Partij, op verzoek van een andere Partij, alle van die Partij ontvangen Vertrouwelijke Informatie retourneren of vernietigen, behalve voor zover bewaring wettelijk vereist is of voor legitieme archiveringsdoeleinden.

#### §6.1.6 Self-supersession — **critical verbatim**

**English (verbatim, do not paraphrase):**

> 6.1.6 This confidentiality obligation continues for two (2) years after the date of this LOI or, if the Parties enter into the HoT, is superseded by the confidentiality provisions therein.

**Nederlands (verbatim, niet parafraseren):**

> 6.1.6 Deze geheimhoudingsverplichting duurt voort gedurende twee (2) jaar na de datum van deze LOI of, indien de Partijen de HoT aangaan, wordt deze vervangen door de daarin opgenomen vertrouwelijkheidsbepalingen.

### §6.3 Information Right (role-specific) **[LOI-only]**

**Source:** Van Gog LOI §6.3.1 (p.7).

**English:**

> 6.3.1 During the period from execution of this LOI until the earlier of its expiry or execution of the HoT, each Site Partner shall inform Digital Energy before entering into binding discussions with any third party that would materially affect the assets for which that Site Partner is designated in Section R:
>
> (a) the Grid Contributor shall notify regarding allocation, sharing, or encumbrance of the grid connection(s) described in Section L;
>
> (b) the Landowner shall notify regarding use, lease, encumbrance, or development of the land described in Section L;
>
> (c) the Heat Offtaker shall notify regarding alternative heat supply arrangements that would materially reduce the heat offtake available for the Project;
>
> (d) where a Site Partner fills multiple roles, the notification obligations of all applicable sub-clauses apply cumulatively.

**Nederlands:**

> 6.3.1 Gedurende de periode vanaf ondertekening van deze LOI tot de vroegste van het vervallen of ondertekening van de HoT, stelt elke Locatiepartner Digital Energy in kennis alvorens bindende besprekingen aan te gaan met derden die de activa waarvoor die Locatiepartner is aangewezen in Sectie R wezenlijk zouden beïnvloeden:
>
> (a) de Netbijdrager stelt in kennis met betrekking tot toewijzing, deling of bezwaring van de netaansluiting(en) beschreven in Sectie L;
>
> (b) de Grondeigenaar stelt in kennis met betrekking tot gebruik, verhuur, bezwaring of ontwikkeling van de grond beschreven in Sectie L;
>
> (c) de Warmteafnemer stelt in kennis met betrekking tot alternatieve warmteleveringsregelingen die de beschikbare warmteafname voor het Project wezenlijk zouden verminderen;
>
> (d) waar een Locatiepartner meerdere rollen vervult, zijn de kennisgevingsverplichtingen van alle toepasselijke sub-clausules cumulatief van toepassing.

---

## 4. HoT-only clauses (binding)

Extracted verbatim from `hot-grower-body-v1.docx`. The HoT uses "Grower" where the LOI uses "Site Partner" — see §1.5. Engines substitute at render time per archetype.

### §3 Binding Nature and Exclusivity **[HoT-only]**

#### §3.1 Binding Effect

**English:**

> 3.1 Binding Effect. These Heads of Terms ("HoT") constitute a legally binding agreement. The Parties shall negotiate, prepare, and execute definitive agreements ("Agreements") in good faith and in accordance with the terms herein.

**Nederlands:**

> 3.1 Bindend Karakter. Deze Contractvoorwaarden ("HoT") vormen een juridisch bindende overeenkomst. De Partijen zullen te goeder trouw en overeenkomstig de hierin opgenomen voorwaarden definitieve overeenkomsten ("Overeenkomsten") onderhandelen, voorbereiden en uitvoeren.

#### §3.2 Obligation to Sign

**English:**

> 3.2 Obligation to Sign. Both Parties commit to finalize and sign the Agreements before expiry of the Exclusivity Period, unless a Valid Withdrawal Event occurs and is properly invoked in accordance with Section 3.4.

**Nederlands:**

> 3.2 Ondertekeningsverplichting. Beide Partijen verplichten zich de Overeenkomsten te finaliseren en te ondertekenen vóór het verstrijken van de Exclusiviteitsperiode, tenzij een Geldige Terugtrekkingsgrond zich voordoet en naar behoren wordt ingeroepen overeenkomstig Artikel 3.4.

#### §3.3 Valid Withdrawal Events

**English:**

> 3.3 Valid Withdrawal Events. A "Valid Withdrawal Event" means any of the following circumstances, to the extent not already addressed herein and not caused by the withdrawing Party's breach: (a) failure to secure financing on terms consistent with the Project's financial assumptions; (b) an increase in Project costs exceeding 20% of the budgeted costs as at the Effective Date; (c) failure to obtain necessary regulatory approvals or permits; (d) failure to obtain DSO (netbeheerder) authorization; or (e) failure to obtain SDE++ subsidy.

**Nederlands:**

> 3.3 Geldige Terugtrekkingsgronden. Een "Geldige Terugtrekkingsgrond" betekent een van de volgende omstandigheden, voor zover niet reeds hierin geadresseerd en niet veroorzaakt door een tekortkoming van de zich terugtrekkende Partij: (a) het niet verkrijgen van financiering op voorwaarden die consistent zijn met de financiële uitgangspunten van het Project; (b) een stijging van de Projectkosten met meer dan 20% van de begrote kosten per de Ingangsdatum; (c) het niet verkrijgen van noodzakelijke goedkeuringen of vergunningen; (d) het niet verkrijgen van goedkeuring van de netbeheerder ("DSO"); of (e) het niet verkrijgen van SDE++-subsidie.

#### §3.4 Withdrawal Procedure

**English:**

> 3.4 Withdrawal Procedure. A Party invoking a Valid Withdrawal Event shall: (a) provide written notice to the other Party within fourteen (14) days of becoming aware of such event, together with reasonable supporting evidence; and (b) if the event is capable of remedy, first use commercially reasonable efforts to remedy it within thirty (30) days before withdrawing.

**Nederlands:**

> 3.4 Terugtrekkingsprocedure. Een Partij die een Geldige Terugtrekkingsgrond inroept, dient: (a) de andere Partij binnen veertien (14) dagen na kennisneming van een dergelijke gebeurtenis schriftelijk in kennis te stellen, samen met redelijke ondersteunende documentatie; en (b) indien de gebeurtenis voor herstel vatbaar is, eerst gedurende dertig (30) dagen commercieel redelijke inspanningen te verrichten om deze te verhelpen alvorens zich terug te trekken.

#### §3.5 Withdrawal Consequences

**English:**

> 3.5 Withdrawal Consequences. Upon valid invocation of a Valid Withdrawal Event in accordance with Section 3.4, the affected Party may terminate these HoT by written notice. Upon such termination, neither Party shall have further obligations hereunder, except that Sections 7 (Confidentiality) and 8 (General Provisions) shall survive.

**Nederlands:**

> 3.5 Gevolgen van Terugtrekking. Bij geldige inroeping van een Geldige Terugtrekkingsgrond overeenkomstig Artikel 3.4, kan de betrokken Partij deze HoT beëindigen door middel van schriftelijke kennisgeving. Na een dergelijke beëindiging hebben de Partijen geen verdere verplichtingen uit hoofde hiervan, met dien verstande dat Artikel 7 (Vertrouwelijkheid) en Artikel 8 (Algemene Bepalingen) van kracht blijven.

#### §3.6 Exclusivity Period

**English:**

> 3.6 Exclusivity Period. These HoT take effect on the date of signature by both Parties ("Effective Date") and remain in force until the earlier of: (a) one (1) calendar year from the Effective Date; or (b) execution of the Agreements (the "Exclusivity Period").

**Nederlands:**

> 3.6 Exclusiviteitsperiode. Deze HoT worden van kracht op de datum van ondertekening door beide Partijen ("Ingangsdatum") en blijven van kracht tot de vroegste van: (a) één (1) kalenderjaar na de Ingangsdatum; of (b) ondertekening van de Overeenkomsten (de "Exclusiviteitsperiode").

#### §3.7 Grower Exclusivity

**English:**

> 3.7 Grower Exclusivity. During the Exclusivity Period, the Grower shall not: (a) enter into any agreement or arrangement that conflicts with, or materially prejudices, the Project; (b) reduce the electrical grid capacity available for this Project; or (c) take any action preventing or delaying realization of a secondary allocation point (secundair allocatiepunt, "SAP") for Digital Energy's benefit.

**Nederlands:**

> 3.7 Exclusiviteit van de Teler. Gedurende de Exclusiviteitsperiode zal de Teler niet: (a) enige overeenkomst of regeling aangaan die in strijd is met, of wezenlijk afbreuk doet aan, het Project; (b) de beschikbare elektriciteitsnetcapaciteit voor dit Project verminderen; of (c) enige handeling verrichten die de realisatie van een secundair allocatiepunt ("SAP") ten behoeve van Digital Energy verhindert of vertraagt.

#### §3.8 Breach of Exclusivity

**English:**

> 3.8 Breach of Exclusivity. Any breach by the Grower of Section 3.7 shall entitle Digital Energy to: (a) seek specific performance; (b) terminate these HoT with immediate effect and recover its documented costs and expenses incurred in connection with the Project; and/or (c) claim damages for losses suffered.

**Nederlands:**

> 3.8 Schending van Exclusiviteit. Elke schending door de Teler van Artikel 3.7 geeft Digital Energy het recht om: (a) nakoming te vorderen; (b) deze HoT met onmiddellijke ingang te beëindigen en haar gedocumenteerde kosten en uitgaven in verband met het Project terug te vorderen; en/of (c) schadevergoeding te vorderen voor geleden verliezen.

### §4 Project Scope **[HoT-only]**

#### §4.1 Objectives and Definitions

**English:**

> 4.1 Objectives and Definitions. The project ("Project") comprises the co-location of a DEC on the Grower's property to: (a) supply heat to the greenhouse facility as more particularly described in Annex A ("Greenhouse"); and (b) potentially supply heat to third parties ("Heat Sales") via pipelines connected to the DEC.

**Nederlands:**

> 4.1 Doelstellingen en Definities. Het project ("Project") omvat de co-locatie van een DEC op het terrein van de Teler voor: (a) het leveren van warmte aan het glastuinbouwbedrijf zoals nader omschreven in Bijlage A ("Kas"); en (b) het mogelijk leveren van warmte aan derden ("Warmteverkoop") via leidingen aangesloten op het DEC.

#### §4.2 Project Company

**English:**

> 4.2 Project Company. Digital Energy shall incorporate a Dutch private limited company as the special-purpose vehicle for the Project ("ProjectBV") within sixty (60) days of the Effective Date. All Agreements shall be entered into by, or assigned to, the ProjectBV.

**Nederlands:**

> 4.2 Projectvennootschap. Digital Energy zal binnen zestig (60) dagen na de Ingangsdatum een Nederlandse besloten vennootschap oprichten als special purpose vehicle voor het Project ("ProjectBV"). Alle Overeenkomsten worden aangegaan door, of overgedragen aan, de ProjectBV.

#### §4.3 Costs

**English:**

> 4.3 Costs. Each Party bears its own costs under these HoT and the Agreements. Digital Energy finances and manages the ProjectBV.

**Nederlands:**

> 4.3 Kosten. Elke Partij draagt haar eigen kosten uit hoofde van deze HoT en de Overeenkomsten. Digital Energy financiert en beheert de ProjectBV.

#### §4.4 Digital Energy Responsibilities

**English:**

> 4.4 Digital Energy Responsibilities. Digital Energy (through the ProjectBV) is responsible for all DEC aspects: planning, design, procurement, installation, commissioning, operation, maintenance, decommissioning, and removal at Agreement expiry (collectively, "Develop and Maintain").

**Nederlands:**

> 4.4 Verantwoordelijkheden van Digital Energy. Digital Energy (via de ProjectBV) is verantwoordelijk voor alle DEC-aspecten: planning, ontwerp, inkoop, installatie, ingebruikname, exploitatie, onderhoud, ontmanteling en verwijdering bij het einde van de Overeenkomsten (gezamenlijk "Ontwikkelen en Onderhouden").

#### §4.5 DEC Components

**English:**

> 4.5 DEC Components. The DEC shall include at minimum: (a) Electrical: step-down transformers; low-voltage distribution panels and cables; power distribution units (PDUs); uninterruptible power supplies (UPS). (b) Energy Storage: battery energy storage systems (BESS) for backup power and energy cost optimization. (c) Thermal: coolant distribution units (CDUs); heat exchangers; dry coolers. (d) Computing: servers, GPUs, ASICs; fiber optic connectivity; routers, switches, firewalls. (e) Mechanical: equipment racks; containerized enclosures or buildings; foundations; gas connections; water connections.

**Nederlands:**

> 4.5 DEC-componenten. Het DEC omvat minimaal: (a) Elektrisch: step-down transformatoren; laagspanningsverdeelpanelen en -kabels; power distribution units (PDU's); noodstroomvoorzieningen (UPS). (b) Energieopslag: batterijopslagsystemen (BESS) voor noodstroomvoorziening en optimalisatie van energiekosten. (c) Thermisch: koelmiddeldistributie-eenheden (CDU's); warmtewisselaars; droge koelers. (d) Computing: servers, GPU's, ASIC's; glasvezelconnectiviteit; routers, switches, firewalls. (e) Mechanisch: apparatuurrekken; gecontaineriseerde behuizingen of gebouwen; funderingen; gasaansluitingen; wateraansluitingen.

#### §4.6 Base Electrical Connection

**English:**

> 4.6 Base Electrical Connection. (a) The connection point where the medium-voltage supply interfaces with the DEC's step-down transformers is the "Base DEC Electrical Connection Point". (b) The Grower shall Develop and Maintain the medium-voltage infrastructure from its existing connection to the Base DEC Electrical Connection Point, not exceeding the length specified in Annex A, Item D.7. Any costs for infrastructure exceeding this length shall be borne by the ProjectBV. (c) The ProjectBV shall Develop and Maintain all infrastructure from the Base DEC Electrical Connection Point to the DEC, including transformers and low-voltage systems ("Base DEC Electrical Connection").

**Nederlands:**

> 4.6 Basis Elektrische Aansluiting. (a) Het aansluitpunt waar de middenspanningstoevoer verbinding maakt met de step-down transformatoren van het DEC is het "Basis DEC Elektrisch Aansluitpunt". (b) De Teler zal de middenspanningsinfrastructuur Ontwikkelen en Onderhouden vanaf haar bestaande aansluiting tot aan het Basis DEC Elektrisch Aansluitpunt, met een lengte van maximaal de lengte vermeld in Bijlage A, Punt D.7. Eventuele kosten voor infrastructuur die deze lengte overschrijdt, komen voor rekening van de ProjectBV. (c) De ProjectBV zal alle infrastructuur Ontwikkelen en Onderhouden vanaf het Basis DEC Elektrisch Aansluitpunt tot aan het DEC, inclusief transformatoren en laagspanningssystemen ("Basis DEC Elektrische Aansluiting").

#### §4.7 Future Electrical Connection

**English:**

> 4.7 Future Electrical Connection. (a) The Parties shall negotiate in good faith and agree on the feasibility, financing, design, construction, and maintenance of any upgraded connection ("Future DEC Electrical Connection") using the Grower's infrastructure or primary allocation point (primair allocatiepunt, "PAP"). (b) Ownership, control, maintenance, usage rights, and liabilities for the Future DEC Electrical Connection shall be allocated pro rata based on each Party's documented capital contribution, to the extent permitted by law. Capital contributions shall be determined in the Agreements.

**Nederlands:**

> 4.7 Toekomstige Elektrische Aansluiting. (a) De Partijen zullen te goeder trouw onderhandelen en overeenstemming bereiken over de haalbaarheid, financiering, ontwerp, bouw en onderhoud van een eventuele verzwaarde aansluiting ("Toekomstige DEC Elektrische Aansluiting") met gebruikmaking van de infrastructuur van de Teler of het primair allocatiepunt ("PAP"). (b) Eigendom, controle, onderhoud, gebruiksrechten en aansprakelijkheden voor de Toekomstige DEC Elektrische Aansluiting worden pro rata verdeeld op basis van de gedocumenteerde kapitaalinbreng van elke Partij, voor zover wettelijk toegestaan. Kapitaalinbreng wordt vastgesteld in de Overeenkomsten.

#### §4.8 Heat Transfer

**English:**

> 4.8 Heat Transfer. (a) The ProjectBV shall establish a heat transfer point ("DEC Heat Transfer Point") on the secondary side of the DEC's heat exchangers, at the isolation valves connecting to the Grower's Heat Pipeline. (b) The Grower shall Develop and Maintain the pipeline from the DEC Heat Transfer Point to the Greenhouse boiler room ("Grower's Heat Pipeline").

**Nederlands:**

> 4.8 Warmteoverdracht. (a) De ProjectBV zal een warmteoverdrachtspunt ("DEC Warmteoverdrachtspunt") realiseren aan de secundaire zijde van de warmtewisselaars van het DEC, bij de afsluiters die verbonden zijn met de Warmteleiding van de Teler. (b) De Teler zal de leiding Ontwikkelen en Onderhouden vanaf het DEC Warmteoverdrachtspunt naar de ketelruimte van de Kas ("Warmteleiding van de Teler").

#### §4.9 Third-Party Distribution

**English:**

> 4.9 Third-Party Distribution. The Parties shall negotiate in good faith and agree on the feasibility, financing, design, construction, and maintenance of pipelines (other than the Grower's Heat Pipeline) for Heat Sales to third parties ("DEC Heat Distribution Pipeline").

**Nederlands:**

> 4.9 Distributie aan Derden. De Partijen zullen te goeder trouw onderhandelen en overeenstemming bereiken over de haalbaarheid, financiering, ontwerp, bouw en onderhoud van leidingen (anders dan de Warmteleiding van de Teler) voor Warmteverkoop aan derden ("DEC Warmtedistributieleiding").

#### §4.10 Optional Provisions

**English:**

> 4.10 Optional Provisions. If indicated as "Include" in Annex A, Items F.1–F.2: (a) CHP Lease: Digital Energy shall lease the Grower's combined heat and power unit (warmtekrachtkoppeling, "CHP") for the fee specified in Item F.1a. (b) Grower Co-Investment: The Grower may elect to co-invest up to the percentage specified in Item F.2a of Project costs in cash, in exchange for a pro-rata share of ProjectBV profits. This election must be exercised before Agreement execution. No voting rights shall attach to such investment.

**Nederlands:**

> 4.10 Optionele Bepalingen. Indien aangegeven als "Opnemen" in Bijlage A, Punten F.1–F.2: (a) WKK-Lease: Digital Energy zal de warmtekrachtkoppeling ("WKK") van de Teler leasen voor de vergoeding vermeld in Punt F.1a. (b) Co-Investering Teler: De Teler kan ervoor kiezen tot het percentage vermeld in Punt F.2a van de Projectkosten in contanten te co-investeren, in ruil voor een pro rata aandeel in de winsten van de ProjectBV. Deze keuze moet worden gemaakt vóór ondertekening van de Overeenkomsten. Aan een dergelijke investering zijn geen stemrechten verbonden.

### §5 Agreements **[HoT-only]**

#### §5.1 Parties and Term

**English:**

> 5.1 Parties and Term. (a) The Agreements shall be between ProjectBV and the Grower. (b) Initial term: thirty (30) years from execution. (c) Automatic renewal for successive periods of five (5) years each, unless either Party gives written termination notice at least five (5) years before expiry of the then-current term.

**Nederlands:**

> 5.1 Partijen en Looptijd. (a) De Overeenkomsten worden gesloten tussen de ProjectBV en de Teler. (b) Initiële looptijd: dertig (30) jaar vanaf ondertekening. (c) Automatische verlenging met opeenvolgende perioden van vijf (5) jaar, tenzij een van de Partijen ten minste vijf (5) jaar voor het verstrijken van de dan lopende termijn schriftelijk opzegt.

#### §5.2 Negotiation Principles

**English:**

> 5.2 Negotiation Principles. The Parties shall negotiate the Agreements in good faith and on commercially reasonable terms, ensuring long-term stability, continuity, and investment security for ProjectBV. The Parties may agree to term extensions, a right of first refusal ("ROFR"), or acquisition conditions.

**Nederlands:**

> 5.2 Onderhandelingsprincipes. De Partijen zullen te goeder trouw en op commercieel redelijke voorwaarden over de Overeenkomsten onderhandelen, waarbij lange-termijn stabiliteit, continuïteit en investeringszekerheid voor de ProjectBV wordt gewaarborgd. De Partijen kunnen overeenstemming bereiken over termijnverlengingen, een voorkeursrecht ("ROFR"), of overnamevoorwaarden.

#### §5.3 ProjectBV Obligations

**English:**

> 5.3 ProjectBV Obligations. (a) Electrical Connection: Provide the Base DEC Electrical Connection. (b) Heat Supply: Supply heat at the DEC Heat Transfer Point: (i) target outlet temperature per Annex A, Item C.1, ±5%; (ii) contingent on the Grower maintaining a return temperature ensuring ΔT of at least 15°C; if the Grower fails to maintain the required return temperature, the ProjectBV's obligation to meet the target outlet temperature shall be suspended to that extent; (iii) delivery basis: delivered-as-produced ("DAP"), using commercially reasonable efforts; and (iv) price per Item C.4. (c) Third-Party Heat: Subject to DEC Heat Distribution Pipeline availability, the ProjectBV may deliver heat to third parties.

**Nederlands:**

> 5.3 Verplichtingen van de ProjectBV. (a) Elektrische Aansluiting: De Basis DEC Elektrische Aansluiting verzorgen. (b) Warmtelevering: Warmte leveren bij het DEC Warmteoverdrachtspunt: (i) beoogde afgiftetemperatuur conform Bijlage A, Punt C.1, ±5%; (ii) afhankelijk van het handhaven door de Teler van een retourtemperatuur die een ΔT van ten minste 15°C waarborgt; indien de Teler de vereiste retourtemperatuur niet handhaaft, wordt de verplichting van de ProjectBV om de beoogde afgiftetemperatuur te halen in zoverre opgeschort; (iii) leveringsbasis: geleverd-als-geproduceerd ("DAP"), met commercieel redelijke inspanningen; en (iv) prijs conform Punt C.4. (c) Warmte aan Derden: Onder voorbehoud van beschikbaarheid van de DEC Warmtedistributieleiding, mag de ProjectBV warmte leveren aan derden.

#### §5.4 Grower Obligations (connections)

**English:**

> 5.4 Grower Obligations. (a) Infrastructure: Provide a fully functional Grower's Heat Pipeline and Base DEC Electrical Connection Point. (b) Base Project Connection: Make available an existing grid connection dedicated to the Project ("Base Project Connection"), comprising the capacities specified in Annex A, Items B.7–B.9 ("Base Connection Capacity", "Base Import Capacity", and "Base Export Capacity"). (c) Future Project Connection: Subject to DSO approval, apply for and make available a future grid connection ("Future Project Connection"), expected to comprise the capacities in Items B.10–B.12 ("Future Connection Capacity", "Future Import Capacity", and "Future Export Capacity"). (d) DSO Costs: ProjectBV bears DSO costs for the Future Project Connection, provided: (i) the Grower submits the application only after Agreement execution, or with prior written consent; and (ii) costs incurred before ProjectBV incorporation are reimbursed within the period in Item E.2, plus interest at EURIBOR + 2% from the due date if payment is late.

**Nederlands:**

> 5.4 Verplichtingen van de Teler. (a) Infrastructuur: Een volledig functionele Warmteleiding van de Teler en Basis DEC Elektrisch Aansluitpunt beschikbaar stellen. (b) Basis Projectaansluiting: Een bestaande netaansluiting beschikbaar stellen voor het Project ("Basis Projectaansluiting"), bestaande uit de capaciteiten vermeld in Bijlage A, Punten B.7–B.9 ("Basis Aansluitcapaciteit", "Basis Importcapaciteit", en "Basis Exportcapaciteit"). (c) Toekomstige Projectaansluiting: Onder voorbehoud van DSO-goedkeuring, aanvragen en beschikbaar stellen van een toekomstige netaansluiting ("Toekomstige Projectaansluiting"), naar verwachting bestaande uit de capaciteiten in Punten B.10–B.12 ("Toekomstige Aansluitcapaciteit", "Toekomstige Importcapaciteit", en "Toekomstige Exportcapaciteit"). (d) DSO-kosten: De ProjectBV draagt de DSO-kosten voor de Toekomstige Projectaansluiting, mits: (i) de Teler de aanvraag pas indient na ondertekening van de Overeenkomsten, of met voorafgaande schriftelijke toestemming; en (ii) kosten gemaakt vóór oprichting van de ProjectBV worden vergoed binnen de termijn in Punt E.2, vermeerderd met rente van EURIBOR + 2% vanaf de vervaldatum bij te late betaling.

#### §5.4(e) SAP Configuration

**English:**

> 5.4(e) SAP Configuration. The Grower shall facilitate SAP realization and submit necessary DSO applications for grid or ATO (Aansluit- en Transportovereenkomst) reconfiguration. Priority: (i) Cable Pooling: SAP registered in ProjectBV's name, governed by a Cable Pooling agreement, enabling ProjectBV to contract its own electricity supplier; (ii) MLOEA: If cable pooling is not approved, SAP in the Grower's name under MLOEA (meerdere leveranciers op één aansluiting), with contractual provisions ensuring ProjectBV access; or (iii) Alternative: If neither is feasible, the Grower shall facilitate ProjectBV's use through a capacity allocation agreement on terms to be negotiated in good faith.

**Nederlands:**

> 5.4(e) SAP-configuratie. De Teler zal de SAP-realisatie faciliteren en de benodigde DSO-aanvragen indienen voor herconfiguratie van het net of de ATO (Aansluit- en Transportovereenkomst). Volgorde: (i) Cable Pooling: SAP geregistreerd op naam van de ProjectBV, beheerst door een Cable Pooling-overeenkomst, waardoor de ProjectBV haar eigen elektriciteitsleverancier kan contracteren; (ii) MLOEA: Indien cable pooling niet wordt goedgekeurd, SAP op naam van de Teler onder MLOEA (meerdere leveranciers op één aansluiting), met contractuele bepalingen die toegang voor de ProjectBV waarborgen; of (iii) Alternatief: Indien geen van beide haalbaar is, zal de Teler het gebruik door de ProjectBV faciliteren via een capaciteitsallocatieovereenkomst op voorwaarden die te goeder trouw worden onderhandeld.

#### §5.5 Land Rights

**English:**

> 5.5 Land Rights. (a) Grant: The Grower shall provide land for the DEC for no additional fee or payment. (b) Legal Form: The Grower shall grant (or procure the grant of) a right of superficies (opstalrecht) and/or enter into a Right in Rem Agreement ("ZRO", Zakelijk Recht Overeenkomst) enabling DEC construction, operation, and maintenance. (c) Area: Approximately the area per MW specified in Annex A, Item D.5, for the combined Base Connection Capacity and Future Connection Capacity. (d) Establishment: The right of superficies shall be established by notarial deed, with easements (erfdienstbaarheden) if necessary. (e) Extension: The Grower shall cooperate in creating additional land rights if Future Connection Capacity becomes available. (f) Zoning: The Parties shall cooperate to ensure compliance with applicable zoning (bestemmingsplan) per Item D.4. (g) Third-Party Consents: If the Grower is not the landowner or does not have unencumbered title, the landowner ("Landowner") and/or land financier ("Land Financier") shall co-sign the Agreements.

**Nederlands:**

> 5.5 Grondrechten. (a) Verlening: De Teler stelt grond beschikbaar voor het DEC zonder aanvullende vergoeding of betaling. (b) Juridische Vorm: De Teler zal een recht van opstal verlenen (of doen verlenen) en/of een Zakelijk Recht Overeenkomst ("ZRO") aangaan die de bouw, exploitatie en onderhoud van het DEC mogelijk maakt. (c) Oppervlakte: Circa de oppervlakte per MW vermeld in Bijlage A, Punt D.5, voor de gecombineerde Basis Aansluitcapaciteit en Toekomstige Aansluitcapaciteit. (d) Vestiging: Het recht van opstal wordt bij notariële akte gevestigd, met erfdienstbaarheden indien nodig. (e) Uitbreiding: De Teler zal meewerken aan het vestigen van aanvullende grondrechten indien Toekomstige Aansluitcapaciteit beschikbaar komt. (f) Bestemmingsplan: De Partijen werken samen om naleving van het toepasselijke bestemmingsplan conform Punt D.4 te waarborgen. (g) Toestemmingen van Derden: Indien de Teler niet de grondeigenaar is of geen onbezwaarde titel heeft, dient de grondeigenaar ("Grondeigenaar") en/of grondfinancier ("Grondfinancier") de Overeenkomsten mede te ondertekenen.

#### §5.6 Operational Flexibility

**English:**

> 5.6 Operational Flexibility. (a) The Parties shall cooperate to maximize DEC uptime and efficiency. (b) ProjectBV may curtail or suspend operations upon fourteen (14) days' prior written notice if adverse market conditions, equipment failure, regulatory constraints, or other circumstances make operation commercially unviable, provided ProjectBV demonstrates to the Grower's reasonable satisfaction that such circumstances existed. Any curtailment exceeding ninety (90) consecutive days requires the Grower's prior written consent.

**Nederlands:**

> 5.6 Operationele Flexibiliteit. (a) De Partijen werken samen om de uptime en efficiëntie van het DEC te maximaliseren. (b) De ProjectBV mag de activiteiten inkorten of opschorten na veertien (14) dagen voorafgaande schriftelijke kennisgeving indien ongunstige marktomstandigheden, apparatuurstoringen, regelgevende beperkingen of andere omstandigheden de exploitatie commercieel onhaalbaar maken, mits de ProjectBV naar redelijke tevredenheid van de Teler aantoont dat dergelijke omstandigheden bestonden. Elke inkorting van meer dan negentig (90) opeenvolgende dagen vereist voorafgaande schriftelijke toestemming van de Teler.

#### §5.7 Subsidy Cooperation

**English:**

> 5.7 Subsidy Cooperation. The Parties shall cooperate in good faith to apply for and secure SDE++ and other applicable subsidies for the Project's benefit. The Parties shall submit the SDE++ application within the next available application window following the Effective Date.

**Nederlands:**

> 5.7 Subsidiesamenwerking. De Partijen werken te goeder trouw samen om SDE++ en andere toepasselijke subsidies aan te vragen en te verkrijgen ten behoeve van het Project. De Partijen dienen de SDE++-aanvraag in binnen de eerstvolgende beschikbare aanvraagperiode na de Ingangsdatum.

### §6 Costs and Revenues **[HoT-only]**

#### §6.1 DEC Costs and Revenues

**English:**

> 6.1 DEC Costs and Revenues. ProjectBV bears all costs and retains all revenues directly attributable to the DEC ("DEC Costs" and "DEC Revenues"), including without limitation: (a) energy costs, including revenue from negative-priced electricity consumption; (b) energy tax (Energiebelasting, "EB"); the Parties shall evaluate combined EB volumes per Item C.5; (c) DSO grid charges: fixed ("kW-Contract") and variable ("kW-Max"); (d) energy trading (PPAs, OTC, day-ahead/intraday markets); (e) ancillary services (FCR, aFRR, mFRR); and (f) grid services (capacity-limiting contracts, redispatch, congestion management).

**Nederlands:**

> 6.1 DEC-kosten en -opbrengsten. De ProjectBV draagt alle kosten en behoudt alle opbrengsten die rechtstreeks aan het DEC zijn toe te rekenen ("DEC-kosten" en "DEC-opbrengsten"), waaronder: (a) energiekosten, inclusief opbrengsten uit het verbruik van negatief geprijsde elektriciteit; (b) Energiebelasting ("EB"); de Partijen evalueren gecombineerde EB-volumes conform Punt C.5; (c) DSO-netkosten: vast ("kW-Contract") en variabel ("kW-Max"); (d) energiehandel (PPA's, OTC, day-ahead/intraday markten); (e) systeemdiensten (FCR, aFRR, mFRR); en (f) netdiensten (capaciteitsbeperkende contracten, redispatch, congestiebeheer).

#### §6.2 Greenhouse Costs and Revenues

**English:**

> 6.2 Greenhouse Costs and Revenues. The Grower bears all costs and retains all revenues directly attributable to the Greenhouse ("Greenhouse Costs" and "Greenhouse Revenues").

**Nederlands:**

> 6.2 Kaskosten en -opbrengsten. De Teler draagt alle kosten en behoudt alle opbrengsten die rechtstreeks aan de Kas zijn toe te rekenen ("Kaskosten" en "Kasopbrengsten").

#### §6.3 Heat Sales Sharing

**English:**

> 6.3 Heat Sales Sharing. Net income from third-party Heat Sales (excluding heat to the Grower) is shared per Annex A, Item E.1. "Net income" means gross revenues minus distribution costs (maintenance, pumping, and applicable taxes on heat sales, excluding corporate income tax), which costs are also shared in the same proportion.

**Nederlands:**

> 6.3 Verdeling Warmteverkoop. Netto-inkomsten uit Warmteverkoop aan derden (exclusief warmte aan de Teler) worden verdeeld conform Bijlage A, Punt E.1. "Netto-inkomsten" betekent bruto-opbrengsten minus distributiekosten (onderhoud, pompen, en toepasselijke belastingen op warmteverkoop, exclusief vennootschapsbelasting), welke kosten ook in dezelfde verhouding worden verdeeld.

#### §6.4 Billing Pass-Through

**English:**

> 6.4 Billing Pass-Through. If SAP configuration requires one Party to receive invoices or revenues intended for the other, such amounts shall be reimbursed within the period in Item E.2.

**Nederlands:**

> 6.4 Doorbelasting. Indien de SAP-configuratie vereist dat een Partij facturen of opbrengsten ontvangt die bestemd zijn voor de andere Partij, worden dergelijke bedragen vergoed binnen de termijn in Punt E.2.

#### §6.5 Audit Rights

**English:**

> 6.5 Audit Rights. Each Party may, upon thirty (30) days' notice, audit the other Party's records relating to shared costs and revenues under this Section 6, at the auditing Party's expense. Audits shall be conducted during normal business hours and not more than once per calendar year.

**Nederlands:**

> 6.5 Auditrechten. Elke Partij kan, na dertig (30) dagen kennisgeving, de administratie van de andere Partij met betrekking tot gedeelde kosten en opbrengsten onder dit Artikel 6 controleren, op kosten van de auditerende Partij. Audits worden uitgevoerd tijdens normale kantooruren en niet meer dan eenmaal per kalenderjaar.

#### §6.6 Disputed Amounts

**English:**

> 6.6 Disputed Amounts. If a Party disputes an invoice, it shall pay the undisputed amount and notify the other Party of the dispute within fourteen (14) days. The Parties shall resolve the dispute in accordance with Section 8.5.

**Nederlands:**

> 6.6 Betwiste Bedragen. Indien een Partij een factuur betwist, betaalt zij het onbetwiste bedrag en stelt zij de andere Partij binnen veertien (14) dagen van het geschil in kennis. De Partijen lossen het geschil op overeenkomstig Artikel 8.5.

### §7 Confidentiality — HoT version (supersedes LOI §6.1) **[HoT-only]**

> **Supersession mechanic.** Per LOI §6.1.6 (see §3 above), on HoT signature the HoT confidentiality regime below **replaces** the LOI regime. The two are not additive.

#### §7.1 Obligation

**English:**

> 7.1 Obligation. Each Party shall keep strictly confidential these HoT and all information disclosed in connection with the Project ("Confidential Information").

**Nederlands:**

> 7.1 Verplichting. Elke Partij houdt deze HoT en alle informatie die in verband met het Project wordt verstrekt strikt vertrouwelijk ("Vertrouwelijke Informatie").

#### §7.2 Permitted Disclosures

**English:**

> 7.2 Permitted Disclosures. Disclosure is permitted: (a) as required by law, court order, or regulatory authority; (b) to affiliates, financiers, and professional advisors (legal, technical, commercial) on a need-to-know basis, if bound by confidentiality obligations no less protective than this Section 7; (c) for inclusion in subsidy applications, regulatory filings, or permit applications, to the extent required; or (d) with prior written consent.

**Nederlands:**

> 7.2 Toegestane Openbaarmakingen. Openbaarmaking is toegestaan: (a) indien vereist door wet, rechterlijk bevel, of toezichthoudende instantie; (b) aan gelieerde ondernemingen, financiers, en professionele adviseurs (juridisch, technisch, commercieel) op need-to-know basis, indien gebonden door geheimhoudingsverplichtingen die niet minder beschermend zijn dan dit Artikel 7; (c) voor opname in subsidieaanvragen, regelgevende dossiers, of vergunningaanvragen, voor zover vereist; of (d) met voorafgaande schriftelijke toestemming.

#### §7.3 Exclusions

**English:**

> 7.3 Exclusions. Confidential Information excludes information that: (a) enters the public domain other than through breach by the receiving Party; (b) was known to the receiving Party before disclosure; (c) is independently developed by the receiving Party; or (d) is received from a third party without breach of any confidentiality obligation owed to the disclosing Party.

**Nederlands:**

> 7.3 Uitzonderingen. Vertrouwelijke Informatie omvat niet informatie die: (a) openbaar wordt anders dan door schending door de ontvangende Partij; (b) de ontvangende Partij reeds bekend was vóór openbaarmaking; (c) zelfstandig is ontwikkeld door de ontvangende Partij; of (d) is ontvangen van een derde zonder schending van enige geheimhoudingsverplichting jegens de verstrekkende Partij.

#### §7.4 Return of Information

**English:**

> 7.4 Return of Information. Upon termination, each Party shall return or destroy Confidential Information of the other Party upon request, except to the extent retention is required by law or for bona fide record-keeping purposes.

**Nederlands:**

> 7.4 Teruggave van Informatie. Bij beëindiging zal elke Partij op verzoek Vertrouwelijke Informatie van de andere Partij retourneren of vernietigen, behalve voor zover bewaring wettelijk vereist is of voor legitieme archiveringsdoeleinden.

#### §7.5 Duration

**English:**

> 7.5 Duration. These obligations continue for two (2) years after termination of these HoT.

**Nederlands:**

> 7.5 Duur. Deze verplichtingen blijven van kracht gedurende twee (2) jaar na beëindiging van deze HoT.

### §8 General Provisions **[HoT-only]**

#### §8.1 Costs

**English:**

> 8.1 Costs. Each Party bears its own costs in negotiating and preparing these HoT and the Agreements.

**Nederlands:**

> 8.1 Kosten. Elke Partij draagt haar eigen kosten voor het onderhandelen en opstellen van deze HoT en de Overeenkomsten.

#### §8.2 Assignment

**English:**

> 8.2 Assignment. (a) Neither Party may assign or transfer any rights or obligations without prior written consent. (b) Exception: Digital Energy may assign to ProjectBV upon incorporation. Digital Energy shall remain jointly and severally liable for ProjectBV's obligations until the Agreements are executed, at which point Digital Energy shall be released.

**Nederlands:**

> 8.2 Overdracht. (a) Geen van de Partijen mag rechten of verplichtingen overdragen of cederen zonder voorafgaande schriftelijke toestemming. (b) Uitzondering: Digital Energy mag overdragen aan de ProjectBV na oprichting. Digital Energy blijft hoofdelijk aansprakelijk voor de verplichtingen van de ProjectBV totdat de Overeenkomsten zijn ondertekend, waarna Digital Energy wordt ontslagen.

#### §8.3 Governing Law

**English:**

> 8.3 Governing Law. These HoT and the Agreements are governed by Dutch law.

**Nederlands:**

> 8.3 Toepasselijk Recht. Op deze HoT en de Overeenkomsten is Nederlands recht van toepassing.

#### §8.4 Jurisdiction

**English:**

> 8.4 Jurisdiction. Disputes are submitted exclusively to the District Court of Amsterdam (Rechtbank Amsterdam).

**Nederlands:**

> 8.4 Bevoegde Rechter. Geschillen worden exclusief voorgelegd aan de Rechtbank Amsterdam.

#### §8.5 Dispute Resolution

**English:**

> 8.5 Dispute Resolution. Before initiating court proceedings, the Parties shall attempt to resolve disputes through good faith negotiations between senior executives for at least fifteen (15) business days.

**Nederlands:**

> 8.5 Geschillenbeslechting. Alvorens een gerechtelijke procedure te starten, trachten de Partijen geschillen op te lossen door te goeder trouw te onderhandelen tussen senior leidinggevenden gedurende ten minste vijftien (15) werkdagen.

#### §8.6 Entire Agreement

**English:**

> 8.6 Entire Agreement. These HoT constitute the entire agreement on this subject matter and supersede all prior negotiations and representations, except in the case of fraud or fraudulent misrepresentation.

**Nederlands:**

> 8.6 Volledige Overeenkomst. Deze HoT vormen de volledige overeenkomst over dit onderwerp en vervangen alle eerdere onderhandelingen en verklaringen, behalve in geval van fraude of frauduleuze misleiding.

#### §8.7 Amendments

**English:**

> 8.7 Amendments. Amendments require written agreement signed by both Parties.

**Nederlands:**

> 8.7 Wijzigingen. Wijzigingen vereisen schriftelijke overeenstemming ondertekend door beide Partijen.

#### §8.8 Waiver

**English:**

> 8.8 Waiver. No failure or delay in exercising any right shall operate as a waiver thereof, nor shall any single exercise preclude further exercise.

**Nederlands:**

> 8.8 Afstand van Recht. Het niet of vertraagd uitoefenen van enig recht houdt geen afstand daarvan in, noch zal enige eenmalige uitoefening verdere uitoefening uitsluiten.

#### §8.9 Severability

**English:**

> 8.9 Severability. If any provision is held invalid or unenforceable, the remaining provisions continue in full force. The Parties shall negotiate in good faith to replace the invalid provision with a valid provision achieving substantially the same effect.

**Nederlands:**

> 8.9 Scheidbaarheid. Indien enige bepaling ongeldig of niet-afdwingbaar wordt geacht, blijven de overige bepalingen volledig van kracht. De Partijen onderhandelen te goeder trouw om de ongeldige bepaling te vervangen door een geldige bepaling met in wezen hetzelfde effect.

#### §8.10 Force Majeure

**English:**

> 8.10 Force Majeure. Neither Party is liable for failure to perform due to events beyond its reasonable control, provided the affected Party: (a) notifies the other promptly; (b) uses commercially reasonable efforts to mitigate; and (c) resumes performance as soon as reasonably practicable.

**Nederlands:**

> 8.10 Overmacht. Geen van de Partijen is aansprakelijk voor het niet nakomen van verplichtingen als gevolg van gebeurtenissen buiten haar redelijke controle, mits de getroffen Partij: (a) de andere Partij onverwijld informeert; (b) commercieel redelijke inspanningen levert om de gevolgen te beperken; en (c) de nakoming zo spoedig als redelijkerwijs mogelijk hervat.

#### §8.11 Notices

**English:**

> 8.11 Notices. Notices must be in writing to the addresses in Annex A, Section G. Notices by email are deemed received on the next business day; notices by courier are deemed received upon confirmed delivery.

**Nederlands:**

> 8.11 Kennisgevingen. Kennisgevingen dienen schriftelijk te geschieden aan de adressen in Bijlage A, Sectie G. Kennisgevingen per e-mail worden geacht te zijn ontvangen op de volgende werkdag; kennisgevingen per koerier worden geacht te zijn ontvangen bij bevestigde aflevering.

#### §8.12 Third Party Rights

**English:**

> 8.12 Third Party Rights. These HoT do not confer any rights on third parties, except that ProjectBV (once incorporated) may enforce rights granted to it herein.

**Nederlands:**

> 8.12 Rechten van Derden. Deze HoT verlenen geen rechten aan derden, behalve dat de ProjectBV (na oprichting) de aan haar hierin verleende rechten kan afdwingen.

#### §8.13 Counterparts

**English:**

> 8.13 Counterparts. These HoT may be executed in counterparts, each deemed an original, together constituting one agreement. Electronic signatures have the same legal effect as original signatures.

**Nederlands:**

> 8.13 Exemplaren. Deze HoT kunnen in meerdere exemplaren worden ondertekend, waarbij elk exemplaar als origineel geldt en alle exemplaren samen één overeenkomst vormen. Elektronische handtekeningen hebben dezelfde rechtskracht als originele handtekeningen.

---

## 5. Recital B pillars — quick-reference table

> Full bodies of each pillar live in `recital_b_pillars.md`. This table is a summary of which pillars apply per role-archetype so engines can quickly determine which Recital B subsections to render.

| Pillar | Topic | Applies to (Site Partner role) | Asset-gate |
|---|---|---|---|
| B.1 | DEC developer capability (Digital Energy's track record, DBFO intent) | All | none |
| B.2 | Counterparty site capability (Grid / Land / Heat) | Role-gated: Grid Contributor ∧/∨ Landowner ∧/∨ Heat Offtaker | role-specific |
| B.3 | Mutual interest — Project thesis (DEC on counterparty site) | All | none |
| B.4 | Economic alignment (BESS JV, heat rev-share, dev-fee equity) | Grid Contributor (for BESS + heat rev-share); optional for other roles | `contribs_bess` OR `returns_heat` |
| B.5 | Asset-specific recitals (BESS, heat, grid, land, multi-location, separate contributions) | Asset-gated per Van Gog §§3.2–3.7 | per asset |

**Role-archetype defaults** (when all roles are held by one counterparty, as in Van Gog):

- **Grower-archetype HoT** (Grid + Land + Heat on one greenhouse operator): renders B.1, B.2 (all three), B.3, B.4 (full), B.5 (all assets gated by deal YAML).
- **Land-only Site Partner LOI** (Landowner only, no grid, no heat): renders B.1, B.2 (Landowner pillar only), B.3, skips B.4, B.5 reduced to land-only sub-recital.
- **Heat-only Site Partner LOI** (Heat Offtaker only): renders B.1, B.2 (Heat Offtaker pillar), B.3, B.4 (heat rev-share only), B.5 (heat sub-recital).
- **Grid-only Site Partner LOI** (Grid Contributor only, no land, no heat): renders B.1, B.2 (Grid pillar), B.3, B.4 (BESS JV only if `contribs_bess` present), B.5 (grid + BESS sub-recitals).

See `recital_b_pillars.md` for the verbatim EN + NL text of each pillar.

---

## 6. Versioning policy

Any change to EN or NL clause text in this file — even a single word — triggers the full template version bump process defined in `version-bump.md`:

1. **Minor bump** (e.g. `v1.0 → v1.1`) for non-substantive wording changes (e.g. "shall" ↔ "will", punctuation, clarifications that do not alter legal effect).
2. **Major bump** (e.g. `v1.0 → v2.0`) for substantive changes (e.g. change to the 2-year confidentiality tail, change to Dutch law / Amsterdam jurisdiction, change to 90-day HoT timeline, change to role definitions, introduction or removal of clauses).
3. **Both sides must be updated.** A change to LOI §6.1.6 (self-supersession) implies a review of HoT §7 and vice versa. Changes to shared clauses (§1, §2, §6.2, §6.4) require version bumps on both the LOI template and the HoT template.
4. **Bilingual review gate.** Any change to EN text requires a matching NL translation; any change to NL text requires a matching EN update. The reviewer set for bilingual changes is **Jelmer + Yoni + SAL + NL-native review** (per contract-review SOP). No clause ships with only one language changed.
5. **NL-native review.** For any clause carrying `[TBD_NL_TRANSLATION]` the NL text must be produced by a native-Dutch legal reviewer before the template is released as v1.0-final. Machine translation is not acceptable for binding HoT clauses.
6. **Source attribution.** Every clause in this file carries a "Source:" note pointing to the Van Gog LOI page or HoT body cell. When a clause is edited, the source note must be updated with the new source document + version.
7. **Log.** Every bump is logged in `template-version.md` for both templates with a one-line diff summary, date, reviewer names, and a link to the PR.

### 6.1 Clauses with `[TBD_NL_TRANSLATION]`

None. Every clause in this v1.0 file has both EN and NL verbatim text sourced directly from signed/execution-form Van Gog LOI (DocuSign envelope `CF30318B-72FC-42D5-AF94-2EDAB78CBB86`) or the grower HoT body DOCX (`hot-grower-body-v1.docx`). No clause is awaiting Dutch translation.

### 6.2 Change-review checklist

Before merging any edit to this file:

- [ ] EN text updated
- [ ] NL text updated to match
- [ ] Source attribution updated if source changed
- [ ] LOI template `DE-LOI-Site-v1.0_TEMPLATE.md` bumped if shared clause touched
- [ ] HoT template `DE-HoT-Site-v1.0_TEMPLATE.md` bumped if shared or HoT clause touched
- [ ] `template-version.md` entry added in both templates
- [ ] Jelmer + Yoni + SAL sign-off recorded
- [ ] NL-native review sign-off recorded (for any NL text change)
- [ ] `cross_doc_gate.py` test suite passes
- [ ] Golden-fixture regression (Van Gog LOI re-render bit-identical to committed golden) passes

---

— End of Site Clause Library —
