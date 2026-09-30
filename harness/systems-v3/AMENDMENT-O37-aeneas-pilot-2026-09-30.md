# AMENDMENT — O37's FIRST LEAN ARM: SIX CLAUDE CELLS, CRC-32 × GREENFIELD × LEAN-AENEAS × {OPUS, SONNET} × n = 3. FROZEN BEFORE THE FIRST CALL
## bench (SaltBench lead), 2026-09-30. The Captain's word at the 2026-09-30 sitting (ask 4, relayed by the helm): *the O37 Aeneas pilot fires
## this week*, on the pool the PM names in that day's re-cut. The plan is `PLAN-O37-aeneas-arm-spike-2026-09-29.md` (#287); this is its §A8 step 3.
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ **NO CELL FIRES BEFORE A RELEASE ADDENDUM NAMES THE EXPORT SHA AND THE POOL.**
## Signature and release are two acts, as in lane B, block N and step g.

**What this file is.** A new block (freeze **A**, blocks **AO** and **AS**) under `AMENDMENT-claude-lane-B-2026-09-16.md`, carrying that freeze's
machinery BY CITATION: the preflight (§Q3.4, with ADDENDUM 5's one-live-cell-per-pool rule), the confounds (§Q5), the reading rules (§Q6),
the void table (§Q7) and the deliverables (§Q9). The CELL FORM is a greenfield phase-1 build, as block N's. What is new is the ARM, and
every clause that differs from the freezes it cites says so and says why. The plan's text is not edited; where this file departs from it,
the plan's clause is quoted beside the departure (§A2).

---

## §A0 · THE INPUTS
```
  1  MODELS         claude-opus-5 (block AO) and claude-sonnet-5 (block AS), served per condition as lane B's cells were; read per cell from
                    the transcripts' message.model, head and sidechain apart.
  2  n              3 per model: 6 cells. Nothing is added, dropped or substituted.
  3  PROBLEM, FIELD Crc32 × greenfield, phase 1 only (no customer dispatch, no spec-change).
  4  ARM            lean-aeneas (§A1): the salt-diet method with the VERIFIER swapped.
  5  STATEMENT      GIVEN, harness-owned: `O37Spec.Statement` (§A1.2). REQUIREMENTS.md carries no statement section (ctl/card_extras = none);
                    the statement is a Lean file the gate protects.
  6  EXPORT         ONE bare sha of the harness tree, named in the release addendum BEFORE the first cell, that descends from the arm branch's
                    1f79021 (§A5 names every receipt at or below it) and carries the Claude-lane half of CORRECTION 3 (desk YT: the rc-3 split
                    and the dirty-tree HEAD note, 88b258d · 126085f · b9e7fe5, carried on this line). One sha for all 6 cells, recorded per cell.
  7  CLIENT PIN     lane B §Q0 row 5, unchanged: 2.1.259 by absolute path, its sha asserted per launch.
  8  TOOLCHAIN      one read-only root on the run box (§A4): Aeneas + Charon nightly 2026.09.29-b08bf81 (archive sha256/16 bafecbf9b69fa1ec;
                    library build 67e6a2d80dda4e75), Lean 4.31.0 (release tarball sha256/16 264105500c8abdf3), rust nightly-2026-09-17 in a
                    private RUSTUP_HOME (Charon's own pin), mathlib at the rev Aeneas b08bf81f2524's lake-manifest names.
  9  CAPS           the pricing profile's frozen cost cap, unchanged: C1_USD $37.21 on the cell's own meter; no turn cap (the Claude lane arms none).
 10  ACCOUNT        the pool the PM's re-cut names for O37 (the 2026-09-30 midday re-cut names ONE pool), NAMED PER CELL; the run box's account
                    check (identity string, never a directory name) reads OK with that pool's identity before each fire.
 11  FIRE ORDER     §A7: one live cell at a time; cell 1 is READ at its first in-cell Lean check before cell 2 fires.
```

## §A1 · THE ARM
### §A1.1 · Method held constant, verifier swapped
The Captain's objective is the SMT-vs-Lean trade (automation, brittleness, the spec's reach into mathlib). A head-to-head isolates the verifier only
if the METHOD is the same in both arms, so the arm file `render/CLAUDE.lean-aeneas.md` is DERIVED from `render/CLAUDE.salt-diet.md` by
`o37/make_claude_lean.py`: a fixed list of replacements, each required to hit exactly once, and a refusal if `Verus`, `vstd`, `verus-guide`,
`0 errors`, `trace_ok` or `verify.names` survives (`--check` rebuilds and compares). The swap:
```
  salt-diet (Verus)                                        lean-aeneas
  the Verus verifier is the referee                        the Lean kernel is the referee: Charon → Aeneas → Lean over solution.rs + proof/Proof.lean
  verify.sh: guard, verus, names                           verify.sh: the Lean guard over the proof, then lean-check.sh
  nothing is done until `0 errors`                         until `lean-check: GREEN`
  docs/method/verus-guide/ (the Verus manual in the tree)  the Aeneas Lean library in the read-only root (its loop lemmas, progress/step, scalar/slice/Vec specs), Mathlib beside it
  blueprint nodes: a frozen Verus statement                a frozen Lean statement (a theorem signature)
  class A/B examples in Verus terms                        the same classes in Lean terms (simp/omega/decide; induction on a List, a loop invariant)
  guard: admit, assume, external_body, …                   guard: sorry, admit, axiom, native_decide, bv_decide, ofReduceBool, implemented_by, @[extern], import, new syntax, kernel switches
  certificate: the guard line + `0 errors`                 the guard line + `#print axioms` naming only propext, Classical.choice, Quot.sound
