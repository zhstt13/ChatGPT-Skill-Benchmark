# Scoring Model

The benchmark uses a 100-point model. Each benchmark case may override weights, but deviations must be documented.

## Core Dimensions

| Dimension | Weight | What it measures |
|---|---:|---|
| Correctness & Evidence | 25 | Whether conclusions are grounded in the repository/task evidence and avoid invented facts. |
| Architecture Quality | 20 | Boundaries, dependency direction, separation of concerns, and structural coherence. |
| Context Management | 15 | Instruction hierarchy, source use, conflict handling, and context efficiency. |
| Maintainability | 15 | Ease of extension, clarity, modularity, and resistance to architecture drift. |
| Preservation & Change Safety | 10 | Whether existing behavior and constraints are preserved during proposed or applied changes. |
| Documentation & Explainability | 10 | Whether outputs make the system understandable to future agents and maintainers. |
| Efficiency | 5 | Avoiding needless files, duplicate rules, excessive context, and unnecessary complexity. |

**Total: 100**

## Score Bands

- **90–100 — Strong:** reliable enough to progress to harder benchmark cases.
- **75–89 — Good with gaps:** useful, but has identifiable weaknesses or missing evidence.
- **60–74 — Fragile:** partially useful, but likely to fail under repository growth or multi-skill composition.
- **Below 60 — Fail:** major correctness, architecture, preservation, or context-management problems.

## Hard-Fail Conditions

A run cannot receive a passing score if it does any of the following:

- invents repository files, dependencies, or constraints as facts;
- deletes or replaces important behavior without task justification;
- claims a validation/test passed when it was not actually performed;
- ignores explicit source precedence or project instructions;
- creates circular or contradictory instruction ownership without documenting it.

## Comparison Protocol

For each skill under test:

1. Run the same task and repository snapshot.
2. Record inputs, skill version/commit, model, and relevant environment constraints.
3. Score independently by dimension.
4. Preserve raw output and evidence references.
5. Compare specialist vs composite skills without assuming either design should win.

## Benchmark Principle

The goal is not to reward the largest or most complicated skill. The benchmark should reward the smallest architecture that reliably solves the task while remaining evidence-grounded, extensible, and safe to evolve.
