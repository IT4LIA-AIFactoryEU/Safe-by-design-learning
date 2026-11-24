#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Author: Simone Betteti
# This file is distributed under the MIT License; see LICENSE.

"""Apply the uniform IT4LIA header to project-owned Python source files."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPDX = "# SPDX-License-Identifier: MIT"
AUTHOR = "# Author: Simone Betteti"
DISCLAIMER = "# This file is distributed under the MIT License; see LICENSE."
HEADER = [SPDX, AUTHOR, DISCLAIMER]

EXCLUDED_PREFIXES = (
    "dataset_interfaces/baseline_interfaces/deep_dissipative_model/",
)
EXCLUDED_FILES = {
    "dataset_interfaces/baseline_interfaces/nanodrone_bb/models.py",
}


def is_project_source(path: Path) -> bool:
    relative = path.relative_to(ROOT).as_posix()
    return relative not in EXCLUDED_FILES and not relative.startswith(EXCLUDED_PREFIXES)


def insertion_index(lines: list[str]) -> int:
    index = 0
    if lines and lines[0].startswith("#!"):
        index = 1
    if index < len(lines) and "coding" in lines[index][:40]:
        index += 1
    return index


def apply_header(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()
    cleaned = [line for line in lines if line not in HEADER]
    index = insertion_index(cleaned)
    while index < len(cleaned) and cleaned[index] == "":
        cleaned.pop(index)
    updated = cleaned[:index] + HEADER + [""] + cleaned[index:]
    rendered = "\n".join(updated).rstrip() + "\n"
    if rendered == original:
        return False
    path.write_text(rendered, encoding="utf-8")
    return True


def main() -> int:
    changed = []
    for path in sorted(ROOT.rglob("*.py")):
        if is_project_source(path):
            if apply_header(path):
                changed.append(path.relative_to(ROOT).as_posix())
    print(f"IT4LIA headers updated: {len(changed)}")
    for relative in changed:
        print(relative)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
