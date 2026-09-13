# `harness/systems-v3/bin/` — the class-C runtime, now tracked

⛔ **Why this directory was created on 2026-09-13.** `harness/systems-v3/` held **36 tracked files and
every one of them was a document** — amendments, designs, pre-registrations, results. The programs that
produce those results, including the gate that decides a cell's verdict, were tracked in **zero commits
anywhere in this repository**. They lived in one untracked directory on one box.

Measured that day with a positive control (`git ls-files harness/` lists `HASHES.txt`, `arms/a0.md`, …
while `git log --all -- '*exec_gate_x*'` returns nothing), on the same shift that an irreplaceable cell
artefact was found recorded as "version-controlled and off-machine" and was in fact in no repository at
all. ⇒ **The same defect twice in one morning, once for evidence and once for the instrument.**

## `exec_gate_x.sh`

The class-C gate for node 1 (`hb_lemma10`). Runs OUTSIDE the fence after the executor stops.

| sha (256/16) | what changed |
|---|---|
| `54b4509b76f84d20` | registered in A5.4, before any class-C fire |
| `eb2b4f1e5d4b3450` | `X0-empty`; the `X6-flag` hard-coded-date fix |
| `b4fb3f8391d143db` | FIX 1 (an empty range reports `VACUOUS`) · FIX 2 (the cap sees the working tree) |
| `e79c769d8ddae638` | **FIX 3** (the content arms read the working tree when the branch is empty) + `FLEET_ROOT` |

**FIX 3, driven 2026-09-13 on the three cases that exist**, `GATE_NO_BUILD=1` throughout (a drive, never
a verdict):

```
  A  empty branch + 513 uncommitted   10 OK ·  2 FAIL   (was 10 OK · 2 FAIL — same TOTALS, different
                                                        MEANING: the OKs now read the proof instead of
                                                        comparing BASE against BASE)
  B  the reference landing, 2 commits 15 OK ·  3 FAIL   byte-for-byte the pre-change baseline
  C  empty branch + clean worktree     7 OK ·  0 FAIL   (was 12 OK · 0 FAIL, 11 arms now VACUOUS)
```

⇒ 🔑 **Case C is the finding the specification did not name: before FIX 3 a cell that did NOTHING AT ALL
scored 12 OK · 0 FAIL while the cell that PROVED the theorem scored 10 OK · 2 FAIL.** An absence of
measurement scored better than the measurement would have.

**Five arms RED-driven on the new worktree path**, each flipping exactly one arm and no other:
`X1-statement` · `X1-others` · `X2-nosorry` · `X1-flags-append` · `X0-scope`.
⚠️ **`X3` (build · axioms · warnings) is routed through the same source selector but its LIVE BUILD is
NOT driven here** — `GATE_NO_BUILD=1` skips it. What is shown is that the block is *entered* with
`SRC=worktree`. Those arms were run by hand on n1a-pro's snapshot; that hand-run is the evidence, and
this line says so rather than letting the drive's green imply more than it measured.

⛔ **`X0-clean` still FAILs on a dirty worktree and that is correct** — the cell's brief requires every
draft to be committed. FIX 3 makes the work *measurable*; it does not make leaving it uncommitted OK.
