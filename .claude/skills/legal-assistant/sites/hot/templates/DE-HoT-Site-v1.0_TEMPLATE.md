# DE-HoT-Site-v1.0 — Master Site HoT Template

**Version:** 1.0
**Derived from:** `hot-grower-body-v1.docx` (legally-locked bilingual EN/NL body, 9 sections, ~35 clauses; see `template-version.md`).
**Formality:** **BINDING in its entirety** — all sections 1–8 are legally binding (contrast: LOI §1–§5 non-binding, LOI §6 binding).
**Language:** bilingual EN/NL side-by-side, rendered via `document-factory/bilingual_body.py`.
**Consumer:** `legal-assistant/sites/hot/generate_site_hot.py` (Phase C — to be built).
**Sibling:** `sites/loi/templates/DE-LOI-Site-v1.0_TEMPLATE.md` (mirrors this structure for the LOI stage).

---

## Template consumption model

This file is the **master source**. Engine rendering flow:

1. Engine loads `{slug}/deal.yaml` (same schema as the LOI engine; `deal_yaml_schema_version == "1.0"`).
2. For each clause below:
   - If marked **always**, the engine renders it.
   - If marked **asset-gated**, the engine renders it only when the trigger condition on `deal.yaml` (or `addons.*` / `site_partners[].contributions[]`) is true.
3. Placeholders `{{...}}` are substituted with data from `deal.yaml` and `config/entities.yaml`.
4. Role labels are derived from `site_partners[].contributions[]` + `.returns[]` via `sites/_shared/site_doc_base.derive_labels()` — identical to the LOI path.
5. Bilingual clauses are rendered via `document-factory.bilingual_body.render_bilingual_clause(doc, en_paragraphs=..., nl_paragraphs=..., heading=..., heading_nl=...)`.
6. After §8, the engine **appends Annex A** by calling `hot-intake` / `annex-fill` routines that populate `hot-grower-annex-a-v1.docx` fields (A–G, plus 16 supporting-documents rows) from `deal.yaml`. The Annex is an integral part of the HoT per the closing line in `hot-grower-body-v1.docx`.
7. Signature page is rendered via `document-factory.signature_block.render_signature_page(doc, ...)` with **`formality="binding"`** — this triggers KvK inclusion per the Van Gog binding pattern (KvK appears in HoT signature blocks, omitted in LOI ones) and per field-registry A.2 (KvK is required for binding execution).
8. `document-factory.format_validators.run_all(doc)` runs post-assembly; results land in `_qa.txt`.
9. Artifact handed off to `sites/_shared/output_router.route(artifact)` for Drive placement under `{Counterparty}_Project_Benelux_Ops/drafts/`.

---

## Placeholder conventions

Identical to the LOI template — single source of truth across LOI and HoT.

- `{{slug}}` — deal slug.
- `{{hot_date}}` — formatted date, `DD-MM-YYYY`. Used in cover and §3.6 (Effective Date).
- `{{provider.legal_name}}`, `{{provider.registration_type}}`, `{{provider.registration_number}}`, `{{provider.address}}` — from `config/entities.yaml`. For the grower HoT body template, the provider is **Digital Energy Group AG** (Swiss), not the Dutch entity — verbatim per §1.1 of the locked body. See §1 below for the exact default.
- `{{site_partners}}` — list; engine iterates. Each site partner exposes:
  - `{{sp.legal_name}}`, `{{sp.kvk_number}}`, `{{sp.registered_address}}`
  - `{{sp.signatory.name}}`, `{{sp.signatory.title}}`, `{{sp.signatory.authority}}` (Sole / Joint)
  - `{{sp.role_labels_en}}`, `{{sp.role_labels_nl}}` — derived.
- `{{any(sp, contribs[asset=X])}}` — shorthand: true if any partner contributes asset X. Used for asset-gating §4 and §5 sub-clauses.
- `{{any(sp, returns[value=Y])}}` — similar for return-value gating.
- `{{addons.bess_co_development}}` — bool; activates BESS-specific language in §4.5.
- `{{annex_a.items.<id>}}` — e.g., `{{annex_a.items.A1_legal_name}}`. For any clause that references an Annex A item (such as "Item A.7" or "Item C.1"), the engine renders the literal pointer text `Annex A, Item <id>` and defers value resolution to the Annex rendering step.
- Fallback for enrichment-target values: `[TBC]` rendered in-place.

---

## Cover page

*Rendered by document-factory `add_cover()` with `bilingual=True` extension.*

**Monolingual title block (bilingual stacked):**
```
Binding Heads of Terms / Bindende Contractvoorwaarden
for / voor
Digital Energy Center Project
```

**Parties block (Between / And format per memory rule `feedback_agreement_format.md`):**
```
between / tussen
Digital Energy Group AG
and / en
{{#each site_partners}}
{{this.legal_name}}   # one line per Site Partner; in grower HoT, the Grower from Annex A Item A.1
{{/each}}

Date / Datum: {{hot_date}}
```

**Cover footer:** drops "Confidential" prefix per memory rule `feedback_cover_page_title.md` (the HoT is confidential by operation of §7, but the cover chrome does not repeat it).

**Cover title rule:** title names the primary document type only — "Binding Heads of Terms" — no secondary labels on the cover (per `feedback_cover_page_title.md`).

---

## Section 1 — Parties / Partijen    *(always rendered — BINDING)*

Heading EN: `1. Parties` | Heading NL: `1. Partijen`

### 1.1 Digital Energy definition

**EN:**
```
1.1 Digital Energy Group AG, a company incorporated under Swiss law,
registered under CHE-408.639.320, with its registered office at
Baarerstrasse 43, 6300 Zug, Switzerland, including its permitted successors
and assigns ("Digital Energy").
```

**NL:**
```
1.1 Digital Energy Group AG, een vennootschap opgericht naar Zwitsers
recht, geregistreerd onder CHE-408.639.320, met statutaire zetel aan
Baarerstrasse 43, 6300 Zug, Zwitserland, met inbegrip van haar toegestane
rechtsopvolgers en rechtverkrijgenden ("Digital Energy").
```

### 1.2 Grower / Site Partner definition

*In the grower variant of the HoT body template, the counterparty is the "Grower". The generator retains the term "Grower" verbatim to match the locked body template. Where a non-greenhouse Site Partner executes the HoT in a future variant, a variant body template is required; this template is the grower variant only.*

**EN:**
```
1.2 The company identified in Annex A, Item A.1, a Dutch private limited
company (besloten vennootschap), registered with the Trade Register (Kamer
van Koophandel) under the number in Item A.2, with its registered office
at the address in Item A.3, including its permitted successors and assigns
("Grower").
```

**NL:**
```
1.2 De vennootschap vermeld in Bijlage A, Punt A.1, een besloten
vennootschap met beperkte aansprakelijkheid, ingeschreven bij de Kamer van
Koophandel onder het nummer in Punt A.2, met statutaire zetel op het adres
in Punt A.3, met inbegrip van haar toegestane rechtsopvolgers en
rechtverkrijgenden ("Teler").
```

### 1.3 Party / Parties

**EN:**
```
1.3 Digital Energy and the Grower are each referred to as a "Party" and
together as the "Parties".
```

**NL:**
```
1.3 Digital Energy en de Teler worden afzonderlijk aangeduid als "Partij"
en gezamenlijk als "Partijen".
```

---

## Section 2 — Recitals / Overwegingen    *(always rendered — BINDING)*

Heading EN: `2. Recitals` | Heading NL: `2. Overwegingen`

### 2.1 Grower ownership and greenhouse operation

**EN:**
```
2.1 The Grower owns and operates a greenhouse facility at the location
specified in Annex A, Item A.7, with a current size per Item A.8 and
planned expansion per Items A.9–A.10, used for the cultivation specified
in Item A.11 and requiring industrial-scale heating for horticultural
operations.
```

**NL:**
```
2.1 De Teler bezit en exploiteert een glastuinbouwbedrijf op de locatie
vermeld in Bijlage A, Punt A.7, met een huidige oppervlakte conform Punt
A.8 en geplande uitbreiding conform Punten A.9–A.10, gebruikt voor de
teelt vermeld in Punt A.11 en waarvoor industriële tuinbouwverwarming
nodig is.
```

### 2.2 DEC definition

**EN:**
```
2.2 Digital Energy has developed the Digital Energy Center ("DEC"), which
captures and reuses waste heat from AI-computing data centers.
```

