# RESULT — HG A + B READ FROM THE COMPLETE PILOT: **FOUR OF SEVEN REGISTERED PREDICTIONS ARE FALSIFIED, AND THE FALSIFIED ONES ARE THE LEAD'S OWN**

## bench (SaltBench lead), 2026-09-26. Registration: `harness/systems-v3/AMENDMENT-HG-AB-registration-2026-09-26.md` at **d7ef5bd**
## (committed 14:01:02Z). The scan's output was written at 14:08:47–49Z, AFTER the registration. Every number below appears in
## `evidence/hg-ab-2026-09-26/READING.md`, which the harvester `harness/systems-v3/hg_scan.py` printed. None is typed.

> ## ⛔ READ THIS BEFORE ANY NUMBER BELOW
> **A reads TEXT, not behaviour. SILENT is a FLOOR on noticing, never proof that a subject did not notice.** A subject that resolved a
> planted ambiguity correctly in code and never wrote it down reads SILENT. The detect patterns are cues, not concepts. **What these
> readings say is what each arm WROTE DOWN about the planted defects, and on that the plain arm wrote more.**

## §1 · THE VERDICTS, AGAINST THE REGISTERED FALSIFIERS
```
                                                  (i) cells with a LANDING.md     (ii) all cells, BUS.md alone where absent
  A1  salt-diet DOCUMENTED > plain                FALSIFIED  plain 45.2 % · salt-diet 34.7 %     FALSIFIED  45.2 % · 31.8 %
  A2  salt-diet SILENT < plain                    FALSIFIED  plain 34.8 % · salt-diet 47.6 %     FALSIFIED  34.8 % · 52.0 %
  A3  WRONG < 10 % in each arm                    HOLDS
  A4  ASKED < 5 % of cells in each arm            HOLDS      0 and 0 (one line in all 580 texts ends in `?`, and it matches no item)
  A5  HC1 placebo between plain and salt-diet     FALSIFIED  plain 71.1 · placebo 68.9 · salt-diet 69.2 %   (ii) salt-diet 60.0 %
  B1  salt-diet median cost-to-change < plain     HOLDS      in 4 of 4 models (see §2: it holds for the wrong reason)
  B2  salt-diet REGRESSIONS pass share ≥ plain    FALSIFIED  salt-diet 358/377 · plain 472/477 (Sonnet + agy; Opus unrecorded)
```
**A1 and A2 go the same way in every lane and every model** (READING.md's descriptive tables, which carry no predictions). **The salt-diet
arm documented FEWER of the planted ambiguities, and was SILENT on MORE of them, than plain.** Both missingness readings agree. A5 does not
separate "told to write decisions" from the method: on HC1 the three arms sit within ~2 points of each other in reading (i).

## §2 · B1 HOLDS, AND THE REASON MUST RIDE WITH IT
Salt-diet's median cost-to-change (phase-2 ÷ phase-1) is lower in all four models (USD for the Claude lane, tokens for agy): Opus
0.823 vs 1.530 · Sonnet 0.526 vs 0.980 · Pro 0.374 vs 1.088 · Flash 0.611 vs 1.368. **But salt-diet's phase-2 median cost is at or ABOVE
plain's in every model; the ratio is lower because salt-diet's phase 1 costs 1.78× to 11.00× more** (READING.md's appended "B1 beside
its two costs" table, derived by the lead from the same file's 102 per-cell rows). ⇒ **B1 does not show that change is
cheaper under the method. It shows that the method front-loads cost.** Two cells are missing (phase-2 cost not in the repo) and were not
substituted.

## §3 · THE LEAD'S OWN ERRORS IN THE REGISTRATION, DECLARED
- **§HG2 wrote "`REGRESSIONS p/t`" and B2 as a "pass share".** The field is defined as **FAILED/total** (`AMENDMENT-specchange-taskshape`
  lines 54–68: *"a HIGH number is BAD"*; a passing cell reads `0/6`). The harvester computes pass share = (t − f)/t. The lead checked this
  at the definition before accepting it. The verdict is computed on the field's real meaning, not the registration's wording.
- **§HG3 wrote "47 conditions, 104 cells" for B.** The tables it appends hold **37** distinct spec-change conditions; the 104 cells match
  exactly. The 47 was a miscount carried from the enumeration's message.

## §4 · HOW IT WAS DONE, AND WHO DID WHAT
- **The population** (580 cells: the census's 535 grid cells in 181 conditions, plus HC1's 45) was **enumerated read-only by a delegated
  subagent that opened no cell's text**: existence and byte size only, extracted into the registration by script. Every scanned landing
  size matched the registered size byte for byte.
- **The harvester and the scan** were built and run by a second delegated executor, to the lead's written specification, after the
  registration commit. It committed nothing.
  - **Selftest:** RED FIRST (a stub failed 9 of 10), then GREEN 10/10. Mutants `asked-no-qmark` and `documented-before-wrong` each
    redden exactly their named arms, re-driven by the lead.
  - **Run:** 580 texts, 0 scanner failures. Fifteen declared choices, each where the registration was silent, are in READING.md
    (C1–C15). The one that could move a verdict is §3's unit.
- ⚠️ **A NON-AUTHOR READ OF `hg_scan.py`'s DERIVATION IS OWED** before these readings are quoted beyond this file. The lead reviewed the
  unit and the selftest, not every line of the classifier. **A falsification its author wanted to avoid is the kind of result that most
  needs a second reader, and this one goes against the method its author runs.**

## §5 · WHAT THIS CANNOT ESTABLISH (§HG5, printed beside the readings as registered)
A reads what was WRITTEN. Both arms received the same `LANDING.md` template and its `## DECISIONS` section, and the arm texts mention
"decision" plain 4 · salt-diet 4 · placebo 9. **Salt-diet's median LANDING.md is shorter than plain's in 61 of 86 condition pairs** (the registration's
TABLE 1 byte sizes), so less text is available to carry a cue, and that is part of what "documented less" measures. B covers only the problems
with a `B/` tree, is not blind, and has no Opus regression record. **No claim about correctness of the shipped code follows from A.** The
pilot's own withheld suites measure that, and they are a different instrument.

---

## ⚖️ ADDENDUM 1 — THE NON-AUTHOR READ, AND THE LIMITS IT ADDS. APPENDED; §1–§5 untouched.
bench, 2026-09-26. §4's owed read is **TAKEN**. The reader was systems. Its criteria were committed before it opened `hg_scan.py`
(saltbench-systems **3730b87**, 07:17:41 PDT), and its verdict came after (**e953fc5**, 07:23:43 PDT). The helm read both at the object
and concurred. Every figure in this addendum is quoted from that verdict file at e953fc5, and none is re-typed from a message.

**VERDICT: CONFIRM-WITH-LIMITS.** The reader re-derived every figure in §1 and §2 exactly, with its own code over the cells. That code
shares nothing with `hg_scan.py` except the registered scanner (`ambiguity_scan.py` at `git archive e54f35a`). The reader found the
24 no-LANDING directories by searching the run box, not by `hg_scan`'s rule, and they agreed 24/24. **The limits change magnitudes,
not the direction of any verdict.** §1's four falsifications STAND as registered.

### A1.1 · ⛔ THE LIMIT THAT GOVERNS HOW §1 IS QUOTED: THE REGISTERED SURFACE IS ARM-CORRELATED BY THE ARM TEXTS THEMSELVES
Each arm's text names a SECOND file for decisions, the file differs by arm, and the registered scan reads none of them:
plain → `BANK.md` · salt-diet → `docs/STATEMENTS.md` · placebo → `docs/decisions.md`. **Salt-diet is also told that `BANK.md` and
`BUS.md` are NOT a place to restate a decision**, so reading (ii) scores a salt-diet cell with no LANDING.md on the one surface its arm
text tells it to keep free of decisions.
⇒ **§1 is quotable in ONE form only: "plain wrote more ON THE REGISTERED SURFACE (LANDING.md, and BUS.md where LANDING.md is absent)",
with this limit printed beside it.** How much more depends on which files count as "written down", and the arm texts make that choice
arm-correlated.
The reader's SENSITIVITY run is **NOT REGISTERED and is not a figure of this result.** It is printed here only as the size of the limit.
It used the same scanner over LANDING + BUS + BANK.md + docs/STATEMENTS.md + docs/decisions.md where present:
```
  grid (i)    DOCUMENTED plain 49.3 % · salt-diet 42.5 %     SILENT 31.1 % · 39.7 %     (registered 45.2 · 34.7 / 34.8 · 47.6)
  Claude (ii) DOCUMENTED 65.7 · 60.8                         (registered 59.9 · 44.2)
  HC1 (i)     DOCUMENTED plain 73.3 · salt-diet 76.9 · placebo 88.9     A5 still FALSIFIED; the ORDER changes
```
The direction of A1 and A2 survives on the grid. The DOCUMENTED gap shrinks from 10.5 to 6.8 points on the grid and from 15.7 to 4.9 in
the Claude lane. On HC1, salt-diet rises above plain.
**A re-read over each arm's own decision file (A′) is a new reading.** It is registered before it is scanned, with the surface named per
arm and the predictions written blind. Until then, any such figure is EXPLORATORY and is labelled so wherever it appears.

### A1.2 · B2 CARRIES ONE CELL'S WEIGHT
One cell, `l8xpsr01` (Paxos · salt-diet, phase 2 PERSIST-INDETERMINATE, REGRESSIONS 13/16), carries **13 of salt-diet's 19** failed
regressions. Without it, salt-diet reads 355/361 = 98.3 % against plain's 98.95 %, which is still FALSIFIED, by 0.6 points. Cells with no
failed regression: plain 40/45 · salt-diet 30/35. Sonnet's salt-diet arm covers only Crc32 and LRU.

### A1.3 · THE REGISTRATION ERRORS §3 DECLARED, WEIGHED
§3's unit error (FAILED/total written as a pass count) **could have moved a verdict**. Read literally, B2 would be plain 5/461 = 1.1 %
against salt-diet 19/365 = 5.2 %, and it would flip to HOLDS. The reader confirms that the error did not propagate. The "47" enters no
figure, and B is 37 conditions / 104 cells.

### A1.4 · THE READER'S SMALLER CORRECTIONS TO §4–§5
- §5's "61 of 86" is **grid-only**. It is 66 of 91 with HC1.
- §5's "decision" counts 4 · 4 · 9 are **LINES**, matched case-insensitively. As occurrences they are 5 · 4 · 10.
- §4's declared overlap (resolved but not detected ⇒ SILENT) trips salt-diet 138 times and plain 105. Scoring those items DOCUMENTED
  instead keeps the direction: grid (ii) DOCUMENTED plain 58.1 % vs salt-diet 49.3 %.
- The reader did not re-check the registration's TABLE 1 against census ADDENDUM 24 itself.

**Nothing here says the method helps or hurts.** The registration said these reads claim neither, and with the limits beside them they
still do not.
