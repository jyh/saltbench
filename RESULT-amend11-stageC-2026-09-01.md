# RESULT — AMENDMENT 11 STEP 1: S2-LEAN STAGE C, `a0`, THE REGISTERED 12, AT `claude-opus-5`

**Authorization** saltbench `8de0b74` (amendment 11 FROZEN, F2), instruments repaired by amendment 12.
**Objection window** opened by the freeze; RELEASED by the Captain at the helm 2026-09-01 14:1x
("unblock it so that it can run everything to completion"), bus offset 30441837.
**Dispatch** 2026-09-01T21:13:09Z · **DRIVER DONE** 22:09:49Z · **run root** `/Users/jyh/bench-c` (fresh).
**Enforcer** `halt_watch.sh … C a0 50000000 12` ARMED 21:12:33Z, **56 s before the first episode**; it exited
**0 on the driver's own DONE line** at `tok=4339167 landed=12`. No `HALT` file was ever written.

---

## §1 · THE GATE READ — `P0 = 12` ⇒ **CEILING HOLD**

Read once, at `ML_ARMS=a0`, from the REGISTERED POPULATION line, per §2's rule:

    REGISTERED POPULATION UC = U ∖ c_dead (amendment 11's gate is a COUNT over THIS set, not a rate over
    the 22 above)  n=12 ids [73, 0, 146, 16, 4, 38, 142, 96, 141, 31, 127, 74]: a0 proven 12/12 = 100.0%

**§4's table: `P0` = 12 lies in 8–12 ⇒ CEILING HOLD. STEP 2 DOES NOT RUN, and STEP 3 cannot arise.**

⭐ **AND AT 12/12 THE CEILING IS NOT A THRESHOLD, IT IS AN EMPTY SET.** The registered reachability argument
is `c ≤ n − P0`, where `c` = a2-only passes. At `P0 = 12` that is **`c ≤ 0`**: not "a salt-positive read is
improbable" but ***there is no problem left on this population for a salt arm to win.*** The bar the
commission wrote (`c − b ≥ 5`) is unreachable by construction, not by margin. Running `a2` here could only
have produced ties and losses, at ≈4M tokens, and it would have measured the population's exhaustion rather
than the method.

**§2's GUARD, DISCHARGED AT THE OBJECT.** The guard requires the landed stage-C rows to be **exactly** the
registered 12 or the read is void. `s2-landings.log` holds **12 rows and only 12**, one per registered id,
every one `DONE`; the instrument reports **12 counted rows, 12 resolved, 0 superseded, 0 unscored, 0 orphan,
0 synthetic**, and the proven list is byte-identical to the registered set. `constants` is **uniform and
exactly the registered regime** — `[(100, 10800, 20000000, 'claude-opus-5', 'high')]`.

**INTEGRITY BLOCK: ALL EMPTY.** `KERNEL_REJECTED []` · `STATEMENT_ALTERED []` · `PROVENANCE (AP-4) []` ·
`AXIOMS_FAIL []` · orphan-B `[]` · superseded `[]` · unscored `[]` · rows outside the draw `[]`.
Classes: `{'PASS': 12}`. Terminations: `{'DONE': 12}`. **Model verified at the manifests, never the banner:
`claude-opus-5` in all 12 episodes, 7–27 calls each.**

⚠️ **A MISREADING SURFACE THIS RUN EXPOSED, AND IT IS THE SAME FAMILY AS THE ONE §2 CLOSED.** At a
stage-C-only root the instrument's HEADLINE line reads
`READING: PROVISIONAL (F3 NOT YET READABLE) — HOLD (<20%: a floor…)`, and its stage-A/stage-B lines read
`0/27`. **That is F3 — stage B — which by §5 deliberately never ran here, and it is not this amendment's
gate.** It prints ABOVE the stage-C block and says HOLD for an entirely different reason than the gate does.
The two agree today by accident; at `P0 = 5` they would have disagreed while both saying "HOLD".
⇒ ***an instrument that reports a stage it was not asked to run states a floor it did not measure.***
Registered here as an OWED reading-instrument repair, not applied (it is a protocol change and needs its own
dated amendment) — and the operating rule until then: **at a stage-C root, read the stage-C block and the
REGISTERED POPULATION line, and ignore the F3 headline entirely.**

---

## §2 · §8 — THE PERMISSIVE-ORACLE DIAGNOSTIC. **`f_vac = 0/4 = 0.000`**

Registered before the run *precisely because* a CEILING is predicted by two different causes. §7's own words:
*"if the CEILING fires, 'the tier is strong' and 'the oracle is permissive' both predict it, and the
registered result cannot distinguish them. §8 is the instrument that can."*

