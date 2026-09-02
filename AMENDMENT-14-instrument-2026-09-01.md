# AMENDMENT 14 — INSTRUMENT (2026-09-01, seat `bench`)

**FOUR instrument repairs, one refuted premise, and one registered rider.** Three were routed or ruled; the
fourth was found because this amendment's own new gate went intermittent (§6). Registered under the pre-registration's amendment rule
(dated, appended, never edited into a frozen text). **Zero model tokens: every item is checker, audit or
harness work over already-landed artifacts.** No episode is re-run and no rate in this campaign moves.

Routed to this seat by the helm's desk word of 2026-09-01 20:0x, items (1) and (2) of four, both marked
**APPLY NOW**, plus the helm's ruling 2 of 17:38 (the per-episode token stop, §8). Item (1) is applied **on a
different trigger than the one it was routed on**, for the reason in §1; §1 is therefore the load-bearing
section of this amendment and everything else follows from it.

---

## §1 THE ROUTED PREMISE IS REFUTED, AND THE REPAIR IT AUTHORISED WOULD HAVE PASSED ITS OWN PROOF

The routed finding (bench, bus 2026-09-01 18:34:30) reported the campaign's only `STATEMENT_ALTERED` —
`problem_112 / a1 / stage B`, `~/bench-aw/state/ep-2714f8d2` — as a false positive **caused by the agent
deleting the harness's `-- start_def` / `-- end_def` section markers**, evidenced by *"the file carries ZERO
markers (grep count 0 over 61 lines), so `bodies.json` has no `problem_spec` key at all."*

**Every clause of that evidence is measured on the wrong file.**

| claim | measurement | verdict |
|---|---|---|
| "the file carries ZERO markers" | the file grepped is `evidence/amend13-AW-2026-09-02/p112_canonical_STATEMENT_ALTERED.lean`, sha256 `d1a3d677411de26e…`, **byte-identical to `ep-2714f8d2/canonical.lean`** | it is the **ASSEMBLED canonical**. `assemble.py` composes it from `frozen.json` + `bodies.json` and **never emits markers for any episode, passing or failing**. Grepping it measures `assemble.py`. |
| "the agent deleted the markers" | the agent's own file, `ep-2714f8d2/eptree/repo/task.lean` | **`grep -c "start_def\|end_def"` = 12**, all pairs present and well-formed. |
| "`bodies.json` has no `problem_spec` key" | `ep-2714f8d2/bodies.json` | `{"spec_isomorphism_proof": "by sorry", "iso_helper_lemmas": "", "_present": {"spec_isomorphism_proof": true, "iso_helper_lemmas": true}}` — **extraction SUCCEEDED and the harness's own presence flags say so.** `problem_spec` is not a stage-B body key in the first place (`extract.py` `WANT["B"]`), so its absence is true of **all 30** stage-B episodes in that root. |

Swept over the whole landed record: **256 `bodies.json` files across all four state roots carry `_present`,
and ZERO have a missing marker pair.** No agent in this campaign has ever damaged the scaffold.

⇒ The routed repair — *emit `SCAFFOLD_DAMAGED` when the delimiter set is damaged **and** the extracted spec is
absent* — has a trigger that **has never once been satisfied**, would not have fired on `112`, and would have
been landed with a red-first proof that **passed**, because the fixture would have been built from the same
false premise. It would have left the false positive in place under a new name.

📌 **The chain that carried it.** The predecessor verified at *an* artifact and reported honestly; it verified
at **the harness's output instead of the agent's input**, and the RESULT document, the evidence README, the
desk row and the helm's APPLY NOW each inherited it as measured fact. **No link could have caught it: each was
quoting a real file with a real sha.**
⇒ 🔑 ***"VERIFIED AT THE ARTIFACT" NAMES A HABIT, NOT A GUARANTEE — THE QUESTION IS ALWAYS "WHICH ARTIFACT,
AND WHO WROTE IT." A finding about what an AGENT did must be measured on a file the AGENT wrote.***

---

## §2 THE REAL MECHANISM, PROVEN AT THE MACHINE

Rebuilt both sides of the comparison for `problem_112` stage B **under the harness's own `sandbox_check.sb`
fence, reusing `check.py`'s `render_profile` and `run_fenced` verbatim** — canonical byte-copied from the
episode and sha-checked, pristine from `assemble(..., pristine=True)` — compiled both, and read the two
`problem_spec` values out of the oleans:

```
CANONICAL constants: #[generated_spec, problem_spec, spec_isomorphism, generated_spec.match_1]
PRISTINE  constants: #[generated_spec, problem_spec, spec_isomorphism, problem_spec.match_1]
problem_spec value EQUAL: false
   the two used-constant sets are 31 names each and differ in EXACTLY ONE:
      canonical … generated_spec.match_1 …      pristine … problem_spec.match_1 …
```

`problem_spec` destructures a `String × Bool` with a pattern `let`, which needs an auxiliary matcher. **Lean
caches matchers per module and names each after whichever declaration elaborated it first.** In the canonical
the agent's `generated_spec` body destructures the same type first, so the matcher is minted as
`generated_spec.match_1` and `problem_spec` **reuses** it; in the pristine `generated_spec := sorry` mints
nothing, so `problem_spec` mints its own. `s2audit.lean` compared `value? cp == value? cc` — a **structural
`Expr ==`, which includes constant NAMES**.

⇒ 🔑 ***A STRUCTURAL COMPARISON OF A FROZEN DECLARATION'S ELABORATED VALUE IS NOT A COMPARISON OF THAT
DECLARATION — IT IS A COMPARISON OF THE WHOLE MODULE***, because elaboration shares auxiliary declarations and
names them after whoever needed them first. The frozen **text** was never at risk: `assemble.py` splices
`fz["problem_spec"]` verbatim, so text immutability holds **by construction**. What varied was the agent's
neighbours.

**The gate FAILS CLOSED throughout — no soundness hole, and `P1 = 9/15` stands.** Only the class name is
wrong; the honest stage-B taxonomy for `a1` is `{PASS 9, AXIOMS_FAIL 6}`.

### The surface, measured two independent ways that agree
Over **239 landed episodes with an `audit.json` across all four state roots** (`~/bench` 138 · `~/bench-a8` 59
· `~/bench-aw` 30 · `~/bench-c` 12):
- from the recorded `audit.json`: non-empty `statement_diffs` = **1** (`ep-2714f8d2`, `problem_spec`,
  `type_identical=true value_identical=false`);
- from the `canonical.olean` files at the Expr level — *does `problem_spec`'s value use a matcher it does not
  own?* — **1 of 239, the same episode**, `#[generated_spec.match_1]`.

⛔ **The surface is LIVE, not hypothetical: 8 episodes carry an agent-owned `generated_spec.*match_1`, and in
one of them it collided with a matcher `problem_spec` also needed — ~1 in 30 in the AW run.** It is
arm-independent, tier-independent and stage-B/C-wide.

---

## §3 REPAIR 1 — `s2audit.lean`: compare matchers by CONTENT, never by owner-derived name

`normAux` delta-expands every auxiliary matcher (`match_<digits>`) to its own definition, level parameters
instantiated, before the comparison. A matcher that cannot be resolved, or has no value, keeps a marker built
from its **original** name so the two sides differ and the gate **fails closed**.

- **`value_identical_raw` is recorded for ever beside `value_identical`,** plus a boolean
  `aux_matcher_renaming`. *A repair that hides the number it changed cannot be audited*, and the 08/31
  comparability law requires the flips to be publishable **by name from the record itself**.
- **Widened as narrowly as the evidence allows** (the 08/31 screen law): `match_<digits>` **only**. Other
  owner-named auxiliaries (`_proof_<n>`, `.eq_def`, …) share the hazard and are **deliberately not
  normalised** — none has been observed in 239 landed episodes, and *a relaxation with no specimen behind it
  is a hole with a rationale*.
- The same normalisation is applied to `a_body_value_identical` (AP-4 provenance), which compares
  `generated_spec` across two modules and has the identical exposure.

⛔ **THE DEFECT MY FIRST CUT OF THIS REPAIR HAD, and it is the sharpest thing in this amendment.** The first
version keyed each matcher on `toString` of its type and value. `toString` prints **binder names**, which are
hygienic and **carry the module they were elaborated in**:

```
C type: … (result._@.canonical.1600460969._hygCtx._hyg.50 : Prod String Bool) … (result_palindrome : Bool) …
P type: … (result._@.pristine.1835493598._hygCtx._hyg.48 : Prod String Bool) … (result_bool   : Bool) …
```

while `Expr ==` is alpha-equivalence and reports these two matchers **EQUAL**. So **a repair for
name-sensitivity was itself name-sensitive, one level down**, and read `value_identical = false` exactly as
before. Found by driving it on the real specimen, not by reading it.
⇒ 🔑 ***A NORMALISATION THAT ROUTES THROUGH A PRINTED FORM IS NOT A NORMALISATION — printing re-introduces
every distinction the comparison was chosen to ignore.*** **Sixth consecutive repair round at this seat to
introduce a fatal; the driven arm is the gate.**

### Gate: `selftest_s2audit.py` (new, tracked)
Every arm compiles a real canonical/pristine pair with the real `lean` **under the fence** and runs
`s2audit.lean` **as a subprocess on the real argv** — never an in-process reimplementation.

| arm | asserts | pre-change |
|---|---|---|
| 1 specimen (`112`) | `statements_identical` **true**, `value_identical_raw` **false**, `aux_matcher_renaming` **true**, and `generated_spec.match_1` really is in the module | **3 of 4 FLIP** |
| 2 altered spec (`c.data.length = 0 → result_str = s` ⇒ `… = c`; matcher untouched) | still **REFUSED**, and for the right declaration | passes under both — *the no-op half* |
| 3 changed constant inside `problem_spec` | still **REFUSED** | passes under both |
| 4 no-op control (unshared pair) | passes, `aux_matcher_renaming` **false**, pristine mints its own matcher | 1 of 2 flips |

**10 assertions, PASS, driven twice consecutively** (an intermittent gate is worse than a red one). Against
the pre-change audit **5 flip and the alteration arms hold** — the repair does not weaken the gate.

📌 My first cut of **arm 2** swapped the two destructured components, which **does not compile at all**
(`result_bool` would be a `String`). The selftest **REFUSED** rather than skipping the arm, which is the only
reason it was noticed. *A fixture that cannot be built proves nothing, and a self-test that silently tests
nothing is the failure it exists to prevent.*

---

## §4 REPAIR 2 — `SCAFFOLD_DAMAGED`, on its TRUE trigger

`extract.py` has always computed `_present` — which `-- start_def X` / `-- end_def X` pairs it actually found —
and **nothing has ever read it** (`grep -n _present harness/s2lean/*` returned exactly one line: its
definition). An agent that really did delete its markers therefore yields empty bodies, `assemble.py`
substitutes the frozen `sorry` defaults, the file compiles, and the episode scores **`AXIOMS_FAIL` with
`sorryAx` — byte-indistinguishable from an agent that honestly admitted the gap.**

⇒ **A DEAD FIELD IS NOT A CHEAP FIELD: it is a measurement taken, paid for, and then discarded at the point of
use.** The routed class name survives; its trigger, its evidence and its subject episode were all wrong.

`check.py` now records `scaffold_present` / `scaffold_missing` / `scaffold_damaged` / `scaffold_unknown` on
every episode and emits `SCAFFOLD_DAMAGED` **between `STATEMENT_ALTERED` and `AXIOMS_FAIL`**:
- it **pre-empts `AXIOMS_FAIL`** because it *explains* the `sorryAx` — the harness substituted the default and
  the agent never wrote a proof;
- it does **not** pre-empt `STATEMENT_ALTERED`, which is the stronger accusation and is measured
  independently;
- `_present` is a **marker-pair** fact, never a content fact: an empty section with intact markers is
  legitimate (`iso_helper_lemmas` is empty in most episodes) and is **not** damage;
- a `bodies.json` with **no `_present` key at all is UNKNOWN, never damaged** — *a checker must not convict an
  episode on a field its own extractor did not write*;
- stage B's `generated_spec_body` is **merged from `--a-bodies` (D5)**, not extracted, so it is deliberately
  outside this test; its provenance is AP-4's job.

**Landed-record effect: ZERO.** 256/256 `bodies.json` carry `_present`; 0 have a missing pair.

---

## §5 REPAIR 3 — the F3 headline at a root where stage B never ran prints NOT-RUN

