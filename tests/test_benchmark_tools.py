from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate_benchmark import validate_repository, validate_run_record  # noqa: E402


class BenchmarkValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = json.loads((ROOT / "benchmark/manifest.json").read_text(encoding="utf-8"))
        self.scoring = json.loads((ROOT / self.manifest["scoring"]).read_text(encoding="utf-8"))
        registry = json.loads((ROOT / self.manifest["candidates"]).read_text(encoding="utf-8"))
        self.candidates = {candidate["id"]: candidate for candidate in registry["candidates"]}
        self.cases = {}
        for relative in self.manifest["cases"]:
            case_path = ROOT / relative
            case = json.loads(case_path.read_text(encoding="utf-8"))
            ground_truth = json.loads((case_path.parent / case["ground_truth_file"]).read_text(encoding="utf-8"))
            case["_finding_ids"] = {finding["id"] for finding in ground_truth["findings"]}
            self.cases[case["id"]] = case
        self.weights = {dimension["id"]: dimension["weight"] for dimension in self.scoring["dimensions"]}

    def test_repository_is_valid(self) -> None:
        self.assertEqual(validate_repository(ROOT), [])

    def test_complete_run_requires_correct_score_total(self) -> None:
        run = {
            "run_id": "case-01-legacy-monolith--baseline--2026-09-16--r01",
            "status": "complete",
            "outcome": "pass",
            "case_id": "case-01-legacy-monolith",
            "case_version": 1,
            "candidate_id": "baseline-repository-skill",
            "candidate_skill_blob": self.candidates["baseline-repository-skill"]["skill_blob"],
            "model": {"id": "test-model"},
            "environment": {"execution_mode": "test", "write_access": False, "tools": []},
            "raw_output_path": "README.md",
            "evidence": [{"finding_id": "LM-001", "path": "fixture/src/orders.js", "anchor": "function createOrder", "classification": "fact"}],
            "verification": {"executed": ["validator"], "unavailable": []},
            "scores": {**{key: 0 for key in self.weights}, "total": 1},
            "hard_fail": {"triggered": False, "reasons": []},
        }
        errors = validate_run_record(ROOT, run, "test-run", self.cases, self.candidates, self.weights, self.scoring["total"])
        self.assertTrue(any("scores.total" in error for error in errors))

    def test_hard_fail_requires_fail_outcome(self) -> None:
        run = {
            "run_id": "case-01-legacy-monolith--baseline--2026-09-16--r02",
            "status": "complete",
            "outcome": "pass",
            "case_id": "case-01-legacy-monolith",
            "case_version": 1,
            "candidate_id": "baseline-repository-skill",
            "candidate_skill_blob": self.candidates["baseline-repository-skill"]["skill_blob"],
            "model": {"id": "test-model"},
            "environment": {"execution_mode": "test", "write_access": False, "tools": []},
            "raw_output_path": "README.md",
            "evidence": [{"finding_id": "LM-001", "path": "fixture/src/orders.js", "anchor": "function createOrder", "classification": "fact"}],
            "verification": {"executed": ["validator"], "unavailable": []},
            "scores": {**{key: 0 for key in self.weights}, "total": 0},
            "hard_fail": {"triggered": True, "reasons": ["fabricated file"]},
        }
        errors = validate_run_record(ROOT, run, "test-run", self.cases, self.candidates, self.weights, self.scoring["total"])
        self.assertTrue(any("outcome must be fail" in error for error in errors))


if __name__ == "__main__":
    unittest.main()

