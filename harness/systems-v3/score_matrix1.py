#!/usr/bin/env python3
"""score_matrix1.py — read matrix #1's registered verdicts off the ARCHIVE, mechanically.

WRITTEN WHILE THE RUN IS STILL FIRING, which is the whole point: arithmetic done after seeing a
number is arithmetic done with a thumb on it.  Every rule here is fixed in
PREREGISTRATION-matrix-opus-1-2026-09-08.md and this file is its executable form.

WHAT IT REFUSES TO DO
  * It keys the condition on ALL THREE fields (task, arm, card_extras) -- section 15.  A scorer
    keying on `arm` alone pools diet-bare with diet-stmt and would collapse four arms into two.
  * It REFUSES a cell whose card_extras is unreadable rather than defaulting it to `none`, because
    the default silently re-creates exactly that pooling.
  * It never converts T to a price and never reads a live METER tick: COST comes from the harvested
    METER.txt only (SS23(e)).
  * ⛔ IT READS A DECLARED SET, NEVER A GLOB OVER THE ARCHIVE.  The first draft searched every harvest
    dir and both cell roots, and on PARTIAL data it silently pooled matrix #1 with stage 1, with the
    five-cell pricing set, with the DROPPED hint arms, and with the VOID cell 57729c86.  The condition
    key (task, arm, card_extras) is correct and was not enough: cells from DIFFERENT RUNS share it.
    ⇒ THE RUN IS THE FOURTH FIELD, and it cannot be read off a cell -- it must be DECLARED.
  * It reports the SIGN TEST as the primary reading and prints `4-of-5 is NOT a result` as a
    registered fact, not a caveat discovered afterwards.
"""
import os, re, sys, math, json, statistics

HARVEST = os.path.expanduser("~/harvest-v3")          # the archive, per SS23(e)
K_POWER = 7.8489                                       # (z.025+z.20)^2, precise quantiles

def cost_of(meter):
    hits = [l for l in open(meter, encoding="utf-8", errors="replace")
            if l.startswith("COST ") and not l.lstrip().startswith("#")]
    if len(hits) != 1:
        return None, "METER has %d COST lines and a price must be unambiguous" % len(hits)
    # SS23(e) + the 59c93bbe VOID.  A VOID meter carries exactly ONE COST line, so the
    # unambiguity check above PASSES it -- and that line reads
    #   COST VOID(UNPRICED)  partial over the priced records $0.00  COST_head $0.00 ...
    # so an UNANCHORED search returns 0.00 and prices a cell that never booted at ZERO.
    # A zero in the plain arm INFLATES the salt premium: the defect fails in the
    # direction that flatters the headline, which is the direction that gets published.
    # Anchor on the FIRST field after COST and refuse anything that is not a bare price.
    m = re.match(r"COST\s+\$([0-9]+\.[0-9]+)(\s|$)", hits[0])
    if m:
        return float(m.group(1)), None
    return None, ("COST line does not open with a bare price -- refusing rather than "
                  "scanning on (a VOID meter carries $0.00 in its prose): %s"
                  % hits[0].split("  ")[0].strip())

def condition_of(celldir):
    """(task, arm, card_extras) -- all three, read from the cell's own ctl.  REFUSES on absence."""
    def rd(f):
        p = os.path.join(celldir, "ctl", f)
        if not os.path.exists(p): return None
        return open(p, encoding="utf-8", errors="replace").readline().strip()
    task = (rd("task") or "").split("\t")[0].strip()
    arm, extras = rd("arm"), rd("card_extras")
    if not task or not arm:
        return None, "task or arm unreadable"
    if extras is None or extras == "":
        return None, ("card_extras is UNREADABLE -- refusing rather than defaulting to 'none', "
                      "because the default pools the bare and statement arms (SS15)")
    return (task, arm, extras), None

def pooled_logsd(groups):
    num = den = 0.0
    for v in groups:
        if len(v) < 2: continue
        ls = [math.log(x) for x in v]; sd = statistics.stdev(ls)
        num += (len(ls)-1)*sd*sd; den += len(ls)-1
    return math.sqrt(num/den) if den else None

