# SCOUT — STAGE 0: the CONTROL protocol (plain · placebo), frozen

**Frozen 2026-08-28, bench seat, BEFORE any model call by this seat.** Commission: council minute
2026-08-28 ITEM 12 (`seat/briefs/2026-08-28-COUNCIL-minute.md`) and the boot brief
`seat/briefs/0000-BOOT-bench.md`. This document supersedes NOTHING in `PRE-REGISTRATION.md` (v4)
or `DESIGN-gate-wave1.md` (v4): wave 1 is **HELD** — no model call is made under that design — and
this stage-0 protocol REUSES its arm-independent machinery by reference (task draw, image digests,
exclusions, harness pin, CHECK 2b, metered unit) while replacing the agent, the arms and the rule
of amendment. Where this page and those documents differ on an *agent* or *arm* matter, this page
governs for the scout; where they differ on a *scoring* or *substrate* matter, they govern and this
page is wrong.

**The rule of amendment, restated in the form that matters (boot brief act A):** nothing runs before
ITS OWN protocol is frozen and dated. Stage 0 freezes the two CONTROL arms. Every TREATMENT arm is
registered later as a **dated amendment appended below the line at the bottom, before that arm's
first call**. The pre-registration's *fixed-sequence* rigidity (primary → secondaries at α=0.05) is
**deliberately dropped**: the scout's deliverable is believability, not a p-value (item 12), so
there is no family of tests to order. Dropping it is said here so it is not slipped.

## 0 · What stage 0 is for

Two control arms, PLAIN and PLACEBO, on the S1 substrate, so that (a) the control numbers exist —
solve rate and the metered-token distribution (its p90 is what the pre-registration's cap RULE
consumes) — and (b) the cheapest non-mechanism explanation of any later treatment win, *"any
equal-length instruction block helps"*, has a measured value before a treatment arm exists.
Stage 0 measures nothing about the salt method. It **cannot** show that a treatment works; it can
only make a later claim that one does harder to fake.

## 1 · The hermetic agent (AGENT OUTSIDE, ENVIRONMENT INSIDE — the 13:3x ruling)

**Agent = Claude Code proper, `claude` 2.1.251, headless (`-p`), on the Studio host, on the
jykriterion subscription.** Never an API key; never the OAuth token in a custom harness.

