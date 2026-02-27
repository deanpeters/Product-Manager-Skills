# v0.5 Release Announcement (Feb 27, 2026) — Streamlit (beta)

## Post Metadata

- **Post Title:** Product Manager Skills v0.5 — Streamlit (beta) Playground
- **Post Subtitle:** Local skill test-driving with safer key handling, provider/model choice, and clearer workflow execution.
- **Opening (first 160 chars):** v0.5 now includes Streamlit (beta): run skills locally with Anthropic/OpenAI/Ollama support, explicit workflow phases, and feedback-first iteration.
- **Primary Link:** [Product Manager Skills repo](https://github.com/deanpeters/Product-Manager-Skills)

---

## Short Promotional Post

v0.5 now includes **Streamlit (beta)**.

You can now test-drive PM skills locally before installing them into your preferred agent workflow.

What shipped:
- Local playground in `app/main.py`
- Provider/model selection (Anthropic, OpenAI, Ollama)
- Environment-variable-only key handling
- Workflow UX fixes so phase-based skills (like PRD) run clearly phase by phase

This is a feature in flight. Feedback is welcome:
- [GitHub Issues](https://github.com/deanpeters/Product-Manager-Skills/issues)
- [Dean on LinkedIn](https://linkedin.com/in/deanpeters)

Release: [Product Manager Skills v0.5](https://github.com/deanpeters/Product-Manager-Skills)

---

## Long-Form Draft

### Title
Product Manager Skills v0.5: Launching the Streamlit (beta) Playground

### Subtitle
Why we built a local testing surface for skills, and what changed to make workflow runs less confusing

### Article Body

v0.5 adds a new **Streamlit (beta)** playground to this repo.

The goal is simple: reduce the friction between "I found a skill" and "I know how this behaves in my context."

Instead of jumping directly into a production agent flow, you can now run skills locally in a guided interface and quickly validate quality, structure, and fit.

What changed in this beta:

1. **Local UI for skill discovery and execution**
   - Browse by theme
   - Run component, interactive, and workflow skills
   - Keep context and outputs visible while iterating

2. **Multi-provider and model selection**
   - Anthropic, OpenAI, and Ollama paths supported
   - Fast/capable model options so you can trade off cost vs depth intentionally

3. **Safer API defaults**
   - Environment-variable key handling only
   - Setup instructions in-app
   - No in-app key entry surface

4. **Workflow UX fixes**
   - Better phase detection for phase-driven skills like `prd-development`
   - Explicit controls to run one phase or all phases
   - Persisted per-phase outputs so "completion" actually maps to generated content

This is intentionally marked **beta**. It is a feature in flight, and we expect to improve it quickly from real usage.

If something feels unclear or broken, we want that feedback early:
- [GitHub Issues](https://github.com/deanpeters/Product-Manager-Skills/issues)
- [LinkedIn](https://linkedin.com/in/deanpeters)
