# AMENDMENT — CLAUDE LANE **(B)**: the 64 owed Claude conditions, FROZEN BEFORE THEIR FIRST CALL
## bench (SaltBench lead), 2026-09-16. Desk row **HC**. Ruled by the Captain 2026-09-16 18:49, in words, to a question that named
## this freeze's five sub-forks: *"Yes (B)"*. It decides: HC stage 2 PARKS · the Claude lane moves to the 64 owed Claude conditions
## (census ADDENDUM 8), Opus brownfield first, then Sonnet · F1–F5 on the lead's recommendations · **the first cell fires only after
## a non-author signs this file.** bench is lead AND hand on this lane (HC stage 1's arrangement).
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ **AND NO CELL FIRES BEFORE §Q2's BUILD ITEMS ARE DRIVEN AND AN ADDENDUM NAMES THE
## EXPORT SHA (§Q0 row 4).** Signature and release are two acts, as at level 6 (its ADDENDUM 2 was the release).

---

## §Q0 · ⚖️ THE INPUTS, IN ONE BLOCK SO THE HAND NEEDS NOTHING ELSE
```
  1  MODEL IDs     claude-opus-5 (blocks O, OS) · claude-sonnet-5 (blocks S*). The served set is PER CONDITION (§Q2 item 3):
                     Opus condition    head · worker-opus · reviewer claude-opus-5 · worker-sonnet claude-sonnet-5 ·
                                       designer claude-fable-5-1 (HC stage 1's table)
                     Sonnet condition  claude-sonnet-5 in EVERY role (F3) — head, both workers, reviewer, designer
  2  n             3 per condition.
  3  POPULATION    64 conditions, 192 cells (§Q1). Nothing is added, dropped or substituted.
  4  EXPORT        ONE bare-master sha, named in an addendum BEFORE the first cell, that (i) descends from cc227b4 and so from
                   eacb9ec (the five repaired brownfield givens) and (ii) carries §Q2's five build items. The addendum lists its
                   harness delta from 9f650a3 (HC stage 1's export). One sha for all 192 cells, recorded per cell.
  5  CLIENT PIN    the versioned client 2.1.259 by ABSOLUTE PATH, sha256/16 884baa38fe1a624b in every launch record
                   (PREDICTIONS-HC-stage1-2026-09-13.md §6.2). The PATH's `claude` is NOT the pin. Its versioned directory is present on the run box
                   (listed 09-16; its sha is asserted per launch, not here).
  6  TASK TREE     the EXPORT's own tasks/systems-v3, and nothing else (§Q2 item 1, measured reason).
  7  CAPS          pricing profile + cost_caps.tsv, unchanged (§Q4).
  8  FIRE ORDER    §Q3, one cell at a time, pairs kept whole; a tripwire cell opens each of O, OS, S.
  9  PREFLIGHT     per block and per cell, §Q3.4. Zero spend except the per-cell sandbox probe turn (§Q2 item 4).
```

---

## §Q1 · THE POPULATION — 64 CONDITIONS, 192 CELLS
Derived from the census, not typed: each model owns 5 problems × {greenfield, brownfield} × {plain, salt-diet} × {none, statement,
spec-change} = 60, less Paxos × statement (4, INEXPRESSIBLE, §C3(a)) and brownfield × spec-change (10, skipped by the Captain,
ADDENDUM 1), = **46**. Opus's greenfield 28 are DONE (§C4), which leaves **18**. Sonnet has no cell of any kind (§D4, §F2), so all 46 are owed.
```
  block  model   field        extras        problems                           arms               conditions   cells
  O      Opus    brownfield   none          Crc32 · FreeList · LRU · LZW · Paxos plain · salt-diet      10          30
  OS     Opus    brownfield   statement     Crc32 · FreeList · LRU · LZW         plain · salt-diet       8          24
  SG     Sonnet  greenfield   none          all five                           plain · salt-diet      10          30
  SB     Sonnet  brownfield   none          all five                           plain · salt-diet      10          30
  SS     Sonnet  greenfield   statement     Crc32 · FreeList · LRU · LZW         plain · salt-diet       8          24
  SBS    Sonnet  brownfield   statement     Crc32 · FreeList · LRU · LZW         plain · salt-diet       8          24
  SC     Sonnet  greenfield   spec-change   all five                           plain · salt-diet      10          30
                                                                                              TOTAL     64         192
```
**ARM → FLAGS** (`cell_build.py --client claude --budgets pricing`, task from the export tree):
```
  bare   --arm <plain|salt-diet> --field <greenfield|brownfield>                 (brownfield takes --phase 1)
  stmt   --arm <plain|salt-diet> --field <greenfield|brownfield> --statement      (brownfield takes --phase 1)
  spec   phase 1 as bare greenfield, then phase 2 by the customer dispatch (card_extras none; customer.sh D7 refuses extras)
```
⛔ **`--arm salt-diet`, NEVER `--arm salt`.** ⛔ **No placebo arm** (the grid has none, census §J3). ⛔ **`--hint` is not used.**

---

## §Q2 · ⛔⛔ THE FIVE BUILD ITEMS — EACH DRIVEN, WITH A CONTROL, BEFORE THE CELLS IT GATES
Each item is a harness change landed on bare master and read by a party that did not write it. **Sequencing (the helm's read,
adopted): items 1, 2, 4 and 5 precede the first Opus cell; item 3 precedes the first Sonnet cell and is the only one whose absence
CORRUPTS a result rather than delaying it.**

**1 · THE FIRE, STAGE AND HARVEST PATH IS TRACKED.** *Measured 2026-09-16 at the run box:* HC stage 1 did NOT run through
`fire_pricing.sh`/`pair_launch_v3.sh` (tracked only on branch `bench/v3-referee-rust`, 778fc25, and absent from master cc227b4). It ran
through two UNTRACKED scripts in the run box's home directory, `bench-hc1-stage.sh` (7,432 B) and `bench-hc1-fire.sh` (18,956 B), which
call `cells_bin.sh`, `cell_build.py` and `cell-watch.sh` directly from the 9f650a3 export directory. ⚠️ **And the stage script took its
TASK tree from a 2026-09-09 referee tree, not from the export.** For stage 1 this is harmless and is checked, not assumed: `G/` is
byte-identical for all five problems, `card.md` differs on four of them only by APPENDED lines that open a `## Statement` section a bare
build does not render, and four stage-1 cells (Crc32, FreeList, LRU, Paxos) carry no Statement section in their root-commit
`REQUIREMENTS.md` (control: 1 `## ` header each). **For this freeze it is not harmless:** that tree
has no `brownfield/` for any problem and no Statement for three. ⇒ **REQUIRED:** the stage and fire scripts tracked in the harness, taking
problem · arm · field · extras · model block as arguments, the task tree and harness ONLY from the export directory named by §Q0 row 4,
roots under the prefix `cells-clb-`, the HC1 guards carried (an ended cell is never re-fired; unique log per invocation; beat-based
liveness, never a process-name search; the pin by absolute path; the credential checked by BODY, because the client exits 0 on an auth
failure), and the harvest (meter + price receipt) tracked beside them. **Control:** a dry build per block shape refuses a task tree
outside the export, and refuses an existing cell.

**2 · RUN STATE FOR A CLAUDE CELL.** *Measured 2026-09-16, the classifier driven read-only on a real Claude brownfield cell (the 09-14
sandbox-probe cell, LZW plain):* `brownfield_rewrite_class.py` ALREADY computes the class and `retained` for a Claude cell
(`UNTOUCHED 1.000`, correct for a cell no subject session edited) and reads its W1 seed **COVERED** by the cell's `ctl/fence.json`.
⛔ Its own comment says a Claude cell's fence "never lands in ctl/" and reads UNVERIFIED; the launcher passes `--settings ctl/fence.json`
and the cell carries it, so **the comment is stale and the column is not.** What it CANNOT do is `run_state`: every non-agy client reads
`UNDETERMINED`. ⇒ **REQUIRED:** `run_state` learns the Claude lane's terminal marker — `ctl/end-<phase>`, written by `cell-watch.sh`
(a stage-1 cell reads `<ts> LANDED landing-1 <sha>`) — DRIVEN over every Claude cell on the box with the census of end kinds printed,
and never LANDED by default. **Controls:** a live cell (fresh `watch.beat`, no `end-1`) reads RUNNING; a cell with no launch log reads
NEVER-LAUNCHED; a COPY of a Claude brownfield cell with a planted wholesale rewrite reads REPLACED (copied under the box's scratch
directory, never into a cells root). The stale comment is corrected in the same commit.

**3 · THE SERVED-MODEL VOID IS READ AGAINST THE CONDITION.** *At cc227b4:* the model is a property of the cells root's
`_bin/models.tsv` (no per-cell flag, `cell-claude.sh` reads its head/worker/designer rows), `agents.json` gives the reviewer the
worker-opus id, and `referee_v3.py` `model_check` accepts the UNION of the served column of the harness's own table — so an Opus record
inside a Sonnet cell reads `clean`. ⇒ **REQUIRED:** (a) an all-Sonnet role table tracked in the export and linked as `_bin/models.tsv`
for Sonnet roots only, with the stage script refusing a root whose table disagrees with the block's model; (b) a per-cell check that
reads EVERY assistant record, head and sidechain, against §Q0 row 1's set for the cell's CONDITION (`<synthetic>` excepted), and prints
the served set per cell. **Control:** the check reads `SUBSTITUTED` on a stage-1 Opus cell's transcript scored as a Sonnet condition,
and `clean` on the same transcript scored as an Opus condition.

**4 · A SANDBOX RECEIPT FOR EVERY CELL'S OWN FENCE, ENFORCED AT LAUNCH.** *At cc227b4:* the probe receipt of 2026-09-14 holds for
client 2.1.259 and ONE fence sha, "never by cells root, never by wave, never by date" (its §R4); fences are rendered per cell and the
deny set enumerates sibling cells; `--require` is built and driven in selftest and referenced by no launcher. That receipt left the
wiring to a lead's ruling (§R4, §R5 item 3). ⇒ **RULED:** wire `--require` into `cell-claude.sh`'s launch for every client but the
DRY stub, and run `probe_sandbox_v3.sh` per cell after staging and before fire, with nothing created in `$HOME` or the cells root
between the probe and the launch (the fence is a render-time glob). **Controls:** a cell with no receipt HOLDs at launch; a cell whose
receipt names another fence sha HOLDs; a cell with its own receipt launches (driven on the DRY stub for the launch half). **Cost:** one
`claude -p` probe turn per cell, metered as its own line and never inside a cell's COST.

**5 · A TRACKED CORRECTNESS SCORER FOR CLAUDE CELLS.** Stage 1 scored cost only (its §6). `score_wave_v3.sh` is the agy scorer (it reads
`agy-stderr-*` and `agy_shell_count_v3.py`) and `score_matrix1.py` is a COST reader on bench branches. ⇒ **REQUIRED:** a
tracked scorer that, from a COPY of each cell, runs the rung's withheld suite, records pass/total AND the failing test NAMES, derives
`bugs_fixed` against the registered detecting tests and `bugs_introduced` against the seed baseline (§B3), attaches item 2's class and
`retained`, and prints on its first line the tree sha it ran from (dirty-tree marker as in `score_wave_v3.sh`). ⛔ **FreeList is margin 1:**
the scorer asserts `exhaust_and_recover` EXISTS and RAN, or V1 reads UNMEASURED for that cell (RECORD-brownfield-givens; at cc227b4 the
name occurs in 0 harness files against 2+ in the withheld tests). **Controls:** the seed itself scores as the baseline; the withheld
reference scores FULL PASS; a FreeList copy with that test removed reads V1 UNMEASURED.

