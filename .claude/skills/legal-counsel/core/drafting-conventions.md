# Drafting Conventions

Standard drafting rules for all contract and legal document generation.

## Language and Style

- Write in plain English. Avoid archaic legalese ("hereinafter", "witnesseth", "whereas" in operative clauses).
- Use "will" for obligations, "may" for permissions, "must" for conditions precedent.
  - **Exception**: Use "shall" when drafting under English law (established convention).
  - **Exception**: Use "skal" when drafting in Norwegian.
- Prefer active voice. Each clause should address one topic.
- Use gender-neutral language throughout.
- Do not use horizontal rules (`---`) to separate sections. Contracts should flow as continuous text with section headings.

## Defined Terms

- Define every capitalised term before or on first use.
- Introduce each defined term on first use in bold with quotation marks: the "**Services**".
- Do not use a capitalised term before defining it.
- Consolidate all definitions in Section 2 (Definitions and Interpretation), with contextual definitions permitted in operative clauses where the term is used only within that section.

## Numbering

- Number all clauses hierarchically: 1., 1.1, 1.1(a), 1.1(a)(i).
- Include cross-references between related clauses (e.g., "subject to Clause 13.2").
- Schedules numbered separately: Schedule 1, Schedule 2, etc.

## Jurisdiction Adaptation

When drafting for a specific jurisdiction, always load the jurisdiction's `contract-law.md` and `terminology.md` files and adapt:

- **Netherlands**: Reference BW articles. Use Dutch legal concepts where appropriate (ingebrekestelling, boeteclausule). Note mandatory provisions (Art. 6:94 BW penalty moderation, Art. 6:248 BW reasonableness and fairness override).
- **Norway**: Reference relevant Norwegian statutes (avtaleloven, kjøpsloven). Use "skal" obligations pattern in Norwegian-law agreements. Consider avtaleloven § 36 fairness control for B2B terms.
- **England and Wales**: Use "shall" for obligations. Reference UCTA 1977 for B2B liability exclusions. Use "Party" (capitalised). Note entire agreement clause significance under English law.
- **United States**: Vary by state. Reference UCC Article 2 for goods components. Note that "material adverse effect" standard differs by state. Delaware law common for corporate matters. Include jury trial waiver where appropriate.
- **Other jurisdictions**: Use internationally recognised conventions. Draft in plain English. Flag jurisdiction-specific requirements with `[LOCAL LAW NOTE: verify under {{jurisdiction}} law]`.

## Output Format

- Produce agreements as a single Markdown document.
- Structure: title block, numbered sections, defined terms in bold on first use, schedules as appendices, signature block before schedules.
- Mark any unresolved items or items requiring legal review with `[REVIEW REQUIRED: reason]`.
- Mark items requiring local law verification with `[LOCAL LAW NOTE: description]`.

## Bilingual Terminology Convention

For non-English jurisdictions (NL, NO), use the local-language term with English translation in parentheses on first use:
- "ingebrekestelling (notice of default)"
- "fritaksmetoden (participation exemption)"
- "recht van opstal (right of superficies)"

After first use, either the local term or the English term may be used consistently.
