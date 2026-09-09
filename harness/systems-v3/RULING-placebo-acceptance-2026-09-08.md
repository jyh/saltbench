# RULING — THE PLACEBO ARM'S ACCEPTANCE (desk row HE), bench as SaltBench lead
# 2026-09-08. Criteria registered in advance; this file records the verdict against them.

## THE OBJECT RULED ON
`CLAUDE.placebo.r4.md`, sha256
`8699d11ea6f0f792ae30a6d63d2165384d538742c0f844016224eb6ad67d5d15`.
⛔ **THE SHA IS THE ARTEFACT AND THE PATH IS NOT.** An earlier revision of this candidate was
edited in place at a stable filename, and a verdict of mine was left attached to bytes that no
longer existed. Two revisions (`873b156c…`, `9f816ab3…`) have been destroyed that way. Every
verdict below names the sha it ruled on; a verdict citing only a path is not re-runnable.

## THE CRITERIA, AND WHERE EACH NUMBER COMES FROM
Registered before this candidate existed. Nothing here was retyped from a message.

| # | criterion | result | instrument |
|---|---|---|---|
| 1 | ratio ≤ 2.0 at 10-word shingles | **0.00** | evidence (non-author refuter), verdict in the private seat record |
| 2 | no salt-diet-only run > 20 words | **0 at every n, 10..37** | same; measured at the criterion's own object, not inferred from an n=14 stitch |
| 3 | sections · heading levels · order | **9/9, identical** | `placebo_check.py` ARM 1 |
| 4 | total length ±10% | **1895 → 1918, +1.2%** | ARM 2 |
| 5 | imperative count ±10% | **46 → 49, +6.5%** | ARM 3 |
| 6 | control floor (my ruling, 2026-09-07) | **10/10** | ARM P |
| 7 | zero method content, 4 classes | **0/0/0/0** | ARM 4, with the control FIRING 55/11/28/10 on the source |

⇒ **VERDICT: THE REGISTERED CRITERIA ARE MET.** The arm fires on the Captain's ratification,
under one condition: **its own cells root, never `~/cells-matrix1`.** A fence's peer deny-set is
a glob taken at render time over `CELLS_ROOT` (measured: 44 peer denies naming that root, 0
naming any other), so building into a live root stales every fence in it — and adding a third
arm to a running matrix would change the population §12 declares and the registered sign test is
computed over, after cells have landed.

## ⛔ WHAT THIS VERDICT DOES **NOT** ESTABLISH — REGISTERED BEFORE ANY RESULT EXISTS
The refuter raised this **at the moment the candidate passed**, which is when it is hardest to
hear and worth most:

> **A shingle count cannot fail a construction that replaced the words.**

r4 was built by replacing each method instruction with an inert one of the same shape, so lexical
overlap **must** go to zero. Criteria 1 and 2 are therefore **NECESSARY AND NOT SUFFICIENT**.

⇒ **THE PLACEBO ARM MAY NEVER BE REPORTED AS "THE PLACEBO PROVABLY CONTAINS NO METHOD."**
What is established is exactly this and no more:
* no lexical overlap with `CLAUDE.salt-diet.md` at 10- to 37-grams;
* zero occurrences of the four forbidden classes, on an instrument whose control fires on the source;
* matched form — sections, order, length, imperative count;
* the complete control floor, so the placebo says nothing LESS than the plain arm says.

**Method paraphrased into new words is invisible to every instrument in this campaign.** That
residual is what the Captain's prose review is for; it is the only gate that can see what the
mechanical gates cannot, and it is not a formality.

## A NOTE ON THE INSTRUMENTS, KEPT BECAUSE IT BEARS ON HOW MUCH THE NUMBERS ARE WORTH
The refuter's forbidden-class table would not reproduce its own earlier table — 11/3/3/4 against
10/2/1/3 — **for the same control files at the same shas.** The files did not move; the
instrument did. They therefore made no cross-run claim and rested only on the single run all
columns came from. ⇒ **fixed controls moving is the proof that columns are not comparable across
runs**, and it is why every run carries its controls instead of citing yesterday's numbers.
My own gate `placebo_check.py` over-reported absence three times today, each time making a peer's
work look worse, because five of its ten control-floor patterns matched a single literal string.
Its counts are worth only what its controls and its verification-at-the-text make them worth.

---

## §2 — WHICH HARNESS THE PLACEBO RUNS ON, AND THE LIMIT THAT BUYS (ruled 2026-09-08 14:4x)

The placebo controls the salt-vs-plain comparison, which is **stage 1's** — and stage 1's cells
record `23b351c` in their own `built-from.tsv` (18 of 20; the other two `5b9927ad`). The placebo
root's runtime is `338d18f`. Against matrix #1's `eee8d83` the two are byte-identical on
everything a claude cell executes; against `23b351c` **six files differ on the claude path**:
`cell-claude.sh`, `fence-hook.sh`, `canary.py`, `cell_trust_v3.py`, `rust_env.sh`,
`smoke_harvest_v3.sh`. Four are repairs made on 2026-09-08.

**RULED: the placebo runs on the REPAIRED harness, and the delta is named in the RUN'S
provenance record.**

⛔ **CORRECTED 2026-09-08 14:4x, ON systems' MEASUREMENT: THE RECEIPT I NAMED DOES NOT EXIST
FOR THESE CELLS.** I wrote "named in every cell's receipt", meaning `ctl/built-from.tsv`.
Measured at a live cell: **claude cells do not have one.** `cell_build.py` writes it only on
the agy branch. Worse than absent — it is a REGRESSION: 20 of 25 stage-1 cells DO carry it,
with `export_sha`, `cfg`, `account`, `vendor` and `arm`. The receipt existed and was lost
between stage 1 and this run.
📌 I had the evidence hours earlier — I ran `cat ctl/built-from.tsv` on an LRU cell, saw it
print nothing, and moved on. **An empty read is a finding; I treated it as a formatting
quirk.**
⇒ The delta is therefore recorded in `PROVENANCE-matrix1-2026-09-08.tsv` (this directory),
and the placebo run must carry the same per-cell record — by whatever vehicle exists when it
fires, not by the one I assumed.

⇒ 🔑 **YOU CANNOT BUY BYTE-COMPARABILITY BY RUNNING THE CONTROL ON AN INSTRUMENT THAT FAILS IN THE
REASSURING DIRECTION.** `23b351c` carries the canary that fails toward `CLEAN`. Running the honest
baseline on it would make the placebo's containment claim unfalsifiable, which is worse than a
delta that can be named in a sentence.

**MEASURED, because the ruling rests on the delta being immaterial to the outcome variable:**
* **What the subject is asked — IDENTICAL.** `SEAT.md`, `BOOT_PROMPT_1.txt`, `BOOT_PROMPT_2.txt`,
  `CLAUDE.plain.md`, `CLAUDE.salt-diet.md`, `POKE.txt`, `RETRY.txt`, `LANDING.md.template`, and
  the entire `tasks/systems-v3` tree (`diff -rq` clean).
* **The subject's environment — IDENTICAL name set.** The launcher now derives it from
  `rust_env.sh --print` minus `CARGO_FLAGS` rather than an inline `printf`; both paths deliver the
  same ten names.
* **How cost is computed — UNCHANGED.** The harvest's 44 changed lines are comments plus one
  functional addition: a CFG-mismatch guard that REFUSES. A guard that refuses can prevent a wrong
  number; it cannot produce a different one.
* **`canary.py`, `fence-hook.sh`, `cell_trust_v3.py` — not reachable from the subject.** `bin/rt`,
  `bin/declare` and `bin/bus` reference them zero times, on a grep proven able to match.

## ⛔ THE LIMIT THIS RULING CREATES, AND IT BINDS ANY RESULTS TABLE
**COST IS COMPARABLE ACROSS THE TWO EXPORTS. CONTAINMENT MEASUREMENTS ARE NOT.**
The placebo's containment figures come from a repaired canary; stage 1's came from one that fails
toward clean. ⇒ **a placebo-vs-stage-1 comparison is valid on cost and INVALID on escape or
containment rates.** A table placing those columns side by side compares two instruments, not two
arms — the same defect the refuter reported against itself the same afternoon, where fixed controls
moving was the proof that columns were not comparable across runs.

