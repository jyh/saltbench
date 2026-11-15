# AMENDMENT — O37 BLOCK WA: WHT AND NTT, GREENFIELD × `none`, agy LANE. FROZEN BEFORE THE FIRST CALL
## bench (SaltBench lead), 2026-11-13. This is block W's sibling freeze (`AMENDMENT-O37-wht-ntt-greenfield-claude-2026-11-11.md`, cited as
## "block W", §W1: "the agy half is a sibling freeze"). The form is block NA's (`AMENDMENT-O37-nine-greenfield-agy-2026-09-25.md`, signed,
## ADDENDA 1–5, cited as "NA"), and it CARRIES NA's lane machinery BY CITATION exactly as NA carries level 6's. A clause below that differs
## from NA says so, and says why. The authority is NA's and block W's: the Captain's council word of 2026-09-25 (the remaining problems run
## on bench at P3, on quota no higher-priority work needs) and his objective "fill out the 14 problems (greenfield only)".
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ **NO CELL FIRES BEFORE §WA2's ITEMS ARE DRIVEN AND A RELEASE ADDENDUM NAMES THE EXPORT SHA
## AND EACH §WA2 RECEIPT AS MET.** Signature and release are two acts, as in NA.

**Why now.** Block W's §W2 build items 1–3 and item 4's leak half were met on 2026-11-13 on the Claude-lane export candidate. Two
problems, WHT and NTT, are the last greenfield × `none` conditions O37 has on either lane (census ADDENDUM 39: LU DECLARED). This block is
their agy half.

---

## §WA0 · THE INPUTS (NA §NA0, row by row)
```
  1  MODEL IDs     gemini-3.1-pro-high · gemini-3.8-flash-high, NA row 1 unchanged. Re-asserted served at launch; a served-model mismatch
                   VOIDS (level 6 §H6 row 1). Neither id has been fired on this lane since 2026-10-24 (the Z wave), so the release
                   re-measures both on the release's client before any cell: a served id is a reading of a day.
  2  n             3 per condition.
  3  POPULATION    8 conditions, 24 cells (§WA1). Nothing is added, dropped or substituted.
  4  EXPORT        ⚖️ THE CHANGE FROM NA: ONE harness sha, named in the release addendum, that (i) carries the agy lane's PRODUCTION
                   LINE today, saltbench-systems 0b783cf3 (the export the Z wave fired on through 2026-10-24; gemini's account on the bus
                   2026-11-13 21:26:10), with its harness tree UNCHANGED, and (ii) carries tasks/systems-v3/{WHT,NTT} at the git tree
                   hashes block W §W2 item 1 drove (WHT 44b92115, NTT 77c64177). CANDIDATE: 6413289d (backup branch
                   bench/o37-WA-agy-export-candidate-2026-11-13) = 0b783cf3 + those two trees OVERLAID in one commit; its harness tree
                   (21e6a4ab) equals 0b783cf3's, and the diff outside the two task dirs is empty. The two task branches are NOT merged,
                   because they would carry 13 Claude-lane harness files into the agy line (merge-base d398cb0f).
                   NA ran on e10f420 / 8ed8cb3, which are not ancestors of 0b783cf3; see §WA4 item 2.
  5  CAPS          NA row 5 as NA ADDENDUM 4 left it, unchanged: T1_TOK 250,000,000 · AGY_PRINT_TIMEOUT 1800 s · AGY_TURN_TIMEOUT
                   2100 s; CAP-TOKENS, CELL-KILLED and TURNS-CUT reported per arm, never a void; ADDENDUM 4's arm-binding of the
                   per-turn deadline is registered here as an OUTCOME, exactly as there (cut turns ÷ turns, truncated cells ÷ cells,
                   CUT-BOUND in its own column, a truncated PASS a FLOOR). No cap is raised.
  6  QUOTA         NA row 6 unchanged: P3, the agy subscription pool (separate from every Claude pool), yielding to any O4 agy cell live
                   or queued; the hand reads agy /usage at each fire and bank.
  7  FIRE ORDER    §WA2.
```

