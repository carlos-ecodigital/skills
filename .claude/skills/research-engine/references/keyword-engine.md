# Keyword Engine

> Keyword generation, anti-keyword filtering, synonym expansion, and dynamic refinement.
> Used during block assembly (Phase 0) and refined after Phase 1 results.

## Core Term Extraction

Extract noun phrases from the research question. These are the seed terms.

**Algorithm:**
1. Parse the question for noun phrases (subjects, objects, proper nouns)
2. Remove stop words and meta-language ("what is the", "research the", "find out about")
3. Keep domain-specific terms intact (don't split "project financing" into "project" and "financing")

**Example:**
"What is the competitive landscape for BESS project financing in the Netherlands?"
→ Seed terms: `competitive landscape`, `BESS`, `project financing`, `Netherlands`

## Keyword Cluster Expansion

Expand each seed term into a cluster of search-ready variants.

| Expansion Type | Purpose | Example for "BESS" |
|---|---|---|
| **Synonyms** | Capture different phrasings | battery energy storage, battery storage, energy storage system |
| **Domain jargon** | Catch specialist terminology | ESS, grid-scale battery, utility-scale storage, stationary storage |
| **Abbreviations** | Catch shortened forms | BESS, ESS |
| **Dutch equivalents** (NL topics) | Catch Dutch-language sources | batterijopslag, energieopslagsysteem |
| **Related concepts** | Catch adjacent topics | energy storage market, battery deployment, storage capacity |

**Rules:**
- Generate 3-7 variants per seed term
- Prioritize specificity over breadth (don't expand so far that results become noisy)
- For Dutch-language expansion, only activate when the topic is NL-specific

## Anti-Keyword Generation

Anti-keywords are terms that share vocabulary with the target topic but would pollute results. They are appended to searches as negative operators.

**Algorithm:**
1. For each seed term, identify **homonyms** (same word, different meaning in different contexts)
2. Identify **adjacent but out-of-scope domains** that would contaminate results
3. Identify **common noise terms** that appear alongside the topic but add no value

**Worked Examples:**

| Seed Term | Anti-Keywords | Rationale |
|---|---|---|
| BESS (grid-scale) | "home battery", "EV battery", "consumer battery", "Tesla Powerwall", "portable" | Consumer-grade batteries are a different market |
| Project financing | "personal finance", "consumer loan", "mortgage", "student loan" | Different finance domain |
| Netherlands | "New Zealand" | NZ/NL confusion in some contexts |
| Data center | "data centre jobs", "careers", "hiring", "internship" | Job listings pollute company research |
| Immersion cooling | "swimming pool", "aquarium", "HVAC residential" | Residential cooling is different |
| AI infrastructure | "AI art", "AI chatbot tutorial", "prompt engineering guide" | Consumer AI content, not infrastructure |
| Grid congestion | "traffic congestion", "network congestion" (telecom) | Different domains use "congestion" |

**Rules:**
- Generate 2-5 anti-keywords per seed term
- Anti-keywords should be specific enough to exclude noise without excluding relevant results
- Test: would a relevant result ever contain this anti-keyword? If yes, don't use it.

## Source-Type Keyword Adaptation

Different source types respond better to different keyword formulations.

| Source Type | Keyword Strategy | Example (for BESS market) |
|---|---|---|
| **Academic** (Google Scholar) | Formal terminology + methodology terms | "battery energy storage system" "market analysis" "Netherlands" |
| **Government / regulatory** | Official terminology, statute names, agency abbreviations | "BESS" "SDE++" "RVO" "energieopslagsysteem" "Energiewet" |
| **News / media** | Current event framing, company names, deal names | "battery storage" "Netherlands" "project" "financing" 2025 2026 |
| **Industry reports** | Report-specific terms, publisher names | "BESS market size" "forecast" "BNEF" "outlook" "Europe" |
| **Company / PR** | Company names directly, product names | "Giga Storage" "GIGA Buffalo" "battery" "Netherlands" |

**Rules:**
- Generate 3-5 search queries per block using different keyword combinations
- Vary the source-type targeting across queries (don't run 5 identical news searches)
- Include at least one query targeting Tier 1 sources specifically

## Dynamic Refinement Protocol

After Phase 1 agents return results, review search performance and refine for Phase 2.

**Step 1: Noise audit.** Review Phase 1 results. Which searches returned irrelevant results?
- Identify the polluting terms (e.g., searches for "Giga Storage" returned Tesla Gigafactory results)
- Add polluting terms to anti-keywords for Phase 2

**Step 2: Gap analysis.** Which sub-questions got zero or weak results?
- Try alternative keyword angles (e.g., Dutch terms instead of English)
- Try different source types (e.g., government sources instead of news)
- Try broader or narrower scope

**Step 3: Dispatch refined queries.** Phase 2 deepening agents get the refined keyword sets.

**Constraints:**
- Maximum 2 refinement rounds (Phase 1 → Phase 2 → stop). Prevents infinite keyword chasing.
- Each refinement must change at least 2 keywords or add at least 2 anti-keywords. If the refinement is trivial, skip it.
