# PRE-REGISTRATION — CAMPAIGN MATRIX #1 (OPUS), REGISTERED BEFORE CELL 1

bench, 2026-09-08, desk row HV. **Written before any cell of this matrix is built or fired, including
the 3-cell smoke.** Stage 1's defect was that four of five orderings encoded a threshold and none
encoded what the design could resolve. **Every clause here carries the sampling behaviour of its own
statistic at the n actually used**, and that is the entire reason this file exists separately from the
price.

## 1. THE DESIGN
**5 problems × 4 arms × n = 3 = 60 cells**, Opus, greenfield.
    problems  Crc32 · FreeList · LRU · LZW · Paxos   (all five frozen in the export, measured)
    arms      plain-bare · diet-bare · plain-STATEMENT · diet-STATEMENT
**The arm letters are resolved from the receipts, not guessed:** the Captain's *(d)* is **plain+
STATEMENT** and *(e)* is **diet+STATEMENT**. ⛔ **placebo is NOT one of the four** — it would be a fifth.
⛔ **Every headline carries the word DIET: this matrix does not measure the un-dieted salt method.**

## 2. THE PRIMARY READING — THE CROSS-PROBLEM SIGN TEST, AND ONLY 5/5 COUNTS
`premium(P) = median(diet-bare, P) / median(plain-bare, P)`, one per problem.
**H0: each problem's premium is equally likely either side of 1.0.**

    >= 5 of 5 premiums > 1   p = 0.0312   ** the ONLY significant outcome **
    >= 4 of 5                p = 0.1875   NOT a positive result
    >= 3 of 5                p = 0.5000

⇒ ⛔ **REGISTERED IN ADVANCE, AND THIS IS THE POINT OF REGISTERING IT: 4-of-5 IS NOT A RESULT.** After
the fact it reads as *"nearly"*; before the fact it is p = 0.19. **If four problems show a premium and
one does not, the verdict word is UNRESOLVED and the report says so in the headline.**
⇒ **k = 5 is the smallest problem count that can reach .05 at all** — stage 1's k = 2 topped out at
p = 0.25, which is why this matrix exists.

## 3. THE GOLD — (d) vs (e), SAME ARITHMETIC, REGISTERED THE SAME WAY
*"If (e) beats (d), THE METHOD IS THE STATEMENT."* Across 5 problems that is **5 paired signs**:
**5/5 → p = 0.0312; 4/5 → p = 0.1875, not a result.** Reported BY NAME, whichever way it falls.

## 4. WHAT THIS DESIGN CANNOT DO, FIXED NOW SO NO NUMBER ESCAPES IT
**n stays 3 per condition, so the resolvable premium floor is 2.0072×** (pooled sd(ln cost) 0.30458,
k = 7.8489). Stage 1's premiums were 1.1655–1.3560, **far below it.**
⇒ 🔑 **EVERY PER-PROBLEM MAGNITUDE IS UNRESOLVED BY CONSTRUCTION. The design is powered on SIGN across
problems (G1) and unpowered on MAGNITUDE within one (G2).**
⇒ ⛔ **The headline may read "salt costs more on all five problems, p = 0.031". It may NOT read "salt
costs 1.36×"** — that number, if quoted at all, appears only with the floor and n beside it (G3).

## 5. THE SPREAD CLAUSE — REGISTERED WITH ITS NULL, WHICH IS WHY STAGE 1's WAS UNREADABLE
At n = 3 with the pooled sd, **a PERFECTLY HOMOGENEOUS condition crosses a 1.5× max/min spread with
probability 0.614.** This matrix has **20 conditions**, so **~12 are EXPECTED to "refute" by sampling
alone.**
⇒ ⛔ **REGISTERED: the COUNT of refuting conditions is not a reading, and WHICH ones refute is not a
location.** Spread is reported as a design property, never as a per-condition verdict. **Without this
clause someone reports "12 of 20 conditions refuted" as a finding; stage 1 published exactly that shape
at 2-of-4.**

## 6. ANCHOR COMPARISONS ARE FORBIDDEN AT n = 1
Stage 1's O4 compared a median-of-3 against two n = 1 anchors and **refutes 7 times in 10 under NO
effect** (exact, distribution-free). ⇒ **No clause in this matrix compares a condition median to a
single cell.** Any anchor used for context is quoted with its n and carries no verdict.

