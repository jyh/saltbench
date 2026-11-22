# AMENDMENT — O37 BLOCK TW: WHT AND NTT × `statement`, GREENFIELD, CLAUDE LANE. FROZEN BEFORE THE FIRST CALL
## bench (SaltBench lead), 2026-11-22. The form is block T's, `AMENDMENT-O37-statement-six-claude-2026-11-11.md` (signed; ADDENDA 1–5;
## its result of record `RESULT-claude-blockT{O,S}-2026-11-22.md`), cited below as "block T", carried BY CITATION. The two problems are
## block W's, `AMENDMENT-O37-wht-ntt-greenfield-claude-2026-11-11.md` (signed; its result of record `RESULT-claude-blockW{O,S}-2026-11-15.md`),
## cited as "block W". A clause that differs from either says so and why.
## Authority: block N's (the Captain's council word of 2026-09-25: the remaining problems run on bench at P3), as block T's.
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ **NO CELL IS BUILT BEFORE THE CAPTAIN HAS READ THE TWO STATEMENTS** (the statement
## arm §2; his council 2026-11-14 ruling 6 read block T's six, not these two), **AND NO CELL FIRES BEFORE A RELEASE ADDENDUM NAMES THE
## EXPORT SHA, THE POOL, AND EACH §TW2 RECEIPT AS MET.**

---
## §TW0 · THE INPUTS (block T §T0, row by row)
```
  1  MODEL IDs   claude-opus-5 · claude-sonnet-5, block T row 1 unchanged. Re-measured served at release by a zero-cell probe.
  2  n           3 per condition.
  3  POPULATION  8 conditions, 24 cells (§TW1).
  4  EXPORT      ONE bare-master sha of saltbench-systems, cut by a studio_export.sh that writes the listing marker, carrying (i) the
                 WHT and NTT `## Statement` sections at the blobs §TW2 item 1 names, (ii) block T's export 7fe4ff7f as an ancestor,
                 (iii) the stager's export-marker check (saltbench-systems 6d852677, the lead's queue row 8, a non-author read owed),
                 and (iv) the watcher's exit-wait beat (systems' 1eba956e, row 9). A DEPARTURE from block T's export, declared: (iii)
                 and (iv) are harness changes since 7fe4ff7f; neither touches tasks/, the referee, the leak checker or the builder.
  5  CLIENT PIN  block T row 5, re-driven at release. ⚠️ A client past 2.1.259 sets "idleCompaction": false in cell settings (the lead's
                 ruling of 2026-11-20, bus offset 107,406,746): declared at release with its schema probe, if the pin moves.
  6  TASK TREE   the EXPORT's tasks/systems-v3, and nothing else. Every cell is built with `cell_build.py --statement`.
  7  CAPS        block T row 7 unchanged: C1_USD $37.21, W1_SEC 144,000; CAP-COST and CAP-WALL armed.
  8  ACCOUNT     P3: a pool the PM names at release, never ahead of P1/P2 work, `cells_account_check.sh` OK before each fire.
  9  FIRE ORDER  §TW3. Every fire through the lead's local gate (refuses in a sitting on the box where the helm sits).
```

## §TW1 · THE POPULATION — 8 CONDITIONS, 24 CELLS
```
  problems   WHT · NTT                                                         block W's two
  models     claude-opus-5 · claude-sonnet-5
  arms       plain+statement · salt-diet+statement                             the statement arm's (d) and (e)
  field      greenfield            extras   statement
  ⇒ 2 × 2 × 2 = 8 conditions · × n 3 = 24 cells
```
These are 8 of the 24 WHT/NTT conditions the census lists NOT DONE (`CENSUS-full-matrix-2026-09-14.md` ADDENDUM 49 §AT2: "x statement,
both lanes; x spec-change, agy lane"). The agy lane's 8 WHT/NTT statement conditions are a sibling's to freeze.

## §TW2 · ⛔⛔ THE ITEMS — EACH DRIVEN, WITH A CONTROL, BEFORE THE CELLS IT GATES
1. **THE SECTIONS REPRODUCE FROM THE TOOL** (block T §T2 item 1). Each section is the output of `extract_statement_v3.py <ref> --names
   <verify.names> --interface <interface.rs> --check --carry-consts` on the export's own reference. The release re-derives both and `cmp`s
   them against the cards. Measured on the T export candidate (7fe4ff7f) at this writing: neither section carries a constant, and the
   cards say the extractor with and without `--carry-consts` produces byte-identical output for both.
2. **THE CAPTAIN HAS READ BOTH** (the statement arm §2). ⛔ OPEN: his read of block T's six does not cover these. His word is recorded in
   the release.
3. **SIZES, RECORDED** (block T §T2 item 3). The section's own bytes (the `rust` block under the card's `## Statement`, T export candidate):
   ```
     WHT   card.md 11,620 B · section 3,466 B · 20 spec fns · contracts of wht, iwht, check_trace
     NTT   card.md 12,328 B · section 3,286 B · 18 spec fns · contracts of ntt, intt, cyclic, check_trace
   ```
   The rendered card's bytes before and after `--statement` are recorded at the release from the built view. Both sections are about a
   third the size of block T's smallest (MaxFlow's 4,140 B rust block) and carry no constant.
