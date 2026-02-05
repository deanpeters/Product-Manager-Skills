---
name: user-story
description: Create clear, concise user stories that combine Mike Cohn's user story format with Gherkin-style acceptance criteria. Use this to translate user needs into actionable development work that focuses on 
type: component
---


## Purpose
Create clear, concise user stories that combine Mike Cohn's user story format with Gherkin-style acceptance criteria. Use this to translate user needs into actionable development work that focuses on outcomes, ensures shared understanding between product and engineering, and provides testable success criteria.

This is not a feature spec—it's a conversation starter that captures *who* benefits, *what* they're trying to do, *why* it matters, and *how* you'll know it works.

## Key Concepts

### The Mike Cohn + Gherkin Format
A user story combines:

**Use Case (Mike Cohn format):**
- **As a** [user persona/role]
- **I want to** [action to achieve outcome]
- **so that** [desired outcome]

**Acceptance Criteria (Gherkin format):**
- **Scenario:** [Brief description of the scenario]
- **Given:** [Initial context or preconditions]
- **and Given:** [Additional preconditions]
- **When:** [Event that triggers the action]
- **Then:** [Expected outcome]

### Why This Structure Works
- **User-centric:** Forces focus on who benefits and why
- **Outcome-focused:** "So that" emphasizes the value delivered, not just the action
- **Testable:** Gherkin acceptance criteria are concrete and verifiable
- **Conversational:** Story is the opening for discussion, not the final spec
- **Shared language:** Product, engineering, and QA all understand the format

### Anti-Patterns (What This Is NOT)
- **Not a task:** "As a developer, I want to refactor the database" (this is a tech task, not user value)
- **Not a feature list:** "I want dashboards, reports, and analytics" (this is too big—needs splitting)
- **Not vague:** "I want a better experience" (unmeasurable, no clear outcome)
- **Not a contract:** Stories are placeholders for conversation, not locked-in specs

### When to Use This
- Translating user needs into development work
- Backlog grooming and sprint planning
- Communicating value to engineering and design
- Ensuring testable acceptance criteria exist before development

### When NOT to Use This
- For pure technical debt or refactoring (use engineering tasks instead)
- When stories are too large (split first—see `user-story-splitting.md`)
- Before understanding the user problem (write a problem statement first)

---

## Application

### Step 1: Gather Context
Before writing a story, ensure you have:
- **User persona:** Who is this for? (reference `proto-persona.md`)
- **Problem understanding:** What need does this address? (reference `problem-statement.md`)
- **Desired outcome:** What does success look like?
- **Constraints:** Technical, time, or scope limitations

**If missing context:** Run discovery interviews or problem validation work first.

---

### Step 2: Write the Use Case

Fill in the template:

```markdown
### User Story [ID]:

- **Summary:** [Brief, memorable title focused on value to the user]

#### Use Case:
- **As a** [user name if available, otherwise persona, otherwise role]
- **I want to** [action user takes to get to outcome]
- **so that** [desired outcome]
```

**Quality checks:**
- **"As a" specificity:** Is this a specific persona (e.g., "trial user") or generic ("user")?
- **"I want to" clarity:** Is this an action the user takes, or a feature you're building?
- **"So that" outcome:** Does this explain the user's motivation? Or is it just restating the action?

**Common mistakes:**
- ❌ "As a user, I want a login button, so that I can log in" (restating the action)
- ✅ "As a trial user, I want to log in with Google, so that I can access the app without creating a new password"

---

### Step 3: Write the Acceptance Criteria

Fill in the template:

```markdown
#### Acceptance Criteria:

- **Scenario:** [Brief, human-readable scenario describing value]
- **Given:** [Initial context or precondition]
- **and Given:** [Additional context or preconditions]
- **and Given:** [Additional context as needed]
- **and Given:** [UI-focused context ensuring 'When' can happen]
- **and Given:** [Outcomes-focused context ensuring 'Then' is delivered]
- **When:** [Event that triggers the action—aligns with 'I want to']
- **Then:** [Expected outcome—aligns with 'so that']
```

**Quality checks:**
- **Multiple Givens are okay:** Preconditions stack up (e.g., "Given I'm logged in" + "Given I have items in my cart")
- **Only one When:** If you need multiple "When" statements, you likely have multiple stories—split them
- **Only one Then:** If you need multiple "Then" statements, you likely have multiple stories—split them
- **Alignment:** Does "When" match "I want to"? Does "Then" match "so that"?

**Red flags:**
- **Multiple Whens/Thens:** Sign of scope creep—split the story (reference `user-story-splitting.md`)
- **Vague Thens:** "Then I see improved performance" (unmeasurable—make it specific)

---

### Step 4: Add a Summary

Write a short, memorable summary that captures the story's value:

```markdown
- **Summary:** [Brief, human-readable title]
```

**Examples:**
- ✅ "Enable Google login for trial users to reduce signup friction"
- ✅ "Bulk delete items to save time for power users"
- ❌ "Add delete button" (feature-centric, not value-centric)

---

### Step 5: Validate and Refine

- **Read aloud to the team:** Does everyone understand who, what, why?
- **Test acceptance criteria:** Can QA write test cases from this?
- **Check for splitting:** If the story feels too big, use `user-story-splitting.md`
- **Ensure testability:** Can you prove "Then" happened?

---

## Examples

### Example 1: Good User Story

