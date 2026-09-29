# PLAN — O37's FIRST LEAN ARM: AENEAS (Charon + Aeneas, safe Rust → pure Lean), A PRICED SPIKE ON ONE PROBLEM. PLAN ONLY; NOTHING FIRES.
## bench (SaltBench lead), 2026-09-29. The Captain's word on the helm's recommendation, 13:0x: *"Let's do that."* The same Rust task verified two
## ways: the existing Verus arm, and Charon + Aeneas translating safe Rust into pure Lean with the specification as a Lean proposition, kernel-checked.
## The benchmark then measures the SMT-vs-Lean trade directly: automation, brittleness, the spec's reach into mathlib, one trust base with x86lean.
## ⛔ **A PLAN, NOT A FREEZE.** No cell is built or fired from this file. The fire is a later word, under its own dated registration.

---

## §A1 · WHAT WAS MEASURED, NOT READ (zero model spend)
The subset question was answered by running the tools on our own reference solutions (the plain, contract-free form of each pilot task's
withheld reference), not from their documentation.
```
  tool pair      Aeneas nightly 2026.09.29-b08bf81 (macos-aarch64 archive sha256/16 bafecbf9b69fa1ec), with its bundled Charon 0.1.273
                 (4bd5a29f6e97). Aeneas's Lean library build for the same nightly: archive sha256/16 67e6a2d80dda4e75.
  task      ref lines   charon   aeneas -backend lean   external definitions Aeneas's library does not model (left for the arm to supply)
  Crc32         54       rc 0     rc 0, 0 warnings       NONE
  LRU          111       rc 0     rc 0, 1 warning        Vec.pop · Vec.remove · Option's PartialEq · Option's Debug
  FreeList     188       rc 0     rc 0, 1 warning        Option's Debug
  LZW          103       rc 0     rc 0, 1 warning        Vec.as_slice · Vec.is_empty · MaybeUninit
  Paxos        377       rc 0     rc 0, 1 warning        Option's PartialEq · Option's Debug
```
- **CRC-32 is inside the subset with nothing left over.** Its reference uses `while` loops, a slice parameter, a `Vec<u32>` table and a derived
  enum. Aeneas emits the loops as its `loop` combinator (a partial fixpoint), and the derived `Clone`/`Debug`/`PartialEq` impls translate.
- The other four are CLOSE, not in. Each needs one to four library models that Aeneas leaves as external definitions. The `Debug` ones come
  only from the derived trace-logging impls. **This is a measurement of the REFERENCE; a subject's own solution can step outside the subset
  in ways the reference does not, and that rate is a finding of the pilot, never assumed.**
- **Not yet measured, and it is the spike's first act (§A5):** whether the emitted Lean for CRC-32 TYPECHECKS against Aeneas's library at
  its pin. That is a Lean elaboration over mathlib, so it runs under the fleet's one-heavy-job lock and is priced below, not done here.
- A source build of Aeneas was attempted first and is recorded because the arm's toolchain must be reproducible. Charon built from source at
  Aeneas's own pin (`e435e5f`) in 1 m 19 s and extracted the CRC-32 reference cleanly. Aeneas's OCaml dependencies did NOT build on this box.
  In a fresh opam switch, `ocamlbuild` segfaults on OCaml 5.3.0 and on 5.4.1, bytecode included, while an older switch's copy runs. **The
  arm therefore pins the published nightly binaries, not a local source build**, and the release registration names the archive shas.

## §A2 · THE PROBLEM: CRC-32
The helm's recommendation holds on the measurement. CRC-32 is the one reference inside the subset outright. Its spec also has a second,
stronger statement available in Lean: the CRC as a polynomial remainder over GF(2)[x]. That exercises the "reach into mathlib" axis,
which no other pilot task offers as cleanly.

