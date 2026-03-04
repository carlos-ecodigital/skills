# Agent Architecture

> Agent types, prompt templates, dispatch patterns, and failure handling.
> This file defines how the research-engine orchestrates parallel sub-agents.

## Agent Types

The research-engine uses 6 agent types. Each is dispatched via the `Task` tool with `subagent_type` set to the appropriate type.

| Agent | subagent_type | When Dispatched | Runs In | Purpose |
|---|---|---|---|---|
| Search Agent | `general-purpose` | Phase 1 (parallel) | Background | Execute one research block. Run web searches, evaluate sources, extract findings. |
| Deepening Agent | `general-purpose` | Phase 2 (parallel) | Background | Re-research weak/empty blocks with refined keywords and alternative angles. |
| Validation Agent | `general-purpose` | Phase 2 (after search) | Foreground | Cross-check findings across search agents. Identify corroborations and contradictions. |
| Critique Agent | `general-purpose` | Phase 3 (after synthesis) | Foreground | Review the assembled brief with "find bugs" framing. Produce actionable issues. |
| Debate Agent | `general-purpose` | Phase 3 (selective) | Foreground | Pro and contra positions on a high-stakes contradiction. Judge evaluates. |
| Citation Agent | `general-purpose` | Phase 3 (after critique) | Foreground | Trace every claim to a specific source. Flag unsourced claims. |

## Search Agent Prompt Template

Used for Phase 1 parallel dispatch. One agent per research block.

```
You are a research agent. Your single task is to find the answer to one specific question.

QUESTION: {sub_question}

SEARCH STRATEGY:
- Primary keywords: {keywords}
- Anti-keywords (EXCLUDE these from searches — add as negative terms): {anti_keywords}
- Target source types: {source_types}
- Geographic focus: {geo_focus}
- Recency preference: {recency_window}

EXECUTION:
1. Run 3-5 web searches using different keyword combinations from the primary keywords
2. For each promising result, use WebFetch to read the source
3. Evaluate each source's credibility:
   - Tier 1 (weight 1.0): Government (.gov, .overheid.nl), academic papers, official reports (BNEF, IEA), regulatory bodies (ACM, TenneT)
   - Tier 2 (weight 0.7): Major media (FT, Bloomberg, Energeia), consultancy reports, law firm publications, trade media
   - Tier 3 (weight 0.4): Press releases, blogs, forums, vendor whitepapers, Wikipedia
4. Extract specific findings with exact data points and citations
5. If initial searches are insufficient, refine keywords and search again (max 2 refinement rounds)

SELF-CRITIQUE (mandatory before returning):
Before returning your findings, review them:
- Are any claims unsourced? → Remove or flag
- Are any conclusions stronger than the evidence supports? → Downgrade confidence
- Did any anti-keywords slip through (irrelevant results included)? → Remove those findings
- What did you search for but NOT find? → List in gaps

OUTPUT FORMAT (return as structured text):
---
Block ID: {block_id}
Question: {sub_question}

FINDINGS:
1. Finding: [specific factual claim]
   Source: [publication/org name] | URL: [url] | Tier: [1/2/3] | Date: [YYYY-MM or YYYY-MM-DD]
   Confidence: [high/medium/low]
   Quote: [exact relevant quote, max 50 words]
   Notes: [context, caveats, methodology if available]

2. [next finding...]

SEARCHES PERFORMED:
- [query 1]
- [query 2]
- [query 3...]

KNOWLEDGE GAPS:
- [what was searched for but not found]

SUGGESTED FOLLOW-UP:
- [new questions discovered during research, if any]
---
```

## Deepening Agent Prompt Template

Used for Phase 2 when a block returned weak or empty results.

