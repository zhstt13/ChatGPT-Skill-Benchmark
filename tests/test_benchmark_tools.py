from __future__ import annotations

import json
import shutil
import sys
import tempfile
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
        self.passing_score = self.scoring["passing_score"]

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
            "raw_output_path": "benchmark/runs/case-01-legacy-monolith--baseline--2026-09-16--r01.md",
            "evidence": [{"finding_id": "LM-001", "path": "fixture/src/orders.js", "anchor": "function createOrder", "classification": "fact"}],
            "verification": {"executed": ["validator"], "unavailable": []},
            "scores": {**{key: 0 for key in self.weights}, "total": 1},
            "hard_fail": {"triggered": False, "reasons": []},
        }
        errors = validate_run_record(ROOT, run, "test-run", self.cases, self.candidates, self.weights, self.scoring["total"], self.passing_score)
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
            "raw_output_path": "benchmark/runs/case-01-legacy-monolith--baseline--2026-09-16--r02.md",
            "evidence": [{"finding_id": "LM-001", "path": "fixture/src/orders.js", "anchor": "function createOrder", "classification": "fact"}],
            "verification": {"executed": ["validator"], "unavailable": []},
            "scores": {**{key: 0 for key in self.weights}, "total": 0},
            "hard_fail": {"triggered": True, "reasons": ["fabricated file"]},
        }
        errors = validate_run_record(ROOT, run, "test-run", self.cases, self.candidates, self.weights, self.scoring["total"], self.passing_score)
        self.assertTrue(any("outcome must be fail" in error for error in errors))

    def test_complete_well_formed_run_is_accepted(self) -> None:
        run_id = "case-01-legacy-monolith--baseline--2026-09-16--r03"
        with tempfile.TemporaryDirectory() as temporary:
            work_root = Path(temporary) / "repo"
            shutil.copytree(ROOT, work_root, ignore=shutil.ignore_patterns("__pycache__"))
            raw_path = work_root / "benchmark/runs" / f"{run_id}.md"
            raw_path.write_text("# Raw output\n\nEvidence-backed analysis.\n", encoding="utf-8")
            run = {
                "run_id": run_id,
                "status": "complete",
                "outcome": "pass",
                "case_id": "case-01-legacy-monolith",
                "case_version": 1,
                "candidate_id": "baseline-repository-skill",
                "candidate_skill_blob": self.candidates["baseline-repository-skill"]["skill_blob"],
                "model": {"id": "test-model"},
                "environment": {"execution_mode": "test", "write_access": False, "tools": []},
                "raw_output_path": f"benchmark/runs/{run_id}.md",
                "evidence": [{"finding_id": "LM-001", "path": "fixture/src/orders.js", "anchor": "function createOrder", "classification": "fact"}],
                "verification": {"executed": ["validator"], "unavailable": []},
                "scores": {
                    "correctness_evidence": 20,
                    "architecture_quality": 15,
                    "context_management": 10,
                    "maintainability": 10,
                    "preservation_change_safety": 5,
                    "documentation_explainability": 5,
                    "efficiency": 5,
                    "total": 70
                },
                "hard_fail": {"triggered": False, "reasons": []},
            }
            copied_cases = {}
            for case_id, case in self.cases.items():
                copied_cases[case_id] = dict(case)
            self.assertEqual(
                validate_run_record(work_root, run, "test-run", copied_cases, self.candidates, self.weights, self.scoring["total"], self.passing_score),
                [],
            )


if __name__ == "__main__":
    unittest.main()
