# AMENDMENT 11 — S2-LEAN **STAGE C** ON U15 AT `claude-opus-5`, GATED ON THE PLAIN ARM

**DRAFT — NOT YET THE AUTHORIZATION.** Registered under desk row AS (the helm's commission, bus 09/01 08:53).
Seat `bench` · drafted 2026-09-01 · **freeze due 09/02** · the dated freeze commit is the authorization (F2), and
**no stage-C model call is made before it**, which is also the commission's stated objection window.
Amends the frozen `SCOUT-S2LEAN-STAGE0.md`; appended, never edited in.

*The commission is the question and the constraints; the pricing, the registration and the freeze are this
seat's. **Every number below is re-derived at the artifact**, and where the commission stated one I say whether
my measurement reproduced it. Two did (§6). One did not survive contact (§2).*

---

## §1 · THE QUESTION

Does the salt arm `a2` raise the rate at which a coding agent produces a **kernel-checked implementation and
correctness proof against a human specification** — S2-Lean stage C — relative to the plain arm `a0`?

**In front of every number in this amendment: `a2` is the salt method's SOLO-RENDERABLE CORE only.** A1/A2/A5/A6
and R5–R7 are unrenderable in a sealed single-agent episode, registered as such before the campaign's first
call. Multi-agent is DECLINED for this instrument by the commission. **Nothing here tests the Advisory tier.**

## §2 · THE POPULATION — **n = 12, NOT 13**

The commission fixes `U15 ∖ c_dead{54, 112} ⇒ n = 13`. That arithmetic is correct and the premise is not.

⛔ **`problem_18` CANNOT BE PASSED BY ANY ARM, AT ANY BUDGET, AND THAT IS A THEOREM.**
Step 0 (`TRIAGE-B-failures-2026-09-01.md` §4, saltbench `bf03f2d`) proves
`stageC_problem18_unsatisfiable : ¬ ∃ impl, (∀ s t, problem_spec impl s t) ∧ impl "aaaa" "aa" = 3`
with axioms `[propext, Classical.choice, Quot.sound]` — the allowlist exactly, no `sorry`, `rc 0`. In Lean
v4.27 `String.drop/take : String → Nat → String.Slice` and `Slice` equality is structural, so `problem_18`'s
occurrence test is FALSE at a genuine occurrence and the spec forces `0` where the frozen `#test` line demands
`3`. A failing `#test` is `rc 1` (measured). **Satisfy `correctness` ⇒ COMPILE. Pass the test ⇒ AXIOMS_FAIL.**
An episode there would be scored as the arm's failure and **would be indistinguishable in the record from a
failure of the method.**

**THE REGISTERED POPULATION IS THEREFORE:**

    problem_0  problem_4  problem_16  problem_31  problem_38  problem_73
    problem_74 problem_96 problem_127 problem_141 problem_142 problem_146      (n = 12)

**HOW IT IS ENFORCED, AND WHAT I GOT WRONG IN THE FIRST DRAFT OF THIS SECTION.** `view_status.json`'s
`c_dead` gains `18`, and `harness/HASHES.txt` re-pins. The driver then lands `NOT_RUN(view_dead)` for 18 of its
own accord (`run_s2_stage0.sh:126`), and the morning line moves it into its own class.

✅ **THE NO-OP PROOF IS RUN AND IT IS EXACT.** Both morning-line runs over `~/bench-a8/state` at `k=27`,
`ML_ARMS=a0,a2`, before and after the edit: **53 lines each; every stage-A and stage-B line byte-identical;
the only changes are `c_dead∩D` in the header and 18 moving from `not proven` to `NOT_RUN(view_dead)` in both
stage-C blocks.** Nothing else moves.

⛔ **BUT MY FIRST DRAFT CLAIMED THE EDIT MAKES THE DENOMINATOR 12 "WITHOUT ANYONE REMEMBERING TO MAKE IT 12",
AND THE PROOF REFUTED MY OWN SENTENCE.** The morning line's stage-C block is over the **C-eligible DRAWN
subset** — `D ∖ c_dead`, which is **23 → 22**, not 15 → 12. The registered population is the *unflagged*
subset, and **the instrument has an unflagged line for stage B only** (the F3 line prints
`unflagged drawn subset U (n=15) … 10/15 = 66.7 %`); **there is no such line for stage C.**

⚠️⚠️ **THAT IS A LIVE MISREADING SURFACE AND IT SITS DIRECTLY UNDER THIS AMENDMENT'S GATE.** After Step 1 the
instrument will print something like `stage C … a0 proven 9/22` **and the campaign's own 20–80 % band would
read 9/22 = 40.9 % as "RUN THE SALT ARM"** — while the registered gate at `9/12` says **CEILING HOLD**. The two
readings of one run point opposite ways, and the wrong one is the one that is printed.

**THE READING RULE, FIXED HERE, BEFORE THE DATA:**
- **`P0` IS A COUNT, NOT A RATE** — every threshold in §4 is a count — and it is the `proven` **count** in the
  stage-C `a0` block. **The printed denominator (22) is the C-eligible DRAWN subset and is NOT this gate's
  denominator.** The gate's denominator is the registered 12 and it is fixed by this amendment.
- **GUARD, so the count cannot silently include something else:** the run's landed stage-C rows must be
  **exactly the registered 12**, verified against the landings log before the gate is read. A row outside the
  12 voids the read until it is explained.
- The separation criterion is **unaffected**: the 10 drawn-but-never-run problems are not-proven for both arms,
  hence concordant, hence contribute 0 to `b` and 0 to `c`. **`|b − c|` over 22 equals `|b − c|` over 12.**
- **OWED, and listed in §12: a reading-instrument amendment adding the registered-population line to the
  stage-C block**, red-first with a proven no-op, the amendment-7 pattern. Until it lands the rule above
  governs. ⇒ *A printed rate whose denominator differs from the gate's is a green light waiting to happen* —
  the same family as the `ship BC` log and `c_dead` itself, found this time **before** it was read rather than
  after.

📌 **AND THE `c_dead` ENTRY IS AN EXTENSION OF THAT LIST'S MEANING, WHICH THIS AMENDMENT SAYS RATHER THAN
HIDES:** `c_dead` was minted as *"the C view does not elaborate"*; 18's C view elaborates perfectly. The list
now means **"the stage-C task cannot be completed"**, of which non-elaboration is one case and provable
unsatisfiability is another. The proof rides in the amendment; the entry rides in the file.

## §3 · THE PRE-FLIGHT — A NEW GATE, BECAUSE THE OLD ONE MEASURED THE WRONG THING

`c_dead` had `problem_18` marked `C: ok` because **`c_dead` is an ELABORATION check: it measures whether the
task can be STATED, never whether it can be DONE.** Fifth instance in a fortnight, at this seat alone, of *a
gate that reads a proxy for the thing instead of the thing.*

**REGISTERED: `harness/s2lean/c_oracle_preflight.py`**, pinned in `HASHES.txt`, run over the registered
population **before the first stage-C call**, its full report archived with the result.

- **CHECK 1 — SLICE-EQ (reaches every problem).** Elaborate the frozen `problem_spec` and inspect the
  **elaborated** term for a `String.Slice` coercion inside an equality. This is 18's exact root cause and it is
  **invisible in the source text**: `(string.drop i).take n = substring` typechecks only because Lean silently
  inserts `String.toSlice`. **The source reads as content equality and means structural equality.**
- **CHECK 2 — GT-vs-`#test` (reaches only problems whose CLEVER reference implementation is not `sorry`).**
  Run the frozen `#test` lines against the reference implementation. If the benchmark's own implementation
  fails the benchmark's own tests, the cell is incoherent before any arm touches it.
- **RED-FIRST, and the green control is not optional.** The gate must REFUSE `problem_18` (`rc 3`,
  `SLICE_EQ_RISK`, the offending line printed) **and must not refuse `problem_0`** — *without the green arm the
  red arm proves only that it refuses everything.* Both driven as subprocesses on the real argv, plus REFUSE
  arms for argument handling and an honesty arm (§below).
- ⚠️ **IT REFUTES; IT DOES NOT CERTIFY, AND THE REPORT SAYS SO IN THAT WORD.** A problem it does not refute is
  printed **UNREFUTED**, never "clean". The result publishes the UNREFUTED/UNREACHED split.

⛔ **THE PRE-FLIGHT I FIRST DESIGNED IS IMPOSSIBLE ON THIS SUBSTRATE, AND FINDING THAT OUT COST ONE `git clone`.**
The obvious gate is "run CLEVER's reference implementation and correctness proof through `check.py` as a
stage-C control", the shape `s2-controls.json` already uses for `problem_0`. **Measured at the artifact
(`clever-gt` at the pinned commit `8348039`): only 4 of 161 CLEVER problems carry a complete reference
`correctness` proof, and of this amendment's 12 exactly ONE does — `problem_0`.** Seven of the twelve have no
reference *implementation* either. ⇒ **STAGE C ASKS THE ARMS TO DO SOMETHING THE BENCHMARK'S OWN AUTHORS DID
NOT DO FOR 11 OF THE 12**, and no GT-based satisfiability gate can exist here.
📌 This discharges an item the source read named as owed and could not reach: *"(f) Verify locally (needs a
clone, forbidden here): exact non-sorry counts per HF column"* — its estimate of ~4 non-sorry
`correctness_proof` rows is now **measured at 4/161 exactly.**
✅ **DRIVEN, BEFORE THE FREEZE, AND THE RESULT IS RECORDED HERE RATHER THAN PROMISED.**
`c_oracle_preflight.py --selftest` ⇒ **9 arms, 0 failed** — four REFUSE arms on argument handling, the **red**
control (`problem_18` ⇒ `rc 3`, `SLICE_EQ_RISK`, the offending elaborated line printed), the **green** control
(`problem_0` ⇒ `rc 0`, not refused), a mixed call that must refuse one and clear the other in the same run, and
an honesty arm asserting the report never calls an unrefuted problem "clean". Every arm a subprocess on the
real argv.
`c_oracle_preflight.py 0 4 16 31 38 73 74 96 127 141 142 146` ⇒ **REFUSED: (none) — all 12 UNREFUTED**, CHECK 1
reaching all 12 (`no-slice-coercion` on every one) and CHECK 2 reaching **5 of 12** (`0, 4, 16, 31, 73`, all
`gt-passes-its-tests`) with 7 UNREACHED for want of a reference implementation.
⇒ **The registered population of 12 stands, and `problem_18` remains the only cell this instrument refuses.**
⚠️ Seven of the twelve are UNREACHED by CHECK 2 and that is printed, not smoothed: **UNREFUTED is the strongest
thing this gate can say, and on seven of the twelve it rests on CHECK 1 alone.**

