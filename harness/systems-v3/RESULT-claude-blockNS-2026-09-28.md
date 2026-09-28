# RESULT — O37 block N, SONNET COLUMN · `claude-sonnet-5` × greenfield × extras=none × the six new problems · n = 3
### bench, 2026-09-28. **12 conditions, 36 cells. The first of block N's two results of record (§N9: "a result of record per model").**
## 📌 The registration is `AMENDMENT-O37-nine-greenfield-claude-2026-09-25.md` (§N0–§N9, ADDENDA 1–12), carried on saltbench PR #265.
## 📌 The per-cell tables are FILES: `evidence/claude-lane-blockN-2026-09-28/blockNS-cells.tsv` (36 rows, the join's greenfield shape) and `blockNS-cellfacts.tsv` (36 rows: pool, export, concurrency, fault window, beat).
## ⛔ Every figure line below is printed by `RESULT-claude-blockNS-2026-09-28-verify.py --print` from those two tables, and the verifier asserts each one against the bytes of this document. No number here was typed from a message or from memory.

---
# §1 · WHAT RAN
`claude-sonnet-5` × **greenfield** × **extras=none** × {Luby, AES, Liveness, MaxFlow, BinomialHeap, LinearScan} × {plain, salt-diet} × 3.
The model is derived per cell from its own transcript by `served_models_v3.py check-cell --condition sonnet` (36 of 36 `clean`; every head
and sidechain record served `claude-sonnet-5`), never from the block name.
```
cells 36 · conditions 12 · models claude-sonnet-5 · cap COST 37.21
run_state ENDED: CAP-COST 6 · ENDED: LANDED 30
export other-five 6087b54 30 · LinearScan 23485e5 6
end_from HEAD 33 · working tree 3
```
Each condition ran on exactly one export, as ADDENDUM 12 registered. `end_from` names where the scorer read the final state: three capped cells
stopped before committing their last state, so their suite result is read from the working tree (lane B §Q6 rule 6: a capped cell's pass is a
floor).

