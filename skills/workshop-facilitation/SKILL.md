---
name: workshop-facilitation
description: Facilitate workshop sessions in a one-step, multi-turn flow. Use when an interactive skill needs consistent pacing, options, and progress tracking.
compatibility: opencode
metadata:
  best_for:
    - "Adding structured facilitation to any PM workshop or guided session"
    - "Running interactive sessions with numbered recommendations and progress tracking"
    - "Ensuring your workshops stay on track and end with actionable choices"
  estimated_time: "varies by workshop"
  intent: >-
    Provide the canonical facilitation pattern for interactive skills: one step at a time, with clear progress, adaptive recommendations at decision points, and predictable interruption handling.
  scenarios:
    - "I want to run a structured positioning workshop with my product team — set up the facilitation protocol"
    - "Help me facilitate a discovery sprint kickoff with clear questions, options, and progress labels"
  theme: workshops-facilitation
  type: interactive
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
- **Progress visibility:** Show user-facing progress labels like `Context Qx/8` and `Scoring Qx/5`.
- **Decision-point recommendations:** Use enumerated options only when a choice is needed, not after every answer.
- **Quick-select response options:** For regular context/scoring questions, provide concise numbered answer options plus `Other (specify)` when useful.
- **Flexible selection parsing:** Accept `#1`, `1`, `1 and 3`, `1,3`, or custom text, then synthesize multi-select choices.
- **Context-aware progression:** Build on previous answers and avoid re-asking resolved questions.
- **Interruption-safe flow:** Answer meta questions directly (for example, "how many left?"), restate status, then resume.
- **Fast path:** If the user requests a single-shot output, skip multi-turn facilitation and deliver a condensed result.

## Application
1. Start with a brief heads-up on estimated time and number of questions.
2. Ask the user to choose an entry mode:
   - `1` Guided mode (one question at a time)
   - `2` Context dump (paste known context; skip redundancies)
   - `3` Best guess mode (infer missing details and label assumptions)
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
8. Provide numbered recommendations only at decision points:
   - after context synthesis,
   - after maturity/profile synthesis,
   - during priority/action-plan selection.
9. Accept numeric or custom choices, synthesize multi-select choices, and continue.
10. If interrupted by a meta question, answer directly, then restate progress and pending question.
11. If the user says stop/pause, halt immediately and wait for explicit resume.
12. End with a clear summary, decisions made, and (if best guess mode was used) an `Assumptions to Validate` list.

## Examples
**Opening:**
"Quick heads-up: this should take about 7-10 minutes and around 10 questions. How do you want to start?
1. Guided mode
2. Context dump
3. Best guess mode"

**User:** "2"

**Facilitator:** "Paste what you already know. I’ll skip answered areas and ask only what’s missing."

**Decision point after synthesis:**
1. **Prioritize Context Design** (Recommended)
2. Prioritize Agent Orchestration
3. Prioritize Team-AI Facilitation

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

## References
- Use as the source of truth for interactive facilitation behavior.
- Apply alongside workshop skills in `skills/*-workshop/SKILL.md` and advisor-style interactive skills.
