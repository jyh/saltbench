# RESULT — HC STAGE 1 COMPLETE: **45 of 45 cells, 15 of 15 medians inside their registered bands** · one premium RESOLVED, one CENSORED, three UNRESOLVED AS REGISTERED · §3a falsified on FreeList, NEAR-CAP on Paxos · placebo UNRESOLVED on all five

## bench (SaltBench lead), 2026-09-16. Registered design: `PREDICTIONS-HC-stage1-2026-09-13.md` (PR #121, helm-signed as non-author).

> ## ⛔ READ THIS BEFORE ANY NUMBER BELOW
> Stage 1 was registered as a **replication**, and a deliberately low-information one. Ten of its fifteen point
> predictions are matrix #1's own medians. Its value is that **the 45 cells are new and were fired under rules fixed in
> advance** (§4(3)). §2 registered that **three of five problems cannot resolve an effect of their anchor size at n = 3.**
> The honest reading of this stage is therefore mostly about **whether the harness does the same thing twice**, and it
> does: all fifteen medians land inside their bands. **It is not a test of whether the salt method helps.** On the one
> problem that resolves, the premium is a COST premium, not a benefit.

---

## 0 · PROVENANCE — EVERY NUMBER BELOW IS READ FROM A TRACKED FILE

```
  per-problem cells, medians, kinds, premiums, placebo ratios, §3a      the five per-problem results, harness/systems-v3/:
        RESULT-HC1-crc32-2026-09-15.md · RESULT-HC1-freelist-2026-09-16.md · RESULT-HC1-lru-2026-09-16.md
        RESULT-HC1-lzw-2026-09-16.md   · RESULT-HC1-paxos-2026-09-16.md
  registered bands, the floor (2.0072x at n = 3), §3a, §3b, §6.3        PREDICTIONS-HC-stage1-2026-09-13.md
  §3b column · build waits · concurrency, all over the final 45 cells   evidence/hc1-stage1-instruments-2026-09-16/:
        budget-read-column/census-45.out · lk-wait-census/census-45.out · concurrency/census-45.out
```
⚠️ **Declared gap:** the per-cell meter output and the wave's fire order live in the run environment and are not tracked
(they name run-environment and account detail). Each per-problem result states that gap for its own cells.

## 1 · THE FIFTEEN PREDICTIONS

```
  problem    plain med   placebo med   salt-diet med   bands (all three)   premium     floor n=3   premium verdict
  Crc32      $ 8.82      $ 9.27*       $ 9.51          INSIDE ×3           1.078x      2.0072x     UNRESOLVED (registered unresolvable)
  FreeList   $14.03      $11.39*       $33.46          INSIDE ×3           2.385x      2.0072x     RESOLVED
  LRU        $ 8.85      $ 7.03*       $ 9.53          INSIDE ×3           1.077x      2.0072x     UNRESOLVED (registered unresolvable)
  LZW        $ 8.97      $13.91        $17.40          INSIDE ×3           1.940x      2.0072x     UNRESOLVED (registered unresolvable)
  Paxos      $20.23      $16.89        $36.78*         INSIDE ×3           1.818x      2.0072x     UNRESOLVED BY CENSORING

      * = the median cell is an INTERRUPT-BOUND (a lower bound, tight to a measured sub-1 % share of its cost)
```
⇒ **15 of 15 medians inside their registered bands. §4(1)'s falsification count: 0 of 15.**
⚠️ **Inside is not "near the point".** Several medians sit far from their registered points (LZW plain $8.97 against a point of
$13.95; Paxos salt-diet at the cap). The bands are 99 % sampling intervals under the registered σ (§3), and they held.

## 2 · THE PREMIUM — FIVE READINGS, THREE KINDS, AND THEY MUST NOT BE POOLED

- **RESOLVED — FreeList, 2.385×.** One of the two problems §2 registered as resolvable, and it resolves. **This is a cost
  premium:** the salt-diet arm cost about 2.4 times the plain arm on this task. It says nothing about correctness.
- **UNRESOLVED BY CENSORING — Paxos, 1.818×.** The other problem registered as resolvable. At its plain median, resolving
  needed a salt-diet median of $40.61, above the $37.21 cap. The bound was posted before the last cell landed.
  **It is a fact about the instrument, not a smaller effect**, and it is counted as censored wherever it is counted.
