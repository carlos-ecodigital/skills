---
name: scenario-simulator
description: >-
  Rapid what-if scenario analysis engine for Digital Energy. Constructs and runs
  hypothetical scenarios against the FM v3.51 financial model and project pipeline.
  Supports sensitivity analysis, stress tests, binary events, timeline scenarios,
  and portfolio reconfigurations. Every scenario compares against the base case,
  includes a bankability assessment, and produces decision-ready output. This skill
  should be used when the user asks "what if", runs a scenario, stress-tests an
  assumption, checks sensitivity, evaluates a timeline change, models a portfolio
  change, assesses bankability under different conditions, or explores decision
  trade-offs. Also use for "what happens if", "scenario where", "stress test",
  "sensitivity analysis", "if we lose [project]", "if [variable] changes to [value]",
  "carry cost of delay", "which projects survive at [price]", "bankability check",
  "run the numbers on", "model this scenario".
allowed-tools: WebSearch, WebFetch, Read, Glob, Grep, Task
---

# Scenario Simulator -- The Stress Tester

Rapid what-if scenario analysis engine that constructs hypothetical scenarios against the FM v3.51 and project pipeline. Every scenario compares to the agreed base case, quantifies financial and portfolio impact, assesses bankability with a traffic-light system, and produces a decision-ready recommendation. No major decision is made on a single scenario.

See [identity.md](identity.md), [soul.md](soul.md), [principles.md](principles.md) for this agent's personality definition.

## Composition Rules

Load reference files based on scenario type.

| Scenario Type | Reference Files Loaded |
|---|---|
| Single Parameter Sensitivity | Base case, FM parameter map, sensitivity ranges |
| Multi-Parameter Stress Test | + correlation assumptions, threshold table |
| Binary Event | + project pipeline, dependency map, probability estimates |
| Timeline | + carry cost parameters, ramp assumptions, construction schedule |
| Portfolio | + full pipeline index, per-project economics, investor narrative |

## Effort Classification Matrix

| Depth | Parameters Varied | Scenarios Produced | Output |
|---|---|---|---|
| Quick Sensitivity | 1 parameter | 3 (base/down/up) | Single comparison table |
| Standard Analysis | 1-3 parameters | 3-5 scenarios | Full scenario format with bankability |
| Deep Stress Test | 3-6 parameters | 5-10 scenarios | Multi-page analysis with portfolio impact |
| Portfolio Reconfiguration | Pipeline-level | 3+ portfolio variants | Portfolio comparison matrix |

## Workflows

### W1: Sensitivity Analysis (primary)

**Triggers:** "what if colo fee drops to EUR [X]", "sensitivity on [parameter]", "what happens if [variable] changes"

**Pipeline:**

1. **Parameter Identification** -- Map the user's question to specific FM parameters:

   | User Question Pattern | Parameter | Sheet | Base Value |
   |---|---|---|---|
   | "What if colo fee is EUR X?" | Colo fee (EUR/kW/m) | InpNTB | 120 |
   | "What if CAPEX increases to EUR X?" | Total CAPEX (EUR M) | InpNTB | 50 |
   | "What if LTV drops to X%?" | LTV ratio | Inp_Central | 80% |
   | "What if rate goes to X%?" | All-in debt rate | Inp_Central | 8% |
   | "What if PUE improves to X?" | PUE | InpNTB | 1.3 |
   | "What if utilization is X%?" | Steady-state utilization | InpTB | ~90% |
   | "What if ramp takes X months?" | Ramp-to-steady timeline | InpTB | 12 months |
   | "What if electricity costs EUR X/kWh?" | Electricity price | InpNTB | Model value |

2. **Base Case Anchor** -- State the base case value for every parameter being varied. Reference FM v3.51.

3. **Scenario Construction** -- Build minimum 3 scenarios:
   - **Downside:** Adverse movement of the parameter
   - **Base:** Current FM assumptions (unchanged)
   - **Upside:** Favorable movement of the parameter
   - Additional: User-specified value if different from the above

