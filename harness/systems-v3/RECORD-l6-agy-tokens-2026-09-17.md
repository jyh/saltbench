# RECORD — LEVEL 6, THE agy LANE IN TOKENS (council 2026-09-17 ⑯)
## bench (SaltBench lead), 2026-09-17, at level 6's close. Companion to `RESULT-gemini-level6-2026-09-17.md`.
## His ⑯, verbatim in scope: **the price of record for saltbench is TOKENS, broken down where possible; dollars are
## secondary** — per cell and per lane, by ROLE and by DIRECTION, phase where the harness logs it; **a VOID stays a
## declared absence; USD derives from tokens, never the reverse.**
## ⛔ Every figure is derived from each cell's own `ctl/agy-meter-1.json`, read read-only on the run box. Nothing is retyped.

---
# §1 · ⛔ WHAT THIS LANE CANNOT SAY — THE VOIDS, DECLARED FIRST BECAUSE ⑯ REQUIRES IT
The Claude lane's ⑯ record carries four directions and a role split. **The agy lane carries three directions and no
role split, and that is a property of the meter, not of the run.** Censused across **all 36 cells** and **31 distinct
meter keys**, with live positive controls:
```
  PRESENT   per_key.input_tokens · per_key.output_tokens · per_key.cache_read_tokens
            per_key.thinking_tokens                                    36 of 36 cells
  ⛔ VOID   cache-create      no key matching `cache_creat` anywhere    ABSENT
  ⛔ VOID   by ROLE           no `role` / `subagent` key                ABSENT
  ⛔ VOID   by PHASE          no `phase` key in the meter               ABSENT
  ⛔ VOID   USD               this lane is a SUBSCRIPTION with no per-token price
```
⚠️ **The controls discriminate:** the same probe returns hits for `input`, `output`, `cache_read` and `thinking` and
nothing for `role`, `phase`, `cache_creat` and `subagent`. **An absence measured with a control that could have fired
is a reading; without one it is a broken search.**
📌 **The PHASE void costs nothing HERE and would cost something later:** level 6 is phase 1 only, so there is one phase
to attribute. **A level with two phases would need the meter to gain the key, not the reader to guess it.**
📌 **The ROLE void is the one that matters, and it is the exact axis that bit the Claude lane:** 30 of HC1's 45 cells
carry SONNET subagent records inside an OPUS cell, and pricing every bucket at the cell's own model over-stated 11 of
15 medians by 2–9 %, all one way. ⇒ **That error is UNAVAILABLE here — not because this lane is careful, but because
this lane has no roles to confuse.** ⚠️ **It is also unavailable to be CHECKED**, which is the same fact wearing its
other face.

---
# §2 · ⭐ THREE IDENTITIES, EACH HOLDING ON 36 OF 36 CELLS — THE INTERNAL CHECK THIS RECORD RESTS ON
```
  T             =  input + output + cache_read        36 of 36   (0 exceptions)
  vendor_total  =  input + output                     36 of 36   (0 exceptions)
  thinking      <= output                             36 of 36   (consistent with thinking being
                                                                  a component of output, never an addend)
```
⇒ 🔑 ***THE METER'S `T` AND THE VENDOR'S OWN TOTAL ARE DIFFERENT QUANTITIES AND DIFFER BY CACHE-READ ALONE*** — which
on this lane is **86.9 % of plain's total and 89.9 % of salt-diet's.** **So "tokens" names two numbers that differ by
roughly a factor of nine, and ⑯ is answered differently by each.** Both are published below; neither is derived from
the other by assumption.

---
# §3 · THE LANE, BY DIRECTION (all 36 cells, no exclusions)

```
  arm         n            T        input      output    cache_read    thinking   vendor total
  plain      18   69,999,404    8,342,898     847,906    60,808,600     593,980      9,190,804
  salt-diet  18  297,952,621   27,950,501   1,962,951   268,039,169   1,173,458     29,913,452
  LANE       36  367,952,025   36,293,399   2,810,857   328,847,769   1,767,438     39,104,256
```

---
# §4 · THE PREMIUM, UNDER EVERY DIRECTION — AND IT IS A CONTEXT COST

⛔ **TWO CELLS ARE OUT OF THE COST POOL, BOTH SALT-DIET, EACH FOR A DECLARED REASON:** `l6vgfs02` (VOID — the arm
was never delivered) and `l6vspt01` (TRUNCATED by the per-turn deadline; the helm ruling of 2026-09-11 puts its
cost figures out of any premium). **Poolable n = 18 plain, 16 salt-diet.**

