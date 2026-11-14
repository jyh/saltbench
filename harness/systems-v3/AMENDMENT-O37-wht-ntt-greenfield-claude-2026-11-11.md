# AMENDMENT — O37 BLOCK W: WHT AND NTT, GREENFIELD × `none`, CLAUDE LANE. FROZEN BEFORE THE FIRST CALL
## bench (SaltBench lead), 2026-11-11. The form is block N's, `AMENDMENT-O37-nine-greenfield-claude-2026-09-25.md` (signed; ADDENDA 1–14),
## cited below as "block N", and it CARRIES block N's machinery BY CITATION exactly as block N carries lane B's. A clause below that differs
## from block N says so, and says why. The authority is block N's: the Captain's council word of 2026-09-25 (the remaining problems run on
## bench at P3, on quota no higher-priority work needs) and his standing objective "fill out the 14 problems (greenfield only)".
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ **NO CELL FIRES BEFORE §W2's ITEMS ARE DRIVEN AND A RELEASE ADDENDUM NAMES THE EXPORT SHA,
## THE POOL, AND EACH §W2 RECEIPT AS MET.** Signature and release are two acts, as in block N.

**Why now.** Census ADDENDUM 39 declared LU NOT FEASIBLE as a Rust port (the Captain's council word of 2026-11-10, ask 3). Of the three
problems block N §N1 left out for having no v3 rung, WHT and NTT now have one, built on the systems lane on 2026-11-10. This block is
their greenfield × `none` slice on the Claude lane.

---

## §W0 · THE INPUTS (block N §N0, row by row)
```
  1  MODEL IDs     claude-opus-5 · claude-sonnet-5, block N row 1 unchanged (the served set per condition as there). Both ids were
                   last measured served on 2026-11-09 (AMENDMENT-O37-aeneas-lzw-2026-11-09.md ADDENDUM 2, receipt 5); the release
                   re-measures them with a zero-cell probe, because a served id is a reading of a day, not a property.
  2  n             3 per condition.
  3  POPULATION    8 conditions, 24 cells (§W1). Nothing is added, dropped or substituted.
  4  EXPORT        ONE bare-master sha of saltbench-systems, named in the release addendum, that (i) carries WHT and NTT at the blobs
                   §W2 item 1 drove and (ii) descends from every export block N released on (6087b54 and 23485e5), so every block-N
                   and lane-B build item is present. One sha for all 24 cells, recorded per cell. ⚠️ At this writing neither task
                   is on master: each is on its own systems-lane branch (WHT head 921a3b35, NTT head 9179f45a).
  5  CLIENT PIN    block N row 5 (lane B §Q0 row 5): the versioned client by absolute path, its sha asserted per launch. The release
                   names the version and re-drives the zero-cell probe on it.
  6  TASK TREE     the EXPORT's own tasks/systems-v3, and nothing else.
  7  CAPS          block N row 7 unchanged: C1_USD $37.21 (cost_caps.tsv), W1_SEC 144,000; CAP-COST and CAP-WALL armed.
  8  ACCOUNT       ⚖️ THE CHANGE FROM BLOCK N: P3 — a pool the PM names for this block at release, from the day lines, never ahead of
                   P1/P2 work, named per cell with `cells_account_check.sh --expect <that pool's identity>` reading OK before each fire
                   (block N row 8's check, unchanged). Block N's run-box window has long closed.
  9  FIRE ORDER    §W3, one cell per pool dir, pairs kept whole; a tripwire cell opens each model.
```

## §W1 · THE POPULATION — 8 CONDITIONS, 24 CELLS
Derived, not typed. O37's population is 216 conditions (census ADDENDUM 28 §AG1). After census ADDENDUM 39 it stands 48 DONE, 24
DECLARED (LU), 48 for NTT and WHT, and 96 statement and spec-change conditions on block N's six. This block takes:
```
  problems   NTT · WHT                       the two with a v3 greenfield rung built 2026-11-10 (systems lane)
  models     claude-opus-5 · claude-sonnet-5  the Claude lane (the agy half is a sibling freeze)
  arms       plain · salt-diet
  field      greenfield            extras   none
  ⇒ 2 × 2 × 2 = 8 conditions · × n 3 = 24 cells
```
**What is NOT in this block:** NTT and WHT × {statement, spec-change} on the Claude lane (16 conditions; no `## Statement` section and no
`B/` tree yet; each card carries a drafted change request, sequency for WHT and negacyclic for NTT), and the agy lane's 24 (a sibling
freeze). Each is a later dated block, written before its own first call.

