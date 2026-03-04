# Template: Reference File

> Meta-template for writing high-quality reference files inside any skill.
> Use this when creating references/ files for new or upgraded skills.
> Version: v1

```markdown
# {Topic Title}

> Source: {Where this knowledge comes from — regulations, industry data, expert interviews, etc.}
> Last updated: {YYYY-MM-DD}
> Accuracy: {feasibility | preliminary | permit-grade}

## Overview

{2-3 sentences: what this file contains and when to load it.}

## Key Data

{The core knowledge. Use tables for structured data, lists for frameworks.}

| {Column 1} | {Column 2} | {Column 3} | {Column 4} |
|------------|------------|------------|------------|
| {Data} | {Data} | {Data} | {Data} |

## Decision Framework

{When to use approach A vs B. Decision trees, matrices, or conditional logic.}

| If... | Then... | Because... |
|-------|---------|-----------|
| {Condition 1} | {Approach A} | {Reasoning} |
| {Condition 2} | {Approach B} | {Reasoning} |

## Common Mistakes

{What practitioners get wrong. Specific, actionable warnings.}

1. **{Mistake 1}:** {What people do wrong} → {What to do instead}
2. **{Mistake 2}:** {What people do wrong} → {What to do instead}
3. **{Mistake 3}:** {What people do wrong} → {What to do instead}

## Cross-References

- Related reference files: `references/{related-file}.md`
- Related skills: `{skill-name}`
- External sources: {URLs, document names, standard references}
```

## Quality Checklist for Reference Files

Before shipping a reference file, verify:

- [ ] **Specific data:** Contains actual numbers, named sources, or concrete frameworks (not just concepts)
- [ ] **Structured format:** Tables and lists dominate over prose paragraphs
- [ ] **Decision-useful:** A reader can make better decisions after reading this file
- [ ] **Source attributed:** Origin of knowledge is noted (regulation, benchmark, analysis)
- [ ] **Date stamped:** "Last updated" date present for time-sensitive data
- [ ] **50-300 lines:** Under 50 lines = too thin; over 300 = should split
- [ ] **Cross-referenced:** Links to related files and skills
- [ ] **Common mistakes:** Includes at least 2-3 "what NOT to do" items

## Anti-Patterns in Reference Files

| Anti-Pattern | Example | Fix |
|-------------|---------|-----|
| Generic textbook content | "Project financing involves structuring..." | Add specific numbers, named standards, DE-specific data |
| Prose-heavy | Paragraphs of explanation without data | Convert to tables, lists, decision trees |
| No sources | "Industry benchmarks suggest..." | Name the benchmark, cite the standard |
| Stale data | Regulation references without version dates | Add "Last updated" and version numbers |
| Too broad | File covers entire domain surface area | Split into focused sub-files per topic |
