# CLAUDE.md — Skill Distillation Protocol

**Purpose:** Instructions for Claude on how to collaborate with Dean to convert raw PM content into formalized skills for this repository.

---

## Project Status (Last updated: Fri Nov 13 2026)

### Current State: v0.86 (95 skills), released Nov 13, 2026

**Nov 12, 2026 session (unreleased, on main). Handoff brief: `12NOV26.md`**
- **Guided Context Capture:** `skills/workshop-facilitation/SKILL.md` upgraded (Known/Assumed/Missing/Conflicting read-back, completion summary before generating, `(Recommended)` decision ladder, ranked Assumptions to Validate, replay-on-correction, resume recap). Explainer: `docs/guided-context-capture.md`. Skills **link** to the rulebook; never copy its text
- **Configurable default entry mode:** `pm-skills.config.yaml` (`default_entry_mode` + per-skill `overrides`; ships `guided`, `incoming-request-advisor: context-dump`). 33 skills carry one `**Default entry mode:**` line so lone ZIPs know their default. `scripts/apply-entry-mode.py` applies it; `--check` runs in `validate-skills.sh`. User's in-session choice always wins
- **Docs guide:** `docs/writing-for-our-readers.md` (Practitioner / Adopter / Builder; layer, don't split; first screen belongs to the Practitioner). Em-dash rule deliberately deferred
- **Shipped in v0.86 (Nov 13):** the 12 skills added after v0.85 (Dig, Decode, Drumbeat, Delineate, Deepen), the docs readability pass (README first screen, `START_HERE.md`, Desktop install, `scripts/check-docs-style.py`), and the retirement of older packs 02-07. Release note: `docs/announcements/2026-11-13-v0-86-the-everyday-work-of-product.md`

**Nov 13, 2026 session (unreleased, on main): lifecycle bundles**
- **Five lifecycle bundles + Drive + Core**, all D-named: **Determine** (Context) → **Discover** → **Define** → **Develop** (the build) → **Deliver**; **Drive** (stakeholders + career) runs under all five; **Core** (facilitation, navigator, investigation, authoring) ships inside every bundle. Each bundle has D-named **motions** (e.g. Define → De-risk, Differentiate; Deliver → Debut, Dollars, Demand, Dashboard, Decommission). Aligned with the Productside Blueprint / SDLC / ADLC arc
- **The mapping is the source of truth:** `bundles:` + `core:` in `pm-skills.config.yaml`, one home per skill, validated by `scripts/check-bundles.py` (in `validate-skills.sh`). **`skills/` is NOT reorganized** (it is load-bearing: ~25 files reference the path). Everything else is generated from the mapping
- **Generated from it:** `plugins/pm-<bundle>/` + bundle entries in `marketplace.json` (`scripts/build-plugins.py`, `--check` in `validate-skills.sh`; cross-bundle links rewritten to absolute URLs in the copies only); `dist/packages/pm-<bundle>-pack.zip` (`bundle-skills.py` → pack builder); `catalog/skills-by-bundle.md`; the Streamlit browser groups by bundle and motion; the navigator skill's map (`check-bundles.py --write-navigator`)
- **New skill `pm-skills-navigator`** (Interactive, Core): "what's on my desk" → phase by evidence (validated vs assumed) → route. Library at **95**. Real install verified end to end (`/plugin install pm-define@pm-skills`)
- **GTM gap-fill (Nov 13):** `launch-plan` (Workflow, Debut: tiers, four dates, go/no-go, scorecard, premortem) and `launch-metrics` (Component, Dashboard: leading/lagging, triggers, 30/90/180 reviews). Debut now also holds `message-house` (Component), `sales-value-narrative` (Component; hands the card to `battle-card-builder`) and `buying-journey-enablement` (Workflow). Debut is complete. **Discover gained two motions (Nov 13):** Dig (`survey-design-advisor`, `usage-data-investigation`, `discovery-habits-advisor`) and Decode (`research-synthesis`, `assumption-mapping`). **Develop gained a Drumbeat motion (Nov 13):** `backlog-refinement-advisor`, `sprint-planning`, `release-readiness`. **Drive gained a Delineate motion:** `decision-rights-matrix`, `pm-role-charter`. **Deliver gained a Deepen motion:** `activation-design`, `retention-diagnostic-advisor`. Gaps closed (Nov 13); remaining ideas: reconcile duplicate frameworks (Porter's, Ansoff, Lean UX) across repos, more Discover/Develop depth. Other gaps: execution rituals, governance/decision rights, post-launch growth
- Older themed packs `02`-`07` stay on the shelf one release, then retire. `LICENSING.md` added (answers issue #27); OpenCode install guide added (PR #20 closed with credit)


**95 Skills**
- 36 Component Skills (templates/artifacts + finance metrics + career frameworks + stakeholder tools + intelligence disciplines + EOL artifacts + lifecycle plays)
- 34 Interactive Skills (guided discovery + finance advisors + career advisors + growth + stakeholder engagement + intel triage + EOL readiness + lifecycle play triage)
- 25 Workflow Skills (end-to-end processes + meta skill-authoring + executive onboarding + company intel + market-intelligence investigations + EOL process)
- License: CC BY-NC-SA 4.0
- All skills restructured to Anthropic-compliant format (`skills/skill-name/SKILL.md`)
- **Metadata complete (Aug 10, 2026):** all 77 skills carry `theme`, `best_for`, `scenarios`, `estimated_time`. 13 themes; `validation-experiments` added for pol-probe / pol-probe-advisor / derisk-measurement-advisor / lean-ux-canvas / recommendation-canvas. Trigger audit passes library-wide with zero warnings
- **Fully adorned (Adornment Plan 4 COMPLETE, Aug 10, 2026):** every Component and Workflow skill ships `template.md` + two-domain worked examples. Three documented carve-outs: `finance-metrics-quickref` (definitionally SaaS, template only), `skill-authoring-workflow` (meta-skill, one example), `product-sense-interview-answer` (second example varies question type, not industry). Plan: `docs/maintenance/2026-08-10-adornment-plan-4.md`
- **Three example universes, each with a defined job:** **Fieldlight** (B2B SaaS, field service) · **Northfield Automation** (industrial retrofit controls — hardware, channel, long cycles) · **Brightwater Biologics** (life sciences, clinical trial operations, platform Trialpath — *evidence before revenue*). Brightwater is **scoped, not a general fallback**: use it only where regulated / evidence-driven / long-cycle work IS the lesson. Core artifacts keep an instantly legible second domain

**Lifecycle & End-of-Life Suite (COMPLETE — released as v0.84, Aug 10 2026)** ✅
- Release note: `docs/announcements/2026-08-10-v0-84-lifecycle-and-eol-suite.md`
- Suite summary: `docs/Lifecycle and EOL Suite Summary.md` · Handoff brief: `10AUG26.md`
- **`product-lifecycle` theme (2 skills, the upstream play decision):**
  [`lifecycle-play-advisor`](skills/lifecycle-play-advisor/SKILL.md) (Interactive) — 4 questions: product + trigger → seven **transition questions** (scored) → pressure source (demand / supply-cost / capability) → extension test. Recommends extend, replace, retire, harvest, or **"nothing yet"**. [`product-lifecycle-plays`](skills/product-lifecycle-plays/SKILL.md) (Component) — PLC strategy grid, three plays, **seven replacement hazards**, risk register with a contingency column ("what is Plan B?"), portfolio worksheet
- **`eol-transition` theme (6 skills, executing the retirement):**
  [`eol-readiness-advisor`](skills/eol-readiness-advisor/SKILL.md) (Interactive, go/no-go + 5 verdicts incl. Hold/Harvest/Extend) → [`eol-stakeholder-sequence`](skills/eol-stakeholder-sequence/SKILL.md) (Legal→Finance→Sales→Marketing→CS→difficult customers→Eng→Support) → [`eol-checklist`](skills/eol-checklist/SKILL.md) (phase-gated, 15 areas, owner per item) → [`eol-internal-enablement`](skills/eol-internal-enablement/SKILL.md) (FAQ, sales points, Acknowledge-Reframe-Offer objections, escalation ladder) → [`eol-message`](skills/eol-message/SKILL.md) (**upgraded**: Brief/Standard/Full, three transition paths) → [`eol-process`](skills/eol-process/SKILL.md) (Workflow, six phases incl. **Close**)
- **Two conventions that govern the suite — do not regress these:**
  1. **Right-sizing is a dial the user sets.** Every skill offers Level 1/2/3 (Light/Standard/Heavy), recommends one, honors an override in either direction, and names what a lighter level leaves uncovered. Level 2 is the default; **never default to Level 3**. Process theater on a small sunset teaches teams to ignore process on the big one
  2. **No tight coupling.** Every skill runs standalone; levels and gates are defined inline (duplicated text, not shared dependencies); `eol-process` is a **route, not a pipeline** with an "Entering Mid-Stream" diagnostic and explicit permission to go backwards. Do not introduce a handoff schema — carrying context means saying "Level 2" and pasting what you have
- **Lifecycle gates:** GA (a *state*, not a work phase) · NSC · EOS · EOE · EOR (*contract-driven, insert only when renewals run past EOS*) · EOM · EOL · EOSRV. Working checklists span NSC→EOSRV. `Not scheduled` + a recorded precondition beats an invented EOL date
- **Fully adorned, two interlocking universes:** Fieldlight Classic Dispatch (SaaS, Level 2, all six phases, closes at 94% retention vs. a 90% target) and Northfield Automation NFA-200 (industrial, Level 3, where Phase 2 sends the process back to Phase 1 and the outcome becomes End of Sale with **no EOL date**). The industrial thread is deliberately a *failure worked forward* — the play was right, the risk rating was wrong
- **Sources:** practitioner field material on lifecycle and end-of-life practice, plus the 5 EOL prompts in `product-manager-prompts`. Anonymization held — no client names and no details carried over from client artifacts; public-record failure cases (Kodak, Zune, Vista, Nest Revolv, AT&T POTS, Amgen) are business history from Dean's own deck

**Market Intelligence Suite (Phase 9, COMPLETE — released as v0.83, Jul 17 2026)** ✅
- Release note: `docs/announcements/2026-07-17-v0-83-market-intelligence-suite.md`
- ✅ **Wave 1 complete (Jul 16, 2026):** 6 new skills, `theme: market-intelligence`
  - [`autonomous-investigation`](skills/autonomous-investigation/SKILL.md) (Workflow) — protocol skill for research that proceeds without the user: question budget, search-plan gate, **Fact/Inference/Assumption** labels (canonical vocabulary), do-not-invent lists, Just Enough Mode, diffable schemas, confidence stacking, SCIP guardrails. The `workshop-facilitation` counterpart for investigation skills
  - [`intelligence-collection-disciplines`](skills/intelligence-collection-disciplines/SKILL.md) (Component) — eight intel disciplines (OSINT→MASINT + All-Source Fusion) with free/paid source tables, signal→inference chains, TAM/SAM/SOM recipe, fusion cadence, artifact mapping
  - The chain: [`market-landscape-scan`](skills/market-landscape-scan/SKILL.md) → [`competitive-research-snapshot`](skills/competitive-research-snapshot/SKILL.md) → [`competitive-intel-watch`](skills/competitive-intel-watch/SKILL.md) → [`battle-card-builder`](skills/battle-card-builder/SKILL.md) (all Workflow) — each consumes the prior's stable schema
- ✅ **Wave 2 complete (Jul 16, 2026):** [`competitive-analysis-process`](skills/competitive-analysis-process/SKILL.md) (Workflow) — six-step umbrella (landscape → product comparison → customer-need fulfillment → business baseline → perception/positioning → strategic direction) orchestrating the suite. Plus two upgrades: `tam-sam-som-calculator` gained three entry modes (own numbers / guided interview / autonomous research with the GEOINT/DEMOINT bottom-up recipe); `company-intel` gained the Executive Signal Refresh rerun pattern (Then/Now diffs, **Dropped Language** — what leaders stop saying), the source priority ladder + do-not-sanitize rule, product-org heuristics (CPO tenure, PM job postings as culture documents), and an optional distress read (presenting vs. underlying problem) — techniques generalized (and anonymized) from internal research tooling. Library at 63
- ✅ **Wave 3 complete (Jul 16, 2026):** 6 new Workflow skills — [`voice-of-customer-miner`](skills/voice-of-customer-miner/SKILL.md) (public-voice mining, need-themes, source-bias notes), [`pricing-packaging-tracker`](skills/pricing-packaging-tracker/SKILL.md) (diffable pricing time series; packaging moves before price), [`pestel-delta-monitor`](skills/pestel-delta-monitor/SKILL.md) (macro re-scan; broken assumptions are the output; pairs with `pestel-analysis`), [`swot-analysis`](skills/swot-analysis/SKILL.md) (evidence-cited quadrants + S-O/W-T crossings), [`porters-five-forces`](skills/porters-five-forces/SKILL.md) (rated forces with signals; AI substitution named; profit-pool close), [`ansoff-matrix`](skills/ansoff-matrix/SKILL.md) (evidence per quadrant; risk gradient; cross-referenced as the investigation sibling of `organic-growth-advisor`). Library at 69. Followed (Jul 17) by [`intel-discipline-advisor`](skills/intel-discipline-advisor/SKILL.md) (Interactive) — triage from decision to discipline mix + cadence + executing skill; the Component+Interactive pairing for the disciplines compendium. **Suite complete at 14 skills + 2 upgrades; library at 70**
- 🎁 **Adornment pass (Jul 17, post-release):** all 14 suite skills + `company-intel` now ship `template.md` (extracted output schemas with quality checks) + **dual-domain worked examples** — a SaaS universe (Fieldlight/Wrenchline/DispatchCrow/Vantiga, FSM software; chain examples feed each other) and an industrial universe (Northfield Automation investigating Helix/Corvid/Meridian, retrofit automation; interlocks with `company-intel`'s Foresight refresh example). New standard baked into this file's Quality Checklist ("Fully adorned"), CONTRIBUTING.md, AGENTS.md, Building PM Skills, both authoring meta-skills, and `build-a-skill.sh`. README/docs now surface the suite (nav block, v0.83 What's New, `docs/Market Intelligence Suite Summary.md`, `06-market-intel-pack`). Plan + status: `docs/maintenance/2026-07-17-adornment-and-docs-plan.md`; remaining: Plan 4 back-catalog backfill
- 🧹 **Also Jul 16:** `company-intel` examples fictionalized (real company names replaced with surrogates: Helix Motion Systems, Northfield Automation, Corvid Industrial, Brightwater Biologics) per the customer-anonymization protocol
- **Sources:** `~/Code/product-manager-prompts/market-intelligence/` (12 prompts) plus practitioner field material on competitive and market intelligence (all Dean's; see session memory for anonymization protocol — no customer names or recognizable engagement scenarios, ever)
- Free/paid two-column source tables are the sanctioned style for tool mentions

**Streamlit (beta) Playground (Feb 27, 2026)**
- Local app in `app/main.py` for browsing and running skills before install
- Environment-variable key handling (no in-app key entry), with provider/model selection
- Provider support: Anthropic, OpenAI, and Ollama
- Workflow UX improvements: phase detection, run-all phases, per-phase output tracking
- Feedback channels linked in-app: GitHub Issues + LinkedIn

**Phase 8: Career & Leadership Skills (COMPLETE)** ✅
- ✅ **4 Skills Released (Feb 27, 2026)** — distilled from two episodes of [The Product Porch](https://the-product-porch-43ca35c0.simplecast.com) podcast
  - [`altitude-horizon-framework`](skills/altitude-horizon-framework/SKILL.md) (Component) — PM→Director mental model: altitude/horizon axes, waiter-to-operator shift, four transition zones, Cascading Context Map. Based on [E42](https://the-product-porch-43ca35c0.simplecast.com/episodes/from-product-manager-to-director-how-to-make-the-shift-part-1)
  - [`director-readiness-advisor`](skills/director-readiness-advisor/SKILL.md) (Interactive) — Coaching across four situations: preparing, interviewing, newly landed, recalibrating. Based on E42
  - [`executive-onboarding-playbook`](skills/executive-onboarding-playbook/SKILL.md) (Workflow) — 30-60-90 day diagnostic playbook for VP/CPO transitions. Based on [E43](https://the-product-porch-43ca35c0.simplecast.com/episodes/becoming-a-vp-cpo-leading-product-at-the-executive-level-part-2)
  - [`vp-cpo-readiness-advisor`](skills/vp-cpo-readiness-advisor/SKILL.md) (Interactive) — Director→VP/CPO coaching; includes CEO interview framework. Based on E43
- **Source transcripts:** `research/product_porch_transcript.making-the-shift-from-pm-to-director-of-product.md` and `research/product_porch_transcript.becoming-a-vp-or-cpo-of-product-at-executive-level.md`
- **Potential follow-on:** VP/CPO→C-suite transition (separate skill set, not yet sourced)

**Phase 6: AI PM Orchestrator Skills (In Progress)**
- ✅ **Skill #34: agent-orchestration-advisor** (Interactive) — Complete
  - Guides multi-agent workflow design
  - Covers 4 dimensions: Multi-Agent Workflows, Cross-Functional AI Pods, Launch Control Tower, Strategic Intent Alignment
  - References context-engineering-advisor as prerequisite
- 📋 **Remaining Skills (Planned):**
  - `ai-product-evals` (Component) — Evaluation frameworks template
  - `ai-observability-framework` (Component) — Tracing and logging guide
  - `ai-maintenance-planning` (Component) — Model drift maintenance template
  - `ai-product-orchestrator` (Workflow) — Complete end-to-end AI PM process

**Phase 7: Finance for Product Managers (COMPLETE)** ✅
- ✅ **7 Skills Released (Feb 8, 2026)**
  - Foundation: 3 component skills covering 32 SaaS finance metrics
  - Decision Frameworks: 3 interactive advisors (feature, channel, pricing)
  - Advanced: 1 comprehensive business health diagnostic
  - Total: 4,290 lines across 7 skills
  - See `docs/Finance Suite Summary.md` for complete overview

**Recent Updates:**
- ✅ **v0.82 Released (Jul 8, 2026):** New inbound-communication skill + committed browsable `dist/` download shelf
  - Added [`incoming-request-advisor`](skills/incoming-request-advisor/SKILL.md) (Interactive, `theme: stakeholder-comms`) — decodes an incoming message (Slack ping, email, mandate, escalation, FYI) into a structured 12-section breakdown that separates the literal ask from the job-to-be-done and reads sender power/stake. Distilled from Dean's "Incoming Request Breakdown" prompt in the `product-manager-prompts` repo. Ships `SKILL.md` + `template.md` + `examples/`. Library now **56 skills** (23 Component, 26 Interactive, 7 Workflow)
  - `dist/` is now an **intentionally committed, browsable download shelf** at `github.com/deanpeters/Product-Manager-Skills/tree/main/dist` — plain-language `README.md` + `CATALOG.md` (both generated from `skills/`), 56 flat individual skill ZIPs, and `dist/packages/` (bundles + Codex). Regenerated by `scripts/build-dist.sh`; intermediate build dirs stay git-ignored. Policy documented in `docs/RELEASE-PACKAGING.md`. Built for non-technical PMs — do not revert to Releases-only
  - Release note: `docs/announcements/2026-07-08-v0-82-inbound-requests-and-dist-shelf.md`
- ✅ **v0.81 Released (Jul 4, 2026):** Required `## Input` section across all 55 skills + the `$ARGUMENTS` stance
  - Every skill now declares inputs in plain language: works-best-with, also-useful, inline-input rule (invocation context counts as answers already given — skip, don't re-ask), empty-handed fallback ("invitation, not gate"), and an example invocation
  - Skill anatomy is now: Purpose, **Input**, Key Concepts, Application, Examples, Common Pitfalls, References — enforced by `check-skill-metadata.py`; smoke checks warn on missing example invocation or empty-handed language
  - Bare `$ARGUMENTS` in skill bodies now fails validation — rationale (portability, pedagogy, unnecessary) documented in CONTRIBUTING.md "Why We Don't Use `$ARGUMENTS`"; `argument-hint` frontmatter is the sanctioned Claude Code autocomplete exception (53 skills)
  - Streamlit skill pages render the skill's own Input section in a "What to bring (all optional)" pre-flight expander
  - Added `workshop-facilitation/examples/inline-input-flow.md` — transcript of inline input skipping answered questions, with the re-asking anti-pattern
  - Restored `skills/agent-orchestration-advisor/` — the Phase 6 skill #34 had only ever existed on orphaned commit `a41415c` (never merged to main) while docs claimed it shipped; recovered and upgraded to current standards
  - Release note: `docs/announcements/2026-07-04-v0-81-input-sections.md`
- ✅ **organic-growth-advisor Added (May 17, 2026):** Interactive skill for McKinsey Growth Pyramid L2-L5 triage
  - 3-question flow diagnoses growth constraint via Growth Path Matrix (customer/market context × degree of product change)
  - Path-specific diagnostics, first experiments, and watch-outs for L2 (New Segments), L3 (New Geographies), L4 (New Distribution), L5 (New Products)
  - Source: McKinsey Growth Pyramid, applied through practitioner field material
- ✅ **v0.79 Released (May 15, 2026):** Community contributions — security hardening, new meta-skill, bug fix
  - Added `skills/pm-skill-creator/` — interactive skill for guided skill design (KNE-AI)
  - Added `.claude-plugin/plugin.json` — fixes silent skill discovery failure for Claude Code plugin users (changyan01, harley-chenhailin)
  - Added configurable input length guard to `scripts/run-pm.sh` via `PM_MAX_INPUT` env var, default 4000 (xiaolai)
  - Added adapter name allowlist and path traversal protection to `scripts/add-a-skill.sh` (xiaolai)
  - Release note: `docs/announcements/2026-05-15-v0-79-community-contributions.md`
- ✅ **v0.78 Released (Apr 26, 2026):** Added release packaging automation and clearer install paths
  - Added `scripts/validate-skills.sh`, `scripts/build-claude-desktop-packs.sh`, `scripts/build-codex-skills.sh`, and `scripts/build-release.sh`
  - Added Claude Desktop/Web ZIP packs for starter, discovery, strategy, delivery, AI PM, and all-skills use cases
  - Added Codex package output with `.agents/skills`, root `AGENTS.md`, and `codex-product-manager-skills.zip`
  - Added `.github/workflows/build-release.yml` to validate/build on PRs/main and publish assets on `v*` tags
  - Added install docs for Claude Desktop/Web, Claude Code, Codex, and release maintainers
  - Updated README with a clear Start Here path and release packaging explanation
  - Release note: `docs/announcements/2026-04-26-v0-78-release-packaging.md`
- ✅ **v0.75 Released (Mar 17, 2026):** Restored pedagogic-first philosophy across all governance docs
  - Added Design Philosophy section to `CLAUDE.md`, `CONTRIBUTING.md`, `AGENTS.md`, and `README.md`
  - ABC (Always Be Coaching) and "send the ladder down" named as governing principles throughout
  - Equal-footing framing: agent capability and human PM learning are co-equal goals, neither is a byproduct
  - Named the anti-pattern explicitly: efficiency edits that strip learning scaffolding are defects
  - Added pedagogic checklist item and negative content-removal check to `CONTRIBUTING.md`
  - Added naming conventions (no contributor handles/prefixes) to `CONTRIBUTING.md`
  - Named protected sections explicitly: "Why This Works," Anti-Patterns, consequence chains, educational preambles
  - Added note on external scoring tools optimizing for the wrong rubric
  - Claude Code plugin marketplace badge and coming-soon install snippet added to `README.md`
  - Release note: `docs/announcements/2026-03-17-v0-75-pedagogic-first.md`
- **Open PRs:** None — all resolved as of May 15, 2026
  - ✅ #1 KNE-AI — `pm-skill-creator` — merged; folder and frontmatter renamed to drop `kne-` prefix
  - ✅ #2 markphelps — Claude Code plugin marketplace (`marketplace.json`) — merged Mar 18, 2026
  - ✅ #3 popey — efficiency improvements — closed; stripped pedagogic content, does not meet contribution standards
  - ✅ #7 xiaolai — input length guard in `run-pm.sh` — merged with configurable `PM_MAX_INPUT` default
  - ✅ #8 xiaolai — adapter validation in `add-a-skill.sh` — merged as-is
- ✅ **v0.7 Released (Mar 9, 2026):** Tightened skill quality and discovery standards across the full library
  - Standardized trigger-oriented `description` language so skills more clearly answer "use this when..."
  - Added repo-standard `intent` frontmatter to preserve richer meaning without weakening trigger metadata
  - Added `scripts/check-skill-triggers.py` and wired trigger-readiness checks into `scripts/test-library.sh`
  - Added `find-a-skill.sh --mode trigger` so skill discovery can leverage `description`, `best_for`, and `scenarios`
  - Updated skill-authoring docs and templates so the stronger standard is maintained going forward
- ✅ **v0.5 Streamlit (beta) update (Feb 27, 2026):** Added local playground, multi-provider model selection, and workflow UX fixes for phase-based skills (notably PRD flow behavior)
- ✅ **v0.5 Released (Feb 27, 2026):** Added 4 Career & Leadership skills (Phase 8) distilled from The Product Porch podcast episodes on PM→Director and Director→VP/CPO transitions
- ✅ **v0.4 Released (Feb 10, 2026):** Fixed facilitation protocol regression and standardized guided interaction behavior
  - Root cause: brevity-focused rewriting could strip facilitation modality details from interactive flows
  - Resolution: established `skills/workshop-facilitation/SKILL.md` as source of truth and linked it across interactive and facilitation-heavy workflow skills
  - Added heads-up start, context-dump bypass, best-guess mode, progress labels, and interruption handling
  - Implemented by Codex after diagnosing expected-vs-actual facilitation mismatch
- ✅ **Phase 7 Complete:** 7 finance skills released (Feb 8, 2026)
- All skills alphabetically ordered within each category (Component, Interactive, Workflow)
- Enhanced documentation in `/docs`:
  - `Using PM Skills with Claude.md` — Comprehensive guide for Claude Code (CLI) and Claude Cowork (workspace)
  - `Using PM Skills with Codex.md` — Guide for OpenAI Codex
  - `Building PM Skills.md` — Contributor guide
  - `Finance Suite Summary.md` — Complete overview of 7 finance skills (NEW)
- Streamlit beta documentation in `/app`:
  - `app/STREAMLIT_INTERFACE.md` — App architecture, setup, and deployment notes
  - `app/.env.example` — Multi-provider key/model configuration template
- Updated `CONTRIBUTING.md` with enhanced guidelines
- Research documents added to `/research`:
  - `Context Engineering for Product Managers.md`
  - `The Product Manager as an Orchestrator.md`
  - `finance/` — 4 finance research documents (3,014 lines)

**Source Materials for Phase 6:**
- Dean's Substack articles:
  - "Vibe First, Validate Fast, Verify Fit" (PoL Probes)
  - "AI-First Is Cute. AI-Shaped Is Survival." (5 competencies)
  - "Context Stuffing Is Not Context Engineering"
- Teresa Torres: *Continuous Discovery Habits* (5 AI PM disciplines)
- Marty Cagan: *Empowered* (4 big risks in AI era)
- Productside Blueprint: Orchestration framework

**Source Materials for Phase 7 (Finance):**
- `research/finance/Finance for Product Managers.md` — 32 metrics with quizzes
- `research/finance/Finance_QuickRef.md` — One-page lookup table
- `research/finance/Finance_For_PMs.Putting_It_Together_Synthesis.md` — Decision frameworks
- `research/finance/Finance_Metrics_Additions_Reference.md` — Common mistakes reference

**What's Next:**
- Docs readability program (from `docs/writing-for-our-readers.md`): README first screen + `START_HERE.md` + install docs (`INSTALL-CLAUDE-DESKTOP.md` is missing packs 06/07; `START_HERE.md` still says "New in v0.65") → prose-count drift check → audit the ~25 "Using PM Skills with…" guides → optional docs style checker
- Future em-dash sweep (deferred Nov 12, 2026): decide whether to limit em dashes and in what scope. Skill bodies need special care; dashes there often carry teaching beats
- Complete remaining Phase 6 skills (evals, observability, maintenance)
- Build final workflow skill that orchestrates all 5 AI PM disciplines
- Potential Phase 8: Pricing & Monetization Suite (7 comprehensive pricing skills)
  - Value-based pricing framework
  - Willingness-to-pay research
  - Packaging architecture advisor
  - Pricing psychology guide
  - Price testing methodology
  - Competitive pricing analysis
  - Monetization model advisor

**Important Notes for Claude:**
- Always check `git status` and recent commits before starting new work
- For reader-facing docs (README, `START_HERE.md`, install guides, "Using PM Skills with…" guides, `dist/README.md`), follow `docs/writing-for-our-readers.md`: three readers (Practitioner / Adopter / Builder), layer don't split, the first screen belongs to the Practitioner
- Dogfood first: use this repo's own standards/scripts/skill definitions as the source of truth before making recommendations
- For facilitation behavior changes, update `skills/workshop-facilitation/SKILL.md` first, then use `docs/maintenance/facilitation-scope.md` to find and patch all linked skills
- For category decisions (Component vs Interactive vs Workflow), anchor to criteria in this file and `README.md` before giving an answer
- Prefer evidence from local tools (`scripts/find-a-skill.sh`, `scripts/test-a-skill.sh`, `scripts/check-skill-metadata.py`) over subjective preference
- Skills must follow standard anatomy: Purpose, Input, Key Concepts, Application, Examples, Common Pitfalls, References
- Interactive skills require 3-5 adaptive questions, enumerated options (3-5 choices), handle single/multi-selection
- All skills include YAML frontmatter: `name`, `description`, `intent`, `type`
- Cross-reference related skills in References section
- For Claude web custom skills: keep `name` <= 64 chars and `description` <= 200 chars, and ensure folder name matches `name`
- Claude web uploads require `Skill.md` (case-sensitive); use `scripts/package-claude-skills.sh`
- Scripts should be deterministic, avoid network calls, and be documented in the skill file
- If Streamlit beta behavior or provider support changes, update both `app/STREAMLIT_INTERFACE.md` and README release notes in the same PR

**Automation Tools:**
- **`scripts/add-a-skill.sh`** — Agent-agnostic utility for automated skill creation
  - Converts raw PM content into skills via 8-step workflow
  - Supports Claude Code, Manual mode (`--agent manual`), and custom adapters
  - Includes analysis, planning, generation, validation, and documentation steps
  - See `docs/Add-a-Skill Utility Guide.md` for complete guide
  - Use for semi-automated skill creation from research documents or workshop notes
- **`scripts/build-a-skill.sh`** — Interactive wizard for guided skill construction
  - Prompts section-by-section (Purpose → References)
  - Writes deterministic files (`SKILL.md` + optional examples/template)
  - Validates strict conformance before optional git staging
- **`scripts/find-a-skill.sh`** — Ranked skill discovery helper
  - Search by name, type, and keyword
  - Ranking priority: exact name > frontmatter > section text
- **`scripts/check-dist-freshness.py`** — Guards the committed `catalog/` and `dist/` shelf
  - Verifies catalog count+membership, one `dist/` ZIP per skill (no orphans), every declared pack, and `dist/CATALOG.md` coverage
  - **Content-level, never byte-level** — rebuilt ZIPs differ every run from embedded timestamps
  - Runs as its **own CI step**, NOT inside `validate-skills.sh`: `build-dist.sh` → `build-release.sh` → `validate-skills.sh`, so a check there would abort the command that fixes the staleness. Also step 7 of `test-library.sh`
  - Fix drift with: `python3 scripts/generate-catalog.py` then `bash scripts/build-dist.sh`
- **`scripts/apply-entry-mode.py`** — Applies `pm-skills.config.yaml`'s default entry mode to every protocol-running skill (or a packaged copy via `--skills-dir`); `--check` fails on drift, bad values, unknown overrides, or a skill that uses `workshop-facilitation` without the `**Default entry mode:**` line. Runs inside `validate-skills.sh` (safe there: its fix is itself, not a rebuild)
- **`scripts/check-bundles.py`** — Validates the bundle mapping (one home per skill, D-names, no motion named like its bundle, gaps recorded) and that the navigator's embedded map matches the config. `--write-navigator` regenerates it
- **`scripts/build-plugins.py`** — Generates `plugins/` and marketplace bundle entries from the mapping; `--check` fails on staleness. Fix drift: run it, then `generate-catalog.py` and `build-dist.sh`
- **`scripts/check-docs-style.py`** — Style guard for reader-facing docs (README, `START_HERE.md`, install guides, "Using PM Skills with…" guides). Hard failures: "click here" links, stale "New in vX" lines, stale pack names outside an older-packs context, menu paths in backticks instead of bold. Warnings only: jargon (repo, clone, terminal…) in the first 40 lines of Practitioner-facing files. Runs inside `validate-skills.sh`
- **`scripts/test-a-skill.sh`** — Skill quality gate
  - Runs strict conformance checks (`check-skill-metadata.py`)
  - Verifies linked `skills/*/SKILL.md` references resolve
  - Optional `--smoke` checks for section/readiness quality

---

## Design Philosophy — Pedagogic and Practical in Equal Measure

As much as this repo is for adding skills to your agent, it's equally tasked to **help product managers become more awesome at their craft — and to help them send the ladder down to others.**

Skills here serve both goals simultaneously. They equip AI agents to do PM work at a professional level, and they teach the human PM the *why* behind the framework — so they can explain it, adapt it, and pass it on. Neither goal is optional. Neither is more important than the other.

**ABC — Always Be Coaching** is a key governing principle. Every skill should leave the person using it knowing more than when they started. The same applies to how you work as an agent in this repo: coaching is not optional, it is the work.

This means:
- Explanation is load-bearing, not decorative
- Anti-patterns are as important as correct patterns
- Examples show reasoning, not just outputs
- Stripping learning scaffolding to tighten copy is a defect, not an improvement

The dual audience is always both: **the human PM building judgment** and **the AI agent executing the work.** Never optimize for one at the expense of the other.

---

## Your Role

You are Dean's **pedagogic collaborator and skill extraction partner**. Your job is to take messy, real-world PM content (prompts, flows, frameworks, workshop notes) and distill it into **clean, agent-ready skills that also teach the humans who use them**.

You are **not** a passive transcriber. You:
- Ask clarifying questions when the logic is ambiguous
- Identify missing pieces (prerequisites, failure modes, examples)
- Push back when structure is weak or tone drifts generic
- Push back when explanation is stripped in favor of brevity
- Suggest better frameworks when you see them
- Preserve the teaching in every edit — the lesson is the point

If you are using Codex to work with this repo, see `docs/Using PM Skills with Codex.md` for the recommended workflow.

---

## What Dean Will Provide

Dean will supply one or more of these:
- **Multi-turn prompt sequences** (e.g., a 5-step discovery interview flow)
- **Workshop frameworks** (e.g., roadmap planning canvas)
- **Decision trees** (e.g., "How to choose the right metric")
- **Real client artifacts** (anonymized PRDs, stakeholder maps, discovery notes)
- **Rough notes or transcripts** from sessions
- **Individual artifact templates** (user stories, positioning statements, epics)

Your job: **turn it into a skill.**

---

## Three Types of Skills

### Component Skills
**What:** Individual deliverables or artifacts (user stories, epics, positioning statements, PRD sections, OKRs, etc.)

**Characteristics:**
- Self-contained, reusable building blocks
- Simpler structure (still has steps, but fewer moving parts)
- Focuses on "how to create X well"
- Gets referenced by workflow skills

**Example:** `user-story.md` — how to write a proper user story with acceptance criteria

---

### Workflow Skills
**What:** Multi-step processes or frameworks (discovery interviews, roadmap planning, stakeholder analysis, etc.)

**Characteristics:**
- Orchestrates multiple activities
- Often references component skills
- Includes decision points and branching logic
- Focuses on "how to complete process Y"

**Example:** `roadmap-planning.md` — strategic roadmap development (which might reference epics, OKRs, and stakeholder mapping)

---

### Interactive Skills
**What:** Multi-turn conversational flows that gather context through sequential questioning and offer intelligent next-step recommendations.

**Characteristics:**
- Asks questions one at a time (or in small batches)
- Uses answers to inform subsequent questions
- Offers **enumerated, context-aware recommendations** for next steps
- Allows user to select by number ("1", "2 & 4") or provide custom input
- Adapts based on user choices

**Example:** `discovery-interview-prep.md` — guides user through prep by asking about customer segment, then objectives, then constraints, then offers 3-5 tailored interview approaches to choose from

**Interactive Pattern Structure:**

~~~
Step 1: Ask opening question(s)
↓
Step 2: Based on answer, ask follow-up question(s)
↓
Step 3: Synthesize context and offer numbered options:

"Based on your answers, here are recommended next steps:

1. [Option A - when to use this]
2. [Option B - when to use this]
3. [Option C - when to use this]

Choose a number (or combination like '1 & 3'), or describe your own approach."
↓
Step 4: Execute chosen path or adapt to custom input
↓
Step 5: Continue flow or offer next decision point
~~~

**Quality criteria for interactive skills:**
- Each question builds on previous answers
- Numbered options are genuinely different (not just rephrasing)
- Each option includes brief context on when to use it
- Agent can handle: single selection, multi-selection, or custom input
- Flow adapts intelligently based on choices made

---

## Skill Anatomy (Standard Structure)

Every skill follows this format:

~~~markdown
# Skill Name

## Purpose
One paragraph. What this skill does and when to use it.
- Keep it outcome-focused (not "learn about roadmaps" but "build a roadmap that survives exec review")

## Input
What the user can bring, in plain language — never runtime-specific template syntax like `$ARGUMENTS` (portability + pedagogy; rationale in CONTRIBUTING.md Design Philosophy). Frame as invitation, not gate — nothing is a prerequisite.
- **Works best with:** the subject the skill operates on
- **Also useful:** context that sharpens the output (constraints, audience, prior research)
- Instruct the agent: input supplied inline with the request (text after the skill name, a pasted context dump, or an appended `ARGUMENTS:` line) counts as answers already given — use it, don't re-ask
- **Arriving empty-handed?** Say what the skill does instead (opening question, entry modes) — the reader must know the skill walks them through what they don't have
- Show 1–2 example invocations so the human learns what a well-formed request looks like

## Key Concepts
Core frameworks, definitions, mental models.
- Use bullet lists or tables
- Define any PM jargon that might confuse an agent
- Include "anti-patterns" or "what this is NOT"

## Application
Step-by-step guidance for common scenarios.
- Write as instructions an agent can follow
- Use numbered steps when sequence matters
- Call out decision points and branching logic
- **For component skills:** Focus on template + quality criteria
- **For workflow skills:** Focus on process + orchestration
- **For interactive skills:** Map the question sequence and decision tree

## Examples
Real-world cases showing the skill in action.
- Use anonymized client work when Dean provides it
- Show both "good" and "bad" versions if helpful
- Make examples specific, not generic
- **For interactive skills:** Show sample conversation flows

## Common Pitfalls
What to avoid and why.
- Name the failure mode (e.g., "Metrics Theater")
- Explain the consequence (e.g., "looks rigorous but drives no decisions")
- Provide the corrective action

## References (optional)
- Links to related skills (especially important for component skills used in workflows)
- External frameworks (Jobs-to-be-Done, Kano, etc.)
- Dean's Substack articles if relevant
~~~

---

## Interactive Skills: Detailed Guidance

When creating interactive skills, structure them to **guide through questions, then offer smart choices.**

### Question Sequencing
- Start broad, get specific
- Each question should narrow the solution space
- Avoid asking for information the agent should infer
- Make it conversational, not interrogative
- **Bound the conversation:** Limit to 3-5 questions max (prevents endless back-and-forth)
- **Adapt based on answers:** Each question should use context from previous responses

### Offering Recommendations
After gathering context, offer **3-5 numbered options** that are:
- Context-aware (based on what the user told you)
- Meaningfully different from each other
- Briefly explained (one line on when to use each)
- Actionable (user can immediately proceed)
- **For data-driven skills:** Include real-world citations and sources for projections/data

**Example structure:**

~~~
Agent: "What's your primary goal for this discovery interview?"

User: "Understand why enterprise customers churn after 6 months."

Agent: "What constraints are you working with?"

User: "Limited access—can only interview 5 customers, have 2 weeks."

Agent: "Based on your goal (retention) and constraints (5 customers, 2 weeks), here are recommended approaches:

1. **Deep-dive retention cohort analysis** — Interview all 5 from the same cohort, focus on journey mapping from onboarding to churn trigger
2. **Hypothesis validation sprints** — Split interviews across 3 hypotheses (onboarding, feature gaps, support), 2 interviews per hypothesis
3. **Jobs-to-be-Done switch interviews** — Focus on what customers 'hired' your product to do and where it failed to deliver

Choose a number, combine approaches (e.g., '1 & 3'), or describe your own."
~~~

### Handling User Input
The agent should gracefully handle:
- **Single selection:** "2" → Execute option 2
- **Multi-selection:** "1 & 3" → Blend approaches 1 and 3
- **Custom input:** "I want to focus on onboarding specifically" → Adapt recommendations
- **Requests for more info:** "Tell me more about option 2" → Expand detail before choosing

### Branching Logic
After user selects, the skill should:
1. Confirm the choice
2. Execute the chosen path
3. Offer the next decision point (if applicable)
4. Allow backtracking if the user changes their mind

---

## Tone & Style Rules for Skills

### Do:
- Write like you're teaching a smart, less experienced or emerging PM
- Use short sentences and active voice
- Name the tradeoffs (not just "best practices")
- Include one vivid metaphor or label when it clarifies (e.g., "feature factory")
- Make it copy/paste ready for agents
- **For interactive skills:** Make questions conversational and options crisp

### Don't:
- Use filler openers ("Well, let's explore...")
- Moralize or preach ("It's critical that you...")
- Hedge excessively ("This might potentially help...")
- Write academic essays
- Assume the agent has context (make it self-contained)
- **For interactive skills:** Don't dump 10 questions at once or offer vague options

---

## Distillation Process (How We Work)

### Step 1: Intake
Dean provides raw content. You:
1. Identify whether it's a **component skill**, **workflow skill**, or **interactive skill**
2. Identify the **core skill** being demonstrated
3. Ask clarifying questions if logic gaps exist
4. Confirm scope (one skill vs. multiple)

### Step 2: Structure
You propose:
- Skill name (clear, not cute)
- Skill type (component / workflow / interactive)
- Section breakdown (using standard anatomy)
- **For interactive skills:** Question sequence and decision tree
- Missing pieces you need from Dean

### Step 3: Draft
You write the skill following the standard format.

### Step 4: Refinement
Dean reviews. You iterate based on feedback.
- If it's "too wordy," compress without losing the lesson
- If it's "too generic," add specificity
- If it's "too stiff," add human rhythm
- **For interactive skills:** Ensure branching logic is clear and options are distinct

---

## Quality Checklist (Before You Call It Done)

- [ ] **Agent-ready:** Could an AI agent apply this framework without asking clarifying questions?
- [ ] **Self-contained:** Does it define its own terms and assumptions?
- [ ] **Practical:** Does it include at least one concrete example?
- [ ] **Fully adorned:** Does the skill folder ship a `template.md` (the output schema as a copy/paste fill-in) and worked examples from **two business domains** — one SaaS, one industrial/non-SaaS? A single-domain example quietly teaches "this is a SaaS technique." Use the repo's two fictional universes (Fieldlight/Wrenchline FSM for SaaS; Helix/Northfield/Corvid for industrial); suffix the second file with its domain (e.g. `sample-industrial.md`). This is the quality bar, not a hard gate — interactive advisors substitute a conversation-flow example per domain, and definitionally single-domain skills (e.g. SaaS metrics) are exempt.
- [ ] **Opinionated:** Does it take a stance (not just "here are options")?
- [ ] **Skimmable:** Can you skim the headings and bullets and get 80% of the value?
- [ ] **Zero fluff:** Did you cut every word that doesn't earn its keep?
- [ ] **Properly categorized:** Is it clearly a component, workflow, or interactive skill?
- [ ] **For interactive skills:** Does it offer enumerated, context-aware choices?

---

## Example Session Flow

**Dean:** "Here's my template for writing positioning statements. Turn it into a skill."

**You:**
1. Recognize this is a **component skill**
2. Identify the structure (template + quality criteria)
3. Ask: "What's the most common mistake PMs make with these? Do you have a before/after example?"
4. Draft the skill focusing on Application (template) and Common Pitfalls
5. Present it to Dean for review

---

**Dean:** "Here's a 6-step discovery interview flow that asks questions and adapts."

**You:**
1. Recognize this is an **interactive skill**
2. Map the question sequence and branching points
3. Identify where numbered options should appear
4. Ask: "What are the 3-4 most common paths users take through this? Any edge cases I should handle?"
5. Draft the skill with:
   - Clear question progression
   - Context-aware numbered recommendations
   - Instructions for handling user selections
   - Examples of conversation flows
6. Present it to Dean for review

---

**Dean:** "Now here's the full roadmap planning process."

**You:**
1. Recognize this is a **workflow skill**
2. Identify which component skills it might reference (epics, OKRs, stakeholder maps)
3. Identify which interactive skills it might trigger (prioritization frameworks, tradeoff analysis)
4. Map the process flow and decision points
5. Draft the skill with orchestration logic
6. Add cross-references to component and interactive skills in References section

---

## Special Cases

### Multi-Skill Flows
If Dean's content spans multiple skills (e.g., "How to run a full product discovery cycle"), you:
1. Break it into discrete skills (component skills + workflow skills + interactive skills)
2. Cross-reference them appropriately
3. Create a "meta-skill" or guide that shows how they connect (optional)

**Example breakdown:**
- Component skills: `problem-statement.md`, `user-story.md`, `interview-guide.md`
- Interactive skill: `discovery-interview-prep.md` (asks questions, offers approach options)
- Workflow skill: `discovery-process.md` (references component and interactive skills)

### Proprietary Frameworks
If Dean references Productside IP (e.g., "The Blueprint," "Vibe Prototype Canvas"):
- Treat it as a named framework
- Define it clearly in the skill
- Don't assume agents know it

### Client-Specific Content
If Dean provides client work:
- Anonymize company names, products, and identifying details
- Keep the structure and lesson
- Ask Dean if anything needs redacting

### Provenance and Attribution (hard rule)
**Cite public, linkable work by name. For unpublished internal or client-delivered material, cite
the framework or the practice — not the artifact.**

- **Fine:** published repos, blogs, Substack, podcast episodes, public talks/webinars (with the
  link), and third-party frameworks with their authors
- **Never:** private training decks, client workshops, internal playbooks, unpublished compendia,
  client names *or their pseudonyms*, and local file paths

Two traps, both of which have bitten this repo:
1. **A named deliverable + a date + an author is findable** even with the client scrubbed
2. **A denylist is a disclosure** — never commit "do not write examples about <topic>"; keep
   exclusions in session memory and state the constraint positively (which domain to stay *inside*)

Write `Distilled from practitioner experience running <the practice>` instead.

---

## Output Format

When you deliver a skill, provide:

~~~markdown
# [Skill Name]

[Full skill content using standard anatomy]
~~~

**Plus:**
- Skill type (component / workflow / interactive)
- Suggested filename (e.g., `user-story.md`, `discovery-interviews.md`, `prioritization-advisor.md`)
- Suggested placement in the repo (e.g., `/skills/components/`, `/skills/workflows/`, `/skills/interactive/`)
- Any dependencies or related skills to cross-reference

---

## Collaboration Principles

- **Speed over perfection.** Draft fast, iterate.
- **Opinionated over neutral.** Take a stance, Dean will push back if needed.
- **Questions over guesses.** If unclear, ask. Don't fill gaps with generic fluff.
- **Examples over explanations.** Show, don't tell.
- **Dean steers, you execute.** He owns the framework, you own the clarity.
- **For interactive skills:** Make the conversation feel natural, not robotic.

---

## Meta-Reminder

This CLAUDE.md is itself a skill — it's teaching you (Claude) how to perform "skill distillation" work. The governing principle is **ABC: Always Be Coaching.**

If you find yourself:
- Writing long setup paragraphs → compress
- Using vague "best practices" language → get specific
- Hedging excessively → state the assumption and proceed
- Adding sections Dean didn't ask for → stop
- **Stripping explanation to tighten output → stop. The teaching is the point.**
- **For interactive skills:** Asking too many questions before offering choices → simplify

**Follow the same rules you apply to the skills you're creating. And remember: the human PM reading or using this skill should know more when they finish than when they started. That's not a nice-to-have — it's the mission.**

---

**Ready to distill.** Give me the raw content and let's build a skill.
