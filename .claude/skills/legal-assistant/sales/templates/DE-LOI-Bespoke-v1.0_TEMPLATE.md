# DE-LOI-Bespoke-v1.0 — Bespoke LOI Template

**Version:** v1.0  
**Type:** `Bespoke` (Pipeline A, sixth agreement type)  
**Status:** Active

## When to use Bespoke (and when NOT to)

The 5 templated LOI types cover the most common patterns:

| Type | For |
|---|---|
| `EndUser` | Direct procurement by a compute customer |
| `Distributor` | Channel / integration partner |
| `Wholesale` | NeoCloud / GPU cloud operator contracting MW capacity |
| `StrategicSupplier` | EPC, modular infrastructure, OEM vendor |
| `EcosystemPartnership` | Standards body, university, consortium |

**Use `Bespoke` when:**

- The deal has materially different clauses from the templated types (joint‑offering structure, consortium GTM, platform‑wide expansion language, etc.).
- Templated‑type fields would need to be abused/misused to model the deal.
- You want the full QA catalogue applied (banned phrases, Unicode arrows, etc.) but need free‑text clauses.

**Do NOT use `Bespoke` when:**

- One of the 5 templated types fits with minor tweaks. Prefer the templated type — you get structural correctness for free and contribute to the template library.
- You want to skip QA validation. `Bespoke` applies the full QA catalogue with no exemptions. Bespoke ≠ unvalidated.
- The deal is counsel‑supplied or counterparty‑supplied as a Word document. Use Pipeline B (`document‑factory/rebrand.py`) instead — it preserves the original authoring.

## Promotion path

If a pattern shows up 3+ times in `Bespoke` YAML, promote it to a new templated type. `Bespoke` is the escape hatch; the templated types are the compounding knowledge capture.

## YAML schema

```yaml
type: Bespoke

# All three are optional overrides. Defaults:
#   agreement_type: "Letter of Intent"
#   subject:        "Bespoke Engagement"
#   party_label:    "Counterparty"
agreement_type: "Letter of Intent"
subject: "..."
party_label: "Partner"      # e.g. Partner, Customer, Supplier, Counterparty

provider:
  short_name: "Digital Energy"
  signatory_name: "..."
  signatory_title: "..."

counterparty:
  name: "...  B.V."         # required
  short: "..."              # required
  description: >-           # required; 1–2 sentences
    a Netherlands-based ...

programme:
  recital_a_variant: default    # or sovereignty | integration | bespoke

dates:
  loi_date: "YYYY-MM-DD"    # required

# Optional supplementary recitals (beyond A and B which are auto-generated).
# Recital A is always library-sourced (see programme.recital_a_variant).
# Recital B is auto-generated from counterparty.short + counterparty.description.
recitals:
  - letter: "C"             # required; uppercase single char by convention
    text: "..."             # required; one sentence, no salesy adjectives
  - letter: "D"
    text: "..."

# Required; at least one clause. Free-text content, structure enforced.
clauses:
  - number: "1"             # required; string (supports 1 / 1.1 / etc. if needed)
    heading: "..."          # required; title-case phrase
    paragraphs:             # required; list of >= 1 paragraph text
      - "1.1 ..."
      - "1.2 ..."
    subclauses:             # optional; lettered (a), (b), (c) items
      - letter: "a"
        text: "..."
      - letter: "b"
        text: "..."

  - number: "2"
    heading: "..."
    paragraphs:
      - "..."
```

## What the renderer does

1. **Cover** — `letterhead()` via the shared `document-factory/add_cover` (same DE branding as the 5 templated types).
2. **Recitals** — (A) from the library (variant driven by `programme.recital_a_variant`), (B) auto-built from `counterparty.short` + `counterparty.description`, (C)… from the optional `recitals:` list.
3. **Clauses** — walks `clauses:` in order. Each becomes `Heading 1` + body paragraphs + optional `(a)/(b)` subclauses. No definitions section, no prescribed Cl. 5 / Cl. 7 — include what the deal needs directly.
4. **Signature** — shared signature block used by all types.
5. **Footer** — `DE-LOI-Bespoke-v1.0` version stamp.

## QA gate

The full `_shared/loi-qa-gate.md` catalogue applies to `Bespoke` output with no exemptions:

- **R-1** banned commitment‑term language
- **R-7** Unicode arrows (`→` `⇒` `➜` …) — template/copy-paste bug
- **R-14** salesy adjectives in Recital B
- **R-21** (document-factory, via `audit_agreement`) — cover carries parties → no `THE UNDERSIGNED` block in body
- all other fail/warn/info rules

Overrides via the usual mechanism (`--override R-11 --override-reason "…"`) if a specific rule is demonstrably inapplicable.

## Filename

`YYYYMMDD_DEG_LOI-Bespoke_{CounterpartyShort}_(DRAFT).docx` (same convention as templated types; the `Bespoke` token identifies it at a glance in SSOT).

## See also

- `examples/intake_example_bespoke.yaml` — minimal runnable example
- `_shared/loi-qa-gate.md` — full rule catalogue
- `document-factory/rebrand.py` — Pipeline B alternative when the deal is already drafted in Word
