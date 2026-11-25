# AMENDMENT (DRAFT, NOT IN FORCE): the agy lane's read fence becomes an ALLOW-LIST over the home directory (2026-11-25)

*bench (lead), 2026-11-25. This is a draft. It binds nothing until three things hold: the build arm in §3 is measured, a
non-author has signed this file at its blob, and an export carries it. No cell of the running NCA/WCA chain changes. It
amends the agy render that `AMENDMENT-agy-ctl-fence-2026-10-13.md` declares. That amendment's §5 ("reads of ctl/ stay
open") is replaced for cells fired under this one only.*

## §1 · WHAT IS WRONG (measured 2026-11-25; evidence `evidence/o37-agy-ctl-read-census-2026-11-25/`)
The srt render denies reads by NAME. Its `denyRead` is the Claude arm's lifted list, plus the cell's siblings as they stand
at render time, plus `harvest-v3`, `rescore-tool` and every home entry named `cells` or `cells-*` (harness `5cd1c209`,
2026-09-10). The class test is a name prefix. A cells root renamed for keeping (`EVIDENCE-…--cells-…`,
`PRESERVED-waves-…/cells-…`), and any scratch or export root, falls outside it.
- **Open now.** Against the live argon cell's own `srt-settings.json` (1,158 `denyRead` entries), 583 of 1,693 non-dot
  home entries on the run box are not covered. They include two old exports whose
  `tasks/systems-v3/{LRU,FreeList,LZW,Crc32,Paxos}/B/` are withheld suites. No open tree holds a B/ suite or a
  reference for a problem the running chain sets. That was checked by path name, and it is the limit of the check.
- **Used.** Over the 705 agy cells of record, 52 subjects named a literal home path outside their cell (OTHER-RECORD).
  Their results show another record's content reaching the subject in 2: `l5fs02` (a `PRESERVED-waves` cell's tests) and
  `l8rfss03` (another cell's brain transcript). Both went through renamed roots. The fence refused 20; 17 received names
  only.
- **ctl/.** Reads of the cell's own `ctl/` are open by the 10-13 ruling. 107 MATRIX subjects read it, and NCA `naaefs01`
  read its briefing claim before producing its receipt.

⇒ ***A DENY-LIST HAS TO ANTICIPATE; AN ALLOW-LIST ONLY HAS TO BE COMPLETE.*** `render_agy_fence_v3.py` says this in its
header. The srt render kept the deny-list shape, and every miss above is something it did not anticipate.

## §2 · THE RULE
```
  denyRead   = [ $HOME ]  +  [ <cell>/ctl ]                      a subpath deny: every home path, existing or LATER
  allowRead  = [ <cell> ]  +  the client binary and its runtime   (the agy binary's dir, node, srt-pin)
               +  the toolchain roots the cell's bin/rt reads      (verus, the cargo root, rustup), each named, never $HOME
               +  the cell's TMPDIR
  allowWrite = unchanged (10-13 §2): <cell>/repo, the client's own ctl/agy-client-<phase>.log, the client temp and .agyhome
```
- **The renderer asserts on the RENDERED set** (the 09-07 lesson): it refuses a config under which any `SENSITIVE` path
  (`render_agy_fence_v3.py`'s list) or any other cells, export, evidence or preserved root is readable. It also refuses
  an `allowRead` entry that is `$HOME`, an ancestor of `$HOME`, or covers a `SENSITIVE` path.
- **ctl/ is closed to reads by the subject.** The client writes its own log there. Whether the client also reads it, and
  whether the turn loop opens ctl files inside the sandbox, is measured before this binds (§3 arm 4).

## §3 · RECEIPTS
**Measured (2026-11-25, run box, srt 0.0.76, cli sha256/16 `f75ea1f8bb31bbd4`, zero spend; probe `~/bench-dry/srtprobe.sh`):**
```
                                   control (no deny)   denyRead [$HOME, cell/ctl] + allowRead [cell, a toolchain file]
  cell/repo/x.txt                   read               read
  cell/ctl/secret                   read               Operation not permitted
  a home path that existed          read               Operation not permitted
  a file created AFTER the config   read               Operation not permitted
  a toolchain file (~/.rustup)      read               read
  /etc/hosts                        read               read
```
An `allowRead` re-opens a path under a denied one, and a deny on a path inside an allowed one wins. Verdicts are read from
the output text.

**Owed before this binds (each a red-first arm, run in a quiet window, because a build perturbs a live cell's wall clock):**
1. A real cell's `bin/rt check` and build, by COPY of a finished cell, under the rendered config: rc 0, beside the same
   copy under the current config.
2. A battery cell (client rc 0, P-DELIVERY/P-PERSIST/P-ANYWHERE/P-SANDBOX, FENCE-OK) on the export carrying the render.
3. Plants: a root under `$HOME` created after render, a renamed cells root, and an old export's `B/`. Each must be
   refused from inside the cell. Controls: the cell's own repo, and the toolchain.
4. ctl/: the client log still lands, and no harness file the turn loop reads goes missing.
5. The renderer's refusal arms: an `allowRead` of `$HOME` or `/Users` is refused; an `allowRead` covering a `SENSITIVE`
   path is refused; a mutant that drops the `$HOME` deny goes RED on plant 3.

## §4 · WHAT IS NOT CHANGED
No cell of record and no figure. The network rule, the write fence and the hook route are unchanged, and so are the census
classes (`evidence/o37-agy-ctl-read-census-2026-11-25/`). That census runs per harvest under this rule too: a subject
that NAMES an outside path is still recorded, even once the fence refuses it.

## §5 · WHEN IT BINDS
It binds from the first agy cell fired on an export whose render implements §2, once §3's owed arms are receipted in an
addendum here and a non-author has signed this file at its blob. Until then it binds nothing.
