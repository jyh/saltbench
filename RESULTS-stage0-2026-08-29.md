# STAGE 0 — RESULTS, 2026-08-29 (bench seat)

Protocol: `SCOUT-STAGE0.md` frozen at `cb8cea3`, amendment 1 + addenda 1–4 (executed at freeze commit `13959bd`→`6c6df80` on the Studio; every manifest names its commit). Substrate: SWE-bench Verified pilot draw, first k = 15 tasks of `TASKLIST.json`, both arms, task-major. Agent: Claude Code 2.1.251 headless, `claude-sonnet-5`, effort high, `--max-turns 40`, on the bench subscription. Scorer: swebench 4.1.0 in the digest-bridged images. Controls: pre-flight 15/15, gold 15/15, EXCLUDED = []. Driver: 00:21:25Z → 01:17:06Z (56 min). Scoring: 01:20Z → 01:41Z. Archive: `runs/stage0-2026-08-28/` (transcripts, manifests, patches, meter, logs; the reproducible trees excluded).

## The morning line (the one pre-declared computation, `harness/morning_line.py`)

```
STAGE-0 MORNING LINE  pairs=15 (tasks with both arms scorable)  excluded_by_controls=0  constants=[(40, 5400, 8000000, 'claude-sonnet-5', 'high')]
  a0 solved 13/15  metered p50=566108 p90=1602434 max=1694954  terminations={'ROUNDS_EXHAUSTED': 3, 'DONE': 12}
  a1 solved 13/15  metered p50=531692 p90=1604555 max=1629090  terminations={'ROUNDS_EXHAUSTED': 2, 'DONE': 13}
  b(a0 only)=0 c(a1 only)=0 n_d=0  |b-c|=0  P(|b-c|>=0 | identical arms)=1.000  INDISTINGUISHABLE AT k=15 (|b-c|<5) — not narrated
  p90 the cap rule consumes (a0, DONE|ROUNDS_EXHAUSTED): 1602434 over 15 episodes; censored a0 rows excluded: 0
  cap-bound episodes a0=3 a1=2  
  removed rows (VOID/QUOTA/ERROR/HARNESS_ERROR): 0  []
  a0 url_mentions=0 blocked_escapes=1 tool_timeouts=0 compactions=0
  a1 url_mentions=0 blocked_escapes=1 tool_timeouts=0 compactions=0
  length term (a1-a0 first-call input+cache_creation+cache_read tokens): median=544 over 15 pairs
  pairs whose arms landed different models/tiers: []
  a0 rt_unfinished total=0
  a1 rt_unfinished total=0
  pair order / wall_s: astropy__astropy-14539:a0(86s)/a1(86s) django__django-13658:a1(34s)/a0(33s) django__django-15315:a0(32s)/a1(33s) django__django-15930:a1(133s)/a0(133s) matplotlib__matplotlib-2:a1(131s)/a0(70s) matplotlib__matplotlib-2:a0(131s)/a1(71s) matplotlib__matplotlib-2:a0(151s)/a1(252s) scikit-learn__scikit-lea:a1(46s)/a0(27s) scikit-learn__scikit-lea:a0(47s)/a1(67s) sphinx-doc__sphinx-10449:a1(86s)/a0(126s) sphinx-doc__sphinx-9602:a1(187s)/a0(287s) sympy__sympy-14248:a0(186s)/a1(187s) sympy__sympy-17655:a1(167s)/a0(107s) sympy__sympy-21612:a0(166s)/a1(207s) sympy__sympy-22914:a0(27s)/a1(26s)
  canonical prompt equal within every pair: True
  models seen per arm: {'a0': ['claude-sonnet-5'], 'a1': ['claude-sonnet-5']}
  no p-value, by design; no task-arm repeated, so sampling variance and arm effect are not separated at stage 0.
```

**Reading, as the freeze binds it:** `|b−c| = 0 < 5` ⇒ INDISTINGUISHABLE AT k = 15, narrated in neither direction. Both arms resolved the same 13 tasks and failed the same 2 (`sympy__sympy-14248`, `sphinx-doc__sphinx-9602` — the two tasks on which both arms hit the 40-call cap). The a0 p90 the cap rule consumes is **1,602,434** metered tokens (⇒ `TOKEN_CAP_PER_TASK = ⌈2 × p90⌉ = 3,204,868` when a treatment amendment invokes the rule). Cap-bound episodes a0 = 3, a1 = 2 (difference 1, not CAP-CONFOUNDED). Zero removed rows.

