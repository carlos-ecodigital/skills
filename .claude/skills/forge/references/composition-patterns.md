# Composition Patterns

> The 6 skill archetypes and multi-agent selection framework.
> Source: Ecosystem analysis of 25+ production skills + Anthropic/LangChain/OpenAI research
> Last updated: 2026-02-19

## Part A: Six Skill Archetypes

### 1. Ops Orchestrator

**Examples:** `ops-chiefops`, `ops-storyops`, `ops-meetings`, `ops-dealops`

**Pattern:** Routes work to domain skills, tracks outcomes, coordinates across workstreams. Never does domain work itself.

**Structural blueprint:**
```
SKILL.md:
  - Core Principle (1 sentence: what this skill maximizes/minimizes)
  - What You Own (numbered list of responsibilities)
  - What You Do NOT Own (with skill references for each)
  - Templates (for each primary output type)
  - Intake Process (trigger → questions → action routing)
  - Integration With Other Skills (routing table)
  - MCP Integration (if applicable: which tools, what patterns)
  - Quality Bar (acceptance criteria for outputs)
  - Anti-Patterns to Avoid (3-5 bullets)

references/:
  - Coordination frameworks, checklists, standard operating procedures
  - NOT domain knowledge (that belongs in the domain skills)
```

**Key traits:**
- Routes to domain skills; never does the domain work itself
- Owns coordination, tracking, and quality assurance
- Templates for recurring outputs (briefs, reports, logs)
- MCP tool usage for live data retrieval (HubSpot, Calendar, etc.)

**Anthropic mapping:** Routing workflow pattern
**LangChain mapping:** Router architecture
**Exemplar:** `ops-chiefops` (score: 85)
**Template:** `templates/ops-orchestrator.md`

---

### 2. Domain Executor

**Examples:** `project-financing`, `seed-fundraising`, `content-engine`

**Pattern:** Deep expertise in a specific domain. Reference-heavy with 75%+ of intelligence in knowledge files. SKILL.md handles workflow orchestration and quality gates.

**Structural blueprint:**
```
SKILL.md:
  - Composition Rules (when to load which reference files)
  - Standard Workflows:
    - Intake → Analysis → Output
    - Advisory Workflow
    - Review Workflow
  - Reference File Loading (matrix or decision tree)
  - Cross-References (to other skills)
  - Quality Bar
  - Disclaimers / Limitations

references/:
  - Deep domain knowledge (standards, frameworks, data tables)
  - Decision frameworks (when to use A vs B)
  - Named sources (regulations, benchmarks, industry data)
  - Comparison matrices and scoring rubrics

examples/:
  - Sample outputs for each workflow
  - Worked examples showing intake → output
```

**Key traits:**
- Heavy reference files with practitioner-grade knowledge
- SKILL.md is lean (routing + QA), references are dense
- Multiple workflows for different user needs (generate, advise, review)
- Clear composition rules for which references to load per task

**Anthropic mapping:** Prompt Chaining workflow pattern
**LangChain mapping:** Skills pattern (40% efficiency gain on repeat requests)
**Exemplar:** `project-financing` (score: 91)
**Template:** `templates/domain-executor.md`

---

### 3. Matrix Composer

**Examples:** `legal-counsel`

**Pattern:** Combinatorial expertise across two or more axes (e.g., specialization × jurisdiction). Loads different reference subsets per task based on the intersection of axes.

**Structural blueprint:**
```
SKILL.md:
  - Composition Model (axis definitions + loading matrix)
  - Entry Points (how user requests map to axis selections)
  - General Principles (apply across all axis combinations)
  - Quality Gates (per output type)

core/:
  - Foundational files shared across ALL specializations
  - General principles, common templates, shared frameworks

specializations/{spec-name}/:
  - overview.md (scope, key concepts, common tasks)
  - {detail-topic}.md (deep knowledge for this specialization)

jurisdictions/{jurisdiction}/:
  - {topic}.md (jurisdiction-specific rules, regulations, standards)
```

