---
name: workshop-facilitation
description: Facilitate workshop sessions in a one-step, multi-turn flow. Use when an interactive skill needs consistent pacing, options, and progress tracking.
intent: >-
  Provide the canonical facilitation pattern for interactive skills: one step at a time, with clear progress, adaptive recommendations at decision points, and predictable interruption handling.
type: interactive
theme: workshops-facilitation
best_for:
  - "Adding structured facilitation to any PM workshop or guided session"
  - "Running interactive sessions with numbered recommendations and progress tracking"
  - "Ensuring your workshops stay on track and end with actionable choices"
scenarios:
  - "I want to run a structured positioning workshop with my product team — set up the facilitation protocol"
  - "Help me facilitate a discovery sprint kickoff with clear questions, options, and progress labels"
estimated_time: "varies by workshop"
---

## Purpose
Provide the canonical facilitation pattern for interactive skills: one step at a time, with clear progress, adaptive recommendations at decision points, and predictable interruption handling.

## Input

**Nothing required** — this skill defines the facilitation protocol other interactive skills follow.
**Also useful:** If invoked standalone, name the session you want facilitated and any context for it; that context carries into the session as answers already given.

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or an appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it covers; don't re-ask.

**Arriving empty-handed? That works too.** When another skill references this protocol, that skill's Input section governs what to provide.

**Example invocation:** `Facilitate a 45-minute retro on our failed beta launch using this protocol.`

## Key Concepts
- **One-step-at-a-time:** Ask a single targeted question per turn.
- **Session heads-up + entry mode:** Start by setting expectations and offering `Guided`, `Context dump`, or `Best guess` mode.
- **Default entry mode (configurable):** Each skill that runs this protocol carries a `**Default entry mode:**` line. It is set from `pm-skills.config.yaml` at the library root: a library-wide `default_entry_mode` plus optional per-skill `overrides`. Precedence: the user's own choice in the session › the config file (if you can read it) › the skill's own line › Guided. The default decides how the first turn opens; it never removes the other two modes, and the user can switch at any time.
- **Progress visibility:** Show user-facing progress labels like `Context Qx/8` and `Scoring Qx/5`.
- **Decision-point recommendations:** Use enumerated options only when a choice is needed, not after every answer.
- **Quick-select response options:** For regular context/scoring questions, provide concise numbered answer options plus `Other (specify)` when useful.
- **Flexible selection parsing:** Accept `#1`, `1`, `1 and 3`, `1,3`, or custom text, then synthesize multi-select choices.
- **Context-aware progression:** Build on previous answers and avoid re-asking resolved questions.
- **Options sharpen each turn:** Early options can use industry-typical examples. By the midpoint, options must reflect the specific product, customer, and situation the user has described. If domain context is thin and the runtime has search, ground options in real roles and workflows; otherwise say the options are typical examples and invite correction. Never invent specifics to make an option look sharp.
- **Show the read before asking (context dump):** Before the first question, summarize what was supplied as **Known / Assumed / Missing / Conflicting**. Credit where each item came from, and keep what a source *reported* separate from what has been *verified*. Then ask only the questions that would most change the artifact.
- **Interruption-safe flow:** Answer meta questions directly (for example, "how many left?"), restate status, then resume. A correction ("go back to Q2") replays that question with options updated for current context. On resume after a pause, recap what was captured, what is still open, and the next question.
- **Completion summary before generating:** Recap what was supplied, what was inferred, what remains unknown or disputed, and whether the work is ready for a decision. Confirm before producing the artifact.
- **Decision ladder:** At a decision point, list the option the evidence favors first, labeled `(Recommended)`, then two or three genuinely distinct alternatives, each with a one-sentence tradeoff, then `Other`. Allow combinations where they make sense. The skill recommends; the user decides.
- **Ranked assumptions:** Whenever best guess mode was used, end with `Assumptions to Validate`, ranked by how much each one could change the decision.
- **Fast path:** If the user requests a single-shot output, skip multi-turn facilitation and deliver a condensed result.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins.

## Application
1. Start with a brief heads-up on estimated time and number of questions.
2. Offer all three entry modes, then open in the skill's default entry mode in the same turn. Don't stall waiting for a pick:
   - `1` Guided mode (one question at a time). Default opening: ask the first question.
   - `2` Context dump (paste known context; skip redundancies). Default opening: invite the paste.
   - `3` Best guess mode (infer missing details and label assumptions). Default opening: ask for a one-sentence minimum, then draft.
   - If context was supplied with the invocation, open at the first real gap and keep the progress label honest.
   - In context dump mode, show the **Known / Assumed / Missing / Conflicting** read before any question.
