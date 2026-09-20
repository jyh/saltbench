# MEASUREMENT — LEVEL 7's RETENTION SEPARATION, DECOMPOSED INTO SURVIVAL AND GROWTH
## bench (SaltBench lead), 2026-09-19. **This is a MEASUREMENT, not an erratum.** It is the act
## `RESULT-claude-blockSB-2026-09-19.md` §8 item 6 declares OWED, discharged the same evening.
## ⛔⛔ **IT DOES NOT AMEND `RESULT-gemini-level7-2026-09-19.md`, WHICH IS SIGNED.** An erratum to a signed
## result of record, and any change to what a REGISTERED PRE-DATA SEPARATOR MEANS, are the Captain's
## (helm, 106th, 2026-09-19). This file supplies the numbers such a decision would rest on and nothing more.
## 📌 Receipt: `l7-retention-decomp.tsv` — 84 rows, produced by importing the LEVEL-7 EXPORT'S OWN classifier.

---
# §1 · WHAT WAS ASKED, AND WHY IT COULD NOT BE ANSWERED BY INSPECTION
`RESULT-gemini-level7-2026-09-19.md` §1 reports: ***"THE SEPARATOR THAT DOES MOVE IS RETENTION, AND IT MOVES
IN THE SAME DIRECTION IN 7 OF 8 (model × problem) PAIRS"*** — §K6 rule 10's primary brownfield separator.
Block SB then established that `retained` is **difflib's similarity ratio of the end file against the seed,
symmetric in additions and deletions**, so it cannot distinguish *"the component was rewritten"* from *"the
component was kept and something large was written beside it."* **The same metric carries level 7's headline.**
⇒ **The question is not whether 7 of 8 is arithmetically right — it is. The question is what the 7 is made of.**

---
# §2 · THE CONTROL, AND IT IS THE REASON THE REST OF THIS FILE CAN BE BELIEVED
Before decomposing anything, the pipeline was made to **reproduce level 7's published table**. On §1b's stated
population — *"only cells that RAN THE EXPERIMENT: ended, and received their arm"*, excluding the three cells
§1b names (`l7cpbs03` VOID(NO-BRIEFING), `l7cfss02`/`l7cfss03` never ran) — **all sixteen printed bands
reproduce, and the headline count reproduces at 7 of 8.**
```
  retained, salt median below plain median:   7 of 8 pairs      level 7 §1 says 7 of 8      ✅ REPRODUCED
  Flash × LZW is the exception                salt 0.446 > plain 0.443                      ✅ REPRODUCED
```
⭐ **A decomposition that could not first reproduce the number it decomposes would be measuring something else**
— which is the whole subject of block SB's §2, so it is proved here rather than assumed.

---
# §3 · THE DECOMPOSITION — SAME 8 PAIRS, SAME STATISTIC, SAME POPULATION
`surv` = seed lines matched / seed lines · `growth` = end lines / seed lines, **from the same differ**, with
**every `retained` asserted equal to the level-7 export's own classifier value** (the producing script imports
`brownfield_rewrite_class.py` from export `9bfb6ef86a36` and fails otherwise; 84 of 84 asserted, 0 refusals).
```
                   RETAINED (published)          SURVIVAL (what §B5's words describe)      GROWTH
  model problem    plain   salt   direction      plain   salt   direction                  plain   salt
  Flash Crc32      0.654  0.292  salt<plain      0.700  0.720  salt>plain   <- FLIPS        1.23x  3.87x
  Flash FreeList   0.664  0.390  salt<plain      0.766  0.929  salt>plain   <- FLIPS        1.31x  3.71x
  Flash LRU        0.948  0.231  salt<plain      0.980  0.765  salt<plain                   1.07x  5.62x
  Flash LZW        0.443  0.446  salt>plain      0.605  0.835  salt>plain                   1.60x  2.87x
  Pro   Crc32      0.694  0.236  salt<plain      0.660  0.780  salt>plain   <- FLIPS        0.93x  5.80x
  Pro   FreeList   0.885  0.610  salt<plain      0.883  0.995  salt>plain   <- FLIPS        0.99x  2.06x
  Pro   LRU        0.976  0.309  salt<plain      0.990  0.912  salt<plain                   1.02x  4.74x
  Pro   LZW        0.990  0.306  salt<plain      0.990  0.805  salt<plain                   1.00x  4.11x
  ----------------------------------------------------------------------------------------------------
  RETAINED  salt below plain in 7 of 8      SURVIVAL  salt below plain in 3 of 8
  THE TWO DISAGREE ON DIRECTION IN 4 OF 8 PAIRS — HALF THE TABLE
  GROWTH    plain medians 0.93x .. 1.60x   ·   salt medians 2.06x .. 5.80x   ·   DISJOINT ON ALL 8 PAIRS
```

