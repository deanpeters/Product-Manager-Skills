---
name: discovery-habits-advisor
argument-hint: "[your team, how it talks to customers today, and what gets in the way]"
description: "Set up a steady rhythm of customer contact that feeds decisions. Use when discovery happens in bursts, or never, and you want a habit the team will actually keep."
intent: >-
  Guided triage from how a team talks to customers today to a sustainable cadence. Diagnoses the
  real blocker (access, time, ownership, or what happens to the evidence), fits a weekly or
  fortnightly touchpoint rhythm to the team and customer reach, and defines who joins, how evidence
  is captured, and how it reaches a decision. Right-sized so a small team starts with one habit.
type: interactive
theme: discovery-research
best_for:
  - "Moving from occasional research projects to steady customer contact"
  - "Diagnosing why a team that 'knows it should' talk to customers doesn't"
  - "Designing a cadence that fits long sales cycles, limited access, or a regulated customer"
  - "Making sure evidence from conversations actually changes a decision"
scenarios:
  - "We do a research sprint once a year and then go quiet. How do we make it continuous?"
  - "We can't reach end customers, only through partners. What cadence works?"
  - "Our team is three people. What's the smallest discovery habit worth keeping?"
  - "We talk to customers but nothing changes. What's missing?"
estimated_time: "10-20 min"
---

# Discovery Habits Advisor

## Purpose

Turn customer contact from an **event** into a **habit**: a rhythm of small, regular conversations
whose evidence reaches the decisions the team is making that week.

Teams usually know they should talk to customers. They don't, because discovery lives in projects
(with a start, an end, and a deck), and projects get squeezed by delivery pressure. A habit fits
inside normal work: a few conversations a week, notes in one place, one visible question the
evidence is aimed at.

The sentence to keep in your head: **the point of a habit is not more customer contact, it's
shorter distance between what customers say and what the team decides.**

## Input

**Works best with:** Your team (who is on it), how you talk to customers today, and what gets in
the way.

**Also useful:** Who you can reach and how (direct, through partners, through support), the length
of your sales cycle, what decisions are coming up, and where evidence currently goes.

Anything supplied with the invocation itself (text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line) counts as answers already given. Use it and skip whatever it covers;
don't re-ask.

**Arriving empty-handed? That works too.** The skill starts by asking how customer contact works
today and what's in the way, then recommends the smallest rhythm that would work. It sizes the
habit to your team, never defaults to the heaviest, and lets you move it either way.

**Example invocations:**
- `Team of 4. We run a discovery sprint once a year. Want something continuous.`
- `We only reach plant engineers through partners. What cadence can we keep?`

---

## Key Concepts

### The Dial: Right-Size the Habit

**Not every team can do the same rhythm.** Pick a level, say why in one line, and let the user move it:

| | **Level 1: Light** | **Level 2: Standard** | **Level 3: Full** |
|---|---|---|---|
| Rhythm | One conversation every two weeks | One or two a week, same slot | Weekly touchpoints with a rotating team |
| Who | The PM | PM + one designer or engineer | The product trio, rotating guests |
| Evidence | One shared notes page | Notes plus a weekly one-line "what we learned" | Notes, a living opportunity tree, review in planning |
| Fits | Small team, long cycles, limited access | Most teams | Teams with access and a high-uncertainty roadmap |

**Level 2 is the default. Never default to Level 3.** A heavy cadence a small team can't keep
teaches the team that discovery is a thing they fail at. If they go lighter, name what it leaves
uncovered (for Level 1: fewer conversations means slower pattern detection, and fewer people
hearing customers directly).

### Find the Real Blocker

Four blockers look identical ("we don't have time") and need different fixes:

| Blocker | What it sounds like | The fix |
|---|---|---|
| **Access** | "We can't reach customers" | Create a standing channel: customer advisory panel, support-ride-alongs, partner introductions, a recruiting pool kept warm |
| **Time** | "We're always in delivery" | Fixed slot, tiny scope, shared by two people; trade a status meeting for it |
| **Ownership** | "Everyone assumes someone else does it" | Name one owner for scheduling and one for the notes |
| **Consequence** | "We talk but nothing changes" | Tie each conversation to a named upcoming decision; review evidence in the meeting where the decision is made |