## 7. VERDICT VOCABULARY — FOUR WORDS, NOT TWO
`HOLDS` · `REFUTED` · **`UNRESOLVED`** (the design could not answer) · **`VOID`** (a component premium
≤ 1, so a generalisation reading is not merely wrong but unreadable). ⇒ **A test with two outcomes for
a three-outcome world reports the missing one as whichever of its two is nearer** — stage 1's O2 said
HOLDS because it had no way to say *I could not answer*.

## 8. STOP LIST — EVERY ENTRY SORTED, PER THE STANDING LAW
**FAULT (may halt the run):** a cell that cannot build · the fence failing its drive · a per-cell HOME
or config dir carrying ANY global instruction file (the guard is a precondition, not hygiene) · quota
exhaustion without a successful account rotation · a harvest that cannot attribute a cell to a problem.
**RESULT (reported, run continues):** any premium below 1 · any spread above 1.5× · a condition median
outside any expectation · the gold pair falling either way · 4-of-5 on either sign test.
⇒ 🔑 **A FAILED PREDICTION IS THE EXPERIMENT WORKING. Re-cut a stop, never waive one.**

## 9. WHAT IS FIRED, IN ORDER
1. **3-cell smoke** — one `plain-bare` on FreeList, LRU, Paxos, the three that have never produced a
   cell. **This pre-registration binds the smoke too.**
2. **60 cells at 4-wide**, on systems' switch-on-cap receipt.
3. Report by cross-problem consistency and the gold pair, by name, G1/G2/G3 on every line.

---

## 10. APPENDED BEFORE THE SMOKE RUNS — THE SMOKE CELLS ARE MATRIX CELLS
The three smoke cells are `plain-bare` on FreeList, LRU and Paxos — **three of the matrix's own 60.**
Registered now, before any of them has produced an outcome:
**They COUNT as n=1 of the n=3 for their conditions.** They are not a separate set and are not re-run
for having been fired first.
⛔ **And the discipline that makes that legitimate:** if a smoke cell FAILS TO LAND, its condition is
completed by firing the remaining cells **exactly as it would have been anyway** — a landed cell is
never discarded, and a failed one is never quietly replaced. **Re-firing a condition because its first
cell displeased me is selection on outcome, and it is forbidden here by name.**
📌 The build already answered the smoke's primary question at zero model spend: **all three never-run
problems BUILD, TRUST and pass `--check` clean** (`ae304f63` FreeList · `a69e9131` LRU · `b7537006`
Paxos). What the launch adds is whether they LAND — the end-to-end half the build cannot speak to.

---

## 11. THE CLIENT PIN — REGISTERED BEFORE ANY CELL OF THIS MATRIX HAS RUN
    installed on the run box:  2.1.251 · 2.1.259 · 2.1.261 · 2.1.263
    ~/.local/bin/claude resolves to:  2.1.263        <- what a PATH lookup would have fired
    stage 1 fired on:                 2.1.259        <- read from the stage-1 cells' own launch logs
**REGISTERED: matrix #1 fires on `CLAUDE_BIN=/Users/jyh/.local/share/claude/versions/2.1.259`**, the
version stage 1 used, verified present and executable.
**Why the older pin and not the newest:** this file's floor of **2.0072×** and the pooled
`sd(ln cost)=0.30458` are derived from **stage-1 dispersion measured on 2.1.259**, and the campaign's
published premiums (1.3560×, 1.1655×) come from that client. **Firing the matrix on 2.1.263 would put
an uncontrolled variable between stage 1 and the matrix** — and the first comparison anyone will make
is matrix-vs-stage-1. The matrix is internally comparable on either pin; **only this pin keeps it
comparable to the numbers already published.**
⛔ **This is a REGISTERED CHOICE, not a default, and it has a cost I am naming: the matrix measures a
client two versions behind current.** If the council prefers the current product, that is a re-cut of
this clause **before** the fire, not a reading of it after.
⭐ **What caught it:** the launcher HOLDs with *"the client is named by its ABSOLUTE versioned path (the
freeze's pin), never resolved from a PATH or a symlink."* ⇒ 🔑 **A SYMLINK FOLLOWS THE NEWEST INSTALL,
SO RESOLVING A CLIENT FROM `PATH` SILENTLY RE-PINS A SCORED RUN EVERY TIME THE VENDOR SHIPS.** The
refusal cost three boot attempts and **zero model spend** — the HOLD fires before the client launches.

