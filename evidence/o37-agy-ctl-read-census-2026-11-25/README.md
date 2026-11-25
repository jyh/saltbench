# O37: what the agy subjects NAMED outside their repo, over the 705 cells of record (2026-11-25)

**What this measures.** For each of the 705 agy cells of record, it counts the subject's tool calls that name a path
outside the cell's `repo/` in one of two places: the cell's own harness directory `ctl/`, or another place under the run
box's home directory. It is a measurement only. No verdict, table or comparison of record changes here. What a CTL-NAMED
or OTHER-RECORD cell does to a result of record is a separate ruling.

**Why it was owed.** NCA cell `naaefs01` read its own `ctl/` (bus 2026-11-24, lead's ruling (A): the cell keeps its
verdict, is flagged CTL-READ and leaves every comparison). That ruling left the 705 earlier cells reading "ctl reads
UNMEASURED". This is that census.

## The tables (printed by `python3 -I tables.py` from `census.tsv` and `hits.tsv`; `--check` fails if this file does not carry them verbatim)

```
  block   arm         cells  CTL-NAMED  OTHER-RECORD  HOME-ENV  NONE-NAMED  UNMEASURED
  MATRIX  plain         135         50             5         2          81           0
  MATRIX  salt-diet     137         53            38        11          54           0
  MATRIX  both          272        103            43        13         135           0
  NA      plain          36          0             0         1          35           0
  NA      salt-diet      37          0             1         1          35           0
  NA      both           73          0             1         2          70           0
  ZF      plain         132          0             0         8         124           0
  ZF      salt          132          0             1         3         128           0
  ZF      both          264          0             1        11         252           0
  WA      plain           6          0             0         1           5           0
  WA      salt-diet       6          0             0         0           6           0
  WA      both           12          0             0         1          11           0
  WA-pro  plain           6          0             0         0           6           0
  WA-pro  salt-diet       6          0             0         0           6           0
  WA-pro  both           12          0             0         0          12           0
  TA      plain          36          0             0         2          34           0
  TA      salt-diet      36          0             0         1          35           0
  TA      both           72          0             0         3          69           0
  all     both          705        103            45        30         549           0
  (a cell can carry CTL-NAMED and OTHER-RECORD both; HOME-ENV is counted only where OTHER-RECORD is absent)
  tool calls listed in hits.tsv: 2473 (CTL 628 · OTHER-RECORD 119 · HOME-ENV 75 · PARENT 1710)
```

**Read with the tables:**
- **CTL-NAMED is all MATRIX (levels 3-8) and has no arm skew** (plain 50 · salt-diet 53). The files named most often
  are the harness's own turn records: `launch.log`, `briefing-claim`, `work-turn-*.ndjson`, `agy-turn1-*.ndjson`,
  `stream-*.ndjson`. Every call is listed in `hits.tsv`.
- **OTHER-RECORD has an arm skew in MATRIX** (salt-diet 38 of 137 · plain 5 of 135). Most targets are the cell's own
  FAMILY root (the directory that holds its sibling replicas), reached by a search or a list from there. A few go
  further: `l8rfss03` (salt-diet) ran `find ~ -name "transcript*.jsonl"` and then read the brain transcript of
  `l8rfpw01`, a plain-arm tripwire cell kept under an `EVIDENCE-…` directory; `l7nffs03` searched a level-6 plain
  family; `l5fs02` listed tests in a `PRESERVED-waves-…` tree; some searched or read a project checkout on the run box (the harness export).
  A channel that touches one arm more than the other is not neutral between the arms. This one carries an input from
  outside the arm, and its sign is unknown.
- **HOME-ENV includes WRITES to a box-wide file.** Some subjects wrote `~/.gitconfig` (for example NA `nalvfp02`, ZF
  `zffzgxp301`, TA `taafs101`). That file is shared by every later cell on the box, so it is a channel between cells.
  It is a write, not a read, and this census does not trace who read it after.
- **No tool call names a withheld suite.** Over `hits.tsv`, the only call matching `/B/`, `withheld`, `hidden`,
  `fault-gate`, `referee`, `score_wave` or `tests-hidden` is `l6vsfq03` grepping its own `ctl/` for "referee".
  This covers what a call NAMES, and that limit binds it (below).

## Method