```
CLAUDE_CONFIG_DIR = /Users/jyh/.claude-bench      credentials + settings.json + the harness hook; nothing else
HOME              = <STATE>/<ep>/home             fresh, empty, per episode
cwd               = <EPROOT>/<ep>/wc              the working copy (§3)
PATH              = /usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin
claude -p "$(cat <STATE>/<ep>/prompt.md)" \
       --model claude-sonnet-5 --effort high \
       --max-turns 40 --dangerously-skip-permissions \
       --disallowedTools "WebFetch,WebSearch,Agent,Task" --strict-mcp-config \
       --setting-sources user --output-format json --session-id <ep-uuid>
```
(`harness/episode.sh` is the normative form of this block; where prose and script differ, the
script at the pinned commit is definitive — the pre-registration's §3 rule, applied here.)

- **Hermeticity of the agent** is exactly: no fleet tree, no memory bank, no MCP, no CLAUDE.md
  above `<EPROOT>/<ep>/`. `<EPROOT>` and `<STATE>` are under `/Users/jyh/bench/` on the Studio, a
  machine holding no `~/projects/claude`. **Asserted, not assumed, before every episode:** no
  `CLAUDE.md` exists on the path from `/` to `<EPROOT>/<ep>/` exclusive; `$CLAUDE_CONFIG_DIR`
  contains no `CLAUDE.md` and no `projects/*/memory/`; `$CLAUDE_CONFIG_DIR/settings.json` and the
  hook script hash to the values recorded in this repo (`harness/HASHES.txt`).
- **The arm IS a CLAUDE.md file** at `<EPROOT>/<ep>/CLAUDE.md` — one directory above the working
  copy, so Claude Code's ancestor discovery loads it and the patch never contains it. Its sha256
  is recorded per episode. `--bare` is NOT used (it disables CLAUDE.md discovery).
- **Network is closed to the agent, three ways, and audited a fourth:** `WebFetch`/`WebSearch`
  are disallowed; a `PreToolUse` hook on `Bash` (harness code, byte-identical in every arm) refuses
  commands matching the network pattern in `harness/hook-deny-network.sh` (curl · wget · git
  clone/fetch/pull · pip/conda/npm install · ssh · scp · nc); the episode container is started with
  `--network none`; and post hoc every Bash command in the transcript is grepped against the same
  pattern — a hit is recorded as `network_attempt` on the episode and the episode is **VOID**
  (reported, never scored). *The issue's fix is public on GitHub; an agent that can fetch it is not
  being measured.*
- **Subagents are disallowed** (`Agent`/`Task`), so the call cap and the metered sum count one
  linear transcript; `isSidechain=true` records, if any appear, VOID the episode.
- **The agent's tests run INSIDE the instance image** (§3), never on the host: the host has no
  project dependencies, and the base block (§4) tells the agent the one way to run anything.

## 2 · Substrate, task subset, scoring, images — UNCHANGED from v5, by reference

- Dataset pin: `princeton-nlp/SWE-bench_Verified`, split `test`, revision
  `c104f840cc67f8b6eec6f759ebc8b2693d585d4a`, 500 rows, content digest
  `4f74c5cff0d5838cd8026295d7ed61ed8171147207ead7d795ff18c977712ae2` — **the recipe is now in
  the repo** (`select_tasks.py --verify-dataset`; silicon's handoff defect, closed): 
  `sha256(json.dumps(rows, sort_keys=True, separators=(",",":")).encode())`.
- **Task subset = the first `k` of the frozen `TASKLIST.json` `pilot` list, in draw order, k = 15.**
  Episodes run task-major, arm-minor: task 1 (arm A, arm B), task 2 (arm B, arm A), … — the
  within-task order alternates so a quota stop leaves complete PAIRS and neither arm always runs
  in the fresher window. Extending k past 15 is an amendment; shrinking it is a REPORTED stop.
- `solved := official harness swebench==4.1.0 (726c546) reports resolved=true` for the SUBMITTED
  patch, run post hoc as a batch with `-d data/verified.json` (local file, content-pinned), `-i`
  the k ids, `--namespace swebench --instance_image_tag latest --max_workers 1 --timeout 1800`.
  Images by DIGEST from `IMAGE-DIGESTS.json` with the pre-registered BRIDGE
  (`docker pull --platform linux/amd64 <image>@<digest>` · `docker tag <image>@<digest>
  <image>:latest`) — 4.1.0 calls `images.get(key)` before any pull, so the bridged tag is what it
  opens (verified in source at this hand). The images are `linux/amd64` only (registry manifest,
  read without a daemon); they run under Rosetta on the arm64 Studio; 4.1.0 defaults `arch=x86_64`
  and creates containers with `platform=linux/x86_64` (source read at this hand).
- **Exclusions per `EXCLUSIONS.md`, arm-independent, both controls run before either arm on every
  task in the subset**: pre-flight (empty patch ⇒ all F2P fail, all P2P pass) and gold-control
  (gold patch resolves). Rows are logged for all k, survivors included.
- No held-out identity, gold patch, test patch or `hints_text` reaches the agent: the prompt is
  built from `problem_statement` ALONE (§4) by a builder whose only dataset argument is the
  instance id (the DESIGN §4 CHECK 1 discipline, applied to the prompt builder).

## 3 · One environment for the agent's tests, the checks and the scorer

Per episode: `docker create --platform linux/amd64 <image>@<digest>`; `docker cp <ctr>:/testbed`
to `<EPROOT>/<ep>/wc` **excluding every `.git` at any depth**; `docker rm`. Then **CHECK 2b on the
host copy** and, after the container below is up, **CHECK 2b again inside it on `/testbed`** —
all four states, fail-closed, logged with the digest (`harness/check2b.sh`):

```
no .git at ANY depth · no packed-refs · no file named .git containing "gitdir:" ·
git rev-parse --git-dir FAILS with GIT_DIR/GIT_COMMON_DIR unset ·
(host form) the image's RepoDigests carries the pinned digest
```

Before ANY harness run (pre-flight, gold-control, scoring) `harness/bridge_assert.sh` asserts, per
id, that `<image>:latest` and `<image>@<digest>` are the SAME image object (`docker image inspect
.Id` equal) — the harness prefers a local `:latest` and never compares a digest (refuter v3/v4),
so this equality is the certificate that the key it opens is the image the table certifies.
**Infrastructure failures get exactly ONE deterministic retry** (same image, same task, same arm,
logged) before an episode is recorded `HARNESS_ERROR`; a HARNESS_ERROR scores UNSOLVED for that
arm and is never an exclusion (EXCLUSIONS.md).

The episode container: `docker run -d --platform linux/amd64 --network none --name ep-<ep>
-v <EPROOT>/<ep>/wc:/testbed -w /testbed <image>@<digest> tail -f /dev/null`. The bind mount
REPLACES the image's `/testbed` (and its 162-tag `.git`) with the agent's copy; the conda env
`testbed` in the image is untouched. The agent reaches it through ONE wrapper, `<EPROOT>/<ep>/rt`,
which runs `docker exec -w /testbed ep-<ep> bash -lc 'source /opt/miniconda3/bin/activate testbed
&& <cmd>'` and appends every command + exit code to `<STATE>/<ep>/rt.log`.

**The submitted patch is NEVER a terminal `git diff` of a repo the agent could touch.** A shadow
git-dir at `<STATE>/<ep>/shadow.git` (outside the agent's tree; `GIT_DIR` set only in the harness
process) commits the pristine copy as `base` before the episode; after it,
`git --git-dir=shadow.git --work-tree=wc add -A && git diff --cached --binary base` is the patch,
sha256-recorded, written to `predictions.jsonl` as `model_patch`. The tree's own `.gitignore` is
honoured (build artifacts drop, as in the official convention). An agent that `git init`s its
working copy is recorded (`agent_made_git=true`), not penalised.

*Feasibility, not validity:* bind-mount I/O under Rosetta is the untested term. The smoke probe
(§7) times one visible-suite run; if a task's visible suite cannot complete inside the wall-clock
ceiling in either arm, that is an arm-independent HARNESS_ERROR row, never an exclusion decided
after seeing an arm.

## 4 · The two arms — the prompt is IDENTICAL, only the CLAUDE.md differs

**The prompt** (`-p`), byte-identical across arms, built by `harness/build_prompt.py` from
`problem_statement` only:

```
You are working in a checkout of the repository at <EPROOT>/<ep>/wc.
Resolve the issue below by changing the repository. When you are done, stop; your changes in the
working copy are your answer. Do not describe the change instead of making it.

<issue>
{problem_statement}
</issue>
```

**The arm file** = `BASE` block + `ARM` block. `BASE` (byte-identical in every arm; the only place
the agent learns HOW to run anything):

```
# Working notes
- Run any project command inside its environment with `<EPROOT>/<ep>/rt <command>`,
  e.g. `<EPROOT>/<ep>/rt python -m pytest path/to/test_file.py -x -q`.
  To use shell features (pipes, cd, &&), quote the whole command as one argument:
  `<EPROOT>/<ep>/rt 'cd tests && python -m pytest test_x.py -q | tail -30'`.
  Commands run without it use a bare host and will not find the project's dependencies.
- There is no network. Do not try to install packages or fetch anything.
- Edit files in place under `<EPROOT>/<ep>/wc`. Do not create commits.
```
(normative bytes: `harness/base.md`, with `__EP__` substituted per episode)

- **Arm ids are OPAQUE on the Studio: `a0` = PLAIN, `a1` = PLACEBO** (`harness/arms/a0.md`,
  `harness/arms/a1.md`). The words "plain" and "placebo" appear in this repo, which is not on
  the Studio; nothing readable by the agent maps an id to a meaning.
- **PLAIN (`a0`)**: `ARM` is EMPTY (`arms/a0.md` is a zero-byte file). The arm file is `BASE`
  alone — 534 bytes rendered.
- **PLACEBO (`a1`)**: `ARM` = `arms/a1.md`, 1,768 bytes, a nine-step generic engineering-process
  checklist (read the issue twice, locate the code, reproduce, minimal change, consistent style,
  run the nearby tests, re-check, review the diff, stop) containing **no** salt content — no
  specification, no property, no checker, no proof, no "statement", no verification vocabulary.
  **Its literal IS the intervention** (refuter v3: "REJECTED." and "please revise" are different
  interventions); it is frozen at commit, sha256 and byte count in `harness/HASHES.txt`
  (`rendered-a1(__EP__)`), and `episode.sh` refuses to run an arm whose rendering is not the
  pinned one.
- **The length rule for every later treatment arm:** its `ARM` block must be within **±10 % of
  the placebo's byte count**, or its amendment must register a length-matched placebo variant
  alongside it and run that too. *Bytes, not tokens: the tokenizer is not callable without a
  model call, and the arms are prose of similar density — the caveat is named, not hidden.*
- **Arm-blindness:** the agent is not told an arm exists. Episode ids are opaque
  (`ep-<8 hex>`); the id→arm map lives in `<STATE>/manifest.jsonl`, never under `<EPROOT>`; the
  arm file is the only byte that differs, and the agent sees it as "project notes".
  `<EPROOT>/<ep>/` contains exactly `CLAUDE.md`, `rt`, `wc/` — nothing else, asserted.

## 5 · Metering — from the session jsonl, deduplicated by `message.id`

The session file is `$CLAUDE_CONFIG_DIR/projects/<cwd-slug>/<ep-uuid>.jsonl`, copied verbatim
into the episode artifact. **One API call lands as one `assistant` line PER CONTENT BLOCK, each
carrying the SAME `message.id`, `requestId` and `usage`** (measured at this hand on this seat's
own session: 45 lines, 22 calls). `harness/meter.py` therefore:

- groups `type=="assistant"` lines by `message.id`; **calls := distinct `message.id`**;
- sums per call `usage.input_tokens + cache_creation_input_tokens + cache_read_input_tokens +
  output_tokens` — **the metered sum, the pre-registration's unit, unchanged**; reports the four
  classes separately, `output_tokens_details.thinking_tokens`, the `model` string per call (an
  OBSERVATION: `claude-sonnet-5` is requested, whatever lands is reported), `service_tier`,
  and `speed`;
- flags and VOIDS on any `isSidechain=true` line (a subagent ran) and on any line whose
  `usage` omits a class (a schema drift is a metering hole, not a zero);
- cross-checks its call count against `num_turns` in the `--output-format json` result and its
  totals against that result's `usage`; a mismatch is reported, and the jsonl governs;
  `total_cost_usd` from the CLI is recorded and NOT used (dollars struck, item 12).

**The call classes "ALL calls in the task" contains, named because no refuter pass named them
(distillation §7):** *subagent* calls (`isSidechain=true`) — counted, and they VOID a stage-0
episode because `Agent`/`Task` are disallowed; *compaction* calls — Claude Code's context
summarisation lands as a `system`/`summary` record: its usage is counted where it lands and the
compaction COUNT is reported per episode; *API-level retries* (429/5xx re-sends) never land in
the jsonl and are not billed — **the metered sum is what LANDED**, which is also what the quota
consumed. The per-call maximum is reported so the pre-registration's 200,000 per-call sub-cap
has a measured distribution behind it before it is enforced anywhere.

**Termination**, typed per episode: `DONE` (the agent stopped) · `ROUNDS_EXHAUSTED`
(`--max-turns 40` fired: the CLI's `num_turns == 40` or the transcript's 40th call is the last) ·
`WALLCLOCK` (`timeout 5400` killed it) · `TOKEN_CEILING` (the harness killed it at a metered
sum ≥ 3,000,000 — a SAFETY stop only; stage 0 has NO enforced parity cap, because its output is the
number the cap rule consumes) · `HARNESS_ERROR` · `VOID` (§1 network/sidechain). `--max-turns`
is accepted by 2.1.251 and absent from its `--help`; **its semantics are established by the smoke
probe (§7) before the first episode, and if it does not cap, the hook counts calls from
`transcript_path` and refuses tools past 40.**

## 6 · What counts as an episode's artifact (`<STATE>/<ep>/`, tarred, sha256-listed)

`manifest.json` (task id · arm · digest · CLAUDE.md sha · prompt sha · settings sha · hook sha ·
claude version · flags verbatim · start/end UTC · termination · exit code) · `session.jsonl`
(verbatim) · `result.json` (the CLI's) · `model_patch.diff` + sha · `check2b.host.log` ·
`check2b.container.log` · `rt.log` · `network_audit.txt` · `meter.json` · `configdir-projects/`
(the config dir's `projects/` subtree, archived then REMOVED after every episode so nothing but
credentials crosses episodes) · and, after the batch, the harness `report.json` for the instance
and the pre-flight/gold-control rows. **`manifest.json` — the only file naming the arm — is
written AFTER the claude process has exited** (arm-blindness by construction: during the run the
id→arm map exists only in the driver's memory). **A green exit says something RAN, not what:** an
episode with no `model_patch.diff` is `NO_PATCH`, scored unsolved, never "missing".

## 7 · Order of operations, and the first model call

1. This freeze + `harness/` committed; `HASHES.txt` written; refuter pass (3 refuters:
   arm-blindness of the pair · metering completeness · leak surfaces · a cheaper explanation for a
   placebo win) — REPAIR-THEN-FIRE, repairs appended to this page dated, before step 2.
   **The harness, all in `harness/`, each with a driven self-test where one is possible:**
   `episode.sh` (runner + watchdog) · `rt.template` (the one wrapper) · `check2b.sh`
   (+`check2b.selftest.sh`, 6 arms) · `hook-deny-network.sh` (`--selftest`, 8 arms; `--pattern`
   is shared with the audit) · `meter.py` (`--self-test`, 9 checks) · `build_prompt.py`
   (`--self-test`: five held-out fields smuggled into the statement, each refused) ·
   `bridge_assert.sh` · `preflight_gold.sh` · `score.sh` · `run_stage0.sh` (driver) ·
   `settings.bench.json` (installed verbatim as `~/.claude-bench/settings.json`) · `hashes.sh` →
   `HASHES.txt`. The Studio holds a copy of `harness/` plus `data/verified.json`,
   `TASKLIST.json`, `IMAGE-DIGESTS.json` under `~/bench/harness/`; the copy's file shas are
   asserted against `HASHES.txt` by `episode.sh` for the two files the agent's run depends on
   (settings, hook) and by the sync receipt for the rest.
2. Captain's hand: `~/.claude-bench` logged in as jykriterion **from inside `tmux attach -t
   bench`** on the Studio (so the credential is created by the session that will read it).
3. **SMOKE PROBE — the first model call on this account, DECLARED here so it owns its boundary:**
   one `claude -p` on the jykriterion account, task `django__django-15315` machinery but the
   prompt `"Reply with the single word OK and stop."`, `--max-turns 2`. It establishes: the
   keychain reads under tmux-over-ssh, the jsonl lands where §5 says, `num_turns` semantics,
   the `model` string, and (separately, no model) one visible-suite run timing through `rt`.
   **It is not an episode, is not scored, and is reported on the bus with its metered tokens.**
4. Pre-flight + gold-control on the k tasks (containers only, no model).
5. Episodes, task-major, sequential, in tmux `bench:run` on the Studio; a bus line per landing
   with the metered sum; `~/bench/logs/` is the live log. The quota triple is read ONCE at
   dispatch, never polled; the 5-hour window is the concurrency limit (sequential = 1).
6. Batch scoring; then the MORNING LINE: solve rate per arm with `b`/`c`, metered-sum
   distribution per arm (p50/p90/max), termination-reason counts, VOID count, and the p90 that the
   cap rule will consume — **no p-value, by design.**

**Model sequence:** Sonnet for both controls and for every treatment arm first; Opus/Fable only on
an arm pair that differs, Fable episodes only on the Captain's word (item 12).

---

*Nothing below this line existed before this seat's first model call. Amendments are appended,
dated, with their reason — never edited into the text above. Treatment arms register here.*

---
