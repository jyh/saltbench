# RESULT — THE STATEMENT ARM ON THE PILOT (AMENDMENT statement-arm-pilot 2026-09-09)
## **INTERIM: wave 1 COMPLETE and scored; wave 2 (FreeList) 4 of 6 landed, 2 STILL RUNNING at the time of writing.**
Every number is derived from the verdicts table beside it and from each cell's harvested `METER.txt` (SS23(e)).

## §1 · WHAT FIRED, AND WHAT DID NOT
```
  18 of 24 cells fired.  Crc32 x6 + LRU x6 (wave 1) + FreeList x6 (wave 2).
  PAXOS x6 NEVER FIRE, and that is a RESULT rather than a shortfall:
    an arm-neutral formal statement CANNOT EXIST for a proof-obligation task -- Paxos's
    extracted statement names `proof fn` because its specification IS proof obligations, and
    the rendered REQUIREMENTS.md is read by the PLAIN arm too. The harness's neutrality gate
    refuses those cells. A plain+statement Paxos cell would be a control told to write proofs.
```

## §2 · CORRECTNESS — pre-registered for these cells by `PRESPEC …437ea70`
```
  wave 1 (12 cells): PASS 12
  wave 2 (4 landed so far): PASS 4 (7/7 each) · 0 NO-BUILD · 0 CAP-COST
```
⇒ **Every statement-arm cell scored so far passes its withheld suite.** ⛔ A PASS is *the withheld
suite did not fail it*, and that suite's 44/44 is a **CEILING, not a strength**.

## §3 · COST, from the ARCHIVE
```
  problem   arm            n   cells                       median
  Crc32     plain         3   $6.36 $6.66 $8.64          $6.6600
  Crc32     salt-diet     3   $5.65 $6.25 $8.56          $6.2500
  FreeList  plain         3   $17.72 $18.26 $18.42       $18.2600
  FreeList  salt-diet     1   $29.00                     $29.0000
  LRU       plain         3   $8.92 $9.36 $15.12         $9.3600
  LRU       salt-diet     3   $13.65 $14.24 $18.65       $14.2400
```

## §4 · ⛔⛔ THE GOLD PAIR — AND THE SIGN IS NOT UNANIMOUS
```
  problem    (e)/(d) premium      bare premium      change
  Crc32     0.9384x              1.1610x           -0.2226
  LRU       1.5214x              1.2826x           +0.2388
  LZW       1.8105x (pilot)      1.3749x           +0.4356 AMPLIFIED
  FreeList  pending (n=1 of 3)   2.8070x           --
```
⇒ 🔑 ***THE BARE ARMS WERE 5 OF 5 ABOVE 1. THE STATEMENT ARM IS NOT UNANIMOUS:*** `Crc32` comes in
**BELOW 1** at 0.9384x. ⛔ **ALL magnitudes are below the registered 2.0072x floor and are
UNRESOLVED** -- the statement arm supports **no magnitude claim at all**, which is a WEAKER
position than the bare arm's, not a friendlier one.

## §5 · ⛔ WHAT THIS CANNOT DELIVER, REGISTERED BEFORE THE FIRST CELL FIRED
```
  one-sided sign test, k of k:  k=3 p=0.1250 · k=4 p=0.0625 · k=5 p=0.0312
```
**k = 5 is the minimum for significance and Paxos is one of the five.** ⇒ **THE GOLD PAIR CANNOT
REACH A VERDICT IN THIS DESIGN.** With `Crc32` below 1 the best attainable at k = 4 is **3 of 4,
p = 0.3125.** ⇒ **These cells buy magnitudes, correctness verdicts and a fourth problem. They
cannot buy a verdict, and that was registered in ADDENDUM 2 before any of them fired.**

## §6 · ⛔ THE CAVEAT THAT TRAVELS WITH EVERY NUMBER HERE
**BUDGET STOPS ARE ARM-CORRELATED.** In the pilot all three CAP-COST cells were `salt-diet` and
none were `plain`; the correctness column scored **18 plain against 12 salt**. The dropped salt
cells are the ones that ran long enough to hit the cap -- **the hard ones** -- so **the treatment
arm's pass rate is biased UP by construction.**
⚠️ **FreeList was the registered cap risk and it has NOT fired so far:** its bare diet median is
**$37.60** against a **$37.21** cap, yet its first diet+statement cell landed at **$28.14**. **Two
cells are pending and no claim is made until the condition closes.**
