# Example: Blueprint Conversion (W2)

> Worked example of converting one agent from multi-agent-technical-drafting-system.md
> into a production-ready skill directory using forge's W2 workflow.
> This example shows the process, not the full output files.

## Context

The multi-agent-technical-drafting-system.md blueprint defines 27 agents including 6 Engineering Disciplines (ED-1 through ED-6). This example converts **ED-1 ELEC** (Electrical Power Distribution) into a production skill.

## Step 1: Read the Blueprint Agent Definition

From the blueprint, ED-1 ELEC covers:
- **Scope:** MV/LV distribution, switchgear, cable sizing, earthing, protection coordination, power quality, lightning protection
- **Standards:** NEN 1010, IEC 61439, IEC 60364, NEN-EN-IEC 62305
- **Non-scope:** Rack power/metering (ED-1B), control/BMS (ED-5), fire safety (ED-6)
- **Calculation templates:** Cable sizing, protection coordination, short-circuit analysis, earthing grid design
- **Failure modes:** Undersized cables, missing discrimination, inadequate earthing, power quality issues

## Step 2: Check Existing Skills

Registry check:
- `dc-engineering` exists (Panel of Experts, 15 specialists) — includes "MV/LV electrical power distribution" as one of its specialists
- **Overlap detected:** dc-engineering already covers ED-1 ELEC's scope as one of its 15 specialist areas

**Decision point:** Should we create a separate ED-1 ELEC skill, or extend dc-engineering?

### Analysis:
| Factor | Separate Skill | Extend dc-engineering |
|--------|---------------|----------------------|
| Scope depth | Can go deeper with dedicated references | Specialist already handles this |
| Context budget | ~3K tokens for dedicated SKILL.md | Already sharing 15-specialist context |
| Ecosystem count | +1 skill (26 total) | No change (25 total) |
| Simplicity (P1) | More complex | Simpler |
| Overlap | Creates redundancy with dc-engineering | No redundancy |

**Forge recommendation: Extend dc-engineering** rather than creating a new skill. Add deeper reference files for the electrical discipline within dc-engineering's existing structure.

## Step 3: Design the Extension (if extending)

Add to dc-engineering:
```
references/
  electrical/
    standards-reference.md      # NEN 1010, IEC 61439 with section references
    cable-sizing-worksheet.md   # Step-by-step cable sizing calculation
    protection-coordination.md  # Discrimination study methodology
    earthing-design.md          # Earthing grid calculations
    failure-modes.md            # Electrical-specific failure modes
```

Update dc-engineering SKILL.md:
- Add composition rules for when to load electrical references
- Add calculation templates section for electrical disciplines
- Update the panel roster to note deeper coverage

## Step 4: If Creating a Separate Skill (for illustration)

If the decision was to create a separate skill (e.g., if the blueprint agent's scope significantly exceeded dc-engineering's coverage):

### Directory Structure
```
.claude/skills/ed-elec/
├── SKILL.md
├── references/
│   ├── nen-1010-reference.md
│   ├── cable-sizing-worksheet.md
│   ├── protection-coordination.md
│   ├── earthing-design.md
│   ├── power-quality-standards.md
│   └── failure-modes.md
```

### SKILL.md (using engineering-discipline template)
```yaml
---
name: ed-elec
description: >-
  Electrical power distribution specialist for Digital Energy data center projects.
  Covers MV/LV distribution design, switchgear selection, cable sizing, earthing
  systems, protection coordination, power quality analysis, and lightning protection
  per NEN 1010, IEC 61439, and IEC 60364. This skill should be used when the user
  asks about electrical design, power distribution, cable sizing, transformer
  selection, switchgear, earthing, protection coordination, short-circuit analysis,
  or power quality. Also use for "MV/LV", "cable sizing", "protection study",
  "earthing grid", "NEN 1010", "IEC 61439", "discrimination", "short circuit".
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
  - WebSearch
  - Bash
---

# ED-1: ELEC -- Electrical Power Distribution

## Mission
Design safe, reliable, and code-compliant electrical power distribution systems for AI colocation facilities.

## Scope
- MV/LV power distribution architecture
- Transformer sizing and selection
- Switchgear specification (IEC 61439)
- Cable sizing and routing (NEN 1010)
- Earthing and bonding systems
- Protection coordination and discrimination
- Short-circuit analysis
- Power quality assessment
- Lightning protection (NEN-EN-IEC 62305)

## Non-Scope
| Topic | Handled By |
|-------|-----------|
| Rack power, metering, PDUs | `dc-engineering` (rack power specialist) |
| Control systems, BMS | `dc-engineering` (controls specialist) |
| Fire detection/suppression | `dc-engineering` (fire safety specialist) |
| Grid connection, TenneT | `netherlands-permitting`, `energy-markets` |
| Financial modeling | `project-financing` |

[... Standards, Calculations, Failure Modes per template ...]
```

### Self-Audit Score Estimate
| Category | Expected Score | Notes |
|----------|---------------|-------|
| Domain Depth | 8 | Strong standards references, calculation worksheets |
| Workflow Clarity | 7 | Calculation templates provide clear process |
| Integration Design | 7 | Clear non-scope with dc-engineering, permitting |
| Context Engineering | 8 | Focused scope, modular reference files |
| Tool Design Quality | 6 | Bash for calculations; no MCP needed |
| Eval Scaffolding | 7 | 4 scenarios: cable sizing, protection study, scope boundary, feasibility |
| Scope Boundaries | 8 | Clear non-scope table |
| Trigger Coverage | 8 | Good keyword coverage for electrical domain |
| Anti-Pattern Guards | 6 | Failure modes section covers key risks |
| Reference File Ratio | 8 | 6 reference files with substantive content |
| **Estimated Total** | **~76** | Grade B — ships |

## Step 5: Registry Update

```markdown
| `ed-elec` | Engineering Discipline | 76 | Active | — | dc-engineering, netherlands-permitting, project-financing |
```

Ecosystem count: 26 skills. Note: approaching governance threshold.

## Step 6: Forge Learning Entry

```markdown
## 2026-02-19 -- Built ed-elec (from blueprint conversion)

### What the user asked for
Convert ED-1 ELEC from multi-agent-technical-drafting-system.md

### What forge delivered
ed-elec skill, Engineering Discipline pattern, score 76, 7 files

### Pattern observations
- Blueprint agents often overlap with existing Panel of Experts skills
- When overlap is >60%, extending the existing skill is better than creating new
- Engineering Discipline template works well for standards-heavy domains
- Cable sizing worksheet format (step-by-step with formulas) is effective

### Registry impact
Ecosystem at 26 skills. If all 27 blueprint agents were converted as separate skills,
we'd hit 52 — far above the 30-skill governance limit. Must merge/consolidate.
```

## Key Takeaways for Blueprint Conversion

1. **Always check overlap first.** Blueprint agents were designed in isolation; the existing ecosystem may already cover their scope.
2. **Prefer extending over creating.** Adding reference files to an existing Panel of Experts skill is simpler and avoids ecosystem bloat.
3. **Use the engineering-discipline template** for agents with standards, calculations, and failure modes.
4. **Track governance implications.** Converting a full blueprint can push the ecosystem past governance limits. Plan for consolidation.
5. **Max 3 skills per session.** Quality over speed. Each skill must self-audit ≥75 before shipping.
