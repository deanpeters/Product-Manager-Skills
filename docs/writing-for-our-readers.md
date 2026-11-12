# Writing for Our Readers

How to write documentation in this repo so nobody gets left behind.

Our readers range from product managers who have never opened GitHub to engineers who wire skills into agent pipelines. Most are somewhere in between. Every reader-facing doc has to work for the least technical person who will open it, without slowing down the most technical one.

Read this before you write or change a README, an install guide, a "Using PM Skills with…" guide, or anything else a non-maintainer might open.

**What this guide covers, and what it doesn't.** This guide is for *docs*. Skill bodies (`skills/*/SKILL.md`) have their own required sections and protected teaching content. For those, follow the skill anatomy in [CONTRIBUTING.md](../CONTRIBUTING.md). Where the two overlap (plain language, defining terms, real examples), they agree.

---

## Why This Matters Here

This library has two jobs in equal measure: equip AI agents to do PM work well, and help product managers get better at their craft and *send the ladder down* to others. Docs carry the second job as much as skills do. A PM who can't get past the install page never gets to the lesson.

So every doc follows the library's governing principle, **ABC: Always Be Coaching.** A Practitioner should leave the first screen with a result *and* a little more understanding than they arrived with. Getting the result fast doesn't mean dropping the explanation.

---

## Our Three Readers

| | The Practitioner | The Adopter | The Builder |
|---|---|---|---|
| **Who** | A PM or product leader who found this on GitHub, LinkedIn, Substack, or the podcast. No engineering background. | A PM or product ops person who uses AI every day and likes to tinker. | A maintainer, contributor, or engineer, plus the AI agents working in the repo. |
| **Has used** | Claude (desktop app or claude.ai) or ChatGPT for chat. Has never installed a skill. May never have opened GitHub. | Has installed a skill, custom GPT, or plugin. Can download a file from GitHub. May use Claude Code, Cowork, or Codex but doesn't code. | Git, a terminal, Claude Code or Codex, YAML, Python scripts. |
| **Wants** | A useful result this week, on a real problem, and to understand the framework well enough to explain it to someone else. | To set up a pack or the full library for their team and adapt it. | To change, test, and ship skills without breaking the library's teaching or its conventions. |
| **Gets lost at** | "Clone the repo", "run this in your terminal", "install the plugin", any unexplained term. | Choices with no recommendation, missing trade-offs, unclear file locations. | Vague steps, missing side effects, facts repeated in several places that drift apart. |
| **Main docs** | Top of `README.md`, `START_HERE.md`, `dist/README.md`, `docs/INSTALL-CLAUDE-DESKTOP.md`, `docs/Using PM Skills 101.md` | `README.md` install sections, `dist/packages/`, `skills/*/SKILL.md`, `docs/INSTALL-CLAUDE-CODE.md`, `docs/INSTALL-CODEX.md`, the "Using PM Skills with…" guides, the Streamlit playground | `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md`, the dated handoff briefs (`DDMMMYY.md`), `docs/RELEASE-PACKAGING.md`, `docs/maintenance/`, `app/STREAMLIT_INTERFACE.md` |

AI agents read our docs too. Write Builder docs so an agent can follow them literally.

---

## The Core Rule: Layer, Don't Split

Don't write a "simple version" and an "advanced version" that drift apart. Write one doc in layers, with the least technical reader first:

1. **What you get.** The outcome, in PM language, plus one line on *why* the framework works.
2. **The fastest way to try it.** One path, no choices, about five minutes.
3. **Other ways to use it.** Options for other tools, with a recommendation.
4. **Reference.** What's inside, how it works, full lists.
5. **For contributors.** Setup, scripts, rules. Link out to Builder docs rather than repeating them.

**The first screen belongs to the Practitioner.** Someone who reads only the first screen should be able to get a real result with one download, or with none. Badges, banners, and release notes come after that path, not before it.

A Builder-only doc (handoff briefs, maintenance plans, release packaging) can skip layers 1 to 3. Say who it's for in its first line, and link Practitioners to where they should be instead.

---

## Writing for the Practitioner