## §WA1 · THE POPULATION — 8 CONDITIONS, 24 CELLS
Derived, not typed. Block W §W1 derives O37's 48 conditions for NTT and WHT; the greenfield × `none` slice is 8 per lane. This block takes
the agy lane's:
```
  problems   NTT · WHT                                 block W's two
  models     gemini-3.1-pro-high · gemini-3.8-flash-high
  arms       plain · salt-diet        field  greenfield        extras  none
  ⇒ 2 × 2 × 2 = 8 conditions · × n 3 = 24 cells
```
The agy client's `cell_build.py` registers exactly these two arms (`--client agy` REFUSES `--arm salt`, measured on the candidate
2026-11-13). Not in this block: NTT and WHT × {statement, spec-change} on either lane (32 conditions), and block W's Claude half.

## §WA2 · ⛔⛔ THE BUILD ITEMS, THE ORDER AND THE TRIPWIRES
**Build items, each driven with a control before the cells it gates:**
1. **TASK VALIDITY ON THIS EXPORT'S HARNESS, BY A NON-BUILDER.** Block W §W2 item 1 (a)–(d), with block W's builder table as the figures to
   reproduce, re-driven on the candidate. ⚖️ THE CHANGE FROM NA: NA cited block N's drive because NA's six trees were byte-identical on the
   same harness line. Here the task trees are identical to block W's but the harness is the agy line, so the drive is repeated here. A
   task that disagrees on any of (a)–(d) is WITHDRAWN by name and its conditions are reported NOT-FIRED(TASK) by an addendum.
2. **THE REFEREE ON DRY CELLS, `--client agy`.** Reference on both registered arms (salt-diet and plain) PASS, and one mutant per task
   TESTS_FAIL. Driven by the lead on the candidate 2026-11-13 (on the run box, scratch dir `wa-export-refdry-2026-11-13`): WHT and NTT salt-diet and
   plain references PASS 11/11, DivideFirst TESTS_FAIL 9/11, OwnRoot TESTS_FAIL 7/11; rubrics WHT cf343b86 · NTT a2f69fee. The release
   re-cites these or re-drives them on a moved export.
3. **NO LEAK INTO A VIEW:** `check_withheld_leak_v3.py` over the export. Driven 2026-11-13 on the candidate: CLEAN, 244 identifiers across
   13 tasks (WHT 30, NTT 28), every positive control fired.
4. **THE LANE IS LIVE ON THIS EXPORT:** the agy battery on one dry cell per model on the release's client (credential window, served
   model, fence intact, TMPDIR identity, the TREE-HASH line), and the agy client version it reads, named in the release. The lane has not
   fired since 2026-10-24.
**Order:**
```
  models     Flash first, then Pro (NA §NA2's reason)
  problems   WHT → NTT (ascending reference size, 816 · 924, block W §W3)
  cells      per problem: plain#1 · salt-diet#1 · plain#2 · salt-diet#2 · plain#3 · salt-diet#3, through the wave supervisor
```
**Tripwires, each ONE cell, read by the lead before its model continues:** `T-WA-F` = Flash · WHT · salt-diet#1 · `T-WA-P` = Pro · WHT ·
salt-diet#1. The reading list is NA's (level 6's, plus the TREE-HASH line), plus ADDENDUM 4's per-turn cut count from the client's stderr.

## §WA3 · PREDICTIONS — REGISTERED BEFORE ANY DATA
NA §NA3 (i) and (iii), carried: (i) within a condition, salt-diet's TURNS-CUT and CAP-TOKENS incidence is ≥ plain's; (iii) CELL-KILLED binds
no cell outside a declared 503 episode. NA's (ii) (incidence rises with reference size) is not carried: two problems of 816 and 924 lines
cannot test it. ⛔ **No prediction about pass rate or premium**: neither problem has run on any lane.
**The price** is in the agy pool's own unit, not dollars (NA row 6): read from agy /usage at each fire; no dollar figure is registered.

## §WA4 · CONFOUNDS — NA §NA4 carried, plus two of this block's own
1. **NEW PROBLEMS, ONE AUTHOR, WHO IS ALSO THE LEAD** (block W §W5 item 1), and **NTT's reference proves less than WHT's** (block W §W5 item
   2), both carried verbatim.
2. **A DIFFERENT HARNESS FROM NA's.** 0b783cf3 carries, beyond NA's exports, the 10-13 ctl fence (ZF export f048a780), the warm-up
   false-refusal fix, the turn-loop wedge stop and EMPTY-TURN label, CREDENTIAL-NETWORK and the token.expiry reader (gemini's account,
   2026-11-13 21:26:10). WA's cells are therefore not poolable with NA's into one cross-problem agy table without that seam printed beside
   it. Nothing in this block compares a WA cell with an NA cell.

