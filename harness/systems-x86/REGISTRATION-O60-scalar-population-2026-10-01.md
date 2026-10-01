# REGISTRATION — THE x86 LANE's FIRST POPULATION: 20 SCALAR PRIMITIVES, SPECIFICATION WITHHELD, FROZEN BEFORE ANY CARD IS BUILT
## bench (SaltBench lead), 2026-10-01. Objective O60, desk ZD. The Captain, 2026-09-30 12:2x, on O60 part 2's recommendation: *"yes,
## wonderful work, accept rec"*. The recommendation: grow O4 #1's CRC-32 proof of concept into *"a first population of about 20 scalar
## primitives (checksums, hash compression rounds, bignum limbs)"*, specification withheld, kernel-checked on x86lean, and *"pre-register
## the 20 tasks whose forms are all covered"*. The census is paris's (x86lean `docs/PRIMITIVE-CENSUS.md`, desk ZD's first act).
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ **NO MODEL CALL BEFORE THE RELEASE ADDENDUM (§Z10) NAMES THE EXPORT AND EVERY RELEASE
## CONDITION READS MET.** Signature and release are two acts. This document fires nothing and spends nothing.

---

## §Z0 · THE INPUTS
```
  1  ROW / MODEL     CLAUDE row only, claude-opus-5 — O4 #1's model, so CRC-32 stands beside this population on the same model (§Z4).
                     The AGY row is NOT registered here; it joins by its own addendum (its model is open while desk ZF watches for Gemini 4).
  2  POPULATION      20 tasks, DERIVED by rule from the census at x86lean dfb26e2 (§Z1). Not hand-picked.
  3  ARMS            plain · salt-diet: O4 #1's frozen x86 arm texts (ARM-plain.md f6e4ff132634 · ARM-salt-diet.md 2e69b6acc5c1),
                     changed per task ONLY by a registered substitution table (§Z2.6)
  4  EXTRAS          FIRST RUN: none — the subject writes its own specification, which is the question this benchmark exists for.
                     statement: registered as a later run on its own release addendum (it needs 20 withheld Lean statements).
  5  n               FIRST RUN: n = 1 per condition = 20 tasks × 2 arms = 40 cells. A population read, never a per-task result.
                     n = 3 is a later run, priced again from the first run's own cells.
  6  x86lean         dfb26e2 (= 50dee87's model and 1,158 vectors; the diff touches two docs and the census script only), vendored
                     STRIPPED as O4 #1 did (vendor_x86lean.py). Lean: the harness pin v4.27.0 if the vendored model builds there; if
                     not, the pin's move is its own addendum before release (§Z10 L2).
  7  REFEREE         O4 #1's referee generalised per task: executor (a) native under Rosetta, executor (b) the x86lean model, AGREEMENT
                     required per input, FUEL F = 2 (§X4's argument carries unchanged); TARGET for salt-diet (axioms propext ·
                     Classical.choice · Quot.sound only); SCREEN(spec) a gate; spec_strength a METRIC, never a gate (CARD-TARGET.md).
  8  CAPS            lane B §Q4, unchanged: C1_USD $37.21 · W1_SEC 144,000 · CAP-COST and CAP-WALL armed. Not scaled by task (§Z6 4).
  9  ACCOUNT         the pool evidence's day line names, per cell, read from ctl/run-cfg.tsv; one Claude cell on a pool dir at a time.
```

---

## §Z1 · THE POPULATION, AND THE RULE THAT DREW IT
The rule was written into `draw.py` before the script was first run. Its inputs are named by hash. Its output is the table below, unedited.
```
  R1  eligible = the census rows whose verdict reads ALL COVERED                                        40
  R2  exclude CRC-32's two rows (crc32-poc · zlib-crc32): O4 #1's function, already on record            −2
  R3  every remaining NON-s2n row is in                                                                 12
  R4  s2n fills to 20 across three strata read from s2n-bignum's own header prototypes, quota by
      largest remainder:  RETURN (no writable pointer) 7 → 2 · WRITE-FIXED (z[S2N_BIGNUM_STATIC n]) 8 → 3 ·
      WRITE-VAR (any other writable pointer) 11 → 3                                                       8
  R5  within a stratum, rank by sha256("O60-ZD|x86lean|<export full sha>|<row>"), take the first quota
```
**Inputs:** census `git show dfb26e28e00c:docs/PRIMITIVE-CENSUS.md` sha256/16 `76914f40057f24d6` (16,515 B; heading 40 of 57, 40 rows parsed) ·
s2n-bignum `include/s2n-bignum.h` at the census's commit `4d1356a74706`, sha256/16 `94cd42586fdb718d` (80,873 B, fetched, not vendored).
**Red control:** the same script on 50dee87's census (heading 41, rows 40) REFUSES, rc 1. Output: `evidence/o60-zd-registration-2026-10-01/population.tsv`.

