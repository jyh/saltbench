# RESULT — x86 PoC, CLAUDE ROW, `none` × {plain, salt-diet} AT n = 3 (CRC-32, scalar x86-64)

## bench (SaltBench lead), 2026-09-26. Registered design: `harness/systems-x86/AMENDMENT-x86-crc32-poc-2026-09-25.md` (PR #267,
## helm-signed as non-author), with its ADDENDA 1–8. Cut `4d960d3`; referee `referee_x86.sh` blob `8cfbf8113196`.

> ## ⛔ READ THIS BEFORE ANY NUMBER BELOW
> **This is ONE problem at n = 3 per arm. It carries NO effect size and NO premium, and it says nothing about "x86" in general, or
> about the method, beyond this card** (§X8, registered before any data). A PASS means: behaviour on 82 withheld inputs agrees with the
> harness's own executor, plus, for salt-diet, a kernel-checked TARGET. For plain, a PASS says nothing about inputs the suite does not
> test.

---

## 0 · PROVENANCE OF EVERY NUMBER IN THIS FILE

```
  end marker, verbatim        each cell's own ctl/end-1, on the run box
  at_end_COST · final_COST    each cell's own ctl/post-end-1.tsv (columns 3 and 5), written by the cell watcher's meter at END
  pool dir (FIRST · SECOND)   each cell's own ctl/run-cfg.tsv, key cfg; FIRST = the run box pool's own dir, SECOND = ADDENDUM 4's
  served-model verdict        served_models_v3.py check-cell --condition opus, per cell, read at harvest
  class · tests · agreement · spec_strength · target · axioms · cell_translation
                              referee_x86.sh's out.json, per cell, run on the BUILD box on a COPY of the cell's repo/, with
                              HARNESS = a git archive of 4d960d3 carrying EXPORTED-FROM.sha
```
The table in §2 was produced by one script over those files and is pasted here **verbatim, not typed**. The script is retained on the
build box and is not tracked here, because it names the run box and its pool dirs; §6 says exactly what it reads.
⚠️ **Declared gap, the same one HC1 declared:** the cells and the referee's out.json live on the run box and the build box, not in this
repository, because they carry host and account paths that must not enter a public tree. A reader reproduces the table by re-running
the referee and the meter against the cells, and should not trust a figure here without doing so.

