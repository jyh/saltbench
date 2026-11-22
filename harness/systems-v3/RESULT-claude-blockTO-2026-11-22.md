# RESULT — O37 block T, OPUS COLUMN · `claude-opus-5` × greenfield × extras=statement × six problems · n = 3
### bench, 2026-11-22. **12 conditions, 36 cells, every one a cell of record. One of block T's two results of record (§T9: "a result of record per model").**
## 📌 The registration is `AMENDMENT-O37-statement-six-claude-2026-11-11.md` (§T0–§T9, signed by the helm 2026-11-11; ADDENDA 1–5: the release draft, THE RELEASE, the cross-lane fence gap, the second pool, the Luby price re-cut and its plain-arm correction)
## 📌 The per-cell table is a FILE: `evidence/blockT-result-2026-11-22/cells.tsv` (72 rows, both models; made by `t-derive.sh` beside it from the objects on the run box, README there). The statement category per cell is `categories.tsv` beside it: a READING, each row naming where it was read.
## ⛔ Every figure line below is printed by `evidence/blockT-result-2026-11-22/t_result_gen.py --block TO --print` from those two tables, and `--check` asserts each one against the bytes of this document. No figure line was typed.

---
# §1 · WHAT RAN
`claude-opus-5` × **greenfield** × **extras = statement** (the card carries the problem's `## Statement` section, extracted from the withheld reference with `--carry-consts`) × {Luby, AES, Liveness, MaxFlow, BinomialHeap, LinearScan} × {plain, salt-diet} × 3, on export `7fe4ff7f` (ADDENDUM 1–2). The model is derived per cell from its own transcripts by `served_models_v3.py check-cell`, never from the block name.
```
rows 36 · conditions 12 · cap COST 37.21
end_1 CAP-COST 1 · DIALOG 1 · LANDED 34
export 7fe4ff7f9789 36
scored HEAD 35 · WORKING-TREE 1
served: 36 of 36 cells clean · head claude-opus-5 only
born-during: 17 of 36 cells saw a $HOME entry born during the run · transcript hits on those entries 0 · control own-id hits > 0 in 36 of 36
section as built (REQUIREMENTS.md at the root commit) equal to the export card: 36 of 36 · VOID by §T7 0
scored at WORKING-TREE: clbvrs02 (LinearScan salt-diet #2, CAP-COST)
end DIALOG: clbvxs03 (MaxFlow salt-diet #3) at 2026-11-20T14:44:18Z
```
**§T7's VOID row** is read by `t_section_cmp.py` (output `t_section_cmp.out`; a planted byte in one section reads 12 VOID, the AES cells): each cell's card as built carries the export card's section byte for byte, and ADDENDUM 1 established that card equal to the extractor's output by `cmp`. **Every cell ended, and every cell is of record.** The one CAP-COST cell (`clbvrs02`) is scored at its WORKING TREE: its `solution.rs` was dirty at the cap, and score_claude_v3's rule reads the working tree. HEAD also passes 9 of 9 (non-scoring). **The DIALOG cell `clbvxs03`** stopped on a permission dialog of the harness's own class. It is a cell of record by block SB's precedent (`RESULT-claude-blockSB-2026-09-19-cells.tsv`, row `clbbps01`, `ENDED: DIALOG`, DONE) and is scored like any other.
**Born-during** (ADDENDUM 3): the entries born during Opus cells are the agy sibling block's per-condition roots and battery directories (`cells-ta-*`) and two client trust-seed lock files. Each one's name has 0 hits in the cell's transcripts, while the cell's own id (the control) hits in every cell.

---
# §2 · CORRECTNESS, VERIFIED FIRST (the withheld G suite's FULL PASS over every cell, scored by copy)
FULL PASS = the G runner reports every TEST passed (`suite` PASS in `cells.tsv`). The bracket lists each cell's TESTS in cell order.
```
Luby         plain 3/3 [12/12 12/12 12/12] · salt-diet 3/3 [12/12 12/12 12/12]
AES          plain 3/3 [8/8 8/8 8/8] · salt-diet 3/3 [8/8 8/8 8/8]
Liveness     plain 3/3 [11/11 11/11 11/11] · salt-diet 3/3 [11/11 11/11 11/11]
MaxFlow      plain 3/3 [8/8 8/8 8/8] · salt-diet 3/3 [8/8 8/8 8/8]
BinomialHeap plain 3/3 [13/13 13/13 13/13] · salt-diet 3/3 [13/13 13/13 13/13]
LinearScan   plain 3/3 [9/9 9/9 9/9] · salt-diet 3/3 [9/9 9/9 9/9]
FULL PASS plain 18 of 18
FULL PASS salt-diet 18 of 18
```
Every Opus cell passes its withheld suite in full, in both arms.

---
# §3 · COST AND THE PREMIUM (block N §N6: every premium is registered UNRESOLVED-UNDERPOWERED)
```
Luby         median COST plain $11.66 · salt-diet $26.06 · ratio 2.2x · CAP-COST plain 0 salt-diet 0 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
AES          median COST plain $7.86 · salt-diet $19.19 · ratio 2.4x · CAP-COST plain 0 salt-diet 0 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
Liveness     median COST plain $14.89 · salt-diet $15.44 · ratio 1.0x · CAP-COST plain 0 salt-diet 0 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
MaxFlow      median COST plain $16.88 · salt-diet $19.67 · ratio 1.2x · CAP-COST plain 0 salt-diet 0 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
BinomialHeap median COST plain $9.16 · salt-diet $28.38 · ratio 3.1x · CAP-COST plain 0 salt-diet 0 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
LinearScan   median COST plain $27.57 · salt-diet $26.96 · ratio 1.0x · CAP-COST plain 0 salt-diet 1 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
total COST (capped at the cap) plain $276.02 · total T (metered, every cell) 278,918,670
total COST (capped at the cap) salt-diet $403.74 · total T (metered, every cell) 474,333,414
capped cells METERED COST (in no COST line above): 1, $38.10 .. $38.10 against cap $37.21
uncapped cells ending above the cap: 0
block total COST (capped at the cap) $679.76 · metered $680.65
```
**Every capped cost ENTERS AT THE CAP;** the capped cells' metered COST is on its own line and used in no COST median, ratio or total. T is metered for every cell. A median at the cap is censored, and its ratio prints its bound. The figures include the harness's own sandbox probe, and both arms pay it.
The sign, which is all the registration reads: the salt-diet median is above plain's in four of six problems, and the two arms are within a tenth either way in Liveness and LinearScan. No magnitude is read.

---
# §4 · THE REGISTERED PREDICTIONS (§T4 (i)–(ii)), REPORTED PER MODEL; A MISS IS A RESULT
```
(i) salt-diet CAP-COST incidence >= plain in 6 of 6 problems (1 strictly, 5 ties, 0 reversed) · HOLDS
(i) Luby salt-diet 0/3 plain 0/3
(i) AES salt-diet 0/3 plain 0/3
(i) Liveness salt-diet 0/3 plain 0/3
(i) MaxFlow salt-diet 0/3 plain 0/3
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
statement plain: EXEC USE 12 · TEST ORACLE 4 · TEST ORACLE (partial) 2
statement salt-diet: USED 18
statement Luby         plain EXEC USE | EXEC USE | TEST ORACLE (partial) · salt-diet USED | USED | USED
statement AES          plain TEST ORACLE | TEST ORACLE | TEST ORACLE · salt-diet USED | USED | USED
statement Liveness     plain EXEC USE | TEST ORACLE | TEST ORACLE (partial) · salt-diet USED | USED | USED
statement MaxFlow      plain EXEC USE | EXEC USE | EXEC USE · salt-diet USED | USED | USED
statement BinomialHeap plain EXEC USE | EXEC USE | EXEC USE · salt-diet USED | USED | USED
statement LinearScan   plain EXEC USE | EXEC USE | EXEC USE · salt-diet USED | USED | USED
salt-diet cells whose solution REDEFINES a provided spec fn (specdefs DIFFERENT > 0): 5 of 18
  clbvys02 Luby #2 defined=22 same=20 diff=2 DIFF:s_op_ok,trace_ok
  clbvxs01 MaxFlow #1 defined=19 same=18 diff=1 DIFF:trace_ok
  clbvhs01 BinomialHeap #1 defined=25 same=12 diff=13 DIFF:rank_answer,size_answer,tree_ms,forest_ms,tree_ok,forest_desc,forest_from,trees_ok,ranks,fwsum,hgap,has_root,roots_ge
  clbvhs02 BinomialHeap #2 defined=25 same=23 diff=2 DIFF:rank_answer,size_answer
  clbvrs01 LinearScan #1 defined=51 same=48 diff=3 DIFF:s_expands_ok,s_alloc_ok,trace_ok
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

---
# ADDENDUM — 2026-11-22 (bench): A NON-AUTHOR AUDIT OF THE STATEMENT CATEGORIES. NO OPUS CATEGORY MOVES. APPENDED; everything above is unchanged.
kent read 25 of block T's 72 categories against the cells' code. That was a drawn sample of 13 (`t_audit_sample.py`), then 12 more under a rule the lead ruled during the audit:
an oracle the English requirements already state, with no Statement name, quote or derivation, is not a Statement use. Every verdict is in
`evidence/blockT-result-2026-11-22/audit-2026-11-22.tsv`. The 10 Opus cells read (`clbvap01`, `clbvhp01`, `clbvhp02`, `clbvhp03`, `clbvrp02`,
`clbvrs02`, `clbvvp03`, `clbvxs03`, `clbvyp03`, `clbvys02`) all AGREE, so §5 is unchanged here.
Three Sonnet cells move, and the rule, the sample and the re-cut are in `RESULT-claude-blockTS-2026-11-22.md`'s addendum.
**One flag, no move:** `clbvys02`'s `trace_ok` adds a determinism conjunct to the card's, so its USED ensures says more than the card's. ADDENDUM 5 classified
the Luby redefinitions the same way.
