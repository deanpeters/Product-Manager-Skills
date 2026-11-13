#!/usr/bin/env python3
"""Print bundle membership from pm-skills.config.yaml, for the pack builders.

  python3 scripts/bundle-skills.py --list        # bundle names, lifecycle order, one per line
  python3 scripts/bundle-skills.py <bundle>      # that bundle's skills plus Core, one per line

Core skills are included so every pack carries the shared helpers (the same
rule scripts/build-plugins.py applies to plugins). Deterministic, no network.
"""
from __future__ import annotations

import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    cfg = yaml.safe_load(open(os.path.join(ROOT, "pm-skills.config.yaml"), encoding="utf-8"))
    bundles = cfg["bundles"]
    if sys.argv[1] == "--list":
        print("\n".join(bundles))
        return 0
    name = sys.argv[1]
    if name not in bundles:
        print(f"Error: unknown bundle '{name}'. Known: {', '.join(bundles)}", file=sys.stderr)
        return 1
    own = [s for m in bundles[name]["motions"].values() for s in (m.get("skills") or [])]
    seen: list[str] = []
    for s in own + list(cfg.get("core") or []):
        if s not in seen:
            seen.append(s)
    print("\n".join(seen))
    return 0


if __name__ == "__main__":
    sys.exit(main())