---

## 12. THE SMOKE RAN ON A DIFFERENT EXPORT FROM THE REMAINING 57 — DECLARED BEFORE THE FIRE
    3 cells (FreeList · LRU · Paxos, plain-bare)   export 5d51f17
    the remaining 57                                export eee8d83
`eee8d83` adds five repairs `5d51f17` lacks: the tmux launch carrier, `CLAUDE_CONFIG_DIR` on that same
carrier, `canary.py`'s shared baits, `fence-hook.sh`'s uncapped audit line, and a studio_export fix.
**REGISTERED JUDGEMENT: the three stay in the matrix as n=1 of their conditions, for COST.**
**Why the difference does not touch cost:** every repair is to the AUDIT, CARRIER or CANARY path. **None
changes the task, the arm, the prompt, the caps or anything the subject can do** — they change what is
RECORDED about a run, not what the run is. The deadman miswiring is a backstop; `CLAUDE_CONFIG_DIR`
resolved to the same value for all three (measured); the canary and audit repairs alter logging only.
⛔ **WHAT THE DIFFERENCE DOES TOUCH, AND IS THEREFORE NOT POOLED: the CONTAINMENT record.** These three
cells' escape verdicts are **WITHDRAWN**, not merely caveated — their canary nonces may be stale and
their audit lines may be torn, both of which fail toward CLEAN. **They contribute a PRICE and no
containment reading**, and any containment claim for this matrix rests on the 57.
⛔ **AND I AM NOT RE-FIRING THEM TO TIDY THIS.** Re-firing would give 6 cells for 3 conditions and a
choice of which 3 to keep — **which is selection on outcome, forbidden by §9 of this file.** The
declaration is the honest instrument; a cleaner-looking dataset bought by choosing among draws is not.
📌 **Cost of the disclosure, stated: 3 of 60 cells carry a footnote the other 57 do not.** I would rather
publish that sentence than a matrix that looks uniform because I discarded the evidence that it wasn't.

---

## 13. ⛔⛔ §12 IS WRONG IN ITS CENTRAL FACT — CORRECTED WITHIN THE HOUR, BEFORE THE 57 FIRE
§12 says the three smoke cells "ran under `5d51f17`." **They did not.** Measured at the object after
`systems` warned me off re-cutting `_bin`:

    ~/cells/_bin/cell-claude.sh   sha256/16 62e9daef8f4dba98   == …-export-50ea7f4's copy
    5d51f17's cell-claude.sh      sha256/16 5b41846b3e742c64   <- the file I verified
    the FAULT-class content guard: 0 occurrences in _bin's launcher, 1 in 5d51f17's
    _bin populated 2026-09-07 21:03 — it has pointed at 50ea7f4 the whole time

⇒ **The WATCHER ran from `5d51f17` because I named that path explicitly; the LAUNCHER came from `_bin`,
which is `50ea7f4`. Two exports in one cell.** ⇒ ⛔ **THE GUARD I RULED A FAULT-CLASS PRECONDITION OF
THE FIRE DID NOT RUN ON THESE THREE CELLS**, and my verification of it was a reading of a file that was
never executed.
⇒ 🔑 ***A COMMIT IS NOT A PUSH; A PUSH IS NOT AN EXPORT; **AND AN EXPORT IS NOT THE RUNTIME.** THE
RUNTIME IS `_bin`.*** I sharpened that law twice today and stopped one layer short of the layer that
actually executes. **Checking the export was the right act on the wrong tree.**
📌 **What this does NOT change:** the three cells' PRICES stand — cost is the subject's work, and both
launchers run the same client with the same caps on the same task. **What it changes is that their
containment posture is now unverified on a THIRD axis** (guard absent), on top of the canary and audit
ones. Their escape verdicts were already withdrawn; **this widens the reason, not the conclusion.**
📌 **And the risk did not materialise, measured independently: 0 of 14 config dirs on the run box carry
any global instruction file.** The guard had nothing to catch. **That is luck, not design, and it is
recorded as luck.**
⛔ **BINDING ON THE 57: `_bin` MUST BE RE-CUT TO `eee8d83` AND THE LAUNCHER'S SHA VERIFIED FROM `_bin`
ITSELF — not from the export — before the first of them fires.** The receipt for this matrix quotes the
`_bin` sha, because that is the only sha that describes what ran.

