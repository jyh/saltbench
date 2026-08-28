# SaltBench Wave 1 — PRE-REGISTRATION (v2)

**Re-frozen 2026-08-27 21:1x, still BEFORE any model call.** v1 (`saltbench 2ef7505`) was
amended after a 6/6 REPAIR-THEN-FIRE refuter pass; amending before the first API request is
what this document's own rule permits, and what it forbids afterwards. Once the first
request of any arm is sent, nothing above the line at the bottom may be revised.

Owner: silicon seat. Governing: council minute 2026-08-27 (`72928e04` + `93130077`) and
the promotion charter `seat/briefs/2026-08-20-saltbench-promotion.md`.
Verdicts: `seat fleet/REFUTER-saltbench-wave1-gate-2026-08-27.md`.

---

## 0 · Status, lane, and what the refuter pass changed

⛔ **PRIVATE.** Nothing publishes until the IARC ruling lands and the Captain says go.
Zero git remotes by construction. Personal lane; no employer-lane code, ever; touches no
tape-out resource and never takes a P1 build ticket.

**v1's four fatal classes, all of which I would have defended:**
1. **n = 50 was unreachable.** The cap starved the draw and the code truncated in silence
   — reproduced at this hand: `measured=42, pilot=0`, raising nothing. §3.
2. **The predicate was a no-op on the real encoding** (JSON strings; `len("[]") == 2`), so
   the criterion guaranteeing a regression surface admitted the 11 instances lacking one.
3. **§3.4's regression rule refused CORRECT patches** on ≥9.5% of the drawn set — a
   mechanical bias against my own treatment arm. I asked refuters for a cheaper
   explanation of a *win* and never asked for one of a *loss*. Rewritten in DESIGN §3.
4. **§6 had no adverse outcome.** Every terminal state read favourable. §6 below.

---

## 1 · The claim, and what it may NOT be quoted for

**Claim:** an agent whose patches must pass a gate solves more tasks correctly than the
same agent without the gate, **at equal enforced token spend**, on the population defined
in §3.

### ⛔ What wave 1 cannot show

- **Not machine-checked proof.** The kernel is not in this loop. Any later write-up citing
  wave 1 for a proof claim is misusing it.
- **The estimand is CONDITIONAL ON THE §3 PREDICATE.** Wave 1 measures the gate's effect
  on tasks with a 1–3-file gold patch, a non-empty regression suite, a ≥500-character
  statement, and ≤9 per repo. **It does not estimate the effect on SWE-bench Verified as a
  whole, and no write-up may state §1's claim without that qualifier.**
- **Contamination is unmeasurable here and cuts toward zero.** Verified has been public
  since 2024 and the model under test may have seen it. On a memorized task the first
  patch is already correct, so the gate can only subtract — every refusal there is an
  incorrect refusal. **Wave 1 cannot separate a contamination-attenuated effect from a
  capability floor**, and §6 no longer pretends otherwise.
- **This is a SCREEN.** At n = 50 pairs, exact McNemar, a **+10-point** effect is detected
  with power **0.14–0.29** depending on discordance (verified at this hand, §5). Wave 1 is
  powered for a large effect and blind to a modest one.

---

## 2 · Substrate — my call, and deliberately adverse

**SWE-bench Verified**, subset per §3, pinned in §3.

The alternative was our own kernel-scorable corpus, which plays to the method's strength —
**which is why it loses.** The sharp question this demo must survive is *"you built the
benchmark to win"*, and the strongest answer is a substrate **we did not design, whose
scoring we do not control, and where our best feature is unavailable.** Adverse on three
axes. If the gate still helps, that is believable in a way a home-corpus win never is.

⚠️ *The honest tension: SaltBench's own tech report argues hidden-test suites sample
properties where proofs state them. That is an argument about what makes a good benchmark.
We are borrowing a neutral one to test a mechanism, not proposing it as a yardstick.*

---

## 3 · Task selection — frozen, and now actually reachable

**`select_tasks.py` in this repo is the NORMATIVE implementation of this section.** Where
prose and code could differ, the code is definitive and this sentence is what makes that
true. *v1 claimed the list was re-derivable "from the public dataset plus this page" and
never named the script — the page alone did not determine the list.*

**Pinned snapshot:** `princeton-nlp/SWE-bench_Verified`, split `test`, 500 rows.

