# Benchmark Run Schema

Every benchmark execution should record:

## Metadata

- Candidate Skill
- Benchmark Version
- Date
- Model / Environment

## Input

- Task definition
- Repository state
- Available references

## Evidence

- Observed files
- Commands or checks performed
- Verified outputs

## Score

| Category | Weight |
|---|---:|
| Evidence & Reasoning | 20 |
| Architecture Quality | 25 |
| Maintainability | 20 |
| Output Quality | 20 |
| System Integration | 15 |

## Final Report

- Strengths
- Weaknesses
- Failure modes
- Improvement suggestions
