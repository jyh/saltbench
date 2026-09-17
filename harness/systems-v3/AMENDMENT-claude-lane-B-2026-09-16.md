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
