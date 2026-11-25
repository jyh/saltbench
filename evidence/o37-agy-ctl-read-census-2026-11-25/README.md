# O37: what the agy subjects NAMED outside their repo, over the 705 cells of record (2026-11-25)

**What this measures.** For each of the 705 agy cells of record, it counts the subject's tool calls that name a path
outside the cell's `repo/` in one of two places: the cell's own harness directory `ctl/`, or another place under the run
box's home directory. It is a measurement only. No verdict, table or comparison of record changes here.

**What was already measured and ruled.** Reads of `ctl/` in the 272 MATRIX cells were censused on 2026-10-13
(`AMENDMENT-agy-ctl-fence-2026-10-13.md` §4, `evidence/agy-ctl-census-2026-10-13/`: 107 subjects READ ctl/, 0 wrote
it). That amendment's §5 ruled: "Reads of ctl/ stay open … No cell is re-run and no figure moves." This census reproduces
that 107 by a second method (below). **What is new here is the OTHER-RECORD class and the four later blocks.**

**Why it was run.** NCA cell `naaefs01` read its own `ctl/` (bus 2026-11-24, the lead's ruling (A)). That ruling
said the 705 earlier cells read "ctl reads UNMEASURED". For MATRIX that sentence was stale: the 10-13 census above had
measured it.

## The tables (printed by `python3 -I tables.py` from `census.tsv` and `hits.tsv`; `--check` fails if this file does not carry them verbatim)

```
  block   arm         cells  CTL-NAMED  OTHER-RECORD  HOME-ENV  NONE-NAMED  UNMEASURED
  MATRIX  plain         135         51             8         4          75           0
  MATRIX  salt-diet     137         56            43        14          49           0
  MATRIX  both          272        107            51        18         124           0
  NA      plain          36          0             0         1          35           0
  NA      salt-diet      37          0             1         1          35           0
  NA      both           73          0             1         2          70           0
  ZF      plain         132          0             0         8         124           0
  ZF      salt          132          0             1         4         127           0
  ZF      both          264          0             1        12         251           0
  WA      plain           6          0             0         1           5           0
  WA      salt-diet       6          0             0         0           6           0
  WA      both           12          0             0         1          11           0
  WA-pro  plain           6          0             0         0           6           0
  WA-pro  salt-diet       6          0             0         0           6           0
  WA-pro  both           12          0             0         0          12           0
  TA      plain          36          0             0         2          34           0
  TA      salt-diet      36          0             0         1          35           0
  TA      both           72          0             0         3          69           0
  all     both          705        107            53        36         537           0
  (a cell can carry CTL-NAMED and OTHER-RECORD both; HOME-ENV is counted only where OTHER-RECORD is absent)
  tool calls listed in hits.tsv: 2970 (CTL 738 · OTHER-RECORD 134 · HOME-ENV 88 · PARENT 2103)
```

**Read with the tables:**
- **CTL-NAMED is all MATRIX (levels 3-8), with no arm skew** (plain 51 · salt-diet 56). The 10-13 census and its
  ruling (§5 above) already cover it. The files named most often are the harness's own turn records (`launch.log`,
  `briefing-claim`, `work-turn-*.ndjson`, `agy-turn1-*.ndjson`).
- **OTHER-RECORD is new, and it has an arm skew in MATRIX** (salt-diet 43 of 137 · plain 8 of 135). Most targets are
  the cell's own FAMILY root (the directory that holds its sibling replicas), reached by a search or a list from there.
  A few go further: `l8rfss03` (salt-diet) ran `find ~ -name "transcript*.jsonl"` and then read the brain transcript of
  `l8rfpw01`, a plain-arm tripwire cell kept under an `EVIDENCE-…` directory; `l7nffs03` searched a level-6 plain
  family; `l5fs02` listed tests in a `PRESERVED-waves-…` tree; some searched or read a project checkout on the run box
  (the harness export). No call names a phase-2 aside (`_aside`). A channel that touches one arm more than the other
  is not neutral between the arms. This one carries an input from outside the arm, and its sign is unknown.
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
them, and a path inside ANY of its families is inside the cell. It reads every `transcript_full.jsonl` under the cell
**and under `<family>/_aside/<id>/`**, where a two-phase cell's phase-1 conversation is moved. Each entry of a
record's `tool_calls` is one call. A call is classified by its **path-role arguments** (keys matching
path|file|dir|uri|url|target|cwd) and its **command line**. Written content is never read as a path.