---
# §2 · CORRECTNESS, VERIFIED FIRST (lane B §Q6 rule 1: withheld-suite FULL PASS over scorable cells)
```
Luby         plain 3/3 [12/12 12/12 12/12] · salt-diet 3/3 [12/12 12/12 12/12]
AES          plain 3/3 [8/8 8/8 8/8] · salt-diet 2/3 [8/8 8/8 1/8]
Liveness     plain 3/3 [11/11 11/11 11/11] · salt-diet 3/3 [11/11 11/11 11/11]
MaxFlow      plain 3/3 [8/8 8/8 8/8] · salt-diet 1/3 [2/8 2/8 8/8]
BinomialHeap plain 3/3 [13/13 13/13 13/13] · salt-diet 3/3 [13/13 13/13 13/13]
LinearScan   plain 1/3 [8/9 9/9 8/9] · salt-diet 0/3 [4/9 4/9 4/9]
FULL PASS plain 16 of 18
FULL PASS salt-diet 12 of 18
```
**Signs only (rule 2).** The sign favours plain on AES, MaxFlow and LinearScan and is level on the other three. **Every salt-diet FAIL is a
CAP-COST cell** (AES #3, MaxFlow #1 and #2, LinearScan #1–#3): the arm ran out of budget before its code passed, and each of those results is
a floor. **Plain's two FAILs are LANDED cells** (LinearScan #1 and #3), each failing one test, `random_programs`, by the scorer's own row.
No classification of that test's failure is made here.

---
# §3 · COST AND THE PREMIUM (lane B §Q6 rule 3; tested CENSORED → UNDERPOWERED)
```
Luby         median COST plain $1.88 · salt-diet $32.78 · ratio 17.5x · CAP-COST plain 0 salt-diet 0 · UNRESOLVED-UNDERPOWERED
AES          median COST plain $1.76 · salt-diet $35.18 · ratio 19.9x · CAP-COST plain 0 salt-diet 1 · UNRESOLVED-UNDERPOWERED
Liveness     median COST plain $1.94 · salt-diet $21.07 · ratio 10.9x · CAP-COST plain 0 salt-diet 0 · UNRESOLVED-UNDERPOWERED
MaxFlow      median COST plain $1.95 · salt-diet $37.74 · ratio 19.3x · CAP-COST plain 0 salt-diet 2 · UNRESOLVED-CENSORED
BinomialHeap median COST plain $1.62 · salt-diet $13.08 · ratio 8.1x · CAP-COST plain 0 salt-diet 0 · UNRESOLVED-UNDERPOWERED
LinearScan   median COST plain $13.74 · salt-diet $37.92 · ratio 2.8x · CAP-COST plain 0 salt-diet 3 · UNRESOLVED-CENSORED
total COST plain $68.10 · total T 130,118,457
total COST salt-diet $514.54 · total T 1,856,566,593
uncapped cells ending above the cap: 1 (clbnxs03 $37.74 ENDED: LANDED)
```
**The verdict kinds are the ones §N6 registered before any data.** CENSORED where more than half a condition's salt-diet cells are capped, so
its median sits at the cap; UNDERPOWERED everywhere else. No premium is RESOLVED, and none can be under rule 2.
⚠️ **The CENSORED ratios are LOWER BOUNDS** (a capped cell's cost enters at the cap, rule 6). **All six premiums are also understated by the
harness's own sandbox probe**, which the table's header declares: its near-constant absolute cost inflates the cheaper arm's cost by the
larger share (desk VX, measured 2026-09-22 over 180 cells). ⇒ The sign is the reading; the magnitudes are not.
⚠️ **`clbnxs03` LANDED at $37.74, above the $37.21 cap, and was not stopped.** The cap is enforced by the watcher's periodic meter read, so a
landing can overshoot it by one turn. Its PASS and its cost stand as they were metered. MaxFlow's salt-diet median is that cell's cost,
between two capped cells, and the condition is CENSORED either way.

---
# §4 · THE THREE REGISTERED PREDICTIONS (§N4), REPORTED PER ARM; A MISS IS A RESULT
```
(i) salt-diet CAP-COST >= plain in 6 of 6 problems (3 strictly, 3 ties)
(ii) plain CAP-COST in reference-size order 0 0 0 0 0 0 · non-decreasing yes
(ii) salt-diet CAP-COST in reference-size order 0 1 0 2 0 3 · non-decreasing NO
(iii) CAP-WALL cells 0
```
- **(i) HELD** in every problem. The cap binds the treatment arm and never bound plain in this column.
- **(ii) MISSED for salt-diet.** Incidence does not rise with reference size: Liveness (0) follows AES (1), and BinomialHeap (0) follows MaxFlow
  (2). For plain it holds only vacuously, at zero throughout. **Reference size, measured by `wc -l` of the reference solution, does not order
  where the cap binds in this column.**
- **(iii) HELD.** No cell reached the wall cap.

---
# §5 · THE DECLARED COLUMNS (ADDENDA 6, 8, 9), PRINTED BESIDE THE TABLES AS REGISTERED
```
pool x arm dir1 plain 13 · dir1 salt-diet 11 · dir2 plain 5 · dir2 salt-diet 7
claude_live_at_fire >0 in 16 of 36 cells
fault window cells clbnas03 clbnvp01
beat sampler: 11 cells sampled · max 181 s (clbnvp01)
```
- **Pool and arm are correlated, as ADDENDUM 6 declared they would be.** Pools are named by number: dir 1 is A2.3's dir, dir 2 the second dir.
  No arm was assigned by pool, and the served model, pinned client, settings, fence and caps are identical across the two.
- **Concurrency:** 16 cells fired while one other Claude-lane cell was live (each fire log's `claude_live_at_fire` line; the live cell is
  named per row in `blockNS-cellfacts.tsv`). Load moves wall time directly and cost only through behaviour.
- **The fault window (ADDENDUM 9):** `clbnas03` (AES salt-diet #3, CAP-COST, FAIL 1/8) and `clbnvp01` (Liveness plain #1, PASS 11/11) stand as
  results under ADDENDUM 9's ruling (0 box-caused tool failures in either cell's window). The window is a confound column for any table
  holding either cell.
- **The liveness guard's basis (ADDENDA 6 and 8).** The 1-s sampler ran from 2026-09-26 21:45:56Z to 2026-09-27 05:45:55Z and saw 11 cells. Ten
  peaked at 79–117 s. **`clbnvp01` reached 181 s, one second past the guard's 180 s threshold, at 21:51:00Z** — 3 minutes after its own
  `LAUNCHING` line (21:47:58Z), and reset at 21:51:01Z. It is the gap between staging and the running cell's first beat, not a stall mid-run.
  No fire occurred in that second (the fire logs' timestamps). The residue ADDENDUM 6's signature named is therefore unexercised in this
  column, not refuted.

---
# §6 · ⛔ A REGISTERED RECORD THAT DOES NOT EXIST, DECLARED
**§N9 asks for "the account-check line per cell", and §N0 row 8 for `cells_account_check.sh --expect` reading OK before each fire. No per-cell
account-check record exists.** Measured on the run box: no fire log and no cell `ctl/` file carries an `ACCOUNT-CHECK` line, and
`clb_fire.sh` at either export carries no call to it (0 matches for `account_check` in 228 lines at each). The check was driven **per DIR, at each dir's entry**, and its readings were posted on the
bus: A2.3's dir on 2026-09-25 (OK, with the RED control firing) and the second dir at ADDENDUM 8 (OK, with the RED control). **What stands in its
place per cell, and what it does NOT establish:** each cell's transcript is under its named pool dir, served `claude-sonnet-5` only, and each
fire's sandbox probe authenticated (a refused probe would have stopped the fire, as ADDENDA 7 and 11 record). That proves the cell RAN
AUTHENTICATED on the named dir. **It does not prove the dir's identity string matched the expected account at that fire**, which is what the
check reads. ⛔ **No cell is voided on this.** §N7 row 11 voids a cell whose check reads NOT OK, and no check read NOT OK. The deviation is
the lead's, and it is recorded here rather than repaired after the fact.

---
# §7 · ⛔ WHAT THIS DOES **NOT** SAY
1. **No magnitude and no effect size** (§N6, §N8 item 1). Every premium is UNRESOLVED by registration.
2. **Nothing about Opus, or Opus versus Sonnet** (§N8 item 2). The Opus column is the second result of record.
3. **Nothing about the 192 conditions outside §N1** (§N8 item 3), and **nothing about whether these six represent the nine** (§N8 item 4: the
   six are the ones judged feasible to port).
4. **These are new problems with no prior cells** (§N5 item 1). A defect in a task is a harness finding, never an arm effect, and a reader should
   not read LinearScan's plain `random_programs` failures as either until someone reads them.
5. **The cap is the pilot's** (§N5 item 2). All six salt-diet FAILs are capped cells, so every salt-diet FAIL here is also a budget stop.
   A heavier problem meeting the same cap censors the arm that works longer.
6. **Nothing here is a claim about the salt METHOD.** Any public sentence, and any claim about the method, is the Captain's (§N9).

---
# §8 · PROVENANCE
```
  cells        36, staged and fired by clb_stage.sh / clb_fire.sh from the export named per cell, on the run box
  harvested    each cell's directory copied off the run box after its end marker
  scored by    score_claude_v3.py (harness 08a3a41a458b), --declared per cell (never a glob), --toolchain-env; tasks from a
               git archive of the cell's own export (6087b54, or 23485e5 for LinearScan)
  meter        each cell's own ctl/post-end-1.tsv (final_T, final_COST, cap_unit, cap, kind)
  model        served_models_v3.py check-cell --condition sonnet, run on the run box over each cell's transcript (36 of 36
               clean); the tool is 6087b54's for all 36, and its table sha is the same at 23485e5
  joined by    join_cells_table.py --block n --served-dir (greenfield shape: 15 columns, no retention, no second producer)
  cellfacts    pool from ctl/run-cfg.tsv · export from ctl/built-from.tsv · claude_live_at_fire from each fire log's CONCURRENCY
               line · fault window from ADDENDUM 9 · beat maximum from ADDENDUM 8's sampler · end_from from the scorer's note
  verifier     RESULT-claude-blockNS-2026-09-28-verify.py — re-derives every figure line above from the two tables and asserts
               it against this document's bytes; --selftest mutates one PASS to FAIL and requires RED
```
