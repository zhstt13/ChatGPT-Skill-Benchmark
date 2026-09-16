# Reference Skills

This directory contains benchmark candidates and synthesized reference implementations.

These skills are **not ground truth**. They exist to be tested against the same benchmark cases as external specialist skills.

## Current Candidate

### `ai-repository-engineer`

A composite repository-engineering skill with three routed modes:

- **Create** — repository/template design and scaffolding strategy.
- **Analyze** — evidence-grounded repository understanding and architecture mapping.
- **Evolve** — refactor, migration, hardening, change-impact, and architecture-drift control.

The candidate intentionally combines patterns from multiple verified external references. The benchmark must determine whether this orchestration actually performs better than narrower specialist skills.

## Planned Comparison Set

Future candidates may include:

- a narrow Repository Architect specialist;
- a Repository Template Builder specialist;
- a Repository Evolution Manager specialist;
- a Skill Composer / Skill Architecture specialist.

This allows tests of **specialist vs composite** architecture instead of only comparing unrelated third-party skills.

## Rule

Any synthesized candidate must link back to `research/SOURCE_CATALOG.md` and document which ideas were adopted, adapted, or intentionally rejected.