---

## 14. THE RUNTIME FOR THE REMAINING 57, AND A REFUSAL I DECLINED TO OVERRIDE
`cells_bin.sh` **REFUSED** (rc 5) to re-point `~/cells/_bin`, and its reason is better than my plan was:
> *"Re-pointing `_bin` swaps the launcher, watcher and harvest for cells that are ALREADY BUILT.
> `built-from.tsv` records instrument shas at BUILD time, so cells run before and after the swap would
> differ and no receipt would say so. … Pass `--repoint` as the 3rd argument to do it anyway."*
⛔ **It offered me the bypass flag and I did not take it.** Re-pointing the shared root would have swapped
the instruments under the three already-built smoke cells and left **no receipt saying so** — turning a
DECLARED difference (§13) into an undeclarable one.
✅ **Instead, the refusal's own alternative: a NEW cells root.**

    ~/cells-matrix1/_bin  installed from  …-export-eee8d83   (28 links into that export)
    ~/cells-matrix1/_bin/cell-claude.sh   sha256/16 5b41846b3e742c64   == the required value
    FAULT-class content guard in the RUNTIME launcher: 1 occurrence
    ~/cells (smoke root) untouched, still 62e9daef8f4dba98

⇒ **The 57 run under `~/cells-matrix1`; the 3 smoke cells stay in `~/cells` with §13's footnote.**
**No cell has a swapped instrument, and every cell's `built-from.tsv` describes what actually ran.**
📌 **The sha was verified FROM `_bin` ITSELF, not from the export** — §13's rule, applied to its own
first case. And it agrees with two independent sources systems supplied (the git object and the export),
which is what makes it a cross-check rather than a restatement.
⛔ **`_bin` is 28 SYMLINKS INTO the export**, so `…-export-eee8d83` must not be moved or deleted while
any cell runs. **A runtime made of links is only as durable as the tree it points at.**
### REMAINING SEQUENCE BEFORE THE FIRE
1. Build 57 cells under `~/cells-matrix1` (4 arms × 5 problems × n=3, minus the 3 smoke cells).
2. **Seed ALL trust in one pass, then verify all 57 records present and `.claude.json` valid** — §11's
   ruling on the unlocked read-modify-write.
3. Render each cell's fence **after the full set exists**, so the peer deny-glob covers every peer.
4. Fire 4-wide. Receipts quote the **`_bin` sha**, not the export's.

---

## 15. THE CONDITION KEY IS **THREE** FIELDS, FOUND BY BUILDING ONE CELL BEFORE 57
A verification build of `LZW · salt-diet · --statement` records:

    ctl/arm          salt-diet          <- IDENTICAL to the diet-BARE arm
    ctl/card_extras  statement          <- the only field that separates them
    ctl/task         LZW
    (a bare cell reads  arm=plain  card_extras=none)

⇒ 🔑 ***THE CONDITION IS `(task, arm, card_extras)`. A SCORER KEYING ON `arm` ALONE SILENTLY POOLS
`diet-bare` WITH `diet-stmt` — AND `plain-bare` WITH `plain-stmt`.*** That would collapse this matrix's
four arms into two, **double the apparent n of each, and mix the very pair the Captain called the
gold** — with no error, no warning, and medians that look entirely reasonable.
⛔ **The HARNESS is not at fault: it records the field.** The hazard is entirely in the reader, and
`score_stage1_close.py` — my own instrument — keys on `(problem, arm)` because stage 1 had only bare
arms and never needed the third field. **It would be WRONG on this matrix and RIGHT on everything it has
ever scored, which is the most dangerous shape an instrument can have.**
⇒ **REGISTERED: the matrix scorer keys on all three fields, reads them from each cell's own `ctl/`, and
REFUSES a cell whose `card_extras` is absent** — an unreadable third field must halt the reading, not
default to `none`, because defaulting silently re-creates the pooling this clause exists to prevent.
📌 This is council 09/07's *"a cell's receipt records no problem field"* one field over — except that
here the receipt DOES record it and the reader would not have looked. **Found by building ONE cell and
reading its `ctl/` before building the other 56.**

