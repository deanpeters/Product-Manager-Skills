#!/usr/bin/env python3
"""Check the bundle mapping in pm-skills.config.yaml against skills/.

Fails (exit 1) when:
  - a skill in skills/ has no home (not in any bundle motion and not in core)
  - a skill appears in more than one place
  - the config names a skill that does not exist
  - a bundle or motion name does not start with D
  - a motion shares its bundle's name (readers would confuse the two)
  - a motion is empty without a 'gap:' line saying what it is waiting for

Usage:
  python3 scripts/check-bundles.py            # check skills/ against the config
  python3 scripts/check-bundles.py --summary  # also print bundle and motion counts
  python3 scripts/check-bundles.py --write-navigator   # regenerate the map inside skills/pm-skills-navigator

The navigator skill carries a copy of the bundle map between BUNDLE-MAP markers (skills must
run standalone, so it can't read the config at runtime). The check fails if that copy drifts.

Deterministic, no network calls.
"""
from __future__ import annotations

import argparse
import collections
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAV_START, NAV_END = "<!-- BUNDLE-MAP:START -->", "<!-- BUNDLE-MAP:END -->"


def render_map(bundles: dict, core: list[str]) -> str:
    """The bundle map the navigator skill carries, generated from the config."""
    lines: list[str] = []
    for bname, bundle in bundles.items():
        lines += [f"**{bname.capitalize()}** ({bundle['phase']}): {bundle['summary']}", ""]
        for mname, motion in bundle["motions"].items():
            skills = motion.get("skills") or []
            names = ", ".join(f"[`{x}`](../{x}/SKILL.md)" for x in skills) if skills else f"*Coming: {motion.get('gap', 'in progress')}*"
            lines.append(f"- **{mname.capitalize()}** ({motion['summary']}): {names}")
        lines.append("")
    lines.append("**Core** (shared helpers that ship with every bundle): " + ", ".join(f"[`{x}`](../{x}/SKILL.md)" for x in core))
    return "\n".join(lines)


def navigator_path(skills_dir: str) -> str:
    return os.path.join(skills_dir, "pm-skills-navigator", "SKILL.md")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--skills-dir", default=os.path.join(ROOT, "skills"))
    ap.add_argument("--config", default=os.path.join(ROOT, "pm-skills.config.yaml"))
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--write-navigator", action="store_true", help="regenerate the map in the navigator skill")
    args = ap.parse_args()

    with open(args.config, encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh) or {}
    bundles = cfg.get("bundles") or {}
    core = cfg.get("core") or []
    if not bundles:
        print("Error: no 'bundles' section in config", file=sys.stderr)
        return 1

    on_disk = {d for d in os.listdir(args.skills_dir) if os.path.isfile(os.path.join(args.skills_dir, d, "SKILL.md"))}
    errors: list[str] = []
    homes: list[tuple[str, str]] = [(s, "core") for s in core]

    for bname, bundle in bundles.items():
        if not bname.startswith("d"):
            errors.append(f"bundle '{bname}' does not start with D")
        for field in ("phase", "summary"):
            if not (bundle or {}).get(field):
                errors.append(f"bundle '{bname}' is missing '{field}'")
        for mname, motion in ((bundle or {}).get("motions") or {}).items():
            where = f"{bname}/{mname}"
            if not mname.startswith("d"):
                errors.append(f"motion '{where}' does not start with D")
            if mname == bname:
                errors.append(f"motion '{where}' shares its bundle's name")
            skills = (motion or {}).get("skills") or []
            if not skills and not (motion or {}).get("gap"):
                errors.append(f"motion '{where}' is empty and has no 'gap:' line")
            if not (motion or {}).get("summary"):
                errors.append(f"motion '{where}' is missing 'summary'")
            homes += [(s, where) for s in skills]

    for skill, count in collections.Counter(s for s, _ in homes).items():
        if count > 1:
            places = ", ".join(w for s, w in homes if s == skill)
            errors.append(f"'{skill}' has {count} homes: {places}")

    mapped = {s for s, _ in homes}
    for skill in sorted(mapped - on_disk):
        errors.append(f"config names unknown skill '{skill}'")
    for skill in sorted(on_disk - mapped):
        errors.append(f"skill '{skill}' has no bundle home (add it to a motion or to core)")

    nav = navigator_path(args.skills_dir)
    if os.path.isfile(nav):
        text = open(nav, encoding="utf-8").read()
        want = f"{NAV_START}\n{render_map(bundles, core)}\n{NAV_END}"
        if NAV_START in text and NAV_END in text:
            have = text[text.index(NAV_START): text.index(NAV_END) + len(NAV_END)]
            if args.write_navigator:
                open(nav, "w", encoding="utf-8").write(text.replace(have, want))
                print("Navigator map regenerated.")
                return 0
            if have != want:
                errors.append("pm-skills-navigator's bundle map is stale; run: python3 scripts/check-bundles.py --write-navigator")
        else:
            errors.append("pm-skills-navigator is missing its BUNDLE-MAP markers")

    if args.summary:
        for bname, bundle in bundles.items():
            motions = (bundle or {}).get("motions") or {}
            total = sum(len((m or {}).get("skills") or []) for m in motions.values())
            detail = ", ".join(f"{k} {len((v or {}).get('skills') or [])}" for k, v in motions.items())
            print(f"{bname}: {total} ({detail})")
        print(f"core: {len(core)}")

    if errors:
        print("Bundle check failed:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print(f"Bundles OK: {len(on_disk)} skills, {len(bundles)} bundles, each skill has exactly one home.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
