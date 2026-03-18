---
name: user-story-mapping
description: Create a user story map that lays out activities, steps, tasks, and release slices. Use when planning a workflow, backlog, or MVP around the user journey.
intent: >-
  Visualize the user journey by creating a hierarchical map that breaks down high-level activities into steps and tasks, organized left-to-right as a narrative flow. Use this to build shared understanding across product, design, and engineering, prioritize features based on user workflows, and identify gaps or opportunities in the user experience.
type: component
---


## Purpose
Visualize the user journey by creating a hierarchical map that breaks down high-level activities into steps and tasks, organized left-to-right as a narrative flow. Use this to build shared understanding across product, design, and engineering, prioritize features based on user workflows, and identify gaps or opportunities in the user experience.

## Key Concepts

### The Jeff Patton Story Mapping Framework
Invented by Jeff Patton, story mapping organizes work into a 2D structure:

**Horizontal axis (left-to-right):** User journey over time
- **Backbone:** High-level activities the user performs
- **Steps:** Specific actions within each activity
- **Tasks:** Detailed work required to complete each step

**Vertical axis (top-to-bottom):** Priority and releases
- **Top rows:** Essential tasks (MVP / Release 1)
- **Lower rows:** Nice-to-have tasks (Future releases)

### Story Map Structure

```
Segment → Persona → Narrative (User's goal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Activity 1] → [Activity 2] → [Activity 3] → [Activity 4] → [Activity 5]
     ↓              ↓              ↓              ↓              ↓
  [Step 1.1]     [Step 2.1]     [Step 3.1]     [Step 4.1]     [Step 5.1]
  [Step 1.2]     [Step 2.2]     [Step 3.2]     [Step 4.2]     [Step 5.2]
  [Step 1.3]     [Step 2.3]     [Step 3.3]     [Step 4.3]     [Step 5.3]
     ↓              ↓              ↓              ↓              ↓
  [Task 1.1.1]   [Task 2.1.1]   [Task 3.1.1]   [Task 4.1.1]   [Task 5.1.1]
  [Task 1.1.2]   [Task 2.1.2]   [Task 3.1.2]   [Task 4.1.2]   [Task 5.1.2]
  [Task 1.1.3]   [Task 2.1.3]   [Task 3.1.3]   [Task 4.1.3]   [Task 5.1.3]
  ...            ...            ...            ...            ...
```

### Anti-Patterns (What This Is NOT)
- **Not a Gantt chart:** This isn't project management—it's user journey visualization
- **Not a feature list:** Activities aren't features—they're user behaviors
- **Not static:** Story maps evolve as you learn more about users

---

## Application

### Step 1: Define the Context

Use `template.md` for the full fill-in structure.

#### Segment
Who are you building for?

```markdown
### Segment:
- [Specify the target segment, e.g., "Small business owners using DIY accounting software"]
```

**Quality checks:**
- **Specific:** Not "users" but "enterprise IT admins" or "freelance designers"

---

#### Persona
Provide details about the persona within this segment (reference `skills/proto-persona/SKILL.md`).

```markdown
### Persona:
- [Describe the persona: demographics, behaviors, pains, goals]
```

**Example:**
- "Sarah, 35-year-old freelance graphic designer, manages 5-10 client projects at once, struggles with invoicing and payment tracking, wants to spend less time on admin and more time designing"

---

### Step 2: Define the Narrative
What is the user trying to accomplish? Frame this as a Jobs-to-be-Done statement (reference `skills/jobs-to-be-done/SKILL.md`).

```markdown
### Narrative:
- [Concise narrative of the persona's objective, e.g., "Complete a client project from kickoff to final payment"]
```

**Quality checks:**
- **Outcome-focused:** Not "use the product" but "deliver a client project on time and get paid"
- **One sentence:** If it takes more than one sentence, the scope may be too broad

---

### Step 3: Identify Activities (Backbone)
List 3-5 high-level activities the persona engages in to fulfill the narrative. These form the backbone of your map.

```markdown
### Activities:
1. [Activity 1, e.g., "Negotiate project scope and pricing"]
2. [Activity 2, e.g., "Execute design work"]
3. [Activity 3, e.g., "Deliver final assets to client"]
4. [Activity 4, e.g., "Send invoice and receive payment"]
5. [Activity 5, optional]
```

