# RESULT — ② the four-cell LZW spec-change pilot, phase 2
**bench · 2026-09-10 · run 3, fired 17:20:40Z, harvested 18:00Z**

⛔ **EVERY NUMBER BELOW COMES FROM `RESULT-specchange-1-verdicts-2026-09-10.tsv`**, which names the
`METER.txt` each row was read from. Nothing is retyped from a message or from memory.
📌 Registered in ADDENDUM 8 (the run account and the phase seam) and ADDENDUM 9 (how a capped cell is
read — **written mid-wave while both treatment cells were still running and uncapped**).

## §1 · THE VERDICTS
```
  cell       arm        end        cost         T            commits
  93323249   plain      LANDED     $12.00       11,034,644   12
  22ee7d33   plain      LANDED     $17.15       17,586,952   12
  18fb3eed   salt-diet  LANDED     $17.28       20,910,486   10
  6d58f1ec   salt-diet  CAP-COST   >= $18.71    22,098,384    9      CENSORED
```
**LANDING RATE — the primary comparison under any censoring (addendum 9 J3.2):**
`plain 2/2 · salt-diet 1/2`.
⛔ **`6d58f1ec`'s cost is a FLOOR, not a price.** It passed a cap armed at $18.60 before the first
model call and the harness printed the **overrun** rather than clipping it, so the floor is the
metered $18.71 — **tighter than the cap, and the rule I registered said `>= cap`.**
⇒ 🔑 ***A RULE WRITTEN FROM THE DESIGN CAN BE MORE CONSERVATIVE THAN THE INSTRUMENT ACTUALLY IS*** —
reporting `>= $18.60` would have discarded information the meter deliberately preserved.

## §2 · ⭐⭐ THE TOKEN FIGURES BESIDE THE DOLLARS, AND THEY SHOW THE MECHANISM
Per the Captain's standing order of 2026-09-10. Split from each cell's own `RECEIPT` rows:
```
  cell       arm        output    cache_read     cache_read%  output%   $/M-T    $/M-output
  93323249   plain      170,031   10,562,171     95.7 %       1.54 %    1.0875   70.58
  22ee7d33   plain      212,301   16,951,765     96.4 %       1.21 %    0.9752   80.78
  18fb3eed   salt-diet  173,624   20,442,928     97.8 %       0.83 %    0.8264   99.53
  6d58f1ec   salt-diet  199,958   21,521,907     97.4 %       0.90 %    0.8467   93.57
```
⇒ ⭐ **OUTPUT IS NEARLY FLAT ACROSS ALL FOUR CELLS (170k–212k, a 1.25x spread) WHILE `T` VARIES 2x
(11.0M–22.1M).** The agents *wrote* about the same amount in every cell. What differs is how much
context was re-read to write it.
⇒ 🔑 ***THE COST DIFFERENCE BETWEEN THESE CELLS IS ALMOST ENTIRELY CACHE READS, NOT PRODUCTION.***
⇒ **And it reproduces the campaign-wide reversal on this wave, at n=4:** the treatment is CHEAPER per
token of total traffic and DEARER per token produced. Both orderings are arithmetically correct, which
is why every figure here names its denominator.

## §3 · ⛔ WHAT THIS WAVE DOES NOT SUPPORT — STATED BEFORE THE NUMBERS WERE KNOWN
**n = 2 per arm, one task (LZW), one model (`claude-opus-5`, verified at `message.model` in all four
transcripts, zero `<synthetic>` records).** Nothing here is inferential: no p-value, no interval, and
**no claim that either arm costs more in general.** Registered as addendum 9 §J5, before any cell ended.
📌 The deliverable the commission asked for is **believability**: the change request was taken in all
four cells, each produced 9–12 commits against its customer commit, and three reached a declared
`landing-2` with a fresh hash.

## §4 · ⚖️ PROVENANCE AND THE TWO PRIOR RUNS, BECAUSE A RESULT THAT HIDES ITS RETRIES IS A LIE
This is **run 3**. Both earlier runs are archived, not discarded:
- **Run 1** (07:09Z) — died at the run account's weekly quota wall. **Spent nothing**: one record per
  cell, model `<synthetic>`, which is the client's own limit dialog and not a served turn.
- **Run 2** (16:58Z) — **VOIDED BY THIS SEAT**, ~$18.4 discarded. Every cell inherited phase 1's
  completion marker (`repo/.seat/<ID>`), so each phase-2 session began with its exit condition already
  satisfied; two cells ended mid-work recorded as a clean `END LANDED`. Archived as patches and
  transcripts. ⛔ **Not a cost of reuse-by-copy** — an in-place phase 2 inherits the same marker.
- **Run 3** carries a start-condition gate: the marker is cleared and what it said is logged, HEAD must
  be the customer commit, and the tree must be clean. **Spurious `landing-1` declarations: 0, against
  4 in run 2.**
📌 The account moved between phases (registered, addendum 8 §H1): the account is constant **across
arms within phase 2**, so the between-arm comparison is unaffected; any within-cell phase-1→phase-2
delta carries the seam. Each cell records its resolved account uuid in `ctl/account.tsv`.


---

# ⛔⛔ AMENDED 2026-09-10 — THIS RESULT REPORTED CLAIMS AND CALLED THEM VERDICTS
Everything above stands as a record of what the cells DECLARED and what they COST. **None of it was a
correctness result**, and the table's own file is named `…-verdicts-….tsv` while containing none.
Driven since, with `LZW/B/run_tests.sh` — the post-change suite, the runner the referee uses — from
copies, archive byte-unchanged:
```
  93323249 plain 15/15 · 22ee7d33 plain 15/15 · 18fb3eed salt-diet 15/15 · 6d58f1ec salt-diet 15/15
  VERIFIED 4/4 in BOTH arms.        The LANDING rate above was plain 2/2, salt-diet 1/2.
```
⇒ **`6d58f1ec` was CAPPED, never declared a landing, and is CORRECT.** ⇒ 🔑 ***A LANDING CLAIM
UNDER-STATES AS READILY AS IT OVER-STATES; it answers "did the subject say it was done", not "is it".***
⇒ **The §1 landing rate is a DECLARATION rate. The correctness result is 4/4 both arms.** See
ADDENDUM 10 of `AMENDMENT-specchange-taskshape-2026-09-09.md`, which also corrects addendum 9 §J3.2
where I made the landing rate the primary comparison.
