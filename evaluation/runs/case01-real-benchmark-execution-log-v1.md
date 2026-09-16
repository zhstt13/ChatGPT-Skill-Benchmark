# Case 01 Real Benchmark Execution Log v1

## Purpose

Track the first real execution attempt for Case 01 — Legacy Monolith.

## Execution Flow

```text
Input Lock
    ↓
Baseline Skill Execution
    ↓
AI Repository Engineer Execution
    ↓
Evidence Review
    ↓
Rubric Scoring
    ↓
Comparison Report
```

## Run Metadata

- Case: `case01-legacy-monolith`
- Status: **Complete — first scored run**
- Model: GPT-5.6 Sol
- Shared input: controlled synthetic Case 01 scenario + input specification
- Limitation: no concrete repository snapshot was supplied

## Baseline Result

- Status: Complete
- Raw output: `evaluation/runs/case01-baseline-raw-output-v1.md`
- Score: **77/100 — Good with gaps**

## AI Repository Engineer Result

- Status: Complete
- Raw output: `evaluation/runs/case01-ai-repository-engineer-raw-output-v1.md`
- Score: **92/100 — Strong**

## Evidence Collection

| Category | Status |
|---|---|
| Architecture Map | Complete |
| Dependency Analysis | Complete within synthetic-input limits |
| Risk Identification | Complete |
| Fact / Assumption Separation | Complete |
| Improvement Plan | Complete |
| Change-impact reasoning | Complete |
| Verification scope | Complete |

Evidence artifact:

- `evaluation/runs/case01-evidence-map-v1.md`

## Scoring

Scored using `rubrics/scoring-model.md`.

Scorecard:

- `evaluation/results/case01-legacy-monolith-scorecard-v1.md`

Comparison report:

- `evaluation/results/case01-comparison-report-v1.md`

## Conclusion

The first scored run is complete. Under the same sparse synthetic input, the AI Repository Engineer produced stronger evidence separation, architecture-pressure analysis, preservation controls, and evolution planning than the minimal baseline, while the baseline was more concise.

This result does not yet prove real-code dependency or boundary accuracy because Case 01 has no concrete repository fixture with known ground truth.
