# AMENDMENT (DRAFT) — O37 BLOCK BC: BROWNFIELD ON THE EIGHT, CLAUDE LANE. FROZEN BEFORE THE FIRST CALL
## bench (SaltBench lead), 2026-11-23. LANDED AS A DRAFT after the seeds' non-author read (all eight: the six by systems, row 236;
## WHT and NTT, seeded by systems, by bench). The seeds and their drives are in saltbench-systems at 5bfba42b; the plant rows are registered in `BROWNFIELD-PLANTS.tsv` in the same commit. The FIELD is the pilot's (`AMENDMENT-brownfield-2026-09-13.md`, cited as "BF": §B1 the rung, §B2 neutrality, §B3 the
## plants and the two-sided metric, §B5 the rewrite-escape classes, §B7 the checklist, ADDENDA 3–7). The LANE FORM is block T's
## (`AMENDMENT-O37-statement-six-claude-2026-11-11.md`, "block T"). The pilot's Claude-lane brownfield freeze is
## `AMENDMENT-claude-lane-B-2026-09-16.md` ("lane B"). A clause that differs from any of them says so and why.
## Authority: his 2026-09-12 order (BF's head: *"Once the brownfield setup is available, go ahead and start it, preapproved"*), and his
## 2026-09-10 order of work (O37: *"once the greenfield is fully populated, take brownfield in any order to completion"*).
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ **NO CELL FIRES WHILE ANY O37 GREENFIELD CONDITION IS NOT DONE** (census ADDENDUM 50 §AU2:
## 48 today; DECLARED conditions count as populated). ⛔ **AND NO CELL FIRES BEFORE A RELEASE ADDENDUM NAMES THE EXPORT, THE POOL, AND EACH
## §BC2 RECEIPT AS MET.**

---
## §BC0 · THE INPUTS (block T §T0, row by row)
```
  1  MODEL IDs   claude-opus-5 · claude-sonnet-5 (block T row 1). Re-measured served at release by a zero-cell probe.
  2  n           3 per condition.
  3  POPULATION  64 conditions, 192 cells (§BC1).
  4  EXPORT      ONE saltbench-systems sha, cut by studio_export.sh, carrying the eight `brownfield/` seeds at the blobs the plant rows name, and
                 block T's export line as an ancestor. A DEPARTURE from block T, declared: brownfield/ trees are new since 7fe4ff7f.
  5  CLIENT PIN  block T row 5, re-driven at release (with the idleCompaction declaration if the pin moves past 2.1.259).
  6  TASK TREE   the EXPORT's tasks/systems-v3 only. Cells built `cell_build.py --client claude --field brownfield --phase 1`, plus
                 `--statement` for the statement conditions (lane B's ARM → FLAGS). `--arm salt-diet`, never `salt`. No placebo, no `--hint`.
  7  CAPS        block T row 7 unchanged (C1_USD $37.21, W1_SEC 144,000; CAP-COST and CAP-WALL armed). No brownfield-specific cap.
  8  ACCOUNT     P3: a pool the PM names at release, never ahead of P1/P2 work; `cells_account_check.sh` OK before each fire.
```

## §BC1 · THE POPULATION — 64 CONDITIONS, 192 CELLS
```
  problems   Luby · AES · Liveness · MaxFlow · BinomialHeap · LinearScan · WHT · NTT     O37's nine less LU (DECLARED, census ADDENDUM 39)
  models     claude-opus-5 · claude-sonnet-5
  field      brownfield            arms   plain · salt-diet            extras   none · statement
  ⇒ 8 × 2 × 2 × 2 = 64 conditions · × n 3 = 192 cells
```
Not in this block: brownfield × spec-change (skipped by his word, census ADDENDUM 1, 2026-09-14: *"we can skip brownfield + spec-change"*); the
agy lane's 64 (a sibling freeze). Whether brownfield × statement is expressible on each problem is §BC2 item 5's (the pilot found Paxos
inexpressible).

## §BC2 · ⛔⛔ THE ITEMS — EACH DRIVEN, WITH A CONTROL, BEFORE THE CELLS IT GATES
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
6. **THE CLAUDE-CLIENT BROWNFIELD FENCE** (BF §B7 row 3, lifted for the pilot): re-driven on the release's client: a cell cannot read
   `BROWNFIELD-PLANTS.tsv` or any seed provenance, with a planted-readable control.

## §BC3 · THE ORDER, THE TRIPWIRES
Opus first, then Sonnet (lane B's order). Problems in block N's order (Luby → AES → Liveness → MaxFlow → BinomialHeap → LinearScan), then
WHT → NTT; extras none before statement; per condition plain#1 · salt-diet#1 · plain#2 · salt-diet#2 · plain#3 · salt-diet#3.
Tripwires, each ONE cell, read and posted by the lead before its model continues: `BC-O` = Opus · Luby · brownfield · none ·
salt-diet#1 · `BC-S` = Sonnet · the same. The reading list is lane B's §Q3.3, plus the class (REPAIRED · REPLACED · REMOVED, BF §B5) and
V1 against the seed baseline.

## §BC4 · PREDICTIONS AND THE PRICE — REGISTERED BEFORE ANY DATA
Predictions, per model, where a miss is a result: (i) within a condition, salt-diet's CAP-COST incidence is ≥ plain's; (ii) CAP-WALL
binds no cell. ⛔ No prediction about V1, V2, pass rate or premium.
**The price** (the lead's brownfield plan, `bf_price.out`, by script from the greenfield spend of record on the
same 64 conditions × the pilot's brownfield/greenfield ratio): **$3,089.49 at the pooled ratio 0.976; range $2,905.90–$3,260.43.**
Its base includes block TW's registered ESTIMATE ($370.54, WHT/NTT × statement, not run). The ratio rests on five other problems on
pilot-era clients. The Luby sextet of each model re-cuts it before AES fires.

## §BC5 · CONFOUNDS — BF's and block T's, carried, plus this block's own
1. BF §B2's hazard, whole: the treatment's content is partly advice about code you did not write, so brownfield is where an arm's
   wording can act as a partial treatment. The placebo question is BF's, unchanged (no placebo arm in this grid).
2. Block T §T5 items 1–3 for the statement conditions (a stronger treatment by construction; the refuter's catch and the planted-
   ambiguity instrument off; carried constants).
3. **THE AUTHOR:** the lead chose six seeds; systems chose WHT's and NTT's. The seed choice, the exclusions and the
   tie-breaks are the controls' subject (§BC2 item 2). A defect in a seed is a HARNESS finding, never an arm effect.
4. **SEEDS DIFFER IN KIND AND MARGIN** (4/9 to 8/11), so nothing is pooled across problems without its margin beside it.

## §BC6 · READING RULES, §BC7 · VOIDS, §BC8 · WHAT THIS BLOCK CANNOT ESTABLISH
§BC6: BF §B3's metric. `bugs_fixed` is V1. `bugs_introduced` is read against the seed baseline and reported as `≥ 0 (suite-limited)`
with the margin beside it. V1 and V2 are separate columns, and `V1 unmeasured` is never passing. The class (BF §B5) is a dependent
variable. A REPLACED cell is scored and reported in its class, never pooled with REPAIRED. Every premium is registered
UNRESOLVED-UNDERPOWERED (block T §T6).
§BC7: block T §T7, plus: a cell whose `ctl/seed-sha` disagrees with its plant row is VOID (N1); a cell built from an export whose seed
baseline was not recorded is VOID.
§BC8: 1. No magnitude, no effect size. 2. Nothing Opus-versus-Sonnet. 3. Nothing brownfield-versus-greenfield as a field effect: those
cells ran on other exports and months apart, and the two fields are never pooled. 4. Nothing about the pilot's five. 5. Nothing about the
agy lane.

## §BC9 · WHAT THE HAND DELIVERS
Block T §T9: a result of record per model with the per-cell V1, `bugs_introduced`, class and statement line; O37's census section
re-cut in the same commit. Any public sentence, and any claim about the method, is the Captain's.
