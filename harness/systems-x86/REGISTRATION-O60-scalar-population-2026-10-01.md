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

---

## ✍️ NON-AUTHOR SIGNATURE — `kent`, 2026-10-01 07:14 PDT, on §Z0–§Z10 (transcribed by the lead from the bus; the signer's own signature file is in the fleet's private record)
Read at blob `3ed10c61fef7`, head `79cead7`, re-resolved at the forge. Re-derived by the signer's own runs: the census at dfb26e2 and the s2n header
at 4d1356a hash-equal to §Z1; `draw.py` → `population.tsv` BYTE-EQUAL, and rc 1 REFUSED on 50dee87's census; `price.py` → `price.tsv` BYTE-EQUAL;
the 2/3/3 quota by largest remainder; the families RET 2 · READ-RET 3 · WRITE 15 disjoint and complete. Three findings, answered in ADDENDUM 1.
**Bound of the signature, in the signer's words:** NOT READ were O4 #1's arm texts and card.md, vendor_x86lean.py, lane B §Q4/§Q7, the 12
non-s2n prototypes, and the model choice. The signature fires nothing; the fire is the Captain's word.

---

## ⚖️ ADDENDUM 1 — THE SIGNER's THREE FINDINGS AND THE HELM's WRITE SMOKE. APPENDED; §Z0–§Z10 and the signature are untouched.
bench (lead), 2026-10-01. No card exists yet, so nothing here follows data.
**1. A SECOND SMOKE PAIR, ON A WRITE TASK (the helm, 07:12; the signer concurs).** 15 of 20 tasks need the WRITE family, so a plumbing failure
there would read as a model failure across 75 % of the population. §Z4's smoke is therefore TWO pairs, plain then salt-diet, each n = 1, plumbing
only and never quoted: CRC-32 (READ-RET, the calibration against O4 #1), then **`s2n-bignum_mux`** (WRITE-VAR, 12 reference instructions,
`void bignum_mux(uint64_t p, uint64_t k, uint64_t *z, const uint64_t *x, const uint64_t *y)`). It was chosen BY RULE, not by eye: *the undrawn s2n
row in a WRITE stratum with the fewest reference instructions* (`evidence/o60-zd-registration-2026-10-01/smoke-write.txt`, using `draw.py`'s
own functions). It is not in the population, so its smoke cells sit beside no scored cell. **§Z10 L7's dry cells and L4's WRITE control precede
it**, and the 20 tasks fire only after BOTH smoke pairs read clean.
**2. THE PRICE QUOTED IS THE RUN AS REGISTERED: 44 CELLS (the signer's finding 1).** `price.py`, unchanged, with 22 cells per arm
(`price-44-with-smoke.tsv`): **LOW $721.49 · CENTRAL $889.84 · CEILING $1,672.95.** §Z7's 40-cell band stands as the population alone, and is
never quoted as the run's price. *(The signer's $1,596.90 was 42 cells, before this addendum's second pair.)*
**3. THE CEILING IS NOT A BOUND (the signer's finding 2).** Its overrun term (0.8116) is the largest of twelve CRC-32 cells. The cap is read on
the cell watcher's beat, so a cell can overrun by whatever it spends between two reads. On the largest tasks (8, 9) one stretch of work may cost
more than on a 12-instruction routine. **That overrun is UNMEASURED here**, and the ceiling is printed with this sentence beside it, as §Z7
already does for the central figure. Every overrun is printed and never clipped (lane B §Q4, unchanged).
**4. EVERY INTERFACE FAMILY READ FROM A PROTOTYPE (the signer's finding 3).** Each row's prototype, from its source at the census's commit:
```
  1  adler32_z         zlib 767c4c9 adler32.c:61     uLong adler32_z(uLong adler, const Bytef *buf, z_size_t len)                 READ-RET
  2  XXH64             xxHash 680bf46 xxhash.h:3705  XXH64_hash_t XXH64(const void* input, size_t len, XXH64_hash_t seed)          READ-RET
  3  MurmurHash3_x86_32  smhasher 07bb4de MurmurHash3.h:29   void (const void *key, int len, uint32_t seed, void *out)                WRITE
  4  MurmurHash3_x64_128 smhasher 07bb4de MurmurHash3.h:33   void (const void *key, int len, uint32_t seed, void *out)                WRITE
  5  lookup3           smhasher 07bb4de lookup3.cpp:28  uint32_t lookup3(const void *key, int length, uint32_t initval)             READ-RET
  6  siphash           SipHash 32d0676 siphash.c:89     int siphash(const void *in, size_t inlen, const void *k, uint8_t *out, size_t outlen)   WRITE
  7  halfsiphash       SipHash 32d0676 halfsiphash.c:82 int halfsiphash(… the same shape …)                                     WRITE
  8  Hacl_Hash_Blake2s_update_multi  hacl-star 504c298 Hacl_Hash_Blake2s.c:596  (uint32_t len, uint32_t *wv, uint32_t *hash, uint64_t prev, uint8_t *blocks, uint32_t nb)   WRITE
  9  Hacl_Hash_Blake2b_update_multi  hacl-star 504c298 Hacl_Hash_Blake2b.c:596  (uint32_t len, uint64_t *wv, uint64_t *hash, FStar_UInt128_uint128 prev, uint8_t *blocks, uint32_t nb)   WRITE
 10  x64_poly1305      hacl-star 504c298 internal/Vale.h:187  uint64_t x64_poly1305(uint8_t *x0, uint8_t *x1, uint64_t x2, uint64_t x3)    WRITE
 11  fsub_e            hacl-star 504c298 internal/Vale.h:185  uint64_t fsub_e(uint64_t *x0, uint64_t *x1, uint64_t *x2)               WRITE
 12  cswap2_e          hacl-star 504c298 internal/Vale.h:173  uint64_t cswap2_e(uint64_t x0, uint64_t *x1, uint64_t *x2)             WRITE
 13–20 and the smoke   s2n-bignum 4d1356a include/s2n-bignum.h (draw.py's own stratum reader)
```
The families stand as §Z2.7 printed them. ⚠️ **Two facts a card must carry, found here:** task 9's `prev` is a 128-bit argument, which System V
passes in TWO registers; and tasks 8 and 9 take a caller-supplied scratch block (`wv`), which the WRITE framing must count as part of the
written region, or AgreeOutside would refuse a correct routine. ⚠️ **Rows 10–12's prototypes are HACL*'s C declarations of Vale assembly**, which
is what a caller links against; the census measured the assembly itself.

---

## ⚖️ ADDENDUM 2 — A NINTH RELEASE CONDITION, L9: THE HOOK FIX OF DESK ZG. APPENDED; everything above is untouched.
bench (lead), 2026-10-01, on the helm's routing (07:21:34): *"hook-deny-v3 at 302ec0c deployed to the run box _bin, read back by blob"*.
**Why.** The O37 pilot's Bash hook refused 9 commands for nothing: Lean's `~~~` operator matched its `~user` rule (O37 RESULT §R7). Every
salt-diet cell here writes Lean, so the defect would fall on that arm alone. systems built the fix at saltbench-systems `302ec0c` (hook blob
`16f37ada78ed`), and kent read it 2026-10-01 07:21.
```
  L9  HOOK     the export of L1 carries the hook at blob 16f37ada78ed (or a descendant that kent or another non-author has
               read); every cell root this run creates renders its _bin from that export, and each root's hook is read back
               BY BLOB before its first cell. The O37 pilot's roots are evidence and are NEVER re-cut.
```
The fix does not stand in for a red drive in this lane: L7's dry cells exercise it on a Lean command that carries `~~~`.

---

## ⚖️ ADDENDUM 3 — ONE SENTENCE OF THE PLAIN ARM IS TASK-SPECIFIC, AND §Z2.6's TABLE CANNOT CHANGE IT. RULED HERE, BEFORE ANY CARD FREEZES. APPENDED.
bench (lead), 2026-10-01, found while building the first card (Adler32, the template) against §Z2.
**The finding.** O4 #1's frozen plain text (`ARM-plain.md`, blob `f6e4ff132634`) has one bullet of testing method whose example is CRC-32's
own oracle: it tells the subject to test a checksum against a reference vector or a bit-serial reference it computes itself. The
salt-diet text has no counterpart, so the sentence is the plain arm's own method. On 19 of the 20 tasks "bit-serial" names nothing
(no bignum, field or hash task has a bit-serial form), and on the CRC-32 smoke it is exact. §Z2.6's substitution table lists the file
name, the entry symbol and the test-line format, and "nothing else", so as registered the builder would REFUSE every card except CRC-32's.
**The three ways, and the one taken:**
```
  (A) keep the sentence verbatim on every task      an inapplicable CRC-specific example in the control arm of 19 tasks
  (B) a per-task example (e.g. arbitrary-precision  a per-task METHOD hint handed to the control arm alone, written by the lead
      arithmetic for the bignum rows)               who also wrote the cards: a treatment the registration never declared
  (C) ONE task-independent rewording, the same on   TAKEN. The example becomes "for a function with a published definition,
      all 20 tasks AND on both smoke pairs           against a reference you compute yourself from that definition". It is still
                                                    an oracle instruction, names no task's method, and is byte-identical across tasks.
```
**What (C) costs, declared:** the population's plain text differs from O4 #1's by this one sentence, so the CRC-32 smoke pair (§Z4,
ADDENDUM 1) calibrates the CARD and the kit against O4 #1's cells, NOT the arm text. Its plain cell's text differs from clbqcp01–03's
by that sentence, and the smoke's reading says so. §Z2.6's table gains exactly this one row (the sentence, the same replacement on every
task), and L6's one non-author read covers it. Every other byte of both arm texts stays as frozen.

---

## ⚖️ ADDENDUM 4 — HIS WORD ON THE FIRE, AND A TENTH RELEASE CONDITION. APPENDED; everything above is untouched.
bench (lead), 2026-10-01, from the council minute of 2026-10-01, item 5 (his words quoted there).
**His word: "yes fire".** The first run (§Z0: 40 cells plus ADDENDUM 1's two smoke pairs) FIRES as registered through ADDENDUM 3, once
§Z10's conditions are met, on a NEW-WEEK pool (one of the two the minute names, from Monday 2026-10-05). ADDENDUM 3 merged on that word (#300).
It does NOT fire before every release condition reads MET in the release addendum, and that addendum names the pool.
```
  L10  POOL     the cell pool's own config dir on the run box reads LIVE at the fire: an account check OK with both tokens
                present, and one authenticated turn (the pool-move and account-check form of O4 #1's ADDENDUM 4). A pool that
                reads BLANKED is never fired on. When none of the new-week pools reads LIVE, the release addendum NAMES the login
                the Captain must perform instead of firing. (Measured at the sitting: only one run-box pool dir read live; three
                read BLANKED.)
```

---

## ⚖️ ADDENDUM 5 — THE SALT-DIET TEXT CARRIES TWO MORE TASK-SPECIFIC FACTS THAN §Z2.6's TABLE. RULED HERE, BEFORE ANY CARD FREEZES. APPENDED.
bench (lead), 2026-10-01, found while inventorying O4 #1's frozen texts for L6 (`ARM-plain.md` blob `f6e4ff132634`, `ARM-salt-diet.md` blob
`2e69b6acc5c1`), against every byte that names CRC-32. The plain text's task-specific bytes are the file name, the `tests.txt` line format and
ADDENDUM 3's sentence, all three in the table already. The salt-diet text has two more, and as registered the builder would refuse every card
except CRC-32's:
```
  (1) the interface module's name     `Crc32X86Interface`, four times (counted in the frozen bytes): the module the subject must never edit. The population's interface is one
                                      of §Z2.7's three harness-owned FAMILY modules, so the name differs by family, not by task.
  (2) the spec's type and its gloss   `Submission.spec : List UInt8 → UInt32` and "what the routine returns for every message, stated in terms
                                      of the message's bytes only". The type is the card's own (Adler32's is `UInt32 → List UInt8 → UInt32`;
                                      a WRITE task's names its output region).
```
**Ruled, in ADDENDUM 3's form:**
- (1) The table gains ONE row: `Crc32X86Interface` → the task's family module, verbatim from the card's Proof deliverable section. It is an
  interface fact, the same file the card names, and it names no task's method.
- (2) The type is substituted verbatim from the card's Proof deliverable section, since it is the interface's own. The gloss becomes ONE
  task-independent wording, byte-identical on all 20 tasks and both smoke pairs: *"what the routine computes for every input the interface
  admits, stated in terms of those inputs only"*. It keeps the clause's rule (the spec speaks of the inputs, never the machine), and it
  names no task's method.
- **Kept verbatim, and declared:** the mutant examples "a wrong convention, a dropped byte, an off-by-one". They are examples of "plainly
  wrong" that apply to a byte or limb input as well as to a message, and they hand no task a method. `<Task>` and `docs/blueprints/<task>.md`
  are the kit's own placeholders, filled by its renderer as for every v3 task. They are not differences from the frozen bytes.
**What this costs, declared:** the population's salt-diet text differs from O4 #1's by the gloss sentence, so the CRC-32 smoke calibrates the
card and the kit, not the salt-diet text. ADDENDUM 3 already says the same of the plain text. Both arms take a table row, and neither table row
can carry method. L6's one non-author read covers both rows.

---

## ⚖️ ADDENDUM 6 — AS REGISTERED, 19 OF THE 20 TASKS CANNOT BE REFEREED. THREE CHANGES FOR HIS WORD, EACH WITH ITS MEASURED COST. APPENDED.
bench (lead), 2026-10-01. Every figure below is paris's or mine, measured on the private harness tree, at zero spend. **Nothing here takes
effect before his word, and nothing fires without the release addendum either way.**
**The finding (paris, the helm's order of 11:26:48).** At the registered pin, x86lean `dfb26e2`, the translator reads the reference routine
end to end for only 3 of 22 rows: vale-cswap2 and both smokes. Five rows are refused on clang's NOP padding alone. Twelve need a closed set of
instructions the model already has: adc · sbb · mul · bsr · bswap · shld · bts · btr · cltq. BLAKE2s/2b as the census built them carry SSE
`movups` (8 and 16 of them), which is outside the lane's own FORMS list. BLAKE2b's SSE-free build of (2) adds one more need, `rep movs`. Under §Z10 L5 ("the reference itself
through the referee: PASS"), a task whose reference the referee cannot read can never be released.
```
  (1) THE PIN    x86lean dfb26e2 → x86lean PR #79 as measured at head 57b445d. The pin names the merge commit only if its TREE equals 57b445d's;
                 otherwise the coverage is re-taken at the merge before the pin moves. The translator's CORE widened by exactly the measured
                 set. Every addition is checked by asm_front's own selftest, which translates all 1,158 vectors and compares each with its
                 hand-written instruction: 612 core EQUAL · 546 non-core REFUSED · 0 BAD, on both the LLVM and the GNU disassembler.
                 btc · xadd · shrd · xchg · repe/repne stay refused, because no reference executes them. Coverage at 57b445d
                 (TRANSLATE-COVERAGE-O60-widened-57b445d.tsv): 22 of 24 rows PASS, including every population task's reference
                 under (2). COST: merge #79, re-vendor (L2, scripted, ~1 min) and re-derive FORMS (L3, scripted; the vectors are
                 unchanged). CRC-32's smoke calibrates against O4 #1 across the move (§Z6 5).
  (2) BLAKE2's   tasks 8–9's source (a) becomes clang's compilation of the SAME verified C at the SAME commit with
      (a)        -mno-sse -mno-sse2 -D_FORTIFY_SOURCE=0. BLAKE2s: 1,827 instructions (census 1,786), 0 SSE forms (census 8).
                 BLAKE2b: 2,139 (census 2,108), 0 SSE forms (census 16). Each build's only branch relocation is the in-file update_block.
                 (Without -D_FORTIFY_SOURCE=0, BLAKE2b's copy becomes a call to __memcpy_chk, which clang does not inline once SSE is off.)
                 Both agree with (b) on every withheld input, and their stack bands are unchanged (K 256 · 512). The cards build
                 both with the flag (private harness tree, cards branch d60c252); on BLAKE2s the flag changes no instruction (disassembly cmp-identical). §Z1's ref.instrs column
                 stays the census's figure; the RESULT prints both. THE ALTERNATIVE: withdraw tasks 8–9 and draw two replacements by
                 §Z1's R5. That keeps the census's objects and changes the population.
  (3) RELATION   §Z2.5 already admits an output defined only up to a stated relation. This names the form the referee and the proof use.
      OUTPUTS    X86WriteInterface (paris, L4) takes `rel`, with `exact` the default. fsub_e is ≡ mod 2^255 − 19 over its 4 LE limbs (the
                 reference leaves 78 of 171 withheld outputs unreduced). x64_poly1305 with finish = 0 uses its accumulator relation
                 (≡ mod 2^130 − 5, top word below 5; the reference leaves 3 of 19 unreduced). Every other task is exact. expected.txt
                 carries the reduced value, and the referee checks the relation.
```
**And the list a subject sees moves with (1).** §Z2.3's lane-wide list was "the scalar forms the pinned vectors execute". It becomes those
forms **intersected with the forms the pinned translator reads**, by `make_forms.py derive --front <the pinned asm_front.py>` (paris, L3).
Without it a card would call a form "allowed" that its own referee refuses to translate, which is a non-scoring outcome on an allowed
instruction. Counted on every vector instance (no form is read in some instances and refused in others): at dfb26e2, 701 = 402 allowed +
299 refused; at #79's 57b445d, **701 = 507 allowed + 194 refused** (still refused, among others: xchg · bt · btc · div/idiv · lzcnt · tzcnt
· popcnt · rcl/rcr · shrd · cmpxchg · xadd · leave · movbe). `check` re-derives the list byte for byte, and both halves are derived, so no
form is typed.
**The lead's recommendation: all three.** Without (1) the population is one task. (2) keeps the population as drawn and is still the same
verified C at the same commit. (3) adds nothing that §Z2.5 did not already allow. **Each of the three is reversible by a dated addendum
before the fire.**

---

## ⚖️ ADDENDUM 7 — HIS WORD (a) ON ALIASING, THE CALL MODULE THAT FIXES EACH TARGET, AND FOUR PHRASES OF REQUIREMENTS PROSE. APPENDED; everything above is untouched.
bench (lead), 2026-10-01. **His word, 14:3x in the helm's window, on the fork put to him: "(a)".** ADDENDUM 6 merged on his earlier word
("yes, fire through addendum 6", 13:42; #307). Every object below is in the private harness tree, named by sha and blob, at zero spend.
**Why this addendum exists.** Wiring §Z10 L7 found that no salt-diet TARGET could be stated for an O60 task. §Z2.7's families are
parametrised (`CorrectFor … pre args …`, and for WRITE a `rel` and the spec's adapter), and no card fixed those terms in Lean. A subject
that wrote its own `pre` could write `pre := False` and pass. O4 #1 never met this, because its one interface baked its frame in.
```
  (1) THE CALL MODULE   (the helm's ruling, 14:10:50: it RESTORES §Z2.4's "a literal in the card and in the ascription"; not his word)
                        Each task's interface/<T>Call.lean is HARNESS-OWNED. It holds the task's SpecShape, Input, pre and args, and,
                        for WRITE, the adapter from the spec to the family's `f` and the `rel`. It is written from the card's printed
                        contract and frame.txt, with a source line named for every clause, and ends in ONE `abbrev Target prog image
                        entry spec`, with the card's K as a literal. The probe is two lines GENERATED from the task name. Each card's
                        Proof deliverable names its call module and the statement to prove. The arm texts do not move: the L6 table is
                        byte-equal, sha256/16 3041a0c3f51c14a9.
                        Driven per family (RET, READ-RET, WRITE): a real control proof stated against Target passes the probe, and a
                        planted pre := False submission builds against its own pre and is REFUSED by the probe. The fidelity read of
                        all 21 against their cards is paris's (19 HOLD, 2 findings, both closed by (2)). kent made a second,
                        independent read of the three author-adjacent modules, with his own mutants (pre := False; an argument
                        narrowed or reordered): all REFUSED.
  (2) ALIASING          (his word (a)) X86CallFrame gains `Arg.same i`, "the same pointer as argument i" (paris; blob 210ce6b4ec2a at
                        7e2d2ac, docstring-only over b8d2d4b; kent's read HOLDS). It binds its slot to its target's pointer, names no region, and adds no conjunct to
                        Setup, so it can bind a Target but never empty one. Red-first both ways: an in-place routine that stores before
                        it loads is REFUTED in-place and PROVED disjoint, and a safe one is PROVED in both. L4's three controls
                        elaborate unchanged. Each Target below is the CONJUNCTION over the calls its card permits:
                          Cswap2ValeCall          92ced1fbc909   disjoint ∧ p0 = p1
                          FsubValeCall            a01eb6fb7b2c   disjoint ∧ out = f1 ∧ out = f2 ∧ f1 = f2 ∧ out = f1 = f2  (mod-p rel)
                          BignumMul4x8AltCall     ea2915e731b7   disjoint ∧ x = y      (paris's finding F1, ruled under (a), 14:51:18)
                          BignumMulP25519AltCall  4c65c37de4e4   disjoint ∧ x = y
                        The cards' sentences stay AS WRITTEN; they now match what is checked.
  (3) DECLARED          (paris's F2) Read-only regions are pairwise disjoint in every Target. Overlapping READ-ONLY inputs are
                        TESTED, NOT PROVED, except where a card names the mode (2): Modadd x/y/m · Mul · Mux · Sub · SipHash24 and
                        HalfSipHash in/k. No write reaches a read-only region, so no correct routine is refused by this.
  (4) REQUIREMENTS ×4   (the helm's call, concurred 14:43:16: it ENFORCES v3's neutrality control 26) These four cards could build NO
                        view in EITHER arm, because REQUIREMENTS.md ships to both arms and carried a control-26 word. Reworded with
                        each card's own vocabulary. No contract, figure or check value moved.
                          Adler32         "so that our streams verify in any zlib-compatible reader"
                                        → "so that any zlib-compatible reader accepts our streams"
                          Murmur3X86_32   "The SMHasher verification above must give 0xB0F57EE3."
                                        → "The SMHasher acceptance check above must give 0xB0F57EE3."
                          Murmur3X64_128  "The SMHasher verification above must give 0x6384BA69."
                                        → "The SMHasher acceptance check above must give 0x6384BA69."
                          Xxh64           "the xxHash specification" (×2) → "the xxHash format document" (×2)
                        All 21 plain views and all 21 salt-diet views now build.
```
**What the release addendum reads with these** (the private tree, branch at 96c6458). Each is red-first or driven, and none of them is a
registration change:
- The builder ships X86CallFrame + the family + <T>Call as libs, and generates the probe.
- The method gate guards every harness-owned file and refuses one absent at the root. Its selftest drives each file by name; three mutants were refused.
- The referee takes salt-diet with those owned files. Driven on paris's RET control: CLASS PASS, AGREE=108, TARGET OK, axioms {propext,
  Classical.choice, Quot.sound}.
- The export allowlist now ships interface/frame.txt, which the builder reads by default and the allowlist lacked, plus O60's inputs.
- The fire route gains conditions `o60` and `o60smoke`.
- The TREATMENT needles are DERIVED from the references (156 for 21 tasks; the positive control reads every needle in its own reference), as the helm ruled at 14:43:16.
**Limits.** No proof of any aliased mode exists for FsubVale and the two Bignum muls. Cswap2's equal call is PROVED for the CONTROL's
routine at de04273 (paris: the reference's own routine, both modes of Cswap2ValeCall.Target), not for any subject's. What shows the form
is provable and discriminating is that proof and the frame's red-first package; the Targets' satisfiability on the routines is what the salt-diet cells test. spec_strength reads UNAVAILABLE on 19 of
22 tasks, because only three frames carry a `spec` directive. It is a metric, never a gate, and the RESULT prints it as "UNAVAILABLE
(frame carries no spec directive)", never as 0.

---

## ⚖️ ADDENDUM 8 — §Z10 AS MEASURED AT ONE EXPORT, 977a753. EIGHT OF TEN CONDITIONS MET; L8 AND L10 ARE OPEN, SO NOTHING FIRES ON THIS ADDENDUM. APPENDED.
bench (lead), 2026-10-01, 22:25–22:40 UTC. Every receipt below was taken at saltbench-systems `977a753` (EXPORTED-FROM
`977a7532955047705aa0204e0434dee4902907fc`), or at a commit that `977a753` contains. Each line names who measured it and where. Zero
model spend. **The release is NOT given here.** L8 and L10 are read on the new-week pool at the fire (ADDENDUM 4), and a later addendum
names that pool with both rows MET. Only then do the smoke pairs fire, then the 40.
```
  L1  EXPORT    MET  ONE sha, 977a753: systems' kit, the 20 cards and both smokes (22 task dirs, each with withheld/tests/expected.txt in
                     the private tree; the run box's cut carries 0 withheld dirs, by construction), the three family modules
                     (X86RetInterface · X86ReadRetInterface · X86WriteInterface) on X86CallFrame, the 21 call modules of ADDENDUM 7 (1),
                     and arm_builder.py. kent's non-author reads cover the harness delta through 977a753 and the objects each read names; the cards and call
                     modules are paris's read (kent read 3 of the 21). Read by NO non-author: the L4 control proofs and the aliasing red-first package
                     (kernel-checked, not read), and the withheld sets. The four cell
                     roots' _bin were RE-POINTED to this export
                     before any cell fired, after a measurement that all 36 link targets are byte-equal between ed1890c and 977a753 (0 of 36
                     differ). So the re-point changed the path a cell resolves and no byte it runs.
  L2  x86lean   MET  e5d7f36 (PR #79 merged; ADDENDUM 6 (1)) vendored STRIPPED, built at the harness Lean pin v4.27.0 (paris, harness
                     da9eca0, an ancestor of 977a753).
  L3  FORMS     MET  tasks/systems-x86/FORMS.tsv at 977a753, derived by make_forms.py from x86lean e5d7f36. Its own header reads
                     "allowed 507 · excluded 237 (SIMD/FP classes) + 194 (the pinned translator refuses every instance)", which is ADDENDUM 6's
                     701 = 507 + 194 over the vector instances. paris re-derived it with `check`, byte for byte.
  L4  FAMILIES  MET  RET · READ-RET · WRITE, each with a kernel-checked control proof at e5d7f36 (paris, da9eca0). The controls were re-pointed
                     at the harness call modules (paris, de04273, its own branch), and Cswap2's control proves both modes of its Target
                     (ADDENDUM 7, Limits).
  L5  PER TASK  MET  The referee, referee_o60.sh blob 447082fea41b, from the 977a753 cut, on all 22 rows (the 20, CRC-32 and BignumMux):
                     each reference PASS with full agreement ×22, each stub TESTS_FAIL ×22, and no REFUSE in any of the 44 logs. All 44
                     verdict lines are byte-identical to the first run at d3c4e00. Between d3c4e00 and 977a753 the withheld sets,
                     frame.txt, check_x86.py and frame.py are unchanged; only the referee moved (the salt-diet path and the TASKS check).
                     (a) = (b), the stack bands and the equality relations are the cards' own (ADDENDUM 6 (3) for the two mod-p rows).
  L6  ARMS      MET  `arm_builder.py table` over the 21 cards at the cut prints a table that is byte-equal to the one kent read (13:03:34 PDT), at
                     sha256/16 3041a0c3f51c14a9. The builder's selftest passes 16 of 16 arms.
  L7  DRY CELL  MET  (i) all 44 cells built --dry at 96c6458 (an ancestor; 96c6458..977a753 touches only referee_o60.sh and x86_clb.sh). (ii) On the
                     run box, at 977a753: --check-only CLEAN on one salt-diet cell per family plus the WRITE smoke, clbps01 Adler32 · clbps13
                     WordClz · clbps11 FsubVale · clbvs01 BignumMux, and on one plain cell, clbpp01 Adler32. Every one renders the pool's
                     settings with cleanupPeriodDays "read back = 3650". (iii) The referee on a stub per family, salt-diet, from the cut:
                     NO_SOLUTION ×4, with the TASKS-vs-export blob check passing ×4. Its red: one byte appended to one card in a scratch
                     TASKS copy gives rc 2, "REFEREE REFUSE: TASKS's card.md is not the export's".
                     ⚠️ NOT DRIVEN, by design: the probe TURNS, which are model calls. They run at each cell's own fire.
  L8  POOL      OPEN evidence's, at the fire: the day line names the pool, plus the account check and one authenticated read.
  L9  HOOK      MET  hook-deny-v3.sh at blob 16f37ada78ed in 977a753 (git hash-object), and read back BY BLOB in each of the four roots'
                     _bin after the re-point. fence-hook.sh is at e783a6b5ad11 in all four.
  L10 POOL      OPEN evidence's, at the fire: the pool's own config dir reads LIVE (both tokens, one authenticated turn). If none reads LIVE,
                     that addendum names the login the Captain must perform instead of firing.
```
**The run as it fires, 44 cells** (the dry stage's own count, by condition and arm): `o60` 20 tasks × {plain, salt-diet} = 40 ·
`o60smoke` BignumMux × 2 (ADDENDUM 1) · `smoke` CRC-32 × 2 (§Z4, O4 #1's calibration). **No task is withdrawn under §Z8:** L5 PASSes all 22 rows.
**A figure in ADDENDUM 7 is corrected here (ADDENDUM 7 itself is not edited):** the TREATMENT needles are **155 for 21 tasks**, not 156.
O60-NEEDLES.tsv reads 155 data rows at 96c6458, at ed1890c and at 977a753. The 156 was 213a5be's. 96c6458 dropped Lookup3's `0xFFFFFF`
when the generator was made to test absence with the TREATMENT gate's own substring rule: the needle is a substring of `0xFFFFFFFF` in the
harness's own Lean. Every other task's needle set is unchanged, and the positive control reads 21/21.
**spec_strength is unchanged from ADDENDUM 7's Limits:** "UNAVAILABLE (frame carries no spec directive)" on 19 of 22 rows, never 0. It is a
metric, never a gate.
**Declared, because a reader of the cells would otherwise have to ask:**
- **The population has TWO build shas.** clbps01, clbps11, clbps13 and clbvs01 were staged at ed1890c. clbpp01 was staged at 977a753, today,
  so that the plain arm's --check-only could be driven. No cell-facing byte differs between them (L1's 36 of 36), and every cell staged from
  now on is staged at 977a753. Each cell's manifest records its own export.
- **The plain cell's launch env has no Lean on PATH and the salt-diet cells' does.** That is the arm design: the route unsets the pinned Lean
  for the plain arm. It is not a defect.
- **The salt-diet referee path on a REAL submission** has been driven on paris's RET control (ADDENDUM 7: CLASS PASS, TARGET OK). Every other
  family's salt-diet verdict is first produced by a cell.
- **Monday re-runs --check-only on all five cells after the weekend's outlet drill**, which may power-cycle the run box, and before L8/L10
  are read.

## ⚖️ ADDENDUM 9 — THE CELLS' BELT DID NOT DENY THE FLEET'S MACHINE-STATE TREE, AND THE RETENTION RULE IS RAISED TO max(present, 3650). L1 MOVES TO 51bd1e9; NOTHING FIRES ON THIS ADDENDUM. APPENDED.
bench (lead), 2026-10-02, 00:58–01:10 UTC (17:58–18:10 PDT 10-01). Zero model spend, no cell launched, no staged cell written. The pool (L8, L10) is named by
ADDENDUM 10 at the fire, as ADDENDUM 8 said of "a later addendum".
**(1) The gap.** Found by `systems` on the run box (one staged fence parsed, rendered 15:27 PDT): the fence's sandbox `denyRead` (627 entries)
and its tool rules carried **0 entries under `~/.fleet`**, the fleet's machine-state tree: an API key, the cold spare, the lanes' pool env
files. `render_fence_v3.py` denies a fixed list of dot-directories and `~/.fleet` was not on it. Re-measured here, on all five staged cells:
the subject runs as the box's own user (`cell-claude.sh` execs the client with `env -i` and no user switch; all five cells are that user's,
on one `_bin`), and the tree is that user's, mode 700. **So the belt was the only layer that could deny it, and it did not.** The file-tool
hook (`fence-hook.sh`, blob e783a6b5ad11, unchanged) is an allowlist and already blocked it: `Read` and `Grep` of a path under `~/.fleet` read
`FENCE-OUTSIDE`, driven on a fixture cell. **No cell has fired on these fences**, so there is no exposure to declare.
**(2) The fix, two commits on 977a753.** `8704870` (systems' 6ace1f8, folded) named two children of the tree; `434a64b` (bench) denies the
WHOLE tree instead, because a named child cannot cover one born after the render, and the weekend's failover drill creates one. Nothing a
cell runs reads the tree: every use in the harness is the launcher's env file or the harvest, both outside the session.
- **Red backwards, selftest:** with 977a753's list the four tree arms FAIL (74 of 78); with the two named children, the arms for a child
  born after the render and for the pool env files FAIL (76 of 78); at 434a64b, 78 of 78.
- **Red then green, the belt itself,** under the pinned sandbox-runtime on the run box, a planted NON-SECRET probe file, removed after:
  the staged fence reads `<tree>/secrets/<probe>` and a probe directly under the tree with rc 0; the 434a64b rendering refuses both,
  `Operation not permitted`. Controls under BOTH: a file in the cell's own `repo/` reads rc 0, `~/.ssh` is denied.
- **The rendering's whole delta** (`--diff` against the staged fence of the plain cell): `denyRead` 627 → 628 and `denyWrite` 635 → 636,
  each `+` the tree alone; four tool rules added. Nothing else moved, so `$HOME` has not changed since the 15:27 render.
**(3) Retention, ruled by the helm 2026-10-01 15:59:21 PDT.** 977a753 wrote `cleanupPeriodDays` 3650 only when the key was ABSENT and kept any
present value. `2a5b4da` writes **max(present, 3650)** through `retention_want.py`, and a value that is not an integer REFUSES the route. Red
first, on the route's own block extracted from `x86_clb.sh` with fixture settings: present 30 reads back **30** at 977a753 and **3650** at
2a5b4da; 10000 → 10000 and absent → 3650 under both; "thirty" → REFUSE, rc 3. `retention_want.py --selftest` 11 of 11; the systems-x86
selftest 32 passed, 0 failed, 5 skipped (environment-gated, not passes).
**(4) What ADDENDUM 8 said that this moves, and what it does not.**
```
  L1  EXPORT    MOVES  to 51bd1e9 (EXPORTED-FROM 51bd1e9039a83606b446676ad08eb56a16582d5c). 977a753..51bd1e9 touches THREE files:
                       render_fence_v3.py, x86_clb.sh, and the new retention_want.py. 2a5b4da..51bd1e9 changes two COMMENTS and no
                       code line (kent's read found them stale). The four roots' _bin are re-pointed to the new export at the fire,
                       never before the drill's failback (below).
  L5  PER TASK  UNMOVED  referee_o60.sh is blob 447082fea41b at both shas.
  L6  ARMS      UNMOVED  arm_builder.py is blob f9ab01dc922d at both shas.
  L7  DRY CELL  OWED AGAIN  --check-only ×5 re-runs on the re-rendered fences (the order below). Its 15:27 receipts are of fences this
                       addendum supersedes.
  L9  HOOK      UNMOVED  hook-deny-v3.sh 16f37ada78ed and fence-hook.sh e783a6b5ad11 at both shas.
```
**(5) The order on Monday, and why it is this order.** A fence is a list rendered at a moment: an entry created under `$HOME` after the render
is outside it. The weekend's drill creates such entries on the run box. So: **the drill's failback → the run box's cells census diffs clean →
the _bin re-pointed to 51bd1e9 → the five staged fences re-rendered → --check-only ×5 → a non-author reads the delta → ADDENDUM 10 (L8, L10)
→ the smoke pairs → the 40.** The launcher re-renders every fence at the moment of use and refuses on any difference, so a fence left stale by
the drill holds the fire. It cannot launch it unfenced. That check is why the order is safe, not a reason to skip it.
**Declared:** the population's build shas become THREE (ed1890c ×4 and 977a753 ×1 staged, 51bd1e9 the route that fires them). The fence of
every cell is rendered at the fire by 51bd1e9's renderer, and each cell's manifest keeps its own staging export.
**Declared on kent's read (`kent`, non-author, 2026-10-01 18:09 PDT, at this addendum's first head 9c715e046cf6 against 977a753..2a5b4da):**
- **The renderer is shared.** The Gemini lane renders through `render_fence_v3.py` too, so its cells' belt now also denies the tree. The
  "nothing a cell runs reads it" measurement covered the Claude-lane cell scripts only. That lane's subject runs as a separate user, and it
  fires no O60 cell. UNMEASURED there, not claimed.
- **The v3 route's sibling, `clb_fire.sh`, still PRESERVES a present retention value.** It fires no O60 cell, and the ruling named the O60
  route.
- kent did NOT read the run-box receipts (the belt drive, the `--diff`, the uid ×5) or the systems-x86 selftest. Those are the lead's alone.

## ⚖️ ADDENDUM 10 — THE RE-CUT, THE HARVEST OF RECORD, ITS DECLARED LIMITS, AND THE FIRE (L8, L10). APPENDED.
bench (lead). Drafted 2026-10-02 (PDT), before any O60 cell fired. **Every line marked OWED is taken on Monday 10-05 in the order of (6),
and this addendum merges only when each reads MET or is declared below, before the first model call.** Zero model spend in everything
drafted here. The design it applies is `DESIGN-correctness-primary-2026-10-02.md` (PR #311): its §D2 classes, §D4 battery and §D5 harvest.
**(1) L1 moves to the re-cut.** ADDENDUM 9 named 51bd1e9. The export is re-cut from saltbench-systems ≥ `c2074e7` (2026-10-02 19:33, desk ZP's isolated native executor, over ≥ `6de3f4e` (18:5x: the merge of the harvest of record `f6cf86f` and systems'
ELSE-3/4 `acd7593`, because `x86_cell_fence.sh` runs on the fire route at `x86_clb.sh:414`; it was ≥ `b629652` (four one-line fixes on the merge `8eca9d8`, below))), the merge holding both
the cut's changes (`a3db4f6`) and the harvest of record (`53420bc`); `merge-base --is-ancestor` reads TRUE for each. **THE CUT, MET 2026-10-05: `c2074e7907ac`** (EXPORTED-FROM
c2074e7907ac08828f57d1d47c33350e87e602c0; 507 files, listing sha256/16 03e1927a4f65acad, 0 withheld-shaped names in the listing or on
the host; is-ancestor TRUE for a3db4f6, 53420bc, f6cf86f, acd7593, 6de3f4e, 51bd1e9 and b629652). The 40 run on these changes, each driven red-first on its own commit:
```
  de04273  the L4 control proofs re-pointed at the harness call modules                       harness
  b629652  N < 1 refuses (D2.14) · --limits prints the frame's blind spots (B6) · a LANDED end with no DECLARED line
           refuses (T2) · cell-watch --harvest RETIRED, refused at arm (C3)                                  harness
  c1172c7, e34db16  target.py: on timeout, kill the build's whole PROCESS GROUP (a grandchild held the fleet build lock)  harness
  782835d  the referee's RUNNER is the canonical build wrapper; its blob is printed per run           harness
  54d4fc8, 82ccbf8  the watcher logs its SNAPSHOT line unconditionally and runs no `git status`;
                    `bin/declare done` records the declared sha                                      SUBJECT-FACING (declare)
  dccb36f  the fence drive probes a WRITE into ../ctl (relative and absolute): denied, 0 landed        harness (drive)
  f386975  the watcher writes its cosmetic s<P> tag by update-ref, never `git tag`, which ran a
           cell-set core.editor / gpg.program outside the fence (0 of 1,882 cell configs armed it)  harness
  fc8c9df, 3518f30, a3db4f6  the watcher reads HEAD only from the cell's OWN store: no gitfile,
           symlink, commondir/gitdir, alternates or unlistable dir under .git, and HEAD^{commit}      harness
```
OWED: kent's non-author read of 51bd1e9..c2074e7 · the four roots' `_bin` re-pointed to the cut (the drill's failback is MET, (6)).
**(2) The harvest of record.** `harvest_o60.py` at saltbench-systems ≥ `f6cf86f` (blob 54ba19296281) with `classify_cell.py` 6f6e4b0cc223
(it was ≥ `ca74578`, blobs 5c49bf396275 / 22585074bc0c, until the rev-4 refuter's ELSE-1/ELSE-2 and kent's `primary` read moved it;
the three changes are below, under the primary outcome)
is the ONLY harvest of an O60 cell. No model-written cell is harvested by any other tool. Its classes are §D2's, with these readings, each
ruled before any O60 cell:
- **The commit each end is judged on.** The tree is materialised from that commit's objects in the cell's own store, never from a
  worktree. Each row is pinned by an arm of `test_harvest_pin.py` at the harvest's own sha, `53420bc`:
  ```
  LANDED        the end line's `landing-N <sha>`; watch.log's DECLARED line must EXIST and agree (absent REFUSES); a landed-N tag, if present, must peel to it
  DONE          the sha `bin/declare done` recorded, which must be on the history of the commit the session ended at
  EXIT-FORCED   the watcher's SNAPSHOT commit: HEAD at the kill, on any branch. EVEN AFTER A LANDING: the DECLARED landing is
                recorded and NOT judged (refuter B, round 4). This is a declared disposition, not a closed item. The cells are
                COUNTED SEPARATELY per arm, each with its landing sha (`SEPARATE EXIT-FORCED-AFTER-LANDING`), so the other
                reading is recoverable without a re-run (the helm, 13:58:33)
  a HALT end    the watcher's SNAPSHOT commit, HEAD at the stop
  ```
- **TREE is the SAME reading twice.** A re-referee rc 124 is the tree's only when the first run also read 124 at the same stage and BOTH
  builds are shown, by the build lock's own log, to have held the lock for the bound. Every other 124 is the QUEUE's: UNSCORABLE.
  The queue wait runs before the lock's bound and inside the referee's 1800 s, so without this a busy box charged the subject.
  No record twice is TREE; anything else is UNSCORABLE.
- **`Submission/Translation.lean` is the referee's.** The referee writes it, so a diagnostic there is UNSCORABLE. The root `Submission.lean`
  is the subject's in any spelling.
- **PASS with DISAGREE stays UNSCORABLE, as registered, and is COUNTED SEPARATELY per arm** (the table's `SEPARATE PASS+DISAGREE` line).
  A REJECTED reading for it waits on a later addendum with evidence. The two-seed probe (zero spend, n = 1, the G-battery's only such
  member) found that member's disagreement stable across seeds, AGREE at the native caller's register state, and its reference
  seed-invariant: the routine's, on that member.
- **REFUSED has a class.** A cell the harvest cannot pin or materialise for a cause IN ITS TREE or in a ref it owns is TREE: REJECTED on a
  declared end, HALTED on a halt, charge ARM, record NONE, `TREE-REFUSE: <cause>`. A cause counts only where it is PROVABLY the subject's
  act. The causes, all of them: a gitfile, symlinked or commondir `.git`; a ref whose exact name `show-ref` does not return once, or that
  does not peel to a commit; a parent directory that resolves elsewhere; an extracted path that is not a file, link or directory; a symlink inside `.git`; a pin its own store lacks; `down -`; a DONE sha off its history;
  a moved landing tag; and unsafe, absolute, outside, colliding or gitlink paths. **`SNAPSHOT -` stays REFUSED** (the helm, 13:47:05). The
  watcher writes it for an unresolvable HEAD, a rewired `.git`, and ANY failure of its `.git` enumeration, environmental ones included, so
  charging it to the arm would be an arm-correlated gate. A human disposes of it. A later split (the watcher naming which term refused) may
  make a subject-provable cause TREE. A refusal from the harness's own inputs stays REFUSED, and the table does not print.
- **`table --manifest` is REQUIRED,** and the manifest is the fire's own record of the cells it staged, never a typed count.
**(3) DECLARED LIMITS, each printed with its COUNT at harvest:** `TREE-REFUSE` rows, by cause · `FETCH-REFUSE` rows (a failed copy, named,
blocking the table until disposed) · `SEPARATE QUEUE-124` per arm · `SEPARATE PASS+DISAGREE` per arm · `SEPARATE EXIT-FORCED-AFTER-LANDING` per arm, with each landing sha · a DONE judged on the declared sha,
an ancestor by design · a missing SNAPSHOT line REFUSES · a failed control STOPS the harvest. The watcher's SNAPSHOT line is a RECORD; the
pin is the harvest's own resolution in the cell's own store. The watcher line was FROZEN at a3db4f6 after five routes were closed. A further
route is declared here with its count, unless the harvest fails to refuse it, and that one stops the run.
**(4) Not shipped, and what follows from it (the helm's ruling (3), 2026-10-02 11:43:46):**
- **The referee call has no wall bound and no cwd.** One non-returning routine wedges the harvest. The operator kills it and re-runs the
  remaining cells one by one; a hang has no emitter, so it is never a class. A routine that `.include`s a file assembles from the cell root
  only.
- **Cost does not govern run 1's reading.** No producer joins `post-end` cost into the row, so §D3 2's cost rules are produced by hand from
  the cells' own meter files or not at all, and this addendum claims neither.
- **The control is PLAIN only.** The Lean path is first exercised by a salt-diet cell. A salt-diet-only box failure reads HARNESS, so the
  whole arm lands in UNSCORABLE; this is the safe direction, declared.
**§D8 item 1 — MET (CLOSED by the helm, 2026-10-02 17:29:34).** The refuter pass on design revision 4 is on record, as this chain, each
link a post on the fleet record:
- systems' claim-by-claim non-author read of revision 4 against the code (15:49:57: 59 claims, 44 HOLD / 9 DIFFER / 6 flagged);
- the helm's sort of it (15:50:45);
- bench's fixes (16:05:59: saltbench-systems b629652 · design 9c4715d, blob d7134b44d479);
- ONE Fable refuter, non-author, over that revision 4 and this addendum (cccaedd2be4a) against b629652 (17:05:23: 15 HOLD, 6 of them with
  a limit · 1 REFUTED, the O1 text contradiction between the two documents · 5 further findings);
- bench's alignment (17:23:25: design e019464, blob d78c1f067ff1 · saltbench-systems f6cf86f);
- kent's non-author read of that delta (17:28:13, HOLDS).
**THE DEVIATION, DECLARED IN THE HELM'S WORDS:** §D8 item 1 reads literally "the re-fired refuter pass on this revision's blob". The pass that
ran was one Fable refuter over revised revision 4 + this addendum, AFTER a claim-by-claim read, and the alignment it forced was read by a
non-author rather than re-refuted. The merge of this addendum still waits on every other line marked OWED.
**§D8 item 3, MET at 53420bc:** the harvest driven end to end on two real cell records (a LANDED plain cell and a CAP-COST salt-diet cell,
from a fresh fetch, with the cut's harness at a3db4f6). Control ACCEPTED, both cells ACCEPTED, and the table printed under its manifest with
all three SEPARATE counts at 0.
**§D8 item 4 — the battery THROUGH THE CLASSIFIER (`harvest_o60.py battery` at 8eca9d8, plain, zero model spend), each member after its
task's control (ACCEPTED 44/44):** G2 22/22 REJECTED. G6c (the reference with a callee-saved register moved before every return) 22/22
REJECTED, and 20 of those read token PASS with every test passing and are rejected ONLY by the agreement column's clobber rider. On those
tasks the referee's token alone would call the violation a pass. G6b (one word written past the frame's stack band at entry) 22/22
REJECTED, ALL 22 with token PASS, rejected only by the MODEL-OUTSIDE rider. G6a (one byte into the guard before the first pointer argument's region)
20/20 REJECTED on the 20 tasks that take a pointer (2 NOT APPLICABLE by name), ALL token PASS and labelled MODEL-OUTSIDE. The native
executor ALSO saw it: its raw output reports `OUTSIDE=` on every member (on all inputs but one each). `agree.py` labels an input from
the model's class FIRST, so a write both executors see reads MODEL-OUTSIDE, and NATIVE-OUTSIDE appears only when the model returned clean. G7, the constant-pointer limit, is MEASURED from the referee's own lowered frames rather than built: of the 20 tasks that take a
pointer, 18 pass every pointer argument as ONE constant on every withheld input. On those, a plain routine that hard-codes its addresses is
ACCEPTED, as §D4's declared limit says. **THE SIGN (the helm, 15:41:24):** the salt-diet TARGET is
`CorrectFor`, which reaches `CorrectCall` (`X86CallFrame.lean`), and that holds `∀ ptrs`, over every separated placement of the regions. So
a routine that depends on the constant address cannot discharge TARGET, and on salt-diet it reads REJECTED. A plain routine faces no such
check. The limit can therefore only RAISE the plain arm's ACCEPTED count. **On these 18 tasks, an arm difference in favour of salt-diet is a
LOWER bound, and one in favour of plain may be inflated by up to the number of plain cells that rely on the constant.** The referee is kept
as registered. A post-run detector: re-referee each ACCEPTED plain cell with one shifted region base. G5 Adler32 is a PATH CONTROL (the helm, 15:51:51): the reference routine, a constant `Submission.spec`, and no `Submission.correct`. It
read `tests=PASS`, `AGREE=92`, token TARGET, `target_unknown = [Submission.correct]`, REJECTED for a MISSING OBLIGATION. It proves the
salt-diet Lean path runs at the cut. **The vacuous-spec property (a constant spec WITH a proof that discharges it) is NOT DRIVEN.** G5 on the other 21 tasks is NOT driven. G4 was
driven through the referee alone (the private tree holds it); each needs a per-task generator, and they are declared here.
**THE OUTCOME OF RECORD IS THE CLASSIFIER'S READING, NEVER THE REFEREE'S TOKEN (the helm, 14:53:49).** No table or figure, public or private,
reports a token count as a result. The token is in every log, so it is the number a later reader or script reaches for, and this battery
shows it calling a callee-saved violation a pass on 20 of 22 tasks. **The agreement rider, from the MODEL executor, is the SINGLE point of
detection for two G6 classes, callee-saved (G6c) and stack past the band (G6b): the native executor checks only regions and their guards,
by design, and reported OUTSIDE on 0 of 22 G6b members. A guard byte (G6a) has TWO detectors** (receipt: the battery's
BATTERY.tsv, blob 57f8ca6f386f, controls ACCEPTED on
every member). A change that weakens the model executor's frame silently re-opens
it, so **G6a, G6b and G6c are regression arms, re-run at any change to `exec_model.py`.**
**THE PRIMARY OUTCOME IS NOT COMPUTED ON RUN 1'S ROWS UNTIL ITS PRODUCER IS REFUTED (the helm, 15:50:45, O1).** The fire's table reports
per-row CLASS and the three SEPARATE counts only. The design's §D3 1 producer ((i)/(ii)/DISCORDANT) is landed and refuted on battery rows,
the two real cells and synthetic rows BEFORE run 1's rows are read; until then no rate is computed. The fire does not wait for it.
**BUILT at ca74578 (`harvest_o60.py primary`), refuted on synthetic rows (DISCORDANT, NO ENDED CELL, +s, u: 9/9 after 7 RED) and on the
two real cells against an answer derived by hand first, which it matched exactly.** Its reading is still not taken on run 1 until this
addendum's refuter verdict is on record.
**AND AT f6cf86f, red-first, after the rev-4 refuter (16:59) and kent's non-author read (16:56):** an arm label outside {plain, salt-diet}
REFUSES (it was counted in no rate); DISCORDANT is reserved for OPPOSITE strict orders, and a tie on one rate with a strict order on the
other prints `TIE-IN-(i)` or `TIE-IN-(ii)` (the helm, 17:19:11), quoting (i)'s order in none of the three; `battery` writes a REFUSED
row on any unforeseen error; `classify_cell.py --selftest` runs D2.14 and B6 (82/82). `test_primary.py` 17/17 (10 GREEN / 7 RED before).
**(5) The served-model guard.** The smoke pair's `model_served` must read the registered model, or the fire HOLDS: a newer model is priced
VOID by the cut's rate table.
**(5b) The native executor's reach (desk ZP, the helm 18:46:21) — MET 2026-10-02 19:33:40 (desk ZP DONE), a RELEASE CONDITION OF THE FIRE.** `exec_native` runs the
subject's routine natively, and until ZP closes, the translate gate is the only thing in front of it. Its completeness is a design review,
not a search. systems: (a) state whether the gate is an allowlist (closed by construction) or a denylist (open by construction), with a
hostile red-first battery, each member refused at translate beside a live control, and/or (b) run the native executor ISOLATED (no write
outside its scratch, no network, the harness tree read-only or absent). kent reads. The cut carries ZP's fix. **Default if unmet by
Sunday 20:00: the fire WAITS.**
**MET AT saltbench-systems `c2074e7`:** `exec_native` runs only under `exec_native.sb` (blob 3449b615af60): reads are an ALLOWLIST
("/" · WORK · /usr/lib · /System · /Library/Apple · /usr/bin/arch · /dev), and network, mach-lookup, fork, exec and writes are denied.
**DECLARED LIMIT:** file METADATA is readable everywhere (the launch aborts without it, bisected), so a routine can learn a path's existence,
size and times, never its content. Read by kent (19:12, 19:33: HOLDS). Controls under it: Crc32's reference, byte-identical to the
unsandboxed run, and the full referee PASS AGREE=82 (plain). The G5 Adler32 salt-diet member reads REJECTED at TARGET, tests=PASS AGREE=92,
its record identical to the unsandboxed run in 26 of 28 fields. The two that differ are run-identity, never a reading:
`work` (each run's own fresh work directory) and `target.spec_dependence.tail`, whose first line is the build queue's
`saltqueue: ticket P2 seat=… pid=…` (a per-run ticket id and process id). Its other two lines, `SPECDEP-CLEAN reached=242` and
`saltbuild EXIT=0`, are equal. No class, token, count, agreement, target error or blob field differs. **Bound: the salt-diet arm is controlled up to a REFUSED
proof; no salt-diet ACCEPTED was driven under the profile.** `target.py` is not inside the profile and the commit does not touch it.
(a), the translator's own correctness, follows Monday.
**(6) The order on Monday, and what each step leaves as a receipt (OWED):**
the drill's failback → the run box's cells census diffs clean → the re-cut (sha) → kent reads 51bd1e9..cut → deploy, `_bin` ×4 re-pointed
→ the five fences re-rendered → `--check-only` ×5 → the build lock's holder named (`lsof`) → **L8 and L10** (the pool, by the PM at the
fire; one authenticated read) → the smoke pairs (the served-model guard) → the 40. The harvest runs per cell after each end, from a copy,
never from a live worktree.
**(6) RECEIPTS, taken in order on 2026-10-05 (PDT):**
- **The drill's failback: MET.** The 10-03 drill was a reboot drill (run 2 PASS); no failover was in effect, and the failover drill
  is 10-10. On the run box: no client or seat loop running, the drill checker reading `idle`, both drills archived.
- **The run box's cells census: CLEAN.** Reference: the 10-01 15:27 render. In the four O60 roots, 124 of 1,355 entries postdate it,
  all of them clbpp01's own staging at 15:27–15:29; nothing later. Seven `$HOME` entries were born after the render, none inside a
  cell: five drill spare config directories, one further client config directory, and one directory of another seat's service.
  A preview with the cut's renderer (`--diff`, read-only, against the staged fences of clbpp01 and clbvs01) adds the six config
  directories and `~/.fleet` to both deny sets, and drops eight config directories that no longer exist in `$HOME` (retired on
  10-02 into `~/.fleet`, which the cut denies whole). The service directory is not a dot directory, so the belt does not deny it,
  like 460 other non-dot entries in `$HOME`. It holds no benchmark material. The file-tool hook, an allowlist, refuses it.
  Deny-by-default for `$HOME` is on the post-40 list, after its census (the helm, 2026-10-01 18:10:07).
- **The re-cut: `c2074e7907ac`**, as in (1). Of the 36 links in each root's `_bin`, 35 are byte-equal between 977a753 and the cut;
  `render_fence_v3.py` differs.
- **THE FIVE PRE-STAGED CELLS ARE RE-STAGED AT THE CUT (found 2026-10-05 at the object).** `bin/declare` is copied into a cell's
  repository at STAGING, while the watcher and every `_bin` tool come from the export at fire. All five cells staged before the cut
  (clbpp01 plain; clbps01, clbps11, clbps13 and clbvs01 salt-diet) carry 977a753's `bin/declare` (sha256/16 b45a8708ee618aa5; the
  cut's is 679d2bf55912df91). Under it, `bin/declare done` writes `down -` always, which (2) charges to the ARM as `TREE-REFUSE`.
  It is the only repository file in those cells that changed at the cut. The fire route does not check that a cell was staged at
  the current export. None of the five has fired, so none is run evidence: each moves whole out of its root (kept, never deleted),
  and each is staged again from the cut, with its `bin/declare` checked by hash before `--check-only`. A guard in the fire route
  is a harness change, so it waits until after the 40. After the re-stage, no cell staged at an earlier export remains.
