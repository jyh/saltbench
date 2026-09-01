# STEP 0 — THE STAGE-B FAILURE TRIAGE (desk row AS, the SaltBench next-wave commission)

Seat `bench` · 2026-09-01 · **zero model tokens** (checker/analysis work over frozen artifacts)
Registered instrument: `SCOUT-S2LEAN-STAGE0.md` §2, "B-FAILURE TRIAGE (blind, by the seat, after the run,
from the two spec texts and the transcript)" — four labels, one per failed (problem, arm).
Commissioned by the helm's 09/01 08:53 bus post (row AS) as **STEP 0, owed before amendment 11**, on the
stated ground that *it bears on whether stage C's oracle (`problem_spec`) is clean on U15.*

It does. **It is not.**

---

## 0 · THE HEADLINE, BEFORE THE METHOD

1. **`problem_18` IS C-DEAD, AND THAT IS A THEOREM, NOT A JUDGEMENT.** In Lean v4.27.0
   `String.drop/take : String → Nat → String.Slice`, and `Slice` equality is *structural* — it forces the base
   strings equal. `problem_18`'s frozen `problem_spec` tests occurrences with
   `(string.drop i).take substring.length = substring`, so for the docstring's **own example** `("aaaa","aa")`
   the occurrence set is **empty** and the spec forces `result = 0`, while the frozen C view carries
   `#test implementation "aaaa" "aa" = 3` and a failing `#test` is `rc 1` (measured, not assumed).
   `stageC_problem18_unsatisfiable` — *no implementation satisfies `correctness` and passes the `#test` lines* —
   is machine-checked with axioms `[propext, Classical.choice, Quot.sound]`, the allowlist exactly, no `sorry`.
   ⇒ **The commission's fixed `n = 13` must become `n = 12`, and the gate registered at 13 must be re-derived
   at 12 BEFORE Step 1 spends a model token.** An episode run on `problem_18` cannot pass, would be scored as
   the arm's failure, and would be indistinguishable in the record from a failure of the method.
2. **22 of the 30 triageable failures (73 %) are not the agent failing to prove a true theorem — the stage-B
   obligation is FALSE.** 17 HUMAN-LOOSE + 5 AGENT-WRONG, over 5 of the 8 failing problems. Only 8 cells
   (3 problems) are PROOF-HARD.
3. **THE LABEL IS A PROPERTY OF THE PROBLEM, NOT OF THE ARM OR THE TIER — 8 problems, 8 single labels, no
   exceptions.** Across arms the label mix is flat (a0 7/2/3 · a1 4/1/2 · a2 6/2/3, exactly proportional to
   cell counts). The salt arm and the plain arm fail *for the same reason on the same problems*.
   ⇒ **This campaign's failure column has been measuring the substrate, not the arms.**
4. **FOUR MORE OF THE REMAINING TWELVE HAVE PERMISSIVE ORACLES** (`0`, `4`, `96`, `127`): each `problem_spec`
   is vacuous on a region its `#test` lines never visit, so stage C will certify implementations that are
   wrong there. Not fatal — stage C stays satisfiable — but it pushes `P0` **up**, toward the CEILING HOLD the
   helm already registered as the likely product. ⇒ **Part of the expected ceiling is an instrument property,
   and it should be read as one when the gate is read.**
5. Out of taxonomy, and reported rather than forced into a label: **the registered four-label scheme cannot
   express what was actually found**, and one label of the four is unreachable on this population by
   construction. §5.

---

## 1 · METHOD, AND WHERE THE BLINDING HELD AND WHERE IT DID NOT

**Population.** Every failed stage-B cell of U15 in both state roots — `~/bench` (Sonnet-5) and `~/bench-a8`
(Opus-5) — resolved by the frozen morning line's own rule (the scored row for `(task, stage, arm)` is the
LATEST by `end_utc` among `DONE|ROUNDS_EXHAUSTED|WALLCLOCK|TOKEN_CEILING`; three supersessions named and
dropped: `38/a0`, `73/a0`, `146/a0` in `~/bench`). **75 scored cells, 31 failed** — 21 Sonnet (7 per arm ×3),
10 Opus (5 per arm ×2), reproducing the record exactly (Sonnet 8/15 each arm, Opus 10/15 each arm).

**Provenance, checked three ways before a single label.** For all 31, the B row's `a_bodies_sha256` equals the
sha256 of the stage-A episode's own `bodies.json`, equals the field recorded inside
`state/s2/<task>/<arm>/A.bodies.json`, and the `generated_spec` text is byte-identical between the two
locations. 31/31 on all three. The corpus is the text that ran.

