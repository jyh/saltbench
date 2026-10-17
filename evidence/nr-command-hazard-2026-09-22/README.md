# The command-hazard census (desk row NR), 2026-09-22

The cells' fence broke some invocations of `git` and `python3` in both arms. This directory holds the census that
asks whether the breakage fell harder on one arm. The paper's limits paragraph cites these files.

## The instrument
`command_hazard_v3.py`, in the private harness tree (`harness/systems-v3/`). The four `agy-out-*.txt` files were
produced by the version at commit `ad4cdc5` (file sha256/16 `7d93da1b10b22022`). It reads each session stream, takes
the first executable token of every shell invocation as its CLASS (`git`, `python3`, `other`), and reports per arm
and class:

- **HAZARD**: failed invocations over completed ones, WITHIN the class. A class-local rate cannot rise just because
  an arm runs more commands. The earlier split by command count was withdrawn because the count is the confounded
  variable.
- **MIX**: the class's share of that arm's invocations.

Failure is judged differently on the two lanes. The Gemini lane (`agy`) uses the meter's own output heuristic
(`agy_meter_v3.command_failed`, imported, not copied). The Claude lane uses the client's error flag. A rate on one
lane is never compared with a rate on the other.

The arm is read from the cells-root name. A root whose arm cannot be read is reported as `UNKNOWN` and named, and
it is in neither arm's row.

## The files
| file | what | source run |
|---|---|---|
| `agy-out-all.txt` | Gemini lane, every root, 340 streams | `ad4cdc5` |
| `agy-out-b4.txt` · `agy-out-l5.txt` · `agy-out-s3.txt` | the three Gemini blocks that carry both arms, one block each (24 · 56 · 45 streams) | `ad4cdc5` |
| `agy-pooled-2026-09-22.tsv` | Gemini lane pooled, an earlier run the same morning (09:23) | the working copy before `8d413ae` |
| `claude-pooled-2026-09-22.tsv` | Claude lane pooled | the working copy committed as `8d413ae` (09:27) |

The two Gemini pooled readings differ slightly (plain `git` 986 vs 972 completed invocations), and both give
81.4 %. The paper quotes `agy-out-all.txt`.

**Edited for publication:** in the four `agy-out-*.txt` files, the home-directory prefix of the `glob:` on line 1
was replaced by `~/`. Nothing else was changed. The originals' sha256/16: all `83fd5de0dc07093a`, b4
`7c6e9d1ab6d40d15`, l5 `27c768871d02e1a7`, s3 `9ee49ea716291d8d`.

## What it shows, and what it does not
`git` hazard, salt-diet minus plain, in percentage points:

| reading | plain | salt-diet | difference | file |
|---|---|---|---|---|
| Gemini, pooled | 81.4 % | 96.7 % | +15.3 | `agy-out-all.txt` |
| Gemini, block b4 | 100.0 % (n 29) | 96.7 % (n 302) | −3.3 | `agy-out-b4.txt` |
| Gemini, block l5 | 63.3 % (n 289) | 94.3 % (n 511) | +31.0 | `agy-out-l5.txt` |
| Gemini, block s3 | 100.0 % (n 58) | 97.6 % (n 254) | −2.4 | `agy-out-s3.txt` |
| Claude, pooled | 91.1 % (n 775) | 92.9 % (n 1,614) | +1.8 | `claude-pooled-2026-09-22.tsv` |

The pooled Gemini row also holds roots that carry only one arm. Of the three blocks that carry both, one (l5)
shows a large gap and the other two show a small gap the other way. The Claude lane's per-block reading was taken
on 2026-09-22 but its output was not kept, so only the pooled Claude row is on file. **So no arm difference
in `git` hazard is established on either lane, and the question NR asks stays open.** No census of the existing
streams can settle it.

The `other` class (49 to 83 % of an arm's invocations in these blocks) has a lower hazard under salt-diet in all
three Gemini blocks (b4 23.9 vs 70.5 %, l5 34.3 vs 85.2 %, s3 30.3 vs 61.5 %). `other` is a mixed class whose composition differs by arm, so that difference is a question
about composition, not evidence of a hazard effect.

These files declare no arm effect. Rows marked `!` have fewer than 20 completed invocations and are anecdotes.
