# RESULT — O37 block W, SONNET COLUMN · `claude-sonnet-5` × greenfield × extras=none × WHT, NTT · n = 3
### bench, 2026-11-15. **4 conditions, 12 cells of record. One of block W's two results of record (§W9 = block N §N9: "a result of record per model").**
## 📌 The registration is `AMENDMENT-O37-wht-ntt-greenfield-claude-2026-11-11.md` (§W0–§W9, signed 2026-11-11; ADDENDA 1–3: the release and the WHT re-price)
## 📌 The per-cell tables are FILES: `evidence/blockW-2026-11-14/cells.tsv` (24 rows, both columns; made by `w-derive.sh` beside it) and `cellfacts.tsv` (24 rows: pool, export, concurrency at fire, fire log)
## ⛔ Every figure line below is printed by `RESULT-claude-blockW-2026-11-15-verify.py --block WS --print` from those two tables, and `--check` asserts each one against the bytes of this document. No figure line was typed; a number in prose names its source.

---
# §1 · WHAT RAN
`claude-sonnet-5` × **greenfield** × **extras=none** × {WHT, NTT} × {plain, salt-diet} × 3. The model is derived per cell from its own
transcript by `served_models_v3.py check-cell`, never from the block name.
```
cells 12 · conditions 4 · model claude-sonnet-5 · cap COST 37.21
run_state ENDED: CAP-COST 3 · ENDED: LANDED 9
export 0916ef9a6d70 12
end_from HEAD 11 · working tree 1
served: 12 of 12 cells clean · head claude-sonnet-5 only
```
**Two cells FAIL their withheld suite, and both are capped salt-diet cells.** `clbiws01` (WHT salt-diet #1, the tripwire T-W-S)
stopped at the cap with its solution uncommitted, so the scorer read the WORKING TREE (`end_from` prints it), as score_claude_v3.py
does. `clbits01` (NTT salt-diet #1) stopped at the cap and is read at HEAD. A third capped cell, `clbits02`, passes, a floor. §2 prints
each cell's tests.

---
# §2 · CORRECTNESS, VERIFIED FIRST (lane B §Q6 rule 1: withheld-suite FULL PASS over scorable cells)
```
WHT  plain 3/3 [11/11 11/11 11/11] · salt-diet 2/3 [1/11 11/11 11/11]
NTT  plain 3/3 [11/11 11/11 11/11] · salt-diet 2/3 [4/11 11/11 11/11]
FULL PASS plain 6 of 6
FULL PASS salt-diet 4 of 6
```
**Plain passes in full in both problems; salt-diet passes 2 of 3 in each.** Rule 2's sign (sign only, per-cell values beside it)
therefore runs toward plain in both problems. ⚠️ Both FAILs are capped cells, and a capped cell's pass result is a floor (rule 6):
each FAIL is a cell that ran out of budget without passing; neither finished, and a floor cannot say whether either would have. The cap is the same dollar cap for both
model columns, so this is a cap-policy reading first (lane B's registered confound: 'a USD cap is a different token budget per model').

---
# §3 · COST AND THE PREMIUM (lane B §Q6 rule 3; tested CENSORED → UNDERPOWERED)
```
WHT  median COST plain $2.09 · salt-diet $26.29 · ratio 12.6x · CAP-COST plain 0 salt-diet 1 · UNRESOLVED-UNDERPOWERED
NTT  median COST plain $1.48 · salt-diet $37.21 · ratio ≥ 25.2x · CAP-COST plain 0 salt-diet 2 · UNRESOLVED-CENSORED
total COST (capped at the cap) plain $10.52 · total T 22,405,305
total COST (capped at the cap) salt-diet $180.74 · total T 660,010,533
capped cells METERED (not used above): 3, $37.23 .. $38.31 against cap $37.21
uncapped cells ending above the cap: 0
```
**The verdict kinds are §W6's (= block N §N6), registered before any data.** No premium is RESOLVED, and none can be under rule 2.
⚠️ **Sonnet NTT is CENSORED:** two of its three salt-diet cells are capped, so its median sits at the cap and the ratio is a lower
bound, printed `≥`. WHT is UNDERPOWERED (its salt-diet median is a landed cell).
⚠️ **Every capped cost ENTERS AT THE CAP (rule 6);** the capped cells' metered figures are on their own line and used in no median, ratio
or total. ⚠️ **The figures include the harness's own sandbox probe** (as block N's tables declare): its near-constant cost inflates the
cheaper arm's share, so the ratios are understated. ⇒ **The sign is the reading; the magnitudes are not.**

---
# §4 · THE REGISTERED PREDICTIONS (§W4), REPORTED PER ARM; A MISS IS A RESULT
```
(i) salt-diet CAP-COST >= plain in 2 of 2 problems (2 strictly, 0 ties)
(ii) CAP-WALL cells 0
```
- **(i)** "within a condition, salt-diet's CAP-COST incidence is ≥ plain's": the line above prints the count of problems where it holds.
- **(ii)** "CAP-WALL binds no cell": the line above prints the count.

---
# §5 · THE DECLARED COLUMNS, PRINTED BESIDE THE TABLES
```
pool pool 1 for all 12
claude_live_at_fire >0 in 8 of 12 cells · unread 0
agy_live_at_fire >0 in 5 of 12 cells · unread 0
```
Concurrency is each fire log's own `CONCURRENCY` lines (`cellfacts.tsv` names the live cell per row). Load moves wall time directly and
cost only through behaviour. The agy lane's cells ran on the same box during block W (block WA); the two lanes share no cell, fence or
account.

---
# §6 · ⛔ THE ACCOUNT CHECK, DECLARED
ADDENDUM 2 item 4(a): `lane_identity.py --expect` against the pool's expected digest returned IDENTITY OK at the release (2026-11-14 00:24
PST), with two negative controls each returning rc 5; item 5's zero-cell probe served both model ids. **No per-cell check was run.** Each
cell's pool and config dir is in `cellfacts.tsv` (one pool for all 24), each transcript was served the column's model for its head
records (§1), and each fire's sandbox probe authenticated. That proves each cell ran authenticated on the named pool's dir, not that the
dir's identity matched at that fire. No cell is voided on this.

---
# §7 · ⛔ WHAT THIS DOES **NOT** SAY
1. **No magnitude and no effect size** (§W8 item 1). Every premium is UNRESOLVED by registration.
2. **Nothing about Opus versus Sonnet as models** (§W8 item 2). The two columns are two results of record, and no sentence here compares them.
3. **Nothing about the O37 conditions outside §W1** (§W8 item 3), and **nothing about LU** (§W8 item 4: WHT and NTT are the two of three judged
   feasible, a selection).
4. **These are new problems, ported by the lead** (§W5 item 1). A defect in a task is a harness finding, never an arm effect. **NTT's reference
   proves less than WHT's** (§W5 item 2): its butterfly is not proved equal to the card's sums. No cell's score is touched by that (the suite
   scores the submission), and it is printed here because the two problems sit side by side.
