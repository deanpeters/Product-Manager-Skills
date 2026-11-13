# Sprint Planning Example: Industrial

**Team:** Northfield firmware team (5 engineers), 2-week sprint, NFA-500 bring-up
**Dependency:** a supplier radio-module sample promised for day 4
**Why this example exists:** a physical dependency with real lead time. The goal had to survive a
late part.

---

```markdown
## Sprint goal
> Firmware boots on the production NFA-500 board and reports a fault code over the service port.

Flexible: can be met on the dev board if the radio sample slips; the radio is the stretch.

## Capacity
| Person | Days | Leave/meetings | Focused |
|---|---|---|---|
| 5 engineers | 50 | 4 leave, 8 meetings, 5 lab-sharing | 33 |
**Focus factor:** 0.8 → ~26 days. Last three sprints finished 7, 8, and 6 items; plan 7.
**Slack held:** 2 items (about 25%): lab bookings fall through; board revisions arrive late.

## Selected work
| Order | Item | Ready? | Size |
|---|---|---|---|
| 1 | Bring up bootloader on production board | Yes | M |
| 2 | Fault-code table over service port | Yes | M |
| 3 | Watchdog configuration | Yes | S |
| 4 | Radio driver smoke test | **Blocked on sample** | M |
| Stretch | Power-cycle test rig script | Yes | S |

## Risks and dependencies
| Item | Owner | Needed by | Fallback |
|---|---|---|---|
| Radio sample | Supply chain lead | Day 4 | Move item 4 to next sprint; goal unaffected |
| Lab slot for thermal test | Test lead | Day 6 | Book a backup slot on day 8 |
**Most likely to break the goal:** the production board revision arriving late.

## Commitment
Believed with one condition: if the board slips past day 2, drop to the dev board and re-plan.
```

## What to learn from this

- **The goal doesn't depend on the late part,** so the supplier slipping costs scope, not success.
- **Slack is larger (25%)** because physical lead times are less forgiving.
- **The condition is named in advance,** so the day-two decision is already made.
