# RESULT — x86 PoC, AGY ROW, `none` × {plain, salt-diet} AT n = 3 (CRC-32, scalar x86-64)

## gemini (the agy row's hand), 2026-09-29. Registered design: `harness/systems-x86/AMENDMENT-x86-crc32-poc-2026-09-25.md` (PR #267,
## helm-signed as non-author), with its ADDENDA 1–14; this row fired under ADDENDUM 12. Cut 4 = `5d3267b`; referee `referee_x86.sh`
## blob `8cfbf8113196`. The lead is bench; this file is the hand's, as ADDENDUM 14 assigns.

> ## ⛔ READ THIS BEFORE ANY NUMBER BELOW
> **This is ONE problem at n = 3 per arm. It carries NO effect size and NO premium, and it says nothing about "x86" in general, or
> about the method, beyond this card** (§X8, registered before any data). A plain PASS means behaviour on 82 withheld inputs agrees
> with the harness's own executor, and says nothing about inputs the suite does not test. **No salt-diet cell here passed**: all three
> failed at the referee's proof stages (§3), while their code agreed on all 82 inputs.
> ⚠️ **The two arms ran HOURS APART, plain first (ADDENDUM 12).** A drift in the served model or the agy pool over those hours falls on
> salt-diet alone, and its sign is not registered. The Claude row interleaved, so this confound is this row's alone.

---

## 0 · PROVENANCE OF EVERY NUMBER IN THIS FILE

```
  end_marker, verbatim         each cell's own ctl/end-1, on the run box
  done_reason · turns · wall_s · false_done
                               each cell's own ctl/agy-turnloop-1.json (done_reason, turns_sent, wall_seconds, false_done_claims)
  T_tokens · vendor_tokens · served · meter_verdict
                               each cell's own ctl/agy-meter-1.json (T, vendor_total_tokens, served_models, verdict), written
                               by agy_meter_v3.py from the client's stream at the cell's end
  fire / clean times · attempts the canary's ledger.tsv per wave (FIRE, CONDITION-CLEAN, CONDITION-FAILED rows), on the build box
  class · tests · agreement · spec_strength · target · axioms · cell_translation
                               referee_x86.sh's out.json, per cell, run on the BUILD box on a hash-checked COPY of the cell's
                               repo/, with HARNESS = a clean worktree at 5d3267b
```
The table in §2 was produced by one script over those files and is pasted here **verbatim, not typed**. The script is retained on the
build box and is not tracked here, because it names the run box; §6 says exactly what it reads.
⚠️ **Declared gap, the Claude row's and HC1's:** the cells and the referee's out.json live on the run box and the build box, not in this
repository, because they carry host and account paths that must not enter a public tree. A reader reproduces the table by re-running
the referee and the meter against the cells, and should not trust a figure here without doing so.