Most teams that "can't find time" actually have a consequence problem: conversations that change
nothing feel optional.

### Aim Every Conversation at a Decision

A standing slot with no question becomes small talk. Keep one **visible question** the team is
trying to answer this month, tied to a decision on the calendar ("whether to fund the bracket kit
in March"). Conversations then gather evidence for something, and the evidence has somewhere to go.

### Access in Long Cycles and Through Partners

Where customers are hard to reach, don't pretend a weekly slot will work. Use whatever contact
exists: **post-sale** (commissioning, support calls), **partners** (ride-alongs, partner calls), and
**trade-show or site visits** as clusters of conversations. Set the habit around the *capture and
review* rhythm even when the conversations come in bursts: a weekly 20-minute evidence review keeps
the habit alive between visits.

### Capture Evidence Where the Team Will See It

One shared place, simple notes, each with who, when, and what was said in their words. Keep
observation separate from interpretation (see [`research-synthesis`](../research-synthesis/SKILL.md)).
A weekly one-line "what we learned" posted where the team already looks (the planning doc, the
channel) does more than a perfect repository nobody opens.

### Share the Hearing

Evidence heard directly changes minds in a way a summary doesn't. Rotate engineers, designers, or
partner managers into conversations. When one person does all the listening, everyone else has a
second-hand version and argues from opinion.

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol:
heads-up, one question per turn, numbered options, and best-guess mode on request.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

### Anti-Patterns (what this is NOT)
- **Not a research method.** It sets the rhythm; interviewing and synthesis live in other skills.
- **Not a mandate for weekly interviews.** Level 1 is a legitimate answer.
- **Not a tooling recommendation.** A shared page is enough.

---

## Application

This skill asks **up to 4 adaptive questions**, then recommends a rhythm.

### Question 1 of 4: How does customer contact work today?

**Agent asks:**

"How do you hear from customers right now?

1. **Occasional projects** (a research sprint, a round of interviews, then quiet)
2. **Indirectly** (support, sales, partners relay it)
3. **Regularly, but nothing changes** (we talk, then deliver as planned)
4. **Hardly at all**"

**Listen for the blocker underneath.** 1 → likely time or ownership. 2 → access, plus second-hand
evidence. 3 → consequence. 4 → access or fear.

### Question 2 of 4: What's actually in the way?

**Agent asks:**

"What's the main reason it isn't steadier?

1. **We can't easily reach customers** (access)
2. **We're always in delivery** (time)
3. **Nobody owns it** (ownership)
4. **We do it, but it doesn't change what we build** (consequence)"

**Confirm the diagnosis.** If they pick time, ask whether the conversations are tied to a decision;
the real blocker is often consequence.

### Question 3 of 4: Who can do this, and how many customers can you reach?

**Agent asks:**

"Who on the team could take part, and roughly how many customer contacts could you arrange in a
month?"

**Size the level:** one person and a handful of contacts → Level 1. A PM plus a partner and a
steady pool → Level 2. A full trio with access and a high-uncertainty roadmap → Level 3. Recommend
one, say why, and invite an override either way.

### Question 4 of 4: What decision is coming up?

**Agent asks:**

"What's the next real decision this evidence could change?"

**Tie the habit to it.** That decision becomes the visible question for the month and the meeting
where evidence is reviewed.

### Final Step: Recommend the habit

```markdown
## Your Discovery Habit: [team / context]

**Level:** [1 Light / 2 Standard / 3 Full], because [one line]. A lighter level would leave
[what it leaves uncovered].
**The real blocker:** [access / time / ownership / consequence] and the fix.

### The rhythm
- **Conversations:** [how many, when, who joins]
- **Where evidence goes:** [one place, who writes the notes]
- **The visible question this month:** [tied to the decision]
- **Weekly review:** [20 minutes, what gets said, who hears it]

### How evidence reaches the decision
[Which meeting, what the evidence changes]

### Start this week
1. [one action, small]
2. [one action]

### Skills to pair
[`discovery-interview-prep`](../discovery-interview-prep/SKILL.md), [`research-synthesis`](../research-synthesis/SKILL.md), [`opportunity-solution-tree`](../opportunity-solution-tree/SKILL.md)
```

---

## Examples

### Example A: SaaS, a small team with consequence trouble

**User:** "Team of 4 at Fieldlight. We run a research sprint every spring, then go quiet. We talk to
customers sometimes but roadmap decisions don't change."

**Agent (Q1):** → **3 (regularly, nothing changes).** **(Q2):** → **4 (consequence).**
**Agent (Q3):** "Two of you could join, and CS can arrange about six contacts a month." → Level 2.

**Recommendation:** *Level 2, because you have two people and a steady pool.* **Blocker:**
consequence. Fix: tie every conversation to a roadmap decision. This month's question: "Does the
route-rebuild pain justify the optimizer in Q3 planning?" Two conversations a week, PM plus an
engineer rotating in; notes in one doc; a one-line "what we learned" in the Monday planning
thread; evidence reviewed in the planning meeting where the decision is made. A lighter level would
mean the engineer never hears a customer, so arguments stay second-hand.

### Example B: Industrial, access through partners

**User:** "We sell controllers through 8 partners and only reach plant engineers through them. Sales
cycle is 8 months. A weekly slot won't work."

**Agent (Q1):** → **2 (indirectly).** **(Q2):** → **1 (access).**
**Agent (Q3):** "The PM and one application engineer; maybe 6-8 contacts a month, in clusters."

**Recommendation:** *Level 1 with a captured rhythm, because contacts come in bursts.* Use
commissioning visits and partner ride-alongs as the source (clusters of conversations), keep a
warm pool of five plant engineers who've agreed to a call, and run a **weekly 20-minute evidence
review** even in quiet weeks. Visible question: "Is downtime or program risk the bigger barrier?"
tied to the tooling decision in March. A lighter level would leave you with second-hand partner
reports, so ask partners to bring an engineer to one call a month.

---

## Common Pitfalls

### Pitfall 1: Discovery as a Project
**Symptom:** A sprint, a deck, then silence.
**Consequence:** Evidence goes stale and the team returns to opinion.
**Fix:** A small standing slot that survives delivery pressure.

### Pitfall 2: A Rhythm Nobody Can Keep
**Symptom:** Weekly interviews planned by a team of three with no access.
**Consequence:** Two weeks in, it's abandoned and discovery feels like failure.
**Fix:** Size the level to the team. Level 1 kept beats Level 3 dropped.

### Pitfall 3: No Decision Attached
**Symptom:** Conversations with no question and no meeting where evidence is used.
**Consequence:** Nothing changes, so the habit feels optional.
**Fix:** Name the decision, and review evidence in the meeting where it's made.

### Pitfall 4: One Listener
**Symptom:** The PM hears customers and reports back.
**Consequence:** Everyone else argues from a summary.
**Fix:** Rotate others into conversations.

### Pitfall 5: A Repository Nobody Opens
**Symptom:** Elaborate tooling, empty habit.
**Consequence:** Evidence exists and nobody sees it.
**Fix:** One shared page and a weekly one-liner where the team already looks.

### Pitfall 6: Ignoring Long Cycles and Gated Access
**Symptom:** Advice copied from fast consumer software.
**Consequence:** A cadence that can't work for your customers.
**Fix:** Use clusters of contact (visits, commissioning) and keep the review rhythm weekly.

---

## References

### Related Skills
- [`discovery-interview-prep`](../discovery-interview-prep/SKILL.md): run the conversations
- [`discovery-process`](../discovery-process/SKILL.md): the full process
- [`research-synthesis`](../research-synthesis/SKILL.md): make sense of what you hear
- [`opportunity-solution-tree`](../opportunity-solution-tree/SKILL.md): where the evidence accumulates
- [`survey-design-advisor`](../survey-design-advisor/SKILL.md): size what you found
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md): interaction protocol

### External Frameworks
- **Continuous discovery habits:** Teresa Torres, *Continuous Discovery Habits* (2021), the weekly touchpoints and product trio.

### Provenance
Distilled from practitioner experience helping product teams build sustainable customer-contact routines.
