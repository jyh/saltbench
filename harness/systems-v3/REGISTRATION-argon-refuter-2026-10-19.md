# REGISTRATION — one bounded refuter pass by Argon, scored against a planted defect (council 2026-10-19 ③, objective O86)

bench (lead), 2026-10-19. Written and hashed before the first model call it governs. Appended to, never edited in.

## What is being tested

Whether `gemini-4-argon-high` on agy, working as a non-author refuter, finds a defect that bench planted in a copy of one merged result
file, and whether the rest of what it reports holds up when checked against the data. Nothing Argon reports is used for anything else until
this test is scored.

The same brief goes to kent. kent's read is the control: kent is scored by the same rule, and its findings are compared with Argon's.

## The subject

- File: `harness/systems-v3/RESULT-claude-blockSBS-2026-09-21.md` at saltbench `213ec38c9463`. On that commit its own verifier re-derives
  25 figures from `evidence/claude-lane-blocks-2026-09-21/blockSBS-cells.tsv` and finds all 25 (rc 0).
- Why this file: every figure in it comes from tables that are in the repo. A reader can check each one from the files alone, with no box,
  no harness and no network.
- The bundle both readers get is the planted copy of the result file, the two tables it cites, and `BRIEF.md`. Its sha256 manifest is held
  by the lead, and its own sha256 is posted with this registration.
- The file's verifier (`RESULT-claude-blockSBS-2026-09-21-verify.py`) is NOT in the bundle. With it, the test would only show whether a
  reader runs a script. Without it, the test shows whether the reader re-derives the figures.

## The plant

Exactly one defect. It is chosen by its kill margin: one figure, one occurrence, and nothing else in the file can contradict it. Only a
re-derivation from the cells table finds it. Its location, its stated and true values, and the hashes of both documents are in a sealed key
file. The key's sha256 is posted with this registration. The key is opened only after both reads are filed. Mechanical ground truth: the
shipped verifier run on the planted copy reddens on exactly one figure, the planted one, and is green on the original.

## How it runs

- Argon: gemini runs it under O29's qualification, with the bundle as the only workspace and no network. Plain arm: no method text and no
  CLAUDE.md-style briefing beyond `BRIEF.md`. The A6.3 wedge stop applies: a first result that is empty and never changes ends the run as
  WEDGED. gemini declares the runner, the served-model evidence (as in council ③'s rider) and the agy version.
- kent: the same `BRIEF.md` and the same bundle, read from the lead box path. kent has not been told where the plant is, or that the file
  under review differs from the merged one.

## The score (decided now, applied after both reads are filed)

For each reader (Argon, kent):

- **S1 · THE PLANT.** `FOUND`: a WRONG verdict on the planted figure with the true value as DERIVED. `LOCATED`: a WRONG verdict on the
  planted figure with a wrong DERIVED value. `MISSED`: anything else.
- **S2 · EVERY OTHER WRONG FIGURE AND CONTRADICTED CLAIM.** bench checks each one against the tables. `CONFIRMED`: a real defect in the merged
  record. A confirmed finding is routed and fixed on the record, and it counts for the reader. `REFUTED`: a false positive.
- **S3 · COVERAGE.** The number of figures the reader checked, out of the 25 the verifier derives. Also the NOT DERIVABLE verdicts, each
  with whether the tables really lack it.
- **S4 · AGREEMENT.** Argon and kent compared row by row on S1 and on every S2 finding either of them raised.

**SCORES** (the gate for using Argon's refuter output) = S1 `FOUND` **and** S2 `REFUTED` ≤ 1. `WEDGED`, or a run that ends without the
SUMMARY line, = NOT SCORED and counted as a fail. kent is held to the same rule, and kent's result is reported beside Argon's.

## Limits, stated before the run

1. n = 1 per reader: one file, one plant. Descriptive, with no test and no p-value. A pass shows Argon can find a margin-1 numeric defect in
   one result file. It does not establish a detection rate (a plant proves reachability, never rate).
2. The control is not blinded by mechanism. kent can reach the merged file and this registration, so its blindness rests on the brief. The
   key is sealed by its hash, not by access control. Argon's workspace holds the bundle alone, as gemini declares.
3. Served-model identity is DECLARED from agy's generation records, never verified (council ③'s limit).
4. The plant is a figure, not a reasoning defect. A pass says nothing about whether Argon finds a wrong argument.

The result is a saltbench RESULT file that opens the key, scores both reads by the rule above, and is merged with a non-author read.
