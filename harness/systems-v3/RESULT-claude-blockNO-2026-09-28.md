# RESULT — O37 block N, OPUS COLUMN · `claude-opus-5` × greenfield × extras=none × the six new problems · n = 3
### bench, 2026-09-29. **12 conditions, 36 cells of record. The second of block N's two results of record (§N9: "a result of record per model").**
## 📌 The registration is `AMENDMENT-O37-nine-greenfield-claude-2026-09-25.md` (§N0–§N9, ADDENDA 1–12 here; ADDENDA 13–14, which govern the one re-fired cell, are carried on saltbench PR #265 at `7b89ff8e9aa8`).
## 📌 The per-cell tables are FILES: `evidence/claude-lane-blockN-2026-09-28/blockNO-cells.tsv` (36 rows, the join's greenfield shape) and `blockNO-cellfacts.tsv` (36 rows: pool, export, concurrency, fault window, beat).
## ⛔ Every figure line below is printed by `RESULT-claude-blockNO-2026-09-28-verify.py --print` from those two tables, and the verifier asserts each one against the bytes of this document. No number here was typed from a message or from memory.

---
# §1 · WHAT RAN
`claude-opus-5` × **greenfield** × **extras=none** × {Luby, AES, Liveness, MaxFlow, BinomialHeap, LinearScan} × {plain, salt-diet} × 3.
The model is derived per cell from its own transcript by `served_models_v3.py check-cell --condition opus` (36 of 36 `clean`), never from the
block name.
```
cells 36 · conditions 12 · models claude-opus-5 · cap COST 37.21
run_state ENDED: CAP-COST 4 · ENDED: LANDED 32
export other-five 6087b54 30 · LinearScan 23485e5 5 · LinearScan 9d87318 1
end_from HEAD 35 · working tree 1
```
**One cell of record is a re-fire, under ADDENDA 13–14.** `clbmrs03` (LinearScan salt-diet #3) lost its credential mid-run: from 17:18:53Z on
2026-09-28 every model call returned `oauth_org_not_allowed`, the credential file unchanged. By ADDENDUM 13 it is **NOT-SCORED(HARNESS)**, in no
median and no count above; its cost to the cut, from `cell_meter.py` over its own slug, is **$24.46 (T 24,201,306), the meter's last metered record at
17:18:44Z, and 61 refused records after it, none metered**. It was ended by the lead at 2026-09-29T03:17Z (its end marker says so). Its re-fire,
`clbmrsr3`, is the third cell of that condition: fired 03:18Z on the second dir, export `9d87318` (ADDENDUM 14's; the LinearScan task tree and
the scorer's blob are byte-identical to `23485e5`'s), and ended at the cap at 04:50Z. **LinearScan salt-diet therefore STRADDLES two pools**
(`clbmrs01`, `clbmrs02` on dir 1; `clbmrsr3` on dir 2), as §N5.3 anticipates, and is declared here.
`end_from` names where the scorer read the final state: `clbmrs01` stopped at the cap before committing, so its suite is read from the working
tree (lane B §Q6 rule 6: a capped cell's pass is a floor).

---
# §2 · CORRECTNESS, VERIFIED FIRST (lane B §Q6 rule 1: withheld-suite FULL PASS over scorable cells)
```
Luby         plain 3/3 [12/12 12/12 12/12] · salt-diet 3/3 [12/12 12/12 12/12]
AES          plain 3/3 [8/8 8/8 8/8] · salt-diet 3/3 [8/8 8/8 8/8]
Liveness     plain 3/3 [11/11 11/11 11/11] · salt-diet 3/3 [11/11 11/11 11/11]
MaxFlow      plain 3/3 [8/8 8/8 8/8] · salt-diet 3/3 [8/8 8/8 8/8]
BinomialHeap plain 3/3 [13/13 13/13 13/13] · salt-diet 3/3 [13/13 13/13 13/13]
LinearScan   plain 3/3 [9/9 9/9 9/9] · salt-diet 3/3 [9/9 9/9 9/9]
FULL PASS plain 18 of 18
FULL PASS salt-diet 18 of 18
```
**Every cell of record passes its withheld suite in full, in both arms.** All four capped cells pass as well, and each of those passes is a
floor (rule 6). With no FAIL in either arm, rule 2's sign is level in all six problems.

---
# §3 · COST AND THE PREMIUM (lane B §Q6 rule 3; tested CENSORED → UNDERPOWERED)
```
Luby         median COST plain $9.31 · salt-diet $17.53 · ratio 1.9x · CAP-COST plain 0 salt-diet 0 · UNRESOLVED-UNDERPOWERED
AES          median COST plain $8.28 · salt-diet $26.57 · ratio 3.2x · CAP-COST plain 0 salt-diet 0 · UNRESOLVED-UNDERPOWERED
Liveness     median COST plain $9.44 · salt-diet $14.12 · ratio 1.5x · CAP-COST plain 0 salt-diet 0 · UNRESOLVED-UNDERPOWERED
MaxFlow      median COST plain $12.50 · salt-diet $22.64 · ratio 1.8x · CAP-COST plain 0 salt-diet 0 · UNRESOLVED-UNDERPOWERED
BinomialHeap median COST plain $9.01 · salt-diet $18.73 · ratio 2.1x · CAP-COST plain 0 salt-diet 0 · UNRESOLVED-UNDERPOWERED
LinearScan   median COST plain $35.07 · salt-diet $37.21 · ratio 1.1x · CAP-COST plain 1 salt-diet 3 · UNRESOLVED-CENSORED
total COST (capped at the cap) plain $255.35 · total T 261,516,586
total COST (capped at the cap) salt-diet $414.26 · total T 472,972,601
capped cells METERED (not used above): 4, $37.43 .. $37.71 against cap $37.21 · metered salt-diet total $415.43
uncapped cells ending above the cap: 0
```
**The verdict kinds are §N6's, registered before any data.** LinearScan is CENSORED: all three salt-diet cells are capped, so its median sits
at the cap. The other five are UNDERPOWERED. No premium is RESOLVED, and none can be under rule 2.
⚠️ **Every capped cost ENTERS AT THE CAP (lane B §Q6 rule 6).** The four capped cells metered $37.43–$37.71; those figures are printed on their
own line and used in no median, ratio or total. **LinearScan's 1.1x is a LOWER BOUND** (a capped numerator), and one of its plain cells
(`clbmrp01`) is capped too, so its denominator's median is exact but that arm touched the same cap.
⚠️ **All six premiums are also understated by the harness's own sandbox probe** (the table's header declares it; desk VX): its near-constant
absolute cost inflates the cheaper arm's share. ⇒ The sign is the reading; the magnitudes are not.
⚠️ **The figures count every session under a cell, including subagents on another model.** In 23 of the 36 cells the subject's own sidechains
were served `claude-sonnet-5` (each cell's served-model record), and `cell_meter.py` prices each record at its SERVED model's rate. The row's
model is the cell's SUBJECT model.
⚠️ **One dollar cap for both model columns (ADDENDUM 10: "the same dollar cap for both models").** ADDENDUM 10's own table measured Opus's dollars
per hour above the other column's on every range it printed, so the same cap is reached in less work here. Stated as the count it produces, and not as a comparison: **4 CAP-COST
cells in this column** (the other column's own record carries its count).

---
# §4 · THE THREE REGISTERED PREDICTIONS (§N4), REPORTED PER ARM; A MISS IS A RESULT
```
(i) salt-diet CAP-COST >= plain in 6 of 6 problems (1 strictly, 5 ties)
(ii) plain CAP-COST in reference-size order 0 0 0 0 0 1 · non-decreasing yes
(ii) salt-diet CAP-COST in reference-size order 0 0 0 0 0 3 · non-decreasing yes
(iii) CAP-WALL cells 0
```
- **(i) HELD** in every problem, strictly only in LinearScan; the other five are ties at zero.
- **(ii) HELD for both arms**, but only at the last step: every capped cell is LinearScan, the largest reference. Five zeros then a non-zero is
  non-decreasing, and it is weak evidence for an ordering.
- **(iii) HELD.** No cell reached the wall cap.

---
# §5 · THE DECLARED COLUMNS (ADDENDA 6, 8, 9), PRINTED BESIDE THE TABLES AS REGISTERED
```
pool x arm dir1 plain 9 · dir1 salt-diet 10 · dir2 plain 9 · dir2 salt-diet 8
claude_live_at_fire >0 in 22 of 36 cells
fault window cells none
beat sampler: 0 cells sampled
```
- **Pool and arm are near-balanced here** (dir 1 is A2.3's dir, dir 2 the second dir). ADDENDUM 10's interleave alternated model columns by dir,
  and nothing assigned an arm by pool. The re-fire is why LinearScan salt-diet straddles the pools (§1).
- **Concurrency:** 22 cells fired while one other Claude-lane cell was live (each fire log's `claude_live_at_fire` line; the live cell is named
  per row in `blockNO-cellfacts.tsv`). Load moves wall time directly and cost only through behaviour.
- **No Opus cell ran inside ADDENDUM 9's fault window, and the 1-s beat sampler (ADDENDA 6 and 8) sampled no cell of this column** (its
  table carries no Opus id), so ADDENDUM 6's residue is unexercised here, not refuted.

---
# §6 · ⛔ THE PER-CELL ACCOUNT CHECK, DECLARED AS FOR THE OTHER COLUMN
§N9 asks for "the account-check line per cell". **Of the 36 cells of record, one carries a pre-fire per-cell check (`clbmrsr3`, OK, with a
wrong `--expect` reading RED as the control), and one a mid-run check (`clbmrs02`, OK, after its fire, declared as such at the time)**
(`acct-check-blockN.log` on the lead's box). The other 34 rest on the per-dir checks at each dir's entry, as the other column's §6 records.
What stands in place per cell: each transcript is under its named pool dir, served `claude-opus-5` for its head records only, and each fire's
sandbox probe authenticated. **That proves each cell ran authenticated on the named dir, not that the dir's identity string matched at that
fire.** ⛔ No cell is voided on this (§N7 row 11 voids a NOT OK, and none read NOT OK). The deviation is the lead's.

---
# §7 · ⛔ WHAT THIS DOES **NOT** SAY
1. **No magnitude and no effect size** (§N6, §N8 item 1). Every premium is UNRESOLVED by registration.
2. **Nothing about Opus versus Sonnet** (§N8 item 2). The two columns are two results of record, and no sentence here compares them.
3. **Nothing about the 192 conditions outside §N1** (§N8 item 3), and **nothing about whether these six represent the nine** (§N8 item 4).
4. **These are new problems with no prior cells** (§N5 item 1). A defect in a task is a harness finding, never an arm effect.
5. **The cap is the pilot's** (§N5 item 2). All four capped cells are LinearScan, so that problem's costs are censored in both arms.
6. **Nothing here is a claim about the salt METHOD.** Any public sentence, and any claim about the method, is the Captain's (§N9).

---
# §8 · PROVENANCE
```
  cells        36 of record (+ clbmrs03, NOT-SCORED(HARNESS), in no table), staged and fired by clb_stage.sh / clb_fire.sh from the export
               named per cell, on the run box
  harvested    each cell's directory copied off the run box after its end marker
  scored by    score_claude_v3.py (harness 08a3a41a458b; blob 76bf38820ac9, identical at 23485e5 and 9d87318), --declared per cell (never a
               glob), --toolchain-env; tasks from a git archive of 23485e5 (LinearScan's tree 9de205720d1f is identical at 9d87318)
  meter        each cell's own ctl/post-end-1.tsv (final_T, final_COST, cap_unit, cap, kind)
  model        served_models_v3.py check-cell --condition opus, run on the run box over each cell's transcript (36 of 36 clean)
  joined by    join_cells_table.py --block m --served-dir (greenfield shape)
  cellfacts    pool from ctl/run-cfg.tsv · export from ctl/built-from.tsv · claude_live_at_fire from each fire log's CONCURRENCY line ·
               fault window from ADDENDUM 9 · beat maximum from ADDENDUM 8's sampler · end_from from the scorer's note
  verifier     RESULT-claude-blockNO-2026-09-28-verify.py — the other column's verifier with the file names changed and one guard for an
               empty beat sample; re-derives every figure line above and asserts it against this document's bytes
```
