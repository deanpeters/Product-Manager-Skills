#!/usr/bin/env python3
"""Add opencode compatibility frontmatter to all 55 SKILL.md files.

- Inserts `compatibility: opencode`
- Nests rich fields (intent, type, theme, best_for, scenarios,
  estimated_time, sources) under `metadata:`
- Preserves `name`, `description`, `argument-hint` as top-level
- Keeps body content (after `---` closing) unchanged
- Writes files in-place
"""

import os
import sys
from ruamel.yaml import YAML

SKILLS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "skills")

META_FIELDS = {
    "intent",
    "type",
    "theme",
    "best_for",
    "scenarios",
    "estimated_time",
    "sources",
}
TOP_FIELDS = {"name", "description", "argument-hint"}

yaml = YAML()
yaml.preserve_quotes = True
yaml.width = 200
yaml.indent(mapping=2, sequence=4, offset=2)


def transform_skill(skill_dir: str) -> bool:
    skill_path = os.path.join(skill_dir, "SKILL.md")
    if not os.path.isfile(skill_path):
        print(f"  SKIP (no SKILL.md): {skill_path}")
        return False

    with open(skill_path, "r") as f:
        raw = f.read()

    parts = raw.split("---", 2)
    if len(parts) < 3:
        print(f"  SKIP (bad frontmatter): {skill_path}")
        return False

    fm_raw = parts[1]
    body = parts[2]

    fm_data = yaml.load(fm_raw)
    if fm_data is None:
        fm_data = {}

    if fm_data.get("compatibility") == "opencode":
        print(f"  SKIP (already compatible): {skill_path}")
        return False

    metadata = {}
    new_fm = {}

    for key, value in fm_data.items():
        if key in META_FIELDS:
            metadata[key] = value
        else:
            new_fm[key] = value

    new_fm["compatibility"] = "opencode"

    if metadata:
        # insert metadata after argument-hint (if present) or after description
        # Build ordered dict-ish approach: compose YAML string manually
        pass

    # Build the final frontmatter as a composed mapping that preserves order
    final = yaml.map()
    final["name"] = new_fm.pop("name")
    final["description"] = new_fm.pop("description")
    final["compatibility"] = "opencode"

    if "argument-hint" in new_fm:
        final["argument-hint"] = new_fm.pop("argument-hint")

    if metadata:
        md = yaml.map()
        for k in sorted(metadata.keys()):
            md[k] = metadata[k]
        final["metadata"] = md

    for k in new_fm:
        final[k] = new_fm[k]

    from io import StringIO
    buf = StringIO()
    yaml.dump(final, buf)
    new_fm_str = buf.getvalue().rstrip("\n")

    new_raw = f"---\n{new_fm_str}\n---{body}"

    with open(skill_path, "w") as f:
        f.write(new_raw)

    print(f"  OK: {skill_path}")
    return True


def main():
    skills = sorted(os.listdir(SKILLS_DIR))
    changed = 0
    skipped = 0

    for skill_name in skills:
        skill_dir = os.path.join(SKILLS_DIR, skill_name)
        if not os.path.isdir(skill_dir):
            continue
        result = transform_skill(skill_dir)
        if result:
            changed += 1
        else:
            skipped += 1

    print(f"\nDone. Changed: {changed}, Skipped: {skipped}")


if __name__ == "__main__":
    main()