## §A3 · THE SPEC PAIR, AND WHY THE HEAD-TO-HEAD USES ONLY ONE OF THEM
A benchmark that compares two arms under different specifications compares nothing. So:
1. **THE HEAD-TO-HEAD SPEC IS THE VERUS ARM'S OWN, TRANSCRIBED.** The Verus reference states `crc32(msg) == crc32_spec(msg)`, where
   `crc32_spec` is a bit-serial register: a reflected one-bit step with the reflected generator `0xEDB88320`, eight steps per byte from an
   initial `0xFFFFFFFF` register, then a final complement. The Lean arm's theorem states that Aeneas's translation returns `ok` of the SAME
   five definitions, transcribed one for one onto `UInt32`/`BitVec 32`. **Equivalence is by construction, and it is checked**: both spec
   definitions are evaluated on every hidden test vector and must agree, and the pairing file is read by a non-author before the first cell.
2. **Termination and panics:** the Verus arm proves no arithmetic overflow and termination (`decreases`). Aeneas's `Result` carries panics
   and its `loop` is a partial fixpoint, so a theorem of the form `= ok _` proves both, for every input. The two claims match. The Lean
   theorem is stated for every message (no length bound), as the Verus contract is.
3. **THE GF(2)[x] STATEMENT IS A SEPARATE, OPTIONAL CLAIM, NEVER IN THE HEAD-TO-HEAD.** "The bit-serial register computes the remainder of
   M(x)·x³² (with the init and final complements) modulo G(x)" is a theorem ABOUT the spec, not about the code, and it is strictly stronger.
   It is measured as its own row (reach into mathlib: does a subject reach for `Polynomial (ZMod 2)` and close it?), and it is never counted as
   a Lean-arm pass.

## §A4 · THE TOOLCHAIN PIN, AND THE ONE-TRUST-BASE CLAIM
```
  Aeneas / Charon     nightly 2026.09.29-b08bf81 binaries (§A1)
  Lean                leanprover/lean4:v4.31.0  (Aeneas's backends/lean/lean-toolchain)
  mathlib             the rev in Aeneas's backends/lean/lake-manifest.json at that nightly
  salt · x86lean      leanprover/lean4:v4.32.0-rc1
```
⛔ **"One trust base with x86lean" is NOT met at this pin.** The two Lean versions differ, and so do their mathlib revisions. The arm's trust
base is Lean v4.31.0's kernel plus Aeneas's library plus that mathlib. Closing the gap takes either an Aeneas nightly that moves to 4.32, or
x86lean at 4.31. That is a later act with its own price. Until then, a result says "kernel-checked in Lean 4.31", not "one trust base".

## §A5 · WHERE IT BUILDS, AND THE FENCE
- **The spike's first act (zero model spend):** typecheck the emitted CRC-32 Lean against the pinned library. Take the mathlib cache, unpack
  the Aeneas library build, then elaborate one file. It goes through the fleet build wrapper (one heavy job, the memory floor), on the box
  that will run the cells. Its receipt: the elaboration rc, the axioms the emitted file depends on (`#print axioms`), and the elapsed time.
- **In a cell:** the subject writes `solution.rs` (safe Rust, the fixed interface) and a Lean proof file. The harness, not the subject, runs
  Charon → Aeneas → the Lean check. The theorem STATEMENT is a harness-owned file whose bytes are hashed at landing, as in the statement arm,
  so a subject cannot weaken what it proves. A Lean elaboration inside a cell is a heavy job on the run box, so these cells run one at a
  time under that box's lock. That is already true of every Claude-lane cell (one per pool), but the lock is stated, not assumed.
- **The fence:** the reference proof and the pairing check's vectors live in the withheld tree, which every cell fence already denies.
  The toolchain directories (the nightly binaries, the Lean toolchain, the library and mathlib builds) are READ-ONLY entries on the cell's
  allowlist. The subject may READ the Aeneas library, which is public, and the fence must not deny it, or the arm measures a handicap.

