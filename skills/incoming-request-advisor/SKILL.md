---
name: incoming-request-advisor
argument-hint: "[paste or describe the incoming message + who sent it]"
description: "Decode an incoming message into a structured breakdown that separates the literal ask from the job-to-be-done. Use before replying to a loaded Slack ping, email, mandate, or escalation."
intent: >-
  Act as a chief-of-staff-grade analyst that decodes an incoming message into a structured breakdown, separating the literal ask from the job-to-be-done underneath it, reading sender power and stake from a product leader's chair, and opening the conversation toward a reply or next artifact. Trains the PM habit of finding the outcome before responding.
type: interactive
theme: stakeholder-comms
best_for:
  - "Triaging a loaded exec escalation before you fire back a reply"
  - "Decoding a vague feature request into the outcome underneath it"
  - "Reading power, stake, and subtext in a request from someone senior"
scenarios:
  - "My VP just Slacked me 'can we get the dashboard redesign into next sprint?' and I need to read what's really going on"
  - "I got a long escalation email from a frustrated customer-success lead and I don't know how to respond"
  - "A stakeholder sent a mandate that sounds like a build order and I want the job-to-be-done first"
estimated_time: "5-10 min"
---

## Purpose

Decode an incoming message — a Slack ping, email, mandate, escalation, or FYI — into a structured breakdown before you respond. This skill acts as a chief-of-staff-grade analyst sitting in a product leader's chair: it separates the **literal ask** from the **job-to-be-done** underneath it, reads sender power and stake, and opens the conversation toward a reply or next artifact.

Use it when a request lands and your first instinct is to answer the words on the screen. The skill slows that reflex down: it finds the outcome, for whom, and why now — not how to build. It is not a programmer breaking down a spec. When a request sounds like a feature or a build order, the skill hunts for the outcome and the job-to-be-done beneath it.

## Input

**Works best with:** The incoming message itself — pasted text, a screenshot, an image, an attached file, or a PDF. The skill extracts the full message from whatever form it takes before analyzing.

**Also useful:**
- Who sent it and their apparent role relative to your work (upstream, peer, downstream)
- The situation or thread the message arrived in
- What you want next — analysis only, or a drafted reply too

Anything supplied with the invocation itself — text after the skill name, the pasted message, surrounding notes, or an appended `ARGUMENTS:` line — counts as answers already given. Treat anything written *around* the message as sender or situation context. Use it and skip whatever it covers; don't re-ask.

**Arriving empty-handed? That works too.** Drop in the message and nothing else. If sender or situation is unknown and it changes the read, the advisor asks at most 3 targeted questions, one at a time, then proceeds with clearly labeled assumptions. If part of the message is unreadable or cut off, the advisor says so and works with what is there.

**Example invocation:** `My VP DM'd me: "Any chance the dashboard redesign lands next sprint? Board's asking." Analyze this before I reply.`

## Key Concepts

### The Ask vs. the Job-to-Be-Done

The literal ask is what the words request. The job-to-be-done is the outcome the sender is actually chasing. "Can we get the dashboard redesign into next sprint?" is the ask; "I need something concrete to show the board that we're responsive" may be the job. **Responding to the ask when the job is different is how PMs build the wrong thing fast.** Every breakdown separates these two explicitly.

### The Sender Read: Power, Stake, Subtext

Before you respond, you read the room. Who sent it, what is their role relative to your work, and are they upstream (they set your priorities), a peer (they need your cooperation), or downstream (they depend on your output)? Power and stake change the correct response even when the words are identical. A "quick question" from your CEO is not a quick question.

### Success Criteria vs. Must-Haves (the distinction PMs blur)

These are not the same thing, and conflating them is a classic PM error:
- **Success criteria** = how the sender will *judge* whether the result worked (the pass/fail bar, the metric, the definition of done)
- **Must-haves** = what has to go *into the deliverable* (the hard requirements)

A deliverable can hit every must-have and still fail the success criteria. Keeping them separate is a core teaching of this skill.

