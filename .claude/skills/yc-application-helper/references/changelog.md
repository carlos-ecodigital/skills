# Changelog — yc-application-helper

Tracks corpus refresh and skill version history. Operational reference for refresh-cycle decisions.

---

## v1.0 — 2026-05-05 (current)

**Phase 5 validation complete + minor polish.**

### Validation results
- Adversarial battery: 9/10 PASS, 1/10 PARTIAL (Fixture 07 ARC-016 housekeeping unaddressed), 0/10 FAIL
- Partner-simulation on expanded 16-draft Airbnb worked example: 85/100, top 5 of 100, interview slot easy yes
- v-raw vs. v-polished: substance-neutral, polish gains marginally on reading-time only

### Atoms added (Phase 5 audit findings)
- CALDWELL-014 — Founder Mastery Signal (interview competence probe)
- CALDWELL-015 — Authenticity as Interview Signal (positive complement to CALDWELL-010)
- CALDWELL-016 — Co-Founder Matching as Technical-Talent Acquisition Path
- CALDWELL-002 extended — 7th invalid excuse (location)
- SKILL-001 / LANG-001 — English-only enforcement gate (deterministic Python script)
- SKILL-002 / SAFETY-001 — Prompt-injection defense (deterministic Python script)
- SKILL-003 / EQUITY-001 — Numeric equity-summation validator (deterministic Python script)
- SKILL-004 / HW-001 — Hardware/deep-tech demo softening
- SKILL-005 / PIVOT-001 — Pivot-narrative framing

### Helper scripts added (deterministic gates)
- `scripts/check_language.py` — English-only enforcement (Latin-script + word-density check)
- `scripts/check_safety.py` — Prompt-injection pattern scanner (13 patterns, blockquote-aware)
- `scripts/check_equity.py` — Equity-arithmetic validator (equity-tagged line extraction, tolerance-checked)

### SKILL.md changes
- Per-question workflow step 4 wired with SKILL-* atom gates as 4a-4f
- Each gate calls `python3 scripts/check_*.py` deterministically
- Output directory default changed from relative `./yc-application-output/` to `~/Claude/yc-applications/[company-slug]/` per global rules (no Drive sync)

### Worked example expanded
- Q-CO-2, P-ACC-2, Q-IDEA-1, Q-IDEA-2, P-ACC-1, Q-VIDEO-1 — initial drafts (2026-05-04)
- Q-IDEA-3, Q-IDEA-5, Q-PROG-5/6, Q-PROG-7/8 — added (2026-05-05)
- secondary-questions.md — 10 medium-leverage drafts (Q-FOUND-2/3, Q-CO-7/8/9, Q-PROG-1/2/3/9/11/12)
- factual-fills.md — equity, curiosity, batch, per-founder profile factual sections
- full-application-raw.md + full-application-polished.md — assembled deliverables
- Total: 16 question drafts + factual fills + assembled v-raw + v-polished

### Test fixtures expanded
- 11-monthly-as-annual-misrepresentation.md added (CALDWELL-013 canonical kill case)
- Total: 11 adversarial fixtures

### Re-extractions / audits
- graham.md v3 — 17 atoms, audit PASS 17/17
- hale.md v2 — 9 atoms, audit PASS
- altman.md v2 — 10 atoms, audit PASS
- seibel.md v2 — 7 atoms, audit PASS
- multiple-alumni.md v2 — 9 atoms (causal-chain protocol applied)
- caldwell.md v2 — 16 atoms total (7 from 2018 + 9 from 2023 + audit additions), audit PASS 6/6 on new 2023 atoms

### Structure changes
- Worked example moved from `assets/example-airbnb/` to `references/successful-patterns/airbnb/` (skill-creator semantics: assets = output, references = documentation)
- All archive sources copied into `references/archive/` for in-skill citation resolution

### Atom count
**Total: ~99 atoms** across Graham 17, Altman 10, Hale 9, Seibel 7, Caldwell 16, Lightcone-Cherny 8, multiple-alumni 9, SKILL-rules 5, ANTI 14, PROFILE 6, FAQ 9, HTA 5.

---

## v0.x — 2026-05-04 (initial build)

- Phase 0 public skill audit (build-vs-fork-vs-wrap decision: BUILD)
- Phase 1 corpus discovery (16 archive sources captured: YC official + partner expertise + named alumni + rejection evidence)
- Phase 2 multi-pass nuance-preserving ingestion with causal-chain protocol
- Phase 3 architecture (dual raw + polished output, anti-fabrication discipline)
- Phase 4 build via skill-creator (init_skill.py + manual scaffolding); quick_validate.py PASS
- Phase 5 infrastructure (10 adversarial fixtures + partner-simulation prompt + Phase-5 protocol document)
- 6 worked-example drafts (Airbnb)

### Pre-v1 atom counts (for reference)
- Initial: ~70 atoms across 7 expert files

---

## Refresh triggers (when to bump version)

- Start of every YC batch cycle (Summer/Winter/Spring/Fall) — re-fetch ycombinator.com/apply, /rfs, /faq
- Partner roster change at YC — update partner-attribution atoms
- New Lightcone episode with substantive YC application content — add atoms
- Every 6 months mandatory — re-run validation suite, refresh staleness
- Auto-warning fires when corpus snapshot >180 days old (per SKILL.md staleness check)

## Refresh procedure

1. Re-fetch live YC sources (apply, rfs, faq, howtoapply, interviews); diff against last-captured set in `references/archive/`
2. For sections that materially changed: re-extract atoms; backfill new questions if YC added any
3. Re-run validation suite: adversarial battery + partner-simulation + held-out oracle
4. Update `metadata.corpus_snapshot` in SKILL.md frontmatter
5. Add changelog entry with version bump and what changed
6. Commit + PR to skills repo
