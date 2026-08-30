# The axiom audit did not change the number — but it closes a hole the reference checker leaves open

**S2-Lean stage-0 audit finding · bench seat · 2026-08-29 · row p option (d), run with its kill-check**

Status: **the headline claim this document set out to publish was REFUTED by its own kill-check.**
What survives is narrower, measured, and different in kind. Both halves are reported below, in the
order they were found.

---

## 0. The claim, and what happened to it

The 2026-08-29 F3 read (a0, stage B, CLEVER, n=15, Sonnet-5) came back **2/15 = 13.3%**, of which
**11/15 were class `AXIOMS_FAIL` with `sorryAx`** — the model wrote a compiling formal spec, could
not prove it isomorphic to the ground-truth spec, and closed the proof with `sorry`.

Because SaltBench's `check.py` classifies by the *first failing gate*
(`COMPILE → KERNEL_REJECTED → STATEMENT_ALTERED → AXIOMS_FAIL → PASS`, `check.py:135,190-194`),
`AXIOMS_FAIL` means: compiled ✓, kernel replay ✓, statements byte-identical ✓, **only the axioms
wrong**. Dropping the axiom gate from *our* checker therefore rescores those 11 as `PASS` and turns
13.3% (floor) into 86.7% (saturated) — the same run, the opposite diagnosis.

That counterfactual is correct **about our checker**. It was then extrapolated to CLEVER's, as
*"CLEVER's reference numbers are sorry-inflated — 11/15 close `spec_isomorphism` with `sorryAx` and
pass every gate an audit-less checker has."* The kill-check named for that claim was: run CLEVER's
own reference checker over our 11 `AXIOMS_FAIL` artifacts and show it returns PASS.

**It does not.** CLEVER's reference checker rejects all 11, for a reason our counterfactual did not
model: it has no axiom audit, but it does have a *sorry grep*, and on an honest `sorry` the two gates
see the same event.

---

## 1. Method — their code, their data, our artifacts

Nothing of ours adjudicates anything in §2–§4. Their `Benchmark` parses their `human_eval` files,
their `ProblemViewTask.get_view` builds the `SPEC_ISOMORPHISM` view, and their
`ProblemViewTask.submit_async` assembles, compiles and scores. We inject only the three fields a
solver is meant to fill: the generated spec, the isomorphism proof, and the isomorphism helper
lemmas. `submit_async` is the entry point CLEVER's README documents for submissions ("Each
submission is compiled and verified using Lean 4", README §"Submitting Your Solutions to CLEVER").

| pin | value |
|---|---|
| CLEVER | `8348039a7ff7730a126d761e71d0439735eeb3e2` (2026-08-26), MIT |
| Lean / mathlib | `leanprover/lean4:v4.27.0` / `a3a10db0e9d66acbebf76c5e6a135066525ac900` |
| SaltBench freeze | `d516ad4` · `check.py` sha256 `9aa58095579dfc7d…` |
| artifacts | the 15 a0 stage-B episodes of the 2026-08-29 F3 read |
| probes | `harness/s2lean/audit/{killcheck,mutate,axprobe}.py`, results in `evidence/audit-2026-08-29/` |

**Cross-validation, recorded before any result was read:** for all 15 problems, the
`isomorphism_theorem` and the ground-truth `problem_spec` that *their* parser produces are
byte-identical to the ones in *our* frozen views (`killcheck.json`, `their_thm_matches_ours` and
`their_gt_matches_ours`, 15/15). Our view builder is not the variable in anything below.

---

## 2. Kill-check — the headline claim is refuted

Their checker over our 15 stage-B artifacts, as submitted (`evidence/audit-2026-08-29/killcheck.log`):

| | their checker | our checker |
|---|---|---|
| `isomorphism_ok` / `passed` | **2/15** | **2/15** |
| agreement, per problem | **15/15** | |

Every `AXIOMS_FAIL` artifact → `isomorphism_ok=False`. Both `COMPILE` artifacts →
`compilation_ok=False` for them too. Both `PASS` artifacts → `isomorphism_ok=True`.

**Why the counterfactual was wrong.** `sorryAx` in `#print axioms` and Lean's
`declaration uses 'sorry'` warning are two views of one event. CLEVER greps the build log for exactly
that warning (`task.py:171`, `_extract_sorry_lines` at `task.py:196-206`) and fails the submission if any line
matches, anywhere in the file. SaltBench's `check.py` *records* the same warning lines
(`check.py:131`) but never gates on them — the axiom audit is the only thing standing between an
admitted `sorry` and a `PASS`. So "our checker minus its axiom gate" is a checker with **neither**
gate, which is not CLEVER and not any checker anyone ships.

⇒ **On honest artifacts our instrument and the reference instrument agree exactly.** The 13.3% F3
read is not an artifact of a stricter checker; it is what CLEVER's own checker says about the same
work. The F3 HOLD stands, unchanged and now externally corroborated.

---

## 3. What the kill-check turned up instead — the statement is not held fixed

`submit_async` reconstructs the problem from the benchmark and then does not use it:

```python
122  original_problem = self.get_view(int(problem.problem_id))
123  # Only change the proofs and helper lemmas
124  original_problem.problem_spec_formal_generated = problem.problem_spec_formal_generated
…
129  original_problem.correctness_helper_lemmas = problem.correctness_helper_lemmas
…
134  lean_code, proof_ranges = format_problem_as_lean_with_line_ranges(problem)   # ← not original_problem
```

`original_problem` is a **dead store**. The file that gets compiled and scored is the view the
*solver* submitted — including the fields the comment on line 123 says are held fixed. The intent is
in the comment; it is absent from the code.

Measured, on the same 15 artifacts, changing one line — the theorem to be proved — to
`theorem spec_isomorphism : True :=` / `trivial` (`evidence/audit-2026-08-29/mutate.log`):

| variant | certified by their checker |
|---|---|
| as submitted | 2/15 |
| **M1** — model's own spec and helper lemmas kept, only the theorem+proof replaced | **13/15** |
| **M2** — M1 with the model's helper lemmas dropped | **15/15** |

(M1's two failures are the two artifacts whose *helper lemmas* do not compile; dropping them is M2.)

Exhibit: `evidence/audit-2026-08-29/exhibits/problem_69.M2-statement-replaced.lean` — the generated
spec and the ground-truth spec are both still there, verbatim, and the theorem tying them together
reads `theorem spec_isomorphism : True`.

**What this is not.** This is a soundness hole for third-party submissions, not evidence that any
published CLEVER number is wrong. The leaderboard's baselines are the authors' own agents; we have
no artifact suggesting any of them altered a statement, and we did not look. Having just been
corrected by a kill-check for extrapolating from our instrument to theirs, this document does not
make the same move twice.

---

## 4. The gate that is genuinely missing — no statement edit required

The mutation in §3 is loud: a reviewer reading the file sees `: True`. The axiom route is not.

Submit the isomorphism theorem **exactly as the benchmark produced it** (verified per problem:
`thm_untouched=True`, 15/15), add one helper lemma

```lean
axiom cheat (P : Prop) : P
```

and discharge the real goal with `cheat _`. The file compiles. An `axiom` is not a `sorry`, so Lean
emits no `declaration uses 'sorry'`, so their grep sees nothing.

**CLEVER's reference checker certifies 15/15** (`evidence/audit-2026-08-29/axprobe.log`). Run
`#print axioms spec_isomorphism` on the very same file and it says, on every one of the 15:

```
'spec_isomorphism' depends on axioms: [cheat, propext, Classical.choice, Quot.sound]
```

This is the gap SaltBench's allowlist `{propext, Classical.choice, Quot.sound}` exists to close, and
it is the one place where the audit does work no sorry-grep can do. The same route covers `axiom`
declarations, `native_decide` (`ofReduceBool`, `Lean.trustCompiler`), and anything else that reaches
the kernel without a `sorry` token. Our checker's statement-diff gate — the §3 hole — is separately
controlled and green (`s2-controls.json`, 30/30, including four `STATEMENT_ALTERED` controls that use
notation and `macro_rules` rather than a visible edit).

---

## 5. What this changes

1. **The F3 read is corroborated, not overturned.** 2/15 = 13.3% by our checker *and* by CLEVER's.
   HOLD (floor) stands. The F5 band divergence (flagged 0/9 vs unflagged 2/6) is untouched by this
   work and remains the sharpest open design question.
2. **The bank's ⭐⭐⭐ line is now wrong as written** and is corrected here: the axiom audit determined
   the sign of the result *against a checker with no gates at all*, which is a strawman. Against the
   reference checker it changed nothing. Its real value is §4 — adversarial artifacts, not honest ones.
3. **Our stage-B number is comparable in kind to CLEVER's published spec-certification numbers**,
   since the two checkers agree on this sample. (Comparable in kind, not in setting: the leaderboard's
   Claude Code row is a different scaffold, budget and model, and our draw includes flagged problems.)
4. **A disclosure to the CLEVER authors is warranted** for §3 and §4 (contact in their README). That is
   the Captain's call, not the seat's; the repo is private until IARC clearance, so nothing goes out
   without a word. Both findings are one-line-reproducible from `harness/s2lean/audit/`.

## 6. Laws this pass added

- **A counterfactual about someone else's instrument is a claim about their code, and must be run
  against their code.** Ours said "an audit-less checker passes these 11"; theirs is audit-less and
  passes none of them, because it has a different gate we had not modelled.
- **Two gates that agree on honest work can disagree completely on adversarial work.** The kill-check
  found agreement 15/15 and, three probes later, 2/15 vs 15/15 on the same artifacts. A checker's
  worth is not read off the population it was calibrated on.
- **The defect is in the incidental clause.** `original_problem` is built, mutated across six lines,
  and never read. The comment above it states the invariant the code drops.

## 7. Reproduction

```bash
# on the Studio, with ~/lean-shared/clever/.lake symlinked into the CLEVER checkout's src/lean4
python3 harness/s2lean/audit/killcheck.py episodes.json killcheck.json   # their checker, our artifacts
python3 harness/s2lean/audit/mutate.py    episodes.json mutate.json      # the dead store (§3)
python3 harness/s2lean/audit/axprobe.py   episodes.json axprobe.json     # the missing audit (§4)
```

Total model cost of this finding: **zero**. Three Lean compile passes over 15 problems, ~10 s each.