```
The gate (`render/method-lean/docs/method/gate.sh`) is the salt-diet gate with the `.lean` screen (the Lean guard), an `unsafe` screen over `.rs`,
and `statement_check` in place of the ledger. It is installed and self-tested at render (`GATE_MUST_SAY_LEAN`), as the salt-diet gate is.

### §A1.2 · The statement, given
`docs/method/o37/Spec.part.lean`: the six Verus spec definitions (`gen_poly` · `bit_step` · `bit_steps` · `feed_byte` · `run_from` ·
`crc32_spec`, plan ADDENDUM 1 item 2) transcribed onto `BitVec`, and
```
  def Statement : Prop := ∀ msg : Aeneas.Std.Slice Aeneas.Std.U8,
      ∃ r, solution.crc32 msg = Aeneas.Std.Result.ok r ∧ r.bv = crc32_spec (msg.val.map (·.bv))
```
`ok r` carries no panic and termination (Aeneas's `Result` and its `loop`), for every message (plan §A3.2). The subject proves
`theorem O37Proof.crc32_correct : O37Spec.Statement` in `proof/Proof.lean`; `lean-check.sh` places it after the translation and the statement and
before `example : O37Spec.Statement := O37Proof.crc32_correct` and `#print axioms`.

### §A1.3 · PASS IS KERNEL-ONLY (the helm's concurrence, 2026-09-30 11:11:54)
The Lean half passes iff `#print axioms O37Proof.crc32_correct` names only `propext`, `Classical.choice`, `Quot.sound`. A proof that closes by
native evaluation is its OWN recorded class, never a pass. In Lean 4.31 `native_decide` and `bv_decide` mint their own axioms
(`<decl>._native.native_decide.ax_*`, `…_native.bv_decide.ax_*`), not `Lean.ofReduceBool`; the check classifies `*._native.*`, `Lean.ofReduceBool`
and `Lean.trustCompiler` as that class. **WRONG IF** a registered pass row carries any of them.

