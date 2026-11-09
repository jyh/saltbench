# AMENDMENT — O37's SECOND LEAN PROBLEM: SIX CLAUDE CELLS, LZW × GREENFIELD × LEAN-AENEAS × {OPUS, SONNET} × n = 3. FROZEN BEFORE THE FIRST CALL
## bench (SaltBench lead), 2026-11-09. The helm's decision of 2026-11-09 10:09 (arm (A) of the lead's price fork): fire at the pilot's terms,
## on spare quota at P3, never ahead of P1/P2 work, under the day lines. The form is the CRC-32 pilot's, `AMENDMENT-O37-aeneas-pilot-2026-09-30.md`
## (signed, ADDENDA 1–6, merged 0c8bf97b), cited below as "the pilot". Its RESULT is `RESULT-O37-aeneas-pilot-2026-09-30.md` (#294).
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ **NO CELL FIRES BEFORE A RELEASE ADDENDUM NAMES THE EXPORT SHA, THE POOL, AND EVERY
## RECEIPT OF §A5 AS MET.** Signature and release are two acts, as in the pilot.

**What this file is.** A second problem for the pilot's arm, and nothing else. Every clause of the pilot binds here BY CITATION unless this
file names the clause and says how it differs and why. The one variable is the PROBLEM (CRC-32 → LZW). What the change of problem forces
(a new statement, a new theorem name, one library model) is declared in §A1 and §A2 so a reader can weigh it.

---

## §A0 · THE INPUTS (the pilot's §A0, row by row)
```
  1  MODELS         claude-opus-5 (block ZO) and claude-sonnet-5 (block ZS): the pilot's ids and the comparison cells' ids (§A2), passed IN
                    FULL, never as an alias. Read per cell from the transcripts' message.model, head and sidechain apart. ⚠️ Both ids are
                    UNMEASURED today: a pre-launch probe that is refused, or serves another id, HOLDS the cell at zero spend (§A7). A
                    substitute model is not this registration's to choose: it breaks the comparison by construction and needs a new one.
  2  n              3 per model: 6 cells (clbeza01–03 Opus, clbwza01–03 Sonnet; both prefixes 0 hits in either repository at freeze).
  3  PROBLEM, FIELD LZW × greenfield, phase 1 only (no customer dispatch, no spec-change).
  4  ARM            lean-aeneas, the pilot's §A1.1 unchanged: the salt-diet method with the VERIFIER swapped (a derived arm file).
  5  STATEMENT      GIVEN, harness-owned: the LZW `O37Spec.Statement` (§A1.2). REQUIREMENTS.md carries no statement section.
  6  EXPORT         ONE bare sha of the harness tree, named in the release addendum, carrying §A5's build. One sha for all 6 cells.
  7  CLIENT PIN     the pilot's: 2.1.259 by absolute path, its sha asserted per launch. ⚠️ A later block found 2.1.259 refuses a NEWER model id
                    (OD ADDENDUM on 2.1.280); whether it still serves the two ids above is read by the probe (row 1). A client change is a
                    release-addendum act with its own probe, never a silent swap.
  8  TOOLCHAIN      the pilot's read-only root, unchanged: Aeneas + Charon nightly 2026.09.29-b08bf81, Lean 4.31.0, rust nightly-2026-09-17.
                    KEPT ON PURPOSE: the lead measured 57 Aeneas nightlies and none was ever on Lean 4.32 (4.31 → 4.35-rc4), so a re-pin buys
                    no shared trust base with x86lean, and would make the second problem differ from the first by more than the problem.
  9  CAPS           the pilot's: C1_USD $37.21 on the cell's own meter; no turn cap. (§A8: it is projected to bind every cell.)
 10  ACCOUNT        the pool the release addendum names, from the PM's re-cut and that day's day-line-check (the 10 % reserve holds), named
                    per cell; the run box's account check (identity string, never a directory name) reads OK before each fire.
 11  FIRE ORDER     §A7: one live cell at a time; P3, on spare quota only.
```

## §A1 · THE ARM, AND WHAT THE NEW PROBLEM CHANGES IN IT
### §A1.1 · Unchanged
The pilot's §A1.1 (the derived arm file, the swap table, the gate) and §A1.3 (PASS IS KERNEL-ONLY: `#print axioms` names only `propext`,
`Classical.choice`, `Quot.sound`; a native closure is its own class) bind unchanged.