## §W2 · ⛔⛔ THE BUILD ITEMS — EACH DRIVEN, WITH A CONTROL, BEFORE THE CELLS IT GATES
1. **THE TWO TASKS ARE RE-DRIVEN BY A NON-BUILDER, ON THE EXPORT'S BYTES** — block N §N2 item 1 (a)–(d), unchanged. ⚖️ **THE CHANGE FROM
   BLOCK N: the lead BUILT both tasks, so the lead may not be the re-driver.** The release names the seat that re-drove, and its table.
   The builder's own figures, for the re-driver to reproduce or refute (systems lane, the two branches above):
   ```
     task  reference lines  Verus (reference)        tests: plain · treatment · trivial   mutants failing   own traces  NEG traces
     WHT   816              47 verified, 0 errors     11/11 · 11/11 · 11/11               5/5 (trivial 0/5)  11/11       11/11
     NTT   924              67 verified, 0 errors     11/11 · 11/11 · 11/11               5/5 (trivial 0/5)  11/11       11/11
   ```
   A task whose drive disagrees with these on any of (a)–(d) is WITHDRAWN from this block by name, its conditions reported as
   NOT-FIRED(TASK), and the population shrinks by an addendum, never silently.
2. **THE CARD READS LAND FIRST.** Each card had a non-author read asked on 2026-11-10 (the systems lane's queue). A finding that changes a
   card changes its task, so item 1 runs on the card as read.
3. **THE REFEREE ON A DRY CELL PER TASK** — the harness's own `referee_v3.py` on a dry cell of the reference (salt and plain) and of a mutant,
   as the builder drove it on 2026-11-10 (reference PASS both arms, mutant TESTS_FAIL), re-driven on the export. The builder's drive found
   both tasks' ambiguity rubrics miscalibrated and recalibrated them; the release states the rubric blobs it drove.
4. **THE ACCOUNT CHECK** and **NO LEAK INTO A VIEW** — block N §N2 items 2 and 3, unchanged.
5. **THE ZERO-CELL PROBE** — one `-p` turn per model on the release's client, its `message.model` set read exactly (the LZW release's
   receipt 5). It costs cents and catches a retired id before a cell spends on it.

## §W3 · THE ORDER, THE TRIPWIRES
```
  models    interleaved, block N ADDENDUM 10's form; Opus's tripwire first.
  problems  WHT → NTT (ascending reference size, 816 · 924)
  cells     per problem: plain#1 · salt-diet#1 · plain#2 · salt-diet#2 · plain#3 · salt-diet#3
```
Tripwires, each ONE cell, read by the lead and posted before its model continues: `T-W-O` = Opus · WHT · salt-diet#1 · `T-W-S` =
Sonnet · WHT · salt-diet#1. The reading list is block N §N3's.

## §W4 · CAPS, PREDICTIONS AND THE PRICE — REGISTERED BEFORE ANY DATA
Caps: block N §N4, unchanged. A cap-out is a RESULT and enters its median at the cap. No cap is raised.
Predictions, per arm and model, where a miss is a result: (i) within a condition, salt-diet's CAP-COST incidence is ≥ plain's; (ii) CAP-WALL
binds no cell. ⛔ No prediction about pass rate or premium: neither problem has run on any lane.
**The price**, from block N's own tables of record (`evidence/claude-lane-blockN-2026-09-28/blockNO-cells.tsv`, `blockNS-cells.tsv`,
`final_COST`, which includes the harness's sandbox probe, as those files' headers say):
```
  model   block-N median per cell (36 cells)   Luby median · AES median (the references bracketing 816 and 924 lines)
  Opus    $15.82                               $13.89 · $15.12
  Sonnet  $13.41                               $12.11 · $9.24
  estimate  12 Opus cells × ~$15 + 12 Sonnet cells × ~$12 ≈ $324     ceiling  24 × $37.21 = $893.04, plus each cell's overrun past the cap
```
The estimate is a reading of other problems and its direction of error is unknown. The WHT triple re-cuts it before NTT fires, as block
N's Luby triple did.