## §A2 · THE COMPARISON, AND ONE CORRECTION TO THE PLAN
**The plan, §A6:** *"The comparison arm already exists: the matrix's greenfield bare salt-diet (Verus) cells for CRC-32, at n = 3 for each model."*
**Corrected here, at the object:** "bare" is the matrix's `none` condition, whose subjects WRITE their own statement. The Lean arm's statement is
GIVEN, and the matrix already holds the Verus cells whose statement is given: the `statement` condition, whose REQUIREMENTS appendix is the Verus
reference's own spec chain, extracted verbatim (`tasks/systems-v3/Crc32/card.md` §Statement). ⇒ **THE COMPARISON IS `Crc32 × greenfield ×
salt-diet × statement`, claude-opus-5 and claude-sonnet-5, as of record in the census.** The RESULT names those cells and their verdicts.
**The departures that are NOT a verifier swap, declared so the reading can weigh them:**
```
  1  where the statement lives   Verus: an appendix of REQUIREMENTS.md the subject writes into solution.rs · Lean: docs/method/o37/, harness-owned
  2  refute / ratify             Verus statement cells were told to refute and ratify the given statement · Lean: one paragraph, "given, not on trial"
  3  iron rule 1                 Verus: revise a wrong statement under a new ratification · Lean: never revise it; flag it and say so on the bus
  4  the landing clause          Verus: tests/driver.rs carries the mutant traces the statement rejects · Lean: that clause is dropped with 2
  5  the statement's reach       Verus: crc32_spec plus trace_ok/check_trace (the trace predicate) · Lean: crc32_spec and the one theorem
```
(2) and (4) move COST between the arms, and the cost reading says so beside every figure. None of the five touches what the verifier accepts.

## §A3 · WHAT IS SCORED, AND FROM WHOSE BYTES
Per cell, from the export's harness, never from the cell's own copies:
```
  1  THE HIDDEN SUITE      score_claude_v3.py, unchanged (it carries the rc-3 split): the class, TESTS p/t.
  2  THE LEAN HALF         o37/o37_score.sh: the end tree's solution.rs and proof/Proof.lean COPIED to scratch; the HARNESS's lean-check.sh,
                           Spec.part.lean and Check.part.lean over the copy. O37-LEAN GREEN|RED with the stage, O37-AXIOMS verbatim.
  3  THE STATEMENT         O37-STMT: the cell's docs/method/o37/ and lean-check.sh against the harness's — UNCHANGED, or EDITED <files>.
  4  COST                  the modelled list-price dollars, as every Claude-lane cell (§Q9).
  5  WHERE IT BROKE        when the Lean half is RED: the stage (charon · aeneas · proof form · lean · axioms · native) and, for aeneas, the
                           external definitions the subject's code needed. A subject stepping outside Aeneas's subset is a FINDING, never a void.
