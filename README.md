# SaltBench

A referee-gated, pre-registered protocol for measuring whether a change to how a coding agent is
instructed changes what it can get past a machine referee. Version 1 ships the protocol, two task
populations with their provenance, frontier baselines on both, a pre-registered null on one with
the blind triage that explains most of it, and the instrument findings as results. It claims no
effect of the method under test; the tests that could show one are stated in the paper and remain
open.

The paper is `paper/saltbench-v1.tex` (build: `cd paper && tectonic saltbench-v1.tex`; the PDF is
committed beside it). Every number in the paper carries a comment naming the file in this
repository it was copied from.

## What is here

| path | what |
|---|---|
| `PRE-REGISTRATION.md` | wave 1 on SWE-bench Verified, frozen before any model call (the substrate was later abandoned as saturated; the datum stays) |
| `SCOUT-STAGE0.md`, `RESULTS-stage0-2026-08-29.md` | the S1 control protocol and its stage-0 result |
| `SCOUT-S2LEAN-STAGE0.md` | the S2-Lean protocol on CLEVER Task 1, frozen 2026-08-29, with amendments 1 to 10 and their results appended in place |
| `AMENDMENT-11` to `AMENDMENT-17`, `RESULT-*` | the later S2-Lean and S2-Rust amendments, each frozen before its first call, and their results |
| `RESULT-DT-sonnet-probe-2026-09-02.md` | the lower-tier probe on the hard band: the paired quote at a 40-call cap, and the appended episode at a 120-call cap that showed the cap was binding |
| `RESULT-DY-deepswe-scout-2026-09-02.md` | the scout for a second version-2 population, verdict no, run at zero model tokens |
| `TRIAGE-B-failures-2026-09-01.md` | the blind triage of every failed S2-Lean stage-B cell; problem 18's stage C is machine-checked unsatisfiable |
| `AUDIT-FINDING-s2lean-2026-08-29.md` | the audit of the benchmark's reference checker |
| `harness/` | the harness: episode drivers, fences, checkers, morning-line instruments, self-tests; `harness/HASHES.txt` pins everything |
| `harness/s2lean/views/` | the CLEVER problems re-cut into stage views (MIT, see `PROVENANCE.md`) |
| `evidence/` | the instruments' outputs and manifests the result files cite, byte for byte |
| `PROVENANCE.md` | every population and third-party artifact, its pin, its licence, what is redistributed |
| `PUBLISH-CHECKLIST.md` | the hygiene and provenance checklist driven before publication |
| `select_tasks.py`, `TASKLIST.json`, `IMAGE-DIGESTS.json` | the S1 draw as code, the frozen list, the evaluation image digests |

The run records (`runs/`, 61 MB of transcripts and manifests) and the S2 episode archives are a
separate data asset, not in the git tree; its DOI is assigned at release (Zenodo) and recorded here
on the flip day.

## The protocol in five lines

1. A referee decides every outcome (the Lean kernel by replay with an axiom allowlist, the Verus
   verifier behind three integrity layers, or a hidden test suite), outside the agent's own
   toolchain invocation.
