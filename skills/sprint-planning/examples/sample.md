# Sprint Planning Example: SaaS

**Team:** Fieldlight onboarding squad (6 engineers, 1 designer), 2-week sprint
**Last sprint:** planned 14, completed 9, carried 5 (third sprint in a row near 65%)
**Why this example exists:** the team's list was 14 tickets with no goal. A goal and honest
capacity turned it into a plan the team believed.

---

```markdown
## Sprint goal
> A new dispatcher can load a day and run their first optimization without asking for help.

Specific (observable in a usability session) · Valuable (the 7-day activation gap) · Flexible (guided
tour, defaults, or error messages could each get there).

## Capacity (set by the team)
| Person | Days | Leave/meetings/support | Focused |
|---|---|---|---|
| 6 engineers | 60 | 3 leave, 9 meetings, 6 support rotation | 42 |
| Designer | 10 | 2 meetings | 8 |
**Focus factor:** 0.75 → ~31 focused days of work.
**Recent throughput:** 9-10 items; plan for 10, not 14.
**Slack held:** 2 items (20%): production issues and review.

## Selected work (serves the goal)
| Order | Item | Ready? | Size |
|---|---|---|---|
| 1 | Default depot address from the account | Yes | S |
| 2 | First-run guided tour for load-day | Needs refinement (copy) | M |
| 3 | Error message when day has no jobs | Yes | S |
| 4 | Sample day data for trials | Yes | M |
| Stretch | Tooltip on "movable" jobs | Yes | S |
**Dropped from the list:** 6 tickets that don't serve the goal (moved to backlog, not lost).

## Risks and dependencies
| Item | Owner | Needed by | Fallback |
|---|---|---|---|
| Tour copy from Marketing | Sam | Day 3 | Ship with placeholder copy, replace in Sprint +1 |
**Most likely to break the goal:** the tour copy.

## Commitment
Team believes it: yes. Review point: day five, check item 2.
```

## What to learn from this

- **Six tickets left the sprint** because they didn't serve the goal. Nothing was deleted.
- **The plan is 10 items against 14 hoped for.** Three sprints of data set the number, not the PM.
- **A fallback sits next to the one external dependency,** so a late copy slips the polish, not the goal.
