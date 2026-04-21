# DE-LOI-Site-v1.0 — Master Site LOI Template

**Version:** 1.0
**Derived from:** `DEC_LOI_Lodewijk_VanGog_DRAFT_v1.pdf` (DocuSigned 2026-04-14, envelope `CF30318B-72FC-42D5-AF94-2EDAB78CBB86`).
**Formality:** non-binding (Section 1–5) + binding (Section 6) per Van Gog §5.
**Language:** bilingual EN/NL side-by-side, rendered via `document-factory/bilingual_body.py`.
**Consumer:** `legal-assistant/sites/loi/generate_site_loi.py` (Phase D).

---

## Template consumption model

This file is the **master source**. Engine rendering:

1. Engine loads `{slug}/deal.yaml`.
2. For each section below:
   - If marked **always**, the engine renders it.
   - If marked **asset-gated**, the engine renders it only when the trigger condition on `deal.yaml` is true.
3. Placeholders `{{...}}` are substituted with data from `deal.yaml`.
4. Role labels are derived from `site_partners[].contributions[]` + `.returns[]` via `site_doc_base.derive_labels()`.
5. Bilingual clauses are rendered via `bilingual_body.render_bilingual_clause(doc, en_paragraphs=..., nl_paragraphs=..., heading=..., heading_nl=...)`.
6. Section R (roles + parties) and Section L (locations) are rendered as their own bilingual tables at the end.
7. Signature page is rendered via `signature_block.render_signature_page(doc, ...)` with `formality="non_binding"` (KvK omitted per Van Gog).

---

## Placeholder conventions

- `{{slug}}` — deal slug.
- `{{loi_date}}` — formatted date, e.g., "14-04-2026".
- `{{provider.legal_name}}`, `{{provider.address}}`, `{{provider.registration_type}}`, `{{provider.registration_number}}` — from `config/entities.yaml` (`de_nl`).
- `{{site_partners}}` — list; engine iterates.
  - `{{sp.legal_name}}`
  - `{{sp.signatory.name}}`, `{{sp.signatory.title}}`
  - `{{sp.role_labels_en}}`, `{{sp.role_labels_nl}}` — derived.
- `{{addons.bess_co_development}}` — bool; activates §3.2.
- `{{locations}}` — list rendered in Section L.
- `{{any(sp, contribs[asset=X])}}` — shorthand: true if any partner contributes asset X. Used for §3.3–§3.5 activation.
- `{{any(sp, returns[value=Y])}}` — similar for return-value gating.
- Fallback for enrichment-target values: `[TBC]` rendered in-place.

---

## Cover page

*Rendered by document-factory `add_cover()` with `bilingual=True` extension.*

**Monolingual title block:**
```
Letter of Intent / Intentieverklaring
for a Digital Energy Center Project / voor een Digital Energy Center-project
```

**Parties block (Between / And format per memory rule `feedback_agreement_format.md`):**
```
between / tussen
{{provider.legal_name}}
and / en
{{#each site_partners}}
{{this.legal_name}}   # one line per Site Partner
{{/each}}

Date / Datum: {{loi_date}}
```

**Cover footer:** drops "Confidential" prefix per memory rule `feedback_cover_page_title.md`.

---

## Section 1 — Parties / Partijen    *(always rendered)*

Heading EN: `1. Parties` | Heading NL: `1. Partijen`

### 1.1 Digital Energy definition

**EN:**
```
1.1 {{provider.legal_name}}, a private limited company (besloten
vennootschap met beperkte aansprakelijkheid) incorporated under Dutch law,
registered with the Dutch Chamber of Commerce under number
{{provider.registration_number}}, with its registered office at
{{provider.address}}, including its permitted successors and assigns
("Digital Energy").
```

**NL:**
```
1.1 {{provider.legal_name}}, een besloten vennootschap met beperkte
aansprakelijkheid opgericht naar Nederlands recht, geregistreerd bij de
Kamer van Koophandel onder nummer {{provider.registration_number}}, met
statutaire zetel aan {{provider.address}}, Nederland, met inbegrip van
haar toegestane rechtsopvolgers en rechtverkrijgenden ("Digital Energy").
```

### 1.2 Site Partner definition

**EN:**
```
1.2 The counterparty or counterparties identified in the LOI Schedule
(Section R), with the registered particulars specified therein, including
its or their permitted successors and assigns (each a "Site Partner" and,
if more than one, collectively the "Site Partners").
```

