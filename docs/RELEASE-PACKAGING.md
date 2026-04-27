# Release Packaging

This repo keeps `skills/` as the canonical source of truth and builds downloadable packages into `dist/`.

The release experience should feel simple:

```text
Download one pack. Upload or unzip one file. Start asking better product questions.
```

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
    02-discovery-pack.zip
    03-strategy-pack.zip
    04-delivery-pack.zip
    05-ai-pm-pack.zip
    99-all-skills-pack.zip

  codex/
    .agents/
      skills/
        <skill-name>/
          SKILL.md
    AGENTS.md
    codex-product-manager-skills.zip

  release/
    claude-desktop/
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

Build Codex package:

```bash
./scripts/build-codex-skills.sh
```

Build everything:

```bash
./scripts/build-release.sh
```

## Important Rules

- Do not edit files under `dist/` directly.
- Do not commit generated ZIP files unless the repo intentionally changes that policy.
- Do not remove `.claude-plugin/marketplace.json`; Claude Code users rely on the marketplace path.
- Keep `skills/` stable and canonical.
- Prefer small Bash scripts and common Unix tools over a heavier build system.

## Install Docs

- Claude Desktop/Web: [`INSTALL-CLAUDE-DESKTOP.md`](INSTALL-CLAUDE-DESKTOP.md)
- Claude Code: [`INSTALL-CLAUDE-CODE.md`](INSTALL-CLAUDE-CODE.md)
- Codex: [`INSTALL-CODEX.md`](INSTALL-CODEX.md)
