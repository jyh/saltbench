# AMENDMENT — the agy lane's ctl/ write grant is INVERTED (2026-10-13)

*bench (lead), 2026-10-13. Registered BEFORE any agy cell fires on the new fence; none is queued. It changes what level 6
ADDENDUM 5 (A5.2) and the agy render declare the fence to be, so it goes to a non-author for signature before it binds.*

## §1 · WHAT WAS WRONG
The agy render granted the subject write access to the whole cell control directory: `allowWrite = [<cell>/repo, <cell>/ctl]`.
The harness TRUSTS files in `ctl/` (`customer.log`, `card_extras`, `task`, `arm`, `end-<N>`). A subject that rewrote one could make a
cell's record rest on a check the harness never ran.
- The first repair (harness `761b2c6`, 2026-10-12) carved out a `denyWrite` for three named files. Driven on the run box at that sha,
  **five write routes still SUCCEED** (rc 0): overwrite `ctl/arm`, overwrite `ctl/end-1`, delete `ctl/end-1`, create a new `ctl/` file,
  write `ctl/agy-client-1.log.x`. A carve-out by name goes stale whenever the harness adds a ctl file.

## §2 · THE RULE (harness branch `gemini/agy-ctl-invert-2026-10-13` @ `b88435c`, parent `761b2c6`)
```
  allowWrite   = <cell>/repo  +  ctl/agy-client-<phase>.log (the client's own --log-file, derived once for the grant and the flag)
                 (+ the client's temp and .agyhome, as before)
  ctl/         is NOT a write root. Every harness ctl file is asserted outside every write root, and the render refuses otherwise.
```
- A `--client-log` that is not exactly `<cell>/ctl/agy-client-<phase>.log` is REFUSED.
- **A THIRD STATE in the render:** a hook deny that is inside the cell and under no write root is declared `outsideWriteRoots`
  and is not added to `denyWrite`. **A5.2's `ctl/web-deny.sh` row is now in that state.** A path outside the cell is still refused.
- **THE DECLARED ROWS CHANGE SHAPE**, and this amendment is their declaration:
```
  filesystem.denyWrite+hookFiles  = { denyWrite: [the 3 .agyhome hook paths], outsideWriteRoots: [ctl/web-deny.sh] }
  filesystem.allowWrite-ctl       = { ctlWritable: [the phase's client log], harnessOutsideWriteRoots: [task, card_extras, customer.log] }
                                    REPLACES the row denyWrite+harnessCtl
```
- **A5.2's containment claim is unchanged.** The workspace hook route is still detect-and-void, and nothing here says the subject
  could not reach a web tool.

## §3 · RECEIPTS (the builder's, harness branch above; zero subject spend except the one live cell)
```
  red-first      branch 232/232 · 761b2c6's renderer under the new suite 223/232, failing exactly the 9 new renderer arms
                 a mutant that makes ctl/ a write root makes the render REFUSE
  drive          srt 0.0.76, every verdict read from outside the fence: at 761b2c6 the 5 routes of §1 succeed; at b88435c all 14
                 attack rows are REFUSED. Controls: client log create+append written · repo/x written · a write outside the cell
                 refused · ctl/task readable · ctl/ listable
  live           1 plumbing-only battery cell, gemini-3.8-flash-high, export b88435c: client rc 0, P-DELIVERY / P-PERSIST /
                 P-ANYWHERE / P-SANDBOX all yes, FENCE-OK; its srt-settings allowWrite holds exactly ONE ctl/ entry (the client log).
                 stream-N, agy-stderr-N and agy-turnloop-stderr-N all LANDED under a fence that does not grant them, and a new
                 ctl/ file is refused, so the turn loop opens them OUTSIDE the sandbox. Nothing else is named.
```
⚠️ **Limit, the builder's:** the arm "5 bad `--client-log` shapes refused" passes vacuously on `761b2c6`, which rejects the unknown flag.

## §4 · THE PAST, MEASURED (`evidence/agy-ctl-census-2026-10-13/`)
**Writes.** 272 agy cells of record (every AGY row of `evidence/v3-cost-tables-2026-09-28/cellroots.tsv`): **0 subject writes to
ctl/.** Two methods: every subject tool call in every conversation (main and subagents) that names ctl/ is a read (751 call shapes,
`ctl-refs.out`); and no `customer.log`, `card_extras`, `task`, `arm` or `end-<N>` has an mtime inside any phase's subject window
(`ctl-census.out` line 2). 107 subjects READ ctl/. **No result of record changes.**
⇒ Limits: a tool call is seen, not what a program it ran wrote; an mtime is a file's last write only.

**The briefing-receipt side route** (AMENDMENT-briefing-receipt ADDENDUM 2: the token must have exactly one route, the arm file —
here and below, the ARM FILE is the subject's `repo/AGENTS.md` (or `repo/CLAUDE.md`), not the harness's `ctl/arm` of §1).
Cells built before 2026-09-16 kept the token at `ctl/briefing-nonce`, readable by the subject (and in `ctl/launch.log`). The harness
census of 2026-09-16 (desk PW) measured level 5 and found 0 receipts earned through it; level 5's result declares it (§D2 of
`RESULT-gemini-flash-level5-2026-09-15.md`), and the launcher has REFUSED that layout since. **What this census adds is the levels
that one did not cover:**
```
  legacy-layout cells of record (ctl/briefing-nonce present)   92  =  s3 38 · b4 12 · l5 42
  a side route used, after the arm file                         27  =  s3 1 (s3cs03) · l5 26
  a side route used BEFORE any arm-file touch (UNSUPPORTED)      0
```
(`side-route-all-legacy.out`; the receipt conversation is the one whose first transcript line contains `Receipt`,
`side_route_all_legacy.py`.) ⚠️ **The table counts calls that NAME a side route** (`briefing-nonce`, `launch.log`, `ARMRECV`).
Whole-cell and `ctl/*` searches were cross-checked by a non-author (kent): 2 cells ran a cell-root content search for `Receipt` before
the arm-file read, and neither surfaced the nonce. ⇒ **The s3 and b4
results carry the same limit as level 5's §D2, and the census of record gets it in one line beside their receipts.** The level-5
count here (26) differs from the 2026-09-16 figure (32) because the population differs: that one read every `~/cells-l5-*` root,
discarded roots included; this one reads the cells of record.

## §5 · WHAT IS NOT CHANGED
- Reads of ctl/ stay open. The fence is a write fence, and the token no longer lives in the cell.
- The client log stays subject-writable. It is the client's own channel, and the lane's 503 count reads it, as before.
- No cell is re-run and no figure moves.

## §6 · WHEN IT BINDS
From the first agy cell fired on an export at or descending from `b88435c` after it reaches the harness's master, and only once
a non-author has signed this file at its blob. Until then no agy cell fires (the helm's 10-11 order).
