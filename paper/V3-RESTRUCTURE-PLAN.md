# THE v3 RE-ARCHITECTURE — A SECTION MAP, WRITTEN BEFORE ANY PROSE MOVES

`paper`, 2026-09-09, on the Captain's ruling *"No, the paper should be about v3"* (helm carry, 12:3x)
and on this seat's own recommendation, posted with both arms before it was taken.

⚖️ **WHY A MAP AND NOT A DRAFT.** The ruling is seven words, `PUBLISH-CHECKLIST.md` section (o)
records a live label ambiguity inside it, and the artifact is 21 pages. **A re-architecture executed
straight into prose is unreviewable**: the Captain would have to read a new paper to find out whether
it is the one he asked for. This map is two minutes to read and says exactly what moves, what is
compressed, what is cut and what has to be written new. ⇒ **It is the first deliverable of the
restructure, not a substitute for it.**

⛔ **NOTHING IN `saltbench-v1.tex` IS MOVED BY THIS FILE.** The paper at `main` is correct as it
stands and remains the artifact until this map is ruled on.

---

## 1. THE CLAIM THE NEW PAPER MAKES, IN ONE SENTENCE

**A referee-gated, pre-registered protocol was run on a seat-as-subject cost matrix, and what it
produced that is worth publishing is what it CAUGHT — about itself, and about measuring method
effects at all.**

⛔ **WHAT IT DOES NOT CLAIM, AND SECTION (l) BINDS THIS:** any Salt effect; any capability result on
the v3 population; and the premium as a headline. **The premium is the occasion, not the claim.** v3
is a COST result with **N = 0** referee verdicts on a withheld suite, three of five magnitudes below
its own resolvable floor under both readings, a gold pair at k = 1, and a one-sided test that cannot
significantly refute. Every one of those is in the paper today and stays.

⇒ 🔑 ***THIS IS WHY THE RE-SCOPE MAKES THE PAPER STRONGER RATHER THAN RISKIER: it moves the headline
off the weakest thing the run supports and onto the strongest.*** Section (n) refused to advertise the
systems population precisely because the ratio could not carry a title. **A title about the protocol
and the instrument does not have that problem** — that material is the best-evidenced in the campaign.

## 2. THE SECTION MAP

| new | section | source | disposition |
|---|---|---|---|
| 1 | Introduction | §1, rewritten | **NEW PROSE.** Opens on the seat-as-subject question and the instrument answer. ~1 page |
| 2 | The seat-as-subject experiment | §3 (systems part) + §4.5 preamble | **MOVED UP AND EXPANDED.** What v3 is, why a cost matrix, the five authored components, the withheld suites |
| 3 | The protocol, as exercised on v3 | §2 whole (2.1–2.6) | **KEPT, RE-ANCHORED.** Each clause illustrated by what it did in v3 rather than in the abstract. Compresses ~20% |
| 4 | The v3 reading, at two readings | §4.5 whole | **THE CENTRE.** Unchanged in substance: both readings, the discharge with the divergence, the four qualifiers, the account boundary, correctness unmeasured |
| 5 | What the instrument caught | §5, expanded | **PROMOTED TO THE SPINE.** Today's findings plus the four this campaign added after §5 was written (below) |
| 6 | The reads that shaped the design | §4.1–4.4 + §3 (other populations) | ⚠️ **COMPRESSED, NOT CUT.** SWE-bench abandoned, the S2-Lean null and its triage, S2-Rust saturation. From ~13k chars to ~5k, as the reason v3 is shaped as it is |
| 7 | The treatment question, open | §6 | **KEPT.** Gap 2 is closed; three gaps stand |
| 8 | Reproducibility | §7 | **KEPT NEARLY WHOLE.** Add the render gate |
| A–C | appendices | unchanged | **KEPT** |
| D | v3 per-cell prices | new | **NEW.** The cell lists the scoreboard no longer prints, so the medians are recoverable by a reader |

## 3. ⭐ THE FOUR FINDINGS §5 DOES NOT YET CARRY, ALL FROM THIS CAMPAIGN

These are the reason section 5 can carry a paper. Each is measured, each is v3's, and **none is in
the paper today.**

1. **An instrument that states a reporting RULE in the grammar of a MEASUREMENT will be quoted as a
   measurement.** The scorer printed *"every per-problem magnitude is UNRESOLVED"*; the abstract
   quoted it faithfully and was false. Reading the paper against its own table found the symptom;
   only reading the scorer found the cause. **No gate could fire on either half.**
2. **A set that grows after a bound is written over it does not inherit the bound, and the growth is
   silent.** The box-load bound was stated over 37 cells; the declared set became 40 and nothing in
   the scoreboard, the premium or the p-value changes shape when an unbounded cell joins.
3. **A source and its rendering are two artifacts, and a repository can hold a correct one beside a
   stale one with every gate green.** A stale build fails toward LOOKING FIXED. Closed by a fifth
   gate the same day.
4. **An absence is a claim about the population the instrument could see.** A sweep over
   `git for-each-ref` measures what the checkout has fetched; a positive control drawn from the same
   truncated population fires correctly and proves nothing.

📌 **And a fifth that belongs beside them, already in §5:** a censored cap returns the cap; a
statistic is a cap's price only in the cap's unit; a gate can penalise the treatment for applying the
treatment; a screen's false positives are invisible until someone goes back for the refused cell; a
fence probed only in its sandbox's language cannot see the layer above it.

## 4. ⛔ THE TWO THINGS THIS MAP CANNOT DECIDE, AND THEY ARE THE CAPTAIN'S

1. **THE TITLE AND THE EDITION STRING.** Section (o) records the collision: `v1` is the paper's
   edition, `v3` is the campaign generation, and this repository never says they are different axes.
   Reading **(a)** keeps the edition and changes the subject; reading **(b)** says the edition label
   should have tracked the campaign. **The map above is identical under both** — only the title page
   differs, which is why the map could be written without the answer.
   ⛔ **`CITATION.cff` AND `\title{}` MUST MATCH BYTE FOR BYTE** whichever is chosen; they carry the
   same string twice today.
2. **HOW HARD TO COMPRESS SECTION 6.** The prior reads are real results with their own registrations
   — the pre-registered S2-Lean null and its blind triage in particular. Compressing them to context
   is defensible; **cutting them is not**, and this map does not propose it.

## 5. COST AND ORDER, SO THE WORK CAN BE PRICED BEFORE IT IS AUTHORISED

```
  1  section 5 -- write the four findings above          NEW PROSE, ~2 pages   INDEPENDENT of the title
  2  section 6 -- compress §4.1-4.4                      editing, ~1 page out  INDEPENDENT of the title
  3  sections 1-2 -- the new opening                     NEW PROSE, ~2 pages   needs the title decided
  4  section 3 -- re-anchor the protocol onto v3         editing               INDEPENDENT
  5  appendix D -- the per-cell price table              mechanical            INDEPENDENT
  6  the title page + CITATION.cff                       one line each         THE CAPTAIN'S
```
⇒ ⭐ **FIVE OF THE SIX ITEMS DO NOT NEED THE TITLE QUESTION ANSWERED**, so the restructure is not
blocked as a whole by section (o). It is blocked in exactly one place, and that place is one line.

⛔ **UNTIL THIS MAP IS RULED ON, THE UPLOAD STAYS GATED** — section (o). An upload prepared against
the wrong subject is not an improvement missed but a wrong paper published.