**Masking.** Each cell was rendered to a file keyed by an opaque token (`sha256(salt‖root|problem|arm)[:8]`),
carrying only: the NL docstring and examples, the human `problem_spec`, the `#test` lines, the isomorphism
theorem, the agent's `generated_spec`, the agent's stage-B proof body and helper lemmas. **Root (tier), arm,
`class` and `termination` were withheld from the labelling corpus.** Labels were assigned from those files
alone, then unmasked.

⚠️ **TWO LEAKS IN THE BLIND, NAMED RATHER THAN GLOSSED.** (a) Enumerating the population necessarily printed a
`(problem, arm, class)` table before the corpus was built, so the mask was against *reading* the arm, not
against having ever seen the table. (b) One cell de-masked itself: `Td4841f4e` is the only corpus entry using
`native_decide`, which is desk row AB's specimen, so I knew it was Opus `18/a0` while labelling it. ⇒ **A mask
applied by the same head that built the population is a discipline, not a guarantee** — the defence that
actually carries the weight here is §3's result: *the label is constant within a problem*, so no per-cell
knowledge of the arm could have moved a label.

---

## 2 · THE TABLE (31 cells)

| tier | problem | arm | class | termination | LABEL | witness in-file |
|---|---|---|---|---|---|---|
| Opus-5 | 0 | a0 | AXIOMS_FAIL | DONE | HUMAN-LOOSE | yes |
| Opus-5 | 0 | a2 | AXIOMS_FAIL | DONE | HUMAN-LOOSE | yes |
| Sonnet-5 | 0 | a0 | AXIOMS_FAIL | DONE | HUMAN-LOOSE | — |
| Sonnet-5 | 0 | a1 | AXIOMS_FAIL | DONE | HUMAN-LOOSE | — |
| Sonnet-5 | 0 | a2 | AXIOMS_FAIL | DONE | HUMAN-LOOSE | — |
| Opus-5 | 4 | a0 | AXIOMS_FAIL | DONE | HUMAN-LOOSE | yes |
| Sonnet-5 | 4 | a1 | AXIOMS_FAIL | DONE | HUMAN-LOOSE | — |
| Opus-5 | 18 | a0 | KERNEL_REJECTED | DONE | **AGENT-WRONG** | yes |
| Opus-5 | 18 | a2 | AXIOMS_FAIL | DONE | **AGENT-WRONG** | yes |
| Sonnet-5 | 18 | a0 | AXIOMS_FAIL | DONE | **AGENT-WRONG** | — |
| Sonnet-5 | 18 | a1 | AXIOMS_FAIL | DONE | **AGENT-WRONG** | — |
| Sonnet-5 | 18 | a2 | AXIOMS_FAIL | DONE | **AGENT-WRONG** | — |
| Sonnet-5 | 73 | a0 | AXIOMS_FAIL | ROUNDS_EXHAUSTED | PROOF-HARD | — |
| Sonnet-5 | 73 | a2 | AXIOMS_FAIL | ROUNDS_EXHAUSTED | PROOF-HARD | — |
| Opus-5 | 96 | a0 | AXIOMS_FAIL | DONE | HUMAN-LOOSE | yes |
| Opus-5 | 96 | a2 | AXIOMS_FAIL | DONE | HUMAN-LOOSE | yes |
| Sonnet-5 | 96 | a0 | AXIOMS_FAIL | DONE | HUMAN-LOOSE | — |
| Sonnet-5 | 96 | a1 | AXIOMS_FAIL | DONE | HUMAN-LOOSE | — |
| Sonnet-5 | 96 | a2 | AXIOMS_FAIL | DONE | HUMAN-LOOSE | — |
| Opus-5 | 112 | a2 | SCREEN | DONE | *(SCREEN-REFUSED — see §5.2)* | yes |
| Sonnet-5 | 112 | a0 | AXIOMS_FAIL | ROUNDS_EXHAUSTED | PROOF-HARD | — |
| Sonnet-5 | 112 | a1 | AXIOMS_FAIL | ROUNDS_EXHAUSTED | PROOF-HARD | — |
| Sonnet-5 | 112 | a2 | AXIOMS_FAIL | ROUNDS_EXHAUSTED | PROOF-HARD | — |
| Opus-5 | 127 | a0 | AXIOMS_FAIL | DONE | HUMAN-LOOSE | yes |
| Opus-5 | 127 | a2 | AXIOMS_FAIL | DONE | HUMAN-LOOSE | yes |
| Sonnet-5 | 127 | a0 | AXIOMS_FAIL | DONE | HUMAN-LOOSE | — |
| Sonnet-5 | 127 | a1 | AXIOMS_FAIL | DONE | HUMAN-LOOSE | — |
| Sonnet-5 | 127 | a2 | AXIOMS_FAIL | DONE | HUMAN-LOOSE | — |
| Sonnet-5 | 141 | a0 | AXIOMS_FAIL | ROUNDS_EXHAUSTED | PROOF-HARD | — |
| Sonnet-5 | 141 | a1 | COMPILE | ROUNDS_EXHAUSTED | PROOF-HARD | yes |
| Sonnet-5 | 141 | a2 | AXIOMS_FAIL | ROUNDS_EXHAUSTED | PROOF-HARD | yes |