---
# §4 · ⇒ WHAT THIS ESTABLISHES, AND WHAT IT DOES NOT
✅ **ESTABLISHED, on arithmetic alone:**
1. **Level 7's 7-of-8 retention separation is a GROWTH separation.** Growth is disjoint on 8 of 8 pairs;
   survival is in the same direction on only 3 of 8, and **flips outright on 4 of 8**.
2. **Over all 84 cells the medians INVERT.** `retained` plain **0.719** vs salt **0.316**; `surv` plain
   **0.715** vs salt **0.860** — ***on the quantity §B5's words describe, the salt-diet arm kept MORE of the
   given than plain did.*** `growth` plain 1.04x vs salt 3.85x.
3. **This is the SECOND lane with the same signature**, measured independently of block SB and reproducing
   its published figure first.
⛔ **NOT ESTABLISHED, and named rather than implied:**
1. **Level 7's numbers are not wrong.** Every `retained` value reproduces. **What is at issue is what the
   number means**, not what it is.
2. **No arm claim is made or withdrawn here.** Level 7 makes no pass-rate claim; this file makes none either.
3. **The MECHANISM is not measured on this lane.** Block SB hypothesises a Verus-proof method file as the
   source of the growth, from two method files' headings. **No such reading was taken for level 7's cells.**
4. **`surv` is a lower bound on survival** — it counts lines the differ MATCHED, and a moved line may not match.
   ⚠️ **This direction matters here:** under-counting matched lines makes salt's survival look LOWER, so it
   works AGAINST the finding in §4①②, never for it.
5. **The cross-lane picture is that survival has no consistent direction at all.** Block SB's survival is
   salt-below-plain on 3 of 5 problems; level 7's is salt-below-plain on 3 of 8 pairs. ⇒ **`retained` gives a
   strong, consistent direction across both lanes and `surv` gives none** — which is what a volume signal
   looks like.

---
# §5 · WHAT IS OWED AND TO WHOM
⚖️ **THE CAPTAIN'S:** whether level 7's §1 takes an erratum, and its wording; and whether the registered
pre-data separator's MEANING changes. Both go to Monday's pack with this file as their evidence.
📌 **MINE, and not taken here:** if an erratum is ruled, it is appended **below** level 7's signed text and
inside nothing. **No byte of `RESULT-gemini-level7-2026-09-19.md` is modified by this commit.**
⛔ **NOBODY'S, YET:** whether the campaign reports `surv` and `growth` beside `retained` from now on. Block SB
proposes it as an additive remedy; it is a change to a registered reading and it is not made by measurement.

---
# §6 · PROVENANCE
```
  cells        84, ~/cells-l7-<condition>/<cellid> on the run box, resolved 84 of 84 from level 7's own
               cells table; read READ-ONLY, nothing written, no cell re-run
  witness      <export 9bfb6ef86a36>/tasks/systems-v3/<problem>/brownfield/solution.rs — the level-7 export,
               whose five brownfield seed shas are IDENTICAL to block SB's build export (checked, both boxes)
  classifier   brownfield_rewrite_class.py from the SAME export, imported (not reimplemented), with every
               `retained` asserted equal to classify()'s own value: 84 of 84, 0 refusals, 0 bytes of stderr
  population   §1b's, verbatim, excluding l7cpbs03 · l7cfss02 · l7cfss03
  receipt      l7-retention-decomp.tsv (84 rows)
  verifier     MEASUREMENT-l7-retention-decomposition-2026-09-19-verify.py — re-derives §2 and §3 from the
               receipt and level 7's own cells table, and asserts them against the bytes of this file.
```
