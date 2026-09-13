# RESULT — the P2 Opus spec-change PAIR (Crc32), 2026-09-13

**Two cells, one problem, both arms, both LANDED and SCORED.** Every number below names the file it
was read from. Nothing here was retyped from a message or from memory.

⛔ **READ §4 BEFORE QUOTING ANY VERDICT: one of the three verdict columns is GREEN on a stub and
carries no information on this problem.**

## §1 · THE PAIR

| field | p2b001 | p2b002 | source |
|---|---|---|---|
| arm | `plain` | `salt-diet` | `ctl/arm` |
| problem | Crc32 | Crc32 | `ctl/task` |
| parent (phase-1 landing) | `3870b58e` | `6a1618ed` | `ctl/copied-from.tsv:copied_from_id` |
| change payload | `6db96d0778e8cb19` | `6db96d0778e8cb19` | `ctl/customer.log` |
| end | `LANDED landing-2 8b8c1e643f12` | `LANDED landing-2 aba5ad443597` | `ctl/end-2` |
| wall (s) | 1286 / 72000 | 1950 / 72000 | `ctl/watch.log` last `METER` |
| T (final) | 18,723,452 | 11,882,956 | `ctl/watch.log` `POST-END` |
| COST (USD, modelled) | 15.3468 | 11.6997 | `ctl/watch.log` `POST-END` |
| commits since the change | 12 | 12 | `p2b-score-20260913T204652Z/ROWS.tsv` |

**The payload sha is identical across the arms.** That is the pair's own self-check: `customer.sh`
prints a payload sha that must match across an arm pair, and it does.

## §2 · THE SUITE (the primary comparison)

Read from `p2b-score-20260913T204652Z/<id>.log`, the post-change (`B`) runner's own output:

| cell | TESTS | REGRESSIONS | CLAUSE_TESTS |
|---|---|---|---|
| p2b001 `plain` | 10/10 | 0/6 | 0/4 |
| p2b002 `salt-diet` | 10/10 | 0/6 | 0/4 |

⛔ **POLARITY, because it is what a reader gets backwards here:** `TESTS p/t` counts **PASSES**;
`REGRESSIONS f/t` and `CLAUSE_TESTS f/t` count **FAILURES**. So `10/10`, `0/6`, `0/4` is a clean pass.

## §3 · THE CONTROLS — why `10/10` is a reading and not a silence

Driven the same shift, same runner, same toolchain environment:

| control | TESTS | REGRESSIONS | CLAUSE_TESTS | meaning |
|---|---|---|---|---|
| raw post-change stub (`B/interface.rs`) | 5/10 | 5/6 | 0/4 | the suite **discriminates** |
| pre-change interface (`G/interface.rs`) | 0/0 | — | — | will not **compile** against `B` |

⇒ **The instrument reads its population.** A `10/10` from an instrument that had never been shown to
fail is not evidence; this one fails on a stub and refuses the wrong spec.

## §4 · ⛔⛔ `CLAUSE_TESTS` (V2) IS UNINFORMATIVE ON THIS PROBLEM

**The stub scores `CLAUSE_TESTS 0/4` — GREEN — while failing 5 of 6 regressions.** The four clause
tests *ran* (the stub built and scored 5/10) and none of them failed.

⇒ ***V2 IS GREEN FOR A SOLUTION THAT COMPUTES THE WRONG ANSWER.*** On Crc32, `V2 GREEN` carries no
information and must be reported as **UNINFORMATIVE**, never quoted beside V1 as comparable evidence.
**V1 discriminates — it is RED on the stub. V2 does not.** They are read independently by design
(`referee_v3.phase2_verdicts()`: `V1 GREEN iff regressions_failed == 0`, `V2 GREEN iff
clause_failed == 0`, no pooled field derived), and this result is why that independence matters.

## §5 · WHAT THIS PAIR SAYS, AND WHAT IT CANNOT

✅ **On Crc32, the two arms are INDISTINGUISHABLE ON CORRECTNESS and the treatment is CHEAPER.**
Identical on TESTS, REGRESSIONS, CLAUSE_TESTS and commit count. The differences are **COST 0.76x**
and **WALL 1.52x** — the treatment ran longer and bought less.