**Quality checks:**
- **Sequential:** Activities happen in order (left-to-right)
- **User actions:** Describe what the user *does*, not what the product *provides*
- **3-5 activities:** Too few = oversimplified, too many = overwhelming

---

### Step 4: Break Activities into Steps
For each activity, list 3-5 steps that detail how the activity is carried out.

```markdown
### Steps:

**For Activity 1: [Activity Name]**
- Step 1: [Detail step 1, e.g., "Review client brief"]
- Step 2: [Detail step 2, e.g., "Draft project proposal"]
- Step 3: [Detail step 3, e.g., "Negotiate timeline and budget"]
- Step 4: [Optional step 4]
- Step 5: [Optional step 5]

**For Activity 2: [Activity Name]**
- Step 1: [Detail step 1]
- Step 2: [Detail step 2]
...
```

**Quality checks:**
- **Actionable:** Each step is something the user does
- **Observable:** You could watch someone perform this step
- **Logical sequence:** Steps follow a natural order

---

### Step 5: Break Steps into Tasks
For each step, list 5-7 tasks that must be completed.

```markdown
### Tasks:

**For Activity 1, Step 1: [Step Name]**
- Task 1: [Detail task 1, e.g., "Read client brief document"]
- Task 2: [Detail task 2, e.g., "Identify key deliverables"]
- Task 3: [Detail task 3, e.g., "Note budget constraints"]
- Task 4: [Detail task 4, e.g., "Clarify timeline expectations"]
- Task 5: [Detail task 5, e.g., "List open questions for client"]
- Task 6: [Optional task 6]
- Task 7: [Optional task 7]

**For Activity 1, Step 2: [Step Name]**
- Task 1: [Detail task 1]
...
```

**Quality checks:**
- **Granular:** Tasks are small, specific actions
- **User-facing or behind-the-scenes:** Include both (e.g., "Send email" and "Receive confirmation")
- **Prioritizable:** You'll prioritize tasks vertically (top = essential, bottom = nice-to-have)

---

### Step 6: Prioritize Vertically
Arrange tasks top-to-bottom by priority:
- **Top rows:** MVP / Release 1 (must-have)
- **Middle rows:** Release 2 (important but not critical)
- **Bottom rows:** Future / Nice-to-have

Draw horizontal "release lines" to demarcate scope.

---

### Step 7: Identify Gaps and Opportunities
Review the map and ask:
- Are there missing steps or tasks?
- Are there pain points we're not addressing?
- Are there opportunities to delight users?
- Do all activities flow logically?

---

## Examples

See `examples/sample.md` for a full story map example.

---

## Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Activities are features, not user behaviors | "Activity 1: Use the dashboard. Activity 2: Generate reports." | Reframe as user actions: "Monitor project progress," "Summarize work for stakeholders" |
| Too many activities | 10+ activities across the backbone | Consolidate. You're likely mixing activities with steps. Aim for 3-5. |
| Tasks are too vague | "Task 1: Do the thing" | Be specific: "Enter client email address in the 'Bill To' field" |
| Ignoring vertical prioritization | All tasks at the same level — no MVP vs. future releases | Draw release lines. Force hard choices about what's MVP. |
| Mapping in isolation | PM creates the map alone, then presents to team | Map collaboratively with product, design, and engineering |

---

## References

### Related Skills
- `skills/proto-persona/SKILL.md` — Defines the persona for the story map
- `skills/jobs-to-be-done/SKILL.md` — Informs the narrative and activities
- `skills/user-story/SKILL.md` — Tasks from the map become user stories
- `skills/problem-statement/SKILL.md` — Problem statement frames the narrative

### External Frameworks
- Jeff Patton, *User Story Mapping* (2014) — Origin of the story mapping technique
- Teresa Torres, *Continuous Discovery Habits* (2021) — Opportunity solution trees (complementary to story maps)

### Dean's Work
- User Story Mapping Prompt (adapted from Jeff Patton's methodology)

### Provenance
- Adapted from `prompts/user-story-mapping.md` in the `https://github.com/deanpeters/product-manager-prompts` repo.

---

**Skill type:** Component
**Suggested filename:** `user-story-mapping.md`
**Suggested placement:** `/skills/components/`
**Dependencies:** References `skills/proto-persona/SKILL.md`, `skills/jobs-to-be-done/SKILL.md`, `skills/user-story/SKILL.md`, `skills/problem-statement/SKILL.md`
