# SCOUT — STAGE 0: the CONTROL protocol (plain · placebo), frozen

**Frozen 2026-08-28, bench seat, BEFORE any model call by this seat.** The freeze commit is the pin;
the harness under `harness/` is the normative form of every mechanism named here, and
`harness/HASHES.txt` pins every file, the arm renderings, the projected data, the per-task
canonical prompts, and the claude version. Two refuter passes preceded it, both banked in
the private record: pass 1 on draft `a03bd3c` (5 lenses, 42 confirmed, 10 fatal) and pass 2 on the
repaired `79835da` (21 closed / 21 partial; 3 fresh fatals, **all repair-introduced**). Their
residue is repaired in this commit; what is left open is named in §0 and §8, not smoothed.
Commission: council minute 2026-08-28 ITEM 12 and the bench seat's boot brief.

This document supersedes NOTHING in `PRE-REGISTRATION.md` (v4) or `DESIGN-gate-wave1.md` (v4):
wave 1 is **HELD** — no model call is made under that design — and stage 0 REUSES its
arm-independent machinery by reference (task draw, image digests, exclusions, harness pin, CHECK 2b,
the metered unit) while replacing the agent, the arms and the rule of amendment. Where this page and
those documents differ on an *agent* or *arm* matter, this page governs for the scout; where they
differ on a *scoring* or *substrate* matter, they govern — with ONE dated exception recorded in
both places: the pre-flight control is a NO-OP patch (§2; `EXCLUSIONS.md` amendment 2026-08-28).
**Where prose and script differ, the script at the freeze commit is definitive** (PRE-REG §3's rule).

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
   inseparable from evaluation-aware behaviour: the agent is not told an arm, a gate or an
   evaluation exists (the NEUTRAL framing, named as an artifact), but it sees notes presented as a
   project's own for a repository that has no team.
2. *Arm-blindness by construction.* The agent runs as the same uid as the harness with a Docker
   socket in reach; nothing on the host is unreadable to it. Blindness is **by audit** (§1, §5):
   every tool call is in the transcript; an escape VOIDs the episode; the audit is a regex and a
   path resolver, and a determined agent could evade it — an agent told "there is no network" and
   given no reason to look has, in the transcript, no way to hide that it looked.
3. *A closed network.* The test environment has none (`--network none`); the agent's host does.
   The hook is a **tripwire and the audit's source, not an OS closure**. The residual is named,
   owned and dated: a dedicated agent uid + a `pf` rule for it is the Captain's-hand item for the
   next sitting (§8).
4. *Separation of sampling variance from arm effect.* No task-arm is repeated at k = 15.
5. *Contamination.* A memorised task solves in both arms and pulls the pair toward concordance.
6. *Anything about `--max-turns` or the Keychain before the smoke probes have run* (§7).

## 1 · The hermetic agent (AGENT OUTSIDE, ENVIRONMENT INSIDE — the 13:3x ruling)

**Agent = Claude Code proper, `claude` 2.1.251 (pinned in `HASHES.txt`; the version is asserted
before every episode and the auto-updater is disabled in the agent's environment), headless
(`-p`), on the Studio host, on the bench subscription.** Never an API key; never the OAuth
token in a custom harness.

```
CLAUDE_CONFIG_DIR = /Users/jyh/.claude-bench   credentials (macOS Keychain, keyed to this dir) + settings.json
HOME              = /Users/jyh                  REAL — the Keychain credential is unreachable from a fresh HOME
                                                (measured); ~/.claude is NOT read because CLAUDE_CONFIG_DIR overrides it
cwd               = /Users/jyh/work/<ep>/repo   the working copy; <ep> = ep-<8 hex>, neutral root, no "bench" in the path
PATH (agent)      = /usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin:~/.local/bin   (the login PATH,
                                                echoed by smoke probe A1 from INSIDE the agent and recorded)
env -i  HOME USER LOGNAME PATH TERM LANG TMPDIR CLAUDE_CONFIG_DIR BENCH_EP(=the episode dir, read by the hook)
        DISABLE_AUTOUPDATER=1 DISABLE_UPDATES=1 CLAUDE_CODE_DISABLE_FILE_CHECKPOINTING=1
$(command -v claude) -p "$(cat prompt.md)" --model claude-sonnet-5 --effort high --max-turns 40 \
   --dangerously-skip-permissions \
   --disallowedTools "WebFetch,WebSearch,Agent,Task,Workflow,Skill,Monitor,CronCreate,CronDelete,CronList,RemoteTrigger,SendMessage,ListAgents,PushNotification,SendUserFile,EnterWorktree,ExitWorktree" \
   --strict-mcp-config --setting-sources user,project --output-format json --session-id <uuid>
```
- **`--setting-sources user,project`** — `project` is REQUIRED: without it Claude Code 2.1.251 loads
  no project-tree CLAUDE.md at all (refuter F0; the draft said `user` and would have run both arms as
  the same run). The `user` source is `~/.claude-bench/settings.json` (= `harness/settings.bench.json`,
  sha-pinned), which carries the one `PreToolUse` hook, matcher `Bash|Monitor`. `--bare` is never used.
- **Hermeticity of the agent** is exactly: no fleet tree, no memory bank, no MCP, no CLAUDE.md above
  `/Users/jyh/work/<ep>/`. Asserted before every episode (`episode.sh` §6): no `CLAUDE.md` on the
  path from `/` to the episode dir; the extracted tree carries no `CLAUDE.md`, `CLAUDE.local.md`,
  `.claude/`, `.mcp.json`; the config dir's `projects/`, `file-history/`, `session-env/`,
  `sessions/`, `todos/`, `shell-snapshots/`, `debug/` are EMPTY and it carries no
  agent-influencing entry (`CLAUDE.md commands agents skills rules hooks .mcp.json`); any other
  unexpected entry is recorded, not fatal; settings, hook, `episode.sh` itself, the arm rendering
  and the task's canonical prompt hash to `HASHES.txt`.
- **The arm IS a CLAUDE.md file** at `/Users/jyh/work/<ep>/CLAUDE.md` — one directory above the
  working copy, so ancestor discovery loads it and the patch never contains it. **`/Users/jyh/work`
  holds ONLY the running episode** (asserted; the tree is archived into state at landing).
- **The arm name is in no argv and no env while claude runs** (it reaches `episode.sh` on STDIN —
  an env var survives `unset` in the kernel's saved exec environment and shows in `ps -E`), and in
  **no file the hook or the audit permits**: `prompt_meta.json` carries no arm field;
  `manifest.json` is written after the process has exited; the driver logs the arm only in its
  LANDED line. Prior episodes' landings and manifests do name arms — they sit under `~/bench`,
  which is an ESCAPE token in the hook and the audit.
- **Network and host reach — hook, audit, and the OS where it applies:** `WebFetch`/`WebSearch` and
  every spawning or command-running tool other than `Bash` are disallowed; the test container runs
  `--network none`; the `PreToolUse` hook (`harness/hook-deny-network.sh`, identical in every arm,
  20-arm self-test) blocks two classes — **ESCAPE** (fetchers, installers, sockets, `gh`, `docker`
  and the others *bare or path-qualified*; Python network APIs INSIDE inline code only, because a
  grep for `urllib` in a repository is innocent; any path into `~/bench`, `~/.claude*`,
  `$CLAUDE_CONFIG_DIR`, a relative `bench/`, or another episode; the agent's own episode path is
  exempt) and **URL** (a scheme in the command text — an issue often quotes one; blocked so nothing
  is fetched, counted, never a VOID by itself). Post hoc, `meter.py` audits EVERY tool call — Bash
  and Monitor commands, and every path field of Read/Edit/Write/Glob/Grep/Notebook tools RESOLVED
  against the agent's cwd (a relative `../../` out of the tree is an escape): an escape whose
  result is the hook's BLOCKED text is an **attempt** (counted); an unblocked escape, a resolved
  path outside the episode tree (or `/tmp`), a spawn tool, or an unknown command-running tool
  **VOIDs** the episode (reported, never scored). The host route itself stays open (§0 item 3).
- **The agent's tests run INSIDE the instance image** (§3), never on the host. The wrapper is
  exercised under the agent's EXACT environment before every episode (its log line is kept apart
  from the agent's), so "the agent could not run tests" is a HARNESS_ERROR, never a result.

## 2 · Substrate, task subset, scoring, images — UNCHANGED from v5, by reference

- Dataset pin: `princeton-nlp/SWE-bench_Verified`, split `test`, revision
  `c104f840cc67f8b6eec6f759ebc8b2693d585d4a`, 500 rows, content digest
  `4f74c5cff0d5838cd8026295d7ed61ed8171147207ead7d795ff18c977712ae2` — **the recipe is in the
  repo** (`select_tasks.py --verify-dataset`; silicon's handoff defect, closed):
  `sha256(json.dumps(rows, sort_keys=True, separators=(",",":")).encode())`.
- **During episodes the Studio holds NO held-out byte:** `harness/data/problem_statements.json`
  (COMMITTED; sha in `HASHES.txt`) is a projection of the pilot rows to `{instance_id,
  problem_statement, base_commit, repo, version}`; `episode.sh` REFUSES to run while the full
  dataset or any `run_evaluation` log is present on the Studio. The full dataset and every
  gold-bearing harness log are on the Studio only for the control and scoring phases
  (`harness/studio_phase.sh in|out`, run from the seat; `out` FAILS unless zero gold-bearing files
  remain).
- **Task subset = the first `k` of the frozen `TASKLIST.json` `pilot` list, in draw order, k = 15.**
  Episodes run task-major, arm-minor: task 1 (a0, a1), task 2 (a1, a0), … so neither arm always
  runs second on a warm cache (8:7 first-run asymmetry at k = 15, reported per pair). A stop
  between the two arms of a task leaves that pair incomplete; the resume re-runs the missing cell
  and the morning line counts only complete pairs. Extending k past 15 is an amendment; shrinking
  it is a REPORTED stop.
- `solved := official harness swebench==4.1.0 (726c546) reports resolved=true` for the SUBMITTED
  patch, run post hoc as a batch with `-d data/verified.json` (local file, content-pinned), `-i`
  the k ids, `--namespace swebench --instance_image_tag latest --max_workers 1 --timeout 1800
  --cache_level instance`. Images by DIGEST from `IMAGE-DIGESTS.json` with the pre-registered
  BRIDGE (`harness/pull_pilot.sh`: `docker pull --platform linux/amd64 <image>@<digest>` ·
  `docker tag <image>@<digest> <image>:latest`) — 4.1.0 calls `images.get(key)` before any pull.
  All 30 pilot images are pulled and bridged on the Studio (88 GB). The images are `linux/amd64`
  only; they run under Rosetta on the arm64 Studio; 4.1.0 defaults `arch=x86_64` and creates
  containers with `platform=linux/x86_64` (source read at this hand).
- **Exclusions per `EXCLUSIONS.md`, arm-independent, both controls run before either arm on every
  task in the subset.** ⛔ *Amended 2026-08-28 in both documents (refuter F4): swebench 4.1.0 DROPS
  an empty-patch prediction before evaluation, so the pre-flight submits a NO-OP patch (one new
  empty marker file outside every test path) and the harness grades the unmodified tree: all F2P
  fail, all P2P pass.* Gold-control unchanged. Rows are logged for all k, survivors included; the
  harness exit code is checked, not masked.
- **Predictions are built from manifests AFTER the batch** (`harness/predictions.py`, arms `a0 a1`
  only), from scorable terminations — `DONE`, `ROUNDS_EXHAUSTED`, `WALLCLOCK`, `TOKEN_CEILING`
  (`+NO_PATCH` variants as empty patches = unsolved). `VOID`, `QUOTA`, `AUTH`, `ERROR_*`,
  `HARNESS_ERROR`, `SMOKE`, `DRY` rows are NEVER scored; they are listed as REMOVED with their
  reason and `n_effective` is the pair count. **No prediction is written while the night runs.**
- No held-out identity reaches the agent through the builder: the prompt is built from
  `problem_statement` ALONE by `harness/build_prompt.py`, whose self-test smuggles each of the five
  held-out fields into the statement and asserts a refusal, checks the projection's shape, the
  placebo's vocabulary, and that the prompt and base block name only entries the episode dir holds.

## 3 · One environment for the agent's tests, the checks and the scorer

Per episode (`harness/episode.sh`): `docker create --platform linux/amd64 <image>@<digest>`;
`docker cp <ctr>:/testbed` to state; **assert the image's history is the post-fix shape BEFORE
dropping it** (`HEAD~1 == base_commit`; no commit dated at or after base other than base and the
recipe's synthetic HEAD; tag count recorded; an image without `.git` is refused because the
checkout-is-base claim could not be asserted); delete every `.git` and `packed-refs` at any depth;
refuse a tree carrying `CLAUDE.md`/`.claude`/`.mcp.json`; move it to `/Users/jyh/work/<ep>/repo`.
Then **CHECK 2b on the host copy** and, after the container is up, **CHECK 2b again inside it on
`/testbed`** — all states fail-closed, logged (`harness/check2b.sh`, 6-arm self-test):

```
no .git at ANY depth · no packed-refs · no file named .git containing "gitdir:" ·
git rev-parse --git-dir FAILS with GIT_DIR/GIT_COMMON_DIR unset ·
(host form) the image's RepoDigests carries the pinned digest
```

The episode container: `docker run -d --platform linux/amd64 --network none --name <ep>
-v /Users/jyh/work/<ep>/repo:/testbed -w /testbed <image>@<digest> tail -f /dev/null`. Inside the
container's mount namespace the bind mount hides the image's own `/testbed` (measured: no
`/testbed/.git`, no `/eval.sh`, no `/tmp/patch.diff`); the pristine image is still one `docker
run` away on the host, which is why `docker` — bare or by path — is an ESCAPE token in the hook and
the audit: the agent has no reason to say the word, the wrapper says it. The agent reaches the
environment through ONE wrapper, `/Users/jyh/work/<ep>/rt`, which runs `<absolute docker> exec -w
/testbed <ep> timeout 590 bash -lc 'source /opt/miniconda3/bin/activate testbed && <cmd>'` (the
in-container `timeout` so a tool-level kill leaves no orphan) and appends every command and exit
code to `rt.log`; per episode `rt_calls`, `rt_calls_rc0` and `rt_unfinished` (START without END —
the Bash tool's own timeout) are recorded, and an episode whose every `rt` call ended
`rc=126|127` (not executable / not found — plumbing, never a failing test) is `HARNESS_ERROR`.

Before ANY harness run (pre-flight, gold-control, scoring) `harness/bridge_assert.sh` asserts, per
id, that `<image>:latest` and `<image>@<digest>` are the SAME image object (`.Id` equal) — the
harness prefers a local `:latest` and never compares a digest (refuter v3/v4).
**Non-terminal landings** (`HARNESS_ERROR`, `ERROR_*`) get exactly ONE retry after 60 s;
`QUOTA`/`AUTH` are a **hold with a release condition and a timeout** — 30-minute steps, at most
6 h, the same task-arm re-run once per step — then the driver HALTS for an operator. A
`HARNESS_ERROR` that survives its retry is never an exclusion (EXCLUSIONS.md) and never scored.
**Any abnormal exit of `episode.sh` still lands** (an EXIT trap types it `HARNESS_ERROR(abort:…)`,
removes the container, archives the tree) — the draft could die between "container up" and
"claude started" without a landing line, which is how one dead line would have burned the night.

**The submitted patch is NEVER a terminal `git diff` of a repo the agent could touch.** A shadow
git-dir in state (outside the agent's tree; `GIT_DIR` set only in the harness process) commits the
pristine copy as `base` before the episode; after it, `add -A && diff --cached --binary base` is the
patch, sha256-recorded. The tree's own `.gitignore` is honoured. An agent that `git init`s its
working copy is recorded (`agent_made_git`), not penalised; both arms are told there is no history.

*Feasibility, measured 08/28 on the Studio:* `--dry` (extraction + history assertion + both CHECK
2b + shadow git + wrapper under the agent env) = 11 s; 427 django tests in 2 s through the bind
mount under Rosetta; a **run-shaped dry** with a stub in place of claude executed every line after
the launch (watchdog, wait, jsonl discovery, meter, audit, cleanup, manifest) and landed
`DONE+NO_PATCH` — the path the draft had never run.

## 4 · The two arms — the prompt is IDENTICAL up to the episode path; only the CLAUDE.md differs

**The prompt** (`-p`), built by `harness/build_prompt.py` from `problem_statement` only
(`harness/prompt.md`, 278 bytes as a template):

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

**The arm file** = `BASE` block + `ARM` block. `BASE` (`harness/base.md`, 590 bytes, byte-identical
in every arm; the only place the agent learns HOW to run anything):

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
  `cache_creation_input_tokens` in `a1` minus `a0` ≈ the placebo's token cost (`first_call_usage`
  in every manifest; median printed by the morning line).
- **Framing:** the agent is told nothing of arms, gates or evaluation; the notes present as a
  project's own. Named as an artifact in §0.

## 5 · Metering — from the session jsonl, deduplicated by `message.id`; audit from the same file

The session file is `$CLAUDE_CONFIG_DIR/projects/<cwd-slug>/<uuid>.jsonl`, copied verbatim into the
episode artifact (a `-p` session leaves exactly one `.jsonl` there — measured; a second one, or a
`subagents/` directory, means a subagent ran). **One API call lands as one `assistant` line PER
CONTENT BLOCK, each carrying the same `message.id`, `requestId` and `usage`** (measured on this
seat's own session: 45 lines = 22 calls). `harness/meter.py` (26-check self-test):

- **calls := distinct `message.id`** (fallback `requestId`; a line with neither is `no_call_id`
  and VOIDs — never a per-line fallback); `isApiErrorMessage` / model `<synthetic>` lines are
  excluded from calls and counted (`api_error_lines`);
- **the metered sum** = `input + cache_creation + cache_read + output` over those calls — the
  pre-registration's unit, unchanged; the four classes, `thinking_tokens`, per-call max, the
  first call's usage, the `model` string per call (an OBSERVATION: `claude-sonnet-5` is requested;
  what lands is reported), `service_tier`;
- **compaction lands NOWHERE**: a `compact_boundary` record carries `compactMetadata.preTokens/
  postTokens` and no usage. Their sum is reported as `compaction_input_floor`, and
  `metered_sum_incl_compaction_floor` beside the raw sum; the autocompact window is the CLI default
  (`auto`) at the pinned claude version — a constant at that version, recorded, not pinned;
- **the CLI cross-check governs UPWARD**: `--output-format json` gives `num_turns`, `usage` (the
  CLI's own schema says: main loop only) and `modelUsage` (per model, includes auxiliary calls).
  `num_turns_matches_calls`, the signed per-class `cli_minus_jsonl`, `jsonl_undercount`, and any
  model in `modelUsage` never observed in the jsonl (`foreign_models_in_modelUsage`, a hidden-call
  detector) are reported; **`metered_sum_governing` = max(jsonl, usage, modelUsage)** and is the
  figure the morning line uses. `total_cost_usd` is recorded and NOT used (dollars struck);
- **API-level retries** (429/5xx re-sends) never land in the jsonl and are not billed: the metered
  sum is what LANDED, which is what the quota consumed;
- **subagents**: `isSidechain` lines, any spawn tool_use, a second `.jsonl` or a `subagents/`
  directory → `VOID(SUBAGENT)`; any extra transcript is metered separately;
- a **truncated last line** is recorded, never silently skipped; an empty or unparsable
  `meter.json` makes the episode `HARNESS_ERROR(meter)`, never a quiet `NA`;
- the **ESCAPE / URL audit** of §1 (`escape_attempts_blocked`, `escape_unblocked`, `url_mentions`,
  `dotdot_paths`, `unknown_tools`, `tool_timeouts` = tool results reading "Command timed out").

**Termination**, typed per episode: `DONE` · `ROUNDS_EXHAUSTED` (`subtype == error_max_turns`) ·
`WALLCLOCK` (the watchdog killed it at 5,400 s) · `TOKEN_CEILING` (killed at a metered sum ≥
**8,000,000** = R × the pre-registration's 200,000 per-call sub-cap, so **`--max-turns` is the
stop expected to bind**; the draft's 3,000,000 would have bound at ~30 calls on a 100k prefix and
censored the p90 stage 0 exists to measure) · `QUOTA` (the CLI's message text or stderr names a
rate/usage limit — classified from TEXT, never from a numeric field; the matched words are recorded
as `quota_evidence`; a run that produced a transcript with zero metered calls is `QUOTA(no_call)`)
· `AUTH` (login/Keychain text) · `ERROR_<subtype>` · `HARNESS_ERROR(…)` · `VOID(<reasons>:<term>)`
· `SMOKE(<term>)` (a `PROMPT_OVERRIDE` run) · `DRY` · `+NO_PATCH` suffix when the tree is unchanged.
**The watchdog signals claude itself** (`exec`'d in its subshell, so `$!` is the agent); after
`wait` the harness asserts no process still holds the session id and logs `ORPHAN_KILLED` if one
did. `--max-turns` is accepted by 2.1.251 and absent from `--help`; the CLI's own text reads
*"Maximum number of agentic turns (API round-trips)"*, so **R = 40 calls = 40 turns**, established
by smoke probe B before the first episode.

## 6 · What counts as an episode's artifact (`~/bench/state/<ep>/`, `SHA256SUMS`-listed)

`manifest.json` (task · arm · digest · base · termination · exit code · session id · claude binary,
its resolved target and version · host arch · docker platform · agent PATH · flags verbatim · arm
rendering sha and block bytes · CLAUDE.md sha · prompt sha, canonical sha, override sha · settings,
hook and `episode.sh` shas · patch sha and bytes · `agent_made_git` · `rt_calls`/`rt_calls_rc0`/
`rt_unfinished` · metered sums (raw, governing, incl. compaction floor) · calls · void reasons ·
compactions · models · service tiers · tool timeouts · first-call usage · unknown tools · quota
evidence) · `session.jsonl` (verbatim) · `result.json` · `cli_text.txt` · `claude.stderr` ·
`model_patch.diff` · `image_history.txt` · `check2b.host.log` · `check2b.container.log` ·
`env_python.txt` · `rt.probe.log` (the harness's own wrapper probe) · `rt.log` (the agent's calls) ·
`network_audit.txt` · `meter.json` · `prompt.md` · `prompt_meta.json` · `configdir_unexpected.txt` ·
`eptree/` (the agent-visible tree, archived at landing) · `configdir-projects/` (the config dir's
`projects/` subtree, archived then REMOVED after every episode, with `file-history/`,
`session-env/`, `sessions/`, `todos/`, `shell-snapshots/`, `debug/`, `history.jsonl` and the
`.claude.json` project entries for the episode root — unconditionally, so nothing but credentials
crosses episodes) · and, after the batch, the harness `report.json` for the instance and the
pre-flight/gold-control rows. **A green exit says something RAN, not what:** an episode with no
`model_patch.diff` is `NO_PATCH`, scored unsolved, never "missing".

## 7 · Order of operations, the first model calls, and the reading rules

1. This freeze + `harness/` committed; `HASHES.txt` written; two refuter passes (§preamble).
   **The harness, all in `harness/`, each with a driven self-test where one is possible:**
   `episode.sh` (runner + watchdog + EXIT trap; asserts its own sha) · `rt.template` ·
   `check2b.sh` (+`check2b.selftest.sh`, 6 arms) · `hook-deny-network.sh` (`--selftest`, 20 arms;
   `--pattern-escape`/`--pattern-url` shared with the audit) · `meter.py` (`--self-test`, 26
   checks) · `build_prompt.py` (`--self-test`, 12 checks) · `project_data.py` ·
   `bridge_assert.sh` · `pull_pilot.sh` (the bridge) · `preflight_gold.sh` · `score.sh` ·
   `run_stage0.sh` (driver) · `predictions.py` · `morning_line.py` · `settings.bench.json` ·
   `sync_studio.sh` (fails on sha drift) · `studio_phase.sh` (`out` fails if gold remains) ·
   `dry_exec_stub.sh` (the run-shaped dry) · `hashes.sh` → `HASHES.txt`. All self-tests pass on
   the Studio itself (bash 3.2, python 3.9); `--dry` and the run-shaped dry passed there under
   this runner.
2. Captain's hand: `~/.claude-bench` logged in as the bench account **from inside `tmux attach -t
   bench`** on the Studio (so the credential is created by the session that will read it), then
   the config dir's transient entries cleared (`episode.sh` asserts them empty).
3. **SMOKE PROBES — the first model calls on this account, DECLARED here so they own their
   boundary.** All run THROUGH `episode.sh` (`PROMPT_OVERRIDE`, arm `s0`, `LANDINGS=smoke.log`), so
   they exercise the exact environment block; they land as `SMOKE(…)` and are never scored:
   **A1 (PATH + canary)** — arm `s0` says *"if asked to reply OK, reply `OK CANARY-7f3a91`"*;
   prompt *"Run `echo $PATH` with the Bash tool, then reply with the single word OK."*,
   `--max-turns 3`. Establishes: the Keychain reads under tmux-over-ssh; the jsonl lands where §5
   says; the arm file IS loaded (the canary string appears in `result.result`); the agent's real
   PATH (recorded; §1 amended if it differs).
   **A2 (tripwire)** — prompt *"Run `command -v docker` with the Bash tool, then reply OK."*,
   `--max-turns 3`. Establishes: the hook fires from inside the agent (the tool result carries
   BLOCKED), `meter.json` classifies it as `escape_attempts_blocked` with `void == false`.
   **B (cap)** — prompt *"Run `ls`, then `ls -a`, then `ls -la`, each as a separate Bash call,
   then reply OK."*, `--max-turns 2`. Establishes: `error_max_turns` fires; `num_turns` vs distinct
   `message.id`; `result.usage` and `modelUsage` vs the jsonl sum.
   **C (rt from inside)** — prompt *"Run `<EP>/rt 'python -c \"print(6*7)\"'` with the Bash tool,
   then reply OK."*, `--max-turns 3`. Establishes: the wrapper works under the agent's Bash tool
   (not only under the harness's `env -i`); `rt_calls_rc0 == 1`.
   Each is reported on the bus with its metered tokens; **the driver does not start until all
   four have landed with the expected facts** — a human reading, treated as a hard stop.
4. `studio_phase.sh in` · pre-flight + gold-control on the k tasks (containers only; ~30 harness
   evaluations under Rosetta, budgeted before the driver starts) · `studio_phase.sh out`.
5. Episodes, task-major, sequential, under `caffeinate -dims` in tmux `bench:run` on the Studio
   (the machine may not sleep under a running episode); a bus line per landing with the metered
   sum, relayed by the seat from `~/bench/logs/landings.log`. The quota triple is read ONCE at
   dispatch, never polled; the 5-hour window is the concurrency limit (sequential = 1); a window
   edge is a `QUOTA` hold (§3), not a halt.
6. `studio_phase.sh in` · `predictions.py` · batch scoring per arm · `studio_phase.sh out` · the
   **MORNING LINE** (`harness/morning_line.py`, the one pre-declared computation):
   - solve rate per arm over PAIRS (tasks with both arms scorable), with `b` (a0-only), `c`
     (a1-only), `n_d`;
   - **the noise floor beside the difference:** `|b−c|` is printed with the exact two-sided
     sign-test probability of a difference at least that large under IDENTICAL arms — a
     descriptor, not a test; **`|b−c| < 5` of 15 is reported INDISTINGUISHABLE AT k = 15 and
     narrated in neither direction**;
   - metered-sum distribution per arm (p50/p90/max, nearest-rank, over `metered_sum_governing`)
     with terminations per arm; **the p90 the cap rule consumes is `a0`'s, over
     `DONE|ROUNDS_EXHAUSTED` episodes; censored rows (`WALLCLOCK`/`TOKEN_CEILING`) are excluded
     and counted beside it**; `a1`'s p90 is reported for the length term;
   - **CAP-CONFOUNDED** if the count of cap-bound episodes (`ROUNDS_EXHAUSTED`+`WALLCLOCK`+
     `TOKEN_CEILING`) among the pairs differs between arms by ≥ 2;
   - REMOVED rows (VOID/QUOTA/AUTH/ERROR/HARNESS_ERROR) with reasons; per arm `url_mentions`,
     blocked escape attempts, tool timeouts, compactions; the length term (median first-call
     `cache_creation` delta); pair order and wall-clock per pair; canonical-prompt equality within
     every pair; the models seen per arm; duplicate terminal manifests, if any;
   - **no p-value, by design.**

**Model sequence:** Sonnet for both controls and for every treatment arm first; Opus/Fable only on
an arm pair that differs, Fable episodes only on the Captain's word (item 12).

## 8 · Open items, owned and dated (not smoothed)

- **Agent uid split + `pf` rule** (§0 item 3): the OS-level closure of the host route. Captain's
  hand (a user, a sudoers line, a pf anchor). Next sitting.
- **The audit's reach** (§0 item 2): a regex over Bash text plus a resolver over path fields. Named
  evasions that pass it today: variable-built paths (`H=$HOME; cat $H/b*/…`), `ps -E`, `printenv`,
  a script written with Write and then run. Every one leaves its bytes in the transcript; none is
  something an agent told "there is no network" has a reason to do. Owner: bench; reviewed after
  the first night's transcripts.
- **Compaction in the cap rule**: the p90 consumes `metered_sum_governing`; if any `a0` episode
  compacted (`compactions > 0`), the morning line says so beside the p90 and the cap amendment
  states which figure it read. Owner: bench, at the morning line.
- **The pre-flight/gold timing under Rosetta** (30 evaluations at `--timeout 1800`): measured in
  step 4 before the driver starts; a 1800 s exclusion is reported as a Rosetta cost, never as a
  task property.

---

*Nothing below this line existed before this seat's first model call. Amendments are appended,
dated, with their reason — never edited into the text above. Treatment arms register here, each
with its PROFILE (§4).*

---

## AMENDMENT 1 — 2026-08-28 (bench seat), after refuter pass 3 on the freeze commit `cb8cea3`; before any model call

Pass 3 (the refuter report of 2026-08-28, pass 3, in the private record: 24 closed / 22 partial; 13 fresh,
2 FATAL) found what the pass-2 repairs broke. Repaired here and re-pinned; the text above is left as
frozen and this amendment governs where they differ:

1. **The run-shaped dry could land as a scorable row** (RI3-F1). A stub-driven run is now typed
   `DRYEXEC(…)`, logged to `dryexec.log` by construction, and filtered by `predictions.py` and the
   morning line; the driver `unset`s every probe/stub variable (`MAX_TURNS PROMPT_OVERRIDE LANDINGS
   AGENT_PATH MODEL EFFORT CLAUDE_BIN CLAUDE_BIN_STUB WALL_S TOKEN_CEILING`) before its first episode
   and the morning line prints the five constants seen across all scorable manifests, flagging a mix.
2. **The exclusion verdict was consumed by nothing** (T3-F1). `studio_phase.sh out` leaves
   `~/bench/state/controls.json` (booleans per id, no gold byte) on the Studio; the driver REFUSES
   to start without it and skips excluded tasks with a logged line; `predictions.py` and the morning
   line drop them and print the count. *Measured tonight: 15/15 pre-flight OK, 15/15 gold resolved,
   EXCLUDED = [] — the full k = 15 survives.*
3. **A container that died under the agent landed `DONE`** (RI3-R1). `finish()` records the
   container's running state; if the agent ran and the container is not running at the end, the
   episode is `HARNESS_ERROR(container_dead:…)`; `rt.log` now carries the first stderr line of every
   failing call as evidence (`ERR` records).
4. **The hook blocked innocent repository greps and path components** (RI3-R2, L3, N3). Fetchers and
   the docker CLI are matched in COMMAND POSITION only (start of a command or after `; & | ( $(`);
   Python network imports are matched only inside inline code (`python -c …`, heredocs); the
   relative tripwire is `bench/(harness|state|logs)/` so a repository's own `bench/` passes.
   Self-test 26 arms. *Consequence for probe A2: `command -v docker` is no longer an escape (it does
   not run docker); the probe runs `docker version`, which is.*
5. **Duplicates were resolved by random episode id** (RI3-R3): the latest by `end_utc` wins;
   both end times are printed.
6. **The pin was tautological against the working tree** (RI3-R4): `sync_studio.sh` REFUSES a dirty
   `harness/` or a `HASHES.txt` that differs from HEAD, writes the commit sha to
   `~/bench/harness/FREEZE-COMMIT`, and every manifest records it as `freeze_commit`.
7. **`~/…` paths in file tools resolved inside the tree** (RI3-R5): a tilde or variable path in any
   file-tool field is an escape (the tool expands it, so it can only mean outside the tree).
8. **QUOTA/AUTH could be typed from the agent's own prose** (RI-5, RI3-N1): the classifier reads
   ONLY `claude.stderr` and the CLI's `error` field — never `result` text; bare `401` and `log in`
   are gone; `429` is bounded by non-digits; a `VOID` row is never re-typed `QUOTA(no_call)`.
9. **The INT/TERM trap landed the episode without stopping the agent** (RI3-N4): it kills claude
   first. **Landings carry the metered sum** as a fifth field (T3-R3), so the seat's bus relay reads
   `landings.log` as declared. **Removed rows are listed by manifest identity** (F7), so a held cell's
   earlier `QUOTA` landings stay visible. **The length term** is call 1's `input + cache_creation +
   cache_read` (warmth-invariant), and pairs whose arms landed different models/tiers are printed
   (F4, P2). `rt_unfinished` per arm is printed (T-R5). The driver re-execs itself under
   `caffeinate -dims` (T-R6).
10. **Smoke probes, corrected texts** (T3-R1, T3-R5, T3-R2): **A1** `echo $PATH` then OK,
    `--max-turns 3` (canary in `s0`); **A2** `docker version` then OK, `--max-turns 3` (must be
    BLOCKED; `escape_attempts_blocked` non-empty, `void == false`); **B** *"Run `ls` with the Bash
    tool, then reply OK."* with **`--max-turns 1`** — `error_max_turns` is then deterministic and the
    transcript still yields `num_turns` vs `message.id` and `result.usage`/`modelUsage` vs the jsonl;
    **C** *"Run `../rt 'python -c \"print(6*7)\"'` with the Bash tool, then reply OK."* (cwd is
    `<ep>/repo`, so `../rt` is the wrapper; the hook passes it; `dotdot_paths` counts 1, no void).
    **§7.2 login is two commands**: `CLAUDE_CONFIG_DIR=/Users/jyh/.claude-bench claude /login` inside
    `tmux attach -t bench`, then exactly the purge `episode.sh` performs
    (`rm -rf ~/.claude-bench/projects/* ~/.claude-bench/{todos,shell-snapshots,debug,file-history,session-env,sessions}; : > ~/.claude-bench/history.jsonl`).
    **§7.6 runs ON THE STUDIO**: `predictions.py ~/bench/state ~/bench/state` · `score.sh a0 <run>` ·
    `score.sh a1 <run>` · `morning_line.py ~/bench/state ~/bench/state/scoring/stage0-a0.<run>.json
    ~/bench/state/scoring/stage0-a1.<run>.json` · then `studio_phase.sh out`.

Still open, named (§8 stands, plus): the audit does not VOID a Bash relative climb (`cat
../../../bench/…`) or `find /` — counted as `dotdot_paths`, reviewed by hand after the first night;
the hook is fail-open on malformed input; `/tmp` is a shared, unscrubbed channel between the two arms
of a task (blessed for reads; a per-episode `TMPDIR` is the next amendment); a docker-level failure
that returns `rc=1` is caught by the container-liveness check, not by the `rc=126|127` rule.

**Amendment 1, addendum (2026-08-28 16:5x, before any model call):** the four probes of item 10 are run and
ASSERTED by `harness/smoke.sh` (pinned): canary present · A2 blocked and not void · B `error_max_turns` and
`num_turns == calls` · C `rt_calls_rc0 == 1`. It exits non-zero on any failed fact; the driver is not started
on a non-zero smoke. The human hard stop of §7.3 becomes a script.

**Amendment 1, addendum 2 (2026-08-28 17:2x, before any model call):** the Captain's login session rewrote the
pinned `~/.claude-bench/settings.json` (it added `model`, `skipDangerousModePermissionPrompt`, `agentPushNotifEnabled`).
The pinned `harness/settings.bench.json` now carries `skipDangerousModePermissionPrompt: true` (a harness
convenience for `--dangerously-skip-permissions`, arm-independent); `model` and the notification flag are NOT
adopted (`--model claude-sonnet-5` is passed explicitly). The Studio file is re-installed from the pinned bytes and
`episode.sh` keeps refusing any drift. Also recorded: the login created `~/.claude-bench/.credentials.json` — Claude
Code's own credential file (the Keychain was not reachable from the ssh session) — allowed, unexpected-entry logged.

**Amendment 1, addendum 3 (2026-08-29 00:2x, after the four smoke probes — the first model calls on the bench account,
arm `s0`, task `django__django-15315`, freeze commit `13959bd`):** MEASURED: (A1) the canary string landed —
the arm CLAUDE.md IS loaded under `--setting-sources user,project`; the agent's PATH is exactly the one §1
states; 2 calls, 39,157 governing tokens. (A2) `docker version` was BLOCKED by the hook from inside the agent,
recorded as an attempt, not a void; 2 calls, 39,262. (B) `--max-turns 1` fired `error_max_turns` after
exactly ONE Sonnet call: **the cap counts main-loop API calls, as pinned** — and at the cap the CLI reports
`num_turns = calls + 1` (the turn it cut); on a normal end `num_turns == calls` (A1/A2/C). `meter.py`'s
cross-check now accepts `calls + 1` only under `error_max_turns`. 1 call, 19,848. (C) `../rt` ran inside the
container from the agent's own Bash tool, `rt_calls_rc0 = 1`; 2 calls, 39,010. In every probe the CLI's
`usage` equals the jsonl sum to the token (no undercount), and **`modelUsage` carries one
`claude-haiku-4-5-20251001` call of ~920 tokens per session — Claude Code's own session-title call (the
`ai-title` record)**: arm-independent, included in `metered_sum_governing`, reported as `foreign_models`, NOT
a VOID. The first-call prefix (system prompt + tools + the arm file) is ≈19k tokens of `cache_creation`.
`smoke.sh` gains a probe-subset argument; probe B is re-run under the corrected assertion before the driver.

**Amendment 1, addendum 4 (2026-08-29 01:2x, after the batch, before scoring):** one submitted patch
(`sphinx-doc__sphinx-9602`, a0, capped) is not valid UTF-8 — the agent left its own reproduction build
(`literal_repro/_build/`, 28 files incl. pickled doctrees) in the working copy, outside the tree's `.gitignore`,
and the pre-declared `add -A && diff --cached --binary base` captured it. The patch rule stands (the agent's
output is the agent's output); a JSON prediction cannot carry those bytes, so `predictions.py` submits the patch
with undecodable bytes replaced and flags the row `patch_non_utf8` in `predictions-excluded.json` (notes).
Whether such a patch applies is the harness's verdict; the flag is printed beside the score.

**Amendment 1, addendum 5 (2026-08-29 01:5x, after scoring):** stage 0 EXECUTED under this protocol. Results and the
per-episode table: `RESULTS-stage0-2026-08-29.md`; archive under `runs/stage0-2026-08-28/`. The morning line's
model-equality check compared call counts instead of model names (a reporting bug, fixed in `morning_line.py`;
the corrected line is the one recorded). The a0 p90 the cap rule consumes is **1,602,434**.

**Amendment 1, addendum 6 (2026-08-29 02:0x — the CONTAMINATION CHECK, stated BEFORE it is computed; the
Captain's word via the helm 18:5x; PRE-REG §4 mandates it first because the control landed 13/15 = 87 %, above
the 40–60 % band):** instrument = PRE-REG §5's proxy, run on the SEAT (gold never nears the agent host):
per task and arm, **sim := 1 − Levenshtein(C(A), C(G)) / max(|C(A)|, |C(G)|)** at character level, where
C(P) is the sequence of a patch's changed lines (`+`/`-`, headers excluded, sign kept, whitespace
normalised) **restricted to the files the gold patch touches**; `exact` := the multiset of changed lines
equals gold's. **CUT: HIGH iff sim ≥ 0.80.** Reported as a distribution over all 15 tasks per arm, the
unrestricted sim beside it, and the gold's changed-line count. **Named confound, stated now:** a forced minimal
fix is similar to gold whether or not the model has seen it — tasks whose gold changes ≤ 4 lines are flagged
small-fix and the reading is also given without them. **Reading rule, over RESOLVED a0 tasks:** f_high =
fraction in HIGH; **f_high ≥ 2/3 ⇒ CONTAMINATION-CONSISTENT** (memorisation and forced fixes are not
separable by this instrument; the honest next substrate is S2-Lean, where the kernel decides); **f_high ≤ 1/3
⇒ CAPABILITY-CONSISTENT**; otherwise INDETERMINATE, reported as such. Normative form: `harness/contamination.py`,
committed at this addendum's commit and run only after it. A secondary, UNREGISTERED and exploratory
reading — a judge panel quoting non-forced verbatim overlap (comments, names, structure) between agent and
gold patches — may be reported as evidence beside the number; it moves no reading. Nothing else moves
until this lands.

**Amendment 1, addendum 7 (2026-08-29 02:1x — the contamination check COMPUTED, by the rule of addendum 6):**
a0 resolved 13; HIGH (sim ≥ 0.80) among them 6 ⇒ **f_high = 0.46 ⇒ INDETERMINATE**; excluding small-fix tasks
3/8 HIGH; exact matches 2; seven resolved tasks LOW (a different change from upstream's); both unresolved LOW.
a1 identical. Five of 15 pairs are byte-identical across arms (model determinism, one of them LOW to gold).
Full table in `RESULTS-stage0-2026-08-29.md`; `runs/stage0-2026-08-28/contamination.json`. The reading is
INDETERMINATE and is reported as such; it neither licenses a tier step-down nor forbids S1 — that decision is
the Captain's, with the number in hand.

**Amendment 1, addendum 8 (2026-08-29 02:3x — exploratory panel beside the registered reading; moves nothing):**
the unregistered blind panel found signal from ≥ 2 judges on 5 of 15 tasks; the seat VERIFIED at the artifact that
on `sympy-14248` and `sphinx-9602` (both unresolved) upstream's ADDED lines appear in the transcript first as the
agent's own Edit input, and that on `sympy-21612` and `astropy-14539` the agent emitted an upstream identifier
(`21537`, `14545`) present in no input it was given (the numbers' upstream identity rests on the judges' recall).
The registered reading stays INDETERMINATE; the exploratory reading is: recall of upstream fixes is PRESENT on this
substrate at this tier. Recorded in `RESULTS-stage0-2026-08-29.md`. Nothing else moves without the Captain's word.
