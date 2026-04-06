---
name: loi-generator
description: >-
  LOI/NCNDA generation engine for Digital Energy. Takes a natural language brief
  from any team member and produces a complete, ready-to-sign Letter of Intent
  with embedded confidentiality and non-circumvention provisions. Supports three
  LOI types: End User (enterprises, AI labs, startups buying compute directly),
  Distributor (partners who package DE capacity with their own services or refer
  customers), and Wholesale (neoclouds buying bulk capacity for resale). Also
  supports Distributor Mode B (referral-only partners). This skill should be
  used when the user says "generate an LOI", "draft an LOI", "create an LOI",
  "LOI for [company]", "letter of intent for [company]", "prepare an LOI",
  "new LOI", "LOI NCNDA", "we need an LOI for", "draft a letter of intent",
  "prepare documents for [company]", "colocation agreement for", "partnership
  agreement for", "prepare commercial documents", or any request to produce
  a pre-contractual document for a colocation customer or channel partner.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - AskUserQuestion
  - WebSearch
  - WebFetch
  - mcp__2c81bf85-2089-44af-a3a9-1de82f765ed9__search_crm_objects
  - mcp__2c81bf85-2089-44af-a3a9-1de82f765ed9__get_crm_objects
---

# LOI-GENERATOR — Letter of Intent Production Engine

## Role

You produce complete, ready-to-sign LOI/NCNDA documents for Digital Energy. Any team member can request an LOI by describing the counterparty and the relationship in natural language. You determine the correct type, gather missing information, generate the document, run a quality check, and output a .docx.

## Source Files

All templates and the generation script live at:
`This skill's directory (`.claude/skills/loi-generator/`):`

Key files:
- `templates/DE-LOI-Distributor-v3.0_TEMPLATE.md` — Distributor template (Mode A: Combined / Mode B: Referral)
- `templates/DE-LOI-Wholesale-v3.0_TEMPLATE.md` — Wholesale template
- `templates/DE-LOI-EndUser-v3.0_TEMPLATE.md` — End User template
- `ASSEMBLY_GUIDE.md` — Type selection logic, bespoke examples, defaults, red-line protocol
- `FEATURE_MATRIX.md` — What goes into each type
- `generate_loi.py` — YAML intake → .docx generation script (DE branding integrated)
- `examples/intake_example_*.yaml` — Example intake files for each type

## Workflow

### Step 1: Understand the Request

The user will say something like:
- "Generate an LOI for Lambda — they want 10 MW of colocation"
- "We need an LOI for TechForce, they're an SI who wants to resell our capacity"
- "Draft an LOI for Meridian AI, small startup, wants bare metal"
- "Prepare an LOI for Nordic Advisors, they'll be referring enterprise customers to us"

From this, determine:
1. **Counterparty name** and what they do
2. **Relationship type** → which LOI type to use
3. **Key commercial terms** mentioned (capacity, territory, service model)

### Step 2: Classify the LOI Type

Read `ASSEMBLY_GUIDE.md` for the type selection logic. Apply this decision tree:

| If the counterparty... | Type |
|---|---|
| Buys compute directly for their own use | **End User** |
| Packages DE capacity with their own services to sell to end users | **Distributor (Mode A)** |
| Introduces customers to DE but doesn't deliver services | **Distributor (Mode B)** |
| Buys capacity in bulk to resell to their own customers (neocloud/GPU cloud) | **Wholesale** |

Tell the user which type you've selected and why. Confirm before proceeding.

### Step 3: Gather Missing Information

Check what the user has provided against the required fields for that type. Ask for what's missing. Be efficient — ask all missing fields in one question, not one at a time.

**Always required (all types):**
- Counterparty legal name, short name, address, jurisdiction
- Registration type and number (KvK, Company No., EIN)
- Contact person name and title
- Signatory name and title (may be same as contact)
- Brief description of the counterparty (for Recital B)

**Type-specific required:**
- **End User:** Service model (Bare Metal / Shared Cloud / Tokens), indicative capacity, minimum term
- **Wholesale:** DEC Block count / MW, minimum term, expansion target
- **Distributor Mode A:** Bespoke Cl. 3 text (you write this — see Step 4), territory, target segments, estimated capacity
- **Distributor Mode B:** Territory, target segments, estimated capacity

**Choices to confirm:**
- Include indicative pricing? (default: no — defer to MSA)
- Existing NDA in place? (default: no — embed NCNDA)
- Any bespoke closing line?
- Wholesale only: deployment phasing?
- Distributor only: preferred partner / exclusivity?

**If user doesn't know registration details:** Accept what they have. Flag missing fields with [TO BE CONFIRMED] in the output. The document can still be generated.

**If counterparty is in HubSpot:** Search HubSpot for the company to pre-fill known details (address, registration, contacts).

### Step 4: Write Bespoke Text (Distributor Only)

For Distributor LOIs, you must write Cl. 3.1 (Partnership Overview) and Cl. 3.2(b) (Partner Service Scope) as bespoke text. Do NOT copy template examples verbatim.