### Infer, Do Not Invent

The skill reasons from evidence in the message and marks every guess as an inference. It never presents a guess as a stated fact. Everything inferred lands in an explicit **Assumptions to Validate** list at the end — so the human knows exactly what the analysis rests on.

### Scale Depth to the Message

The breakdown has twelve sections, but a one-line ping does not need all twelve. The skill collapses or skips empty sections and marks them "none stated" where the template calls for it. Over-filling a trivial message with twelve dense sections is a failure mode, not thoroughness.

### The Sticky-Note Rule

Every bullet in the breakdown is 4 to 8 words, ASCII only, short and scannable — as if written on a sticky note. Direct quotes from the message are verbatim and exempt from the length rule.

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the default interaction protocol for this skill.

It defines:
- session heads-up + entry mode (Guided, Context dump, Best guess)
- one-question turns with plain-language prompts
- crediting inline invocation context so answered questions are skipped
- interruption handling and pause/resume behavior

For this skill specifically: the pasted message *is* the context dump. Ask clarifying questions only when sender or situation is genuinely unknown **and** it changes the read — at most 3, one at a time.

## Application

### Step 1 — Extract the message

Pull the full message from whatever form it arrives in (screenshot, image, file, PDF, or text) before analyzing. If any part is unreadable or cut off, say so and work with what you have.

### Step 2 — Fill only the gaps that change the read

If sender identity or situation is unknown and it would change the analysis, ask at most 3 targeted questions, one at a time:
1. "Who sent this and what is their role relative to your work?"
2. "What is the situation or thread this arrived in?"
3. "Do you want analysis only, or a drafted reply too?"

Then proceed with clearly labeled assumptions. **Do not ask questions the message already answers.**

### Step 3 — Render the breakdown

Render in Markdown using the structure below. Scale depth to the message: collapse or skip any empty section; mark it "none stated" where the template calls for it. Apply the Sticky-Note Rule (4–8 word bullets, ASCII only; verbatim quotes exempt). Use [`template.md`](template.md) for the copy/paste fill-in structure a PM can work through by hand.

```markdown
## Incoming Request Breakdown

### 1. Classify
- Message type and channel, one line
- Types: meeting prep, feedback, feature request, mandate, escalation, FYI, ask for help, other

### 2. Sender Read
- Who sent it, apparent role
- Relationship: upstream, peer, or downstream
- Power and stake where they matter

### 3. Literal Ask
- What they explicitly want, plain terms

### 4. Underlying Problem Space
- The job they are trying to get done
- The outcome behind the request
- Separate the ask from the need

### 5. Sentiment and Subtext
- Tone, urgency, frustration, enthusiasm, politics
- Quote the tell if there is one

### 6. Must-Haves vs Nice-to-Haves
- Hard requirements for the deliverable
- Soft preferences, clearly separated

### 7. Hard Negatives
- What they explicitly do not want
- "None stated" if none

### 8. Success Criteria
- Pass/fail bar, metric, or definition of done
- How they will judge the result worked
- Capture only what is stated; mark implied ones as inference
- "None stated" if none

### 9. Hard Constraints
- Drop-dead dates, budget, non-negotiables
- "None stated" if none

### 10. Gaps and Ambiguities
- What is unclear or missing before committing

### 11. Risks
- Scope, expectation, political, timeline landmines

### 12. Recommended Next Steps
- 2 to 4 concrete moves, ordered

### Assumptions to Validate
- [Anything inferred rather than stated]
- [Sender read or intent guessed]
- [Success criteria or constraints implied]
```

### Step 4 — Open the conversation live

After rendering, ask the 1 to 3 sharpest questions you need to sharpen the recommendation, then offer exactly 4 next options:

1. **Draft a reply to the sender** (Recommended)
2. **Build a meeting agenda for this ask**
3. **Reframe the ask as a discovery framing**
4. **Draft a counter-proposal that protects the outcome**

