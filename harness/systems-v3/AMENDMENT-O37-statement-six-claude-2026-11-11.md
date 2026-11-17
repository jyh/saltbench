# AMENDMENT — O37 BLOCK T: BLOCK N's SIX PROBLEMS × `statement`, GREENFIELD, CLAUDE LANE. FROZEN BEFORE THE FIRST CALL
## bench (SaltBench lead), 2026-11-11. The form is block N's, `AMENDMENT-O37-nine-greenfield-claude-2026-09-25.md` (signed; ADDENDA 1–14),
## cited below as "block N", carried BY CITATION; the statement arm is the pilot's (`AMENDMENT-statement-arm-pilot-2026-09-09.md`, with its
## ADDENDUM 1: the sections are EXTRACTED, not authored), cited as "the statement arm". A clause that differs from either says so and why.
## Authority: block N's (the Captain's council word of 2026-09-25: the remaining problems run on bench at P3).
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ **NO CELL IS BUILT, LET ALONE FIRED, BEFORE THE CAPTAIN HAS READ THE SIX STATEMENTS**
## (the statement arm §2), **AND NO CELL FIRES BEFORE A RELEASE ADDENDUM NAMES THE EXPORT SHA, THE POOL, AND EACH §T2 RECEIPT AS MET.**

---

## §T0 · THE INPUTS (block N §N0, row by row)
```
  1  MODEL IDs   claude-opus-5 · claude-sonnet-5, block N row 1 unchanged. Re-measured served at release by a zero-cell probe.
  2  n           3 per condition.
  3  POPULATION  24 conditions, 72 cells (§T1).
  4  EXPORT      ONE bare-master sha of saltbench-systems carrying (i) the six `## Statement` sections at the blobs §T2 item 1 names and
                 (ii) every block-N export (6087b54, 23485e5) as an ancestor. ⚠️ At this writing the sections are on branch
                 bench/o37-statements-2026-11-11 (head 8bf04bdc, base 3ea54f5, the LZW export), not on master.
  5  CLIENT PIN  block N row 5, re-driven at release.
  6  TASK TREE   the EXPORT's tasks/systems-v3, and nothing else. Every cell is built with `cell_build.py --statement`.
  7  CAPS        block N row 7 unchanged: C1_USD $37.21, W1_SEC 144,000; CAP-COST and CAP-WALL armed.
  8  ACCOUNT     P3: a pool the PM names at release, never ahead of P1/P2 work, `cells_account_check.sh` OK before each fire.
  9  FIRE ORDER  §T3.
```

## §T1 · THE POPULATION — 24 CONDITIONS, 72 CELLS
```
  problems   Luby · AES · Liveness · MaxFlow · BinomialHeap · LinearScan     block N's six
  models     claude-opus-5 · claude-sonnet-5
  arms       plain+statement · salt-diet+statement                           the statement arm's (d) and (e)
  field      greenfield            extras   statement
  ⇒ 6 × 2 × 2 = 24 conditions · × n 3 = 72 cells
