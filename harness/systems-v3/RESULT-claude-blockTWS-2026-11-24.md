# RESULT — O37 block TW, SONNET COLUMN · `claude-sonnet-5` × greenfield × extras=statement × WHT, NTT · n = 3
### bench, 2026-11-24. **4 conditions, 12 cells, every one a cell of record. One of block TW's two results of record (§TW9 = block T §T9: "a result of record per model").**
## 📌 The registration is `AMENDMENT-O37-statement-wht-ntt-claude-2026-11-22.md` (§TW0–§TW9, signed by the helm 2026-11-22; ADDENDA 1–4: the size correction, the release draft, THE RELEASE, the WHT price re-cut and the §TW5.2 section finding). Its form is block T's (`RESULT-claude-blockT{O,S}-2026-11-22.md`), carried here.
## 📌 The per-cell table is a FILE: `evidence/blockTW-result-2026-11-24/cells.tsv` (24 rows, both models; made by `tw-derive.sh` beside it from the objects on the run box, README there). The statement category per cell is `categories.tsv` beside it: a READING, each row naming where it was read.
## ⛔ Every figure line below is printed by `evidence/blockTW-result-2026-11-24/tw_result_gen.py --block TWS --print` from those two tables, and `--check` asserts each one against the bytes of this document. No figure line was typed.

