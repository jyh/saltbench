# BROWNFIELD-BRIEFING-DIFF.md — §B2's N3, published BEFORE the run

⛔ **§5 of the design: an audit is a DIFF, never a reading.** This file is the greenfield→brownfield
briefing delta, per arm, taken from cells built at MATCHED NONCES so the only differences are the ones
the field introduces.

## ⇒ THE PROPERTY THAT MATTERS, AND IT HOLDS FOR BOTH ARMS
**Each arm's METHOD FILE (`CLAUDE.md`) is BYTE-IDENTICAL between greenfield and brownfield.**
⛔ This is §B2's sharpest hazard made checkable: *the treatment's content substantially IS advice about how
to approach code you did not write*, so a brownfield field that altered either arm's briefing would be
adding treatment and calling it a field. **It does not.**

## THE DELTA, per arm (LZW, nonces matched)
```
  plain    files differing: REQUIREMENTS.md, solution.rs      REQUIREMENTS.md  +9 / -0     CLAUDE.md IDENTICAL
  salt     files differing: REQUIREMENTS.md, solution.rs      REQUIREMENTS.md  +9 / -0     CLAUDE.md IDENTICAL
```
**Exactly two files differ in each arm, and the +9 is the same nine lines in both** — the card addendum.
`solution.rs` differs because that IS the field: greenfield gets the interface stubs, brownfield gets the seed.

## THE ADDED LINES, verbatim (identical in both arms)
```

## The component already exists

An implementation of this component is already present in `solution.rs`. It was written earlier, by
someone else, against the requirements above, and it builds.

It is yours to do with as you judge best: keep it, change it, or set it aside and start again. Nothing
about it is fixed except the interface, which is unchanged. The requirements above are what the work is
measured against, and they are exactly the same requirements whether or not that file had been there.
```
⛔ **It says an implementation EXISTS. It does not say it is WRONG** — that is what V1 measures, and a
briefing that pointed at the defect would measure nothing. It also carries **zero** terms from §B2's N2
neutrality list, checked with the pattern IMPORTED from `neutrality_grep.py`.

📌 **The diff is per-ARM and not per-TASK because the addendum is byte-identical across all four tasks** —
one text, so a per-task diff would be four copies of this one.
