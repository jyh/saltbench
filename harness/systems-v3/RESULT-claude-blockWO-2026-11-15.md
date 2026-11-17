# RESULT — O37 block W, OPUS COLUMN · `claude-opus-5` × greenfield × extras=none × WHT, NTT · n = 3
### bench, 2026-11-15. **4 conditions, 12 cells of record. One of block W's two results of record (§W9 = block N §N9: "a result of record per model").**
## 📌 The registration is `AMENDMENT-O37-wht-ntt-greenfield-claude-2026-11-11.md` (§W0–§W9, signed 2026-11-11; ADDENDA 1–3: the release and the WHT re-price)
## 📌 The per-cell tables are FILES: `evidence/blockW-2026-11-14/cells.tsv` (24 rows, both columns; made by `w-derive.sh` beside it) and `cellfacts.tsv` (24 rows: pool, export, concurrency at fire, fire log)
## ⛔ Every figure line below is printed by `RESULT-claude-blockW-2026-11-15-verify.py --block WO --print` from those two tables, and `--check` asserts each one against the bytes of this document. No figure line was typed; a number in prose names its source.

---
# §1 · WHAT RAN
`claude-opus-5` × **greenfield** × **extras=none** × {WHT, NTT} × {plain, salt-diet} × 3. The model is derived per cell from its own
transcript by `served_models_v3.py check-cell`, never from the block name.
```
cells 12 · conditions 4 · model claude-opus-5 · cap COST 37.21
run_state ENDED: CAP-COST 1 · ENDED: EXIT-FORCED 1 · ENDED: LANDED 10
export 0916ef9a6d70 12
end_from HEAD 12
served: 12 of 12 cells clean · head claude-opus-5 only
```
**One end kind is a harness fault, not the subject's.** `clbdtp03` (NTT plain #3) declared its landing and ended `EXIT-FORCED` 30 minutes
later (its own ctl/watch.log: `DECLARED`, then `EXIT-FORCED busy 1812 s after the declaration`): its watcher was fired in the C locale, where the box reader never reads the input box EMPTY, so the
exit keys were withheld until the force timer (the lead's fire; the drivers now set a UTF-8 locale). Its meter is flat from the
declaration on, and its withheld suite reads at HEAD (§2). It is a cell of record, end kind printed as it is.
**One uncapped cell metered above the cap:** `clbdws01` (WHT salt-diet #1, the tripwire T-W-O) LANDED and its final meter (cells.tsv)
reads above the cap (§3's last line): it landed between two cap ticks. It is not a CAP-COST cell and enters at its metered figure.

---
# §2 · CORRECTNESS, VERIFIED FIRST (lane B §Q6 rule 1: withheld-suite FULL PASS over scorable cells)
```
WHT  plain 3/3 [11/11 11/11 11/11] · salt-diet 3/3 [11/11 11/11 11/11]
NTT  plain 3/3 [11/11 11/11 11/11] · salt-diet 3/3 [11/11 11/11 11/11]
FULL PASS plain 6 of 6
FULL PASS salt-diet 6 of 6
```
**Every cell of record passes its withheld suite in full, in both arms.** The one capped cell (`clbdws02`) passes as well; that pass
is a floor (rule 6). With no FAIL in either arm, rule 2's sign is level in both problems.

---
# §3 · COST AND THE PREMIUM (lane B §Q6 rule 3; tested CENSORED → UNDERPOWERED)
```
WHT  median COST plain $6.81 · salt-diet $37.21 · ratio ≥ 5.5x · CAP-COST plain 0 salt-diet 1 · UNRESOLVED-CENSORED
NTT  median COST plain $9.73 · salt-diet $25.99 · ratio 2.7x · CAP-COST plain 0 salt-diet 0 · UNRESOLVED-UNDERPOWERED
total COST (capped at the cap) plain $49.36 · total T 46,743,832
total COST (capped at the cap) salt-diet $176.55 · total T 224,144,902
capped cells METERED (not used above): 1, $38.35 .. $38.35 against cap $37.21
uncapped cells ending above the cap: 1 (clbdws01)
```
**The verdict kinds are §W6's (= block N §N6), registered before any data.** No premium is RESOLVED, and none can be under rule 2.
⚠️ **Opus WHT is CENSORED:** its salt-diet median IS its one capped cell (`clbdws02`; `clbdws03` is below it and `clbdws01` above it in
cells.tsv), so the median sits at the cap and the ratio is a lower bound, printed `≥`. NTT is UNDERPOWERED (no capped cell in either arm).
⚠️ **Every capped cost ENTERS AT THE CAP (rule 6);** the capped cells' metered figures are on their own line and used in no median, ratio
or total. ⚠️ **The figures include the harness's own sandbox probe** (as block N's tables declare): its near-constant cost inflates the
cheaper arm's share, so the ratios are understated. ⇒ **The sign is the reading; the magnitudes are not.**

---
# §4 · THE REGISTERED PREDICTIONS (§W4), REPORTED PER ARM; A MISS IS A RESULT
```
(i) salt-diet CAP-COST >= plain in 2 of 2 problems (1 strictly, 1 ties)
(ii) CAP-WALL cells 0
```
- **(i)** "within a condition, salt-diet's CAP-COST incidence is ≥ plain's": the line above prints the count of problems where it holds.
- **(ii)** "CAP-WALL binds no cell": the line above prints the count.

---
# §5 · THE DECLARED COLUMNS, PRINTED BESIDE THE TABLES
```
pool pool 1 for all 12
claude_live_at_fire >0 in 9 of 12 cells · unread 0
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