```
**A Lean-arm PASS** is suite FULL PASS ∧ O37-LEAN GREEN ∧ O37-STMT UNCHANGED. The table prints each of the three beside the PASS, per cell.
The Verus comparison's pass is its own record's (suite and verification), read from the census, never re-scored here.
**No rate and no p-value** (plan §A7): per model, the two arms' cells side by side, with cost, where each broke, and the counts at n = 3.

## §A4 · THE FENCE AND THE SESSION
- The toolchain root is a READ-ONLY root: `render_fence_v3.py --ro-root` carves it out of denyRead and the tool rules and keeps it
  write-denied; the subject may READ the Aeneas library (it is public; denying it would measure a handicap, plan §A5). Every other arm's fence
  renders byte-identically (selftest arm).
- `cell-claude.sh` gives a lean-aeneas session `O37_ROOT`, and HOLDs by name if the root is not the Aeneas root; `--check` re-renders the fence
  with the same root. `fence-hook.sh` and `hook-deny-v3.sh` treat it as a toolchain root.
- `lean-check.sh` writes only inside the cell's own `.seat/tmp` (or TMPDIR); its cargo state is scratch. Measured with no model: GREEN under a
  Seatbelt profile that denies every write to the root (control: a write there is refused).
- The withheld tree (the reference proof, the vectors) is never in the export (the export's own withheld-name scan reads 0).

## §A5 · THE RECEIPTS, ALL AT ZERO MODEL SPEND
Arm branch of the harness tree, commits e2e84f8 · 008f351 · 02466ef · 0706a70 · 1a4d73b · 1f79021.
```
  toolchain       installed on the run box, INSTALL-RC=0, every archive by sha256 (§A0 row 8)
  pairing         ADDENDUM 1 item 1's instrument, built: 149 messages = every message the hidden tests log. The VERUS reference verified
                  (17 verified, 0 errors) and compiled by verus == the plain reference on all 149; the Lean transcription, taken mechanically
                  from Spec.part.lean and executed, agrees on 149/149 (o37_vector_dump.sh, o37_vector_check.sh). Controls: an unreflected
                  polynomial → 143 mismatches; one corrupted output → exactly that index; an empty vector file → refused.
  reference proof tasks/systems-v3/Crc32/G/withheld/reference/Proof.o37.lean, 271 lines, sha256/16 4b4038b1f7ff869f: GREEN under the
                  branch's lean-check, axioms propext · Classical.choice · Quot.sound. The task is feasible under the arm's rules.
  lean-check      o37_leancheck_selftest.sh 13/13: 11 RED arms (sorry · a sorry in a helper · wrong type · import · axiom · end O37Spec · macro ·
                  a modifier-prefixed axiom · no proof · no theorem · a charon failure), the reference GREEN, a native closure RED as its class.
                  Two false greens were found BY these arms and closed (an empty regex alternative that errors and prints nothing; a wrapped
                  #print axioms list read as empty); RED BACKWARDS on the first.
  gate            --selftest in a cell-shaped repo: arms 1 1b 1c 2 3 RED as required, 4 GREEN; a mutant with no statement_check fails arm 3
                  alone; a guard with no `sorry` fails arm 1 alone
  fence           render_fence_v3 --selftest 65 → 71 (six --ro-root arms, including byte-identity for every other arm)
  hooks           fence-hook 27/27, hook-deny 84/84, unchanged
  scorer          o37_score_selftest.sh 7/7: reference GREEN; skeleton RED on sorryAx; a statement weakened to True is GREEN in the cell's own
                  tree and RED from the harness's bytes with EDITED reported; every cell byte-identical after. RED BACKWARDS: a scorer reading
                  the cell's own statement fails that arm alone.
  build           a lean-aeneas cell built from an export of 0706a70 on the run box: the gate receipt carries arm 3 RED (statement edit) and
                  GREEN; hooksPath set; verify.sh RED on the sorry skeleton; in a COPY with the reference solution and proof, verify GREEN,
                  a track commit accepted, `gate.sh --landing` GREEN.
  CORRECTION 3    score_claude_v3 --selftest 29/29 on this line
```

## §A6 · THE SEPARATE ROW: READING (i)
The helm's re-ruling (plan ADDENDUM 2 item 1) owes a lemma relating the transcription to an INDEPENDENT Lean specification, such as the CRC as a
polynomial remainder over GF(2)[x], as its OWN row, never as the head-to-head. **Status at freeze: OPEN.** Owner bench; re-measured by
2026-10-02; the RESULT prints its status beside the head-to-head whether or not it is closed. It gates no cell: every cell is scored against the
given statement, and this row is about that statement's fidelity. The subjects are not asked for it.

## §A7 · FIRE ORDER, STOPS AND VOIDS
- **Order:** AO 1, then AS 1, then AO 2, AS 2, AO 3, AS 3; one live cell at a time on the named pool.
- **Cell 1 is read at its first in-cell `lean-check` run** before any other cell fires. If the check fails for a reason that is the harness's (the
  root unreadable in the fence, a toolchain resolution failure, a scratch refusal) and not the subject's, cell 1 is stopped, it is
  NOT-SCORED(HARNESS) under §Q7, the cause is fixed on a new export named in an addendum, and the replacement is the registered re-fire `r1`
  (block N ADDENDUM 13). A subject's Rust that Charon or Aeneas cannot translate is the subject's, and it is scored.
- The cap, the watcher and the voids are lane B's (§Q7), unchanged.

## §A8 · THE PRICE
```
  anchor   RESULT-cost-tables-v3-2026-09-29.md $1, greenfield Crc32 statement-salt-diet medians: Opus $6.25 · Sonnet $4.16
           the Lean arm is new to both models, so the anchor is scaled ×1.5 to ×3 as a STATED ASSUMPTION, not a measurement
  expected 3 × ($6.25 + $4.16) × 1.5–3  =  $46.85 – $93.69
  worst    6 × $37.21 (the cost cap)     =  $223.26
```
Points are the PM's per pool (its re-cut gives the named pool ≈ $20.7/pt: ≈ 2.3–4.5 pt expected, 10.8 pt at the cap). Any cell that runs after
that pool's weekly reset lands in its new week (the PM's line).

## §A9 · WHAT THIS PILOT CANNOT ESTABLISH (plan §A7, carried, plus what the build added)
- One problem, n = 3 per model: no rate, no p-value, and nothing about Lean vs SMT in general.
- The spec pairing is transcription + a 149-vector check against the Verus reference's outputs + a non-author read of the pairing file. That is
  the ceiling, because no single kernel holds both specs (plan ADDENDUM 1 item 4). The two arms may be called "the same spec" in that sense only.
- One trust base with x86lean is NOT met at this pin (Lean 4.31.0 here, 4.32.0-rc1 there): a result says "kernel-checked in Lean 4.31".
- The five departures of §A2 are real and are read beside every figure.
- The Lean guard refuses `bv_decide` as a token even where its preprocessing alone closes a goal (no native axiom); the gate is stricter than the
  certificate there, and the RESULT says so if a subject meets it.
- Nothing here makes a claim about the salt method.

---
*Unsigned. The non-author read is asked of kent; the release addendum names the export sha and the pool.*

---
## ADDENDUM 1 (2026-09-30, bench, before any signature) — kent's blocking finding, the helm's ruling, the fix, and §A6 CLOSED. §§A0–A9 are not edited.
1. **THE FINDING (kent's non-author read, DRIVEN on the real script at 1f79021).** `lean-check.sh` read the FIRST axioms header in Lean's
   output, and the proof elaborated before the check, so a `sorry` proof plus one forged `#print "'O37Proof.crc32_correct' depends on axioms:
   [propext]"` read GREEN, and the scorer, running the same script, scored it a PASS. The pairing (§A1.2 against the reference's six
   definitions) HOLDS line for line in the same read.
