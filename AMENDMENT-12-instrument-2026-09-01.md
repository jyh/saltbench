# AMENDMENT 12 — THE INSTRUMENT AMENDMENTS BESIDE THE GATE (C-dead, the stage-C reading line, the enforcer, prompt_C, and the controls gate)

Seat `bench` · dated **2026-09-01** · registered under desk row AS, on the helm's 09:12:46 word
("`c_dead`'s SUCCESSOR is a SATISFIABILITY check … register it as an instrument amendment beside the gate";
"ROW AV WIDENS to the guard question … bench dates both protocol amendments").
Amends the frozen `SCOUT-S2LEAN-STAGE0.md`. Appended, never edited in.
**Rides with AMENDMENT 11 and must land before it**: amendment 11's gate is unreadable without §2 and §3 below.

*Every change here is ZERO MODEL TOKENS, red-first, and proven a no-op on the landed record where it touches a
reading. Nothing in this amendment changes any landed verdict, and §5 says so with the number.*

---

## §1 · WHY THESE ARE ONE DOCUMENT

Five repairs, one cause. `c_dead` answered *"does the C view elaborate?"* and was read as *"can the stage-C task
be done?"*; the morning line's stage-C block prints a rate over one population while amendment 11's gate is a
count over another; the budget enforcer has been rewritten from a bank paragraph three times because it never
had a file; and `prompt_C.md` forbids nothing about `native_decide` while the checker rejects it.

and the checker-controls gate reads a single boolean written by a run that may predate the checker it is
certifying.

**Each is the same defect in a different coat: A GATE, A PRINTED NUMBER, AN ENFORCER, A PROMPT AND A GREEN
LIGHT ARE ALL INSTRUMENTS, AND EACH OF THESE FIVE MEASURED A PROXY FOR THE THING INSTEAD OF THE THING.**

## §2 · `c_dead` HAS TWO COMPONENTS, AND THE UNION LIVES IN THE GENERATOR

**THE DEFECT.** `view_status.json` is **generated** by `views_selftest.sh`, which compiles all 161 stage-C views
and calls a view dead when it does not elaborate. `problem_18` elaborates perfectly and is unpassable by any arm
at any budget — a theorem (AMENDMENT 11 §2). Adding `18` to the generated file **by hand** would have been
dropped, silently, by the next person to run the sweep: the sweep is *right* about elaboration and has no idea
the meaning was extended. ⇒ *an edit to a generated file is a change with an expiry date nobody wrote down.*

**THE REPAIR.**

- **`harness/s2lean/c_dead_unsat.json`** — the registered second component. `18` with its theorem, its axiom set
  (`propext, Classical.choice, Quot.sound` — the allowlist exactly), its root cause, and `"elaborates": true`
  stated in the file so the apparent contradiction with its own `C: ok` row is answered where a reader meets it.
  **Additions are protocol changes and are made by dated amendment only, each carrying a machine-checked
  refutation. Never add an id because an arm failed on it.**
- **`harness/s2lean/c_dead_merge.py`** — the **single implementation** of
  `c_dead = c_dead_elaboration ∪ c_dead_unsat`. `views_selftest.sh` now calls it after writing its own
  component, and a by-hand refresh of an existing `view_status.json` runs the same code path. There is no second
  copy to drift.
- **`view_status.json`** now carries `c_dead_elaboration` and `c_dead_unsat` beside `c_dead`, so the split is
  recoverable from the file rather than from this document.

**DRIVEN — `c_dead_merge.py --selftest` ⇒ 11 arms, 0 failed**, every arm a subprocess on the real argv: a **RED**
arm asserting that with no registry the union is the elaboration component alone (if it ever goes green the tool
has stopped telling the components apart), the green union, the component split, the *elaborating* dead cell,
idempotence under repeated runs, **two REFUSE arms** (an id the sweep never saw; a legacy file whose `c_dead`
already claims a registered id and carries no split — the split is unrecoverable and guessing it would silently
mislabel a measurement), the accepted form of that same file, a no-write assertion for stdout mode, a bad-arg
refusal, and an arm asserting the real registry names exactly `[18]`.