def floor_at(logsd, n, k=K_POWER):
    if logsd is None or n is None or n < 2: return None
    return math.exp(logsd*math.sqrt(2.0*k/float(n)))

def sign_test(k_pos, k_tot):
    """P(at least k_pos of k_tot on one side | H0) -- the registered primary reading."""
    def comb(n, r):
        c = 1
        for i in range(r): c = c*(n-i)//(i+1)
        return c
    return sum(comb(k_tot, i) for i in range(k_pos, k_tot+1)) / float(2**k_tot)

# ── THE DECLARED SET.  Matrix #1 is the cells in MATRIX_ROOT, plus the three SMOKE cells named in
#    SS12, plus the AMENDMENT 26 top-up root, and nothing else.  A glob over the archive is not a
#    set: it pools other runs.  A SECOND NAMED ROOT IS STILL A SET.
MATRIX_ROOT = os.path.expanduser("~/cells-matrix1")
TOPUP_ROOT  = os.path.expanduser("~/cells-n3-topup")     # AMENDMENT 26 -- the n=3 top-up cells
# ── THE STATEMENT-ARM ROOTS (AMENDMENT statement-arm-pilot 2026-09-09, addenda 1-2).  A LIST, because
#    the arm fires in waves and the fence law forbids building a second wave while the first runs: each
#    wave gets a FRESH root, so the declared set names roots, not one root.
#    ⛔ ADDING A ROOT HERE IS AN AMENDMENT ACT, NOT A CONVENIENCE.  The build script's own closing note
#    is the reason this exists: "cells in this fresh root are invisible to the scorer until the
#    amendment declares this root in ... Without that, these cells will run, cost money, and score
#    nowhere."  They ran tonight; this is the half that makes them count.
STMT_ROOTS = [os.path.expanduser("~/cells-stmt-2026-09-09"),      # wave 1: Crc32 + LRU, export aaf570e
              os.path.expanduser("~/cells-stmt-free-2026-09-09")]  # wave 2: FreeList, export 311b208
SMOKE = {"ae304f63": "~/cells", "a69e9131": "~/cells", "b7537006": "~/cells"}   # SS12

def declared_set(include_smoke):
    """The declared set, with the SMOKE cells IN or OUT.

    ⛔⛔ THE SWITCH IS THE WHOLE POINT AND IT WAS REGISTERED BEFORE EITHER READING EXISTED.
    Three of matrix #1's five problems reach n=3 in the plain-bare arm ONLY by counting one SS12
    smoke cell each -- cells built for a different purpose, in a different root, in a different
    RUN.  This file's own law is that THE RUN IS THE FOURTH FIELD and cannot be read off a cell.
    So the headline was resting on a pooling this file declares but the scoreboard never showed.
    The AMENDMENT 26 top-up fires one plain cell per affected problem so those three reach n=3
    INSIDE their own run.  It does NOT remove the smoke cells: with the top-up in and the smoke
    also in, those conditions read n=4, and the dependency is diluted rather than discharged --
    which is harder to see, not easier.  ⇒ BOTH READINGS ARE COMPUTED AND BOTH ARE PRINTED.
    """
    declared = {}
    for root in [MATRIX_ROOT, TOPUP_ROOT] + STMT_ROOTS:
        if not os.path.isdir(root): continue
        for cid in sorted(os.listdir(root)):
            c = os.path.join(root, cid)
            # ⛔ FILTER ON STRUCTURE, NEVER ON NAME.  This read `cid != "_bin"` plus an
            # isdir(ctl) test: it excluded ONE non-cell by name and admitted any other
            # directory that happened to carry a ctl/.  `_audit` appears in this root
            # mid-run and has bitten two other tools of mine by exactly that route.
            # A cell is a directory with ctl/arm.  Nothing else is, whatever it is called.
            if os.path.exists(os.path.join(c, "ctl", "arm")): declared[cid] = c
    if include_smoke:
        for cid, root in SMOKE.items():
            c = os.path.join(os.path.expanduser(root), cid)
            if os.path.isdir(os.path.join(c, "ctl")): declared[cid] = c
    return declared