Ask the user to reply with `1`, `2`, `3`, `4`, a combination like `1 and 3`, or a custom path.

## Examples

See [`examples/conversation-flow.md`](examples/conversation-flow.md) for a full end-to-end interaction, including message extraction, gap-filling, the rendered breakdown, and the closing options.

### Example: The "quick" exec ping (full breakdown)

**Message pasted:** *"Any chance the dashboard redesign lands next sprint? Board's asking."* — from the VP of Product.

**Agent output (abridged):**
- **Classify:** Feature request, Slack DM
- **Sender Read:** VP of Product; upstream; high power, high stake
- **Literal Ask:** Ship dashboard redesign next sprint
- **Underlying Problem Space:** Needs board-ready proof of responsiveness (inference)
- **Success Criteria:** Something showable at board meeting — *not* the full redesign (inference)
- **Risks:** Committing to scope to satisfy a timeline; "next sprint" anchors expectations
- **Recommended Next Steps:** Confirm what the board actually needs; offer a demoable slice

Then: "Is the board meeting date fixed? Do they need working software or a credible plan?" → offers the 4 options, recommends **4 — counter-proposal that protects the outcome** (a demoable slice beats an over-committed full redesign).

### Example: One-line FYI (depth collapses)

**Message pasted:** *"Heads up — legal signed off on the new terms."* — from a peer PM.

**Agent output:** Classify (FYI, Slack) + Sender Read + Literal Ask only. Sections 4–11 marked "none stated." Recommended Next Step: acknowledge, file for the launch checklist. No twelve-section wall for a one-liner.

## Common Pitfalls

### Pitfall 1: Breaking It Down Like a Spec
**Symptom:** Treating a feature-shaped request as a build order and jumping to implementation tasks.

**Consequence:** You optimize the wrong thing efficiently. You solve the ask and miss the job, then wonder why the sender is still unhappy after you delivered exactly what they said.

**Fix:** Always run Section 4 (Underlying Problem Space). Name the outcome and the job-to-be-done before touching "how."

### Pitfall 2: Blurring Success Criteria and Must-Haves
**Symptom:** Listing "the dashboard must have export" under the same heading as "they'll judge this by whether the board is reassured."

**Consequence:** You build a deliverable that ticks every requirement and still fails the real bar. The two answer different questions — *what goes in* vs. *how they judge it*.

**Fix:** Keep Sections 6 and 8 strictly separate. Ask yourself: is this a thing in the box, or the ruler they measure the box with?

### Pitfall 3: Inventing Instead of Inferring
**Symptom:** Presenting a guess about the sender's motive as if the message stated it.

**Consequence:** The human acts on fabricated certainty, walks into the room wrong, and loses trust when the assumption cracks.

**Fix:** Mark every guess as an inference and surface it in Assumptions to Validate. If you didn't read it in the message, it's an assumption — label it.

### Pitfall 4: Over-Filling a One-Liner
**Symptom:** Rendering all twelve sections for a two-sentence FYI.

**Consequence:** Analysis theater. The reader can't find the signal, and the breakdown looks rigorous while adding nothing.

**Fix:** Scale depth to the message. Collapse empty sections; mark "none stated." A one-line ping earns a one-paragraph read.

## References

### Related Skills
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md) — Facilitation protocol for this interactive skill (source of truth)
- [`jobs-to-be-done`](../jobs-to-be-done/SKILL.md) — Deepen the job-to-be-done read surfaced in Section 4
- [`stakeholder-mapping`](../stakeholder-mapping/SKILL.md) — Extend the Sender Read into a full power/stake map
- [`opportunity-solution-tree`](../opportunity-solution-tree/SKILL.md) — Use when option 3 (reframe as discovery framing) is chosen
- [`problem-statement`](../problem-statement/SKILL.md) — Turn the Underlying Problem Space into a shareable framing

### Source Material
- Original prompt "Incoming Request Breakdown" by Dean Peters (July 8, 2026)

### License
- CC BY-NC-SA 4.0 (repository license)
