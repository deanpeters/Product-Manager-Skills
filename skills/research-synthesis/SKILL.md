---
name: research-synthesis
argument-hint: "[the research you have: interview notes, tickets, survey comments]"
description: "Turn raw interview notes and feedback into themes, insights, and opportunity statements. Use when you have a pile of research and need to know what it says before deciding anything."
intent: >-
  Take research that is still raw (interview notes, call transcripts, tickets, survey comments) and
  walk it through coding, affinity grouping, insight writing, and opportunity framing, with every
  insight traced to the notes behind it and every claim sized by how many people said it. Ends with
  opportunity statements ready for an opportunity solution tree, and a list of what the research
  does not show.
type: workflow
theme: discovery-research
best_for:
  - "Making sense of 5 to 30 interviews before anyone proposes a solution"
  - "Separating what customers did and said from what the team concluded"
  - "Producing opportunity statements that trace back to evidence"
  - "Showing a stakeholder what the research does and does not support"
scenarios:
  - "I ran eight dispatcher interviews and have a folder of notes. What do they say?"
  - "Support tickets and interviews seem to disagree. Help me sort what's real"
  - "Turn these plant-visit notes into opportunities for the roadmap discussion"
  - "Leadership wants the insight in one page; I want it traceable"
estimated_time: "45-90 min"
---

# Research Synthesis

## Purpose

Turn a pile of raw research into **themes, insights, and opportunity statements you can defend**.
The skill walks the notes through four moves: **code** what happened, **group** it by affinity,
**write insights** that say something, and **frame opportunities** the team can act on. Every
insight carries the quotes and the count behind it.

The sentence to keep in your head: **synthesis is not summary.** A summary shortens the notes. A
synthesis finds the pattern across them, says what it means, and says how sure you can be.

It is the step between running interviews ([`discovery-interview-prep`](../discovery-interview-prep/SKILL.md))
and structuring what you learned ([`opportunity-solution-tree`](../opportunity-solution-tree/SKILL.md)).

## Input

**Works best with:** Raw notes from interviews, calls, visits, or tickets. Rough is fine. The
closer to what people actually said, the better.

**Also useful:** The research question you started with, who you spoke to (role, segment, how
recruited), and any hypotheses you held going in, so they can be checked rather than confirmed.

Anything supplied with the invocation itself (text after the skill name, a pasted context dump, or
an appended `ARGUMENTS:` line) counts as answers already given. Use it and skip whatever it covers;
don't re-ask.

**Arriving empty-handed? That works too.** The skill opens by asking what you're trying to learn
and what you have, tells you which of your material is usable as-is, and works from whatever you
paste. It never invents quotes, participants, or counts to fill a gap.

**Example invocations:**
- `Synthesize these 8 dispatcher interviews. Question: why do rescheduled days still go wrong?`
- `Here are 40 support tickets and 6 interview notes about commissioning. Find the themes.`

---

## Key Concepts

### Observation, Interpretation, Opinion

The whole skill rests on keeping three things apart:

| | What it is | Example | Where it goes |
|---|---|---|---|
| **Observation** | What a person did or said, in their words | "I rebuild the schedule in a spreadsheet every morning" | Notes and quotes |
| **Interpretation** | What you think it means | "Dispatchers don't trust the auto-schedule" | Insights, labeled as interpretation |
| **Opinion** | What you or a stakeholder already believed | "We need smarter routing" | Hypotheses to test, never evidence |

Most weak synthesis is opinion wearing observation's clothes. Label each claim with the right
one. Use the Fact / Inference / Assumption vocabulary from
[`autonomous-investigation`](../autonomous-investigation/SKILL.md) if you want a shared language
with other research in this library: Fact = observed, Inference = interpreted from observation,
Assumption = believed but not shown.

### The Four Moves

1. **Code.** Break the raw notes into single observations, one idea per note, each tagged with who
   said it and where. This is the slow, necessary step. A note that holds three ideas hides two.
2. **Group.** Cluster similar observations by affinity (what belongs together), letting the
   groups emerge from the notes rather than from your hypotheses. Name each group in the
   customer's terms, as a short phrase ("the 2 p.m. rebuild").