def _census(declared):
    """Count each root SEPARATELY.  ⛔ The receipt line used to say 'in the matrix root' for cells
    that are not in it: a census that misattributes its own population is worse than none."""
    n_smoke = sum(1 for k in SMOKE if k in declared)
    n_top   = sum(1 for k, v in declared.items() if v.startswith(TOPUP_ROOT + os.sep))
    n_stmt  = sum(1 for k, v in declared.items()
                  if any(v.startswith(r + os.sep) for r in STMT_ROOTS))
    return len(declared) - n_smoke - n_top - n_stmt, n_top, n_smoke, n_stmt

def score(declared, title):
    print("=" * 78)
    print(title)
    m, t, k, st = _census(declared)
    print("declared set: %d cells (%d matrix root + %d top-up AMENDMENT 26 + %d smoke SS12"
          " + %d statement-arm)\n" % (len(declared), m, t, k, st))

    cells, refused, reached_back = {}, [], []
    for cid, cell in sorted(declared.items()):
        hv = sorted(d for d in os.listdir(HARVEST) if d.startswith(cid + "-"))
        if not hv: continue                      # not harvested yet — silently pending, not refused
        # ⛔⛔ THE LATEST HARVEST THAT PARSES AS A PRICE, NOT SIMPLY THE LATEST HARVEST.
        # This read hv[-1] — the lexicographically last dir — and a cell can hold more than one
        # harvest.  On 2026-09-09 two LANDED, fully priced cells were harvested against the wrong
        # account first and wrote VOID(UNMETERED); both were re-harvested and recovered, and they
        # scored correctly ONLY because the good harvest happened to sort second.  Had the VOID
        # sorted last, this scorer would have refused a cell that has a perfectly good price one
        # directory away — dropping it from its condition and moving that problem's median.
        # ⇒ A SELECTOR THAT PICKS BY NAME IS CORRECT ONLY WHILE THE NAMES HAPPEN TO ORDER THE WAY
        #   THE CONTENT DOES.  Reported by systems, who hit the near-miss.
        # ⚠️ Reaching PAST the newest harvest is disclosed, never silent: an older price is still a
        # price, but the reader must be told the newest one did not parse.
        cond, err = condition_of(cell)
        if err: refused.append((cid, err)); continue
        cost, cerr, used, tried = None, None, None, 0
        for d in reversed(hv):
            m = os.path.join(HARVEST, d, "METER.txt")
            tried += 1
            if not os.path.exists(m):
                cerr = "harvest has no METER.txt"; continue
            c, e = cost_of(m)
            if e is None:
                cost, cerr, used = c, None, d; break
            cerr = e
        if cost is None:
            refused.append((cid, "%s (examined %d harvest(s), none priced)" % (cerr, tried))); continue
        if used != hv[-1]:
            reached_back.append((cid, used, hv[-1]))
        cells.setdefault(cond, []).append((cid, cost))

    print("MATRIX #1 — read from the ARCHIVE, keyed on (task, arm, card_extras)\n")
    if refused:
        print("REFUSED (never defaulted):")
        for cid, why in refused: print("  %-10s %s" % (cid, why))
        print()
    if reached_back:
        print("⛔ PRICED FROM AN EARLIER HARVEST (the newest did not parse as a bare price):")
        for cid, used, newest in reached_back:
            print("  %-10s used %s   newest %s" % (cid, used, newest))
        print("  Each of these had a later harvest that is VOID or unparseable. The price is real")
        print("  and the reach-back is disclosed rather than silent.\n")
    print("%-9s %-10s %-10s %5s  %s" % ("task", "arm", "extras", "n", "cells"))
    med = {}
    for cond in sorted(cells):
        v = [c for _, c in cells[cond]]
        shown = " ".join("$%.2f" % x for x in v)
        if len(v) >= 3: med[cond] = statistics.median(v)
        print("%-9s %-10s %-10s %5d  %s%s" % (cond[0], cond[1], cond[2], len(v), shown,
              "" if len(v) >= 3 else "   <- below n=3, no median taken"))

    groups = [[c for _, c in v] for k, v in cells.items() if len(v) >= 3]
    # ⛔⛔ THE FLOOR IS REGISTERED, NOT FITTED TO THIS RUN.  This computed the pooled
    # sd from matrix #1's OWN cells and gated G2 on the result.  The pre-registration
    # (line 36, and line 101 on provenance) registers the floor as 2.0072x from
    # sd(ln cost)=0.30458, measured on STAGE 1 at client 2.1.259; SS18 authorises
    # recomputing the arithmetic at the n ACTUALLY ACHIEVED -- a different n, never a
    # different sigma.  Fitting sigma to this run gave 0.1082 and a floor of 1.2808x:
    # a materially WEAKER gate than the one registered, and weaker in the direction
    # that flatters the hypothesis under test.  Caught while blind to the outcome, which
    # is the only honest moment to touch a gate.
    REGISTERED_LOGSD = 0.30458          # stage 1, client 2.1.259 -- the registered sigma
    sd_run = pooled_logsd(groups)       # REPORTED as information; NEVER gates
    n_min  = min((len(g) for g in groups), default=None)
    sd = REGISTERED_LOGSD
    fl = floor_at(REGISTERED_LOGSD, n_min)
    print("   (run's OWN pooled sd(ln cost) = %s -- REPORTED ONLY, it gates nothing;\n"
          "    substituting it would refit the registered gate to the data it judges)"
          % (("%.4f" % sd_run) if sd_run is not None else "n/a"))
    print("\nG3 PROVENANCE  REGISTERED sd(ln cost)=%s  n=%s  k=%.4f  resolvable floor=%s"
          % ("%.4f" % sd if sd else "--", n_min, K_POWER, "%.4fx" % fl if fl else "--"))

    print("\nPRIMARY READING — THE CROSS-PROBLEM SIGN TEST (registered before cell 1)")
    prem = {}
    for (t, a, e) in list(med):
        if a == "salt-diet" and e == "none":
            q = med.get((t, "plain", "none"))
            if q: prem[t] = med[(t, a, e)] / q
    verdict = None
    if prem:
        pos = sum(1 for v in prem.values() if v > 1.0); tot = len(prem)
        p = sign_test(pos, tot)
        verdict = (pos, tot, p, dict(prem))
        for t in sorted(prem): print("  %-9s premium %.4fx  %s" % (t, prem[t], "above 1" if prem[t] > 1 else "BELOW 1"))
        print("  %d of %d problems show a premium > 1   p = %.4f   -> %s"
              % (pos, tot, p, "SIGNIFICANT" if p <= 0.05 else "NOT a result"))
        if tot == 5 and pos == 4:
            print("  ** 4-of-5 is p=0.1875 and was registered IN ADVANCE as NOT a positive result. **")
        if fl:
            # ⛔⛔ STATE THE FACT AND THE RULE SEPARATELY. This printed "at least one premium is
            # BELOW the floor -> every per-problem MAGNITUDE is UNRESOLVED", which reads as a claim
            # about EVERY problem and is one. The paper took it at its word: the abstract at
            # origin/main said "every per-problem magnitude falls below the resolvable floor" while
            # its own body table showed TWO of five clearing it. Caught by `paper`, 2026-09-09.
            # ⇒ A REPORTING RULE WRITTEN IN THE LANGUAGE OF A MEASUREMENT WILL BE QUOTED AS ONE.
            below = sorted(t for t, v in prem.items() if v < fl)
            clear = sorted(t for t, v in prem.items() if v >= fl)
            print("  G2 FLOOR %.4fx at n=%s -- PER PROBLEM (SS14: the floor is per-problem and n is not uniform)" % (fl, n_min))
            print("      BELOW  (magnitude UNRESOLVED) : %s" % (", ".join(below) or "none"))
            print("      CLEARS (magnitude resolvable) : %s" % (", ".join(clear) or "none"))
            if below:
                print("      => THE REGISTERED HEADLINE IS THE SIGN ACROSS PROBLEMS, NOT A RATIO.")
                print("         This is a REPORTING RULE. It is NOT a claim that every magnitude")
                print("         fell below: %d of %d premium(s) DO clear the floor, and any prose"
                      % (len(clear), len(prem)))
                print("         saying otherwise contradicts this table.")
    else:
        print("  not readable yet — needs plain-bare and diet-bare at n=3 on at least one problem")

    print("\nTHE GOLD PAIR — (d) plain+statement vs (e) diet+statement")
    gold = {}
    for (t, a, e) in list(med):
        if a == "salt-diet" and e == "statement":
            q = med.get((t, "plain", "statement"))
            if q: gold[t] = med[(t, a, e)] / q
    if gold:
        pos = sum(1 for v in gold.values() if v > 1.0); tot = len(gold)
        for t in sorted(gold): print("  %-9s %.4fx" % (t, gold[t]))
        print("  %d of %d  p = %.4f  -> %s" % (pos, tot, sign_test(pos, tot),
              "SIGNIFICANT" if sign_test(pos, tot) <= 0.05 else "NO VERDICT at this k"))
        if tot < 5:
            print("  ** k=%d: the statement arm exists on %d problem(s). Four cards lack a `## Statement`" % (tot, tot))
            print("     section (SS16), so this pair CANNOT reach .05 and is reported without a verdict. **")
    else:
        print("  no statement-arm pair at n=3 yet")
    return verdict


