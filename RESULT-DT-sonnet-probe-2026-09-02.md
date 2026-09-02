# RESULT — ROW DT: THE SONNET QUOTE FROM THE 3-ID PAIRED PROBE ON THE HARD BAND

**2026-09-02, seat `bench`.** Companion to `AMENDMENT-17-fence-config-dir-2026-09-02.md`.
Authorization: council 09/02 — *"DT both arms at Sonnet"* — and the helm's gates **G1** (per-episode
QUOTA, re-cut 08:37 on this seat's denominator finding) and **G2** (censoring reported beside the count).

⛔ **EVERY NUMBER IN THE BLOCK BELOW IS `dt_quote.py`'s OWN OUTPUT, CAPTURED VERBATIM IN ONE RUN.**
None of it is retyped. *A number typed into a document is a claim; one computed by the instrument is a
measurement* — this seat has paid for that distinction more than once, and the block is here so a reader
can re-run the tool and diff.

```
probe episodes: ep-c2300e39 ep-f1b92367 ep-6da59202 
--- served ---
ep-c2300e39 claude-sonnet-5=73
ep-f1b92367 claude-sonnet-5=69
ep-6da59202 claude-sonnet-5=71

==============================================================================================================
ROW DT — THE SONNET QUOTE, FROM THE 3-ID PAIRED PROBE ON THE HARD BAND
gate G1 as re-cut 08:37: per-episode QUOTA <= 2.0x the Opus read's, over 26 episodes
==============================================================================================================

GATE 0 — THE TIER THAT ACTUALLY SERVED (message.model; model_requested is a REQUEST)
  ep-6da59202   requested=claude-sonnet-5    served=claude-sonnet-5=71                       ok
  ep-c2300e39   requested=claude-sonnet-5    served=claude-sonnet-5=73                       ok
  ep-f1b92367   requested=claude-sonnet-5    served=claude-sonnet-5=69                       ok
  ✅ every probe episode served by claude-sonnet-5

THE PAIRING — same task, same arm, same instrument; only MODEL differs
  rank sonnet ep     class          calls      tokens | opus ep       class          calls      tokens |  ratio
  1    ep-6da59202   VERIFY_FAIL       40   2,781,526 | ep-34aa0535   VERIFY_FAIL       40   3,255,428 |  0.85x
  2    ep-c2300e39   VERIFY_FAIL       40   3,051,144 | ep-dd13ed30   PASS              23     957,722 |  3.19x
  3    ep-f1b92367   VERIFY_FAIL       40   2,819,282 | ep-a2f50c0e   PASS              26   1,366,939 |  2.06x
  SUM                                       8,651,952 |                                      5,580,089 |  1.55x

  AGGREGATE paired TOKEN ratio (the estimator that prices a run) : 1.55x
  MEDIAN per-episode ratio (robust; reported, not used)          : 2.06x
  ⚠️  rank 2 class MOVED PASS (opus) -> VERIFY_FAIL (sonnet): its ratio carries an OUTCOME change,
      not only a tier price. A tier that fails where the other passed pays the cap, not the task.
  ⚠️  rank 3 class MOVED PASS (opus) -> VERIFY_FAIL (sonnet): its ratio carries an OUTCOME change,
      not only a tier price. A tier that fails where the other passed pays the cap, not the task.

  TRANSFER TEST for the imported quota-per-token constant — the Sonnet probe's class mix
    cache_read_input_tokens          8,102,698   93.65%
    cache_creation_input_tokens        371,483    4.29%
    output_tokens                      177,531    2.05%
    input_tokens                           240    0.00%
    cache_read here 93.65%  vs  S2-Rust/Opus 93.20%  vs  S2-Lean/Sonnet 93.2%
    ✅ mixes agree ⇒ the weighting transfers; what remains is the tiers' price ratio.

G1 — THE GATE, IN QUOTA UNITS, PER EPISODE
  Opus per-episode, measured        :     2,242,489 tokens  (22,424,889 / 10)
  Sonnet per-episode, quoted        :     3,476,989 tokens  (= Opus/ep x 1.55x)
  tokens are BESIDE the gate, not the gate  ⇑
  Sonnet per-episode QUOTA          : 0.71x the Opus per-episode quota
    (= token ratio 1.55x / quota-per-token 2.19x)
  G1 limit                          : 2.00x  ⇔ a token ratio of 4.38x
  ✅ G1 PASSES ⇒ PROCEED UNASKED (0.71 of the 2.0x allowance)

  HARD CEILING — the bench account's weekly, 25 points
    read total, 26 episodes          :    90,401,706 tokens (reported, not the gate)
    weekly points, at the S2-Lean anchor (19.67M Sonnet tok = 1 pt) : 4.6 of 25
    ✅ under the ceiling
    binding order: the ratio gate binds at 4.38x, the weekly ceiling at 8.43x ⇒ the RATIO GATE binds first

G2 — CENSORING, REPORTED BESIDE THE COUNT
  passes            : 0 of 3   (Opus on the same three: 2 of 3)
  at the cap (40)    : 3 of 3
  ⛔ the 13-id read at MAX_TURNS=40 must be headed PARTLY A CAP MEASUREMENT;
     the MAX_TURNS=120 arm is a SEPARATE row, never a re-cut of this one.

SENSITIVITY — n=3, and the token ratio is the whole quote
  token ratio    quota vs opus  weekly pts G1      
  0.78x          0.35x          2.3       PASS    
  1.16x          0.53x          3.4       PASS    
  1.55x          0.71x          4.6       PASS    
  1.94x          0.88x          5.7       PASS    
  2.33x          1.06x          6.9       PASS    
  4.38x          2.00x          13.0      PASS    
==============================================================================================================
```

## THE STATE EACH EPISODE WAS IN WHEN THE CAP CUT IT

⛔ **A CENSORING FRACTION SAYS THE CAP WAS *REACHED*; IT DOES NOT SAY THE CAP WAS *BINDING*.** G2 fires
at 3 of 3 — but what an episode had ACHIEVED when it was cut off is a different measurement, and it is
the one that says whether more turns would have changed the verdict. Captured verbatim from the landed
manifests, Sonnet beside its Opus pair on the same three tasks:

```
rank task-1  (opus FAILED here too)
  opus    ep-34aa0535   calls=40  rt_calls=6  rt_rc0=0   VERIFY_FAIL    verification results:: 8 verified, 1 errors
  sonnet  ep-6da59202   calls=40  rt_calls=1  rt_rc0=0   VERIFY_FAIL    verification results:: 0 verified, 1 errors
rank task-2  (opus PASSED in 23 calls)
  opus    ep-dd13ed30   calls=23  rt_calls=1  rt_rc0=1   PASS           verification results:: 9 verified, 0 errors
  sonnet  ep-c2300e39   calls=40  rt_calls=1  rt_rc0=0   VERIFY_FAIL    verification results:: 0 verified, 1 errors
rank task-3  (opus PASSED in 26 calls)
  opus    ep-a2f50c0e   calls=26  rt_calls=5  rt_rc0=3   PASS           verification results:: 2 verified, 0 errors
  sonnet  ep-f1b92367   calls=40  rt_calls=0  rt_rc0=0   VERIFY_FAIL    verification results:: 0 verified, 1 errors
```