3. Run one question per turn and wait for an answer before continuing.
4. Keep questions plain-language; include a short example response format when helpful.
5. Show progress each turn:
   - `Context Qx/8` during context collection
   - `Scoring Qx/5` during assessment/scoring
6. Ask follow-up clarifications only when they materially improve recommendation quality.
7. For regular context/scoring questions, offer quick-select numbered response options when practical:
   - Keep options concise and mutually exclusive when possible.
   - Include `Other (specify)` if likely answers are open-ended.
   - Accept multi-select responses like `1,3` or `1 and 3`.
8. Provide numbered recommendations only at decision points, formatted as a decision ladder (`(Recommended)` first, distinct alternatives with one-line tradeoffs, `Other`):
   - after context synthesis,
   - after maturity/profile synthesis,
   - during priority/action-plan selection.
9. Accept numeric or custom choices, synthesize multi-select choices, and continue.
10. If interrupted by a meta question, answer directly, then restate progress and pending question. If the user says "go back to Qx," replay that question with options updated for what you now know.
11. If the user says stop/pause, halt immediately and wait for explicit resume. On resume, recap captured / open / next question before continuing.
12. Before generating the artifact, give the completion summary (supplied · inferred · unknown or disputed · ready for a decision?) and confirm.
13. End with a clear summary, decisions made, and (if best guess mode was used at any point) a ranked `Assumptions to Validate` list.

## Examples
**Opening:**
"Quick heads-up: this should take about 7-10 minutes and around 10 questions. How do you want to start?
1. Guided mode
2. Context dump
3. Best guess mode

Let's start one question at a time. `Context Q1/10`: what's the session for?"

*(This opening assumes the default entry mode is Guided. With Context dump as the default, the same turn would end with "Paste what you already know." With Best guess, it would end with "Give me the session in one sentence and I'll draft the plan.")*

**User:** "2"

**Facilitator:** "Paste what you already know. I’ll skip answered areas and ask only what’s missing."

**User:** *(pastes notes on a dispatch-scheduling feature)*

**Facilitator:** "Here's what I took from your notes:
- **Known:** Users are dispatchers at mid-size field service companies; launch target is Q2.
- **Assumed:** 'Reduce no-shows' means technician no-shows. I inferred that from the scheduling context, so correct me if it's wrong.
- **Missing:** Success metric and baseline.
- **Conflicting:** Notes say 'SMB first' and also 'our enterprise pilot accounts.'

Two questions would change this most. `Context Q1/2`: which segment is v1 for?"

**Decision point after synthesis:**
1. **Prioritize Context Design** (Recommended) — your answers point to inconsistent inputs as the root constraint
2. Prioritize Agent Orchestration — faster visible wins, but builds on context you said is unreliable
3. Prioritize Team-AI Facilitation — fixes adoption first; slower to show output gains
4. Other (describe your own priority)

**User:** "1 and 3"

**Facilitator:** "Great. We’ll run Context Design first, with Team-AI Facilitation in parallel."

**Inline input at invocation:** when the user supplies context with the invocation itself, credit it as answers, open at the first unanswered question, and keep progress labels honest (start at `Context Q2/6` if Q1 was covered). Full transcript, including the re-asking anti-pattern: [examples/inline-input-flow.md](examples/inline-input-flow.md).

## Common Pitfalls
- Asking multiple questions in the same turn.
- Offering recommendations after every answer (creates interaction drag).
- Using shorthand labels without plain-language questions.
- Hiding progress, so users don't know how much remains.
- Ignoring the user's chosen option or custom direction.
- Failing to label assumptions when running in best-guess mode.
- **The silent resolve:** quietly picking a side when the supplied context conflicts. The artifact looks clean but rests on a choice the user never made. Surface it under **Conflicting** and ask.
- **The flat assumption list:** listing assumptions without ranking them. The one guess holding up the whole plan gets buried among trivia. Rank by how much each could change the decision.
- **Generating before the recap:** jumping from the last answer straight to the artifact. The user never gets to catch a misread before it spreads. Give the completion summary and confirm first.
- **The stalled opening:** listing the three modes and then waiting for a pick. That turn adds nothing. Open in the default mode; the user can still switch.
- **Placeholder options:** options like "Option A / Option B" or generic roles late in a session. These show the skill wasn't listening. Use what the user has told you.

## References
- Use as the source of truth for interactive facilitation behavior.
- User-facing explainer of the contract (Guided Context Capture): [docs/guided-context-capture.md](https://github.com/deanpeters/Product-Manager-Skills/blob/main/docs/guided-context-capture.md).
- Evidence-label vocabulary shared with autonomous research: [autonomous-investigation](../autonomous-investigation/SKILL.md).
- Apply alongside workshop skills in `skills/*-workshop/SKILL.md` and advisor-style interactive skills.