def main():
    if not os.path.isdir(HARVEST):
        print("no archive at %s" % HARVEST); return 2

    a = score(declared_set(True),
              "READING A -- THE CONTINUITY READING: matrix root + top-up + the SS12 smoke cells")
    print()
    b = score(declared_set(False),
              "READING B -- SMOKE OUT: matrix root + top-up ONLY, every cell from this run")

    # ⛔⛔ THE COMPARISON IS THE POINT, AND IT IS REPORTED WHICHEVER WAY IT COMES OUT.
    # Registered before either reading existed, so this is a pre-committed comparison and not a
    # choice made after seeing two numbers.  If B agrees with A, the headline does not depend on
    # the borrowed cells and the published disclosure is discharged BY MEASUREMENT.  If B differs,
    # THE DIFFERENCE IS THE RESULT and it outranks the headline.  There is no third branch here on
    # purpose: a scorer that reports one reading when they agree and two when they do not has made
    # the disagreement invisible in exactly the case that matters.
    print("\n" + "=" * 78)
    print("A vs B -- DOES THE HEADLINE DEPEND ON THE BORROWED SMOKE CELLS?")
    if a is None or b is None:
        print("  NOT YET READABLE: one reading has no problem at n=3 in both bare arms.")
        print("  ⛔ This is NOT 'no dependency'. Report the disclosure verbatim until both read.")
        return 0
    (pa, ta, ppa, _), (pb, tb, ppb, _) = a, b
    print("  A: %d of %d   p = %.4f        B: %d of %d   p = %.4f" % (pa, ta, ppa, pb, tb, ppb))
    if (pa, ta) == (pb, tb):
        print("  ⇒ IDENTICAL SIGN VERDICT WITHOUT THE BORROWED CELLS.")
        print("     The published smoke-cell dependency is DISCHARGED. Report both readings anyway:")
        print("     the reader cannot reconstruct the set from a single number.")
    else:
        print("  ⇒ ⛔⛔ THE READINGS DISAGREE. THE DISAGREEMENT IS THE RESULT AND OUTRANKS THE")
        print("     HEADLINE. The 5-of-5 figure rests on cells built as a smoke, in another root,")
        print("     for another purpose. Do not publish A without B beside it.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