Read the examples in `ASSEMBLY_GUIDE.md` for the closest archetype, then adapt:
- **What does this specific partner do?** (their core capability, in their language)
- **What do they bring to the partnership?** (customer relationships, technical capability, market presence)
- **What does the combined offering enable?** (what the end user gets that neither party delivers alone)
- **What's their specific service scope?** (comprehensive — can be narrowed in MSA)

Write with heart. These words define the relationship. Be specific to this partner, not generic.

### Step 5: Generate the YAML Intake

Create a YAML intake file with all gathered parameters. Use the example files as templates:
- `intake_example_distributor.yaml` for Distributor Mode A
- `intake_example_distributor_referral.yaml` for Distributor Mode B
- `intake_example_wholesale.yaml` for Wholesale
- `intake_example_enduser.yaml` for End User

Fill all fields. Use defaults from `ASSEMBLY_GUIDE.md` for protection parameters:
- Confidentiality survival: 3 years
- NC duration: 24 months
- PBI survival: 10 years (Distributor only)
- LOI validity: 12 months from LOI date
- Programme: platform_mw = "100+", site_count = "14" (confirm with CPO if changed)

### Step 6: Generate the Document

Run the generation script:
```bash
cd /path/to/skills/.claude/skills/loi-generator
python3 generate_loi.py examples/intake.yaml --output /path/to/output.docx
```

### Step 7: Quality Check (MANDATORY)

Before presenting the output, run these checks:

**Completeness:**
- [ ] All [PLACEHOLDER] text resolved? (search for `[` in the .docx)
- [ ] Counterparty name consistent throughout?
- [ ] Correct LOI type and mode?
- [ ] Recital A uses the correct variant for this type?
- [ ] Recital B accurately describes the counterparty?
- [ ] Cl. 3 matches the actual relationship?
- [ ] Cl. 5 (Project Finance) present?
- [ ] Cl. 6 uses correct ALT (A or B)?
- [ ] Cl. 7 (Non-Circumvention) present/absent as expected for this type?
- [ ] Signature blocks have correct names and titles?

**Brand compliance:**
- [ ] No "data center" (must be "Digital Energy Center" or "DEC")
- [ ] No "waste heat" (must be "energy recycling")
- [ ] No "Superpod" (must be "DEC Block")
- [ ] No geography lock in Recital A (should be sovereignty-agnostic)

**Legal consistency:**
- [ ] Dutch law, Amsterdam courts, CISG excluded?
- [ ] eIDAS electronic signatures referenced?
- [ ] Good faith clause references Art. 6:248 BW?
- [ ] Binding/non-binding status correctly stated?
- [ ] Survival periods match defaults (3yr confidentiality, 24mo NC, 10yr PBI)?

**Tone:**
- [ ] Institutional calm register — no promotional language?
- [ ] First sentences do work — no throat-clearing?
- [ ] Bespoke text (Distributor Cl. 3) reads as written for this partner, not a template?

### Step 8: Present to User

Tell the user:
1. What type of LOI was generated and why
2. The output file location
3. Any fields marked [TO BE CONFIRMED] that need completion
4. Any choices you made on their behalf (and why)
5. Remind them to review before sending — especially Cl. 3 (commercial terms) and Recital B (counterparty description)

## Defaults

| Parameter | Default | Source |
|---|---|---|
| Provider legal name | Digital Energy Netherlands B.V. | Standard |
| Provider signatory | Confirm with user | — |
| Programme MW | 100+ | Confirm with CPO if changed |
| Site count | 14 | Confirm with CPO if changed |
| Confidentiality survival | 3 years | All types |
| NC duration | 24 months | Distributor + Wholesale |
| PBI survival | 10 years | Distributor only |
| LOI validity | 12 months | All types |
| Pricing included | No (defer to MSA) | Override if user specifies pricing |
| NDA exists | No (embed NCNDA) | Override if user confirms existing NDA |

## Branded Formatting

All LOI .docx output MUST use the document-factory letterhead system for consistent branding. After generating the LOI content via `generate_loi.py`, apply the branded cover page and headers/footers:

1. The LOI .docx should use the `agreement` profile formatting from `document-factory`:
   - Cover page with DE logo, document title, counterparty name, date, "Confidential" classification
   - Header on continuation pages: small DE logo (left) + document title (right)
   - Footer on all pages: `Digital Energy Group AG | Baarerstrasse 43, 6300 Zug | CHE-408.639.320 | digital-energy.group`
   - Inter font, A4 margins (25mm left, 20mm right)

2. The `generate_loi.py` script handles this internally. If producing a manual LOI, use the branded .dotx template from:
   - **Google Drive:** `NEW_Marketing/DE_Marketing/DE_Brand_Assets/03_Templates/Document_Templates/DE_Agreement.dotx`
   - **Skills repo:** `.claude/skills/document-factory/generate.py --profile agreement`

**Cross-reference:** See `document-factory` skill for the full template system, CLI reference, and entity configuration.

## What This Skill Does NOT Do

- It does not send the LOI. The human reviews and sends.
- It does not negotiate terms. Use the `legal-counsel` skill for red-line responses.
- It does not create the Master Introduction Agreement (DE-MIA). That is a separate workstream.
- It does not produce MSAs, Sales Order Forms, or SLAs. Those are post-LOI documents.
- It does not make up counterparty details. If information is missing, it asks or flags [TO BE CONFIRMED].