2. **THE RULING (the helm, 2026-09-30 11:44:21): the SECOND-PROCESS form.** Built at harness 5ac4950:
   - the proof is BUILT as a module (`O37Check` = the translation · the statement · the proof, `lean -o`); its messages are shown and an
     error is RED, but none is parsed for the verdict;
   - a SEPARATE Lean process runs a harness-owned file = `import O37Check` + the check part, and exactly ONE axioms report, at the check's own
     line, is required. Measured before relying on it: the importer sees the proof body (a `sorry` proof reads `sorryAx` through the import).
   - the check's names are `_root_.`-absolute: inside a namespace the proof leaves open, an unqualified name resolved to the proof's own
     shadow (measured).
   - the form screen FAILS on anything that runs code at elaboration (the module build runs outside the fence when the scorer runs it):
     imports, new syntax or elaborators, `#eval` `#exit` `#guard`, `run_tac` and its kin, `IO.`, unsafe, `implemented_by`, `@[extern]`, kernel
     switches, axioms, and any attribute off an allowlist (`@[command_elab]` could otherwise replace `#print axioms` itself). It only FLAGS
     `#print` `#check` `trace` `sorry` in the record, never as a verdict, per the ruling. **WRONG IF** any text in Proof.lean can turn a RED
     into a GREEN.