All four permissive specs passed, so the denominator is full. Every certified implementation was evaluated at
its **frozen** probe point, inside the region its own spec cannot constrain:

| problem | why vacuous there | probe | value | verdict |
|---|---|---|---|---|
| `0` | spec guarded by `numbers.length > 1` | `impl [] 0.5`, `impl [1] 0.5` | `false`, `false` | CORRECT |
| `4` | spec guarded by `0 < numbers.length` | `impl []` | `0` | CORRECT **[soft cell]** |
| `96` | spec fixes membership only — never order or multiplicity; `7` is not a `#test` input | `impl 7` | `[2, 3, 5]` | CORRECT |
| `127` | spec guarded by `s1 ≤ e1 → s2 ≤ e2`; `(5,0)` is ill-formed, so even the totality clause is switched off | `impl (5,0) (0,10)` | `NO` | CORRECT |

**`f_vac = 0/4`; hard cells only (excluding `4`, whose docstring genuinely leaves MAD of `[]` undefined):
`0/3`.** ⇒ **NOT ONE of the twelve passes was bought with oracle permissiveness at a point where it was
available for free.** The agents wrote implementations that are **right where the specification could not
have forced them to be** — they answered the docstring, not merely the `problem_spec`.

⛔ **THE LIMIT OF THAT SENTENCE, STATED HERE RATHER THAN LEFT TO BE FOUND.** This is **n = 4, one probe
region each, five evaluated points in total**. A vacuous region is infinite and the probe visits a corner of
it. ***It refutes; it does not certify.*** What is licensed: *the cheapest and most obvious way to exploit
this oracle was not taken.* What is **not** licensed: "the implementations are correct". Amendment 11 §8's
own instruction governs the use of this number — **beside `P0`, never against it.** It does not change the
record, any episode's class, or the gate.

---

## §3 · PREDICTIONS, SCORED — **ONE HELD, ONE FAILED, ONE UNSCOREABLE, ONE SPLIT**

**1. `P0 ∈ [8,11]`, point estimate 9 ⇒ CEILING HOLD fires and Step 2 never runs. — BRANCH HELD, INTERVAL FAILED.**
The branch is right and the number is outside the interval I registered: **`P0 = 12`, and 12 ∉ [8,11]**.
📌 The miss has a direction worth naming: **12 was the reachable maximum and I excluded it.** My registered
interval could not contain the outcome in which the tier simply solves the whole population. Scored as a
miss on the interval; the branch clause is the half that held.

**2. Most common non-pass is `AXIOMS_FAIL` with `sorryAx`; `COMPILE` materially more common at C than at B. —
UNSCOREABLE.** There are **zero non-passes**. This prediction has no denominator and is recorded as
unscoreable, **not** as held. *A prediction about the shape of failure is silent in a run without failures,
and calling that a success would be the cheapest kind of hindsight.*

**3. `m_C > 1` — median stage-C tokens exceed stage B's 399,454. — FAILED, AND ON THE SIGN.**
Measured median (governing) **284,716 ⇒ `m_C` ≈ 0.71**; on `metered_sum`, 263,190 ⇒ 0.66. I predicted only
the sign, on the grounds that the sign was what the evidence supported, and **the sign is wrong**: stage C is
**cheaper per episode than stage B**, not dearer. The mechanism is visible in the artifacts — stage B asks for
an isomorphism proof against a *human* spec and is where this campaign's episodes ground; stage C asks for an
implementation and a correctness proof, and at this tier that is the easier half. The CLEVER leaderboard
asymmetry I cited in §7.1 (Task 2 ≈65 % vs Task 1 ≈42 %) predicted the RATE correctly and I failed to carry
the same asymmetry into the COST.

**4. Per item: passes include `{0,4,16,31,73}`; failures concentrate in `{141,142,146}`. — SPLIT, AND THE
DISCRIMINATING HALF FAILED.** The pass clause held **vacuously** (everything passed). The failure clause is
**refuted outright: all three named problems passed** — `146` in 182 s, `142` in 281 s, `141` in 584 s.
⭐ **`141` is the sharp one.** At Sonnet stage B it burned **11,757,659 tokens across 100 calls and FAILED**;
here it certifies in **912,687 tokens and 584 s**. This is the 08/31 law measured a second time and harder:
***a cost model built on a weaker model's failures models its flailing and does not transfer up a tier.***

---

## §4 · PRICE — **4,352,098 METERED / 56.7 MIN**, THE FIFTH CONSECUTIVE OVER-ESTIMATE