**NL:**
```
2.2 Digital Energy heeft het Digital Energy Center ("DEC") ontwikkeld, dat
restwarmte van AI-datacenters opvangt en hergebruikt.
```

---

## Section 3 — Binding Nature and Exclusivity / Bindende Aard en Exclusiviteit    *(always rendered — BINDING; this is the commercial lock)*

Heading EN: `3. Binding Nature and Exclusivity` | Heading NL: `3. Bindende Aard en Exclusiviteit`

### 3.1 Binding Effect / Bindend Karakter

**EN:**
```
3.1 Binding Effect. These Heads of Terms ("HoT") constitute a legally
binding agreement. The Parties shall negotiate, prepare, and execute
definitive agreements ("Agreements") in good faith and in accordance with
the terms herein.
```

**NL:**
```
3.1 Bindend Karakter. Deze Contractvoorwaarden ("HoT") vormen een juridisch
bindende overeenkomst. De Partijen zullen te goeder trouw en overeenkomstig
de hierin opgenomen voorwaarden definitieve overeenkomsten
("Overeenkomsten") onderhandelen, voorbereiden en uitvoeren.
```

### 3.2 Obligation to Sign / Ondertekeningsverplichting

**EN:**
```
3.2 Obligation to Sign. Both Parties commit to finalize and sign the
Agreements before expiry of the Exclusivity Period, unless a Valid
Withdrawal Event occurs and is properly invoked in accordance with Section 3.4.
```

**NL:**
```
3.2 Ondertekeningsverplichting. Beide Partijen verplichten zich de
Overeenkomsten te finaliseren en te ondertekenen vóór het verstrijken van
de Exclusiviteitsperiode, tenzij een Geldige Terugtrekkingsgrond zich
voordoet en naar behoren wordt ingeroepen overeenkomstig Artikel 3.4.
```

### 3.3 Valid Withdrawal Events / Geldige Terugtrekkingsgronden

**EN:**
```
3.3 Valid Withdrawal Events. A "Valid Withdrawal Event" means any of the
following circumstances, to the extent not already addressed herein and
not caused by the withdrawing Party's breach: (a) failure to secure
financing on terms consistent with the Project's financial assumptions;
(b) an increase in Project costs exceeding 20% of the budgeted costs as at
the Effective Date; (c) failure to obtain necessary regulatory approvals
or permits; (d) failure to obtain DSO (netbeheerder) authorization; or
(e) failure to obtain SDE++ subsidy.
```

**NL:**
```
3.3 Geldige Terugtrekkingsgronden. Een "Geldige Terugtrekkingsgrond"
betekent een van de volgende omstandigheden, voor zover niet reeds hierin
geadresseerd en niet veroorzaakt door een tekortkoming van de zich
terugtrekkende Partij: (a) het niet verkrijgen van financiering op
voorwaarden die consistent zijn met de financiële uitgangspunten van het
Project; (b) een stijging van de Projectkosten met meer dan 20% van de
begrote kosten per de Ingangsdatum; (c) het niet verkrijgen van
noodzakelijke goedkeuringen of vergunningen; (d) het niet verkrijgen van
goedkeuring van de netbeheerder ("DSO"); of (e) het niet verkrijgen van
SDE++-subsidie.
```

### 3.4 Withdrawal Procedure / Terugtrekkingsprocedure

**EN:**
```
3.4 Withdrawal Procedure. A Party invoking a Valid Withdrawal Event shall:
(a) provide written notice to the other Party within fourteen (14) days of
becoming aware of such event, together with reasonable supporting evidence;
and (b) if the event is capable of remedy, first use commercially reasonable
efforts to remedy it within thirty (30) days before withdrawing.
```

**NL:**
```
3.4 Terugtrekkingsprocedure. Een Partij die een Geldige Terugtrekkingsgrond
inroept, dient: (a) de andere Partij binnen veertien (14) dagen na
kennisneming van een dergelijke gebeurtenis schriftelijk in kennis te
stellen, samen met redelijke ondersteunende documentatie; en (b) indien de
gebeurtenis voor herstel vatbaar is, eerst gedurende dertig (30) dagen
commercieel redelijke inspanningen te verrichten om deze te verhelpen
alvorens zich terug te trekken.
```

### 3.5 Withdrawal Consequences / Gevolgen van Terugtrekking

**EN:**
```
3.5 Withdrawal Consequences. Upon valid invocation of a Valid Withdrawal
Event in accordance with Section 3.4, the affected Party may terminate
these HoT by written notice. Upon such termination, neither Party shall
have further obligations hereunder, except that Sections 7 (Confidentiality)
and 8 (General Provisions) shall survive.
```

**NL:**
```
3.5 Gevolgen van Terugtrekking. Bij geldige inroeping van een Geldige
Terugtrekkingsgrond overeenkomstig Artikel 3.4, kan de betrokken Partij
deze HoT beëindigen door middel van schriftelijke kennisgeving. Na een
dergelijke beëindiging hebben de Partijen geen verdere verplichtingen uit
hoofde hiervan, met dien verstande dat Artikel 7 (Vertrouwelijkheid) en
Artikel 8 (Algemene Bepalingen) van kracht blijven.
```

### 3.6 Exclusivity Period / Exclusiviteitsperiode

**EN:**
```
3.6 Exclusivity Period. These HoT take effect on the date of signature by
both Parties ("Effective Date") and remain in force until the earlier of:
(a) one (1) calendar year from the Effective Date; or (b) execution of the
Agreements (the "Exclusivity Period").
```

**NL:**
```
3.6 Exclusiviteitsperiode. Deze HoT worden van kracht op de datum van
ondertekening door beide Partijen ("Ingangsdatum") en blijven van kracht
tot de vroegste van: (a) één (1) kalenderjaar na de Ingangsdatum; of (b)
ondertekening van de Overeenkomsten (de "Exclusiviteitsperiode").
```

### 3.7 Grower Exclusivity / Exclusiviteit van de Teler

**EN:**
```
3.7 Grower Exclusivity. During the Exclusivity Period, the Grower shall
not: (a) enter into any agreement or arrangement that conflicts with, or
materially prejudices, the Project; (b) reduce the electrical grid capacity
available for this Project; or (c) take any action preventing or delaying
realization of a secondary allocation point (secundair allocatiepunt,
"SAP") for Digital Energy's benefit.
```

**NL:**
```
3.7 Exclusiviteit van de Teler. Gedurende de Exclusiviteitsperiode zal de
Teler niet: (a) enige overeenkomst of regeling aangaan die in strijd is
met, of wezenlijk afbreuk doet aan, het Project; (b) de beschikbare
elektriciteitsnetcapaciteit voor dit Project verminderen; of (c) enige
handeling verrichten die de realisatie van een secundair allocatiepunt
("SAP") ten behoeve van Digital Energy verhindert of vertraagt.
```

### 3.8 Breach of Exclusivity / Schending van Exclusiviteit

**EN:**
```
3.8 Breach of Exclusivity. Any breach by the Grower of Section 3.7 shall
entitle Digital Energy to: (a) seek specific performance; (b) terminate
these HoT with immediate effect and recover its documented costs and
expenses incurred in connection with the Project; and/or (c) claim damages
for losses suffered.
```

**NL:**
```
3.8 Schending van Exclusiviteit. Elke schending door de Teler van Artikel
3.7 geeft Digital Energy het recht om: (a) nakoming te vorderen; (b) deze
HoT met onmiddellijke ingang te beëindigen en haar gedocumenteerde kosten
en uitgaven in verband met het Project terug te vorderen; en/of (c)
schadevergoeding te vorderen voor geleden verliezen.
```

---

## Section 4 — Project Scope / Projectomvang    *(BINDING; several sub-clauses asset-gated)*

Heading EN: `4. Project Scope` | Heading NL: `4. Projectomvang`

### 4.1 Objectives and Definitions / Doelstellingen en Definities    *(always rendered)*

**EN:**
```
4.1 Objectives and Definitions. The project ("Project") comprises the
co-location of a DEC on the Grower's property to: (a) supply heat to the
greenhouse facility as more particularly described in Annex A
("Greenhouse"); and (b) potentially supply heat to third parties
("Heat Sales") via pipelines connected to the DEC.
```