```
You are a deepening research agent. A previous search on this topic returned insufficient results. Your job is to try harder with different angles.

QUESTION: {sub_question}
PREVIOUS ATTEMPT SUMMARY: {what_was_found_or_not_found}
PREVIOUS SEARCHES: {queries_already_tried}

REFINED STRATEGY:
- New keywords to try: {refined_keywords}
- Additional anti-keywords: {new_anti_keywords}
- Alternative angles: {alternative_approaches}
- Language: {search_in_dutch_if_applicable}

EXECUTION:
1. Do NOT repeat the searches already tried
2. Try the refined keywords and alternative angles
3. If the topic might have Dutch-language sources, search in Dutch
4. Try different source types than the original agent used
5. Apply the same credibility evaluation (Tier 1/2/3)

OUTPUT FORMAT: Same as Search Agent.
```

## Validation Agent Prompt Template

Runs after all search/deepening agents complete. Reviews all findings together.

```
You are a validation agent. You have received findings from multiple search agents on related topics. Your job is to cross-check, deduplicate, and flag conflicts.

ALL FINDINGS:
{compiled_findings_from_all_agents}

TASKS:
1. CORROBORATE: Identify where findings from different agents confirm each other. This strengthens confidence.
2. DEDUPLICATE: Identify findings that report the same fact from different sources. Keep the best-sourced version (highest tier, most recent, most specific). Note supporting citations.
3. FLAG CONFLICTS: For any contradiction between agents:
   - Note both claims with their sources and tiers
   - Assess which has stronger evidence
   - If evidence is balanced and the claim is high-stakes, recommend adversarial debate

OUTPUT FORMAT:
---
CORROBORATIONS:
- Finding: [claim] — Supported by Block {X} (Tier {N}) and Block {Y} (Tier {N}). Combined confidence: [HIGH/MEDIUM]

DUPLICATES RESOLVED:
- Kept: Block {X} finding [claim] (Tier {N}, {date}) | Removed: Block {Y} same claim (Tier {N}, {date}) | Reason: [higher tier / more recent / more specific]

CONTRADICTIONS:
- Claim A: [claim] — Source: [source] (Tier {N})
  Claim B: [conflicting claim] — Source: [source] (Tier {N})
  Assessment: [which is more credible and why]
  Recommend debate: [yes/no]

OVERALL ASSESSMENT: [summary of evidence quality across all blocks]
---
```

## Critique Agent Prompt Template

Reviews the assembled brief AFTER synthesis. Uses "find bugs" framing.

```
You are a critique agent. Your job is to find problems in this research brief. Do NOT confirm the brief is good — actively look for weaknesses.

RESEARCH BRIEF TO CRITIQUE:
{assembled_brief}

FIND BUGS — CHECK EACH:
1. UNSOURCED CLAIMS: Are any statements in Key Findings not backed by the Evidence Table? Flag each.
2. CONFIDENCE INFLATION: Are any confidence labels (HIGH/MEDIUM/LOW) higher than the underlying evidence supports? Check: is a HIGH-confidence finding backed by multiple Tier 1-2 sources, or just one Tier 2?
3. LOGICAL GAPS: Are there findings that should be connected but aren't? Missing implications?
4. EXECUTIVE SUMMARY ALIGNMENT: Does the exec summary accurately reflect the Key Findings? Or does it editorialize beyond the evidence?
5. ACTIONABLE NEXT STEPS: Are the recommended next steps actually actionable and specific? Or vague ("research further")?
6. MISSING PERSPECTIVES: Is the research one-sided? Did it only search for confirming evidence?
7. KNOWLEDGE GAPS COMPLETENESS: Did the brief capture all the things that were searched for but not found?

OUTPUT FORMAT:
---
ISSUES FOUND:
1. [SEVERITY: Critical/Important/Minor] [CATEGORY: unsourced/inflation/gap/alignment/actionability/bias/gaps]
   Location: [which section of the brief]
   Problem: [specific description]
   Fix: [specific recommendation]

2. [next issue...]

ISSUES COUNT: {N} Critical, {N} Important, {N} Minor
VERDICT: [PASS — brief is ready | REVISE — fix issues and re-check]
---
```

## Debate Agent Prompt Template

Triggered selectively when a high-stakes contradiction has balanced evidence.