| # | task (census row) | family | reference measured by the census | entry | ref. instrs | stratum |
|---:|---|---|---|---|---:|---|
| 1 | zlib-adler32 | checksum | spec + vectors (zlib C) | `adler32_z` | 284 | – |
| 2 | xxh64 | hash (non-crypto) | spec + vectors (xxHash C) | `XXH64` | 219 | – |
| 3 | murmur3-x86-32 | hash (non-crypto) | spec + vectors (smhasher C++) | `MurmurHash3_x86_32` | 96 | – |
| 4 | murmur3-x64-128 | hash (non-crypto) | spec + vectors (smhasher C++) | `MurmurHash3_x64_128` | 192 | – |
| 5 | lookup3 | hash (non-crypto) | spec + vectors (smhasher C++) | `lookup3` | 144 | – |
| 6 | siphash-2-4 | hash (keyed) | spec + vectors (SipHash C) | `siphash` | 257 | – |
| 7 | halfsiphash | hash (keyed) | spec + vectors (SipHash C) | `halfsiphash` | 235 | – |
| 8 | hacl-blake2s | hash compression | HACL* (clang of verified C) | `Hacl_Hash_Blake2s_update_multi` | 1,786 | – |
| 9 | hacl-blake2b | hash compression | HACL* (clang of verified C) | `Hacl_Hash_Blake2b_update_multi` | 2,108 | – |
| 10 | vale-poly1305 | MAC | Vale (the verified assembly) | `x64_poly1305` | 189 | – |
| 11 | vale-fsub | field arithmetic | Vale (the verified assembly) | `fsub_e` | 23 | – |
| 12 | vale-cswap2 | field arithmetic | Vale (the verified assembly) | `cswap2_e` | 58 | – |
| 13 | s2n-word_clz | bignum limb | s2n-bignum (the verified assembly) | `word_clz` | 6 | RETURN |
| 14 | s2n-word_bytereverse | bignum limb | s2n-bignum | `word_bytereverse` | 3 | RETURN |
| 15 | s2n-bignum_mod_n256_alt | bignum limb | s2n-bignum | `bignum_mod_n256_alt` | 94 | WRITE-FIXED |
| 16 | s2n-bignum_mul_4_8_alt | bignum limb | s2n-bignum | `bignum_mul_4_8_alt` | 93 | WRITE-FIXED |
| 17 | s2n-bignum_mul_p25519_alt | bignum limb | s2n-bignum | `bignum_mul_p25519_alt` | 139 | WRITE-FIXED |
| 18 | s2n-bignum_modadd | bignum limb | s2n-bignum | `bignum_modadd` | 31 | WRITE-VAR |
| 19 | s2n-bignum_sub | bignum limb | s2n-bignum | `bignum_sub` | 55 | WRITE-VAR |
| 20 | s2n-bignum_mul | bignum limb | s2n-bignum | `bignum_mul` | 47 | WRITE-VAR |

By source: s2n-bignum 8 · Vale 3 · HACL* 2 · spec-only 7. By family: bignum limb 8 · hash (non-crypto) 4 · field arithmetic 2 · hash (keyed) 2 ·
hash compression 2 · checksum 1 · MAC 1. *(The `ref. instrs` column is the census's count for the REFERENCE's code; the subject writes its own.)*

---

## §Z2 · WHAT EVERY CARD MUST BE — FIXED HERE, SO NO CARD IS FITTED TO AN ARM
A card is built from this section and the reference's own public contract, never from an arm's output. O4 #1's `card.md` is the template.
1. **REQUIREMENTS** in the customer's prose, naming the function by its public name and standard (e.g. *"BLAKE2s compression of whole blocks,
   as RFC 7693"*), with the standard's own check value where it has one. Never the reference's code and never a formal specification.
2. **SIGNATURE** = the reference's own C prototype under System V AMD64, as the census measured its entry. Preconditions (aliasing, size
   relations, key length) come from the reference's own documented contract, are printed in the card, and every withheld input meets them.