📌 **Also owed before a cost-capped fire, zero spend:** `rates.tsv` was read 2026-09-05 and its header orders a re-read before any run
whose caps are set in cost. Re-read and re-date, or record in the release addendum why the rows stand.

---

## §Q3 · ⚖️ THE DISCRIMINATING TARGET, THE ORDER, THE TRIPWIRES, THE PROCEDURE
### §Q3.1 · Expectations — each cites a result of record and says when that record is another lane or model. None predicts an arm contrast.
```
  order  block  expectation            prior
  1      O      VARIES (retention)     OTHER LANE. agy Pro level 4: retained plain 0.621..0.992, salt-diet 0.137..0.756; REPLACED 0 vs 2;
                                       FULL PASS plain 12/12, salt-diet 7/12 (RESULT-gemini-brownfield-level4-2026-09-14.md §R2, §R3).
                                       Its LRU and Paxos cells STAND; FreeList and LZW are VOID for the find-the-defect claim (§V3)
                                       and ORDER only. No Claude brownfield cell has a result of record.
  2      OS     VARIES — BORROWED      No brownfield × statement cell has a result of record on any lane. Borrowed from row 1.
  3..7   S*     BORROWED FROM OPUS     every Sonnet expectation is the Opus row of the same condition (census §C4, block O/OS once
                                       scored). A different Sonnet shape is a result about Sonnet, never a failed prediction.
```
⛔ **Crc32 is a LOUD, CEILING rung** (all five mutants at margin 5/6 with one failing set, RECORD-brownfield-givens; census ADDENDUM 4)
and its brownfield conditions are registered **AT CEILING**, fire LAST inside their block, and are never pooled with the other four.
⛔ **A CEILING IS NOT PARITY** (UNRESOLVED-BY-CEILING on pass rate). ⛔ **LANDED IS NOT VERIFIED** (§Q6 rule 1).

### §Q3.2 · The order
```
  blocks      O → OS → SG → SB → SS → SBS → SC       (SC last: phase 2, C2 is §9's half-rule on a number never observed,
                                                       and the Opus spec-change row already carries CAP-COST censoring)
  problems    LRU → Paxos → FreeList → LZW → Crc32    (direct standing priors → voided-for-finding priors → the ceiling rung;
                                                       statement blocks omit Paxos)
  cells       per problem: plain#1 · salt-diet#1 · plain#2 · salt-diet#2 · plain#3 · salt-diet#3
```
**One cell at a time.** A halt after any cell leaves every earlier PAIR whole (stage 1 §6.1's stopping argument, per pair).

### §Q3.3 · Tripwires — ONE cell, read by the lead, posted, before its block continues
```
  T-O    Opus · LRU · salt-diet · brownfield bare (the treatment arm, the cheapest standing prior)
  T-OS   Opus · FreeList · salt-diet · brownfield statement (the widest level-4 separation; level 7's BS choice)
  T-S    Sonnet · LRU · plain · greenfield bare (the first Sonnet-headed cell the campaign has ever run; plumbing, not arms)
  T-SC   the first SC cell, read after its phase 2 ends
```
**The lead reads, for each:** `ctl/field` · `ctl/card_extras` (and `## Statement` rendered for T-OS) · the given at the first commit
byte-identical to the export's (brownfield) · W1 COVERED · a P-SANDBOX receipt for the cell's own fence sha · the pin sha in the launch
record · the end marker verbatim · `run_state` terminal (item 2) · the served set (item 3; T-S: every record `claude-sonnet-5`, and no
COST-BLIND) · the scorer's first line naming the export sha · the concurrency column. **All read ⇒ the block continues on one bus line.**
Any row that does not read HOLDS the block; the tripwire cell counts as cell 1 of its condition unless §Q7 voids it.

### §Q3.4 · The preflight, carried from stage 1 §6.3 with one registered change
1. **QUOTA** on the Claude lane, read before each block and at each bank (the Claude log reports percent USED).
2. **IDENTITY** of the cells' config dir from the credential-identity tool, never from the directory's name; and a trivial authenticated
   read checked by its BODY.
3. ⚖️ **CONCURRENCY — THE ONE CHANGE, AND IT IS DECLARED RATHER THAN SLIPPED.** Stage 1 registered *"no cell of any wave running"* and
   under-enforced it (23 of 45 cells shared the box with agy cells; its §5.1). **This freeze registers instead: no other CLAUDE-lane cell
   live (enforced by the fire script), agy-lane cells PERMITTED, and the per-cell concurrency census a REPORTED column.** Why: the agy
   lane's levels 6-8 run as continuous chains on the same box, and the stage-1 rule would make this lane's progress a function of that
   schedule. Stage 1 measured the cost of the exposure as readable (load moves wall time directly and cost only through behaviour; the
   treatment arm was the least exposed). Pairs fire adjacently (§Q3.2), so a pair's two cells share their exposure more closely than
   any two cells do. ⛔ The hand yields its NEXT fire (never a running cell) when the agy hand declares a zero-spend window that needs no
   cell of either lane live (`dry_phase2_v3.sh` refuses while any `cell-claude.sh` process is live).
4. **A FRESH ROOT: settings → fence → trust, in that order.**
5. **THE PIN** by absolute path. 6. **PER CELL:** stage → `cell-claude.sh --check` → sandbox probe → fire, nothing created in between.

---

## §Q4 · CAPS — CARRIED, NOT RE-DERIVED, AND WHICH ONES ARE ARMED
```
  phase 1   C1_USD $37.21     phase 2 (SC only)   C2_USD $18.60           cost_caps.tsv, unchanged; the builder REFUSES a differing cap
  wall      W1_SEC 144,000    W2_SEC 72,000                                pricing profile, cell_build.py
  printed   T1_TOK 250,000,000 · T2_TOK 120,000,000 — READ AND PRINTED, NEVER A CAP under the COST unit
  other     IDLE_SEC 600 · POKE_MAX 12 · STALL_SEC 2,700 · EXIT_FORCE_SEC 1,800
```
⛔⛔ **F4's PREMISE IS CORRECTED AT THE OBJECT.** The sub-fork said the 250 M-token cap "may bind Sonnet before USD does". At cc227b4,
`cell-watch.sh` `load_budgets` sets `CAP_UNIT=COST` whenever a `C<phase>_USD` row exists, and under COST the meter tick ends the session
on CAP-COST and **prints T without ever ending on it**; CAP-TOKENS is reachable only in the TOKENS unit, which a pricing cell REFUSES to
arm. ⇒ **The armed caps are CAP-COST and CAP-WALL, for both models.** *(The agy lane's unwired token cap, found earlier on 2026-09-16 (level 6 ADDENDUM 7), was the
opposite shape: a registered cap no script read. Here the script reads the row and deliberately does not arm it.)*
**F4 AS RULED, RESTATED ON THE ARMED CAPS:** Opus carries the lane's USD cap unchanged. For Sonnet the same USD cap stands (a different
cap is a new dated amendment), and at `rates.tsv`'s rows Sonnet costs 0.40 × Opus on every column, so **$37.21 buys a Sonnet session the
token mix $93.03 buys an Opus one.** **REGISTERED PREDICTIONS, per arm, before any data:** (i) on every problem, CAP-COST incidence in a
Sonnet condition is ≤ that in the Opus condition of the same field × extras × arm; (ii) within a condition, salt-diet's CAP-COST
incidence is ≥ plain's (stage 1 §5.3: the cap censored the treatment arm on FreeList and Paxos); (iii) CAP-WALL binds no cell. Each is
reported as a split by arm and model, and a miss is a result.
⛔ **A cap-out is a RESULT, not a void, and enters its median at the cap** (PREDICTIONS-HC-stage1 §4 item 2). No cap is raised.

---

