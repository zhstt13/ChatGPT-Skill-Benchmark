# Case 02 — Baseline Repository Skill — Raw Output v1

## Run Conditions

- Benchmark: Case 02 — Repository Template Engineering
- Candidate: Baseline Repository Skill
- Input: `benchmarks/datasets/repository-test-corpus-v1/case02-repository-template-engineering.md`
- Constraint: the scenario does not specify programming language, runtime, deployment platform, CI provider, or concrete integrations.

## Proposed Repository Tree

```text
/
├── README.md
├── src/
├── tests/
├── docs/
└── .github/
    └── workflows/
        └── ci.yml
```

If the repository is not hosted on GitHub, replace `.github/workflows/ci.yml` with the CI configuration used by the actual hosting platform.

## Ownership Model

- `src/` — application/source code.
- `tests/` — automated tests.
- `docs/` — project documentation that does not belong in the README.
- `README.md` — setup, repository purpose, and contributor entry point.
- CI configuration — automated quality checks.

Keep new modules near the code they own and avoid creating additional top-level directories until a real need appears.

## Documentation Strategy

Use the README as the first navigation surface. Put longer architecture or operating notes in `docs/`. Avoid copying the same guidance into multiple files.

## Validation and Quality Gates

Once the runtime is selected, CI should run the project's normal checks, such as:

1. dependency/setup verification;
2. linting or formatting checks;
3. automated tests;
4. build/type checks when the chosen stack supports them.

No validation command is claimed to have run because no concrete runtime or repository implementation was provided.

## Migration / Evolution Considerations

Start with the small structure above. If the project grows into independently owned packages or deployable services, split those areas only when the separation is justified by real ownership or build/runtime needs. Add AI skill files when the team has concrete reusable agent procedures to store.

## Assumptions / Unknowns

Unknown: language, runtime, deployment target, hosting provider, required integrations, test framework, and exact AI-agent runtime.

The proposed tree is therefore a generic starting point rather than a stack-specific scaffold.
