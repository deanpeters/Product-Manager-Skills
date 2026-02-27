# Using PM Skills with Claude

This repo is a library of PM skill files designed for AI agents. Claude Code (CLI) and Claude Cowork (workspace) can both read these files and apply them as structured instructions.

For quick local experimentation before running in Claude, you can also use the Streamlit (beta) playground:

```bash
pip install -r app/requirements.txt
streamlit run app/main.py
```

---

## With Claude Code (CLI)

Claude Code is Anthropic's official command-line interface for Claude. It reads files from your local filesystem and can apply skills directly.

### Quick Start

1. **Clone this repo** to your local machine:
   ```bash
   git clone https://github.com/deanpeters/Product-Manager-Skills.git
   cd product-manager-skills
   ```

2. **Navigate to the repo directory** in your terminal:
   ```bash
   cd product-manager-skills
   ```

3. **Invoke Claude Code** with a skill reference:
   ```bash
   claude "Using the skill at skills/prd-development/SKILL.md, create a PRD for our mobile onboarding redesign"
   ```

### How to Apply Skills

**Component skills** (templates/artifacts):
```bash
claude "Using skills/user-story/SKILL.md, write user stories for a checkout flow"
```

**Interactive skills** (guided discovery):
```bash
claude "Use skills/prioritization-advisor/SKILL.md to help me choose a prioritization framework"
```
Claude will ask 3-5 adaptive questions, then offer numbered recommendations. Answer with:
- A single number: `"2"`
- Multiple selections: `"1 & 3"`
- Custom input: `"I want to focus on retention metrics specifically"`

**Workflow skills** (end-to-end processes):
```bash
claude "Run skills/discovery-process/SKILL.md for our enterprise customer churn problem"
```
These orchestrate multiple phases. Claude will outline the process, then execute phase by phase.

### Working with Multiple Skills

Chain skills explicitly:
```bash
claude "First use skills/problem-framing-canvas/SKILL.md to define the problem. Then apply skills/opportunity-solution-tree/SKILL.md to map solutions."
```

### Installing Skills Globally (Optional)

You can install skills in Claude's global skills directory for access from any project:

1. **Copy skills to Claude's directory**:
   ```bash
   mkdir -p ~/.claude/skills
   cp -r skills/* ~/.claude/skills/
   ```

2. **Invoke without file paths**:
   ```bash
   claude "Use the user-story skill to write stories for checkout"
   ```

Claude will automatically find skills in `~/.claude/skills/`.

### Installing via skills.sh (Optional)

If you prefer marketplace-style install, you can discover and install without cloning this repo.

1. **Search the marketplace**:
   ```bash
   npx skills find product management
   ```

2. **List skills in this repo**:
   ```bash
   npx skills add deanpeters/Product-Manager-Skills --list
   ```

3. **Install directly for Claude Code**:
   ```bash
   npx skills add deanpeters/Product-Manager-Skills --skill user-story -a claude-code -g
   ```

4. **Confirm what is installed for Claude Code**:
   ```bash
   npx skills list -a claude-code
   ```

5. **Use in Claude Code**:
   ```bash
   claude "Use the user-story skill to write stories for checkout"
   ```

If you are on an older CLI that does not support `--agent`, install first, then copy manually:

```bash
npx skills add deanpeters/Product-Manager-Skills@user-story
mkdir -p ~/.claude/skills
cp -R ~/.codex/skills/user-story ~/.claude/skills/
```

Alternative install syntax (also shown on skills.sh pages):
   ```bash
   npx skills add deanpeters/Product-Manager-Skills@user-story
   ```

<a id="github-zip-install"></a>
### Installing from GitHub ZIP (Claude Desktop or Claude Web)

Custom skills are uploaded manually. Claude does not continuously sync skills from a GitHub repo URL.

The Claude Skills UI expects each uploaded skill to include a `Skill.md` file (case-sensitive). This repo stores source files as `SKILL.md`, so package first.