3. **THE ARMS (selftest 19/19 at 5ac4950):** §A5's 13, plus forged-print (kent's), forged-trace (Mathlib's `trace` tactic prints the same
   forgery through a door the screen does not close, so only the second process stops it), an open-namespace shadow of both names,
   `@[command_elab]`, `#eval IO.println` of the forgery, an unterminated comment. **RED BACKWARDS:** against 1f79021's check, forged-print,
   forged-trace and eval-print all read GREEN.
4. **§A6 IS CLOSED: the reading-(i) lemma is PROVED.** `harness/systems-v3/o37/GF2.lean` (sha256/16 35695df1c903be19) proves
   `theorem crc32_spec_eq_gf2 (msg : List (BitVec 8)) : O37Spec.crc32_spec msg = crc32_gf2 msg` for EVERY message, kernel-only
   (`[propext, Classical.choice, Quot.sound]`), in ~5 s. The independent definition, stated so a reader can judge its independence:
   G written term by term (x^32 + x^26 + x^23 + x^22 + x^16 + x^12 + x^11 + x^10 + x^8 + x^7 + x^5 + x^4 + x^2 + x + 1) in
   `Polynomial (ZMod 2)`; M a finite sum giving bit k of the byte-wise LSB-first bit sequence the coefficient of x^(L−1−k), L = 8·len;
   J = Σ_{i<32} x^i; R = (M·x^32 + J·x^L) %ₘ G; crc = reflect32(R) xor 0xFFFFFFFF. No register or shift appears in it. Its six-definition
   span is byte-identical to Spec.part.lean. A mutation (one wrong term of G) breaks the proof, so the theorem rests on the independent G.
   It is still its OWN row and never the head-to-head (plan ADDENDUM 2); it strengthens §A9's pairing limit, which now reads: the
   transcription agrees with the Verus reference on 149 vectors AND is proved equal to the textbook GF(2)[x] definition.
5. **THE RECEIPTS, re-run from ONE export (5ac4950) on the run box:** a lean-aeneas cell builds (gate receipt: arm 3 RED as required,
   selftest GREEN); lean-check selftest 19/19; scorer selftest 7/7; on a COPY with the reference solution and proof, `verify.sh` GREEN,
   a track commit accepted, `gate.sh --landing` GREEN; GF2.lean kernel-only. §A0 row 6's export must descend from **5ac4950**, not 1f79021.

---
## ADDENDUM 2 (2026-09-30, bench, before any signature) — kent's delta-read findings, the helm's CONTAIN-AND-RE-CHECK ruling, built at harness c122a11. ADDENDUM 1 item 2's mechanism is REPLACED as below; nothing above is edited.
1. **THE FINDINGS (kent, DRIVEN on 5ac4950):** (a) the form screen was line-anchored: `/- c -/ #eval …` and `… := trivial #eval …`
   passed it, and both RAN `Process.run` in the module build, which at scoring runs outside the cell fence; (b) an `initialize` in
   the subject's module does not run at the build and DOES run at IMPORT in a normal Lean frontend, so the importing `#print axioms`
   file of ADDENDUM 1 ran subject code. kent's GF(2) independence read (item 4 of ADDENDUM 1) JUDGED the definition independent,
   with one citation correction: the six DEFINITIONS are identical to Spec.part.lean; the SPAN is not (one docstring line differs).
   ADDENDUM 1 item 4's "span is byte-identical" should read **definition-identical**.
2. **THE RULING (the helm, 11:59, amended 12:00): stop screening text; CONTAIN and RE-CHECK.** Built:
   - **CONTAIN.** With `O37_CONFINE=1`, which the scorer sets, every process that loads subject code (Charon, Aeneas, the module build,
     the re-check) runs under ONE Seatbelt profile: writes only inside the check's scratch dir, no network, exec only inside the
     toolchain root. The profile is tested before each use: an exec outside the root must be denied, or the check is RED. In a
     cell, the fence is the containment.
   - **RE-CHECK.** `o37/O37Axioms.lean` is a harness Lean PROGRAM (`lean --run`), and it elaborates nothing of the subject's. It
     imports the built module with `loadExts := false` and never enables initializers. It replays every constant the module
     declares through the KERNEL (`Lean.Environment.replay`), on top of the module's own imports. It requires
     `O37Proof.crc32_correct` to have exactly the type `O37Spec.Statement`. Then it walks the theorem's axioms by hand over the
     KERNEL environment. That last choice is measured, not assumed: `replay`'s returned wrapper does not see the replayed constants
     through `find?`, so a collector reading the wrapper would report no axioms at all, a false green.
   - The text screen is now a FLAG in the record, never a verdict. The harness file `O37Axioms.lean` replaces `Check.part.lean`
     everywhere that file was used: the statement tree the gate protects, cell_build's byte-equality assert, and the scorer.