```
Of O37's 216 (census ADDENDA 28 and 39): 48 DONE, 24 DECLARED (LU), and these 24 are 24 of the 96 statement and spec-change conditions on
the six. The agy lane's 24 statement conditions are a sibling freeze. Spec-change on the six is a later block (their `B/` trees are built
and await reads).

## §T2 · ⛔⛔ THE ITEMS — EACH DRIVEN, WITH A CONTROL, BEFORE THE CELLS IT GATES
1. **THE SECTIONS REPRODUCE FROM THE TOOL** (the statement arm A1.2 item 2). Each section is the output of
   `extract_statement_v3.py <ref> --names <verify.names> --interface <interface.rs> --check --carry-consts` on the export's own reference;
   the release re-derives all six and `cmp`s them against the cards. `--carry-consts` is ⚖️ **A DEPARTURE**, declared: three statements
   (AES: SBOX, INV_SBOX · Liveness: FUEL · LinearScan: FUEL, MAX_BLOCKS, MAX_INSTRS, MAX_VREG) index constants of the reference, and a
   statement its reader cannot evaluate is not a statement; the flag carries each definition verbatim and every line stays a source line.
   The two extractor commits that make this possible (628e0e1a, 17857827) need a non-author read before release.
2. **THE CAPTAIN HAS READ ALL SIX** (the statement arm §2). His word is recorded in the release.
3. **SIZES, RECORDED** (the statement arm A1.2 item 4), card bytes before → after, and the section's own bytes:
   ```
     Luby          9,300 → 16,037   section  6,737        Liveness   9,258 → 19,046   section  9,788
     AES           7,252 → 17,506   section 10,254        MaxFlow   10,234 → 15,686   section  5,452
     BinomialHeap  7,743 → 15,586   section  7,843        LinearScan 9,031 → 26,242   section 17,211
   ```
   A treatment that varies three-fold in size across problems is a fact the reading carries.
4. **NEUTRALITY ON A BUILT VIEW PER PROBLEM AND ARM**: the cell build's own gate. Driven 2026-11-11 on the run box at 8bf04bdc: 12 dry
   cells, all rc 0, zero hits; a planted "theorem" in Luby's section REFUSED (2 hits). Re-driven at the export.
5. **THE ACCOUNT CHECK, NO LEAK INTO A VIEW, THE ZERO-CELL PROBE** — block N §N2 items 2–3 and block W §W2 item 5, unchanged.

## §T3 · THE ORDER, THE TRIPWIRES
Block N §N3's problem order (Luby → AES → Liveness → MaxFlow → BinomialHeap → LinearScan) and cell order, models interleaved (block N
ADDENDUM 10). Tripwires: `T-T-O` = Opus · Luby · salt-diet+statement#1 · `T-T-S` = Sonnet · the same. Each is read and posted before its
model continues; the reading list is block N §N3's, plus one line: did the subject use, ignore, or contradict the statement.

## §T4 · CAPS, PREDICTIONS AND THE PRICE — REGISTERED BEFORE ANY DATA
Caps: block N §N4. Predictions, per model, where a miss is a result: (i) within a condition, salt-diet+statement's CAP-COST incidence is ≥
plain+statement's; (ii) CAP-WALL binds no cell. No prediction about pass rate or premium.
**The price**: block N's own spend on the same six problems with `extras = none` (`evidence/claude-lane-blockN-2026-09-28/blockNO-cells.tsv`
and `blockNS-cells.tsv`, `final_COST` summed): Opus $671.00 · Sonnet $582.64 = **$1,253.64 for 72 cells**. That is the estimate; its direction
is unknown (a statement may shorten the salt arm's specification work or lengthen the plain arm's reading). Ceiling **72 × $37.21 = $2,679.12**,
plus each cell's overrun past the cap. The Luby sextet re-cuts the price before AES fires.

## §T5 · CONFOUNDS — block N §N5 items 2–3, plus the statement arm's own
1. **THE STATEMENT ARM IS A STRONGER TREATMENT BY CONSTRUCTION** (the statement arm A1.2 item 1): a formal specification derived verbatim
   from the withheld reference. The (d)/(e) comparison is within it, where both arms get it. It is not a fence leak.
2. **THE REFUTER'S CATCH AND THE PLANTED-AMBIGUITY INSTRUMENT ARE OFF BY CONSTRUCTION** in every cell built with a statement, as each
   section's own comment says. No ambiguity score from this block is read as one.
3. **CARRIED CONSTANTS** (§T2 item 1) make three sections larger than the extraction alone; AES's carries two 256-entry tables.

## §T6 · READING RULES, §T7 · VOIDS, §T8 · WHAT THIS BLOCK CANNOT ESTABLISH
§T6 = block N §N6 (every premium registered UNRESOLVED-UNDERPOWERED). §T7 = block N §N7, row 11 included, plus: **a cell built from a
section that does not `cmp` equal to the tool's re-derivation is VOID** (the statement arm A1.2 item 2).
§T8: 1. No magnitude, no effect size. 2. Nothing about Opus versus Sonnet. 3. Nothing about the statement arm versus `extras = none`
across blocks: the two blocks ran months apart, on different exports and pools, and that contrast is not registered here.

## §T9 · WHAT THE HAND DELIVERS
Block N §N9, plus the per-cell answer to §T3's extra line. A result of record per model, the census's O37 section re-cut in the same commit.
Any public sentence, and any claim about the method, is the Captain's.

---
# ✍️ SIGNED — the helm (208th head), 2026-11-11 00:43 PST, bus offset 100,181,456: blob 9243186c4238 at head 30beb4bfcade, read whole
(85 lines), WITH LIMITS. Checked by arithmetic: 6 × 2 × 2 = 24 conditions × n 3 = 72 cells; T's 24 of the O37 ledger's 96 statement and
spec-change conditions on the six; the price $671.00 + $582.64 = $1,253.64 and the ceiling 72 × $37.21 = $2,679.12. Every departure is
declared where a signer meets it (--carry-consts, the VOID row, the stronger-treatment and off-instrument confounds, §T8.3). Not checked:
block N's machinery carried by citation; the price tables' rows (the sums were checked, not the cells files); the extractor commits
628e0e1a and 17857827; the statement sections themselves; the model ids' served state (the zero-cell probe's job). Signature is not release.

---
# ADDENDUM 1 (2026-11-17, bench) — RELEASE, ⛔ DRAFT: NOT A RELEASE UNTIL ITEM 5's ACCOUNT CHECK AND ZERO-CELL PROBE ARE FILLED AND THE POOL IS NAMED
**Export: saltbench-systems `7fe4ff7f`** (branch `bench/o37-T-export-candidate-2026-11-17`, backup) = the block WC candidate 74b1e0b4 (which
holds the block T stager 09516b81, itself on the line of every block-N export) + two harness fixes by systems taken at this re-cut, not
mid-block: ae969557 (the box reader treats NBSP after the prompt glyph as whitespace in every locale) and ba46e212 (cell-watch reaps the
client's descendants at end_session). Against 09516b81: `tasks/systems-v3` (tree e2cbc84c), `referee_v3.py`, `check_withheld_leak_v3.py`,
`extract_statement_v3.py`, `cell_build.py` and `neutrality_grep.py` are byte-identical; `clb_stage.sh` and `clb_fire.sh` are byte-identical
to 74b1e0b4's. Ancestors include 6087b54, 23485e5, 8bf04bdc, 628e0e1a, 17857827 and 0c57f378. ⚖️ **A DEPARTURE FROM §T0 row 4, declared:**
the export is not on bare master (block N's exports are not on master; block W's ADDENDUM 1 states the same departure).
On the run box by `studio_export.sh --no-toolchain`: 423 files, listing sha256/16 92407c849ee2ab58, withheld-shaped names 0 in the listing
and 0 on the host, marker written last. ⚠️ **Two earlier T cuts are recorded and were never used:** the 11-15 cut of 09516b81 and a first
cut of 7fe4ff7f were taken by `git archive` of the whole task tree (1,142 and 1,144 files, 650 withheld-shaped), not by the exporter; both
were moved into a fenced scratch directory on the run box on 2026-11-17 and no cell was staged or fired from either. Driven the same day,
the block T stager REFUSES both (rc 3, "the export's task tree carries withheld material") and stages from the clean cut (rc 0, dry).
**Signature:** the helm's, above. **Item 2** (his read of the six): MET, council 2026-11-14 ruling 6, "O37 accepted", at 8bf04bdc's sections,
"block T is RELEASED to build", each launch under its pool's day-line gate.
**§T2 receipts:**
1. MET 2026-11-17, locally at 7fe4ff7f: each of the six sections re-derived with the command its card names (`extract_statement_v3.py …
   --check --carry-consts`), rc 0, and the card's ```rust block `cmp` EQUAL in 6 of 6 (bytes: Luby 5,436 · AES 8,881 · Liveness 8,430 ·
   MaxFlow 4,140 · BinomialHeap 6,543 · LinearScan 15,813). Control: the same comparison on a one-byte mutant of Luby's output reads
   DIFFER. The extractor commits' non-author read: systems, CONCUR for the six as built (STATUS-systems row 151, bus offset
   101,803,062, 2026-11-13 19:18), and its read of the extractor fix 0c57f378, CONCUR (bus offset 101,831,547, 19:50).