**NOT ESTABLISHED:** two of the six diffs were read in full and the consequence of a third derived.
For the remaining three, non-reachability from the subject was established — not that their
internals are irrelevant on every axis. Sufficient for a cost comparison; not sufficient for a
containment one, which is why the limit above is registered rather than assumed away.

---

## §3 — RATIFIED AND FIRED (2026-09-08 15:4x)

**THE CAPTAIN'S WORD, verbatim and complete:** *"ratify the placebo r4"*. Nothing added, nothing
glossed into a methodology endorsement. Anchored to
`CLAUDE.placebo.r4.md` (in the private seat record), sha256
`8699d11ea6f0f792ae30a6d63d2165384d538742c0f844016224eb6ad67d5d15`, 11,584 B, read back out of
`origin/master` at the moment of ratification — the same bytes this file's §1 ruled on.

📌 **WHY THE VERBATIM QUOTE MATTERS HERE OF ALL PLACES.** An earlier Captain ruling on this same
campaign is recorded only as the words *"strip the instructions"*, and that wording appears on **no
ruling surface at all** — it is now a declared, dated block (`placebo-wording`). One placebo ruling
in this campaign is unhomeable. This one is quoted, dated, and attached to a committed sha.

**BENCH'S WORD: FIRE, on four conditions.** Verified before giving it: `render/CLAUDE.placebo.md`
was still ABSENT from the export and the builder still refused `--arm placebo` by name — the gate
held all the way to the ratification.

1. **The installed text is verified by sha AFTER the copy, and comes from the REF** —
   `git show origin/master:…/CLAUDE.placebo.r4.md`, never a working-tree copy or a backup, then
   re-`shasum` the installed file against `8699d11e…`. The export is not a git repository, so
   **nothing downstream will ever notice a drift introduced by this one copy**, and it is the
   single step between a ratified artefact and the cells built from it.
2. **Its own cells root** (`~/cells-placebo`), never `~/cells-matrix1`: the fence peer glob is
   scoped to one `CELLS_ROOT` (measured 44 / 0), and matrix #1's declared set must not change
   mid-experiment.
3. **The export delta is named in the run's provenance record**, written AT BUILD TIME rather than
   reconstructed afterwards — claude cells carry no `ctl/built-from.tsv` (§2), and matrix #1's had
   to be recovered from mutable state.
4. **The box's concurrency does not rise while matrix #1 is still firing.** Matrix #1 was priced at
   4-wide and the harness records box-busyness in its own harvest notes. ⇒ **a reviewer must never
   have to ask whether the matrix's tail cells were measured on a busier machine than its head
   cells** — a question with no answer after the fact.

⇒ `placebo-ratification` DISCHARGED. Still outstanding on this seat's rows: `gemini-subject-group`.

---

## §4 — THE GATE CELL IS EXCLUDED FROM THE PLACEBO'S ANALYSIS SET (ruled 2026-09-08 18:0x, before the wave exists)

`pb1a2b3c` (Crc32 · placebo · none) is the gate cell: it was fired alone, to prove the arm works
end to end before fifteen cells commit to it. **It is excluded from any placebo analysis set**, for
two reasons that are both measured rather than stylistic:

1. **IT RAN ALONE.** Matrix #1's arms were measured at 4-wide and the placebo wave will be too
   (the cap ruling). A cell measured with the box to itself differs from the arms it would be
   compared against **in contention, which is not the treatment** — the same confound that bars
   cross-stage comparison between stage 1 (~1-wide) and matrix #1 (4-wide).
2. **ITS OWN RECEIPT SAYS SO.** `ctl/comparator.tsv` records
   `comparator_export = NOT DECLARED — … A cell whose comparator is undeclared cannot support a
   cross-run comparison; this row says so rather than being absent.` ⇒ **the cell declares its own
   unfitness for the comparison**, and excluding it is agreeing with its receipt rather than
   overriding it.

⛔ **REGISTERED BEFORE THE WAVE EXISTS, WHICH IS THE POINT.** An exclusion decided after seeing a
cell's price is selection on outcome (§10). This one is decided from how the cell was RUN, before
any placebo price exists at all, and it would be equally binding if the gate cell turned out to be
the cheapest or the dearest thing in the arm.

📌 The wave cells must carry `COMPARATOR_EXPORT` set to `<export>/harness/systems-v3` — the harness
level, not the export root. Export `6b6fc12` refuses the wrong level at rc=4 with zero cells
created (driven RED and GREEN here), so this is now enforced rather than remembered.

---

## §5 — THE CONTAMINATED WAVE'S ADMISSIBILITY (ruled 2026-09-08 23:1x, BLIND)

**Trigger.** systems measured the double-launch contamination per cell and handed the call up
(bus `@43944351`, 09/08 21:42). My 21:44 post deferred it — *"not mine to decide at this gauge"* —
to "the next bench". ⛔ **The gauge was the whole of that reason, and it dissolved at the
compaction. A deferral whose stated condition no longer holds is a stale STOP**, and a stale STOP
is caught by nobody, because a hold being obeyed and a hold still needed look identical from
inside. So it is ruled here.

⛔⛔ **AND IT IS RULED NOW BECAUSE IT CANNOT BE RULED HONESTLY LATER.** No re-fired placebo price
exists yet. Once one does, any rule I write is selection on outcome (§10) — and this is the
load-bearing rung of the campaign, the arm that decides whether salt's premium is its CONTENT or
merely its FORM. **This section is worth what it is worth only because I am blind while writing it.**

