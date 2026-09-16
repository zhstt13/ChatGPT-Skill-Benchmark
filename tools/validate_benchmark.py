#!/usr/bin/env python3
"""Validate the Canonical v1 benchmark without third-party dependencies."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SHA1_RE = re.compile(r"^[0-9a-f]{40}$")
RUN_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{5,}$")


def load_json(path: Path, errors: list[str]) -> dict[str, Any] | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing JSON file: {path}")
        return None
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON in {path}: {exc.msg} at line {exc.lineno}")
        return None
    if not isinstance(data, dict):
        errors.append(f"JSON root must be an object: {path}")
        return None
    return data


def safe_path(root: Path, relative: Any, errors: list[str], label: str) -> Path | None:
    if not isinstance(relative, str) or not relative.strip():
        errors.append(f"{label} must be a non-empty relative path")
        return None
    candidate = (root / relative).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        errors.append(f"{label} escapes repository root: {relative}")
        return None
    return candidate


def require_strings(data: dict[str, Any], keys: list[str], errors: list[str], label: str) -> None:
    for key in keys:
        if not isinstance(data.get(key), str) or not data[key].strip():
            errors.append(f"{label}.{key} must be a non-empty string")


def git_blob_sha(path: Path) -> str:
    payload = path.read_bytes()
    return hashlib.sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def validate_scoring(root: Path, path: Path, errors: list[str]) -> tuple[dict[str, int], int, int]:
    data = load_json(path, errors)
    if not data:
        return {}, 0, 0
    dimensions = data.get("dimensions")
    total = data.get("total")
    if not isinstance(dimensions, list) or not dimensions:
        errors.append("scoring.dimensions must be a non-empty array")
        return {}, 0, 0
    if not isinstance(total, int) or total <= 0:
        errors.append("scoring.total must be a positive integer")
        return {}, 0, 0
    weights: dict[str, int] = {}
    for index, dimension in enumerate(dimensions):
        label = f"scoring.dimensions[{index}]"
        if not isinstance(dimension, dict):
            errors.append(f"{label} must be an object")
            continue
        dim_id = dimension.get("id")
        weight = dimension.get("weight")
        if not isinstance(dim_id, str) or not dim_id:
            errors.append(f"{label}.id must be a non-empty string")
            continue
        if dim_id in weights:
            errors.append(f"duplicate scoring dimension: {dim_id}")
        if not isinstance(weight, int) or weight <= 0:
            errors.append(f"{label}.weight must be a positive integer")
            continue
        weights[dim_id] = weight
    passing_score = data.get("passing_score")
    if not isinstance(passing_score, int) or not 1 <= passing_score <= total:
        errors.append("scoring.passing_score must be an integer from 1 to scoring.total")
        passing_score = total
    if weights and sum(weights.values()) != total:
        errors.append(f"scoring dimensions total {sum(weights.values())}, expected {total}")
    return weights, total, passing_score


def validate_run_schema(path: Path, errors: list[str]) -> None:
    data = load_json(path, errors)
    if not data:
        return
    required = data.get("required")
    properties = data.get("properties")
    expected = {
        "run_id", "status", "outcome", "case_id", "case_version", "candidate_id",
        "candidate_skill_blob", "model", "environment", "raw_output_path", "evidence",
        "verification", "scores", "hard_fail",
    }
    if not isinstance(required, list) or not expected.issubset(set(required)):
        errors.append("run schema must require every canonical Run Record field")
    if not isinstance(properties, dict) or not expected.issubset(set(properties)):
        errors.append("run schema must define every canonical Run Record field")


def validate_candidates(root: Path, path: Path, errors: list[str]) -> dict[str, dict[str, Any]]:
    data = load_json(path, errors)
    if not data:
        return {}
    rows = data.get("candidates")
    if not isinstance(rows, list) or not rows:
        errors.append("candidates.candidates must be a non-empty array")
        return {}
    candidates: dict[str, dict[str, Any]] = {}
    for index, candidate in enumerate(rows):
        label = f"candidates[{index}]"
        if not isinstance(candidate, dict):
            errors.append(f"{label} must be an object")
            continue
        require_strings(candidate, ["id", "label", "kind", "skill_path", "skill_blob"], errors, label)
        candidate_id = candidate.get("id")
        if not isinstance(candidate_id, str) or not candidate_id:
            continue
        if candidate_id in candidates:
            errors.append(f"duplicate candidate id: {candidate_id}")
            continue
        blob = candidate.get("skill_blob")
        if not isinstance(blob, str) or not SHA1_RE.fullmatch(blob):
            errors.append(f"{label}.skill_blob must be a 40-character Git blob SHA")
        skill_path = safe_path(root, candidate.get("skill_path"), errors, f"{label}.skill_path")
        if skill_path:
            if not skill_path.is_file():
                errors.append(f"{label}.skill_path does not exist: {candidate.get('skill_path')}")
            elif isinstance(blob, str) and SHA1_RE.fullmatch(blob) and git_blob_sha(skill_path) != blob:
                errors.append(f"{label}.skill_blob does not match current file content")
        workflows = candidate.get("workflow_paths", [])
        if not isinstance(workflows, list) or not all(isinstance(item, str) for item in workflows):
            errors.append(f"{label}.workflow_paths must be an array of strings when present")
        else:
            for workflow in workflows:
                workflow_path = safe_path(root, workflow, errors, f"{label}.workflow_paths")
                if workflow_path and not workflow_path.is_file():
                    errors.append(f"{label}.workflow path does not exist: {workflow}")
        task_classes = candidate.get("supported_task_classes")
        if not isinstance(task_classes, list) or not task_classes or not all(isinstance(item, str) for item in task_classes):
            errors.append(f"{label}.supported_task_classes must be a non-empty array of strings")
        candidates[candidate_id] = candidate
    return candidates


def validate_case(
    root: Path,
    case_path: Path,
    candidate_ids: set[str],
    errors: list[str],
) -> dict[str, Any] | None:
    case = load_json(case_path, errors)
    if not case:
        return None
    label = f"case {case_path.relative_to(root)}"
    require_strings(case, ["id", "title", "task_class", "fixture_root", "ground_truth_file", "task"], errors, label)
    case_id = case.get("id")
    if isinstance(case_id, str) and case_path.parent.name != case_id:
        errors.append(f"{label}.id must match its directory name")
    if not isinstance(case.get("version"), int) or case["version"] < 1:
        errors.append(f"{label}.version must be a positive integer")
    required_candidates = case.get("candidates")
    if not isinstance(required_candidates, list) or len(required_candidates) < 2:
        errors.append(f"{label}.candidates must name at least two candidates")
    else:
        for candidate_id in required_candidates:
            if candidate_id not in candidate_ids:
                errors.append(f"{label} references unregistered candidate: {candidate_id}")
    fixture_root = safe_path(case_path.parent, case.get("fixture_root"), errors, f"{label}.fixture_root")
    if fixture_root and not fixture_root.is_dir():
        errors.append(f"{label}.fixture_root does not exist: {case.get('fixture_root')}")
    ground_truth_path = safe_path(case_path.parent, case.get("ground_truth_file"), errors, f"{label}.ground_truth_file")
    if not ground_truth_path or not ground_truth_path.is_file():
        if ground_truth_path:
            errors.append(f"{label}.ground_truth_file does not exist: {case.get('ground_truth_file')}")
        return case
    ground_truth = load_json(ground_truth_path, errors)
    if not ground_truth:
        return case
    if ground_truth.get("case_id") != case.get("id"):
        errors.append(f"{label} and ground truth disagree on case_id")
    findings = ground_truth.get("findings")
    if not isinstance(findings, list) or not findings:
        errors.append(f"{label} ground truth must contain a non-empty findings array")
        return case
    seen_ids: set[str] = set()
    for index, finding in enumerate(findings):
        finding_label = f"{label}.ground_truth.findings[{index}]"
        if not isinstance(finding, dict):
            errors.append(f"{finding_label} must be an object")
            continue
        require_strings(finding, ["id", "severity", "claim"], errors, finding_label)
        finding_id = finding.get("id")
        if isinstance(finding_id, str):
            if finding_id in seen_ids:
                errors.append(f"{label} has duplicate finding id: {finding_id}")
            seen_ids.add(finding_id)
        evidence = finding.get("evidence")
        if not isinstance(evidence, list) or not evidence:
            errors.append(f"{finding_label}.evidence must be non-empty")
            continue
        for evidence_index, item in enumerate(evidence):
            evidence_label = f"{finding_label}.evidence[{evidence_index}]"
            if not isinstance(item, dict):
                errors.append(f"{evidence_label} must be an object")
                continue
            require_strings(item, ["path", "anchor"], errors, evidence_label)
            evidence_path = safe_path(case_path.parent, item.get("path"), errors, f"{evidence_label}.path")
            if evidence_path and evidence_path.is_file():
                text = evidence_path.read_text(encoding="utf-8")
                anchor = item.get("anchor")
                if isinstance(anchor, str) and anchor not in text:
                    errors.append(f"{evidence_label}.anchor not found in {item.get('path')}: {anchor!r}")
            elif evidence_path:
                errors.append(f"{evidence_label}.path does not exist: {item.get('path')}")
    minimum = ground_truth.get("minimum_expected_finding_ids")
    if not isinstance(minimum, list) or not minimum:
        errors.append(f"{label}.ground_truth.minimum_expected_finding_ids must be non-empty")
    elif not set(minimum).issubset(seen_ids):
        errors.append(f"{label}.ground_truth.minimum_expected_finding_ids contains unknown IDs")
    case["_finding_ids"] = seen_ids
    return case


def validate_run_record(
    root: Path,
    run: dict[str, Any],
    label: str,
    cases: dict[str, dict[str, Any]],
    candidates: dict[str, dict[str, Any]],
    weights: dict[str, int],
    total: int,
    passing_score: int,
) -> list[str]:
    errors: list[str] = []
    required = [
        "run_id", "status", "outcome", "case_id", "case_version", "candidate_id",
        "candidate_skill_blob", "model", "environment", "raw_output_path", "evidence",
        "verification", "scores", "hard_fail",
    ]
    for key in required:
        if key not in run:
            errors.append(f"{label} missing required field: {key}")
    run_id = run.get("run_id")
    if not isinstance(run_id, str) or not RUN_ID_RE.fullmatch(run_id):
        errors.append(f"{label}.run_id must be lowercase kebab-case and at least 6 characters")
    status = run.get("status")
    if status not in {"draft", "complete", "invalidated"}:
        errors.append(f"{label}.status must be draft, complete, or invalidated")
    if run.get("outcome") not in {"pass", "fail", "not-scored"}:
        errors.append(f"{label}.outcome must be pass, fail, or not-scored")
    case = cases.get(run.get("case_id"))
    if not case:
        errors.append(f"{label}.case_id is not registered")
    elif run.get("case_version") != case.get("version"):
        errors.append(f"{label}.case_version does not match registered case")
    candidate = candidates.get(run.get("candidate_id"))
    if not candidate:
        errors.append(f"{label}.candidate_id is not registered")
    elif run.get("candidate_skill_blob") != candidate.get("skill_blob"):
        errors.append(f"{label}.candidate_skill_blob does not match current registered candidate")
    if case and run.get("candidate_id") not in case.get("candidates", []):
        errors.append(f"{label}.candidate_id is not enabled for this case")
    if case and candidate and case.get("task_class") not in candidate.get("supported_task_classes", []):
        errors.append(f"{label}.candidate does not support the case task_class")
    model = run.get("model")
    if not isinstance(model, dict) or not isinstance(model.get("id"), str) or not model["id"].strip():
        errors.append(f"{label}.model.id must be a non-empty string")
    environment = run.get("environment")
    if not isinstance(environment, dict):
        errors.append(f"{label}.environment must be an object")
    else:
        if not isinstance(environment.get("execution_mode"), str) or not environment["execution_mode"].strip():
            errors.append(f"{label}.environment.execution_mode must be a non-empty string")
        if not isinstance(environment.get("write_access"), bool):
            errors.append(f"{label}.environment.write_access must be a boolean")
        if not isinstance(environment.get("tools"), list) or not all(isinstance(item, str) for item in environment["tools"]):
            errors.append(f"{label}.environment.tools must be an array of strings")
    raw_output = safe_path(root, run.get("raw_output_path"), errors, f"{label}.raw_output_path")
    expected_raw_path = root / "benchmark/runs" / f"{run.get('run_id', '')}.md"
    if raw_output and raw_output != expected_raw_path.resolve():
        errors.append(f"{label}.raw_output_path must be benchmark/runs/<run_id>.md")
    if raw_output and not raw_output.is_file():
        errors.append(f"{label}.raw_output_path does not exist")
    evidence = run.get("evidence")
    if not isinstance(evidence, list):
        errors.append(f"{label}.evidence must be an array")
    elif status == "complete" and not evidence:
        errors.append(f"{label}.evidence cannot be empty for a complete run")
    elif case:
        for index, item in enumerate(evidence):
            item_label = f"{label}.evidence[{index}]"
            if not isinstance(item, dict):
                errors.append(f"{item_label} must be an object")
                continue
            require_strings(item, ["finding_id", "path", "anchor", "classification"], errors, item_label)
            if item.get("finding_id") not in case.get("_finding_ids", set()):
                errors.append(f"{item_label}.finding_id is not in case ground truth")
            if item.get("classification") not in {"fact", "hypothesis", "recommendation"}:
                errors.append(f"{item_label}.classification must be fact, hypothesis, or recommendation")
            source = safe_path(root, f"benchmark/cases/{case['id']}/{item.get('path', '')}", errors, f"{item_label}.path")
            if source and source.is_file():
                if isinstance(item.get("anchor"), str) and item["anchor"] not in source.read_text(encoding="utf-8"):
                    errors.append(f"{item_label}.anchor is not present in fixture evidence")
            elif source:
                errors.append(f"{item_label}.path does not exist in fixture")
    verification = run.get("verification")
    if not isinstance(verification, dict) or not isinstance(verification.get("executed"), list) or not isinstance(verification.get("unavailable"), list):
        errors.append(f"{label}.verification must contain executed and unavailable arrays")
    scores = run.get("scores")
    if not isinstance(scores, dict):
        errors.append(f"{label}.scores must be an object")
    else:
        expected = set(weights)
        present = set(scores) - {"total"}
        if present != expected:
            errors.append(f"{label}.scores dimensions must exactly match canonical scoring dimensions")
        numeric_sum = 0
        for dimension, weight in weights.items():
            value = scores.get(dimension)
            if not isinstance(value, int) or isinstance(value, bool) or not 0 <= value <= weight:
                errors.append(f"{label}.scores.{dimension} must be an integer from 0 to {weight}")
            else:
                numeric_sum += value
        if scores.get("total") != numeric_sum:
            errors.append(f"{label}.scores.total must equal the sum of dimensions ({numeric_sum})")
        if isinstance(scores.get("total"), int) and not 0 <= scores["total"] <= total:
            errors.append(f"{label}.scores.total must be between 0 and {total}")
    hard_fail = run.get("hard_fail")
    if not isinstance(hard_fail, dict) or not isinstance(hard_fail.get("triggered"), bool) or not isinstance(hard_fail.get("reasons"), list):
        errors.append(f"{label}.hard_fail must contain boolean triggered and array reasons")
    elif hard_fail["triggered"] and run.get("outcome") != "fail":
        errors.append(f"{label}.outcome must be fail when hard_fail.triggered is true")
    elif not hard_fail["triggered"] and hard_fail["reasons"]:
        errors.append(f"{label}.hard_fail.reasons must be empty when hard_fail.triggered is false")
    if status == "complete" and run.get("outcome") == "not-scored":
        errors.append(f"{label}.complete runs must have pass or fail outcome")
    if isinstance(scores, dict) and isinstance(scores.get("total"), int) and isinstance(hard_fail, dict):
        if not hard_fail.get("triggered") and run.get("outcome") == "pass" and scores["total"] < passing_score:
            errors.append(f"{label}.pass outcome requires score at least {passing_score}")
        if not hard_fail.get("triggered") and run.get("outcome") == "fail" and scores["total"] >= passing_score:
            errors.append(f"{label}.fail outcome below hard-fail requires score below {passing_score}")
    return errors


def validate_source_lock(root: Path, errors: list[str]) -> None:
    path = root / "research/SOURCE_LOCK.json"
    data = load_json(path, errors)
    if not data:
        return
    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("SOURCE_LOCK.sources must be a non-empty array")
        return
    seen: set[str] = set()
    for index, source in enumerate(sources):
        label = f"SOURCE_LOCK.sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{label} must be an object")
            continue
        require_strings(source, ["id", "repository", "ref", "commit"], errors, label)
        if isinstance(source.get("id"), str):
            if source["id"] in seen:
                errors.append(f"duplicate source lock id: {source['id']}")
            seen.add(source["id"])
        if isinstance(source.get("commit"), str) and not SHA1_RE.fullmatch(source["commit"]):
            errors.append(f"{label}.commit must be a 40-character commit SHA")


def validate_repository(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    manifest_path = root / "benchmark/manifest.json"
    manifest = load_json(manifest_path, errors)
    if not manifest:
        return errors
    require_strings(manifest, ["id", "title", "scoring", "candidates", "run_schema"], errors, "manifest")
    scoring_path = safe_path(root, manifest.get("scoring"), errors, "manifest.scoring")
    candidate_path = safe_path(root, manifest.get("candidates"), errors, "manifest.candidates")
    schema_path = safe_path(root, manifest.get("run_schema"), errors, "manifest.run_schema")
    if schema_path and not schema_path.is_file():
        errors.append("manifest.run_schema does not exist")
    elif schema_path:
        validate_run_schema(schema_path, errors)
    weights, total, passing_score = validate_scoring(root, scoring_path, errors) if scoring_path else ({}, 0, 0)
    candidates = validate_candidates(root, candidate_path, errors) if candidate_path else {}
    entries = manifest.get("cases")
    if not isinstance(entries, list) or len(entries) < 3:
        errors.append("manifest.cases must contain at least three cases")
        entries = []
    cases: dict[str, dict[str, Any]] = {}
    seen_paths: set[str] = set()
    for value in entries:
        if value in seen_paths:
            errors.append(f"manifest.cases contains duplicate path: {value}")
            continue
        seen_paths.add(value)
        case_path = safe_path(root, value, errors, "manifest.cases entry")
        if not case_path or not case_path.is_file():
            if case_path:
                errors.append(f"manifest case path does not exist: {value}")
            continue
        case = validate_case(root, case_path, set(candidates), errors)
        if case and isinstance(case.get("id"), str):
            if case["id"] in cases:
                errors.append(f"manifest contains duplicate case id: {case['id']}")
            cases[case["id"]] = case
    runs_dir = root / "benchmark/runs"
    if not runs_dir.is_dir():
        errors.append("benchmark/runs directory is missing")
    else:
        for record_path in sorted(runs_dir.glob("*.json")):
            run = load_json(record_path, errors)
            if run:
                errors.extend(validate_run_record(root, run, str(record_path.relative_to(root)), cases, candidates, weights, total, passing_score))
    validate_source_lock(root, errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root (default: inferred from this script)")
    args = parser.parse_args()
    errors = validate_repository(args.root)
    if errors:
        print(f"FAIL: {len(errors)} validation error(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    manifest = json.loads((args.root / "benchmark/manifest.json").read_text(encoding="utf-8"))
    print(f"PASS: Canonical benchmark valid ({len(manifest['cases'])} cases; {len(list((args.root / 'benchmark/runs').glob('*.json')))} run records).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
