# Evaluation Protocol

This directory defines how benchmark runs are recorded and compared.

## Required Run Metadata

Every run should record:

- benchmark case and version/commit;
- skill name and skill source commit/version;
- model and relevant execution configuration;
- repository/task snapshot used as input;
- whether repository write access was available;
- tools/connectors available during the run;
- raw output or artifact references;
- validations/tests actually executed;
- score by rubric dimension;
- hard-fail conditions, if any;
- evaluator notes and unresolved uncertainty.

## Fair Comparison Rules

1. Use the same task and repository snapshot for compared skills.
2. Do not give one skill hidden context that another skill does not receive unless the experiment is explicitly testing context strategy.
3. Separate **task-result quality** from **skill-architecture quality**.
4. Record tool failures or unavailable capabilities rather than scoring them as successful actions.
5. Compare composite and specialist skills; do not assume larger skill bundles are better.

## Recommended Run Record

```yaml
run_id: <unique-id>
benchmark: <path-or-id>
benchmark_commit: <sha>
skill: <name>
skill_commit: <sha-or-version>
model: <model>
repository_snapshot: <sha-or-fixture-id>
write_access: true|false
tools: []
outputs: []
verification:
  executed: []
  unavailable: []
scores:
  correctness_evidence: 0
  architecture_quality: 0
  context_management: 0
  maintainability: 0
  preservation_change_safety: 0
  documentation_explainability: 0
  efficiency: 0
hard_fail: false
notes: ""
```

Use `rubrics/scoring-model.md` for the default 100-point weighting and hard-fail rules.
