# RESULT — O37's FIRST LEAN ARM: SIX CLAUDE CELLS, CRC-32 × GREENFIELD × LEAN-AENEAS × {OPUS, SONNET} × n = 3
## bench (SaltBench lead), 2026-09-30. Registration `AMENDMENT-O37-aeneas-pilot-2026-09-30.md` (signed, ADDENDA 1–6; merged 0c8bf97b).
## Every figure below names the file it comes from. The cell table is DERIVED by `evidence/o37-aeneas-pilot-2026-09-30/o37-derive.sh`
## into `evidence/o37-aeneas-pilot-2026-09-30/cells.tsv` (sha256/16 9b27bae062ab…); nothing in it was typed.

---

## §R1 · THE SIX CELLS — ALL SIX ARE A LEAN-ARM PASS
A Lean-arm PASS (§A3) is: hidden suite FULL PASS ∧ the Lean half GREEN from the harness's bytes ∧ the statement UNCHANGED.
```
  cell      model            end      dirty  suite  tests  Lean half  axioms (kernel replay, then walked)       statement  PASS  proof lines  final $
  clbeca01  claude-opus-5    LANDED   0      PASS   6/6    GREEN      Classical.choice · Quot.sound · propext   UNCHANGED  PASS  246          13.8698
  clbeca02  claude-opus-5    LANDED   0      PASS   6/6    GREEN      Classical.choice · Quot.sound · propext   UNCHANGED  PASS  217          16.6597
  clbeca03  claude-opus-5    LANDED   0      PASS   6/6    GREEN      Classical.choice · Quot.sound · propext   UNCHANGED  PASS  253          13.1300
  clbwca01  claude-sonnet-5  LANDED   0      PASS   6/6    GREEN      Classical.choice · Quot.sound · propext   UNCHANGED  PASS  243          20.8473
  clbwca02  claude-sonnet-5  LANDED   0      PASS   6/6    GREEN      Classical.choice · Quot.sound · propext   UNCHANGED  PASS  346          19.6846
  clbwca03  claude-sonnet-5  LANDED   0      PASS   6/6    GREEN      Classical.choice · Quot.sound · propext   UNCHANGED  PASS  361          24.8527
```
- Every cell: export 865290f21637 (ADDENDUM 5–6), client 2.1.259, served models `clean` (head only the condition's model; Sonnet's
  sidechains Sonnet; Opus spawned no sidechain), end tree clean (dirty 0). The `final $` column is the post-end meter (`ctl/post-end-1.tsv`
  col 5), the same instrument as block SS's `final_COST` (it includes the harness's own sandbox probe under the cell's slug).
- The hidden suite ran over a COPY of each cell's `solution.rs` with `tasks/systems-v3/Crc32/G/run_tests.sh` (runner sha16
  3f1d7e4497d86c0e, `cells.tsv`). The Lean half ran through the export's own `o37/o37_score.sh` in scoring mode: confined, all three
  use-time controls passed, every constant the module declares replayed through the kernel, the type checked as exactly `O37Spec.Statement`.
- **Spend: $109.04** over six cells (sum of the `final $` column). That is ABOVE the registration's expected band ($46.85–$93.69, §A8) and
  inside its worst case ($223.26). The anchor's ×1.5–3 for a new arm was an assumption, and it was low for Sonnet (§R2).

## §R2 · BESIDE THE COMPARISON CONDITION (§A2: Crc32 × greenfield × salt-diet × statement, the Verus cells whose statement is given)
```
                      Verus × statement (of record)                         Lean-aeneas (this pilot)
  claude-opus-5       st04crc3 · st05crc3 · st06crc3: suite PASS 6/6 each    3 of 3 PASS
                      median $6.25                                          $13.13 · $13.87 · $16.66 (median $13.87)
  claude-sonnet-5     clbscs01 · 02 · 03: suite PASS 6/6 each                3 of 3 PASS
                      $3.80 · $4.16 · $5.52 (median $4.16)                   $19.68 · $20.85 · $24.85 (median $20.85)
```
Sources: the Opus verdicts are `RESULT-statement-arm-verdicts-2026-09-09.tsv` (class PASS, 6/6), and the Opus median is
`RESULT-cost-tables-v3-2026-09-29.md` §$1 (greenfield statement-salt-diet). The Sonnet cells are `evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv`
(final_COST, PASS 6/6). Cells per condition: `CELLMAP-descriptive-tables-v2-2026-09-27.tsv`.
**Reading, sign only, n = 3 per condition (no rate, no p-value, §A9):** both arms passed every cell at both models. The Lean arm cost more in
every pairing, by about 2× at the Opus median and about 5× at the Sonnet median. Both arms ran on one problem.

