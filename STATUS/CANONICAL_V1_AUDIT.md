# Canonical v1 Repository Audit

## Scope

This audit inspected the repository state immediately before Canonical v1 was introduced (base commit `849c8f59563a1240df27ed2fd5d2ccdf6de06424`) and verifies the corrective work in:

- `1f3d3f530d4a262fa6ab6db998ed467f10ba4fac` — Canonical benchmark framework;
- `a90e53c98542e6697d396d1939877f96bf6c5e5a` — stricter run validation.

## Findings in the pre-v1 repository

| Finding | Impact | Resolution |
|---|---|---|
| 138 tracked files were 135 Markdown and 3 text files; there was no executable validator, test suite or CI workflow. | Results could not be reproduced or checked mechanically. | Added standard-library validator, score renderer, unit tests and GitHub Actions CI. |
| Case 01 was described as complete with `77/100` and `92/100`, while related status, result and evidence files still said `TBD`, `Prepared` or `Pending`. | The repository could imply validated results that did not have one canonical evidence trail. | Historical artifacts retained but explicitly marked non-canonical; Canonical runs now require raw output + valid JSON record. |
| Scoring used incompatible dimension sets and weights across README, protocol, schema and scorecards. | Scores from different documents were not comparable. | `benchmark/scoring.json` is the only scoring owner; the validator enforces exact dimensions, 100 total, outcome and hard-fail rules. |
| `Case 02` referred both to an AI-agent analysis case and a repository-template-design case. | Comparisons could use different tasks under the same identifier. | Replaced by stable, distinct IDs and task classes for three concrete cases. |
| Test corpus and ground truth were prose-only. | Architecture claims could not be falsified against real paths or code. | Added three inspectable fixtures with file-and-anchor-grounded findings. |
| Candidate identities used moving files without an immutable per-run fingerprint. | A later Skill edit could silently change the meaning of a past score. | Candidate registry pins Git blob SHA; validator verifies the file content and each Run Record's pinned blob. |
| External sources were labeled verified without pinned revisions. | Source reuse could drift as upstream default branches changed. | Added `research/SOURCE_LOCK.json` with verified public repository revisions and named path verification. |
| There was no canonical boundary between historical templates and current results. | Draft files could be mistaken for benchmark evidence. | `benchmark/manifest.json` defines the sole Canonical v1 input set; legacy `evaluation/` is excluded by design. |

## Verification performed

- `python tools/validate_benchmark.py` — PASS; 3 cases and 0 asserted Canonical runs.
- `python -m unittest discover -s tests -v` — PASS; 4 tests.
- GitHub Actions `Benchmark validation` on both Canonical v1 commits — SUCCESS.
- Remote branch head confirmed after each commit.

## Deliberately unresolved items

1. **No model-runtime result is fabricated.** The repository has no built-in mechanism to invoke an installed ChatGPT Skill runtime. A real result must be captured through that runtime and saved as a valid Run Record.
2. **No license was selected.** The public repository had no license; choosing one is a legal/policy decision and was intentionally not made automatically.
3. **Source locks are snapshots.** Refresh them deliberately when the synthesis work needs newer upstream material.

## Current conclusion

The repository is now a usable and repeatable benchmark framework, not merely a collection of templates. It is ready for fair candidate runs; it does not claim a winner until those runs are genuinely executed and recorded.

