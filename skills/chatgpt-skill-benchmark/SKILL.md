---
name: chatgpt-skill-benchmark
description: Run, document, validate, or compare repository-engineering Skill candidates using the user's ChatGPT-Skill-Benchmark canonical cases. Use for requests to benchmark Skills, record a candidate run, score a run, or inspect the benchmark's current status. Do not use for ordinary repository engineering or Skill authoring.
---

# ChatGPT Skill Benchmark

Use the canonical project at https://github.com/zhstt13/ChatGPT-Skill-Benchmark as the source of truth. Read its current README.md and benchmark/manifest.json before operating; pin the commit SHA for a run. The installed skill is a workflow entry point, not a copy of the project's fixtures, validator, or scores. If the repository is unavailable, say so instead of inventing its current state.

## Select the task

- **Inspect/status:** Read STATUS/PROJECT_PROGRESS_V1.md, the canonical manifest, and actual run records. Keep the historical evaluation/ and benchmarks/ material separate from canonical results. Report only what the records substantiate.
- **Execute a candidate:** Read the manifest, its selected case.json, benchmark/candidates.json, and the candidate's pinned SKILL.md and workflow files. Give the candidate the identical task and unmodified fixture used for other candidates. Keep ground_truth.json out of the candidate's input; use it only afterward for evaluation. Record exact model, tools, execution mode, write access, case version, fixture revision, and candidate blob. Never simulate a model run or infer results from a template.
- **Evaluate or compare:** Read BENCHMARK_SPEC.md, benchmark/run.schema.json, benchmark/scoring.json, the ground truth, and each candidate's untouched raw output. Compare equivalent runs under the same case, model, permissions, and tools, identifying differences when conditions diverge. Classify assertions as facts, hypotheses, or recommendations; cite exact fixture paths and anchors. Explain every subjective score from observed evidence. Honor hard-fail rules; a numeric total alone cannot override them.

## Record and verify an actual run

1. Save raw output without edits as benchmark/runs/<run-id>.md and a corresponding JSON record based on benchmark/RUN_TEMPLATE.json. Use distinct IDs for repetitions; preserve previous records. Record only checks actually executed and name unavailable checks separately.
2. Validate the real repository checkout with `python tools/validate_benchmark.py` and `python -m unittest discover -s tests -v`. For a complete record, run `python tools/score_run.py benchmark/runs/<run-id>.json`. These commands validate the framework and score arithmetic; they do not execute or prove the candidate's behavior.
3. Put a summary under benchmark/results/ only after matching records validate and comparison conditions are disclosed. A draft, historical score, or untested candidate is never a canonical winner.

Use a writable local checkout or the connected GitHub tools when needed. Confirm changes before claiming they were saved. The project currently defines three repository-analysis cases; check the current manifest before claiming new cases, results, or capabilities.
