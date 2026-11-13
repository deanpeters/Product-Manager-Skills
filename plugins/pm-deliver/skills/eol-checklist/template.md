# EOL Checklist Template

Fill in the level and phases first, then build only the areas your level warrants. Quality checks
at the bottom.

## Provenance
Adapted from `prompts/eol-checklist.md` in the
`https://github.com/deanpeters/product-manager-prompts` repo.

---

## Pick your level first

| | Level 1 — Light | Level 2 — Standard | Level 3 — Heavy |
|---|---|---|---|
| Scope | Feature, internal tool, API | Commercial product, active customers | Revenue-critical, hardware, regulated |
| Phases | 2-3 (NSC, EOS, EOL) | 4-5 (NSC, EOS, EOE, EOM, EOL) | All 6 (NSC through EOSRV) |
| Areas | 4 | 11 | 15 |
| Gates | Not needed | Between major phases | Between every phase, with approvers |

**Most sunsets are Level 2.** Insert EOR if contracts run past EOS. Drop EOSRV if there are no
service obligations — and say so rather than leaving it blank.

**Sticky-note rule:** every item is 4-8 words, starts with a verb, and names an owning function.

---

## Template

```markdown
## EOL Checklist: [Product Name]

**Level**: [1-Light / 2-Standard / 3-Heavy]
**Phases in scope**: [list]
**Phases not in scope**: [list + one-line why]
**Target EOL date**: [date / TBD / Not scheduled]

### Lifecycle Phase Definitions (include only phases in scope)

- **NSC (Notice of Status Change)**: Decision communicated; planning begins
- **EOS (End of Sale)**: No new customers can purchase
- **EOE (End of Expansion)**: Existing customers cannot add capacity
- **EOR (End of Renewal)**: Existing contracts will not be renewed
- **EOM (End of Maintenance)**: Bug fixes and patches stop
- **EOL (End of Life)**: Product is fully retired
- **EOSRV (End of Service)**: Support and service obligations end

---

### Phase: [Name] -- Target Date: [date / TBD / Not scheduled]

(Repeat per phase. Include only the areas your level warrants.)

#### Product and Strategy (L1+)
- [ ] [Verb-first item, 4-8 words] -- Owner: [function]

#### Engineering and Technical (L1+)
- [ ] [Item] -- Owner: [function]

#### Support (L1+)
- [ ] [Item] -- Owner: [function]

#### Documentation and Training (L1+)
- [ ] [Item] -- Owner: [function]

#### Legal and Contractual (L2+)
- [ ] [Item] -- Owner: [function]

#### Financial Planning (L2+)
- [ ] [Item] -- Owner: [function]

#### Sales (L2+)
- [ ] [Item] -- Owner: [function]

#### Marketing (L2+)
- [ ] [Item] -- Owner: [function]

#### Customer Success (L2+)
- [ ] [Item] -- Owner: [function]

#### IT Systems (L2+)
- [ ] [Item] -- Owner: [function]

#### Data Management (L2+)
- [ ] [Item] -- Owner: [function]

#### Inventory and Supply Chain (L3)
- [ ] [Item] -- Owner: [function]

#### Channel and Partner Management (L3)
- [ ] [Item] -- Owner: [function]

#### Regulatory and Compliance (L3)
- [ ] [Item] -- Owner: [function]

#### Internal Organizational Alignment (L3)
- [ ] [Item] -- Owner: [function]

---

### Phase Gate Criteria (L2+)

#### [Phase A] to [Phase B]
- [ ] [What must be true] -- Approver: [role]
- [ ] [What must be true] -- Approver: [role]

---

### Post-EOL Actions (all levels)

- [ ] [Archive artifacts and records] -- Owner: [function]
- [ ] [Run lessons-learned review] -- Owner: [function]
- [ ] [Publish final report] -- Owner: [function]

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]
```

---

## Quality checks

Any "no" is a rewrite, not a nitpick.

**Proportion**
- [ ] Level was chosen deliberately, not defaulted to the heaviest
- [ ] Phases out of scope are listed with a one-line reason
- [ ] If you went lighter than recommended, you know which area dropped out

**Item hygiene**
- [ ] Every item is 4-8 words and starts with a verb
- [ ] Every item names an owning function — no blanks, no "the team"
- [ ] Each item sits in the phase where the work happens, not where it's announced

**The four things sunsets strand**
- [ ] **Data** — export format, availability window, deletion schedule
- [ ] **Contracts** — renewal language, SLA terms, refunds or credits owed
- [ ] **Access** — API keys, integrations, SSO, downstream readers
- [ ] **Money** — forecast adjustment, rev-rec treatment, cost of the sunset itself

**Gates**
- [ ] Every gate names an approver (no approver = not a real gate)
- [ ] Gates state conditions that must be *true*, not dates that must pass

**Dates**
- [ ] No date was invented to fill a blank
- [ ] Any `Not scheduled` entry is paired with the precondition to schedule it

**Closure**
- [ ] A lessons-learned review is on the list and owned
- [ ] Assumptions are stated plainly rather than silently resolved
