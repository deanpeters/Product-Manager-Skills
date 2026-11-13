# Usage Data Investigation Example: SaaS

**Question:** trials of the Route Optimizer start, but few reach a first optimized route. Where do they stall, and who?
**Unit:** trial account · **Window:** March trials · **Decision:** where to focus onboarding work

**Why this example exists:** the funnel showed one step, but the segment cut showed it was really
one kind of account, and the data had nothing to say about why.

---

```markdown
## Data check
- Tracking: "first optimized route" fires on route save; verified on three test accounts.
- Definition: unchanged in window.
- Missing: 6 internal test accounts removed; 3 trials from a partner API not tracked (noted).
- Sample: 212 trial accounts. Enough to read the funnel; thin for segments under 20.

## Funnel (March trials, N = 212)
| Step | Count | To next |
|---|---|---|
| Trial started | 212 | 78% |
| Dispatcher invited | 165 | 71% |
| Day loaded | 117 | 42% |
| First route optimized | 49 | n/a |
**Biggest drop:** day loaded → first optimized (117 → 49).

## Segments
| Segment | N | Reached first route |
|---|---|---|
| 50-100 technicians | 88 | 24 (27%) |
| 101-300 technicians | 84 | 22 (26%) |
| Over 300 | 40 | 3 (8%) |

## Findings
1. **Fact:** 49 of 212 trials (23%) reached a first optimized route within 7 days.
2. **Fact:** the biggest drop is between loading a day and optimizing it (117 to 49).
3. **Fact:** accounts over 300 technicians reached it at 8% (3 of 40) vs about 27% elsewhere.
4. **Inference:** large accounts may need a configuration step the smaller ones skip. (Not shown.)
5. **Assumption:** dispatchers don't see value. (The data can't show this.)

## What people must answer
| Question | Who | Ask |
|---|---|---|
| Why do large accounts stop after loading a day? | Dispatchers at 5 large trial accounts | "Walk me through what you did after the day loaded." |
```

## What to learn from this

- **The average (23%) hid a segment (8%).** The finding was in the cut.
- **Finding 4 is labeled an Inference,** and finding 5 an Assumption nobody should act on.
- **The investigation ends with five phone calls,** which is what the data pointed toward.
