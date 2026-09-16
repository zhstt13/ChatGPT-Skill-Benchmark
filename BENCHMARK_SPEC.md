# Canonical Benchmark Specification v1

## Scope

این Specification فقط قرارداد بنچمارک را تعریف می‌کند. این پروژه runtime مدل، ابزارهای اختصاصی یا اجرای خودکار Skillهای ChatGPT را شبیه‌سازی نمی‌کند.

## Canonical ownership

| Concern | Canonical owner |
|---|---|
| Case registry | `benchmark/manifest.json` |
| Scoring weights and hard-fail rules | `benchmark/scoring.json` |
| Candidate identity and pinned Skill blob | `benchmark/candidates.json` |
| Run-record contract | `benchmark/run.schema.json` |
| Case task, fixture and expected findings | `benchmark/cases/<case-id>/` |
| Machine validation | `tools/validate_benchmark.py` |
| Human-readable score rendering | `tools/score_run.py` |
| Project state | `STATUS/PROJECT_PROGRESS_V1.md` |

No other document can override these owners silently.

## Case contract

Every Case has:

- a stable `id` and integer `version`;
- one task statement in `case.json`;
- an inspectable `fixture/` rather than only a prose scenario;
- `ground_truth.json` with finding IDs, severities and exact file/anchor evidence;
- a stated candidate set;
- a task class (`analyze-evolve` or `create`) so unrelated tasks are not compared under one ID.

The fixture is intentionally small enough for inspection but concrete enough to falsify unsupported claims. Ground truth is a minimum evidence set, not permission to hallucinate additional facts.

## Run contract

A result is Canonical only if a JSON Run Record validates and its referenced raw output exists. A complete record includes:

- exact case and candidate IDs;
- candidate Skill blob/revision;
- model and environment constraints;
- raw output path;
- path-backed evidence with a classification (`fact`, `hypothesis`, or `recommendation`);
- executed versus unavailable checks;
- canonical dimension scores totaling 100;
- a hard-fail declaration.

`complete` means the record is internally complete. It does **not** mean the Candidate was generally proven superior; comparison requires equivalent runs for every candidate.

## Scoring

`benchmark/scoring.json` is the only source of score weights and the current passing threshold. A hard-fail prohibits a passing result even if a numeric total is high. Examples: inventing files/dependencies as facts, claiming unexecuted validation passed, ignoring explicit source precedence, or silently changing behavior.

The score renderer verifies arithmetic; it does not generate subjective scores. The evaluator must document the reason for each score in the raw output or a linked evidence artifact.

## Repeatability and drift

Candidate registry entries use the Skill file's Git blob SHA. When a Skill changes, add a new candidate revision or update the pinned blob deliberately; never overwrite the identity of a prior run. Repeated runs should receive distinct run IDs and preserve the same fixture revision.

## Legacy artifacts

The old Markdown-heavy evaluation layer is retained for history only. It contains templates, drafts and conflicting preliminary claims. It is outside the Canonical v1 input set and is never read by the validator.