**NL:**
```
1.2 De wederpartij of wederpartijen vermeld in de Bijlage (Sectie R), met
de statutaire gegevens daarin vermeld, met inbegrip van haar of hun
toegestane rechtsopvolgers en rechtverkrijgenden (elk een "Locatiepartner"
en, indien meer dan een, gezamenlijk de "Locatiepartners").
```

### 1.3 Party / Parties

**EN:**
```
1.3 Digital Energy and each Site Partner are each referred to as a "Party"
and together as the "Parties".
```

**NL:**
```
1.3 Digital Energy en elke Locatiepartner worden afzonderlijk aangeduid
als "Partij" en gezamenlijk als "Partijen".
```

### 1.4 Role assignment

**EN:**
```
1.4 The LOI Schedule assigns each Site Partner one or more roles:
Grid Contributor (the party providing or applying for the electrical grid
connection), Landowner (the party providing land for the DEC), and Heat
Offtaker (the party receiving the waste heat). Where this LOI refers to a
specific role, the obligation applies only to the Site Partner designated
for that role in Section R.
```

**NL:**
```
1.4 De Bijlage wijst aan elke Locatiepartner een of meer rollen toe:
Netbijdrager (de partij die de elektrische netaansluiting verschaft of
aanvraagt), Grondeigenaar (de partij die grond beschikbaar stelt voor het
DEC), en Warmteafnemer (de partij die de restwarmte ontvangt). Waar deze
LOI verwijst naar een specifieke rol, geldt de verplichting uitsluitend
voor de Locatiepartner die voor die rol is aangewezen in Sectie R.
```

---

## Section 2 — Background and Purpose / Achtergrond en Doel    *(always rendered)*

### 2.1 DEC definition

**EN:** `2.1 Digital Energy has developed the Digital Energy Center ("DEC"), which captures and reuses waste heat from AI-computing data centers.`
**NL:** `2.1 Digital Energy heeft het Digital Energy Center ("DEC") ontwikkeld, dat restwarmte van AI-datacenters opvangt en hergebruikt.`

### 2.2 Project scope statement

**EN:**
```
2.2 The Parties wish to explore the development of a DEC project (the
"Project") at the location(s) specified in the LOI Schedule (Section L).
The roles and asset contributions are as set out in Section R. The Project
is intended to be implemented through a project-specific limited liability
company (besloten vennootschap met beperkte aansprakelijkheid) to be
incorporated by Digital Energy as the special-purpose vehicle for the
Project ("ProjectBV") and the Site Partner(s).
```

**NL:**
```
2.2 De Partijen wensen de ontwikkeling van een DEC-project (het "Project")
te verkennen op de locatie(s) vermeld in de Bijlage (Sectie L). De rollen
en activa-bijdragen zijn uiteengezet in Sectie R. Het Project is bedoeld
om te worden uitgevoerd via een projectspecifieke besloten vennootschap
met beperkte aansprakelijkheid die door Digital Energy zal worden opgericht
als special purpose vehicle voor het Project ("ProjectBV") en de
Locatiepartner(s).
```

---

## Section 3 — Project Overview / Projectoverzicht

Heading EN: `3. Project Overview` | Heading NL: `3. Projectoverzicht`

### 3.1 DEC Development / DEC-ontwikkeling    *(always rendered)*

**EN:**
```
Digital Energy intends to design, build, finance, and operate a DEC at the
Project location(s). Digital Energy expects to bear the cost and risk of
the DEC, including, at the end of the term, removal and site restoration.
The DEC is expected to be owned and operated by the ProjectBV.
```

**NL:**
```
Digital Energy is voornemens een DEC te ontwerpen, bouwen, financieren en
exploiteren op de projectlocatie(s). Digital Energy verwacht de kosten en
het risico van het DEC te dragen, met inbegrip van verwijdering en
locatieherstel aan het einde van de looptijd. Het DEC zal naar verwachting
eigendom zijn van en worden geëxploiteerd door de ProjectBV.
```

### 3.2 BESS Co-Development / BESS Co-Ontwikkeling    *(asset-gated: `addons.bess_co_development == true`)*

