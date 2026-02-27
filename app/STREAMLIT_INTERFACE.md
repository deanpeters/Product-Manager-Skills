# PM Skills Playground — Streamlit Interface (beta)

A local web app for browsing and test-driving PM skills against available LLM APIs before committing to installing them in Claude Code, Cowork, or Codex.

**Status:** Streamlit (beta). This is a new feature in flight and we are actively testing and refining it. Feedback is welcome via [GitHub Issues](https://github.com/deanpeters/Product-Manager-Skills/issues) or [LinkedIn](https://linkedin.com/in/deanpeters).

**Pedagogic goal:** Lower the barrier from "I've heard about this skill" to "I've seen it work in my context." Users pick a theme, read what they're getting into, then run the skill — with full multi-turn conversation for interactive skills, progress tracking, and an explicit bail path at every step.

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
| `type` | frontmatter | yes |
| `theme` | frontmatter | optional |
| `best_for` | frontmatter | optional |
| `scenarios` | frontmatter | optional |
| `estimated_time` | frontmatter | optional |
| `sections` | parsed from `##` headings | derived |
| `purpose_short` | first paragraph of Purpose section | derived |
| `has_examples` | presence of `examples/` subdir | derived |

### Four Screens

```
Home (theme browser)
  └─ Theme (skill cards)
       └─ Skill Detail (preview + scenario input)
            └─ Session (run the skill)
```

Navigation is state-based (`st.session_state.view`). The `nav()` helper handles all transitions and resets session state cleanly on each move.

### Session Types

**Component skills** (single-shot):
- User enters scenario → one API call → artifact rendered as markdown
- "Try a different scenario" returns to Skill Detail

**Interactive skills** (multi-turn chat):
- Pre-flight info box shown before session starts (sets expectations, names the bail path)
- First user message auto-sent on session start; Claude opens with the skill's Step 0
- Progress indicator parses `Q1/3` / `Context Q2/3` / `Step N of M` patterns from assistant messages
- `st.chat_input` for freeform responses; typing `done`, `bail`, `exit`, or `quit` ends the session gracefully
- Sidebar always shows: **↩ Start over** · **← Different skill** · **🏠 Home**

**Workflow skills** (phase-based):
- Phase headings auto-detected from `### Phase N` patterns in the Application section
- Phase radio selector lets users jump to any phase
- Each phase: enter context → Run → output → Re-run or Continue to next phase

### System Prompt

Each session uses the full `SKILL.md` body as the system prompt, with a short facilitation addendum for interactive skills:

```python
def build_system_prompt(skill):
    # Full skill body + (for interactive) facilitation rules:
    # - One question at a time
    # - Show Q1/3-style progress labels
    # - Stay true to the skill's structure
```

---

## Adding Theme Metadata to a Skill

Skills appear in the themed browser only if they have a `theme` field in their frontmatter. All other skills appear in an "All other skills" expander on the Home screen.

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

**Validation:** Adding these fields does not break `scripts/check-skill-metadata.py` — the validator only checks required fields (`name`, `description`, `type`) and ignores unknown keys.

**Currently tagged:** 16 skills across all 7 themes (2 per theme minimum, 4 in Career & Leadership). Remaining 30 skills can be tagged in follow-on passes using the same frontmatter pattern.

---

## UX Design Decisions

**Theme-first, not type-first.** Users come with a job to be done ("I'm preparing for a Director interview"), not a skill type ("I want an interactive skill"). Themes map to situations; type badges (🧱 🔄 🎭) set expectations about the interaction.

**Pre-flight for interactive and workflow skills.** Before starting a multi-turn session, the user sees what they're getting into: estimated time, what the conversation will produce, and where the bail controls are. Component skills go straight to the output — they're single-shot.

**Bail is always visible.** During a session, the sidebar always shows Start over, Different skill, and Home. These reset state cleanly without losing the skill selection context. Typing `done` or `bail` in chat also exits gracefully.

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
- **Export conversation** — download a session as markdown
- **Theme metadata for remaining 30 skills** — follow-on tagging pass
- **Search** — keyword search across skill names, descriptions, and best_for bullets