| state | meaning |
|---|---|
| CTL-NAMED | at least one call names a path component `ctl` (`<cell>/ctl/x`, `../ctl`, `ctl/x`, `ls ctl`) |
| OTHER-RECORD | at least one call names a path under `$HOME` outside every family of the cell whose top directory is not a dot-directory: another cell or family root, a preserved or evidence tree, a project checkout |
| HOME-ENV | the only outside paths are `$HOME` itself or dot-files and dot-directories (`ls ~`, `~/.gitconfig`) |
| NONE-NAMED | at least one transcript was read and no call names any of the above |
| UNMEASURED | no transcript or no directory, never printed as 0 (none here) |

These are excepted as toolchain inputs a build reads: `~/.cargo .rustup .elan .cache .local .npm .gradle .m2 .opam
.verus .vargo`, `~/verus-pin` and `~/bench-src/cargo-root*`. A call that is only a PARENT reach (`..`, or the cell
directory itself) is listed in `hits.tsv` and never sets a state. In `hits.tsv`, `$HOME` is written as `~`. A path
into a checkout under `~/projects` is written as the role `~/<a project checkout>`, because those are private records
on the run box. Each argument is shown up to its first newline, followed by ` …` where it was cut.

**Run:** `python3 -I ctl_census.py --join join.tsv --home $HOME --out census.tsv --hits hits.tsv` on the run box,
2026-11-25. ctl_census.py sha256/16 `6b239291b601970a`; join.tsv `224211fc66f8fc60`; census.tsv `8eaa73c04f793192`;
hits.tsv `bc09f4f4d42b4538`.

## Controls (each is red first)

- **Selftest** `python3 -I ctl_census.py --selftest`: 25/25. It runs planted fixtures, one per shape above,
  including a write whose content says `../ctl` (not counted), `grep ioctl` (not counted), `find ~` (HOME-ENV),
  another cell's brain file (OTHER-RECORD), `~/verus-pin` (not counted), a copied record that names its other family
  (not counted), and a phase-1 transcript under `_aside/` (read).
- **Mutants**, each RED on exactly its arms: gemini's original needle (`\.\./ctl|/ctl/|ctl/(launch|…)`) 9/11 on the
  first suite, missing `cd .. && cat ctl/…` and `ls ctl`; an absent transcript counted as 0 (10/11); the root column
  read as one path (11/12); OUTSIDE disabled (15/19); no toolchain exception (18/19); OTHER-RECORD never set (18/21);
  a copied record judged against one family (23/24); no cargo-root exception (23/24); the one-depth brain glob in place
  of the walk (24/25).
- **Second method, agreeing:** CTL-NAMED in MATRIX is 107, and the 10-13 census, with a different needle (the whole
  serialized call) plus stream tool records, read 107 over the same 272 cells.
- **Positive control at the object:** NCA `naaefs01` (outside the 705, known to have read `ctl/`) reads CTL-NAMED with
  8 calls, the 8 in gemini's list. Its `write_file` of LANDING.md, which mentions ctl, is not counted.
  `ncalbas01` (T-NCA-A) reads NONE-NAMED, as gemini's census does.
- **Raw-bytes axis:** among the NONE-NAMED cells of an earlier run, 23 transcripts carry the byte string `/ctl` or
  `ctl/`. Read one by one, all 28 matches are outside `tool_calls`: 24 tool RESULTS, 2 model texts and 2 system
  messages. So no call was missed there. Those results are limit 1 below.

## What this changes in the web census of 2026-11-20 (a note; no figure there moves)

That census's glob (`cells-*/*/.agyhome/…/transcript_full.jsonl`) does not reach a phase-1 transcript under
`<family>/_aside/<id>/`. Here that is 213 transcripts in 108 cells of record (MATRIX 60, ZF 48). Read now, they hold
**0 `search_web` and 0 `read_url_content` calls**, so its WEB-SERVED 10 and CLEAN 695 stand. Its statement that it read
"every brain transcript" did not cover them, and this paragraph records that.

## Limits (they bind every row above)

1. **A count of what was NAMED, not of what was SEEN.** A recursive search or listing from a parent reaches `ctl/` or a
   sibling cell without naming it. The raw-bytes axis found tool results carrying `ctl/` LINE CONTENT that way
   (`s3cp02`, `s3ps03`, `s3ft02`: `grep_search` results from `ctl/stream-1.ndjson`), and listings carrying `ctl/` names,
   in cells this census reads NONE-NAMED. So NONE-NAMED is a lower bound on contact. It is not "never touched".
   PARENT calls are listed as candidates.
2. **`$HOME` only.** Paths outside the home directory (`/tmp`, shared and mounted volumes) are not classified.
3. **No ruling.** CTL-NAMED stands under the 10-13 ruling. Whether an OTHER-RECORD cell leaves a comparison, as the
   WEB-SERVED cells do, changes what published tables assert. It is ruled separately and is not applied here.
