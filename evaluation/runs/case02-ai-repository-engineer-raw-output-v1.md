# Case 02 — AI Repository Engineer — Raw Output v1

## Mode

Create

## Proven Input

The team needs a reusable repository foundation for AI-assisted software projects that supports growth, collaboration, maintenance, and future skill integration.

The benchmark does **not** specify programming language, runtime, deployment target, CI provider, test framework, or concrete integrations. Those remain unknown and must not be invented.

## Minimum Project Contract

Before stack-specific scaffolding, the template should require these values to be chosen by the adopting project:

- product/runtime type;
- deployment target;
- package/dependency manager;
- test, lint, format, and type/build commands;
- CI provider;
- required external integrations;
- whether project-specific Agent Skills exist.

Until those are known, keep the base template stack-neutral.

## Proposed Repository Tree

```text
/
├── README.md
├── ARCHITECTURE.md
├── src/
├── tests/
└── docs/
    └── workflows/
```

Conditional surfaces, created only when evidence justifies them:

```text
.github/workflows/ci.yml     # only when GitHub Actions is the chosen CI provider
skills/                      # only when the first project-specific reusable Skill exists
scripts/                     # only when a repeated repository operation needs one canonical executable owner
packages/ or services/       # only when independent ownership/runtime boundaries actually emerge
DECISIONS.md or docs/adr/    # only when durable architecture decisions need historical records
```

Do not ship empty speculative directories merely because they may be useful later.

## Ownership Map

| Concern | Canonical owner | Rule |
|---|---|---|
| Project entry/navigation | `README.md` | Link outward; do not duplicate architecture or workflow detail. |
| Durable architecture boundaries | `ARCHITECTURE.md` | Own module/service boundaries and dependency direction. |
| Product/runtime code | `src/` | Code-specific rules live with the code/tooling that enforces them. |
| Verification | `tests/` + chosen tool config | Tests prove behavior; docs do not claim tests passed. |
| Task procedures | `docs/workflows/` | Procedures only; durable constraints stay with their canonical owner. |
| Agent Skills | `skills/<skill>/` when activated | Each Skill owns its reusable agent procedure and references repository rules instead of copying them. |
| CI | provider-specific config when selected | Executes canonical validation commands; does not redefine them. |

## Documentation Strategy

1. `README.md` is the cold-start entry point: purpose, setup pointer, important paths, validation pointer.
2. `ARCHITECTURE.md` stores durable repository boundaries and dependency rules.
3. `docs/workflows/` stores multi-step human/agent procedures only when those procedures are substantial enough to need a file.
4. Skill instructions live with each Skill and reference canonical repository rules instead of mirroring them.
5. ADRs are added only for decisions whose history matters; they are not a second architecture manual.

This creates one owner per concern and keeps startup context small.

## Validation and Quality Gates

Because the stack is unknown, exact commands cannot be specified yet. The adopting project must map canonical commands for:

- test;
- lint/format verification;
- type/build verification when applicable;
- dependency or lockfile integrity when applicable.

CI should call those same canonical commands rather than duplicate their logic.

Repository-level structural checks should be introduced only when drift appears or the rule is important enough to enforce mechanically. Useful checks may include:

- broken documentation links;
- duplicate canonical instruction files;
- forbidden dependency direction between established packages/services;
- Skill metadata/schema validation after Skills exist.

No check is reported as executed in this benchmark run because no concrete repository implementation exists.

## Evolution Path

### Stage 1 — Small project

Keep `src/`, `tests/`, README, architecture notes, and only the documentation actually needed.

### Stage 2 — Repeated workflows or Agent Skills appear

Add `docs/workflows/` content and `skills/` entries only for procedures that are genuinely reusable. Keep rules and workflows separate.

### Stage 3 — Independent runtime/ownership boundaries appear

Promote code into `packages/`, `apps/`, or `services/` only when there is evidence of separate ownership, deployment, dependency, or release needs. Record dependency direction in `ARCHITECTURE.md` and enforce important boundaries where practical.

### Stage 4 — Architecture history matters

Add ADR storage only after decisions become numerous or consequential enough that current-state documentation alone is insufficient.

## Extension Points

- stack-specific starter configuration;
- CI-provider adapter;
- project-specific Skills;
- independently owned packages/services;
- structural validation scripts.

Each extension requires a concrete owner and an observed need before it becomes part of the template.

## Non-Goals

The base template should not pre-create:

- speculative microservices;
- multiple overlapping architecture documents;
- a generic plugin framework without a real integration;
- empty Skill directories;
- duplicated CI and local validation logic;
- stack-specific config before the stack is chosen.

## Cold-Start Check

A new maintainer or agent should be able to answer from the root surfaces:

1. What is this project? → `README.md`
2. Where does product code belong? → `src/`
3. Where are durable boundaries defined? → `ARCHITECTURE.md`
4. How is behavior verified? → `tests/` and the selected canonical validation commands
5. Where does a reusable agent procedure go? → `skills/` only after the first real Skill exists
6. Where does a multi-step operating procedure go? → `docs/workflows/`

## Verification Status

Verified in this run: consistency of the proposed ownership model against the benchmark requirements and the Candidate Skill/Create workflow.

Not verified: runtime behavior, CI execution, build/test success, or concrete path existence in a generated repository, because this benchmark provides a design scenario rather than an implemented repository snapshot.
