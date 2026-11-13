# Release Readiness Example: Industrial

**Release:** firmware 2.1 for NFA-500 controllers, over the air to ~2,000 field units
**Why this example exists:** no physical rollback once flashed, so reversibility is the whole question.

---

```markdown
## The release
**What changes:** new fault-detection algorithm and a radio stack update.
**What does not change:** control logic, I/O mapping, certified safety functions.
**Reaches:** ~2,000 field units. **Reversibility:** a failed flash can brick a unit; rollback needs a
site visit.
**Level:** 3 Heavy.

## The seven checks
| Check | State | Evidence |
|---|---|---|
| Tested | Bench, thermal chamber, 30-unit soak for 3 weeks | Test report. **Not tested:** units on the oldest hardware revision (B) |
| Rollout | 20 units → 200 → remainder, 1 week each | Move-on: zero failed flashes and fault rate not above baseline |
| Monitoring | Flash success rate, fault-code volume, hotline calls | Watcher: service lead, daily for 14 days |
| Rollback | Previous image kept in the unit's second bank; auto-revert if boot fails | **Rehearsed on 10 bench units** |
| Support | Hotline briefed; script for "controller offline after update" | Done |
| Certification | Radio stack change checked with the assessment body | **Not confirmed**: pending reply |
| Timing | Avoid plants' scheduled shutdown weeks | Customer calendar reviewed |

## Go / hold criteria
| # | Criterion | Threshold | Type |
|---|---|---|---|
| 1 | Soak test | 0 failures in 30 units | Must-pass |
| 2 | Auto-revert on boot failure | Works on 10 of 10 bench units | Must-pass |
| 3 | Radio stack certification impact | Assessment body confirms no re-evaluation | Must-pass |
| 4 | Hardware revision B units | Tested or excluded from the rollout | Must-pass |

## Decision
**Hold.** Criteria 3 and 4 are open. Exclude revision B from stage 1. Re-decide when the assessment
body replies. Decided by: Engineering director.
```

## What to learn from this

- **The two-bank image made a rollback exist.** Without it, this would be a physical visit per unit.
- **The hold named two specific blockers,** not a general unease.
- **Excluding hardware revision B is a scoping move,** not a delay of the whole release.
