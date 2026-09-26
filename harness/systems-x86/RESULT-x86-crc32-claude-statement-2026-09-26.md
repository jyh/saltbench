# RESULT — x86 PoC, CLAUDE ROW, `statement` × {plain, salt-diet} AT n = 3 (CRC-32, scalar x86-64)

## bench (SaltBench lead), 2026-09-26. Registered design: `harness/systems-x86/AMENDMENT-x86-crc32-poc-2026-09-25.md` (PR #267,
## helm-signed as non-author), with its ADDENDA 1–11. Cut 4 = `5d3267b` (ADDENDUM 9); referee `referee_x86.sh` blob `8cfbf8113196`.
## Its sibling, the `none` conditions on cut `4d960d3`: `RESULT-x86-crc32-claude-none-2026-09-26.md` (PR #268).

> ## ⛔ READ THIS BEFORE ANY NUMBER BELOW
> **This is ONE problem at n = 3 per arm. It carries NO effect size and NO premium, and it says nothing about "x86" in general, or
> about the method, beyond this card** (§X8, registered before any data). **ONE CELL (clbkcs02) IS CAP-COST, NOT LANDED:** its referee
> verdict is of its END STATE and is printed beside its run state; it is never counted as a landing. A PASS means: behaviour on 82
> withheld inputs agrees with the harness's own executor, plus, for salt-diet, a kernel-checked TARGET whose post does NOT pin the
> halt reason (§4). For plain, a PASS says nothing about inputs the suite does not test.

---

## 0 · PROVENANCE OF EVERY NUMBER IN THIS FILE
```
  end marker, verbatim        each cell's own ctl/end-1, on the run box (it carries the RUN STATE: LANDED or CAP-COST)
  at_end_COST · final_COST    each cell's own ctl/post-end-1.tsv (columns 3 and 5), written by the cell watcher's meter at END
  pool dir (FIRST · SECOND)   each cell's own ctl/run-cfg.tsv, key cfg; FIRST = the run box pool's own dir, SECOND = ADDENDUM 4's
  served-model verdict        served_models_v3.py check-cell --condition opus, per cell, read at harvest
  class · tests · agreement · spec_strength · target · axioms · cell_translation
                              referee_x86.sh's out.json, per cell, run on the BUILD box on a COPY of the cell's repo/, with
                              HARNESS = a git archive of 5d3267b carrying EXPORTED-FROM.sha
```
The table in §2 was produced by one script over those files and is pasted here **verbatim, not typed**. The script is retained on the
build box, and is not tracked because it names the run box and its pool dirs. It is the `none` RESULT's gatherer, with the six cell ids
and the root changed.
⚠️ **Declared gap, the same as the `none` RESULT's:** the cells and the referee's out.json live off-tree; a reader reproduces the table by
re-running the referee and the meter against the cells.

