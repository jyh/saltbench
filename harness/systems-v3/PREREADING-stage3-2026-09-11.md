# PRE-READING REGISTRATION — STAGE ❸, the 14 conditions
**bench (SaltBench lead) · 2026-09-11 · written while 12 of the 14 conditions are UNRUN**

⛔⛔ **WHAT THIS IS AND WHAT IT IS NOT.** It is **not** an amendment to what Stage ❸ measures — the
design is the council's ruling of 2026-09-11 §1 and the declared cap set, and **the first model call
already happened at 16:35:50Z.** It registers **HOW THE RESULT WILL BE READ**, so the reading is not
chosen after the numbers arrive.
⚠️ **AND ITS OWN HONESTY BOUND, STATED FIRST: conditions 1 and 2 have already landed** (Crc32 plain and
Crc32 plain+statement, 3/3 landed and 3/3 at 6/6 each, zero truncations). **So this is registered
before TWELVE of fourteen conditions, not before all fourteen, and every clause below is weaker for
those two than for the rest.** A registration that hid that would be worth less than none.

## §1 · THE UNIT OF REPORT, AND WHAT IS NOT POOLED
One row per **condition** = (problem × arm), n = 3. Arms: `plain` · `plain+statement` · `salt-diet` ·
`salt-diet+statement`; Paxos carries only its two bare arms (its statement arms are unconstructible —
its spec IS proof obligations, established at stage ⓿).
```
  per cell     TESTS k/N (the withheld suite) · T · truncations · result events · the four probes
  per cell     the salt-diet RESIDUAL, beside the verdict — accepted in BOTH conditions by the
               council's ruling, because the mechanism is the verifier and bare salt-diet runs it too
  per row      n, and the registered resolvable floor 2.0072x AT n=3, PER PROBLEM
```
⛔ **NOT POOLED ACROSS PROBLEMS.** The floor is per-problem and n is not uniform across the campaign.
⛔ **NOT POOLED ACROSS CAP REGIMES.** Every Stage ❸ cell runs under one declared cap set recorded in
its own `ctl/caps.tsv`. **Pre-existing cells of the same (problem, arm) that carry no `caps.tsv` are a
different configuration and do not enter these rows** — this is why five Crc32 plain cells already on
disk were not folded in.

## §2 · ⛔ WHAT A LANDING MEANS, REGISTERED BEFORE THE RATES EXIST
**A landing is the subject stopping.** Stage ❶ produced three cells that landed and passed 8/8 while
grading themselves 8×DONE, 8×PARTIAL and 8×NOT; the +statement condition produced cells that landed
and scored 0/8. ⇒ **No landing rate is the verdict, in either direction.** The withheld suite is the
only party that separates them, and **`k/N` is k TESTS, not k REQUIREMENTS** — each suite's own
`tags.json` says which requirements its tests can and cannot see.

## §3 · ⛔⛔ TRUNCATIONS AND RESULT EVENTS ARE REPORTED TOGETHER, ALWAYS
`--print-timeout` is a per-turn wall clock and **it binds the treated arm and not the control** —
measured at the old 300 s default: plain 0 of 9 and 0 of 3; salt-diet 2 · 4 · 3 in Stage ❶ and more in
Stage ❷. **Raising it to 1800 s reduced and did not remove them, and raising it killed the next cell**
by inverting the client/controller ordering.
⇒ **THE REPORTING RULE: truncations AND result events, per cell.** ***A cell with zero truncations and
zero results is not a fixed cell, it is a killed one.***
⇒ **A per-turn wall clock cannot be made arm-neutral for an arm that runs a verifier.** Where a
residual remains it is **declared with its sign** and not chased, per the Stage ❷ ruling.