| | registered (§6) | actual |
|---|---|---|
| Step 1 total | central 14.7M · corner **34.8M** · commission 8–24M | **4,352,098** |
| wall | ≤12 h HALT | **3,400 s = 0.94 h** |
| per-episode governing | — | p50 **284,716** · p90 333,730 · max 949,908 · min 138,912 |
| calls | R=100 | median **12** (min 7, max 27) — the cap was never approached |

**The run cost 30 % of my central estimate and 12.5 % of the pessimistic corner, and came in BELOW the
commission's own low end of 8M.** Zero `ROUNDS_EXHAUSTED`, zero `WALLCLOCK`, zero `TOKEN_CEILING`, zero
HALTs, zero retries, zero holds. The 50M budget arm never rose above **8.7 %** of its threshold.

⇒ **THIS SEAT HAS NOW OVER-PRICED FIVE CONSECUTIVE STAGES, AND §6 SAID SO IN ADVANCE** ("`m_C` is an
assumption, not a measurement, and this seat has been wrong about exactly this four times"). Writing the
warning did not make the estimate better — the pessimistic corner was **8× the truth**. The honest lesson is
not "estimate lower"; it is that **`m_C` was never measured and a stage's cost multiplier cannot be reasoned
out from an adjacent stage.** The cheap fix existed and I did not take it: **one stage-C episode, run once,
would have priced the other eleven** — and at 138,912 tokens it would have cost 3 % of the run.

---

## §5 · WHAT THIS RESULT IS, AND THE THREE THINGS IT IS NOT

**IT IS:** a measurement that `claude-opus-5`, on the plain arm with no salt content, **certifies
implementation + correctness proof on 12 of 12** unflagged, C-live CLEVER problems — kernel-replayed,
statements byte-identical to frozen, axioms inside `{propext, Classical.choice, Quot.sound}` — at ~363k
tokens and ~4.7 min per problem; **and** that on the four cells where the reference oracle is provably
permissive, **not one pass exploited it**.

**IT IS NOT A RESULT ABOUT THE SALT METHOD.** No salt arm ran, and by §1's reachability argument none could
have registered a gain on this population. The campaign's standing sentence is unchanged: **nothing about the
salt method has been tested at stage C.**

**IT IS NOT COMPARABLE TO A STAGE-B NUMBER.** Stage B is the isomorphism task and reads 10/15 at this tier;
stage C is a different task with a different failure surface, and the 08/31 law stands — **class distributions
and rates are not naively comparable across stages any more than across tiers.**

**IT IS NOT A CEILING OF THE INSTRUMENT.** The checker refused nothing, screened nothing, and its integrity
block is empty; the twelve passes are passes by every gate the campaign owns. What is exhausted is **this
population**, not the method's measurability — which is precisely why §9.5's fallback is a different
substrate and not a larger `k`.

---

## §6 · BRANCHES DISCHARGED, AND WHAT FOLLOWS

- **STEP 2 (`a2` on the same 12): DOES NOT RUN.** `3 ≤ P0 ≤ 7` is false; `c ≤ 0`.
- **STEP 3 (`a1` placebo): CANNOT ARISE** — it is conditional on Step 2's `c − b ≥ 5`.
- **§9.5 AT THE CEILING: the fallback is NOT a larger `k`.** Per the Captain's standing word, the default-if-
  silent next act is the **S2-Rust READ-ONLY scout** (zero model tokens) — the commission's PRIMARY treatment
  substrate, on which there is still zero record.
- **ROW AW** (`a1` at Opus, the arm-independence question) — GO by ruling 15, after this read.
- **ROW AV's stage-A half** stays REGISTERED AND NOT APPLIED (§10): repairing the guarded-vs-total
  `generated_spec` defect would break comparability with 114 landed stage-A episodes for a stage this
  amendment does not authorise. *Spend comparability only when a run needs it.*
- **OWED, un-applied, named above:** the F3-headline repair at a stage-C-only root (§1's ⚠).

**LAWS THIS RUN ADDED.** A ceiling read at the maximum is not a threshold but an empty set — say `c ≤ 0`, not
"unlikely" · a prediction about the shape of failure is unscoreable in a run without failures, and scoring it
as held is hindsight · an instrument that reports a stage it was not asked to run states a floor it did not
measure · a stage's cost multiplier cannot be reasoned out from an adjacent stage, and one episode would have
measured it · a vacuous-region probe refutes and does not certify · the false-positive direction of a checker
is invisible unless the fixture drives it · a fence that protects a run can destroy one, and which it does
depends only on WHEN you touch it.