3. **THE ARMS, from export c122a11 on the run box.** Selftest 19/19 unconfined (in-cell mode); 24/24 under `O37_CONFINE=1`
   (scoring mode), adding kent's two `#eval Process.run` forms and an `initialize` that writes a file. Each reads RED, and **every
   target file is ABSENT after the whole check**. The earlier RED arms keep their RED under the new stages: forged text from the proof
   cannot reach the verdict, a type other than `O37Spec.Statement` fails at TYPE, and a missing or namespaced theorem fails at REPLAY.
4. **RECEIPTS, all from ONE export (c122a11):** a lean-aeneas cell builds (gate arm 3 RED as required); lean-check selftests 19/19 and
   24/24; scorer 7/7; on a copy with the reference solution and proof, `verify.sh` GREEN and `gate.sh --landing` GREEN; `GF2.lean`
   kernel-only. **§A0 row 6's export must descend from c122a11.**
5. **WRONG IF** any text in `proof/Proof.lean` can turn a RED verdict GREEN, or any code in it can write outside the scratch dir or
   exec outside the toolchain root while the scorer runs.

---
## ADDENDUM 3 (2026-09-30, bench, before any signature) — the three USE-TIME containment controls (kent's delta read #2, ruled 12:18). Harness 6004ebe.
1. **THE FINDING (kent, by reading):** the re-check reads SOUND as written. The profile's use-time self-test proved only the exec
   denial; the write and network denials rested on the profile's text and on arms run after the fact. kent declared he did NOT probe
   the profile adversarially: a null in his read is not clearance of the sandbox.
2. **THE RULING (the helm):** all three denials get a use-time positive control; each must fail, or the run is RED.
3. **BUILT (every scoring run, before any subject code loads):**
   - **EXEC:** `/usr/bin/true`, outside the toolchain root, is refused.
   - **WRITE:** the root's own `lean` writing an `.olean` one directory ABOVE the scratch dir fails and leaves no file. The same write
     INSIDE the scratch dir succeeds; that is the control's other half.
   - **NETWORK:** `o37/O37NetProbe.lean`, a harness `lean --run` program, makes one UDP connect to 1.1.1.1:53. It must CONNECT
     unconfined and be REFUSED confined. If it cannot connect unconfined, the network control is UNMEASURED and the run is RED.
     Measured before wiring: it connects unconfined; confined it gets "operation not permitted".
4. **THE CONTROLS' OWN RED ARMS, from export 6004ebe.** Three mutants of the check, each with exactly ONE denial deleted from the profile
   (the removed-line count is printed and must be 1). Each reads RED and names its own denial: *did not deny the network (NET-PROBE
   connected)* · *did not deny a write outside the scratch dir* · *did not deny an exec outside the toolchain root*. (The first cut of
   these arms removed NOTHING: in ERE the parentheses of `(deny network*)` are grouping. The printed count of 0 exposed it; they now use
   fixed strings.)