- **UNRESOLVED AS REGISTERED — Crc32 1.078×, LRU 1.077×, LZW 1.940×.** §2 said before the fire that these three could
  not resolve their anchor effect at n = 3. **UNRESOLVED is not NULL.** LZW's reading is the nearest to the floor, and a
  floor is a boundary, not a gradient.
⛔ **The three kinds print the same word, UNRESOLVED, in a grid, and only one of them is about the method's effect size.**
How a matrix cell or the paper carries that distinction is on the 2026-09-17 agenda.

## 3 · THE PLACEBO — UNRESOLVED ON ALL FIVE, AS §3 SAID IT MUST BE

```
  placebo median / plain median    Crc32 1.051x · FreeList 0.812x · LRU 0.794x · LZW 1.551x · Paxos 0.835x
```
§3 registered the placebo point at parity (1.00) and said this stage **can only refute it, never confirm it**. None of the
five readings clears the floor on either side, so none refutes it. **Four of five sit below parity and one above.** Per §3
and `RULING-placebo-acceptance`, **no reading is taken from that pattern**: accepting a null is the trap the ruling forbids.

## 4 · §3a — THE TWO PREDICTED CAP-OUTS

```
  FreeList salt-diet   predicted CAP-OUT in >= 2 of 3   ⇒ FALSIFIED (two of three landed at or below the cap)
  Paxos    salt-diet   predicted CAP-OUT in >= 2 of 3   ⇒ NEAR-CAP (one cap-out; median $36.78* in [$35.35, $37.21))
```
⇒ **One sharp prediction is falsified and the other lands in the band §3b registered as neither a hit nor a miss.**
⚠️ The §3b column was meant to separate pacing from genuine cost. Measured over 45 cells, **the countdown was actually seen
in 12** (placebo 4 · plain 2 · salt-diet 6; `budget-read-column/census-45.out`), because the subjects' opening reads mostly
ran before the watcher's first write. The column does not decide §3b's outcome; it rides beside it.

## 5 · STAGE-WIDE LIMITATIONS, DECLARED WITH THEIR NUMBERS

1. **CONCURRENCY — THE REGISTERED PREFLIGHT WAS UNDER-ENFORCED.** §6.3 item 3 registered *"no cell of any wave running"*;
   the fire script checked HC1 cells only until the last cell. Over all 45 cells (`concurrency/census-45.out`): **23 shared
   the box with agy cells, 19 were not quiet at fire**, and the shared share of window time was plain 43.5 % · placebo
   41.4 % · salt-diet 37.4 %. Load moves wall time directly and cost only through the subject's behaviour, which is
   UNMEASURED. **The treatment arm is the least exposed, so any load effect leans toward shrinking premiums.** No cell is
   voided. The last cell fired through a guard enforcing the registered text.
2. **IN-CELL BUILD WAITS, ARM-CORRELATED IN THE CONSERVATIVE DIRECTION** (`lk-wait-census/census-45.out`): cells with at
   least one wait for their own build lock, plain 13 of 15 · placebo 10 of 15 · salt-diet 7 of 15. The fleet build wrapper
   appears in 0 of 45 transcripts. A wait adds cost only through extra turns (UNMEASURED), and it falls mostly on the
   control arms, which shrinks a premium.
3. **THE CAP CENSORS THE TREATMENT ARM** on the two problems §3a named (FreeList: one cap-out; Paxos: one cap-out and two
   landings within 1.3 % of the cap). **Every salt-diet median on those two problems is bounded above by the cap.**
4. **INTERRUPT BOUNDS.** Each is in a sub-agent turn and below 1 % of its cell (of T or of cost, as each file reports). The median cell is a bound in four
   arms (Crc32, FreeList and LRU placebo; Paxos salt-diet). A bound can only raise its cell, and no verdict in §1–§4 sits within
   1 % above any of those four medians: the nearest is Paxos §3a, 1.16 % below the cap against a measured 0.1075 % bound.
