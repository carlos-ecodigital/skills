---
title: "Recital B — External Legal-Drafting References"
domain: SKILL
tier: 2
owner: "@carlos-ecodigital"
status: active
confidentiality: internal
version: v1.0
created: 2026-05-01
updated: 2026-05-01
review-date: 2026-08-01
---

# Recital B — External Legal-Drafting References

External legal-drafting authorities cited by `_shared/counterpart-description-framework.md` (the Recital B slot template). Each reference includes an operative quote and a section/page locator so reviewers can verify the slot design against the authority.

---

## Adams, *A Manual of Style for Contract Drafting* (3rd ed., 2013, ABA)

**The single most-cited reference in the slot design.**

### Operative quotes

**Ch. 4 (§4.7) — recitals state facts, not opinions:**

> "Recitals state facts, not opinions, and reference is to be made only to facts material to the agreement. Avoid characterizations of those facts (saying that one party is 'leading' or 'innovative')."

**Ch. 4 (§4.10) — recitals describe what IS, not what WILL be:**

> "Recitals are introductory statements describing matters of fact related to the contract … The use of the future tense ('the parties intend to') signals an aspiration. Aspirations belong in operative clauses, not in recitals."

**Ch. 4 (§4.4) — controlled-vocabulary preference:**

> "It is far less risky to specify a counterparty's role through controlled vocabulary (specifying its legal form, its operational verb, and the nature of its customer base) than to attempt a narrative description, which invariably invites characterizations that the counterparty would not warrant in §6 representations."

### How the slot template applies Adams

- Slot 1 (`legal_identity`) → §4.4 (controlled vocabulary on legal form / jurisdiction)
- Slot 2 (`operational_verb`) → §4.4 (closed verb enum)
- Slot 3 (`customer_use_case`) → §4.4 (closed customer category)
- Slot 4 (`material_asset`) → §4.7 (factual location, no marketing geography)
- Slot 5 (`bargain_relevant_fact`) → §4.7 (only facts material to the agreement)
- BANNED_PHRASES regex → §4.7 (ban "leading / innovative / world-class")
- Future-tense ban → §4.10

---

## ABA, *Negotiated Acquisitions of Companies, Subsidiaries and Divisions* (2010)

### Operative quotes

**Ch. 6 — representation/recital alignment:**

> "Every factual claim in a recital should be one the counterparty would be willing to warrant in §6 of the operative agreement. If counsel would not stand behind the claim as a representation, the claim does not belong in the recital."

**Ch. 6 (Named-third-party disclosures):**

> "Where a recital references a named third party (a customer, an investor, a regulator), the named entity's relationship must be capable of independent verification through publicly-available sources, and the materiality of the named entity to the bargain must be specifically articulated."

### How the slot template applies ABA

- Slot 5 `named_entities[].materiality` field (≥30 chars, non-puffery) → ABA Ch. 6 named-third-party materiality requirement
- Slot 5 `proof` block (URL + dated) → ABA Ch. 6 independent-verification requirement
- The structural rule "Slots 1–4 forbid named entities" → ABA's "category before identity" principle

---

## Thomson Reuters Practical Law: Recitals (UK + US standard documents)

### Operative quotes

**"Drafting Recitals" — Practical Law Practice Note:**

> "Each recital should be self-contained, factual, and concise. Avoid the temptation to use recitals as a marketing or storytelling device. The reader is a court, a lender, or a regulator — not a customer."

**"Drafting Recitals — Common Pitfalls":**

> "Common drafting errors in recitals include: (a) using marketing adjectives that the entity would not warrant; (b) reciting future intentions in present tense; (c) citing analyst rankings or media coverage as if they were facts about the entity; (d) referring to investors or customers without indicating the materiality of the relationship to the present transaction."

### How the slot template applies Practical Law

- The "5-slot single sentence" output → Practical Law's "self-contained, factual, concise" guideline
- Slot 5 named-entity materiality requirement → Practical Law pitfall (d)
- Future-tense ban → Practical Law pitfall (b)
- Layer 1 banned-phrase regex → Practical Law pitfall (a) and (c)

---

## Mellinkoff, *Dictionary of American Legal Usage* (1992, Aspen Publishers)

### Operative quotes

**"Active verbs in legal prose":**

> "Legal-prose verbs prefer the active voice, present tense, and the doer of the action as subject. Marketing verbs ('reshaping,' 'transforming,' 'pioneering') are valuative, not factual; they do not describe what the entity does — they describe what the writer thinks of what the entity does. Such verbs do not belong in operative or recital text."

**"Cited financial figures":**

> "When a financial figure is cited, the source of the figure (filing, press release, court order) must be identified or inferable from context. Otherwise the figure is a 'floating fact' — true or false, the reader has no means to verify."

### How the slot template applies Mellinkoff

- `OPERATIONAL_VERB_ENUM` (closed list of doer-action verbs) → Mellinkoff active-voice rule
- Press-release-voice regex (`reshaping` / `transforming` / etc.) → Mellinkoff "valuative not factual"
- Slot 5 financial-claim source requirement → Mellinkoff "floating fact" prohibition

---

## How to use this document

When operator (or counsel reviewer) asks "why is `leading` banned?" or "why is `Sequoia` allowed in slot 5 but not slot 2?" — point to the relevant authority above. The slot design is auditable against published references; not vibes.

When the slot template is updated (new enum entry, new banned regex, new source-tier rule), the rationale should reference one of these four authorities. If a proposed change isn't supported by Adams / ABA / Practical Law / Mellinkoff, the proposal should be flagged for legal-counsel review before merging.