**NL:**
```
4.1 Doelstellingen en Definities. Het project ("Project") omvat de
co-locatie van een DEC op het terrein van de Teler voor: (a) het leveren
van warmte aan het glastuinbouwbedrijf zoals nader omschreven in Bijlage A
("Kas"); en (b) het mogelijk leveren van warmte aan derden
("Warmteverkoop") via leidingen aangesloten op het DEC.
```

### 4.2 Project Company / Projectvennootschap    *(always rendered)*

**EN:**
```
4.2 Project Company. Digital Energy shall incorporate a Dutch private
limited company as the special-purpose vehicle for the Project ("ProjectBV")
within sixty (60) days of the Effective Date. All Agreements shall be
entered into by, or assigned to, the ProjectBV.
```

**NL:**
```
4.2 Projectvennootschap. Digital Energy zal binnen zestig (60) dagen na de
Ingangsdatum een Nederlandse besloten vennootschap oprichten als special
purpose vehicle voor het Project ("ProjectBV"). Alle Overeenkomsten worden
aangegaan door, of overgedragen aan, de ProjectBV.
```

### 4.3 Costs / Kosten    *(always rendered)*

**EN:**
```
4.3 Costs. Each Party bears its own costs under these HoT and the
Agreements. Digital Energy finances and manages the ProjectBV.
```

**NL:**
```
4.3 Kosten. Elke Partij draagt haar eigen kosten uit hoofde van deze HoT
en de Overeenkomsten. Digital Energy financiert en beheert de ProjectBV.
```

### 4.4 Digital Energy Responsibilities / Verantwoordelijkheden van Digital Energy    *(always rendered)*

**EN:**
```
4.4 Digital Energy Responsibilities. Digital Energy (through the ProjectBV)
is responsible for all DEC aspects: planning, design, procurement,
installation, commissioning, operation, maintenance, decommissioning, and
removal at Agreement expiry (collectively, "Develop and Maintain").
```

**NL:**
```
4.4 Verantwoordelijkheden van Digital Energy. Digital Energy (via de
ProjectBV) is verantwoordelijk voor alle DEC-aspecten: planning, ontwerp,
inkoop, installatie, ingebruikname, exploitatie, onderhoud, ontmanteling
en verwijdering bij het einde van de Overeenkomsten (gezamenlijk
"Ontwikkelen en Onderhouden").
```

### 4.5 DEC Components / DEC-componenten    *(always rendered — the full DEC component list is baseline; BESS-specific language applies universally in the grower body template since BESS is listed as a standard DEC component, not an addon)*

*Asset-gating note:* in the grower body template, §4.5(b) Energy Storage is baseline DEC scope (not gated). `{{addons.bess_co_development}}` governs only the **equity co-investment structure** — when true, additional BESS-SPV language may be rendered; when false, the grower body's default baseline applies. For the grower body v1, render verbatim as below; co-investment structure is addressed in §4.10(b).

**EN:**
```
4.5 DEC Components. The DEC shall include at minimum: (a) Electrical:
step-down transformers; low-voltage distribution panels and cables; power
distribution units (PDUs); uninterruptible power supplies (UPS).
(b) Energy Storage: battery energy storage systems (BESS) for backup power
and energy cost optimization. (c) Thermal: coolant distribution units
(CDUs); heat exchangers; dry coolers. (d) Computing: servers, GPUs, ASICs;
fiber optic connectivity; routers, switches, firewalls. (e) Mechanical:
equipment racks; containerized enclosures or buildings; foundations; gas
connections; water connections.
```

**NL:**
```
4.5 DEC-componenten. Het DEC omvat minimaal: (a) Elektrisch: step-down
transformatoren; laagspanningsverdeelpanelen en -kabels; power distribution
units (PDU's); noodstroomvoorzieningen (UPS). (b) Energieopslag:
batterijopslagsystemen (BESS) voor noodstroomvoorziening en optimalisatie
van energiekosten. (c) Thermisch: koelmiddeldistributie-eenheden (CDU's);
warmtewisselaars; droge koelers. (d) Computing: servers, GPU's, ASIC's;
glasvezelconnectiviteit; routers, switches, firewalls. (e) Mechanisch:
apparatuurrekken; gecontaineriseerde behuizingen of gebouwen; funderingen;
gasaansluitingen; wateraansluitingen.
```

### 4.6 Base Electrical Connection / Basis Elektrische Aansluiting    *(asset-gated: `any(sp, contribs[asset=grid_interconnection]) == true` — always true for grower HoT where the grower provides the base MV connection; gate retained for variant templates)*

**EN:**
```
4.6 Base Electrical Connection. (a) The connection point where the
medium-voltage supply interfaces with the DEC's step-down transformers is
the "Base DEC Electrical Connection Point". (b) The Grower shall Develop
and Maintain the medium-voltage infrastructure from its existing connection
to the Base DEC Electrical Connection Point, not exceeding the length
specified in Annex A, Item D.7. Any costs for infrastructure exceeding this
length shall be borne by the ProjectBV. (c) The ProjectBV shall Develop and
Maintain all infrastructure from the Base DEC Electrical Connection Point
to the DEC, including transformers and low-voltage systems ("Base DEC
Electrical Connection").
```

**NL:**
```
4.6 Basis Elektrische Aansluiting. (a) Het aansluitpunt waar de
middenspanningstoevoer verbinding maakt met de step-down transformatoren
van het DEC is het "Basis DEC Elektrisch Aansluitpunt". (b) De Teler zal de
middenspanningsinfrastructuur Ontwikkelen en Onderhouden vanaf haar
bestaande aansluiting tot aan het Basis DEC Elektrisch Aansluitpunt, met
een lengte van maximaal de lengte vermeld in Bijlage A, Punt D.7. Eventuele
kosten voor infrastructuur die deze lengte overschrijdt, komen voor
rekening van de ProjectBV. (c) De ProjectBV zal alle infrastructuur
Ontwikkelen en Onderhouden vanaf het Basis DEC Elektrisch Aansluitpunt tot
aan het DEC, inclusief transformatoren en laagspanningssystemen ("Basis DEC
Elektrische Aansluiting").
```

### 4.7 Future Electrical Connection / Toekomstige Elektrische Aansluiting    *(asset-gated: `annex_a.items.B10_future_connection_capacity` present OR `addons.future_grid_upgrade == true`)*

**EN:**
```
4.7 Future Electrical Connection. (a) The Parties shall negotiate in good
faith and agree on the feasibility, financing, design, construction, and
maintenance of any upgraded connection ("Future DEC Electrical Connection")
using the Grower's infrastructure or primary allocation point (primair
allocatiepunt, "PAP"). (b) Ownership, control, maintenance, usage rights,
and liabilities for the Future DEC Electrical Connection shall be allocated
pro rata based on each Party's documented capital contribution, to the
extent permitted by law. Capital contributions shall be determined in the
Agreements.
```

**NL:**
```
4.7 Toekomstige Elektrische Aansluiting. (a) De Partijen zullen te goeder
trouw onderhandelen en overeenstemming bereiken over de haalbaarheid,
financiering, ontwerp, bouw en onderhoud van een eventuele verzwaarde
aansluiting ("Toekomstige DEC Elektrische Aansluiting") met gebruikmaking
van de infrastructuur van de Teler of het primair allocatiepunt ("PAP").
(b) Eigendom, controle, onderhoud, gebruiksrechten en aansprakelijkheden
voor de Toekomstige DEC Elektrische Aansluiting worden pro rata verdeeld
op basis van de gedocumenteerde kapitaalinbreng van elke Partij, voor
zover wettelijk toegestaan. Kapitaalinbreng wordt vastgesteld in de
Overeenkomsten.
```

### 4.8 Heat Transfer / Warmteoverdracht    *(asset-gated: `any(sp, returns[value=energy_heat]) == true` — always true for grower HoT; gate retained for variant templates)*

**EN:**
```
4.8 Heat Transfer. (a) The ProjectBV shall establish a heat transfer point
("DEC Heat Transfer Point") on the secondary side of the DEC's heat
exchangers, at the isolation valves connecting to the Grower's Heat
Pipeline. (b) The Grower shall Develop and Maintain the pipeline from the
DEC Heat Transfer Point to the Greenhouse boiler room ("Grower's Heat
Pipeline").
```

