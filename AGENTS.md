# Repository Guidelines

## Project Structure & Module Organization
- `skills/<skill-name>/SKILL.md` holds each skill. Skill folders use lowercase kebab-case names (e.g., `skills/user-story/SKILL.md`).
- `research/` contains reference essays that inform skills.
- `docs/` contains usage guides, including `docs/Using PM Skills with Codex.md`.
- `app/` contains the Streamlit (beta) playground (`app/main.py`) and setup docs (`app/STREAMLIT_INTERFACE.md`).
- Root docs like `README.md`, `CONTRIBUTING.md`, `PLANS.md`, and `CLAUDE.md` explain catalog, contribution flow, and skill distillation.

## Build, Test, and Development Commands
This is a Markdown-first repository with no build system or automated tests.
- `rg --files` lists all files quickly.
- `rg "SKILL.md"` finds skill definitions.
- `rg "skill-name"` verifies references before submitting.
- `streamlit run app/main.py` launches the Streamlit (beta) skill playground.

## Coding Style & Naming Conventions
- Write in Markdown with clear headings and short paragraphs.
- Skills must follow the standard sections: Purpose, Key Concepts, Application, Examples, Common Pitfalls, References.
- Include frontmatter fields (`name`, `description`, `type`) at the top of each skill file.
- Keep `name` <= 64 characters and `description` <= 200 characters for Claude web upload compatibility.
- Ensure the skill folder name matches the frontmatter `name` exactly (lowercase kebab-case).
- Use fenced code blocks with language tags for commands or templates.
- Keep language concise and opinionated; avoid filler.

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

## Claude Custom Skills Compatibility
- Claude web uploads require `Skill.md` (case-sensitive). Use `scripts/package-claude-skills.sh`.
- Any scripts under a skill should be deterministic, avoid network calls, and be documented in the skill.
- Review skills and scripts for safety before sharing or running.

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
- Agent-ready, self-contained, and practical.
- Include at least one concrete example and one explicit anti-pattern.
- Define jargon on first use and keep tradeoffs explicit.
