# Using PM Skills with Codex

Codex can apply these skills directly from your repo files. There are two practical paths:
- Local workspace (Codex in your coding environment)
- Codex on ChatGPT (`chatgpt.com/codex`) with GitHub connected
- Skills marketplace install via `npx skills`

If you want a quick local rehearsal before using Codex directly, try the Streamlit (beta) playground:

```bash
pip install -r app/requirements.txt
streamlit run app/main.py
```

---

## Option 1: Local Workspace (Fastest)

1. Open this repo in your Codex workspace.
2. Pick a skill file at `skills/<skill-name>/SKILL.md`.
3. Prompt Codex with the explicit file path.

Example:

```text
Using the skill at skills/prd-development/SKILL.md, create a PRD for a mobile onboarding redesign. Ask up to 3 clarifying questions first, then proceed.
```

### How to Apply Skill Types

- **Component skills**: ask for a specific artifact (for example, user story, positioning statement, epic hypothesis).
- **Interactive skills**: expect 3-5 adaptive questions, then numbered recommendations.
- **Workflow skills**: ask Codex to outline phases, then execute one phase at a time.

### Chain Multiple Skills

```text
First use skills/problem-framing-canvas/SKILL.md to define the problem. Then apply skills/user-story/SKILL.md to write stories for the chosen solution.
```

---

## Option 2: Codex on ChatGPT (GitHub-Connected)

Codex on ChatGPT works against connected repos. No ZIP upload flow is required.
Availability can vary by plan and rollout region.

1. Open [Codex](https://chatgpt.com/codex).
2. Connect GitHub when prompted (or via ChatGPT settings).
3. Select this repo and branch.
4. Prompt Codex to use a specific skill path, for example:

```text
Use skills/finance-based-pricing-advisor/SKILL.md to evaluate whether we should test a 10% price increase. Show assumptions and risks.
```

### Practical Prompt Pattern

Use this structure to keep outputs consistent:

```text
Using skills/<skill-name>/SKILL.md:
1) Ask up to 3 clarifying questions.
2) Follow the skill sections exactly.
3) Show output in markdown.
4) End with risks, assumptions, and next steps.
```

---

## Option 3: Install from skills.sh (No Local Clone Required)

If you prefer marketplace-style installation, use the Skills CLI.

Discover first:

```bash
npx skills find product management
npx skills add deanpeters/Product-Manager-Skills --list
```

Install for Codex:

```bash
npx skills add deanpeters/Product-Manager-Skills --skill <skill-name> -a codex -g
```

Examples:

```bash
npx skills add deanpeters/Product-Manager-Skills --skill user-story -a codex -g
npx skills add deanpeters/Product-Manager-Skills --skill prd-development -a codex -g
npx skills add deanpeters/Product-Manager-Skills --skill finance-based-pricing-advisor -a codex -g
```

Equivalent GitHub URL form (also supported on skills.sh pages):

```bash
npx skills add https://github.com/deanpeters/Product-Manager-Skills --skill <skill-name>
```

Show installed skills for Codex:

```bash
npx skills list -a codex
```

### Pairing with Repo Utilities (Recommended)

If you have the repo locally, use the built-in discovery utility first, then install with `npx skills`:

```bash
./scripts/find-a-skill.sh --keyword pricing --type interactive
npx skills add deanpeters/Product-Manager-Skills --skill finance-based-pricing-advisor -a codex -g
```

This gives you better local filtering before install.

### Discover Skills Without Cloning

If you do not want to clone this repo:

1. Search marketplace skills:
   ```bash
   npx skills find pricing
   ```
2. List available skills in this repo:
   ```bash
   npx skills add deanpeters/Product-Manager-Skills --list
   ```
3. Install the one you want:
   ```bash
   npx skills add deanpeters/Product-Manager-Skills --skill <skill-name> -a codex -g
   ```

You can also browse on [skills.sh](https://skills.sh/) and copy the command from each skill page.

---

## Troubleshooting

- **Codex cannot find the file**: confirm repo/branch selection and exact case-sensitive path.
- **Output is generic**: provide real constraints (stage, KPI target, customer segment, timeline).
- **Format drift**: explicitly instruct Codex to follow `Purpose, Key Concepts, Application, Examples, Common Pitfalls, References`.

---

## Official References

- [Codex in ChatGPT](https://openai.com/index/introducing-codex/)
- [Getting started with Codex](https://help.openai.com/en/articles/11096431-getting-started-with-codex)
- [Apps in ChatGPT (GitHub connection)](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt/)
- [Skills homepage](https://skills.sh/)
- [Skills CLI docs](https://skills.sh/docs/cli)