**Criteria, metadata only** (no task inspected, no solution read, no arm run before the
list was frozen). Applied over the 500 rows, **measured**:

| # | criterion | rejects |
|---|---|---|
| 1 | `len(FAIL_TO_PASS) ≥ 1` — a solvable signal exists | 0 |
| 2 | `len(PASS_TO_PASS) ≥ 1` — a regression signal exists | **11** |
| 3 | gold patch touches 1–3 files (file list only; content unread) | 9 |
| 4 | problem statement ≥ 500 chars | 78 |
| 5 | **≤ 9 tasks per source repository** — applied during the draw | *binding* |

⛔ **v1 called criterion 2 "the discriminating one". It is not** — it removes 2.2%. The
criteria that actually shape the population are 4 (the length floor) and **5, the cap,
which v1 introduced almost in passing and which is the one that broke the design.**

**The algorithm, stated explicitly because v1's prose was unimplementable** (criterion 5
has no per-item form, and no tie-break was given for which N of a repo survive):

1. filter by criteria 1–4;
2. sort by `sha256(instance_id + SEED)`;
3. walk that order, admitting while the repo's count `< 9`;
4. **RAISE if fewer than 80 admitted** — never truncate;
5. partition into **measured-50 / pilot-30 by largest-remainder apportionment within each
   repo**, so the pilot mirrors the measured set's repo mix.

```
SEED         = saltbench-wave1-2026-08-27      (unchanged from v1)
N_MEASURED   = 50        N_PILOT = 30          (pilot raised from 10, §4)
MAX_PER_REPO = 9                               (raised from 4)
```

**Why 9, from measured arithmetic rather than preference.** Ceiling
`Σ min(eligible_r, cap)` over the 11 eligible repos: `4→42 · 5→52 · 6→62 · 8→78 · 9→86`.
We need 80. **Cap 8 starves.** ⛔ **The cap materially re-weights the substrate — django is
46% of the raw split and 12% of the measured set — so the wave-1 solve rate is NOT
comparable to any published SWE-bench figure.** (§4 already forbids quoting one.)

⛔ **Step 5 replaces a tail-take.** v1 took offsets 50–59 of the capped walk; because the
cap is spent in hash order the big repos fill early, so the tail was composed entirely of
the smallest codebases — a pilot sharing near-zero composition with the set it calibrates,
a bias surviving n → ∞.

**The frozen list is committed as `TASKLIST.json`**, discharging v1's promise that it be
frozen before any arm runs.

**Exclusions** are arm-independent by construction and logged in `EXCLUSIONS.md`, created
with its header before the run. An instance is excluded **iff** (i) the **pre-flight** —
empty patch at base — fails to produce all-F2P-fail and all-P2P-pass, or (ii) the
**gold-control** — gold patch in the same image — fails to resolve. Both are computed
before either arm runs and cannot depend on arm outcomes. ⛔ **Any per-arm run failure not
reproduced by an arm-independent control scores UNSOLVED for that arm; it is never an
exclusion.** *v1's trigger was "fails in both arms" with an action clause reading
universally — and one-arm failures ARE the discordant pairs, which carry 100% of the
McNemar information.* Excluded pairs are **not refilled**; `n_effective` and the exclusion
count appear in the headline.

---

## 4 · Model — one mid tier, band MEASURED, pilot on BOTH arms

**Candidate: `claude-sonnet-5`** ($2/MTok in, $10/MTok out).

⛔ **No baseline percentage is asserted.** The band is a property of
`model × substrate × harness`; a leaderboard figure came from a different scaffold.

**Pilot: the 30 tasks of §3, run on BOTH arms** (30 pairs, not 30 control tasks).

- Routes the tier if the control-arm rate lands in **40–60%**.
- **Measures discordance**, the sole input to power — so the §5 MDE is published from
  measurement rather than guessed. ⛔ Pilot discordance feeds **only** the published MDE,
  never `n`, the band, or the tier.
- ⚠️ **The band decision is a ROUTING HEURISTIC, not evidence about the model's baseline**,
  and is reported with its exact 95% CI. At n=10 (v1) a dead-centre model mis-routed
  **34.4%** of the time; at n=30 that falls to ~10%.