**NL:**
```
4.8 Warmteoverdracht. (a) De ProjectBV zal een warmteoverdrachtspunt ("DEC
Warmteoverdrachtspunt") realiseren aan de secundaire zijde van de
warmtewisselaars van het DEC, bij de afsluiters die verbonden zijn met de
Warmteleiding van de Teler. (b) De Teler zal de leiding Ontwikkelen en
Onderhouden vanaf het DEC Warmteoverdrachtspunt naar de ketelruimte van de
Kas ("Warmteleiding van de Teler").
```

### 4.9 Third-Party Distribution / Distributie aan Derden    *(asset-gated: `addons.third_party_heat_distribution == true` OR `annex_a.items.E1_heat_sales_share` non-zero)*

**EN:**
```
4.9 Third-Party Distribution. The Parties shall negotiate in good faith
and agree on the feasibility, financing, design, construction, and
maintenance of pipelines (other than the Grower's Heat Pipeline) for Heat
Sales to third parties ("DEC Heat Distribution Pipeline").
```

**NL:**
```
4.9 Distributie aan Derden. De Partijen zullen te goeder trouw
onderhandelen en overeenstemming bereiken over de haalbaarheid,
financiering, ontwerp, bouw en onderhoud van leidingen (anders dan de
Warmteleiding van de Teler) voor Warmteverkoop aan derden ("DEC
Warmtedistributieleiding").
```

### 4.10 Optional Provisions / Optionele Bepalingen    *(asset-gated: per sub-clause — see below)*

*Sub-gating:*
- **§4.10(a) CHP Lease** renders only when `annex_a.items.F1_chp_lease_include == "Include"` (Field F.1 toggle).
- **§4.10(b) Grower Co-Investment** renders only when `annex_a.items.F2_co_invest_include == "Include"` (Field F.2 toggle) OR `addons.bess_co_development == true`.
- If neither is "Include", the entire §4.10 clause is suppressed.

**EN:**
```
4.10 Optional Provisions. If indicated as "Include" in Annex A, Items
F.1–F.2: (a) CHP Lease: Digital Energy shall lease the Grower's combined
heat and power unit (warmtekrachtkoppeling, "CHP") for the fee specified in
Item F.1a. (b) Grower Co-Investment: The Grower may elect to co-invest up
to the percentage specified in Item F.2a of Project costs in cash, in
exchange for a pro-rata share of ProjectBV profits. This election must be
exercised before Agreement execution. No voting rights shall attach to
such investment.
```

**NL:**
```
4.10 Optionele Bepalingen. Indien aangegeven als "Opnemen" in Bijlage A,
Punten F.1–F.2: (a) WKK-Lease: Digital Energy zal de warmtekrachtkoppeling
("WKK") van de Teler leasen voor de vergoeding vermeld in Punt F.1a.
(b) Co-Investering Teler: De Teler kan ervoor kiezen tot het percentage
vermeld in Punt F.2a van de Projectkosten in contanten te co-investeren,
in ruil voor een pro rata aandeel in de winsten van de ProjectBV. Deze
keuze moet worden gemaakt vóór ondertekening van de Overeenkomsten. Aan
een dergelijke investering zijn geen stemrechten verbonden.
```

---

## Section 5 — Agreements / Overeenkomsten    *(BINDING; negotiation framework for the definitive Agreements)*

Heading EN: `5. Agreements` | Heading NL: `5. Overeenkomsten`

### 5.1 Parties and Term / Partijen en Looptijd    *(always rendered)*

**EN:**
```
5.1 Parties and Term. (a) The Agreements shall be between ProjectBV and
the Grower. (b) Initial term: thirty (30) years from execution. (c)
Automatic renewal for successive periods of five (5) years each, unless
either Party gives written termination notice at least five (5) years
before expiry of the then-current term.
```

**NL:**
```
5.1 Partijen en Looptijd. (a) De Overeenkomsten worden gesloten tussen de
ProjectBV en de Teler. (b) Initiële looptijd: dertig (30) jaar vanaf
ondertekening. (c) Automatische verlenging met opeenvolgende perioden van
vijf (5) jaar, tenzij een van de Partijen ten minste vijf (5) jaar voor
het verstrijken van de dan lopende termijn schriftelijk opzegt.
```

### 5.2 Negotiation Principles / Onderhandelingsprincipes    *(always rendered)*

**EN:**
```
5.2 Negotiation Principles. The Parties shall negotiate the Agreements in
good faith and on commercially reasonable terms, ensuring long-term
stability, continuity, and investment security for ProjectBV. The Parties
may agree to term extensions, a right of first refusal ("ROFR"), or
acquisition conditions.
```

**NL:**
```
5.2 Onderhandelingsprincipes. De Partijen zullen te goeder trouw en op
commercieel redelijke voorwaarden over de Overeenkomsten onderhandelen,
waarbij lange-termijn stabiliteit, continuïteit en investeringszekerheid
voor de ProjectBV wordt gewaarborgd. De Partijen kunnen overeenstemming
bereiken over termijnverlengingen, een voorkeursrecht ("ROFR"), of
overnamevoorwaarden.
```

### 5.3 ProjectBV Obligations / Verplichtingen van de ProjectBV    *(always rendered; heat-supply sub-clause requires `returns[value=energy_heat]` — always true in grower HoT)*

**EN:**
```
5.3 ProjectBV Obligations. (a) Electrical Connection: Provide the Base DEC
Electrical Connection. (b) Heat Supply: Supply heat at the DEC Heat
Transfer Point: (i) target outlet temperature per Annex A, Item C.1, ±5%;
(ii) contingent on the Grower maintaining a return temperature ensuring ΔT
of at least 15°C; if the Grower fails to maintain the required return
temperature, the ProjectBV's obligation to meet the target outlet
temperature shall be suspended to that extent; (iii) delivery basis:
delivered-as-produced ("DAP"), using commercially reasonable efforts; and
(iv) price per Item C.4. (c) Third-Party Heat: Subject to DEC Heat
Distribution Pipeline availability, the ProjectBV may deliver heat to
third parties.
```

**NL:**
```
5.3 Verplichtingen van de ProjectBV. (a) Elektrische Aansluiting: De Basis
DEC Elektrische Aansluiting verzorgen. (b) Warmtelevering: Warmte leveren
bij het DEC Warmteoverdrachtspunt: (i) beoogde afgiftetemperatuur conform
Bijlage A, Punt C.1, ±5%; (ii) afhankelijk van het handhaven door de Teler
van een retourtemperatuur die een ΔT van ten minste 15°C waarborgt; indien
de Teler de vereiste retourtemperatuur niet handhaaft, wordt de
verplichting van de ProjectBV om de beoogde afgiftetemperatuur te halen
in zoverre opgeschort; (iii) leveringsbasis: geleverd-als-geproduceerd
("DAP"), met commercieel redelijke inspanningen; en (iv) prijs conform
Punt C.4. (c) Warmte aan Derden: Onder voorbehoud van beschikbaarheid van
de DEC Warmtedistributieleiding, mag de ProjectBV warmte leveren aan
derden.
```

### 5.4 Grower Obligations / Verplichtingen van de Teler    *(always rendered; sub-clause (e) SAP requires `contribs[asset=grid_interconnection]`)*

**EN (5.4(a)–(d)):**
```
5.4 Grower Obligations. (a) Infrastructure: Provide a fully functional
Grower's Heat Pipeline and Base DEC Electrical Connection Point. (b) Base
Project Connection: Make available an existing grid connection dedicated
to the Project ("Base Project Connection"), comprising the capacities
specified in Annex A, Items B.7–B.9 ("Base Connection Capacity", "Base
Import Capacity", and "Base Export Capacity"). (c) Future Project
Connection: Subject to DSO approval, apply for and make available a future
grid connection ("Future Project Connection"), expected to comprise the
capacities in Items B.10–B.12 ("Future Connection Capacity", "Future
Import Capacity", and "Future Export Capacity"). (d) DSO Costs: ProjectBV
bears DSO costs for the Future Project Connection, provided: (i) the
Grower submits the application only after Agreement execution, or with
prior written consent; and (ii) costs incurred before ProjectBV
incorporation are reimbursed within the period in Item E.2, plus interest
at EURIBOR + 2% from the due date if payment is late.
```