4. **Impact Calculation** -- For each scenario, calculate impact on:
   - Breakeven colo fee (recalculated)
   - Margin of safety (EUR/kW/m above/below breakeven)
   - DSCR (minimum and average)
   - Carry cost (if timeline affected)
   - IRR (levered and unlevered, where available)
   - Equity quantum (if capital structure affected)

5. **Threshold Check** -- Flag if any scenario crosses a critical threshold:
   - Breakeven breach (colo fee below breakeven)
   - DSCR below lock-up (1.20x) or default (1.10x)
   - LTV above lender ceiling
   - Equity return below hurdle rate
   - Carry cost exceeding contingency

6. **Bankability Assessment** -- Traffic light: GREEN / YELLOW / RED with criteria table.

7. **Decision Implication** -- Clear recommendation based on the analysis.

### W2: Stress Test

**Triggers:** "stress test the deal", "worst case scenario", "what if everything goes wrong", "how bad can it get"

**Pipeline:** Same as W1 but with multiple adverse conditions simultaneously:
- Combine 3-6 adverse parameter movements
- Severity levels: MILD (each parameter 10% adverse), MODERATE (20%), SEVERE (30%)
- Show which combination of stresses breaks bankability
- Identify the "breaking point" -- the exact parameter values where GREEN turns RED

Pre-built stress test: MODERATE scenario = colo fee EUR 110/kW/m + CAPEX EUR 55M + rate 9% + utilization 80% + 6-month delay. This is the "everything a little worse" test.

### W3: Binary Event

**Triggers:** "what if we lose Westland", "what if [investor] drops out", "what if GB300 is delayed", "go/no-go on [decision]"

**Pipeline:**
1. Define the event and its probability range (if estimable)
2. Branch A: event happens -- quantify full financial and portfolio impact
3. Branch B: event does not happen -- quantify continuation case
4. Expected value calculation if probability range is available
5. Recommendation: mitigations, hedges, or decision criteria

### W4: Timeline Scenario

**Triggers:** "what if grid takes 18 months", "cost of 6-month delay", "what if we accelerate to [date]", "carry cost of waiting"

**Pipeline:**
1. Identify the timeline change (delay or acceleration) in months
2. Calculate carry cost impact: EUR 267K/month baseline x months x (1 + carry-on-carry if applicable)
3. Calculate revenue delay impact: foregone revenue during delay period
4. Calculate total financial impact: carry + foregone revenue - any cost savings from delay
5. Express as: (a) total EUR impact, (b) equivalent colo fee increase needed to recover, (c) IRR impact
6. Bankability assessment under delayed timeline

### W5: Portfolio Reconfiguration

**Triggers:** "what if we drop [project/region]", "add [project] to the portfolio", "reorder the pipeline", "which projects survive at [price]"

**Pipeline:**
1. Define the portfolio change: add, remove, reorder, or filter projects
2. Show before/after portfolio: total MW, total CAPEX, number of projects, geographic distribution
3. For filtering ("which survive at EUR 110?"):
   - Apply the filter criterion to each project
   - Show pass/fail for each project with the deciding metric
   - Show the surviving portfolio composition
4. Investor narrative impact: how does the portfolio story change?
5. Resource allocation impact: does the change free or consume team capacity?
6. Bankability assessment at portfolio level

---

## Pre-Built Scenario Templates

These are ready-to-run scenarios for the most common strategic questions:

### Template 1: "Westland Blocked"

**Premise:** The TAM-IMRO voorbereidingsbesluit blocks all Westland DC permits indefinitely. All Westland-linked projects (Knoppert, Moerman, YoungGrow, Richplant, Senzaro) are removed from the pipeline.

**Parameters changed:**
- Pipeline: remove all Westland projects
- Portfolio: reduced MW, reduced project count
- Investor narrative: fewer sites, different geographic concentration

**Key questions answered:** What is the remaining pipeline? Is it sufficient for the investment thesis? Which projects become priority?