### §A1.2 · The statement, given
LZW's `trace_ok` is a THIN wrapper, as CRC-32's is (`op_ok` per op against `encode_model` / `decode_model`, `tasks/systems-v3/LZW/card.md`
§Statement). So, as in the pilot (§A2 there), the Lean statement is the components' own Verus `ensures`: `encode`'s four and `decode`'s one,
transcribed one for one with their spec closure of 17 definitions (`init_dict` · `first_idx` · `code_of` · `in_dict` · `enc` · `enc_dict` ·
`dec_entry` · `dec` · `dec_dict` · `dec0_entry` · `dec0` · `dec0_dict` · `encode_model` · `decode_model` · `encode_dict` · `decode_dict` ·
`codes_view`) onto `List`. The proposition:
```
  def Statement : Prop :=
    (∀ input : Aeneas.Std.Slice Aeneas.Std.U8, input.val.length ≤ MAX_INPUT →
      ∃ out, solution.encode input = Aeneas.Std.Result.ok out ∧
        codes_view out.val = encode_model (input.val.map (·.bv)) ∧
        decode_model (codes_view out.val) = input.val.map (·.bv) ∧
        (∀ i : Nat, (h : i < out.val.length) → ((out.val[i]).val : Int) < 256 + i) ∧
        decode_dict (codes_view out.val) = encode_dict (input.val.map (·.bv)))
    ∧
    (∀ codes : Aeneas.Std.Slice Aeneas.Std.U16, codes.val.length ≤ MAX_INPUT →
      ∃ out, solution.decode codes = Aeneas.Std.Result.ok out ∧
        out.val.map (·.bv) = decode_model (codes_view codes.val))
```
with `MAX_INPUT = 65280`. The subject proves `theorem O37Proof.lzw_correct : O37Spec.Statement` in `proof/Proof.lean`.
**Four declared deviations from the Verus text**, each in the statement file's header:
```
  1  first_idx's index        Verus `int`, here `Nat`: its only caller passes 0, so the Verus `i < 0` arm is unreachable
  2  carriers                 a byte is `BitVec 8`, a code `Int`
  3  out-of-range prev[0]     Verus leaves it unspecified; here `getD … 0`, unreachable (every dictionary entry is non-empty)
  4  decode's length bound    `codes.length ≤ MAX_INPUT`, a requires Verus does NOT have. Aeneas's `Vec.push` FAILS past `Usize.max` (Aeneas
                              Std `Vec.lean`:156-162 at the pin) where Verus's cannot, so an unbounded decode half is FALSE of the reference.
                              The bound keeps the output ≤ n(n+1)/2 = 2,130,771,840 < U32.max, and every test drives inside it.
```
(4) was a non-author reader's finding (paris, 2026-11-09), measured at the pin before it was taken. The reader's other arm, `∃ r, … = ok r ∨
fail`, was NOT taken: it weakens the statement.

### §A1.3 · The one library model, supplied by the harness (new: the pilot met none)
At the pin, `#print axioms` on the REFERENCE's translation reads `solution.encode` and `solution.decode` on the standard three ONLY; the
reference reaches `alloc.vec.Vec.as_slice` (left by Aeneas as an axiom) only through the trace checker, which the statement does not include.
A SUBJECT may call `as_slice` inside `encode`. **The harness supplies it**, after Aeneas and before `lean-check`'s kernel replay, as
`def alloc.vec.Vec.as_slice … := ok v.slice` (Aeneas Std `structure Vec := slice : Slice`, so this is the Vec's own slice and never fails),
and only when the axiom occurs exactly once in exactly the expected form. **Why the harness and not the subject:** Rust's `Vec::as_slice` has
one meaning, and a RED for a library gap would measure Aeneas's coverage, not the subject. Any OTHER external a subject's code leaves as an
axiom is the subject's and reads RED at the axiom check (the pilot's §A3 row 5: a subject stepping outside Aeneas's subset is a FINDING).
**WRONG IF** a cell's Lean half is GREEN with an `as_slice` that is not the harness's bytes.

## §A2 · THE COMPARISON
The pilot's §A2 rule: the matrix's cells whose Verus statement is GIVEN, **`LZW × greenfield × salt-diet × statement`**, as of record:
```
  claude-opus-5     6d58f1ec · 9aca67c5 (lower bound: FLOOR) · f5f66c47
  claude-sonnet-5   clbszs01 · clbszs02 (lower bound: CAP-COST) · clbszs03
```
(`CELLMAP-descriptive-tables-v2-2026-09-27.tsv`, columns cell · lower_bound · lb_reason.) The RESULT reads their verdicts from their own
records, never re-scored here. ⚠️ **One comparison cell already ended CAP-COST at this same cap**, so the cap is not new to LZW.
The pilot's five departures (§A2 there) carry, with one change: row 5 (the statement's reach) reads, for LZW, "Verus: the components' ensures
plus trace_ok/check_trace · Lean: the components' ensures and the one theorem". §A1.2's deviation (4) is a SIXTH departure: the Lean
decode half is bounded where the Verus one is not.