---
# §1 · WHAT RAN
`claude-sonnet-5` × **greenfield** × **extras = statement** (the card carries the problem's `## Statement` section, the extractor's output on the export's own reference, §TW2 item 1) × {WHT, NTT} × {plain, salt-diet} × 3, on export `e4f786fe` (ADDENDUM 3). The model is derived per cell from its own transcripts by `served_models_v3.py check-cell`, never from the block name.
```
rows 12 · conditions 4 · cap COST 37.21
end_1 LANDED 12
export e4f786fe25c0 12
scored HEAD 12
served: 12 of 12 cells clean · head claude-sonnet-5 only
born-during: 1 of 12 cells saw a $HOME entry born during the run · transcript hits on those entries 0 · control own-id hits > 0 in 12 of 12
section as built (REQUIREMENTS.md at the root commit) equal to the export card: 12 of 12 · VOID by §TW7 0
```
**§TW7's VOID row** is read by `tw_section_cmp.py` (block T's `t_section_cmp.py` re-cut for TW; output `tw_section_cmp.out`): each cell's card as built carries the export card's section byte for byte, and ADDENDUM 3 established that card equal to the extractor's output by `cmp`. **Every cell landed, every cell is of record, and every cell is scored at HEAD** (no `solution.rs` was dirty at the end).
**Born-during** (block T ADDENDUM 3's check): the entries born during the one Sonnet cell (`clbpts03`) are another seat's x86lean test files on the run box (`k1-d406-KU.json`, `k1b-d406.log`). Each name has 0 hits in the cell's transcripts, while the cell's own id (the control) hits in every cell.

---
# §2 · CORRECTNESS, VERIFIED FIRST (the withheld G suite's FULL PASS over every cell, scored by copy)
FULL PASS = the G runner reports every TEST passed (`suite` PASS in `cells.tsv`). The bracket lists each cell's TESTS in cell order.
```
WHT          plain 3/3 [11/11 11/11 11/11] · salt-diet 3/3 [11/11 11/11 11/11]
NTT          plain 3/3 [11/11 11/11 11/11] · salt-diet 3/3 [11/11 11/11 11/11]
FULL PASS plain 6 of 6
FULL PASS salt-diet 6 of 6
```
Every Sonnet cell passes its withheld suite in full, in both arms. **This is a CEILING:** with no failure in either arm, the suite cannot tell the arms apart on correctness, and the reading is UNRESOLVED-BY-CEILING (block T's reading rules, §TW6).

---
# §3 · COST AND THE PREMIUM (§TW6 = block T §T6: every premium is registered UNRESOLVED-UNDERPOWERED)
```
WHT          median COST plain $1.43 · salt-diet $18.84 · ratio 13.2x · CAP-COST plain 0 salt-diet 0 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
NTT          median COST plain $1.53 · salt-diet $16.73 · ratio 11.0x · CAP-COST plain 0 salt-diet 0 · n plain 3 n salt-diet 3 · UNRESOLVED-UNDERPOWERED
total COST (capped at the cap) plain $9.14 · total T (metered, every cell) 17,427,863
total COST (capped at the cap) salt-diet $104.08 · total T (metered, every cell) 360,876,044
capped cells: 0
uncapped cells ending above the cap: 0
block total COST (capped at the cap) $113.22 · metered $113.22
```
No cell was capped, so no COST enters at the cap. T is metered for every cell. The figures include the harness's own sandbox probe, and both arms pay it.
The sign, which is all the registration reads: the salt-diet median is above plain's in both problems. No magnitude is read. Sonnet's plain cells are the block's cheapest (about $1 to $2 each), which is why the ratio prints large; it is printed, never read.

---
# §4 · THE REGISTERED PREDICTIONS (§TW4 (i)–(ii)), REPORTED PER MODEL; A MISS IS A RESULT
```
(i) salt-diet CAP-COST incidence >= plain in 2 of 2 problems (0 strictly, 2 ties, 0 reversed) · HOLDS
(i) WHT salt-diet 0/3 plain 0/3
(i) NTT salt-diet 0/3 plain 0/3
(ii) CAP-WALL cells 0
```
- **(i)** "within a condition, salt-diet+statement's CAP-COST incidence is ≥ plain+statement's": read per problem, as registered. It holds by two ties at zero, which is the weakest way to hold.
- **(ii)** "CAP-WALL binds no cell": the line above prints the count.
- No prediction about pass rate or premium was registered, and none is read.

---
# §5 · THE STATEMENT LINE (§TW3: did the subject use, ignore, or contradict the statement?)
The category per cell is a READING of the subject's code, in block T's categories (the lead's ruling, bus offset 106,504,279) under block T's audit rule (its RESULTs' addenda: an oracle or exec form whose content the English already states, with no Statement name, quote or derivation, is not a Statement use). **USED** needs the ensures on every contracted exec fn INSIDE `verus!`, checked by line position, AND the subject's own clean run. **EXEC USE** = Statement spec fns reimplemented as exec code in the solution and checked at runtime. A category is not a score.
```
statement plain: TEST ORACLE 2 · TEST ORACLE (partial) 1 · WEAK TRACE 3
statement salt-diet: USED 6
statement WHT          plain WEAK TRACE | TEST ORACLE | WEAK TRACE · salt-diet USED | USED | USED
statement NTT          plain TEST ORACLE (partial) | TEST ORACLE | WEAK TRACE · salt-diet USED | USED | USED
salt-diet cells whose solution REDEFINES a provided spec fn (specdefs DIFFERENT > 0): 5 of 6
  clbpws01 WHT #1 defined=17 same=16 diff=1 DIFF:op_ok
  clbpws02 WHT #2 defined=17 same=15 diff=2 DIFF:op_ok,trace_ok
  clbpws03 WHT #3 defined=17 same=16 diff=1 DIFF:op_ok
  clbpts02 NTT #2 defined=17 same=16 diff=1 DIFF:op_ok
  clbpts03 NTT #3 defined=17 same=15 diff=2 DIFF:op_ok,trace_ok
```
**A mechanical cross-check** (`tw_used_check.py`, output `tw_used_check.out`, 0 conflicts over both models): every USED cell's latest clean Verus run comes at or after its last write to `solution.rs`.
**The plain arm.** No Sonnet plain cell implements `check_trace` or any Statement fn as exec code. Three test against an oracle built from the Statement: `clbpwp02` (`hent` and the sum of products), `clbptp02` (`dsum`/`idft`/`cyc`/`partner` by name), and `clbptp01` (partial: an `idft` oracle that names `winv` and `ninv`, which only the Statement supplies, but computes both by Fermat, not by the Statement's closed forms). Three carry only a WEAK TRACE: `clbptp03` and `clbpwp03` name Statement fns in LANDING only, and `clbpwp01`'s one Statement-only token is the constant name `B52` in its tests (the bound itself is in the English). ⚠️ **Two are BORDERLINE** (`clbptp01`, `clbpwp01`), each under the audit rule's "a name only the Statement supplies counts as a derivation", and each row says so. Each row of `categories.tsv` names the lines read.
**On the redefinitions (ADDENDUM 4's §TW5.2 section finding, extended to NTT).** Every DIFFERENT here is a STRENGTHENING of the card's spec fn, on out-of-domain traces only: `op_ok` gains a result-length conjunct (NTT: and a residues conjunct), and `trace_ok` gains a determinism clause (R5, "the same vector gives the same answer"). Because `check_trace`'s contract is `r == trace_ok(t@)`, both change its specified result, but only on traces no real call produces, and the withheld suite does not exercise them. Each such cell's category is USED, recorded "USED; CONTRADICTED-NARROW (named edits)" in its source column. No score changes. Every Sonnet edit was in the tally as first read (`evidence/blockTW-2026-11-22/tw-cells.tsv`); `clbpts02` also made its `ntt`/`intt`/`cyclic` ensures unconditional, a further strengthening of its own contracts. Sonnet: 5 of 6 salt-diet cells strengthen the statement (WHT 3, NTT 2). The one correction to the tally is an Opus cell's (`clbats02`, in the Opus RESULT's §5), and it moves no count.

---
# §6 · CONFOUNDS (§TW5, carried) AND WHAT THIS RESULT CANNOT ESTABLISH (§TW8, carried)
1. **The statement arm is a stronger treatment by construction** (block T §T5.1): a formal specification extracted verbatim from the withheld
   reference. Both arms here get it. The plain/salt-diet comparison is made inside it, and the statement is not a fence leak.
2. **The refuter's catch and the planted-ambiguity instrument are off by construction** in every cell built with a statement (block T §T5.2).
3. **The two problems' author is the lead** (block W §W5.1), who also extracted their statements. §TW2 item 1's re-derivation and the
   Captain's read are the controls. The section finding in §5 is a HARNESS finding about the statement, never an arm effect.
4. **NTT's reference proves less than WHT's** (block W §W5.2): its butterfly is not proved equal to the sums, so NTT's statement states what
   the reference's checker states, and nothing about the butterfly. This table sets the two side by side, so it is printed here.
5. §TW8: no magnitude and no effect size; nothing about Opus versus Sonnet; nothing about the statement arm versus `extras = none` across
   blocks (block W ran on another export and pool); nothing about block T's six problems, or about LU. Every premium is
   UNRESOLVED-UNDERPOWERED as registered (§TW6), and a 6-of-6 pass in each arm is UNRESOLVED-BY-CEILING. Any public sentence, and any claim
   about the method, is the Captain's (§TW9).
