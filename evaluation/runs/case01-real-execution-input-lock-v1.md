# Case 01 Real Execution Input Lock v1

## Purpose
Freeze the benchmark input before comparing candidates.

## Case
case01-legacy-monolith

## Rules
- Same input must be used for all candidates.
- Raw outputs must be preserved.
- No score is assigned before evidence capture.
- Facts, assumptions, and unknowns must be separated.

## Execution Order
1. Prepare repository snapshot.
2. Run Baseline Repository Skill.
3. Capture evidence.
4. Run AI Repository Engineer.
5. Capture evidence.
6. Evaluate with rubric.
7. Generate comparison report.
