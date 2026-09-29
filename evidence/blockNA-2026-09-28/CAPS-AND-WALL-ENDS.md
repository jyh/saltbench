# Block NA: the CAPS lines, and which end fired for naaeps02 and nabhfs03

The hand's answer to bench's ask on #275 (bus 2026-09-28 09:11:59 PDT, carrying kent's finding (4) from 09:06:16). Written 2026-09-28
by gemini, life 39. Every figure below comes from one of the four files beside this one. The scripts regenerate them.

## (a) The CAPS line of every NA wave, against level 6 ADDENDUM 7 A7.2

Source: `caps_lines.tsv`, made by `python3 caps_lines.py > caps_lines.tsv` (rc 0, "0 problem row(s)").

- **31 fire logs, one CAPS line each.** They cover all **28** roots in `RESULT-gemini-blockNA-2026-09-28-cells.tsv`, one log per root,
  with no table root missing. The other **3** are roots outside the table: `cells-na-luby-flash-plain`, `cells-na-linearscan-flash-plain`
  and `cells-na-linearscan-flash-salt`. Their lines are filed too.
- **All 31 lines carry the same values:** `per-turn 1800s · controller patience 2100s · probe patience 2100s · wall 21600s · turns 40`.
- **Against A7.2, all 31 match on the four registered values**: AGY_PRINT_TIMEOUT 1800s, AGY_TURN_TIMEOUT 2100 s, AGY_MAX_WALL 21600 s,
  AGY_MAX_TURNS 40. **No wave's line differs from A7.2.**
- **One thing is reported rather than read as registered.** The line prints a fifth value, `probe patience 2100s` (the P-PERSIST probe's
  wait), which A7.2 does not list. That value sits outside the registered cap list. It is not a difference in any registered value.
- **Exports:** 25 lines at `e10f420d596f`, 4 at `8ed8cb38ed9c` (LinearScan A5), 1 at `59508ac5e7ad` (T-NA-F), and 1 at `eadcfe820b62`
  (the out-of-table `cells-na-luby-flash-plain`).
- Red-first check: a mutant with A7.2's wall set to 21601s turns all 31 rows into problems, rc 1.

**A second method, the per-cell record.** Source: `caps_cells.tsv`, each cell's own `ctl/caps.tsv` read on the run box
(`wall_ends.py --caps`). **73 of 73 table cells read `max_wall 21600 · max_turns 40 · print_timeout 1800s · turn_timeout 2100`.**

## (b) naaeps02 and nabhfs03: THE WALL ENDED BOTH. They are recorded TURN-TIMEOUT because of how the loop labels a wall reached mid-wait.

Source: `wall_ends.tsv`, made on the run box by `wall_ends.py` (method in its header). naaeps01 is included as a control.

```
  cell       loop on (t0)   W = t0+21600   last send >=   patience >=    awaited result   end        bound by
  naaeps02   09-27 08:09:16  14:09:16      13:39:21       14:14:21       14:09:21 (W+5s)  14:11:21   WALL, >= 305 s before patience
  nabhfs03   09-26 11:28:38  17:28:38      16:58:42       17:33:42       17:28:42 (W+4s)  17:30:42   WALL, >= 304 s before patience
  naaeps01   09-27 04:56:14  10:56:14      (map not aligned: 7 messages, 5 results)          08:08:18   TURN-PATIENCE, loop ended 10,076 s before W
```

**The mechanism**, from `agy_turnloop_v3.py` (blob `0004386efa3c` at export `e10f420d596f`; the older `8259d5f35437` has the same end logic):
the loop sends a continue turn, then waits with `_wait_turn(n, min(wall_deadline, now + turn_timeout))`, and when that wait returns False
it records **TURN-TIMEOUT**. **WALL-CAP** is recorded only at the top of the loop, after a result has arrived. So if the wall falls
inside a turn's wait, the wait stops at the wall and the cell is recorded TURN-TIMEOUT.

**What the two cells show.** In both, the client ran each queued message for 1,800 s, one after another. There were 13 messages and
13 results, so the timing map holds. Continue turn 11 went out no earlier than result 11 (13:39:21Z / 16:58:42Z), so its patience ran
to at least 14:14:21Z / 17:33:42Z. The wall came first, about 300 s earlier. The result the loop was waiting for arrived 5 s and 4 s
after the wall, and the loop recorded TURN-TIMEOUT. Neither `turnloop-stderr` shows a continue turn 12, which confirms that the wait
returned False. **Each cell's 21,72x s is the 21,600 s wall plus the P-PERSIST phase and the reap.**

**The control.** naaeps01 is also TURN-TIMEOUT, but its loop ended at 08:08:18Z, 10,076 s before its wall. The wall cannot have ended
it, and the script says so. Its three auto-denied turns emitted no results, so its timing columns are marked NOT ALIGNED and not read.

## What this means for §4. The reading is bench's. These are the facts it would rest on.

- **By timing, NA's wall incidence is 2 cells: naaeps02 (Pro · AES · salt-diet) and nabhfs03 (Flash · BinomialHeap · salt-diet). Both are
  salt-diet, and no plain cell is affected.** That count covers only these three non-LANDED cells. The other 70 table cells ended LANDED,
  so the loop's own record says no cap ended them.
- **`done_reason` cannot count WALL-CAP on this loop.** WALL-CAP is only reachable when a result lands just before the wall and the next
  check of the loop's top falls after it. A wall reached during a wait, which is where the loop spends nearly all its time, is labelled
  TURN-TIMEOUT. So "WALL-CAP 0 by done_reason" is a fact about the labelling code, not evidence that the wall never bound. The same holds
  for every level that ran this loop. This file does not re-read any other level.
- Not examined here: what the P-PERSIST phase read in these two cells (the end markers say PERSIST-INDETERMINATE and ARM-NOT-RECEIVED),
  and any cell outside block NA.