3. **Write insights.** For each group that matters, say what it means: a sentence that tells the
   team something they could be wrong about. "Dispatchers rebuild the day by hand because they
   can't see which jobs are movable" is an insight. "Dispatchers use spreadsheets" is a fact.
4. **Frame opportunities.** Restate each insight as an unmet need in the customer's words, with no
   solution inside it: "I need to know which jobs I can move without calling the customer." That
   is the shape [`opportunity-solution-tree`](../opportunity-solution-tree/SKILL.md) wants.

### Count Everything, Then Say How Sure You Are

Qualitative research is small and purposive. That is fine, provided you report it as what it is.
For every theme record **how many of your participants** showed it ("6 of 8") and **how strongly**
(unprompted and emotional, or only when asked). Do not turn "6 of 8 interviewees" into "75% of
customers." Say instead how the sample was chosen and what it can't speak to.

### Confirmation Is the Default, So Look for the Opposite

People code what they expected to hear. Counter it on purpose: before grouping, write down your
hypotheses; during grouping, tag every observation that **contradicts** one; before concluding,
read the contradictions aloud. A theme with no counter-evidence anywhere deserves a second look,
not a celebration.

### Insight Quality Check

A good insight is **specific** (names who and when), **evidenced** (traces to quotes and a count),
**surprising or decision-relevant** (the team could be wrong without it), and **free of a
solution**. If it passes the "so what?" question, keep it. If you could have written it without
the interviews, drop it.

### What the Research Does Not Show

Every synthesis ends with a short list of **gaps**: who you didn't hear from, questions nobody
answered, claims supported by one voice. That list is as valuable as the insights, because it
decides what to research next and keeps the team from over-reading what you found.

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol when
running this conversationally. If you want the grouping step as a live team session, run it as an
affinity-mapping workshop with those rules.

**Default entry mode:** Guided · set in `pm-skills.config.yaml` (library-wide default or a per-skill override); the user's own choice in the session always wins. On the first turn, offer all three modes, then open in the default without waiting for a pick: Guided asks the first question, Context dump invites the paste, Best guess asks for a one-sentence minimum and drafts with every assumption labeled.

### Anti-Patterns (what this is NOT)
- **Not a transcript summary.** Shortening notes is not finding patterns.
- **Not a place for solutions.** Ideas go in a separate list. Opportunities describe needs.
- **Not statistics.** Eight interviews don't give percentages. Report counts and sampling.
- **Not a verdict.** It reports what the research supports. The team decides what to do.

---

## Application

Use [`template.md`](template.md) for the scaffold.

**Output convention.** Artifact first: the research frame, coded observations, themes with counts,
insights with evidence, opportunity statements, contradictions, gaps. Commentary short, after.
Mark any quote, count, or participant you could not trace to the supplied notes as
`[NEEDS SOURCE]`. Never fill one in.

**If the PM brings a draft synthesis, critique first.** For each insight: does it trace to quotes?
Is a count attached? Is anything an opinion in disguise? Does it contain a solution? Where is the
counter-evidence? Name gaps; offer rewrites last.

### Step 1: Frame the Research
The question you were trying to answer, who you spoke to and how they were chosen, the number of
sessions, and the hypotheses you held going in (write them now, before coding).

### Step 2: Code the Notes
Break notes into single observations, each with a participant tag and, where it matters, whether
it was unprompted. Keep customer words verbatim. Flag anything that contradicts a hypothesis.

### Step 3: Group by Affinity
Cluster observations and name each cluster in the customer's terms. Let clusters emerge. Merge or
split until each cluster holds one idea. Count participants per cluster.

### Step 4: Write Insights
For the clusters that matter most (most participants, strongest emotion, or biggest decision
consequence), write one insight each: who, what, why it matters, labeled as interpretation. Attach
two or three quotes and the count. Run the insight quality check.

### Step 5: Frame Opportunities
Restate each insight as an unmet need in the customer's words, no solution inside. Keep a separate
"ideas heard" list so solutions raised by participants aren't lost or confused with needs.

### Step 6: Read the Contradictions and Name the Gaps
List observations that cut against your hypotheses or against an insight. State who you didn't
hear from and what is supported by one voice. Say how sure you are about each insight (strong,
suggestive, thin) and why.

