# v0.78 — Release Packaging: One Download, Then Better PM Work

**Released:** April 26, 2026

---

## What We Added

v0.78 turns Product Manager Skills from a useful repo into something people can actually install without needing to understand the repo first.

We added release packaging for the main ways people use AI tools today:

- Claude Desktop/Web users can download ready-to-upload ZIP packs.
- Claude Code users can keep using the existing plugin marketplace path.
- Codex users can download a package with `.agents/skills` and `AGENTS.md`.
- Maintainers can build all release artifacts with one command.
- GitHub Actions can build and attach release files automatically on version tags.

The source of truth is still `skills/`. The new `dist/` output is just the shelf where release artifacts are assembled.

---

## Why We Added It

The skills were already useful. The installation story was still too technical.

That creates friction for the exact people this repo is meant to help: product managers who want better discovery, clearer strategy, stronger PRDs, better stories, and sharper prioritization, but who do not want to become packaging experts first.

The job to be done is:

> When a PM wants to use these skills with their AI tool, they need a simple way to get the right version installed so they can start doing better product work quickly.

This release removes setup guesswork. It makes the first step smaller.

---

## Who It Is For

### Nontechnical PMs using Claude Desktop or Claude Web

They can download `01-core-pm-starter-pack.zip`, upload it to Claude Skills, and start with a real product problem.

### Claude Code users

They can keep using the plugin marketplace. This release preserves that path instead of replacing it with ZIPs meant for a different product.

### Codex users

They can download `codex-product-manager-skills.zip`, unzip it into a repo, and get `.agents/skills` plus `AGENTS.md` in the right shape.

### Maintainers

They can run:

```bash
./scripts/build-release.sh
```

That validates skills, builds Claude packs, builds the Codex package, copies useful docs, and creates the master release ZIP.

---

## How It Makes Life Better

Before v0.78, someone had to understand the repo structure before they could use the repo well.

After v0.78:

- A PM can choose a starter pack instead of cloning a repo.
- A Claude user can upload one ZIP instead of packaging skills by hand.
- A Codex user can unzip one file instead of recreating `.agents/skills`.
- A maintainer can publish releases repeatably instead of assembling artifacts manually.
- The README tells people which path to use instead of making them infer it.

The release experience should now feel like:

```text
Download one pack. Upload or unzip one file. Start asking better product questions.
```

---

## What Changed in the Repo

- Added `scripts/validate-skills.sh`
- Added `scripts/build-claude-desktop-packs.sh`
- Added `scripts/build-codex-skills.sh`
- Added `scripts/build-release.sh`
- Added `.github/workflows/build-release.yml`
- Added install docs for Claude Desktop/Web, Claude Code, Codex, and maintainers
- Updated `README.md` with a clearer Start Here path
- Updated `AGENTS.md` with packaging guidance for Codex and coding agents

---

## Plain-English Blurb

Product Manager Skills v0.78 makes the library easier to install and share.

Instead of asking PMs to understand GitHub folders and packaging scripts, this release creates ready-made downloads for Claude Desktop/Web and Codex, keeps Claude Code marketplace support intact, and gives maintainers one command to build everything.

The point is simple: less setup, faster adoption, better product work.

---

*Release authored by Dean Peters with Codex.*