```
  quantity                 plain median    salt-diet median    salt/plain
  T (in+out+cache_read)      3,988,132          15,921,781         3.992x
  input                        522,376           1,777,106         3.402x
  output                        51,563             108,857         2.111x
  cache_read                 3,343,759          14,076,560         4.210x
  thinking                      35,930              66,262         1.844x
  vendor total (in+out)        588,914           1,867,368         3.171x

  poolable n: plain 18 · salt-diet 16
```
⇒ ⭐ **THE PREMIUM IS LARGEST IN CACHE-READ (4.21×) AND SMALLEST IN OUTPUT (2.11×), WITH EVERY OTHER DIRECTION IN
BETWEEN.** ⇒ 🔑 ***THE SALT ARM'S COST IS PREDOMINANTLY A COST OF CARRYING CONTEXT, NOT OF GENERATING TEXT.*** The
method makes the subject READ more far more than it makes it WRITE more.
⭐⭐ **AND THIS REPRODUCES THE CLAUDE LANE'S SHAPE ON A DIFFERENT VENDOR, A DIFFERENT HARNESS AND DIFFERENT PROBLEMS:**
HC1 measured **T 2.168× against output 1.324×** — same ordering, same conclusion, independently arrived at.
⇒ **Two lanes now agree that the premium is a context cost. That is the strongest claim in this record**, and it is
the one a reader should take away rather than any single ratio.
⚠️ **The MAGNITUDES differ substantially between lanes (3.99× here vs 2.17× on HC1) and are NOT comparable:** different
vendor, different problems, different arm files, different n. **What is comparable is the ORDERING of the directions.**

---
# §5 · WHAT THE BUDGET UNIT ACTUALLY IS ON THIS LANE, AND WHY USD IS A VOID RATHER THAN A CALCULATION
⑯ says **USD derives from tokens, never the reverse.** On the Claude lane that derivation exists: published rates per
million tokens, per direction, per model. **On this lane it does not.** The agy lane runs on a SUBSCRIPTION with no
per-token price, so a USD figure here could only be manufactured by borrowing another vendor's rate card.
⇒ ⛔ **USD IS A DECLARED ABSENCE, NOT A NUMBER WE HAVE NOT GOT ROUND TO.** Borrowing a rate would invert ⑯ exactly:
it would derive tokens' meaning from a dollar figure that was itself invented.
✅ **THE UNIT THAT IS REAL HERE IS POOL PERCENTAGE**, and `gemini` measured it for this whole wave:
```
  the level-6 resumption   5 legs · 12 conditions · 36 cells · ~27 h wall
  agy WEEKLY pool          2 % -> 6 % used
  per-condition 5-hour peak  25 %   (paxos-flash-plain-bf, 00:58Z); every row read below-90
```
⇒ **36 cells cost about 4 points of a weekly pool.** ⚠️ **That is a reading of this wave, not a rate:** the 5-hour
window is the real constraint and a wave shaped differently would spend the same weekly total against a much tighter
peak. **Do not turn 4 points / 36 cells into a per-cell price.**

---
# §6 · PER-CELL, THE FULL TABLE (⑯ asks for per cell AND per lane)

