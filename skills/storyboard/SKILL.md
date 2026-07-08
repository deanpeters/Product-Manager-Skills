---
name: storyboard
description: Create a six-frame storyboard that shows a user's journey from problem to solution. Use when you need a fast narrative for alignment, concept reviews, or demos.
compatibility: opencode
argument-hint: "[user and problem]"
metadata:
  intent: >-
    Create a 6-frame visual narrative that tells the story of a user's journey from problem to solution, using the classic storytelling arc to build empathy, illustrate value, and make abstract product
    concepts concrete. Use this to align stakeholders, pitch features, communicate vision, or test if your solution resonates emotionally before building it.
  type: component
---


## Purpose
Create a 6-frame visual narrative that tells the story of a user's journey from problem to solution, using the classic storytelling arc to build empathy, illustrate value, and make abstract product concepts concrete. Use this to align stakeholders, pitch features, communicate vision, or test if your solution resonates emotionally before building it.

This is not a UI mockup—it's a storytelling tool that brings the human side of your product to life.

## Input

**Works best with:** The user and the problem-to-solution story you want told.
**Also useful:** The emotional arc, key moments you know must appear, and the audience for the storyboard (execs, design review, sales).

Anything supplied with the invocation itself — text after the skill name, a pasted context dump, or an appended `ARGUMENTS:` line — counts as answers already given. Use it and skip whatever it covers; don't re-ask.

**Arriving empty-handed? That works too.** The skill asks who the user is and what changes for them, then builds the six frames.

**Example invocation:** `Storyboard: overwhelmed pharmacy tech discovers our auto-refill queue and ends the day on time — for next week's concept review.`

## Key Concepts

### The 6-Frame Storyboard Structure
Based on classic narrative arcs, the 6-frame format follows this pattern:

1. **Frame 1: Main Character** — Introduce the persona and their context
2. **Frame 2: The Problem Emerges** — Show the challenge or obstacle they face
3. **Frame 3: The "Oh Crap" Moment** — Escalate the problem to create urgency
4. **Frame 4: The Solution Appears** — Introduce your product/feature
5. **Frame 5: The "Aha" Moment** — Show the user experiencing the breakthrough
6. **Frame 6: Life After the Solution** — Illustrate the improved state

### Why This Works
- **Emotional engagement:** Stories create empathy in ways specs can't
- **Concrete over abstract:** Visual narrative makes vague concepts tangible
- **Memorable:** People remember stories better than feature lists
- **Alignment tool:** Stakeholders can react to a story and give feedback
- **Low-fidelity:** Doesn't require polished design—sketches work great

### Anti-Patterns (What This Is NOT)
- **Not a user flow diagram:** This is emotional storytelling, not process documentation
- **Not a feature demo:** Focus on user outcomes, not product capabilities
- **Not marketing copy:** Authentic narrative, not hype

### When to Use This
- Pitching a new product or feature to stakeholders
- Aligning teams on user value (product, design, engineering, execs)
- Testing if a product idea resonates emotionally
- Communicating vision at all-hands or investor meetings
- Validating problem/solution fit before building

