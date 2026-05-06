# Kevin Hale — Atomized (v2 — re-extracted with causal-chain protocol)

**Source:** archive/hale-how-to-pitch-your-startup.md
**v2 changes:** HALE-001 + HALE-003 mechanisms upgraded; 2 new atoms added (HALE-008 time-pressure mechanism, HALE-009 noun-verb-object operational forcing).

**Atom count:** 9 (was 7).

---

## HALE-001 — The 3-Component Idea Frame ⟵ v2 UPGRADED

```yaml
atom_id: HALE-001
source: archive/hale-how-to-pitch-your-startup.md
expert: Kevin Hale
applies_to_questions: [Q-IDEA-1, Q-IDEA-2, Q-CO-7]
rule_type: framework
confidence: high
when_applies: Any idea description.
when_does_not_apply: Pure-research / pre-product technical bets where "solution" is "we are attempting to solve X" rather than a concrete product.
why_it_exists: Causal chain — (1) any startup is a hypothesis for rapid growth. (2) Rapid growth comes from competitor-resistant compounding — the company outpaces incumbents who have more resources. (3) Problem + solution alone is commodity: any team with the same problem-solution pair will compete on execution speed. (4) Insight is the third component because it's what ENABLES faster growth than competitors despite their resources — not a credibility-boost or a clever twist, but the structural reason this team will outpace incumbents. (5) Without insight, growth is execution-bound; with insight, growth is structurally compounded.
underlying_model: Insight = "unfair advantage" in the operational sense — the mechanism by which competitors with same problem and same solution still lose. Examples: distribution access (Facebook had Harvard), schlep tolerance (Stripe had bank-relationship willingness), demographic alignment (Airbnb had been hosts themselves). Without insight, the team is doing the same thing competitors are; with insight, the team is doing something competitors can't replicate even with more money.
contradicts: none
```