---

## 16. ⛔⛔ MATRIX #1 CANNOT DELIVER ITS GOLD — THE STATEMENT ARM EXISTS ON ONE PROBLEM
Building the 56 remaining cells, **24 of 24 `--statement` builds REFUSED** with:
    REFUSE: --statement but the card has no `## Statement` section
Measured in the task material:

    ## Statement section   LZW 1  ·  Crc32 0 · FreeList 0 · LRU 0 · Paxos 0
    ## Hint section        LZW 1  ·  the rest 0
    card.md size           LZW 14,575 B  vs  4,087-7,341 B for the others

⇒ 🔑 ***THE STATEMENT ARMS ARE BUILDABLE FOR LZW AND NO OTHER PROBLEM. THE GOLD PAIR — (d) plain+stmt
vs (e) diet+stmt — CAN EXIST ON EXACTLY ONE PROBLEM, WHICH IS k = 1, p = 0.5000, AND BY §2 OF THIS FILE
THAT IS NO VERDICT AT ALL.*** The four other cards were authored without the section; this is a CONTENT
gap, not a harness fault, and the refusal is the harness working.

### WHAT #1 CAN AND CANNOT DELIVER, AS BUILT
    ✅ BARE PAIR, ALL 5 PROBLEMS, n=3      30 cells   -> the cross-problem sign test, k=5, p=0.0312
    ✅ LZW STATEMENT PAIR, n=3              6 cells   -> the gold at k=1, p=0.5000, NO VERDICT
    ⛔ statement pair on 4 problems        24 cells   -> UNBUILDABLE until `## Statement` is authored
    built and complete right now: 33 in ~/cells-matrix1 + 3 smoke = 36 of the 60
⇒ **The headline claim SURVIVES: "salt costs more on all five problems" is fully buildable and is the
only outcome that reaches p ≤ .05.** ⇒ **The gold does NOT survive at n=1 and must not be reported as
though it did** — that is §2's clause applied to the pair it was written for.
⛔ **AND THE AUTHORING IS NOT MINE TO INVENT.** Council 09/07 dropped the HINT arms because *"the hint is
problem-specific, the Captain's hour per problem."* **A `## Statement` is the same object class** — it
is the artefact the salt method seals against, and **a seat that writes it decides what the treatment
arm measures.** ⇒ **Recorded as OWED, with the cost named: four cards, an author's hour each.**
📌 **24 partial cell directories were removed** — a stub dir with no `ctl/arm` must never be countable
as a cell, and 57 dirs in a root of 33 cells is exactly the miscount that produces a wrong denominator.

---

## 17. THE CONDITION KEY NEEDED A **FOURTH** FIELD, AND THE SCORER FOUND IT ON PARTIAL DATA
`score_matrix1.py` was written while the run was still firing — and its first draft, driven against 5
harvested cells, **silently pooled matrix #1 with stage 1, with the five-cell pricing set, with the
DROPPED `hint` arms, and with the VOID cell `57729c86`.** It searched every harvest dir and both cell
roots, so `Crc32 plain none` read n=3 from stage 1's cells and `LZW plain none` read n=4 including a
price stage 1 had excluded by name.
⇒ 🔑 ***(task, arm, card_extras) IS CORRECT AND WAS NOT ENOUGH: CELLS FROM DIFFERENT RUNS SHARE IT.
THE RUN IS THE FOURTH FIELD, AND UNLIKE THE OTHER THREE IT CANNOT BE READ OFF A CELL — IT MUST BE
DECLARED.*** §15 fixed the key one dimension short.
✅ **REGISTERED: the scorer reads a DECLARED SET — the cells in `~/cells-matrix1` plus the three smoke
ids named in §12 — and nothing else. A GLOB OVER THE ARCHIVE IS NOT A SET.** It prints the set's size
and composition on every run, so a reader can see what was counted before reading what was concluded.
📌 **Why this was cheap: the scorer was driven on PARTIAL data, before any conclusion depended on it.**
A scorer first run when the data is complete is a scorer whose first output is also its verdict, and
nobody re-reads a verdict's denominator. ⇒ **DRIVE THE SCORER WHILE IT STILL HAS NOTHING TO SAY.**