🔒 **HERMETICITY:** the clone lives at `~/clever-gt` on the Studio — **outside `~/lean-shared/clever` and
outside every episode's working directory**, so the shared build the arms compile against stays GT-free. The
pre-flight is the CHECKER's compile, never an agent's. `~/lean-shared/clever` is unchanged and re-verifiable by
its three `leanproj-*` pins.

## §4 · THE GATE, RE-DERIVED AT n = 12

The commission's gate at n = 13: `P0 ≤ 2 ⇒ FLOOR HOLD` · `P0 ≥ 9 ⇒ CEILING HOLD` · `3 ≤ P0 ≤ 8 ⇒ STEP 2` ·
`STEP 3: a1 iff c − b ≥ 5`; separation `|b − c| ≥ 5`.

**The ceiling is not a percentage — it is a REACHABILITY argument, and that is what must be re-derived.** With
`b` = a0-only passes and `c` = a2-only passes (`s2_morning_line.py:211` prints `b` = FIRST-arm-only, so at
`ML_ARMS=a0,a2` `b` is a0-only — *picked here, before the data, per the amendment-9 law that a contingency
registered in two notations is two contingencies*):

    c ≤ n − P0   (a2 can only win where a0 lost)        b ≤ P0   (a2 can only lose where a0 won)
    a SALT-POSITIVE read (c − b ≥ 5) needs c ≥ 5  ⇒  P0 ≤ n − 5
    a PLAIN-POSITIVE read (b − c ≥ 5) needs b ≥ 5  ⇒  P0 ≥ 5