3. **ALLOWED INSTRUCTIONS:** ONE lane-wide list, the SAME on every task — derived by script from the pinned vectors: the scalar forms they
   execute (XMM-class forms excluded). A task-specific list would hand the subject a fingerprint of the reference. `bin/rt check` refuses a form
   outside it, at FORM level (mnemonic and operand classes, the census's own `form_of`). O4 #1's "also not" rules carry over (fs/gs, flags
   left undefined, alignment padding).
4. **STACK BAND K**, per task, DERIVED: the reference's measured maximum stack depth, rounded up to a power of two, minimum 256 (O4 #1's).
   A literal in the card and in the ascription; never read from the submission.
5. **OUTPUT EQUALITY:** exact output bytes and return register, UNLESS the reference's own contract defines its output only up to a stated
   relation (e.g. a field element not fully reduced). Then the card states that relation, the referee checks that relation, and the
   withheld expected values carry it.
6. **ARM TEXTS:** O4 #1's frozen texts with a per-task SUBSTITUTION TABLE (the file name, the entry symbol, the test-line format of
   `tests.txt`, and nothing else), applied by a builder that REFUSES any other difference from the frozen bytes. Both arms take the same
   substitutions, which keeps v3's neutrality rule.
7. **INTERFACE FAMILIES.** CRC-32's `Crc32X86Interface.CorrectFor` frames ONE shape: buffers read, a value returned. The population needs three:
   ```
     RET         registers in → value in rax          tasks 13 14
     READ-RET    buffers read → value in rax/eax      tasks 1 2 5, and CRC-32 (its family)
     WRITE       buffers read → an output region written (+ an optional return), AgreeOutside widened to exclude exactly that region
                                                      tasks 3 4 6 7 8–12 15–20 (3 4 6 7 write their hash through an `out` pointer)
   ```
   Each family is HARNESS-OWNED, names no task's function (so it is interface, not treatment), and ships with ONE kernel-checked control
   proof on a population task before release (§Z10 L4). The WRITE family is new; nothing in the lane has proved a memory-writing routine yet.

---

