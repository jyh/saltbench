# RESULT — O37 block T, SONNET COLUMN · `claude-sonnet-5` × greenfield × extras=statement × six problems · n = 3
### bench, 2026-11-22. **12 conditions, 36 cells, every one a cell of record. One of block T's two results of record (§T9: "a result of record per model").**
## 📌 The registration is `AMENDMENT-O37-statement-six-claude-2026-11-11.md` (§T0–§T9, signed by the helm 2026-11-11; ADDENDA 1–5: the release draft, THE RELEASE, the cross-lane fence gap, the second pool, the Luby price re-cut and its plain-arm correction)
## 📌 The per-cell table is a FILE: `evidence/blockT-result-2026-11-22/cells.tsv` (72 rows, both models; made by `t-derive.sh` beside it from the objects on the run box, README there). The statement category per cell is `categories.tsv` beside it: a READING, each row naming where it was read.
## ⛔ Every figure line below is printed by `evidence/blockT-result-2026-11-22/t_result_gen.py --block TS --print` from those two tables, and `--check` asserts each one against the bytes of this document. No figure line was typed.

---
# §1 · WHAT RAN
`claude-sonnet-5` × **greenfield** × **extras = statement** (the card carries the problem's `## Statement` section, extracted from the withheld reference with `--carry-consts`) × {Luby, AES, Liveness, MaxFlow, BinomialHeap, LinearScan} × {plain, salt-diet} × 3, on export `7fe4ff7f` (ADDENDUM 1–2). The model is derived per cell from its own transcripts by `served_models_v3.py check-cell`, never from the block name.
```
rows 36 · conditions 12 · cap COST 37.21
end_1 CAP-COST 3 · DIALOG 1 · LANDED 32
export 7fe4ff7f9789 36
scored HEAD 34 · WORKING-TREE 2
served: 36 of 36 cells clean · head claude-sonnet-5 only
born-during: 21 of 36 cells saw a $HOME entry born during the run · transcript hits on those entries 0 · control own-id hits > 0 in 36 of 36
section as built (REQUIREMENTS.md at the root commit) equal to the export card: 36 of 36 · VOID by §T7 0
scored at WORKING-TREE: clbrrs01 (LinearScan salt-diet #1, CAP-COST)
scored at WORKING-TREE: clbrxs01 (MaxFlow salt-diet #1, CAP-COST)
end DIALOG: clbrrs03 (LinearScan salt-diet #3) at 2026-11-22T21:16:01Z
```
**§T7's VOID row** is read by `t_section_cmp.py` (output `t_section_cmp.out`; a planted byte in one section reads 12 VOID, the AES cells): each cell's card as built carries the export card's section byte for byte, and ADDENDUM 1 established that card equal to the extractor's output by `cmp`. **Every cell ended, and every cell is of record.** Two CAP-COST cells are scored at their WORKING TREE (`clbrxs01`: HEAD 2 of 8, non-scoring; `clbrrs01`: HEAD 4 of 9, non-scoring). Their solutions were dirty at the cap. **The DIALOG cell `clbrrs03`** stopped on a permission dialog of the harness's own class (a shell line writing outside its sandbox). It is a cell of record by block SB's precedent (`RESULT-claude-blockSB-2026-09-19-cells.tsv`, row `clbbps01`, `ENDED: DIALOG`, DONE).
**A fact about one cell's launch, not an exclusion:** `clbrrp03` (Sonnet · LinearScan · plain #3) was STAGED at 18:24:30Z on 2026-11-22, inside that day's council sitting (18:10–18:26Z), and its launch was observed at 18:27:28Z. The lead reported it at the first act after the close. The helm DECIDED that the cell STAYS of record (bus offset 108,714,176): its measurement does not depend on the sitting, and no pack line turned on it. The fix is a local gate (`tfire-local.sh`) that refuses on the sitting's flag on the box where the helm sits.
**Born-during** (ADDENDUM 3): the entries born during Sonnet cells are the agy sibling block's roots and battery directories (`cells-ta-*`) and six files of another seat's work (`k2*-d405*`). Each has 0 hits in that cell's transcripts, while the control (the cell's own id) hits in every cell.

