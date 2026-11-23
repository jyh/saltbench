# AMENDMENT (DRAFT) — O37 BLOCK BCA: BROWNFIELD ON THE EIGHT, agy LANE. FROZEN BEFORE THE FIRST CALL
## bench (SaltBench lead), 2026-11-23. LANDED AS A DRAFT after the seeds' non-author read (all eight: the six by systems, row 236;
## WHT and NTT, seeded by systems, by bench). The seeds and their drives are in saltbench-systems at 5bfba42b; the plant rows are registered in `BROWNFIELD-PLANTS.tsv` in the same commit. The FIELD is the pilot's (`AMENDMENT-brownfield-2026-09-13.md`, cited as "BF": §B1 the rung, §B2 neutrality, §B3 the
## plants and the two-sided metric, §B5 the rewrite-escape classes, §B7 the checklist, ADDENDA 3–7). The LANE FORM is block T's
## (`AMENDMENT-O37-statement-six-claude-2026-11-11.md`, "block T") for the arms' rules, and block TA's (`AMENDMENT-O37-statement-six-agy-2026-11-17.md`,
## "TA") for the agy lane. Its Claude-lane sibling is block BC (`AMENDMENT-O37-brownfield-eight-claude-2026-11-23.md`, beside this file), cited as "BC". A clause that differs from any of them says so and why.
## Authority: his 2026-09-12 order (BF's head: *"Once the brownfield setup is available, go ahead and start it, preapproved"*), and his
## 2026-09-10 order of work (O37: *"once the greenfield is fully populated, take brownfield in any order to completion"*).
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ **NO CELL FIRES WHILE ANY O37 GREENFIELD CONDITION IS NOT DONE** (census ADDENDUM 50 §AU2:
## 48 today; DECLARED conditions count as populated). ⛔ **AND NO CELL FIRES BEFORE A RELEASE ADDENDUM NAMES THE EXPORT, THE POOL, AND EACH
## §BCA2 RECEIPT AS MET.**

---
## §BCA0 · THE INPUTS (TA §TA0, row by row)
```
  1  MODEL IDs     gemini-3.8-flash-high · gemini-4-argon-high (TA row 1). Re-measured served by the lane battery; a mismatch VOIDS.
  2  n             3 per condition.
  3  POPULATION    64 conditions, 192 cells (§BCA1).
  4  EXPORT        ONE harness sha, named in the release: the agy cell lane's export AS RELEASED at that time (lineage aa071afc, the hook
                   export) carrying the eight `brownfield/` seeds at the blobs the plant rows name. A DEPARTURE from TA, declared.
  5  CLIENT        agy at the version and sha the release names; settings carry `"agentMode": ""`; TA ADDENDUM 2 ruling 3's client guard.
  6  CAPS          TA row 6 unchanged: T1_TOK 250,000,000 · AGY_PRINT_TIMEOUT 1800 s · AGY_TURN_TIMEOUT 2100 s; truncation in EVENTS.
  7  QUOTA         TA row 7 unchanged: P3, the agy pool, yielding to any O4 agy cell live or queued.
  8  TASK TREE     the EXPORT's tasks/systems-v3 only; cells built `cell_build.py --client agy --field brownfield --phase 1`, plus
                   `--statement` for the statement conditions.
```

## §BCA1 · THE POPULATION — 64 CONDITIONS, 192 CELLS
```
  problems   Luby · AES · Liveness · MaxFlow · BinomialHeap · LinearScan · WHT · NTT     O37's nine less LU (DECLARED, census ADDENDUM 39)
  models     gemini-3.8-flash-high · gemini-4-argon-high
  field      brownfield            arms   plain · salt-diet            extras   none · statement
  ⇒ 8 × 2 × 2 × 2 = 64 conditions · × n 3 = 192 cells
```
Not in this block: brownfield × spec-change (skipped by his word, census ADDENDUM 1, 2026-09-14: *"we can skip brownfield + spec-change"*); the
Claude lane's 64 (BC). Whether brownfield × statement is expressible on each problem is §BCA2 item 5's (the pilot found Paxos
inexpressible).

## §BCA2 · ⛔⛔ THE ITEMS — EACH DRIVEN, WITH A CONTROL, BEFORE THE CELLS IT GATES
1. **THE SEEDS, AT THE EXPORT.** Per problem: the seed's sha256 at the export equals its plant row's. S1 (`bin/rt check` GREEN in a BUILT
   dry cell, the containment half included; driven ahead on all eight in the seeds'
   drafts, `s1-rtcheck/`, and re-driven at the export), S2 (the withheld suite fails on the raw seed, the failing tests
   named from that run), S3 (no warning beyond the plain reference's own warning set; a planted control fires). Drafts: saltbench-systems
   `drafts/o37-brownfield-seeds-2026-11-23/` (all eight). WHT and NTT were seeded by systems, a non-author (row 236 (2),
   5ed13106), and read by bench (README, NON-AUTHOR READ OF WHT AND NTT).
2. **THE PLANT ROWS ARE REGISTERED BEFORE ANY CELL** (BF §B3), in `harness/systems-v3/BROWNFIELD-PLANTS.tsv`, with the non-author read of
   each choice. The draft rows declare four refusals EXCLUDED as declinations, two tie-breaks stated after the margins were read, AES's
   printed-vector visibility and MaxFlow's shared absence of the reference's defensive fallback. The non-author read (systems, row 236,
   2026-11-23, at 3285d174) UPHELD the refusals, the AES tie-break and the S3 baseline reading, and REVERSED the two reference comments
   that contradicted the seeded code: both sentences are DELETED and S1–S3 re-run on the two seeds (README, FORK c). A later reversal
   re-runs S1–S3 the same way.
3. **THE SEED BASELINE** (BF §B3: the withheld suite on the seed, per problem, recorded before any cell). It is the reference against which
   `bugs_introduced` is read. It is re-run at the export, and must equal S2's named set.
4. **NEUTRALITY:** N2 driven at the export (pattern imported from `neutrality_grep.py`; drafts: 0 hits in 12 files, control fires). N1
   (seed bytes identical across a condition's cells, `ctl/seed-sha`) and N3 (the greenfield→brownfield briefing diff published) are driven
   at the first cells of each problem, with their REDs, as BF ADDENDUM 7 ordered. `check_withheld_leak_v3.py` CLEAN on the export.
5. **EXPRESSIBILITY:** one dry build per problem × {none, statement}, rc 0, both arms. A problem whose brownfield × statement build
   refuses is INEXPRESSIBLE for that extras and leaves the population by a release addendum, never silently.
6. **THE LANE IS LIVE AND THE FENCE HOLDS ON THIS EXPORT** (TA §TA2 item 6, and the cell lane's release reading of the helm's digest #1471):
   the agy battery on one dry brownfield cell per model, and a cell cannot read `BROWNFIELD-PLANTS.tsv` or any seed provenance (under
   `.agyhome` included), with a planted-readable control.

## §BCA3 · THE ORDER, THE TRIPWIRES
Flash first, then argon (TA's order). Problems in block N's order (Luby → AES → Liveness → MaxFlow → BinomialHeap → LinearScan), then
WHT → NTT; extras none before statement; per condition plain#1 · salt-diet#1 · plain#2 · salt-diet#2 · plain#3 · salt-diet#3.
Tripwires, each ONE cell, read and posted by the lead before its model continues: `BCA-F` = Flash · Luby · brownfield · none ·
salt-diet#1 · `BCA-P` = argon · the same. The reading list is TA's, plus the class (REPAIRED · REPLACED · REMOVED, BF §B5) and
V1 against the seed baseline.

## §BCA4 · PREDICTIONS AND THE PRICE — REGISTERED BEFORE ANY DATA
Predictions, per model, where a miss is a result: (i) within a condition, salt-diet's TURNS-CUT incidence (in EVENTS) and CAP-TOKENS incidence is
≥ plain's; (iii) CELL-KILLED binds no cell outside a declared 503 episode (TA §TA3). ⛔ No prediction about V1, V2, pass rate or premium.
**The price**, in cell wall (the lead's brownfield plan, `bf_price.out`, by script from the greenfield wall
of record on the same 64 conditions × the pilot's brownfield/greenfield ratio): **90.5 h at the pooled ratio 1.315; range 63.3–90.5 h**;
agy pool points per cell UNMEASURED. Its base carries 22.7 h of ESTIMATE: block TWA's (WHT/NTT × statement, not run) and argon × none on
the six (never run; TA argon × NA flash/TA flash per arm, across NA's older-client seam). The ratio rests on five other problems on
pilot-era clients. The Luby sextet of each model re-cuts it before AES fires.

## §BCA5 · CONFOUNDS — BF's and block T's, carried, plus this block's own
1. BF §B2's hazard, whole: the treatment's content is partly advice about code you did not write, so brownfield is where an arm's
   wording can act as a partial treatment. The placebo question is BF's, unchanged (no placebo arm in this grid).
2. TA §TA4 items 1–3 for the statement conditions and the model and client seams (a stronger treatment by construction; the refuter's catch and the planted-
   ambiguity instrument off; carried constants).
3. **THE AUTHOR:** the lead chose six seeds; systems chose WHT's and NTT's. The seed choice, the exclusions and the
   tie-breaks are the controls' subject (§BCA2 item 2). A defect in a seed is a HARNESS finding, never an arm effect.
4. **SEEDS DIFFER IN KIND AND MARGIN** (4/9 to 8/11), so nothing is pooled across problems without its margin beside it.

## §BCA6 · READING RULES, §BCA7 · VOIDS, §BCA8 · WHAT THIS BLOCK CANNOT ESTABLISH
§BCA6: BF §B3's metric. `bugs_fixed` is V1. `bugs_introduced` is read against the seed baseline and reported as `≥ 0 (suite-limited)`
with the margin beside it. V1 and V2 are separate columns, and `V1 unmeasured` is never passing. The class (BF §B5) is a dependent
variable. A REPLACED cell is scored and reported in its class, never pooled with REPAIRED. Every premium is registered
UNRESOLVED-UNDERPOWERED (block T §T6).
§BCA7: TA §TA5's voids, plus: a cell whose `ctl/seed-sha` disagrees with its plant row is VOID (N1); a cell built from an export whose seed
baseline was not recorded is VOID.
§BCA8: 1. No magnitude, no effect size. 2. Nothing Flash-versus-argon as models; nothing Claude-versus-agy (so nothing BC versus BCA). 3. Nothing brownfield-versus-greenfield as a field effect: those
cells ran on other exports and months apart, and the two fields are never pooled. 4. Nothing about the pilot's five. 5. Nothing about the
Claude lane.

## §BCA9 · WHAT THE HAND DELIVERS
TA §TA6: a result of record per model (the tree-hash line and the O4 concurrency column per cell) with the per-cell V1, `bugs_introduced`, class and statement line; O37's census section
re-cut in the same commit. Any public sentence, and any claim about the method, is the Captain's.