- **A pilot above 60% triggers the contamination check (§5) BEFORE any tier step-down**,
  so a memorized ceiling is not misread as a capability ceiling.
- At most **two** re-pilots; then *"no affordable model sits in the measurable band"* is
  reported as a result — with the CI, so a reader can see it is a routing outcome.

**Pinned identically for both arms, before the first call:** model id and snapshot,
`output_config.effort`, `thinking` mode and display, `max_tokens`, caching configuration
and TTL, and temperature. *An unpinned effort setting is a larger lever on the dollar
figure than the gate is.*

---

## 5 · Design, statistic, and what is always reported

**Paired, within-task.** All arms attempt the identical list; `P₁` is generated once and
shared (DESIGN §7). The unit is the **pair**.

- **Primary ESTIMAND:** the paired difference in solve rate over all attempted tasks
  (`solved` as defined in DESIGN §2; no accepted proposal ⇒ unsolved).
- **Primary TEST:** the **exact conditional binomial McNemar test, equal-tailed two-sided
  doubling, α = 0.05. No χ² approximation, corrected or otherwise, at any n_d.**
  *Verified at this hand: the three common variants disagree in nine cells for
  6 ≤ n_d ≤ 25 — e.g. n_d=8 at 7:1 is exact p=0.0703 (NS) and uncorrected χ² p=0.0339
  (SIG). Naming the variant after seeing the split is a live researcher degree of freedom.*
- **Both are reported in the headline, estimate first**, with `b`, `c`, `n_d` and an exact
  CI on the paired risk difference. *A "significant win" at this n can rest on six
  discordant pairs.*

**Pre-registered MDE (verified at this hand, exact test, n=50, 80% power):**

| discordance | 0.16 | 0.20 | 0.30 | 0.40 | 0.50 |
|---|---|---|---|---|---|
| detectable marginal delta | 15.7 pts | 17.6 | 21.9 | 25.4 | 28.7 |

Power at **+10 points**: 0.288 / 0.241 / 0.179 / 0.143 at those discordances — **a real
+10-point improvement is missed roughly three times in four.** §5's write-up sentence is
therefore fixed now: *"this screen could not see an effect below X points at the observed
discordance."*

⛔ **DISCORDANCE PRECONDITION, verified: if `n_d ≤ 5` the pre-registered test has ZERO
power at any split** — the minimum attainable two-sided p is `2·(½)^n_d`, i.e. 0.0625 at
n_d=5 and 0.03125 at n_d=6. **At n_d ≤ 5 no p-value is reported**; the result reads *"the
arms were too concordant for this screen (n_d = k of 50)"* with `b`, `c`, refusal counts
and the exact CI.

**Always reported:** raw token counts per arm by class (uncached in, cache-write,
cache-read, output incl. thinking), dollars at list rates, container-evaluation runs,
wall-clock, solves, per-task budget consumed **as a distribution**, fraction of ceiling
consumed, typed termination reason, attempts per task, `base_fail_rate`,
`base_fail_rate_round1`, `lift`, refusal
precision (patch- and task-level), the selected set's gold-patch-file-count histogram and
per-repo composition, and the two leak covariates `p2p_recoverable` / `f2p_recoverable`
plus `rewrites_existing_test` — **all computed after scoring and never shown to gate or
agent.** The primary result is reported **stratified** on `rewrites_existing_test` and on
`f2p_recoverable > 0`.

**Cost has no undefined branch:** the ratio is printed only with its denominator inline
(`$X / 23 solved`), and **when solves < 5 it prints `undefined (k solves)`** — never
imputed. Gate model calls are charged to the arm that makes them. **No conclusion rests on
the cost ratio; it is context for the primary statistic.**

**Contamination proxy:** normalized edit similarity between the control arm's submitted
patch and the gold patch, reported as a distribution, with the paired result stratified
high/low at a pre-stated cut. *If the effect lives in the low-similarity stratum and
vanishes in the high, that is the contamination signature, visible instead of confounding.*

---

## 6 · Adverse outcomes — THREE, declared before the run

⛔ **v1 registered both outcomes as "interesting" and I called that win-either-way.
Registering both as interesting is NOT registering one as ADVERSE**, and every terminal
state v1 admitted read favourable. That is the ceiling-that-cannot-be-exceeded, in the one
document written to prevent it.