### §5.1 — NO PER-CELL ADJUSTMENT IS PERFORMED. NONE.
⚠️ **AMENDED BY §8.3 — READ IT BEFORE APPLYING THIS.** The MECHANISM stated below (*run 2 mutating run 1's tree mid-run*) is **REFUTED**: 15/15 double-runs were SEQUENTIAL. **The REFUSAL STANDS** on (a) the adjustment-magnitude ground below and (b) cross-cell CONTENTION. The text is kept unedited because the record must show what was believed when the rule was made.

systems' table carries a `run1` column, **and that column is the trap.** No adjustment is made:
not run1-as-clean, not delta subtraction, not a median-delta correction, not a multiplicative one.
**Reason:** the perturbation is `+1.7%` … `+309.4%`, median ~29% (bus `@43944351`), against
matrix #1 premiums of Crc32 **1.1610×** · LZW **1.3749×** · LRU **1.4465×** (same post) — the same
order as the effect, and **larger on two problems** (`pw08lru` +43.8% vs LRU's +45%; `pw12lzw`
+52.6% vs LZW's +37%).
⇒ 🔑 ***AN ADJUSTMENT WHOSE MAGNITUDE IS THE EFFECT'S MAGNITUDE MOVES THE FINDING OUT OF THE DATA
AND INTO THE ADJUSTMENT.***
⛔ **`run1` is not the clean price and must never be used as one.** Run 2 launched against the
SAME cell directory, so run 1's own trajectory was perturbed by a peer mutating its tree while it
worked. `run1` is a smaller number of unknown fidelity, not a measurement.

### §5.2 — THE ONE INFERENCE THE WAVE CAN STILL CARRY, AND IT HAS A DIRECTION
⚠️ **NARROWED BY §6.4 AND BAND-SCOPED BY §11.1.** The *a fortiori* admission below holds **only where the comparison is RESOLVABLE** — below the floor, a fortiori of UNRESOLVED is UNRESOLVED — and "resolvable" means **outside the two-sided band [0.4982, 2.0072]**, not below a single threshold.

The contamination is positive **BY CONSTRUCTION, NOT BY OBSERVATION**: `both-runs = run1 + run 2's
additional spend`, and spend is non-negative.
⛔ **The 8-of-8 positive deltas are ARITHMETIC, NOT A SIGN TEST, and must never be reported as
one.** (A sign test there would read p=0.0039 and would be meaningless: the outcome was not free
to fall the other way.)
⇒ Subject to §5.3's guard, **the contaminated price is an UPPER BOUND on the clean price.**

The placebo decides CONTENT-driven vs FORM-driven. Contamination **inflates** the placebo, moving
it **toward salt** — i.e. toward "form-driven", toward **gutting the headline I published at
5/5, p=0.0312.** ⇒ **the defect cannot manufacture the result that flatters this campaign.**

⇒ **ADMISSIBLE IN ONE DIRECTION ONLY:**
- contaminated placebo **at or below plain** ⇒ "content-driven, not form-driven" is supported
  **A FORTIORI** — the defect could only have pushed the other way.
- contaminated placebo **above plain, or near salt** ⇒ **THE WAVE SAYS NOTHING.** That outcome is
  fully explicable by the defect alone. Report **UNRESOLVED** — never as a refutation of salt.

This is the asymmetry already registered at §20 of `PREREGISTRATION-matrix-opus-1-2026-09-08.md`
(*a one-sided test can confirm, cannot refute*), stated here **before it is convenient.**
⛔ **THE LIMIT, AND IT IS THIS SEAT'S OWN CARD:** a bias against the arm under test licenses
retain-and-label-as-a-FLOOR **for a NUMBER; a VERDICT must be CORRECTED.** So §5.2 admits the wave
to **SUPPORT** a verdict a fortiori and **NEVER to RENDER one.** **No magnitude, no premium and no
ratio is ever published from these cells.**

### §5.3 — THE GUARD THAT MAKES THE UPPER BOUND TRUE, AND IT NEEDS A MEASUREMENT NOT YET TAKEN
⚠️ **A SECOND, CONJUNCTIVE CLAUSE WAS ADDED BY §8.2.** The END test below is **necessary and NOT sufficient**: a cell is admissible only if **(i)** one run reached a normal END **AND (ii)** the contaminated TOTAL is computable under §23(e). ⛔ Read alone, the test below ADMITS the paxo three, which §5.2 cannot use. See also §8.5 (`DONE` satisfies (i), not (ii)).

"contaminated ≥ clean" is **NOT unconditional.** If BOTH runs died early, their sum can fall below
one clean pass. ⇒ the bound holds only for a cell in which **AT LEAST ONE RUN REACHED A NORMAL END**
(`END LANDED landing-N`): such a cell demonstrably completed the work at least once, so its total
spend is ≥ the cost of completing it once.
⇒ ⛔ **REQUIRED BEFORE §5.2 TOUCHES ANY CELL — systems publishes the per-cell END status of BOTH
runs, measured at the cell.** It is not in this repository (checked: 0 local hits for the wave's
cell ids), so it is a measurement, not a lookup. **§5.2 is inert until that table exists.**
⇒ **Pre-disqualified from the record as it already stands:**
- **`pw10lzw`** — run 1 ended `END DIALOG` at $3.79, *broken and therefore cheap*. Inadmissible on
  every reading unless run 2 is shown to have ended normally.
- **`pw13paxo` · `pw14paxo` · `pw15paxo`** — run 2 was killed mid-flight; its spend sits in the
  METER and in **no post-end line**, so §23(e) cannot price them. Their "0%" is an **ARTEFACT OF
  THE KILL**, not a clean cell. Inadmissible.

### §5.4 — A RE-FIRE IS A NEW RUN AND IS NEVER POOLED
If the wave re-fires, its cells are a **NEW RUN** under the condition key and are **never pooled**
with the contaminated ones — not to raise n, not to fill a problem. (Same law that keeps `M-v1`
and `M-v2` apart: two regimes are never pooled because one of them named the perturbation.)
📌 The contaminated cells are **RETAINED AND LABELLED, never deleted.** systems has deleted nothing
and is right not to: they are the record of what happened.

### §5.5 — WHAT THIS RULING DELIBERATELY DOES NOT DECIDE
**Whether the re-fire HAPPENS is a SPEND decision** — box, quota, schedule — and is the helm's or
the Captain's, not this seat's. This section makes the re-fire's *scoring* safe whether it fires
tonight, next week, or never.
📌 §4's gate-cell exclusion is **untouched and is not revisited** now that outcomes are known —
re-opening it here, with the census in hand, would be the precise thing §4 was written to prevent.

⇒ ✅ **systems: the placebo half of your block on `SEAT:bench` is DISCHARGED by this section.** What
remains in front of you is the box and a spend word, **and neither is mine.**

---

## §6 — WHAT THE CLEAN RE-FIRE CAN AND CANNOT ESTABLISH (registered 2026-09-08 23:3x, BLIND)

**The helm ruled FIRE at 23:25** (bus `@44124094`), queued in `watch/gate/systems`, releasing when
paris frees the Studio. **These cells do not exist yet.** This section is written in that window, and
it exists because §5 governed only the CONTAMINATED cells — **it said nothing about how the CLEAN
re-fire is read, and that is the larger hole.**

### §6.1 — THE PLACEBO ARM IS AN EQUIVALENCE CLAIM WEARING A DIFFERENCE TEST
The arm exists to ask **whether salt's premium is CONTENT or FORM.** The reading that answers it —
*"placebo landed near plain, so the premium is content"* — is an **ACCEPTANCE OF A NULL.**
⛔ **No significance test licenses that.** G1's sign test, G2's floor and the whole matrix machinery
detect **DIFFERENCE**; they are **silent on SAMENESS**. An equivalence claim needs a declared margin
and the n to reach it, and this arm has registered neither.

### §6.2 — THE ARITHMETIC, AND IT IS AGAINST US
Registered `sd(ln cost) = 0.30458`, `k = 7.8489`, floor `= exp(σ·√(2k/n))`. The wave is **15 cells /
5 problems ⇒ n = 3 ⇒ floor = 2.0072×.** Against matrix #1's own measured salt premiums:
```
  Crc32     1.1610x   BELOW the floor — UNRESOLVABLE at n=3
  LZW       1.3749x   BELOW the floor — UNRESOLVABLE at n=3
  LRU       1.4465x   BELOW the floor — UNRESOLVABLE at n=3
  Paxos     2.6514x   above
  FreeList  2.7306x   above
```
⇒ 🔑 ***ON THREE OF FIVE PROBLEMS THE PLACEBO ARM AT n=3 CANNOT RESOLVE A FORM-EFFECT THE SIZE OF
SALT'S OWN MEASURED EFFECT.*** **The arm is underpowered to answer the question it exists to answer,
on the majority of its problems** — and that is a property of the **DESIGN, not of the data**, so it
is knowable tonight and is registered tonight rather than discovered in the write-up.
📌 n required per problem: **1.37× → 15 · 1.20× → 44 · 1.10× → 161.** The wave buys 3.

### §6.3 — THE RULE, REGISTERED BEFORE THE CELLS EXIST
⛔⛔ **SUPERSEDED BY §11.1 — DO NOT APPLY THE TWO-REGION FORM BELOW.** It is **one-sided on a two-sided floor**: it files a premium below **0.4982** as UNRESOLVED when that is **RESOLVED LOW**. The corrected rule has **THREE** regions and a resolved-low result **fires §11.2/§11.4**. The forbidden sentence below is unaffected and still binds.

The clean placebo arm is **diagnostic in ONE direction, and it is the direction that COSTS this
campaign:**
```
  placebo premium over plain ABOVE 2.0072x  ⇒ RESOLVED. Form drives cost; salt's premium is at
                                              least partly FORM. The finding is DAMAGED. PUBLISH IT.
  placebo premium over plain BELOW 2.0072x  ⇒ UNRESOLVED. Nothing more.
```
⛔⛔ **THE FORBIDDEN READING, NAMED NOW BECAUSE IT WILL BE TEMPTING LATER:** *"the placebo came in
near plain, so salt's premium is real method."* **That sentence must not appear in any write-up of
this arm.** A below-floor result is **the expected outcome of an underpowered arm whatever the truth
is**, and it carries no information about the null. ⇒ 🔑 ***AN ARM THAT CANNOT FAIL TO RETURN THE
FLATTERING-LOOKING ANSWER HAS NOT TESTED ANYTHING.***

### §6.4 — ⛔ THIS NARROWS §5.2, WHICH OVERCLAIMED, AND THE CORRECTION IS MINE
§5.2 admitted the contaminated wave a fortiori: *"contaminated placebo AT OR BELOW plain ⇒
content-driven supported A FORTIORI."* **That was written before I did §6.2's arithmetic and it is
too strong.** An *a fortiori* argument inherits the resolution of the reading it strengthens, and
**"at or below plain" is not a resolved reading when the gap is under the floor — it is noise.**
⇒ **§5.2 IS NARROWED:** the contaminated wave can support the content-driven reading a fortiori
**only where the comparison is resolvable at all.** Below the floor, *a fortiori* of UNRESOLVED is
still **UNRESOLVED**.
⇒ 🔑 ***A ONE-SIDED ADMISSIBILITY RULE STILL INHERITS THE POWER OF THE TEST IT FEEDS — I WROTE THE
ASYMMETRY CORRECTLY AND ATTACHED IT TO A COMPARISON THAT CANNOT RESOLVE.*** Corrected here, still
blind, ninety minutes after writing it and before any cell of the re-fire exists.

### §6.5 — WHAT WOULD MAKE THE ARM DIAGNOSTIC, STATED SO THE CHOICE IS EXPLICIT
Either **(a)** declare an equivalence margin δ in advance and run to the n it requires (§6.2's table
prices it), or **(b)** declare the arm **DESCRIPTIVE** — it reports placebo's cost and refuses any
content-vs-form verdict. ⛔ **What is not available is (c): run n=3 and read the null.**
📌 **This is not an argument against firing.** The helm's FIRE is correct and the cells are worth
having: the arm can still **DAMAGE** the finding, and an arm that can only hurt you is worth running.
It simply **cannot help**, and that must be on the record before it returns.

---

## §7 — THE ARM IS **DESCRIPTIVE** (ruled by the helm 2026-09-08 23:40; default-if-silent to the Captain)

§6.5 left the choice open — **(a)** declare an equivalence margin and run to its n, or **(b)** declare
the arm DESCRIPTIVE — and named **(c) run n=3 and read the null** as forbidden **and as the default if
nobody chose.** The helm ruled **(b)**, **before any cell of the re-fire exists**, which was the whole
point of asking. **It is default-if-silent to the Captain and nothing is irreversible before he reads it.**

### §7.1 — ADOPTED ON A SHARPER GROUND THAN THE ONE THIS SEAT ARGUED, AND I VERIFIED IT AT THE OBJECT
I argued **value** (*75 cells to resolve only 1.37× is a poor trade*). The helm's ground is
**structural**, and it is better. Re-derived here from the registered `σ=0.30458`, `k=7.8489`:
```
  n=  3/problem (  15 cells)  floor 2.0072   Crc32 1.1610 -> unresolved
  n= 15/problem (  75 cells)  floor 1.3656   Crc32 1.1610 -> unresolved
  n= 44/problem ( 220 cells)  floor 1.1995   Crc32 1.1610 -> unresolved
  n=161/problem ( 805 cells)  floor 1.0998   Crc32 1.1610 -> RESOLVED
```
⇒ 🔑 ***THERE IS NO CHEAP VERSION OF (a).*** The affordable rungs resolve the **largest** sub-floor
premium and leave the **smallest** standing — so a partial (a) **would be published as though it had
resolved the placebo question**, which is precisely what (c) is forbidden for. ⇒ **(a) at 75 or 220
cells is (c) with a bigger n.** Only the 805-cell rung is honest, and that is **53.7× the wave** on a
campaign that already holds a 5/5 result.

### §7.2 — WHAT "DESCRIPTIVE" MEANS OPERATIONALLY, SO IT CANNOT DRIFT
⚠️ **CLAUSE 2 IS BAND-SCOPED BY §11.1.** Read *"a premium clearing **the band in EITHER direction**"*, not "clearing 2.0072×". Clauses 1, 3 and 4 are unchanged and bind as written.

1. The arm **reports the placebo's COST per problem** and renders **no content-vs-form verdict.**
2. **§6.3's asymmetry still binds:** a premium **clearing 2.0072×** is RESOLVED, **DAMAGES** the
   finding, and **is published.** The arm can still hurt us and that is why it is worth firing.
3. **§6.3's forbidden sentence stays forbidden** — *"the placebo came in near plain, so salt's premium
   is real method"* appears nowhere.
4. **No equivalence claim, no "≈ plain", no null accepted**, in any write-up or table.

### §7.3 — (a) IS TRIGGERED, NOT DEAD
**If the descriptive wave shows ANY premium clearing 2.0072×**, the placebo question becomes live and
the **805-cell rung returns as a Captain-tier spend.**
⇒ 🔑 ***A TRIGGER NAMES THE OBSERVATION THAT WOULD CHANGE THE ANSWER; A DEFERRAL NAMES A DATE.***
This is the Blocks law's own distinction applied to a research decision rather than to a seat.

### §7.4 — QUOTA: `UNMEASURED` → PARTLY MEASURED, AND THE MISSING TERM HAS AN OWNER
⛔ **THE CONVERSION CLAUSE BELOW IS STRUCK BY §9 AS UNATTRIBUTABLE** — the cells authenticate as an account nine seats share, so a delta measures the account, not the cells. **§7's ruling is unaffected**: it rests on the structural ground, which §9.1 records as now the only load-bearing one.

The helm supplied tonight's readings at no extra cost (three accounts, all with room, windows resetting
tonight). ⛔ **What is missing is not an account reading — it is the CELL→QUOTA CONVERSION**, and
nothing on the helm's side maps a cell to a quota unit. ⇒ **Owner: `systems`**, which runs the cells
and reads quota at dispatch; **one measured per-cell quota delta turns §6.2's table from cells into
quota and makes (a) decidable by arithmetic instead of argument.**
📌 ⛔ **THE RULING DOES NOT DEPEND ON IT.** **(b) is right even if quota were infinite**, because the
affordable rungs of (a) are dishonest and the honest rung is disproportionate. Stated so that a later
quota measurement is not mistaken for a reason to revisit §7.

### §7.5 — ONE ATTRIBUTION CORRECTED, IN THE DIRECTION THAT FAVOURED THIS SEAT
The helm had written *"bench's framing was not the error."* **It was, in part:** this seat's block
registration read *"WHAT REMAINS IS PURELY A SPEND DECISION — roughly 15 cells of quota."* The
account-vs-host mapping was the helm's; **naming quota as the binding constraint was this seat's.**
The helm accepted the correction in full.
⇒ 🔑 ***AN OVER-GENEROUS ATTRIBUTION IS STILL A FALSE ATTRIBUTION, AND IT IS HARDER TO CORRECT BECAUSE
THE PARTY IT FAVOURS HAS NO REASON TO OBJECT.*** Recorded here because a campaign record that keeps
only the flattering half of an exchange is not a record.

---

## §8 — WHAT systems' §5.3 CENSUS CHANGED (ruled 2026-09-09 00:1x)

systems took the census **before anything moved**, as ordered, and returned three findings the ask did
not contain. ⭐ **And the ordering mattered for a reason neither of us stated:** `ctl/end-N` and
`ctl/post-end-N.tsv` are **one file per phase, and run 2 OVERWROTE run 1** — for 12 of 15 cells the
surviving price file describes run 2. **`watch.log` is append-only and is the only reason the census
was still possible.** ⇒ 🔑 ***THE EVIDENCE WAS NOT DESTROYED BY THE NEXT BUILD; IT WAS ALREADY
HALF-DESTROYED BY THE SECOND RUN, HOURS AGO.***

### §8.1 — MATRIX #1 IS CLEAN OF THE ORPHAN LEAK. MEASURED, BECAUSE NOBODY ELSE WOULD.
systems scoped its 24-process orphan leak to the placebo wave (11 of 16 priced cells inside the
window) and declared the direction on COST **UNMEASURED**. **It did not check matrix #1, correctly —
matrix #1 is not its wave. It is this campaign's published headline, so the check is the lead's.**
```
  leak window opened     2026-09-09T03:34:51Z   (systems, cross-checked by its own 20:48=03:48:47Z pair)
  matrix1 earliest END   2026-09-08T19:04:22Z
  matrix1 latest   END   2026-09-09T00:51:59Z
  MARGIN                 2h 42m 52s BEFORE the leak began
  cells carrying an END  37 of 37   (the other 2 dirs are `_audit` and `_bin` — no ctl/, not cells)
```
⇒ ✅ **NO matrix #1 cell was metered inside the leak window. 5/5, p = 0.0312 is untouched by it**, with
its four registered qualifiers unchanged.
⛔ **Scope, stated rather than implied:** this clears matrix #1 of **THIS** leak only. It says nothing
about box load from any other source, which remains unmeasured for every cell this campaign has priced.
📌 The two non-cells are exactly why the scorer's set filter keys on **structure** (`ctl/arm` exists)
and never on a name.

### §8.2 — ⛔ §5.3 HAD A HOLE, AND systems FOUND IT: THE END TEST ALONE ADMITS CELLS §5.2 CANNOT USE
§5.3's guard was *"at least one run reached a normal END."* **Read literally it PASSES
`pw13/14/15paxo`** — their run 1 ended `END LANDED landing-1`. **And §5.2 still cannot use them**:
run 2's spend sits in the METER and in **no post-end line**, so §23(e) cannot price the contaminated
**TOTAL**. ⇒ ***YOU CANNOT BOUND A CLEAN PRICE BY A TOTAL YOU CANNOT COMPUTE.***
⇒ **§5.3 GAINS A SECOND, CONJUNCTIVE CLAUSE.** A cell is admissible to §5.2 only if **BOTH**:
**(i)** at least one run reached a normal END, **AND (ii)** the contaminated TOTAL is computable from
post-end lines under §23(e).
⇒ 🔑 ***A CRITERION CAN PASS A CELL THAT A DIFFERENT CLAUSE STILL EXCLUDES, AND THE PASS IS THE
DANGEROUS ONE BECAUSE IT ARRIVES AS A GREEN.*** (systems' law, adopted verbatim.)
📌 My §5.2 pre-disqualification of the paxo three was right **and right for the reason given**; what
was defective was **§5.3's test, which read alone would have overturned it.**

### §8.3 — ⛔ §5.1's STATED MECHANISM IS REFUTED. THE REFUSAL STANDS, AND I NAME WHICH GROUND CARRIES IT.
§5.1 said run 2 perturbed run 1 *"by a peer mutating its tree while it worked."* **Measured: 15 of 15
double-runs were SEQUENTIAL** — run 2 armed strictly after run 1's END, closest gap 3m34s, zero
overlap on any cell. ⇒ **That mechanism did not occur. The factual claim is WITHDRAWN.**
⛔ **A ruling standing on a false stated reason is a ruling waiting to be overturned by the first
person who checks the reason.**
⇒ **§5.1's REFUSAL STANDS on two grounds, neither of them the withdrawn one:**
- **(a) the load-bearing one, untouched:** an adjustment whose magnitude is the effect's magnitude
  moves the finding out of the data and into the adjustment.
- **(b) systems' replacement mechanism, adopted:** run 1 and run 2 of **DIFFERENT** cells overlapped
  constantly, so the two runs were measured at **different box CONCURRENCY**. Not tree mutation —
  **contention.** Still not comparable.
⛔⛔ **AND I AM NOT TAKING THE RESCUE.** The inference sitting there — *"run 1 is the clean price after
all, 16 cells rescued"* — is **refused.** §5 was ruled **BLIND on purpose**, and a measurement arriving
afterwards that happens to rescue 16 cells is precisely what §10 forbids acting on. **systems reported
a fact that would flatter this campaign and refused to spend it; the lead does not spend it either.**
⇒ 🔑 ***A CORRECTION THAT REPAIRS A RULING'S REASON WHILE KEEPING ITS CONCLUSION IS HONEST ONLY IF THE
CONCLUSION NEVER RESTED ON THE REPAIRED PART — SO THE SURVIVING GROUND MUST BE NAMED, NOT ASSUMED.***

### §8.4 — `pw10lzw` IS ADMITTED; THE PAXO THREE STAY OUT
- **`pw10lzw`: PRE-DISQUALIFICATION LIFTED.** §5.3 named the condition — *"unless run 2 is shown to
  have ended normally."* Run 2 ended `END LANDED landing-1`, `post-end-1.tsv` LANDED **$15.5326**.
  **Met at the object** ⇒ **ADMISSIBLE.** Its run-1 `DIALOG` at $3.79 is simply the cheap broken half
  of a total whose other half completed the work.
- **`pw13/14/15paxo`: INADMISSIBLE**, now on **§8.2(ii)** — not on the END test, which they pass.

### §8.5 — `DONE` vs `LANDED`: RULED, BECAUSE A CLASSIFICATION LEFT OPEN GETS DECIDED BY WHOEVER NEEDS IT FASTEST
**`DONE` (`down - FINAL: …`) COUNTS as a normal END for §5.3(i)**: it is a terminal, non-error phase and
the cell completed its work. ⛔ **It does not by itself satisfy §8.2(ii)** — a `DONE` run whose spend
reaches no post-end line still leaves the total uncomputable.
📌 systems flagged it as **moot** for all four cells it touches (`pw06free pw07lru pw09lru pw12lzw` each
landed on run 1) **and said so in one line rather than letting it look load-bearing.** Ruled anyway,
because it recurs.

### §8.6 — THE ORPHAN LEAK IS A CAMPAIGN-WIDE INSTRUMENT GAP, NOT A PLACEBO INCIDENT
24 busy-wait processes forked by the **subject** of `pw01crc3`, re-parented to init, burning ~11 cores
for **3h23m**, outliving their cell's END by **3h09m**.
⇒ 🔑 ***THE HARNESS REAPS THE CLIENT AND THE WATCHER, AND NOTHING REAPS WHAT THE SUBJECT FORKED. A
CELL'S END IS NOT THE END OF THE CELL'S PROCESSES, AND NO ARM IN THIS CAMPAIGN LOOKS.***
⇒ **Registered as a standing limitation on every cost this campaign publishes:** a cell's measured cost
is taken on a box whose load may include the residue of earlier cells, and **nothing measures that.**
⛔ **Direction on COST: UNMEASURED**, per systems' own scoping, and this seat is **not upgrading it** —
extra CPU does not spend tokens, and whether it reached cost through timeouts or retries was not driven.

---

## §9 — §7.4's CONVERSION CLAUSE IS STRUCK AS UNATTRIBUTABLE (2026-09-09 00:2x)

§7.4 named an owner for a measurement: *"Owner: `systems` … one measured per-cell quota delta turns
§6.2's table from cells into quota and makes (a) decidable by arithmetic instead of argument."*
⛔ **STRUCK.** systems refused the ask as not answerable by the instrument it assumes, the helm
withdrew it, and both are right.

**The reason, and it is structural rather than practical:** the cells authenticate as the Studio's shared run account,
**which NINE roster seats share — including `systems` itself**, with three live on it
concurrently at 23:33. A before/after account reading measures **the account**, not **the cells**;
every other seat's consumption lands inside the subtraction.
⇒ 🔑 ***A DELTA ON A SHARED AGGREGATE ATTRIBUTES NOTHING.*** The number §7.4 named **does not exist at
the instrument §7.4 named.**
📌 If an attributable per-cell figure exists it will come from **the cells' own records**, not an
account panel — and specifying that instrument is `systems`', not this seat's.

### §9.1 — WHAT THIS DOES TO §7, AND WHY THE ANSWER IS "NOTHING"
**(b) DESCRIPTIVE stands, and it now rests ENTIRELY on the structural argument** — the affordable rungs
of (a) do not answer the question the arm exists to ask, so a partial (a) is (c) with a bigger n, and
only the 805-cell rung is honest.
⭐ **§7.4 closed with: *"(b) is right even if quota were infinite … stated so that a later quota
measurement is not mistaken for a reason to revisit §7."*** That line was written as belt-and-braces.
**It is now the only load-bearing one.**
⇒ 🔑 ***A RULING WITH TWO INDEPENDENT GROUNDS SURVIVES LOSING ONE — BUT ONLY IF BOTH WERE STATED AT
THE TIME.*** Had §7 rested on the quota arithmetic, this withdrawal would have reopened a decision
made blind, and the re-decision would have been made with the wave already fired. **Declaring a
ground's independence is cheap when written and unavailable afterwards.**
📌 Desk row **IR** is amended by the helm on the same measurement: its cell→quota clause struck, the
**2.0072× re-open trigger untouched** and still the live condition.

### §9.2 — MY OWN SHARE, STATED WITHOUT TAKING THE EXCULPATION AND WITHOUT INFLATING IT
The helm records the original framing as unanswerable *"through no fault of bench's."* **Half of that
I accept and half I do not.** The *unattributability* is a fact neither party held. But this seat's
block registration read *"PURELY A SPEND DECISION — roughly 15 cells of quota,"* which **named quota as
the binding constraint without ever checking that quota was attributable to a cell.**
⇒ 🔑 ***A CONSTRAINT NAMED WITHOUT CHECKING THAT IT IS MEASURABLE IS A DEFERRAL WEARING A DECISION'S
CLOTHES.*** It routed a question to a party who could not answer it, in a form that looked answerable.
⛔ Recorded at this weight deliberately: an over-generous attribution and an over-eager self-blame are
one error in opposite clothes, and this seat committed the second one earlier tonight within an hour
of refusing the first.

### §9.3 — THE RE-FIRE LANDED, AND THE §18 FENCE DEFECT IS PROVEN CLOSED
```
  15 cells · 4-wide · NEW root and NEW id prefix (§5.4: never pooled)
  fences rendered AFTER the population was final ....... 15/15, drift 0
  booted on first attempt .............................. 4 of 4   (vs six fast-deaths last wave)
```
⇒ **The ordering clause was obeyed, the census survived, and the fence-drift defect that cost this
campaign three cells and blocked sixteen is closed with a driven result rather than a repair note.**
⛔ **No price is read from these cells here, and none may be**: §7.2's four clauses and §6.3's
forbidden sentence bind whatever comes back.

---

## §11 — ⛔⛔ §6.3 WAS ONE-SIDED ON A TWO-SIDED FLOOR. CORRECTED, STILL BLIND. (2026-09-09 02:1x)

**systems found it and the helm re-derived it from the distribution rather than reading it off the
post. I have re-derived it a third time.** All three agree to the digit.
```
  z_0.975 = 1.959964 · z_0.80 = 0.841621 · k = (z+z)² = 7.8489
  floor F = exp(σ√(2k/n)) = 2.0072      1/F = 0.498216
  ⇒ the acceptance region is exp(±σ√(2k/n)) = [0.4982, 2.0072]
  ⇒ a ratio is UNRESOLVABLE iff |ln(ratio)| < σ√(2k/n) — SYMMETRIC IN LOG SPACE BY CONSTRUCTION
```
⛔ **§6.3 said only *"below 2.0072× ⇒ UNRESOLVED."*** That files **0.45** and **0.35** — both **outside
the band and therefore RESOLVED** — as *"nothing follows."*
⇒ 🔑 ***A ONE-SIDED TEST ON A TWO-SIDED FLOOR DOES NOT LOSE POWER EVENLY — IT LOSES IT ENTIRELY ON ONE
SIDE. AND AN INSTRUMENT THAT CAN ONLY FAIL TOWARD "NO SIGNAL" READS AS CONSERVATIVE AND IS NOT.***
📌 **The loss falls exactly where the placebo comes in CHEAPER than plain — the side on which a finding
would call the arm's validity into question.** My rule was written to stop over-claiming and it
suppressed the one result that says the instrument is broken.

### §11.1 — THE CORRECTED RULE: THREE REGIONS, NOT TWO
```
  premium > 2.0072          RESOLVED HIGH. Form drives cost; the finding is DAMAGED. PUBLISH.
  0.4982 … 2.0072           UNRESOLVED. Nothing follows. (unchanged)
  premium < 0.4982          RESOLVED LOW.  ⇒ PUBLISH. ⛔ NEVER "unresolved". ⇒ §11.2 FIRES.
```
This replaces §6.3's two-region form and propagates: **§7.2 clause 2** now reads *a premium clearing
**the band in EITHER direction*** is RESOLVED and published; **§5.2 / §6.4's** *a fortiori* admission
is likewise band-scoped, not threshold-scoped.
📌 **Matrix #1 is unaffected in fact** — all five premiums (1.1610 … 2.7306) sit on the high side, so
the low half never arose — **but the RULE as stated was one-sided and would have bitten the first arm
whose premium fell below 1.** *A defect that has not yet fired is still a defect; it was one arm away.*

### §11.2 — WHAT A RESOLVED-LOW RESULT MEANS, AND THE DISCRIMINATOR, REGISTERED BEFORE ONE EXISTS
A placebo costing **less than half** of plain is a **large effect of FORM ALONE**, and it has two
readings that a cost number cannot separate:
- **(a) THE PLACEBO SUPPRESSED THE WORK.** Then it is not "form without content" — it changed the task,
  and **it is not a valid control**: the content attribution `(salt/plain) ÷ (placebo/plain)` is void.
- **(b) THE FORM GENUINELY HELPS.** Structure gives process where a bare briefing flails. Then the arm
  is valid and the finding is real and interesting: **form cheapens while salt's content dearens.**

⇒ ⛔ **THE DISCRIMINATOR IS AN OUTCOME COMPARISON, NOT A COST ONE, AND IT IS MANDATORY:** on a
resolved-low result, compare **landing rate** (cells reaching a normal END with tests passing) between
`placebo` and `plain`.
```
  placebo lands at plain's rate   -> reading (b). The arm STANDS; publish the cheapening effect.
  placebo lands BELOW plain       -> reading (a). The arm is INVALID as a control for content-vs-form.
```
⇒ 🔑 ***A CONTROL THAT MOVES COST BY MORE THAN THE RESOLVABLE FLOOR IN EITHER DIRECTION IS NOT A NULL;
IT IS AN INTERVENTION, AND WHICH ONE IT IS CANNOT BE READ OFF THE COST IT MOVED.***
⛔ **And the limit on §11.2 itself:** a resolved-low result invalidates the **INTERPRETATION**, never
the **DATA**. The cells are real, they stay in the record, and they are published either way.

### §11.3 — THE TIMING IS THE REASON THIS IS WORTH ANYTHING
**LZW currently sits at 0.6595 — INSIDE the band.** ⇒ **systems raised a one-sided-test defect while
the affected side had not fired**, which is the only moment at which fixing it is not selection on
outcome. **Registered blind, for the fourth time in this document, and for the same reason each time.**
⭐ **And the helm routed it instead of ruling it** — *"§6.3 is bench's, bench is the lead, and bench is
lit; ruling a lead's design clause because I happen to be awake is the failure the two-level card
names."* **Recorded because a routed ruling and a taken one leave identical artefacts, and only the
routing shows in the record if someone writes it down.**

### §11.4 — ⛔ THE DISCRIMINATOR I JUST REGISTERED WAS INERT. POOLED, IT WORKS. (same sitting, 02:2x)

§11 closed by naming a RISK: *"landing rate is a RATE on 3 cells and will itself often be
UNRESOLVED."* **I left it as a risk instead of computing it. Computed:**
```
  per-problem, 3 v 3, Fisher one-sided:
    the ONLY resolvable table is  placebo 0/3 vs plain 3/3,  p = 0.0500
    ⇒ 1 resolvable table out of 16. Every other outcome is UNRESOLVED.
```
⇒ **§11.2's discriminator, as written, is INERT** — it decides the arm's validity on one table in
sixteen. ⇒ 🔑 ***A DISCRIMINATOR REGISTERED WITHOUT ITS OWN POWER CALCULATION IS A DEFERRAL WEARING A
DECISION'S CLOTHES*** — my own phrase from §9.2, earned again, in the clause I wrote to close §9.2's
lesson. **Naming a risk is not pricing it.**

**THE FIX, AND IT IS AVAILABLE BECAUSE THE QUESTION IS ARM-LEVEL:** *"did this briefing suppress the
work?"* is a property of **the briefing**, which is identical across problems. ⇒ **the rate POOLS
across all five: 15 placebo vs 15 plain.**
```
  pooled 15 v 15, against plain 15/15:  placebo ≤ 11/15 RESOLVES  (11/15 -> p=0.0498)
                                        vs 1 table in 16 per-problem
```
⛔⛔ **AND THE DISTINCTION THAT MAKES THIS LEGITIMATE, BECAUSE IT LOOKS LIKE THE POOLING THIS CAMPAIGN
FORBIDS:** pooling a **RATE** across problems is sound here because the briefing is constant across
them. Pooling **COST** across problems is **NOT**, and never has been — problems differ by orders of
magnitude in cost, which is why every premium in this campaign is per-problem.
⇒ 🔑 ***THE SAME DATA, TWO POOLINGS, ONE LEGITIMATE AND ONE NOT — AND THE DIFFERENCE IS NOT THE DATA,
IT IS WHAT THE QUESTION IS ABOUT.*** A reader who checks "does this campaign pool across problems?"
gets the wrong answer in both directions.

⚠️⚠️ **DISCLOSURE, BECAUSE THIS IS NOT A FULLY BLIND REGISTRATION AND SAYING SO IS THE WHOLE POINT.**
Before deriving the above I read the re-fire's per-cell END status at the object: **12 of 15 cells
landed (`END LANDED`), 3 Paxos still running.** ⇒ **I therefore knew ONE arm's landing behaviour when I
chose this rule**, and reading (a) — *the placebo suppressed the work* — already looked unlikely.
⇒ **What I have NOT seen: any placebo COST, any premium, and `plain`'s landing rate in this
comparison.** The discriminator's actual inputs are still closed to me.
⇒ ⭐ **AND THE DIRECTION OF THE CONTAMINATION IS AGAINST THIS CAMPAIGN, WHICH IS WHY THE RULE STANDS:**
pooling makes the test **STRICTER** — it converts an almost-never-firing check into one that fires on
any placebo landing ≤ 11/15. **A partial un-blinding that makes the instrument harder to pass cannot
manufacture a flattering result.** ⛔ Had the fix run the other way — a change that made the arm easier
to validate, chosen after glimpsing that it was landing well — **it would be void under §10 and I
would have had to leave the inert version standing.**

---

## §12 — CLOCK ERRATUM: EVERY SECTION STAMP IN THIS FILE IS DERIVED, NOT MEASURED

⛔ **I never ran `date` before writing a single section header tonight.** Each stamp was inferred from
the helm's bus-post times — **and eight of the helm's nine stamps were themselves hand-typed, running
up to 65 minutes ahead.** My stamps drifted the same way, less far, and **all in one direction: late.**

**THE AUTHORITATIVE CHRONOLOGY IS THE COMMIT CLOCK, which is machine-written:**
```
  §5    ruled  23:09:03   (stamped "23:1x")     ba7d3dd
  §6    ruled  23:27:43   (stamped in §6 head)  11597f8
  §7    ruled  23:41:32                         3428344
  §8    ruled  00:09:35   (stamped "00:1x")     e7bd838
  §9    ruled  00:19:48   (stamped "00:2x")     e5ccdd7
  §11   ruled  02:04:59   (stamped "02:1x")     0863a52
  §11.4 ruled  02:08:57   (stamped "02:2x")     c76dd18
  notices      02:23:08                         7579946
```
⇒ 🔑 ***A TIMESTAMP COPIED FROM ANOTHER PARTY'S DOCUMENT IS NOT A MEASUREMENT — AND IT INHERITS THAT
PARTY'S ERROR SILENTLY, WITH NO CHANNEL THAT CAN REPORT IT.*** Mine were not even drift: **drift is a
clock going wrong; I read a number off someone else's page and wrote it down as an observation.**

### §12.1 — WHAT THIS DOES AND DOES NOT AFFECT, BECAUSE THE DISTINCTION IS THE WHOLE POINT
⛔ **NOT affected — and this is the part that matters:** every **blind-registration** claim in this
file rests on **ORDER relative to the DATA**, never on absolute clock time. §5 was ruled before any
re-fired price existed; §6 before any placebo premium; §11 while LZW sat **inside** the band; §11.4
with the disclosure that I had seen END statuses and nothing else. **The commit order above confirms
each of those orderings and none of them moves.**
⚠️ **Affected:** any reconstruction that interleaves my sections with another seat's events **by
stamp**. An auditor asking *"did bench rule this before systems measured that?"* would be comparing my
inflated numbers against the helm's more-inflated ones. **Use the commit times above and the bus BYTE
OFFSETS, which are the only monotonic order on that record.**

### §12.2 — NOT REWRITTEN IN PLACE, FOR THE SAME REASON AS EVERY OTHER CORRECTION HERE
The stamps stay as typed. **Rewriting them would erase the evidence that this file's chronology was
ever derived rather than measured** — and this document has kept six superseded clauses standing for
exactly that reason. **This section is the correction; the stamps carry a pointer, not a patch.**
✅ **ADOPTED, one line:** *`date` runs in the same command that composes any text carrying a time, and
its output is interpolated — never typed, and never read off another party's post.*

### §11.5 — THE LANDING-RATE DISCRIMINATOR MUST EXCLUDE INFRASTRUCTURE NON-LANDINGS (registered blind)

§11.2/§11.4 decide the placebo's validity from a **landing rate**: if the placebo lands below plain,
reading (a) — *the briefing suppressed the work* — is supported. ⛔ **That inference requires every
non-landing to be ATTRIBUTABLE TO THE BRIEFING, and I registered it without saying so.**

**Observed live while `rf13paxo` was still running, which is why this is registrable blind:**
```
  token spend  FLAT across 5 consecutive METER lines (09:55:41 → 09:59:42, 20792016 each)
  transcript   FLAT, 1,582,116 B, delta 0 over 8 s
  yet ALIVE    rf13paxo/repo/target/debug/driver, etime 08:39 — a SUBJECT-FORKED binary
```
⇒ **The agent is blocked on a subprocess, not stalled.** And §8.6 already records that **nothing reaps
what the subject forks.** ⇒ **A subject-forked binary that never returns burns the cell to `CAP-WALL`
and produces a NON-LANDING that says nothing whatever about the briefing.**
⇒ 🔑 ***A RATE IS ONLY EVIDENCE ABOUT THE THING IT VARIES WITH, AND I BUILT A DISCRIMINATOR ON A
DENOMINATOR THAT MIXES TWO CAUSES.*** The placebo arm cannot be convicted of suppressing work by a
cell that died holding a hung compiler.

**⇒ THE RULE: before §11.4's pooled 15 v 15 is computed, every non-landing is CLASSIFIED at the cell:**
```
  SUBJECT non-landing       the agent finished and its work did not pass      -> COUNTS
  INFRASTRUCTURE non-landing  CAP-WALL/CAP-TOKENS while blocked on a
                              subject-forked process, harness fault, boot
                              failure, killed watcher                        -> EXCLUDED, and the
                                                                                exclusion PUBLISHED
```
⛔ **Both arms are classified by the same rule and the counts are published for each** — an exclusion
applied to one arm only is the defect this whole document exists to prevent.
⛔ **AND THE EXCLUSIONS ARE PUBLISHED WITH THE RATE, NEVER FOLDED INTO IT.** *A refusal that reports
its own scope is not a blind spot;* a denominator quietly reduced is.
⚠️ **Residue, stated:** classification is a judgement at the cell and I am registering the CATEGORIES,
not a mechanical test. A cell whose subject forked a hung process **because the briefing led it there**
is genuinely ambiguous — and I am not pretending otherwise. **If that case arises, it is published as
ambiguous rather than assigned.**

### §11.6 — THE LANDING-RATE HALF OF §11.2's DISCRIMINATOR IS SETTLED, AND IT IS SETTLED BEFORE ANY COST

**The re-fire is complete: 15 of 15 cells reached a normal END.** `rf13paxo` closed
`POST-END LANDED at-end T 25083474 cost 22.1918` — the last of them.
```
  placebo re-fire landings ......... 15 / 15
  INFRASTRUCTURE non-landings ...... 0   ⇒ §11.5's classification has nothing to classify
```
⇒ **Reading (a) — *the placebo briefing suppressed the work* — is pre-empted.** An arm that suppresses
work does not land fifteen of fifteen. ⛔ **Formally: §11.2's discriminator FIRES only on a
resolved-low COST result, and no cost is known to this seat.** So this does not trigger it; **it
determines its landing-rate input in advance.**
⇒ ⭐ **AND THAT IS THE WHOLE VALUE OF SAYING IT NOW.** §11.4 was registered with a disclosed partial
un-blinding (I had seen 12/15 END statuses). **This closes the same input at 15/15 while every price
remains unseen** — so if a resolved-low premium arrives, the validity question is already answered and
cannot be answered *by* the premium that raised it.
⇒ 🔑 ***AN INPUT TO A DISCRIMINATOR SHOULD BE FIXED BEFORE THE INPUT THAT WILL TRIGGER IT — otherwise
the trigger and the adjudication are drawn from the same reading.***
⛔ **WHAT THIS IS NOT:** not a cost, not a premium, not a content-vs-form verdict, and **not a claim
that the arm is valid** — §11.2's reading (b) requires the comparison to plain, which is systems'
to compute and mine only to have ruled on. §7.2's four clauses and §6.3's forbidden sentence bind
unchanged.
📌 Plain's landing rate is NOT known to this seat and is the other half of the pooled 15 v 15.

---

## §13 — THE ARM IS CLOSED. IT RETURNS **UNRESOLVED** ON ALL FIVE PROBLEMS, AND THAT SUPPORTS NOTHING.

**systems reported under §7.2 and offered no verdict, correctly** — *"the §7.2 table licenses the cost
column and nothing else, and its reading is bench's."* This is the reading.
```
  the arm        15/15 END LANDED and priced · $193.42 · 0 void · 0 cap · 0 drift · 0 failed boots
  the result     ALL FIVE problems UNRESOLVED, inside the band [0.4982, 2.0072]
  region         §11.1's MIDDLE region on every problem
  reading (a)    NOT triggered — and §11.6 had already pre-empted it at 15/15 landings
```

### §13.1 — WHAT IT ESTABLISHES: **NOTHING ABOUT ITS OWN QUESTION**
⛔ **The placebo arm does not answer content-vs-form, and it was never going to.** §6.2 registered
exactly this before a cell existed: at n=3 the floor is 2.0072× while salt's own premiums on Crc32
(1.1610), LZW (1.3749) and LRU (1.4465) sit **below** it. **An UNRESOLVED result was the predicted
outcome, and it arrived.**
⛔⛔ **§6.3's FORBIDDEN SENTENCE REMAINS FORBIDDEN AND IS NOW LIVE RATHER THAN HYPOTHETICAL:** *"the
placebo came in near plain, so salt's premium is real method."* **That sentence is exactly what this
result looks like and exactly what it does not say.** systems reached the same line unprompted — *below
floor is the expected outcome of an underpowered arm whatever the truth is* — and I record its
agreement because **two parties independently declining the same flattering reading is the only
evidence that the prohibition is load-bearing rather than decorative.**
⇒ 🔑 ***THE ARM DID NOT DAMAGE THE FINDING. THAT IS NOT SUPPORT FOR THE FINDING.*** The distinction is
the entire product of this document.

### §13.2 — THE DISPOSITION, UNDER §7.3's OWN TRIGGER
§7.3: *"if the descriptive wave shows ANY premium CLEARING the 2.0072× floor, the placebo question
becomes live and the 805-cell rung returns as a Captain-tier spend."*
⇒ **No premium cleared the band in either direction.** ⇒ **THE TRIGGER DID NOT FIRE. (a) stays off
the table, the 805-cell rung is not bought, and (b) DESCRIPTIVE stands as the final disposition** —
default-if-silent to the Captain, who may still overturn it.

### §13.3 — WHAT $193.42 BOUGHT, STATED PLAINLY BECAUSE IT IS THE UNCOMFORTABLE PART
**This arm cost $193.42 and returned no information about the question it exists to ask.** ⛔ **That is
not an execution failure** — systems ran it clean on every axis it controls. **It is a DESIGN property,
registered in §6.2 before the spend.**
⇒ **What it bought is a REFUTATION THAT DID NOT ARRIVE.** §7 authorised it on exactly that basis:
*an arm that can only hurt you is worth running.* It could have cleared the floor and damaged a 5/5
headline; it did not. ⇒ 🔑 ***A NULL FROM AN ARM THAT COULD ONLY HURT YOU IS WORTH ITS PRICE AND IS
STILL NOT EVIDENCE FOR YOU*** — and a campaign that cannot hold both halves of that sentence will
spend the money and then quote the null.
📌 **And the cheaper lesson for the next arm, which §10.2 already carries: the question "what can this
arm resolve?" costs nothing before the cells and $193.42 after.**

### §13.4 — WHAT REMAINS OPEN, AND IT IS NOT THIS ARM
⚠️ **systems leaves one thing open and I am carrying it forward rather than closing it:** *the
harvester grace guard is DEPLOYED AND UNPROVEN* — 14 of 15 graces were 6–7 s and only `rf06free`
(pre-fix) took 191 s. ⇒ **0 NO-COST after the fix is evidence about the CELLS, not about the GUARD.**
**The clean run must not be read as a verified fix**; its first real exercise is the next cell that
ends busy. ⇒ 🔑 ***A GUARD THAT NEVER MET ITS CASE IS UNTESTED NO MATTER HOW GREEN THE RUN AROUND IT
WAS*** — the same shape as a gate whose red arm was never driven.

---

## §14 — ⛔ THE FLOOR IS PER-PROBLEM, AND `n` IS NOT UNIFORM. §11.1's SINGLE BAND WAS TOO NARROW ON TWO.

Measured at the object while auditing desk row `HC`'s completion test — **cells per (problem × arm),
ENDed only, across `cells-matrix1` and `cells-placebo-refire`:**
```
              placebo   plain   salt-diet
  Crc32          3        3         3
  FreeList       3        2 ⛔      4
  LRU            3        3         4
  LZW            3        6         6
  Paxos          3        2 ⛔      4
```
⛔ **`plain` is at n=2 on FreeList and Paxos.** Every floor in §6.2, §11.1, §11.4 and §13 was stated as
a single number for all five problems — **`n=3 ⇒ floor 2.0072×`** — and that is **wrong on two of
them.**
```
  n=3  floor 2.0072   band [0.4982, 2.0072]
  n=2  floor 2.3474   band [0.4260, 2.3474]   <- FreeList, Paxos
```
⇒ 🔑 ***A FLOOR IS A FUNCTION OF n, SO A SINGLE FLOOR IS A CLAIM THAT n IS UNIFORM — AND I NEVER
CHECKED.*** The registered σ made the arithmetic feel settled; the **denominator** was the unchecked
half, on a campaign that has corrected four denominators tonight.

### §14.1 — BOTH CONCLUSIONS SURVIVE, AND I CHECKED RATHER THAN ASSUMING
- **§13's *"all five UNRESOLVED inside the band"* — UNCHANGED.** The true band on FreeList and Paxos is
  **WIDER** (`[0.4260, 2.3474]`), and a wider band contains strictly more. **An error that made my
  stated band too NARROW cannot have admitted something a correct band excludes.**
- **matrix #1's magnitudes on those two — UNCHANGED.** FreeList **2.7306** and Paxos **2.6514** both
  still clear their true n=2 floor of **2.3474**. ⇒ **RESOLVED on the correct arithmetic, not only on
  the convenient one.**
⇒ **So this corrects the STATED RULE and moves no result.** ⛔ **Which is exactly when a correction is
easiest not to publish**, and the reason it is here: *the next arm's n will differ again, and the rule
is what that arm will inherit.*

### §14.2 — THE RULE, RESTATED CORRECTLY
**Every floor, band and admissibility test in this document is evaluated at the n OF THE COMPARISON IT
JUDGES**, which is `min(n_arm1, n_arm2)` for that problem — **never at a campaign-wide n.** Any table
publishing a floor **prints the n it was computed at**, beside it.
📌 §11.4's pooled 15 v 15 is unaffected: it pools a RATE over the ARM, not a per-problem magnitude.

### §14.3 — AND STAGE 1 IS NOT LANDED. THE GAP IS TWO CELLS.
Desk row `HC`'s test is *"stage 1 landed at n=3 on both problems."* ⛔ **Two defects in that sentence:**
its premise says **"LZW, CRC-32 — the only two that exist"** while **FIVE problems are built and run**;
and **stage 1 is at n=3 on three of five** — `FreeList` and `Paxos` need **one `plain` cell each.**
⇒ **The row stays OPEN, its scope corrected and its gap named as two cells** — not as "stage 1 is
outstanding", which is what it read as before and what nobody could act on.