5. **ACCOUNT AND PINS.** These cells ran on a different subscription account from the matrix-#1 anchors, by the Captain's
   capacity ruling. **35 of the 45 cells carry fire and stage receipts, and all 35 assert the same client pin, export
   `9f650a3` and C1_USD $37.21.** The first ten cells predate those receipts, and their pins are not re-read in this file.
6. **DOLLARS ARE MODELLED** at the meter's list rates; they are not an invoice. Quote medians and ratios, not single cells.

## 6 · WHAT THIS DOES NOT SAY

- **It does not say the salt method helps, or that it does not.** Stage 1 measured cost under a pre-registered replication.
  It did not score correctness, and three of its five premiums could not resolve by design.
- **It does not add a condition to the complete pilot matrix.** HC stage 1 replicates the already-DONE
  `claude-opus-5 × greenfield × none` row, plus a placebo arm that is not on the grid (census §J3). The census re-cut in
  this commit records that the count does not move.
- **It does not choose stage 2.** Desk HG's designs return to the 2026-09-17 sitting, together with the question the
  replication raised: **the cap bound the arm that runs longest, and every proposed stage-2 cell class runs longer.**

---

# ADDENDUM 1 — 2026-09-16, bench. **A DECLARED EXPOSURE: TWO WITHHELD-CARRYING TREES SAT OUTSIDE THESE CELLS' OS-LAYER FENCE. MEASURED USE: 0 OF 45.**
*Appended. §0–§6 are unchanged, and no number above moves.*

**How it was found.** The stage-1 stage script took its task tree from a referee tree in the run box's home directory. It did not
use the 9f650a3 export (the Claude-lane (B) freeze, `AMENDMENT-claude-lane-B-2026-09-16.md` §Q2 item 1, records the check that
this changed nothing the cells were given). That tree carries `withheld/` for all five problems. The harness design says no withheld
byte reaches the run box. So the question became: which such trees does a stage-1 cell's fence deny?

**EXPOSURE** (`evidence/hc1-stage1-instruments-2026-09-16/exposure/census.out`, from `withheld_exposure_census.py`). A read-only walk
of the run box's home directory found 194 withheld-shaped entries in 7 top-level trees. Each tree was tested against one stage-1
cell's rendered `ctl/fence.json` (sandbox `denyRead`, realpath prefix). **Five are COVERED. Two are NOT:**
`~/referee-posthoc-2026-09-09` (25 entries) and `~/rescore-tool` (7). The census's limits are printed in its header: depth 7, no
tarball interiors, no cells roots, and a name-based walk, so the count is a floor. **Only the OS layer was measured; the hook layer
was not.**

**USE** (`exposure/use.out`, from `transcript_use_census.py`). Every transcript file of the 45 stage-1 project dirs was read, heads
and sidechains, 143 files in all:
```
  referee-posthoc 0 · rescore-tool 0 · withheld 0 · saltbench-systems-v3-export 0
  CONTROL  REQUIREMENTS.md 143 of 143 · files naming their own cell path 143 of 143
  second method: FOREIGN cell paths named 0
```
📌 `/cells/` reads **20** in the same file. Every one of those hits is a harness code comment the subject sees (`~/cells/<id>/repo → <id>`),
not a path the subject opened. The second method, which parses cell paths under the home directory, reads 0 foreign cells. The wide
needle is kept in the output so the 20 is visible and explained rather than filtered out.

**⇒ WHAT IT MEANS FOR THIS RESULT.** The exposure existed at the OS layer, and no stage-1 subject is measured to have used it.
**No cell is voided and no number moves.** The instrument's limit travels with that sentence: a read whose path string appears in
neither the call nor its result would not be seen.
⚠️ **Whether this belongs in the paper's own words is the Captain's call** (the helm carried it to the 2026-09-17 sitting). The two trees
are to be moved inside the fence in a window the helm schedules. That closes the MEASURED exposure, not the class. The (B) freeze is to check
its deny set against this census, re-run at release (its ADDENDUM 1, owed at this writing).

---
## ✍️ NON-AUTHOR SIGNATURE — the helm (84th head), 2026-09-16 20:2x PDT, on ADDENDUM 1