## 1 · WHAT RAN
Six scored cells, fired one at a time in §X2 order (plain #1, salt-diet #1, #2, #3), each preceded by an account check, a
`--check-only` and the fire's own P-SANDBOX and P-NET probe turns, GREEN at every launch that happened. Two cells had a first
attempt that did NOT launch, $0 spent on a subject: plain #2's P-NET turn failed authentication on the first dir (ADDENDUM 6), and
plain #3 was HELD by the run-dir guard on a client's leftover `.claude.json` temp file. Every cell is `card_extras = none`. The smoke pair
(clbwcp01, clbwcs01) was read under §X3 as plumbing and is **not** in this table.

## 2 · THE TABLE (verbatim output; costs in USD from each cell's own meter)

```
id	arm	n	end_marker	at_end_COST	final_COST	pool_dir	class	tests	agreement	spec_strength	target	axioms	cell_translation
clbqcp01	plain	1	2026-09-26T00:40:32Z LANDED landing-1 c3791677d806	5.1896	5.2591	FIRST	PASS	PASS	AGREE=82	n/a	n/a	n/a	n/a
clbqcs01	salt-diet	1	2026-09-26T01:53:33Z LANDED landing-1 bb77e62a2de3	32.6659	32.8430	FIRST	PASS	PASS	AGREE=82	82/82	OK	Classical.choice,Quot.sound,propext	identical
clbqcp02	plain	2	2026-09-26T02:37:50Z LANDED landing-1 83f9ea501ad0	10.4061	10.4989	SECOND	PASS	PASS	AGREE=82	n/a	n/a	n/a	n/a
clbqcs02	salt-diet	2	2026-09-26T03:31:05Z LANDED landing-1 1694c46a9354	26.7035	27.5359	SECOND	PASS	PASS	AGREE=82	82/82	OK	Classical.choice,Quot.sound,propext	identical
clbqcp03	plain	3	2026-09-26T04:06:21Z LANDED landing-1 894be0256ed0	7.1446	7.2947	SECOND	PASS	PASS	AGREE=82	n/a	n/a	n/a	n/a
clbqcs03	salt-diet	3	2026-09-26T05:06:15Z LANDED landing-1 6616f9075a0f	30.3255	30.5436	SECOND	PASS	PASS	AGREE=82	82/82	OK	Classical.choice,Quot.sound,propext	identical
```

**Served model:** `served_models_v3.py check-cell --condition opus` read `clean` (set_verdict clean) for all six cells, each read at its
harvest. It is not a table column because the script above does not read it. It is stated here from those six reads.

## 3 · THE REGISTERED PREDICTIONS (§X5), READ
- **(i) salt-diet's cap incidence ≥ plain's:** HOLDS trivially at 0 ≥ 0. No cell reached the $37.21 cap: salt-diet's highest final cost
  is 32.8430, and plain's is 10.4989. **The CAP-COST censoring §X5 (i) called EXPECTED did not occur**, so no salt-diet figure here is a
  floor. That is a failed expectation, reported as one, never a finding.
- **(ii) every salt-diet cell that reaches TARGET reads the three standard axioms:** HOLDS, 3 of 3 (`Classical.choice, Quot.sound,
  propext`), with `cell_translation=identical` in all three.
- **(iii) no plain cell reads `cell_translation=differs`:** HOLDS, 3 of 3 (plain ships no Lean, so the line is absent).

## 4 · WHAT EACH VERDICT CARRIES BESIDE IT
- **clbqcp02 (plain · #2) is DECLARED, not voided (ADDENDUM 7).** Its pool dir's client config had a browser-integration default set.
  Its transcripts carry 0 uses of any browser or MCP tool, but what the client OFFERED is unmeasured. The flag travels with its PASS.
- **Two pool dirs** (column `pool_dir`, ADDENDA 4–6): cells 1–2 ran on the first and 3–6 on the second, after the first dir's credential
  failed a refresh at a probe turn, with nothing spent on a subject. The model, client pin, cut, views, fence render, budgets and referee
  were the same on both. It is a billing pool, not a treatment, and both arms span both dirs.
- **The TMPDIR confound (§X6 4):** every cell ran with `CLAUDE_CODE_TMPDIR` inside the cell, as ruled. The client's cwd-tracking write
  to the system temp dir is refused on shell calls, measured on every call in both smoke cells and in block N's transcripts (a declared,
  arm-identical cost). It was not re-counted in these six. The smoke cells also saw a few here-documents refused, 3 in salt-diet and 1 in
  plain. That count is not a contrast at n = 1.

## 5 · WHAT THIS CANNOT ESTABLISH (§X8, registered before any data)
**No effect size and no premium** at n = 3 on one problem, and **nothing about models, other problems, or cross-lane**. Six of six PASS
means both arms produced a CRC-32 routine that agrees with the harness's executor on 82 withheld inputs, and that each salt-diet cell also
proved its TARGET in the kernel. For plain, a PASS says nothing about inputs the suite does not test. **The cost column is not a
comparison either:** salt-diet cells carry a proof, which is the treatment, not overhead to subtract.

## 6 · HOW THE TABLE WAS PRODUCED (the retained script, described)
For each of the six cell ids, it reads the run box's `ctl/end-1`, then `ctl/post-end-1.tsv` columns 3 and 5, then `ctl/run-cfg.tsv`'s
`cfg`, mapped to FIRST or SECOND. It then reads the build box's referee `out.json` (`class`, `tests`, `agreement`, `spec_strength`,
`target.class`, `target.axioms`, `target.cell_translation`). A missing source prints `MISSING` and is never filled. It printed none.