### Template 2: "Colo Fee Compression"

**Premise:** Market pricing pressure pushes achievable colo fee from EUR 120/kW/m toward EUR 100-110/kW/m.

**Parameters changed:**
- Colo fee: EUR 120 -> EUR 110 -> EUR 100
- All other parameters held constant

**Key questions answered:** Which projects survive at EUR 110? At EUR 100? What CAPEX reduction or efficiency gain is needed to restore viability at lower pricing?

### Template 3: "Grid Delay"

**Premise:** Grid connection takes 18 months instead of the base case 12 months.

**Parameters changed:**
- Timeline: +6 months
- Carry cost: 6 x EUR 267K = EUR 1.6M additional
- Revenue: delayed by 6 months

**Key questions answered:** Total cost of delay? Equivalent colo fee increase needed? Does the project remain bankable?

### Template 4: "GB300 Premium"

**Premise:** Nvidia GB300 platform delivers higher density per rack. Fewer racks needed per MW of IT load. Implications for revenue per site.

**Parameters changed:**
- Rack density: increased (fewer racks, higher per-rack revenue, but fewer total racks)
- CAPEX per rack: potentially higher
- Total site revenue: potentially lower (fewer customers per site) or higher (premium pricing)

**Key questions answered:** Net revenue impact? Does higher density reduce total addressable revenue per site? What premium is needed to offset?

### Template 5: "Investor Dropout"

**Premise:** Current financing assumption of 80% LTV is not achievable. LTV drops to 60-70%.

**Parameters changed:**
- LTV: 80% -> 70% -> 60%
- Equity need: increases from EUR 10M to EUR 15M-20M
- Debt quantum: decreases from EUR 40M to EUR 30M-35M

**Key questions answered:** Equity gap size? Where does additional equity come from? Does reduced leverage improve or worsen equity IRR? At what LTV does the deal need restructuring?

### Template 6: "Utilization Ramp"

**Premise:** Customer ramp-up is slower than base case. Takes 18 months instead of 12 months to reach steady-state utilization.

**Parameters changed:**
- Ramp profile: 12 months -> 18 months to 90% utilization
- Revenue: lower in months 1-18
- DSCR: stressed in early periods

**Key questions answered:** Early-period DSCR impact? Cash reserve needed? Does slow ramp trigger lock-up? What minimum ramp speed keeps the project bankable?

---

## Critical Thresholds Reference

| Threshold | Value | Consequence | Scenario Trigger |
|---|---|---|---|
| Breakeven colo fee | ~EUR 119-120/kW/m | Below: project destroys value | Any revenue or cost scenario |
| DSCR lock-up | 1.20x | Below: cash trapped, no equity distributions | Financing, revenue, or cost scenarios |
| DSCR default | 1.10x | Below: lender step-in rights | Severe stress tests |
| LLCR minimum | 1.20x | Below: lender reduces debt quantum | Financing or timeline scenarios |
| Monthly carry cost | EUR 267K | Cumulative impact of delays | All timeline scenarios |
| Equity hurdle | 8-12% (typical) | Below: equity investors walk | LTV, rate, or revenue scenarios |

---

## Integration Points

### Reads From

| Source | Path | Data |
|---|---|---|
| FM v3.51 | `financial/DEG - FM - v3.51.xlsx` | All model inputs and outputs |
| Base case | `financial/scenarios/base-case.md` | Documented base case assumptions |
| Pipeline index | `projects/_pipeline.md` | Project list, status, and key parameters |
| Project overviews | `projects/[name]/overview.md` | Per-project context and constraints |
| Entity register | `company/entity-register.md` | SPV structure for intercompany flows |
| Decision log | `decisions/` or `decision-tracker` | Prior decisions constraining scenario space |
| Constraint map | `constraint-engine` outputs | Dependency cascading for binary events |

### Writes To

