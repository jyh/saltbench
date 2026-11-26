# The (b′) re-cut: the 2 CONTENT cells out of every comparison, old line beside new (O37, 2026-11-25)

Census **ADDENDUM 52** (2026-11-25, arm (b′), the Captain's ruling at the 2026-11-25 sitting) puts the two agy cells of record that
received another record's CONTENT, `l5fs02` and `l8rfss03`, out of every comparison under ADDENDUM 47's WEB-SERVED rule; the other 50
OTHER-RECORD cells stay, labelled. This directory shows what that moves. It **replaces no table of record** and is not the source of any
figure in the paper; each RESULT it touches carries a dated addendum quoting its `*-moved-vs-ruled.txt` verbatim.

```
python3 -I check_recut.py            # reproduce every file here from the instruments of record; exit 1 on any byte difference
python3 -I check_recut.py --mutant   # the same with one tracked file altered in a scratch copy; must exit 1
```

- **The instrument:** `../o37-agy-ctl-read-census-2026-11-25/recut/recut_sets.py`, a copy of the 11-20 `recut.py` changed only in
  which cells it takes out: the 10 WEB-SERVED cells (read from `../o37-agy-web-served-2026-11-20/join.tsv`) plus the ids in a set
  file. The set is `../o37-agy-ctl-read-census-2026-11-25/recut/set-content.txt` (derived from `other_seen.tsv`, never typed).
  No instrument of record is changed.
- **Control, every run:** each OLD reproduces its RESULT of record's table rows exactly (`run.log`: descriptive v2 864/864,
  v2 + O57 864/864, cost v3 922/922, correctness v3 781/781, ZF check green); `#TAKEN-OUT-NOWHERE 0 of 12`.
- **Two readings, two file families:**
  - `<label>-moved.txt`: the RECORD (OLD) against the record without the 12 (NEW), as the 11-20 re-cut's files are. `ZF-moved.txt`
    and `blockNA-moved.txt` equal the 11-20 ones byte for byte: the two cells are MATRIX cells, so blocks NA and ZF do not move.
  - `<label>-moved-vs-ruled.txt` (the four MATRIX instruments): the RULED state (the record without the 10 WEB-SERVED, the 11-20
    NEW) against NEW, by the 11-20 `recut_diff.py`. This is what (b′) adds on top of the 11-20 re-cut, and it is what the RESULT
    addenda quote. Three of the four equal #474's `out-content/` files byte for byte; the O57 one is new here.

## What moves on top of the 11-20 re-cut
Read from the `*-moved-vs-ruled.txt` files (and listed there in full):
- **Correctness P4:** Flash × FreeList × greenfield, salt-diet, goes from `−` to `—`; with `l5fs02` out the ADDENDUM 3d guard prints the
  condition `unmeasured` (it was recorded by condition, 0 / 3). Not a pass. Flash bare P4 counts `0 2 1 1 1` → `0 2 0 1 2`.
- **Correctness P3:** Flash × LRU × spec-change, salt-diet phase 2, `3 / 3` → `2 / 2` (`l8rfss03` was a PASS).
- **Descriptive T4 (v2 and O57), cost $4 and W4:** every k-of-m sign holds; medians and the per-condition cells of the two conditions move.

## Declared, as in the 11-20 re-cut
The correctness tool's own arithmetic check goes red on the NEW run (`run.log`: `tool rc ... new 1`) because one more condition prints
`unmeasured`; that is the removal, not a fault. The removal is one-armed (both cells salt-diet), and moves salt-diet's record in both
directions at once (a `−` and a PASS leave).

## Limits
The 50 that stay are not shown uncontaminated (the census README, limit 1: NONE-NAMED and NAMES-ONLY are lower bounds on contact).
Nothing here is about the salt method.
