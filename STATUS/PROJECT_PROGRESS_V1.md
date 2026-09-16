# ChatGPT Skill Benchmark — Canonical Status v1

## Current state: Framework ready; canonical results not yet recorded

The repository now has a reproducible benchmark framework for repository-engineering Skills:

- three uniquely identified benchmark cases;
- concrete, inspectable fixtures for each case;
- path-and-anchor-backed ground truth;
- a single 100-point scoring model;
- a candidate registry pinned to Skill file blobs;
- a JSON Run Record contract;
- a standard-library validator, score renderer and GitHub Actions validation workflow;
- source pins for the external references used in synthesis.

## What is deliberately not claimed

No Canonical v1 model run or winner is recorded yet. A real result must include the exact model/runtime, candidate revision, raw output, evidence map, executed checks and a valid Run Record. The repository does not have a built-in ChatGPT Skill runtime, so it must not pretend to have automatically executed one.

## Historical prototype material

Earlier Case 01/02/03 Markdown artifacts remain under `evaluation/` and `benchmarks/` for traceability. They are not canonical evidence because they mix templates, drafts, incompatible score models and incomplete execution metadata. In particular, the old `77/100` and `92/100` Case 01 figures are historical scenario-only comparisons, not v1 repository-analysis results.

## Next repeatable action

Run both registered candidates against the same fixture, save the untouched output plus a Run Record in `benchmark/runs/`, then validate and render the scorecard. Case 01 is the recommended first run because it exercises concrete architecture analysis and safe evolution; Case 02 and Case 03 then test agent-boundary and frontend-growth reasoning.

