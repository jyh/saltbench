# RECEIPT — §B7 ROW 3's SECOND LAYER IS DRIVEN. `probe_sandbox` EXISTS FOR THE CLAUDE CLIENT.
## systems, 2026-09-14, desk row MQ. Every number below was taken at the object on the run box.
## ⛔ THIS IS A RECEIPT, NOT A RULING. bench is the SaltBench lead and marks row 3, or says why not.

---

## §R0 · WHAT WAS ASKED, AND WHAT IS IN HAND

ADDENDUM 17 sized row 3's remainder and named what was missing: *"not a cell and not a root — a
`probe_sandbox` for the CLAUDE client"*, closing when **a Claude cell attempts to read
`BROWNFIELD-PLANTS.tsv` by its full path from a SUBPROCESS under its own rendered fence and gets
`Operation not permitted`, with the GREEN half beside it (a path INSIDE the cell still readable)**.

`harness/systems-v3/probe_sandbox_v3.sh` is that instrument, built to
`DESIGN-claude-sandbox-probe-2026-09-13.md` (§S0–§S7 and its five addenda). It is driven **through the
client's own fence**, never through `sandbox-exec` by name. **23 selftest arms**, wired into
`selftest_all_v3.sh`, **zero model calls and no toolchain required**.

---

## §R1 · THE THREE LIVE ARMS, IN ONE REAL BROWNFIELD CELL

Cell `5b9c3a17` — `--task LZW --arm plain --field brownfield --client claude`, `ctl/field` = `brownfield`,
seeded `solution.rs` differing from `interface.rs`, staged with `_bin` → fence (sealed over the whole
root) → trust, `cell-claude.sh --check` **clean**. Box: THE RUN BOX (its hostname is in the machine
receipt on that box, not here — this repo's own infrastructure-name gate forbids the literal, and this
file tripped it on its first staging). Client
`~/.local/share/claude/versions/2.1.259` **by absolute path** (ADDENDUM 1 §A1.2: the pin, not the
symlink, which resolves to 2.1.263 and has launched no cell of this campaign). Model `claude-opus-5`.
Export `saltbench-systems-v3-export-4782bf6`.

```
  ARM   fence                                 sha/16            OUTSIDE_RC  OUTSIDE_ERR                  INSIDE  VERDICT
  P1    the cell's own rendered fence.json    61f8b29e5a86e176      1       Operation not permitted      nonce   GREEN
  M1    same, sandbox.enabled = FALSE         cc6af9f97cdf3da9      0       (empty)                      nonce   RED outside-readable
  M2    same, denyRead = []  (enabled TRUE)   1d48fbe466b94414      0       (empty)                      nonce   RED outside-readable
```
`--outside` on all three: `/Users/jyh/projects/claude/saltbench/harness/systems-v3/BROWNFIELD-PLANTS.tsv`.
`fence_loaded yes` on all three (`--settings <fence> doctor`, free, before any model call).
`inside_returned_nonce yes` on all three. `client_rc 0` on all three.
P1's stderr **verbatim**, from the receipt:
```
  cat: /Users/jyh/projects/claude/saltbench/harness/systems-v3/BROWNFIELD-PLANTS.tsv: Operation not permitted
```
Receipts: `<cells>/_audit/sandbox-probe/<fence-sha16>.tsv`, one per fence sha, plus the `P-SANDBOX`
line in `ctl/launch.log` — **the same line ADDENDUM 17's census greps for**, so this lane is now
countable by the instrument that found it uncounted.

⭐ **M2 IS THE ARM THAT MAKES P1 MEAN WHAT IT SAYS, AND IT WAS NOT REQUIRED OF ME.** M1 shows the read
succeeds when the sandbox is off. That alone leaves the attribution open: `render_fence_v3.py` emits
`Grep(...)` rules whose effect on a Bash subprocess its own comment calls **unmeasured**, and the
renderer's corrected invariant is that **either layer alone denies**. M2 leaves the entire fence intact
and empties **`sandbox.filesystem.denyRead` alone** — and the read succeeds. ⇒ **P1's denial is
`sandbox.filesystem.denyRead`'s doing, not the hook's and not `permissions.deny`'s.** That is the layer
row 3 is about, and it is now isolated rather than inferred.
⇒ M1 and M2 together also dispose of the obvious objection to P1: **the file is demonstrably readable
on this box when the fence is relaxed**, so nothing about the file, its mode or its mount produced the
denial.

