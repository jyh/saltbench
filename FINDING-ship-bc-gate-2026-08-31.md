# FINDING — the `ship BC` gate is GREEN, and the line it is green on was written by a run that executed NOTHING

**Measurement only. No repair is made here** — the `ship BC` gate is the act that puts ground truth on the
episode host, so its predicate is a hermeticity property of the protocol and changing it is a design act under
its own dated amendment. This document proves the defect at the machine and prices the repair; it does not
apply one. Evidence: `evidence/ship-bc-gate-finding-2026-08-31/` (the read-only probe and its output).

## 1 · What the bank claimed, and what is actually true

The amendment-8 bank named this as a 📌 STALE GATE: *"`ship BC` reads `~/bench/logs/run_s2_stage0.log`, which the
a8 run no longer writes, so it passed on the SONNET run's DONE — a green light wired to nothing."*

That was a code read, and it is **understated**. The truth at the artifact is worse and more specific.

## 2 · The gate, run verbatim and read-only, right now

`harness/s2lean/stage_views.sh:17`:

```sh
$SSH "$STUDIO" 'grep -q "S2 STAGE A DRIVER DONE" ~/bench/logs/run_s2_stage0.log 2>/dev/null' \
  || { echo "REFUSE: the Studio's stage-A driver has not printed DONE (FORCE_BC=1 to override)"; exit 3; }
```

**GATE = PASS.** It would ship 322 ground-truth files onto the host on the next invocation.

The file holds four DONE lines. The newest is **not** the Sonnet run's, as the bank said — it is
`2026-08-31T18:32:19Z S2 STAGE A DRIVER DONE k=27`, i.e. **today, 11:32 PDT**, and its context is:

```
18:32:18Z SMOKE GATE OK …
18:32:18Z CONTROLS GATE OK
18:32:18Z ONLY_IDS / TC_AMEND / R_AMEND / M_AMEND / W_AMEND  (the amendment-8 knobs)
18:32:19Z S2 STAGE A DRIVER DONE k=27
```

**START/LANDED lines between those gates and that DONE: 0.** One second, twenty-seven problems, nothing run.

## 3 · Which run wrote it — and this is the point

That invocation is **the first of the two fatals amendment 8 caught before a single model token was spent**: the
driver, pointed at the old state root, found every episode already landed from the Sonnet run, **skipped all of
them, and printed DONE.** The cure was a fresh state root (`~/bench-a8`), and the real run's own DONE line lives
there — `~/bench-a8/logs/run_s2_stage0.log:226`, `2026-08-31T20:09:16Z`, 97 minutes later.

⇒ **THE GATE'S GREEN LIGHT WAS MINTED BY THE EXACT BUG THE FRESH STATE ROOT WAS CREATED TO ESCAPE.** The defect
was caught, the run was moved away from it, and the artifact it left behind stayed in the gate's file — where it
now reads as authorization.

📌 The **ship target is fine**: `~/bench-a8/s2views` is a symlink to `~/bench/s2views`, so the hardwired
destination is the directory the a8 run actually used. Only the *gate* went stale. A defect in the incidental
half again, as on 08/26 and 08/30.

## 4 · The three ways this predicate fails, named separately

1. **WRONG ROOT.** The path is hardwired to `~/bench` while the driver takes an arbitrary `$BENCH`. A run in any
   other root is gated on a file it never writes.
2. **NO FRESHNESS.** `grep -q` over an append-only log matches *any* DONE line ever written. The gate cannot
   distinguish this run's completion from one two days old.
3. **NO SUBSTANCE.** A DONE line is a claim by the driver, not a fact about the state. A driver that skips every
   episode prints the same line as one that ran them all — as this file proves in one second of wall clock.

## 5 · The repair, priced but NOT applied

**Gate on the CONTENT, not on the log** — the campaign's own law (*the receipt is the content, not the tool that
moved it*). The predicate `ship BC` actually wants is "stage A is complete for the drawn set in the active state
root", which is exactly the read-only pre-flight already driven by hand on 08/29: the drawn ids equal the staged
ids, and every `A.bodies.json` is non-empty and carries its provenance (`a_episode`, `a_bodies_sha256`,
`a_view_sha256`, `a_termination`, `a_passed`). That predicate cannot be satisfied by a driver that ran nothing,
cannot be satisfied by a stale log, and is root-relative by construction.

Cost: small — one function, a `BENCH` parameter, four REFUSE arms and an accept arm driven under the run-shaped
dry, as a dated amendment. **What makes it NOT tonight's work:** `ship BC` is the act that ends stage-A
hermeticity, so its gate is part of the protocol's safety claim, not a convenience. It gets registered before it
runs, like everything else here.

**Until it is repaired, the operating rule is:** ⛔ **treat `ship BC`'s gate as decorative — verify stage-A
completion by hand, in the active state root, before invoking it.** It is green right now on a no-op.

## 6 · Laws

- **A gate that reads a path the run no longer writes is a green light wired to nothing** (banked 08/31) — and
  its sharper form, paid for here: **a green light can be minted by the very bug you escaped, and it outlives
  the escape.**
- **`grep -q` over an append-only log is a gate with no clock.** Any predicate that must mean "this run" and is
  written against a cumulative file is unsound by construction.
- **A driver's DONE line is a claim, not a measurement.** Gate on the state the stage produced, never on the
  sentence the stage printed.
