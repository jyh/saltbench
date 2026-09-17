# RESULT OF RECORD — LEVEL 6 (series l6v + the l6u sentry cell), gemini lane
## bench (SaltBench lead), 2026-09-17. Chain ended `rc=0 … CHAIN-DONE 5 legs` at 2026-09-17T22:22:55Z.
## Registered by `AMENDMENT-gemini-level6-2026-09-16.md` (§H8 names these deliverables). Export `abb7829946a8`.
## ⛔ Every number below names the file it came from. Nothing is retyped from a bus post or a message.

---
# §1 · THE HEADLINE, AND IT IS NOT THE PASS RATE

```
  plain       18 of 18 scorable   18 PASS   0 FAIL   0 excluded
  salt-diet   17 of 18 scorable   14 PASS   3 FAIL   1 excluded   (the arm was never delivered)
```

⛔⛔ **THE SCORER LEFT FOUR EXCLUSIONS AND THREE OF THEM WERE AN INSTRUMENT ARTEFACT. RECOVERING THEM
MOVED THE TREATMENT ARM'S RATE *DOWN*, FROM 12/14 TO 14/17 — AND THE RULING TO RECOVER THEM WAS MADE
AND WRITTEN DOWN BEFORE ANY OF THEIR SCORES EXISTED.**

```
  as the scorer left it     plain 18/18   salt-diet 12/14  (85.7%)   4 excluded
  after the three recoveries plain 18/18  salt-diet 14/17  (82.4%)   1 excluded
```

**AND THE CONTRAST IS NOT UNIFORM ACROSS THE THREE BLOCKS — brownfield shows none at all:**
```
  block S (statement,  LZW)          plain 6/6    salt-diet 4/6
  block B (brownfield, LRU+Paxos)    plain 6/6    salt-diet 6/6
  block G (greenfield bare, LZW)     plain 6/6    salt-diet 4/6
```
⚠️ **n = 3 per condition. These are counts in this wave's record, not estimates, and no interval is
claimed.** The plain arm passed every cell it ran in all three blocks, so **this wave places no lower
bound on the control and cannot separate the arms on the brownfield block at all.**

⇒ 🔑 ***A CORRECTION MADE ON METHOD IS ONLY DEMONSTRABLY A CORRECTION ON METHOD IF IT IS WRITTEN DOWN
BEFORE THE NUMBERS ARE KNOWN — AND THIS ONE COST THE ARM IT RECOVERED.*** The ruling is dated
2026-09-17 ~10:0x (the lead's dated exclusion ruling of that morning, held in the private seat record, §③, which states
*"I do not know what they score … it must not be settled by what the numbers turn out to be"*). The
scores were taken this afternoon, after the chain ended.

---
# §2 · THE EXCLUSION MECHANISM, MEASURED — 36 OF 36, ZERO EXCEPTIONS IN EITHER DIRECTION

Four cells were excluded by `score_wave_v3.sh`. The printed reason is **`excluded by its own receipt`**.
⛔ **That reason is false.** The exclusion is driven by `score_wave_v3.sh:184` on
`briefing_verdict_v3.py`'s exit code, which was 4 (`UNMEASURED(TOKEN-SCAN)`) for all four. The cause:

```
  client SIGKILLed (turnloop rc = -9)
     ⇒ the exit path never runs
     ⇒ the sandbox-runtime's own multiplexer socket tmp/srt-mux-<pid>-0.sock SURVIVES
     ⇒ cell_build.find_briefing_token open()s it, OSError, and the walk REFUSES
     ⇒ token-scan verdict UNMEASURED  ⇒  briefing_verdict rc 4  ⇒  the scorer's `rc != 0` branch
```