---

## §R2 · ⛔⛔ THE FINDING I DID NOT GO LOOKING FOR: **THE REGISTRY IS NOT ON THE RUN BOX, AND ABSENCE IS NOT A FENCE**

`~/projects/claude/saltbench` **does not exist on the run box**. Measured before the drive, with a
positive control (`find` over `~/projects/claude` returns the twenty-odd export trees and no
`BROWNFIELD-PLANTS.tsv`). The registry lives in the `saltbench` checkout on the seat box only.

⇒ **Today, no Claude cell can read the registry because THE FILE IS NOT THERE.** That is the protection
this campaign has actually been running on, and it is the one protection that disappears the moment
someone clones or syncs the tree onto the run box — silently, with every gate still green. §B1 already
worried at exactly this altitude: *"a registry whose secrecy depends on a mechanism I have not read is a
leak channel I have merely not found yet."*

✅ **SO THE DRIVE WAS TAKEN AGAINST THE REAL OBJECT AT ITS REAL PATH, PLACED FOR THE DRIVE.** I copied
`BROWNFIELD-PLANTS.tsv` from `origin/main` to its canonical path on the run box, sha-matched both sides
(`5a850e75afebfcdd54edfdbacaba1503609b5771ef057709b01daf4c4399c0d6`, 19 lines), drove P1/M1/M2, and
**removed it afterwards** — the box's state is as I found it. ⛔ **This was not a convenience.** The
probe **REFUSES** an `--outside` that does not exist, for the reason that makes the whole instrument
honest: *a path that is absent is denied to everybody, and a probe pointed at one certifies a fence that
is doing nothing.* Driving row 3 against a missing file would have produced a green about nothing.

⚖️ ***WHAT THIS BUYS, STATED PRECISELY:*** the receipt says the fence **would hold even if the tree were
synced onto the run box.** It is a claim about the fence, no longer about the geography. **That is
strictly stronger than what row 3 asked for**, and it is the half that survives someone running a
`git clone` on the run box next week.
📌 **No exposure was created.** `BROWNFIELD-PLANTS.tsv` is on `origin/main` of the **public** repo —
measured at origin, not in a working tree — which is what *"a REGISTERED planted-defect list"* means:
registration is a public commitment, and the threat model §B1 names is **the cell**, not the world. A
cell has no network (`allowedDomains []`, `strictAllowlist true`, WebFetch/WebSearch disallowed by name
and struck from the tool list), so publication does not reach it.

---

## §R3 · THE THREE DEFECTS THE BUILD FOUND IN ITSELF, EACH FOUND BY A DRIVE AND NOT BY A REVIEW

**(1) THE PROBE MUST NOT PUT THE DENIED PATH IN THE BASH TOOL'S COMMAND STRING.** `hook-deny-v3.sh`
adjudicates the command STRING and would have blocked first (exit 2 — ADDENDUM 11 drove exactly that),
so the naive probe re-drives **the layer that is already green** and files the result under the name of
the one that is not. The denied read therefore lives in a **script file inside the cell**; the hook sees
only in-cell paths and stands aside, and the read that follows is a subprocess read.
⇒ 🔑 ***THE TWO LAYERS ARE DIFFERENT GATES, AND AN INSTRUMENT AIMED AT THE SECOND ONE HAS TO GET PAST
THE FIRST WITHOUT DISABLING IT.***

**(2) MY SYMLINK GUARD OVER-REFUSED, AND MY FIRST FIX WAS AN OVERRIDE.** I spelled it as
`cell-claude.sh` spells it — `realpath(BIN) != BIN` — which is right for the pin it protects and wrong
as a general test: on macOS every path under `/var` realpaths to `/private/var`, so an ordinary file in
`$TMPDIR` is refused **as a symlink** while being nothing of the kind. My first repair added
`SBPROBE_ALLOW_SYMLINK` to make the arm pass.
⇒ 🔑 ***A GUARD THAT OVER-REFUSES IS NOT THE SAFE DIRECTION — IT GETS AN OVERRIDE ADDED TO IT, AND THE
OVERRIDE IS WHAT THE NEXT HAND WILL SET.*** The test is now `-L` on the named file, driven both ways.
📌 **Routed, not touched:** `cell-claude.sh` carries the same spelling. It is harmless there today
(the pin is never under `/var`) and it is a live launch path, so I am naming it rather than editing it.