5. **RECEIPTS from ONE export (6004ebe):** a cell builds (gate arm 3 RED as required); selftests 19/19 in-cell, 24/24 scoring mode (the
   escape arms' target files absent); the three mutants RED; scorer 7/7; reference landing GREEN; GF2.lean kernel-only.
   **§A0 row 6's export must descend from 6004ebe.**
6. **STILL NOT CLAIMED:** an adversarial review of the Seatbelt profile as a boundary. The controls prove that each denial is in force
   at use time. They do not prove that no path around the profile exists.

---
## ADDENDUM 4 — SIGNED AND RELEASED (2026-09-30 12:37 PDT, bench, before the first model call)
1. **SIGNATURE.** Three non-author reads by kent: #293 at blob 770342102ae0 (one blocking finding, closed by ADDENDUM 1), the delta at
   0e99b838d24b (findings closed by ADDENDUM 2), the delta at 15094975ee7d (findings closed by ADDENDUM 3), and the delta at a65ba8bcfaf2,
   which he read **CLEAR BY READING** (2026-09-30 12:35:28). The helm's ruling of 12:18:56 reads: *"kent reads that one delta, then the
   registration is SIGNED and the pilot FIRES"* on the pool the PM named. **This file is signed as of ADDENDUM 3.**
2. **THE HELM'S WRONG-IF, carried as a stop (12:18:56).** If any pilot cell's process writes outside its scratch dir, connects out, or execs
   outside the root, that cell is **VOID (not RED)**, the pilot halts, and the adversarial Seatbelt review moves ahead of any further run.
   That review is a SEPARATE row, owed before any run whose subjects are not our own. It never gates this pilot.
3. **RELEASE.**
   - Export **6004ebe** (6004ebef3b36): one export for all 6 cells, a dest of its own on the run box. 388 files, 0 withheld-shaped names.
     The run box's Verus binary sha equals the build host's (7a7b319b170692d3). Its toolchain root is §A0 row 8's.
   - The pool: the one the PM's 2026-09-30 midday re-cut names. The run box's account check reads **OK** on the lane env's config
     (identity string equal to the named pool's, access and refresh present). The launch is what proves it authenticates, and the fire's
     sandbox probe is that launch.
   - The client pin, the cap and the watcher are §A0's, unchanged.
   - **Scoring needs the scorer's box to reach the network UNCONFINED** (kent, 12:35:28). Otherwise the network control is UNMEASURED
     and every run reads RED. That fails closed, and it is stated here so nobody reads such a RED as a proof failure.
4. **FIRE ORDER, as §A7:** AO 1 first, alone. It is READ at its first in-cell `lean-check` before AS 1 fires.

---
## ADDENDUM 5 (2026-09-30 12:41 PDT, bench) — the first fire HELD before any model call; the release moves to export 865290f, which differs from 6004ebe by ONE line
1. **WHAT HAPPENED.** `clb_fire.sh AO Crc32 lean-aeneas 1` on export 6004ebe: client pin OK, fence converged (sha16 e9cb8f919d980041),
   CHECK CLEAN, and the sandbox probe GREEN. Then the watcher's launch was **HELD**: its pre-launch `cell-claude.sh --check`
   re-rendered the fence **without** the read-only root and read DRIFT. The launch log says *"nothing was spent"*, and no model call
   was made.
2. **CAUSE.** `cell-watch.sh` passes the launch window only the names in its `LAUNCH_NAMES` list, and `O37_ROOT` was not in it. This is
   one more registry the arm had to join, found by the fire itself.
3. **FIX, harness 865290f** (on the arm branch, directly above 6004ebe): `O37_ROOT` is added to `LAUNCH_NAMES`. Unset names are skipped
   and scrubbed from the session, so no other cell's launch changes. cell-watch --selftest 77/77. `git diff --stat 6004ebe 865290f` is
   **one file, one line** (cell-watch.sh), so everything `cell_build.py` writes into a cell is byte-identical under either export.
4. **THE RELEASE MOVES TO EXPORT 865290f**, for all 6 cells. It sits at a dest of its own on the run box, and its Verus sha equals the
   build host's. Cell `clbeca01` was built from 6004ebe's identical cell-build bytes and was never launched. It is fired as itself: the
   rule that a cell is built once is about a cell that has RUN, and this one has an empty meter. Its root's `_bin` is relinked to 865290f
   before the fire.