### Step 7: Hand Off and Hand Back
Point to [`opportunity-solution-tree`](../opportunity-solution-tree/SKILL.md) for structuring the
opportunities, and to [`assumption-mapping`](../assumption-mapping/SKILL.md) for the beliefs the
team is still holding. Close with a short summary (supplied, inferred, unknown) and a numbered
ladder, evidence-favored first, labeled `(Recommended)`: run two more interviews to cover the
missing segment; build the opportunity tree from the strong insights; map the assumptions behind
the leading idea; or take the thin insights back to customers.

---

## Examples

See [`examples/sample.md`](examples/sample.md) (Fieldlight dispatcher interviews, SaaS) and
[`examples/sample-industrial.md`](examples/sample-industrial.md) (Northfield plant-visit notes,
industrial). The second shows contradicting evidence changing an insight.

---

## Common Pitfalls

### Pitfall 1: Summarizing Instead of Synthesizing
**Symptom:** The output is each interview in a shorter paragraph.
**Consequence:** Readers get eight small stories and no pattern.
**Fix:** Code, group, and write insights that span participants.

### Pitfall 2: Confirmation Coding
**Symptom:** Every theme matches the original hypothesis.
**Consequence:** The research confirms what the team already believed, which is the opposite of learning.
**Fix:** Write hypotheses first, tag contradictions, read them before concluding.

### Pitfall 3: Percentages From Small Samples
**Symptom:** "75% of customers want X," from eight interviews.
**Consequence:** Stakeholders treat a qualitative signal as market data.
**Fix:** Report "6 of 8 participants," how they were chosen, and what that can't tell you.

### Pitfall 4: Solutions in the Opportunities
**Symptom:** "Customers need an auto-scheduler."
**Consequence:** The team skips the problem and defends a feature.
**Fix:** State the need in the customer's words with no solution in it.

### Pitfall 5: Insights Nobody Could Be Wrong About
**Symptom:** "Customers value reliability."
**Consequence:** Nothing changes, because nothing was learned.
**Fix:** Make it specific enough that the team could disagree, and trace it to evidence.

### Pitfall 6: Invented Quotes and Counts
**Symptom:** A confident quote or "7 of 10" that is not in the notes.
**Consequence:** One discovered fabrication ends trust in the whole synthesis.
**Fix:** Every quote and count traces to the supplied notes, or is `[NEEDS SOURCE]`.

### Pitfall 7: No Gaps List
**Symptom:** The synthesis reads as complete.
**Consequence:** The team over-reads it and never researches who was missing.
**Fix:** End with who you didn't hear from and what rests on one voice.

---

## References

### Skill Files
- [`template.md`](template.md): research frame, coded observations, themes, insights, opportunities, gaps
- [`examples/sample.md`](examples/sample.md), [`examples/sample-industrial.md`](examples/sample-industrial.md)

### Related Skills
- [`discovery-interview-prep`](../discovery-interview-prep/SKILL.md): upstream; how the research was gathered
- [`discovery-process`](../discovery-process/SKILL.md): the end-to-end process this step sits inside
- [`opportunity-solution-tree`](../opportunity-solution-tree/SKILL.md): downstream; structures the opportunities
- [`assumption-mapping`](../assumption-mapping/SKILL.md): downstream; the beliefs still untested
- [`jobs-to-be-done`](../jobs-to-be-done/SKILL.md): a lens for naming needs
- [`voice-of-customer-miner`](../voice-of-customer-miner/SKILL.md): public-voice mining that can feed the same grouping
- [`autonomous-investigation`](../autonomous-investigation/SKILL.md): the Fact / Inference / Assumption vocabulary
- [`workshop-facilitation`](../workshop-facilitation/SKILL.md): interaction protocol

### External Frameworks
- **Affinity diagramming:** Jiro Kawakita's KJ method, widely used in design research.
- **Opportunities as customer needs:** Teresa Torres, *Continuous Discovery Habits* (2021).
- **Coding qualitative data:** standard practice from qualitative research, for example Johnny Saldaña, *The Coding Manual for Qualitative Researchers*.

### Provenance
Distilled from practitioner experience synthesizing customer research for B2B and industrial products.