**EN:**
```
The Parties anticipate that the Project will include the co-development of
a Battery Energy Storage System ("BESS") as an initial development phase.
The BESS is intended to utilise the Grid Contributor's electrical
connections as described in the LOI Schedule (Section L) and to be located
on the Landowner's property. The anticipated configuration is approximately
{{contribs_bess.mw}} MW / {{contribs_bess.mwh}} MWh utilising
{{contribs_bess.chemistry}} technology, subject to detailed engineering
and procurement.

The BESS is intended as a joint investment between Digital Energy and the
Grid Contributor. The Parties anticipate a
{{contribs_bess.co_invest_pct}}/{{100-contribs_bess.co_invest_pct}} equity
joint venture structure, with the BESS to be owned and operated by a
dedicated BESS SPV. The BESS is expected to generate revenue from energy
arbitrage, frequency containment reserve (FCR), and other ancillary
services on the Dutch electricity balancing market.

The BESS is intended to be operational prior to the DEC, providing the
Grid Contributor with standalone investment returns before the DEC
development phase commences. At DC financial close, the Parties anticipate
that the Grid Contributor's BESS equity interest will convert to an equity
interest in the ProjectBV, with the conversion terms to be agreed in the HoT.

All BESS terms, including final capacity, total investment, equity and
debt structure, revenue arrangements, grid-sharing with the DEC,
operational management, and equity conversion mechanics, are to be agreed
in the HoT.
```

**NL:**
```
De Partijen voorzien dat het Project de gezamenlijke ontwikkeling omvat van
een Battery Energy Storage System ("BESS") als initiële ontwikkelingsfase.
Het BESS is bedoeld om de elektrische aansluitingen van de Netbijdrager te
benutten zoals beschreven in de Bijlage (Sectie L) en te worden
gesitueerd op het eigendom van de Grondeigenaar. De beoogde configuratie
is circa {{contribs_bess.mw}} MW / {{contribs_bess.mwh}} MWh gebruikmakend
van {{contribs_bess.chemistry}}-technologie, onder voorbehoud van
gedetailleerde engineering en inkoop.

Het BESS is bedoeld als gezamenlijke investering tussen Digital Energy en
de Netbijdrager. De Partijen voorzien een joint-venture-aandelenstructuur
van {{contribs_bess.co_invest_pct}}/{{100-contribs_bess.co_invest_pct}},
waarbij het BESS eigendom zal zijn van en wordt geëxploiteerd door een
speciaal daarvoor opgerichte BESS-SPV. Het BESS zal naar verwachting
inkomsten genereren uit energie-arbitrage, frequentiereserve (FCR) en
andere ondersteunende diensten op de Nederlandse elektriciteitsbalanceringsmarkt.

Het BESS is bedoeld om operationeel te zijn vóór het DEC, waardoor de
Netbijdrager zelfstandige investeringsrendementen ontvangt voordat de
DEC-ontwikkelingsfase aanvangt. Bij financial close van het DC voorzien
de Partijen dat het BESS-aandelenbelang van de Netbijdrager wordt
omgezet in een aandelenbelang in de ProjectBV, met de conversievoorwaarden
overeen te komen in de HoT.

Alle BESS-voorwaarden, waaronder definitieve capaciteit, totale
investering, eigen vermogen- en schuldstructuur, opbrengstregelingen,
netdeling met het DEC, operationeel beheer en conversievoorwaarden, zijn
overeen te komen in de HoT.
```

### 3.3 Heat Supply / Warmtelevering    *(asset-gated: `any(sp, returns[value=energy_heat])`)*

**EN:**
```
The Project's objective includes recovering and supplying waste heat from
the DEC to the Heat Offtaker designated in Section R. The DEC converts
electricity into compute capacity and, as a by-product, generates thermal
energy. The facility is designed to capture this heat and deliver it to
the adjacent Heat Offtaker's agricultural operations via a direct pipeline
connection, replacing conventional gas-fired heating.

The Parties anticipate that the heat supply will be formalised through a
long-term heat offtake agreement between the ProjectBV and the Heat
Offtaker, with pricing indexed to inflation (CPI). The specific heat
supply terms, including price per MWh, volume commitments, delivery
specifications, indexation mechanism, minimum offtake obligations, credit
support, and contract duration, are to be agreed in the HoT.

The Parties anticipate that the economic benefit of the heat revenue will
be shared between Digital Energy and the Grid Contributor, in recognition
of the Grid Contributor's contribution of the electrical grid connections
that enable the DEC's operations. The terms of such revenue sharing are
to be agreed in the HoT.
```

