# PM Skills Playground — Streamlit Interface (beta)

A local web app for **learning PM Skills setup/integration**, **finding the right skill for a situation**, and **test-driving PM skills** against available LLM APIs.

**Status:** Streamlit (beta). This is a new feature in flight and we are actively testing and refining it. Feedback is welcome via [GitHub Issues](https://github.com/deanpeters/Product-Manager-Skills/issues) or [LinkedIn](https://linkedin.com/in/deanpeters).

**Pedagogic goal:** Lower the barrier from "I've heard about this skill" to "I've seen it work in my context." The app now supports three paths:
- **Learn** for setup and integration guidance
- **Find My Skill** for situation-to-skill recommendation
- **Run Skills** for worked examples and live testing

---

## Running Locally

```bash
# From the repo root
pip install -r app/requirements.txt
streamlit run app/main.py
```

**API keys:** Environment variable only. Set one or more provider keys in `app/.env` (copy `app/.env.example`) or export them in your shell before launch.

**Providers + models:** The sidebar auto-detects available providers from env setup, shows an API setup warning/instructions if none are found, and lets users choose provider + model per session.

```bash
cp app/.env.example app/.env
# Edit app/.env and add one or more keys (plus optional defaults)

# Example:
# ANTHROPIC_API_KEY=sk-ant-...
# ANTHROPIC_MODEL=claude-sonnet-4-6
# ANTHROPIC_MODELS=claude-haiku-4-5-20251001,claude-sonnet-4-6
# OPENAI_API_KEY=sk-...
# OPENAI_MODEL=gpt-4o-mini
# OPENAI_MODELS=gpt-4o-mini,gpt-4o
# OLLAMA_ENABLED=1
# OLLAMA_BASE_URL=http://localhost:11434
# OLLAMA_MODEL=qwen2.5:latest
# OLLAMA_MODELS=qwen2.5:latest,llama3.2:latest
```

**Built-in fast/capable defaults:**
- `anthropic`: `claude-haiku-4-5-20251001` (fast), `claude-sonnet-4-6` (capable)
- `openai`: `gpt-4o-mini` (fast), `gpt-4o` (capable)
- `ollama`: `qwen2.5:latest` (fast), `llama3.2:latest` (capable)

---

## Architecture

### File Structure

```
app/
  main.py                   # Single-file Streamlit app
  requirements.txt          # streamlit, anthropic, openai, pyyaml, python-dotenv
  .env.example              # Multi-provider API key + model template
  .env                      # Your local env vars (gitignored)
  STREAMLIT_INTERFACE.md    # This file
```

### How Skills Are Loaded

`load_skills()` walks `skills/*/SKILL.md`, parses YAML frontmatter, and extracts `##` sections into a dict. All skill content is cached with `@st.cache_data` — changes to skill files require a cache clear or app restart.

Parsed fields per skill:

| Field | Source | Required |
|-------|--------|----------|
| `name` | frontmatter | yes |
| `description` | frontmatter | yes |
| `intent` | frontmatter | yes |
| `type` | frontmatter | yes |
| `theme` | frontmatter | optional |
| `best_for` | frontmatter | optional |
| `scenarios` | frontmatter | optional |
| `estimated_time` | frontmatter | optional |
| `sections` | parsed from `##` headings | derived |
| `purpose_short` | first paragraph of Purpose section | derived |
| `has_examples` | presence of `examples/` subdir | derived |

### Navigation Model

```
Home (mode chooser)
  ├─ Learn Hub (docs-driven onboarding and platform guides)
  │    └─ Guide Detail (renders markdown guide files from docs/)
  ├─ Find My Skill
  │    └─ Ranked skill suggestions (situation → metadata-based matches)
  └─ Run Skills (learning simulator)
       ├─ Skill + Context Input
       │    └─ Worked Example Output
       │         ├─ Filled Template / Form
       │         └─ Steps and Transformations
       └─ Advanced Browser (optional)
            └─ Theme (skill cards)
                 └─ Skill Detail (preview + scenario input)
                      └─ Session (run the skill)
```

Navigation is state-based (`st.session_state.view`). The `nav()` helper handles transitions and resets session artifacts when switching contexts.

### Find My Skill

**What it does:**
- Takes a plain-language description of the user's situation
- Ranks matching skills using trigger-oriented metadata
- Shows why a skill matched, plus `best_for` and `scenarios`
- Sends users directly to preview or run a recommended skill

**Ranking signals used:**
- `name`
- `description`
- `best_for`
- `scenarios`
- `intent`
- `purpose_short`

This mode is intentionally aligned with the repo's stronger trigger metadata standard and the CLI's `find-a-skill.sh --mode trigger` behavior.

### Session Types

**Learning simulator** (default Run Skills flow):
- User chooses a skill + context (preset or custom) and clicks **Run the Skill Steps**
- One API call runs the selected skill end-to-end internally (no follow-up questioning)
- Output is rendered as:
  - **Filled Template / Form** (worked example artifact)
  - **Steps and Transformations** (what changed at each step)
  - **Assumptions Made** (explicit gaps the model filled)

**Advanced sessions** (optional manual mode):
- Available under the "Need the older advanced browser?" expander in Run Skills
- Preserves previous behavior for component, interactive, and workflow session testing

**Interactive skills in advanced mode** (multi-turn chat):
- Pre-flight info box shown before session starts (sets expectations, names the bail path)
- "What to bring" expander on every skill detail page renders the skill's own `## Input` section (v0.81+) — shows what context sharpens the session while making explicit that arriving empty-handed is fine; the guided flow covers the gaps
- First user message auto-sent on session start; Claude opens with the skill's Step 0
- Progress indicator parses `Q1/3` / `Context Q2/3` / `Step N of M` patterns from assistant messages
- `st.chat_input` for freeform responses; typing `done`, `bail`, `exit`, or `quit` ends the session gracefully
- Sidebar always shows: **↩ Start over** · **← Different skill** · **🏠 Home**

**Workflow skills in advanced mode** (phase-based):
- Phase headings auto-detected from `### Phase N` patterns in the Application section
- Phase radio selector lets users jump to any phase
- Each phase: enter context → Run → output → Re-run or Continue to next phase

**Multi-Turn interactions**
**What:** Multi-turn conversational flows that gather context through sequential questioning and offer intelligent next-step recommendations.
**Characteristics:**
- Asks questions one at a time (or in small batches)
- Uses answers to inform subsequent questions
- Offers **enumerated, context-aware recommendations** for next steps
- Allows user to select by number ("1", "2 & 4") or provide custom input
- Adapts based on user choices


### System Prompt

The learning simulator uses the full `SKILL.md` body plus instructions to run the workflow internally without follow-up questions:

```python
def build_learning_simulator_system_prompt(skill):
    # Full skill body + simulation instructions:
    # - run end-to-end internally
    # - no follow-up questions
    # - include assumptions explicitly
```

Advanced sessions keep the existing behavior, including the interactive facilitation addendum:

```python
def build_system_prompt(skill):
    # Full skill body + (for interactive) facilitation rules:
    # - One question at a time
    # - Show Q1/3-style progress labels
    # - Stay true to the skill's structure
```

---

## Lifecycle Bundles (how the browser groups skills)

The browser groups skills by **lifecycle bundle**: Determine, Discover, Define, Develop, Deliver, Drive, and Core. The grouping is not stored in the skill files. `app/main.py` reads the `bundles:` and `core:` sections of `pm-skills.config.yaml` (the same mapping that builds the Claude Code plugins and the download packs) and:

- builds the home cards and the Skill Finder's filter from the bundles,
- shows each bundle's skills grouped under their **motions** (for example Define → De-risk, Differentiate),
- shows a "Coming" note for a motion that has no skills yet (a gap the config records),
- overrides a skill's frontmatter `theme` with its bundle. If the config is missing or unreadable, the app falls back to the old `theme` frontmatter below.

To move a skill between bundles, edit the config (then run `python3 scripts/check-bundles.py`). Don't edit the app.

## Adding Theme Metadata to a Skill (legacy fallback)

Used only when `pm-skills.config.yaml` has no `bundles:` section. Skills appear in the themed browser only if they have a `theme` field in their frontmatter. All other skills appear in an "All other skills" expander on the Home screen.

**Add these optional fields to `SKILL.md` frontmatter:**

```yaml
---
name: your-skill-name
description: "..."
type: component|interactive|workflow
theme: career-leadership          # one of the 7 theme slugs below
best_for:
  - "Plain-language use case (shown as bullet in skill card)"
  - "Another use case"
  - "Third use case"
scenarios:
  - "Pre-built scenario the user can one-click load"
  - "Another scenario"
estimated_time: "10-15 min"
---
```

**The 7 theme slugs:**

| Slug | Display Name |
|------|-------------|
| `career-leadership` | Career & Leadership |
| `discovery-research` | Discovery & Research |
| `strategy-positioning` | Strategy & Positioning |
| `pm-artifacts` | Writing PM Artifacts |
| `finance-metrics` | Finance & Metrics |
| `ai-agents` | AI & Agents |
| `workshops-facilitation` | Workshops & Facilitation |

**Validation:** Adding these fields does not break `scripts/check-skill-metadata.py` as long as required fields are present. The validator now checks required fields (`name`, `description`, `intent`, `type`) and ignores other unknown keys.

**Currently tagged:** 16 skills across all 7 themes (2 per theme minimum, 4 in Career & Leadership). Remaining 30 skills can be tagged in follow-on passes using the same frontmatter pattern.

---

## UX Design Decisions

**Mode-first for clarity.** The app now separates **Learn** (how to install/use/integrate), **Find My Skill** (discover the right skill from a situation), and **Run Skills** (execute skills with models). This reduces first-time confusion and keeps docs as source of truth.

**Context-first inside Run Skills.** Users now get the shortest path to learning output: pick a skill, add context, run once, and inspect both artifact and transformation path.

**Advanced mode stays available.** The older themed browser and manual session flows are still available when users want multi-turn interaction or phase-by-phase control.

**Learning output structure is fixed.** The simulator asks for consistent sections so users always see:
1. Filled Template/Form
2. Steps and Transformations
3. Assumptions Made

**Learn + Practice in one flow.** The Learn hub includes starter “Run this skill” actions so onboarding and execution are connected, not separate products.

**Situation-first discovery.** Users rarely think in skill names. The finder uses trigger-oriented metadata so people can describe the problem in normal language and still reach the right skill.

**Progress from the skill itself.** Interactive skills built on the facilitation protocol already emit `Q1/3`-style progress labels. The app parses these rather than maintaining a separate step counter, so progress tracking is automatically correct as skills are updated.

**Scenario chips as scaffolding.** Pre-built scenarios lower the blank-canvas anxiety of a new user. They're stored in the skill's frontmatter, not hardcoded in the app — adding scenarios to a skill automatically makes them available in the playground.

---

## Deployment (Streamlit Community Cloud)

The app can be deployed, but it uses environment-variable key loading only and supports multiple providers.

**Option A: Shared key with usage limits**
- Set one or more provider secrets (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`) or enable local Ollama (`OLLAMA_ENABLED=1` and `OLLAMA_BASE_URL`).
- Optionally set default and available models (`ANTHROPIC_MODEL`, `OPENAI_MODEL`, `OLLAMA_MODEL`, and `*_MODELS` lists).
- Add rate limiting (e.g., max tokens per session) to avoid runaway costs.
- Not yet implemented.

**Option B: Private deployment**
- Keep the app internal and control access to the hosted environment.
- Recommended if you do not want to expose a shared API key-backed endpoint publicly.

**To deploy:**
1. Fork or push this repo to GitHub
2. Connect to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Set main file to `app/main.py`
4. Set Python version to 3.11+

---

## Known Limitations

- **Cache refresh:** Skill changes require restarting the app or clearing Streamlit's cache (`st.cache_data.clear()`). During active skill development, run with `streamlit run app/main.py --server.fileWatcherType poll` to auto-reload.
- **30 unthemed skills:** Skills without a `theme` tag appear in an expander on Home. See [Adding Theme Metadata](#adding-theme-metadata-to-a-skill) to promote them into themed cards.
- **No streaming:** API responses render all at once after completion. Streaming would improve perceived responsiveness for long outputs — a future enhancement.
- **Workflow phase detection:** Phases are auto-detected from `### Phase N` headings in the Application section. Workflow skills without this naming convention show as a single "Full workflow" phase.

---

## Future Enhancements

- **Streaming responses** for lower perceived latency
- **Shared hosted key** option with session-level rate limiting for public demos
- **Related skills panel** — surface cross-references from the skill's References section
- **Export worked example** — download simulator output as markdown
- **Theme metadata for remaining 30 skills** — follow-on tagging pass
- **Finder polish** — richer ranking explanations, recent searches, and saved recommendation paths