**Lead with the outcome, not the mechanism.** Write "Turn a vague feature request into a problem statement your team can test", not "This skill implements the problem-framing canvas."

**Teach one thing on the way.** A sentence of *why* ("framing the problem before the solution stops teams from building the wrong thing well") is what turns a download into a skill the reader keeps. Keep it to a sentence or two. Don't let it become a lecture.

**Give one path first.** Offer a single recommended route before any options. Choices come after the reader's first success.

**Write numbered steps, one action each.** Name the exact menu, button, or field, in bold: **Settings → Capabilities → Skills**. Say what the reader should see when the step works.

**Use direct download links.** Link to the file itself, not to a folder. A folder link drops the reader into GitHub's file browser.
- A pack: `https://github.com/deanpeters/Product-Manager-Skills/releases/latest/download/<pack>.zip`
- One skill: `https://github.com/deanpeters/Product-Manager-Skills/raw/main/dist/<skill-name>.zip`

**Keep terminal commands out.** No command lines in Practitioner sections. If a step really needs one, move it to a section labeled for Claude Code or terminal users. (Claude Code's `/plugin` commands count as terminal commands for this rule.)

**Say what not to do where it matters.** "Upload the skill ZIP. Don't unzip it first." "Unzip the pack first. Claude won't accept the pack itself." Readers who don't know the rules break them by guessing.

**Give a prompt to paste.** Every "try it" moment includes a real prompt with `[ ]` placeholders and invented details. Every skill's `## Input` section already has an `Example invocation`. Reuse it rather than inventing a new one. Readers copy prompts; they rarely invent them.

**Give a time estimate.** "About five minutes." "About 15 minutes." It tells readers the step is safe to start now. Skills carry an `estimated_time` you can quote.

**Tell them they can arrive empty-handed.** Every interactive skill will walk the reader through what they don't have (see [Guided Context Capture](guided-context-capture.md)). Say so. It removes the fear of "doing it wrong."

**Explain framework terms on first use.** Name the framework and its author, then say in a phrase what it does. "Jobs to Be Done (Clayton Christensen's idea that customers 'hire' a product to make progress)". The same goes for our own vocabulary: component, interactive, and workflow skills; entry modes; packs.

### Swap or explain these words

| Instead of | Write | Or explain once as |
|---|---|---|
| repo, repository | this project on GitHub | |
| clone | download | |
| skill | | a set of instructions that teaches Claude how to do one piece of PM work with you, and explains why it works |
| component / interactive / workflow skill | | one artifact (like a user story) / a guided conversation that asks a few questions, then recommends / a multi-step process that strings several together |
| plugin | | a package that installs many skills at once (Claude Code only) |
| ZIP, pack | | a single file that holds one skill. A pack holds several skill ZIPs. |
| run the skill, invoke | start a chat and ask for the work | |
| frontmatter, YAML, SKILL.md | (leave out of Practitioner text) | |
| CLI, terminal, shell | (leave out, or move to a Builder section) | |
| commit, push, branch, PR | (Builder docs only) | |

### Name the tool exactly

Readers mix these up, and so do we. Use the exact name, and don't call one by another's name.

| Name | What it is | How skills get in |
|---|---|---|
| **claude.ai** | Claude in a web browser | **Settings → Capabilities → Skills**, upload a skill ZIP |
| **Claude desktop app** | Claude as an app on Mac or Windows. It has chat, Cowork, and Code tabs. | Same **Settings → Capabilities → Skills** path as claude.ai |
| **Claude Code** | Claude working inside a folder on your computer, in the desktop app's Code tab or a terminal | The plugin marketplace (recommended), or skill folders in `~/.claude/skills/`. See [INSTALL-CLAUDE-CODE.md](INSTALL-CLAUDE-CODE.md) |
| **Claude Cowork** | Claude doing longer tasks on your files, in the desktop app | See [Using PM Skills with Claude Cowork](Using%20PM%20Skills%20with%20Claude%20Cowork.md) |
| **Codex** | OpenAI's coding agent | The Codex package (`pm-skills-codex.zip`). See [INSTALL-CODEX.md](INSTALL-CODEX.md) |
| **ChatGPT and other chats** | Other AI assistants | Upload or paste `SKILL.md` (and `template.md` when there is one) |
| **Streamlit playground** | A local app for trying skills before installing them | Builder setup with your own API key. See [app/STREAMLIT_INTERFACE.md](../app/STREAMLIT_INTERFACE.md) |

When a step only applies to one of these tools, put the tool's name in the heading.

---

## Writing for the Adopter

**Put options in a table with a recommendation.** For example, "I use… / Get this / Notes", with the recommended row first or marked.

**Explain trade-offs in one line each.** "The all-skills pack adds every skill to your list. Start with the starter pack, or the pack for the work in front of you, unless you need everything."

**Say where things live.** Name the folder and the file a reader will end up with: "you should now have `~/.claude/skills/prioritization-advisor/SKILL.md`."

**Show how to adapt safely.** If a reader might edit a template or a skill for their team, say which parts are safe to change (examples, wording, the domain) and which carry the lesson (Key Concepts, Common Pitfalls, the "why" behind each step). Changing the default entry mode, for example, is a one-line config change. See [Guided Context Capture](guided-context-capture.md#setting-the-default-entry-mode).

---

## Writing for the Builder

**Put commands in fenced `bash` blocks, one command per block** unless they must run together.

**State side effects before the command.** Anything that costs money, publishes, pushes, tags, or deletes. The Streamlit playground uses *your* provider API key, so say so before a reader launches it. Release commands push artifacts that other people download.

**Keep facts in one place and link to them.** Counts, sizes, versions, and rules live in one source file. Link to it rather than copying the number. Stale skill counts are the most common error in this repo. The README states the count in several places, and the drift checks don't cover prose. `catalog/` and `dist/CATALOG.md` are generated from `skills/`, so they're the place to point.

**Write rules an agent can follow literally.** Say "Run `bash scripts/validate-skills.sh`. Commit only if it exits 0." rather than "Make sure checks pass."

---

## House Style for Every Doc

- **Dashes:** no rule yet. Whether to limit em dashes is deferred to a future sweep, which will also decide its scope. Until then, match the style of the doc you're editing, and don't strip dashes from skill bodies: there, an em dash often carries a consequence chain or a teaching beat.
- Write short sentences in the second person and present tense.
- Make headings tasks or questions the reader has: "Start Here", "Which pack should I choose?"
- Use invented examples only. Never a real customer's name, people, products, quotes, or numbers. Use the repo's fictional universes: **Fieldlight** (B2B SaaS, field service), **Northfield Automation** (industrial), and **Brightwater Biologics** (life sciences, only where regulated work is the lesson). Use `example.invalid` for made-up URLs. The provenance rules in [CLAUDE.md](../CLAUDE.md) govern what can be cited.
- Keep it vendor-neutral. A doc can name a tool where a step really needs it, but it shouldn't read as an endorsement. See "Commercial Neutrality and Provider Boundaries" in [CONTRIBUTING.md](../CONTRIBUTING.md).
- Link text says where it goes: "[Draft a problem statement](...)", never "click here".
- Every doc that will go stale says when it was last checked, or links to the file that holds the live facts.

---

## Before You Publish: Checklist

- [ ] **First screen:** can a Practitioner get a real result from it with at most one download?
- [ ] **One path first:** is there a single recommended route before any options?
- [ ] **Coaching:** does the reader learn *why*, not just *how*, in a sentence or two?
- [ ] **Steps:** does every step name the exact button or menu, and say what success looks like?
- [ ] **Jargon:** is every term from the swap table replaced or explained, and every framework named and explained on first use?
- [ ] **Tool names:** is each tool named exactly (claude.ai, Claude desktop app, Claude Code, Cowork, Codex)?
- [ ] **Commands:** are terminal commands only in sections labeled for Claude Code or Builders?
- [ ] **Links:** do all links work, and do download links go to the file, not a folder?
- [ ] **Facts:** were counts, packs, and versions checked against the repo today, or linked rather than copied?
- [ ] **House style:** no real customer details, vendor-neutral?
- [ ] **Three reads:** have you read it once as each reader? Best of all, have a non-technical colleague try the first screen without your help, and watch where they stop.