## §18 — WHEN A CELL IS REPLACED, AND WHY THIS IS NOT §10 (registered 2026-09-08 13:2x, BEFORE the replacement fired)

Cell `59c93bbe` (LRU · plain · none) ended `FAILED-BOOTS — six consecutive fast deaths,
class HARNESS`. Its harvest exited 3 with `COST VOID(UNPRICED)`. It never booted, so it
produced no subject behaviour of any kind.

**THE RULE.** A cell is replaced **if and only if it produced no subject outcome** — the
harvest exits non-zero with the meter `VOID(UNMETERED)`, or the cell ends in a class
`HARNESS` termination. A cell that BOOTED and produced a price is **NEVER** replaced,
whatever that price is, and no condition is ever re-fired because its spread displeased me.

**WHY §10 DOES NOT BITE.** §10 forbids re-firing a condition because its first cell
displeased me, and names that selection on outcome. A VOID cell has no outcome to select
on: the instrument did not run. The distinction is not a judgement call at scoring time —
it is readable from the harvest's exit code and the meter's own VOID token, both written
by the harness before I see any price.

**THE HONEST WEAKNESS, DISCLOSED RATHER THAN PAPERED OVER.** I already know the two
surviving prices in that condition ($7.75, $6.68) — I read them from the archive while
diagnosing the VOID. So I cannot claim this replacement was decided blind. What defends it
is that the rule has **no discretion in it**: VOID ⇒ replace, always, in every condition,
decided by the harness's exit code and not by me. Knowing the prices cannot move a decision
that admits no choice. The rule is written here so the NEXT void is governed by a clause
that predates it.

**LIMITS.** At most ONE replacement per voided cell. A second VOID in the same condition
leaves that condition at its achieved n; it is reported at that n and never pooled upward,
and the registered floor arithmetic (`n >= 2k(sigma^2)/(delta^2)`) is recomputed at the n
actually achieved rather than the n intended.

**STATE AT REGISTRATION.** Eleven cells ended, twenty-two running. Every condition reaches
n=3 except LRU · plain · none, which stands at n=2 solely because of this void. That is the
one hole this clause fills, and it fills no other.

## §19 — G3 PROVENANCE: THE RUN IS SPLIT IN ITS DECLARATION AND SINGLE IN ITS EXECUTION (measured 2026-09-08 13:3x, mid-run)

A new export (`e1830fe`) landing prompted the check. It found something older and
closer to home: the running cells carry
`HARNESS_V3=/Users/jyh/projects/claude/saltbench-systems-v3-export/harness/systems-v3`
— the **unsuffixed** path, which is a real directory dated **Sep 5**, not the
`eee8d83` this matrix is declared on. It is declared that way in `~/cells/toolchain.env`
(lines 3 and 7), so every cell inherits it. `_bin`, the fire script and the harvest all
name `eee8d83` explicitly. On its face that is §13's defect one field over.

**IT IS INERT, AND HERE IS WHY, MEASURED RATHER THAN ARGUED:**

1. `_common_v3.sh:17` is the only consumer that matters — `HARNESS=${HARNESS_V3:-...}`
   — so anything sourcing it resolves `$HARNESS` to the stale dir. **Nothing in the
   live path sources it.** Its only importers are `test_strength.py` and itself;
   `cell-claude.sh` and `cell-watch.sh` contain no reference to `HARNESS_V3` or
   `_common_v3` at all.
2. `smoke_harvest_v3.sh` never uses `$HARNESS/`, and the harvest is invoked with an
   explicit `--export <eee8d83 harness>`.
3. `VERUS_GUARD` also names the stale dir — and that file is **byte-identical** across
   both exports (sha 7d42a090…), so the guard the cells run is the guard I verified.
4. ⭐ THE STRONGEST ARM, because it converts a silent failure into a loud one: the price
   inputs `rates.tsv` and `cost_caps.tsv` **do not exist in the stale export**. Had any
   pricing step resolved through `$HARNESS`, it would have died with a missing file
   rather than returned a wrong number. There is no path by which a stale rate reaches
   a published price.
5. The two `_common_v3.sh` copies differ by exactly four lines, and the newer one is
   the STRICTER of the pair (it requires `VERUS_SHA256` under §27). `VERUS_SHA256` is
   set in every running cell, so even the stale copy would have passed.

