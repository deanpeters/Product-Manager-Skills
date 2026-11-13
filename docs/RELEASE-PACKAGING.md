# Release Packaging

This repo keeps `skills/` as the canonical source of truth and builds downloadable packages into `dist/`.

The release experience should feel simple:

```text
Download one pack. Unzip it. Upload the skill ZIPs inside. Start asking better product questions.
```

## `dist/` Is a Committed, Browsable Download Shelf

**Policy (intentional):** `dist/` is checked into the repo so anyone — including
non-technical PMs who never touch a terminal — can browse to
`https://github.com/deanpeters/Product-Manager-Skills/tree/main/dist`, read a
plain-language `README.md`, scan the `CATALOG.md`, and download a skill or a pack
directly. Making the library easy and educational to access is the point; hiding
the ZIPs behind the Releases tab worked against that.

The **tracked** layout (produced by `scripts/build-dist.sh`):

```text
dist/
  README.md              # plain-language landing page (renders on GitHub)
  CATALOG.md             # browsable catalog of every skill, by category
  <skill-name>.zip       # individual, upload-ready skill ZIPs (flat)
  packages/
    pm-skills-starter-pack.zip
    pm-determine-pack.zip      lifecycle bundles (generated from the config)
    pm-discover-pack.zip
    pm-define-pack.zip
    pm-develop-pack.zip
    pm-deliver-pack.zip
    pm-drive-pack.zip
    02-discovery-pack.zip      older themed packs, kept one release (superseded)
    03-strategy-pack.zip
    04-delivery-pack.zip
    05-ai-pm-pack.zip
    06-market-intel-pack.zip
    07-lifecycle-eol-pack.zip
    99-all-skills-pack.zip
    pm-skills-codex.zip
```

`README.md` and `CATALOG.md` are **generated from `skills/`**, so they never drift
from the source. Re-run `scripts/build-dist.sh` after adding or changing skills.

The intermediate build directories (`dist/claude-desktop/`, `dist/codex/`,
`dist/skill-zips/`, `dist/release/`, and the master `dist/*-release.zip`) remain
**git-ignored** — only the curated shelf above is committed.

GitHub Releases still exist and are still produced on `v*` tags; the committed
`dist/` shelf is a complement to them, not a replacement.

## Maintainer Flow

From the repo root:

```bash
./scripts/build-release.sh
git tag v0.78.0
git push origin v0.78.0
```

Pushing a version tag that starts with `v` triggers GitHub Actions to build artifacts and attach them to a GitHub Release.

## What Gets Built

```text
dist/
  claude-desktop/
    01-core-pm-starter-pack.zip
    pm-skills-starter-pack.zip
    pm-<bundle>-pack.zip       one per bundle in pm-skills.config.yaml
    02-discovery-pack.zip
    03-strategy-pack.zip
    04-delivery-pack.zip
    05-ai-pm-pack.zip
    06-market-intel-pack.zip
    99-all-skills-pack.zip

  skill-zips/
    <skill-name>.zip

  codex/
    .agents/
      skills/
        <skill-name>/
          SKILL.md
    AGENTS.md
    codex-product-manager-skills.zip

  release/
    claude-desktop/
    skill-zips/
    codex/
    docs/
    README.md

  Product-Manager-Skills-<version>-release.zip
```

## Scripts

Run validation only:

```bash
./scripts/validate-skills.sh
```

Build Claude Desktop/Web packs:

```bash
./scripts/build-claude-desktop-packs.sh
```

This also regenerates `dist/skill-zips/` because Claude packs are bundles of individual upload-ready skill ZIPs.

Build Codex package:

```bash
./scripts/build-codex-skills.sh
```

Build everything:

```bash
./scripts/build-release.sh
```

Check that the committed shelf still matches `skills/`:

```bash
python3 ./scripts/check-dist-freshness.py
```

## Why `check-dist-freshness.py` Exists

`check-library-drift.py` verifies `marketplace.json` and doc links. It does
**not** look at `catalog/` or `dist/` — so the library can pass CI completely
green while the browsable download shelf still advertises the previous release.
That is exactly what happened between v0.83 and v0.84, and it was caught by hand.

`check-dist-freshness.py` closes that hole. It verifies, content-level:

- `catalog/skills-index.yaml` — declared `count:` and full membership
- `dist/<skill>.zip` — one per skill, and no orphans left behind
- `dist/packages/` — every pack declared in `build-claude-desktop-packs.sh`
- `dist/CATALOG.md` — mentions every skill

**It runs as its own CI step, not inside `validate-skills.sh`.** `build-dist.sh`
calls `build-release.sh`, which calls `validate-skills.sh` — so a freshness check
living there would abort the very command you run to fix staleness. Keep it
separate.

Checks are content-level and never byte-level: rebuilt ZIPs differ on every run
because of embedded timestamps, so comparing archive bytes would fail constantly
and train everyone to ignore the check.

## Important Rules

- Do not edit files under `dist/` by hand — they are generated. Re-run `scripts/build-dist.sh` to refresh the committed shelf.
- The committed `dist/` shelf (README, CATALOG, skill ZIPs, `packages/`) **is** intentionally version-controlled; the intermediate build dirs are git-ignored. This is the "intentional policy change" the older rule referred to.
- Claude Desktop/Web packs are ZIPs of individual upload-ready skill ZIPs. Users unzip the pack first, then upload the skill ZIPs inside to Claude.
- Codex packages are expanded `.agents/skills` folders inside a ZIP, not ZIPs of ZIPs.
- Do not remove `.claude-plugin/marketplace.json`; Claude Code users rely on the marketplace path.
- After adding, renaming, or removing a skill, run `python3 scripts/generate-catalog.py` **and** `bash scripts/build-dist.sh`, then commit the result. CI enforces this via `check-dist-freshness.py`.
- Keep `skills/` stable and canonical.
- Prefer small Bash scripts and common Unix tools over a heavier build system.

## Install Docs

- Claude Desktop/Web: [`INSTALL-CLAUDE-DESKTOP.md`](INSTALL-CLAUDE-DESKTOP.md)
- Claude Code: [`INSTALL-CLAUDE-CODE.md`](INSTALL-CLAUDE-CODE.md)
- Codex: [`INSTALL-CODEX.md`](INSTALL-CODEX.md)

## Lifecycle bundles (v0.85)

The library is grouped into six bundles (Determine, Discover, Define, Develop, Deliver, Drive) plus Core, defined once in the `bundles:` section of `pm-skills.config.yaml` and checked by `scripts/check-bundles.py`. Three things are generated from that one mapping, so they cannot drift:

| Output | Built by | For |
|---|---|---|
| `plugins/pm-<bundle>/` + entries in `.claude-plugin/marketplace.json` | `scripts/build-plugins.py` | Claude Code plugin installs |
| `dist/packages/pm-<bundle>-pack.zip` | `scripts/build-claude-desktop-packs.sh` (via `scripts/bundle-skills.py`) | Claude Desktop/Web downloads |
| `catalog/skills-by-bundle.md`, `bundle`/`motion` in `skills-index.yaml` | `scripts/generate-catalog.py` | Browsing |

Every bundle carries the Core skills so facilitation links keep working when a bundle is installed alone. `skills/` is still the only place anyone edits. The older themed packs (`02`-`07`) stay on the shelf for one release, then are removed.

After changing a skill or the mapping: `python3 scripts/build-plugins.py`, `python3 scripts/generate-catalog.py`, `bash scripts/build-dist.sh`.