**Key traits:**
- Two+ axes of expertise that combine in different ways per request
- Loading matrix: user request → identify axes → load relevant subset
- Shared core files + specialized files = context efficiency
- Scales well: adding a new specialization or jurisdiction adds a directory, not a rewrite

**When to use Matrix Composer vs Domain Executor:**
- If the skill has 3+ distinct sub-domains AND each sub-domain has its own knowledge base → Matrix Composer
- If the skill has deep expertise in one area with different workflows → Domain Executor
- Rule of thumb: if you'd need a 2D table to map "which knowledge to load" → Matrix Composer

**Anthropic mapping:** Routing + Prompt Chaining (classify axes, then chain)
**LangChain mapping:** Skills pattern with multi-dimensional routing
**Exemplar:** `legal-counsel` (score: 94) — 10 specializations × 4 jurisdictions
**Template:** Use Domain Executor template + add `core/`, `specializations/`, `jurisdictions/` directories

---

### 4. Passive Foundation

**Examples:** `de-brand-bible`

**Pattern:** Not directly invoked by users. Serves as an authoritative data source referenced by other skills. All files are references; no workflows.

**Structural blueprint:**
```
SKILL.md:
  - Purpose (what this file provides to other skills)
  - Contents Index (map of reference files with descriptions)
  - Usage by Other Skills (which skills reference this, and how)
  - Update Protocol (when and how to refresh data)

references/:
  - Authoritative data tables, standards, benchmarks
  - Persona definitions, proof points, positioning data
  - Any "single source of truth" data that multiple skills need
```

**Key traits:**
- Rarely invoked directly by users (description notes this)
- Referenced by 3+ other skills
- All content is reference data, not instructions
- Update protocol ensures data stays current
- Changes here cascade to all dependent skills

**Anthropic mapping:** Shared state / persistent memory
**Harrison Chase mapping:** File systems as memory — persistent shared state
**Exemplar:** `de-brand-bible` (score: 86)
**Template:** `templates/passive-reference.md`

---

### 5. Engineering Discipline

**Examples:** From `multi-agent-technical-drafting-system.md` blueprint (ED-1 ELEC, ED-2 MECH, etc.)

**Pattern:** Pure calculation/analysis agents for technical engineering domains. Standards-driven with calculation templates, failure mode libraries, and resource ladders.

**Structural blueprint:**
```
SKILL.md:
  - Mission (1 sentence)
  - Scope (bulleted list of what this discipline covers)
  - Non-Scope (with arrows to other disciplines/skills)
  - Standards & Methods (table: standard | scope | version)
  - Calculation Templates (for each common calculation type)
  - Failure Modes (what goes wrong and how to catch it)
  - Resource Ladder (accuracy grade → required level of detail)
  - Interface with Domain Agents (how domain agents delegate)

references/:
  - Standards tables with specific section references
  - Calculation worksheets and formulas
  - Material/equipment specifications
  - Code compliance checklists
  - Failure mode libraries with root causes
```

**Key traits:**
- Standards-referenced (named codes, regulation numbers, version dates)
- Calculation templates with formula documentation
- Failure mode awareness (what goes wrong in this discipline)
- Resource ladder (feasibility → preliminary → permit-grade accuracy)
- Composes with other engineering disciplines and domain agents

**Anthropic mapping:** Parallelization (sectioning) — independent subtasks
**Exemplar:** None yet (blueprint agents not yet converted)
**Template:** `templates/engineering-discipline.md`

---

### 6. Panel of Experts

**Examples:** `netherlands-permitting`, `dc-engineering`, `ai-infrastructure`, `energy-markets`

**Pattern:** Multiple specialist personas within one skill. Each "expert" has distinct knowledge and the skill routes to the right one based on the user's question.