## Per-episode table

| # | task | arm | order | termination | calls | metered (governing) | wall s | patch B | rt calls (rc0) | resolved |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | django__django-15315 | a0 | 1st | DONE | 5 | 103607 | 32 | 704 | 1 (1) | ✅ |
| 2 | django__django-15315 | a1 | 2nd | DONE | 4 | 83526 | 33 | 704 | 0 (0) | ✅ |
| 3 | django__django-13658 | a1 | 1st | DONE | 5 | 104873 | 34 | 879 | 0 (0) | ✅ |
| 4 | django__django-13658 | a0 | 2nd | DONE | 5 | 102045 | 33 | 879 | 0 (0) | ✅ |
| 5 | sympy__sympy-14248 | a0 | 1st | ROUNDS_EXHAUSTED | 40 | 1394671 | 186 | 3286 | 8 (8) | ❌ |
| 6 | sympy__sympy-14248 | a1 | 2nd | ROUNDS_EXHAUSTED | 40 | 1520093 | 187 | 2490 | 2 (2) | ❌ |
| 7 | django__django-15930 | a1 | 1st | DONE | 31 | 1328254 | 133 | 1578 | 11 (9) | ✅ |
| 8 | django__django-15930 | a0 | 2nd | DONE | 34 | 1092688 | 133 | 2125 | 12 (10) | ✅ |
| 9 | sympy__sympy-22914 | a0 | 1st | DONE | 5 | 104887 | 27 | 659 | 1 (1) | ✅ |
| 10 | sympy__sympy-22914 | a1 | 2nd | DONE | 4 | 85277 | 26 | 659 | 1 (1) | ✅ |
| 11 | sympy__sympy-17655 | a1 | 1st | DONE | 29 | 872109 | 167 | 752 | 10 (7) | ✅ |
| 12 | sympy__sympy-17655 | a0 | 2nd | DONE | 24 | 615317 | 107 | 797 | 8 (6) | ✅ |
| 13 | matplotlib__matplotlib-24970 | a0 | 1st | DONE | 13 | 332795 | 131 | 806 | 6 (3) | ✅ |
| 14 | matplotlib__matplotlib-24970 | a1 | 2nd | DONE | 8 | 202532 | 71 | 586 | 3 (2) | ✅ |
| 15 | sphinx-doc__sphinx-9602 | a1 | 1st | DONE | 37 | 1604555 | 187 | 2824 | 10 (7) | ❌ |
| 16 | sphinx-doc__sphinx-9602 | a0 | 2nd | ROUNDS_EXHAUSTED | 40 | 1694954 | 287 | 578602 | 21 (19) | ❌ |
| 17 | sympy__sympy-21612 | a0 | 1st | DONE | 27 | 911173 | 166 | 1425 | 11 (9) | ✅ |
| 18 | sympy__sympy-21612 | a1 | 2nd | DONE | 30 | 1154715 | 207 | 1437 | 11 (8) | ✅ |
| 19 | matplotlib__matplotlib-22865 | a1 | 1st | DONE | 21 | 630744 | 131 | 844 | 6 (5) | ✅ |
| 20 | matplotlib__matplotlib-22865 | a0 | 2nd | DONE | 13 | 348104 | 70 | 852 | 3 (3) | ✅ |
| 21 | scikit-learn__scikit-learn-26323 | a0 | 1st | DONE | 7 | 160252 | 47 | 579 | 3 (3) | ✅ |
| 22 | scikit-learn__scikit-learn-26323 | a1 | 2nd | DONE | 15 | 370821 | 67 | 579 | 4 (3) | ✅ |
| 23 | scikit-learn__scikit-learn-14894 | a1 | 1st | DONE | 8 | 179325 | 46 | 595 | 3 (2) | ✅ |
| 24 | scikit-learn__scikit-learn-14894 | a0 | 2nd | DONE | 6 | 128168 | 27 | 595 | 2 (2) | ✅ |
| 25 | matplotlib__matplotlib-25775 | a0 | 1st | ROUNDS_EXHAUSTED | 40 | 1602434 | 151 | 7561 | 0 (0) | ✅ |
| 26 | matplotlib__matplotlib-25775 | a1 | 2nd | ROUNDS_EXHAUSTED | 40 | 1629090 | 252 | 4677 | 5 (3) | ✅ |
| 27 | sphinx-doc__sphinx-10449 | a1 | 1st | DONE | 17 | 519044 | 86 | 1716 | 6 (4) | ✅ |
| 28 | sphinx-doc__sphinx-10449 | a0 | 2nd | DONE | 28 | 901882 | 126 | 1278 | 8 (4) | ✅ |
| 29 | astropy__astropy-14539 | a0 | 1st | DONE | 21 | 566108 | 86 | 2041 | 5 (5) | ✅ |
| 30 | astropy__astropy-14539 | a1 | 2nd | DONE | 19 | 531692 | 86 | 2019 | 4 (3) | ✅ |

