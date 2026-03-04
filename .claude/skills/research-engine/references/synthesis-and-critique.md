# Synthesis & Critique

> How findings from multiple agents merge into a coherent brief, and how that brief gets stress-tested.
> Loaded for Standard Brief and Deep Dive workflows.

## Merge Protocol

After all search and deepening agents return, the orchestrator synthesizes findings through 5 sequential steps.

### Step 1: Deduplication

Multiple agents frequently find the same fact from different sources.

**Rules:**
- Two findings report the same fact if they convey the same specific claim (same metric, same entity, same conclusion)
- Keep the best-sourced version as primary citation (highest tier, most recent, most specific with methodology)
- Move other versions to "supporting citations" — they count toward the Corroboration factor
- If one version has exact numbers and another has a range, keep the exact version
- If versions disagree on the specific number while reporting the same metric, treat as a conflict (Step 2)

### Step 2: Contradiction Resolution

Apply the rules from `credibility-framework.md` Conflict Resolution section:

1. **Cross-tier conflict:** Tier 1 wins unless Tier 2 is significantly more recent AND field is fast-moving
2. **Same-tier conflict:** Present both claims. Hypothesize why they differ (methodology, timing, scope, sample)
3. **High-stakes trigger check:** Does this contradiction affect a Key Finding? Is evidence balanced? Would resolution change the recommendation? If ALL true, trigger adversarial debate (see Debate Protocol below)

**Output for each contradiction:**
```
CONTRADICTION:
- Claim A: [claim] — Source: [name] (Tier [N], [date])
- Claim B: [claim] — Source: [name] (Tier [N], [date])
- Resolution: [Tier 1 prevails / Both presented / Debate triggered]
- Note: [hypothesis for the discrepancy]
```

### Step 3: Evidence Weighting

Calculate the composite confidence score for each finding using the formula from `credibility-framework.md`:

```
Confidence = Tier_Weight x Recency x Geo_Relevance x Corroboration x Specificity
```

For corroboration: count deduplicated supporting citations from Step 1. Use the Corroboration Factor table:
- 3+ independent sources agree: 1.2 (bonus)
- 2 independent sources agree: 1.0
- Single source only: 0.7
- Sources conflict on this point: 0.5 (flag for resolution)

### Step 4: Confidence Labeling

Map each finding's composite score to a label:

| Score | Label |
|---|---|
| >= 0.7 | **HIGH** |
| 0.4 – 0.69 | **MEDIUM** |
| 0.2 – 0.39 | **LOW** |
| < 0.2 | **PRELIMINARY** |

**Calibration check (anti-overconfidence):** After labeling, review the distribution. Research shows agents are approximately 30% overconfident (arXiv 2602.06948). If >50% of findings are labeled HIGH, actively look for reasons to downgrade 1-2 of them. Ask: "What assumption would need to be wrong for this to be false?"

### Step 5: Knowledge Gap Identification

Compile all gaps from two sources:
- Agent-reported gaps (what agents searched for but did not find)
- Coverage gaps (sub-questions from the decomposition that have no findings at all)

For each gap, note:
- What was searched for
- What searches were tried
- Why it might be unavailable (paywalled, not public, does not exist, wrong keywords)
- What would be needed to fill it (primary research, paid report, expert interview, FOIA request)

## Self-Critique Protocol

**Trigger:** Every Standard Brief and Deep Dive. Not for Quick Lookup.

**Framing:** "Find bugs" — not "confirm quality." The critique agent's job is to attack the brief.

**Critique checklist (7 items):**
1. **Unsourced claims:** Any statement in Key Findings not backed by the Evidence Table? Flag for removal or additional sourcing
2. **Confidence inflation:** Any label too high for the underlying evidence? Downgrade. A finding with 1 Tier 2 source from 2023 should not be HIGH.
3. **Logical gaps:** Findings that should be connected but are not? Note the missing connection
4. **Executive summary alignment:** Does the exec summary accurately reflect Key Findings, or does it editorialize? Fix
5. **Actionable next steps:** Are next steps specific and actionable, or vague ("research further")? Refine
6. **Missing perspectives:** Is the research one-sided? Did it only search for confirming evidence? Flag
7. **Knowledge gaps completeness:** Are all searched-but-not-found items captured? Add missing gaps