**NL (5.4(a)–(d)):**
```
5.4 Verplichtingen van de Teler. (a) Infrastructuur: Een volledig
functionele Warmteleiding van de Teler en Basis DEC Elektrisch
Aansluitpunt beschikbaar stellen. (b) Basis Projectaansluiting: Een
bestaande netaansluiting beschikbaar stellen voor het Project ("Basis
Projectaansluiting"), bestaande uit de capaciteiten vermeld in Bijlage A,
Punten B.7–B.9 ("Basis Aansluitcapaciteit", "Basis Importcapaciteit", en
"Basis Exportcapaciteit"). (c) Toekomstige Projectaansluiting: Onder
voorbehoud van DSO-goedkeuring, aanvragen en beschikbaar stellen van een
toekomstige netaansluiting ("Toekomstige Projectaansluiting"), naar
verwachting bestaande uit de capaciteiten in Punten B.10–B.12 ("Toekomstige
Aansluitcapaciteit", "Toekomstige Importcapaciteit", en "Toekomstige
Exportcapaciteit"). (d) DSO-kosten: De ProjectBV draagt de DSO-kosten voor
de Toekomstige Projectaansluiting, mits: (i) de Teler de aanvraag pas
indient na ondertekening van de Overeenkomsten, of met voorafgaande
schriftelijke toestemming; en (ii) kosten gemaakt vóór oprichting van de
ProjectBV worden vergoed binnen de termijn in Punt E.2, vermeerderd met
rente van EURIBOR + 2% vanaf de vervaldatum bij te late betaling.
```

### 5.4(e) SAP Configuration / SAP-configuratie    *(asset-gated: `any(sp, contribs[asset=grid_interconnection])`)*

**EN:**
```
5.4(e) SAP Configuration. The Grower shall facilitate SAP realization and
submit necessary DSO applications for grid or ATO (Aansluit- en
Transportovereenkomst) reconfiguration. Priority: (i) Cable Pooling: SAP
registered in ProjectBV's name, governed by a Cable Pooling agreement,
enabling ProjectBV to contract its own electricity supplier; (ii) MLOEA:
If cable pooling is not approved, SAP in the Grower's name under MLOEA
(meerdere leveranciers op één aansluiting), with contractual provisions
ensuring ProjectBV access; or (iii) Alternative: If neither is feasible,
the Grower shall facilitate ProjectBV's use through a capacity allocation
agreement on terms to be negotiated in good faith.
```

**NL:**
```
5.4(e) SAP-configuratie. De Teler zal de SAP-realisatie faciliteren en de
benodigde DSO-aanvragen indienen voor herconfiguratie van het net of de
ATO (Aansluit- en Transportovereenkomst). Volgorde: (i) Cable Pooling: SAP
geregistreerd op naam van de ProjectBV, beheerst door een Cable
Pooling-overeenkomst, waardoor de ProjectBV haar eigen elektriciteitsleverancier
kan contracteren; (ii) MLOEA: Indien cable pooling niet wordt goedgekeurd,
SAP op naam van de Teler onder MLOEA (meerdere leveranciers op één
aansluiting), met contractuele bepalingen die toegang voor de ProjectBV
waarborgen; of (iii) Alternatief: Indien geen van beide haalbaar is, zal
de Teler het gebruik door de ProjectBV faciliteren via een
capaciteitsallocatieovereenkomst op voorwaarden die te goeder trouw worden
onderhandeld.
```

### 5.5 Land Rights / Grondrechten    *(asset-gated: `any(sp, contribs[asset=land])`)*

**EN:**
```
5.5 Land Rights. (a) Grant: The Grower shall provide land for the DEC for
no additional fee or payment. (b) Legal Form: The Grower shall grant (or
procure the grant of) a right of superficies (opstalrecht) and/or enter
into a Right in Rem Agreement ("ZRO", Zakelijk Recht Overeenkomst)
enabling DEC construction, operation, and maintenance. (c) Area:
Approximately the area per MW specified in Annex A, Item D.5, for the
combined Base Connection Capacity and Future Connection Capacity.
(d) Establishment: The right of superficies shall be established by
notarial deed, with easements (erfdienstbaarheden) if necessary.
(e) Extension: The Grower shall cooperate in creating additional land
rights if Future Connection Capacity becomes available. (f) Zoning: The
Parties shall cooperate to ensure compliance with applicable zoning
(bestemmingsplan) per Item D.4. (g) Third-Party Consents: If the Grower
is not the landowner or does not have unencumbered title, the landowner
("Landowner") and/or land financier ("Land Financier") shall co-sign the
Agreements.
```

**NL:**
```
5.5 Grondrechten. (a) Verlening: De Teler stelt grond beschikbaar voor het
DEC zonder aanvullende vergoeding of betaling. (b) Juridische Vorm: De
Teler zal een recht van opstal verlenen (of doen verlenen) en/of een
Zakelijk Recht Overeenkomst ("ZRO") aangaan die de bouw, exploitatie en
onderhoud van het DEC mogelijk maakt. (c) Oppervlakte: Circa de
oppervlakte per MW vermeld in Bijlage A, Punt D.5, voor de gecombineerde
Basis Aansluitcapaciteit en Toekomstige Aansluitcapaciteit. (d) Vestiging:
Het recht van opstal wordt bij notariële akte gevestigd, met
erfdienstbaarheden indien nodig. (e) Uitbreiding: De Teler zal meewerken
aan het vestigen van aanvullende grondrechten indien Toekomstige
Aansluitcapaciteit beschikbaar komt. (f) Bestemmingsplan: De Partijen
werken samen om naleving van het toepasselijke bestemmingsplan conform
Punt D.4 te waarborgen. (g) Toestemmingen van Derden: Indien de Teler niet
de grondeigenaar is of geen onbezwaarde titel heeft, dient de grondeigenaar
("Grondeigenaar") en/of grondfinancier ("Grondfinancier") de Overeenkomsten
mede te ondertekenen.
```

*Signature-page consequence:* when §5.5(g) applies (i.e., `annex_a.items.D_landowner_is_grower == false` OR `annex_a.items.D_land_financier_present == true`), the signature page adds Landowner and/or Land Financier co-signatory panels (present in the HoT body signature table by default; populated conditionally by the engine).

### 5.6 Operational Flexibility / Operationele Flexibiliteit    *(always rendered)*

**EN:**
```
5.6 Operational Flexibility. (a) The Parties shall cooperate to maximize
DEC uptime and efficiency. (b) ProjectBV may curtail or suspend operations
upon fourteen (14) days' prior written notice if adverse market
conditions, equipment failure, regulatory constraints, or other
circumstances make operation commercially unviable, provided ProjectBV
demonstrates to the Grower's reasonable satisfaction that such
circumstances existed. Any curtailment exceeding ninety (90) consecutive
days requires the Grower's prior written consent.
```

**NL:**
```
5.6 Operationele Flexibiliteit. (a) De Partijen werken samen om de uptime
en efficiëntie van het DEC te maximaliseren. (b) De ProjectBV mag de
activiteiten inkorten of opschorten na veertien (14) dagen voorafgaande
schriftelijke kennisgeving indien ongunstige marktomstandigheden,
apparatuurstoringen, regelgevende beperkingen of andere omstandigheden de
exploitatie commercieel onhaalbaar maken, mits de ProjectBV naar redelijke
tevredenheid van de Teler aantoont dat dergelijke omstandigheden bestonden.
Elke inkorting van meer dan negentig (90) opeenvolgende dagen vereist
voorafgaande schriftelijke toestemming van de Teler.
```

### 5.7 Subsidy Cooperation / Subsidiesamenwerking    *(always rendered; SDE++ is a Valid Withdrawal Event trigger in §3.3(e))*

**EN:**
```
5.7 Subsidy Cooperation. The Parties shall cooperate in good faith to
apply for and secure SDE++ and other applicable subsidies for the
Project's benefit. The Parties shall submit the SDE++ application within
the next available application window following the Effective Date.
```

**NL:**
```
5.7 Subsidiesamenwerking. De Partijen werken te goeder trouw samen om
SDE++ en andere toepasselijke subsidies aan te vragen en te verkrijgen ten
behoeve van het Project. De Partijen dienen de SDE++-aanvraag in binnen de
eerstvolgende beschikbare aanvraagperiode na de Ingangsdatum.
```

---

## Section 6 — Costs and Revenues / Kosten en Opbrengsten    *(BINDING; the commercial split)*

Heading EN: `6. Costs and Revenues` | Heading NL: `6. Kosten en Opbrengsten`

### 6.1 DEC Costs and Revenues / DEC-kosten en -opbrengsten    *(always rendered)*

