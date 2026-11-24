#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Author: Simone Betteti
# This file is distributed under the MIT License; see LICENSE.

"""Fail-closed checks for repository-side IT4LIA policy requirements."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "IT4LIA_COMPLIANCE_CHECKLIST.md",
    "THIRD_PARTY_NOTICES.md",
    "VERSION",
    "CHANGELOG.md",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/ISSUE_TEMPLATE/question.yml",
    ".github/dependabot.yml",
)
EXCLUDED_PREFIXES = (
    "dataset_interfaces/baseline_interfaces/deep_dissipative_model/",
)
EXCLUDED_FILES = {
    "dataset_interfaces/baseline_interfaces/nanodrone_bb/models.py",
}
RAW_DATA_PATHS = (
    "datasets/CED/DATAUNIF.MAT",
    "datasets/Silverbox/SNLS80mV.csv",
    "datasets/Silverbox/SNLS80mV.mat",
    "datasets/Silverbox/Schroeder80mV.csv",
    "datasets/Silverbox/Schroeder80mV.mat",
    "datasets/nanodrone_S3/parameters/raw_data/data",
)


def sha256(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def project_python_files() -> list[Path]:
    files = []
    for path in ROOT.rglob("*.py"):
        relative = path.relative_to(ROOT).as_posix()
        if relative in EXCLUDED_FILES or relative.startswith(EXCLUDED_PREFIXES):
            continue
        files.append(path)
    return sorted(files)


def main() -> int:
    failures: list[str] = []

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            failures.append(f"missing required file: {relative}")

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(
        r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)"
        r"(?:-[0-9A-Za-z.-]+)?",
        version,
    ):
        failures.append(f"VERSION is not Semantic Versioning: {version}")

    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    if "MIT License" not in license_text or "IT4LIA AI Factory" not in license_text:
        failures.append("LICENSE lacks MIT or IT4LIA project text")

    for path in project_python_files():
        head = "\n".join(path.read_text(encoding="utf-8").splitlines()[:12])
        relative = path.relative_to(ROOT).as_posix()
        if "SPDX-License-Identifier: MIT" not in head:
            failures.append(f"missing MIT disclaimer: {relative}")
        if "Author: Simone Betteti" not in head:
            failures.append(f"missing author: {relative}")

    manifest_path = ROOT / "IT4LIA_README_SHA256.txt"
    expected_readmes = {}
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        expected, relative = line.split("  ", 1)
        expected_readmes[relative] = expected
    actual_readmes = {
        path.relative_to(ROOT).as_posix(): path
        for path in ROOT.rglob("*")
        if path.is_file() and path.name.lower().startswith("readme")
    }
    if set(actual_readmes) != set(expected_readmes):
        failures.append("README file set changed from the immutable manifest")
    for relative, expected in expected_readmes.items():
        path = ROOT / relative
        if not path.is_file() or sha256(path) != expected:
            failures.append(f"immutable README changed: {relative}")

    for relative in RAW_DATA_PATHS:
        if (ROOT / relative).exists():
            failures.append(f"download-only raw data is bundled: {relative}")

    manifest = ROOT / "datasets/EXTERNAL_DATA_MANIFEST.json"
    fetcher = ROOT / "datasets/fetch_external_datasets.py"
    if not manifest.is_file() or not fetcher.is_file():
        failures.append("external dataset manifest or fetcher is missing")

    if failures:
        print("IT4LIA repository checks: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"IT4LIA repository checks: PASS ({len(project_python_files())} project Python files)")
    print(f"Immutable README files verified: {len(expected_readmes)}")
    print("Organization-level settings and policy exceptions still require checklist review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
