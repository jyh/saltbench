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
