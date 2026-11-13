#!/usr/bin/env python3
"""Generate bundle plugins from the `bundles:` mapping in pm-skills.config.yaml.

For each bundle (Determine, Discover, Define, Develop, Deliver, Drive) this writes

    plugins/pm-<bundle>/
      .claude-plugin/plugin.json
      README.md                  what the bundle is, by motion, with plain-language summaries
      skills/<skill>/...         copies of the bundle's skills + the Core skills

and upserts one entry per bundle into .claude-plugin/marketplace.json
(every other entry in that file is left exactly as it is).

skills/ stays the ONLY place anyone edits. plugins/ is build output, like dist/.

Why copies: a plugin installs in isolation, so it cannot reach sibling skills by
relative path. Core skills (workshop-facilitation and friends) ship inside every
bundle so the facilitation links keep working. Any other relative link that
would leave the bundle is rewritten, in the copy only, to an absolute GitHub URL.

Usage:
  python3 scripts/build-plugins.py           # regenerate plugins/ and the bundle marketplace entries
  python3 scripts/build-plugins.py --check   # exit 1 if plugins/ or the marketplace entries are stale

Deterministic: no timestamps, no network calls.
"""
from __future__ import annotations

import argparse
import filecmp
import json
import os
import posixpath
import re
import shutil
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
OUT = os.path.join(ROOT, "plugins")
CONFIG = os.path.join(ROOT, "pm-skills.config.yaml")
MARKET = os.path.join(ROOT, ".claude-plugin", "marketplace.json")
ROOT_PLUGIN = os.path.join(ROOT, ".claude-plugin", "plugin.json")
BLOB = "https://github.com/deanpeters/Product-Manager-Skills/blob/main/"
LINK_RE = re.compile(r"(\]\()([^)\s]+)(\))")
SKIP = {".DS_Store", "__pycache__"}


def plugin_name(bundle: str) -> str:
    return f"pm-{bundle}"


def title(bundle: str) -> str:
    return bundle.capitalize()


def bundle_skills(bundle: dict) -> list[str]:
    out: list[str] = []
    for motion in bundle["motions"].values():
        out += motion.get("skills") or []
    return out


def rewrite_links(text: str, rel_file: str, keep: set[str]) -> str:
    """Make relative links survive isolation. rel_file is repo-relative, e.g. skills/x/SKILL.md."""
    base = posixpath.dirname(rel_file)

    def fix(m: re.Match) -> str:
        target = m.group(2)
        if target.startswith(("http://", "https://", "#", "mailto:")):
            return m.group(0)
        path, _, anchor = target.partition("#")
        if not path:
            return m.group(0)
        resolved = posixpath.normpath(posixpath.join(base, path))
        parts = resolved.split("/")
        if parts[0] == "skills" and len(parts) > 1 and parts[1] in keep:
            return m.group(0)  # stays inside the bundle: relative link still resolves
        if resolved.startswith(".."):
            return m.group(0)
        url = BLOB + resolved + ("#" + anchor if anchor else "")
        return f"{m.group(1)}{url}{m.group(3)}"

    return LINK_RE.sub(fix, text)


def copy_skill(name: str, dest_root: str, keep: set[str]) -> None:
    src = os.path.join(SKILLS, name)
    for dirpath, dirnames, filenames in os.walk(src):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP)
        for fn in sorted(filenames):
            if fn in SKIP:
                continue
            sp = os.path.join(dirpath, fn)
            rel_in_skill = os.path.relpath(sp, src)
            dp = os.path.join(dest_root, "skills", name, rel_in_skill)
            os.makedirs(os.path.dirname(dp), exist_ok=True)
            if fn.endswith(".md"):
                text = open(sp, encoding="utf-8").read()
                repo_rel = posixpath.join("skills", name, rel_in_skill.replace(os.sep, "/"))
                open(dp, "w", encoding="utf-8").write(rewrite_links(text, repo_rel, keep))
            else:
                shutil.copyfile(sp, dp)


def bundle_readme(bname: str, bundle: dict, core: list[str], version: str) -> str:
    lines = [
        f"# PM Skills: {title(bname)}",
        "",
        f"> {bundle['summary']}",
        "",
        f"**Lifecycle phase:** {bundle['phase']}",
        "",
        "Generated from `pm-skills.config.yaml`. Do not edit here: change the skill in "
        "[`skills/`](https://github.com/deanpeters/Product-Manager-Skills/tree/main/skills) "
        "and rebuild with `python3 scripts/build-plugins.py`.",
        "",
        "## Install",
        "",
        "```",
        f"/plugin install {plugin_name(bname)} --marketplace deanpeters/Product-Manager-Skills",
        "```",
        "",
        "## Skills by motion",
        "",
    ]
    for mname, motion in bundle["motions"].items():
        lines += [f"### {title(mname)}", "", motion["summary"], ""]
        skills = motion.get("skills") or []
        if skills:
            lines += [f"- [`{s}`](skills/{s}/SKILL.md)" for s in skills]
        else:
            lines.append(f"_Coming: {motion.get('gap', 'in progress')}_")
        lines.append("")
    lines += [
        "## Also included (Core)",
        "",
        "Shared helpers the skills above lean on:",
        "",
        *[f"- [`{s}`](skills/{s}/SKILL.md)" for s in core],
        "",
        "## License",
        "",
        "CC BY-NC-SA 4.0. See [LICENSING.md](https://github.com/deanpeters/Product-Manager-Skills/blob/main/LICENSING.md).",
        "",
    ]
    return "\n".join(lines)


