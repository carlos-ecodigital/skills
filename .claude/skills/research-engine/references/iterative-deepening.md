# Iterative Deepening

> The 3-phase progressive refinement model. Based on Step-DeepResearch (arXiv 2512.20491).
> Loaded for Deep Dive workflow. Standard Brief uses Phase 1-2 only.

## Why Iterative (Not One-Shot)

One-shot research dispatches all agents simultaneously and hopes the results are sufficient. This fails for complex topics because:
- You don't know what you don't know until after Phase 1
- Multi-hop discovery reveals related questions only after initial results
- Keyword refinement requires seeing what Phase 1 noise looked like
- Dependent blocks can't run until their prerequisites complete

Step-DeepResearch showed 90.2% improvement over single-pass approaches by using progressive refinement. The quality gain comes from iteration, not from dispatching more agents in parallel.

## Phase Model

### Phase 1: Broad Reconnaissance

**Goal:** Maximum coverage across all research dimensions with minimum depth.

**What happens:**
1. All independent blocks from the decomposition dispatch as parallel Search Agents
2. Each agent runs 3-5 searches with varied keyword combinations
3. Each agent self-critiques before returning
4. Orchestrator collects all findings

**Duration:** ~60-80% of total research effort for Quick Lookup. ~30-40% for Standard Brief. ~20-30% for Deep Dive.

**Exit criteria:** All Phase 1 agents have returned (completed or timed out).

### Phase 2: Targeted Deepening

**Goal:** Fill gaps and deepen weak areas identified in Phase 1.

**What happens:**
1. **Coverage assessment:** Map Phase 1 findings back to original sub-questions
   - Strong coverage (>=2 Tier 1-2 sources): DONE — no further research needed
   - Weak coverage (1 source, or Tier 3 only): DEEPEN — dispatch Deepening Agent
   - No coverage: GAP — dispatch Deepening Agent with alternative angles
2. **Multi-hop discovery:** Review Phase 1 findings for new questions
   - Agents may have proposed `suggested_follow_up` blocks
   - Orchestrator evaluates: within scope? Strengthens the brief? -> Accept (max 3 new blocks)
3. **Keyword refinement:** Review Phase 1 noise
   - Which searches returned irrelevant results? -> Add polluting terms to anti-keywords
   - Which keywords worked well? -> Reuse patterns for weak blocks
4. **Dependent blocks:** Execute blocks that needed Phase 1 answers as input
5. **Deepening dispatch:** All Phase 2 agents run in parallel

**Duration:** ~40-50% of effort for Standard Brief. ~30-40% for Deep Dive.

**Exit criteria:** All Phase 2 agents returned. No sub-question has zero coverage (or has been explicitly flagged as a knowledge gap).

### Phase 3: Verification & Gap Filling (Deep Dive Only)

**Goal:** Stress-test the findings and close remaining gaps.

**What happens:**
1. **Validation Agent** cross-checks all findings (corroborations, contradictions, duplicates)
2. **Adversarial debate** if triggered by high-stakes contradictions
3. **Final gap scan:** Any sub-questions still at LOW or PRELIMINARY? One more targeted search
4. **Synthesis** begins after Phase 3 completes

**Duration:** ~20-30% of Deep Dive effort.

**Exit criteria:** Validation complete. Debates resolved. All gaps either filled or explicitly documented.

## Phase Transition Triggers

| From | To | Trigger |
|---|---|---|
| Phase 1 -> Phase 2 | All Phase 1 agents returned | Automatic |
| Phase 2 -> Phase 3 | All Phase 2 agents returned (Deep Dive only) | Automatic |
| Phase 2 -> Synthesis | All Phase 2 agents returned (Standard Brief) | Automatic |
| Any Phase -> Stop | Token budget exhausted | Force stop, synthesize what exists |
| Any Phase -> Stop | All sub-questions at MEDIUM+ confidence | Early exit — quality threshold met |

## Stopping Criteria

Research stops when ANY of these is true:
1. **Quality threshold met:** All sub-questions answered at MEDIUM or higher confidence
2. **Max phases reached:** Phase 2 for Standard Brief, Phase 3 for Deep Dive
3. **Token budget exhausted:** Approaching tool call limit for the effort level
4. **Diminishing returns:** Phase 2 deepening found no new information beyond Phase 1

When stopping due to budget or diminishing returns, note this in the Methodology section: "Research terminated after Phase {N} due to {reason}. Remaining gaps documented in Knowledge Gaps section."

## Effort Budgets

| Depth | Phase 1 Agents | Phase 2 Agents | Phase 3 Agents | Total Tool Calls |
|---|---|---|---|---|
| Quick Lookup | 1-2 | 0 | 0 | ~5 |
| Standard Brief | 3-5 | 2-3 | 0 | ~30 |
| Deep Dive | 5-8 | 3-5 | 2-3 | 50+ |

## Checkpointing (Deep Dive Only)

For Deep Dive workflows that may exceed a single context window or session:

**When to checkpoint:**
- After Phase 1 completes (all Phase 1 findings collected)
- After Phase 2 completes (refined findings + multi-hop discoveries)
- Before Phase 3 synthesis (all raw data preserved)

**State file format:**
```
RESEARCH STATE — {timestamp}
Question: {original question}
Effort: Deep Dive
Phase completed: {1/2/3}

RESEARCH PLAN:
{decomposition blocks with dependency map}

COMPLETED BLOCKS:
{block_id}: {status: complete/weak/gap}
  Findings: {list of findings with sources}
  Gaps: {what wasn't found}

PENDING BLOCKS:
{blocks not yet executed}

MULTI-HOP DISCOVERIES:
{new blocks proposed by agents}

KEYWORD REFINEMENTS:
{anti-keywords added, keyword changes}
```

**Resume protocol:**
1. Read state file
2. Identify which phase was completed
3. Resume from the next phase
4. Do not re-run completed blocks unless specifically instructed