## §WA5 · WHAT THIS BLOCK CANNOT ESTABLISH
Block W §W8 items 1, 3 and 4 (no effect size; nothing outside the 8; WHT and NTT are a SELECTION). Also: nothing Claude-versus-agy (level 6's
cross-lane rule), and nothing about NA's six.

## §WA6 · WHAT THE HAND DELIVERS
NA §NA6 unchanged: level 6 §H8's list, plus the tree-hash line per cell, the O4 concurrency column and ADDENDUM 4's cut columns. ⇒ **A result
of record per model**, and O37's census section re-cut in the same commit. Any public sentence, and any claim about the method, is the
Captain's. The hand is named in the release (NA's was `gemini`).

---

## ✍️ NON-AUTHOR SIGNATURE — the helm (210th head), 2026-11-13 21:51 PST, bus offset 101,943,023 (transcribed by the lead)
COMPLETE WITH LIMITS, on blob `bb6c9a4db2aa` at head `2ea26341523f`, read whole (97 lines). Checked: §WA1's 24 and the client's own refusal
fixing the two arms; §WA0 row 4's harness kept byte-identical and the merge refused; §WA2's repeated non-builder drive with its reason, the
run dirs for items 2–3, the lane-live battery; §WA3 dropping NA's (ii) with its reason and no pass-rate prediction; §WA4's seam. Its
limits, named and not cleared: NA, block W, level 6 and NA ADDENDUM 4 taken as cited; candidate 6413289d not opened; items 2–3's runs not
re-read; gemini's account of 0b783cf3 not read.

## §WA2 item 1, MET (recorded, not a release): systems (built neither task) re-drove block W §W2 item 1 (a)–(d) on 6413289d on a second
box, bus offset 101,945,641: WHT and NTT match block W's builder table on every column, and every VERUS / TESTS / MUTANT / TRACE / OWN line is
identical to its own run on the Claude-lane candidate 6615a7f8. Neither task is withdrawn. Item 4 (the lane-live battery) and the release
remain.

---