## 1 · WHAT RAN
Six scored cells from cut 4, fired one at a time in §X2 order (plain #1, salt-diet #1, #2, #3). Each fire was preceded by an account check,
a `--check-only` whose launch fence carries `d0d54b5`'s x86-roots re-assertion (the reason for cut 4), and the fire's own P-SANDBOX and
P-NET probe turns, GREEN at every launch. Every view carried the statement hand-out asserted against its pinned blobs (statement
`630a37ba2545`, spec `b336720df2e1`). Neutrality read zero hits on the two views the lead opened (clbkcp01, clbkcs01). For the other
four it rests on the builder's gate, which REFUSES to stage a view that fails it (§X7). **plain + statement is a DOCUMENT:** its `import
Crc32X86Interface` resolves only in the salt-diet overlay, a declared property of the condition, not a repaired one.
**Served model:** `check-cell --condition opus` read `clean` for all six cells, each read at its harvest.

## 2 · THE TABLE (verbatim output; costs in USD from each cell's own meter)
```
id	arm	n	end_marker	at_end_COST	final_COST	pool_dir	class	tests	agreement	spec_strength	target	axioms	cell_translation
clbkcp01	plain	1	2026-09-26T07:16:43Z LANDED landing-1 57ad43256aa4	7.1430	7.2281	FIRST	PASS	PASS	AGREE=82	n/a	n/a	n/a	n/a
clbkcs01	salt-diet	1	2026-09-26T08:40:54Z LANDED landing-1 8460634b8860	36.2658	37.2308	FIRST	PASS	PASS	AGREE=82	82/82	OK	Classical.choice,Quot.sound,propext	identical
clbkcp02	plain	2	2026-09-26T09:31:42Z LANDED landing-1 56ff5b516c29	8.5273	8.6901	SECOND	PASS	PASS	AGREE=82	n/a	n/a	n/a	n/a
clbkcs02	salt-diet	2	2026-09-26T11:31:54Z CAP-COST cost 38.0216 USD CELL-CUMULATIVE (every session of BOTH phases) >= cap 37.21 USD PHASE-1 ONLY -- TWO SCOPES: never quote this cost as a phase-1 figure; overrun printed, never clipped; T 52032777 read beside it (also cell-cumulative), never the cap	38.0216	38.0216	FIRST	PASS	PASS	AGREE=82	82/82	OK	Classical.choice,Quot.sound,propext	identical
clbkcp03	plain	3	2026-09-26T12:13:40Z LANDED landing-1 d49e1dd49289	7.8533	8.0586	FIRST	PASS	PASS	AGREE=82	n/a	n/a	n/a	n/a
clbkcs03	salt-diet	3	2026-09-26T13:23:07Z LANDED landing-1 110dea1c967b	31.6514	32.6979	FIRST	PASS	PASS	AGREE=82	82/82	OK	Classical.choice,Quot.sound,propext	identical
```

## 3 · THE REGISTERED PREDICTIONS (§X5), READ
- **(i) salt-diet's cap incidence ≥ plain's:** HOLDS, **1 of 3 ≥ 0 of 3.** clbkcs02 is CAP-COST at 38.0216 against the 37.21 cap, with
  the overrun printed and never clipped. Its cost is a FLOOR (§X5 (i)). Separately, clbkcs01 LANDED at 36.2658 and its post-END metering
  (the client gone) took its final figure to 37.2308. Both figures are shown and neither is rounded.
- **(ii) every salt-diet cell that reaches TARGET reads the three standard axioms:** HOLDS, 3 of 3, including the CAP-COST cell's end
  state; `cell_translation=identical` in all three.
- **(iii) no plain cell reads `cell_translation=differs`:** HOLDS, 3 of 3 (plain ships no Lean).

## 4 · WHAT EACH VERDICT CARRIES BESIDE IT
- **clbkcs02 is CAP-COST.** The subject had merged its verified routine, statement and proof, written LANDING.md, and banked. It was cut
  before `bin/declare`. The referee's CLASS PASS is of that end state, a clean tree. **It is not a landing, and it is never counted in a
  landing rate.**
- **THE HALT-REASON LIMIT OF THE STATEMENT** (routed by x86lean's refuters, held by the lead): `CorrectFor`'s post, `t.stopped ∧ t.rip =
  ret`, does not pin WHY the run stopped, because a fault is also `stopped`. The argument that a faulting halt at `ret` is unreachable
  (`SysVCall`: `prog.at? ret = none`) is sound but **UNPROVED**. What bounds every PASS here regardless is AGREEMENT=82: a routine that
  faults instead of returning disagrees with the native run. The fix belongs to the NEXT statement revision, by a new blob and a new
  amendment, never mid-block.
- **Two pool dirs** (column `pool_dir`): clbkcp02 ran on the second (ADDENDUM 10, trigger (c), with the first pool at 92 %), and the other
  five ran on the first. The model, pin, cut, views, fence render, budgets and referee are the same on both.
- **The first dir's first token refresh under use** fell INSIDE clbkcs03 (12:54 UTC). It landed in the file and the cell metered straight
  through it; the per-minute credential ledger has the rows.
- **The TMPDIR confound (§X6 4)** and its declared, arm-identical cost ride here exactly as in the `none` RESULT.

## 5 · WHAT THIS CANNOT ESTABLISH (§X8, registered before any data)
**No effect size and no premium** at n = 3 on one problem, and **nothing about models, other problems, or cross-lane**. **No contrast
between `none` and `statement`** is claimed either: they ran on different cuts by design (ADDENDUM 9), and the pairing was never
registered as a contrast. **The cost column is not a comparison:** salt-diet cells carry a proof, which is the treatment, and one is
censored at the cap.