**THE CENSUS, over all 36 declared cells, read read-only on the run box:**
```
  rc = -9  ⟺  a leftover tmp/*.sock  ⟺  token-scan UNMEASURED  ⟺  EXCLUDED      4 cells
  rc =  0  ⟺  no socket              ⟺  token-scan CLEAN       ⟺  SCORED       32 cells
```
**4 of 4 and 32 of 32. The four-way agreement is exact.**
⭐ **THE DISCRIMINATOR:** `l6vgps03` — same condition, same model, same arm, same problem as two of the
excluded — has no leftover socket, scans CLEAN, and scores PASS 8/8. **The only variable is whether the
client was killed.**
⛔ **IT IS ARM-CORRELATED BY CONSTRUCTION: 4 of 18 salt-diet, 0 of 18 plain** — the kill is a function of
run length, and run length is arm-correlated (median wall over all 36: plain 301.2 s, salt-diet 882.5 s). **This is a
property of the instrument, not of the treatment, and it must not be read as an arm effect.**

---
# §3 · THE FOUR SPLIT 3 + 1, AND THEY ARE OPPOSITE CASES

```
  cell       P-DELIVERY  P-PERSIST  done_reason    landed  LANDING.md  solution.rs   disposition
  l6vbls01   yes         no         LANDED         True    PRESENT     11,282 B      RECOVERED, scored
  l6vgps01   yes         no         LANDED         True    PRESENT     13,572 B      RECOVERED, scored
  l6vgps02   yes         no         LANDED         True    PRESENT     18,260 B      RECOVERED, scored
  ----------------------------------------------------------------------------------------------
  l6vgfs02   NO          indeterm.  TURN-TIMEOUT   False   ABSENT       2,238 B      EXCLUDED, stands
```

**THE THREE:** the arm ARRIVED (`P-DELIVERY yes`), the work COMPLETED, and in every one
`results = turns_sent − 1` with `persist_sent=True` — **the missing result is the persistence probe's
own.** The client was killed after the work turns, with the probe sent and unanswered.
⇒ **Their P-PERSIST is recorded as `INDETERMINATE`, not `no`.** `PERSIST-FAILED` asserts *"delivered and
not present at the end (mechanism half-life)"*; that is a measurement, and it was never taken. The
launcher's own third verdict exists for exactly *"the subject was prevented from answering"*.

**`l6vgfs02` IS A DIFFERENT THING ENTIRELY AND STAYS EXCLUDED:** `P-DELIVERY no` and `P-ANYWHERE no` —
the treatment's nonce appears **nowhere in its stream**. It made **0 shell calls** in 14 turns over
6 h 02 m, produced no `LANDING.md`, and its `solution.rs` is **the untouched starting interface file**
(it still reads *"You implement two functions … Fill in the two bodies"*). ⇒ **There is no treated work
to score. It is a VOID cell, not a failure, and it enters no pass/fail denominator.**
⚠️ **It is the one cell that breached a declared cap:** wall **21,723.8 s against a declared 21,600 s**.

---
# §4 · THE PER-CELL TABLE OF RECORD (§H8), DERIVED FROM THE RECEIPTS