## §W5 · CONFOUNDS — block N §N5 items 2 and 3 carried, item 1 restated
1. **NEW PROBLEMS, ONE AUTHOR, WHO IS ALSO THE LEAD.** WHT and NTT were ported from Lean v1 by bench, the lead of this block, on 2026-11-10.
   §W2 item 1's non-builder re-drive is the control on that. A defect in a new task is a HARNESS finding, never an arm effect.
2. **NTT's REFERENCE PROVES LESS THAN WHT's.** WHT's reference proves its round trip; NTT's checker matches the card's sums exactly, but its
   butterfly is not proved equal to the sums (priced and deferred on 2026-11-10). This touches no cell's score (the suite scores the
   submission), and it is printed beside any table that sets the two problems side by side.

## §W6 · READING RULES, §W7 · VOIDS, §W8 · WHAT THIS BLOCK CANNOT ESTABLISH
§W6 = block N §N6 (every premium registered UNRESOLVED-UNDERPOWERED). §W7 = block N §N7, row 11 included.
§W8: 1. No magnitude and no effect size. 2. Nothing about Opus versus Sonnet as models. 3. Nothing about the 208 O37 conditions outside
§W1. 4. Nothing about LU: these are the two of the three that were judged feasible, which is a selection, declared here.

## §W9 · WHAT THE HAND DELIVERS
Block N §N9, unchanged: a result of record per model, with the census's O37 section re-cut in the same commit. Any public sentence, and any
claim about the method, is the Captain's.

---
# ✍️ SIGNED — the helm (208th head), 2026-11-11 00:43 PST, bus offset 100,181,456: blob d00177a07117 at head b51d6ba6834c, read whole
(108 lines), WITH LIMITS. It checked by arithmetic 8 conditions × n 3 = 24 cells, the O37 ledger's 216, the estimate $324 and the ceiling
$893.04. Not checked: block N's machinery carried by citation; the builder figures in §W2 item 1 (the re-driver's job); the price tables'
rows; the extractor commits; the model ids' served state (the zero-cell probe's job). Signature is not release.

---
# ADDENDUM 1 (2026-11-13, bench) — RELEASE, ⛔ DRAFT: NOT A RELEASE UNTIL ITEMS 4a AND 5 ARE FILLED AND THE POOL IS NAMED
**Export: saltbench-systems `0916ef9a`** = the export candidate 6615a7f8 (3ea54f5 + WHT 36417e31 + NTT 7573e701) + the block W stager
(clb_stage/clb_fire/clb_harvest learn `--freeze W`, blocks WS/WO, roots 8; fixture `clb_blockW_selftest.sh` 13/13, RED on 6615a7f8 on its
7 W arms). Against 6615a7f8 only those four harness files differ: `tasks/` (c6fbed80), `referee_v3.py` (37610865) and
`check_withheld_leak_v3.py` (d8e37b8e) are byte-identical, so items driven on 6615a7f8 hold for this export.
**§W2 receipts:**
1. MET — re-driven by systems, who built neither task (on 6615a7f8, bus offset 101,903,529): WHT and NTT match the builder's table
   on (a)–(d), every column; neither withdrawn.
2. MET — the card reads (systems lane, landed before item 1; findings taken on the task branches before the export was cut).
3. MET — `referee_v3.py` on dry cells of 6615a7f8 (run box `~/bench-dry/w-export-refdry-2026-11-13/`, archive sha256/16
   84b1e1526c77a493): reference PASS 11/11 in the salt and plain arms for both tasks; mutants DivideFirst TESTS_FAIL 9/11 and OwnRoot
   TESTS_FAIL 7/11. Rubric blobs driven: WHT cf343b86, NTT a2f69fee.
4. (b) NO LEAK — MET on 6615a7f8 (same checker and tasks/ bytes as 0916ef9a): CLEAN, 244 identifiers across 13 tasks, every control fired.
   (a) THE ACCOUNT CHECK — ⛔ OPEN: owed on the pool the PM names (§W0 row 8, P3).
5. THE ZERO-CELL PROBE — ⛔ OPEN: owed on that pool's client.
**Pool:** ⛔ OPEN (the PM's cut). **Order:** §W3 as registered. Nothing fires before this heading loses its DRAFT mark.