⭐ **AND THE SELF-TEST WAS ITSELF DRIVEN, because a green self-test proves nothing until you break the program.**
Two mutations, each caught: *the union drops the unsat component* ⇒ 2 arms flip red; *the REFUSE on an
unrecoverable split becomes a silent guess* ⇒ 1 arm flips red.

**APPLIED, AND THE DELTA IS EXACT:** `view_status.json` re-written through `c_dead_merge.py` — **all 161
per-problem rows byte-identical**, `c_dead` 18 → 19 entries (`+18`), `c_dead_elaboration` equal to the previous
`c_dead` exactly, `c_dead_unsat = [18]`.

## §3 · THE STAGE-C READING LINE — THE GATE'S DENOMINATOR, PRINTED

**THE DEFECT, found before the data rather than after.** `s2_morning_line.py` prints stage C over `CE`, the
C-eligible **drawn** subset, and stage B's F3 line over `U`, the unflagged drawn subset — so the instrument had
an unflagged line for stage B and **none for stage C**, while amendment 11's gate is a **count over
`UC = U ∖ c_dead`**. At `k = 27` that is **22 against 12**.

⚠️ **THE TWO READINGS OF ONE RUN CAN POINT OPPOSITE WAYS.** A run that proves 9 of the registered 12 and 4
problems that are in `CE` but not in `UC` prints `a0 proven 13/22` = 59.1 %, **inside the campaign's 20–80 %
"RUN THE SALT ARM" band**, while the registered gate at `9/12` is a **CEILING HOLD**. The wrong one is the one
that is printed. *A printed rate whose denominator differs from the gate's is a green light waiting to happen* —
the `ship BC` log and `c_dead` itself are the same family, found after the fact; this one was found before.

**THE REPAIR — STRICTLY ADDITIVE.** Stage C (and stage C only) gains, per arm:

    REGISTERED POPULATION UC = U ∖ c_dead (amendment 11's gate is a COUNT over THIS set, not a rate over the 22
    above)  n=12 ids [...]: a0 proven 9/12 = ...

plus a pairs line over the same set beside the existing one. **No existing line changes.**

⭐ **THE CONSEQUENCE THAT MATTERS MORE THAN THE LINE: the instrument now DERIVES amendment 11's registered
population instead of taking it from the amendment's prose.** At `k = 27` it computes
`UC = [73, 0, 146, 16, 4, 38, 142, 96, 141, 31, 127, 74]` — amendment 11 §2's twelve, exactly, `18` absent
because §2 put it in `c_dead_unsat`. The gate's denominator is now a measurement, not a typed constant.

**DRIVEN — `selftest_morning_line.py` ⇒ 10 arms, 0 failed** (was 9), every arm a subprocess on the real argv.
The new arm runs at `k = 27` — the live configuration — on **its own state root**, deliberately: folding stage-C
rows into the shared fixture would move `manifests: N considered (M dropped)` and the three frozen contrast
counts, and the nine amendment-7 arms would then be re-baselined to test something they do not test.
**An additive change gets an additive fixture.**

✅ **RED-FIRST, against the pre-change `s2_morning_line.py` with the identical selftest: 6 of the amendment-12
assertions FLIP RED, and all 9 frozen arms pass under BOTH — which is the no-op proof.** One of the red arms
asserts the CE line still reads `13/22` and it passes under both: *the frozen number is untouched; the missing
one is added.*

⛔ **AND THE RED RUN CAUGHT A DEFECT IN MY OWN GATE.** An arm read `.group(1)` off a regex that does not match
when the line is absent — which is precisely the red case — so the control **crashed with a traceback instead of
reporting FAIL, taking the remaining arms with it.** Second instance in that same file of the law it already
carries in a comment: **A GATE WHOSE FAILURE PATH HAS NEVER EXECUTED IS AN UNTESTED GATE**, and the failure path
is reached by running the control, not by reading the code. Fixed; both arms re-driven.