```
  cell      arm        model            T        input     output   cache_read   thinking  note
  l6uspq01  plain      Pro     1,000,293     127,019    13,197      860,077      8,264  
  l6vblp01  plain      Flash   3,971,258     679,297    48,844    3,243,117     30,822  
  l6vblp02  plain      Flash   3,292,285     430,884    45,261    2,816,140     28,455  
  l6vblp03  plain      Flash   3,804,355     465,242    46,057    3,293,056     32,521  
  l6vbpp01  plain      Flash   7,992,405     824,754    80,381    7,087,270     58,160  
  l6vbpp02  plain      Flash   8,133,242     585,321    85,248    7,462,673     64,551  
  l6vbpp03  plain      Flash   6,177,131     520,790    78,794    5,577,547     57,306  
  l6vgfp01  plain      Flash   4,571,225     558,621    62,717    3,949,887     42,450  
  l6vgfp02  plain      Flash   4,244,069     523,961    54,282    3,665,826     39,339  
  l6vgfp03  plain      Flash   4,005,007     551,247    59,298    3,394,462     44,256  
  l6vgpp01  plain      Pro     1,311,863     183,693    11,290    1,116,880      4,984  
  l6vgpp02  plain      Pro     1,091,399     165,509    14,361      911,529      7,477  
  l6vgpp03  plain      Pro     1,232,089     152,915    17,908    1,061,266     11,508  
  l6vsfq01  plain      Flash   5,147,496     602,031    60,057    4,485,408     45,740  
  l6vsfq02  plain      Flash   4,980,956     772,609    61,170    4,147,177     44,810  
  l6vsfq03  plain      Flash   5,844,965     863,393    68,938    4,912,634     49,005  
  l6vspb01  plain      Pro     1,601,334     169,127    18,249    1,413,958     10,119  
  l6vspb02  plain      Pro     1,598,032     166,485    21,854    1,409,693     14,213  
  l6vbls01  salt-diet  Flash  15,083,897   1,707,686    93,585   13,282,626     59,943  
  l6vbls02  salt-diet  Flash  14,937,746   1,846,526    86,940   13,004,280     50,971  
  l6vbls03  salt-diet  Flash  13,783,042   1,513,397    89,458   12,180,187     54,523  
  l6vbps01  salt-diet  Flash  14,891,518   1,335,246   113,090   13,443,182     78,087  
  l6vbps02  salt-diet  Flash  18,713,325   2,109,908   136,704   16,466,713     88,378  
  l6vbps03  salt-diet  Flash  24,560,143   2,151,071   206,129   22,202,943    123,513  
  l6vgfs01  salt-diet  Flash  23,941,795   2,183,775   148,116   21,609,904    100,571  
  l6vgfs02  salt-diet  Flash     172,717     109,583     6,195       56,939      5,521  VOID(arm never delivered)
  l6vgfs03  salt-diet  Flash  35,553,998   3,050,981   203,993   32,299,024    134,541  
  l6vgps01  salt-diet  Pro     4,905,540     508,874    42,062    4,354,604     21,866  
  l6vgps02  salt-diet  Pro    16,759,665   1,942,643   107,083   14,709,939     50,009  
  l6vgps03  salt-diet  Pro    12,471,112   1,032,234    77,558   11,361,320     45,608  
  l6vsft01  salt-diet  Flash  13,941,899   1,088,070   115,298   12,738,531     72,908  
  l6vsft02  salt-diet  Flash  25,643,973   2,234,058   130,571   23,279,344     72,581  
  l6vsft03  salt-diet  Flash  18,215,862   1,941,036   110,631   16,164,195     81,119  
  l6vspt01  salt-diet  Pro    17,892,929   1,416,653   104,004   16,372,272     52,070  TRUNCATED(per-turn)
  l6vspt02  salt-diet  Pro     7,705,397     513,916    84,749    7,106,732     32,286  
  l6vspt03  salt-diet  Pro    18,778,063   1,264,844   106,785   17,406,434     48,963  
```

---
# §7 · WHAT THIS RECORD DOES NOT DO
1. **It prices nothing in dollars**, and §5 says why that is a refusal rather than an omission.
2. **It pools nothing with the Claude lane.** The ORDERING of the directions is compared; no magnitude is.
3. **It makes no p-value claim.** Medians over n = 16–18, with one arm spanning 4.9M–35.6M.
4. **It does not re-open level 6's scores.** Its two cost exclusions are declared and are not score exclusions:
   `l6vspt01` is SCORED (and FAILED) and only its cost figures are out of the pool.
5. ⛔ **It does not claim the agy lane is cheap.** 4 points of a weekly pool is a fact about a 36-cell wave on a
   pool that was nearly empty of other work. **The 5-hour peak of 25 % on a single condition is the number that
   would bind a busier week**, and it is the one to watch.

---
# §8 · PROVENANCE
```
  meters       <cell>/ctl/agy-meter-1.json, all 36, read READ-ONLY over ssh on the run box
  identities   T = in+out+cache_read · vendor_total = in+out · thinking <= out, each 36 of 36
  voids        censused over 31 distinct meter keys with positive controls that fired
  pool figures gemini's chain-close measurement (agy weekly 2 % -> 6 %; per-condition 5h peak 25 %)
  HC1 comparison  harness/systems-v3/RESULT-HC1-stage1-2026-09-16.md ADDENDUM 2, at origin/main
                  (merged cbfc290): T 2.168x · output 1.324x, both verified in that file
  population   the 36 of the level-6 manifest; ids cross-checked between conditions.tsv and cells.tsv
```
