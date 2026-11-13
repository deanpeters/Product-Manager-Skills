#!/usr/bin/env python3
"""Detect silent drift between what the docs claim and what's actually shipped.

Checks:
- every skills/<name>/ directory has an entry in .claude-plugin/marketplace.json
- every marketplace.json entry points at a skill directory that exists (no ghosts)
  (bundle entries with source "./" install the whole repo and are exempt;
  lifecycle-bundle entries must point at a generated plugins/<name>/ folder)
- every skills/<name>/SKILL.md link mentioned in README.md and CLAUDE.md resolves
- prose counts agree with the library: total skills (README badge, banner, tagline, headings,
  install guide, marketplace description, CLAUDE.md), skills per type, and skills per lifecycle
  bundle in the README pack table

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

    plugins = marketplace.get("plugins", [])
    # Bundle entries (source "./") install the whole repo, not one skill dir.
    bundles = [p for p in plugins if p.get("source") in ("./", ".")]
    # Lifecycle-bundle entries point at generated plugins/<name>/ folders
    # (scripts/build-plugins.py); each must exist and carry a plugin manifest.
    lifecycle = [p for p in plugins if p.get("category") == "lifecycle-bundle"]
    for entry in lifecycle:
        src = entry.get("source", "")
        if not os.path.isfile(os.path.join(src, ".claude-plugin", "plugin.json")):
            issues.append(
                f"marketplace_bundle_broken: lifecycle bundle '{entry['name']}' has no "
                f"plugin at {src} (run python3 scripts/build-plugins.py)"
            )
    listed = {p["name"] for p in plugins if p not in bundles and p not in lifecycle}
    for bundle in bundles:
        if not os.path.isdir("skills"):
            issues.append(
                f"marketplace_bundle_broken: bundle '{bundle['name']}' needs a "
                f"skills/ directory at the repo root"
            )

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


def read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def check_prose_counts(skills: set[str]) -> list[str]:
    """Counts written in prose must match the library. These surfaces drift silently."""
    import collections

    import yaml

    issues: list[str] = []
    total = len(skills)

    def expect(path: str, pattern: str, want: int, label: str) -> None:
        if not os.path.isfile(path):
            return
        found = re.findall(pattern, read(path))
        if not found:
            issues.append(f"prose_count_missing: {path} has no '{label}' to check")
        for got in found:
            if int(got) != want:
                issues.append(f"prose_count: {path} says {got} for '{label}', library has {want}")

    expect("README.md", r"skills-(\d+)-informational", total, "skills badge")
    expect("README.md", r"(\d+) battle-tested", total, "banner/tagline")
    expect("README.md", r"## (\d+) Skills, 3 Types", total, "Skills, 3 Types heading")
    expect("README.md", r"[Aa]ll (\d+) skills", total, "all N skills")
    expect("docs/INSTALL-CLAUDE-CODE.md", r"all (\d+) skills", total, "all N skills")
    expect(MARKETPLACE_PATH, r"(\d+) battle-tested", total, "marketplace description")
    expect("CLAUDE.md", r"Current State: v[\d.]+ \((\d+) skills\)", total, "status line")
    expect("CLAUDE.md", r"\*\*(\d+) Skills\*\*", total, "Skills heading")

    types: collections.Counter = collections.Counter()
    for name in skills:
        m = re.search(r"^type:\s*(\w+)", read(f"skills/{name}/SKILL.md"), re.M)
        if m:
            types[m.group(1)] += 1
    for kind in ("workflow", "interactive", "component"):
        expect("README.md", rf"{kind.upper()} SKILLS \((\d+)\)", types[kind], f"{kind} box")
        expect("CLAUDE.md", rf"- (\d+) {kind.capitalize()} Skills", types[kind], f"{kind} count")

    if os.path.isfile("pm-skills.config.yaml") and os.path.isfile("README.md"):
        cfg = yaml.safe_load(read("pm-skills.config.yaml")) or {}
        readme = read("README.md")
        for bname, bundle in (cfg.get("bundles") or {}).items():
            own = sum(len(m.get("skills") or []) for m in bundle["motions"].values())
            row = re.search(rf"pm-{bname}-pack\.zip.*?\((\d+) skills\)", readme)
            if row and int(row.group(1)) != own:
                issues.append(f"prose_count: README pack table says {row.group(1)} for {bname}, config has {own}")
    return issues


def main() -> int:
    skills = skill_dirs()
    if not skills:
        print("No skills found under skills/*/SKILL.md.")
        return 1

    issues = check_marketplace(skills) + check_doc_links(skills) + check_prose_counts(skills)

    if not issues:
        print(
            f"No library drift detected ({len(skills)} skills; marketplace, "
            f"doc links, and prose counts in sync)."
        )
        return 0

    print("Library drift detected:\n")
    for issue in issues:
        print(f"- {issue}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
