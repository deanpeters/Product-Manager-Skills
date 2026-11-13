#!/usr/bin/env python3
"""Fail when the committed catalog/ and dist/ shelf have drifted from skills/.

Why this exists
---------------
`check-library-drift.py` verifies marketplace.json and doc links. It does NOT
look at `catalog/` or `dist/`, so the library could pass CI completely green
while the browsable download shelf still advertised the previous release. That
happened between v0.83 and v0.84 and was caught by hand.

Why it is not part of validate-skills.sh
----------------------------------------
`build-dist.sh` calls `build-release.sh`, which calls `validate-skills.sh`. If
this check lived there, the very command you run to FIX staleness would abort
before regenerating anything. So it is a standalone script, wired into CI as its
own step and run by hand before committing a skill change.

Checks are deliberately content-level, never byte-level: rebuilt ZIPs differ on
every run because of embedded timestamps, so comparing archive bytes would fail
constantly and teach everyone to ignore it.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
CATALOG = ROOT / "catalog"
DIST = ROOT / "dist"
PACK_BUILDER = ROOT / "scripts" / "build-claude-desktop-packs.sh"

FIX = (
    "Fix with:\n"
    "  python3 scripts/generate-catalog.py\n"
    "  bash scripts/build-dist.sh"
)


def skill_names() -> set[str]:
    return {p.parent.name for p in SKILLS.glob("*/SKILL.md")}


def declared_packs() -> set[str]:
    """Pack ZIP names declared in build-claude-desktop-packs.sh."""
    if not PACK_BUILDER.exists():
        return set()
    text = PACK_BUILDER.read_text()
    names = set(re.findall(r'pack_skills\s+"([^"]+\.zip)"', text))
    names |= set(re.findall(r'pack_all_skills\s+"([^"]+\.zip)"', text))
    names = {n for n in names if "$" not in n}  # the bundle loop's template, not a real pack
    # Lifecycle bundle packs are generated from the bundles: mapping in the config.
    try:
        import yaml
        cfg = yaml.safe_load((ROOT / "pm-skills.config.yaml").read_text()) or {}
        names |= {f"pm-{b}-pack.zip" for b in (cfg.get("bundles") or {})}
    except ImportError:
        pass
    return names


def main() -> int:
    problems: list[str] = []
    skills = skill_names()

    if not skills:
        print("Error: no skills found", file=sys.stderr)
        return 2

    # 1. catalog/skills-index.yaml -- declared count and membership
    index = CATALOG / "skills-index.yaml"
    if not index.exists():
        problems.append("catalog/skills-index.yaml is missing")
    else:
        text = index.read_text()
        m = re.search(r"^count:\s*(\d+)", text, re.M)
        if not m:
            problems.append("catalog/skills-index.yaml has no count: field")
        elif int(m.group(1)) != len(skills):
            problems.append(
                f"catalog/skills-index.yaml says count: {m.group(1)}, "
                f"but skills/ has {len(skills)}"
            )
        listed = set(re.findall(r"^- name:\s*(\S+)", text, re.M))
        for missing in sorted(skills - listed):
            problems.append(f"catalog/skills-index.yaml is missing: {missing}")
        for orphan in sorted(listed - skills):
            problems.append(f"catalog/skills-index.yaml lists a removed skill: {orphan}")

    # 2. dist/ -- one individual ZIP per skill, no orphans
    if not DIST.exists():
        problems.append("dist/ is missing")
    else:
        zips = {p.stem for p in DIST.glob("*.zip")}
        for missing in sorted(skills - zips):
            problems.append(f"dist/{missing}.zip is missing")
        for orphan in sorted(zips - skills):
            problems.append(f"dist/{orphan}.zip has no matching skill")

    # 3. dist/packages/ -- every declared pack is present
    packages = DIST / "packages"
    if not packages.exists():
        problems.append("dist/packages/ is missing")
    else:
        present = {p.name for p in packages.glob("*.zip")}
        for pack in sorted(declared_packs()):
            # the starter pack is republished under its public name
            if pack == "01-core-pm-starter-pack.zip":
                if "pm-skills-starter-pack.zip" not in present:
                    problems.append("dist/packages/pm-skills-starter-pack.zip is missing")
                continue
            if pack not in present:
                problems.append(f"dist/packages/{pack} is missing (declared in build-claude-desktop-packs.sh)")

    # 4. dist/CATALOG.md -- regenerated alongside the ZIPs
    catalog_md = DIST / "CATALOG.md"
    if not catalog_md.exists():
        problems.append("dist/CATALOG.md is missing")
    else:
        text = catalog_md.read_text()
        for missing in sorted(s for s in skills if s not in text):
            problems.append(f"dist/CATALOG.md does not mention: {missing}")

    if problems:
        print("Distribution drift detected:\n")
        for p in problems:
            print(f"- {p}")
        print(f"\n{FIX}")
        return 1

    print(
        f"dist/ and catalog/ are in sync with skills/ "
        f"({len(skills)} skills, {len(declared_packs())} declared packs)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
