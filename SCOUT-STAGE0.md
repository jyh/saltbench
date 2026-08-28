# SCOUT — STAGE 0: the CONTROL protocol (plain · placebo), frozen

**Frozen 2026-08-28, bench seat, BEFORE any model call by this seat** (the freeze commit is the pin;
draft `a03bd3c` was refuted first — 5 lenses, 42 confirmed findings, 10 fatal — and this is the
repaired text; the verdict lives in `seat/fleet/REFUTER-saltbench-stage0-2026-08-28.md`).
Commission: council minute 2026-08-28 ITEM 12 and the boot brief `seat/briefs/0000-BOOT-bench.md`.

This document supersedes NOTHING in `PRE-REGISTRATION.md` (v4) or `DESIGN-gate-wave1.md` (v4):
wave 1 is **HELD** — no model call is made under that design — and stage 0 REUSES its
arm-independent machinery by reference (task draw, image digests, exclusions, harness pin, CHECK 2b,
the metered unit) while replacing the agent, the arms and the rule of amendment. Where this page and
those documents differ on an *agent* or *arm* matter, this page governs for the scout; where they
differ on a *scoring* or *substrate* matter, they govern and this page is wrong.
**`harness/` is the NORMATIVE form of every mechanism named here** (the pre-registration's §3 rule):
where prose and script differ, the script at the freeze commit is definitive.

**The rule of amendment (boot brief act A):** nothing runs before ITS OWN protocol is frozen and
dated. Stage 0 freezes the two CONTROL arms. Every TREATMENT arm is registered later as a **dated
amendment appended below the line at the bottom, before that arm's first call**, carrying its arm
PROFILE (§4). The pre-registration's *fixed-sequence* rigidity is **deliberately dropped**: the
scout's deliverable is believability, not a p-value (item 12), so there is no family of tests to
order. Dropping it is said here so it is not slipped.

## 0 · What stage 0 is for — and what it cannot show

Two control arms, PLAIN (`a0`) and PLACEBO (`a1`), on the S1 substrate, so that (a) the control
numbers exist — solve rate and the metered-token distribution, whose `a0` p90 is what the
pre-registration's cap RULE consumes — and (b) the cheapest non-mechanism explanation of a later
treatment win, *"a longer instruction block helps"*, has a measured value before a treatment arm
exists. Stage 0 measures nothing about the salt method.

**Stage 0 CANNOT show (the wave-1 cannot-show list, re-cut for the scout):**
1. *A mechanism.* PLAIN–PLACEBO differs in bytes AND content by design; it is not a controlled
   contrast, it is the price of a generic block. A placebo win is "compliance with house notes",
   inseparable from evaluation-aware behaviour (the agent sees a working path and project notes;
   it is not told an arm, a gate, or an evaluation exists — the NEUTRAL framing, named as an artifact).
2. *Arm-blindness by construction.* The agent runs as the same uid as the harness with a Docker
   socket in reach; nothing on the host is unreadable to it. Blindness is **by audit** (§1, §5):
   every tool call is in the transcript and an escape VOIDs the episode.
3. *A closed network.* The test environment has none; the agent's host does. Closed by hook, by
   audit, and by the absence of a reason — not by the OS. The residual is named, owned, and dated:
   the uid split + `pf` rule for the agent user is the Captain's-hand item for the next sitting.
4. *Separation of sampling variance from arm effect.* No task-arm is repeated at k = 15.
5. *Contamination.* A memorised task solves in both arms and pulls the pair toward concordance.

## 1 · The hermetic agent (AGENT OUTSIDE, ENVIRONMENT INSIDE — the 13:3x ruling)

**Agent = Claude Code proper, `claude` 2.1.251, headless (`-p`), on the Studio host, on the
jykriterion subscription.** Never an API key; never the OAuth token in a custom harness.

```
CLAUDE_CONFIG_DIR = /Users/jyh/.claude-bench   credentials (macOS Keychain, keyed to this dir) + settings.json
HOME              = /Users/jyh                  REAL — the Keychain credential is unreachable from a fresh HOME
                                                (measured); ~/.claude is NOT read because CLAUDE_CONFIG_DIR overrides it
cwd               = /Users/jyh/work/<ep>/repo   the working copy; <ep> = ep-<8 hex>, neutral root, no "bench" in the path
PATH (agent)      = /usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin:~/.local/bin   (the login PATH,
                                                echoed by the smoke probe from INSIDE the agent and recorded)
env -i HOME USER LOGNAME PATH TERM LANG TMPDIR CLAUDE_CONFIG_DIR BENCH_EP   (BENCH_EP = the episode dir, read by the hook)
$(command -v claude) -p "$(cat prompt.md)" --model claude-sonnet-5 --effort high --max-turns 40 \
   --dangerously-skip-permissions --disallowedTools "WebFetch,WebSearch,Agent,Task,Workflow,Skill" \
   --strict-mcp-config --setting-sources user,project --output-format json --session-id <uuid>
```
- **`--setting-sources user,project`** — `project` is REQUIRED: without it Claude Code 2.1.251 loads
  no project-tree CLAUDE.md at all (refuter F0; the draft said `user` and would have run both arms as
  the same run). The `user` source is `~/.claude-bench/settings.json` (= `harness/settings.bench.json`,
  sha-pinned), which carries the one `PreToolUse` hook. `--bare` is never used (it disables CLAUDE.md).
- **Hermeticity of the agent** is exactly: no fleet tree, no memory bank, no MCP, no CLAUDE.md above
  `/Users/jyh/work/<ep>/`. Asserted before every episode (`episode.sh` §6): no `CLAUDE.md` on the
  path from `/` to the episode dir; the extracted tree carries no `CLAUDE.md`, `CLAUDE.local.md`,
  `.claude/`, `.mcp.json`; the config dir's `projects/` is EMPTY and its entries match a frozen
  allowlist; settings, hook, arm rendering and the task's canonical prompt hash to `HASHES.txt`.
- **The arm IS a CLAUDE.md file** at `/Users/jyh/work/<ep>/CLAUDE.md` — one directory above the
  working copy, so ancestor discovery loads it and the patch never contains it. **`/Users/jyh/work`
  holds ONLY the running episode** (asserted; the previous tree is archived into state at landing).
- **The arm name exists in no file, no argv and no env while claude runs**: it reaches `episode.sh`
  as an environment variable consumed and unset; `prompt_meta.json` carries no arm field;
  `manifest.json` — the only file naming the arm — is written after the process has exited.
- **Network and host reach — hook, audit, and the OS where it applies:** `WebFetch`/`WebSearch` are
  disallowed; the test container runs `--network none`; the `PreToolUse` hook on `Bash`
  (`harness/hook-deny-network.sh`, identical in every arm) blocks two classes — **ESCAPE** (fetchers,
  installers, sockets, `gh`, the `docker` CLI by name, and any literal path into `~/bench`, `~/.claude*`
  or another episode; the agent's own episode path is exempt) and **URL** (a scheme in the command
  text — an issue often quotes one; blocked so nothing is fetched, counted, never a VOID by itself).
  Post hoc, `meter.py` audits EVERY tool call — Bash commands and the paths of Read/Edit/Write/Glob/
  Grep: an escape whose result is the hook's BLOCKED text is an **attempt** (counted); an unblocked
  escape, a file tool outside the episode tree, or a spawn tool **VOIDs** the episode (reported,
  never scored). *The issue's fix is public on GitHub; an agent that can fetch it is not being
  measured — and one that tries is reported.* The host route itself stays open (§0 item 3).
- **The agent's tests run INSIDE the instance image** (§3), never on the host: the host has no
  project dependencies, and the base block (§4) tells the agent the one way to run anything. The
  wrapper is exercised under the agent's EXACT environment before every episode (`rt` → python
  version from inside the container), so "the agent could not run tests" is a HARNESS_ERROR, never
  a result.

