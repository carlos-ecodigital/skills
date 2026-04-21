# LOI Common Defined Terms — Library

Reusable definitions for injection into LOI Cl. 2 Definitions. Consumed by
`legal-assistant/colocation/generate_loi.py` via the intake-YAML field
`custom.definitions_include: [super_factory_initiative, ...]`.

Pattern: each term has a **key** (snake_case, stable), a **text** body
(definition as it appears in the LOI), **usage notes** (when to include),
and **types** (LOI types that should include it). Operators choose via the
intake-YAML include list; engine injects in list order at the top of Cl. 2.

Adding verbatim free-text into `custom.definitions` still works — the
library is a convenience for recurring terms, not a replacement.

## Super-Factory Initiative

- **Key:** `super_factory_initiative`
- **Types:** StrategicSupplier, Wholesale (when referenced in programme framing)
- **Text:**

> **"Super-Factory Initiative"** means the Provider's programme to deploy a
> network of AI-ready modular data-centre sites across Europe, integrating
> accelerated-compute capacity with heat recycling and behind-the-meter
> power production, whether as independent-node inference facilities or as
> a unified compute fabric (such as through NVIDIA Spectrum-XGS scale-across
> architecture). The Provider may engage additional suppliers and partners
> within the Initiative on independent terms.

- **Usage:** Counterparty-neutral, programme-level term. Keep the "Provider's
  programme" phrasing (not "joint programme") — ownership stays with DE. Names
  the initiative without tying it to any single supplier; allows parallel-
  supply relationships (Vertiv, Armada, InfraPartners).

## Designated Site

- **Key:** `designated_site`
- **Types:** StrategicSupplier (when `supplier.rofr` block is populated), Wholesale
- **Text:**

> **"Designated Site"** means a named site within Digital Energy's active
> development pipeline for which the Provider has identified a specific
> scope of supply or services and has given the counterparty written
> notice of a defined response window for commercial engagement.

- **Usage:** Required whenever the LOI's RoFR or capacity-reservation
  mechanics reference named sites rather than the full pipeline. Pair with
  `supplier.rofr.site_scope` intake field.

## Framework Agreement

- **Key:** `framework_agreement`
- **Types:** StrategicSupplier (all variants)
- **Text:**

> **"Framework Agreement"** means the definitive written agreement between
> Digital Energy and the Supplier governing the scope, pricing, technical
> specifications, delivery, warranty, and commercial terms of Supplier's
> supply to the Provider, to be negotiated and executed following the
> date of this LOI. Until a Framework Agreement is executed, this LOI
> does not itself commit either Party to any specific commercial terms
> beyond the binding clauses identified in Clause 8.

- **Usage:** Replaces the MSA term for StrategicSupplier LOIs — reflects
  the supply-chain framing (supplier has multiple downstream agreements
  against one master framework) rather than the customer-services framing.

## DEC Block

- **Key:** `dec_block`
- **Types:** Internal / operator-only — **NEVER include in customer-facing
  clauses** (linter rule R-4 fails on body-level "DEC Block").
- **Text (internal-use only):**

> **"DEC Block"** means a standardised 1.2 MW IT compute unit comprising
> integrated power, cooling, and rack infrastructure engineered to accept
> accelerated-compute workloads at full density within a single deployable
> module.

- **Usage:** Operator-facing documentation only. Use "data centre module"
  or "1.2 MW IT compute unit" in LOI body text where an equivalent is
  needed. Listed here so internal operators have a canonical definition
  to reference when translating customer-facing language.

## Extending the library

When a new term recurs across ≥2 counterparties and ≥2 LOI types, promote
it here. Keep definitions parsimonious — LOI Cl. 2 is a reference point,
not a narrative section. Each term should fit in one paragraph.

When a term is genuinely counterparty-specific (e.g., a custom product
name, a bilateral programme), use `custom.definitions[]` inline in the
intake YAML rather than extending the library.