## §Q5 · ⛔⛔ THE CONFOUNDS — REGISTERED, AND THEY TRAVEL WITH EVERY TABLE
1. **THE MODEL AXIS IS A TEAM AXIS.** An Opus condition is an Opus head with Sonnet and Fable workers (HC1's table); a Sonnet condition
   is Sonnet in every role (F3). Any Opus↔Sonnet difference names both, every time.
2. **THE ROLE TEXT IS UNCHANGED IN A SONNET CELL, AND IT IS FALSE THERE.** `render/SEAT.md` routes classes to `worker-sonnet`,
   `worker-opus` and `designer` and says the design tier costs several times the others; `agents.json`'s names say the same. ⚖️ **Ruled
   on the lead's rec: kept byte-identical across models,** so the model axis carries no prompt delta; the false tier text is declared here
   and in every Sonnet table.
3. **A USD CAP IS A DIFFERENT TOKEN BUDGET PER MODEL** (§Q4). A Sonnet-vs-Opus difference in censoring is a cap-policy result first.
4. **CONCURRENCY WITH THE AGY LANE** (§Q3.4 item 3): a reported column, with its registered direction of bias.
5. **DATE, EXPORT AND ACCOUNT versus the priors in §Q3.1**: they order the wave and are never the other arm of a contrast.
6. **CROSS-LANE:** block O versus agy level 4 or level 7 is NOT a registered contrast (client, model, caps in different units, fences
   of different construction).

---

## §Q6 · THE READING RULES
1. **VERIFIED FIRST.** A condition's pass rate is withheld-suite FULL PASS over scorable cells; LANDED is a separate column; a
   self-graded landing is never quoted.
2. **SIGN ONLY.** No brownfield dispersion has been measured (§B6) and no Sonnet dispersion exists, so no floor here is this
   population's own. Retention, pass rate and cost premium are reported as signs with their per-cell values beside them.
3. **THE VERDICT-KIND VOCABULARY, REGISTERED (F5).** Every premium carries exactly one of RESOLVED · UNRESOLVED-UNDERPOWERED ·
   UNRESOLVED-CENSORED · UNRESOLVED-MEASURED · NOT-SCORED, tested CENSORED → UNDERPOWERED → MEASURED, and a bare "UNRESOLVED" is not a
   legal cell. ⛔ **By rule 2, RESOLVED and UNRESOLVED-MEASURED are UNAVAILABLE in this freeze by construction** (both need a floor this
   population supports). **Every condition's expected kind is therefore registered now as UNRESOLVED-UNDERPOWERED,** read CENSORED where
   the cap's arithmetic forbids a clearing median, NOT-SCORED where §Q7 removes the cells. *This freeze fills the matrix with signs and
   correctness; it cannot produce evidence about effect size, and says so before the first call.*
4. **RETENTION IS THE BROWNFIELD PRIMARY SEPARATOR,** per cell, never averaged across problems; REPLACED below 0.20 (§B5) and UNTOUCHED
   reported as classes. A class is quoted only for a cell whose run state is terminal (§Q2 item 2) and whose W1 reads COVERED.
5. **FIND-THE-DEFECT PER CELL:** `bugs_fixed` from the failing-test names against the registered detecting tests; `bugs_introduced ≥ 0
   (suite-limited)` with the margin beside it (§B3).
6. **CAPS AS FLOORS** (§Q4). A capped cell's pass result is a floor and its cost enters at the cap.
7. **THE REGISTERED READING IS ARM WITHIN CONDITION.** Statement-versus-bare, Opus-versus-Sonnet and Claude-versus-agy readings are
   not registered; if made, §Q5 travels with them.
8. **An arm-correlated cut is decided by its sign.** 9. **A cost result and a pass-rate result are two results.**

## §Q7 · WHAT VOIDS A CELL (faults only — no expectation from §Q3 appears here)
```
  1  a served model outside the CONDITION's set (§Q0 row 1), head or sidechain            VOID(MODEL)
  2  METER-BLIND, or COST-BLIND (a served model with no rates row)                          VOID(UNPRICED)
  3  ctl/field or ctl/card_extras differs from the condition                                VOID
  4  cell-claude.sh --check HOLDs, or no sandbox receipt for the cell's fence sha            DO NOT FIRE
  5  the launch record's client sha is not 884baa38fe1a624b                                 VOID(PIN)
  6  the given at the first commit is not the export's (the classifier's witnesses REFUSE)  VOID(GIVEN)
  7  W1 reads UNCOVERED                                                                     class and retention NOT QUOTED; cell scored
  8  FAILED BOOT / a credential that did not authenticate                                   NOT-SCORED(HARNESS), re-fired as a new cell id
  9  CAP-COST · CAP-WALL · STALL · IDLE · POKE exhaustion                                   NOT void: reported per arm and model
 10  an ended or result-bearing cell dispatched into again                                  DO NOT FIRE (reuse by copy only)
```

## §Q8 · WHAT THIS FREEZE CANNOT ESTABLISH, SAID BEFORE ANY DATA
1. **No magnitude and no effect size** (§Q6 rules 2-3). 2. **Nothing about Opus versus Sonnet as models** (§Q5.1-3). 3. **No cross-lane
comparison.** 4. **A ceiling says nothing about the arms.** 5. **A planted defect is not a sample of real defects; k = 1 per problem**
(§B8). 6. **Nothing about whether a subject used the statement.** 7. **Nothing about the 124 Claude cells run before the sandbox probe
existed** (receipt §R4).

## §Q9 · WHAT THE HAND DELIVERS, AND WHAT THE LEAD OWES AFTER
```
  the release addendum (export sha + delta from 9f650a3 + the five items' receipts + the rates re-read) · the tripwire readings ·
  per-cell: model · block · problem · arm · field · extras · export sha · pin sha · fence sha + probe receipt · COST · T · wall ·
  end kind verbatim · run state · suite pass/total + failing names · bugs_fixed · bugs_introduced floor + margin · retained · class ·
  W1 · served set (head, sidechain) · agy concurrency share · attempt number · source receipt · CAP incidence split by arm and model ·
  the quota rows read · per-condition score receipts as FILES, each scorer's first line naming the export sha
```
⇒ **The lead writes a result of record per block and RE-CUTS THE MATRIX CENSUS IN THE SAME COMMIT** (council 09-16 ⑤d), with the verdict
kind beside every premium. Any public sentence, and any claim about the method, is the Captain's.

---

---
## ✍️ NON-AUTHOR SIGNATURE — the helm (83rd head), 2026-09-16 19:3x PDT, on §Q0–§Q9

**SIGNED AT BLOB `4aa24eb2f4429f0774ce6db1616b9c1b1f28d738`**, resolved at `2ebd98c:harness/systems-v3/AMENDMENT-claude-lane-B-2026-09-16.md`. Read WHOLE, all 265 lines. A NEW file, so append-only does not apply and I say so rather than claiming an arm I did not drive.
📌 **SCOPE, TAKEN FROM THE FREEZE'S OWN WORDS: this covers §Q0–§Q9 and RELEASES NOTHING.** No cell fires until §Q2's five items are driven with controls and a release addendum names the export sha. **Signature and release are two acts.**

### WHAT I DROVE AT THE OBJECT — each with a control
```
  1 BLOB IDENTITY   2ebd98c:<this file> = 4aa24eb2f…  == the blob the lead pinned                    ✅
                    one commit, ONE file, off merge-base 8728e2e                                     ✅
  2 §Q1 ARITHMETIC  DERIVED, never read off the table: 5×2×2×3 = 60 per model, less Paxos×statement
                    4 and brownfield×spec-change 10 ⇒ 46 owed. Opus greenfield done = 5×2×3−2 = 28,
                    so Opus owed 18 = O(10)+OS(8). Sonnet 46 = SG+SB+SS+SBS+SC. TOTAL 64.
                    Block table sums: conditions 64 · cells 192 · n=3 consistent                     ✅
  3 F4's PREMISE    THE CORRECTION IS TRUE AT THE CODE, and the code says so itself. cell-watch.sh
    (it OVERTURNS   `if [ -n "$COST_CAP" ]; then CAP_UNIT=COST; else CAP_UNIT=TOKENS`, and its own
     a sub-fork)    comment: "a C<phase>_USD row arms the cap in COST — CAP-COST ends the session,
                    T is read and printed beside the cost and never ends it."                        ✅
                    The pricing profile REFUSES to arm in TOKENS ⇒ CAP-TOKENS is unreachable here.   ✅
  4 ITEM 3's        `referee_v3.py:524-529` builds `served` as a SET over EVERY row of models.tsv
    CORRUPTION      and flags only models OUTSIDE that union ⇒ an Opus record inside a Sonnet cell
    RISK            really does read `clean`. THE FREEZE'S SEQUENCING CLAIM IS CORRECT: item 3 is
                    the only one whose absence CORRUPTS rather than delays.                          ✅
  5 ITEM 5's        `exhaust_and_recover` at cc227b4: harness files 0 · withheld test files 13
    FreeList CLAIM  (the freeze claims 0 vs "2+"). The margin-1 assertion is well founded.           ✅
  6 HYGIENE         no session trailer or chat URL in title, body or commit message                  ✅
```

### ⚖️ THE FORK AT §Q3.4 ITEM 3 — RULED (b), ON THE LEAD'S RECOMMENDATION
**(b): no other CLAUDE-lane cell live; agy-lane cells PERMITTED; the per-cell concurrency census a REPORTED column.**
**THE REASON IS THE REGISTERED READING, NOT CONVENIENCE.** §Q6 rule 7 registers the reading as **ARM WITHIN CONDITION**, and §Q3.2 fires pairs adjacently (`plain#1 · salt-diet#1 · …`). ⇒ ***THE CONFOUND IS SMALLEST EXACTLY WHERE THE READING IS TAKEN*** — a pair's two cells share their agy exposure more closely than any two cells in the wave do. **(a) would buy protection where no contrast is registered, and pay for it by making this lane's progress a function of the agy chain schedule** — with levels 6, 7 and 8 running as continuous chains on one box, that is a lane that may not fire at all.
⭐ **AND IT IS A CONFOUND WITH A KNOWN SIGN, WHICH IS A BOUND RATHER THAN A DOUBT:** load moves wall time directly and cost only through behaviour. It is registered (§Q5.4), reported per cell (§Q9), and the yield clause protects the agy lane's zero-spend windows. ⛔ **(a) IS NOT REFUTED — it is the stricter rule, and it is declined on price, which is a different thing and is said so plainly.**

### ⛔ WHAT I DID **NOT** VERIFY — named so this signature is not read wider than it is
1. **§Q1's population against the CENSUS.** I derived 64/192 from the freeze's OWN stated exclusion rules and it is internally exact. **I did not open census ADDENDUM 8 to confirm it says 64.** If the census disagrees, my arm 2 does not catch it.
2. **§Q3.1's priors** — the level-4 retention figures, REPLACED counts and FULL PASS rates are quoted from another lane's result of record. **I did not re-read it.**
3. **The `rates.tsv` 0.40× claim** underneath F4's restatement, and stage 1's §5.1/§5.3 figures.
4. **The 09-14 sandbox receipt's §R4/§R5**, which item 4 rests on.
5. **The five §Q2 items themselves** — unbuilt by construction; they are preconditions, and this signature asserts nothing about whether they will pass.
⇒ **This signature covers the freeze's INTEGRITY: pinned, internally exact in its population arithmetic, its two code-level claims true at the objects with the corrupting one correctly singled out, its fork ruled, and its scope honestly bounded.** It is not a second opinion on the science.

### 📌 ONE THING THE CAPTAIN SHOULD HEAR, AND IT IS NOT AN OBJECTION
**His *"Yes (B)"* answered a question that named F4 as posted — and F4's PREMISE WAS THEN FOUND FALSE at the code.** The lead did the right thing: it **restated** F4 on the armed caps with three registered predictions rather than quietly dropping it. ⇒ 🔑 ***AN ACCEPTED FORK IS NOT AN ACCEPTED PREMISE, AND THE PARTY WHO DISCOVERS THE PREMISE MOVED OWES THE WORD, NOT THE SILENCE.*** It is carried to the 09-17 council alongside the same shape found tonight on desk `PT`. **Nothing is blocked by it.**

**⇒ SIGNED.** Nothing fires before §Q2's five items are driven with their controls and a release addendum names the export sha and carries the `rates.tsv` re-read.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>

---

## ⚖️ ADDENDUM 1 — §Q2 ITEM 6 (THE DENY SET AGAINST A CENSUS), AND WHAT BUILDING ITEMS 1, 2 AND 5 CHANGED. APPENDED; §Q0–§Q9 and the signature untouched.
**bench (lead), 2026-09-16 20:0x PDT.** Each clause below narrows or adds a precondition. None loosens one. It goes to a non-author for signature
before it binds, and it cites `RESULT-HC1-stage1-2026-09-16.md` ADDENDUM 1 and its instruments, which land in saltbench #184.

### A1.1 · ⛔ §Q2 ITEM 6 — THE FENCE IS CHECKED AGAINST A CENSUS OF WITHHELD TREES, RE-RUN AT RELEASE, NEVER AGAINST A LIST
**Found while building item 5, measured at the objects** (`RESULT-HC1-stage1-2026-09-16.md` ADDENDUM 1, with its instruments and outputs
under `evidence/hc1-stage1-instruments-2026-09-16/exposure/`). A read-only census of the run box's home directory found 194
withheld-shaped entries in 7 top-level trees. A Claude cell's sandbox `denyRead` covers 5 of them. **Two are NOT covered:** a referee tree
(25 entries, uncovered for both lanes) and a rescore tool (7 entries, uncovered for the Claude lane only). HC stage 1's measured use of
either was 0 across all 143 transcript files.
⇒ **REQUIRED BEFORE THE FIRST CELL:**
1. Both trees are moved inside the belt or off the box, in a two-lane-quiet window the helm schedules. A tree in reach of a live cell is
   never moved.
2. `withheld_exposure_census.py` is RE-RUN at release against a cell staged from the release export, and against a current agy fence.
   **Every tree reads COVERED**, and `census.out` is filed with the release addendum.
3. **The census's limits ride with its verdict:** depth 7, no tarball interiors, no cells roots, a name-based walk. **Moving the two trees
   closes the MEASURED exposure, not the class**, and a green census is a floor on the population, never proof of its size.

### A1.2 · ⛔ THE RUN BOX TAKES A NO-WITHHELD EXPORT, AND SCORING RUNS OFF THE BOX (refines §Q0 rows 4 and 6)
`studio_export.sh` is the harness's allowlist export; its header says *"no withheld byte ever reaches the Studio"*. Measured on the run box: export
`abb7829` holds **0** withheld dirs, and export `9f650a3`, the one HC stage 1 used, holds **42** (under `~/projects`, which is fenced).
⇒ **The release export is cut by the allowlist exporter and carries no `withheld/` or `mutants/`.** `clb_stage.sh` REFUSES a task tree
that carries either (driven: the 9f650a3 export was refused by name). ⇒ **Item 5's scorer runs on HARVESTED COPIES of ended cells, on a
box where the withheld suite legitimately lives.** The scorer does not care where it runs; this clause fixes where it may.

### A1.3 · CELLS ROOTS ARE CREATED ONCE, IN THE SAME WINDOW
A cells root is a new `$HOME` entry, and an entry created while any cell of either lane is live sits outside that cell's fence until its
next render. ⇒ **All 64 roots are created by one `clb_stage.sh --roots` run in A1.1's window.** Staging refuses a missing root
(driven: refused by name, with 0 clb roots in `$HOME` afterwards).

### A1.4 · WHAT A DRY DRIVE OF THE FIRE PATH CANNOT REACH, SO T-O READS IT (adds to §Q3.3)
`clb_fire.sh --dry` stops BEFORE the settings render. A dry scratch config dir was REFUSED by `render_fence_v3.py`, because a config dir
outside the `~/.claude*` deny set cannot be fenced. That refusal is the guard working. ⇒ **The first real fire is the first drive of settings
→ trust → fence convergence → `--check` → sandbox probe → `--require` → launch on the tracked scripts.** ⇒ **T-O's reading list gains:** the
fire log's `SETTINGS … read back`, `TRUST SEEDED`, `FENCE CONVERGES (sha16 …)`, `CHECK CLEAN` and `P-SANDBOX GREEN for fence …` lines, and the
receipt file under `<root>/_audit/sandbox-probe/` for that sha.

### A1.5 · THE LANE'S ENV FILE IS UNTRACKED BY DESIGN, AND THE RELEASE ADDENDUM NAMES ITS KEYS
The stage, fire and harvest scripts take the config dir, the pinned client, its sha, the export and the probe's outside file from a run-box
env file, because the public tree's gate forbids account and host names. **The release addendum names the file's keys, and the export sha
and pin sha it asserts. It never names the values that identify an account.**

### A1.6 · WHERE THE ITEMS STAND AT THIS WRITING
```
  item 1  tracked stage · fire · harvest     built, dry-driven, awaiting a non-author read     (A1.3, A1.4)
  item 2  run_state for claude cells         helm-signed, on harness master 4dfcad6
  item 3  served-model void by condition     systems
  item 4  --require wired + per-cell probe   systems (item 1's fire already calls both)
  item 5  Claude correctness scorer          helm-signed, on harness master 4dfcad6 (A1.2)
  item 6  deny set vs census                 this addendum; the move and re-run are A1.1's window
```

---
## ✍️ NON-AUTHOR SIGNATURE — the helm (84th head), 2026-09-16 20:2x PDT, on ADDENDUM 1 (A1.1–A1.6)

**SIGNED AT BLOB `e287d99be50f1ea94986171e8c880772f2679f9c`**, resolved at `78832de:harness/systems-v3/AMENDMENT-claude-lane-B-2026-09-16.md` — **the blob and the head the lead pinned in its own ask, matched at the forge.** Read WHOLE.
📌 **SCOPE: A1.1–A1.6 only. §Q0–§Q9 and the 83rd head's signature are untouched and are not re-opened.** This addendum **RELEASES NOTHING** — it adds preconditions to a freeze that already fires nothing.

### WHAT I DROVE AT THE OBJECT — each with a control
```
  1 BLOB + TIP      e287d99be5… == the lead's pinned blob · head 78832de == the lead's ask      ✅
  2 APPEND-ONLY     TWO methods: numstat 54/0, and removed-line count 0 against a control
                    that finds the added lines. §Q0–§Q9 and the prior signature untouched.      ✅
  3 EVERY CLAUSE    read one by one against the claim "each narrows or adds a precondition,
    NARROWS         none loosens": A1.1 adds a release re-run · A1.2 fixes where the scorer
                    may run · A1.3 forces one roots run · A1.4 adds to T-O's reading list ·
                    A1.5 constrains what the addendum may name. TRUE of all five.              ✅
  4 A1.1 AGAINST    194 entries / 7 trees · 5 covered · 2 not (25 and 7) · 0 use across 143
    ITS SOURCE      transcript files — each re-read off #184's TRACKED OUTPUTS, not its prose.  ✅
  5 THE FOUR CODE   verified at the source on this box, verbatim:
    CLAIMS          studio_export.sh:6   "no withheld byte ever reaches the Studio"            ✅
                    clb_stage.sh:70-71   find -type d \( -name withheld -o -name mutants \)
                                         then die — BOTH names, exactly as A1.2 claims         ✅
                    clb_stage.sh:28      "a missing root is REFUSED and names this mode"       ✅
                    clb_fire.sh:100      "⛔ --dry STOPS HERE, AND SAYS WHAT IT DID NOT DRIVE"
                                         with :21 "up to the settings render and stops there"  ✅
  6 REFUSAL DRIVEN  clb_stage.sh:70's expression on a fixture: a clean task tree PASSES, a
    (both arms       tree carrying `withheld/` REFUSES and names it, a tree carrying
     differ)         `mutants/` REFUSES and names it. The guard discriminates.                 ✅
  7 HYGIENE         no session trailer in the commit (control: Co-Authored-By = 1), no chat
                    URL in the PR body, all 10 forge checks green                              ✅
```

### ⭐ A1.6 IS ALREADY SUPERSEDED, AND ITS HEADING IS WHY THAT IS NOT A DEFECT
A1.6 reads *"item 1 … awaiting a non-author read"* and items 2 and 5 at `4dfcad6`. **Within five minutes of this blob, item 1 was on master; within thirteen, §Q2 items 1–5 were all merged and master had moved to `2822925`.** ⇒ **The table was true when written and is false now.** It is not a defect **because its heading is `WHERE THE ITEMS STAND AT THIS WRITING`** — the self-scoping form the stale-matter law asks for. ⇒ 🔑 ***A PRESENT-TENSE STATUS TABLE ROTS; ONE THAT DATES ITSELF IN ITS OWN HEADING IS A RECORD INSTEAD OF A CLAIM.*** Recorded so a later reader takes A1.6 as history, not as state — **read the harness master, never this table.**

### ⛔ WHAT I DID **NOT** VERIFY
1. **A1.2's export measurements** — that `abb7829` holds 0 withheld dirs and `9f650a3` holds 42. Those are readings of the RUN BOX's exports; **the exports are not on this box** and I did not reproduce them. I verified the exporter's stated contract and the stager's refusal, which is a different and weaker thing, and I say so.
2. **A1.3's and A1.4's driven refusals as the lead drove them** — I verified the code paths and drove A1.2's refusal expression on a fixture; I did not run `clb_stage.sh` or `clb_fire.sh --dry` end to end, which need run-box env.
3. **A1.5's env file** — untracked by design; I confirmed only that the addendum names keys and not values.
4. **`render_fence_v3.py`'s refusal of a scratch config dir** (A1.4's premise) — not driven.
5. **Whether the two uncovered trees will in fact be moved.** That is the helm's ~21:55 window, which this head owns; **this signature asserts the requirement, never its discharge.**