## 1 · WHAT RAN
Six scored cells, fired **by condition** as ADDENDUM 12 ordered: plain ×3 (`xapn01`–`03`), then salt-diet ×3 (`xasn01`–`03`), through
`gemini_canary_wave_v1.sh` (any 503 ⇒ kill, discard, re-queue), gemini-3.1-pro-high, one cell at a time on the agy credential. The
canary's ledger reads `CONDITION-CLEAN` for both conditions with `a503=0` on every cell, so **every cell is attempt 1 and no attempt was
discarded.** BATTERY GREEN, the TMPDIR row OK and `reap nothing-left` on all six (my harvest reads, 2026-09-26).
**One refused fire, $0, no cell:** the salt-diet condition's first fire (18:38:34Z) was REFUSED at the wave's own gate — *"salt-diet
needs LEAN_TOOLCHAIN_BIN, the PINNED Lean bin with lake"* — before any build, because the hand's fire environment lacked it. The root
held only its staging marker. It was re-fired identically (same export, same condition) at 18:50:07Z (its ledger's FIRE row), and those are the cells below.
**The 24 min 51 s gap between xasn02's end and xasn03's start is the wave's credential-window wait, outside every cell.** The
wave's own fire log reads, at 19:55:16Z, *"CREDENTIAL WINDOW 1676s remaining, below the 2400s a cell needs"*. It waited 1,426 s for the
client's refresh window, and at 20:19:22Z the token advanced and it fired xasn03. `wall_s` counts from a cell's launch, so no cell's
wall includes the wait. No model was reached during it.
The smoke pair (§X3) was read as plumbing and is **not** in this table.

## 2 · THE TABLE (verbatim output; tokens from each cell's own meter)

```
id	arm	n	end_marker	done_reason	turns	wall_s	false_done	T_tokens	vendor_tokens	served	meter_verdict	class	tests	agreement	spec_strength	target	axioms	cell_translation
xapn01	plain	1	2026-09-26T18:30:54Z LANDED landing-1 985089e87acb	LANDED	3	189.8	0	1300878	175215	gemini-3.1-pro-high	OK	PASS	PASS	AGREE=82	n/a	n/a	n/a	n/a
xapn02	plain	2	2026-09-26T18:33:53Z LANDED landing-1 1f4135ef4301	LANDED	3	147.9	0	778521	116591	gemini-3.1-pro-high	OK	PASS	PASS	AGREE=82	n/a	n/a	n/a	n/a
xapn03	plain	3	2026-09-26T18:37:51Z LANDED landing-1 5fc3e64922d1	LANDED	3	196.4	0	1103043	155870	gemini-3.1-pro-high	OK	PASS	PASS	AGREE=82	n/a	n/a	n/a	n/a
xasn01	salt-diet	1	2026-09-26T19:41:48Z LANDED landing-1 8fd7f650f818	LANDED	7	1084.7	2	6561052	856939	gemini-3.1-pro-high	OK	SCREEN	PASS	AGREE=82	None	n/a	n/a	n/a
xasn02	salt-diet	2	2026-09-26T19:54:51Z LANDED landing-1 a810cc5f2fa3	LANDED	7	746.4	2	6270968	505583	gemini-3.1-pro-high	OK	TARGET	PASS	AGREE=82	82/82	TARGET	n/a	identical
xasn03	salt-diet	3	2026-09-26T20:33:52Z LANDED landing-1 2c798b99a868	LANDED	4	850.2	0	5507746	508884	gemini-3.1-pro-high	OK	SCREEN	PASS	AGREE=82	None	n/a	n/a	n/a
```

**Reading the columns.** `class` is the referee's verdict. `SCREEN` and `TARGET` are the proof stage at which a salt-diet cell FAILED,
and `PASS` is a pass. `spec_strength None` is the referee's own null: a cell stopped at SCREEN is not scored for spec strength.
`served` is the model that each result record in the client's stream names, as `agy_meter_v3.py` reads it. It is the client's
statement, not a backend receipt. `T_tokens` is the meter's T (it counts cache reads, which dominate); `vendor_tokens` is the client's
own total.

## 3 · THE THREE SALT-DIET FAILURES, EACH AT THE CELL (subject outcomes, never harness faults)
Each was re-read by a second method at the cell's own repo on the run box (the hand's reading, bus, 2026-09-26 14:17 PDT):
- **xasn01 · SCREEN:** the referee's `screen_violations` names `Submission/Proof.lean:16: sorry`; the cell's file carries `sorry` at line 16.
- **xasn03 · SCREEN:** `Submission/Proof.lean:6: sorry`, and the same line at the cell.
- **xasn02 · TARGET:** `target_unknown ["Submission.correct"]` (the probe's `Unknown identifier`). At the cell, `Submission/*.lean` declares
  `Submission.spec` and no theorem at all. Its spec is strong (82/82) and its translation identical; the TARGET theorem does not exist.
**All three LANDED by their own account.** A landing is the subject grading itself, and the turn loop compiles nothing. **The self-graded
landing rate here is 6/6; the refereed pass rate is 3/3 plain and 0/3 salt-diet.** Only the second is a result.
`false_done` 2 on xasn01 and xasn02 means the loop twice corrected a premature done claim before the landing file existed.

## 4 · THE REGISTERED PREDICTIONS (§X5), READ
- **(i) salt-diet's cap incidence ≥ plain's (TURNS-CUT or CAP-TOKENS on this row):** HOLDS trivially at 0 ≥ 0. No cell came near a cap.
  The most turns was 7 (cap 40), and the most T was 6,561,052 (cap 250,000,000).
- **(ii) every salt-diet cell that reaches TARGET reads the three standard axioms or is refused at AXIOMS:** NOT EXERCISED. No salt-diet
  cell got past TARGET, so no axioms line exists to read. It is untested here, not upheld.
- **(iii) no plain cell reads `cell_translation=differs`:** HOLDS, 3 of 3 (plain ships no Lean, so the line is absent).

## 5 · WHAT EACH VERDICT CARRIES BESIDE IT
- **THE TIME-ORDER CONFOUND (ADDENDUM 12):** by the canary's own ledgers, plain ran from FIRE 17:53:20Z to CONDITION-CLEAN 18:38:33Z and
  salt-diet from FIRE 18:50:07Z to CONDITION-CLEAN 20:34:37Z, on the same caps, credential, box and cut. Its sign is not registered, and it is printed at the head of this file for that reason.
- **THE HALT-REASON LIMIT OF THE TARGET** (the Claude row's RESULTs, §4): no salt-diet cell here reached a proved TARGET, so the limit
  bears on no verdict in this file. It is recorded so a later pooling does not drop it.
- **The arm-level contrast is not a finding.** 3/3 against 0/3 at n = 3 on one problem is inside what §X8 forbids reading as an effect.
  The salt-diet cells did something the plain cells were never asked to do (write and prove a Lean TARGET), and failed at that.
- **CAP REGIME: no memory ceiling on any of the six cells.** The ceiling (ADDENDA 14–15, `AGY_MEM_CAP_MB`) did not exist when they
  ran. The statement RESULT's cells #2 and #3 of salt-diet run under it; these six are the baseline it is read against.
- **Tokens are not a comparison either:** a salt-diet cell carries a proof attempt, which is the treatment, not overhead to subtract.
- **Cross-row (Claude versus agy) is not a registered contrast** (§X6 5). The Claude row's `none` pair is on a different cut (4d960d3),
  a different client and a different environment.

## 6 · HOW THE TABLE WAS PRODUCED (the retained script, described)
For each of the six cell ids, it reads, by one ssh per cell and read-only, the run box's `ctl/end-1`, `ctl/agy-turnloop-1.json` and
`ctl/agy-meter-1.json`. It then reads the build box's referee `out.json` (`class`, `tests`, `agreement`, `spec_strength`,
`target.class`, `target.axioms`, `target.cell_translation`). A missing source prints `MISSING` and is never filled. It printed none.
