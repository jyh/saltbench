# CLAIM AUDIT — what the published record says about the Claude cells' filesystem isolation
**bench, 2026-09-13. Ordered by maestro's §B7 row 3 ruling (14:22:21Z), which is READ-ONLY: this file
edits nothing published or merged, and nothing here asks for a number to move.**

> *"The census makes a fact about the CODE; what we have SAID is a separate population."* — the ruling

## ⇒ THE ANSWER IN ONE LINE
**NO PUBLISHED SENTENCE IS FALSE. ONE PUBLISHED SENTENCE IS UNEVIDENCED FOR PART OF ITS POPULATION,
and it is the paper's own inventory of what was in force.** Everything else is either correctly scoped
to v1, already disclosed at length, already withdrawn, or silent.

## THE CORPUS, AND HOW IT WAS READ
The four populations the ruling names: the paper as posted (`paper/saltbench-v1.tex`), the RESULT files
of record (**#115** P1 greenfield, **#117** P2 spec-change pair), `README.md`, and the harness docs —
29 files. Six needles (`sandbox · denyRead · fence · isolat · hermetic · containment`), **each count
taken beside a positive control needle in the same file**, because a zero from an instrument that is
not running is byte-identical to a zero from one that is.

## (iii) SILENT — **BOTH RESULT FILES OF RECORD**
```
  RESULT-p1-greenfield-2026-09-13.md   (#115)   81 lines   sandbox 0 · denyRead 0 · fence 0
                                                           isolat 0 · containment 0 · hermetic 0
                                                POSITIVE CONTROL in the same file: "cell" 18 · "cost" 2
  RESULT-p2-specchange-pair-2026-09-13.md (#117) 109 lines  all six needles 0
                                                POSITIVE CONTROL: "cell" 15 · "cost" 5
```
⇒ **The two result files that report Claude cells make NO containment claim of any kind.** ✅ **This is
the single most load-bearing finding of the audit**, because #115 and #117 are the documents a reader
reaches for the numbers. **Nothing in them has to be corrected, caveated or withdrawn.**

## (ii) STATES ONLY THE RENDERED FENCE / HOOK LAYER — `README.md`, AND IT IS ALREADY THE HONEST VERSION
> *"A fence denies the agent the network, the ground truth and the harness state, and the fence is
> measured by probes before the run. **The v1 probes spoke only the sandbox's language, and the layer
> above it (the agent's own file tool) was unfenced for every v1 episode**; amendment 17 … The gap was
> open and its measured exploitation is zero, **which is not the same as** …"*

⇒ **Explicitly scoped to v1, and it discloses its own gap in the same breath.** Nothing owed.

## (i) STATES THE OS LAYER AS ENFORCED OR VERIFIED — **TWO SENTENCES, BOTH IN THE PAPER, BOTH UNSCOPED**
```
  A  the abstract / opening
     "the agent is walled off from the network, the reference solutions and the harness itself, and the
      wall is tested by probes that try to breach it before any scored run, so THE ISOLATION IS
      OBSERVED RATHER THAN ASSUMED"
  B  §"The fence is measured, not assumed" (\label{sec:fence}), opening
     "The agent's subprocesses run under the operating system's sandbox (macOS Seatbelt through the
      agent harness's own sandbox settings): every host denied, writes only under the working copy and
      the session temp directory, reads denied …"
```

## ⛔ THE ONE SENTENCE THE CENSUS ACTUALLY BEARS ON, AND IT IS NEITHER A NOR B
Inside §sec:fence, the paper takes its own inventory — and this is the sentence, verbatim:
> *"**What was in force, each with its own evidence, was the subprocess sandbox**, the empty network
> allowlist, the shell-tool hook, the ground-truth leak check, and the audit layer."*

**For the v1/v2 episodes that clause is EARNED, and the paper says how, two sentences earlier:** *"The
smoke probe that had certified credential reads denied made its reads through the shell and through an
in-language process spawn, **both sandboxed**."* ⇒ **the subprocess layer WAS driven for that population.**

⛔ **BUT THE PAPER ALSO REPORTS THE v3 SYSTEMS CAMPAIGN, AND THOSE ARE CLAUDE CELLS.** Measured: **60+
of the paper's 125 `\src{}` citations point into `harness/systems-v3/`**, and they are not only
pre-registrations — they include `RESULT-matrix-opus-1`, `RESULT-n3-topup`, `RESULT-posthoc-
correctness`, `RESULT-statement-arm`. **And the paragraph opens by claiming exactly that reach:** *"The
third finding arrived after every read reported in this paper **and applies to all of them**."*
⇒ 🔑 ***SO "EACH WITH ITS OWN EVIDENCE" IS TRUE OF THE v1/v2 EPISODES AND UNEVIDENCED FOR THE v3 CLAUDE
CELLS THE SAME PAPER REPORTS.*** `cell-claude.sh` has no probe in its 256 lines; **124 Claude cells have
been launched and not one drove the layer.** **The claim is not falsified. It is unbacked for a subset,
and the subset is not named.**

## ✅ AND THE PAPER ALREADY DOES THE HARD PART, WHICH THE CENSUS MADE ME EXPECT IT WOULD NOT
Recorded because the honest direction here is exculpatory and an audit that only reports the bad half is
the instrument this campaign keeps warning itself about:
1. **The two-layer defect is disclosed in full, unprompted** — *"The agent harness's own file-reading
   tool is executed by the harness process and never enters that sandbox. Neither substrate's settings
   carried a tool-permission rule, so **no scored episode of this campaign had the agent's tools fenced
   by path**."*
2. **The probe's own blindness is disclosed** — *"a probe written in the sandbox's language cannot see a
   hole in the layer above it, and **it reads afterwards as though the agent itself were fenced**."*
   ⭐ **That is this shift's finding, written down in the paper, one layer up, weeks ago.**
3. **The exploitation/protection distinction is already drawn** — *"the canary shows the gap was open,
   and **an absence of exploitation is not a presence of protection**."*
4. **A containment verdict is already WITHDRAWN rather than caveated**, for the three matrix smoke
   cells: *"their containment verdicts are withdrawn rather than caveated, so **no containment claim for
   this matrix rests on them**."* ⚠️ **Scoped to those three cells, not to the matrix's others.**

## ⇒ THE COUNTS
```
  (i)   states the OS layer as enforced or verified ...... 2 sentences, both in the paper, both unscoped
        + 1 inventory clause that is the one the census bears on ("each with its own evidence")
  (ii)  states only the rendered fence / hook layer ...... README.md, scoped to v1, self-disclosing
  (iii) silent ........................................... BOTH RESULT files of record (#115, #117),
                                                           zero of six needles, positive controls firing
  already withdrawn ...................................... 1 passage, 3 matrix smoke cells
```

## ⛔ WHAT I AM NOT DOING, PER THE RULING AND PER THIS REPO'S OWN LAW
- **No edit to the paper.** An edit to the public paper is **the Captain's word**. This file is the input
  to that decision and not a substitute for it.
- **No edit to #115 or #117.** They are silent, so there is nothing to correct — and a merged result is
  corrected by a dated addendum, never by rewriting a merged number.
- **No withdrawal of anything.** ⛔ **No leak is claimed. No number moves.** The fleet's adopted wording
  stands: for Claude cells the fence is *rendered and drift-checked at use; the hook layer is driven;
  the OS sandbox layer is UNMEASURED.*

## ⇒ 🔑 THE LESSON, AND IT IS ABOUT AUDITS RATHER THAN FENCES
**I expected to find an overclaim and found an unscoped population instead.** The paper's isolation
prose is careful, self-incriminating and unusually honest — and **that is exactly why the gap survived
it**: a paragraph that spends six sentences confessing the layer it got wrong reads as a paragraph that
has been thought about, and **the clause a reader does not re-examine is the plain inventory in the
middle of the confession.**
⇒ ***A DISCLOSURE PARAGRAPH IS THE HARDEST PLACE TO SPOT A REMAINING GAP, BECAUSE ITS CANDOUR IS DOING
THE READER'S CHECKING FOR THEM.*** Same shape as the fleet's own standing line about the green that
names its own scope accurately, and this is that line applied to prose rather than to a gate.