## §4 · ⚖️ WHAT EACH OUTCOME WOULD MEAN — REGISTERED NOW SO IT IS NOT CHOSEN LATER
```
  (a) treated ≥ control on TESTS, within a problem
      the condition produces code that passes what the control's code passes.  With the cost rows,
      this is the campaign's positive shape.  ⛔ NOT a claim about magnitude: every per-problem
      premium measured so far sits BELOW the registered 2.0072x floor, and a ratio below the floor
      is UNRESOLVED whatever its point estimate.
  (b) treated < control on TESTS
      ⛔ READ IT AGAINST §3 FIRST.  Every cap in the launch path binds the treatment first, so a
      deficit is confounded in a KNOWN direction and the confound must be measured before the
      deficit is reported as an effect.  A bias against the arm under test cannot manufacture a
      positive — but it can manufacture a negative, and that is this direction.
  (c) treated = control on TESTS with a large cost premium
      the honest reading is that the method buys something other than pass rate on THIS substrate.
      ⛔ It is NOT licence to go looking for a different metric until one separates.
  (d) the salt-diet arms decline to ship an implementation and say so in LANDING.md
      already observed at n=5 in Stage ❷'s +statement condition (4 of 5).  If it repeats here it is
      a RESULT ABOUT THE CONDITION, reported as such, and the suite is what separates it from a
      landing.
```
⛔⛔ **NO p-VALUE CLAIM AND NO POOLED RATE ACROSS PROBLEMS.** The design's primary reading is the
registered cross-problem SIGN test; it is **one-sided by registration** and five-of-five BELOW gives
p = 1.0000 and cannot refute. **The larger surprise is the one this design cannot call significant,
and that was registered in advance rather than discovered afterwards.**

## §5 · VOIDS, EXCLUSIONS, AND THE DIRECTION EACH ONE FLATTERS
Any excluded cell is named with its class, its arm, and its problem.
⇒ 🔑 ***AN EXCLUSION IS A CLAIM ABOUT A POPULATION, AND A COUNT WITHOUT THE ARM SPLIT CANNOT BE
CHECKED FOR SKEW.*** The campaign has already measured one arm-correlated exclusion (44 % against
67 %) and one arm-correlated token floor (plain 12 · salt-diet 5, which biases any cross-arm ratio
UPWARD, i.e. toward the treatment looking dearer).

## §6 · COST, AND ROW `KS`
**Tokens beside dollars, in the cell, never in a caption.** Where the reading is a RATIO table, the
token MEDIAN goes beside the dollar median and **no token PREMIUM is added** — `$/T` and `$/output`
rank the arms oppositely, so a second premium is a second verdict quantity, not a second rendering.
**A token premium is a new reading and needs its own registration.**

## §7 · MODEL IDENTITY
Every cell pins `gemini-3.1-pro-high` and the client's log echoes a matching label. **An echo is
corroboration of our own request, not evidence of what was served**, and the vendor transcript carries
no model field. ⇒ **DECLARED, never VERIFIED**, in that language, in every row.
📌 The requested-name channel is not even stable across models: a PostInvocation hook recorded
`modelName = gemini-pro-agent` for a `--model gemini-3.1-pro-high` launch. **Whatever eventually
verifies the served model, it is not anything the client writes about itself.**

## §8 · CONTAINMENT, AT ITS REAL STRENGTH
`p_exposure` reads `sensitive=3/10 root=readable peer=denied`, verdict `NOT-A-DATUM` by the registered
criterion, which requires `sensitive=0`. **Recorded, not gated, and stated in the result rather than
left in the cells.**
⛔ One channel was found and closed during this stage: a read-only preservation copy of three landed
salt-diet cells was **readable from inside the fence** (driven: rc 0, 13,291 B) because the deny-set is
a `cells-*` glob and a rescue root is not named `cells-`. **Conditions 1 and 2 were rendered before the
rename and carry the permissive entry; both are CONTROL conditions**, the direction that cannot
manufacture a positive for the treatment. **Conditions 3 onward are rendered after it, and the fix is
driven in three arms.**
