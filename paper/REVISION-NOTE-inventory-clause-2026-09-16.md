# REVISION NOTE — the §sec:fence inventory clause is unevidenced for part of its population

**Status: OPEN, to be carried by the next planned revision of the paper. The posted arXiv version is
NOT revised by this note, and nothing here is an edit to the paper.** An edit to the public paper is the
Captain's decision; this file is the input to that decision, written so the revision can carry it
without re-deriving anything.

Ruled by the Captain 2026-09-13 ("Yes (2)", desk LW). Written 2026-09-16 by bench (SaltBench lead).
Inputs: `harness/systems-v3/AUDIT-published-fence-claims-2026-09-13.md` (PR #120), the matrix census
(PR #119), and `harness/systems-v3/RECEIPT-claude-sandbox-probe-2026-09-14.md`.

---

## 1 · THE CLAUSE, EXACTLY

`paper/saltbench-v1.tex`, line 102, as tracked at the last change to that file (`aee2fa5`, 2026-09-09):

> What was in force, each with its own evidence, was the subprocess sandbox, the empty network
> allowlist, the shell-tool hook, the ground-truth leak check, and the audit layer.

## 2 · WHY IT NEEDS A SCOPE

**The clause is not false. It is unevidenced for part of the population the paper reports.**

- **For the v1/v2 episodes it is EARNED**, and the paper says how, two sentences earlier: *"The smoke
  probe that had certified credential reads denied made its reads through the shell and through an
  in-language process spawn, both sandboxed."* The subprocess layer was driven for that population.
- **For the v3 Claude cells it is UNEVIDENCED.** The paper reports the v3 systems campaign (over 60 of its
  `\src{}` citations point into `harness/systems-v3/`), and the paragraph opens by claiming that reach:
  *"The third finding arrived after every read reported in this paper and applies to all of them."* For
  those cells the OS sandbox layer was **rendered and drift-checked, but never driven**: the audit measured
  124 Claude cells launched and not one that drove the layer.

The adopted wording for Claude cells stands: *the fence is rendered and drift-checked at use; the hook
layer is driven; the OS sandbox layer is UNMEASURED.*

## 3 · THE PROPOSED SCOPE — six words (the ruling anticipated about eight), a PROPOSAL, not an edit

```
  What was in force for the v1 and v2 episodes, each with its own evidence, was ...
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^
```

The insertion confines the clause to the population whose evidence the paper actually cites. It changes
no number and withdraws no claim. Whether the revision also states the v3 status in the same paragraph
is the author's choice; the adopted wording in §2 is the accurate form if it does.

## 4 · ⛔ THE CONDITION THE RULING ANTICIPATED HAS BEEN MET — AND IT DOES *NOT* CHANGE THE SCOPE LINE

**Read this before assuming the note is out of date.** The 2026-09-13 ruling said that a driven
Claude-client sandbox probe *would make the clause evidenced for v3 and change the scope line.*

**That probe was driven, on 2026-09-14** (commit `1f1d908`, `RECEIPT-claude-sandbox-probe-2026-09-14.md`).
**It does not change the scope line for the paper, and the receipt says why, in its own words:**

- **§R4:** *a probe built today **cannot be applied retroactively to a cell that has landed.*** The 124
  v3 Claude cells the paper reports landed before the probe existed. The receipt shows the layer works on
  **one real cell, on the pinned client, at that date**; it is evidence about the mechanism, not about
  those cells.
- **§R5:** the probe's enforcement mode (`--require` on the launch path) is **built and driven, but
  unwired**, awaiting a ruling. So no cell fired since has been probed per cell either.

⇒ **The scope proposed in §3 stands as written.** A future ruling that wires `--require` into the launch
path would make *subsequently fired* Claude cells per-cell evidenced — and would warrant revisiting this
note for any revision that reports such cells. It would not reach back to the cells this paper reports.

## 5 · ⛔ THE CHECK TO RUN BEFORE ANY EDIT

**Confirm that the arXiv-POSTED wording of this sentence equals the tracked tex before editing either.**
The tracked file last changed on 2026-09-09 and the paper was posted on 2026-09-10, which makes equality
likely — **and "likely" is exactly what this check exists to replace.**

- Compare **text**, never bytes. arXiv rebuilds from source, so a PDF byte comparison can only ever
  answer "different" and says nothing about wording.
- Extract the sentence from the posted source or rendered text and compare it to line 102 of
  `paper/saltbench-v1.tex` at the revision's base commit.
- If they differ, the posted wording is what readers have, and the revision must scope **that** text.

## 6 · WHAT THIS NOTE DOES NOT DO

1. It does not edit the paper, the tex, or the posted version.
2. It does not correct either result file of record (#115, #117). Both are silent on OS-layer
   enforcement, so there is nothing in them to correct.
3. It claims no leak and moves no number. The paper already discloses the two-layer defect in full,
   discloses its own probe's blindness, and draws the exploitation/protection distinction explicitly —
   this note scopes one inventory clause and nothing else.