## 2 · Substrate, task subset, scoring, images — UNCHANGED from v5, by reference

- Dataset pin: `princeton-nlp/SWE-bench_Verified`, split `test`, revision
  `c104f840cc67f8b6eec6f759ebc8b2693d585d4a`, 500 rows, content digest
  `4f74c5cff0d5838cd8026295d7ed61ed8171147207ead7d795ff18c977712ae2` — **the recipe is in the
  repo** (`select_tasks.py --verify-dataset`; silicon's handoff defect, closed):
  `sha256(json.dumps(rows, sort_keys=True, separators=(",",":")).encode())`.
- **During episodes the Studio holds NO held-out byte:** `harness/data/problem_statements.json` is
  a projection of the pilot rows to `{instance_id, problem_statement, base_commit, repo, version}`
  (sha in `HASHES.txt`); `episode.sh` REFUSES to run while the full dataset is present. The full
  dataset and every gold-bearing harness log are on the Studio only for the control and scoring
  phases (`harness/studio_phase.sh in|out`, run from the seat), and are moved off before the first
  episode and after the last scoring run.
- **Task subset = the first `k` of the frozen `TASKLIST.json` `pilot` list, in draw order, k = 15.**
  Episodes run task-major, arm-minor: task 1 (a0, a1), task 2 (a1, a0), … so a stop leaves complete
  pairs and neither arm always runs second on a warm cache (8:7 first-run asymmetry at k = 15, reported).
  Extending k past 15 is an amendment; shrinking it is a REPORTED stop.
- `solved := official harness swebench==4.1.0 (726c546) reports resolved=true` for the SUBMITTED
  patch, run post hoc as a batch with `-d data/verified.json` (local file, content-pinned), `-i`
  the k ids, `--namespace swebench --instance_image_tag latest --max_workers 1 --timeout 1800`.
  Images by DIGEST from `IMAGE-DIGESTS.json` with the pre-registered BRIDGE (`docker pull --platform
  linux/amd64 <image>@<digest>` · `docker tag <image>@<digest> <image>:latest`) — 4.1.0 calls
  `images.get(key)` before any pull. The images are `linux/amd64` only (registry manifest, read
  without a daemon); they run under Rosetta on the arm64 Studio; 4.1.0 defaults `arch=x86_64` and
  creates containers with `platform=linux/x86_64` (source read at this hand).
- **Exclusions per `EXCLUSIONS.md`, arm-independent, both controls run before either arm on every
  task in the subset.** ⛔ *Amended 08/28 (refuter F4): swebench 4.1.0 DROPS an empty-patch
  prediction before evaluation, so the pre-flight submits a NO-OP patch (a new empty marker file
  outside every test path) and the harness grades the unmodified tree: all F2P fail, all P2P pass.*
  Gold-control unchanged. Rows are logged for all k, survivors included.
- **Predictions are built from manifests AFTER the batch** (`harness/predictions.py`), from
  scorable terminations only — `DONE`, `ROUNDS_EXHAUSTED`, `WALLCLOCK`, `TOKEN_CEILING`
  (`+NO_PATCH` variants as empty patches = unsolved). `VOID`, `QUOTA`, `ERROR_*`, `HARNESS_ERROR`
  rows are NEVER scored; they are listed as REMOVED with their reason and `n_effective` is the
  pair count. **No prediction is written while the night runs.**
- No held-out identity reaches the agent through the builder: the prompt is built from
  `problem_statement` ALONE by `harness/build_prompt.py`, whose self-test smuggles each of the five
  held-out fields into the statement and asserts a refusal.

## 3 · One environment for the agent's tests, the checks and the scorer

Per episode (`harness/episode.sh`): `docker create --platform linux/amd64 <image>@<digest>`;
`docker cp <ctr>:/testbed` to state; **assert the image's history is the post-fix shape BEFORE
dropping it** (`HEAD~1 == base_commit` and no commit dated after base other than the recipe's
synthetic HEAD; tag count recorded — refuter L3 turned the maintainers' build date into a
per-episode assertion); delete every `.git` and `packed-refs` at any depth; refuse a tree carrying
`CLAUDE.md`/`.claude`/`.mcp.json`; move it to `/Users/jyh/work/<ep>/repo`. Then **CHECK 2b on the
host copy** and, after the container is up, **CHECK 2b again inside it on `/testbed`** — all states
fail-closed, logged (`harness/check2b.sh`, 6-arm self-test):

```
no .git at ANY depth · no packed-refs · no file named .git containing "gitdir:" ·
git rev-parse --git-dir FAILS with GIT_DIR/GIT_COMMON_DIR unset ·
(host form) the image's RepoDigests carries the pinned digest
```

The episode container: `docker run -d --platform linux/amd64 --network none --name <ep>
-v /Users/jyh/work/<ep>/repo:/testbed -w /testbed <image>@<digest> tail -f /dev/null`. Inside the
container's mount namespace the bind mount hides the image's own `/testbed` (measured: no
`/testbed/.git`, no `/eval.sh`, no `/tmp/patch.diff`); the pristine image is still one `docker
run` away on the host, which is why `docker` is an ESCAPE token in the hook and the audit — the
agent has no reason to say the word: the wrapper says it. The agent reaches the environment
through ONE wrapper, `/Users/jyh/work/<ep>/rt`, which runs `<absolute docker> exec -w /testbed <ep>
bash -lc 'source /opt/miniconda3/bin/activate testbed && <cmd>'` and appends every command and
exit code to `rt.log`; per episode `rt_calls` and `rt_calls_rc0` are recorded and an episode whose
every `rt` call failed is `HARNESS_ERROR`, never a result.

Before ANY harness run (pre-flight, gold-control, scoring) `harness/bridge_assert.sh` asserts, per
id, that `<image>:latest` and `<image>@<digest>` are the SAME image object (`.Id` equal) — the
harness prefers a local `:latest` and never compares a digest (refuter v3/v4).
**Infrastructure failures get exactly ONE deterministic retry** (same image, task, arm; logged
`RETRY` by the driver) before the driver HALTS for an operator; a `HARNESS_ERROR` that survives
the retry is never an exclusion (EXCLUSIONS.md) and never scored (§2).

**The submitted patch is NEVER a terminal `git diff` of a repo the agent could touch.** A shadow
git-dir in state (outside the agent's tree; `GIT_DIR` set only in the harness process) commits the
pristine copy as `base` before the episode; after it, `add -A && diff --cached --binary base` is the
patch, sha256-recorded. The tree's own `.gitignore` is honoured. An agent that `git init`s its
working copy is recorded (`agent_made_git`), not penalised; both arms are told there is no history.

*Feasibility, measured 08/28:* extraction + both CHECK 2b + shadow git + wrapper assertion = 11 s;
427 django tests in 2 s through the bind mount under Rosetta. If a task's visible suite cannot
complete inside the wall-clock ceiling in either arm, that is an arm-independent covariate
(`rt.log` wall time, tool-timeout count per arm), reported.

## 4 · The two arms — the prompt is IDENTICAL up to the episode path; only the CLAUDE.md differs

**The prompt** (`-p`), built by `harness/build_prompt.py` from `problem_statement` only:

```
You are working in a checkout of the repository at /Users/jyh/work/<ep>/repo.
Resolve the issue below by changing the repository. When you are done, stop; your changes in the
working copy are your answer. Do not describe the change instead of making it.

<issue>
{problem_statement}
</issue>
```
The episode path differs per episode, so the prompt is pinned CANONICALLY: `HASHES.txt` carries
one `prompt-canonical <instance_id> <sha256>` line per pilot task (path → `__EP__`), `episode.sh`
asserts the episode's canonical sha against it, and the morning line asserts equality within pairs.

**The arm file** = `BASE` block + `ARM` block. `BASE` (`harness/base.md`, byte-identical in every
arm; the only place the agent learns HOW to run anything):

```
# Working notes
- Run any project command inside its environment with `<EP>/rt <command>`,
  e.g. `<EP>/rt python -m pytest path/to/test_file.py -x -q`.
  To use shell features (pipes, cd, &&), quote the whole command as one argument:
  `<EP>/rt 'cd tests && python -m pytest test_x.py -q | tail -30'`.
  Commands run without it use a bare host and will not find the project's dependencies.
- There is no network. Do not try to install packages or fetch anything.
- The checkout at `<EP>/repo` has no git history; do not use git. Edit files in place there.
  Do not create commits.
```

- **Arm ids are OPAQUE on the Studio: `a0` = PLAIN, `a1` = PLACEBO, `s0` = the smoke-probe canary.**
  The words "plain" and "placebo" appear in this repo, which is not on the Studio.
- **PLAIN (`a0`)**: `ARM` is EMPTY (`arms/a0.md`, 0 bytes). Rendered: 590 bytes.
- **PLACEBO (`a1`)**: `ARM` = `arms/a1.md`, **1,789 bytes**, eight numbered "house conventions"
  (read the whole issue · match style · small and local · preserve public behaviour · comments ·
  docs/changelog format · no new dependencies or commits · stop when resolved). ⛔ *Re-cut 08/28
  after refuters P1/F6: the draft placebo told the agent to reproduce, run the nearest tests, act
  on their failures, and confirm the expected behaviour — the next rung's active ingredient. The
  frozen placebo mandates NO tool call and contains none of: test, reproduce, verify, spec,
  property, checker, proof, statement, assert, expected* (asserted by `build_prompt.py --self-test`).
  **Its literal IS the intervention**; it is pinned as `rendered-a1(__EP__)` in `HASHES.txt` and
  `episode.sh` refuses an arm whose rendering is not the pinned one.
- **The placebo's PROFILE, registered now so a treatment amendment can be matched on more than one
  dimension** (refuter P5): bytes 1,789 · steps 8 · tool-mandating steps 0 · done-condition present
  (step 8) · statement/verification steps 0. **Every treatment amendment states its own profile,
  lists each dimension on which it differs, and its `ARM` block is within `[1,610, 1,968]` bytes
  (±10 %) — or it registers a profile-matched placebo variant beside it and runs that too.** The
  mechanical length term is also MEASURED, no tokenizer needed: per task, call 1's
  `cache_creation_input_tokens` in `a1` minus `a0` ≈ the placebo's token cost, reported.
- **Framing:** the agent is told nothing of arms, gates or evaluation; the notes present as a
  project's own. Named as an artifact in §0.

## 5 · Metering — from the session jsonl, deduplicated by `message.id`; audit from the same file

The session file is `$CLAUDE_CONFIG_DIR/projects/<cwd-slug>/<uuid>.jsonl`, copied verbatim into the
episode artifact. **One API call lands as one `assistant` line PER CONTENT BLOCK, each carrying the
same `message.id`, `requestId` and `usage`** (measured on this seat's own session: 45 lines = 22
calls). `harness/meter.py` (17-check self-test):

- **calls := distinct `message.id`** (fallback `requestId`; a line with neither is `no_call_id`
  and VOIDs — never a per-line fallback); `isApiErrorMessage` / model `<synthetic>` lines are
  excluded from calls and counted (`api_error_lines`);
- **the metered sum** = `input + cache_creation + cache_read + output` over those calls — the
  pre-registration's unit, unchanged; the four classes, `thinking_tokens`, per-call max, the
  `model` string per call (an OBSERVATION: `claude-sonnet-5` is requested; what lands is
  reported), `service_tier`, `speed`;
- **compaction lands NOWHERE**: a `compact_boundary` record carries `compactMetadata.preTokens/
  postTokens` and no usage. Their sum is reported as `compaction_input_floor`, and
  `metered_sum_incl_compaction_floor` beside the raw sum; the autocompact window is the CLI default
  (`auto`), recorded as such in every manifest, not pinned;
- **the CLI cross-check governs UPWARD**: `--output-format json` gives `num_turns` and `usage`;
  `num_turns_matches_calls` and the signed per-class `cli_minus_jsonl` are reported; when the CLI
  figure is larger it governs (`metered_sum_governing`) and `jsonl_undercount` is printed —
  the jsonl governs only downward. `total_cost_usd` is recorded and NOT used (dollars struck);
- **API-level retries** (429/5xx re-sends) never land in the jsonl and are not billed: the metered
  sum is what LANDED, which is what the quota consumed;
- **subagents**: `isSidechain` lines, any spawn tool_use (`Agent`/`Task`/`Workflow`/`Skill`, all
  disallowed), a second `.jsonl` or a `subagents/` directory under the config dir → `VOID(SUBAGENT)`;
  any extra transcript is metered separately so a VOID episode still has a complete number;
- a **truncated last line** is recorded (`truncated_last_line`), never silently skipped; an empty
  or unparsable `meter.json` makes the episode `HARNESS_ERROR(meter)`, never a quiet `NA`;
- the **ESCAPE / URL audit** of §1, with `escape_attempts_blocked`, `escape_unblocked`,
  `url_mentions`, `dotdot_paths`, and the `void_reasons` list.

**Termination**, typed per episode: `DONE` · `ROUNDS_EXHAUSTED` (`--max-turns 40` fired:
`subtype == error_max_turns`) · `WALLCLOCK` (the harness watchdog killed it at 5,400 s) ·
`TOKEN_CEILING` (killed at a metered sum ≥ **8,000,000** = R × the pre-registration's 200,000
per-call sub-cap, so **`--max-turns` is the stop expected to bind**; the draft's 3,000,000 would
have bound at ~30 calls on a 100k prefix and censored the p90 stage 0 exists to measure) ·
`QUOTA` (the CLI returned an error naming a rate/usage limit) · `ERROR_<subtype>` (any other CLI
error) · `HARNESS_ERROR` · `VOID(<reasons>:<term>)` · `+NO_PATCH` suffix when the tree is
unchanged. **The watchdog signals claude itself** (`exec`'d in its subshell, so `$!` is the agent);
after `wait` the harness asserts no process still holds the session id and logs `ORPHAN_KILLED`
if one did (refuter F5/M1: the draft killed the subshell and let the agent keep spending).
`--max-turns` is accepted by 2.1.251 and absent from `--help`; the CLI's own text reads *"Maximum
number of agentic turns (API round-trips)"*, so **R = 40 calls = 40 turns**, established by smoke
probe B (§7) before the first episode.

## 6 · What counts as an episode's artifact (`~/bench/state/<ep>/`, sha256-listed)

`manifest.json` (task · arm · digest · base · termination · exit code · session id · claude binary
and version · host arch · docker platform · agent PATH · flags verbatim · arm rendering sha and
block bytes · CLAUDE.md sha · prompt sha and canonical sha · settings and hook shas · patch sha and
bytes · `agent_made_git` · `rt_calls`/`rt_calls_rc0` · metered sums · calls · void reasons ·
compactions) · `session.jsonl` (verbatim) · `result.json` (the CLI's) · `model_patch.diff` ·
`image_history.txt` · `check2b.host.log` · `check2b.container.log` · `env_python.txt` (the
wrapper under the agent env) · `rt.log` · `network_audit.txt` · `meter.json` · `prompt.md` ·
`prompt_meta.json` · `eptree/` (the agent-visible tree, archived at landing: `CLAUDE.md`, `rt`,
`repo/`) · `configdir-projects/` (the config dir's `projects/` subtree, archived then REMOVED
after every episode, unconditionally, so nothing but credentials crosses episodes) · and, after
the batch, the harness `report.json` for the instance and the pre-flight/gold-control rows.
**A green exit says something RAN, not what:** an episode with no `model_patch.diff` is
`NO_PATCH`, scored unsolved, never "missing".

## 7 · Order of operations, the first model calls, and the reading rules

1. This freeze + `harness/` committed; `HASHES.txt` written; refuter pass on the draft
   (`a03bd3c`, 5 lenses: arm-blindness · metering · leaks · placebo-cheaper · harness-executes,
   each finding attacked by 2–3 skeptics) → REPAIR → a second pass on the repairs → this commit.
   **The harness, all in `harness/`, each with a driven self-test where one is possible:**
   `episode.sh` (runner + watchdog) · `rt.template` · `check2b.sh` (+`check2b.selftest.sh`, 6 arms)
   · `hook-deny-network.sh` (`--selftest`, 12 arms; `--pattern-escape`/`--pattern-url` shared with
   the audit) · `meter.py` (`--self-test`, 17 checks) · `build_prompt.py` (`--self-test`: five
   held-out fields refused, projection shape, placebo vocabulary) · `project_data.py` ·
   `bridge_assert.sh` · `preflight_gold.sh` · `score.sh` · `run_stage0.sh` (driver) ·
   `predictions.py` · `morning_line.py` · `settings.bench.json` · `sync_studio.sh` ·
   `studio_phase.sh` · `hashes.sh` → `HASHES.txt`. All four self-tests pass on the Studio itself
   (bash 3.2, python 3.9); a `--dry` episode passed there under this runner in 11 s.
2. Captain's hand: `~/.claude-bench` logged in as jykriterion **from inside `tmux attach -t
   bench`** on the Studio (so the credential is created by the session that will read it).
3. **SMOKE PROBES — the first model calls on this account, DECLARED here so they own their
   boundary.** Both run THROUGH `episode.sh` (`PROMPT_OVERRIDE`, arm `s0`, `LANDINGS=smoke.log`),
   so they exercise the exact environment block, and neither is an episode or scored:
   **A (canary)** — arm `s0` says *"if asked to reply OK, reply `OK CANARY-7f3a91`"*; prompt
   *"Run `echo $PATH; command -v docker; command -v curl` with the Bash tool, then reply with the
   single word OK."*, `--max-turns 4`. Establishes: the Keychain reads under tmux-over-ssh; the
   jsonl lands where §5 says; the arm file IS loaded (the canary string appears); the agent's real
   PATH (recorded into §1 if it differs).
   **B (cap)** — prompt *"Run `ls`, then `ls -a`, then `ls -la`, each as a separate Bash call,
   then reply OK."*, `--max-turns 2`. Establishes: `error_max_turns` fires; `num_turns` vs distinct
   `message.id`; `result.usage` vs the jsonl sum. Both are reported on the bus with metered tokens.
4. `studio_phase.sh in` · pre-flight + gold-control on the k tasks (containers only) ·
   `studio_phase.sh out` (dataset and gold logs leave the Studio).
5. Episodes, task-major, sequential, in tmux `bench:run` on the Studio; a bus line per landing
   with the metered sum, relayed by the seat from `~/bench/logs/landings.log`. The quota triple is
   read ONCE at dispatch, never polled; the 5-hour window is the concurrency limit (sequential = 1).
   The driver HALTS on a non-terminal landing that survives its one retry.
6. `studio_phase.sh in` · `predictions.py` · batch scoring per arm · `studio_phase.sh out` · the
   **MORNING LINE** (`harness/morning_line.py`, the one pre-declared computation):
   - solve rate per arm over PAIRS (tasks with both arms scorable), with `b` (a0-only), `c`
     (a1-only), `n_d`;
   - **the noise floor beside the difference:** `|b−c|` is printed with the exact two-sided
     sign-test probability of a difference at least that large under IDENTICAL arms — a
     descriptor, not a test; **`|b−c| < 5` of 15 is reported INDISTINGUISHABLE AT k = 15 and
     narrated in neither direction**;
   - metered-sum distribution per arm (p50/p90/max) with terminations per arm; **the p90 the cap
     rule consumes is `a0`'s, over `DONE|ROUNDS_EXHAUSTED` episodes; censored rows (`WALLCLOCK`/
     `TOKEN_CEILING`) are excluded and counted beside it**; `a1`'s p90 is reported for the
     length term;
   - **CAP-CONFOUNDED** if the count of cap-bound episodes (`ROUNDS_EXHAUSTED`+`WALLCLOCK`+
     `TOKEN_CEILING`) differs between arms by ≥ 2;
   - REMOVED rows (VOID/QUOTA/ERROR/HARNESS_ERROR) listed with reasons; `url_mentions` and blocked
     escape attempts per arm; pair order and wall-clock per episode;
   - **no p-value, by design.**

**Model sequence:** Sonnet for both controls and for every treatment arm first; Opus/Fable only on
an arm pair that differs, Fable episodes only on the Captain's word (item 12).

---

*Nothing below this line existed before this seat's first model call. Amendments are appended,
dated, with their reason — never edited into the text above. Treatment arms register here, each
with its PROFILE (§4).*

---