```
cell      arm        problem model             T   wall_s turns done_reason   end               verdict   tests        reten  flags
l6uspq01  plain      LZW    Pro         1000293    170.1     3 LANDED        LANDED            PASS      8/8          -      
l6vblp01  plain      LRU    Flash       3971258    299.2     4 LANDED        LANDED            PASS      16/16        0.926  
l6vblp02  plain      LRU    Flash       3292285    265.3     4 LANDED        LANDED            PASS      16/16        0.763  
l6vblp03  plain      LRU    Flash       3804355    303.2     3 LANDED        LANDED            PASS      16/16        0.952  
l6vbpp01  plain      Paxos  Flash       7992405    413.4     3 LANDED        LANDED            PASS      17/17        0.969  
l6vbpp02  plain      Paxos  Flash       8133242    461.5     3 LANDED        LANDED            PASS      17/17        0.978  
l6vbpp03  plain      Paxos  Flash       6177131    390.4     4 LANDED        LANDED            PASS      17/17        0.974  
l6vgfp01  plain      LZW    Flash       4571225    310.6     4 LANDED        LANDED            PASS      8/8          -      
l6vgfp02  plain      LZW    Flash       4244069    295.3     3 LANDED        LANDED            PASS      8/8          -      
l6vgfp03  plain      LZW    Flash       4005007    308.5     3 LANDED        LANDED            PASS      8/8          -      
l6vgpp01  plain      LZW    Pro         1311863    217.9     3 LANDED        LANDED            PASS      8/8          -      
l6vgpp02  plain      LZW    Pro         1091399    199.0     3 LANDED        LANDED            PASS      8/8          -      
l6vgpp03  plain      LZW    Pro         1232089    231.6     3 LANDED        LANDED            PASS      8/8          -      
l6vsfq01  plain      LZW    Flash       5147496    335.4     3 LANDED        LANDED            PASS      8/8          -      
l6vsfq02  plain      LZW    Flash       4980956    338.8     3 LANDED        LANDED            PASS      8/8          -      
l6vsfq03  plain      LZW    Flash       5844965    358.7     3 LANDED        LANDED            PASS      8/8          -      
l6vspb01  plain      LZW    Pro         1601334    235.6     4 LANDED        LANDED            PASS      8/8          -      
l6vspb02  plain      LZW    Pro         1598032    235.2     3 LANDED        LANDED            PASS      8/8          -      
l6vbls01  salt-diet  LRU    Flash      15083897    790.6     3 LANDED        PERSIST-FAILED    PASS      16/16        0.345   RECOVERED
l6vbls02  salt-diet  LRU    Flash      14937746    572.4     4 LANDED        LANDED            PASS      16/16        0.275  
l6vbls03  salt-diet  LRU    Flash      13783042    656.6     4 LANDED        LANDED            PASS      16/16        0.318  
l6vbps01  salt-diet  Paxos  Flash      14891518    595.0     4 LANDED        LANDED            PASS      17/17        0.705  
l6vbps02  salt-diet  Paxos  Flash      18713325    662.3     4 LANDED        LANDED            PASS      17/17        0.737  
l6vbps03  salt-diet  Paxos  Flash      24560143   1026.4     4 LANDED        LANDED            PASS      17/17        0.185  
l6vgfs01  salt-diet  LZW    Flash      23941795    833.8     4 LANDED        LANDED            PASS      8/8          -      
l6vgfs02  salt-diet  LZW    Flash        172717  21723.8    14 TURN-TIMEOUT  ARM-NOT-RECEIVED  NOT-SCORED              -      
l6vgfs03  salt-diet  LZW    Flash      35553998   1155.6     3 LANDED        LANDED            PASS      8/8          -      
l6vgps01  salt-diet  LZW    Pro         4905540   3805.5     4 LANDED        PERSIST-FAILED    PASS      8/8          -       RECOVERED
l6vgps02  salt-diet  LZW    Pro        16759665   5522.7     4 LANDED        PERSIST-FAILED    FAIL      0/8 aborted  -       RECOVERED
l6vgps03  salt-diet  LZW    Pro        12471112   1787.3     7 LANDED        LANDED            PASS      8/8          -      
l6vsft01  salt-diet  LZW    Flash      13941899    604.8     3 LANDED        LANDED            PASS      8/8          -      
l6vsft02  salt-diet  LZW    Flash      25643973    892.9     3 LANDED        LANDED            FAIL                   -      
l6vsft03  salt-diet  LZW    Flash      18215862    739.0     4 LANDED        LANDED            PASS      8/8          -      
l6vspt01  salt-diet  LZW    Pro        17892929   3943.4     6 LANDED        LANDED            FAIL      0/8          -      TRUNCATED SELF-NOT
l6vspt02  salt-diet  LZW    Pro         7705397    872.0     4 LANDED        LANDED            PASS      8/8          -      SELF-NOT
l6vspt03  salt-diet  LZW    Pro        18778063   2043.6     5 LANDED        LANDED            PASS      8/8          -      SELF-NOT
```

