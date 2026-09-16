# Case 01 Comparison Report v1

## Benchmark Case

Case 01 — Legacy Monolith Repository

## Candidates

- Baseline Repository Skill
- AI Repository Engineer

## Input Consistency

- Same controlled benchmark input
- Same model: GPT-5.6 Sol
- Same evaluation rubric
- Same constraint: no concrete repository snapshot was supplied

## Evidence Sources

- `evaluation/runs/case01-baseline-raw-output-v1.md`
- `evaluation/runs/case01-ai-repository-engineer-raw-output-v1.md`
- `evaluation/runs/case01-evidence-map-v1.md`
- `evaluation/results/case01-legacy-monolith-scorecard-v1.md`

## Results

### Baseline Repository Skill

**Score: 77/100 — Good with gaps**

The baseline remained concise and evidence-bounded. It correctly avoided fabricating repository paths or dependency directions, listed major unknowns, and proposed incremental discovery/refactoring steps. Its main weakness was depth: ownership, dependency pressure, target architecture, verification, and change-impact reasoning were only lightly developed.

### AI Repository Engineer

**Score: 92/100 — Strong**

The AI Repository Engineer produced a more systematic analysis. It explicitly separated facts, hypotheses, and unknowns; ranked architecture pressure; described a target state without inventing a folder structure; and connected migration steps to preservation, verification, and impact checks. Its principal cost was verbosity on a sparse synthetic input.

## Evidence Comparison

| Area | Baseline | AI Repository Engineer |
|---|---|---|
| Repository Understanding | Correct but high-level | Explicitly scoped, proof-aware, and bounded by unavailable evidence |
| Architecture Analysis | Conceptual map only | Current state + ownership gaps + architecture pressure + target-state model |
| Dependency Analysis | Recommends mapping dependencies | Separates known opacity from unknown direction and defines required next evidence |
| Risk Identification | General regression/maintenance risks | Ranked risks linked to evidence and discovery requirements |
| Improvement Plan | Incremental general plan | Analyze → rank → migrate one slice → harden proven boundaries |
| Change Safety | Tests before refactor | Explicit contract preservation, impact surface review, and no rewrite without evidence |
| Efficiency | Very concise | More rigorous but materially longer |

## Final Score

| Candidate | Score | Band |
|---|---:|---|
| Baseline Repository Skill | **77/100** | Good with gaps |
| AI Repository Engineer | **92/100** | Strong |

## Interpretation

This run supports a narrower conclusion than a real-repository benchmark: under the same sparse synthetic input, the composite AI Repository Engineer produced more explicit architecture, evidence, preservation, and evolution reasoning than the minimal baseline.

It does **not** yet prove that the AI Repository Engineer maps real dependencies or boundaries more accurately, because Case 01 currently lacks a concrete code fixture with known ground truth.

## Improvement Plan

1. Preserve the AI Repository Engineer's evidence discipline, ownership model, and Current → Target reasoning.
2. Add a concise-response path for low-information cases to reduce unnecessary output cost.
3. Upgrade Case 01 with a small concrete legacy-monolith fixture containing known dependency and boundary problems.
4. Re-run both candidates against the fixture and compare findings against ground truth.
5. Only after that run, treat Case 01 as a true repository-analysis accuracy benchmark rather than a controlled reasoning benchmark.

## Status

**Case 01 first scored run: COMPLETE**
