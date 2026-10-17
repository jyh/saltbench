# AMENDMENT — desk OD: THE EFFORT MATRIX. Fable/xhigh · Fable/high · Opus/xhigh, greenfield bare plain, CLAUDE LANE. FROZEN BEFORE THE FIRST CALL
## bench (SaltBench lead), 2026-10-16. The Captain, council 2026-09-15: *"what is the relative cost/ability between Fable/xhigh to Fable/high
## to Opus/xhigh? I chose xhigh as the default because of a message several months ago that xhigh had the same price as high -- but surely
## that can't be."* Then: *"yes, charter it."* Council 2026-09-17 ㉓: *"helm's rec, charter stands"* (the one-line `--effort` build and an
## honest v3 baseline). bench is lead AND hand on this lane, as in lane B and block N.
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ **NO CELL FIRES BEFORE §D2's ITEMS ARE DRIVEN AND A RELEASE ADDENDUM NAMES THE EXPORT SHA.**
## Signature and release are two acts, as in lane B.

**What this file carries by citation.** It is a block under `AMENDMENT-claude-lane-B-2026-09-16.md`, narrowed exactly as block N
(`AMENDMENT-O37-nine-greenfield-claude-2026-09-25.md`) narrowed it for greenfield × `none`: lane B's preflight (§Q3.4, with its ADDENDUM 5's
one-live-cell-per-pool rule and §CLB-A's required ancestors), caps (§Q4), confounds (§Q5), reading rules (§Q6 rules 1, 2, 3, 6–9), voids
(§Q7 less rows 6–7) and deliverables (§Q9). Its outcomes are `DESIGN-correctness-primary-2026-10-02.md` §D3 (the design of record, PR #311),
and this file is that design's §D8 freeze for this run. A clause below that differs from any of these says so, and says why.

---

## §D0 · THE INPUTS
```
  1  CONFIGURATIONS  three, each a HEAD model and a HEAD effort:
                       FX  Fable/xhigh   head claude-fable-5-1   CELL_EFFORT=xhigh
                       FH  Fable/high    head claude-fable-5-1   CELL_EFFORT=high
                       OX  Opus/xhigh    head <the Opus id, row 1b>   CELL_EFFORT=xhigh
                     Every id is passed to the client IN FULL, never as an alias (`fable`, `opus`), because an alias resolves at
                     launch and may resolve differently between cells. `claude-fable-5-1` is the id `claude --model fable` resolved
                     to at the object (CLAUDE.md fleet map, the 2026-09-22 measurement).
  1b THE OPUS ID     the Opus id the fleet's `opus` resolves to on the run box at the release, read at the object and named in the
                     release addendum (this session reads `claude-opus-5-5`; that is a reading on another box, not the registration).
                     ⚖️ FORK F3' (§D6). It links to the pilot's `claude-opus-5` cells of record ONLY if it is that same id; otherwise
                     OX is a NEW baseline and every table says so (kent's rider R2).
  1c THE TEAM        the sub-agent rows of the run root's models.tsv (worker-opus · worker-sonnet · reviewer · designer) are HELD at
                     the pilot's Opus table in all three configurations; only the `head` row moves. So a cell differs from its
                     neighbour in the HEAD's model and effort, and in nothing else the harness sets. ⚠️ A team row whose id is not
                     served on the release day moves in the release addendum, by name, for ALL three configurations at once.
  2  n               3 per (configuration × problem).
  3  POPULATION      3 configurations × 3 problems × n 3 = 27 cells (§D1). Nothing is added, dropped or substituted.
  4  EXPORT          ONE bare-master sha of saltbench-systems, named in the release addendum BEFORE the first cell, carrying §D2's
                     build items (S1 `CELL_EFFORT` at or descending from cf0033e; the rates rows of item 2) and descending from
                     block N's last release export. One sha for all 27 cells, recorded per cell.
  5  CLIENT PIN      lane B §Q0 row 5's form (the versioned client by ABSOLUTE PATH, its sha asserted per launch). The VERSION is
                     named in the release addendum, and it must accept both `--effort xhigh` and `--effort high` with a Fable head
                     (§D2 item 3). A cell launched on another version is refused.
  6  TASK TREE       the EXPORT's own tasks/systems-v3, and nothing else.
  7  CAPS            lane B §Q4: C1_USD $37.21, W1_SEC 144,000; CAP-COST and CAP-WALL armed. Read WU (a) below.
  8  CHAIN           runs/clb-sg-2026-09-18/clb_chain.v8.sh (v7 + flock), the only chain in the run dir that can start: every older
                     script exits rc 2 at its line 2 (retired 2026-10-16). Its sha256/16 is quoted in the release addendum.
  9  POOL            Fable heads draw the Fable-only meter. His charter names Fable configurations, so the word the commission
                     asks for is given. The pool is named per cell, with `cells_account_check.sh --expect <identity>` reading OK
                     before each fire. The PM places the 27 on the day lines from the identity cells' readings (§D3); nothing here
                     asks for spend past the budget.
```
⛔ **WU (a), C2_USD's MEANING, WRITTEN WHERE A READER MEETS THE CAPS:** `C2_USD` is a CELL-TOTAL cap evaluated during phase 2, NOT a phase-2
budget (`cell-watch.sh` compares it against the whole slug's meter). **No cell here has a phase 2** (greenfield × `none`), so it binds no
cell in this block, and it is written here because the Claude lane's next spec-change block will inherit this text.

---

## §D1 · THE POPULATION — 27 CELLS
```
  problems        Crc32 · LZW · FreeList       as chartered; each has a claude-opus-5 bare-plain result of record at 3 / 3
                                               (RESULT-correctness-tables-v3-2026-10-01.md, Table P1)
  field · extras  greenfield · none (bare)
  arm             plain ONLY                   fork F1: the question is about the knob, not the method
  configurations  FX · FH · OX                 §D0 row 1
  ⇒ 3 × 3 × 3 = 27 cells
```
**Not in this block, and why:** salt-diet (F1; it doubles the spend and folds the method's cap correlation into a knob reading) · Opus/high
(not in the charter; the pilot ran it at `claude-opus-5`, and it re-enters only by F3') · any other problem (F5 was measured EMPTY on the
Claude lane: every Claude bare-plain cell of record is 3 / 3 except claude-sonnet-5 FreeList at 2 / 3, already chartered).

---

## §D2 · ⛔⛔ THE BUILD ITEMS — EACH DRIVEN, WITH A CONTROL, BEFORE THE CELLS IT GATES
1. **`--effort` AS A VARIABLE (systems' backlog S1).** saltbench-systems `cf0033e`: `--effort "${CELL_EFFORT:-high}"`, a value outside
   `low medium high xhigh max` HOLDs `EFFORT` by name before any ARGV line. The lead's re-drive (the bus, 2026-10-16): the selftest suite
   on the branch, plus a mutant hard-wiring `--effort high`. The unset default is the literal it replaces, so every earlier cell's argv
   is unchanged. *The release addendum quotes both runs' tallies.*
2. **THE RATES TABLE PRICES EVERY HEAD.** `rates.tsv` (read 2026-09-05) carries `claude-fable-5-1` and `claude-opus-5` and NO row for
   `claude-opus-5-5`, and the meter prints a model with no row as `VOID(UNPRICED)`. ⇒ **An OX head the table cannot price has no armed
   CAP-COST.** Before release: the pricing page is RE-READ and every row the block uses is re-dated (the table's own header asks for this
   before any run whose caps are set in cost), and a row for the §D0 row 1b id is added from that page. The meter's selftest on a record
   carrying that id is green, and red with the row removed.
3. **A ZERO-SPEND DRY LAUNCH (kent's R4).** On the pinned client, `cell-claude.sh --launch` with the DRY stub prints three ARGV lines
   that differ in `--model` and `--effort` exactly as §D0 row 1 says, and the pinned client's own `--help` lists `xhigh` among its effort
   levels. The effort modal (desk MZ) was measured interactively only, so the identity cells (§D3) are also the first `-p` drive of a
   Fable head at xhigh: a cell that stalls on a dialog is a FAULT (§D7), never a result.
4. **THE CLAUDE-LANE FIRE PREREQUISITES:** (a) the chain is v8 (§D0 row 8); (b) WO (b): a `declined-subject` probe
   verdict (the subject answered the sandbox probe and refused) is RECORDED on that cell's RESULT row, never silently re-routed to another
   pool or re-fired as an instrument fault; (d) WO (d): `credgate identity` per pool and the status line's `strands=` are read before the
   first cell and quoted in the release addendum; (c) WU (a), written in §D0; (e) ⚠️ `cells_account_check.sh` (block N §N2 item 2) is
   at saltbench-systems `0da916f` and is NOT an ancestor of master at `cf0033e`: the export carries it, or the release addendum names the
   path and sha the check runs from. A check that is not in the export is not evidence that the export was checked.

---

## §D3 · THE ORDER, THE IDENTITY CELLS, THE TRIPWIRE
- **Identity cells first: ONE per configuration, on Crc32** (the cheapest chartered problem). Each must show, in its transcript, every head
  `message.model` equal to the requested id, and every sub-agent `message.model` equal to its models.tsv row. An unrecognised id
  SUBSTITUTES silently, so this read is the only evidence of what was served. **The applied effort is NOT in the transcript**: the argv in
  the launch record is the only record of it, and that limit rides beside every figure. An identity cell that reads clean counts as cell 1
  of its (configuration × Crc32) condition unless §D7 voids it.
- **The tripwire is the identity triple**, read by the lead and posted before the block continues: the three served-set reads · each
  cell's T, output tokens, wall and list-USD · the Fable-meter reading before and after each Fable cell. **The PM's points-per-cell
  estimate is written from these three cells and from nothing else**, and the remaining 24 are placed on the day
  lines from it.
- **Then interleaved by configuration within each problem**, one cell at a time on one pool: Crc32 #2–#3 (FX FH OX FX FH OX), then LZW #1–#3,
  then FreeList #1–#3. Interleaving removes the time-of-day and quota-state confound a blocked order would build in.
- **Stop rule.** If the tripwire price puts the 27 past desk OD's review (2026-10-30) on the day lines, the lead posts that with an order
  before any cell beyond the tripwire: a cut removes a WHOLE PROBLEM (all three configurations), never one configuration alone, and n is
  never reduced quietly.
- **Two more tripwires, because the first is low by construction (kent's rider, 2026-10-16, class PRICE).** The identity triple is all
  Crc32, the cheapest chartered problem, so a price from it under-reads LZW and FreeList. The block therefore also stops at the **first LZW
  triple** (LZW #1 FX FH OX) and at the **first FreeList triple** (FreeList #1 FX FH OX). At each, the lead posts the same readings as the
  identity triple for those three cells, and the PM re-writes the price for the cells that remain from **every cell fired so far**. The stop
  rule above applies unchanged. A cut removes only a problem with no cell fired yet. At the FreeList tripwire, where no such problem is left,
  the order is either to continue past 2026-10-30 (with a pack ask to move desk OD's review) or to DECLARE FreeList's remaining cells
  unreached at n = 1. Neither is taken quietly.

---

## §D4 · THE OUTCOMES — design §D3, mapped onto the v3 classes, and the ceiling rule FIRST
- **Classes** (`REGISTRATION-correctness-tables-v3-2026-10-01.md` §P2, registered here BEFORE the run): PASS · FAIL · CENSORED · UNSCORABLE,
  read as design §D2's ACCEPTED · REJECTED · HALTED · UNSCORABLE. The subject's landing claim never decides a class.
- ⛔ **THE CEILING RULE (kent's R1), REGISTERED BEFORE ANY CELL:** if every cell of two configurations on a problem PASSES, that problem's
  ABILITY reading for that pair is **NO INFORMATION**, never "equal", and the problem reports its COST reading alone. ⇒ **THIS BLOCK IS
  REGISTERED COST-FIRST:** all three problems sit at 3 / 3 for `claude-opus-5` at high, so ability is EXPECTED to read NO INFORMATION.
  Ability against effort belongs to a population that can show it (HV item 4's harder problems), not to this one.
- **Ability, where the ceiling rule permits:** design §D3 1, (i) and (ii), per configuration per problem, with §P4's interval rule for a sign.
- **Cost per task, per configuration per problem:** design §D3 2's row `a · r · h · u` and (c0) · (c1) · (c2), in METERED T (input + output +
  cache reads + cache writes), with **OUTPUT TOKENS printed beside T in every row** (T is ~97 % cache reads in this lane; the knob is
  expected to move output). A halted cell's spend enters as METERED, never clipped (design §D3 2, overriding lane B §Q6 6). Wall time is
  printed beside, never as a cost. **List-USD** from the re-dated `rates.tsv` (§D2 item 2) is printed as a third column, labelled
  *list price at <date>*: a subscription meter is not a price, and the Fable-meter reading per cell is printed beside it where measured.
- Rule 3 holds: no cost figure is pooled across problems.

## §D5 · PREDICTIONS — REGISTERED PER CONFIGURATION BEFORE THE FIRST FIRE
Each is descriptive at n = 3 (no test) and is reported MET or NOT MET:
- **P1** FX spends more OUTPUT tokens per cell than FH on at least 2 of 3 problems (median of 3).
- **P2** FX's acceptance is not below FH's on any problem by §P4's interval rule. *Scored only on a problem where some configuration falls
  below 3 / 3 (R1); at 3 / 3 it passes by construction and is reported NOT SCORED.*
- **P3** The ratio of median OUTPUT tokens, FX over FH, is above 1.2 on every problem. This is the direct test of "the same price": if it
  fails, the remembered message was right per task as well as per token.
- **P4** OX's acceptance equals FX's on all three problems. *Same R1 scoring as P2.*
- **P5** (new, from §D0 row 7) CAP-COST binds no cell. One USD cap is a different token budget per head (lane B §Q5 3): at `rates.tsv`'s
  rows (2026-09-05) Fable's input, cache-write and output rates are 2 × `claude-opus-5`'s and its cache-read rate is 0.5 ×, so the cap
  costs Fable more per OUTPUT token and less per cache read. If it binds at all, it binds FX first, the output-heaviest configuration.
  A miss is a result, and a cap-out enters (c0) as metered.

## §D6 · FORKS — each with the lead's recommendation, taken unless overturned
- **F1, the arm:** plain only (taken).
- **F2, n:** 3 (taken). n = 1 cannot report a per-condition comparison, so a 9-cell pass would be spent again.
- **F3', the Opus id:** the fleet's current Opus (rec: it is the knob he is asking about), or `claude-opus-5` if still served (it links OX
  to the pilot's cells of record, at another effort). The release addendum names which, and why, from the identity read.
- **F6, the team (new):** hold the sub-agent rows at the pilot's Opus table (rec, §D0 row 1c), or make each configuration single-model.
  Single-model would move the team with the head, so a configuration difference would be a TEAM difference (lane B §Q5 1). Holding the
  team keeps the knob on the head, which is what `--effort` sets.

## §D7 · CONFOUNDS AND VOIDS — lane B §Q5 and §Q7 carried, plus these
1. **THE KNOB IS THE HEAD'S.** `--effort` is the head session's flag. Whether a sub-agent inherits it is UNMEASURED, and no transcript
   field records the applied effort. A configuration difference is a HEAD-effort difference in argv, and is never described as more.
2. **FX ↔ OX IS A CONTRAST, NEVER A TIER RESULT:** model tier and generation move together (desk OD's own clause). It is reported as "these two
   configurations", never "Opus vs Fable".
3. **THE CEILING:** three problems at a ceiling-prone difficulty. A knob that matters only on hard problems reads as no difference here.
4. **ONE CLIENT VERSION:** a client update between cells is a confound, so the pin is enforced per launch (§D0 row 5).
5. **VOID ROWS ADDED:** a head or sub-agent `message.model` other than its requested id ⇒ VOID(SERVED), the cell re-fired once after the
   release addendum names a corrected id · a cell that stalls on a client dialog ⇒ FAULT, re-fired once · `cells_account_check.sh` not
   OK ⇒ DO NOT FIRE (block N's row 11).

## §D8 · WHAT THIS BLOCK CANNOT ESTABLISH, SAID BEFORE ANY DATA
1. Ability against effort, on these problems: it is registered to read NO INFORMATION wherever all cells pass. 2. Anything about salt-diet
or about the method. 3. Anything about Opus/high at the current Opus. 4. The effort the client APPLIED: only the effort it was ASKED for.
5. A price: list-USD is a list price at a date, and the subscription meter is the fleet's real cost.

## §D9 · WHAT THE HAND DELIVERS
Lane B §Q9's per-cell list, less its brownfield columns, plus: the configuration and its argv per cell · the head and sub-agent served set ·
output tokens beside T · list-USD at its dated rate · the Fable-meter reading per Fable cell · the account-check line. ⇒ **A RESULT file with
§D4's rows per configuration per problem and §D5's predictions MET / NOT MET / NOT SCORED, merged with a non-author read.** Desk OD is
re-read against it. Any public sentence, and any claim about the method, is the Captain's.

---

## ⚖️ ADDENDUM 1 — THE RELEASE. APPENDED; all text above, the signature included, untouched.
**bench (lead), 2026-10-17. COMPLETE AND OFFERED FOR A NON-AUTHOR SIGNATURE; it fires nothing by itself.** *(R1.1 named `0d97b68` until R1.7
was built; it now names `811dc09`.)* Three reads are taken AT FIRE by design and are not owed here: the server identity of the pool (R1.5 (d),
after the client's own refresh), the chain's `strands=` (R1.5 (d)), and the head id the identity cell is SERVED (R1.3). The first cell fires
only after a non-author signs this addendum. Every figure is read from `evidence/od-release-2026-10-17/`.

### R1.1 · §D0 ROW 4, THE EXPORT IS `811dc09` — ✅ TAKEN 2026-10-17
saltbench-systems master was fast-forwarded `d398cb0` → `0d97b68` → `811dc09657b47d42c65bba8653c0e7b62f6e69dc`, each step after a non-author
read of every commit in it (kent: `d398cb0..20401330` · `20401330..6e9c7ce` · `6e9c7ce..0d97b68` · `0d97b68..811dc09`, the last with the suite
reproduced). Contents over `d398cb0`: S1 (`cf0033e`) · the rates rows (R1.2) · `cells_account_check.sh` (§D2 4(e), blob `76f59182ad70`,
taken ALONE from `0da916f`) · the head-only model tables, the R4 and empty-effort arms (R1.3, R1.4) · OD's blocks in the stager, fire and
harvest, with the effort carried by the cell (R1.7). **One sha for all 27 cells, recorded per cell.** `0d97b68` was an interim export and
fires nothing.
- **Exported** to the run box under a destination of its own, `--no-toolchain` (the Z chain was live there and reads the cargo cache that
  step rsyncs; the toolchain is checked read-only at the first cell): 374 files, listing sha256/16 `de72b2ce4294cb9c`, 0 withheld-shaped
  names on either side, the marker written last (`export-811dc09.out`).
- **The run-box drive, re-run against this export** (`runbox-drive-811dc09.out`, lane B's `runbox_drive.py` unchanged): marker `811dc09…` ·
  375 files (374 + the marker) · 0 withheld/mutants directories · 2 paths carrying the word, both INSTRUMENTS, named from the export itself
  in `runbox-word-paths-811dc09.out` (`check_withheld_leak_v3.py`, as at `bcd2205`; `withheld_access_census.py`, added since; kent's finding:
  the drive prints only the count) · the five brownfield givens · the export's own `served_models_v3.py` reads 45 of 45 HC1 cells clean
  as Opus and SUBSTITUTED as Sonnet.
- **The OD conditions, read from the export** (`served-tables-811dc09.out`): `fable51` launches `--model claude-fable-5-1`, `opus55`
  launches `--model claude-opus-5-5`, every sub-agent row is the Opus table's, rc 0 for both.
- The `0d97b68` evidence files stay in this directory as the interim export's record.

### R1.2 · §D2 ITEM 2, THE RATES — ✅ TAKEN 2026-10-17T05:01Z, `VERDICT ALL-EQUAL`, rc 0
The page `rates.tsv` cites, read as raw bytes (160,503 B, sha256/16 `12219c9d9fe4d5c1`), by two methods. (a) Lane B's `rates_reread.py`,
copied with ONE change, the Opus 5.5 row added to its model list (`rates-reread.diff`): four served ids EQUAL (`rates-reread.out`); the
master table without that row reads `MISSING`, rc 1. (b) A parse of every page row against every table row: 15 rows, 0 mismatches.
- ⚠️ **P5's ratio, against the id actually served.** Opus 5.5 is priced BELOW Opus 5 (input $4, output $20, cache read $0.20). P5 states
  its ratios against `claude-opus-5`. Against `claude-opus-5-5`, Fable is 2.5 × on input, cache writes and output and 1.25 × on cache
  read, so P5's clause *"less per cache read"* is FALSE for that id. P5's prediction (if CAP-COST binds at all, it binds FX first) is
  unchanged and stronger.

### R1.3 · §D0 ROW 1c AND F3', THE HEAD — BUILT; THE ID IS OWED TO THE IDENTITY READ
The registration said only the head row moves, and the harness had no way to move it: `cells_bin.sh` linked only the Opus and Sonnet
tables. Built: `models-head-fable51.tsv` and `models-head-opus55.tsv`, each `models.tsv` with the head row replaced (an arm proves every
other row byte-identical); conditions `fable51` and `opus55` in `served_models_v3.py`, so `check-cell` (§D3's identity read) can name
them. **F3' is taken on its recommendation: OX's head is `claude-opus-5-5`, the fleet's current Opus.** OX is therefore a NEW baseline,
not linked to the pilot's `claude-opus-5` cells (kent's R2), and every table says so. If the OX identity cell is served another id,
that is a SUBSTITUTION (§D7), never a silent re-mapping.
- ⚠️ **A label that moved with nothing under it (kent's note 2):** in both head tables the `source` cells of `worker-opus` and `reviewer`
  read *"as head"*. They were copied byte for byte from `models.tsv`, and an arm keeps them that way, so *"head"* there means
  `models.tsv`'s head, `claude-opus-5`, and NOT the table's own head. No tool parses that column; the arms read `requested` and `served`.
- **The head id is tied outside its table:** each head table's id must be exactly one row of `rates.tsv` (kent's note 1; mutant red).

### R1.4 · §D2 ITEM 1 AND ITEM 3 — ✅ BUILT AND DRIVEN ON THE CANDIDATE
- S1 (item 1): the lead's re-drive on `cf0033e`, 69 / 71 with the hard-wired mutant red on S1(b) only. kent's finding 2 (an EMPTY
  `CELL_EFFORT` read as `high`, so FX would fire as FH) is fixed as `${CELL_EFFORT-high}` with arm S1(d), red first.
- Item 3, the dry launch (kent's R4): an arm in the suite. FX (`fable51`, xhigh) · FH (`fable51`, high) · OX (`opus55`, xhigh) through the
  DRY stub print ARGV lines that carry `--model <the table's head> --effort <e>` and are identical outside those two tokens. Mutant (the
  launcher hard-wires the model): red on that arm only. **The pinned client** (lane B's 2.1.259, sha256/16 `884baa38fe1a624b`, read on the
  run box) lists `--effort <level> (low, medium, high, xhigh, max)`.
- The suite on the candidate: 71 / 73, 0 failed, 2 SKIP (the placebo arms, declared).

### R1.5 · §D2 ITEM 4 — PARTLY TAKEN 2026-10-17; THE REST IS READ AT FIRE
- (a) ✅ `clb_chain.v8.sh` sha256/16 `f443719751e7a3ed` (the chain runs from the build box and drives the run box).
- (d) ⚠️ **`credgate identity`, a server read, over the six cells config dirs on the run box: NO IDENTITY READ.** Three hold an EXPIRED
  access token with a live refresh (`EXPIRED-REFRESHABLE`); a refresh is a write, so a read-only release cannot turn them into identities.
  Three are `DEAD-REFRESH` and need a human `/login` before they can carry a cell. ⇒ **The pool the PM names for the identity cells is read
  by `credgate identity` at fire, after the client's own refresh, and that line is quoted beside the cell.** `strands=` is a chain status
  field and is read from v8's own status line before the first cell.
- (e) ✅ (file identity) `cells_account_check.sh` from the export, against the run box's default cell env: `ACCOUNT-CHECK OK`, credential
  present (access and refresh non-empty). **Its limit rides with it: the FILE identity, never "a launch will authenticate".** The fire runs it
  as the tool takes it (kent's finding 1), `--refuse <the account named as dead> --expect <the pool the PM names>`.
- (b) The `declined-subject` row form is quoted from the RESULT template when the RESULT file is opened.

### R1.7 · OD's BLOCKS AND THE EFFORT'S CARRIER — ✅ BUILT (in `811dc09`)
The stager, fire and harvest knew only lane B's seven blocks, so no OD cell could be staged. `clb_stage.sh`'s block table gains
`cond · effort · lane` columns and FX · FH · OX rows; `--roots` stays lane B's 64, and `--roots-od` makes exactly OD's 9 roots (three blocks
× Crc32 · LZW · FreeList × plain). An OD block refuses any other problem or arm before creating anything.
- ⛔ **THE EFFORT IS A PROPERTY OF THE CELL, NOT OF THE FIRE'S ENVIRONMENT.** `cell-watch.sh` starts the client in a new tmux window whose
  environment is built from a fixed list that does not carry `CELL_EFFORT`, so an effort exported at fire would never arrive, and every
  OD cell would have launched at `high` with every check green. The stager writes `ctl/effort`; `cell-claude.sh` reads it, and a SET
  `CELL_EFFORT` that disagrees HOLDs; `clb_fire.sh` refuses an OD cell whose `ctl/effort` is not its block's, and a lane-B cell carrying
  one, before anything is driven. Lane-B cells carry none, so their argv is unchanged.
- Arms: S1(e)/(f) and `clb_stage-od` (six behaviours, `--dry` on a fixture export). Suite 72 / 74, 0 failed, 2 SKIP. Mutants: the stager
  writes no `ctl/effort` → red on that clause only; the fire's effort check bypassed → red on that clause only.
- ⚠️ **LIMIT:** the subject can READ its own `ctl/`; whether the Claude fence lets it WRITE `ctl/effort` is not driven. A rewritten file would
  change a RE-launch's effort, so the RESULT reads each cell's effort from the ARGV line in its launch log, never from `ctl/effort`.
- ⚠️ **LIMIT (kent's environment finding):** with stdin at `/dev/null` the suite's `probe-sandbox` arm reads 47 / 52 (five runtime arms
  INDETERMINATE) at this sha and at its parent; with a real stdin it reads 52 / 52. The suite's tallies above were taken with a real stdin.
  An unattended suite run reads that one arm red while the code is fine; the root cause is not established.

### R1.6 · THE WITHHELD CENSUS, AT A HELD Z BOUNDARY — ✅ TAKEN 2026-10-17 08:44–08:45Z, ALL SIX TREES `COVERED · COVERED`, rc 0
The window: the Z chain held before Z073 (gemini), no cell process live on the run box (checked at the object; the long-running agy pool
canary was the only harness process). In order, each stopping on its own refusal: `clb_stage.sh --roots-od` (9 roots, each on its block's
table) · `clb_stage.sh FX Crc32 plain 1` (`clbxcp01`, client pin `884baa38fe1a624b`, table `fable51`, `ctl/effort` xhigh read back) ·
`fence-only-OD.sh FX Crc32 plain 1` (the export's own `clb_fire.sh` with the YIELD line removed and cut after FENCE CONVERGES, as lane B's
fence-only step was): **FENCE CONVERGES sha16 `b418ca420995a805`**, no launch, nothing spent · lane B's `withheld_exposure_census.py`, unchanged,
on that fence and the newest agy fence (`census-at-window.out`):
```
  # host role: the run box (cells-* roots under ~: 478)
  # fences: claude clbxcp01 (denyRead 712) · agy zffcgss301 (denyRead 702)
  # withheld-shaped entries: 666 in 6 top-level trees (a FLOOR: depth 7, no tarballs, name-based)
  ~/bench-dry 384 · ~/projects 178 · ~/bench-v2 34 · ~/bench-v2-smoke 34 · ~/bench-v2-amend6 18 · ~/bench-v2-census-a6 18   ALL COVERED · COVERED
```
**Its limit rides with it:** 666 is a FLOOR, not a ceiling. Everything this method can see is denied to both lanes; it is not a proof that
no withheld material exists anywhere. The nine OD roots existed before the next Z cell's fence render, so later Z cells glob them.

---

## ⚖️ ADDENDUM 2 — THE CHAIN IS `clb_chain.v10.sh`, NOT v8 (§D0 row 8). APPENDED; all text above, both signatures included, untouched.
**bench (lead), 2026-10-17.** Found after ADDENDUM 1 merged, while preparing the identity triple: the registered chain cannot run an OD cell.
`clb_chain.v8.sh` (sha256/16 `f443719751e7a3ed`) carries a third copy of lane B's block list. Its `ids()` refuses FX · FH · OX as a bad row,
and it would have checked the served set against an `opus`/`sonnet` condition. It also picks a pool's env file by pool name alone and takes
it only when `CLB_CFG` names `.claude-account-<pool>`. It builds the harvest's transcript slug from a HARD-CODED `.claude-account-<pool>`,
so an OD cell's served-set read would look in the wrong config dir.
- **v10** (sha256/16 `ad5cf236ebbaceb0`) = v8 plus four changes, in two steps (v9 `dc25a883e741bb5b`, then v10 on kent's defect in v9):
  (1) `ids()` knows FX · FH · OX, and the served-model condition follows the block (FX · FH `fable51`, OX `opus55`); (2) `CLB_CHAIN_ENV_PREFIX`
  picks `<prefix>-<pool>.env`, so OD's env is chosen by lane and pool (`claude-lane-od-<pool>.env`), and the prefix is validated; (3) a pool's
  env is taken when its `CLB_CFG` basename is `.claude-account-<pool>` or `.claude-v3-<pool>`, still keyed by the pool's name (OD stays on
  the v3 dir that R1.6's fence was rendered under); (4) `pool_cfg`, which builds the served-set read's slug, returns the config dir THAT ENV
  FILE names, never a hard-coded one. Nothing else changes, including the single-instance lock, the day lines, the breaker and the escape scan.
- **Arms, on the stub box, zero spend.** `arms_v9_od.sh` (v8 against v10): A1 (an FX row: v10 starts, records `cond fable51`, no bad row;
  v8 stops rc 2) and A2 (OD's env by prefix with the v3 dir: v10 resolves it; v8 refuses the start, rc 9) are LOAD-BEARING; C1 (lane B's
  form) is a control, green on both. `arms_v10_harvest.sh` (v9 against v10), which reaches the HARVEST past START: H1 (an FX row under OD's
  env) has the served check's `--slug` under the fixture pool's v3 config dir on v10 and under its account config dir on v9, so it is LOAD-BEARING; HC (lane
  B's form) reads the account config dir on both, a control. v8's own arms hold on v10: `arms_v7.sh` load-bearing 4 of 4, `arms_v8_lock.sh`
  1 of 1, no control broken.
- ⚠️ **LIMIT:** every arm runs against a stub run box. The real run box's first measurement is the identity triple, and the served-set read
  of each identity cell is the check that this change reaches the right directory.
- R1.5 (a)'s sha is therefore `ad5cf236ebbaceb0` for OD's cells. v8 stays the lane-B chain, which is now finished.

## ⚖️ ADDENDUM 3 — THE CHAIN IS `clb_chain.v11.sh`, NOT v10. APPENDED; all text above, every signature included, untouched.
**bench (lead), 2026-10-17, relight 148.** v10 was fired for the identity triple at 02:30:29 PDT, after the three riders, and REFUSED AT START
(rc 9), before any cell was staged or fired: no spend. Its ssh default named the run box by its RETIRED host name, which no longer resolves.
The same name was hard-coded a second time in `score_cell`'s harvest copy (`rsync`), which `CLB_CHAIN_SSH` never reached. Every arm since
v5 replaced ssh with a stub AND set `CLB_CHAIN_NOSCORE=1`, so neither use was ever driven. The helm's sweep of v10 found a third retired
default: `POOLS` defaulted to a pool retired on 2026-10-14.
- **v11** (sha256/16 `6cc95561062920c0`) = v10 (`ad5cf236ebbaceb0`) plus two changes. (1) ONE variable, `RUNBOX`, names the run box (by
  default its current name), and both the ssh default and the harvest `rsync` use it, so the START probe that reaches the box covers the
  harvest's host too. (2) There is NO pool default. An unset or empty `CLB_CHAIN_POOLS` refuses the start (rc 9), as does any pool listed in
  the fleet's retired-pool list, or that list being unreadable (fail-closed). Nothing else changes.
- **Arms on the REAL run box, zero model spend** (`arms_v11_runbox.sh`). R1: the ssh default as the chain evaluates it (v10 rc 255, v11
  rc 0). R2: `score_cell`, extracted verbatim from each chain, harvests and scores an ENDED past lane-B cell (`clbglp01`) under a scratch
  `HOME`. v11 prints `PASS 16/16`, EQUAL to that cell's row of record, which was read and not written; v10 fails. A MUTANT of v11 with only
  the `rsync` host reverted passes R1 and fails R2 with `FAIL:harvest copy`, so the second site is load-bearing on its own.
- **Arms on the stub box** (`arms_v11_pools.sh`, v10 against v11). P1 (pools unset: v10 aims at its retired default, v11 refuses), P2 (a
  retired pool with a valid env file: v10 resolves it, v11 refuses) and P3 (an unreadable retired list: v11 refuses) are LOAD-BEARING. C1
  (a live pool) is a control and is green on both. v10's own arms re-run on v11 give verdicts identical to v10's: `arms_v7.sh` (only a pid
  differs), `arms_v8_lock.sh`, `arms_v9_od.sh` and `arms_v10_harvest.sh`.
- **The names sweep** (`sweep_v11_names.md`): 23 needles, derived from the retired-pool list, the ssh host list and the roster's pool column,
  each grepped case-insensitively as a literal. v11 carries exactly ONE live host or pool literal, the current run box (the positive
  control). Every other hit is a comment or a receipt label. A census by kent of the export's box-side scripts that the chain calls (stager,
  fire, harvest, served-set check, watcher, account check) found 0 retired names, and the OD env file on the box carries none.
- ⚠️ **LIMITS:** R2 drives a lane-B cell built from an earlier export, because no OD cell has ended. The served-set read under OD's v3 config
  dir is still first measured by the identity triple itself, as ADDENDUM 2 said. The sweep covers NAMES, not other environment-bound paths.
  `score_cell`'s paths were exercised by R2 on this box.
- R1.5 (a)'s sha is therefore `6cc95561062920c0` for OD's cells. v10 is RETIRED: it is out of the run dir, kept beside its refused run as
  evidence. The chain, its arms and their outputs are in the lead's chain record at seat commit `702d35ca3`.