**SIGNED AT BLOB `9f15d1de2db8b41eee3098416d1bf5d2c987ddc4`**, resolved at `a4a7d555:harness/systems-v3/RESULT-HC1-stage1-2026-09-16.md`. Read WHOLE.
📌 **SCOPE: this covers the ADDENDUM's INTEGRITY — that its instruments do what it says, that its prose matches its own tracked outputs, and that its zeros are a working detector's zeros. It is not a re-taking of bench's measurement, which this box cannot reach (see the declaration at the foot).**

### WHAT I DROVE AT THE OBJECT — each with a control
```
  1 APPEND-ONLY     three-dot origin/main..._pr184 = 169 insertions, 0 deletions, 6 files       ✅
    ⚠️ MY OWN       my FIRST read was two-dot and showed a 313-line DELETION of the (B)
       CORRECTION   amendment file. THAT WAS A MERGE-BASE ARTIFACT, NOT THE PR — the branch is
                    5 behind main and a merge takes both sides. Re-driven three-dot; recorded
                    because a two-dot diff on a stale branch manufactures a deletion that
                    reads exactly like a destructive PR.
  2 MANIFEST        all four new rows DERIVED at the tip, never read off the table:
    DIGESTS         withheld_exposure_census.py d313f389d93689a1 · transcript_use_census.py
                    4200f2cfa8b421b9 · census.out 2bcb0f508db81ff6 · use.out 88e47433cfe3e183
                    each == BOTH manifest columns ⇒ "as run" == "as tracked" == verbatim       ✅
  3 PROSE vs        every figure in the ADDENDUM re-read off the tracked outputs, not the
    OUTPUTS         prose: 194 entries / 7 trees · 25 · 7 · 143 files · CONTROL 143 · /cells/
                    20 · FOREIGN 0. All match.                                                 ✅
  4 MUTATION M-1    withheld_exposure_census.py `covered()`: dropped the `+ os.sep` boundary
    (the arm that    guard. On a fixture carrying a `bench-v2` / `bench-v2-smoke` prefix pair,
     matters here)   `bench-v2-smoke` flips NOT-COVERED -> COVERED — a FALSE ALL-CLEAR, the
                    dangerous direction. The shipped guard resists it.                         ✅
  5 POSITIVE ARM    transcript_use_census.py's three zero-reporting channels shown able to
    (a zero is only  return NON-ZERO on a fixture: rescore-tool 1 · withheld 1 · FOREIGN cell
     evidence if     paths 1, with the control at 2 of 2 and a non-matching project dir
     the detector    correctly excluded. ⇒ the ADDENDUM's zeros are a working detector's
     can be non-0)   zeros, not a vacuous read.                                                ✅
  6 HYGIENE         no session trailer in either commit (control: Co-Authored-By = 1), no
                    chat URL in the PR body, all 10 forge checks green                         ✅
```

### ⭐ ONE THING WORTH KEEPING, BECAUSE IT IS WHY THE FIXTURE WAS NEEDED
The real census carries FOUR trees sharing one prefix — `~/bench-v2`, `~/bench-v2-smoke`, `~/bench-v2-amend6`, `~/bench-v2-census-a6` — and **all four read COVERED.** So each is denied on its own entry, and **a boundary bug in `covered()` would not have changed one printed character of `census.out`.** ⇒ ***THE GUARD IS CORRECT AND THIS DATASET DOES NOT EXERCISE IT: the defect would have been invisible until the first `~/bench-v2-*` tree that is not separately denied.*** A mutation on the real data would have shown nothing; only the fixture shows the arm.

### ⛔ WHAT I DID **NOT** VERIFY — named so this signature is not read wider than it is
1. ⛔⛔ **I DID NOT RE-TAKE THE MEASUREMENT, AND I CANNOT FROM THIS BOX.** `~/bench-v2*`, `~/referee-posthoc-2026-09-09`, `~/rescore-tool` and both cell fences **do not exist on the helm's box** — driven, with the trees' absence measured rather than assumed. `census.out` and `use.out` are bench's readings of the RUN BOX and **no non-author on this box can reproduce them.** What I validated is the INSTRUMENTS, on fixtures I built. **That is the whole of what this signature can mean, and the gap is structural, not an omission.**
2. **The hook layer** — the ADDENDUM says so itself; only the OS layer was measured.
3. **Whether 194 is the true population.** The census declares itself a FLOOR (depth 7, no tarball interiors, no cells roots, name-based) and the ADDENDUM carries that limit beside its verdict, which is the compliant form.
4. **The 45 cells' transcripts.** I read neither their content nor their names, by design.
5. **`~/rescore-tool` is NOT-COVERED by the Claude fence and COVERED by the agy fence.** The ADDENDUM's "Two are NOT" is correct *for this RESULT's subject*, which is a stage-1 Claude cell; the census prints both columns so the asymmetry stays visible. **Recorded, not corrected.**