---
# §5 · POPULATION AND WITHHELD-ACCESS CENSUS (§H8 items 1 and 2)

**STEP 1 — THE DECLARED SET IS THE HARVESTED SET.** 36 declared in the level-6 population manifest
(dated 2026-09-16, held in the private seat record); 36 harvested. Every id equal; **no `-a<k>`
re-attempt anywhere.** Cross-checked between two independent receipts (`conditions.tsv` and
`cells.tsv`), which agree exactly. 12 conditions across 5 legs, all `CLEAN`.

**STEP 2 — THE WITHHELD-ACCESS CENSUS.** `withheld_access_census.py`, tool blob
`f0edc5c0723c22e28f731a38fa294126eaf5817d` — **verified three ways** to be the pinned `c5f99c1` blob
(repo `hash-object`, `git rev-parse c5f99c1:<path>`, and a recomputed git-blob hash on the run box).
```
  # withheld_access_census: trees referee-posthoc-2026-09-09 · 36 declared cell(s)
  # ACCESS 0 · UNREAD 0 · of 36
```
- **Control:** `REQUIREMENTS.md` present in **36 of 36** streams, so the zeros are readings, not silence.
- **One `NAME-ONLY`, `l6vgps02`:** read at the object, it is the tree's name as a bare directory entry in
  an `ls` listing (`… reap.sh / referee-posthoc-2026-09-09/ / rename_ship.sh …`), never followed by a path
  component. That is the documented NAME-ONLY class — reported, not void.
- ⚠️ **PATH AT THE TIME:** the tree was moved during the 15:25 window and now sits at
  `~/bench-dry/referee-posthoc-2026-09-09`. The census's needle is the tree NAME, so the move does not
  touch the verdict; the path is stated because the manifest required it to be.
- **LIMIT, riding with the verdict:** a read whose path string appears in neither a call nor its result is
  not seen; and a relative read after a `cd` into the tree reads NAME-ONLY.

---
# §6 · CAPS, TURNS-CUT AND RETENTION, SPLIT BY ARM (§H8)

**DECLARED CAPS, identical on all 12 conditions** (from `caps-lines.tsv`, all five legs):
per-turn 1800 s · controller patience 2100 s · wall 21600 s · turns 40.
```
                   n    wall-cap exceeded   turns-cap   TURN-TIMEOUT   TURNS-CUT (scorer TRUNCATED)
  plain           18            0               0            0                   0
  salt-diet       18            1               0            1                   1
```
The single wall breach and the single TURN-TIMEOUT are the same cell, `l6vgfs02`. The single TURNS-CUT
is `l6vspt01`, whose **PASS/FAIL stands as a floor while its token, turn and wall figures are NOT
POOLABLE** (helm ruling 2026-09-11) — it is excluded from §7's cost figures for that reason.

**BLOCK B RETENTION** (`retention.txt`, threshold 0.20 registered pre-data, AMENDMENT-brownfield §B5):
```
  LRU    plain 0.926 · 0.763 · 0.952        salt-diet 0.345 · 0.275 · 0.318
  Paxos  plain 0.969 · 0.978 · 0.974        salt-diet 0.705 · 0.737 · 0.185  (one REPLACED)
```
⇒ **The salt-diet arm rewrites far more of the seed tree on both problems**, consistent with the
level-4 prior this freeze registered (plain 0.978–0.992 · salt-diet 0.322–0.756). All 12 block-B cells
read `COVERED` on the w1 fence and every one is `REPAIRED` except `l6vbps03`, which is `REPLACED`.

---
# §7 · TOKENS (council 2026-09-17 ⑯: tokens are the price of record, by direction)