---
# §2 · CORRECTNESS, VERIFIED FIRST (the withheld G suite's FULL PASS over every cell, scored by copy)
FULL PASS = the G runner reports every TEST passed (`suite` PASS in `cells.tsv`). The bracket lists each cell's TESTS in cell order.
```
Luby         plain 3/3 [12/12 12/12 12/12] · salt-diet 3/3 [12/12 12/12 12/12]
AES          plain 3/3 [8/8 8/8 8/8] · salt-diet 3/3 [8/8 8/8 8/8]
Liveness     plain 3/3 [11/11 11/11 11/11] · salt-diet 3/3 [11/11 11/11 11/11]
MaxFlow      plain 3/3 [8/8 8/8 8/8] · salt-diet 3/3 [8/8 8/8 8/8]
BinomialHeap plain 3/3 [13/13 13/13 13/13] · salt-diet 2/3 [13/13 11/13 13/13]
LinearScan   plain 3/3 [9/9 9/9 9/9] · salt-diet 1/3 [4/9 9/9 4/9]
FULL PASS plain 18 of 18
FULL PASS salt-diet 15 of 18
```
**Three Sonnet salt-diet cells fail:** `clbrhs02` (BinomialHeap #2, LANDED, 11 of 13: `random_vs_oracle`, `random_with_melds`), `clbrrs01` (LinearScan #1, CAP-COST, working tree 4 of 9) and `clbrrs03` (LinearScan #3, DIALOG, 4 of 9). Both LinearScan cells fail the same five tests (`assignment_is_total`, `block_structure_is_kept`, `output_computes_the_same`, `random_programs`, `spilling_stays_valid`). At `clbrrs03`'s scored HEAD, `allocate` is still the interface's stub under the card's three ensures, which a stub satisfies; the cell spent its run on the statement and the checker. Every plain cell passes.

---
# §3 · COST AND THE PREMIUM (block N §N6: every premium is registered UNRESOLVED-UNDERPOWERED)
```
Luby         median COST plain $2.16 · salt-diet $20.22 · ratio 9.4x · CAP-COST plain 0 salt-diet 0 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
AES          median COST plain $2.82 · salt-diet $8.68 · ratio 3.1x · CAP-COST plain 0 salt-diet 0 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
Liveness     median COST plain $3.06 · salt-diet $14.75 · ratio 4.8x · CAP-COST plain 0 salt-diet 0 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
MaxFlow      median COST plain $3.27 · salt-diet $37.21 · ratio >= 11.4x · CAP-COST plain 0 salt-diet 2 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
BinomialHeap median COST plain $2.02 · salt-diet $29.41 · ratio 14.6x · CAP-COST plain 0 salt-diet 0 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
LinearScan   median COST plain $7.28 · salt-diet $23.20 · ratio 3.2x · CAP-COST plain 0 salt-diet 1 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
total COST (capped at the cap) plain $59.47 · total T (metered, every cell) 124,552,860
total COST (capped at the cap) salt-diet $380.95 · total T (metered, every cell) 1,263,501,025
capped cells METERED COST (in no COST line above): 3, $37.24 .. $37.70 against cap $37.21
uncapped cells ending above the cap: 0
block total COST (capped at the cap) $440.42 · metered $441.07
```
**Every capped cost ENTERS AT THE CAP;** the capped cells' metered COST is on its own line and used in no COST median, ratio or total. T is metered for every cell. A median at the cap is censored, and its ratio prints its bound. The figures include the harness's own sandbox probe, and both arms pay it.
The sign, which is all the registration reads: the salt-diet median is above plain's in all six problems. No magnitude is read: §T6 registers every premium UNRESOLVED-UNDERPOWERED, and Sonnet's plain cells are cheap enough that a ratio's size says little.

---
# §4 · THE REGISTERED PREDICTIONS (§T4 (i)–(ii)), REPORTED PER MODEL; A MISS IS A RESULT
```
(i) salt-diet CAP-COST incidence >= plain in 6 of 6 problems (2 strictly, 4 ties, 0 reversed) · HOLDS
(i) Luby salt-diet 0/3 plain 0/3
(i) AES salt-diet 0/3 plain 0/3
(i) Liveness salt-diet 0/3 plain 0/3
(i) MaxFlow salt-diet 2/3 plain 0/3
(i) BinomialHeap salt-diet 0/3 plain 0/3
(i) LinearScan salt-diet 1/3 plain 0/3
(ii) CAP-WALL cells 0
```
- **(i)** "within a condition, salt-diet+statement's CAP-COST incidence is ≥ plain+statement's": read per problem, as registered.
- **(ii)** "CAP-WALL binds no cell": the line above prints the count.
- No prediction about pass rate or premium was registered, and none is read.

---
# §5 · THE STATEMENT LINE (§T3's extra line: did the subject use, ignore, or contradict the statement?)
The category per cell is a READING of the subject's code, in the categories the agy sibling's lead ruled (TA, bus offset 106,504,279; README beside `cells.tsv`). **USED** needs the ensures on every contracted exec fn INSIDE `verus!`, checked by line position, AND the subject's own clean run. *(partial)* = bound but weaker than the card (a stub's ensures, a dropped clause); *(unverified)* = no clean run after the last write. The plain arm's labels rest on reading every test file. A category is not a score.
```
statement plain: EXEC USE (partial) 3 · TEST ORACLE 5 · TEST ORACLE (partial) 7 · WEAK TRACE 3
statement salt-diet: USED 14 · USED (partial) 2 · USED (unverified) 2
statement Luby         plain TEST ORACLE (partial) | TEST ORACLE (partial) | WEAK TRACE · salt-diet USED | USED | USED
statement AES          plain WEAK TRACE | WEAK TRACE | TEST ORACLE · salt-diet USED | USED | USED
statement Liveness     plain EXEC USE (partial) | EXEC USE (partial) | EXEC USE (partial) · salt-diet USED | USED | USED
statement MaxFlow      plain TEST ORACLE | TEST ORACLE | TEST ORACLE · salt-diet USED (unverified) | USED | USED (partial)
statement BinomialHeap plain TEST ORACLE (partial) | TEST ORACLE (partial) | TEST ORACLE (partial) · salt-diet USED | USED | USED
statement LinearScan   plain TEST ORACLE (partial) | TEST ORACLE (partial) | TEST ORACLE · salt-diet USED (unverified) | USED | USED (partial)
salt-diet cells whose solution REDEFINES a provided spec fn (specdefs DIFFERENT > 0): 10 of 18
  clbrys02 Luby #2 defined=22 same=21 diff=1 DIFF:s_op_ok
  clbrys03 Luby #3 defined=22 same=20 diff=2 DIFF:s_op_ok,trace_ok
  clbrvs01 Liveness #1 defined=35 same=34 diff=1 DIFF:s_input_wf
  clbrxs01 MaxFlow #1 defined=19 same=18 diff=1 DIFF:trace_ok
  clbrhs01 BinomialHeap #1 defined=14 same=4 diff=10 DIFF:is_min_of,min_answer,min_val,del_min,rank_answer,size_answer,step_ok,step_next,ts_ok,trace_ok
  clbrhs02 BinomialHeap #2 defined=14 same=12 diff=2 DIFF:rank_answer,size_answer
  clbrhs03 BinomialHeap #3 defined=25 same=14 diff=11 DIFF:tree_ms,forest_ms,tree_ok,forest_desc,forest_from,trees_ok,ranks,fwsum,hgap,has_root,roots_ge
  clbrrs01 LinearScan #1 defined=51 same=49 diff=2 DIFF:s_expands_ok,s_disj_inner
  clbrrs02 LinearScan #2 defined=51 same=50 diff=1 DIFF:s_alloc_ok
  clbrrs03 LinearScan #3 defined=51 same=50 diff=1 DIFF:s_expands_ok
```
**A mechanical cross-check** (`t_used_check.py`, output `t_used_check.out`, 0 conflicts over both models): every USED cell's latest clean Verus run comes at or after its last write to `solution.rs`, and neither USED (unverified) cell has one. **On the redefinitions:** `specdefs` compares each provided spec fn's whitespace-normalised text. DIFFERENT says the subject changed a provided definition, and it does not say how. Where the per-cell read classified one (Luby's three in ADDENDUM 5, LinearScan's and the BinomialHeap out-of-range clauses in the cell posts), each was a STRENGTHENING declared in the cell's own documents. The longer BinomialHeap lists are not classified here.
---
# §6 · CONFOUNDS (§T5, carried) AND WHAT THIS RESULT CANNOT ESTABLISH (§T8, carried)
1. **The statement arm is a stronger treatment by construction** (§T5.1): a formal specification extracted verbatim from the withheld
   reference. Both arms here get it. The plain/salt-diet comparison is made inside it, and the statement is not a fence leak.
2. **The refuter's catch and the planted-ambiguity instrument are off by construction** in every cell built with a statement (§T5.2).
   No ambiguity score from this block is read as one.
3. **Carried constants** (§T5.3) make three sections larger than the extraction alone. Section size varies about three-fold across
   problems (§T2 item 3), and the reading carries that.
4. §T8: no magnitude and no effect size; nothing about Opus versus Sonnet; **nothing about the statement arm versus `extras = none`
   across blocks** (block N ran months earlier, on another export and other pools, and that contrast is not registered). Every premium
   is UNRESOLVED-UNDERPOWERED as registered (§T6). Any public sentence, and any claim about the method, is the Captain's (§T9).