5. **Nothing here is a claim about the salt METHOD.** Any public sentence, and any claim about the method, is the Captain's (§W9).

---
# §8 · PROVENANCE
```
  cells        12 of record in this column (24 in the block), staged and fired by clb_stage.sh / clb_fire.sh from export 0916ef9a on the
               run box, each through the lead's driver (score the previous cell by copy, day-line-check, fire, register)
  scored by    score_claude_v3.py from a git archive of saltbench-systems 0916ef9a (harness and the WHT, NTT task trees), --declared per
               cell (never a glob), --toolchain-env, over a copy of each cell taken after its end marker; the withheld tests never reach
               the run box
  meter        each cell's own ctl/post-end-1.tsv (final_T, final_COST, cap_unit, cap, kind)
  model        served_models_v3.py check-cell, run on the run box over each cell's transcript (12 of 12 clean)
  derived by   evidence/blockW-2026-11-14/w-derive.sh (the run box, its home, the export dir, a local systems clone and the toolchain env
               are its environment, named in its header)
  cellfacts    pool from ctl/run-cfg.tsv (written by number) · export from ctl/built-from.tsv · concurrency from each fire log
  verifier     RESULT-claude-blockW-2026-11-15-verify.py: block NO's verifier re-written for W's shape; prints every figure line above
               from the two tables and asserts each against this document. Its selftest has four arms that can fail (the cap rule as a
               mutant; a FAIL read as PASS as a mutant; an 11-cell column refused; a tie at the cap read in both row orders, red on the
               old cost-only sort) and one PIN (Opus WHT reads CENSORED, the rule a first draft got wrong by counting capped cells instead
               of reading the median). It refuses a condition with other than 3 cells (its median is the middle of three).
```
