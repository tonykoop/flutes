#!/usr/bin/env python3
"""Validate the public NAF workbook/comparison slice."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKBOOK_ROWS = REPO_ROOT / "design-table" / "public-naf-workbook-rows.csv"
COMPARISON_ROWS = REPO_ROOT / "analysis" / "naf-workbook-measured-log-comparison.csv"
FAMILY_SPEC = REPO_ROOT / "family-spec.csv"
NOTES = REPO_ROOT / "analysis" / "naf-workbook-measured-log-notes.md"

EXPECTED_KEYS = {"F4", "A4", "C5"}
EXPECTED_WORKBOOK_ROWS = {f"NAF-PUB-{key}" for key in EXPECTED_KEYS}
EXPECTED_COMPARISON_ROWS = {f"NAF-CMP-{key}" for key in EXPECTED_KEYS}
LOCAL_PATH_PATTERNS = (
    re.compile(r"file://", re.I),
    re.compile(r"(?<![A-Za-z])[A-Za-z]:[\\/]"),
    re.compile(r"/mnt/"),
    re.compile(r"/tmp/"),
    re.compile(r"/home/"),
    re.compile(r"/Users/"),
)
PRIVATE_HEADER_TOKENS = {
    "owner",
    "customer",
    "recipient",
    "price",
    "date",
    "private",
    "source_path",
    "archive_path",
    "row_number",
}


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def add_if(condition: bool, findings: list[str], message: str) -> None:
    if condition:
        findings.append(message)


def check_required_paths() -> list[str]:
    findings: list[str] = []
    for path in (WORKBOOK_ROWS, COMPARISON_ROWS, FAMILY_SPEC, NOTES):
        add_if(not path.exists(), findings, f"missing required artifact: {path.relative_to(REPO_ROOT)}")
    return findings


def check_no_local_paths(paths: list[Path]) -> list[str]:
    findings: list[str] = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for pattern in LOCAL_PATH_PATTERNS:
            for match in pattern.finditer(text):
                line_no = text.count("\n", 0, match.start()) + 1
                findings.append(f"{path.relative_to(REPO_ROOT)}:{line_no}: local path fragment {match.group(0)!r}")
    return findings


def check_headers_are_public(path: Path) -> list[str]:
    rows = read_rows(path)
    if not rows:
        return [f"{path.relative_to(REPO_ROOT)}: no data rows"]
    headers = set(rows[0])
    findings = []
    for header in headers:
        normalized = header.lower().replace("-", "_").replace(" ", "_")
        for token in PRIVATE_HEADER_TOKENS:
            if token in normalized:
                findings.append(f"{path.relative_to(REPO_ROOT)}: private/public-hostile header {header!r}")
    return findings


def check_workbook_rows() -> list[str]:
    rows = read_rows(WORKBOOK_ROWS)
    findings: list[str] = []
    row_ids = {row["row_id"] for row in rows}
    keys = {row["source_note"] for row in rows}
    add_if(row_ids != EXPECTED_WORKBOOK_ROWS, findings, f"workbook rows mismatch: {sorted(row_ids)}")
    add_if(keys != EXPECTED_KEYS, findings, f"workbook key set mismatch: {sorted(keys)}")
    for row in rows:
        add_if(row.get("authority") != "public_workbook_extract_unvalidated", findings, f"{row['row_id']}: authority must remain public_workbook_extract_unvalidated")
        add_if(row.get("source_workbook") != "design-table/flute-dimensions-parametric.xlsx", findings, f"{row['row_id']}: source_workbook must stay repo-relative")
        add_if(not row.get("hole_positions_from_foot_mm"), findings, f"{row['row_id']}: missing hole position list")
    return findings


def check_comparison_rows() -> list[str]:
    rows = read_rows(COMPARISON_ROWS)
    findings: list[str] = []
    comparison_ids = {row["comparison_id"] for row in rows}
    workbook_ids = {row["workbook_row_id"] for row in rows}
    keys = {row["key"] for row in rows}
    add_if(comparison_ids != EXPECTED_COMPARISON_ROWS, findings, f"comparison rows mismatch: {sorted(comparison_ids)}")
    add_if(workbook_ids != EXPECTED_WORKBOOK_ROWS, findings, f"comparison workbook links mismatch: {sorted(workbook_ids)}")
    add_if(keys != EXPECTED_KEYS, findings, f"comparison key set mismatch: {sorted(keys)}")
    for row in rows:
        add_if(row.get("authority") != "public_sanitized_build_log_aggregate", findings, f"{row['comparison_id']}: authority must remain public_sanitized_build_log_aggregate")
        add_if(not row.get("public_built_log_count"), findings, f"{row['comparison_id']}: missing public built-log count")
    return findings


def check_family_spec_links() -> list[str]:
    rows = read_rows(FAMILY_SPEC)
    findings: list[str] = []
    naf_rows = [row for row in rows if row["member_id"] in {f"NAF-6H-{key}" for key in EXPECTED_KEYS}]
    add_if(len(naf_rows) != 3, findings, f"expected 3 NAF family-spec rows, found {len(naf_rows)}")
    for row in naf_rows:
        member = row["member_id"]
        add_if(row.get("dimension_provenance") != "measurement_required", findings, f"{member}: dimension_provenance must remain measurement_required")
        add_if(row.get("source_artifact") != "design-table/public-naf-workbook-rows.csv", findings, f"{member}: source_artifact must point to public workbook rows")
    return findings


def run_checks() -> list[str]:
    findings = check_required_paths()
    if findings:
        return findings
    public_paths = [WORKBOOK_ROWS, COMPARISON_ROWS, FAMILY_SPEC, NOTES]
    findings.extend(check_no_local_paths(public_paths))
    findings.extend(check_headers_are_public(WORKBOOK_ROWS))
    findings.extend(check_headers_are_public(COMPARISON_ROWS))
    findings.extend(check_workbook_rows())
    findings.extend(check_comparison_rows())
    findings.extend(check_family_spec_links())
    notes = NOTES.read_text(encoding="utf-8")
    add_if("does not promote the packet to" not in notes, findings, "notes must preserve non-promotion wording")
    return findings


def main() -> int:
    findings = run_checks()
    if findings:
        print("public NAF comparison check failed:", file=sys.stderr)
        for finding in findings:
            print(f"  - {finding}", file=sys.stderr)
        return 1
    print("public NAF comparison check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