⇒ **G3 PROVENANCE HOLDS FOR MATRIX #1.** The declaration is stale; the execution is
single-export.

⛔ **AND toolchain.env IS NOT EDITED WHILE THE MATRIX RUNS.** Repointing `HARNESS_V3`
now would make cells launched after the edit differ from cells launched before it —
manufacturing, mid-experiment, the exact split this section just proved absent. The
repair is owed BETWEEN runs, and it is recorded here so it is not lost: `toolchain.env`
lines 3 and 7 should name the export the run is declared on, so that the declaration and
the runtime cannot drift apart silently again.

## §18(b) — AMENDED BY THE INCIDENT THE ORIGINAL CLAUSE CAUSED (2026-09-08 21:0x)

§18 as written says a VOIDed cell gets one replacement. It does not say WHEN, and I executed it
immediately, building the replacement into the live cells root at 20:17Z while 22 cells were
still pending. **The fence's peer deny-set is a glob taken at RENDER time**, so one new directory
staled all 33 existing fences at once. Cells launching afterwards hit `render_fence_v3: DRIFT`,
held six times, and died `FAILED-BOOTS (class HARNESS)`. Two cells (`7fa6c322`, `823de693`) were
lost that way and sixteen were blocked — a fence-drift census read `pending clean: 0`.

**THE AMENDMENT.** Replacements are **BATCHED**, and built only during a launch pause:
1. STOP the scheduler and any armed waiter, and stop watchers that are HOLDING rather than
   running — a watcher that has not launched costs nothing to stop and costs a whole cell to
   leave holding.
2. Build EVERY replacement owed at that moment, together. The second addition costs exactly what
   the first does, so batching is free and serial addition is not.