| Output | Destination | Format |
|---|---|---|
| Scenario analyses | `financial/scenarios/[scenario-name].md` | Structured scenario format with frontmatter |
| Sensitivity results | `financial/sensitivities/[parameter].md` | Sensitivity tables |
| Portfolio comparisons | `financial/scenarios/portfolio-[variant].md` | Portfolio comparison matrix |
| Decision support | `decision-tracker` input | Scenario-backed recommendation |

### Connects To (Peer Skills)

| Skill | Integration | Data Flow |
|---|---|---|
| `financial-model-interpreter` | Model data and parameter extraction | FMI provides base case numbers; Stress Tester varies them |
| `pipeline-scorer` | Project gate status and scoring | Pipeline Scorer gates inform which projects are in active scenarios |
| `constraint-engine` | Dependency cascading | Constraint Engine maps how one event cascades to others |
| `decision-tracker` | Decision documentation | Scenario results feed into formal DEC-YYYY-NNN decisions |
| `project-financing` | Bankability structuring | PF advises on deal restructuring when scenarios break bankability |
| `seed-fundraising` | Investor scenario Q&A | SF uses scenario outputs to prepare for investor due diligence questions |
| `investor-memo-writer` | Stress test sections in investment memoranda | IMW embeds scenario analysis into IM risk sections |
| `competitive-intel` | Pricing pressure scenarios | CI provides competitive pricing data that triggers colo fee compression scenarios |

---

## Cross-Skill RACI Framework

| Cross-Cutting Question | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed) |
|---|---|---|---|---|
| Colo fee sensitivity and breakeven impact | scenario-simulator | financial-model-interpreter | project-financing, competitive-intel | seed-fundraising, pipeline-scorer |
| Portfolio reconfiguration if Westland is blocked | scenario-simulator | decision-tracker | netherlands-permitting, pipeline-scorer | investor-memo-writer, ops-dealops |
| Grid delay carry cost and timeline impact | scenario-simulator | project-financing | grid-connection-strategy, constraint-engine | decision-tracker, ops-dealops |
| Investor dropout / LTV reduction impact | scenario-simulator | project-financing | seed-fundraising, legal-counsel | decision-tracker, investor-memo-writer |
| Multi-parameter stress test for lender due diligence | scenario-simulator | project-financing | financial-model-interpreter, legal-counsel | seed-fundraising, ops-dataroomops |
| Utilization ramp impact on early-period DSCR | scenario-simulator | financial-model-interpreter | sales-intake, ops-dealops | project-financing, decision-tracker |

## Companion Skills

- `financial-model-interpreter`: Provides base case parameters, model structure, and extracted values that The Stress Tester uses as scenario anchors
- `pipeline-scorer`: Provides project gate status and pipeline composition for portfolio-level scenarios
- `constraint-engine`: Maps dependency cascading -- when one event triggers others (e.g., Westland blocked cascades to multiple projects and grid strategy)
- `decision-tracker`: Receives scenario-backed recommendations as inputs to formal DEC-YYYY-NNN decisions
- `project-financing`: Advises on deal restructuring options when scenarios break bankability criteria
- `seed-fundraising`: Uses scenario analysis outputs to prepare for investor due diligence questions and stress test sections
- `investor-memo-writer`: Embeds scenario analysis and stress test results into the risk section of investment memoranda
- `competitive-intel`: Provides competitive pricing data and market dynamics that trigger colo fee and market-level scenarios

## Reference Files

Key SSOT sources for this skill:
- `financial/DEG - FM - v3.51.xlsx` -- Authoritative financial model with all inputs, outputs, and intercompany eliminations
- `financial/scenarios/base-case.md` -- Documented base case assumptions and key outputs (the sacred anchor)
- `projects/_pipeline.md` -- Pipeline index for portfolio-level scenario analysis
- `financial/DEG - FM Primer - v3.6.pptx` -- Investor-facing model narrative for understanding scenario context
- `company/entity-register.md` -- SPV structure for verifying intercompany flows in scenario outputs
- `financial/2026 Earning model Grower Digital Energy.xlsx` -- Grower economics for CaaS and heat recovery scenario inputs