## §4 · THE ENFORCER IS AN ARTIFACT NOW, NOT A BANK PARAGRAPH

**THE DEFECT, banked twice as a law and repaired only now.** A registered stop rule needs a live enforcer, and
this seat has written that watch **three times** — `amend3_watch.sh`, the `a8watch`, and now — each in a
**session-scoped scratchpad**. Each died with its head; each next head rewrote it from a bank paragraph. The
DESIGN was inherited every time. The ARTIFACT never was, *and only an artifact can be re-armed in one command.*

**`harness/s2lean/halt_watch.sh`**, tracked and pinned. It writes `$BENCH/HALT` and does nothing else — the
driver reads that file **inside its arm loop** (`run_s2_stage0.sh:120`) and exits 4 after the episode in flight.
**It never signals and never kills:** stopping a run mid-episode corrupts the landing the stop rule exists to
protect. Arms: **BUDGET** (Σ `metered_sum` over *this run's own* landings ≥ `TOK_MAX`) ⇒ HALT · **WALL** ⇒ HALT ·
**STALL** (landings, meter **and** the in-flight transcript static) ⇒ **EVENT, never a HALT** · **DEAD** (no
claude process and no `DRIVER DONE`, two consecutive polls) ⇒ EVENT · **PROBE-FAILED** ⇒ EVENT.

📌 **STALL REPORTS AND DOES NOT HALT, and that is the 08/30 law spent rather than quoted:** landings and the
meter **both move only at episode end**, so a healthy 26-minute episode is byte-identical to a dead driver under
an end-of-unit instrument. Reading the transcript makes the report honest; halting on it would throw away a live
episode.

**DRIVEN — `halt_watch.sh --selftest` ⇒ 21 arms, 0 failed**, every arm a subprocess on the real argv: 6 REFUSE
arms (relative root, missing root, bad stage, non-numeric budget, **zero budget** — a zero budget halts before
the first episode — unknown arg), the green under-budget path with its measured total, the budget HALT with the
reason **written into the file**, the wall arm firing with the budget nowhere near, **two SCOPE arms** (another
stage's or another arm's landings must not count — a watch that counts the previous stage's spend halts a run
that has spent nothing, and it looks exactly like a real breach), a **since-ARMED** arm, two DONE arms (another
stage's `DRIVER DONE` is not mine), and two arms proving a pre-existing HALT file is reported and **not**
overwritten. Mutation-driven: *the budget arm never fires* ⇒ 3 arms red; *the scope filter ignores the arm* ⇒
1 arm red.

## §5 · `prompt_C.md` AND ROW AV — THE SENTENCE, AND ITS CONTROL, TOGETHER

**REGISTERED AND APPLIED.** `prompt_C.md` gains, arm-blind (it is a per-stage file, identical in `a0`, `a1`,
`a2`):

> Do not use `native_decide`: the checker replays the file through the Lean kernel with no compiled code
> available, so a proof that depends on it is rejected. `decide` is fine.

**COMPARABILITY COST: ZERO, AND IT IS MEASURED, NOT ASSUMED.** Over both state roots, the 201 scored episodes
are **114 stage A and 87 stage B — `prompt_C.md` has never been used in a scored episode of this campaign.**
Changing it now costs no comparison; changing it after Step 1 would have cost the whole read.

⭐ **THE SECOND HALF OF THE SENTENCE IS DRIVEN, NOT ASSERTED.** The prohibition is measured (row AB; three
controls; one production episode). *"`decide` is fine"* was not, and an over-cautious agent avoiding `decide`
would depress `P0` and I would be reading an artifact of my own prompt. So the control kit gains **`C_decide`**,
the exact differential sibling of the existing `C_ax`: the **same** problem, the **same** gold implementation and
proof, the **same** helper lemma — `by decide` instead of `by native_decide`, expected **PASS** where `C_ax`
expects `AXIOMS_FAIL`/`KERNEL_REJECTED`. Controls kit 30 → **31**. *A prohibition with no measured alternative is
half a sentence.*

⛔ **ROW AV's STAGE-A HALF IS REGISTERED AND DELIBERATELY NOT APPLIED, WHICH IS A DECISION AND IS STATED AS ONE.**
Step 0 found that **four of eight failing stage-B problems are one defect**: the reference `problem_spec` GUARDS
its conclusion while `generated_spec`, as `prompt_A.md` asks for it, is TOTAL — **a guarded spec and a total spec
are never isomorphic, and stage B asks for an isomorphism.** The repair would be a sentence in `prompt_A.md`.
**I am not making it, because `prompt_A.md` HAS run — 114 landed stage-A episodes — and changing it would break
comparability with every stage-A and stage-B reading this campaign owns, in exchange for a repair amendment 11
authorises no stage to use.** Amendment 11 runs **no stage A and no stage B**. ⇒ **DESK: the guard question is a
live protocol question for the next substrate or the next re-read, and the moment to spend the comparability is
when a run needs it.** Recorded here so it cannot be adopted quietly later.

## §5b · THE CONTROLS GATE — FOUND LIVE WHILE CLOSING AMENDMENT 11's §12, AND IT WAS GREEN AGAINST A CHECKER THAT NO LONGER EXISTED

**THE DEFECT, MEASURED ON THE MACHINE, NOT REASONED ABOUT.** `run_s2_stage0.sh` gated every scored episode on

    python3 -c "import json,sys;sys.exit(0 if json.load(open('$cj')).get('controls_pass') else 1)"

— **one summary field**: no clock, no tie to the checker about to run, no idea which controls produced it.
The commission itself warned about this shape ("verify … C-control rows are PRESENT, not `controls_pass: true`
believed"), which is why I read the rows by hand. Reading them turned up the rest:

⛔ **THE LANDED `s2-controls.json` IN BOTH STATE ROOTS (dated `2026-08-29T10:33:38Z`, 30/30, `controls_pass:
true`) CERTIFIES `screen.py = aa2c9376…` — AND THE SCREEN THAT WOULD HAVE SCORED THIS RUN IS `cc591ca6…`**,
amendment 9's §9.5 widening, landed 08/31 and synced today. Four of the five recorded checker shas match; the
fifth does not, and **the gate compares none of them.** Amendment 9 proved that particular widening a **no-op
over all 201 landed episodes**, so nothing was harmed — *and the gate could not have known that.* **A green
light that cannot be wrong is not a gate.**

⇒ **THIRD INSTANCE OF ONE SHAPE AT THIS SEAT IN THREE DAYS:** `ship BC` gated on a **DONE line in a log**
(08/31, repaired by amendment 10); `c_dead` gated on **elaboration** (§2 above); this gated on a **boolean**.
The cure is the same all three times, and it is worth stating once as a rule rather than three times as a
repair: **READ THE CONTENT, IN THE PLACE THE WORK WILL HAPPEN.**

**THE REPAIR — `harness/s2lean/controls_gate.py`**, pinned, called by the driver. Five clauses, each a refusal
(*a refusal is a result*): the summary must agree with itself (`controls_pass` **and** `n_ok == n`); **every
file in `checker_sha256` must match the sha of the LIVE file** in the harness directory — the clause that fires
today; this stage's control **family** must be present, `ok`, and each row's recorded class inside its own
`expect_class`; an optional clock; and a non-empty results block with a class on every row, because
**`controls_pass: true` over zero rows is the failure a boolean cannot express.**

**DRIVEN — `controls_gate.py --selftest` ⇒ 17 arms, 0 failed**, every arm a subprocess on the real argv.
⭐ **The arm that carries the finding is DIFFERENTIAL on one fixture: the new gate REFUSES the drifted record
naming both shas, and the OLD one-line predicate — run verbatim, in the same arm, on the same file — EXITS 0.**
Both arms differ, on the specimen, rather than on my say-so. Also driven: `controls_pass` false · `n_ok != n` ·
an empty results block under a true boolean · **a required control ABSENT (which is exactly what a stage-C run
inherits if it is handed a controls file written before `C_decide` existed)** · a required control not ok · a
row whose class contradicts its own expectation · a checker file named but missing · no `checker_sha256` at
all · the clock in both directions · three bad-argument refusals.

⛔ **AND WIRING IT IN INTRODUCED A FATAL, WHICH THE RUN-SHAPED DRY CAUGHT AND WHICH I AM RECORDING RATHER THAN
QUIETLY FIXING.** My first wiring was `python3 controls_gate.py … | tee -a "$RL" || { … exit 3; }` — **a
pipeline's status is `tee`'s**, so a REFUSING gate would have read as green: *the exact defect this gate exists
to remove, reintroduced by the plumbing that reports it.* Now captured, not piped. **Fifth consecutive repair
round at this seat to introduce a fatal — the run-shaped dry is part of the gate, not a formality.**

**STATE:** the controls are re-run at the CURRENT checker set as part of this amendment (31 arms — the 30
frozen plus `C_decide` of §5), and the new record replaces the stale one in the run root. **The old record is
not deleted and not trusted:** it is the specimen this section is about.

## §6 · WHAT THIS AMENDMENT DOES NOT DO

It does not change any landed verdict, any scored class, any rate, or any pinned view. It does not change
`check.py`, `screen.py`, `episode_s2.sh`, `run_s2_stage0.sh` or any arm file. It does not touch `prompt_A.md` or
`prompt_B.md`. The `CE` line, the F3 line and all three band readings are byte-for-byte what they were.

## §7 · PINS

`HASHES.txt` regenerated with `CLEVER_SRC` set. Delta: **6 files re-pinned** (`prompt_C.md`,
`s2_controls_kit.py`, `s2_morning_line.py`, `selftest_morning_line.py`, `view_status.json`, `views_selftest.sh`)
and **4 added** (`c_dead_merge.py`, `c_dead_unsat.json`, `c_oracle_preflight.py`, `halt_watch.sh`). Nothing else
moved — all 161 × 4 view pins, every arm rendering and every other harness file are identical.
✅ **The three `leanproj-*` pins REPRODUCE BYTE-IDENTICALLY** from the Studio's live project
(`66fd2abd… / 75f31318… / d55ca003…`), which is itself the content check that the shared build is the pinned one.

## §8 · LAWS THIS AMENDMENT ADDS

- **An edit to a GENERATED file is a change with an expiry date nobody wrote down** — put it in the generator, or
  in a registry the generator reads.
- **A printed rate whose denominator differs from the gate's is a green light waiting to happen**, and the two
  can point opposite ways on the same run.
- **Make the instrument DERIVE the registered population** — a denominator typed into an amendment is a claim; a
  denominator computed by the tool is a measurement.
- **An enforcer that lives in a session which must exit has an expiry date** — this seat paid it three times, and
  the fix was always a tracked file.
- **A prohibition with no measured alternative is half a sentence.**
- **A gate that reads a summary cannot tell a result from a memory of one** — third instance of one shape in
  three days (a DONE line, an elaboration check, a boolean). **Read the content, in the place the work will
  happen.**
- **A green light that cannot be wrong is not a gate**, and the way to find out is to run the old predicate and
  the new one on the same specimen.
- **The plumbing that reports a gate can defeat it:** `cmd | tee || fail` takes `tee`'s status.
- **A gate whose failure path has never executed is an untested gate** — reached by running the control, never by
  reading the code.
- **Spend comparability only when a run needs it**: a repair that breaks a landed record and serves no
  authorised stage is a repair that should wait, and saying so is a decision, not an omission.
