#!/usr/bin/env python3
"""Validate one Canonical v1 Run Record and render its scorecard."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from validate_benchmark import ROOT, load_json, validate_repository, validate_run_record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_record", type=Path, help="path to a JSON Run Record")
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root")
    args = parser.parse_args()
    root = args.root.resolve()
    repository_errors = validate_repository(root)
    if repository_errors:
        print("Cannot score because the benchmark framework is invalid:", file=sys.stderr)
        for error in repository_errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    local_errors: list[str] = []
    run_path = args.run_record.resolve()
    run = load_json(run_path, local_errors)
    if not run:
        for error in local_errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    manifest = json.loads((root / "benchmark/manifest.json").read_text(encoding="utf-8"))
    scoring = json.loads((root / manifest["scoring"]).read_text(encoding="utf-8"))
    registry = json.loads((root / manifest["candidates"]).read_text(encoding="utf-8"))
    candidates = {candidate["id"]: candidate for candidate in registry["candidates"]}
    cases = {}
    for relative in manifest["cases"]:
        case = json.loads((root / relative).read_text(encoding="utf-8"))
        ground_truth = json.loads((root / Path(relative).parent / case["ground_truth_file"]).read_text(encoding="utf-8"))
        case["_finding_ids"] = {finding["id"] for finding in ground_truth["findings"]}
        cases[case["id"]] = case
    weights = {dimension["id"]: dimension["weight"] for dimension in scoring["dimensions"]}
    local_errors.extend(validate_run_record(root, run, str(run_path), cases, candidates, weights, scoring["total"], scoring["passing_score"]))
    if local_errors:
        print("Run Record is not valid:", file=sys.stderr)
        for error in local_errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    candidate = candidates[run["candidate_id"]]
    print(f"# {run['run_id']}")
    print()
    print(f"- Case: `{run['case_id']}` v{run['case_version']}")
    print(f"- Candidate: {candidate['label']} (`{run['candidate_id']}`)")
    print(f"- Model: {run['model']['id']}")
    print(f"- Status: {run['status']} / outcome: {run['outcome']}")
    print()
    print("| Dimension | Score | Weight |")
    print("|---|---:|---:|")
    for dimension in scoring["dimensions"]:
        dim_id = dimension["id"]
        print(f"| {dimension['label']} | {run['scores'][dim_id]} | {dimension['weight']} |")
    print(f"| **Total** | **{run['scores']['total']}** | **{scoring['total']}** |")
    if run["hard_fail"]["triggered"]:
        print()
        print("**Hard fail:** " + "; ".join(run["hard_fail"]["reasons"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
