# AMENDMENT 13 — ROW AW: `a1` (PLACEBO) AT `claude-opus-5`, STAGE A+B ON U15
## THE ARM-INDEPENDENCE QUESTION. Dated 2026-09-01. **THE COMMIT THAT FREEZES THIS FILE IS THE AUTHORIZATION.**

**Commission:** desk row AW, GO'd by the Captain at the helm 2026-09-01 14:1x ("AW (a1@Opus as the
arm-independence question, GO by ruling 15) after the gate read … AW runs in every branch after the gate
read (≈13M, kriterion)"). The gate read landed at 22:09Z (`P0 = 12/12`, CEILING HOLD, saltbench `2219c23`).
**No `a1`-at-Opus model call has been made. This amendment is written before the first one.**

---

## §1 · THE QUESTION, AND WHY IT IS NOT THE QUESTION `a2` ASKED

Amendment 8 measured a **tier raise** on U15 stage B: `a0` **8/15 → 10/15** and `a2` **8/15 → 10/15**, and
read the NULL between them (`|b − c| = 0`). The campaign's only measured movement to date is therefore
**+2 on both arms, attributable to the TIER**.

**AW asks a question neither arm could answer: is that +2 ARM-INDEPENDENT?**

`a1` is the **PLACEBO** — an equal-length generic process prompt with no salt content
(`harness/s2lean/placebo.md`, 1,746 B against `a2.md`'s 1,913 B; `base.md` is 627 B and common to all).
If `a1` also moves 8 → 10, the +2 is a property of the model tier that **no prompt content produced**, and
the null between `a0` and `a2` is strengthened: *the instrument moves with the tier and not with the arm.*
If `a1` does **not** move, then something about the prompt pair interacts with the tier, and the `a0`/`a2`
comparison at Opus rests on a floor that is not flat.

⛔ **WHAT THIS DOES NOT TEST, SAID FIRST:** this is not a test of the salt method. `a2` is the salt arm and it
already read the null. AW measures the **placebo's** tier response, which is a property of the INSTRUMENT.

---

## §2 · THE BASELINES — MEASURED AT THE ARTIFACT, NOT QUOTED FROM A BANK

Re-derived 2026-09-01 22:2x from the manifests + `check.json` in both state roots, latest-by-`end_utc` per
cell, `models` read per episode (never a banner):

| root | arm | model | U15 proven | the proven set |
|---|---|---|---|---|
| `~/bench` | `a0` | `claude-sonnet-5` | **8/15** | `{4, 16, 31, 38, 54, 74, 142, 146}` |
| `~/bench` | `a1` | `claude-sonnet-5` | **8/15** | `{16, 31, 38, 54, 73, 74, 142, 146}` |
| `~/bench` | `a2` | `claude-sonnet-5` | **8/15** | `{4, 16, 31, 38, 54, 74, 142, 146}` |
| `~/bench-a8` | `a0` | `claude-opus-5` | **10/15** | `{16, 31, 38, 54, 73, 74, 112, 141, 142, 146}` |
| `~/bench-a8` | `a2` | `claude-opus-5` | **10/15** | `{4, 16, 31, 38, 54, 73, 74, 141, 142, 146}` |

**U15** = `[73, 0, 146, 16, 4, 38, 142, 96, 112, 141, 31, 54, 127, 18, 74]` (the unflagged drawn subset, n=15).

📌 **THREE FACTS THE SETS SHOW AND THE RATES HIDE, all of which shape §4's predictions:**
1. **The Opus COMMON CORE is `{16, 31, 38, 54, 73, 74, 141, 142, 146}` (9 problems)** — proven by both content
   arms at the tier. `a0`-only = `{112}`, `a2`-only = `{4}`.
2. **`a1` AT SONNET ALREADY PROVED `73`**, which `a0` and `a2` reached only at Opus. The placebo is not a
   uniformly weaker arm; it is a *differently* placed one, and at n=15 that is one problem, not a finding.
3. **THE TIER RAISE IS NOT MONOTONE PER PROBLEM** — `a0` GAINED `{73, 112, 141}` and **LOST `{4}`**
   (amendment 8's own unpredicted result). Any prediction that assumes `a1` only gains is assuming away a
   measured behaviour of this instrument.

---

## §3 · THE CRITERION — REGISTERED HERE, BEFORE THE DATA, IN ONE NOTATION

*(Amendment 9's law: a contingency registered in two notations is two contingencies until someone picks one,
and the moment to pick is before the data.)*

Let **`P1`** = `a1` proven count over U15 at `claude-opus-5`. `a1`'s Sonnet baseline is **8**, so the tier
delta is **`Δ1 = P1 − 8`**. Both content arms measured **`Δ = +2`**.

| `P1` (of 15) | `Δ1` | reading |
|---|---|---|
| **9 – 11** | +1 … +3 | **ARM-INDEPENDENT** — `a1`'s tier response is within ±1 of the +2 both content arms showed. The +2 is a property of the TIER. |
| **≤ 8** | ≤ 0 | **ARM-DEPENDENT (placebo does not rise)** — the content arms' floor is not flat, and the `a0`/`a2` null at Opus needs re-reading. |
| **≥ 12** | ≥ +4 | **ARM-DEPENDENT (placebo rises MORE)** — the inert prompt would out-gain both content arms; that would be a finding about the prompts, not the tier. |

**Pairwise, on the campaign's standing rule and no other:** `b` = `a0`-only, `c` = `a1`-only, over U15 at
Opus, both arms at the tier. **`|b − c| ≥ 5` = a separation; anything less is INDISTINGUISHABLE.** Reported as
counts. **No p-value, by design.** n = 15, one arm, one run.

⛔ **THE BAND IS THREE-WAY AND EXHAUSTIVE ON PURPOSE** (*enumerate the whole outcome space or claim none*).
There is no outcome of this run that lacks a registered reading.

---

## §4 · PREDICTIONS — PER ITEM, NOT AS A MEAN

*(This seat's law, paid for five times: when the items are paired and the control is already measured,
predict PER ITEM — a mean is the estimator of last resort, not of first.)*

1. **`P1 = 10`, interval `[9, 11]` ⇒ I PREDICT ARM-INDEPENDENT.** Ground: the tier moved both content arms by
   exactly +2 with a 9-problem common core, and the placebo shares `base.md` with both.
   📌 **The interval is registered to CONTAIN ITS OWN EXTREMES this time.** Amendment 11's `[8,11]` excluded
   the reachable maximum 12 and the outcome landed there. `[9,11]` is the arm-independent band by
   construction; the failure modes are `≤8` and `≥12` and both are named above.
2. **PER ITEM: `a1`'s Opus set ⊇ the 9-problem common core, and its gain over its own Sonnet set is `{141}`.**
   Ground: `141` is the one problem BOTH content arms gained at the tier, and `a1` already holds `73`.
3. **AT LEAST ONE NON-MONOTONE CELL IS LIVE: I do NOT predict `a1` loses nothing.** `a0` lost `{4}` at the
   tier and `a1` does not hold `4` to begin with; the exposed cells are `{16, 31, 38, 54, 73, 74, 142, 146}`.
   I predict **0 or 1 losses**, and I register that a loss is expected behaviour of this instrument, not an
   anomaly to be explained away.
4. **`0`, `96`, `112`, `127`, `18` REMAIN UNPROVEN BY `a1`.** `18` is provably unpassable at stage C but its
   stage-B cell is live and has never been proven by any arm at any tier; `0`, `96`, `127` have never been
   proven by any arm at stage B.
5. **COST: stage A ≈ 4M (the `a2` stage-A figure, since `placebo.md` and `a2.md` are within 10 % on length),
   stage B ≈ 11M, TOTAL ≈ 15M.** ⛔ **AND I REGISTER THAT THIS SEAT HAS NOW OVER-ESTIMATED FIVE CONSECUTIVE
   STAGES**, the last by 3.4×. **I therefore predict the ACTUAL comes in UNDER 15M**, and I say so before the
   run rather than discovering it again afterwards.

---

## §5 · REGIME — MATCHED TO `~/bench-a8` EXACTLY, BECAUSE COMPARABILITY IS THE WHOLE POINT

| knob | value | why |
|---|---|---|
| `M_AMEND` | `claude-opus-5` | the tier under test |
| `R_AMEND` | `100` | as `a0`/`a2` ran |
| `TC_AMEND` | **`30000000`** | ⛔ **the a8 value, NOT amendment 11's 20M.** Both are non-binding (max observed stage-B episode 3,165,325), but a comparison arm must carry the CONTROL's ceiling. *An instrument asymmetry that does not bind today binds the day the distribution moves.* |
| `W_AMEND` | `10800` | as `a0`/`a2` ran |
| `ARMS` | `a1` | `a0` and `a2` at Opus are already landed in `~/bench-a8` and are NOT re-run |
| stages | **A then B** | stage B REQUIRES a scored stage-A pass in its own root (`run_s2_stage0.sh:125`). ⛔ Reusing the SONNET `a1` stage-A bodies would confound the tier — the a8 run ran its own stage A at Opus for both content arms, and comparability demands `a1` do the same. |
| population | U15 via `ONLY_IDS`, `k=27` | the seeded draw still chooses; the operator only narrows |

## §6 · THE ROOT — AND THE STAGE-A FENCE THAT MAKES IT NON-TRIVIAL

⛔ **STAGE A REFUSES IF ANY `frozen.json` OR `C.lean` EXISTS UNDER `$BENCH` *OR* `$VIEWS`**
(`episode_s2.sh:85-90`), and it separately refuses a `.pristine-cache` holding a B/C `canonical.lean`.
`~/bench/s2views` **HOLDS GROUND TRUTH** (322 GT files) and every existing root symlinks to it.
⛔ **`stage_views.sh ship A` STILL HANGS** (undiagnosed since 08/30; its `--delete --delete-excluded` rsync
sits at 0 % CPU on both ends, reproducibly, while every other rsync on the same link is clean).

**THE CURE IS THE ONE THE BANK PRESCRIBES, AND IT IS NOT THE TOOL:** build `~/bench-aw/s2views` **by hand** as
an A-VIEWS-ONLY tree (`A.lean` + `frozenA.json` per problem, an EMPTY `.pristine-cache`), and
**VERIFY IT BY CONTENT SET-HASH** against the seat's known A-views figure **`bc4d6eafc0430ed2`** before the
first episode. *The receipt is the content, never the exit code of the thing that moved it.*
After stage A completes, `frozen.json` (stage B's requirement) is added to that same tree **by hand**, again
set-hash verified, and stage B runs. **`ship BC`'s `bc_gate.py` IS pointed at this run and MUST pass** — this
run has a real stage A, which is exactly the provenance that gate verifies (unlike amendment 11's stage C,
where it would have refused correctly and irrelevantly).

**Both gates still apply:** `smoke.log` inherited (pinned to `episode_s2.sh=cfb8a714…`) and the **fresh**
`s2-controls.json`, verified by `controls_gate.py` **against the live checker shas**, per stage.

## §7 · BUDGET AND THE REGISTERED STOPS

Pessimistic corner, stage B: `15 × p90(a2@Opus, 1,876,634) ≈ 28.1M`. Stage A corner: `15 × 366,028 ≈ 5.5M`.
Each HALT sits **above** its corner, because a HALT that binds is a budget rule and the protocol forbids one:

- **HALT 35M per arm-stage** (`halt_watch.sh $BENCH <STAGE> a1 35000000 12`), armed in `tmux` **on the
  Studio, BEFORE the first episode of EACH stage** — never in the seat's session, which dies at exit.
- **HALT 12 h wall per arm-stage**, cooperative via `$BENCH/HALT` read inside the driver's arm loop.
- **Weekly ≤ 75 %**, **Sep 7 16:00 protected**, kriterion only.
- **One quota reading at THIS dispatch. Never a poll.**

## §8 · WHAT THIS AMENDMENT CANNOT SAY

n = 15, **one** arm, **one** run, no repetition, **no p-value**. A three-way band on a single count is a
coarse instrument and is stated as one. It cannot separate "the placebo prompt is inert" from "the placebo
prompt helps exactly as much as the salt prompt does" — **both predict ARM-INDEPENDENT**, and distinguishing
them is not on this instrument at any n it can afford. It says nothing about stage C (read at the ceiling on
a different population) and nothing about the salt method, which `a2` already answered as the null.