⛔ **WHAT IT CANNOT SAY.** `n = 1 PAIR` on **ONE** problem. Crc32 is a problem this campaign has
already measured as discriminating nothing in greenfield (11/11 across both arms). **A ceiling on
correctness is a statement about the problem, not a finding about the method.** Both arms could read
their own cost cap as a live countdown in `repo/BUDGET.md`, which makes the cap an **input** and not
only a limit. The cost figures are modelled at list rates: a unit for comparing arms, never an invoice.

## §6 · PROVENANCE, INCLUDING TWO DEFECTS IN THE INSTRUMENTS

- **Scorer export ≠ builder export, deliberately, and both are recorded.** Both cells record
  `export_sha 23b351c` in `ctl/built-from.tsv`; that export's `referee_v3.py` carries **zero**
  occurrences of `phase2_verdicts`. Scoring used `ecd3924`, which carries 13. A result whose scorer
  is not its builder must say so, and this one does.
- ⛔ **The harvest REFUSED, and its remedy would have produced the failure it exists to prevent.**
  `smoke_harvest_v3.sh` keys a CFG check on `built-from.tsv:cfg` and directed a re-run against the
  **builder's** account directory. Measured: the transcripts are **ABSENT** under the directory the
  refusal named, for both cells, and **PRESENT** under the one the cells actually ran on, with mtimes
  matching both landings. **`built-from.tsv:cfg` is the BUILDER's config dir** — these cells were
  built on one account on September 7–8 and ran phase 2 on another. The tool already carries the
  same lesson for the *path* ("the slug is filed under the path the cell had **when it ran**") and
  has not carried it across to the *config dir*.
  ⇒ **REPAIRED AND RE-HARVESTED THE SAME SHIFT.** The harvest now prefers a run-time `ctl/run-cfg.tsv`
  row over the build-time one and its refusal names which file it read; the cell records that row at
  each launch. Driven RED/GREEN/RED, then end to end on both cells: **rc 0, `METER + HEAD SHARE
  taken`, no `VOID`** — `COST $15.35` (p2b001) and `COST $11.70` (p2b002), from
  `harvest-v3/<id>-<stamp>/METER.txt`.
  ⭐ **Those receipts AGREE with the cells' own `POST-END` meter lines ($15.3468 / $11.6997), which is
  the point of quoting both: two different files, one instrument, the same number.** Where this file
  gives four decimal places it is citing `ctl/watch.log`; the harvest receipt rounds to two.
  ⚠️ **`ctl/run-cfg.tsv` on these two cells is RECONSTRUCTED, not written at launch** — the repair is
  committed and unmerged, so it did not run for them. The row is measured, not recalled (each cell's
  transcript slug exists under the named config dir and under no other v3 config dir on the box), and
  the file says so in its own `provenance` field.
- 📌 **Nothing in either cell records the config dir it RAN on.** `ctl/account.tsv` is empty in both;
  `ctl/launch.log`'s ARGV line lists environment **names**, not values. **Owed repair:** the cell
  records its run-time config dir, and the harvest prefers that over the build-time row.
- ⚠️ **p2b002 was staged BY HAND, not by `cell_copy_v3.py`, and was reconciled afterwards.** Its
  parent's run records sat loose in `ctl/`, which made the harvest read the parent's
  `END LANDED landing-1` as an end kind of its own and the parent's `post-end-1.tsv` as its own
  §31(b) receipt. Reconciled in place after the cell ended: 9 records relocated to `ctl/phase1/`,
  split at `ctl/copied-from.tsv:copied_at`; **107 watch.log lines in, 81 + 26 out, zero lost**; a
  pre-image of all 893 files is archived beside the cell. The positive control is recorded: the
  unreconciled directory shows the inversion (1 and 1), the reconciled one shows 0 and 0, and the
  same pass on the correctly-staged `p2b001` is a no-op by construction.

## §7 · FILES

```
  scored rows        p2b-score-20260913T204652Z/ROWS.tsv          (run box)
  per-cell suite     p2b-score-20260913T204652Z/<id>.log          (run box)
  cells              cells-p2b-opus-specchange/{p2b001,p2b002}    (run box)
  pre-image          cells-p2b-opus-specchange/_archive/p2b002-preimage-20260913T204313Z
  scorer export      saltbench-systems-v3-export-ecd3924  = ecd3924828cb3b1255115a3094e2ceee51d62dfd
```