**AT n = 12 THE REGISTERED GATE IS** (`P0` = the proven COUNT over the registered 12, read per §2's rule):

| P0 (of 12) | branch |
|---|---|
| **0 – 2** | **FLOOR HOLD** — under the campaign's 20 % floor (2/12 = 16.7 %). A finding about the tier, not the method. |
| **3 – 7** | **STEP 2** — run `a2` on the same 12. |
| **8 – 12** | **CEILING HOLD** — `c ≤ 4 < 5`: a salt-positive read is **unreachable at ANY k on this population**. The bar is absolute, exactly as the commission wrote it. |

⛔ **THE WINDOW SHRANK, AND THAT IS A CONSEQUENCE OF THE DEAD CELL, NOT A CHOICE:** `3 ≤ P0 ≤ 8` (six values of
thirteen) becomes `3 ≤ P0 ≤ 7` (five of twelve). **Removing one unpassable problem narrowed the range in which
this experiment can run at all.**
📌 And a sharper consequence, worth stating because it was invisible at n = 13: **the commission's registered
expectation `P0 ∈ [9,12]` of 13 contained a cell that cannot pass**, so its true reachable maximum was 12, not
13. Re-expressed as a rate and applied to n = 12 it is `P0 ∈ [8,11]` — **which lies entirely inside the CEILING
HOLD region.** The helm said as much in the commission ("the likely product is a0's stage-C certification rate
and a HOLD"); the re-derivation makes it *more* likely, because the ceiling threshold falls 9 → 8 while the
expectation does not move. **This spend is bought with eyes open and the eyes are open wider than they were.**

## §5 · REGIME, ARMS, AND WHAT DOES NOT SHIP

- **Model** `claude-opus-5` (ruling O read tier-scoped; row c is the Captain's precedent for Opus on U15).
  **No Sonnet arm.** Fable absent from the driver's allowlist by construction.
- **Arms as pinned, unchanged:** `a0` = `base.md` alone · `a2` = base + `harness/arms/a2.md`
  (1,913 B, `0c37d7c8…`) · `a1` = `harness/s2lean/placebo.md`, only if §9 Step 3 fires.
- **Regime:** amendment-8's — `R_AMEND=100`, `TC_AMEND=20000000` (**deliberately non-binding**: every `a0` U15
  row before amendment 4 ran with the ceiling DEAD, so a binding ceiling now would be an instrument asymmetry
  favouring the control), `W_AMEND` as amendment 8 set it. **Own state root** (fresh, so nothing is skipped and
  no prior artifact is touched), with `smoke.log` and `s2-controls.json` copied in so both gates still apply.
- **NO STAGE A AND NO STAGE B.** Verified at the driver, not assumed: `run_s2_stage0.sh` requires
  `A.bodies.json` only for stage B (`:125`); stage C's sole precondition is the `c_dead` check (`:126`).
  Stage C reads the **human** `problem_spec` from the C view and is independent of both earlier stages.
- ⛔ **`ship BC` IS NOT RUN, AND AMENDMENT 10'S GATE MUST NOT BE POINTED AT THIS RUN.** `bc_gate.py` verifies
  **stage-A provenance** per cell (`a_passed`, `a_bodies_sha256` = the sha of that episode's own `bodies.json`).
  A stage-C run has no stage A, so that gate would **REFUSE 12/12 correctly and irrelevantly** — a red light
  wired to nothing, the exact mirror of the green one amendment 10 was built to remove. The C views are already
  on the host (`~/bench/s2views`, 161 frozen + 161 C; `~/bench-a8/s2views` is a symlink to it). **Verify the
  views BY CONTENT (set-hash) before the run; ship nothing.**
- **Pre-flight S1–S5 at the current sha**, and — the commission's own instruction — **verify
  `s2-controls.json` EXISTS on the Studio with C-control rows PRESENT, not `controls_pass: true` taken on
  faith.** (The scouts read a clone where the file was absent. A gate that reads a summary field is the defect
  this seat repaired in `ship BC` on 08/31.)

## §6 · BUDGET, RE-DERIVED AT THE ARTIFACT

Measured over the 30 Opus U15 stage-B manifests in `~/bench-a8` (`meter.json` per episode):

| | n | Σ tokens | mean | median | p90 | max | median calls |
|---|---|---|---|---|---|---|---|
| stage B `a0` | 15 | 9,160,733 | **610,716** | 399,454 | 966,017 | 2,859,925 | 15 |
| stage B `a2` | 15 | 10,930,115 | **728,674** | 474,390 | 1,875,609 | 3,164,300 | 17 |
| stage A `a0` | 15 | 1,722,313 | 114,821 | 99,779 | 152,470 | 302,924 | 7 |
| stage A `a2` | 15 | 4,229,985 | 281,999 | 283,629 | 366,028 | 736,854 | 13 |

✅ **The commission's "612k/730k per episode" REPRODUCES**: those are the means, and mine agree to under 1,000
tokens on both arms. Stated because a number inherited is not a number measured.

**Step 1 (`a0` × 12), on the commission's `m_C ∈ [1,3]`:** 7.3M · 14.7M · **22.0M** — the commission's 8–24M,
reproduced. **Two arms at the central multiplier ≈ 35M**, inside the commission's ≤ 52M.

⛔ **BUT `m_C` IS AN ASSUMPTION, NOT A MEASUREMENT, AND THIS SEAT HAS BEEN WRONG ABOUT EXACTLY THIS FOUR TIMES.**
Its own law: *a mean over a set selected for difficulty is not a population mean* · *a cost model built on a
weaker model's failures does not transfer up a tier* · *predict per item; a mean is the estimator of last
resort* · *a gate decided on a point estimate has assumed away its own largest unknown*. **Pessimistic corner
for Step 1: 12 × p90(966,017) × 3 ≈ 34.8M.**

**REGISTERED STOPS** — and a HALT that binds is a budget rule, which the protocol forbids, so each sits
**above** the pessimistic corner:
- **HALT 50M per arm-stage** (commission said 40M; my pessimistic corner is 34.8M and 40M leaves 15 % of head-
  room, which is not headroom — **I am raising it and saying why, rather than discovering it at 39M**).
- **HALT 12 h wall per arm-stage**, cooperative, via `$BENCH/HALT` checked **inside the arm loop**
  (amendment 8 addendum 1), with the enforcer in `tmux` **on the Studio** and armed **BEFORE the first
  episode** — never in the seat's session, which dies at exit.
- **Weekly ≤ 75 %**, **Sep 7 16:00 protected**, kriterion only, fleet QUIET at bench.
- **One quota reading at dispatch. Never a poll.** (Owed at dispatch, not now.)

## §7 · PREDICTIONS — REGISTERED BEFORE ANY STAGE-C CALL

Recorded so they can fail. Grounds named so a failure teaches something.

1. **`P0 ∈ [8, 11]` of 12, point estimate 9 ⇒ I PREDICT THE CEILING HOLD FIRES AND STEP 2 NEVER RUNS.**
   Grounds: the CLEVER leaderboard puts a Claude agent at ~65 % on Task 2 (impl+proof, 104/161) against ~42 %
   on Task 1 (spec isomorphism) — **stage C is the EASIER half on this benchmark** — and Opus `a0` already
   scored 10/15 = 67 % at stage B on this very population, which is unflagged and therefore the cleaner subset.
   Four of the twelve oracles are provably permissive (§8) which pushes it up further.
2. **The most common non-pass class is `AXIOMS_FAIL` with `sorryAx`**, as it has been in all 45 stage-B
   episodes of this campaign, and **`COMPILE` is materially more common at stage C than at stage B** — because
   stage C's canonical file contains the `#test` lines and a failing `#test` is `rc 1 = COMPILE`, a failure
   mode stage B structurally cannot have.
3. **Cost per episode exceeds stage B's**: median `a0` stage-C tokens > 399,454 (`m_C > 1`). I do **not**
   predict a value for `m_C`; I predict its sign, because that is what the evidence supports.
4. **Per item, not as a mean** (this seat's law, paid for four times): the passes will include
   `0, 4, 16, 31, 73` — the five with a real reference implementation and, for `0`, a complete reference proof
   — and the failures will concentrate in `141, 142, 146`, the recursive and String-library-heavy specs where
   Opus stage B burned 7,033–8,086 characters of lemmas and still ran out of rounds.

⚠️ **AND THE ALTERNATIVE EXPLANATION, REGISTERED BEFORE THE DATA SO IT CANNOT BE ADOPTED AFTER IT:** if the
CEILING fires, **"the tier is strong" and "the oracle is permissive" both predict it**, and the registered
result cannot distinguish them. §8 is the instrument that can.

## §8 · THE PERMISSIVE-ORACLE DIAGNOSTIC — REGISTERED BEFORE THE RUN, COSTS ZERO MODEL TOKENS

Step 0 measured that **four of the twelve reference specs are vacuous on a region their `#test` lines never
visit**: `problem_0` (silent for `numbers.length ≤ 1`) · `problem_4` (silent on `[]`) · `problem_96` (silent on
order and multiplicity) · `problem_127` (vacuous on ill-formed intervals). A stage-C episode can therefore
**certify an implementation that is wrong there**, and it will be scored PASS, correctly, by a checker doing
exactly its job.

**REGISTERED MEASUREMENT, over the landed artifacts after the run, never fed back:** for each stage-C PASS on
those four, evaluate the certified `implementation` on a **pre-declared probe point inside the vacuous region**
— `problem_0`: `[]` and `[x]` · `problem_4`: `[]` · `problem_96`: is `impl 7` strictly increasing and
duplicate-free · `problem_127`: `impl (5,0) (0,10)` ∈ {"YES","NO"} — and report `f_vac` = the fraction of those
passes that are wrong at their probe point. **The probe points are fixed here, before the run.**

⇒ This converts *"P0 was high"* into *"P0 was high **and** k of the passes exploit oracle permissiveness"*, and
it is the only thing in this amendment that can tell a tier reading from an instrument reading. It does not
change `P0`, the record, or the gate: **it is reported BESIDE the number, never against it.**

## §9 · THE BRANCHES — PRE-REGISTERED, AND THE DRIVER DOES NOT ENFORCE THEM

1. **STEP 1** — `a0` stage C over the 12 ⇒ `P0`.
2. **THE GATE READ** — §4's table, read once, with `ML_ARMS=a0`.
3. **STEP 2**, iff `3 ≤ P0 ≤ 7` — `a2` on the same 12, same regime, `ML_ARMS=a0,a2`.
4. **STEP 3**, iff `c − b ≥ 5` — `a1` (placebo) on the same 12, to test whether a salt gain survives an
   equal-length inert prompt. **Note the direction, fixed here: `c` is a2-only. The registered trigger is a
   SALT WIN, and amendment 9 established that its predecessor's `b − c ≥ 2` could not fire at all.**
5. **AT THE CEILING the fallback is NOT a larger k** — it is a sitting word (Sonnet stage C under a re-read
   ruling O, or the Captain-ruled PRIMARY substrate S2-Rust, on which there is still zero record and which
   needs a scout before any word).

## §10 · GOVERNANCE

- **Row AV** — the `native_decide` out-of-bounds sentence goes in **`prompt_C.md` only**, and it is owed
  *before* Step 1 because stage C is where an implementation would reach for it. Step 0 sharpens the case: the
  campaign's only `KERNEL_REJECTED` came from `native_decide` in a helper the cone-scoped axiom audit never
  audits. **Its stage-A sibling is not yet a row and should be:** four of eight failing problems failed stage B
  because the reference spec GUARDS its conclusion while `generated_spec`, as `prompt_A.md` asks for it, is
  TOTAL — **a guarded spec and a total spec are never isomorphic, and stage B asks for an isomorphism.**
- **Row AW** — after the gate read.
- **Ruling O** read tier-scoped. No Sonnet arm. Fable design phase permitted and priced; a refuter beside.
- **Commit hygiene:** no `Claude-Session:` trailers (this repo is destined public). `Co-Authored-By` fine.

## §11 · WHAT THIS AMENDMENT DOES NOT TEST

Multi-agent (A1/A2/A5/A6, R5–R7) — DECLINED for this instrument by the commission: registered unrenderable,
forbidden by the frozen fence (`episode_s2.sh:161`, voids the episode `:306`), three unverified premises, an
unmeasured 2–5× multiplier, and **no organisation arm reaches `|b − c| ≥ 5` with `a0` near the ceiling.** The
Advisory tier remains untested by this campaign, as it has been by every read so far.

## §12 · THE FREEZE — WHAT MUST BE TRUE BEFORE THE DATED COMMIT

- [x] `c_oracle_preflight.py` selftest GREEN — **9 arms, 0 failed** (§3) · [ ] pinned in `HASHES.txt`
- [x] the pre-flight driven over all 12, report archived, **UNREFUTED for all 12** (§3)
- [x] the §2 no-op proof run and archived (53 lines each; A and B byte-identical) · [ ] `view_status.json` `c_dead` += 18 — **lands WITH the freeze, not before it: the edit is what this amendment authorises**
- [ ] `prompt_C.md` carries the row-AV sentence
- [ ] S1–S5 pre-flight green at the current sha; `s2-controls.json` present on the Studio **with C-control rows
      read, not `controls_pass` believed**
- [ ] the C views verified on the host BY SET-HASH; nothing shipped
- [ ] the HALT enforcer written and armed on the Studio **before** the first episode
- [ ] the reading-instrument amendment of §2 (a registered-population line in the stage-C block), or the §2 reading rule carried explicitly into the result
- [ ] `HASHES.txt` regenerated and reproducing; freeze commit made; **only then** the first model call