**NL:**
```
Het Project heeft mede tot doel restwarmte van het DEC terug te winnen en
te leveren aan de Warmteafnemer aangewezen in Sectie R. Het DEC zet
elektriciteit om in rekencapaciteit en genereert als bijproduct thermische
energie. De installatie is ontworpen om deze warmte op te vangen en via
een directe pijpleidingverbinding te leveren aan de aangrenzende agrarische
activiteiten van de Warmteafnemer, ter vervanging van conventionele
gasgestookte verwarming.

De Partijen voorzien dat de warmtelevering wordt geformaliseerd door
middel van een langlopende warmteafnameovereenkomst tussen de ProjectBV
en de Warmteafnemer, met prijsindexatie aan inflatie (CPI). De specifieke
warmteleveringsvoorwaarden, waaronder prijs per MWh, volumeverplichtingen,
leveringsspecificaties, indexatiemechanisme, minimale afnameverplichtingen,
kredietondersteuning en contractduur, zijn overeen te komen in de HoT.

De Partijen voorzien dat het economisch voordeel van de warmteopbrengst
wordt gedeeld tussen Digital Energy en de Netbijdrager, ter erkenning van
de bijdrage van de Netbijdrager in de elektrische netaansluitingen die de
werking van het DEC mogelijk maken. De voorwaarden van een dergelijke
opbrengstverdeling zijn overeen te komen in de HoT.
```

### 3.4 Grid Connection / Netaansluiting    *(asset-gated: `any(sp, contribs[asset=grid_interconnection])`)*

**EN:** *(brief; specifics deferred to HoT)*
```
The Parties anticipate that the Grid Contributor will make available
(through sharing, transfer, or new-connection application as determined in
Section R) the electrical grid connection(s) required for the DEC's
operation. The specific connection arrangement terms, including capacity
reservation, cost allocation, and transfer or sharing instrument, are to
be determined in the HoT.
```

**NL:**
```
De Partijen voorzien dat de Netbijdrager de voor de werking van het DEC
benodigde elektrische netaansluiting(en) beschikbaar zal stellen (via
deling, overdracht of nieuwe aansluitaanvraag zoals bepaald in Sectie R).
De specifieke aansluitvoorwaarden, waaronder capaciteitsreservering,
kostenverdeling en overdrachts- of deelinstrument, worden vastgelegd in
de HoT.
```

### 3.5 Land / Grond    *(asset-gated: `any(sp, contribs[asset=land])`)*

**EN:**
```
Where a Site Partner provides land, the Parties contemplate that the
Landowner would make land available for the DEC, to be secured by a right
of superficies (recht van opstal) or similar arrangement under Dutch law.
The anticipated land area for a DEC is approximately 300 m² per MW of
electrical capacity. The terms and conditions of any such land
arrangement, including any fee or compensation, are to be determined in
the HoT.
```

**NL:**
```
Waar een Locatiepartner grond beschikbaar stelt, beogen de Partijen dat de
Grondeigenaar grond ter beschikking stelt voor het DEC, te verzekeren door
een recht van opstal of vergelijkbare regeling naar Nederlands recht. De
verwachte grondoppervlakte voor een DEC bedraagt circa 300 m² per MW
elektrisch vermogen. De voorwaarden van een dergelijke grondregeling, met
inbegrip van eventuele vergoeding of compensatie, worden vastgelegd in de
HoT.
```

### 3.6 Multiple Locations / Meerdere Locaties    *(always rendered)*

**EN:**
```
The Project may comprise one or more locations as listed in Section L of
the LOI Schedule. Digital Energy will assess each location and the Parties
will agree in the HoT which locations (if any) proceed to development.
```

**NL:**
```
Het Project kan een of meer locaties omvatten zoals vermeld in Sectie L
van de Bijlage. Digital Energy zal elke locatie beoordelen en de Partijen
zullen in de HoT overeenkomen welke locaties (indien van toepassing) tot
ontwikkeling overgaan.
```

### 3.7 Separate Contributions / Afzonderlijke Bijdragen    *(rendered when `len(site_partners) > 1`)*

**EN:**
```
Where different Site Partners fill different roles as designated in
Section R, Digital Energy shall coordinate the integration of the
respective contributions.
```

**NL:**
```
Waar verschillende Locatiepartners verschillende rollen vervullen zoals
aangewezen in Sectie R, zal Digital Energy de integratie van de respectieve
bijdragen coördineren.
```

### 3.8 Term / Looptijd    *(always rendered)*

