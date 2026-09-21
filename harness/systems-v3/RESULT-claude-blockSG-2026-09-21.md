# RESULT — block SG · `claude-sonnet-5` × greenfield × extras=none · n=29 (+1 declared)
### bench, 2026-09-21. **10 conditions. ⛔ AND THE COST CAP BINDS ONE ARM AND NOT THE OTHER, WHICH MAKES IT A TREATMENT.**
## 📌 The per-cell table is a FILE: `evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv` (29 rows, 15 columns, + a declared exclusion in its header).
## ⛔ Every figure below is derived from that table by `RESULT-claude-blockSG-2026-09-21-verify.py`.

---
# §1 · WHAT RAN
`claude-sonnet-5` × **greenfield** × **extras=none** × 5 problems × {plain, salt-diet} × 3 reps = **10 conditions.**
```
  rows in the table   29        run_state   ENDED: LANDED 24 · ENDED: CAP-COST 5
  model               claude-sonnet-5, derived per cell from its own served-*.out, 29 of 29
  w1_fenced           `-` for all 29 — GREENFIELD HAS NO SEED, so there is no W1 witness to fence
```
⚠️ **A GREENFIELD TABLE IS A DIFFERENT SHAPE, NOT A SHORTER ONE.** `class`, `retained`, `surv`, `growth`, `seed_lines`, `end_lines`, `kept` and `end_from` are all claims **about a seed**, and this block has none. They are **omitted rather than emitted blank**, because a blank cell reads as a measurement that came back empty.
⛔ **`clbglp01` (LRU, plain, rep 1) IS DECLARED AND EXCLUDED, NOT DROPPED.** It was fired and harvested **BY HAND** — the work list's own header says so — and **has no `served-*.out` anywhere** (control: every sibling's exists), so its SERVED model cannot be derived. **Its own `ctl` records `claude-sonnet-5`, but that is the REQUESTED model, and the served receipt is the authority — which is the entire reason ADDENDUM 12 exists.** A weaker claim is not promoted to fill a column. ⇒ **The LRU × plain condition therefore carries n=2 in this table and n=3 in the run.**

---
# §2 · ⛔⛔ THE COST CAP IS ARM-CORRELATED, AND THAT IS THE FIRST THING TO READ
```
                  cells   CAPPED at $37.21      suite
  plain           14      0  of 14              PASS 13 · FAIL 1
  salt-diet       15      5  of 15              PASS 14 · BUILD-FAIL 1
```
⇒ 🔑 ***A CAP THAT BINDS ONE ARM AND NEVER THE OTHER IS NOT A BUDGET, IT IS A TREATMENT.*** `cap_unit` is `COST` and the cap is `$37.21` for every cell; **it cuts 5 salt-diet cells and 0 plain ones.**
⭐ **AND THE DIRECTION IS KNOWN, WHICH MAKES IT A BOUND RATHER THAN A DOUBT:** the cap can only ever **remove** salt-diet work. So **every salt-diet figure below is a LOWER BOUND on cost and a FLOOR on correctness** — the arm cannot have been flattered by it.

---
# §3 · CORRECTNESS — AND THE ONE BUILD-FAIL IS A CELL THAT WAS CUT OFF, NOT A CELL THAT FAILED
```
  suite        PASS 27 · FAIL 1 · BUILD-FAIL 1   (of 29)
  per problem  Crc32 6/6 · FreeList 4/6 · LRU 5/5 · LZW 6/6 · Paxos 6/6
  the two non-PASS cells, named:
    clbgfp03  FreeList plain      FAIL        6/7   ENDED: LANDED       $4.05   not capped
    clbgfs02  FreeList salt-diet  BUILD-FAIL  0/0   ENDED: CAP-COST    $37.70   CAPPED
```
⛔ **`clbgfs02` IS THE SAME CELL AS ONE OF §2's FIVE CAPPED CELLS.** It did not build **and it ran out of budget**; `0/0` is the signature of a suite that never ran, not of a suite that ran and failed. ⇒ ***SCORING IT AS A FAILURE WOULD MANUFACTURE A ZERO FROM AN UNFINISHED CELL*** — the same law that governs a cell with no `LANDING.md`. **It is reported, named, and placed in NO correctness denominator.**
✅ **`clbgfp03` IS A GENUINE FAILURE AND IS COUNTED AS ONE:** it LANDED, was not capped, spent $4.05, and its suite ran and returned **6 of 7**. ⇒ **On this block the only unambiguous correctness failure is in the PLAIN arm.**
⚠️ **FreeList is the problem carrying both**, and `RECORD-brownfield-givens` already flags FreeList's given as **MARGIN 1**. This block is greenfield, so that record does not apply directly — **named here because the coincidence is the kind of thing a later reader should check rather than rediscover.**

---
# §4 · COST — THE ARMS DIFFER BY MUCH MORE HERE THAN ON BROWNFIELD, AND IT IS CENSORED
```
                 median COST   total COST   total T          suite PASS
  plain          $1.74         $29.79        47,910,941      13 of 14
  salt-diet      $14.39        $292.87      995,011,724      14 of 15
  ratio          8.27x         9.83x         20.77x
```
⛔ **ALL THREE RATIOS ARE LOWER BOUNDS** — five salt-diet cells are censored at the cap (§2) and none of plain's is.
⭐ **THE CONTRAST WITH BLOCK O IS THE INTERESTING PART AND IT IS STATED AS AN OBSERVATION:** on `brownfield × none` at Opus the median cost ratio is **1.89×**; here on `greenfield × none` at Sonnet it is **8.27×**. ⚠️ **TWO THINGS DIFFER AT ONCE — THE FIELD AND THE MODEL — SO THIS BLOCK CANNOT ATTRIBUTE THE GAP TO EITHER.** It is a pair of readings, not a decomposition, and naming it here is not the same as explaining it.

---
# §5 · ⛔ WHAT THIS DOES **NOT** SAY
1. **It is one model on one field with extras=none.** Nothing here reaches Opus, brownfield, or any treatment.
2. **The salt-diet arm's cost and correctness are both censored by an arm-correlated cap.** Its figures are bounds.
3. **`clbgfs02` is in no correctness denominator**, and the block's 27/29 is therefore over 28 scorable cells, not 29.
4. **n is 29 in the table and 30 in the run.** See §1's declared exclusion; the condition count is 10 either way.
5. **No cell was re-run.** Every number is a re-reading of artifacts that existed before this shift.
6. **Nothing here is a claim about the salt METHOD** — these are `plain` vs `salt-diet` arms.

---
# §6 · PROVENANCE
```
  cells        30 fired; 29 with a derivable served model, staged at ~/bench-dry/clb-score/, scored as they landed
  scored by    score_claude_v3.py from 283362105d75's harness, --declared (never a glob), --toolchain-env
  retention    NOT RUN, and not applicable: greenfield has no seed to decompose against
  meter        each cell's own ctl/post-end-1.tsv (final_T, final_COST, cap_unit, cap)
  model        model_served_v3.py, from each cell's own served-<cell>.out; 29 of 29 claude-sonnet-5
  table        evidence/claude-lane-blocks-2026-09-21/blockSG-cells.tsv
  verifier     RESULT-claude-blockSG-2026-09-21-verify.py — re-derives every figure FROM the table
               and asserts it against the BYTES of this document. No typed expectations.
```