⇒ **A1.1–A1.6 tighten a freeze that fires nothing, their cross-references to #184 are exact, and every code claim I could reach is true at the source.** ⛔ **The two trees move, and the census re-runs green against the release export, BEFORE the first cell.**

---

## ⚖️ ADDENDUM 2 — §Q2 ITEMS 3 AND 4 AS LANDED, THE SONNET SUBAGENT-MODEL RULE (VISIBLE), AND THE RELEASE EXPORT'S BYTES. APPENDED; all text above, signatures included, untouched.
**bench (lead), 2026-09-16.** Every clause narrows a check or declares a difference; none loosens one. It goes to a non-author before it binds.
**Every figure below is read from `evidence/claude-lane-b-addendum2-2026-09-16/`**, the lead's two read-only drives on the run box at 20:2x PDT. None is retyped from a message.

### A2.1 · §Q2 ITEM 3 AS LANDED — THE HEAD IS HELD EXACTLY, NOT TO THE SET (a narrowing, accepted by the lead)
`served_models_v3.py` (systems; helm-signed at the branch tip `43e44b5`, merged to harness master at `33d8016`) reads every assistant line, head and
sidechain, against the CONDITION. A set check alone would pass a Sonnet HEAD under the Opus condition, because the Opus set contains
`claude-sonnet-5`. ⇒ **Registered:**
- the head is held to the condition's head model EXACTLY;
- a sidechain spawned with no `model` is held to the launcher's assignment for its role;
- everything else is held to the condition's set;
- `set_verdict` prints §Q2.3(b)'s literal set reading beside the verdict.

**Control on the real object, re-driven by the lead with the RELEASE EXPORT'S OWN COPY of the tool** (`runbox_drive.out`, `TALLY`): all 45 HC1
cells read `clean` (set `clean`, rc 0) as Opus, and `SUBSTITUTED` (set `SUBSTITUTED`, rc 1) as Sonnet.

### A2.2 · §Q5 ROW 7 — IN A SONNET CELL THE SUBAGENT MODEL IS FORCED, AND THE SUBJECT CAN SEE THAT IT IS
**Why** (`hc1-subject-model-census.out`, `# ARM` and `# TOTAL`):
- In HC1, the head passed an explicit per-call `model` on at least one Agent spawn in **11 of 45** cells, and asked for `opus` in **7**.
- By arm, the `opus` requests were salt-diet **5/15** · plain **2/15** · placebo **0/15**.
- A Sonnet head doing the same would be served Opus. That is VOID(MODEL) under §Q7 row 1, and the void would fall mostly on the treatment arm.
- The builder's independent census, taken over a pulled copy by a different method, reads the same 11, 7 and spawn totals.

**The rule** (harness master `2822925`):
- When the root's `_bin/models.tsv` requests ONE model for every role, `cell-claude.sh`'s launch environment sets `CLAUDE_CODE_SUBAGENT_MODEL=<head>`
  and `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1`.
- The rule is derived from the table, never from the word "sonnet".
- The probe turn gets the same environment (`cell-claude.sh --env`), and the ARGV line names both variables.
- Opus roots get neither variable, so their environment is HC1's.

**The mechanism, measured by the builder at the object on the pinned client (`884baa38fe1a624b`), in two turns:**
- WITH the variables, the spawn carried no `model`, and the worker-opus sidechain was served `claude-sonnet-5` (check-cell: clean).
- CONTROL, WITHOUT them, the same head passed `"model": "opus"` and was served `claude-opus-5` (SUBSTITUTED, "the SUBJECT requested model=opus").

⚠️ **The lead did not reproduce these two turns; the builder holds their receipts.** The reading that binds is T-S (§Q3.3): every sidechain is
served `claude-sonnet-5`, and the ARGV line names both variables.

⛔ **VISIBLE TO THE SUBJECT, AND DECLARED AS SUCH:** under FORCE, the client removes the Agent tool's optional `model` parameter from its schema.
- **Both arms of a Sonnet condition see the identical schema**, so the registered reading (§Q6 rule 7, arm within condition) is untouched.
- An Opus-versus-Sonnet reading is not registered. It carries this difference beside §Q5.1–3.

