#!/usr/bin/env python3
"""Detect silent drift between what the docs claim and what's actually shipped.

Checks:
- marketplace.json is either a single root plugin (source "./") or a legacy
  per-skill plugins[] list kept in sync with skills/*/
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
    """Validate marketplace.json against the skill tree.

    Two supported shapes:
    1. Single-plugin marketplace: one entry with source "./" (or ".") that
       ships the whole repo via root .claude-plugin/plugin.json.
    2. Legacy per-skill marketplace: one plugins[] entry per skills/<name>/.
    """
    issues: list[str] = []
    if not os.path.isfile(MARKETPLACE_PATH):
        return [f"marketplace_missing: {MARKETPLACE_PATH} not found"]

    with open(MARKETPLACE_PATH, "r", encoding="utf-8") as handle:
        marketplace = json.load(handle)

    plugins = marketplace.get("plugins", [])
    if not plugins:
        return [f"marketplace_empty: {MARKETPLACE_PATH} has no plugins entries"]

    # Single-plugin layout (preferred): source is the repo root.
    if len(plugins) == 1:
        plugin = plugins[0]
        source = plugin.get("source", "").rstrip("/") or "."
        if source in {".", "./"}:
            plugin_json_path = ".claude-plugin/plugin.json"
            if not os.path.isfile(plugin_json_path):
                issues.append(
                    "marketplace_single_plugin_missing_manifest: "
                    f"{plugin_json_path} not found for source '{source}'"
                )
                return issues
            with open(plugin_json_path, "r", encoding="utf-8") as handle:
                plugin_json = json.load(handle)
            expected_name = plugin_json.get("name")
            actual_name = plugin.get("name")
            if expected_name and actual_name != expected_name:
                issues.append(
                    "marketplace_plugin_name_mismatch: marketplace lists "
                    f"'{actual_name}' but {plugin_json_path} name is "
                    f"'{expected_name}'"
                )
            if not skills:
                issues.append(
                    "marketplace_single_plugin_no_skills: skills/ is empty"
                )
            return issues

    # Legacy per-skill layout: every skill dir <-> marketplace entry.
    listed = {plugin["name"] for plugin in plugins}

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