3. Re-render every pending fence ONCE, with the render environment PINNED
   (`--verus-root`/`--cargo-root`, per `cell-claude.sh`'s own comment). Back up each fence first,
   and verify twice: `--check` rc 0, AND a backup-vs-new diff showing the only change is the new
   peers.
4. **SEED TRUST for every new cell** (`cell_trust_v3.py --seed`). `cell_build.py` does NOT do
   this; a newly built cell is refused at a second gate, `cell_trust_v3: REFUSE — repo is NOT
   trusted`, and dies the same six-hold death. This is not optional and it is not in the build.
5. Only then resume.

⛔ **AND THE DIAGNOSTIC WARNING, because it nearly cost more than the outage.** Running the fence
renderer's `--diff` WITHOUT the pinned roots reports a large phantom drift — a fresh rendering
appears to add `/Users/jyh/bench-src` to `denyRead`. Acting on it would install a fence hiding
each cell's own cargo registry, which presents as a MISSING CRATE rather than as a denial.
⇒ **A DIAGNOSTIC RUN IN A DIFFERENT ENVIRONMENT FROM THE PRODUCER MANUFACTURES A FALSE DIAGNOSIS.**
Always diff with the producer's pinned arguments.

📌 SCOPE: this amends the PROCEDURE for executing §18 and changes none of its criteria. Which
cells are replaced, and why, is unchanged: only a cell that produced no subject outcome, decided
by the harness's exit code, never by a price.

## §20 — THE PRIMARY TEST IS ASYMMETRIC IN POWER, AND THAT IS STATED BEFORE THE DATA (2026-09-08 15:2x)

Driving `sign_test()` at every decision-relevant k before the run completes — 5/5 → 0.0312 ·
4/5 → 0.1875 · 3/5 → 0.5 · 2/2 → 0.25 · 0/5 → 1.0, all matching §2 exactly — made an asymmetry
visible that §2 does not say out loud.

**THE TEST REGISTERED IN §2 IS ONE-SIDED**: it asks `P(at least k premiums ABOVE 1 | H0)`, in the
direction the campaign expects (salt costs more). Consequently:

    all five premiums ABOVE 1   p = 0.0312   -> the hypothesis can be CONFIRMED at .05
    all five premiums BELOW 1   p = 1.0000   -> the hypothesis CANNOT be REFUTED at .05

⇒ ⛔ **THIS DESIGN CAN CONFIRM ITS HYPOTHESIS AND CANNOT SIGNIFICANTLY REFUTE IT.** A five-problem
sweep landing entirely in the *opposite* direction — salt CHEAPER everywhere, which would be a
larger surprise than the result being sought — produces no significant finding under the primary
reading. §67 requires any premium below 1 to be REPORTED, and §33 requires the outcome reported by
name whichever way it falls, so the observation cannot be buried; but it cannot be called
significant either, because the test was pointed one way in advance.

**THIS IS NOT A DEFECT TO REPAIR MID-RUN AND IT WILL NOT BE.** Switching to a two-sided test now
would change the bar after cells have landed — and it would raise 5/5 from 0.0312 to 0.0625, which
**fails .05**, i.e. the change most defensible in principle is also the one that would retire the
only outcome this design can call. Making that swap while blind to the result would still be
changing a registered gate; making it after seeing the sign would be indefensible. The clause is
registered instead, so a reader knows the shape of the instrument rather than inferring symmetry
it does not have.

⇒ 🔑 **A ONE-SIDED TEST IS A CLAIM ABOUT WHICH SURPRISE YOU ARE WILLING TO MEASURE.** Ours measures
the expected one. Any write-up must say so beside the p-value, not in a methods appendix.

📌 ROUNDING, since two renderings of the floor are now in the fleet record: the value is
**2.007254…**; this file and the scorer print **2.0072** (truncated), systems' receipts print
**2.0073** (rounded). **One number, two renderings — not two floors.** Recorded so nobody
reconciles a discrepancy that does not exist.

## §21 — I KNOW WHAT THE LAST CELL IS WORTH BEFORE I FIRE IT (registered 2026-09-09 00:1x, BEFORE the cell runs)

The run has drained. Four problems have premiums, **all above 1**:

    Crc32 1.1610x · FreeList 2.7306x · LZW 1.3749x · Paxos 2.6514x
    4 of 4  ->  p = 0.0625  ->  NOT a result

`LRU salt-diet` stands at **n=2** ($11.19, $11.21) because `879326db` VOIDed in the fence-drift
outage I caused. §18 requires exactly one replacement, and §18(b) requires it batched at a launch
pause. That pause is now.

⛔⛔ **AND I CAN SEE WHAT IT IS WORTH BEFORE IT RUNS.** LRU's plain median is $7.75. Its two
surviving diet cells are $11.19 and $11.21 — extraordinarily tight. A third cell anywhere near them
puts the median near $11.20 and the premium near **1.44, above 1** — which turns 4-of-4 into
**5-of-5, p = 0.0312, the ONLY outcome this design can call significant** (§2, §20).

**SO THIS IS REGISTERED BEFORE THE CELL EXISTS:**
1. **The cell fires because §18 requires it**, written at 12:5x when I did not know a campaign would
   turn on it. It is not fired because it is likely to help. **A rule containing no discretion is
   worth exactly what it is worth at the moment discretion would be profitable.**
2. **WHATEVER IT RETURNS, IT STANDS.** If it lands below 1, LRU's premium is below 1, the count is
   4-of-5, **p = 0.1875, and §2 registered that IN ADVANCE as NOT a positive result.** I will report
   that outcome by name and will not re-fire, re-median, or reclassify it. §10 forbids re-firing a
   condition because its result displeased me, and §18 caps replacements at one per void.
3. **THE PREDICTION ABOVE IS PART OF THE RECORD.** If the cell lands near $11.20 and the headline
   becomes p=0.031, this paragraph exists so that no reader has to take on trust that the prediction
   came before the number. If it lands far from $11.20, this paragraph is a failed prediction and
   that is also the experiment working (§67).
4. ⛔ **THE OUTCOME DOES NOT MOVE G2.** Two premiums already exceed the 2.0072x floor (FreeList
   2.7306, Paxos 2.6514) and two do not (Crc32 1.1610, LZW 1.3749). The registered gate declares
   **every per-problem magnitude UNRESOLVED while any premium is below the floor**, so even at 5/5
   the headline is a SIGN and never a ratio.

⇒ 🔑 **THE MOST DANGEROUS CELL IN A CAMPAIGN IS THE ONE WHOSE VALUE YOU CAN ESTIMATE BEFORE YOU RUN
IT.** The protection is not that I will be honest; it is that §18 already removed the choice, in
writing, hours before the choice existed.
