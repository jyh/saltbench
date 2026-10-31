# RESULT — O90 stage 1, the truth axis (AMENDMENT-O90-stage1 A3.2–A3.5, ADDENDA 3–10) — 2026-10-31

Every figure below is copied from a file in `harness/s2lean/o90-2026-10-23/truth-2026-10-31/`, named beside it. Nothing is
retyped from a message.

## The decision (A3.4b)

Over all WRITTEN, scored sentences, confirmed-FALSE against not, a5 against a0, one-sided Fisher exact, p ≤ 0.10
("wrong on truth" if a5's rate is significantly higher). From `flaglog.out`:

```
PER SENTENCE (whole): a5 39 / 915 · a0 0 / 39 confirmed FALSE of scored written sentences · one-sided Fisher p = 0.1898 · artifacts unreached by the confirmer a5 0 · a0 0
PER SENTENCE (doc): a5 0 / 159 · a0 0 / 39 confirmed FALSE of scored written sentences · one-sided Fisher p = 1.0000 · artifacts unreached by the confirmer a5 0 · a0 0
```

**p = 0.1898 > 0.10: the test does not find a5 wrong on truth.** This is the registered test's outcome at this n. It is
not a finding that the two arms are equally truthful: a0 contributes 39 written sentences, against a5's 915 (see Limits).

## The assumption the test rests on, printed beside it (A3.4b)

The confirmer sees flagged sentences only, so the per-sentence test is fair only if the readers flag the two arms at like
rates. From `flaglog.out`:

```
FLAG RATE per sentence (mechanism, arm): FALSE flags / scored reads
  claude   a0  0 / 39
  claude   a5  32 / 922
  gemini   a0  0 / 39
  gemini   a5  103 / 928
FALSE FLAGS NOT CONFIRMED (mechanism, arm): not_confirmed / flags
  *        a5  62 / 135
  claude   a5  2 / 32
  gemini   a5  60 / 103
```

Neither reader flagged any a0 sentence. The two readers disagree on a5: of read 2's (Claude) 32 flags the confirmer
rejected 2; of read 1's (Gemini) 103 it rejected 60.

**The condition is read, not only printed** (`fisher-checks.out`, from `o90_fisher_checks.py`, whose control line reproduces
the decision's 39 / 915 and p = 0.1898 exactly):

```
FLAG-RATE FISHER read 1 (gemini): a5 103/928 vs a0 0/39 one-sided p = 0.0113
FLAG-RATE FISHER read 2 (claude): a5 32/922 vs a0 0/39 one-sided p = 0.2597
```

**The like-flag-rate condition FAILS for read 1** and is not rejected for read 2. Its direction: a5 is exposed to more
confirmer noise than a0, which pushes the test TOWARD firing, so it does not weaken a test that did not fire.

**A9.6 (1), the flag rate split by k** (read 1 only; read 2 cannot split, A9.6 (4)). `split-by-k.out`, from
`o90_split_by_k.py` over `read1-rows.tsv` and `read1-split.tsv` (read 1's own `split.tsv`, copied by hash
ef161369aca302eb; all 103 split sessions matched a row, and the split counts equal `split.tsv`'s 34 FALSE · 64 OK · 5 TIMEOUT):

```
A9.6 (1) FLAG RATE split by k, read 1 (gemini): FALSE flags / scored reads [unscored]
  a0 chunk 0 / 39  [0]
  a0 split 0 / 0  [0]
  a5 chunk 69 / 830  [0]
  a5 split 34 / 98  [5]
```

Every split read is a5, and split reads flag at a much higher rate than chunk reads (34/98 against 69/830). Since a split
read sees one sentence where a chunk read sees up to 7, this is the shift A9.6 (1) exists to make visible. It acts on a5
alone, in the direction of more flags.

## Per artifact (A3.4a: REPORTED, does not decide)

`flaglog.out`, PER ARTIFACT: 17 a5 artifacts carry at least one confirmed-FALSE sentence, 6 a5 artifacts are UNSCORED (a
sentence in them was never scored), 1 a5 artifact reads 0. a0 (23 artifacts listed): 9 read 0, 14 have no written prose, 0 UNSCORED.
By A3.4a this rule cannot decide at the calibration's n; its noise rate is the calibration's (next section).

## The confirmer's calibration (A3.4a, ADDENDUM 5)

`calib-summary.txt`:

```
CALIBRATION (A3.4a): TRUE scored 45 · confirmed FALSE 1 · rate 0.0222 · 95 % upper 0.1011 · UNSCORED 0
  PLANTED mut_true=NO scored 42 · confirmed FALSE 38 (recall)
  PLANTED mut_true=YES scored 2 · confirmed FALSE 0 (recall)
```

At the 95 % upper bound (10.1 %) the a5 noise-only per-artifact fire rate is far above A3.4a's 25 % line, so the
per-artifact table above is reported and does not decide.

## The sets as run

| set | file | units | outcome |
|---|---|---|---|
| read 1 (Gemini, A9) | `read1-rows.tsv` | 153 chunks | DONE (its own run; rows copied by hash) |
| read 2 (Claude, A3.3/A7.6) | `read2-rows.tsv`, `read2-run.log` | 153 chunks | DONE, no HALT |
| calibration (A3.4a) | `calib.tsv`, `calib-run.log` | 30 sessions | DONE |
| confirmer (A3.4) | `confirmations.tsv`, `confirm-run.log` | 24 artifacts | DONE: 39 yes · 61 no · 5 UNSCORED |
| merge + flag log | `flaglog.tsv`, `flaglog.out` | — | rc 0 (tools by sha in `merge-tools.sha`) |
| checks asked by the PM's read | `fisher-checks.out`, `split-by-k.out` | — | `o90_fisher_checks.py`, `o90_split_by_k.py` (no spend) |

Claude spend, one meter (`claude-meter.tsv`, summed by unit prefix): read 2 159 attempts (7 failed) 17.233731 USD ·
calibration 30 (0 failed) 2.476885 USD · confirmer 27 (4 failed) 5.219255 USD · total 24.929871 USD = 1.283 points at
ADDENDUM 10's R (19.4315 USD/pt as the driver printed it, `read2-run.log`), against the 3-point cap.

## Limits (they ride with the decision)

1. **a0's n is 39 written sentences** (14 of its 23 listed artifacts have no written prose). With 0 flags on a0, the test's power
   against a small a5 excess is low; p = 0.1898 is a failure to find, not evidence of equality.
2. **UNSCORED is not missing at random** (A9.6 (6)): 6 a5 artifacts are UNSCORED and leave the per-sentence denominators;
   which sentences they are is listed by id in the runs' rows.
3. **The two readers disagree on a5** (flag rates 32/922 vs 103/928; flags the confirmer rejected 2/32 vs 60/103). The confirmer is one
   Claude model (A3.4), the same vendor as read 2; that agreement is not independent of read 2's flags.
4. **The confirmer's false-positive rate is bounded at 10.1 %** (95 %, n = 45). The bound applies to flagged sentences
   that are in fact not false: the confirmer scored 100 a5 flagged sentences (`confirmations.tsv`: 39 yes + 61 no), so noise
   alone can account for about 6.9 (0.1011 × 61 / (1 − 0.1011), if every NO is right) to 10.1 (if all 100 were true) of the
   39 confirmations, 18–26 % (systems' F2 on #419). Noise can only lower a5's count, which raises p. a0 has no flags to confirm, so noise cannot
   touch its rate.
5. The Claude spend is priced at ADDENDUM 10's pinned R, with its four limits.
6. **The like-for-like read is 0 against 0.** All 39 of a0's written sentences are doc comments, and none of a5's 39
   confirmed FALSE is a doc comment (`flaglog.out`, PER SENTENCE (doc): a5 0 / 159 · a0 0 / 39). So the decision compares a5's
   doc and explanation prose with a0's doc prose only, and the doc-only read finds nothing in either arm.
7. **The decision's 39 / 915 rests on `o90_flaglog.py`'s rule E1 (taken at ad190cd), which the amendment does not register.**
   E1 decides a confirmed FALSE before UNSCORED. Three a5 sentences were flagged FALSE by read 1, left UNSCORED by read 2, and
   confirmed yes: 60/a5 ep-0144a0f3 explain:18 · 82/a5 ep-47933543 explain:20 · 149/a5 ep-32ec30df explain:24 (each its
   artifact's only FALSE and only unscored sentence). A3.4 (M2) as registered reads "an artifact with ANY unscored sentence, AT
   A READ or at the confirmer, is UNSCORED", and the tool's own docstring and printed header say the same, so as printed they
   are false of these three rows. **Read literally, M2 gives** per artifact a5 14 FALSE · 9 UNSCORED · 1 zero, and per sentence
   a5 36/912 vs a0 0/39, one-sided p = 0.2151 (`fisher-checks.out`, STRICT). E1 is the reading that leans toward firing, so the
   reported p is the lower of the two; both are above 0.10 (systems' F1 on #419; the PM's ask 4).
8. This RESULT reports stage 1's truth axis only; it makes no claim about the salt method's effect beyond the registered test.