`ctl_census.py` runs on the run box. It is read-only and spends nothing. Its population is the web census's `join.tsv`
(`../o37-agy-web-served-2026-11-20/join.tsv`: 705 rows, derived there from tracked files, never typed). Each cell
is `$HOME/<root>/<id>` for every family named in the root column. A record held in several families is read in all of
them, and a path inside ANY of its families is inside the cell. For every brain transcript
(`.agyhome/…/brain/*/.system_generated/logs/transcript_full.jsonl`), each entry of a record's `tool_calls` is one call.
A call is classified by its **path-role arguments** (keys matching path|file|dir|uri|url|target|cwd) and its
**command line**. Written content is never read as a path.

| state | meaning |
|---|---|
| CTL-NAMED | at least one call names a path component `ctl` (`<cell>/ctl/x`, `../ctl`, `ctl/x`, `ls ctl`) |
| OTHER-RECORD | at least one call names a path under `$HOME` outside every family of the cell whose top directory is not a dot-directory: another cell or family root, a preserved or evidence tree, a project checkout |
| HOME-ENV | the only outside paths are `$HOME` itself or dot-files and dot-directories (`ls ~`, `~/.gitconfig`) |
| NONE-NAMED | at least one transcript was read and no call names any of the above |
| UNMEASURED | no transcript or no directory, never printed as 0 (none here) |

These are excepted as toolchain inputs a build reads: `~/.cargo .rustup .elan .cache .local .npm .gradle .m2 .opam
.verus .vargo`, `~/verus-pin` and `~/bench-src/cargo-root*`. A call that is only a PARENT reach (`..`, or the cell
directory itself) is listed in `hits.tsv` and never sets a state.

**Run:** `python3 -I ctl_census.py --join join.tsv --home $HOME --out census.tsv --hits hits.tsv` on the run box,
2026-11-25. ctl_census.py sha256/16 `04036d3d3ff003dc`; join.tsv `224211fc66f8fc60`; census.tsv `1712aa3764172f1f`;
hits.tsv `a3cb06cfa6ad57a4`. In `hits.tsv`, `$HOME` is written as `~`, and a path into a checkout under `~/projects` is written as the role `~/<a project checkout>` (those are private records on the run box). Each argument is shown up to its first newline, followed by ` …` where it was cut.

## Controls (each is red first)

- **Selftest** `python3 -I ctl_census.py --selftest`: 24/24. It runs planted fixtures, one per shape above,
  including a write whose content says `../ctl` (not counted), `grep ioctl` (not counted), `find ~` (HOME-ENV),
  another cell's brain file (OTHER-RECORD), `~/verus-pin` (not counted), and a copied record that names its other family
  (not counted).
- **Mutants**, each RED on exactly its arms: gemini's original needle (`\.\./ctl|/ctl/|ctl/(launch|…)`) 9/11 on the
  first suite, missing `cd .. && cat ctl/…` and `ls ctl`; an absent transcript counted as 0 (10/11); the root column
  read as one path (11/12, the defect that first read 10 cells UNMEASURED); OUTSIDE disabled (15/19); no toolchain
  exception (18/19); OTHER-RECORD never set (18/21); a copied record judged against one family (23/24); no cargo-root
  exception (23/24).
- **Positive control at the object:** NCA `naaefs01` (outside the 705, known to have read `ctl/`) reads CTL-NAMED with
  8 calls, the 8 in gemini's list. Its `write_file` of LANDING.md, which mentions ctl, is not counted.
  `ncalbas01` (T-NCA-A) reads NONE-NAMED, as gemini's census does.
- **Second axis (raw bytes):** among the NONE-NAMED cells of an earlier run, 23 transcripts carry the byte string
  `/ctl` or `ctl/`. Read one by one, all 28 matches are outside `tool_calls`: 24 tool RESULTS (GENERIC records), 2
  model texts and 2 system messages. So the call needle missed no call there. Those results are the limit below.

## Limits (they bind every row above)

1. **A count of what was NAMED, not of what was SEEN.** A recursive search or listing from a parent reaches `ctl/` or a
   sibling cell without naming it. The second axis found tool results carrying `ctl/` LINE CONTENT that way
   (`s3cp02`, `s3ps03`, `s3ft02`: `grep_search` results from `ctl/stream-1.ndjson`), and listings carrying `ctl/`
   names, in cells this census reads NONE-NAMED. So NONE-NAMED is a lower bound on contact. It is not "never touched".
   PARENT calls (1710) are listed as candidates.
2. **`$HOME` only.** Paths outside the home directory (`/tmp`, `/Users/Shared`, volumes) are not classified.
3. **No ruling.** Whether a CTL-NAMED or OTHER-RECORD cell leaves a comparison, as naaefs01 and the WEB-SERVED cells
   do, changes what published tables assert. It is ruled separately and is not applied here.