## §R3 · WHAT THE CELLS DID (from the cells, not interpreted beyond them)
- **Every subject stayed inside Aeneas's modelled subset**, so no Lean half failed at translation. The subjects wrote table-driven CRC-32s
  (the landing message of clbeca01 says so in its own words). Whether a subject's code can fall outside the subset (plan §A7) is
  UNMEASURED here: none did.
- **RED before GREEN, where watched live:** clbeca01, clbwca01 and clbeca02 each read RED on the skeleton (`sorryAx`) before their first
  GREEN, and some later read RED again before GREEN (the verdict lines, read live from the transcripts). For the last three cells the live
  watch emitted only end markers, so their sequence is not stated here. Why a subject went RED is not inferred.
- **The containment and the fence.** The scoring runs met no confinement event: all three use-time controls passed and every Lean half was
  GREEN. In the cells, the fence's hooks REFUSED 27 attempts, which therefore never ran: 7 in the Opus root and 20 in the Sonnet root, read
  from both roots' `_audit/fence.log` + `deny.log`, counting BLOCK lines. By class: writes to a scratch path under `/tmp` (SCRATCH);
  absolute-path commands, mostly a `cd` into the cell's OWN `.seat/tmp` (ESCAPE); one `find /` for files named o37 (NAMES); the client's
  memory write outside the fence (FENCE-OUTSIDE). **A refused command is not an escape, so the helm's VOID-and-halt stop (ADDENDUM 4 item 2)
  did not fire.** ⚠️ The own-cell ESCAPE refusals look like a harness FALSE POSITIVE (the hook's own-cell neutralising missed that `cd`
  form). It is routed to systems as a finding. It is not scored, and it applied in every cell whose subject wrote that form.

## §R4 · THE SEPARATE ROW (§A6): CLOSED BEFORE THE FIRE
`harness/systems-v3/o37/GF2.lean` proves the transcribed spec equal to an independent GF(2)[x] remainder definition for every message,
kernel-only (ADDENDUM 1 item 4; kent judged it independent, 2026-09-30 11:58:32). It is never part of the head-to-head.

## §R5 · WHAT THIS CANNOT ESTABLISH (carried from §A9, plus what the run showed)
- One problem, n = 3 per model: nothing about Lean vs SMT in general, and no rate.
- The suite is 6 tests (`G/run_tests.sh`), the same suite for both arms. The Lean theorem is a strictly stronger claim about the code than the
  suite, and a stronger claim than a passing suite. It is stated beside the PASS, never counted as more passes.
- §A2's five departures are real. Departure 2 (the Verus statement cells were told to refute and ratify; the Lean cells were not) moves COST
  toward the Verus arm, which makes the measured Lean premium, if anything, an UNDER-statement on that axis alone.
- "One trust base with x86lean" is not met (Lean 4.31 here); the claim is "kernel-checked in Lean 4.31".
- The Seatbelt profile as a boundary is unreviewed (desk ZE). The pilot's subjects are our own models on our own box.
- Nothing here makes a claim about the salt method.

## §R6 · kent's non-author read (2026-09-30 18:33:01), TAKEN; §§R1–R5 above are not edited
1. **The Opus comparison is a different instrument from the Lean cells' meter.** The $6.25 is `RESULT-cost-tables-v3-2026-09-29.md` §$1, the
   median over `claude-cost-raw.tsv`'s st04 · st05 · st06crc3 ($8.5561 · $5.6526 · $6.2530). Those are 09-09 cells priced by the cost-table pipeline,
   and whether a sandbox probe ran under their slug is not established. If none did, the Lean side carries a probe the Verus side lacks. That cost
   is ≈ $0.07–$0.29 per cell (block SS's header), so it could OVERSTATE the Lean premium by at most ≈ 0.05× on 2.22×. "About 2×" stands.
   (Sonnet is like for like: block SS's final_COST is the same cell_meter, probe included.)
2. **st04crc3 is VOID(UNDERSTATED), a FLOOR (≥ $8.56)**, as the cost table marks it. The Opus median of {≥ 8.56, 5.65, 6.25} is $6.25 whatever the
   floor's true value, so the figure is robust. It is still a floor, and it is said here.
3. **§R5's departure claim widens:** departures 1, 4 and 5 also add work only the Verus subjects did (writing the statement into solution.rs,
   carrying mutant traces, the trace predicate's reach). No listed departure points the other way. ⇒ **every listed departure that moves cost moves it
   toward the Verus arm**, so on the listed departures the measured Lean premium is, if anything, an under-statement.
4. kent could not reach §R3's fence count from his box (the audit logs are on the run box). It is bench's measurement, NOT a non-author check.