3. Sizes: §T2 item 3's table stands; the six task trees are unchanged since 09516b81.
4. MET 2026-11-17 on the run box at the clean export: 12 dry cells (the six × plain, salt-diet) built by `cell_build.py --statement` into a
   scratch cells root, all rc 0, neutrality "zero hits" 12 of 12; REQUIREMENTS.md identical across the arms but for the work-order nonce
   line. Control: a copy of the export with one planted line `// theorem: planted` inside Luby's section REFUSED in both arms (2 hits, rc 4).
5. NO LEAK — MET: `check_withheld_leak_v3.py` CLEAN, 343 identifiers across 13 tasks, every positive control fired, 0 in any view.
   THE ACCOUNT CHECK — ⛔ OPEN: owed on the pool the PM names (§T0 row 8, P3). THE ZERO-CELL PROBE — ⛔ OPEN: owed on that pool's client.
**Roots:** created 2026-11-17 18:08Z on the run box in a quiet window (no client, watcher, fire, verus or cargo process): `clb_stage.sh
--roots --freeze T` from the clean export, rc 0, 24 roots with `_bin` linked into 7fe4ff7f, each root's model table read back (12 Opus,
12 Sonnet, equal to the registered 24).
**Pool:** ⛔ OPEN (the PM's cut). **Order:** §T3 as registered. Nothing fires before this heading loses its DRAFT mark.
