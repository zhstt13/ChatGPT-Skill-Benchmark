# Create Workflow

Use when designing a new repository or reusable repository template.

## Procedure

1. **Define the minimum project contract** — product type, runtime, deployment target, team/agent usage, required integrations, testing expectations, and durable constraints. State assumptions instead of hiding them.
2. **Choose the smallest viable repository shape** — add deployable surfaces, packages, docs, skills, workflows, scripts, or config only when they have independent ownership.
3. **Assign canonical owners** — every durable concern should have one obvious home. Avoid mirrored rules and duplicated configuration.
4. **Design navigation and context loading** — make important paths discoverable to both humans and agents without forcing all documentation into startup context.
5. **Define validation** — identify the tests, lint/type checks, CI gates, or structural checks that protect important contracts.
6. **Create template artifacts** — folder tree, starter files, README, architecture notes, examples, and optional scripts only as needed by the requested template.
7. **Run a cold-start check** — verify that a new maintainer/agent can locate the entrypoints, understand where new work belongs, and identify how to validate changes.

## Template Quality Rules

- Prefer one canonical way to perform a common task.
- Do not prebuild speculative modules for future features.
- Keep generated scaffolding replaceable and clearly separated from durable project rules.
- Include upgrade paths for intentionally simplified choices.
- A template is incomplete if its important boundaries have no verification strategy.

## Output Shape

- Assumptions and constraints
- Proposed repository tree
- Ownership map
- Required starter files
- Validation strategy
- Extension points and non-goals