4. **NEUTRALITY ON A BUILT VIEW PER PROBLEM AND ARM**: the cell build's own gate, re-driven at the export (4 dry cells), with a planted
   "theorem" in one section REFUSED as the control.
5. **THE ACCOUNT CHECK, NO LEAK INTO A VIEW, THE ZERO-CELL PROBE**: block T §T2 item 5, unchanged.
6. **THE STAGER REFUSES A NON-EXPORT** (new, from queue row 8): `export_marker_check.sh` reads OK on the release export, and the stager's
   selftest arm `export-marker` is green on the export's own harness. Control: the quarantined full-tree cut refused.

## §TW3 · THE ORDER, THE TRIPWIRES
Block W §W3's order (WHT → NTT; per problem plain#1 · salt-diet#1 · plain#2 · salt-diet#2 · plain#3 · salt-diet#3), models interleaved.
Tripwires: `TW-O` = Opus · WHT · salt-diet+statement#1 · `TW-S` = Sonnet · the same. Each is read and posted before its model continues,
the reading list block T §T3's, including the statement line (did the subject use, ignore, or contradict the statement), read in block
T's categories with USED checked by line position and the subject's own clean run.

## §TW4 · CAPS, PREDICTIONS AND THE PRICE — REGISTERED BEFORE ANY DATA
Caps: block T §T4. Predictions, per model, where a miss is a result: (i) within a condition, salt-diet+statement's CAP-COST incidence is ≥
plain+statement's; (ii) CAP-WALL binds no cell. No prediction about pass rate or premium.
**The price**, printed by `evidence/blockTW-2026-11-22/tw_price.py` (output `tw_price.out`) from three tracked tables, nothing typed:
block W's own metered spend on WHT/NTT (`extras = none`), scaled per model × arm by block T's metered spend on the six over block N's
(the statement arm against `extras = none` on the same six problems):
```
opus   plain     N six 18 cells $255.56 · T six 18 cells $276.02 · ratio 1.080 · W WHT/NTT 6 cells $49.36 -> $53.31
opus   salt-diet N six 18 cells $415.43 · T six 18 cells $404.63 · ratio 0.974 · W WHT/NTT 6 cells $177.69 -> $173.07
sonnet plain     N six 18 cells $68.10 · T six 18 cells $59.47 · ratio 0.873 · W WHT/NTT 6 cells $10.52 -> $9.19
sonnet salt-diet N six 18 cells $514.54 · T six 18 cells $381.61 · ratio 0.742 · W WHT/NTT 6 cells $181.99 -> $134.97
block TW estimate $370.54 for 24 cells · ceiling 24 x $37.21 = $893.04, plus each cell overrun past the cap
```
Control on the inputs: block N's sums reproduce block T §T4's registered price per model (Sonnet $582.64 exact; Opus $670.99 against
$671.00, a cent of rounding in the registration). ⚠️ The ratio is measured on six OTHER problems, months apart (block T §T8.3), and is an
estimate whose direction of error is unknown. The WHT triple of each model re-cuts it before NTT fires.

## §TW5 · CONFOUNDS — block T §T5 carried whole, block W §W5 carried whole
1. Block T §T5.1–2: the statement arm is a stronger treatment by construction (a specification extracted verbatim from the withheld
   reference); the refuter's catch and the planted-ambiguity instrument are off by construction.
2. Block W §W5.1: **the two problems' author is the lead**, who also extracted their statements. §TW2 item 1's re-derivation by the tool
   and the Captain's read are the controls. A defect in a task or a section is a HARNESS finding, never an arm effect.
3. Block W §W5.2: **NTT's reference proves less than WHT's** (its butterfly is not proved equal to the sums), so NTT's extracted statement
   states what the reference's checker states, nothing about the butterfly. It is printed beside any table that sets the two side by side.

## §TW6 · READING RULES, §TW7 · VOIDS, §TW8 · WHAT THIS BLOCK CANNOT ESTABLISH
§TW6 = block T §T6 (every premium registered UNRESOLVED-UNDERPOWERED). §TW7 = block T §T7 whole, the section-`cmp` VOID row included
(read per cell as block T's result did, by `t_section_cmp.py`'s method on the card as built).
§TW8: 1. No magnitude, no effect size. 2. Nothing about Opus versus Sonnet. 3. Nothing about the statement arm versus `extras = none` across
blocks (block W ran on another export and pool). 4. Nothing about the six problems of block T, or about LU (declared not feasible).

## §TW9 · WHAT THE HAND DELIVERS
Block T §T9: a result of record per model, the per-cell statement line, the census's O37 section re-cut in the same commit. Any public
sentence, and any claim about the method, is the Captain's.