## Observations (recorded, not narrated)

- **Identical patches:** on `django__django-15315` both arms shipped the byte-identical 704-byte patch (the known fix). Task-level concordance is total: the same 13 resolved, the same 2 unresolved.
- **Tool use by arm:** a0 (plain) made 89 `rt` calls across its 15 episodes, a1 (house conventions, no tool-mandating step) 76 — somewhat fewer, not none; the difference moved no score. (My bus post of 01:5x mis-stated these as 22 vs 4 and the total spend as ≈21.5M; corrected on the bus at 01:5x — the figures here are the computed ones.)
- **Spend:** a0 10,059,085 tokens, a1 10,816,650 tokens, total 20,875,735 (governing sums, incl. one ~920-token Haiku session-title call per episode). Median episode ≈ 0.55M; the 5 capped episodes ≈ 1.4–1.7M each.
- **Length term:** the placebo costs a median 544 tokens on call 1 (a1 − a0 first-call prefix).
- **One non-UTF-8 patch:** `sphinx-doc__sphinx-9602` a0 (capped) left its own `literal_repro/_build/` in the working copy; submitted with replaced bytes and flagged (addendum 4). It did not resolve; neither did a1's clean 0-byte-flagged attempt on the same task.
- **Blocked escapes:** one per arm across the batch (both hook tripwires, neither a void); zero URL mentions, zero tool timeouts, zero compactions, zero subagents.
- **Believability artifacts:** every transcript (`session.jsonl`), manifest (with freeze commit, shas, flags), patch, `rt.log`, CHECK 2b logs, and the harness reports are in the archive; canonical prompts equal within every pair; only `claude-sonnet-5` seen in both arms.

## What this does and does not say

Stage 0 measured nothing about the salt method (by design, §0). It says: the harness runs, is hermetic in the ways the freeze claims and audited in the ways it admits, meters to the token, and produces a control pair that is indistinguishable at k = 15 — the placebo priced at 544 tokens of prefix and no solves. The treatment arms (TDD · spec-lite · spec-as-checker · full salt) register next as dated amendments with their profiles; each runs against these same 15 tasks under the cap rule's number above.

## Contamination check (PRE-REG §4/§5; instrument, cut and reading rule stated in addendum 6 BEFORE computing)