def build(out_dir: str, cfg: dict, version: str) -> dict[str, dict]:
    core: list[str] = cfg.get("core") or []
    entries: dict[str, dict] = {}
    for bname, bundle in cfg["bundles"].items():
        pname = plugin_name(bname)
        dest = os.path.join(out_dir, pname)
        own = bundle_skills(bundle)
        keep = set(own) | set(core)
        for s in sorted(keep):
            copy_skill(s, dest, keep)
        os.makedirs(os.path.join(dest, ".claude-plugin"), exist_ok=True)
        motions = ", ".join(title(m) for m in bundle["motions"])
        desc = f"{bundle['summary']} {len(own)} skills ({motions}); shared helper skills included."
        manifest = {
            "name": pname,
            "description": desc,
            "version": version,
            "author": {"name": "Dean Peters"},
            "homepage": "https://github.com/deanpeters/Product-Manager-Skills",
            "repository": "https://github.com/deanpeters/Product-Manager-Skills",
            "license": "CC-BY-NC-SA-4.0",
            "keywords": ["product-management", "pm", bname] + list(bundle["motions"]),
        }
        with open(os.path.join(dest, ".claude-plugin", "plugin.json"), "w", encoding="utf-8") as fh:
            json.dump(manifest, fh, indent=2)
            fh.write("\n")
        with open(os.path.join(dest, "README.md"), "w", encoding="utf-8") as fh:
            fh.write(bundle_readme(bname, bundle, core, version))
        entries[pname] = {
            "name": pname,
            "source": f"./plugins/{pname}",
            "description": desc,
            "category": "lifecycle-bundle",
            "tags": ["pm", "bundle", bname] + list(bundle["motions"]),
        }
    top = os.path.join(out_dir, "README.md")
    with open(top, "w", encoding="utf-8") as fh:
        fh.write(
            "# plugins/\n\n**Generated. Do not edit.** Each folder is one installable bundle, built from the "
            "`bundles:` mapping in `pm-skills.config.yaml` by `scripts/build-plugins.py`. "
            "The source of truth is `skills/`.\n\n"
            + "\n".join(f"- [`{plugin_name(b)}`]({plugin_name(b)}/README.md): {d['summary']}" for b, d in cfg["bundles"].items())
            + "\n"
        )
    return entries


def upsert_marketplace(entries: dict[str, dict]) -> str:
    with open(MARKET, encoding="utf-8") as fh:
        market = json.load(fh)
    keep = [p for p in market["plugins"] if p.get("category") != "lifecycle-bundle"]
    # bundle entries go right after the all-in-one entry, before per-skill entries
    idx = next((i for i, p in enumerate(keep) if p["name"] == "product-manager-skills"), -1) + 1
    market["plugins"] = keep[:idx] + list(entries.values()) + keep[idx:]
    return json.dumps(market, indent=2) + "\n"


def trees_equal(a: str, b: str) -> list[str]:
    diffs: list[str] = []

    def walk(cmp: filecmp.dircmp, prefix: str = "") -> None:
        diffs.extend(f"only in generated: {prefix}{n}" for n in cmp.left_only)
        diffs.extend(f"only on disk: {prefix}{n}" for n in cmp.right_only)
        diffs.extend(f"differs: {prefix}{n}" for n in cmp.diff_files)
        for sub, c in cmp.subdirs.items():
            walk(c, f"{prefix}{sub}/")

    walk(filecmp.dircmp(a, b))
    return diffs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    cfg = yaml.safe_load(open(CONFIG, encoding="utf-8"))
    version = json.load(open(ROOT_PLUGIN, encoding="utf-8")).get("version", "0.0.0")

    if args.check:
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            gen = os.path.join(tmp, "plugins")
            os.makedirs(gen)
            entries = build(gen, cfg, version)
            problems = trees_equal(gen, OUT) if os.path.isdir(OUT) else ["plugins/ is missing"]
            if upsert_marketplace(entries) != open(MARKET, encoding="utf-8").read():
                problems.append("marketplace.json bundle entries are stale")
        if problems:
            print("Plugins are stale. Run: python3 scripts/build-plugins.py", file=sys.stderr)
            for p in problems[:20]:
                print(f"  - {p}", file=sys.stderr)
            return 1
        print(f"Plugins OK: {len(cfg['bundles'])} bundles match pm-skills.config.yaml.")
        return 0

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    entries = build(OUT, cfg, version)
    updated = upsert_marketplace(entries)  # read before opening the file for writing
    with open(MARKET, "w", encoding="utf-8") as fh:
        fh.write(updated)
    print(f"Built {len(entries)} bundle plugins into plugins/ and updated marketplace.json.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
