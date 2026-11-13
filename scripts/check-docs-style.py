#!/usr/bin/env python3
"""Style check for reader-facing docs (see docs/writing-for-our-readers.md).

Hard failures (exit 1):
  - "click here" link text (say where the link goes)
  - a "New in vX" / "Part of the vX" stale-version line outside changelogs
  - a stale pack name (02-discovery ... 07-lifecycle-eol) outside a line that
    calls it older/legacy/retire
  - a Settings menu path in backticks instead of bold (the Adopter needs to see it)

Warnings (printed, never fail):
  - Practitioner-file first-screen jargon (repo, clone, terminal, CLI, frontmatter, YAML,
    repository) in the first 40 lines of a file

Deterministic, no network calls.
Usage: python3 scripts/check-docs-style.py [--strict-warnings]
"""
from __future__ import annotations

import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ["README.md", "START_HERE.md", "dist/README.md", "docs/Platform Guides for PMs.md"]
# Files whose first screen belongs to the Practitioner (non-technical reader)
PRACTITIONER = {"README.md", "START_HERE.md", "dist/README.md", "docs/Platform Guides for PMs.md",
                "docs/INSTALL-CLAUDE-DESKTOP.md", "docs/Using PM Skills 101.md",
                "docs/Using PM Skills with Claude Desktop.md", "docs/Using PM Skills with ChatGPT Desktop.md"}
GLOBS = ["docs/INSTALL-*.md", "docs/Using PM Skills*.md"]
STALE_PACK = re.compile(r"0[2-7]-(discovery|strategy|delivery|ai-pm|market-intel|lifecycle-eol)-pack")
LEGACY_OK = re.compile(r"older|legacy|retire|replaced", re.I)
JARGON = re.compile(r"\b(repo|repository|clone|terminal|CLI|frontmatter|YAML)\b", re.I)


def main() -> int:
    paths = [os.path.join(ROOT, f) for f in FILES]
    for g in GLOBS:
        paths += sorted(glob.glob(os.path.join(ROOT, g)))
    errors: list[str] = []
    warns: list[str] = []
    for p in paths:
        if not os.path.isfile(p):
            continue
        rel = os.path.relpath(p, ROOT)
        lines = open(p, encoding="utf-8").read().split("\n")
        in_code = False
        for n, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                in_code = not in_code
            if in_code:
                continue
            if re.search(r"\[click here\]|\bclick here\b", line, re.I):
                errors.append(f'{rel}:{n}: "click here" link text')
            if re.search(r"(New in|Part of the) v0\.\d+", line):
                errors.append(f"{rel}:{n}: stale version line")
            if STALE_PACK.search(line) and not (LEGACY_OK.search(line) or "<summary>" in line):
                # table rows listing older packs sit inside a <details> block; allow those
                if not any("Older pack" in l or "older packs" in l.lower() for l in lines[max(0, n - 8):n]):
                    errors.append(f"{rel}:{n}: stale pack name outside an 'older packs' context")
            if re.search(r"`Settings\s*(->|→)", line):
                errors.append(f"{rel}:{n}: menu path in backticks; bold it, for example **Settings → Capabilities → Skills**")
            if n <= 40 and rel in PRACTITIONER and JARGON.search(line) and not line.startswith(("[![", "http")):
                warns.append(f"{rel}:{n}: first-screen jargon: {JARGON.search(line).group(0)}")
    for w in warns:
        print(f"warning: {w}")
    if errors:
        print("Docs style check failed:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    if warns and "--strict-warnings" in sys.argv:
        return 1
    print(f"Docs style OK ({len(paths)} files, {len(warns)} warnings).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