> 3 components: Problem (significant + widespread), Solution (stems from problem, not pre-existing tech), Insight / Unfair Advantage (what enables faster growth despite competitors' resources).

**Application implication:** Q-IDEA-1 strong answer makes all 3 visible: problem (specific, named pain), solution (concrete, demoable), insight (non-obvious mechanism by which competitors with similar resources still lose). Skill validates each Q-IDEA-1 draft for all 3 components present. Anti-pattern: stating insight as adjective ("we're better at X") instead of mechanism ("we have access to X that competitors structurally cannot get").

---

## HALE-002 — Lead with What, Not Why or How

```yaml
atom_id: HALE-002
source: archive/hale-how-to-pitch-your-startup.md
expert: Kevin Hale
applies_to_questions: [Q-CO-2, Q-CO-7]
rule_type: rule (compression)
confidence: high
when_applies: Q-CO-2 (50-char) and Q-CO-7. Lead sentence in both must be the "what."
when_does_not_apply: Q-IDEA-1 which is structurally a "why" question. Rule reversed there.
why_it_exists: Causal chain — (1) why and how presuppose context the partner doesn't have. (2) Without context, "why we're doing this" lands as undefined-pronoun-reference. (3) The partner has to construct context from later sentences — meaning the first sentence has wasted its budget. (4) Lead with what gives the partner an immediate noun to attach why and how to.
underlying_model: Information-density mechanism. Partners have ~5 minutes; the first sentence determines whether the next 4 minutes are productive (noun anchored, mom-test passable) or wasted (still constructing what the company is).
contradicts: none for Q-CO; complements PG-009 (clarity = competence).
```

> "Lead with 'what' your company does; 'why' and 'how' obscure clarity."

**Application implication:** Q-CO-2 / Q-CO-7 first sentence: noun-led, plain language, name the verb the user does, name the customer. Anti-pattern openers: "We believe...", "In a world where...", "We're building..."

---

## HALE-003 — X-for-Y Conditional (with collapse mechanism) ⟵ v2 UPGRADED

```yaml
atom_id: HALE-003
source: archive/hale-how-to-pitch-your-startup.md
expert: Kevin Hale
applies_to_questions: [Q-CO-2, Q-CO-7]
rule_type: conditional rule
confidence: high
when_applies: Whenever description uses "X for Y" analogy. ALL THREE conditions must hold.
when_does_not_apply: When description doesn't use the analogy — apply HALE-006 instead.
why_it_exists: Causal chain — (1) analogies work by transferring concept-clarity from a known X to an unknown business. (2) The transfer requires X to be more clearly understood than the target. (3) When X is smaller / less famous than Y, the transfer collapses: the partner has to think harder about X than about the actual business. (4) "Buffer for Snapchat" fails because Buffer (smaller) requires more explanation than Snapchat (larger) — the analogy makes the description WORSE than direct description. (5) Each of the 3 conditions guards a specific collapse mode: condition 1 (X recognized) prevents X-explanation tax, condition 2 (Y need clear) prevents motivation-construction tax, condition 3 (Y market large) prevents "interesting niche" dismissal.
underlying_model: Analogies are concept-loans. They work only when the lender has more concept-equity than the borrower. When the loan is reversed, the analogy actively damages comprehension by forcing partners to re-examine the lender.
contradicts: PG via /howtoapply (PG advises avoiding "Airbnb of X" entirely in description) — resolves: PG advises against in product description specifically; Hale conditional permits in idea/competition framing if all 3 hold. Documented in `contradictions-register.md` CONTRADICTION-002.
```

> Effective ONLY when:
> 1. X is universally recognized billion-dollar company
> 2. Y genuinely wants/needs that model (clear unmet need)
> 3. Y market is substantial enough to support a large business

**Application implication:** Skill detects "X for Y" usage and verifies all 3 conditions; flags if any unsatisfied. Default recommendation: avoid in Q-CO-2 / Q-CO-7 entirely (per PG); permit in Q-IDEA-1 / Q-IDEA-2 only if 3 conditions hold.

---

## HALE-004 — Mom-Test for Clarity

```yaml
atom_id: HALE-004
source: archive/hale-how-to-pitch-your-startup.md
expert: Kevin Hale
applies_to_questions: [Q-CO-2, Q-CO-7, Q-IDEA-1]
rule_type: validation test
confidence: high
when_applies: Every product description and idea explanation.
when_does_not_apply: Highly technical questions (Q-PROG-3 tech stack) where partner audience IS technical.
why_it_exists: Causal chain — (1) clarity isn't a virtue; it's the only way the description spreads via word-of-mouth. (2) Word-of-mouth spreading requires non-experts to repeat the description accurately. (3) Therefore the description must be reproducible by non-experts. (4) The mom-test ("explain like you're talking to your mom") is a proxy for reproducibility — if mom can repeat it, anyone can.
underlying_model: Comprehension is upstream of word-of-mouth. Without comprehension, no spread; without spread, no organic growth.
contradicts: none
```

> "Be conversational — explain it like you're talking to your mom."

**Application implication:** Skill validation gate: spawn fresh subagent unfamiliar with the company; have it explain Q-CO-2 / Q-CO-7 back. If clarification required, description fails.

---

## HALE-005 — Anti-Marketing-Speak (Banned Vocabulary)

```yaml
atom_id: HALE-005
source: archive/hale-how-to-pitch-your-startup.md + arc-tip-3 (Seibel corroboration)
expert: Kevin Hale + Seibel
applies_to_questions: [ALL written]
rule_type: anti-pattern (vocabulary)
confidence: high
when_applies: Every written response.
when_does_not_apply: Never.
why_it_exists: Causal chain — (1) AI-generated and consultant-trained writing converges on marketing language. (2) Partners pattern-match this register as substance-free. (3) Buzzwords substitute for thought; they're the verbal tic of someone hiding the actual idea. (4) Each banned word triggers a mini-rejection that the founder must overcome with later content.
underlying_model: Marketing language signals "this person doesn't have the idea, they have the slogan." Partners are calibrated to this signal because they see it constantly.
contradicts: none
```

> Banned: marketing speak, MBA jargon, buzzwords. Specifically (per Seibel via arc-tip-3): "platform," "revolutionize," "disrupt," "synergy," "innovate."

**Application implication:** Skill anti-pattern detection scans drafts. Includes "platform" (Seibel-named), plus general buzzword list: "leverage" (verb), "ecosystem," "seamless," "robust," "cutting-edge," "transform," "empower," "unlock."

---

## HALE-006 — Concrete Description Format

```yaml
atom_id: HALE-006
source: archive/hale-how-to-pitch-your-startup.md
expert: Kevin Hale
applies_to_questions: [Q-CO-2, Q-CO-7]
rule_type: pattern (positive)
confidence: high
when_applies: Default for any product description.
when_does_not_apply: Pre-product / research-stage with no concrete product yet.
why_it_exists: Causal chain — (1) Hale's exemplars (Airbnb, Dropbox, Lumini) all follow noun-led, action-specific format. (2) The format succeeds because partners must be able to describe the product to a colleague after one read. (3) Noun-led + verb-specific + customer-named gives partners a complete reproducible description in one sentence. (4) Any deviation requires partner to construct missing pieces, which costs cognitive budget.
underlying_model: Reproducibility = comprehension test. The format isn't aesthetic; it's the format that survives ~5-min-read partner workflow.
contradicts: none
```

> Hale's concrete examples:
> - **Airbnb:** "First online marketplace letting travelers book rooms with locals"
> - **Dropbox:** "Synchronizes files across your computers"
> - **Lumini:** "X-ray vision for soldiers and first responders"
>
> Template: [optional adjective] [marketplace / app / service / tool] for [user] to [verb] [object].

**Application implication:** Q-CO-2 / Q-CO-7 use this template. Skill produces 2-3 candidates; user picks. Each variant scored: noun-led? user named? verb specific? customer named? Within character limit?

---

## HALE-007 — Pre-amble Anti-Pattern

```yaml
atom_id: HALE-007
source: archive/hale-how-to-pitch-your-startup.md
expert: Kevin Hale
applies_to_questions: [Q-CO-2, Q-CO-7]
rule_type: anti-pattern
confidence: high
when_applies: Description fields specifically.
when_does_not_apply: Q-IDEA-1 where origin story is appropriate.
why_it_exists: Pre-amble burns the partner's most attentive moment on filler.
underlying_model: First-sentence real estate is highest-leverage. Pre-amble destroys it.
contradicts: none
```

> "Avoid preambles and storytelling [in the description specifically]."

**Application implication:** Skill flags openers: "We," "Our," "Imagine," "In today's," "The future of." Rewrite to noun-verb-object opening.

---

## HALE-008 — Time-Pressure Cognitive Budget (NEW — was missing in v1)

```yaml
atom_id: HALE-008
source: archive/hale-how-to-pitch-your-startup.md (mechanism extracted but never atomized in v1)
expert: Kevin Hale (corroborates ARC-001 Shen)
applies_to_questions: [ALL written]
rule_type: rule (mechanism — independent of HALE-007)
confidence: high
when_applies: Every written response.
when_does_not_apply: Never.
why_it_exists: Causal chain — (1) partners spend ~5 minutes per application. (2) That budget is cognitive, not just clock-time. (3) Every preamble word, every redundant phrase, every paragraph the partner re-reads costs a slice of that 5 minutes. (4) When the budget exhausts, the partner moves on regardless of remaining content. (5) Therefore information density per word is the binding constraint — not "make it sound good" but "make every word earn its budget."
underlying_model: Distinct from HALE-007 (preamble) — HALE-008 is the GENERAL principle applying to every section. Preamble is one form; redundancy is another; over-explanation is another. Anti-pattern is whatever wastes the cognitive budget.
contradicts: none
```

> "Be concise — demonstrates deep thought and efficiency."

**Application implication:** Skill brevity gate measures words per claim. Sections with low information-density-per-word (lots of words, few claims) flagged for compression.

---

## HALE-009 — Noun-Verb-Object Operational Forcing (NEW — was missing in v1)

```yaml
atom_id: HALE-009
source: archive/hale-how-to-pitch-your-startup.md (extracted from concrete-description discussion)
expert: Kevin Hale
applies_to_questions: [Q-CO-2, Q-CO-7]
rule_type: rule (mechanism behind HALE-006)
confidence: high
when_applies: Description fields. The WHY behind the noun-verb-object template.
when_does_not_apply: Never (universal for descriptions).
why_it_exists: Causal chain — (1) noun-led writing forces the writer to commit to what the company IS, not what it ASPIRES to be. (2) Verb-specific writing forces commitment to what the user DOES, not what they WILL do. (3) Customer-named writing forces commitment to who the user IS, not who they MIGHT be. (4) Aspirational writing ("We're building a platform that empowers...") evades all three commitments. (5) Therefore noun-verb-object isn't a stylistic preference — it's an operational forcing function that prevents aspirational hand-waving.
underlying_model: The template forces the founder to think operationally. Aspirational writing is the failure mode of founders who haven't done the operational thinking; the template prevents that failure.
contradicts: none
```

> Hale's pattern (extracted): noun-led + verb-specific + customer-named → forces operational commitment over aspirational hand-waving.

**Application implication:** Skill description-validator checks Q-CO-2 / Q-CO-7 drafts for noun-verb-object structure. Aspirational openers ("We're building...", "Our platform...") flagged as failure of operational forcing.

---

## Summary

**Atoms:** 9 (7 from v1 + 2 new HALE-008/009; HALE-001 + HALE-003 upgraded with mechanisms)
**Coverage:** Q-CO-2, Q-CO-7, Q-IDEA-1, Q-IDEA-2, Q-PROG-3 (peripheral)