**TOTALS (30 triageable + 1 out of taxonomy): HUMAN-LOOSE 17 · AGENT-WRONG 5 · PROOF-HARD 8 · SCREEN-REFUSED 1.**
**BY ARM:** a0 7/2/3 · a1 4/1/2 · a2 6/2/3 (+1 screen). **BY TIER:** Sonnet 10/3/8 · Opus 7/2/0 (+1 screen).

The registered reading rule says a low rate is a tier floor *only if AGENT-WRONG + PROOF-HARD dominate*. They
do not: 13 of 30 (43 %) against HUMAN-LOOSE's 17 (57 %). The rate is not in the `< 20 %` band, so the clause
does not fire — but the reading it encodes is the one that matters here, and it points at the substrate.

---

## 3 · WHY EACH LABEL, IN ONE LINE EACH

- **`0` — HUMAN-LOOSE.** `problem_spec`'s conclusion is guarded by `numbers.length > 1`; it is vacuous on lists
  of length ≤ 1. Every agent spec is total, hence strictly stronger. Two cells wrote machine-checked witnesses
  (`bad_impl` / `iso_counterexample`: correct on long lists, `true` on `[]`).
- **`4` — HUMAN-LOOSE.** Guarded by `0 < numbers.length`; vacuous on `[]`. One cell recorded
  `iso_forward_direction_false` with a witness parameterised over the value returned on `[]`.
- **`18` — AGENT-WRONG** (and see §4: the human spec is *also* broken, worse, and the taxonomy has no word for
  it). All five agent specs scan `List.range (|s| − |t| + 1)`, forcing `impl s "" = |s| + 1`; the frozen
  `#test implementation "a" "" = 1` demands `|s|`. Mechanical contradiction with a `#test` line ⇒ AGENT-WRONG
  by the registered definition. ⚠ **The deciding artifact was withheld from the arm that had to decide it:**
  the stage-A view (`views/problem_18/A.lean`) carries only the three NL examples and *not* the five `#test`
  lines; `"a" ""` appears in neither the docstring nor the NL examples. The docstring is silent on the empty
  substring and both readings are defensible. The label is mechanically correct and the finding is about the
  instrument.
- **`73` — PROOF-HARD.** The agent spec (count of mismatched mirror pairs) *is* the minimum number of changes;
  the human spec quantifies over all equal-length palindromes. Equivalent, and the equivalence needs an
  optimality argument. Both cells ROUNDS_EXHAUSTED on a bare `sorry`; no witness of non-isomorphism.
- **`96` — HUMAN-LOOSE.** `problem_spec` fixes membership only — never order, never multiplicity. Every agent
  spec pins the exact list or `Pairwise (· < ·)`. Witness recorded twice: `bad_impl n = primes ++ primes`
  satisfies `problem_spec` everywhere and fails `generated_spec 3`.
- **`112` — PROOF-HARD.** `problem_spec` is a recursive characterisation; the isomorphism is TRUE — a sibling
  cell **proved it completely** (amendment 9, `ep-6b5540c0`). The three remaining cells ROUNDS_EXHAUSTED on a
  bare `sorry`.
- **`127` — HUMAN-LOOSE.** Guarded by `s1 ≤ e1 → s2 ≤ e2 →`; vacuous on ill-formed intervals, where every
  (total) agent spec still forces `"YES"`/`"NO"`. Witness recorded twice (`maybe_impl`: correct on well-formed
  intervals, `"MAYBE"` elsewhere).
- **`141` — PROOF-HARD.** The specs agree; the obligation reduces to a `String.splitOn`/`splitOnAux`
  equivalence. Two cells wrote **7,033 and 8,086 characters** of String-library lemmas and still ran out of
  rounds. No witness of non-isomorphism.