**ADVERSE-1 — the gate did not discriminate.** Refusal precision is compared against
**`base_fail_rate`** — the failure rate of the proposals **the gate actually adjudicated in
the treatment arm** (DESIGN §2), which is the exact chance level for a rate-matched
content-blind refuser on that same stream. **If the 95% CI for `lift` (= precision ÷
`base_fail_rate`) includes or falls below 1.0, wave 1 reports "the gate did not
discriminate" as ADVERSE.**
⛔ *Corrected 21:2x before the first call: this section had said the CONTROL arm's
patch-failure rate while DESIGN said BOTH arms' — two different denominators for one
quantity, and neither was the population the gate judged. The gate never sees a control
proposal.* ⭐ *The capability floor structurally
cannot rescue this: the floor is a claim about the AGENT's recovery; this measures the
GATE's judgement.*

**ADVERSE-2 — net harm.** If the discordant split significantly favours the control arm
(`b > c`, exact two-sided p ≤ 0.05), wave 1 reports the gating discipline as
**NET-HARMFUL at this tier** — more correct patches destroyed than incorrect ones caught.
**This is adverse and is NOT read as evidence for the capability floor.**

**ADVERSE-3 — the cost clause in §1 is enforced.** §1 says "at equal enforced token
spend". **If treatment cost-per-solved-task exceeds control's by more than K = 2× with no
significant solve gain, §1's claim is reported NOT SUPPORTED.** K is fixed now, because
without a pre-stated K any figure can be narrated as acceptable.

**And the floor hypothesis is downgraded to what one tier can support:** a null at a single
tier is consistent with *both* the capability floor *and* a worthless gate *and*
contamination attenuation. **Wave 1 cannot separate them and will make no floor claim.**
⛔ *v1 held two incompatible propositions: §4 chose the tier expressly so the effect would
be measurable, and §6 reserved the right to blame a null on that same tier being below the
floor.*

---

## 7 · Stopping rule

Fixed n = 50 pairs per arm. **No optional stopping, no peeking-then-extending.** Any
batch-sequential extension requires a boundary committed here *before* it runs.

---

## 8 · The persuasion artifact

**3–5 discordant-pair case studies**, drawn from **both discordance directions in
proportion**, ties broken by the §3 draw order. ⛔ **At least one gate-was-wrong case ships
if one exists.** *v1's rule selected "largest held-out delta" and then asserted every case
shows the gate catching a false green — control-favouring pairs cannot show that, so the
rule could select cases contradicting their own caption.*

Every case study must exhibit a refusal whose **typed** reason names the specific defect
the revision fixed. *An illustration that cannot show the mechanism firing is not an
illustration of the mechanism.* Case studies are illustration; the statistic is the
evidence, and the write-up says so.

---

## 9 · Abandon conditions

- **Harness fault — CONJUNCTIVE:** discard only if `n_d = 0` **AND** refusals issued = 0
  **AND** submitted patches are byte-identical on every pair. ⛔ *v1 discarded any run with
  `n_d = 0` as a harness fault — which is exactly the null §6 promises to report, and an
  active gate can produce it by refusing correctly and the agent recovering to the same
  outcome.* Liveness is established by an **arm-independent falsifier**: refusals > 0 and
  at least one shadow-scored refused patch whose outcome differs from its revision's.
- **Refusal rate, with its unit named:** the **per-task** rate (fraction of tasks with ≥1
  refusal). **< 2% is inert** — report and discard. **> 98% is a REPORTED result of harm**,
  not a discard.
- **Too few discordant pairs to test:** `n_d ≤ 5` → reported per §5, never as a null.
- **Leak check with a failing arm:** every scored prediction's sha must appear in the
  accepted-patch log.
- **Cost:** exceeding the ruled $150–400 before the paired run completes → **stop and
  report**, never quietly reduce n.

*Budget arithmetic, so the three-arm design is not wishful: 3 arms × 50 tasks + 30 pilot
pairs ≈ 210 episodes at K = 3 rounds. At Sonnet-5 list rates and ~100k in / 20k out per
round, ≈ $250 — inside the ruled band, and the enforced token cap is what keeps it there.*

---

*Nothing below this line existed before the first model call. Amendments are appended,
dated, with their reason — never edited into the text above.*

---
