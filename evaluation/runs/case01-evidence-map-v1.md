# Case 01 — Evidence Map v1

## Run scope

- Case: `case01-legacy-monolith`
- Candidates: `baseline-repository-skill` and `ai-repository-engineer`
- Shared input: Case 01 scenario + Case 01 input specification
- Model: GPT-5.6 Sol

## Input facts available to both candidates

The controlled benchmark input explicitly states:

1. The application is growing and legacy.
2. Responsibilities are mixed.
3. Some modules are large.
4. Documentation is weak.
5. Dependencies are hidden / unclear.
6. Architectural boundaries are unclear.

No concrete directory tree, files, dependency manifests, runtime entrypoints, tests, CI configuration, deployment topology, or commit history were supplied.

## Candidate A — Baseline Repository Skill

### Evidence mapping

| Finding | Evidence status | Notes |
|---|---|---|
| Mixed responsibilities | Supported | Explicit in benchmark input |
| Large modules | Supported | Explicit in benchmark input |
| Weak documentation | Supported | Explicit in benchmark input |
| Hidden dependencies | Supported | Explicit in benchmark input |
| Regression risk during refactor | Reasoned inference | Clearly framed as risk, not fact |
| Need repository inventory | Recommendation | Appropriate discovery step |
| Need dependency mapping | Recommendation | Directly addresses supplied problem |
| Need stronger tests before refactor | Recommendation | Safety-oriented; current test coverage remains unknown |

### Fact / assumption / unknown separation

- Facts were limited to the supplied scenario.
- Unknown repository structure and runtime surfaces were explicitly listed.
- No fabricated file paths, dependency directions, or module names were introduced.

### Main strengths

- Concise and evidence-bounded.
- Provides all five requested output categories at a basic level.
- Recommends incremental rather than repository-wide restructuring.

### Main gaps

- No explicit canonical ownership analysis.
- Dependency reasoning remains generic.
- Findings are not ranked by evidence/impact.
- No explicit Current → Target architecture transition.
- Verification status is only implicit.

## Candidate B — AI Repository Engineer

### Evidence mapping

| Finding | Evidence status | Notes |
|---|---|---|
| Mixed responsibilities | Supported | Explicit in benchmark input |
| Large modules | Supported | Explicit in benchmark input |
| Weak documentation | Supported | Explicit in benchmark input |
| Hidden dependency relationships | Supported | Explicit in benchmark input |
| Dependency direction unknown | Supported absence | Correctly refuses to infer direction |
| Circular dependency possibility | Hypothesis | Explicitly marked unproven |
| Canonical ownership unknown | Supported absence | Input contains no ownership evidence |
| Need discovery before mutation | Recommendation | Directly follows evidence-first rule |
| Need one-slice migration | Recommendation | Safe incremental evolution strategy |
| Need enforcement after proven boundary | Recommendation | Consistent with long-term drift resistance |

### Fact / assumption / unknown separation

- Proven facts are explicitly separated from unknowns and hypotheses.
- Repository paths, owners, packages, entrypoints, tests, and deployment surfaces are not invented.
- The output explicitly states that the architecture map is conceptual and evidence-bounded.

### Main strengths

- Explicit evidence standard and proof scoping.
- Clear Analyze → Evolve transition.
- Ranked architecture pressure.
- Current-state, target-state, migration, impact, and verification sections are all distinct.
- Recommendations are conditional on future repository evidence.

### Main gaps

- Output is materially longer than the baseline for a sparse synthetic input.
- Several sections overlap conceptually and could be compressed without losing rigor.
- Actual architecture quality cannot be proven against real code because the case does not include a concrete repository snapshot.

## Evidence conclusion

Neither candidate triggered a hard-fail condition. Both avoided inventing repository-specific facts. Candidate B exposed more explicit reasoning structure and preservation controls; Candidate A was more concise but less systematic.
