# Decomposition Engine

> The algorithm for breaking any research question into parallel, searchable blocks.
> This is the core intellectual engine of the research skill.

## Intent Classification

Every research question falls into one of four intent types. Classify before decomposing.

| Intent Type | Signal Words | Example | Implications |
|---|---|---|---|
| **Exploratory** | "what is", "landscape", "overview", "map" | "What is the competitive landscape for BESS in NL?" | Cast wide net. Entity mapping + trend analysis strategies. Multiple dimensions. |
| **Evaluative** | "compare", "which", "better", "pros and cons" | "Compare single-phase vs two-phase immersion cooling" | Structured comparison. Same dimensions measured across options. Side-by-side output. |
| **Confirmatory** | "is it true", "verify", "fact check", "validate" | "Is it true that TenneT has 6 GW of transport capacity requests?" | Narrow search. Find the primary source. Confirm or deny with citation. |
| **Quantitative** | "how much", "what is the number", "size", "price" | "What is the current FCR price in the Netherlands?" | Find the specific number. Prioritize Tier 1 sources. Recency critical. |

## Dimension Extraction

Every research question has 1-5 orthogonal dimensions. Extract them explicitly.

**Algorithm:**
1. Identify the **subject** (what entity/concept is being researched)
2. Identify the **aspect** (what about it — size, players, structure, rules, technology)
3. Identify the **scope** (geographic, temporal, industry boundaries)
4. Identify **implicit dimensions** (timeframe if not stated, comparison baseline if evaluative)

**Worked Example:**
Question: "What is the competitive landscape for BESS project financing in the Netherlands?"

| # | Dimension | Type | Sub-Questions Generated |
|---|---|---|---|
| 1 | Competitors/players | Entity mapping | Who are the active BESS project finance lenders in NL? Which advisory firms are active? |
| 2 | Financing structures | Qualitative | What deal structures have been used for Dutch BESS projects? What are typical terms (gearing, DSCR, tenor)? |
| 3 | Netherlands jurisdiction | Scope constraint | Applied as geographic filter to all searches, not a separate block |
| 4 | BESS asset class | Scope constraint | Applied as topic filter; generates anti-keywords (exclude home/EV battery) |
| 5 | Current timeframe (implicit) | Temporal scope | Focus on 2024-2026 data; recency weighting applied |

## Sub-Question Generation Rules

For each substantive dimension (not scope constraints), generate 2-4 specific, answerable sub-questions.

**Rules:**
- Each sub-question must be answerable from publicly available sources
- Each sub-question should target a specific piece of information, not a broad topic
- Tag each with: research type (quantitative/qualitative), expected source tier, estimated difficulty (straightforward/moderate/deep)
- Avoid compound questions — split "What are the players and their market shares?" into two sub-questions

**Quality test:** Could a research analyst hand this sub-question to a junior researcher and get back a useful, focused answer? If not, decompose further.

## Dependency Mapping

Most sub-questions are independent (80-90%) and can run in parallel.

**Rule:** B depends on A only if B requires the *answer* to A, not just the same topic.

| Dependency Type | Example | Treatment |
|---|---|---|
| Independent | "Who are the lenders?" and "What are typical terms?" | Phase 1 — run in parallel |
| Soft dependency | "How do NL terms compare to EU?" needs NL terms first | Phase 2 — runs after Phase 1 with NL terms as context |
| Hard dependency | Rare in research. More common in execution tasks. | Phase 2 — blocked until dependency resolves |

Default assumption: blocks are independent unless proven otherwise.

## Block Assembly

Each research block is a self-contained task for a search agent.

**Block specification:**
```
Block ID: {dimension}_{sub_question_number}
Question: {specific sub-question}
Strategy: {quantitative scan | entity mapping | regulatory review | trend analysis | comparative analysis | opinion synthesis}
Primary keywords: {3-5 terms}
Anti-keywords: {1-3 exclusion terms}
Target source types: {Tier 1-2 government | Tier 1-2 media | Tier 2-3 industry | all}
Expected output: {data table | entity list | narrative summary | timeline | comparison matrix}
Confidence threshold: {HIGH required | MEDIUM acceptable | any}
Tool budget: {3-5 searches for standard | 5-8 for deep}
```

## Strategy Classification

Each block gets a strategy tag that determines how the search agent approaches it.

| Strategy | When | Approach | Typical Sources |
|---|---|---|---|
| **Quantitative scan** | Looking for numbers, metrics, data points | Focus on Tier 1 sources. Extract exact figures with citations. Cross-check across sources. | Reports, databases, filings |
| **Entity mapping** | Looking for companies, people, organizations | Cast wide net across Tier 1-2. Cross-reference lists. Aim for completeness. | News, industry reports, association directories |
| **Regulatory review** | Looking for rules, requirements, legislation | Tier 1 only. Exact statute references. Check for recent amendments. | Government sites, law firm publications, official gazettes |
| **Trend analysis** | Looking for direction, momentum, change over time | Multiple data points over time. Recency weighted. Tier 1-2. | Time-series data, analyst reports, news archives |
| **Comparative analysis** | Comparing options, approaches, markets | Structured data collection across a common framework. Side-by-side output. | Multiple sources per comparator |
| **Opinion synthesis** | Looking for expert views, market sentiment | Tier 2-3 acceptable. Attribution required. Diversity of viewpoints. | Analyst commentary, expert interviews, opinion pieces |

## Multi-Hop Discovery

During execution, search agents may discover related questions not in the original plan.

**Rules for multi-hop:**
- Agents can propose new blocks in their output under `suggested_follow_up`
- The orchestrator evaluates proposals: is this within scope? Would it strengthen the brief?
- Maximum 3 new blocks per phase (prevents unbounded expansion)
- New blocks execute in the next phase, not the current one
- Anti-pattern: do not follow every tangent. Only follow discoveries that directly strengthen the original research question.