**EN:** `The Parties contemplate an initial term of thirty (30) years with automatic renewal periods.`
**NL:** `De Partijen beogen een initiële looptijd van dertig (30) jaar met automatische verlengingsperioden.`

### 3.9 Costs / Kosten    *(always rendered)*

**EN:**
```
Each Party bears its own costs in connection with this LOI and the
pre-feasibility assessment. For the avoidance of doubt, neither Party is
entitled to reimbursement of any costs from any other Party in connection
with this LOI or the pre-feasibility assessment. Digital Energy expects to
finance the DEC and the ProjectBV.
```

**NL:**
```
Elke Partij draagt haar eigen kosten in verband met deze LOI en het
pre-haalbaarheidsonderzoek. Voor de duidelijkheid, geen der Partijen heeft
recht op vergoeding van kosten van een andere Partij in verband met deze
LOI of het pre-haalbaarheidsonderzoek. Digital Energy verwacht het DEC en
de ProjectBV te financieren.
```

---

## Section 4 — Pre-Feasibility & HoT Timeline    *(always rendered)*

Heading EN: `4. Pre-Feasibility Assessment and HoT` | Heading NL: `4. Pre-haalbaarheidsonderzoek en HoT`

### 4.1 Pre-feasibility purpose

**EN:**
```
Digital Energy intends to conduct a pre-feasibility assessment covering,
among other matters, electrical engineering, thermal integration, site
planning, heat-demand analysis, site investigation(s), and any
location-specific assessments.
```

**NL:**
```
Digital Energy is voornemens een pre-haalbaarheidsonderzoek uit te voeren
dat onder meer betrekking heeft op elektrotechniek, thermische integratie,
locatieplanning, warmtevraaganalyse, locatieonderzoek(en) en eventuele
locatiespecifieke beoordelingen.
```

### 4.2 HoT invitation + Variable Schedule + data carry-forward

**EN:**
```
If the pre-feasibility assessment is positive, Digital Energy expects to
invite the Site Partner(s) to enter into binding HoT. It is anticipated
that the HoT would include an exclusivity period during which the relevant
Site Partner(s) would be expected to refrain from entering into
arrangements that would conflict with the Project. The HoT is also expected
to include a Variable Schedule specifying site-specific and deal-specific
parameters. Data provided in the LOI Schedule carries forward to the HoT
where applicable. The HoT is expected to address, among other matters, the
BESS co-development terms, heat supply arrangements, grid connection
allocation, development fee structure, and land access conditions.
```

**NL:** *(verbatim from Van Gog §4.2 NL column)*

### 4.3 90-day target

**EN:**
```
Target timeline: execution of the HoT within ninety (90) days of this LOI,
subject to satisfactory pre-feasibility assessment, Digital Energy's
timely completion thereof, and the Site Partner(s)' reasonable cooperation.
```

**NL:**
```
Streeftijdlijn: ondertekening van de HoT binnen negentig (90) dagen na
deze LOI, onder voorbehoud van een bevredigend pre-haalbaarheidsonderzoek,
tijdige afronding daarvan door Digital Energy, en redelijke medewerking
van de Locatiepartner(s).
```

### 4.4 Site access cooperation

**EN:**
```
Each Site Partner intends, subject to reasonable advance notice and its
operational requirements, to provide Digital Energy and its advisors
access to the relevant site(s) and technical documentation relevant to
the assets described in the LOI Schedule during normal business hours, to
support the pre-feasibility assessment.
```

**NL:** *(verbatim from Van Gog §4.4 NL column)*

---

## Section 5 — Term of this LOI / Looptijd van deze LOI    *(always rendered)*

**EN:**
```
This LOI enters into force on the date of signature by the last Party and
continues until the earlier of (a) the execution of the HoT; or (b) twelve
(12) months from the last-signature date, unless extended by written
agreement of the Parties. Upon expiry, all obligations cease except
Section 6.1 (Confidentiality) and Section 6.2 (Governing Law and
Jurisdiction), which survive in accordance with their terms.
```

**NL:** *(derived from Van Gog §5 NL column, adapted for parameterized 12-month validity)*

---

## Section 6 — Binding Provisions / Bindende Bepalingen    *(ALWAYS RENDERED; this is the binding anchor)*

### 6.1 Confidentiality / Vertrouwelijkheid

