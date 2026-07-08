#!/usr/bin/env python3
"""Validate skill conformance for repository, Claude, and OpenCode compatibility.

Checks:
- Valid YAML frontmatter
- name present, lowercase kebab-case, and <= 64 chars
- description present and <= 200 chars
- intent present and non-empty (top-level or under metadata)
- type present and one of: component, interactive, workflow (top-level or under metadata)
- folder name matches frontmatter name
- compatibility field accepted when present (opencode supported)
- metadata field accepted as optional nested map
- required sections exist in order:
  Purpose, Input, Key Concepts, Application, Examples, Common Pitfalls, References
- no $ARGUMENTS template syntax in the body (outside code formatting) — skills
  declare inputs in plain language via the Input section; see CONTRIBUTING.md
  "Why We Don't Use $ARGUMENTS"
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys
from dataclasses import dataclass

try:
    import yaml
except ImportError:  # pragma: no cover
    print("PyYAML is required. Install with: python3 -m pip install pyyaml", file=sys.stderr)
    raise


@dataclass
class Issue:
    path: str
    code: str
    detail: str


VALID_TYPES = {"component", "interactive", "workflow"}
REQUIRED_SECTIONS = [
    "Purpose",
    "Input",
    "Key Concepts",
    "Application",
    "Examples",
    "Common Pitfalls",
    "References",
]
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FORBIDDEN_TEMPLATE_PATTERN = re.compile(r"\$ARGUMENTS\b")


def check_forbidden_template_syntax(path: str, body: str) -> list[Issue]:
    # Mentions inside code formatting (e.g., the authoring skills naming the
    # anti-pattern as `$ARGUMENTS`) are allowed; bare usage is not.
    prose = re.sub(r"```.*?```", "", body, flags=re.S)
    prose = re.sub(r"`[^`\n]*`", "", prose)
    if FORBIDDEN_TEMPLATE_PATTERN.search(prose):
        return [
            Issue(
                path,
                "template_syntax_forbidden",
                "$ARGUMENTS does not expand outside Claude Code; declare inputs "
                'in the Input section instead (CONTRIBUTING.md, "Why We Don\'t '
                'Use $ARGUMENTS")',
            )
        ]
    return []


def split_frontmatter(text: str) -> tuple[dict | None, str]:
    if not text.startswith("---\n"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    data = yaml.safe_load(parts[1]) or {}
    body = parts[2]
    return data, body


def check_required_sections(path: str, body: str) -> list[Issue]:
    issues: list[Issue] = []
    headings = re.findall(r"^##\s+(.+?)\s*$", body, flags=re.MULTILINE)
    section_positions: dict[str, int] = {}

    for section in REQUIRED_SECTIONS:
        try:
            section_positions[section] = headings.index(section)
        except ValueError:
            issues.append(Issue(path, "section_missing", section))

    if len(section_positions) == len(REQUIRED_SECTIONS):
        positions = [section_positions[section] for section in REQUIRED_SECTIONS]
        if positions != sorted(positions):
            issues.append(
                Issue(
                    path,
                    "section_order_invalid",
                    "Expected order: " + " > ".join(REQUIRED_SECTIONS),
                )
            )

    return issues


def check_skill(path: str) -> list[Issue]:
    if not os.path.isfile(path):
        return [Issue(path, "file_missing", "Skill file not found")]

    if os.path.basename(path) != "SKILL.md":
        return [Issue(path, "file_name_invalid", "Skill file must be named SKILL.md")]

    with open(path, "r", encoding="utf-8") as handle:
        text = handle.read()

    issues: list[Issue] = []
    data, body = split_frontmatter(text)
    if data is None:
        issues.append(Issue(path, "frontmatter_missing", "Missing or malformed frontmatter"))
        return issues

    metadata = data.get("metadata") or {}

    name = str(data.get("name") or "").strip()
    description = str(data.get("description") or "").strip()
    intent = str(metadata.get("intent") or data.get("intent") or "").strip()
    skill_type = str(metadata.get("type") or data.get("type") or "").strip()

    if not name:
        issues.append(Issue(path, "name_missing", "Frontmatter name is required"))
    elif len(name) > 64:
        issues.append(Issue(path, "name_too_long", f"{len(name)} chars"))
    elif not NAME_PATTERN.fullmatch(name):
        issues.append(Issue(path, "name_invalid_format", "Expected lowercase kebab-case"))

    if not description:
        issues.append(Issue(path, "description_missing", "Frontmatter description is required"))
    elif len(description) > 200:
        issues.append(Issue(path, "description_too_long", f"{len(description)} chars"))

    if not intent:
        issues.append(Issue(path, "intent_missing", "Frontmatter intent is required"))

    if not skill_type:
        issues.append(Issue(path, "type_missing", "Frontmatter type is required"))
    elif skill_type not in VALID_TYPES:
        issues.append(Issue(path, "type_invalid", f"Expected one of: {', '.join(sorted(VALID_TYPES))}"))

    folder = os.path.basename(os.path.dirname(path))
    if name and folder != name:
        issues.append(Issue(path, "folder_name_mismatch", f"folder={folder} name={name}"))

    issues.extend(check_required_sections(path, body))
    issues.extend(check_forbidden_template_syntax(path, body))
    return issues


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate PM skill metadata and structure conformance."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Optional SKILL.md file paths. If omitted, validates skills/*/SKILL.md.",
    )
    return parser.parse_args(argv)


def resolve_skill_files(paths: list[str]) -> list[str]:
    if not paths:
        return sorted(glob.glob("skills/*/SKILL.md"))

    resolved: list[str] = []
    for raw_path in paths:
        matches = sorted(glob.glob(raw_path))
        if matches:
            for match in matches:
                if os.path.isdir(match):
                    resolved.append(os.path.join(match, "SKILL.md"))
                else:
                    resolved.append(match)
            continue

        if os.path.isdir(raw_path):
            resolved.append(os.path.join(raw_path, "SKILL.md"))
        else:
            resolved.append(raw_path)

    deduped: list[str] = []
    seen = set()
    for path in resolved:
        norm = os.path.normpath(path)
        if norm not in seen:
            seen.add(norm)
            deduped.append(norm)
    return deduped


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    skill_files = resolve_skill_files(args.paths)
    if not skill_files:
        print("No skills found.")
        return 1

    all_issues: list[Issue] = []
    for path in skill_files:
        all_issues.extend(check_skill(path))

    if not all_issues:
        print("All skills pass conformance checks.")
        return 0

    print("Skill conformance issues detected:\n")
    for issue in all_issues:
        print(f"- {issue.code}: {issue.path} ({issue.detail})")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