### A2.3 · §Q2 ITEM 4 AS LANDED — HARDER THAN §Q2.4 ASKED
`cell-claude.sh --launch` (systems; helm-signed at `1e84112`) runs `probe_sandbox_v3.sh --require <cell> --bin <client>`. It HOLDs before any
run-cfg, LAUNCHING or ARGV line. `--require` additionally refuses:
- a receipt whose recorded `fence_sha256` is not this fence's;
- a receipt driven with another client;
- a receipt with NO client field (`f97ddcb`, merged at `3853baf`; the lead's surviving mutant, now killed).

The DRY-stub exemption is by BYTES, never by name. **§Q2.4's "driven on the DRY stub" is read as "driven on `/usr/bin/true`"**, because the stub
is the exemption and cannot also be the test.

### A2.4 · THE RELEASE EXPORT'S BYTES (the release addendum still names the census, the window, the toolchain and the rates re-read; this clause names only what was measured here)
```
  harness master   2822925 = items 1–5 (item 3 at merge 33d8016, item 4 at 1e84112) + the item1↔3 integration (merge b7eb4f1)
                   + the follow-ups (merge 3853baf) + the A2.2 rule (2822925). It descends from cc227b4, and so from eacb9ec (§Q0 row 4 (i)).
  export           on the run box, cut by studio_export.sh (the allowlist exporter), --no-toolchain. Its marker reads 2822925e3f5b….
                   362 files plus the marker · 0 directories named withheld or mutants · exactly 1 path containing either word:
                   harness/systems-v3/check_withheld_leak_v3.py, the leak INSTRUMENT · no refusal file              (runbox_drive.out)
  givens           tasks/systems-v3/<P>/brownfield/solution.rs, blob ids computed from the export's bytes:
                   Crc32 3e31075 (1638 B) · FreeList c330b63 (6636 B) · LRU a911477 (2883 B) · LZW 10db31a (2748 B) · Paxos 9e536ca (10519 B)
                   (runbox_drive.out). They are equal, 5 of 5, to eacb9ec's blobs at those paths (git rev-parse), i.e. §Q0 row 4's repaired givens.
  lane env keys    CLB_CFG · CLB_BIN · CLB_PINSHA · CLB_EXPORT · CLB_PROBE_OUTSIDE (names only; the values are untracked: the infra-name gate)
```
⚠️ **Owed, non-blocking** (from systems' read of the integration):
- `clb_stage.sh`'s `cond_of` is a second copy of the block→model map.
- The ROOTS line types 18 and 46 without comparing their sum to 64.

Both are right today, and both are follow-ups.

---
## ✍️ NON-AUTHOR SIGNATURE — the helm (84th head), 2026-09-16 20:3x PDT, on ADDENDUM 2 (A2.1–A2.4)

**SIGNED AT BLOB `aefee39aa6c4f3fa2e9ea409e06d017856719184`**, head `92bbd490` — **both matched the lead's own ask, character for character, before I read a line.** ADDENDUM 2 read WHOLE.
📌 **SCOPE: A2.1–A2.4. Everything above, including both prior signatures, is untouched and not re-opened.** Releases nothing.

### WHAT I DROVE — each with a control
```
  1 TIP + BLOB      92bbd490 · aefee39aa6… == the ask                                          ✅
  2 APPEND-ONLY     THREE methods, not one: numstat 0 deletions over 7 files · removed-line
                    count 0 against a control that finds the additions · and a STRICT BYTE
                    PREFIX drive — the first 39,900 bytes of the new file are byte-identical
                    to the base, 45,863 total. The lead's own two figures, re-derived.        ✅
  3 MANIFEST        all four rows DERIVED at the tip: 327c903ce84c8a99 · 46b745d028c49d57 ·
                    c3d6f31fe2c5a042 · 70515a72d8c227de, each == BOTH columns, verbatim       ✅
  4 THE ARITHMETIC  re-derived BY ME from the 45 PER-CELL ROWS, never from the `# ARM` and
                    `# TOTAL` lines the addendum quotes: cells 45 · no_transcript 0 ·
                    explicit 11 · opus 7; salt-diet 5 · plain 2 · placebo 0; ASIDE 2.
                    Every figure in A2.2 agrees with my independent tally.                    ✅
  5 MUTATION M-1    the census's wrong-box `REFUSE` removed ⇒ on this box (no HC1 cells) it
                    prints a CLEAN, GREEN `# TOTAL cells=0 … asked_opus=0` at rc 0. The
                    shipped guard REFUSES at rc 1. Both arms driven, on the real defect.      ✅
  6 READ-ONLY       the lead's declaration checked through TWO layers: `runbox_drive.py` has
    (the live-cell   no write, chmod, rename or spawn but the one `check-cell` subprocess;
     declaration)    and `served_models_v3.py`'s `check_cell` (231–394) contains ZERO write
                    calls against a POSITIVE CONTROL of 14 in `selftest` (425–704).           ✅
```

### ⭐ THE CENSUS REFUSES ON THE WRONG BOX, AND THAT IS THE BEST LINE IN THIS PR
`hc1_subject_model_census.py` ends with `if not cells: sys.exit("REFUSE: … this is not the box the cells ran on")`, and its comment states the reason: *"a census of a HOME names no host: on the wrong box it would print an empty, clean-looking table."*
⇒ **I drove exactly that, both ways, on the build box.** Without the guard the instrument reports **zero cells, zero explicit models, zero opus requests, rc 0** — a perfect all-clear that means only *"you ran it on the wrong machine."* ⚠️ **This is not hypothetical: I hit the same class tonight** re-driving #184's exposure census on the build box, where it died only because a fence path was missing. **Had the fence been present and the trees absent, it would have printed a clean, empty, entirely wrong census.** ⇒ 🔑 ***AN INSTRUMENT WHOSE POPULATION IS "`$HOME`" IS RUNNABLE ON A MACHINE THAT CANNOT FALSIFY IT, AND IT FAILS TOWARD "NOTHING HERE".*** **Every `$HOME`-scoped instrument in this campaign should carry this guard**; this one does, and the whole of A2.2 rests on it.

### ⛔ WHAT I DID **NOT** VERIFY
1. **The two run-box drives themselves.** They ran on the run box while `l6vspt01` was live; **I read both scripts and re-derived their outputs' arithmetic, and I did not re-run them.** No non-author on this box can.
2. **A2.2's two measured turns.** The addendum already declares the lead did not reproduce them and that the builder holds the receipts. **I did not open those receipts**, so the FORCE mechanism rests on the builder's word plus the code, exactly as A2.2 says.
3. **A2.4's export readings** — marker, 362 files, the five given blobs, the zero-withheld count. Run-box bytes; taken from `runbox_drive.out` as the lead's readings.
4. **T-S**, which A2.2 names as the reading that actually binds. It has not run.
5. **The two follow-ups the addendum declares owed.** ⚠️ **I flag the second as this campaign's own idiom-law clause 1:** *"the ROOTS line types 18 and 46 without comparing their sum to 64"* is a TYPED EXPECTATION, and a typed expectation is correct-not-verified. It is right today and the addendum says so; **it should be derived before it is relied on.**

⇒ **A2.1–A2.4 narrow four checks, declare their differences, and every figure I could reach re-derives from the tracked bytes rather than from the prose.** The lead pinned its blob and head in the ask, which made this the cheapest signature of the night — **that is the form, and it should be the standard.**

---

## ⚖️ ADDENDUM 3 — ⑤(a): **THE SONNET CELLS FIRE FIRST.** §Q3.2 RE-SEQUENCED · §Q3.1 RE-BASED · §Q3.3 RE-ORDERED WITH ONE TRIPWIRE ADDED · AND ⑯'s TOKEN FORM. APPENDED; all text above, signatures included, untouched.
bench (SaltBench lead), 2026-09-17. Council 09/17 afternoon **⑤(a)** and **⑯**, the Captain's words verbatim in that sitting's minute (the private
record; cited by DATE and by his words, as this freeze cites council 09-16). ⑤(a): *"Ah! What I actually meant was to schedule the Sonnet cells next to
decrease the bench spend rate (vs Opus) -- the caveat remains the same."* ⑯: *"On saltbench, what we really want is the token
cost, borken down if possible. Dollars are secondary."*
⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT**, as §Q0–§Q9, ADDENDUM 1 and ADDENDUM 2 were. ⛔ **Nothing fires before BOTH this
addendum and the release addendum** (the minute's own condition).

### A3.0 · ⛔ THE NUMBER, DECLARED RATHER THAN QUIETLY TAKEN — THE MINUTE'S "ADDENDUM 3" AND A DRAFT ALREADY CARRYING THAT NUMBER
The minute homes ⑤(a) at *"the lane-B freeze ADDENDUM 3 (bench)"*. **A draft on the unmerged release branch already called
itself ADDENDUM 3** (sections R3.1–R3.6, written 2026-09-16, unsigned, never offered). Two claims to one number, neither wrong
when written — the file registry is per-branch and git reports no collision.
⇒ **RESOLVED IN THE DIRECTION THAT KEEPS THE RECORD READABLE: this addendum takes 3, matching the minute; the release draft is
renumbered ADDENDUM 4 (R4.1–R4.6) on its own branch before it is offered.** It is unsigned and unmerged, so the renumber costs
nothing; the alternative left `main` reading 1 · 2 · 4 with a gap, and the minute's own pointer wrong.
⚠️ **AND THE RELEASE DRAFT HAS TWO SENTENCES THIS RULING FALSIFIES, WHICH ARE AMENDED IN THE SAME ACT AND NAMED HERE SO THE
AMENDMENT IS NOT SILENT:** R3.5's heading assumes block O fires first, and R3.6 says of T-S *"It fires after block O and block
OS, in §Q3.2's order."* **Both are corrected on that branch.** Nothing above this line is touched.

### A3.1 · §Q3.2 — THE ORDER, RE-SEQUENCED
```
  blocks      SG → SB → SS → SBS → SC → O → OS
              (all five SONNET blocks, then the two OPUS blocks — ⑤(a).
               SC stays LAST AMONG THE SONNET BLOCKS on §Q3.2's own reason, which is intra-Sonnet and
               survives the move: phase 2, C2 is §9's half-rule on a number never observed, and the Opus
               spec-change row already carries CAP-COST censoring. That reason never depended on O or OS.)
  problems    LRU → Paxos → FreeList → LZW → Crc32     UNCHANGED (statement blocks omit Paxos)
  cells       per problem: plain#1 · salt-diet#1 · plain#2 · salt-diet#2 · plain#3 · salt-diet#3   UNCHANGED
```
**One cell at a time** and the per-pair stopping argument are UNCHANGED: a halt after any cell still leaves every earlier PAIR
whole, because the re-order moves whole blocks and never splits a pair.
📌 **Counts, derived from §Q1 and not typed: 138 Sonnet cells (30+30+24+24+30) then 54 Opus (30+24) = 192.**

### A3.2 · §Q3.1 — RE-BASED, AND WHAT THE RE-ORDER BREAKS (MEASURED AT THE CENSUS, NOT REASONED)
§Q3.1 rows 3..7 read *"BORROWED FROM OPUS … block O/OS once scored."* ⛔ **Under ⑤(a) two of those five borrow from blocks that
have not fired.** Measured at `CENSUS-full-matrix-2026-09-14.md` §C4 (Opus: **DONE 28 · INEXPRESSIBLE 2 · BLOCKED 30**, the 28
being greenfield only):
```
  block  its Opus counterpart                      status          verdict
  SG     greenfield × bare × 5                     DONE  9ffa1a8   ✅ prior INTACT
  SS     greenfield × statement × 4                DONE  173ee84   ✅ prior INTACT
  SC     greenfield × spec-change × 5              DONE  20836ad   ✅ prior INTACT
  SB     brownfield × bare   = BLOCK O             NOT FIRED       ⛔ PRIOR BROKEN BY THE RE-ORDER
  SBS    brownfield × statement = BLOCK OS         NOT FIRED       ⛔ PRIOR BROKEN BY THE RE-ORDER
```
⇒ 🔑 ***THREE OF FIVE SONNET BLOCKS KEEP THEIR PRIOR BECAUSE OPUS'S GREENFIELD IS ALREADY DONE; THE TWO BROWNFIELD BLOCKS LOSE
THEIRS, AND A MECHANICAL RE-ORDER WOULD HAVE CARRIED THE WORD "BORROWED" OVER A PRIOR THAT NO LONGER EXISTS.***
✅ **REMEDY — the freeze's own form, not a new one:** SB and SBS take the **OTHER LANE** prior, exactly as §Q3.1 row 1 gives it to
block O, carrying its caveats unchanged (agy Pro level 4: LRU and Paxos STAND; **FreeList and LZW are VOID for the
find-the-defect claim (§V3) and ORDER only**). The re-based table:
```
  order  block  expectation             prior
  1      SG     BORROWED FROM OPUS      Opus greenfield × bare × 5, DONE (§C4; RESULT-matrix-opus-1 9ffa1a8)
  2      SB     VARIES (retention)      OTHER LANE — §Q3.1 row 1's prior verbatim, caveats included.
                                        ⛔ No Claude brownfield cell has a result of record; that sentence
                                           of row 1 is now true of SB, which fires first.
  3      SS     BORROWED FROM OPUS      Opus greenfield × statement × 4, DONE (RESULT-statement-arm 173ee84)
  4      SBS    BORROWED, TWO SIDES     brownfield from row 2 (other lane) · statement from row 3. ⛔ No
                                        brownfield × statement cell has a result of record on ANY lane.
  5      SC     BORROWED FROM OPUS      Opus greenfield × spec-change × 5, DONE (RESULT-p1-specchange 20836ad)
  6      O      VARIES (retention)      OTHER LANE, unchanged — AND NOW ALSO the SB rows, freshly scored
  7      OS     VARIES — BORROWED       from row 6, unchanged — AND NOW ALSO the SBS rows, freshly scored
```
⛔ **Crc32 is unchanged in every respect**: a LOUD, CEILING rung, registered AT CEILING, fires LAST inside its block, never
pooled with the other four. ⛔ **A CEILING IS NOT PARITY.** ⛔ **LANDED IS NOT VERIFIED** (§Q6 rule 1).

### A3.3 · ⛔⛔ THE DIRECTION OF BORROWING REVERSES FOR O AND OS, AND THE PROTECTING CLAUSE MUST REVERSE WITH IT
§Q3.1 ends: *"A different Sonnet shape is a result about Sonnet, never a failed prediction."* **That clause exists because the
borrowing ran Opus → Sonnet.** Under ⑤(a) rows 6 and 7 gain a same-condition prior that is a **Sonnet** row.
⇒ ***REGISTERED, BEFORE EITHER BLOCK FIRES: where an Opus row's cited prior is a Sonnet row of the same condition, A DIFFERENT
OPUS SHAPE IS A RESULT ABOUT OPUS, NEVER A FAILED PREDICTION.*** The asymmetry is a property of the ORDER, not of the models.
⇒ 🔑 ***A RE-ORDER THAT LEAVES THE PROTECTING CLAUSE POINTING THE OLD WAY HANDS THE LAST BLOCKS A PREDICTION THEY NEVER HAD***
— and it would arrive as *"Opus failed to reproduce Sonnet"*, which is not a claim this freeze is entitled to make.
📌 It is written here rather than left to §Q6 because it costs one sentence now and is unrecoverable after block O is read.

### A3.4 · §Q3.3 — THE TRIPWIRE ORDER, AND THE ONE THE RE-ORDER MAKES NECESSARY
```
  1  T-S    SG · LRU · plain · greenfield bare       THE CAMPAIGN'S FIRST CLAUDE-LANE (B) CELL. Plumbing, not arms.
  2  T-SB   SB · LRU · salt-diet · brownfield bare   ⭐ NEW — see below
  3  T-SC   the first SC cell, read after its phase 2 ends
  4  T-O    O · LRU · salt-diet · brownfield bare    unchanged in content; no longer first
  5  T-OS   OS · FreeList · salt-diet · brownfield statement    unchanged in content
```
⛔⛔ **WHY T-SB EXISTS, AND IT IS A HOLE THE RE-ORDER OPENS RATHER THAN AN ADDITION I WANTED:** under the frozen order **T-O was
the lane's first brownfield cell**, and its reading list is where the brownfield-specific rows live — *the given at the first
commit byte-identical to the export's*, and (release addendum) *`w1_fenced` read on a brownfield COPY, which no ended Claude
brownfield cell has ever produced*. **⑤(a) moves the first brownfield fire into block SB, which had no tripwire at all.**
⇒ 🔑 ***A RE-ORDER DOES NOT MOVE A TRIPWIRE — IT MOVES WHAT THE TRIPWIRE WAS THE FIRST OF***, and the coverage that was
incidental to being first is the coverage that is silently lost.
✅ **T-SB's reading list is the UNION of T-O's and T-S's**, because it is both the lane's first brownfield cell and a Sonnet
cell: the brownfield rows of the release addendum's T-O list, **plus** T-S's forced-subagent-model and served-set rows.
**Any row that does not read HOLDS block SB.** The tripwire cell counts as cell 1 of its condition unless §Q7 voids it — unchanged.
📌 **T-O is not weakened by moving:** its list is unchanged and it is still read before block O continues. What it loses is only
its accidental role as the lane's first brownfield fire, which T-SB now holds.

### A3.5 · ⑯ — TOKENS ARE THE PRICE OF RECORD. WHAT THE INSTRUMENT ALREADY EMITS, WHAT IT CANNOT, AND THE ONE CLAUSE THAT BINDS THE HAND
**Driven read-only on the run box this afternoon; nothing was written to any cell, slug or config dir. Instrument:
`cell_meter.py` from the release export, sha256/16 `faf81afbbd7062c0`. Evidence:
`evidence/claude-lane-b-addendum3-2026-09-17/` — the capture, its driver, and `derive_table.py`, which produces every figure
below from the capture's bytes. No figure here is typed (idiom law clause 1).**

**(a) BY DIRECTION AND BY ROLE-CLASS: ALREADY NATIVE, PER CELL.** `cell_meter.py` prints, for every (bucket × served model):
`records · input · cache_creation (5m/1h) · cache_read · output · T · share_T · COST · share_COST`, and labels the dollar
*"modelled at list rates (rates.tsv), not an invoice."* ⇒ **⑯'s form is the instrument's own output; what ⑯ changes is which
half LEADS the record.** Tokens lead; USD derives. The campaign's published prices to date lead with USD and are re-based.

**(b) BY PHASE: FREE, AND ALREADY WRITTEN BY THE CELL.** `cell_meter.py`'s contract is one session per phase, and the cell's own
`ctl/run-cfg.tsv` carries `cfg` · `run_at` · **`phase`** per launch.

**(c) BY THE FOUR ROLES ⑯ NAMES: A DECLARED ABSENCE, WITH ITS CAUSE AND ITS PRICE.** The buckets are `head · exec · wf` —
*mechanism* classes. **`T_exec` is keyed by SERVED MODEL, not by executor**, so two subagents of the same model are summed and
their identities discarded — although the per-agent files (`subagents/agent-*.jsonl`) exist on disk. ⇒ **head vs worker is
available; designer vs reviewer is NOT, and that is ⑯'s declared absence, stated rather than approximated.** The remedy is to key
the `exec` bucket by the agent file as well as the model; it is a harness change to a FROZEN export, so it is **named and PARKED
to the pilot's completion per ⑱** — it is not taken here.

**(d) PER LANE:** the sum over the per-cell captures. **No new instrument, and no lane figure is ever computed from a dollar.**

**(e) ⛔⛔ THE CLAUSE THAT ACTUALLY BINDS THE HAND, AND IT COSTS NO HARNESS BYTE.** `clb_harvest.py` derives a cell's session slug
from **`CLB_CFG`** — the lane env, a MUTABLE key, which has already moved. Driven on three landed cells, both arms each:
```
  ARM A   the slug as clb_harvest.py derives it    VOID(UNMETERED) — "no session dir for this
                                                    cell. Unmetered is not zero."        3 of 3
  ARM B   the slug THE CELL ITSELF records         a full receipt, T 6.6M – 9.3M         3 of 3
```
⇒ 🔑 ***THE TOOL IS CORRECT AND ITS ANSWER IS FALSE: "no session dir for this cell" is true of the path it derived and false of
the cell — and the honest rider "Unmetered is not zero" is the sentence that makes a reader accept it. THE MOST DANGEROUS VOID
IS THE ONE THAT DECLARES ITS OWN INTEGRITY.***
✅ **REGISTERED, AND IT IS A PROCEDURE, NOT A CODE CHANGE** (the export is frozen and named by the release addendum; a code change
re-opens §Q0 row 4):
1. **A cell is metered from the `cfg` its OWN `ctl/run-cfg.tsv` records**, never from the ambient `CLB_CFG`. Where a cell records
   more than one distinct `cfg`, every one is read and the fact is declared.
2. **At harvest, `cell_meter.py`'s FULL stdout is captured into the cell's evidence**, because the token record lives OUTSIDE the
   cell, under a path derived from a key that moves. ⚠️ ***A PRICE OF RECORD THAT IS RE-DERIVED FROM A MOVING KEY IS NOT A RECORD.***
3. **A VOID is quoted verbatim with its reason and stays a declared absence** — never a zero, never a dollar divided back into tokens.
⚠️ **THE `VOID(UNDERSTATED)` CASE IS NOT AN ERROR AND MUST NOT BE SMOOTHED:** an interrupted turn makes a cell's T a LOWER BOUND,
so a median over n=3 containing one becomes a **BAND**. The instrument volunteers this; the reading must carry it.

### A3.6 · ⭐⭐ ⑤'s CAVEAT IS ANSWERED AT **T-S**, AGAINST A RECORD THAT ALREADY EXISTS — SO SONNET-FIRST DELAYS NOTHING
The caveat is the Captain's: **equal token volume between the models is UNMEASURED**, and the per-cell point prices (0.18 vs
0.45) are a *rate* applied to a count nobody has compared. The minute says the first Sonnet block's tripwire is the measurement.
⛔ **It cannot be settled against T-O**, which differs from T-S in **both** arm and field (`O · LRU · salt-diet · brownfield` vs
`SG · LRU · plain · greenfield`); two cells differing in two factors do not price a model.
✅ **It is settled against HC stage 1's `hc1lp01/02/03` — `LRU · plain · greenfield · bare`, T-S's condition EXACTLY, one model
up, n=3, all LANDED.** Metered this afternoon:
```
  cell      T             T_head              head's own split: cache_read · output · input · cache_creation
  hc1lp01   9,322,934     6,504,380 (70%)     97.20% · 1.05% · 0.0025% · 1.74%
  hc1lp02   8,143,625     6,599,181 (81%)     96.74% · 1.26% · 0.0021% · 1.99%
  hc1lp03   6,651,048 ⛔  5,574,212 (84%)     96.86% · 1.14% · 0.0025% · 1.99%   ⛔ LOWER BOUND
  ⇒ the registered median (§Q6) is a BAND: [8,143,625 , 9,322,934]
```
⇒ **When T-S lands, the caveat is answered the same hour and does not wait for block O.** The Opus half is a PRIOR record, so
this addendum registers the comparison **before the Sonnet half exists**, which is the only order in which it proves anything.
⛔ **WHAT THIS DOES NOT LICENSE:** the two are separated by MODEL and by DATE, not by model alone — different weeks, different
client build, HC1's own registered confounds. **It is a token-volume reading with its confounds declared, never an arm result.**

### A3.7 · WHAT THIS ADDENDUM DOES NOT DO — SAID BEFORE ANY CELL FIRES
1. **It does not change any arm, any cap, any scoring rule, any confound, or §Q7's void list.** It moves an ORDER and re-bases the
   expectations that order invalidates.
2. **It does not settle whether a Sonnet cell costs fewer tokens.** It registers the comparison and names the cells; A3.6's Opus
   half is an existing record and the Sonnet half does not exist yet.
3. **It does not repair `clb_harvest.py`.** The defect is measured, its remedy is a procedure, and the code change is parked to ⑱.
4. **It does not re-price the campaign in tokens.** ⑯'s re-basing of published USD figures is owed and is not this document.

---
## ✍️ NON-AUTHOR SIGNATURE — the helm (89th head), 2026-09-17 14:2x PDT, on ADDENDUM 3 (A3.0–A3.7)

**SIGNED AT BLOB `f7575ae0f9f169e617555a38cbc5cbf1829d7f30`**, resolved at `33503a6025a60e11689924f523a7622a5a679873:harness/systems-v3/AMENDMENT-claude-lane-B-2026-09-16.md` — **the blob and the head the lead pinned in its own ask, matched at the forge in one command.** Read WHOLE.
📌 **SCOPE: A3.0–A3.7 only.** §Q0–§Q9 and the 83rd and 84th heads' signatures are untouched and are not re-opened. **This addendum RELEASES NOTHING** — nothing fires before it AND the release addendum, which is the minute's own condition.

### WHAT I DROVE AT THE OBJECT — each with a control
```
  1 BLOB + HEAD     f7575ae0f9… == the lead's pinned blob · head 33503a60… == the lead's ask       ✅
  2 APPEND-ONLY     TWO methods: `cmp` of the first 50,618 bytes against origin/main (IDENTICAL),
                    and numstat 167/0. Both prior signatures present and unchanged (2 hits each,
                    base and head).                                                                 ✅
  3 THE LOAD-BEARING CLAIM — A3.2's broken priors, re-derived at the CENSUS, not read off the table:
                      SG  greenfield × none        DONE  9ffa1a8     prior INTACT                   ✅
                      SS  greenfield × statement   DONE  173ee84     prior INTACT                   ✅
                      SC  greenfield × spec-change DONE  20836ad     prior INTACT                   ✅
                      SB  brownfield = block O     BLOCKED, not fired  PRIOR BROKEN                 ✅
                      SBS brownfield = block OS    BLOCKED, not fired  PRIOR BROKEN                 ✅
                    and the totals DONE 28 · INEXPR 2 · BLOCKED 30, with 10+8+10 = 28 proving
                    the 28 IS greenfield-only — which is the whole of why three priors survive.     ✅
  4 THE MAPPING     block → (field, extras) taken from §Q1's OWN table, so "SB's counterpart IS
                    block O" is derived rather than asserted: SB = Sonnet brownfield none,
                    O = Opus brownfield none.                                                       ✅
  5 THE COUNTS      DERIVED from §Q1's table: SG 30 · SB 30 · SS 24 · SBS 24 · SC 30 = 138 Sonnet;
                    O 30 · OS 24 = 54 Opus; 64 conditions / 192 cells.                              ✅
  6 MUTATION CONTROL  a wrong sha planted into a census COPY → arm 3 FAILS. The arm can fail.       ✅
```

### ⚖️ WHY I AGREE THAT THIS NEEDED A NON-AUTHOR AND NOT A `sed`
**A3.2 is correct and it is the reason the re-order is not mechanical.** Three Sonnet blocks keep their prior *because Opus's greenfield is already DONE*, and the two brownfield blocks lose theirs *because their counterparts are the very blocks ⑤(a) moved to the end*. A mechanical re-order carries the word **"BORROWED"** over a prior that no longer exists, and it reads exactly like a clean rename.
⭐ **A3.3 is the clause I would have been most likely to miss, and it is unrecoverable after block O is read:** the protecting clause *"a different Sonnet shape is a result about Sonnet, never a failed prediction"* exists **because the borrowing ran Opus → Sonnet.** Under ⑤(a) rows 6 and 7 gain a *Sonnet* prior, so the clause must reverse or the last two blocks inherit a prediction they never had — arriving as *"Opus failed to reproduce Sonnet"*, which this freeze is not entitled to claim. **Registering it before either block fires is the only order in which it costs one sentence.**
⭐ **A3.4's T-SB is a hole the re-order OPENS, not an addition the lead wanted:** T-O's coverage of the brownfield-specific rows was *incidental to being first*, and ⑤(a) moves the first brownfield fire into a block that had no tripwire at all. ***A re-order does not move a tripwire — it moves what the tripwire was the first of.***

### ⛔ WHAT I DID **NOT** VERIFY — named so this signature is not read wider than it is
1. **A3.5's token figures and the `clb_harvest.py` two-arm drive.** I did not re-run `cell_meter.py`, re-derive any T, or reach the run box. The evidence directory and `derive_table.py` are cited and I accepted them as the lead's own receipts.
2. **A3.6's `hc1lp01/02/03` numbers**, including the `VOID(UNDERSTATED)` lower bound that makes the median a BAND. Read, not driven.
3. **The release draft's renumber to ADDENDUM 4** and the two sentences A3.0 says are amended on that branch — a different branch, not offered here.
4. **Whether the census itself is right.** Arm 3 checks this addendum against `CENSUS-full-matrix-2026-09-14.md`; if the census is wrong, my arm inherits that and does not catch it. *(The 83rd head declared the same limit about §Q1 against the census, in the other direction.)*
5. **The five §Q2 build items and the export's bytes** — covered by ADDENDA 1 and 2, not re-opened.

### ⚠️ TWO THINGS I OWE THE LEAD, BOTH SMALL AND NEITHER BLOCKING
- **The ask's append figure is off by 50 bytes:** it states **15,190 B** and the append measures **15,240 B**. Append-only is proven independently by `cmp` and by numstat 0-deletions, so nothing rests on it — **but it is a number in a pinned ask, and a pinned ask's numbers are the thing a signer is supposed to check.**
- **bench's correction to the helm is accepted and it is mine, not the lead's:** the minute's ⑤ chain and the helm's gate line to bench both name **T-O** as the tripwire read before the block continues. Under ⑤(a) **the campaign's first cell is T-S (`SG · LRU · plain · greenfield bare`)**, and T-O is no longer first. **The minute and the gate are corrected by the helm in the same act as this signature.**

**⇒ SIGNED.** A3.0–A3.7 are internally exact, their load-bearing claim is true at the census by an independent derivation with a control that fails, and their scope is honestly bounded by their author. Nothing fires before the release addendum names the export sha and carries the `rates.tsv` re-read.

## ⚖️ ADDENDUM 4 — THE RELEASE: THE EXPORT IS NAMED, THE CENSUS IS RE-RUN, THE RATES ARE RE-READ, AND T-O's READING LIST. APPENDED; all text above, signatures included, untouched.
**bench (lead), 2026-09-16, completed and renumbered 2026-09-17.** This is the addendum §Q0 row 4 and A1.1 require before the first cell.
**It fires nothing by itself:** the lane's first cell fires only after a non-author signs it. Every figure is read from
`evidence/claude-lane-b-release-2026-09-16/`.
⛔ **TWO POINTERS RESOLVED HERE, BECAUSE ADDENDUM 3 IS SIGNED AND IS NEVER EDITED:**
1. **§A3.0 names this addendum's sections by their PRE-RENUMBER labels, `R3.5` and `R3.6`. They are `R4.5` and `R4.6` below.** A3.0 was
   describing the draft as it then stood, which was correct when written; the labels moved in the same act that renumbered the addendum.
2. ⛔ **THE FIRST CELL IS `T-S` (`SG · LRU · plain · greenfield bare`, id `clbglp01`), NOT `T-O` (`clbols01`)** — ADDENDUM 3 §A3.4. Every
   "first cell" in the sections below means T-S. **The ids are derived from the harness's own maps** (`clb_harvest.py`'s `BLOCKS`/`PROBS`/`ARMS`),
   never typed: `SG LRU plain 1` → root `cells-clb-sg-lru-plain`, id `clbglp01`; `SB LRU salt-diet 1` → `cells-clb-sb-lru-saltdiet`, id `clbbls01`.

### R4.1 · §Q0 ROW 4 — THE EXPORT IS `bcd2205`
- **Why not `2822925`, which ADDENDUM 2 A2.4 measured:** `bcd2205` is `2822925` plus ONE file, `clb_stage.sh` (ruled (A) by the helm and read by
  it, AGREES). The stager now reads ONE block table, and `--roots` REFUSES before creating anything unless the enumeration equals §Q1's
  64 = 18 + 46. Before that, the ROOTS line typed the split and never compared its count. Under §Q0 row 4 (one sha for all 192 cells), release
  was the last moment this fix cost an addendum rather than a split lane.
- **A2.4's run-box drive is RE-RUN against this export, not inherited** (`runbox-drive-bcd2205.out`): the marker reads `bcd2205682c7…` ·
  362 files plus the marker · 0 withheld/mutants directories · 1 path carrying the word (the leak instrument) · givens 5/5 as in A2.4 · the
  export's own `served_models_v3.py` reads 45 of 45 HC1 cells clean as Opus and SUBSTITUTED as Sonnet. Beside the 2822925 export on the run
  box, a content digest of every file differs in exactly one: `clb_stage.sh`.
- **(i) Lineage:** it descends from `cc227b4`, and so from `eacb9ec` (`git merge-base --is-ancestor`, both yes). The five brownfield givens in
  the export's bytes equal `eacb9ec`'s blobs, 5 of 5.
- **(ii) §Q2's build items:** items 1, 2 and 5 at merge `e9124f3` · item 3 at merge `33d8016` · item 4 at `1e84112` · the item 1↔3 integration
  at merge `b7eb4f1` · the follow-ups at merge `3853baf` · A2.2's rule at `2822925` · the one-table stager at `bcd2205`. Each is an ancestor of
  `bcd2205`.
- **The delta from `9f650a3`** (HC stage 1's export) is `harness-delta-9f650a3-bcd2205.tsv`: 65 commits and 54 paths
  (harness/systems-v3 23 A · 21 M; tasks/systems-v3 7 A · 3 M). `rates.tsv`, `cost_caps.tsv` and `models.tsv` are blob-identical at both ends.
- **One sha for all 192 cells,** recorded per cell by the stager.

### R4.2 · A1.1 ITEM 2 — THE WITHHELD CENSUS, RE-RUN AT RELEASE — ✅ **TAKEN 2026-09-17 15:41Z, ALL SIX TREES `COVERED · COVERED`, rc 0**
- **The instrument** is `withheld_exposure_census.py`, a COPY of #184's instrument. It differs ONLY by a guard that REFUSES when `~` holds no
  `cells-*` root, and by a printed host-role line (`census-guard.diff`). Driven on the build box: `REFUSE`, rc 1. #184's original is untouched,
  because it backs a published MANIFEST digest.
- **The fences:** the Claude fence of **the lane's FIRST STAGED cell**, staged from the `bcd2205` export, and a current agy fence.
  ⛔ **AMENDED BY ADDENDUM 3 (⑤(a)): this line read *"the Claude fence of T-O's cell"*** and was true when written. Under ⑤(a) the first
  staged cell is **T-S's, `clbglp01`** (root `cells-clb-sg-lru-plain`), so that is the fence the census covers. ⚠️ **It is written as a ROLE
  ("the first staged cell") and not as a second hard-coded id**, because the first cell is exactly the thing this campaign has now moved twice.
  📌 The step that renders it is generic in its arguments despite its name: `fence-only-TO.sh` takes `<block> <Problem> <arm> <n>` and derives
  the root and id from them (its line 27), so **only the ARGUMENTS change — `SG LRU plain 1`.** *(The name says T-O; the instrument is not
  its label, and a reader who trusts the name will think it is being run on the wrong cell.)*
- ✅ **TAKEN.** The tracked reading is `evidence/claude-lane-b-release-2026-09-16/census-at-window.out`, run by the helm at the
  close of its 2026-09-17 window on the fence `clbglp01` staged for this purpose (step 3½), rc 0:
```
  # host role: the run box (cells-* roots under ~: 190)
  # fences: claude ~/cells-clb-sg-lru-plain/clbglp01/ctl/fence.json (denyRead 223)
  #         agy    ~/cells-l6v-lzw-flash-salt-bare/l6vgfs03/ctl/srt-settings.json (denyRead 190)
  # withheld-shaped entries: 194 in 6 top-level trees (a FLOOR: depth 7, no tarballs, name-based)
  tree                    entries  claude   agy
  ~/projects                   58  COVERED  COVERED
  ~/bench-v2                   34  COVERED  COVERED
  ~/bench-v2-smoke             34  COVERED  COVERED
  ~/bench-dry                  32  COVERED  COVERED
  ~/bench-v2-amend6            18  COVERED  COVERED
  ~/bench-v2-census-a6         18  COVERED  COVERED
```
  **Every tree reads COVERED on both fences. The condition is met and this addendum may be offered for signature.**
- ⚠️ **A1.1 ITEM 3's LIMIT RIDES WITH THE VERDICT, NOT BEHIND IT:** the 194 is a **FLOOR**, not a ceiling — depth 7, no tarballs,
  name-based. ⇒ **It is not a proof that no withheld material exists anywhere; it is a proof that everything this method can see is
  denied to BOTH lanes.** A census reporting a ceiling would be claiming more than it measured.
- 📌 **The fence it covers is `clbglp01`'s, which is the FIRST STAGED cell as this section requires — and under ⑤(a) that is T-S, not
  T-O.** The runbook's own hand-off line still said `O LRU salt-diet 1`; it was not followed. **The role was satisfied, not the label.**

### R4.3 · RATES — RE-READ, TWO SIDES, BY SCRIPT — ✅ **TAKEN 2026-09-17, `VERDICT ALL-EQUAL`, rc 0**
`rates_reread.py` compares the prompt-caching page that `rates.tsv` cites, row by row and figure by figure, for the three served models.
**The tracked reading is `evidence/claude-lane-b-release-2026-09-16/rates-reread.out`:**
```
  page 157,459 B  sha256/16 0bde1d1be67c46c4      (the URL is rates.tsv's own SOURCE line; fetched HTTP 200)
  claude-opus-5     EQUAL   page 5 · 6.25 · 10 · 0.5 · 25       rates 5 · 6.25 · 10 · 0.5 · 25
  claude-sonnet-5   EQUAL   page 2 · 2.5 · 4 · 0.2 · 10         rates 2 · 2.5 · 4 · 0.2 · 10
  claude-fable-5-1  EQUAL   page 10 · 12.5 · 20 · 0.25 · 50     rates 10 · 12.5 · 20 · 0.25 · 50
  VERDICT ALL-EQUAL
```
⭐ **THREE RED ARMS WERE DRIVEN ON THIS PAGE READ, not inherited from the pre-window drive** (`rates-reread-red-arms.out`) — a check is
validated by its ability to FAIL, and a control taken against different bytes is a different control:
```
  a one-figure mutant on the RATES side    rc 1   DIFFERS, and it names claude-sonnet-5
  a one-figure mutant on the PAGE side     rc 1   DIFFERS, and it names claude-opus-5 — the page sha CHANGES with it,
                                                  which is how the instrument shows it read the bytes it names
  a MISSING row on the rates side          rc 1   MISSING (page row found · rates row absent), never "equal"
```
⛔ **THE ROWS STAND UN-REDATED, AND THAT IS A CONSEQUENCE OF THE FREEZE, NOT A PREFERENCE:** `rates.tsv` is a blob **inside the named
export** (`8756904f2d1117114c7767133f083ae2b8fd642d`, identical at the export sha, at harness master and on disk), so re-dating `read_on`
would change the export and re-open §Q0 row 4. **The verification is recorded HERE instead.**
⚠️ **AND THE READER OF A PRICE DOES NOT SEE THIS PAGE:** `cell_meter.py` prints `rates rates.tsv read_on 2026-09-05` in EVERY run, so a cell
receipt carries the date the rows were WRITTEN and not the date they were last VERIFIED. **This section is that surface** — a limit must ride
where its verdicts ride, and this one cannot, so it is named at both ends.

### R4.4 · A1.5 — THE LANE ENV FILE'S KEYS
`CLB_CFG` · `CLB_BIN` · `CLB_PINSHA` · `CLB_EXPORT` · `CLB_PROBE_OUTSIDE`. `CLB_PINSHA` asserts `884baa38fe1a624b` (§Q0 row 5), and the client
at `CLB_BIN` reads the same. `CLB_EXPORT` names the `bcd2205` export, and its marker, read through the env file, is `bcd2205682c7`. The values that identify an account or a host are untracked.

### R4.5 · T-O — WHAT THE LEAD READS BEFORE BLOCK O CONTINUES (§Q3.3 + A1.4, in one list)
⛔ **AMENDED BY ADDENDUM 3 (⑤(a)): T-O IS NO LONGER THE FIRST CELL OF THE LANE.** This section was written when block O fired first and its
original heading said *"WHAT FIRES"*. **The list below is unchanged and still binds T-O**; what moved is only its position — the lane's first
cell is now **T-S**, and its first BROWNFIELD cell is **T-SB**, whose reading list is the UNION of this list and R4.6's.
**T-O** is `clb_fire.sh O LRU salt-diet 1`: one sandbox probe turn, then the cell, registered as an executor (`shape=process`). The lead reads
its fire log WHOLE, then:
```
  staging      ctl/field · ctl/card_extras · the given at the first commit byte-identical to the export's · the export sha in the cell record
  fire path    SETTINGS … read back · TRUST SEEDED · FENCE CONVERGES (sha16 …) · CHECK CLEAN · P-SANDBOX GREEN for fence … ·
               the receipt under <root>/_audit/sandbox-probe/ for that sha · the pin sha in the launch record
  in the cell  W1 COVERED · the end marker verbatim · run_state terminal (item 2) · the served set, clean (item 3)
  after        the scorer's first line naming the export sha (item 5, off the box, A1.2) · the concurrency column
```
**All read ⇒ block O continues, on one bus line.** Any row that does not read HOLDS the block.

**WHERE AND HOW T-O IS SCORED (A1.2 made concrete, and driven across boxes on a harvested copy, `score-xbox-drive.out`):**
- **Harvest:** copy the ended cell off the run box, excluding `repo/target/` (read-only at the source).
- **Tree:** on the build box, where the withheld suite lives, `git archive bcd2205 harness/systems-v3 tasks/systems-v3`. ⛔ **Then write
  `EXPORTED-FROM.sha` = `bcd2205` into that tree.** Without the marker the scorer's first line reads *"not a git tree, no
  EXPORTED-FROM.sha"*, and §Q3.3's row *"the scorer's first line naming the export sha"* cannot read (driven: RUN 1 against RUN 2).
- **Score:** `score_claude_v3.py --tasks <tree>/tasks/systems-v3 --declared <file>`.
- **The drive:**
  - An HC stage 1 cell copy scored end to end.
  - A never-ended brownfield probe cell was REFUSED as UNDETERMINED, which is the right refusal.
  - ⚠️ **It is a plumbing drive, not a result.** It scores ONE HC1 cell and states no HC1 rate.
  - **The `w1_fenced` column has not yet been read on a brownfield COPY** (no ended Claude brownfield cell existed).
    ⛔ **AMENDED BY ADDENDUM 3 (⑤(a)): its first reading is `T-SB`, not `T-O`.** This line said *"T-O is its first reading"* — true only while
    block O fired first. ⑤(a) moves the lane's first BROWNFIELD cell into block SB, so **`w1_fenced` must read COVERED on T-SB's harvested copy**,
    and it joins **T-SB's** list (ADDENDUM 3 §A3.4, where T-SB's list is the union of this one and R4.6's). **It stays on T-O's list too** — a
    column read once is not a column proved on every block.
    ⇒ 🔑 ***THIS IS THE THIRD SENTENCE ⑤(a) FALSIFIED, AND THE ONLY ONE NOT IN A SECTION ABOUT THE ORDER.*** The first two were found by reading
    R4.5 and R4.6, which are *about* tripwires; this one is inside a SCORING paragraph and names T-O only in passing. **Defects cluster in the
    incidental**, and a spot-check of the sections a ruling is "about" will not find them — only a census of every mention will.

### R4.6 · T-S — THE READING LIST'S ADDITIONS (§Q3.3 T-S, plus A2.2), SO BLOCK SG DOES NOT OPEN ON §Q3.3's LIST ALONE
**T-S** is `clb_fire.sh SG LRU plain 1`, the campaign's first Sonnet-headed cell.
⛔ **AMENDED BY ADDENDUM 3 (⑤(a)).** This sentence read *"It fires after block O and block OS, in §Q3.2's order"* — **true when written and
false since the 09-17 council.** **T-S now fires FIRST of the entire lane**, so §Q3.4 item 2 (the cells' config-dir IDENTITY, from the
credential tool and never from the directory's name) is read at T-S, not at T-O. ⭐ **And its token reading answers ⑤'s caveat the same hour**,
against `hc1lp01/02/03` — T-S's exact condition one model up, n=3, already landed (ADDENDUM 3 §A3.6).
Besides §Q3.3's rows, the lead reads:
```
  launch     the ARGV line's "env names:" carries BOTH CLAUDE_CODE_SUBAGENT_MODEL and CLAUDE_CODE_SUBAGENT_MODEL_FORCE
             (cell-claude.sh prints the env NAMES on every launch); an Opus root's ARGV line carries NEITHER (T-O is the control)
  probe      the sandbox probe turn ran with the same two names (cell-claude.sh --env)
  served     served_models_v3.py check-cell --condition sonnet: clean, EVERY assistant record head and sidechain claude-sonnet-5,
             no COST-BLIND; any Agent spawn input carrying a `model` key is itself a finding (FORCE removes the parameter)
```
**Any row that does not read HOLDS block SG,** and A2.2's rule is then unverified at the object. It is posted, never assumed.
