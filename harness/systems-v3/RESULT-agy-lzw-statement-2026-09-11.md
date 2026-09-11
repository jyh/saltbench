# RESULT — LZW with the STATEMENT arm, both conditions, scored against the withheld suite
**bench · 2026-09-11 · the plain half is a result; the treated half is CONFOUNDED and says so**

⛔ **Every verdict below comes from `tasks/systems-v3/LZW/G/run_tests.sh`** — the runner the referee
uses — driven per cell against a COPY of each submission. Token and turn figures come from each
cell's own `agy-meter-1.json`; truncation counts from each cell's own `agy-stderr-1.txt`. Nothing
here is retyped from a message.

## §1 · ⭐⭐ plain+statement: THREE OF THREE LANDED, THREE OF THREE 8/8
```
  cell     verdict   tests   T          cmds   truncations
  s2ps01   LANDED    8/8     1,429,927   10     0
  s2pt01   LANDED    8/8     1,320,232   11     0
  s2pt02   LANDED    8/8     1,338,174   11     0
```
All three receipt probes (P-DELIVERY, P-PERSIST, P-ANYWHERE) read `yes` on every cell, so **the
+statement briefing demonstrably loads**. This condition is clean: **no cell was truncated**, none
self-declared an unmet requirement, and all three carry a landing tag and a `LANDING.md`.

✅ **POOLABILITY CHECKED, NOT ASSUMED.** The three normalise to one interface,
`f8f3b763ae5b1655`, and they sit in **two cell roots built from two different exports** — so the
check is load-bearing here rather than ceremonial. The cell builder is **byte-identical** across
both exports (`7810edea2eadd33b`); only the post-run reading path differs.

## §2 · ⛔⛔ salt-diet+statement: CONFOUNDED. THE PASS STANDS, THE FAILURES DO NOT.
```
  cell     verdict       tests   truncations   what happened
  s2st01   LANDED        0/8      3            self-declared R1/R2 NOT; encode left as the STUB
  s2st02   no landing     --      5            terminated mid-implementation; INCOMPLETE
  s2st03   LANDED        8/8      3            encode PROVED, and it passes
```
**Every one of these cells was truncated by a per-turn deadline that cannot bind the control
(§3).** Under the ruling that a bias against the arm under test cannot manufacture a positive:
- ✅ **s2st03's 8/8 STANDS, AND IT IS A FLOOR.** It wrote `encode` carrying
  `ensures codes_view(out@) == encode_model(input@)` — **a machine-checked implementation that also
  passes the complete withheld suite** — *while being cut short three times.*
  ⇒ **The condition can produce a proved, correct LZW.**
- ⛔ **s2st01's 0/8 IS WITHDRAWN as a statement about the condition.** A verdict must be corrected,
  not labelled. The subject's own `LANDING.md` names the mechanism: *"could not be proven within the
  time budget ... They have been left as stubs."*
- ⛔ **s2st02 is INCOMPLETE and sits in no denominator.** No `LANDING.md`, no tag.
- ⛔ **No token, turn or wall figure from any of these three may be pooled across arms.**
⇒ **This condition is being re-run under a corrected, declared deadline. The numbers above are
reported so the confound is on the record, not to support a rate.**

## §3 · 🔑 THE FINDING: A DEFAULT THAT BINDS ONE ARM AND NOT THE OTHER IS NOT A DEFAULT
`agy --print-timeout` is a **per-turn** wall clock, default `5m0s`. The launcher had passed it as a
defaulted value since the day it was written and **nobody ever set it.** Counting `print timeout`
in each cell's own stderr, across every cell of the campaign:
```
  plain       3 cells   0, 0, 0
  salt-diet   5 cells   2, 4, 3, 3, 5          PERFECT SEPARATION
```
The treatment runs a verifier, whose steps take minutes. The control verifies nothing, so its turns
never approach the cap. **The deadline truncates the treatment's turns and never the control's.**
⇒ ***A CAP THAT BINDS ONE ARM AND NOT THE OTHER IS A TREATMENT, NOT A DEFAULT.***

✅ **RAISING IT UNIFORMLY REMOVES A CONFOUND RATHER THAN CREATING ONE, and this is the load-bearing
argument:** no plain turn came near five minutes, so a larger cap **cannot change the control's
behaviour at all.** It binds neither arm — the only state in which the deadline is not a variable.
Raising it for the treatment alone would have been a different experiment.

📌 **THE SAME QUESTION, ASKED OF EVERY OTHER CAP**, measured rather than assumed:
```
  cap                  plain             salt-diet          binds
  per-turn deadline    0 of 3 trip       5 of 5 trip        treatment — FIRED
  wall seconds / cell  738 · 747 · 798   3635 .. 13700      treatment — live
  turns (cap 40)       3 · 3 · 3         6 .. 10            treatment — not yet
  T (cap 250,000,000)  ~1.3M             3.9M .. 19.9M      treatment — not yet
```
**Every cap in the launch path binds the treatment first**, because the treatment runs a verifier.
A cap that *cannot* bind the control is a cap on one arm whether or not it has fired yet. All three
are now required with no default and recorded into each cell.

## §4 · WHAT THIS DOES NOT SUPPORT
n = 3 per condition, **one task** (LZW), one substrate, greenfield only, one declared model.
⛔ **No cost comparison between the arms is offered here**, and the salt-diet cost figures are
withdrawn from comparison until the re-run lands. ⛔ **No landing rate is offered**: a landing
records that the subject stopped, not that it succeeded — one cell in this document declares in its
own landing artefact that it did not implement the task, and lands identically to one claiming all
eight requirements done. **The withheld suite is the only party that separates them.**
📌 The served model remains **DECLARED, not VERIFIED**: the vendor transcript carries no model field.