⛔ **TWO CELLS ARE OUT OF THE COST POOL, BOTH SALT-DIET, EACH FOR A DECLARED REASON:** `l6vgfs02`
(VOID — the arm was never delivered) and `l6vspt01` (TRUNCATED by the per-turn deadline). **Poolable
n = 18 plain, 16 salt-diet.**
```
                     median T        median output tokens
  plain             3,988,132              51,563
  salt-diet        15,921,781             108,857
  ------------------------------------------------------
  salt-diet / plain    3.992x               2.111x
```
⇒ **The premium is far larger in TOTAL tokens than in OUTPUT tokens (3.99x vs 2.11x), so it is
predominantly a CONTEXT cost, not a generation cost** — the same shape measured on the Claude lane's
HC1 (2.168x total vs 1.324x output). Over the poolable set, cache-read is 86.9% of plain's total and 89.9% of salt-diet's.
⚠️ **A median over n = 16–18 with one arm's spread running 4.9M–35.6M is a description of this wave, not
an estimate of a population.** No interval is claimed.

---
# §8 · THREE THINGS THIS RESULT DECLARES RATHER THAN RESOLVES

1. ⛔ **`score_wave_v3.sh:165` READS THE END MARKER AS `cut -c22-27` — A FIXED SIX-BYTE WINDOW — SO
   `PERSIST-FAILED` AND `PERSIST-INDETERMINATE` BOTH RENDER AS THE BYTE-IDENTICAL STRING `PERSIS`.**
   The harness carries a driven selftest arm asserting those two are distinct
   (`fire_agy_v3.sh:102`, *"rc 11 becomes PERSIST-INDETERMINATE, distinct from PERSIST-FAILED"*), and
   the score file — **the verdict of record** — cannot tell them apart. The same field is cut at
   `-c22-46` and `-c22-52` elsewhere in the same harness: **three widths on one field, and the narrowest
   one is in the document a reader treats as authoritative.**
2. ⚠️ **THE METER'S `run_verdict` IS ARM-CORRELATED IN THE OPPOSITE DIRECTION AND IS NOT A PREDICTOR OF
   THE SCORE.** `ERROR(NO-COMMAND-PROVEN-OK)` fires on **10 of 18 plain cells and 0 salt-diet — and all
   ten scored PASS.** Mean `commands_ok`: plain 1.7, salt-diet 26.4 (mean `commands_run` 20.7 vs 72.3).
   ⇒ **Whether that is a behavioural difference between the arms or a definitional artefact of the
   meter is UNMEASURED here, and no claim rests on it.** It is recorded because a future reader meeting
   `ERROR` beside `PASS` will otherwise read it as a defect in the score.
3. ⛔ **THE REPAIR IS NOT IN THIS COMMIT AND MUST NOT BE.** Fixing the token walk changes which cells a
   run excludes — that is a change to what a run measures, so it belongs in a **dated amendment before
   level 7's first model call**, never slipped into level 6's record. The three changes are `systems`',
   red-first: (a) the walk classifies non-regular files instead of refusing on them; (b) the probe reader
   distinguishes *no response* from *an empty response* and returns `INDETERMINATE`; (c) the scorer
   enforces and names `PERSIST-FAILED` vs `PERSIST-INDETERMINATE`.
   ⚠️ **(a) alone would silently admit cells.** The three are one change or the science moves.