**EN:**
```
6.1 DEC Costs and Revenues. ProjectBV bears all costs and retains all
revenues directly attributable to the DEC ("DEC Costs" and "DEC Revenues"),
including without limitation: (a) energy costs, including revenue from
negative-priced electricity consumption; (b) energy tax (Energiebelasting,
"EB"); the Parties shall evaluate combined EB volumes per Item C.5;
(c) DSO grid charges: fixed ("kW-Contract") and variable ("kW-Max");
(d) energy trading (PPAs, OTC, day-ahead/intraday markets); (e) ancillary
services (FCR, aFRR, mFRR); and (f) grid services (capacity-limiting
contracts, redispatch, congestion management).
```

**NL:**
```
6.1 DEC-kosten en -opbrengsten. De ProjectBV draagt alle kosten en behoudt
alle opbrengsten die rechtstreeks aan het DEC zijn toe te rekenen
("DEC-kosten" en "DEC-opbrengsten"), waaronder: (a) energiekosten,
inclusief opbrengsten uit het verbruik van negatief geprijsde
elektriciteit; (b) Energiebelasting ("EB"); de Partijen evalueren
gecombineerde EB-volumes conform Punt C.5; (c) DSO-netkosten: vast
("kW-Contract") en variabel ("kW-Max"); (d) energiehandel (PPA's, OTC,
day-ahead/intraday markten); (e) systeemdiensten (FCR, aFRR, mFRR); en
(f) netdiensten (capaciteitsbeperkende contracten, redispatch,
congestiebeheer).
```

### 6.2 Greenhouse Costs and Revenues / Kaskosten en -opbrengsten    *(always rendered)*

**EN:**
```
6.2 Greenhouse Costs and Revenues. The Grower bears all costs and retains
all revenues directly attributable to the Greenhouse ("Greenhouse Costs"
and "Greenhouse Revenues").
```

**NL:**
```
6.2 Kaskosten en -opbrengsten. De Teler draagt alle kosten en behoudt alle
opbrengsten die rechtstreeks aan de Kas zijn toe te rekenen ("Kaskosten"
en "Kasopbrengsten").
```

### 6.3 Heat Sales Sharing / Verdeling Warmteverkoop    *(asset-gated: `addons.third_party_heat_distribution == true` OR `annex_a.items.E1_heat_sales_share` non-zero)*

**EN:**
```
6.3 Heat Sales Sharing. Net income from third-party Heat Sales (excluding
heat to the Grower) is shared per Annex A, Item E.1. "Net income" means
gross revenues minus distribution costs (maintenance, pumping, and
applicable taxes on heat sales, excluding corporate income tax), which
costs are also shared in the same proportion.
```

**NL:**
```
6.3 Verdeling Warmteverkoop. Netto-inkomsten uit Warmteverkoop aan derden
(exclusief warmte aan de Teler) worden verdeeld conform Bijlage A, Punt
E.1. "Netto-inkomsten" betekent bruto-opbrengsten minus distributiekosten
(onderhoud, pompen, en toepasselijke belastingen op warmteverkoop,
exclusief vennootschapsbelasting), welke kosten ook in dezelfde verhouding
worden verdeeld.
```

### 6.4 Billing Pass-Through / Doorbelasting    *(asset-gated: `any(sp, contribs[asset=grid_interconnection])` — required when SAP configuration exists)*

**EN:**
```
6.4 Billing Pass-Through. If SAP configuration requires one Party to
receive invoices or revenues intended for the other, such amounts shall be
reimbursed within the period in Item E.2.
```

**NL:**
```
6.4 Doorbelasting. Indien de SAP-configuratie vereist dat een Partij
facturen of opbrengsten ontvangt die bestemd zijn voor de andere Partij,
worden dergelijke bedragen vergoed binnen de termijn in Punt E.2.
```

### 6.5 Audit Rights / Auditrechten    *(always rendered)*

**EN:**
```
6.5 Audit Rights. Each Party may, upon thirty (30) days' notice, audit the
other Party's records relating to shared costs and revenues under this
Section 6, at the auditing Party's expense. Audits shall be conducted
during normal business hours and not more than once per calendar year.
```

**NL:**
```
6.5 Auditrechten. Elke Partij kan, na dertig (30) dagen kennisgeving, de
administratie van de andere Partij met betrekking tot gedeelde kosten en
opbrengsten onder dit Artikel 6 controleren, op kosten van de auditerende
Partij. Audits worden uitgevoerd tijdens normale kantooruren en niet meer
dan eenmaal per kalenderjaar.
```

### 6.6 Disputed Amounts / Betwiste Bedragen    *(always rendered)*

**EN:**
```
6.6 Disputed Amounts. If a Party disputes an invoice, it shall pay the
undisputed amount and notify the other Party of the dispute within
fourteen (14) days. The Parties shall resolve the dispute in accordance
with Section 8.5.
```

**NL:**
```
6.6 Betwiste Bedragen. Indien een Partij een factuur betwist, betaalt zij
het onbetwiste bedrag en stelt zij de andere Partij binnen veertien (14)
dagen van het geschil in kennis. De Partijen lossen het geschil op
overeenkomstig Artikel 8.5.
```

---

## Section 7 — Confidentiality / Vertrouwelijkheid    *(BINDING; supersedes LOI §6.1 per LOI §6.1.6 self-supersession clause)*

Heading EN: `7. Confidentiality` | Heading NL: `7. Vertrouwelijkheid`

**Critical note on supersession:** The LOI §6.1 confidentiality clause contains a **self-supersession sub-clause (Van Gog §6.1.6)** that causes it to be superseded by the HoT §7 on execution of this HoT. That design-of-record mechanism is what makes HoT §7 non-redundant with the LOI. At HoT signing, the parties replace LOI §6.1 with the clauses below. This supersession is load-bearing — preserve §7 verbatim EN and NL without consolidation against the LOI library.

### 7.1 Obligation / Verplichting

**EN:**
```
7.1 Obligation. Each Party shall keep strictly confidential these HoT and
all information disclosed in connection with the Project ("Confidential
Information").
```

**NL:**
```
7.1 Verplichting. Elke Partij houdt deze HoT en alle informatie die in
verband met het Project wordt verstrekt strikt vertrouwelijk ("Vertrouwelijke
Informatie").
```

### 7.2 Permitted Disclosures / Toegestane Openbaarmakingen

**EN:**
```
7.2 Permitted Disclosures. Disclosure is permitted: (a) as required by
law, court order, or regulatory authority; (b) to affiliates, financiers,
and professional advisors (legal, technical, commercial) on a need-to-know
basis, if bound by confidentiality obligations no less protective than
this Section 7; (c) for inclusion in subsidy applications, regulatory
filings, or permit applications, to the extent required; or (d) with
prior written consent.
```

**NL:**
```
7.2 Toegestane Openbaarmakingen. Openbaarmaking is toegestaan: (a) indien
vereist door wet, rechterlijk bevel, of toezichthoudende instantie;
(b) aan gelieerde ondernemingen, financiers, en professionele adviseurs
(juridisch, technisch, commercieel) op need-to-know basis, indien gebonden
door geheimhoudingsverplichtingen die niet minder beschermend zijn dan
dit Artikel 7; (c) voor opname in subsidieaanvragen, regelgevende
dossiers, of vergunningaanvragen, voor zover vereist; of (d) met
voorafgaande schriftelijke toestemming.
```

### 7.3 Exclusions / Uitzonderingen

**EN:**
```
7.3 Exclusions. Confidential Information excludes information that:
(a) enters the public domain other than through breach by the receiving
Party; (b) was known to the receiving Party before disclosure; (c) is
independently developed by the receiving Party; or (d) is received from a
third party without breach of any confidentiality obligation owed to the
disclosing Party.
```

**NL:**
```
7.3 Uitzonderingen. Vertrouwelijke Informatie omvat niet informatie die:
(a) openbaar wordt anders dan door schending door de ontvangende Partij;
(b) de ontvangende Partij reeds bekend was vóór openbaarmaking;
(c) zelfstandig is ontwikkeld door de ontvangende Partij; of (d) is
ontvangen van een derde zonder schending van enige geheimhoudingsverplichting
jegens de verstrekkende Partij.
```

### 7.4 Return of Information / Teruggave van Informatie