```markdown
### User Story 042:

- **Summary:** Enable Google login for trial users to reduce signup friction

#### Use Case:
- **As a** trial user visiting the app for the first time
- **I want to** log in using my Google account
- **so that** I can access the app without creating and remembering a new password

#### Acceptance Criteria:

- **Scenario:** First-time trial user logs in via Google OAuth
- **Given:** I am on the login page
- **and Given:** I have a Google account
- **and Given:** The "Sign in with Google" button is visible
- **When:** I click the "Sign in with Google" button and authorize the app
- **Then:** I am logged into the app and redirected to the onboarding flow
```

**Why this works:**
- Persona is specific ("trial user visiting for the first time")
- Action is clear ("log in using my Google account")
- Outcome explains motivation ("without creating a new password")
- Acceptance criteria are testable (QA can verify each step)
- Only one When, one Then (appropriately scoped)

---

### Example 2: Bad User Story (Too Vague)

```markdown
### User Story 999:

- **Summary:** Improve login experience

#### Use Case:
- **As a** user
- **I want to** better login
- **so that** I can use the app

#### Acceptance Criteria:

- **Scenario:** User logs in
- **Given:** I want to log in
- **When:** I log in
- **Then:** It works better
```

**Why this fails:**
- "User" is too generic (trial user? returning user? admin?)
- "Better login" is not an action (what specifically?)
- "Use the app" is not a specific outcome (everyone wants to use the app)
- Acceptance criteria are untestable ("works better" = unmeasurable)

**How to fix it:**
- Narrow the persona: "trial user," "returning user without password manager," etc.
- Define the action: "log in using Google," "reset my password via email," etc.
- Specify the outcome: "without remembering a new password," "in under 30 seconds," etc.
- Make acceptance criteria falsifiable: "Then I am redirected to the dashboard within 2 seconds"

---

### Example 3: Story That Needs Splitting

```markdown
### User Story 100:

- **Summary:** Manage shopping cart

#### Use Case:
- **As a** shopper
- **I want to** add items, remove items, update quantities, apply coupons, and checkout
- **so that** I can complete my purchase

#### Acceptance Criteria:

- **Scenario:** Shopping cart management
- **Given:** I have items in my cart
- **When:** I add an item
- **Then:** It appears in the cart
- **When:** I remove an item
- **Then:** It disappears from the cart
- **When:** I update quantity
- **Then:** The quantity changes
- **When:** I apply a coupon
- **Then:** The discount is applied
- **When:** I checkout
- **Then:** I proceed to payment
```

**Why this needs splitting:**
- Multiple "When" statements = multiple stories
- Scope is too large for a single sprint
- Different outcomes aren't related (adding items ≠ applying coupons)

**How to split it:**
Use `user-story-splitting.md` to break this into:
1. "Add items to cart"
2. "Remove items from cart"
3. "Update item quantities"
4. "Apply discount coupons"
5. "Checkout and proceed to payment"

Each becomes its own story with focused acceptance criteria.

---

## Common Pitfalls

### Pitfall 1: Technical Tasks Disguised as User Stories
**Symptom:** "As a developer, I want to refactor the API, so that the code is cleaner"

**Consequence:** This is an engineering task, not a user story. No user value is delivered.

**Fix:** If there's no user outcome, it's not a user story—use an engineering task or tech debt ticket instead.

---

### Pitfall 2: "As a User" (Too Generic)
**Symptom:** Every story starts with "As a user"

**Consequence:** No persona clarity. Different users have different needs.

**Fix:** Use specific personas: "As a trial user," "As a paid subscriber," "As an admin," etc. (reference `proto-persona.md`)

---

### Pitfall 3: "So That" Restates "I Want To"
**Symptom:** "I want to click the save button, so that I can save my work"

**Consequence:** No insight into *why* the user cares. Just restating the action.

**Fix:** Dig into the motivation: "so that I don't lose my progress if the page crashes" (real outcome).

---

### Pitfall 4: Multiple When/Then Statements
**Symptom:** Acceptance criteria with 5 "When" statements and 5 "Then" statements

**Consequence:** Story is too big. Likely multiple features bundled together.

**Fix:** Split the story using `user-story-splitting.md`. Each When/Then pair should be its own story (or at least evaluated for splitting).

---

### Pitfall 5: Untestable Acceptance Criteria
**Symptom:** "Then the user has a better experience" or "Then it's faster"

**Consequence:** QA can't verify success. Ambiguous definition of "done."

**Fix:** Make it measurable: "Then the page loads in under 2 seconds" or "Then the user sees a success confirmation message."

---

## References

### Related Skills
- `user-story-splitting.md` — How to break large stories into smaller ones
- `proto-persona.md` — Defines the "As a [persona]" section
- `problem-statement.md` — Stories should address validated problems
- `epic-hypothesis.md` — Epics decompose into user stories

### External Frameworks
- Mike Cohn, *User Stories Applied* (2004) — Origin of the "As a / I want / so that" format
- Gherkin (Cucumber) — "Given/When/Then" acceptance criteria format
- INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable)

### Dean's Work
- [Link to relevant Dean Peters' Substack articles if applicable]

---

**Skill type:** Component
**Suggested filename:** `user-story.md`
**Suggested placement:** `/skills/components/`
**Dependencies:** References `proto-persona.md`, `problem-statement.md`
**Used by:** `user-story-splitting.md`, `epic-hypothesis.md`