**Process:**
1. Dispatch Critique Agent with the assembled brief (see `agent-architecture.md` for prompt template)
2. Critique agent returns issues with severity ratings (Critical / Important / Minor)
3. If any Critical or Important issues: fix them in the brief
4. Max 1 refinement loop. If the critique finds issues, fix them, done. Do not re-critique. Diminishing returns.

## Adversarial Debate Protocol

**Trigger criteria (ALL must be true):**
1. Contradiction affects a Key Finding
2. Both claims from Tier 1-2 sources
3. Corroboration is similar (neither claim has decisive evidence advantage)
4. Resolution would change the brief's recommendation

**Process:**
1. Frame the contradiction clearly: Claim A vs Claim B
2. Dispatch Debate Agent (see `agent-architecture.md` for prompt template)
3. Debate agent runs advocate/advocate/judge protocol
4. Judge produces verdict: [A wins / B wins / Genuinely inconclusive]
5. Incorporate verdict into the brief:
   - If A or B wins: Lead with the winning claim, note the losing claim as a minority position
   - If inconclusive: Present both claims with equal weight, note the unresolved nature

**Anti-pattern:** Do NOT trigger debate for every conflict. Only high-stakes contradictions that meet ALL 4 criteria. Most conflicts resolve through simple tier/recency comparison.

## Citation Verification Protocol

**Trigger:** Every Standard Brief and Deep Dive. Runs after critique/revision.

**Process:**
1. Dispatch Citation Agent with the final brief and all raw source material (see `agent-architecture.md`)
2. Citation agent checks every factual claim against the source findings
3. Categories: OK / UNSOURCED / OVERSTATED / CHECK URL

**Handling results:**
- UNSOURCED: Remove the claim or mark as unverified
- OVERSTATED: Reword to match what the source actually says
- CHECK URL: Note the URL issue but keep the finding if the source is otherwise credible

**Why separate from synthesis:** The synthesis agent optimizes for coherence and narrative flow. The citation agent optimizes for accuracy and traceability. These are different goals and benefit from separation.

## DE Ecosystem Comparison (When Overlay Active)

After synthesis is complete and the brief is assembled, if a DE domain overlay is active:

1. Read the relevant `_shared/` reference files (identified in `de-domain-overlays.md`)
2. For each data point in the brief that has a counterpart in the ecosystem files:
   - Compare: which is more recent? Which has a better source?
   - Keep the best version in the brief
   - If the research found newer/better data: flag the ecosystem file entry as stale
3. Produce an "Ecosystem Data Updates" appendix:

```
ECOSYSTEM DATA UPDATES:
| Data Point | Ecosystem Value | Ecosystem Source | Research Value | Research Source | Recommendation |
|---|---|---|---|---|---|
| [metric] | [old value] | [old source] | [new value] | [new source] | Update / Keep / Review |
```

4. Updates to `_shared/` files require explicit user approval. The brief only recommends — it does not auto-update.

## Quality Chain Execution Order

Summary of the full Phase 3 sequence for quick reference:

```
1. Merge Protocol (Steps 1-5)
   Dedup → Contradictions → Weighting → Labeling → Gaps
2. Assemble brief (orchestrator)
3. Self-Critique (Critique Agent)
   → Fix Critical/Important issues (max 1 loop)
4. Adversarial Debate (if triggered by Step 2)
   → Incorporate verdict into brief
5. Citation Verification (Citation Agent)
   → Remove UNSOURCED, reword OVERSTATED
6. DE Ecosystem Comparison (if overlay active)
   → Produce updates appendix
7. Final brief ready for delivery
```

Each step depends on the previous one completing. No parallelism within Phase 3 — the quality chain is strictly sequential to prevent compounding errors.