## §A3 · WHAT IS SCORED, AND FROM WHOSE BYTES
The pilot's §A3, unchanged, with LZW's hidden suite (`tasks/systems-v3/LZW/G/run_tests.sh`, its sha16 recorded per cell) in row 1 and
`O37Proof.lzw_correct` in row 2. **A Lean-arm PASS** is suite FULL PASS ∧ O37-LEAN GREEN ∧ O37-STMT UNCHANGED. **No rate and no p-value.**
**CAP-COST is an outcome of record on the cost axis** (the helm's 10:09 reading): a capped cell is scored as it stands at the cap, and its
row says CAP-COST beside its suite, Lean-half and statement columns. It is never re-fired at a higher cap under this registration (§A8 (B)).

## §A4 · THE FENCE AND THE SESSION
The pilot's §A4, unchanged (the read-only root, `O37_ROOT` HOLD-by-name, `lean-check` writing only in the cell's scratch, the withheld tree
never in the export), plus: **the withheld tree for LZW** (the reference proof of §A5 row 3, the vector file) is never in the export, and the
export's withheld-name scan reads 0 for it.

## §A5 · THE RECEIPTS — WHAT IS MEASURED AT FREEZE, AND WHAT THE RELEASE OWES
**Measured at freeze, zero model spend, at the pin** (the lead's spike plan, ADDENDA 1–9, a private record; each figure below is that record's):
```
  translation     the LZW reference, Verus annotations stripped by a tool that prints its drops, as a plain crate: cargo build rc 0.
                  RED CONTROL on the task's withheld counter-traces: reference TRACE_OK true 4/4 · mutant false 4/4.
                  charon rc 0 · aeneas rc 0 · emitted Lean 594 lines (sha256/16 ef78a8ef31e36510) · lean rc 0, 0 errors, 0 warnings;
                  a planted-error copy → rc 1 at the planted line. One external left: Vec.as_slice.
  statement       the 17 definitions + Statement typecheck against the reference's translation: rc 0, 0 errors (file sha256/16
                  64eab54233415d93, after the reader's repair).
  pairing (ii)    the stripped Rust reference and the Lean spec run on the same inputs (5 encodes, 3 decodes on codes no encoder emits,
                  including an out-of-range 300 and the kwkwk path): 8/8 AGREE; the four Lean round-trips read true. RED CONTROL: a
                  one-token mutant of `enc` → DISAGREE on 4 of 8.
  non-author read paris, 2026-11-09: all 17 definitions are the Verus ones; the deviations hold; the encode half says what the four ensures
                  say, no more, no less; one repair (deviation 4), MEASURED and taken.
  the model       §A1.3's model: with the axiom, `check_trace` lists `Vec.as_slice`; with the model, lean rc 0 and the standard three only.
                  The model REFUSES unless the axiom occurs exactly once (driven on another problem's emit: found 0, rc 1).
```
**OWED before the release addendum, each with its receipt in that addendum** (the pilot carried all of these AT its freeze; this file
carries them as preconditions, and says so):
```
  1  HARNESS       the o37 machinery KEYED BY PROBLEM (today it is CRC-32's by construction: the spec file, the theorem name in the
                   axiom program, the arm file's statement paragraph). The LZW spec + statement under the harness's o37 dir; the
                   theorem name a per-problem input; §A1.3's model applied inside lean-check after aeneas. REGRESSION ARM: a CRC-32
                   cell renders and scores BYTE-IDENTICALLY to the pilot's export 865290f (arm file, gate, spec, scorer selftests).
  2  SELFTESTS     o37_leancheck_selftest and o37_score_selftest re-run for LZW with the pilot's RED arm classes (sorry · axiom · import ·
                   wrong type · no theorem · native closure · a statement weakened in the cell's tree READ RED from the harness's bytes),
                   plus two new: an `as_slice` axiom with no model → RED; a FOREIGN `as_slice` body in the cell → RED. RED BACKWARDS for each.
  3  FEASIBILITY   a REFERENCE PROOF of `O37Proof.lzw_correct` over the reference's translation, GREEN under the export's lean-check with
                   the standard three axioms, kept in the withheld tree (the pilot's §A5 "reference proof": "the task is feasible under the
                   arm's rules"). ⚠️ PRICE UNMEASURED: the statement carries the round-trip decode_model ∘ encode_model = id, which CRC-32's
                   did not. Without this receipt a CAP-COST or a RED could not be told apart from an infeasible task, so it is a
                   PRECONDITION, not a nicety. Releasing without it changes what a verdict asserts, and is not this file's to choose.
  4  BUILD         an LZW lean-aeneas cell built from the export on the run box: gate receipt arm 3 RED (statement edit) and GREEN;
                   verify.sh RED on the sorry skeleton; in a COPY with the reference solution and proof, verify GREEN and
                   `gate.sh --landing` GREEN.
  5  PROBE         the pre-launch sandbox probe serves the registered id (§A0 row 1) on the pinned client, per model, at zero cells.
```