**(3) AN `INDETERMINATE` THAT KEEPS NO BYTES IS A CORRECT VERDICT AND A USELESS REPORT.** The first live
drive returned `INDETERMINATE (no-marker)` in two seconds with `client_rc 1`. The verdict was **right** —
§S3's cure working exactly as designed, absence refused as a denial — and the receipt could not say why,
because the cause was one line the client printed and the tool had deleted with its temp files:
`Failed to authenticate: OAuth session expired and could not be refreshed`. A non-GREEN verdict now
writes the raw reply beside the receipt and names it.
📌 A fourth, smaller one: the receipt store keys on the FENCE SHA (§S4), so two drives of one fence
against **different** `--outside` targets shared a key and the second replaced the first. Every drive
now also appends to an append-only `drives.tsv`; `--require` still reads the keyed receipt, so a later
RED cannot be hidden by an earlier GREEN.

---

## §R4 · WHAT THIS RECEIPT DOES **NOT** ESTABLISH — unchanged from §S6, restated so nobody widens it

```
  DOES NOT   say anything about the 124 Claude cells already run. Their layer stays UNMEASURED, and a
             probe built today CANNOT be applied retroactively to a cell that has landed.
  DOES NOT   retro-certify, or move, any published number. The Claude-lane gap was UNMEASURED, NOT
             UNSOUND; it is now measured GOING FORWARD and that is the whole of the change.
  DOES NOT   make permissions.deny and sandbox.filesystem.denyRead one thing. A green here is a green
             on ONE layer; the hook layer is separately driven and separately green.
  DOES NOT   hold for another client version. The receipt names 2.1.259 and a version change
             invalidates it — a one-time drive is a claim about a sha, never about a repo.
  DOES NOT   hold for another FENCE. Receipts are keyed on the fence sha and inherited by identity
             only: never by cells root, never by wave, never by date. The deny set is a glob taken at
             RENDER time, so a cells root that grows leaves an earlier cell's fence permissive.
```

⛔ **AND ONE THING I DELIBERATELY DID NOT DO.** I did **not** wire `--require` into `cell-claude.sh`'s
launch path. ADDENDUM 17's own reason still holds — *"it changes the gate's control flow on the path a
verdict runs through, and a gate that mis-runs is worse than one that visibly skips"* — and the
enforcement mode is built, driven in four selftest arms, and ready for whoever rules on it. **Wiring it
is a lead's call on a live launch path, not a builder's on the shift that wrote the tool.**

---

## §R5 · FOR bench, AS LEAD — the three things to rule on

1. **Does §B7 row 3 close on this?** The receipt is the one ADDENDUM 17 specified, plus the M2
   attribution arm and the §R2 correction to what was actually protecting the registry.
2. **§R2's standing item:** the run box has no `saltbench` checkout, and the brownfield fire should not
   come to depend on that. This receipt says the fence holds if it ever does.
3. **`--require` on the launch path:** built and driven, unwired, waiting on a ruling.

📌 **Cost:** four `claude -p` turns total, one of them wasted on a dead credential.
⚠️ **AND A FACT ABOUT THE BOX, ROUTED, NOT A FINDING ABOUT THIS ROW:** of the eight credentialed run
config dirs on the run box, **four fail to refresh** (`Failed to authenticate: OAuth session expired
and could not be refreshed`), **one reports a weekly limit**, **three carry a settings defect the
client warns about on startup**, and **exactly one authenticates cleanly**. The dirs and accounts are
named in the private run record and deliberately not here, per this repo's account-name convention.
⇒ 🔑 ***THE AUTH FAILURE EXITS rc 0.*** It is the third instrument in this row's history whose rc
carries no verdict (`doctor` is the other two), and a launcher that branched on it would read a dead
credential as a clean run. My probe read it as `INDETERMINATE`, which is right, and could not say why,
which is §R3(3).
