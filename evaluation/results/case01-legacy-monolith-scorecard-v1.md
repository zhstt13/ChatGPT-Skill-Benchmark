# Case 01 — Legacy Monolith Scorecard v1

## Benchmark

Repository Engineering Comparison — first scored run

## Candidates

- Baseline Repository Skill
- AI Repository Engineer

## Run conditions

- Same controlled Case 01 input
- Same model: GPT-5.6 Sol
- Same scoring model: `rubrics/scoring-model.md`
- No concrete repository snapshot was supplied; scores therefore measure behavior on the controlled synthetic case, not proven performance on a real codebase

## Evidence artifacts

- `evaluation/runs/case01-baseline-raw-output-v1.md`
- `evaluation/runs/case01-ai-repository-engineer-raw-output-v1.md`
- `evaluation/runs/case01-evidence-map-v1.md`

## Score

| Dimension | Weight | Baseline | AI Repository Engineer | Evidence summary |
|---|---:|---:|---:|---|
| Correctness & Evidence | 25 | 24 | 25 | Both avoid invented repo facts; AI candidate separates proof states more explicitly |
| Architecture Quality | 20 | 12 | 18 | Baseline gives a safe high-level map; AI candidate adds ownership, pressure ranking, target-state, boundaries, and impact reasoning |
| Context Management | 15 | 9 | 14 | Baseline lists unknowns; AI candidate explicitly scopes evidence, unknowns, hypotheses, and unavailable validation |
| Maintainability | 15 | 11 | 14 | Both recommend incremental change; AI candidate adds one-slice migration, canonical ownership, and hardening |
| Preservation & Change Safety | 10 | 8 | 9 | Both avoid rewrite-first advice; AI candidate explicitly preserves contracts and requires impact checks |
| Documentation & Explainability | 10 | 8 | 9 | Both are understandable; AI candidate is more traceable but more verbose |
| Efficiency | 5 | 5 | 3 | Baseline is much shorter; AI candidate carries additional process/detail cost on a sparse case |
| **Total** | **100** | **77** | **92** | |

## Score band

- **Baseline Repository Skill: 77/100 — Good with gaps**
- **AI Repository Engineer: 92/100 — Strong**

## Hard-fail review

No hard-fail condition was observed for either candidate:

- no fabricated repository files or dependency facts;
- no unsupported claim that tests or validation passed;
- no destructive change recommendation;
- no contradictory instruction ownership introduced.

## Observations

### Baseline Repository Skill

Strengths:

- concise and efficient;
- remains inside supplied evidence;
- identifies major unknowns;
- recommends incremental discovery, testing, dependency mapping, and refactoring.

Gaps:

- limited ownership analysis;
- no ranked architecture pressure;
- no explicit Current → Target model;
- weaker change-impact and verification framing.

### AI Repository Engineer

Strengths:

- explicit fact / hypothesis / unknown separation;
- evidence-bounded architecture map;
- clear Analyze → Evolve progression;
- ranked risks and conditional discovery requirements;
- target-state, migration, impact, and verification reasoning are separated;
- repository-wide rewrite is explicitly rejected without evidence.

Gaps:

- noticeably more verbose than necessary for the sparse synthetic case;
- several sections could be compressed while preserving the same rigor;
- real repository architecture accuracy remains untested until a concrete repository snapshot is used.

## Improvement actions

1. Keep the AI Repository Engineer evidence discipline and change-safety model.
2. Reduce output verbosity for low-evidence/small-scope cases.
3. Add a concrete repository fixture in a future benchmark revision so dependency and boundary accuracy can be tested against ground truth.
4. Re-run Case 01 on that fixture before treating this score as a repository-level performance result.