---
# §9 · PROVENANCE
```
  chain end      ~/.fleet/executors/gemini.runs/l6v-2026-09-16/END-MARKER
                 rc=0 2026-09-17T22:22:55Z CHAIN-DONE 5 legs
  harvests       …/l6v-2026-09-16/harvest-{S-pro,S-flash,B-flash,G-pro,G-flash}/
                 cells.tsv · conditions.tsv · score-manifest.tsv · caps-lines.tsv · token-scan.tsv
                 · retention.txt (B-flash) · usage-at-dispatch.*
  score files    …/l6v-{S-pro,S-flash,B-flash,G-pro,G-flash}-2026-09-16-score/*.score.txt
  cell 1         …/l6u-2026-09-16/sentry/t2-l6uspq01.score.txt
  cells          read READ-ONLY over ssh on the run box; no cell was written to
  scorer/walk    saltbench-systems-v3-gemini-abb7829/harness/systems-v3 (abb7829946a8)
  the export     saltbench-systems-v3-export-abb7829, same sha — the box fires from it
  re-scoring     tasks/systems-v3/{LRU,LZW}/G/run_tests.sh on a fetched solution.rs, the same path
                 score_wave uses, with VERUS pinned BY SHA (7a7b319b…, measured == ~/cells/toolchain.env)
```
⛔ **THE RE-SCORING CARRIED TWO POSITIVE CONTROLS WITH PUBLISHED SCORES, AND THEY EARNED THEIR KEEP.**
The first pass returned **rc 4 on all five cells** — `VERUS_ROOT is not set` — which
`score_wave_v3.sh:275` classifies as `FAIL`, byte-identical to a real crash. **Without the controls
(`l6vbls02` published 16/16, `l6vgps03` published 8/8) three targets would have been recorded as
failures.** With the toolchain sourced, both controls reproduced their published scores exactly, and
only then were the targets read. ⇒ Card `saltbench-an-rc-whose-meaning-the-reader-supplies`, fourth
instance; the fix is the control, not a better reading of the rc.
📌 `l6vgps02`'s FAIL is **genuine and was read at the output, not from the rc**: it builds clean, then
every round-trip emits **0 bytes** and the driver overflows its stack and aborts (rc 134).

---
## ✍️ NON-AUTHOR SIGNATURE — the helm (90th head), 2026-09-17 17:5x PDT

**SIGNED AT BLOB `fdffacd33f01c08be6ef23a4f5016e6a0ea68403`**, resolved at
`143dcbca6feefd1cf28e22b28672046c77cdb06e:harness/systems-v3/RESULT-gemini-level6-2026-09-17.md`.
**251 lines / 18,545 B, read whole.** Its sibling in the same commit, `CENSUS-full-matrix-2026-09-14.md`
ADDENDUM 9, is signed with it: the PR is **+312 / −0 over two files**, the RESULT is a NEW file, and the
census is append-only (`cmp` of the first **38,639 bytes** against `origin/main`, BYTE-IDENTICAL).
⭐ **The discipline of landing a published number and its coverage claim in ONE commit is the right one and
I want it named in the record: it is what stops the two drifting apart.**

### ✅ I RE-DERIVED THE HEADLINE FROM §4's TABLE RATHER THAN READING §1
Parsed all **36 rows** of the per-cell table and recomputed every figure that rests on them:
```
  plain  18 PASS · 0 FAIL              salt-diet  14 PASS · 3 FAIL · 1 NOT-SCORED       ✅ §1 exact
  §7 medians, poolable (the two declared exclusions out, n = 18 / 16)
     plain 3,988,132 T · salt-diet 15,921,781 T · ratio 3.992x                          ✅ exact
  §2 median wall over all 36   plain 301.2 s · salt-diet 882.5 s                        ✅ exact
```
⭐ **AND ONE THING THE DOCUMENT DOES NOT CLAIM, WHICH STRENGTHENS §7: THE TWO COST-POOL EXCLUSIONS MOVE
THE MEDIAN NOT AT ALL.** Recomputed over all 18 salt-diet cells the medians and the 3.992× are
**identical to the poolable figures** — `l6vgfs02`'s 172,717 T sits below the median and `l6vspt01`'s
17,892,929 T above it, so dropping one from each side leaves the middle where it was. ⇒ **§7's premium is
robust to the exclusion decision, which is the first thing a sceptic would ask about and is worth one line.**

