#!/usr/bin/env python3
"""Detect silent drift between what the docs claim and what's actually shipped.

Checks:
- every skills/<name>/ directory has an entry in .claude-plugin/marketplace.json
- every marketplace.json entry points at a skill directory that exists (no ghosts)
- every skills/<name>/SKILL.md link mentioned in README.md and CLAUDE.md resolves

Why this exists: v0.81 shipped two fixes for exactly these failures — a skill
(agent-orchestration-advisor) that docs referenced for months but only existed
on an orphaned commit, and a marketplace.json that silently lagged the library
by 8 skills. Docs that claim more than the repo contains erode trust one broken
link at a time; this check makes that drift a build failure instead of a
discovery.
"""

from __future__ import annotations

import glob
import json
import os
import re
import sys

MARKETPLACE_PATH = ".claude-plugin/marketplace.json"
DOCS_TO_SCAN = ["README.md", "CLAUDE.md"]
SKILL_LINK_PATTERN = re.compile(r"skills/([a-z0-9-]+)/SKILL\.md")
# Documentation examples use these as stand-ins for a real skill name.
PLACEHOLDER_NAMES = {"skill-name", "new-skill-name", "your-skill-name"}


def skill_dirs() -> set[str]:
    return {
        os.path.basename(os.path.dirname(path))
        for path in glob.glob("skills/*/SKILL.md")
    }


def check_marketplace(skills: set[str]) -> list[str]:
    issues: list[str] = []
    if not os.path.isfile(MARKETPLACE_PATH):
        return [f"marketplace_missing: {MARKETPLACE_PATH} not found"]

    with open(MARKETPLACE_PATH, "r", encoding="utf-8") as handle:
        marketplace = json.load(handle)

    listed = {plugin["name"] for plugin in marketplace.get("plugins", [])}

    for name in sorted(skills - listed):
        issues.append(
            f"marketplace_entry_missing: skills/{name}/ exists but has no "
            f"entry in {MARKETPLACE_PATH}"
        )
    for name in sorted(listed - skills):
        issues.append(
            f"marketplace_ghost_entry: {MARKETPLACE_PATH} lists '{name}' "
            f"but skills/{name}/SKILL.md does not exist"
        )
    return issues


def check_doc_links(skills: set[str]) -> list[str]:
    issues: list[str] = []
    for doc in DOCS_TO_SCAN:
        if not os.path.isfile(doc):
            continue
        with open(doc, "r", encoding="utf-8") as handle:
            text = handle.read()
        for name in sorted(set(SKILL_LINK_PATTERN.findall(text)) - PLACEHOLDER_NAMES):
            if name not in skills:
                issues.append(
                    f"doc_link_broken: {doc} references skills/{name}/SKILL.md "
                    f"which does not exist"
                )
    return issues


def main() -> int:
    skills = skill_dirs()
    if not skills:
        print("No skills found under skills/*/SKILL.md.")
        return 1

    issues = check_marketplace(skills) + check_doc_links(skills)

    if not issues:
        print(
            f"No library drift detected ({len(skills)} skills; marketplace "
            f"and doc links in sync)."
        )
        return 0

    print("Library drift detected:\n")
    for issue in issues:
        print(f"- {issue}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