## §A6 · THE PRICE
**Spike acts (§A5, first bullet): zero model quota.** One heavy-slot elaboration, plus a mathlib cache download (several GB, once).
**A pilot of the matrix's form:** CRC-32 × greenfield × `none` × the Lean arm × {claude-opus-5, claude-sonnet-5} × n = 3 = **6 Claude cells**.
The comparison arm already exists: the matrix's greenfield bare salt-diet (Verus) cells for CRC-32, at n = 3 for each model.
```
  anchor (RESULT-cost-tables-v3-2026-09-29.md $1, greenfield bare-salt-diet CRC-32 medians)   Opus ≥ $7.21 · Sonnet $4.79
  the Lean arm is new to both models, so the anchor is scaled ×1.5 to ×3 as a stated assumption, not a measurement
  expected  3 × ($7.21 + $4.79) × 1.5–3  =  $54 – $108            worst case  6 × $37.21 (the cost cap)  =  $223.26
  at 0.02794–0.03172 pt per USD  ⇒  expected 1.5–3.4 pt · worst case 6.2–7.1 pt
```
The agy lane's half (Pro, Flash) is a sibling plan once the Claude half's first cell is read, because the Gemini clients' tool use inside a
Lean proof loop is itself unmeasured.

## §A7 · WHAT THIS PLAN AND THE PILOT CANNOT ESTABLISH
- One problem, n = 3 per model: no rate, no p-value, and **nothing about Lean vs SMT in general**. It shows whether the arm is expressible,
  what it costs, and where it breaks.
- The subset measurement is of the REFERENCE. A subject's solution may fall outside it, and that is a pilot finding.
- The spec equivalence is by transcription plus a vector check. It is not a mechanised proof that the Lean and Verus spec definitions agree
  on all inputs. A reader who needs that is owed a separate lemma.
- "One trust base with x86lean" is not met at this pin (§A4).
- Nothing here makes a claim about the salt method.

## §A8 · ORDER OF WORK, EACH A SEPARATE WORD
1. This plan: a non-author read (kent). 2. The spike act (§A5, first bullet): zero spend, the heavy slot, its receipt posted.
3. A dated registration for the 6-cell pilot, written before its first call, with the harness items built red-first: the Charon → Aeneas →
Lean check inside the cell, the statement hash, and the fence allowlist. 4. The fire, on his budget line.

---
## ADDENDUM 1 (2026-09-29, bench) — kent's read (0 KILL · 1 DEFECT · 1 CITATION) and the helm's §A3 answer. §A3's text above is not edited.
1. **DEFECT TAKEN, §A3.1's vector check NAMES ITS INSTRUMENT NOW.** The Verus side's spec is `open spec fn`, which is GHOST code and never
   executes, so "both spec definitions are evaluated" had no instrument on one side. The check is: **the Lean transcription, executed, against
   the Verus REFERENCE's outputs on every hidden test vector.** The reference is Verus-verified to equal its spec for every input, so
   agreement ties the transcription to the Verus spec through the reference. That is weaker than a proof about the spec text, and it is
   the ceiling, because no single kernel holds both.
2. **CITATION TAKEN:** the Verus spec chain is SIX definitions, not five: `gen_poly` · `bit_step` · `bit_steps` · `feed_byte` · `run_from` ·
   `crc32_spec`. The transcription is of all six.
3. **THE HELM'S ANSWER (bus 13:30:10), recorded as given:** transcription plus vectors is enough for the SPIKE. A mechanised equivalence lemma
   is owed before the PILOT fires, and the pilot's RESULT may not call the two arms "the same spec" without it. The fallback if it proves
   hard: the two specs as distinct rows, never head-to-head.
4. **kent's finding on that answer (bus 13:30:54), recorded beside it, not ruled here:** under §A3.1 as written, the transcription IS the
   Lean arm's spec, so a lemma "transcribed spec = Lean spec" closes by `rfl` and certifies nothing about Verus. The fidelity crosses two
   kernels, and no single theorem in either tool can state it. Two checkable readings: (i) a lemma from the transcription to an INDEPENDENT
   Lean spec, such as the GF(2)[x] remainder (§A3.3's row, real and not trivial); (ii) the named vector check of item 1 plus the non-author
   read of the pairing file, the ceiling available. **Which lemma the pilot's registration owes is the helm's word. It does not block the
   spike act, which spends nothing.**