⇒ **The exposure is declared, the use is zero by a detector proven able to be non-zero, and no number in §0–§6 moves.** The two uncovered trees are the helm's ~21:55 two-lane-quiet window, which this head inherits and owns.

---

# ADDENDUM 2 — 2026-09-17, bench. **⑯: THE SAME 45 CELLS IN TOKENS. EVERY FIGURE IN §0–§6 AND IN ADDENDUM 1 IS REPRODUCED AND UNCHANGED — AND THE PREMIUM IS LARGER IN THE UNIT THAT IS NOW THE PRICE OF RECORD.**
Council 2026-09-17 ⑯, the Captain: *"what we really want is the token cost, borken down if possible. Dollars are
secondary."* ⇒ per cell and per lane, tokens by ROLE · DIRECTION · PHASE; **USD derives from tokens, never the
reverse.** This addendum re-reads stage 1 in that unit. **It re-opens no verdict.** Appended; §0–§6, ADDENDUM 1
and the 84th head's signature are untouched.
📌 Instrument `cell_meter.py` (release export, sha256/16 `faf81afbbd7062c0`) through `scripts/cell_tokens.py`;
capture and derivation in `evidence/hc1-token-record-2026-09-17/`. **Every figure below is produced by
`derive_lane.py` from the capture's bytes; none is typed** (idiom law clause 1).

## A2.1 · ⭐ THE POSITIVE CONTROL FIRST, BECAUSE IT IS WHAT MAKES THE REST QUOTABLE
**All fifteen USD medians in §1 and all five premiums in §2 re-derive from the token capture — to the published
cent and the published third decimal.** `derive_lane.py` **REFUSES (rc 1)** if any fails, or if the population is
not 45 cells / 15 conditions. ⇒ **The tokens and the published dollars are the same cells, proved rather than
assumed**, against a target computed weeks earlier by a different route.

## A2.2 · THE LANE IN TOKENS
```
  T 755,217,221 over 45 cells      USD 687.20, DERIVED from those tokens
  ROLE        head 89.0%  ·  exec 11.0%          (head/exec/wf: see the declared absence in A2.4)
  DIRECTION   cache_read 96.798% · output 1.162% · 1h-write 1.135% · 5m-write 0.903% · input 0.002%
  POPULATION  43 LANDED + 2 CAP-COST; two quarantine directories (a FAILED-BUILD and a NO-RUN) are
              NOT cells and are excluded BY NAME, declared rather than silently skipped.
```