*Render sub-clauses 6.1.1 through 6.1.6 verbatim from Van Gog §6.1. The
critical self-supersession clause 6.1.6 MUST be preserved verbatim in both
EN and NL because it is the design-of-record mechanism that makes a HoT
confidentiality clause non-redundant with LOI confidentiality.*

### 6.2 Governing Law and Jurisdiction / Toepasselijk Recht en Bevoegde Rechter

Verbatim from Van Gog §6.2: Dutch law + District Court of Amsterdam.

### 6.3 Information Right / Informatierecht

Verbatim from Van Gog §6.3, including the role-specific sub-clauses:
- (a) Grid Contributor notification duty
- (b) Landowner notification duty
- (c) Heat Offtaker notification duty

### 6.4 Miscellaneous / Diversen

Verbatim from Van Gog §6.4: severability, amendments-in-writing, GDPR, IP
non-grant, EN-prevails-over-NL.

*Full EN+NL source text for §6.1–§6.4 is maintained in*
`sites/_shared/site_clause_library.md` *to avoid duplication. The LOI
engine pulls from there at render time.*

---

## Section 7 — Execution / Ondertekening    *(always rendered)*

**EN:** `Each signatory represents and warrants that they have full authority to execute this LOI on behalf of the Party they represent.`
**NL:** `Elke ondertekenaar verklaart en garandeert dat hij/zij volledig bevoegd is om deze LOI te ondertekenen namens de Partij die hij/zij vertegenwoordigt.`

Closing line: `LOI Schedule: integral part / Bijlage: integraal onderdeel`

---

## Section L — Locations / Locaties    *(rendered as a schedule table)*

Bilingual table with columns:
- EN: `Location | Address | Parcel (Kadaster) | DSO | Municipality | Zoning`
- NL: `Locatie | Adres | Kadaster-referentie | Netbeheerder | Gemeente | Bestemming`

One row per entry in `deal.locations[]`. Values default to `[TBC]` when
enrichment targets are unresolved at LOI stage.

---

## Section R — Roles + Parties Schedule    *(rendered as a schedule table)*

For each Site Partner, produce one bilingual panel listing:
- Legal name + KvK (if known, optional at LOI)
- Registered address
- Signatory name + title
- Role labels (derived) — EN and NL
- Contributions (asset, instrument, key details) — per-contribution sub-row
- Returns (value, instrument, key details) — per-return sub-row

The render order mirrors the signature-page order. Engine groups
contributions + returns together under each partner so the bankable
structure is visible at a glance.

---

## Signature page    *(rendered via `signature_block.render_signature_page(...)`)*

Call with:
- `provider_party=DE_ENTITIES["nl"]`
- `site_partners=[SigParty(...)` for each Site Partner; role labels
  derived via `site_doc_base.derive_labels()`
- `formality="non_binding"` — **KvK is omitted from LOI signature blocks
  per Van Gog pattern**; KvK appears only in HoT signature blocks.
- `provider_signatory_name` / `provider_signatory_title` — from intake
  override or blank for manual fill.

---

## Engine contract (Phase D `generate_site_loi.py`)

1. Load `{slug}/deal.yaml`; validate `deal_yaml_schema_version == "1.0"`.
2. Call `site_doc_base.derive_labels()` on each Site Partner — attach
   `role_labels_en` and `role_labels_nl` to each.
3. Call `document-factory.add_cover(bilingual=True, ...)` for the cover.
4. For each section above:
   - Check asset-gate condition against `deal.yaml`.
   - If passes, render bilingual clause via
     `document-factory.bilingual_body.render_bilingual_clause(...)`.
   - Substitute `{{placeholders}}` before rendering.
5. Render Section L and Section R tables.
6. Render signature page via
   `document-factory.signature_block.render_signature_page(...)`.
7. Write `.docx` to `/tmp/YYYYMMDD_DE_LOI_Site_{slug}_v1_(DRAFT).docx`.
8. Run `document-factory.format_validators.run_all(doc)` post-assembly;
   write results to `_qa.txt`.
9. Hand off to `sites/_shared/output_router.route(artifact)` for Drive
   placement under `{Counterparty}_Project_Benelux_Ops/drafts/`.

---

## Versioning

Any change to clause text (EN or NL) is a **template version bump**
requiring the full Jelmer/Yoni/SAL + NL-native review cadence per
`version-bump.md`. Placeholder-list changes and engine-integration
changes can land without template version bump so long as no rendered
text changes.