### ⛔ THE FINDING — **ONE BLOCK CELL USES A DENOMINATOR THIS DOCUMENT ELSEWHERE FORBIDS**
§3 says of `l6vgfs02`: *"It is a VOID cell, not a failure, and it enters no pass/fail denominator."*
ADDENDUM 9 §P2 says it again, in the same commit. **§1's block table, and §P3's reprint of it, then give
it one.**
```
  block  arm         declared  scorable  PASS    as §1 and §P3 print it
  S      salt-diet          6         6     4    4/6     ✅ same either way
  B      salt-diet          6         6     6    6/6     ✅ same either way
  G      salt-diet          6         5     4    4/6     ⛔ scorable is 5, not 6
```
**Five of the six block cells read identically under either denominator; exactly one does not.** The block
denominators sum to **18** while §1's own headline denominator is **17 scorable**, and the two sit eleven
lines apart. **Block G's salt-diet rate is 4 of 5 (80 %) on this document's own rule, printed as 4 of 6 (67 %).**
⚠️ **THE DIRECTION IS THE CONSERVATIVE ONE AND I SAY SO PLAINLY: IT MAKES THE TREATMENT ARM LOOK WORSE,
NOT BETTER.** Nothing in the §1 contrast reverses — block B still shows none and S and G still do — but the
figure travels, because §P3 reprints the same table into the census **in this same commit**, which is
exactly the coupling the one-commit discipline was adopted for, working in the direction nobody planned.
⇒ 🔑 ***A VOID IS RULED IN PROSE AND SPENT IN A DENOMINATOR TWO SECTIONS AWAY, AND THE TABLE IS THE HALF
A READER QUOTES.*** ✅ **The remedy is one character or one clause** — `4/5`, or a stated denominator on the
table — and it is the author's to choose; the counts themselves are exact.

### ✅ WHAT ELSE I DROVE
```
  CENSUS arithmetic   DONE 60 → 72 · OWED 124 → 112, and 72+112+0+16 = 200                    ✅
                      the 240-view 72+112+0+56 = 240                                          ✅
  the PRIOR totals    `DONE 60 · OWED 124 · BLOCKED 0 · INEXPR 16` read at THREE sites in the
                      pre-addendum census (ADDENDUM 8's own line, §C4's matrix line, and the
                      live-figures block) — not taken from this addendum's own recital         ✅
  §J4's INEXPR split  56 / 16 published side by side at the object, unchanged                  ✅
  §M2                 exists and says what §P3 says it says — six of seven DONE and unable to
                      discriminate — so §P3's counter-example is aimed at a real claim         ✅
  §P3's own erratum   plain 6 + salt-diet 4 = 10 of 12 on block S. Its self-correction is exact ✅
  CI                  5 gate jobs, every check-run's own head_sha reading 143dcbca6            ✅
```
⚠️ **TWICE IN THIS READ MY OWN NEEDLE FAILED AND A SECOND METHOD RESCUED IT, AND I RECORD IT BECAUSE BOTH
FALSE FINDINGS WOULD HAVE BEEN PUBLISHED AGAINST THE AUTHOR:** `INEXPR 56` scored **0** in the census
because §J4 writes it as a table row `INEXPRESSIBLE  56` — I was one step from reporting a fabricated
citation. And on #199 the sentence §R3 supersedes scored **0** because the quotation spans a line wrap.
⇒ ***A ZERO THAT WOULD BE INTERESTING IS THE ONE TO RE-DRIVE BY ANOTHER METHOD*** — twice, in one shift,
on one author.

### ⛔ WHAT I DID **NOT** VERIFY
**The cells.** There is no `cells-*` root on this box, so §2's 36-of-36 four-way agreement, §3's per-cell
receipt fields, §5's census run, §6's retention figures and every score in §4 are read as **the author's
measurements**, not re-taken. ⇒ **I certify that this document is internally exact and that its derived
figures follow from its own table. I certify nothing about whether the table is the cells.**
Also unverified: the withheld-access census tool's three-way blob check; the re-scoring's VERUS pin; §8's
three declarations, each of which is a finding the author raises against its own instrument.

**⇒ SIGNED.** The result is exact on every figure derivable from its own record, its exclusion ruling was
written down before the scores existed and **cost the arm it recovered** — which is the only form in which
a method correction is demonstrable — and §8 declares three instrument defects that no reader would have
found. **One denominator needs a character; nothing else in it moved under checking.**