Desk word item (2). At a state root with no stage-B `a0` rows, the numerator is an **absence** while the
denominator is still the drawn set, so `band(0, len(D))` returned `HOLD (<20%: a floor)` — **a registered
decision printed off a stage that never ran**, directly above the stage-C block that did. The `PROVISIONAL`
prefix already fired and did not save it: *it qualified the reading while the reading still named a band.*

- **nothing resolved ⇒ `NOT RUN`, and no band is computed at all**;
- **partly resolved ⇒ unchanged `PROVISIONAL`** — an *incomplete* measurement is not an *absent* one, and this
  repair must not silence a partial read;
- the two subset lines print `NOT RUN`; the band comparison prints `NOT COMPARED`; `READING:` becomes
  `NOT RUN … — F3 is UNREAD, which is not the same as HELD`, with **no `PROVISIONAL` prefix**.

⛔ **My first cut printed the band it was refusing to print** (*"band(0/27) would read HOLD (<20%) off a stage
that never ran"*) — **re-creating, in the explanation, exactly the greppable string the repair exists to
remove.** Caught by this repair's own selftest arm. *An explanation that quotes the thing it forbids is the
thing it forbids.*

### Gate and no-op
`selftest_morning_line.py` grows to **12 arms** (+1 NOT-RUN arm of 5 assertions, +1 **control** of 4). The
control is the arm that matters: **a repair that suppresses a false HOLD by suppressing all HOLDs passes the
five NOT-RUN assertions and destroys the instrument.** Against the pre-change tool the **5 NOT-RUN assertions
flip and all 4 control assertions pass**; the 8 pre-existing arms pass under both.

**Proven on real state, 24 invocations** (4 roots × `ML_ARMS` ∈ {a0, a0a1, a0a2} × k ∈ {15, 27}):

| root | stage B / a0 | verdict |
|---|---|---|
| `~/bench` | ran | **nothing altered — ONE line ADDED**, the empty `SCAFFOLD_DAMAGED: []` integrity line |
| `~/bench-a8` | ran | **nothing altered — the same one added line** |
| `~/bench-aw` | never ran (a1-only root) | 5 lines replaced + the added line; **every replaced line IS the repair** |
| `~/bench-c` | never ran (stage-C-only root) | 5 lines replaced + the added line; **every replaced line IS the repair** |

(The `SCAFFOLD_DAMAGED` integrity line is added by §4: *a class the morning line cannot print is a class the
campaign will not see.* It is strictly additive and empty on the entire landed record.)

⭐ **`~/bench-aw` is a second live instance the desk did not name.** That root holds **only `a1`**, so the F3
line — which is defined on `a0` — was printing `0/27 = 0.0% ⇒ HOLD (<20%)` **for an arm that never ran
there**, in the very read that produced `P1 = 9/15`. Same defect, different cause for the emptiness.

---

## §6 REPAIR 4 — the audit's process sweep kills processes it does not own

**Not routed by anyone. Found because this amendment's own new gate went INTERMITTENT** — green when
published, red when re-run beside the controls — and the seat's own law says *an intermittent gate is worse
than a red one: find the cause, do not re-run until it agrees.*

`run_fenced` sweeps `pgrep -f <belt>` after each fenced step and SIGKILLs every match, as a belt for anything
that escaped the process group. The compile and pristine steps pass **per-invocation** source paths
(`ccanon`, `pfile`). The audit step passed **`a.audit` — `<harness>/s2audit.lean`, identical for every
invocation.** So one `check.py` sweeping after its audit kills **any other `check.py`'s in-flight audit
against the same harness dir.**

Measured, three invocations staggered by 9 s under load:

```
c0 class=AXIOMS_FAIL  audit_rc=0   retry=None
c1 class=HARNESS      audit_rc=-9  retry=-9   err=RuntimeError('audit did not run: no JSON on stdout (rc=-9)')
c2 class=AXIOMS_FAIL  audit_rc=0   retry=None
```

killed once, retried by FN-5, and **killed again by the same sweep**, which is why the single retry does not
save it. ⇒ ***A SWEEP WHOSE PATTERN NAMES A SHARED FILE DOES NOT CLEAN UP AFTER ITSELF — IT CLEANS UP AFTER
EVERYBODY.***

**Fix:** the audit's belt is now `olean`, which lives in this invocation's fresh `cwork` and appears in the
audit's argv. Sequential runs are unaffected — with one invocation live, both patterns select exactly the same
processes — so this is a **no-op for every run this campaign has ever done**, which run episodes sequentially
by construction. It fails LOUD (class `HARNESS`), so **no landed episode can have been mis-scored by it**; the
cost is intermittency, not error.

⛔ **AND IT BIT THE CONTROLS DURING THIS VERY AMENDMENT, WHICH IS THE BLAST RADIUS STATED HONESTLY.** The
first controls re-run came back **28/31**, with `C_pos`, `C_neg` and `C_ax` all class `HARNESS` at
`audit=0.1s` — three consecutive controls whose audits died instantly while I was driving the new selftests
against the same harness directory. **My own testing killed the gate's audits through the exact defect the
testing was there to repair.** The controls were re-run clean afterwards (§9) — *the first record is kept and
not trusted; it is the specimen.*

⛔⛔ **AND THE DEFECT IN THIS REPAIR'S FIRST GATE, which is the sharper half.** My first cut of
`selftest_check_concurrency.py` reproduced the RACE: three staggered invocations, asserting none is killed. It
passed against the amended checker — **and it also passed against the pre-change checker, three times**,
because the collision needs one audit to be mid-flight when another sweeps, which depends on machine load.
**A gate whose red control only fires under load is a gate that reads green for ever** — the same
intermittency, one level up, in the instrument built to catch it.
⇒ The shipped arm does not race at all. A **decoy** process whose command line carries the shared audit path
is started, one `check.py` runs, and the decoy must survive. **RED 3/3 (`decoy=KILLED`, FAIL) · GREEN 3/3
(`decoy=ALIVE`, PASS)** — deterministic in both directions, single invocation, no timing assumption.
⇒ ***REPRODUCING A DEFECT IS NOT THE SAME AS GATING IT: a gate must fail on the broken version EVERY time,
and a race only fails SOMETIMES. Test the mechanism, not the symptom.***

---

## §7 WHAT THIS AMENDMENT DOES NOT DO

- **No episode is re-run and no model call is made.** Zero model tokens.
- **No rate, band or registered reading moves.** `P0 = 12/12`, `P1 = 9/15`, `Δ1 = +1`, `f_vac = 0/4` all stand.
- **Stage C is untouched.** Amendment 11 is frozen at `8de0b74`; its objection window closes **09/02**, and
  **no stage-C model call has been made.**
- Rows **AV** (`native_decide`) and **CO** (the Seatbelt fence) are **not** landed here — the helm's word
  ripens them together at the VeruSAGE stage-0 regime boundary, as **one** regime change.
- `_proof_<n>` / `.eq_def` auxiliaries are **not** normalised (§3), and the reason is recorded rather than the
  convenience.

---

## §8 REGISTERED RIDER — THE PER-EPISODE TOKEN STOP (the helm's ruling 2 of 2026-09-01 17:38)

Registered **before** the next priced run, as the helm's word required, and attaching to whichever commission
governs that run (row DD's VeruSAGE §11 is the helm's dated debt; this rider moves there intact if the helm
would rather hold it). Registering it here rather than waiting is deliberate: **a stop registered after the
run it would have bound is not a stop.**

**THE RULE.** A per-episode **HALT** at **4 × the p90 of the governing regime** (the same D16 corner the cap
rule already consumes: that stage, `a0`, `DONE|ROUNDS_EXHAUSTED`). It is a **HALT, never a FAIL** — a halted
episode is recorded as halted and is **unresolved for the rate**, because scoring an episode we stopped as a
failure would let the budget instrument move the result.

**WHY 4, chosen from the record rather than picked.** Over all 177 passing S2-Lean episodes in the landed
record, per regime (stage × tier), the ratio of the **most expensive PASSING episode** to that regime's p90:

| stage/model | n pass | p90 (all) | max PASSING | max-pass / p90 |
|---|---|---|---|---|
| A / opus-5 | 45 | 307,091 | 737,877 | **2.40** |
| A / sonnet-5 | 67 | 340,564 | 568,733 | 1.67 |
| B / opus-5 | 29 | 1,190,213 | 2,860,947 | **2.40** |
| B / sonnet-5 | 24 | 8,864,343 | 9,128,436 | 1.03 |
| C / opus-5 | 12 | 912,687 | 949,908 | 1.04 |

⭐ **NO PASSING EPISODE HAS EVER EXCEEDED 2.40× ITS REGIME'S p90 — and 2.40 is hit independently in two
regimes.** The single runaway that motivated the rule, `problem_112 / a1 / B / opus-5` at **9,271,167 tokens =
7.79× that regime's p90**, is the **only** episode in the whole record above 2.40×, and it **failed**.
⇒ 4× sits between the worst legitimate episode ever observed (2.40×) and the one runaway (7.79×) — near their
geometric mean (4.32), placed **below** it so the conservative error is *not halting*. It would have halted
`112/a1` at ≈4.76M, saving ≈4.5M (≈31 % of that stage's entire spend) and **would not have touched a single
one of the 177 passing episodes**, with 67 % headroom above the worst.

⛔ **AND THE CAVEAT THAT MADE THIS RULE NECESSARY IS NOT REPEALED BY IT.** *A corner from order statistics
assumes the tail it bounds.* 4× a p90 is still a p90-derived number, so the rule is a **budget** instrument
and is not evidence about the distribution. Its honesty comes from the HALT being visible, not from the
multiple being right.

**DERIVED, NOT TYPED.** `s2_morning_line.py` now prints the stop per stage beside the corner it is built on
(`per-episode TOKEN STOP at the registered 4x …`), computed from the same p90 the cap rule consumes. A driven
arm asserts the printed stop **is** 4× the printed p90 per stage, read off the tool's own output — *a
self-test that recomputes the quantity tests its own arithmetic, not the tool's.* The 09/01 law applied to a
budget: **a number typed into an amendment is a claim; one computed by the instrument is a measurement.**

📌 **NOT WIRED INTO THE DRIVER HERE, and the reason is this seat's own record.** `TOKEN_CEILING` is the
existing enforcement point (amendment 4, live since 08/30) and the change is small — but **five consecutive
repair rounds at this seat introduced a fatal, and the run-shaped dry is the gate.** The wiring lands with the
run that first uses it, under that run's dry, not under this one. What is registered here is the RULE and its
NUMBER, which is what had to precede the run.

---

## §9 COMPARABILITY RE-READ — THE FLIPS, BY NAME

The 08/31 comparability law: a checker change must be followed by a re-read of the landed record with the
flips published **by name**. Driven over **every landed stage-B/C episode with a `canonical.olean` across all
four state roots (110 episodes)**: the pristine is rebuilt from that root's own `frozen.json` (cached per
problem+stage) and **both** the pre-change and the amended `s2audit.lean` are run on the same pair. Stage A is
excluded because it compares no value at all (`frozen "A"` = `generated_spec` with `cmpVal = false`) and
therefore cannot move.

**PREDICTION, REGISTERED BEFORE THE RE-READ COMPLETED (this section committed with the code, results appended
after):**
1. **Exactly ONE flip: `ep-2714f8d2` (`problem_112 / a1 / B`, root `~/bench-aw`), `false → true`.** Grounded
   in two independent sweeps that already agree — the recorded `audit.json` (1 of 239 with a non-empty
   `statement_diffs`) and the Expr-level trip-condition sweep over all 239 `canonical.olean` files (1 of 239
   where `problem_spec`'s value uses a matcher it does not own).
2. **ZERO `true → false` flips.** This is the clause that could genuinely fail and is the reason the re-read
   is driven rather than argued: delta-expansion makes the comparison **stricter** where two modules hold a
   **same-named** matcher with **different content** — a real difference the name-comparison could not see.
   If any such episode exists, the amended checker will find it, and it will be a **catch, not a regression** —
   but it would move a class, so it must be published by name.
3. **No `HARNESS`/error rows.** Any episode whose pristine cannot be rebuilt is reported, not skipped.

**RESULT — BOTH CLAUSES HELD, and the third had nothing to report.**

```
RE-READ COMPLETE: 110 stage-B/C episodes re-audited under BOTH checkers
FLIPS: 1
   ('/Users/jyh/bench-aw', 'ep-2714f8d2', 'problem_112', 'B', 'a1',
    (False, ('problem_spec',)) -> (True, ()))
ERRORS: 0
```

1. ✅ **Exactly one flip, and it is the predicted one.** `ep-2714f8d2` (`problem_112 / a1 / B`,
   `~/bench-aw`): `statements_identical false → true`, `statement_diffs ['problem_spec'] → []`.
   **`STATEMENT_ALTERED → AXIOMS_FAIL`.**
2. ✅ **Zero `true → false` flips.** Delta-expansion is strictly stricter where two modules hold a same-named
   matcher with different content; **no such episode exists in the landed record.** This was the clause that
   could have failed, and it is why the re-read was driven rather than argued.
3. ✅ **Zero errors** — every one of the 110 pristines rebuilt and every audit produced JSON on both checkers.

**NO RATE MOVES.** The `a1` stage-B taxonomy becomes **`{PASS 9, AXIOMS_FAIL 6}`** — which is what the AW
RESULT already published as the honest reading. `P0 = 12/12`, `P1 = 9/15`, `Δ1 = +1`, `f_vac = 0/4` all stand
untouched.

### Controls, re-run at the amended checker
**`CONTROLS PASS (31/31)`**, `controls_pass = true`, `n_ok = 31`, certifying the live shas
`check.py 006117e11d1bc4f0…` · `s2audit.lean 2c4a689fc1257735…` · `screen.py cc591ca662684e8d…` ·
`assemble.py 11698336484a92d4…` · `sandbox_check.sb f0e34eee14330ba9…`. Record at
`~/s2-controls-amend14-clean.json` (copied into the evidence dir).

📌 **`C_notation_noscreen` and `B_notation_noscreen` still return `STATEMENT_ALTERED`** — the refuter-F3
notation-hijack controls, which are the real question this amendment could have broken. They fire under the
amended comparison exactly as before: **the normalisation removed a naming artifact, not the gate.**

`controls_gate.py` driven BOTH ways on the same live harness:
- fresh record ⇒ **`CONTROLS GATE PASS`**, all 5 checker shas matched;
- the OLD landed record ⇒ **`CONTROLS GATE REFUSE`**, naming both drifted files
  (`check.py … 9aa58095 → 006117e1`, `s2audit.lean … 37ccc2c5 → 2c4a689f`).

⛔ **THE FIRST CONTROLS RE-RUN CAME BACK 28/31 AND IS KEPT AS A SPECIMEN, NOT AS A RESULT** —
`C_pos`/`C_neg`/`C_ax` all `HARNESS` at `audit=0.1 s`, because I was driving the new selftests against the
same harness dir and **killed their audits through §6's defect.** It is in the evidence dir beside the clean
run. *The stale record is kept and not trusted; it is the specimen.*

---

## §10 LAWS THIS AMENDMENT ADDS

- ***"Verified at the artifact" names a habit, not a guarantee — the question is always "which artifact, and
  who wrote it."*** A finding about what an AGENT did must be measured on a file the AGENT wrote; a harness's
  own composition can only ever testify about the harness.
- ***A structural comparison of a frozen declaration's elaborated value is not a comparison of that
  declaration — it is a comparison of the whole module.***
- ***A normalisation that routes through a printed form is not a normalisation:*** printing re-introduces
  every distinction the comparison was chosen to ignore.
- ***A dead field is not a cheap field*** — it is a measurement taken, paid for, and discarded at the point of
  use, and its absence from the verdict is invisible by construction.
- ***"No data" is not 0***, and a `PROVISIONAL` prefix does not repair a band: it qualifies a reading that
  still names one.
- ***An explanation that quotes the thing it forbids is the thing it forbids.***
- ***A fixture that cannot be built proves nothing*** — refuse the arm, never skip it.
- ***A repair that hides the number it changed cannot be audited*** — carry the pre-change verdict in the
  record for ever.
- ***A sweep whose pattern names a shared file does not clean up after itself — it cleans up after
  everybody.*** A cleanup belt must name something only this invocation owns.
- ***Reproducing a defect is not the same as gating it:*** a gate must fail on the broken version EVERY time,
  and a race only fails sometimes. Test the mechanism, not the symptom — and a gate whose RED control only
  fires under load reads green for ever.
- ***A number typed into an amendment is a claim; one computed by the instrument is a measurement*** — applied
  here to a budget, not just to a population.