## §Z3 · THE WITHHELD REFERENCE, PER TASK
`gen_hidden.py` per card, as O4 #1's: inputs = the standard's published vectors where it has them, the boundary lengths (0 · 1 · block−1 ·
block · block+1 · several blocks, as the function's own block size defines them), the precondition edges, and seeded random inputs.
**Expected values come from TWO sources that must agree on EVERY input, or the task is not released:**
(a) the census's own reference at its pinned commit, built and run natively (the verified artifact itself for s2n-bignum and Vale; clang's
compilation of verified C for HACL*; the reference C for the spec-only rows); and (b) an independent implementation written from the public
standard (Python integers for the s2n and field rows, from the header's stated function; the RFC or paper text for the rest).
⚠️ **The reference column is not uniform and the RESULT says so:** for the seven spec-only rows, (a) is unverified C and the published vectors
are the only external anchor. A wrong expected value there would be shared by (a) and (b) only if both misread the standard the same way.

---

## §Z4 · THE ORDER
**Smoke first, never pooled:** the CRC-32 card rebuilt by the generalised kit, plain then salt-diet, n = 1. It checks the kit's plumbing
against O4 #1's own cells (same model, same card), and its pass or fail is NEVER quoted. Then the 20 tasks in an order ranked by
sha256("O60-ZD-order|<export full sha>|<row>"), each task's plain cell then its salt-diet cell, so any drift over the run falls on both arms.

## §Z5 · PREDICTIONS — REGISTERED BEFORE ANY CARD EXISTS
(i) salt-diet's CAP-COST incidence ≥ plain's, and **CAP-COST CENSORING of salt-diet on the largest tasks (8, 9) is EXPECTED**: O4 #1's
salt-diet cells cost $27.54–38.02 on a 12-instruction routine, one already over the cap. Censored cells are floors, never raised. (ii) every
salt-diet cell reaching TARGET reads the three standard axioms, or is refused at AXIOMS. (iii) no plain cell reads a `cell_translation` line.
(iv) every salt-diet cell reaching TARGET reports a spec_strength. ⛔ **No prediction about pass rate, spec_strength's value, or any premium.**

## §Z6 · CONFOUNDS — THEY TRAVEL WITH EVERY TABLE
1. **TASKS ARE NOT EXCHANGEABLE.** Reference size runs 3 to 2,108 instructions. No pooled rate is printed without the per-task table beside it.
2. **THE ARM TEXTS WERE WRITTEN FOR CRC-32.** Only §Z2.6's substitutions change them; whatever else in them fits CRC-32 better is part of the arm.
3. **PUBLIC FUNCTIONS.** Every task is a well-known function with public implementations, several with public proofs. Recall is uncontrolled,
   and it is arm-identical. This measures producing a correct and (for salt-diet) verified routine, never novelty.
4. **ONE CAP FOR ALL TASKS.** The pilot's cap is kept so cells stay comparable with O4 #1's. On large tasks it binds salt-diet first (§Z5 i).
5. **EXECUTOR (a) IS ROSETTA, not an x86 CPU** (as O4 #1). **The Lean pin** may differ from O4 #1's (§Z0 6); if it does, the smoke pair
   carries the difference and the RESULT names it.
6. **ONE MODEL.** Nothing here is about models.

## §Z7 · THE PRICE OF THE FIRST RUN — DERIVED, from O4 #1's twelve Claude-row cells (`price.py`, output `price.tsv`)
```
  inputs   RESULT-x86-crc32-claude-none-2026-09-26.md sha256/16 738ac1bb3f5a1576 · …-claude-statement-… 7b1a5968f2f952d6 (final_COST)
  plain      n=6  min 5.2591  median 7.6767  max 10.4989          salt-diet  n=6  min 27.5359  median 32.7704  max 38.0216
  40 cells   LOW $655.90 (20 × the minima) · CENTRAL $808.94 (20 × the medians) · CEILING $1,520.86 (40 × (cap 37.21 + overrun 0.8116))
  + smoke    2 cells, inside the same per-cell ceiling: ≤ $76.04
```
⚠️ **THE CENTRAL FIGURE IS BIASED LOW AND SAID SO:** its inputs are CRC-32 cells, a 12-instruction routine, and every population task's
reference is larger except tasks 13 and 14. **THE CEILING IS THE BINDING NUMBER**, because the cap stops every cell. Six of the twelve inputs are
`statement` cells, used because the `none` condition has only six. In pool points the price is evidence's to convert on its day line.

## §Z8 · VOIDS (faults only)
O4 #1's §X7 (lane B §Q7 rows 1–5 and 8–10; the cell build's refusals; REFEREE-FUEL → NOT-SCORED(HARNESS)) · plus: a task whose §Z10 L5 fails is
WITHDRAWN BEFORE ITS FIRST CELL by an addendum that names it, and the population is then 19 and said so. **A task is never withdrawn after a
cell of it has run.**

## §Z9 · WHAT THIS CANNOT ESTABLISH
No effect size and no premium (n = 1 per task, one model) · nothing per task beyond "this cell did or did not" · nothing about other models or
the AGY row · a PASS is behaviour on the task's withheld inputs plus, for salt-diet, a kernel-checked TARGET against the cell's OWN spec, whose
strength is a separate measured number; for plain a PASS says nothing about untested inputs.

---

## §Z10 · RELEASE CONDITIONS — each MET, with its receipt, in a release addendum before the smoke pair
```
  L1  EXPORT       ONE saltbench-systems sha carrying the generalised kit, the 20 cards with their withheld sets, the three
                   interface families and the substitution builder (§Z2)
  L2  x86lean      dfb26e2 vendored STRIPPED (the treatment-word walk at 0, controls fired); built at the harness Lean pin,
                   or the pin's move recorded by addendum
  L3  FORMS        the lane-wide allowed list derived by script from the pin's vectors; `bin/rt check` refuses a form outside it
                   (red drive with one uncovered form per family, e.g. a BMI/ADX form)
  L4  FAMILIES     RET · READ-RET · WRITE, each with a kernel-checked control proof of a population task at the pin
  L5  PER TASK     (a) = (b) on every withheld input · the reference itself through the referee: PASS, full agreement · a stub:
                   FAIL · the stack band derived, the equality relation stated
  L6  ARMS         the substitution builder's output for every task, refused on any non-table difference; one non-author read
                   of the table
  L7  DRY CELL     one per family, end to end at zero spend (build → fence → probe → referee on a stub)
  L8  POOL         evidence's day line names the pool; the account check and one authenticated read on it
```
**Proposed hands** (the helm routes; nothing here binds another seat): the kit and referee generalisation · `systems`; the vendoring and
the three family control proofs · `paris`; the 20 cards and withheld sets · `bench`. Whoever builds a release condition does not read it.