📌 **THE PATTERN UNDER FOUR OF THE FIVE FALSE OBLIGATIONS IS ONE DEFECT.** `0`, `4`, `127` (and `96` in its own
way) are all *the human spec guarding its conclusion with a well-formedness hypothesis and thereby saying
nothing outside it*, while `generated_spec` — as a `Prop` over the same signature, which is what stage A asks
for — is total. ⇒ **A GUARDED SPECIFICATION AND A TOTAL SPECIFICATION ARE NEVER ISOMORPHIC, AND STAGE B ASKS
FOR AN ISOMORPHISM.** The task as posed is unsatisfiable on every problem whose reference spec is guarded, and
nothing in the stage-A prompt tells the agent to guard.

---

## 4 · `problem_18`: THE ORACLE CONTRADICTS ITS OWN TESTS (machine-checked)

Everything here is in `evidence/step0-b-triage-2026-09-01/`, driven at `~/lean-shared/clever` on the Studio
with the campaign's pinned toolchain (Lean v4.27.0, mathlib `a3a10db0`).

**The mechanism.** `probe18_slice.lean` establishes, kernel-checked:
`String.drop : String → ℕ → String.Slice`, `String.take : String → ℕ → String.Slice`; and
`¬ ((("aaaa").drop 1).take ("aa").length = ("aa"))` — because `Slice` equality is structural, so it forces
`congrArg String.Slice.str : "aaaa" = "aa"`. **The occurrence test is false at a genuine occurrence.**

**The consequence.** `probe18_unsat.lean` takes the frozen `problem_spec` verbatim from
`views/problem_18/frozen.json` and proves, with **axioms `[propext, Classical.choice, Quot.sound]` — the
allowlist exactly, no `sorry`, `rc 0`:**

```
occ_set_empty                        : the occurrence set for ("aaaa","aa") is ∅
occ_card_zero                        : hence its Finset card is 0
problem_spec_forces_zero_at_aaaa_aa  : problem_spec impl "aaaa" "aa" → impl "aaaa" "aa" = 0
stageC_problem18_unsatisfiable       : ¬ ∃ impl, (∀ s t, problem_spec impl s t) ∧ impl "aaaa" "aa" = 3
```

**And the `#test` line is enforced.** `probe_test_is_an_error.lean` drives a deliberately false `#test` and
measures `error … Found a counter-example!` with **`RC=1`** — matching `check.py`'s own header
(*"Stage C's `#test` lines are IN the canonical file: a failing test = rc 1 = COMPILE"*). So a `problem_18`
stage-C episode can reach `PASS` by no route: satisfy `correctness` and the `#test` fails (`COMPILE`); pass the
`#test` and `correctness` is unprovable (`AXIOMS_FAIL`).

**Why the existing gate did not catch it.** `view_status.json` records `problem_18: {A: ok, B: ok, C: ok}` and
`c_dead = [39,44,54,62,65,77,81,87,97,110,111,112,113,119,153,155,157,160]` — 18 is not among them.
`c_dead` is an **elaboration** check: it asks whether the C *view* compiles, which it does. ⇒ **`c_dead` MEASURES
WHETHER THE TASK CAN BE STATED, NEVER WHETHER IT CAN BE DONE** — a fifth instance, in a fifth place, of this
seat's recurring defect: *a gate that reads a proxy for the thing instead of the thing.*

**Scope, measured not eyeballed.** A text sweep of all 161 frozen `problem_spec`s for `take|drop|extract|
dropRight|takeRight` returns **31 problems**; intersected with the 13 C-eligible U15 problems it returns
**{18, 38, 142}**. `38` operates on `List Char` and `142` on `List Int` — list operations, no `Slice`
involved. ⇒ **Within the commission's population, `problem_18` is the only carrier of this defect, and it is
fatal.**

---

## 5 · WHAT THE FROZEN TAXONOMY COULD NOT SAY (reported, not silently re-interpreted)

The four labels are frozen and I did not edit them. Two things did not fit, and forcing them in would have
hidden the finding:

**5.1 · `HUMAN-BUGGY` IS UNREACHABLE ON U15 BY CONSTRUCTION.** Its registered definition is *"agent spec
contradicts a **flagged** clause"* — and `U15 = D ∖ flagged_spec_ids` by definition. **A four-label taxonomy
applied to a population that excludes one label's precondition is a three-label taxonomy**, and it is the label
that would have carried `problem_18`'s real defect: not *loose*, but **wrong** — a reference spec that
contradicts its own shipped tests. `problem_18` is scored AGENT-WRONG above because the agents *do*
mechanically contradict a `#test` line; that label is correct and it is not the whole truth. **The taxonomy
has no cell for "both specs are wrong, in different places."** Amendment 11's business, registered before use.