## ⚖️ ADDENDUM 1 (2026-11-13, bench) — THE FLASH HALF IS RELEASED; THE PRO HALF IS HELD, BECAUSE TODAY'S CLIENT DOES NOT SERVE ITS ID. APPENDED.
**§WA2 item 4, the lane-live battery** (hand `gemini`, bus offset 101,971,201; run dir on the run box `gemini-wa-battery-2026-11-13`):
```
  export        6413289d by studio_export.sh: rc 0, 386 files, 0 withheld-shaped names on both sides, required-ancestors 5/5;
                the verifier's sha equal on both boxes; TREE-HASH: WHT 4/4 and NTT 4/4 export files equal to the git blobs, and every
                WHT file a dry cell's copied.tsv names is equal to the export's
  client        agy 1.5.9. It SELF-UPDATED from 1.4.10 during the read (binary mtime 06:09Z), so the release names 1.5.9
  pool          Gemini weekly 100 % / five-hour 100 % before each live turn; credential window about 55 min at Flash's turn (> 2400 s)
  Flash         dry render: fence rendered, BATTERY GREEN, lifted. Live battery: TMPDIR identity OK, FENCE-OK, P-DELIVERY / P-PERSIST /
                P-ANYWHERE / P-SANDBOX yes, SERVED gemini-3.8-flash-high verdict OK, the egress row failing as it must ⇒ GREEN
  Pro           dry render GREEN; live battery: the client REFUSED the id: "model gemini-3.1-pro-high is not recognized". Its model
                list carries no Gemini 3.1 Pro. Nothing served, nothing spent. Last served on this lane 2026-09-28 (NA)
```
**RELEASED: the Flash half.** Its four conditions (WHT and NTT × {plain, salt-diet} × gemini-3.8-flash-high, 12 cells) fire under §WA2's
order, which already puts Flash first. Export **6413289d**; client **agy 1.5.9**; hand **gemini**; P3 on the agy pool, yielding to any O4
agy cell live or queued, /usage read at each fire and bank. `T-WA-F` (Flash · WHT · salt-diet#1) opens it, and the lead reads it before
Flash continues. Every §WA2 receipt: item 1 systems (offset 101,945,641), item 2 the lead (101,927,000), item 3 the lead (same post),
item 4 above.
**A CLIENT SEAM, declared beside §WA4 item 2:** NA and the Z wave ran on older agy clients; WA's cells run on 1.5.9. Nothing here compares
a WA cell with a cell from another client.
**THE PRO HALF IS HELD, NOT DECLARED.** §WA0 row 1 registers gemini-3.1-pro-high, and today's client cannot run it, so no Pro cell can be
what this file registered. Substituting another id (the Z wave's Pro-slot legs fired gemini-4-argon-high) changes a registered input and
what the block asserts about the agy lane's model set, so it is the Captain's word, put through the helm's pack. **DEFAULT, if no word
comes:** Pro's four conditions (12 cells) are reported NOT-FIRED(MODEL) by a census addendum, naming this addendum and the client's
refusal. The default asserts nothing about any Pro model. Not measured: whether the 1.4.10 binary still serves the id (gemini's limit).

---
## ⚖️ ADDENDUM 2 (2026-11-14, bench) — THE PRO SLOT IS RE-REGISTERED ON `gemini-4-argon-high`, WITH A MODEL SEAM. PRICED BEFORE ANY PRO CALL. APPENDED.
**Authority:** the Captain's council word of 2026-11-14 (ruling 3, recorded in the helm's council minute in the
private run record): *"WA's Pro slot: YES, as the rec"*, the rec being this re-registration. It replaces ADDENDUM 1's default (NOT-FIRED(MODEL)),
which therefore never fires.
**What changes:** §WA0 row 1's Pro id. `gemini-3.1-pro-high` (which today's client does not serve, ADDENDUM 1) is replaced by
`gemini-4-argon-high`, the id the Z wave fired in the Pro slot through 2026-10-24 (`AMENDMENT-ZF-gemini4-argon-2026-10-13.md`). Nothing
else in §WA0–§WA6 moves: the population (4 Pro conditions, 12 cells), the export 6413289d, the arms, the caps, the order (WHT → NTT, the
same per-problem cell order), the tripwire `T-WA-P` (Pro · WHT · salt-diet #1, read by the lead before Pro continues), P3 on the agy pool
yielding to any O4 agy cell live or queued, and the hand (gemini).
**⚖️ THE MODEL SEAM, declared:** a `gemini-4-argon-high` cell is never pooled, tabled beside or compared with any `gemini-3.1-pro-high`
result (block NA's, the pilot's, or any other). WA's Pro result is a result about argon on WHT and NTT, and its census line names argon.
§WA5 carries: nothing Claude-versus-agy, nothing Flash-versus-argon as models.
**THE PRICE, before the first Pro call.** §WA3 prices in the agy pool's own unit, and that unit did not move over the 12 Flash cells (the
hand read the pool at 100 % weekly at every fire), so no points-per-cell figure exists to scale. The lane's binding resource is cell wall,
so the price is stated there. Every figure is printed by `evidence/blockWA-2026-11-14/pro_price.py` from two tracked files
(`evidence/zf-result/zf-cells.tsv`, the Z wave's legs, and `evidence/blockWA-2026-11-14/cells.tsv`, WA Flash's cells):
```
Z gf-none plain: argon n 15 median wall 1099.9 s · flash n 15 median 478.0 s · ratio 2.301
Z gf-none salt-diet: argon n 12 median wall 1470.1 s · flash n 15 median 2006.5 s · ratio 0.733
Z gf-none plain, every harvested leg (wedges included): argon n 15 median 1099.9 s · flash n 15 median 478.0 s · ratio 2.301
Z gf-none salt-diet, every harvested leg (wedges included): argon n 15 median 1552.0 s · flash n 15 median 2006.5 s · ratio 0.773
WA WHT plain: Flash median wall 587.2 s · Pro price 3 x 587.2 x 2.301 = 4054 s
WA WHT salt-diet: Flash median wall 1487.2 s · Pro price 3 x 1487.2 x 0.733 = 3269 s
WA NTT plain: Flash median wall 614.1 s · Pro price 3 x 614.1 x 2.301 = 4239 s
WA NTT salt-diet: Flash median wall 1263.0 s · Pro price 3 x 1263.0 x 0.733 = 2776 s
Pro price, every leg: 14674 s = 4.1 h
Pro price, 12 cells: 14338 s of cell wall = 4.0 h; agy pool points per cell UNMEASURED (pool read 100 % weekly through all 12 Flash cells)
```
The salt-diet ratio excludes three argon FreeList salt-diet wedges (the Z wave's), which lowers argon's median; the every-leg line beside
it is the reading with them. Both rest on other problems (the Z wave's five), so the direction of error on WHT and NTT is unknown. The
first Pro triple (WHT) re-cuts it before NTT fires, as block W's did.
**BEFORE THE FIRST PRO CELL (the release conditions, in order):**
1. The lane-live battery (§WA2 item 4) on one dry argon cell on the release's client, by the hand: credential window, the served model
   (`gemini-4-argon-high`, and a mismatch VOIDS), fence intact, TMPDIR identity, the TREE-HASH line, and the client version and sha. If
   agy 1.5.9 does not serve argon, the Pro slot HOLDS and the lead writes the next addendum; nothing substitutes silently.
2. The agy pool read at that fire; a pool the hand's own O4 work needs comes first (P3).
3. `T-WA-P` fires alone and the lead reads it before Pro continues.
Nothing fires on Pro before a non-author has read this addendum.

---
## ⚖️ ADDENDUM 3 (2026-11-14, bench) — `T-WA-P`'s FIRST CELL IS NOT SCORED (A LANE FAULT); THE EXEBOX CERT PATH IS FIXED IN OUR OWN LAUNCHER, PER CELL. APPENDED.
**Why:** every cell on agy 1.5.9 meets the same transient on its first command: `open /tmp/claude/exebox-cert-<n>.crt: operation not
permitted` (counts from the hand's reads: the battery 3, `wawfs101` 1, `wanfs301` 1, `wawas101` 3; the F2 probe below 5). Flash and the
battery recovered by re-running the command. In `wawas101` (`T-WA-P`, argon · WHT · salt-diet #1) argon instead asked to bypass the
sandbox, the PreToolUse hook denied that, and argon then ran 0 commands in 5 turns.
**1. `wawas101` is NOT-SCORED(HARNESS).** Its receipts are kept and it enters no denominator. Both causes belong to the lane: the
cert-path transient (§2 shows it is our launcher's), and the harness's denial text, which turned a recoverable transient into a stop. So
the cell measures the lane and not argon on WHT. It is replaced by ONE re-fire under block N ADDENDUM 13's `r<k>` form, `wawas1r1`, in a
fresh root, after release conditions 1–4 below. It is still `T-WA-P`, and the lead reads it before Pro continues. A BUILD-FAIL score was
rejected, because no command was ever attempted: that score would grade the harness's words, not the subject's code.
**2. The cause, read from the code and the cells' own files** (the hand, 2026-11-14, no spend):
- `agy_launch_v3.sh`'s client wrapper sets `CLAUDE_CODE_TMPDIR` to the cell's tmp on the sandbox-runtime arm. Only the battery and the
  non-turn-loop launch use that wrapper.
- A live cell runs the turn loop. `do_launch` writes `ctl/agy-turnloop-env-<phase>.json` from `HOME`, `PATH`, `TMPDIR` and the
  toolchain variables only, and `agy_turnloop_v3.py` passes that JSON as the WHOLE environment of the sandbox runtime.
- The runtime therefore never sees `CLAUDE_CODE_TMPDIR`, and it gives its child its default, `TMPDIR=/tmp/claude`. That path does not
  exist on the run box (F2 read it absent before and after).
Measured on the run box: F2's cell and `wawas101` each carry "TURN LOOP ON", a battery wrapper line WITH the variable, and an env JSON
with 0 occurrences of it. The F2 probe (2026-11-14 22:51–22:58Z, one argon battery turn) saw `TMPDIR=/tmp/claude` and no
`CLAUDE_CODE_TMPDIR` in the model's shell. **The drop is in our launcher, not in the client.**
**3. The fix (arm L): on the sandbox-runtime arm only, the turn-loop env JSON carries `CLAUDE_CODE_TMPDIR` set to the cell's tmp**, the
value the client wrapper already passes. Nothing else moves: no `/tmp/claude` is created, and no fence, hook text or other lane changes.
The rejected arm was F1, a fresh box-global `/tmp/claude` per agy cell. It is a cross-cell channel that needs a quiet box (about 4 h with
no Claude cell on the run box, from ADDENDUM 2's price), and its write allowance does not open the path while an ancestor stays in the
deny list (the hand's zero-spend probe).
The hook's denial text does NOT change: Flash's 12 cells ran under it, and changing it now would move a treatment input between the two
models. If L removes the transient, the denial is never reached.
**⚖️ AN ENVIRONMENT SEAM, declared beside ADDENDUM 2's model seam:** WA Flash's 12 cells ran with the subject's shell `TMPDIR` at
`/tmp/claude`, a path that did not exist, and they met the transient. WA Pro runs with it at the cell's tmp. §WA5 already carries
nothing Flash-versus-argon, and this is one more reason.
**⚠️ A LIMIT ON EARLIER agy RESULTS, stated here and not yet measured:** levels 6–8 and WA Flash ran the same turn-loop env under the
sandbox runtime, so their subjects' shells presumably saw `TMPDIR=/tmp/claude` too. Not measured: per cell, whether that path ever
existed while the cell was live, and whether any command in it used `TMPDIR`. The one known instance of the path existing: the hand
created it for about 30 s at 21:30:56Z on 2026-11-14 while one Claude cell was live (empty when read before removal). A census is owed
before any of those results is quoted with a claim that rests on the subject's temporary files.
**BEFORE `wawas1r1` (the release conditions, in order; ADDENDUM 2's three still stand):**
1. The launcher change (arm L) with a RED arm: the turn-loop env JSON on the sandbox-runtime arm lacking the variable FAILS.
2. **RED FIRST, then green, on one dry argon battery cell run through the TURN LOOP:** the transient reproduced without L (F2 is that
   receipt, 5 failures), then the same battery with L shows 0 `exebox-cert` failures, the shell's `TMPDIR` equal to the cell's tmp, and
   ADDENDUM 2's battery lines green.
3. The scorer defect named by the hand (`agy_shell_count_v3.py` counts a DONE step with no error field as a working shell, while client
   1.5.9 reports a failed start in the step's OUTPUT) is fixed with a RED fixture before any argon cell is scored. WA Flash's result does
   not cite that column.
4. A non-author has read this addendum.
**Not established:** why a re-run succeeds. If 1–2 do not remove the transient, Pro HOLDS and the lead writes the next addendum.
**THE EXPORT AND THE ID THE PRO HALF RUNS ON.** Pro fires on export **3796e6b4**, not ADDENDUM 1's 6413289d. It is 6413289d plus two commits
(01d59f84, the scorer fix of condition 3; 3796e6b4, arm L), and `git diff --stat 6413289d 3796e6b4` names four harness files only:
`agy_client_env_v3.py` (new), `agy_launch_v3.sh`, `agy_shell_count_v3.py`, `selftest_all_v3.sh`. No task, card, suite or treatment file
moves, so the subject sees the same problem and arms. The lead read the launcher diff and the new helper: the variable is added on the
sandbox-runtime arm only and refused on the others. The agy lane forms a cell id as a prefix plus a two-digit rep, so `wawas1r1` is
fired as cell id **`wawas1r01`** in a fresh root, and its receipts write "wawas1r1 (cell id wawas1r01)".
**Condition 2, MET (recorded, not a release):** one dry argon battery `waL01` on export 3796e6b4 through the turn loop (the hand,
2026-11-15 00:55–01:00Z, client 1.5.9 at its pinned sha): 0 `exebox-cert` failures in the stream against F2's 5 on the same treatment;
0 failed starts; the shell's `TMPDIR` and `CLAUDE_CODE_TMPDIR` both the cell's tmp; battery return codes as F2's; the fence intact; served
`gemini-4-argon-high`; the fixed scorer counts 10 commands made, 10 succeeded; `/tmp/claude` absent before and after. Limit: one turn of
the battery treatment, not argon on WHT.
**Condition 4, MET: a non-author read** by kent (2026-11-14 19:37 PST, bus offset 102,997,856), at head 04a66d13 and blob 15b2a412,
with saltbench-systems at 3796e6b4. A FINDING, not a signature. Every claim checked holds: append-only; four harness files; the cause
read from the code; §1's exclusion and the limit are visible. Both new arms go RED under a mutant (the srt rule disabled: 8/10; the
failed-start test removed: 17/19, red on `wawas101`'s shape). Three limits, recorded:
- (1) the failed-start parser reads only the first line after the step header, so a blank line there would read as a success. An arm
  for that shape is owed BEFORE `wawas1r01` is scored. It is not owed before the fire.
- (2) the last link of the cause, the sandbox runtime's default, rests on the launcher's comment citing the vendor's file, plus the
  measured contrast (0 against 5, one battery turn each).
- (3) the rest of the launcher and the turn loop was not read beyond the changed lines.
**Pro is RELEASED for `T-WA-P` = `wawas1r01` ALONE** on export 3796e6b4. The lead reads it before Pro continues.