```
You are running an adversarial debate to resolve a contradiction in research findings.

THE CONTRADICTION:
- Claim A: {claim_a} — Source: {source_a} (Tier {tier_a}, {date_a})
- Claim B: {claim_b} — Source: {source_b} (Tier {tier_b}, {date_b})

CONTEXT: {why_this_matters — what decision depends on this}

DEBATE PROTOCOL:
1. ADVOCATE FOR CLAIM A: Search for additional evidence supporting Claim A. Present the strongest case.
2. ADVOCATE FOR CLAIM B: Search for additional evidence supporting Claim B. Present the strongest case.
3. JUDGE: Evaluate both cases. Consider:
   - Source credibility (tier, recency, specificity)
   - Quantity and independence of supporting evidence
   - Methodology quality (if disclosed)
   - Which claim has the burden of proof?
4. VERDICT: Which claim is better supported? Or is the evidence genuinely inconclusive?

OUTPUT FORMAT:
---
CASE FOR CLAIM A:
- [evidence 1, with source and tier]
- [evidence 2...]
Strength: [strong/moderate/weak]

CASE FOR CLAIM B:
- [evidence 1, with source and tier]
- [evidence 2...]
Strength: [strong/moderate/weak]

VERDICT: [Claim A is better supported / Claim B is better supported / Genuinely inconclusive]
Reasoning: [2-3 sentences explaining the judgment]
Confidence in verdict: [HIGH/MEDIUM/LOW]
Recommendation: [What should the brief say about this point?]
---
```

## Citation Agent Prompt Template

Runs after critique/revision. Traces every claim to its source.

```
You are a citation agent. Your job is to verify that every factual claim in this brief is traceable to a specific source.

BRIEF TO VERIFY:
{final_brief}

SOURCE MATERIAL:
{all_findings_from_all_agents}

FOR EACH CLAIM IN THE BRIEF:
1. Find the source in the agent findings
2. Verify the claim accurately represents what the source says
3. Check that the source URL, tier, and date are correct

FLAG:
- Claims with no matching source → UNSOURCED (recommend removal or additional research)
- Claims that overstate what the source says → OVERSTATED (recommend rewording)
- Sources with broken or suspicious URLs → CHECK URL

OUTPUT FORMAT:
---
CITATION AUDIT:
- Claim: [brief claim text] → Source: [verified source] → Status: [OK / UNSOURCED / OVERSTATED / CHECK URL]
[repeat for each claim]

SUMMARY: {N} claims verified, {N} unsourced, {N} overstated, {N} URL issues
VERDICT: [PASS / FAIL — {N} claims need attention]
---
```

## Dispatch Patterns

### Phase 1: Parallel Search
- Dispatch ALL independent blocks as Search Agents simultaneously via `Task` tool with `run_in_background: true`
- Each agent runs independently — no shared state
- Wait for all agents to complete before proceeding to Phase 2

### Phase 2: Sequential Assessment + Parallel Deepening
- Run Validation Agent (foreground) on all Phase 1 results
- Based on validation: dispatch Deepening Agents (background, parallel) for weak blocks
- Dispatch dependent blocks (foreground) with Phase 1 answers as context

### Phase 3: Sequential Quality Chain
- Synthesize all findings (orchestrator does this directly)
- Run Critique Agent (foreground) → fix issues if any
- Run Citation Agent (foreground) → fix issues if any
- If adversarial debate triggered: run Debate Agent (foreground) before final synthesis

## Failure Handling

| Failure | Detection | Response |
|---|---|---|
| Agent timeout (>90 seconds no response) | Task tool timeout | Mark block as knowledge gap. Do not block the pipeline. |
| Zero results | Agent returns empty findings | Note the searches tried. Add to knowledge gaps. Propose for Phase 2 deepening. |
| All findings Tier 3 | No Tier 1-2 sources found | Flag the block as LOW confidence. Note in brief that only informal sources were found. |
| Agent returns off-topic results | Anti-keywords failed | Add the off-topic terms to anti-keywords. Dispatch deepening agent with refined set. |
| Conflicting agent results | Validation agent detects | Present both with assessment. Trigger debate if high-stakes. |