**EN:**
```
7.4 Return of Information. Upon termination, each Party shall return or
destroy Confidential Information of the other Party upon request, except
to the extent retention is required by law or for bona fide record-keeping
purposes.
```

**NL:**
```
7.4 Teruggave van Informatie. Bij beëindiging zal elke Partij op verzoek
Vertrouwelijke Informatie van de andere Partij retourneren of vernietigen,
behalve voor zover bewaring wettelijk vereist is of voor legitieme
archiveringsdoeleinden.
```

### 7.5 Duration / Duur

**EN:**
```
7.5 Duration. These obligations continue for two (2) years after
termination of these HoT.
```

**NL:**
```
7.5 Duur. Deze verplichtingen blijven van kracht gedurende twee (2) jaar
na beëindiging van deze HoT.
```

---

## Section 8 — General Provisions / Algemene Bepalingen    *(BINDING; §8 survives termination per §3.5)*

Heading EN: `8. General Provisions` | Heading NL: `8. Algemene Bepalingen`

### 8.1 Costs / Kosten

**EN:** `8.1 Costs. Each Party bears its own costs in negotiating and preparing these HoT and the Agreements.`
**NL:** `8.1 Kosten. Elke Partij draagt haar eigen kosten voor het onderhandelen en opstellen van deze HoT en de Overeenkomsten.`

### 8.2 Assignment / Overdracht

**EN:**
```
8.2 Assignment. (a) Neither Party may assign or transfer any rights or
obligations without prior written consent. (b) Exception: Digital Energy
may assign to ProjectBV upon incorporation. Digital Energy shall remain
jointly and severally liable for ProjectBV's obligations until the
Agreements are executed, at which point Digital Energy shall be released.
```

**NL:**
```
8.2 Overdracht. (a) Geen van de Partijen mag rechten of verplichtingen
overdragen of cederen zonder voorafgaande schriftelijke toestemming.
(b) Uitzondering: Digital Energy mag overdragen aan de ProjectBV na
oprichting. Digital Energy blijft hoofdelijk aansprakelijk voor de
verplichtingen van de ProjectBV totdat de Overeenkomsten zijn ondertekend,
waarna Digital Energy wordt ontslagen.
```

### 8.3 Governing Law / Toepasselijk Recht

**EN:** `8.3 Governing Law. These HoT and the Agreements are governed by Dutch law.`
**NL:** `8.3 Toepasselijk Recht. Op deze HoT en de Overeenkomsten is Nederlands recht van toepassing.`

### 8.4 Jurisdiction / Bevoegde Rechter

**EN:** `8.4 Jurisdiction. Disputes are submitted exclusively to the District Court of Amsterdam (Rechtbank Amsterdam).`
**NL:** `8.4 Bevoegde Rechter. Geschillen worden exclusief voorgelegd aan de Rechtbank Amsterdam.`

### 8.5 Dispute Resolution / Geschillenbeslechting

**EN:**
```
8.5 Dispute Resolution. Before initiating court proceedings, the Parties
shall attempt to resolve disputes through good faith negotiations between
senior executives for at least fifteen (15) business days.
```

**NL:**
```
8.5 Geschillenbeslechting. Alvorens een gerechtelijke procedure te
starten, trachten de Partijen geschillen op te lossen door te goeder trouw
te onderhandelen tussen senior leidinggevenden gedurende ten minste
vijftien (15) werkdagen.
```

### 8.6 Entire Agreement / Volledige Overeenkomst

**EN:**
```
8.6 Entire Agreement. These HoT constitute the entire agreement on this
subject matter and supersede all prior negotiations and representations,
except in the case of fraud or fraudulent misrepresentation.
```

**NL:**
```
8.6 Volledige Overeenkomst. Deze HoT vormen de volledige overeenkomst over
dit onderwerp en vervangen alle eerdere onderhandelingen en verklaringen,
behalve in geval van fraude of frauduleuze misleiding.
```

### 8.7 Amendments / Wijzigingen

**EN:** `8.7 Amendments. Amendments require written agreement signed by both Parties.`
**NL:** `8.7 Wijzigingen. Wijzigingen vereisen schriftelijke overeenstemming ondertekend door beide Partijen.`

### 8.8 Waiver / Afstand van Recht

**EN:**
```
8.8 Waiver. No failure or delay in exercising any right shall operate as a
waiver thereof, nor shall any single exercise preclude further exercise.
```

**NL:**
```
8.8 Afstand van Recht. Het niet of vertraagd uitoefenen van enig recht
houdt geen afstand daarvan in, noch zal enige eenmalige uitoefening
verdere uitoefening uitsluiten.
```

### 8.9 Severability / Scheidbaarheid

**EN:**
```
8.9 Severability. If any provision is held invalid or unenforceable, the
remaining provisions continue in full force. The Parties shall negotiate
in good faith to replace the invalid provision with a valid provision
achieving substantially the same effect.
```

**NL:**
```
8.9 Scheidbaarheid. Indien enige bepaling ongeldig of niet-afdwingbaar
wordt geacht, blijven de overige bepalingen volledig van kracht. De
Partijen onderhandelen te goeder trouw om de ongeldige bepaling te
vervangen door een geldige bepaling met in wezen hetzelfde effect.
```

### 8.10 Force Majeure / Overmacht

**EN:**
```
8.10 Force Majeure. Neither Party is liable for failure to perform due to
events beyond its reasonable control, provided the affected Party:
(a) notifies the other promptly; (b) uses commercially reasonable efforts
to mitigate; and (c) resumes performance as soon as reasonably practicable.
```

**NL:**
```
8.10 Overmacht. Geen van de Partijen is aansprakelijk voor het niet
nakomen van verplichtingen als gevolg van gebeurtenissen buiten haar
redelijke controle, mits de getroffen Partij: (a) de andere Partij
onverwijld informeert; (b) commercieel redelijke inspanningen levert om
de gevolgen te beperken; en (c) de nakoming zo spoedig als redelijkerwijs
mogelijk hervat.
```

### 8.11 Notices / Kennisgevingen

**EN:**
```
8.11 Notices. Notices must be in writing to the addresses in Annex A,
Section G. Notices by email are deemed received on the next business day;
notices by courier are deemed received upon confirmed delivery.
```

**NL:**
```
8.11 Kennisgevingen. Kennisgevingen dienen schriftelijk te geschieden aan
de adressen in Bijlage A, Sectie G. Kennisgevingen per e-mail worden
geacht te zijn ontvangen op de volgende werkdag; kennisgevingen per
koerier worden geacht te zijn ontvangen bij bevestigde aflevering.
```

### 8.12 Third Party Rights / Rechten van Derden

**EN:**
```
8.12 Third Party Rights. These HoT do not confer any rights on third
parties, except that ProjectBV (once incorporated) may enforce rights
granted to it herein.
```

**NL:**
```
8.12 Rechten van Derden. Deze HoT verlenen geen rechten aan derden,
behalve dat de ProjectBV (na oprichting) de aan haar hierin verleende
rechten kan afdwingen.
```

### 8.13 Counterparts / Exemplaren

**EN:**
```
8.13 Counterparts. These HoT may be executed in counterparts, each deemed
an original, together constituting one agreement. Electronic signatures
have the same legal effect as original signatures.
```

**NL:**
```
8.13 Exemplaren. Deze HoT kunnen in meerdere exemplaren worden ondertekend,
waarbij elk exemplaar als origineel geldt en alle exemplaren samen één
overeenkomst vormen. Elektronische handtekeningen hebben dezelfde
rechtskracht als originele handtekeningen.
```

---

## Section 9 — Execution / Ondertekening    *(always rendered; closing paragraph from body template)*

**EN:** `9. Execution. Each signatory represents and warrants that they have full authority to execute these HoT on behalf of the Party they represent.`
**NL:** `9. Ondertekening. Elke ondertekenaar verklaart en garandeert dat hij/zij volledig bevoegd is om deze HoT te ondertekenen namens de Partij die hij/zij vertegenwoordigt.`

Closing line: `Annex A: Variable Schedule (integral part) / Variabelenoverzicht (integraal onderdeel)`

Document terminator: `— End of Heads of Terms / Einde Contractvoorwaarden —`

---

## Annex A — Variable Schedule    *(integral part; populated by hot-intake)*

After §9 and the closing line, the engine appends the populated `hot-grower-annex-a-v1.docx`. Annex A is an **integral part** of the HoT (explicit body-template language).

