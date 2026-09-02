# RESULT — AMENDMENT 15, THE GROUND-TRUTH PASS OVER THE WHOLE POPULATION

**2026-09-01 22:16 PDT, seat `bench`. Zero model tokens.** The three-way ground-truth pass of amendment 15 §4
(b′) / addendum 1 §A3, run over **all 207 built views**, at the registered pin
`release/0.2025.09.12.bb1f342`, `--crate-type=lib --rlimit 250 --smt-option smt.random_seed=0`.
Wall **16.8 min**, 2–3 referee invocations per task. Record: `harness/s2rust/state/task_dead.json`.

## THE TALLY

| verdict | n | share of 207 |
|---|---|---|
| **LIVE — drawable** | **180** | 87.0 % |
| `TASK_CONTEXT_INCOMPLETE` | 27 | 13.0 % |
| `TASK_DEAD` | **0** | — |
| `PIN_DEFECT` (reference `COMPILE`) | **0** | — |
| `SCAFFOLD_DEFECT` (ours) | **0** | — |

## THE THREE BLOCKING GATES, ALL DISCHARGED AT THE WHOLE POPULATION

1. ⭐⭐ **`PIN_DEFECT` = 0 over 207.** §8.4's blocking gate required the reference `COMPILE` count to reach
   zero under the benchmark's pinned Verus. It does — **not on a sample, on every task.** ⇒ **the
   `task_dead` rate the morning's binary reported (33 %, 6.6× §3.5's own fallback threshold) was 100 % PIN
   DEFECT and 0 % benchmark.** Had §3.5's "today's release" stood, this wave would have pre-registered
   roughly a third of its population as dead proofs and attributed our toolchain error to the benchmark.
2. ⭐⭐ **`TASK_DEAD` = 0 over 207.** **Every reference proof in the population verifies.** There is no dead
   task on this substrate at the pinned toolchain — a cleaner starting position than S2-Lean ever had, and it
   is the first time this campaign has been able to say a `c_dead` analogue is EMPTY rather than small.
3. ⭐⭐ **`SCAFFOLD_DEFECT` = 0 over the 180.** For every task whose reference body can be compiled at all,
   **our assembled canonical verifies exactly where the benchmark's own file does.** The scaffold —
   `rustspan` + `build_views_verus` + the two-region assembler — is exonerated on the whole population, not
   by argument and not by the byte-exact pristine self-test alone, but by the referee.

## `TASK_CONTEXT_INCOMPLETE` — 27, AND THEY ARE ALL IN ONE PROJECT

All **27 are `NR`; `AC` contributes ZERO.** The failures are name-resolution errors — 22 plain `error:`
(mostly `cannot find macro …`), 3 `E0425` (function), 1 `E0433` (type path), 1 `E0412` (type) — i.e. the
record's `task` omits definitions its own `ground_truth` supplies. **Unsolvable by any agent**, removed from
the draw, pre-registered by id.
📌 The concentration in one project is itself evidence the class is real and not our parser: a scaffold bug
would not respect a project boundary.

## THE POPULATION, ACCOUNTED IN FULL

| class | n |
|---|---|
| **LIVE — the wave's drawable population** | **180** |
| `TASK_CONTEXT_INCOMPLETE` (the benchmark's record) | 27 |
| `TARGET_ABSENT` (target is not a proof-fn declaration) | 24 |
| `SHAPE` (stripped body carries content) | 17 |
| `EXEC_TARGET` | 15 |
| `TARGET_AMBIGUOUS` | 4 |
| **total = `AC ∪ NR`** | **267** |

**n = 180 is comfortably above the ~80-paired-problem floor §2 requires**, so the wave is viable at the
population the design actually admits. ⚠️ And it is 180 rather than **31**: DD §3.2's `UNFAITHFUL` clause
(b), had it stood, would have refused 176 of 207 and left a draw below the floor (addendum 1 §A3).

## TIMING — the pricing input §8(v) was missing

Per-task wall for a LIVE verdict (**two** referee runs, so roughly halve for one): **min 0.3 s · median
1.1 s · mean 5.3 s · p90 10.5 s · max 358.6 s.** The spread is three orders of magnitude and the tail is
long — one task takes ~6 min for two runs. ⇒ `WALL_S`, `MAX_TURNS` and the **4 × p90 token stop** must be
priced from the stage-0 controls' own metered distribution on THIS substrate; amendment 11 §6's numbers do
not transfer and neither does the paper's 11.6 min/task anchor (Sonnet 4.5, hands-off, whole tasks).

## WHAT THIS RESULT DOES NOT SAY

It says nothing about how often an AGENT will pass — no model has been called on this substrate and none will
be before stage 0's remaining receipts. It says the **instrument** is sound at the population: the referee is
pinned, the reference proofs all verify, our assembler changes no verdict, and the tasks that cannot be
solved are named and removed before any arm sees them.

**LAW THIS RESULT ADDS.** A dead-task list produced under the wrong toolchain is not a small error in a
number — it is a *different list*, and it removes real tasks while leaving the broken binary in place.
Measure `task_dead` only after the pin is gated, never alongside it.

---

## APPENDED 23:0x — THE RLIMIT CURVE AND THE DETERMINISM CONTROL (§8.5), BOTH DISCHARGED

**900 referee invocations, 40.6 min, over the 180 LIVE tasks' reference bodies THROUGH OUR SCAFFOLD**, at the
registered pin, seed 0. Record: `harness/s2rust/state/rlimit_curve.json`.

| `--rlimit` | PASS | climb |
|---|---|---|
| 10 | 179 / 180 | — |
| 50 | **180 / 180** | +1 |
| **250** (registered) | **180 / 180** | **+0** |

✅ **PIN VERDICT: NOT INDICTED. The curve is FLAT into R = 250 (+0).** The protocol's indictment condition —
*the pin is indicted if the PASS curve is still climbing at 250* — does not fire. The single task that needs
more than R = 10 returns `RLIMIT` there and passes at 50, and nothing anywhere needs more than 50.

✅ **DETERMINISM: 0 flips over 3 repeats at R = 250** (§11.3's control; a nonzero count would have indicted
the *pin*, not the solver, and blocked). The referee is reproducible at the pinned rlimit and seed.

📌 **WHAT THE CURVE DOES AND DOES NOT LICENCE, said precisely.** It measures the budget against the
**reference** proofs, and they are cheap: 179 of 180 fit in the CLI default. It therefore establishes that
**R = 250 is not too LOW** — no reference proof is failing for want of budget, so no failure under it can be
blamed on the ceiling. It does **not** establish that 250 is enough for an *agent's* proof, which may be far
more expensive than a human's: that headroom is exactly what 250 buys over veval.py's own choice, and the
`RLIMIT` class exists — kept separate from `VERIFY_FAIL`, never charged to the arm — precisely because the
curve cannot answer that question in advance.
⇒ 🔑 ***A BUDGET VALIDATED ON THE REFERENCE SOLUTION IS VALIDATED AGAINST THE CHEAPEST PROOF ANYONE WILL EVER
WRITE FOR THAT TASK. It bounds the budget from below and says nothing from above.***

📌 It also settles the `R = 10` vs `R = 250` dispute at the object: DD ⟦R U1⟧ corrected the draft's claim that
"10 is the published regime" (10 is the CLI default; `veval.py` passes 250). **Measured, both work for the
reference proofs** — 179/180 at 10, 180/180 at 50 — so the refuter's correction stands on provenance, and
the practical gap between the two values on ground truths is **one task**.