### When NOT to Use This
- For technical implementation details (use architecture diagrams instead)
- When the user problem is trivial or well-understood
- As a replacement for user research (storyboards illustrate insights, don't create them)

---

## Application

Use `template.md` for the full fill-in structure.

### Step 1: Gather Context
Before creating the storyboard, ensure you have:
- **Persona clarity:** Who is the main character? (reference `skills/proto-persona/SKILL.md`)
- **Problem understanding:** What challenge do they face? (reference `skills/problem-statement/SKILL.md`)
- **Solution definition:** What product/feature will help? (reference `skills/positioning-statement/SKILL.md`)
- **Desired outcome:** What does success look like for the user?

**If missing context:** Run discovery work first. Don't fabricate personas or problems.

---

### Step 2: Answer the 7 Storyboard Questions

Ask these questions one at a time to develop the narrative:

1. **Who is the main character experiencing this problem?** (Name, age, role, context)
2. **Describe the problem or challenge the main character is facing.**
3. **Describe the "Oh Crap" moment where the problem creates a major issue.**
4. **How is the solution introduced to the main character?**
5. **Describe the main character using the solution and experiencing an "Aha" moment.**
6. **What is life like for the main character after using the solution?**
7. **Do you have any specific visual style or rendering instructions?** (Default: fat-marker sharpie sketches, minimal and monochrome)

---

### Step 3: Write the 6-Frame Narrative

Based on the answers above, draft the narrative:

```markdown
## Generated 6-Frame Storyline

**Frame 1: Introducing the Main Character**
- [Insert description of the main character, their setting, and context]
- [Example: "Sarah, 35, is a freelance graphic designer juggling 10 client projects from her home office"]

**Frame 2: The Problem Emerges**
- [Describe the main character's challenge and how it affects their life]
- [Example: "She's drowning in invoice tracking—8 hours per month chasing late payments via spreadsheets and email"]

**Frame 3: The 'Oh Crap' Moment**
- [Highlight the escalation of the problem into a major issue]
- [Example: "A major client's payment is 2 weeks overdue. Sarah realizes she forgot to follow up because she was focused on design work. The client has now gone silent, and she's anxious about cash flow."]

**Frame 4: The Solution Appears**
- [Explain how the solution is introduced and the main character's initial reaction]
- [Example: "Sarah discovers SmartInvoice, a tool that automatically sends payment reminders at optimal times. She's skeptical—will it sound too pushy?—but decides to try it."]

**Frame 5: The 'Aha' Moment**
- [Show the main character using the solution and experiencing a breakthrough]
- [Example: "Two days later, Sarah receives a notification: 'Client XYZ just paid!' The AI-timed reminder worked—no awkward follow-up call needed. She feels relieved and in control."]

**Frame 6: Life After the Solution**
- [Describe the resolution and how life improves after overcoming the problem]
- [Example: "Sarah now spends 30 minutes per month on invoicing instead of 8 hours. She's reclaimed her evenings, spending time with family instead of chasing payments. Her cash flow is predictable, and her anxiety is gone."]

**Optional Visual Elements**
- [If no visual style specified: "Use fat-marker, sharpie-style sketches—minimal, monochrome, hand-drawn feel"]
- [If visual elements provided: "Include user-provided images, GIFs, or icons"]
```

---

### Step 4: Visualize Each Frame

For each frame, create or describe the visual:

**Frame 1: Main Character**
- **Visual:** Sarah at her desk, surrounded by sticky notes, laptop open, coffee cup
- **Mood:** Busy, slightly stressed
- **Tools:** DALL·E, MidJourney, hand-drawn sketches

**Frame 2: The Problem Emerges**
- **Visual:** Sarah staring at a spreadsheet labeled "Overdue Invoices," multiple browser tabs open
- **Mood:** Overwhelmed
- **Details:** Clock showing 10pm, to-do list getting longer

**Frame 3: The 'Oh Crap' Moment**
- **Visual:** Sarah's phone showing "Day 14: Payment Overdue from Client XYZ" notification. Her face shows worry.
- **Mood:** Anxious, urgent
- **Details:** Calendar showing upcoming rent due date

**Frame 4: The Solution Appears**
- **Visual:** Sarah's laptop showing the SmartInvoice landing page with headline "Stop Chasing Payments"
- **Mood:** Curious, hopeful
- **Details:** Testimonial quote: "Saved me 5 hours/month"

**Frame 5: The 'Aha' Moment**
- **Visual:** Sarah's phone showing notification "Client XYZ just paid! $5,000 received." She's smiling, relieved.
- **Mood:** Joy, relief, empowerment
- **Details:** Background shows sunset—she's done with work early

**Frame 6: Life After the Solution**
- **Visual:** Sarah playing with her kids in the backyard, laptop closed on the patio table
- **Mood:** Peaceful, balanced
- **Details:** Clock showing 6pm (not 10pm anymore)

---

### Step 5: Test the Storyboard

Ask these questions:
1. **Is the main character relatable?** Would your target persona recognize themselves?
2. **Is the problem visceral?** Do people *feel* the frustration in Frame 2-3?
3. **Is the "Oh Crap" moment real?** Does it escalate the problem authentically?
4. **Is the solution introduction natural?** Or does it feel forced/contrived?
5. **Is the "Aha" moment believable?** Can users imagine experiencing this?
6. **Is the "after" state aspirational?** Would users want this outcome?

If any answer is "no," revise.

---

## Examples

See `examples/sample.md` for full storyboard examples.

Mini example excerpt:

```markdown
**Frame 1:** Sarah, 35, freelance designer juggling 10 clients\n**Frame 2:** Spends 8 hours/month chasing overdue invoices\n**Frame 3:** $5,000 payment is 2 weeks overdue\n```

---

## Common Pitfalls

### Pitfall 1: Generic Persona
**Symptom:** "Meet User, a busy professional"

**Consequence:** No one identifies with this character.

**Fix:** Get specific: "Meet Sarah, 35, freelance designer, juggling 10 clients, home office, loves design but hates admin."

---

### Pitfall 2: Weak Problem
**Symptom:** "User has a problem with efficiency"

**Consequence:** Problem doesn't resonate emotionally.

**Fix:** Make it visceral: "Sarah spends 8 hours/month chasing overdue invoices, missing family dinners, feeling anxious about cash flow."

---

### Pitfall 3: Forced Solution Introduction
**Symptom:** "User magically discovers our product"

**Consequence:** Feels contrived, not authentic.

**Fix:** Show realistic discovery: "Sarah sees a recommendation in a designer forum" or "Sarah's colleague mentions it."

---

### Pitfall 4: Feature-Centric "Aha" Moment
**Symptom:** "User sees the dashboard and loves the features"

**Consequence:** No emotional payoff.

**Fix:** Focus on outcome: "Sarah gets notification: '$5,000 received!' She's relieved—no awkward call needed."

---

### Pitfall 5: Vague "After" State
**Symptom:** "Life is better now"

**Consequence:** Not aspirational or concrete.

**Fix:** Be specific: "Sarah leaves work at 6pm now, spending evenings with her kids instead of chasing clients. On-time payments jumped from 50% to 80%."

---

## References

### Related Skills
- `skills/proto-persona/SKILL.md` — Defines the main character
- `skills/problem-statement/SKILL.md` — Frames the problem for Frame 2-3
- `skills/positioning-statement/SKILL.md` — Informs the solution introduction in Frame 4
- `skills/jobs-to-be-done/SKILL.md` — Informs the desired outcome in Frame 6

### External Frameworks
- Joseph Campbell, *The Hero's Journey* (1949) — Classic narrative structure
- Pixar's story rules — "Once upon a time... Every day... Until one day..."
- Donald Miller, *Building a StoryBrand* (2017) — Story-driven marketing frameworks

### Dean's Work
- Storyboard Storytelling Prompt (6-Frame Storyline Generator)

### Provenance
- Adapted from `prompts/storyboard-storytelling-prompt.md` in the `https://github.com/deanpeters/product-manager-prompts` repo.

---

**Skill type:** Component
**Suggested filename:** `storyboard.md`
**Suggested placement:** `/skills/components/`
**Dependencies:** References `skills/proto-persona/SKILL.md`, `skills/problem-statement/SKILL.md`, `skills/positioning-statement/SKILL.md`, `skills/jobs-to-be-done/SKILL.md`
