#!/usr/bin/env bash
#
# build-dist.sh - Assemble the committed, browsable dist/ distribution folder.
#
# This is the folder users can navigate to at:
#   https://github.com/deanpeters/Product-Manager-Skills/tree/main/dist
#
# Layout produced (all tracked in git):
#   dist/README.md              plain-language landing page (renders on GitHub)
#   dist/CATALOG.md             browsable catalog of every skill, by category
#   dist/<skill>.zip            individual, upload-ready skill ZIPs (flat)
#   dist/packages/<pack>.zip    curated bundles + the Codex package
#
# It runs the existing build-release.sh (which validates + builds every
# artifact), then curates the tracked layout and regenerates the two docs.
# Nothing under dist/ is hand-maintained; re-run this to refresh it.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
DIST="$ROOT/dist"

echo "[1/4] Building all release artifacts (validate + packs + codex + skill zips)"
bash "$SCRIPT_DIR/build-release.sh" >/dev/null
echo "  done"

echo "[2/4] Curating tracked layout"
# Clear the tracked parts (leave the ignored build scratch dirs in place)
find "$DIST" -maxdepth 1 -type f -name '*.zip' -delete 2>/dev/null || true
rm -rf "$DIST/packages"
mkdir -p "$DIST/packages"

# Individual skill ZIPs -> dist/ root (flat)
cp "$DIST"/skill-zips/*.zip "$DIST"/
skill_zip_count="$(find "$DIST" -maxdepth 1 -type f -name '*.zip' | wc -l | tr -d ' ')"

# Curated bundles + codex -> dist/packages/
# Lifecycle bundle packs come from the bundles: mapping in pm-skills.config.yaml.
bundle_packs=()
while read -r b; do bundle_packs+=("pm-${b}-pack"); done \
  < <(python3 "$SCRIPT_DIR/bundle-skills.py" --list)
for p in pm-skills-starter-pack "${bundle_packs[@]}" \
         99-all-skills-pack; do
  cp "$DIST/claude-desktop/$p.zip" "$DIST/packages/"
done
cp "$DIST/codex/pm-skills-codex.zip" "$DIST/packages/"
echo "  $skill_zip_count individual skill ZIPs, $(find "$DIST/packages" -name '*.zip' | wc -l | tr -d ' ') packages"

echo "[3/4] Generating CATALOG.md and README.md"
python3 - "$ROOT" <<'PY'
import os, sys, glob
try:
    import yaml
except ImportError:
    sys.exit("PyYAML required (used elsewhere in this repo)")

root = sys.argv[1]
dist = os.path.join(root, "dist")
skills_dir = os.path.join(root, "skills")

def frontmatter(path):
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    return yaml.safe_load(text[3:end]) or {}

skills = []
for p in sorted(glob.glob(os.path.join(skills_dir, "*", "SKILL.md"))):
    fm = frontmatter(p)
    name = fm.get("name") or os.path.basename(os.path.dirname(p))
    skills.append({
        "name": name,
        "type": (fm.get("type") or "other").lower(),
        "desc": (fm.get("description") or "").strip().strip('"'),
    })

TYPES = [
    ("component", "Component Skills", "Self-contained artifacts and templates."),
    ("interactive", "Interactive Skills", "Guided, multi-turn advisors that ask then recommend."),
    ("workflow", "Workflow Skills", "End-to-end processes that orchestrate other skills."),
]
by_type = {t: [s for s in skills if s["type"] == t] for t, _, _ in TYPES}
total = len(skills)

# ---- CATALOG.md ----
lines = [
    "# Skill Catalog",
    "",
    f"All **{total} skills** in this library. Each links to its individual "
    "download ZIP in this folder — click, download, unzip, and upload the "
    "`SKILL.md` to Claude. No terminal required.",
    "",
    "> New here? Read [`README.md`](README.md) first — it explains how to pick "
    "a pack and install.",
    "",
]
for key, title, blurb in TYPES:
    rows = sorted(by_type[key], key=lambda s: s["name"])
    if not rows:
        continue
    lines += [f"## {title} ({len(rows)})", "", f"_{blurb}_", "",
              "| Skill | What it does |", "|---|---|"]
    for s in rows:
        lines.append(f"| [`{s['name']}`]({s['name']}.zip) | {s['desc']} |")
    lines.append("")
open(os.path.join(dist, "CATALOG.md"), "w", encoding="utf-8").write("\n".join(lines))

# ---- bundle + legacy rows (bundles come from pm-skills.config.yaml) ----
cfg = yaml.safe_load(open(os.path.join(root, "pm-skills.config.yaml"), encoding="utf-8"))
core = cfg.get("core") or []
bundle_rows = ""
for bname, b in cfg["bundles"].items():
    n = sum(len(m.get("skills") or []) for m in b["motions"].values())
    bundle_rows += (f"| [`pm-{bname}-pack.zip`](packages/pm-{bname}-pack.zip) | "
                    f"**{bname.capitalize()}**: {b['summary']} {n} skills + shared helpers |\n")

# ---- CATALOG: browse by bundle (the lifecycle view) ----
desc = {s["name"]: s["desc"] for s in skills}
cat_lines = ["", "## Browse by lifecycle bundle", "",
             "_The same skills, grouped by where they fit in the product lifecycle._", ""]
for bname, b in cfg["bundles"].items():
    cat_lines += [f"### {bname.capitalize()} ({b['phase']})", "", f"{b['summary']}", ""]
    for mname, m in b["motions"].items():
        cat_lines += [f"**{mname.capitalize()}**: {m['summary']}", ""]
        for sk in (m.get("skills") or []):
            cat_lines.append(f"- [`{sk}`]({sk}.zip): {desc.get(sk, '')}")
        if not m.get("skills"):
            cat_lines.append(f"- _Coming: {m.get('gap', 'in progress')}_")
        cat_lines.append("")
cat_lines += ["### Core (ships with every bundle)", ""]
cat_lines += [f"- [`{sk}`]({sk}.zip): {desc.get(sk, '')}" for sk in core] + [""]
with open(os.path.join(dist, "CATALOG.md"), "a", encoding="utf-8") as fh:
    fh.write("\n".join(cat_lines))

# ---- README.md ----
readme = f"""# Product Manager Skills — Downloads

Welcome. This folder is the **easy download shelf** for the library — no code, no
terminal. Grab what you want, unzip it, and upload the skills to Claude.

There are **{total} skills** in total. Two ways to get them:

## 1. Grab a bundle (recommended)

Bundles live in [`packages/`](packages/). Download one ZIP, unzip it, and you'll
find upload-ready skill ZIPs inside.

| Bundle | Best for |
|---|---|
| [`pm-skills-starter-pack.zip`](packages/pm-skills-starter-pack.zip) | Most PMs: a small, practical starter set |
{bundle_rows}| [`99-all-skills-pack.zip`](packages/99-all-skills-pack.zip) | Everything — all {total} skills |
| [`pm-skills-codex.zip`](packages/pm-skills-codex.zip) | OpenAI Codex users (`.agents/skills` + `AGENTS.md`) |

### The lifecycle bundles

The library follows the product lifecycle. Each `pm-<name>-pack.zip` holds one
phase, plus the shared helper skills, so it works on its own:
**Determine** (set outcomes, read the market) → **Discover** (find the real problem)
→ **Define** (shape and test the solution) → **Develop** (turn it into buildable work)
→ **Deliver** (take it to market, measure, retire). **Drive** runs under all five:
your stakeholders and your career.

## 2. Grab one skill at a time

Every skill has its own ZIP right here in this folder. Browse them in
[`CATALOG.md`](CATALOG.md), then click the one you want.

## How to install (Claude Desktop / Web)

1. Download a bundle (or an individual skill ZIP).
2. If it's a bundle, unzip it. Inside is a folder of smaller skill ZIPs.
   **Don't upload the outer bundle ZIP to Claude.** Upload the skill ZIPs inside it.
3. In Claude, open **Settings → Capabilities → Skills** and upload one or more skill ZIPs.
4. Start a chat and paste: `Which of these skills fits what's on my desk this week?`
   You'll know it worked when Claude names a skill and starts asking you questions.
   Arriving empty-handed is fine; the skills ask for what they need.

Full step-by-step guides live in [`../docs/`](../docs): `INSTALL-CLAUDE-DESKTOP.md`,
`INSTALL-CLAUDE-CODE.md`, and `INSTALL-CODEX.md`.

---

_This folder is generated by `scripts/build-dist.sh` from the canonical `skills/`
source. Don't edit files here by hand — re-run the script to refresh them._
"""
open(os.path.join(dist, "README.md"), "w", encoding="utf-8").write(readme)
print(f"  catalog + readme written ({total} skills)")
PY

echo "[4/4] dist/ assembled and ready to commit"
echo
echo "Tracked layout:"
echo "  dist/README.md"
echo "  dist/CATALOG.md"
echo "  dist/*.zip                ($skill_zip_count individual skills)"
echo "  dist/packages/*.zip       (bundles + codex)"