**Annex A population contract:**
1. The `hot-intake` skill (or `generate_site_hot.py` in batch mode) reads `deal.yaml` + `.hot_input.yaml` and populates fields per `sites/hot/field-registry.json` (58 fields across sections A–G + 3 header fields).
2. Only Annex A input fields (yellow/green XML-marker cells) are written. The body template is **never modified** (per `template-version.md`).
3. Supporting documents (16 rows in the Annex A checklist) are populated with status `attached` / `pending` / `n/a` per `deal.yaml.supporting_documents`.
4. The Annex is merged into the main `.docx` by `document-factory.append_annex(doc, annex_path)` — preserving the Annex's own pagination break and heading.

---

## Signature page    *(rendered via `document-factory.signature_block.render_signature_page(..., formality="binding")`)*

The HoT signature page differs from the LOI signature page in three load-bearing ways:

| Aspect | LOI (non_binding) | **HoT (binding)** |
|---|---|---|
| KvK / registration number | omitted | **included** (per Van Gog binding pattern + field-registry A.2 required) |
| Signatory title | optional | **required** (field-registry A.5) |
| Signing authority disclosure | omitted | **rendered when `A.6 == "Joint"`** (two-signature flag) |
| Landowner + Land Financier panels | n/a | **conditional**, per §5.5(g) |

**Call signature:**
```python
signature_block.render_signature_page(
    doc,
    provider_party=DE_ENTITIES["ch"],                # Digital Energy Group AG (Swiss, not NL) — grower body references DE AG
    provider_signatory_name="Jonathan Mattis Glender",
    provider_signatory_title="Chairman of the Board",
    site_partners=[SigParty(...) for sp in deal.site_partners],
    formality="binding",                              # <-- critical toggle
    include_landowner=bool(deal.annex_a.items.get("D_landowner_is_grower") is False),
    include_land_financier=bool(deal.annex_a.items.get("D_land_financier_present")),
)
```

**Rendered panels (per body template Table 1):**
- `DIGITAL ENERGY GROUP AG` — Name / Title / Date — single panel.
- `GROWER / TELER [per A.1]` — Name [per A.4] / Title [per A.5] / Date — single panel; KvK rendered inline per `formality="binding"`.
- `LANDOWNER / GRONDEIGENAAR` (if applicable / indien van toepassing) — conditional on §5.5(g) trigger.
- `LAND FINANCIER / GRONDFINANCIER` (if applicable / indien van toepassing) — conditional on `D_land_financier_present`.

---

## Engine contract (Phase C `generate_site_hot.py`)

Mirrors the LOI engine. Numbered steps map 1:1 to the LOI engine contract for consistency.

1. **Load.** Load `{slug}/deal.yaml`; validate `deal_yaml_schema_version == "1.0"` and `stage in ("hot", "both")`.
2. **Load annex input.** Load `{slug}/.hot_input.yaml` (or derive from `deal.yaml`). Validate against `sites/hot/field-registry.json` — required fields present, regex validations pass (e.g., KvK 8 digits).
3. **Derive labels.** Call `sites/_shared/site_doc_base.derive_labels()` on each Site Partner — attach `role_labels_en` and `role_labels_nl`.
4. **Cover.** Call `document-factory.add_cover(bilingual=True, title_en="Binding Heads of Terms", title_nl="Bindende Contractvoorwaarden", ...)`.
5. **Body.** For each clause above:
   - Check asset-gate condition against `deal.yaml` / `addons.*` / `contribs[]` / `returns[]`.
   - If passes, substitute `{{placeholders}}` and render bilingual clause via `document-factory.bilingual_body.render_bilingual_clause(...)`.
   - Suppress clauses that fail the gate; adjust numbering only where the body template's clause numbers themselves would become orphaned (none do in v1.0 — all gated clauses have standalone numbers).
6. **§9 close.** Render the execution paragraph and the bilingual closing line.
7. **Annex A.** Call `annex-fill` routine to populate `hot-grower-annex-a-v1.docx` fields from `deal.yaml` per field-registry; append annex via `document-factory.append_annex(doc, populated_annex_path)`.
8. **Signature page.** Call `document-factory.signature_block.render_signature_page(doc, ..., formality="binding", include_landowner=..., include_land_financier=...)`. KvK is rendered per §5.5(g) trigger evaluation.
9. **Validators.** Run `document-factory.format_validators.run_all(doc)` post-assembly. Additionally run HoT-specific checks: (a) Annex A field completeness against `required_fields == 44`; (b) §4.10 sub-gate coherence (neither CHP nor co-invest => §4.10 suppressed); (c) §5.5(g) signature-page consistency (co-signatory panels match trigger).
10. **Write.** `/tmp/YYYYMMDD_DE_HoT_Site_{slug}_v1_(DRAFT).docx`.
11. **QA.** Write validator results to `_qa.txt` beside the artifact.
12. **Route.** Hand off to `sites/_shared/output_router.route(artifact)` for Drive placement under `{Counterparty}_Project_Benelux_Ops/drafts/` (same routing contract as LOI engine).

---

## Asset-gating map (summary)

For the engine's gate evaluator, the following clauses are asset-gated (all others in §1–§9 render always):

| Clause | Gate condition | Typical evaluation for grower HoT |
|---|---|---|
| §4.6 Base Electrical Connection | `any(sp, contribs[asset=grid_interconnection])` | **true** (grower provides base MV) |
| §4.7 Future Electrical Connection | `annex_a.items.B10_future_connection_capacity` present OR `addons.future_grid_upgrade == true` | conditional |
| §4.8 Heat Transfer | `any(sp, returns[value=energy_heat])` | **true** (grower receives heat) |
| §4.9 Third-Party Distribution | `addons.third_party_heat_distribution == true` OR `annex_a.items.E1_heat_sales_share` non-zero | conditional |
| §4.10(a) CHP Lease | `annex_a.items.F1_chp_lease_include == "Include"` | conditional |
| §4.10(b) Grower Co-Investment | `annex_a.items.F2_co_invest_include == "Include"` OR `addons.bess_co_development == true` | conditional |
| §5.4(e) SAP Configuration | `any(sp, contribs[asset=grid_interconnection])` | **true** |
| §5.5 Land Rights (and §5.5(g) co-sign trigger) | `any(sp, contribs[asset=land])`; §5.5(g) only if `D_landowner_is_grower == false` or `D_land_financier_present == true` | **true** for land; §5.5(g) conditional |
| §6.3 Heat Sales Sharing | `addons.third_party_heat_distribution == true` OR `annex_a.items.E1_heat_sales_share` non-zero | conditional |
| §6.4 Billing Pass-Through | `any(sp, contribs[asset=grid_interconnection])` | **true** |

All §1, §2, §3, §7, §8, §9, and the non-gated sub-clauses in §4–§6 render **always**. The HoT has no "fully optional" top-level section — every top-level section is binding and rendered.

---

## Relationship to `sites/_shared/site_clause_library.md`

At time of writing (v1.0), `sites/_shared/site_clause_library.md` does not yet exist. The LOI template's §6.1–§6.4 references it as the design-of-record location for shared binding clauses (confidentiality, governing law, info right, miscellaneous).

**Plan for de-duplication:** when `site_clause_library.md` is introduced, the following HoT clauses should be pulled from it rather than re-declared here — avoiding drift against the LOI:
- §7 (Confidentiality) — HoT-specific version, **does not de-duplicate** with LOI §6.1; keep verbatim in this template because the supersession mechanism requires distinct text.
- §8.3 (Governing Law) — aligns with LOI §6.2; candidate for library.
- §8.4 (Jurisdiction) — aligns with LOI §6.2; candidate for library.
- §8.9 (Severability) — aligns with LOI §6.4; candidate for library.

Until the library exists, this template holds the canonical text for §7–§8.

---

## Versioning

Any change to clause text (EN or NL) is a **template version bump** requiring the full Jelmer/Yoni/SAL + NL-native review cadence per `version-bump.md`. Placeholder-list changes and engine-integration changes can land without a template version bump so long as no rendered text changes.

**Coordination with body .docx:** because this markdown is derived from the locked `hot-grower-body-v1.docx`, any body update **must** trigger a matching update here. The `template-version.md` ledger is the authoritative version gate for both files. The body hash and this template's hash are both tracked in `template-version.md` once v1.0 is formally approved by Jelmer.