1. **Download this repo from GitHub** (Code -> Download ZIP), then unzip it.
2. **Build upload-ready ZIP** for the skill you want:
   ```bash
   ./scripts/zip-a-skill.sh --skill user-story
   ```
   For one full category (for example component skills only):
   ```bash
   ./scripts/zip-a-skill.sh --type component --output dist/skill-zips
   ```
   For a curated starter pack:
   ```bash
   ./scripts/zip-a-skill.sh --preset core-pm --output dist/skill-zips
   ```
   For all skills at once:
   ```bash
   ./scripts/zip-a-skill.sh --all --output dist/skill-zips
   ```
3. **In Claude Desktop or Claude Web**:
   - Go to **Settings -> Capabilities -> Skills**
   - Click **Upload skill**
   - Select a ZIP file from `dist/skill-zips/`
4. **Enable the uploaded skill** and run a quick smoke test prompt.

`zip-a-skill.sh` runs `package-claude-skills.sh` internally, strips unsupported upload frontmatter keys (for example `type`), then zips packaged folders for upload.

### Advanced Option: MCP Integrations

If you want deeper tool/repo integrations (instead of ZIP upload workflows), use MCP. This is a separate setup path from custom skill uploads.

- Anthropic Help: [Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- Anthropic Docs: [Model Context Protocol (MCP)](https://docs.anthropic.com/en/docs/mcp)

### Tips for Claude Code

- **Be specific with context**: Supply goals, constraints, target users, and relevant background
- **Reference file paths explicitly** when skills aren't globally installed
- **Use multi-turn flows**: Interactive skills work best in conversational mode
- **Combine skills**: Workflow skills often reference component and interactive skills automatically

### Troubleshooting

**Claude says it cannot find a file**:
- Verify you're in the `product-manager-skills` directory
- Check the file path is correct (case-sensitive)
- Use `ls skills/` to confirm skill names

**Output is too generic**:
- Provide more specific constraints and examples
- Ask Claude to ask clarifying questions first
- Reference the "Examples" section of the skill explicitly

**Claude doesn't follow the skill format**:
- Remind it: "Follow the skill structure: Purpose, Key Concepts, Application, Examples, Common Pitfalls"

---

## With Claude Cowork (Workspace)

Claude Cowork is Anthropic's workspace integration (similar to Cursor, Windsurf, etc.). It can load skills as persistent knowledge modules.

### Quick Start

1. **Open the repo in Cowork**:
   - File → Open Workspace
   - Select `product-manager-skills` folder

2. **Reference skills naturally**:
   ```
   Using the PRD Development skill, create a PRD for our mobile feature
   ```

3. **Cowork will automatically find** `skills/prd-development/SKILL.md` and apply it.

### How Skills Work in Cowork

**Component skills** — Request specific artifacts:
```
Use the positioning-statement skill to define our positioning for enterprise customers
```

**Interactive skills** — Conversational flows:
```
Run the prioritization-advisor skill. I need help choosing a framework.
```
Cowork will ask adaptive questions inline, offering numbered options. Respond in chat:
- `2` (select option 2)
- `1 & 4` (select multiple)
- `Tell me more about option 3` (ask for details)

**Workflow skills** — Multi-phase processes:
```
Start the discovery-process workflow for our B2B customer retention problem
```
Cowork will outline phases and execute step-by-step, prompting for input at decision points.

### Loading Skills as Knowledge Modules

For persistent access across sessions:

1. **Add skills to Cowork's knowledge base**:
   - Settings → Knowledge Modules
   - Add Folder: `product-manager-skills/skills`

2. **Skills become globally available**:
   ```
   Use the epic-breakdown-advisor skill
   ```
   No need to specify file paths.

### Working with Multiple Skills

Cowork understands skill dependencies. When you invoke a workflow skill, it automatically references related component and interactive skills:

```
Run the product-strategy-session workflow
```

Cowork will:
1. Use `positioning-workshop` (interactive)
2. Apply `problem-statement` (component)
3. Reference `jobs-to-be-done` (component)
4. Orchestrate `roadmap-planning` (workflow)

### Tips for Cowork

- **Skills persist across sessions**: Once loaded, Cowork remembers skill formats
- **Reference by name**: Just say "Use the [skill-name] skill" — Cowork finds the file
- **Natural language works**: You don't need exact file paths
- **Combine skills implicitly**: Workflow skills auto-orchestrate related skills
- **Ask for examples**: "Show me an example from the skill first"

### Troubleshooting

**Cowork doesn't recognize a skill**:
- Verify the workspace includes the `product-manager-skills` folder
- Check Settings → Knowledge Modules to confirm skills are loaded
- Try using the full path: `skills/user-story/SKILL.md`

**Output doesn't match the skill format**:
- Say: "Follow the [skill-name] skill structure exactly"
- Reference specific sections: "Use the Application section from the skill"

**Interactive skill skips questions**:
- Explicitly request: "Ask me the discovery questions first, one at a time"

---

## Comparison: Claude Code vs. Cowork

| Feature | Claude Code (CLI) | Claude Cowork (Workspace) |
|---------|------------------|---------------------------|
| **Access** | Command-line terminal | IDE/editor integration |
| **Skill Loading** | Explicit file paths or global install | Automatic workspace scanning |
| **Multi-turn flows** | Conversational in terminal | Inline chat with code context |
| **Best for** | Standalone PM work, quick artifacts | Integrated development, context-aware work |
| **Skill chaining** | Explicit ("First X, then Y") | Implicit (workflows auto-orchestrate) |

---

## General Best Practices (Both Tools)

### 1. **Start with Context**
Before invoking a skill, provide:
- Goal: What you're trying to accomplish
- Constraints: Time, resources, data availability
- Audience: Who will use the output
- Background: Relevant product/user context

Example:
```
Context: We're a B2B SaaS product with 50 enterprise customers. Churn is 15% annually.
I need to run discovery interviews to understand why.

Use the discovery-interview-prep skill to plan 5 customer interviews over 2 weeks.
```

### 2. **Know Your Skill Types**
- **Component** (10-30 min): Single artifact (user story, positioning statement, epic)
- **Interactive** (30-90 min): Guided discovery with adaptive questions
- **Workflow** (days/weeks): End-to-end process (discovery cycle, PRD development, roadmap planning)

### 3. **Let Interactive Skills Drive**
Don't skip the questions. Interactive skills ask 3-5 questions to gather context, then offer smart recommendations. Answer honestly—the quality of recommendations depends on accurate input.

### 4. **Chain Skills Explicitly (or Let Workflows Do It)**
For custom flows:
```
First use problem-framing-canvas, then opportunity-solution-tree, then pol-probe-advisor
```

For standard processes:
```
Run the discovery-process workflow
```
(It handles the chaining automatically.)

### 5. **Iterate on Outputs**
Skills produce drafts. Refine them:
```
This positioning statement is close, but too feature-focused. Rewrite emphasizing business outcomes.
```

### 6. **Reference Examples**
Every skill includes real-world examples. Ask to see them:
```
Show me the "good" and "bad" examples from the user-story skill before we start
```

---

## Skill Categories Quick Reference

### Component Skills (16)
Templates for specific deliverables. Use when you need a standard artifact.

**Examples**: `user-story`, `positioning-statement`, `epic-hypothesis`, `problem-statement`, `pol-probe`

### Interactive Skills (14)
Guided discovery flows. Use when you need help deciding approach or gathering context.

**Examples**: `prioritization-advisor`, `epic-breakdown-advisor`, `context-engineering-advisor`, `pol-probe-advisor`, `agent-orchestration-advisor`

### Workflow Skills (4)
End-to-end processes. Use when running a complete PM cycle.

**Examples**: `discovery-process`, `prd-development`, `roadmap-planning`, `product-strategy-session`

---

## Need Help?

- **README**: See the main [README.md](../README.md) for full skill catalog
- **Skill Structure**: Each skill has Purpose, Key Concepts, Application, Examples, Common Pitfalls, References
- **CLAUDE.md**: See [CLAUDE.md](../CLAUDE.md) for skill design philosophy
- **Issues**: Report problems at [GitHub Issues](https://github.com/deanpeters/Product-Manager-Skills/issues)

---

**Ready to use Claude with PM skills?** Pick a skill from the catalog and start with a clear goal and context. Claude will guide you through the rest.
