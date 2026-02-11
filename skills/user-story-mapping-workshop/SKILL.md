---
name: user-story-mapping-workshop
description: Guide product managers through creating a user story map by asking adaptive questions about the system, users, workflow, and priorities—then generating a two-dimensional map with backbone (activitie
type: interactive
---


## Purpose
Guide product managers through creating a user story map by asking adaptive questions about the system, users, workflow, and priorities—then generating a two-dimensional map with backbone (activities), user tasks, and release slices. Use this to move from flat backlogs to visual story maps that communicate the big picture, identify missing functionality, and enable meaningful release planning—avoiding "context-free mulch" where stories lose connection to the overall system narrative.

This is not a backlog generator—it's a visual communication framework that organizes work by user workflow (horizontal) and priority (vertical).

## Key Concepts

### What is a User Story Map?

A story map (Jeff Patton) organizes user stories in **two dimensions**:

**Horizontal axis (left to right):** Activities arranged in narrative/workflow order—the sequence you'd use explaining the system to someone

**Vertical axis (top to bottom):** Priority within each activity, with the most essential tasks at the top

**Structure:**
```
Backbone (Activities across top)
↓
User Tasks (descending vertically by priority)
↓
Details/Acceptance Criteria (at the bottom)
```

### Key Principles

**The Backbone:** Essential activities form the system's structural core—these aren't prioritized against each other; they're the narrative flow.

**Walking Skeleton:** The highest-priority tasks across all activities form the minimal viable product—the smallest end-to-end functionality.

**Ribs:** Supporting tasks descend vertically under each activity, indicating priority through placement.

**Left-to-Right, Top-to-Bottom Build Strategy:** Build incrementally across all major features rather than completing one feature fully before starting another.

### Why This Works
- **Visual communication:** Story maps remain displayed as information radiators, maintaining focus on the big picture
- **Narrative structure:** Organizes by user workflow, not technical architecture
- **Release planning:** Horizontal slices reveal MVPs and incremental releases
- **Gap identification:** Reveals missing functionality that flat backlogs obscure

### Anti-Patterns (What This Is NOT)
- **Not a Gantt chart:** Story maps show priority, not time estimates
- **Not technical architecture:** Maps follow user workflow, not system layers (UI → API → DB)
- **Not a project plan:** It's a discovery and communication tool, not a schedule

### When to Use This
- Starting a new product or major feature
- Reframing an existing backlog (moving from flat list to visual map)
- Aligning stakeholders on scope and priorities
- Planning MVP or incremental releases

### When NOT to Use This
- Single-feature projects (story map overkill)
- When backlog is already well-understood and prioritized
- For technical refactoring work (no user workflow to map)

---

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the default interaction protocol for this skill.

It defines:
- session heads-up + entry mode (Guided, Context dump, Best guess)
- one-question turns with plain-language prompts
- progress labels (for example, Context Qx/8 and Scoring Qx/5)
- interruption handling and pause/resume behavior
- numbered recommendations at decision points
- quick-select numbered response options for regular questions (include `Other (specify)` when useful)

This file defines the domain-specific assessment content. If there is a conflict, follow this file's domain logic.

## Application

This interactive skill asks **up to 5 adaptive questions**, offering **3-4 enumerated options** at each step.

Use `template.md` for the facilitation agenda and outputs checklist.

Interaction pattern: Pair with `skills/workshop-facilitation/SKILL.md` when you want a one-step-at-a-time flow with numbered recommendations at decision points and quick-select options for regular questions. If the user asks for a single-shot output, skip the multi-turn facilitation.

---

### Step 0: Gather Context (Before Questions)

**Agent suggests:**

Before we create your story map, let's gather context:

**Product/Feature Context:**
- What system or feature are you mapping?
- Product concept, PRD draft, or existing backlog
- Website copy, positioning materials, or user flows
- Existing user stories (if transitioning from flat backlog)

**User Context:**
- Target personas or user segments
- User research, interviews, or journey maps
- Jobs-to-be-done or problem statements

**You can paste this content directly, or describe the system briefly.**

---

### Question 1: Define Scope

**Agent asks:**
"What are you mapping? (What's the scope?)"

**Offer 4 enumerated options:**

1. **Entire product** — "Full end-to-end system from discovery to completion" (Common for new products or full rewrites)
2. **Major feature area** — "Specific workflow within a larger product (e.g., 'onboarding,' 'checkout,' 'reporting')" (Common for feature launches)
3. **User journey** — "Specific user goal or job-to-be-done (e.g., 'hire a contractor,' 'file taxes')" (Common for JTBD-driven mapping)
4. **Redesign/refactor** — "Existing product/feature being rebuilt or simplified" (Common for legacy system modernization)

**Or describe your specific scope.**

**User response:** [Selection or custom]

---

### Question 2: Identify Users/Personas

**Agent asks:**
"Who are the primary users for this map? (List personas or user segments.)"

**Offer 4 enumerated options:**

1. **Single persona** — "One primary user type (e.g., 'small business owner')" (Simplifies mapping, good for MVP)
2. **Multiple personas, shared workflow** — "Different user types, same core activities (e.g., 'buyer' and 'seller' both browse listings)" (Common for marketplaces)
3. **Multiple personas, different workflows** — "Different user types with distinct workflows (e.g., 'admin' vs. 'end user')" (Requires separate maps or swim lanes)
4. **Roles within organization** — "Different job functions (e.g., 'PM,' 'designer,' 'engineer')" (Common for internal tools)

**Or describe your users.**

**Adaptation:** Use personas from context provided in Step 0 (proto-personas, JTBD, etc.)

**User response:** [Selection or custom]

---

### Question 3: Generate Backbone (Activities)

**Agent says:**
"Let's build the backbone—the narrative flow of activities users perform to accomplish their goal."

**Agent generates 5-8 activities** based on scope (Q1) and users (Q2), arranged left-to-right in workflow order.

**Example (if Scope = "E-commerce checkout"):**

```
Backbone Activities (left to right):

1. Browse Products
2. Add to Cart
3. Review Cart
4. Enter Shipping Info
5. Enter Payment Info
6. Confirm Order
7. Receive Confirmation
```

**Agent asks:**
"Does this backbone capture the full workflow? Should we add, remove, or reorder activities?"

**User response:** [Approve, modify, or add custom activities]

---

### Question 4: Generate User Tasks (Under Each Activity)

**Agent says:**
"Now let's add user tasks under each activity, organized by priority (top = must-have, bottom = nice-to-have)."

**Agent generates 3-5 user tasks per activity**, arranged vertically by priority.

**Example (for Activity 2: "Add to Cart"):**

```
Add to Cart (Activity)
├─ Add single item to cart (must-have, walking skeleton)
├─ Adjust quantity (must-have)
├─ Add multiple items at once (should-have)
├─ Save item for later (nice-to-have)
└─ Add gift wrapping (nice-to-have)
```

**Agent repeats for all backbone activities**, showing the full map.

**Agent asks:**
"Does this capture the key tasks? Are priorities correct (top = MVP, bottom = later releases)?"

**User response:** [Approve, modify, or add custom tasks]

---

### Question 5: Identify Release Slices (Walking Skeleton + Increments)

**Agent says:**
"Let's define release slices by drawing horizontal lines across the map."

**Agent generates 3 release slices:**

**Release 1 (Walking Skeleton):** Top-priority tasks across all activities—minimal end-to-end functionality

**Release 2 (Next Increment):** Second-priority tasks that enhance the core workflow

**Release 3 (Polish/Expansion):** Third-priority tasks (nice-to-haves, edge cases, optimizations)

**Example:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Release 1 (Walking Skeleton):
- Browse products (basic list view)
- Add single item to cart
- Review cart (line items + total)
- Enter shipping info (name, address)
- Enter payment info (credit card only)
- Confirm order (basic confirmation)
- Receive email confirmation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Release 2 (Enhanced):
- Product filtering/search
- Adjust quantity in cart
- Save for later
- Multiple shipping options
- Multiple payment methods
- Order tracking link
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Release 3 (Polish):
- Product recommendations
- Guest checkout
- Gift wrapping
- Promo codes
- Advanced payment options
- Post-purchase surveys
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Agent asks:**
"Do these release slices make sense? Should we adjust scope or priorities?"

**User response:** [Approve or modify]

---

### Output: User Story Map

After completing the flow, the agent outputs:

```markdown
# User Story Map: [Scope from Q1]

**Users:** [From Q2]
**Date:** [Today's date]

---

## Backbone (Activities)

[Activity 1] → [Activity 2] → [Activity 3] → [Activity 4] → [Activity 5] → [Activity 6]

---

## Full Story Map

### [Activity 1: Name]
- **[Task 1.1]** — Must-have (Release 1)
- **[Task 1.2]** — Should-have (Release 2)
- **[Task 1.3]** — Nice-to-have (Release 3)

### [Activity 2: Name]
- **[Task 2.1]** — Must-have (Release 1)
- **[Task 2.2]** — Should-have (Release 2)
- **[Task 2.3]** — Nice-to-have (Release 3)

[...repeat for all activities...]

---

## Release Slices

### Release 1: Walking Skeleton (MVP)
**Goal:** Minimal end-to-end functionality

**Stories:**
- [Task 1.1] — [Activity 1]
- [Task 2.1] — [Activity 2]
- [Task 3.1] — [Activity 3]
- [Task 4.1] — [Activity 4]
- [Task 5.1] — [Activity 5]
- [Task 6.1] — [Activity 6]

**Why this is the walking skeleton:** Delivers complete workflow with simplest version of each activity.

---

### Release 2: Enhanced Functionality
**Goal:** Improve core workflow with priority enhancements

**Stories:**
- [Task 1.2] — [Activity 1]
- [Task 2.2] — [Activity 2]
- [Task 3.2] — [Activity 3]
[...]

---

### Release 3: Polish & Expansion
**Goal:** Nice-to-haves, edge cases, optimizations

**Stories:**
- [Task 1.3] — [Activity 1]
- [Task 2.3] — [Activity 2]
[...]

---

## Next Steps

1. **Refine stories:** Use `skills/user-story/SKILL.md` to write detailed stories with acceptance criteria
2. **Estimate effort:** Score stories (story points, t-shirt sizes)
3. **Validate with stakeholders:** Walk through map left-to-right, confirm priorities
4. **Display map:** Print/post as information radiator for ongoing reference

---

**Ready to write user stories? Let me know if you'd like to refine the map or break down specific stories.**
```

---

## Examples

### Example 1: Good Story Map (E-commerce Checkout)

**Q1 Response:** "Major feature area — E-commerce checkout workflow"

**Q2 Response:** "Single persona — Online shopper"

**Q3 - Backbone Generated:**
```
Browse → Add to Cart → Review Cart → Enter Shipping → Enter Payment → Confirm → Receive Confirmation
```

**Q4 - User Tasks Generated:**

```
Browse Products
├─ View product list (R1)
├─ Search/filter (R2)
└─ Product recommendations (R3)

Add to Cart
├─ Add single item (R1)
├─ Adjust quantity (R2)
└─ Save for later (R3)

Review Cart
├─ View line items + total (R1)
├─ Apply promo code (R2)
└─ Estimate shipping cost (R3)

[...etc...]
```

**Q5 - Release Slices:**
- **Release 1:** Walking skeleton—basic flow with no extras
- **Release 2:** Search, quantity adjustment, promo codes
- **Release 3:** Recommendations, guest checkout, gift options

**Why this works:**
- Backbone follows user narrative (not technical layers)
- Walking skeleton delivers end-to-end value
- Incremental releases add sophistication without breaking core flow

---

### Example 2: Bad Story Map (Technical Layers)

**Backbone (WRONG):**
```
UI Layer → API Layer → Database Layer → Deployment
```

**Why this fails:**
- Not user-centric (users don't care about technical architecture)
- Can't deliver end-to-end value incrementally
- Waterfall thinking disguised as story mapping

**Fix:**
- Map by user workflow: "Sign Up → Configure Settings → Invite Team → Start Project"
- Each release delivers full workflow, not a single layer

---

## Common Pitfalls

### Pitfall 1: Flat Backlog in Disguise
**Symptom:** Story map is just a vertical list, no horizontal narrative

**Consequence:** Loses communication benefit; still "context-free mulch"

**Fix:** Force horizontal structure—activities across top, tasks descending vertically

---

### Pitfall 2: Technical Architecture as Backbone
**Symptom:** Backbone = "Frontend → Backend → Database"

**Consequence:** Not user-centric, can't deliver value incrementally

**Fix:** Backbone should follow user workflow, not system layers

---

### Pitfall 3: Feature-Complete Waterfall
**Symptom:** Release 1 = "Build Activity 1 fully," Release 2 = "Build Activity 2 fully"

**Consequence:** No end-to-end value until all activities complete

**Fix:** Walking skeleton = thin slice across ALL activities, incrementally enhanced

---

### Pitfall 4: Too Much Detail Too Soon
**Symptom:** Trying to map every edge case and acceptance criterion upfront

**Consequence:** Analysis paralysis, lost big picture

**Fix:** Start with backbone + high-level tasks, refine later

---

### Pitfall 5: Map Hidden in a Tool
**Symptom:** Story map lives in Jira/Miro, never displayed

**Consequence:** Loses value as information radiator

**Fix:** Print/post map physically; make it visible to team daily

---

## References

### Related Skills
- `skills/user-story-mapping/SKILL.md` — Component skill with story mapping template
- `skills/user-story/SKILL.md` — Converts map tasks into detailed user stories
- `skills/proto-persona/SKILL.md` — Defines users for mapping
- `skills/jobs-to-be-done/SKILL.md` — Informs backbone activities

### External Frameworks
- Jeff Patton, *User Story Mapping* (2014) — Origin of story mapping framework
- Jeff Patton, "The New User Story Backlog is a Map" (blog) — Explains backbone concept

### Dean's Work
- [If Dean has story mapping resources, link here]

### Provenance
- Derived from `skills/user-story/SKILL.md`, `skills/user-story-splitting/SKILL.md`, and `skills/user-story-mapping/SKILL.md`.

---

**Skill type:** Interactive
**Suggested filename:** `user-story-mapping-workshop.md`
**Suggested placement:** `/skills/interactive/`
**Dependencies:** Uses `skills/user-story-mapping/SKILL.md`, `skills/user-story/SKILL.md`, `skills/proto-persona/SKILL.md`
