# Benchmark Execution Package v1

## Purpose

Provide a consistent execution procedure for running Skill candidates against the repository engineering benchmark corpus.

## Execution Flow

1. Select Benchmark Case
2. Prepare identical input for all Skill candidates
3. Run candidate Skill
4. Capture raw output
5. Extract evidence
6. Apply rubric
7. Generate scorecard
8. Record improvement actions

## Required Inputs

- Benchmark Case ID
- Skill name and version
- Model configuration
- Input repository or scenario
- Execution timestamp

## Required Outputs

- Repository understanding summary
- Architecture analysis
- Evidence list
- Facts / Assumptions / Unknowns
- Risks
- Improvement plan
- Final notes

## Rules

- Do not score without evidence.
- Do not treat assumptions as facts.
- Analyze current state before proposing changes.
- Preserve existing behavior unless explicitly requested otherwise.
