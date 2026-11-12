#!/usr/bin/env python3
"""Apply pm-skills.config.yaml's default entry mode to skill files.

Every skill that runs the workshop-facilitation protocol carries one line:

    **Default entry mode:** Guided · ...

It also fails --check when a skill says to use workshop-facilitation but has no
such line, so new interactive skills can't silently miss the setting.

This script rewrites the mode name in that line from the config
(per-skill override, else facilitation.default_entry_mode, else guided).

Usage:
  python3 scripts/apply-entry-mode.py                      # rewrite skills/ in place
  python3 scripts/apply-entry-mode.py --check              # exit 1 if skills/ disagrees with config
  python3 scripts/apply-entry-mode.py --skills-dir DIR --filename Skill.md
                                                           # stamp a packaged copy (build scripts)

Deterministic, no network calls.
"""
from __future__ import annotations

import argparse
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG = os.path.join(ROOT, "pm-skills.config.yaml")

MODES = {"guided": "Guided", "context-dump": "Context dump", "best-guess": "Best guess"}
# A skill "runs the protocol" when its body (above References) says to use workshop-facilitation.
USES_RE = re.compile(r"use \[`workshop-facilitation`\]", re.I)
LINE_RE = re.compile(r"^(\*\*Default entry mode:\*\* )(Guided|Context dump|Best guess)( ·)", re.M)


def load_config(path: str) -> tuple[str, dict[str, str]]:
    if not os.path.exists(path):
        return "guided", {}
    with open(path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    fac = data.get("facilitation") or {}
    default = fac.get("default_entry_mode", "guided")
    overrides = fac.get("overrides") or {}
    bad = [v for v in [default, *overrides.values()] if v not in MODES]
    if bad:
        sys.exit(f"Error: unknown entry mode(s) {bad} in {path}; use one of {sorted(MODES)}")
    return default, overrides


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--skills-dir", default=os.path.join(ROOT, "skills"))
    ap.add_argument("--filename", default="SKILL.md")
    ap.add_argument("--config", default=CONFIG)
    ap.add_argument("--check", action="store_true", help="report drift instead of writing")
    args = ap.parse_args()

    default, overrides = load_config(args.config)
    names = sorted(d for d in os.listdir(args.skills_dir) if os.path.isfile(os.path.join(args.skills_dir, d, args.filename)))

    errors: list[str] = []
    for name in overrides:
        if name not in names:
            errors.append(f"override names unknown skill '{name}'")

    stamped = changed = 0
    for name in names:
        path = os.path.join(args.skills_dir, name, args.filename)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        matches = LINE_RE.findall(text)
        if not matches:
            if name in overrides:
                errors.append(f"'{name}' has an override but no 'Default entry mode' line")
            body = text.split("\n## References", 1)[0]
            if USES_RE.search(body):
                errors.append(f"'{name}' uses workshop-facilitation but has no 'Default entry mode' line "
                              "(copy it from any advisor, e.g. skills/prioritization-advisor/SKILL.md)")
            continue
        if len(matches) > 1:
            errors.append(f"'{name}' has {len(matches)} 'Default entry mode' lines (expected 1)")
            continue
        stamped += 1
        want = MODES[overrides.get(name, default)]
        if matches[0][1] == want:
            continue
        changed += 1
        if args.check:
            errors.append(f"'{name}' says {matches[0][1]}, config says {want}")
        else:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(LINE_RE.sub(lambda m: m.group(1) + want + m.group(3), text))

    for e in errors:
        print(f"ERROR: {e}", file=sys.stderr)
    if errors:
        if args.check:
            print("Fix: add any missing lines by hand, then run python3 scripts/apply-entry-mode.py", file=sys.stderr)
        return 1
    verb = "would change" if args.check else "changed"
    print(f"Entry mode: default={default}, overrides={len(overrides)}; {stamped} skills carry the line, {changed} {verb}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