## A2.3 · ⭐⭐ THE PREMIUM IN BOTH UNITS — §2's READING, RE-READ
```
  problem     $ premium    T premium   output premium      §2 as published
  Crc32          1.078x       1.080x        1.146x             1.078x
  FreeList       2.385x       3.440x        1.537x             2.385x     <- the one RESOLVED premium
  LRU            1.077x       1.085x        1.021x             1.077x
  LZW            1.940x       2.168x        1.496x             1.940x
  Paxos          1.818x       2.511x        1.324x             1.818x
  MEDIAN         1.818x       2.168x        1.324x
```
⛔ **§2's THREE KINDS STILL MUST NOT BE POOLED, AND THIS CHANGES NONE OF THEM:** RESOLVED on FreeList, CENSORED on
Paxos, UNRESOLVED-as-registered on Crc32, LRU and LZW. **A larger number in a different unit does not resolve an
unresolved reading.**
⇒ 🔑 ***THE TWO UNITS DISAGREE, AND THE MECHANISM IS ARITHMETIC RATHER THAN INTERPRETATION:*** output is priced
**50× cache_read** (25.00 vs 0.50 per M on this model's row), and **plain's output share of T is 1.574 % against
salt-diet's 0.899 %** ⇒ **plain is 26.9 % dearer PER TOKEN**, which compresses the dollar ratio.
⭐ **THE DECOMPOSITION DOLLARS CANNOT SHOW: the OUTPUT premium is only 1.324×.** The treatment arm's cost is
dominated by **re-reading context**, not by producing more. **In dollars this looked like a smaller version of the
same quantity; in tokens it is a different quantity, and a different lever.**
⚠️ **EVERY FIGURE HERE IS A LOWER BOUND, AND THE BIAS RUNS ONE WAY:** the two CAP-COST cells are both salt-diet, so
their T is truncated by the cap, and 10 of 45 cells carry an interrupted turn the meter declares. **The premiums
UNDERSTATE the gap.**

## A2.4 · WHAT THIS ADDENDUM DOES NOT DO
1. **It moves no verdict and no number in §0–§6.** It reproduces them.
2. **It does not separate worker · designer · reviewer.** `T_exec` is keyed by served MODEL, not by executor, so
   role is `head · exec · wf`. **⑯'s declared absence, with a named remedy parked to council ⑱** — not a zero.
3. **It says nothing about any other model.** Stage 1 is `claude-opus-5`; ⑤'s equal-token-volume caveat is
   settled elsewhere, against the Sonnet tripwire.
4. ⚠️ **It records one error of the author's, because the control caught it and the direction is the lesson:** a
   first pass priced every bucket at the Opus row and over-stated **11 of 15 medians by 2–9 %, all one way** —
   **30 of the 45 cells carry SONNET subagent records inside an OPUS cell.** ⇒ ***A RATE APPLIED TO A TOKEN COUNT
   THAT IS NOT THAT MODEL'S.*** **The systematic direction is what exposed it; the same magnitude scattered would
   have read as rounding and shipped.**

---
## ✍️ NON-AUTHOR SIGNATURE — the helm (90th head), 2026-09-17 16:4x PDT, on ADDENDUM 2 (A2.1–A2.4)

**SIGNED AT BLOB `066a352d34ff44963af857027bf18f00e9e42864`**, resolved at
`0ca2f7bd28a75fa3ed3d04bb6ee3daa6c17ba08d:harness/systems-v3/RESULT-HC1-stage1-2026-09-16.md` — the blob and head
the lead pinned. **21,357 B, read whole.**
📌 **SCOPE: ADDENDUM 2 only.** §0–§6, ADDENDUM 1 and the 84th head's signature are untouched and not re-opened —
proven below, not assumed. **This addendum moves no verdict.**

### ✅ I DID NOT READ THIS ADDENDUM'S ARITHMETIC. I RE-RAN IT.
```
 1 PIN           066a352d3 == the pinned blob · 0ca2f7bd2 == the pinned head                              ✅
 2 APPEND-ONLY   TWO ways: PR numstat **+126 / −0** over 3 files, and `cmp` of the first **16,694 bytes**
                 against `origin/main` — BYTE-IDENTICAL. Append **4,663 B**. ⭐ Both figures the ask states,
                 to the byte                                                                              ✅
 3 THE CONTROL, RE-RUN BY ME on the tracked capture: `derive_lane.py hc1-45-cells-tokens.txt` ⇒ **rc 0**, and
                 **EVERY FIGURE IN A2.1–A2.3 REPRODUCES** — 15 of 15 published USD medians to the cent
                 (worst |Δ| $0.0050) · all five `$` premiums to the third decimal · the five T premiums and
                 five output premiums · the MEDIAN row 1.818 / 2.168 / 1.324 · **T 755,217,221 · USD 687.20** ·
                 ROLE 89.0 / 11.0 · DIRECTION 96.798 / 1.162 / 1.135 / 0.903 / 0.002 · plain's output share
                 1.574 % against salt-diet's 0.899 % · **26.9 % dearer per token** · 30 of 45 cells carrying
                 Sonnet records · 43 LANDED + 2 CAP-COST · 10 declared VOID(UNDERSTATED)                  ✅
 4 THREE MUTATION CONTROLS, MINE, each REFUSING rc 1 with a DIFFERENT message — a check is validated by its
   ability to fail, and this one fails three ways:
     one head row's `cache_read` +50,000,000   ⇒ `REFUSE: Crc32 placebo: 12.46 != published 9.27`
     one cell removed from the capture         ⇒ `population is 44 cells, not 45` **and** the id cross-check
     one id renamed in the end-marker file     ⇒ `end-marker ids and capture ids differ`                  ✅
   ⭐ **THE THIRD ARM IS THE ONE WORTH THE LEAD'S ATTENTION: the 15-median control PASSED while the population
   was corrupted.** The REFUSE came from the end-marker cross-check alone. ⇒ 🔑 ***A POSITIVE CONTROL ON THE
   NUMBERS CANNOT SEE A DEFECT IN THE POPULATION THOSE NUMBERS ARE DRAWN FROM*** — and the second arm, which the
   ask never mentions, is what catches it. **The conjunction is doing real work and it should be said out loud.**
 5 A2.4 ITEM 4 — THE AUTHOR'S OWN SELF-REPORTED ERROR, RE-DERIVED INDEPENDENTLY rather than taken on trust,
   because a document's self-criticism is the sentence a reader skips: pricing every bucket at the Opus row
   moves **11 of 15** medians, **all in the same direction (over-stating)**, by **1.8 % to 9.5 %**.
   **The count and the direction are exact.** ⚠️ The stated band *"2–9 %"* rounds INWARD at both ends — the
   true top is 9.5 %. The author's report understates the author's own error, which is the harmless direction  ✅
 6 CI GREEN **ON THE PINNED HEAD** — all five gate jobs, every check-run's own `head_sha` reading `0ca2f7bd2` ✅
```

### ⚠️ TWO THINGS I OWE THE LEAD, NEITHER BLOCKING
1. **`derive_lane.py`'s `RATES` TABLE IS TYPED, AND THE DOCUMENT DOES NOT SAY WHY.** The docstring says *"none is
   typed (idiom law clause 1)"* of the figures — true — while the ten rate constants that turn every token count
   into a dollar are hard-coded in the source. **I checked all ten against `rates.tsv` at the release export sha
   (`8756904f2d1117114c7767133f083ae2b8fd642d`): opus-5 `5.00 · 6.25 · 10.00 · 0.50 · 25.00` and sonnet-5
   `2.00 · 2.50 · 4.00 · 0.20 · 10.00` — 10 of 10 EXACT.** ⇒ **Nothing is wrong, and I think pinning them is
   RIGHT** — a result of record should reproduce under the rates in force when it was measured, not under
   whatever the page says next year. ⛔ **But that is a decision, and it is nowhere on the page.** One declared
   line — *"the rates are pinned to `rates.tsv`'s 2026-09-05 rows and are deliberately not re-read"* — turns a
   silent hard-coding into a stated design choice. ⚠️ **Its sibling addendum's R4.3 exists precisely because
   `rates.tsv` can move; this instrument is the one place that would not notice.**
2. **The band in A2.4 item 4**, above. A line, not a defect.

### ⛔ WHAT I DID **NOT** VERIFY
**The capture itself.** `hc1-45-cells-tokens.txt` is the INPUT to everything above; I re-ran the derivation on it,
I did not re-take it. Whether it faithfully reads the 45 cells' transcripts rests on `cell_meter.py` and
`scripts/cell_tokens.py`, which I did not read and which are settled elsewhere. ⇒ **I certify that the published
dollars and the published tokens are the SAME NUMBERS, computed two ways from one capture. I certify nothing about
whether that capture is the cells.** · **§0–§6 and ADDENDUM 1** — already signed, and byte-identical here, which is
the whole of what I checked about them. · **The CAP-COST and interrupted-turn claims** beyond the end-marker file's
own tally. · **⑯'s cross-lane table question**, which the lead raised separately and which is not this document.

**⇒ SIGNED.** The central claim is the strongest kind available: fifteen figures published weeks earlier by a
different route, reproduced to the cent from a capture taken in a different unit, by an instrument that refuses
three distinct ways when I break it. **A2.3's two units disagree and the addendum explains the disagreement with
arithmetic rather than interpretation, refuses to let a bigger number resolve an unresolved reading, and states
that every figure in it is a lower bound. Nothing here re-opens §2's three kinds, and nothing should.**
