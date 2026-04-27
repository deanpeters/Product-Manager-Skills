# Repository Guidelines

## Operating Philosophy — Pedagogic and Practical in Equal Measure

As much as this repo is for adding skills to your agent, it's equally tasked to **help product managers become more awesome at their craft — and to help them send the ladder down to others.**

Skills here serve both goals simultaneously. The PM using a skill should finish knowing more than when they started — not just have a completed artifact. The reasoning embedded in a skill is what makes the output trustworthy, explainable, and transferable to the next person.

**ABC — Always Be Coaching** is a key governing principle.

This has direct implications for how you work in this repo as an agent:

- **Do not optimize for brevity at the cost of explanation.** Stripping learning scaffolding to tighten a skill is a defect, not an improvement.
- **Anti-patterns are load-bearing.** They teach the human what to watch for in the wild. Do not remove them.
- **Examples show reasoning, not just outputs.** A shorter example that hides the thinking is worse than a longer one that shows it.
- **The dual audience is always both:** the human PM building judgment and the AI agent executing the work. Never optimize for one at the expense of the other.

If you are making efficiency improvements, tighten fluff — not lessons. If you are unsure which is which, leave it in.

---

## Project Structure & Module Organization
- `skills/<skill-name>/SKILL.md` holds each skill. Skill folders use lowercase kebab-case names (e.g., `skills/user-story/SKILL.md`).
- `commands/<command-name>.md` holds reusable orchestration commands that chain local skills.
- `catalog/` holds generated indexes for fast browsing (`skills-by-type.md`, `commands.md`, and YAML indexes).
- `research/` contains reference essays that inform skills.
- `docs/` contains usage guides, including `docs/Using PM Skills with Codex.md`.
- `app/` contains the Streamlit (beta) playground (`app/main.py`) and setup docs (`app/STREAMLIT_INTERFACE.md`).
- `dist/` contains generated release artifacts. Do not edit generated files there directly.
- Root docs like `README.md`, `CONTRIBUTING.md`, `PLANS.md`, and `CLAUDE.md` explain catalog, contribution flow, and skill distillation.

## Build, Test, and Development Commands
This is a Markdown-first repository with lightweight validation and packaging scripts.
- `rg --files` lists all files quickly.
- `rg "SKILL.md"` finds skill definitions.
- `rg "skill-name"` verifies references before submitting.
- `./scripts/find-a-command.sh --list-all` lists available workflow commands.
- `./scripts/validate-skills.sh` validates canonical skill folders before packaging.
- `./scripts/build-release.sh` builds all downloadable release artifacts.
- `./scripts/test-library.sh` validates skills + commands and regenerates catalogs.
- `streamlit run app/main.py` launches the Streamlit (beta) skill playground.

## Coding Style & Naming Conventions
- Write in Markdown with clear headings and short paragraphs.
- Skills must follow the standard sections: Purpose, Key Concepts, Application, Examples, Common Pitfalls, References.
- Include frontmatter fields (`name`, `description`, `type`) at the top of each skill file.
- Keep `name` <= 64 characters and `description` <= 200 characters for Claude web upload compatibility.
- Ensure the skill folder name matches the frontmatter `name` exactly (lowercase kebab-case).
- Use fenced code blocks with language tags for commands or templates.
- Keep language concise and opinionated; avoid filler.

### Interactive Skills
**What:** Multi-turn conversational flows that gather context through sequential questioning and offer intelligent next-step recommendations.

**Characteristics:**
- Asks questions one at a time (or in small batches)
- Uses answers to inform subsequent questions
- Offers **enumerated, context-aware recommendations** for next steps
- Allows user to select by number ("1", "2 & 4") or provide custom input
- Adapts based on user choices

## Testing Guidelines
No automated tests exist. Validate changes by:
- Ensuring linked skill paths resolve (e.g., `skills/prd-development/SKILL.md`).
- Confirming examples and references are accurate and consistent.
- Skimming for structure compliance and readability.
- For Claude web upload, ensure frontmatter is valid YAML and use the packaging helper to generate `Skill.md` copies.

## Operating Principle (Dogfood First)
- Use this repo's own definitions, scripts, and standards before making structural decisions.
- If deciding skill type/category, anchor to local criteria in `README.md`, `CLAUDE.md`, and relevant `SKILL.md` files.
- Prefer proving decisions with repo tools (`scripts/find-a-skill.sh`, `scripts/test-a-skill.sh`, `scripts/check-skill-metadata.py`) over opinion.
- Treat `skills/` as the canonical source of truth for all packaging.
- Preserve compatibility with Claude Desktop/Web, Claude Code, and Codex.
- Prefer small, maintainable Bash scripts over complex build systems.
- Do not rename skills unless necessary.

## Cross-Repo Boundary
- This repository is the shared PM skills library, not the Productside playbook distribution repo.
- Productside playbook skill content must be created/edited in `/Users/deanpeters/Code/productside_playbook_skills`.
- When supporting Productside work, treat this repo as read-only reference/tooling unless explicitly asked to change this repo.

## Claude Custom Skills Compatibility
- Claude web uploads require `Skill.md` (case-sensitive). Use `scripts/package-claude-skills.sh`.
- Any scripts under a skill should be deterministic, avoid network calls, and be documented in the skill.
- Review skills and scripts for safety before sharing or running.
- Do not delete existing Claude Code marketplace files such as `.claude-plugin/marketplace.json`.

## Codex Skill Guidance
When users ask for product management help, inspect available skills before improvising. Prefer the most specific skill.

Relevant topics include:
- discovery
- Jobs to be Done
- personas
- product strategy
- prioritization
- roadmaps
- PRDs
- user stories
- acceptance criteria
- AI product management
- agent workflows
- stakeholder alignment

These are product management coaching and artifact-generation workflows, not software engineering workflows.

## Commit & Pull Request Guidelines
- Commit messages in history use the imperative voice with a clear subject (e.g., `Add agent-orchestration-advisor skill`), sometimes followed by an issue tag and an em dash for context.
- PRs should include a short summary, link relevant issues, and note skill type (component/interactive/workflow).
- If adding a new skill, update the catalog in `README.md` to keep counts and tables accurate.

## Release Checklist
- Update skill counts and tables in `README.md`.
- Ensure new skills are linked in the correct section (Component/Interactive/Workflow).
- Spot-check cross-links from `README.md` and `CONTRIBUTING.md`.
- Confirm any renamed skills update paths and references.
- If Streamlit beta changed, update `app/STREAMLIT_INTERFACE.md`, `app/.env.example`, and release notes in `README.md`/`docs/announcements/`.

## Skill Quality Expectations
- **Pedagogic first:** The PM using this skill should know more when they finish than when they started.
- Agent-ready, self-contained, and practical.
- Include at least one concrete example that shows reasoning, not just output.
- Include at least one explicit anti-pattern — this is not optional decoration.
- Define jargon on first use and keep tradeoffs explicit.
- Do not remove explanation, anti-patterns, or examples in the name of brevity. That is the mission, not the padding.