## §A6 · THE SEPARATE ROW: FIDELITY
The pilot's reading (i) (a lemma relating the transcription to an INDEPENDENT specification) has no LZW counterpart registered here. The
pairing's ceiling is §A5's: transcription + an 8-row vector check + a non-author read. The RESULT says so beside the head-to-head.

## §A7 · FIRE ORDER, STOPS AND VOIDS
- **Order:** ZO 1 (clbeza01), ZS 1 (clbwza01), ZO 2, ZS 2, ZO 3, ZS 3; one live cell at a time on the named pool; **day-line-check before
  EACH launch** — a pool over its day line HOLDS the next cell on the pool's clock, never on the work; P1/P2 work on that pool goes first.
- **Cell 1 is read at its first in-cell `lean-check` run** before any other cell fires, with the pilot's §A7 rule for a harness-caused
  failure (stopped, NOT-SCORED(HARNESS), fixed on a new export named in an addendum, re-fired as the registered `r1`).
- **THE RE-PRICE STOP (the helm's WRONG-IF, 10:09):** after ZO 1 and again after ZS 1, the cell's own `final $` is read against §A8's
  projection. If a cell LANDS under the cap where all six were projected to bind, or the measured multiplier moves the projection past the
  cap on fewer than all six, the next cell HOLDS and the price is re-posted to the helm before it fires.
- **A probe refused or serving another id** (§A0 row 1) HOLDS at zero spend; it is never a void and never a substitution.
- The cap, the watcher and the voids are lane B's (the pilot's §A7), unchanged.

## §A8 · THE PRICE
```
  anchor   RESULT-cost-tables-v3-2026-09-29.md §$1, greenfield LZW statement-salt-diet medians: Opus ≥ $18.54 · Sonnet ≥ $12.36 (both FLOORS)
  ratio    the pilot's MEASURED Lean ÷ Verus at the median (RESULT §R2): Opus 2.22× · Sonnet 5.01×   — n = 3, one problem
  project  Opus ≥ $41.2 · Sonnet ≥ $61.9 per cell: BOTH ABOVE the $37.21 cap
  ceiling  6 × $37.21 = $223.26, plus each cell's overrun past the cap, UNMEASURED for this arm (no pilot cell reached it)
```
⇒ **All six cells are EXPECTED to end CAP-COST.** The result is then mostly a censoring fact on the cost axis: whether the arm fits the
pilot's budget on a second problem. A ratio carried from CRC-32 to LZW is an assumption about the arm, which is what the cells measure.
**(B), a higher cap for the Lean arm, is NOT registered here:** it changes what a Lean verdict asserts beside the pilot's, so it is the
Captain's word (the 2026-09-18 ① class (b)), asked only if this block's result says the budget is the whole story.

## §A9 · WHAT THIS BLOCK CANNOT ESTABLISH
- Two problems, n = 3 per model: no rate, no p-value, and nothing about Lean vs SMT in general.
- The pairing's ceiling is §A6's; "the same spec" means that, and the bounded decode half (deviation 4) is a declared difference.
- One trust base with x86lean is NOT met at this pin (Lean 4.31.0 here, 4.32.0-rc1 there), as in the pilot.
- If §A8 holds, a CAP-COST row says the arm did not finish inside the pilot's budget. It says nothing about whether it would have.
- Nothing here makes a claim about the salt method.

---
*Unsigned. The non-author read is asked; the release addendum names the export sha, the pool, and §A5's five owed receipts as met.*