```
CONTAMINATION PROXY — cut HIGH >= 0.80 (stated before computing); primary = a0
task                                 arm   sim unrest exact str  gold agnt  tot small  resolved/term
astropy__astropy-14539               a0  1.000  0.121  True HIGH    2    2   12 True   ✅/DONE
astropy__astropy-14539               a1  1.000  0.125  True HIGH    2    2   11 True   ✅/DONE
django__django-13658                 a0  0.984  0.984 False HIGH    7    6    6 False  ✅/DONE
django__django-13658                 a1  0.984  0.984 False HIGH    7    6    6 False  ✅/DONE
django__django-15315                 a0  1.000  1.000  True HIGH    6    6    6 False  ✅/DONE
django__django-15315                 a1  1.000  1.000  True HIGH    6    6    6 False  ✅/DONE
django__django-15930                 a0  0.369  0.185 False LOW     5    8   28 False  ✅/DONE
django__django-15930                 a1  0.228  0.203 False LOW     5    2   12 False  ✅/DONE
matplotlib__matplotlib-22865         a0  0.903  0.903 False HIGH    8    8    8 False  ✅/DONE
matplotlib__matplotlib-22865         a1  0.929  0.929 False HIGH    8    8    8 False  ✅/DONE
matplotlib__matplotlib-24970         a0  0.182  0.182 False LOW    21    5    5 False  ✅/DONE
matplotlib__matplotlib-24970         a1  0.036  0.036 False LOW    21    2    2 False  ✅/DONE
matplotlib__matplotlib-25775         a0  0.424  0.390 False LOW    39   31   46 False  ✅/ROUNDS_EXHAUSTED
matplotlib__matplotlib-25775         a1  0.626  0.454 False LOW    39   28   35 False  ✅/ROUNDS_EXHAUSTED
scikit-learn__scikit-learn-14894     a0  0.128  0.128 False LOW    13    3    3 False  ✅/DONE
scikit-learn__scikit-learn-14894     a1  0.128  0.128 False LOW    13    3    3 False  ✅/DONE
scikit-learn__scikit-learn-26323     a0  0.982  0.982 False HIGH    4    3    3 True   ✅/DONE
scikit-learn__scikit-learn-26323     a1  0.982  0.982 False HIGH    4    3    3 True   ✅/DONE
sphinx-doc__sphinx-10449             a0  0.156  0.187 False LOW    12    2    5 False  ✅/DONE
sphinx-doc__sphinx-10449             a1  0.237  0.230 False LOW    12    6   12 False  ✅/DONE
sphinx-doc__sphinx-9602              a0  0.753  0.001 False LOW    12   10 16116 False  ❌/ROUNDS_EXHAUSTED
sphinx-doc__sphinx-9602              a1  0.519  0.467 False LOW    12    9   19 False  ❌/DONE
sympy__sympy-14248                   a0  0.435  0.435 False LOW    65   68   68 False  ❌/ROUNDS_EXHAUSTED
sympy__sympy-14248                   a1  0.533  0.533 False LOW    65   44   44 False  ❌/ROUNDS_EXHAUSTED
sympy__sympy-17655                   a0  0.822  0.822 False HIGH    4    6    6 True   ✅/DONE
sympy__sympy-17655                   a1  0.828  0.828 False HIGH    4    5    5 True   ✅/DONE
sympy__sympy-21612                   a0  0.225  0.153 False LOW     2    4    7 True   ✅/DONE
sympy__sympy-21612                   a1  0.219  0.153 False LOW     2    4    7 True   ✅/DONE
sympy__sympy-22914                   a0  0.107  0.107 False LOW     2    6    6 True   ✅/DONE
sympy__sympy-22914                   a1  0.107  0.107 False LOW     2    6    6 True   ✅/DONE
a0: resolved 13; HIGH among resolved 6 (f_high=0.46) => INDETERMINATE [PRIMARY]; exact-match 2; excluding small-fix tasks: 3/8 HIGH; sim distribution (all 15): min 0.107 p50 0.435 max 1.000
a1: resolved 13; HIGH among resolved 6 (f_high=0.46) => INDETERMINATE; exact-match 2; excluding small-fix tasks: 3/8 HIGH; sim distribution (all 15): min 0.036 p50 0.533 max 1.000
```

**Reading by the pre-stated rule (a0, resolved 13): f_high = 6/13 = 0.46 ⇒ INDETERMINATE.** Not ≥ 2/3 (contamination-consistent), not ≤ 1/3 (capability-consistent). Excluding the 6 small-fix tasks (gold ≤ 4 changed lines): 3/8 HIGH. Exact-match to gold: 2 (`django-15315`, `astropy-14539` — 6- and 2-line fixes). **Seven resolved tasks are LOW-similarity: the agent resolved them with a different change from upstream's** — the shape memorisation does not produce. Both unresolved tasks are LOW. a1 reads identically (6/13, 0.46).