2. A fence denies the agent the network, the ground truth and the harness state, and the fence
   is measured by probes before the run. The v1 probes spoke only the sandbox's language, and the
   layer above it (the agent's own file tool) was unfenced for every v1 episode; amendment 17
   records the finding, the repair and its canary, and the paper states it. Its section 11 adds
   the campaign-wide audit: across 278 landed Lean episodes no agent ever directed a file tool at
   a fenced path. The gap was open and its measured exploitation is zero, which is not the same as
   protection.
3. A dated freeze commit is the authorization. Predictions are registered and scored; adverse
   outcomes are named; every later change is a dated amendment appended before its own first
   call. Frozen text is never edited.
4. A budget stop is a halt, never a failure.
5. Of every gate, ask which arm is more likely to trip it.

## Reproducing

The task populations are re-derived from their pinned sources by the harness's view builders.
The pins are lines in `harness/HASHES.txt`; the episode scripts refuse to run a stage whose view or
checker hash is not the pinned one. The morning-line instruments reproduce every rate in the paper
from the episode manifests, and their self-tests drive the script's real argv. The episodes ran
under Claude Code 2.1.251 headless on a subscription; the agent is not redistributed, and a rerun
needs a Claude Code login, the Lean and Verus toolchains at the pinned versions, and a run host
laid out as `SCOUT-S2LEAN-STAGE0.md` section 3 and `AMENDMENT-15-s2rust-2026-09-01.md` section 6
describe (the scripts call it `studio`; set `STUDIO` to your own ssh host).

```
# 1. verify every file pin in the table against the tree (95 files; every line must read OK)
cd harness && awk '!/^#/ && NF==2 && $2 ~ /^[0-9a-f]{64}$/ {print $2"  "$1}' HASHES.txt \
  | while read h f; do [ -f "$f" ] && echo "$h  $f"; done | shasum -a 256 -c

# 2. rebuild the 30 projected S2/S1 problem statements (not redistributed; verifies against the pin)
python3 fetch_problem_statements.py --download        # or --rows <your data/verified.json>

# 3. rebuild the S2-Lean views from a CLEVER checkout at the pinned commit (tracked under s2lean/views/)
python3 s2lean/build_views.py <clever-checkout> s2lean/views

# 4. rebuild the S2-Rust views from the pinned tasks.jsonl and compare the set-hash to HASHES.txt
python3 s2rust/build_views_verus.py <tasks.jsonl> <viewsdir> --projects AC,NR
python3 s2rust/views_sethash.py <viewsdir>          # -> "<sha256> count=207"; grep views-set-sha256 HASHES.txt

# 5. the drivers (each refuses to start unless its own pins and smoke gate hold)
caffeinate -dims ./run_stage0.sh <k> [start_index]                 # S1, env: BENCH H ARMS
./s2lean/run_s2_stage0.sh <A|B|C> <k> [start_index]                # S2-Lean, env: BENCH H EPROOT ARMS
printf '%s\n' a0 | ./s2rust/episode_s2rust.sh <task_id>            # one S2-Rust episode, env: BENCH H CFG VIEWS VERUS_ROOT

# 6. the morning lines, from the manifests a run leaves under its state root
python3 s2lean/s2_morning_line.py <state-root> <k>
python3 morning_line.py <state-root> <a0-report> <a1-report>
```

## Licence

Code under Apache-2.0 (`LICENSE`); data and documents under CC BY 4.0 (`LICENSE-DATA`).
Third-party material keeps its own licence: CLEVER (MIT, Trishul, UT Austin), VeruSAGE-Bench and
lynette (MIT, Microsoft), SWE-bench (MIT) and the source repositories of the drawn issues. See
`PROVENANCE.md`.

No issue text from SWE-bench Verified is redistributed here: its dataset card carries no licence
field, so the repository ships the 30 ids, the pinned revision and two checksums instead, and
`harness/fetch_problem_statements.py` rebuilds the projection and verifies it against the pin
(`PROVENANCE.md` section 1.3).

## A glossary for the record's vocabulary

The protocol documents, amendments and result files are frozen: they are appended to, never edited.
They therefore keep the working vocabulary of the operation that produced them. Nothing in it is a
technical term of this benchmark, and none of it is needed to read the paper; it is listed here so
that a reader meeting a word in a frozen document knows what it meant.

| word | what it means in these documents |
|---|---|
| the Captain | the repository owner, who rules on scope, publication and anything that leaves the machine |
| the helm | the coordinating session that carries work between sessions and to the owner; it commissions and does not decide the science |
| a seat | one working session with its own written instructions, memory and workdir, named (`bench` ran the campaign, `paper` prepared this publication). "Seat instructions" are that session's brief |
| the bus | the append-only log the sessions post to. A citation like "bus 09/01 21:35:05" or "bus offset 30441837" names a post by its timestamp or its byte offset in that file |
| a council | a sitting at which the owner rules. "Ruled at council" means the decision is the owner's, not a session's |
| a desk row | a tracked unit of commissioned work, carrying a short id (`DD`, `DT`, `DY`). Row ids appear in amendment headers to say what authorized the work |
| a refuter | a session commissioned to attack a result, a gate or a document before it ships. "The refuter pass" is that attack and its repairs; findings carry ids like `F3`, `FN2-01`, `P2C2-01` |
| a commission | the written instruction a session was given. "Beyond the commission" flags work that exceeded it, so a reader can strike it |
| the Studio | the run host on which the episodes executed. `STUDIO` is an environment variable naming it; a rerun sets it to its own host |
| a morning line | an instrument that recomputes every published rate from the run manifests, so no rate in the paper is typed by hand |
| the fleet | the set of projects this one sits beside. It appears only in provenance and hygiene notes, never in a result |

## Citing

See `CITATION.cff`.

## Contributing

The frozen documents are appended to, never edited. Commit messages carry no chat-session
trailers or URLs; `Co-Authored-By` is fine. The Scrub CI (`.github/workflows/scrub.yml`) enforces
both on every push, and a fresh clone arms the local hook with
`git config core.hooksPath .githooks`.
