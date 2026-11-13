# Release Readiness Template

Unconfirmed items are `[NEEDS SOURCE]` or "not confirmed", never assumed done.

---

## 1. The release
**What is shipping:** · **What does not change:** · **Reaches (accounts / units):** · **Reversibility:**
**Level:** [1 Light / 2 Standard / 3 Heavy] because [reach and reversibility]. A lighter level would leave [uncovered].

## 2. The seven checks
| Check | State | Evidence | Owner |
|---|---|---|---|
| 1. What changes (and doesn't) | | | |
| 2. Tested: what, where, **what was not tested** | | | |
| 3. Rollout stages and move-on criteria | | | |
| 4. Monitoring: signals, watcher, duration | | | |
| 5. Rollback: method, time, rehearsed? | | | |
| 6. Support and customer communication | | | |
| 7. Dependencies and timing (why now) | | | |

## 3. Go / hold criteria (agreed before the status)
| # | Criterion | Threshold | Must-pass or Watch | Result |
|---|---|---|---|---|

## 4. Decision
**Go / Hold / Go with conditions:** · **Decided by (one person):** · **Conditions:**
**Open items:** [owner, date]

---

## Quality checks
- [ ] Level is justified by reach and reversibility
- [ ] Rollback is named, timed, and rehearsed (or its absence is flagged)
- [ ] Rollout is staged with criteria
- [ ] Monitoring has named signals and a named watcher
- [ ] Go/hold criteria were written before the status
- [ ] One person decides
- [ ] Why-now is justified