Cross-arm determinism, measured: 5 of 15 pairs are byte-identical across arms (13658, 15315, 14894, 26323, 22914) — the model writes the same fix regardless of the arm file; one of them (`sympy-22914`) is LOW-similarity to gold (0.107), i.e. identical across arms without resembling upstream.

**What this instrument can and cannot say:** it cannot separate memorisation from a forced minimal fix on the HIGH tasks (named before computing); it CAN say that half the solves were reached by a route upstream did not take. The 87 % ceiling is therefore not read as memorised, and not read as clean either — INDETERMINATE, as the rule says. The exploratory judge panel (unregistered; reported beside this, moving nothing) is recorded below when it lands.

## Exploratory judge panel (UNREGISTERED; 15 tasks × 3 blind Fable judges on the a0 patch + transcript vs gold; moves no reading)

| task | verdicts | forced fix |
|---|---|---|
| django__django-15315 | no/no/no | F/F/F |
| django__django-13658 | no/no/no | F/F/F |
| sympy__sympy-14248 | SIGNAL/SIGNAL/SIGNAL | n/n/n |
| django__django-15930 | no/no/no | F/F/F |
| sympy__sympy-22914 | no/no/no | F/F/F |
| sympy__sympy-17655 | SIGNAL/SIGNAL/no | F/F/F |
| matplotlib__matplotlib-24970 | no/no/no | F/F/F |
| sphinx-doc__sphinx-9602 | SIGNAL/SIGNAL/SIGNAL | n/n/n |
| sympy__sympy-21612 | no/SIGNAL/SIGNAL | F/n/n |
| matplotlib__matplotlib-22865 | no/no/no | F/F/F |
| scikit-learn__scikit-learn-26323 | no/no/no | F/F/F |
| scikit-learn__scikit-learn-14894 | no/no/no | F/F/F |
| matplotlib__matplotlib-25775 | no/no/no | F/n/F |
| sphinx-doc__sphinx-10449 | no/no/no | n/n/n |
| astropy__astropy-14539 | SIGNAL/SIGNAL/SIGNAL | F/F/F |

Signal from ≥ 2 judges on 5 of 15: `sympy-14248` (3/3), `sphinx-9602` (3/3), `astropy-14539` (3/3), `sympy-21612` (2/3), `sympy-17655` (2/3, weakest). Unanimous no-signal on the other 10, mostly where the fix is forced.

**Verified by the seat at the artifact (not the judges' word):**
- `sympy-14248` (UNRESOLVED, capped): gold's added line `s = pform     # First element` and `_keep_coeff(-c, m)` appear in the transcript FIRST as the agent's Edit input — before any read could have shown them (they are gold ADDED lines, absent from the base tree); the agent later rewrote both.
- `sphinx-9602` (UNRESOLVED, capped): gold's added comment `# Wrap the Text nodes inside brackets by literal node if the subscript is a Literal` and `nodes.literal('', '', subnode)` likewise appear first as the agent's Edit input; the agent then changed `literal`→`inline` and kept the now-false comment.
- `sympy-21612` (resolved): the agent wrote `# issue 21537` in a test — the string `21537` is in the transcript 6×, in the prompt 0×, in gold 0×. The judges recall 21537 as the upstream issue PR 21612 closed; the seat cannot verify that offline and says so.
- `astropy-14539` (resolved): the agent wrote *"I'll use 14545, a plausible next PR number for this fix"* and named the changelog `14545.bugfix.rst` — `14545` is in no input it was given; the judges recall it as the real upstream PR number (same caveat).

**The skeptic's caveats stand as the panel stated them:** three judges of one model family are correlated, not independent; the two identifier findings rest on the judges' own recall of upstream numbers; the 17655 docstring is a single mirror-inverted sentence; forced-fix is itself a judge call.

**Reading (exploratory, beside the registered INDETERMINATE):** the model has seen upstream's fixes for at least two of these tasks — verbatim added lines reproduced before they could be read — and recall did not deliver either solve. Contamination is present on this substrate at this tier; whether it inflates the 13/15 cannot be told from these instruments. That is the honest S1 statement, and it is the reason item 12 gave for S2-Lean: the kernel decides there, and no proxy is needed.