**5.2 · ONE OF THE 31 "FAILURES" NEVER FAILED TO PROVE ANYTHING.** `Opus 112/a2` (`ep-6b5540c0`) carries
`class = SCREEN`: it was refused by the pragma screen and **never compiled**. Amendment 9 established that it
is a **complete kernel-checked proof**. It is excluded from the four-label counts and reported as
SCREEN-REFUSED, because triaging a proof failure that did not occur would manufacture a data point. It is
also, incidentally, the strongest evidence for `112`'s PROOF-HARD label: the theorem its siblings could not
prove is provable, and one of them proved it.

---

## 6 · A SEPARATE, SMALLER FINDING FOUND WHILE CHECKING PROVENANCE

`s2_morning_line.py:164-167` (`agent_body`) intends to use the staged
`state/s2/<task>/<arm>/A.bodies.json` *only when it is provenanced*, guarding with
`sha256(A.bodies.json) == m["a_bodies_sha256"]`. **That guard can never be true**: `A.bodies.json` is a
*wrapper* that adds five metadata keys around the episode's `bodies.json`, so its hash differs from the
wrappee's hash by construction. Measured over all **78** U15 stage-B rows in both roots
(`measure_dead_guard.py`): **first branch taken 0 · fallback taken 78 · fallback text identical to the staged
text 78 · neither 0.**

**No reading changes** — the fallback reads the same bytes, 78/78 — so this is not a correction to any landed
number. What it is: **a provenance guard that has never once guarded**, in the recall instrument, which is the
component that can withhold the F3 band. Not repaired here: a repair to a pinned instrument is a dated
amendment, and this one is a no-op today. ⇒ **A GUARD WHOSE PREDICATE CANNOT HOLD IS INDISTINGUISHABLE FROM NO
GUARD, AND IT LOOKS LIKE A GUARD IN EVERY REVIEW.**

---

## 7 · WHAT THIS OWES AMENDMENT 11 (recommendations; the amendment registers them, this document does not)

1. **`n = 12`, not 13.** Drop `problem_18` with the §4 proof as the ground, and **re-derive the gate at 12** —
   the commission's `P0 ≤ 2 ⇒ FLOOR` / `P0 ≥ 9 ⇒ CEILING` / `3 ≤ P0 ≤ 8 ⇒ Step 2` were fixed against 13.
2. **A C-ORACLE PRE-FLIGHT, red-first, before Step 1.** `c_dead` proves the view elaborates; it does not prove
   the task is winnable. The check that would have caught `problem_18` a week ago is: *for each problem, is
   `problem_spec` consistent with its own `#test` lines?* Cheapest sound form: the CLEVER reference
   implementation + its correctness proof, run through `check.py` as a stage-C control — the shape
   `s2-controls.json` already uses for `problem_0` alone. ⚠ It needs the CLEVER source back on the Studio
   (deleted from the shared clone at boot; pin `8348039`), which is a fetch and belongs in the amendment.
3. **State the guarded-vs-total problem in `prompt_A.md`, or accept that stage B is unwinnable wherever the
   reference spec is guarded.** Four of eight failing problems are that single defect. This is the stage-A
   sibling of desk row AV's `native_decide` question and should be ruled with it.
4. **Register the taxonomy gap (§5.1) before it is used**, and keep the SCREEN-REFUSED cell out of any
   failure-mode denominator (§5.2).
5. **Read the gate knowing four of the twelve oracles are permissive** (§0.4). A ceiling read on this
   population is partly an instrument reading.

## 8 · REPRODUCTION

```
evidence/step0-b-triage-2026-09-01/
  sweep_stageB_rows.py        the population sweep (piped to the Studio; both roots)
  cells_unmasked.json         31 cells: both spec texts, proof, helpers, class, termination, provenance
  masked-corpus/*.txt         the 31 files the labels were actually assigned from (arm/tier/class withheld)
  triage_labels.json          the per-problem label and its one-line ground
  triage_table.json           the unmasked table of §2
  probe18_slice.lean/.out     String.Slice structural equality, kernel-checked
  probe18_unsat.lean/.out     stage C on problem_18 is unsatisfiable, axioms = the allowlist, RC=0
  probe_test_is_an_error.*    a failing #test is an error with RC=1
  measure_dead_guard.py       78/78 rows take the fallback; the §6 guard never fires
```
Lean probes: `ssh kriterion 'bash -lc "cd ~/lean-shared/clever && lake env lean <file>"'`.