**Structural blueprint:**
```
SKILL.md:
  - Panel roster (list of specialists with their domains)
  - Routing rules (how user requests map to specialists)
  - Collaboration rules (when multiple specialists should weigh in)
  - Shared principles (apply across all specialists)

references/:
  - Per-specialist knowledge files
  - Shared standards and regulations
  - Cross-specialist integration points
```

**Key traits:**
- Multiple specialist voices within one skill (6-17 specialists)
- Internal routing table maps questions to specialists
- Collaboration mode for cross-cutting questions
- Scales well: adding a specialist adds reference files, not a new skill

**When to use Panel of Experts vs multiple Domain Executors:**
- If specialists share context and frequently collaborate → Panel (one skill)
- If specialists are independent with no shared context → Separate Domain Executors
- Rule of thumb: if a user question would need 2+ specialists to answer → Panel

**Anthropic mapping:** Parallelization (voting) — multiple perspectives on same input
**Exemplar:** `netherlands-permitting` (17 specialists)
**Template:** Use Domain Executor template + add panel roster and routing rules

---

## Part B: Multi-Agent Selection Framework

When designing a NEW skill, use this framework to select the right composition pattern.

### Pattern Mapping

| If the skill needs... | Use pattern... | Anthropic name | LangChain name |
|----------------------|---------------|---------------|---------------|
| Fixed sequence of steps | Prompt Chaining | Prompt Chaining | — |
| Route input to different handlers | Routing | Routing | Router |
| Independent parallel subtasks | Sectioning | Parallelization | Subagents |
| Multiple perspectives on same input | Voting | Parallelization | — |
| Dynamic task decomposition | Orchestrator-Workers | Orchestrator-Workers | Manager |
| Iterative refinement with criteria | Evaluator-Optimizer | Evaluator-Optimizer | — |
| Sequential state handoff | Handoffs | — | Handoffs |
| Load specialized knowledge on-demand | Skills | — | Skills |

### Decision Tree

```
Is the task decomposition known in advance?
├── Yes
│   ├── Are the steps independent? → Parallelization (Sectioning)
│   └── Are the steps sequential? → Prompt Chaining
└── No
    ├── Does the task vary significantly per input?
    │   ├── Yes → Orchestrator-Workers (dynamic decomposition)
    │   └── No
    │       ├── Is there clear evaluation criteria?
    │       │   ├── Yes → Evaluator-Optimizer (iterative refinement)
    │       │   └── No → Routing (classify and dispatch)
    │       └── Do multiple perspectives add value?
    │           └── Yes → Voting (Panel of Experts pattern)
```

### Archetype Selection Shortcut

```
What does the skill primarily do?

1. Coordinate work across multiple skills → Ops Orchestrator
2. Produce outputs using deep domain knowledge → Domain Executor
3. Handle requests that span 2+ knowledge axes → Matrix Composer
4. Provide shared data for other skills → Passive Foundation
5. Perform engineering calculations to standards → Engineering Discipline
6. Answer questions from multiple specialist viewpoints → Panel of Experts
```

### When NOT to Create a New Skill

Before creating a new skill, run the simplicity gate:

1. **Can a reference file solve it?** If the new "skill" is just a data source, add a reference file to an existing skill or create a Passive Foundation skill.
2. **Can an existing skill be extended?** If the new skill overlaps 60%+ with an existing skill, extend the existing skill with new workflows or references.
3. **Is it genuinely distinct?** The new skill must have its own scope, non-scope, and trigger phrases that don't overlap with existing skills.
4. **Does it have enough substance?** A skill with <3 reference files and <2 workflows is probably too thin to be standalone.

### Complexity Budget

| Ecosystem Size | Governance Rule |
|---------------|----------------|
| 1-10 skills | Build freely; focus on quality over quantity |
| 11-20 skills | Every new skill needs a justification (what gap does it fill?) |
| 21-30 skills | New skills require audit of overlap with existing skills |
| 30+ skills | Merge before building. One-in-one-out policy. |

Current ecosystem: ~24 skills. **Every new skill needs an overlap audit.**
