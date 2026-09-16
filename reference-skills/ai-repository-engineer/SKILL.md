---
name: ai-repository-engineer
description: >
  Use when the task is to create, understand, audit, restructure, harden, or evolve a software/AI repository; design a reusable repository template; map architecture and dependencies; reduce repository drift; or coordinate repository-level rules and skills. Route the request to Create, Analyze, or Evolve based on the repository state and requested outcome.
---

# AI Repository Engineer

Repository-level engineering for AI-assisted projects. Optimize for evidence, clear ownership, minimal structure, preservation of existing behavior, and long-term maintainability.

## Modes

Choose by outcome, not by artifact name.

| Mode | Use when | Workflow |
|---|---|---|
| **Create** | A new repository/template is being designed or scaffolded | `workflows/create.md` |
| **Analyze** | An existing repository must be understood, mapped, audited, or documented | `workflows/analyze.md` |
| **Evolve** | An existing repository must be refactored, migrated, hardened, or reorganized | `workflows/evolve.md` |

Modes may compose. Typical sequences are `Analyze → Evolve` for existing repositories and `Create → Evolve` when a new template needs guardrails.

## Core Rules

1. **Evidence before architecture.** Never invent files, dependencies, conventions, readers, or constraints. Distinguish observed facts from proposed design.
2. **Current → Target.** Before mutation, state the proven current structure, the desired target, and the smallest safe path between them.
3. **Preserve behavior by default.** Structural improvement does not justify silent feature deletion or contract changes.
4. **One owner per concern.** Avoid duplicate rule owners, duplicate configuration, parallel canonical docs, and conflicting paths.
5. **Progressive structure.** Do not create a folder, module, manifest, workflow, or abstraction without an independent responsibility that justifies it.
6. **Rules are not workflows.** Durable constraints and task procedures should have separate ownership when both are large enough to deserve files.
7. **Prefer deletion and consolidation before abstraction.** A simpler repository is better only when required behavior, validation, security, and operability remain intact.
8. **Architecture needs enforcement.** Important boundaries should name the check, test, lint rule, CI gate, or review rule that can detect violations where practical.
9. **Context is routed.** Load only the repository evidence and reference material that can change the next decision.
10. **Proof claims are scoped.** A structural check does not prove runtime behavior; an unexecuted test is not a pass.

## Required Outputs

Produce only outputs relevant to the mode. Common artifacts:

- `REPOSITORY_MAP.md` — important surfaces, ownership, and navigation.
- `ARCHITECTURE.md` — boundaries, dependencies, data/control flow, constraints.
- `CHANGE_IMPACT.md` — affected surfaces, risks, preservation requirements, verification.
- `DECISIONS.md` or ADRs — only for durable architecture decisions that need a record.
- Template tree/config/docs — in Create mode when requested.

Do not generate every artifact by default.

## Completion Gate

Before calling repository work complete:

- verify changed paths and references exist;
- check for contradictory ownership or duplicated canonical rules;
- run available targeted validation/tests when mutation occurred;
- record what was actually verified and what remains unproven;
- confirm the result is no more complex than necessary.

## Benchmark Sources

This candidate synthesizes patterns from the verified source catalog in `../../research/SOURCE_CATALOG.md`, especially skill-based architecture, repository understanding, software architecture extraction, codebase boundary design, and skill/template authoring references.
