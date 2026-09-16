#!/usr/bin/env python3
"""ol_lower_bound_margins.py -- which cell prices printed in the paper are LOWER BOUNDS, and how far each
registered verdict sits from them. Zero spend: reads harvested METER.txt and RECORDS.tsv files only.

usage: ol_lower_bound_margins.py <paper.tex> <harvest-view> [<label for the tex blob>]

  <paper.tex>     paper/saltbench-v1.tex. Its appendix price table is PARSED, never retyped: every row
                  "<problem> & <arm> & \\$x \\$y ..." is a condition, and an \\underline{} price is a borrowed
                  smoke cell (the paper's own definition of reading B).
  <harvest-view>  a view of the harvest archive built by harvest_view_asof.sh. The receipt of record cuts it
                  at the commit that last changed the tex (aee2fa5, 2026-09-10T04:06:48Z): every price the
                  paper prints had been harvested by then, and the whole archive is NOT usable because a
                  later re-harvest can carry the same price as a published one (it does: $11.19).

WHAT IT MEASURES
  1. Each printed price is matched to the ONE harvest in the view whose METER.txt COST equals it and whose
     RECORDS.tsv costs sum to it. Zero or several matches REFUSE (rc 3): a price naming no unique record
     is not a datum.
  2. A cell is a LOWER BOUND by TWO methods, which must agree or it REFUSES (rc 4):
       (a) its METER.txt declares "LOWER BOUND";
       (b) its RECORDS.tsv carries a record whose stop_reason is null -- an interrupted turn.
  3. For each lower-bound cell: the RECORDED cost of its interrupted records as a share of the cell's cost.
     THIS IS NOT A BOUND ON THE UNDERSTATEMENT. The client stops writing usage where the interrupt lands,
     so what is recorded of an interrupted turn is known and what is missing from it is not measured by
     anything here. The share says where the understatement lives and how large the recorded part is.
  4. Per group, reading and problem: the arm medians, the premium (diet median / plain median, as the paper
     computes it), which arm's MEDIAN rests on a lower-bound cell (the direction of the bias), and the
     MARGIN to each registered threshold the premium could cross:
       plain side -> premium falls: to 1.0x (a sign), and to the 2.0072x floor if the premium clears it;
       diet side  -> premium rises: to 1.0x if the premium is below it, and to the floor if below it.
     Each margin is printed two ways: 'uplift' = the same relative rise on every lower-bound cell of that
     arm; 'k' = the unrecorded remainder of every interrupted turn in that arm as a multiple of its
     recorded cost. 'none' = that arm's lower-bound cells alone cannot reach the threshold.
"""
import csv, glob, os, re, statistics, sys

FLOOR = 2.0072     # the resolvable floor at n=3 the paper states (score_matrix1.py G3 line)

HOME = os.path.expanduser("~")

def tilde(path):
    return "~" + path[len(HOME):] if path.startswith(HOME) else path

def die(rc, msg):
    print("REFUSE: " + msg); sys.exit(rc)

if len(sys.argv) < 3:
    die(2, "usage: ol_lower_bound_margins.py <paper.tex> <harvest-view> [<label>]")
tex, view = sys.argv[1], sys.argv[2]
label = sys.argv[3] if len(sys.argv) > 3 else "(unlabelled)"

# ---- 1. parse the paper's appendix price table ---------------------------------------------------------
ROW = re.compile(r"^(Crc32|FreeList|LRU|LZW|Paxos) & (plain|diet)-(bare|statement) & (.*?)\\\\\s*$")
table = []
for ln, line in enumerate(open(tex), 1):
    m = ROW.match(line)
    if not m:
        continue
    task, arm, extras, body = m.group(1), m.group(2), m.group(3), m.group(4)
    for tok in re.findall(r"\\underline\{\\\$([0-9]+\.[0-9]{2})\}|\\\$([0-9]+\.[0-9]{2})", body):
        table.append(dict(line=ln, task=task, arm=arm, extras=extras, p=tok[0] or tok[1], smoke=bool(tok[0])))
if not table:
    die(3, "no appendix price rows found in " + tex)
print("source   %s  (%s)  appendix rows: %d conditions, %d printed prices, %d underlined (smoke)"
      % (os.path.basename(tex), label, len({(c["task"], c["arm"], c["extras"]) for c in table}), len(table),
         sum(c["smoke"] for c in table)))

# ---- 2. match each price to one harvest; classify it twice --------------------------------------------
bycost = {}
nmeter = 0
for d in sorted(glob.glob(os.path.join(view, "*/"))):
    mp = os.path.join(d, "METER.txt")
    if not os.path.exists(mp):
        continue
    nmeter += 1
    mc = re.search(r"^\s*COST \$([0-9.]+)", open(mp).read(), re.M)
    if mc:
        bycost.setdefault(mc.group(1), []).append(d.rstrip("/"))
print("view     %s  harvests with METER.txt: %d" % (tilde(view), nmeter))

cells = []
for c in table:
    hits = bycost.get(c["p"], [])
    if len(hits) != 1:
        die(3, "tex line %d: $%s (%s %s %s) matches %d harvests: %s" % (c["line"], c["p"], c["task"], c["arm"], c["extras"], len(hits), [os.path.basename(x) for x in hits]))
    h = hits[0]
    lb_meter = bool(re.search(r"lower bound", open(os.path.join(h, "METER.txt")).read(), re.I))
    rows = list(csv.DictReader(open(os.path.join(h, "RECORDS.tsv")), delimiter="\t"))
    if not rows or "stop_reason" not in rows[0] or "cost_usd" not in rows[0]:
        die(4, "RECORDS.tsv of %s lacks stop_reason/cost_usd" % os.path.basename(h))
    null = [r for r in rows if r["stop_reason"].strip().lower() in ("", "null", "none")]
    if lb_meter != (len(null) > 0):
        die(4, "%s: METER lower-bound=%s but RECORDS.tsv interrupted records=%d" % (os.path.basename(h), lb_meter, len(null)))
    cost_all = sum(float(r["cost_usd"]) for r in rows)
    if abs(cost_all - float(c["p"])) > 0.01:
        die(4, "%s: RECORDS.tsv sums to $%.4f, the paper prints $%s" % (os.path.basename(h), cost_all, c["p"]))
    null_cost = sum(float(r["cost_usd"]) for r in null)
    c.update(price=float(c["p"]), harvest=os.path.basename(h), lb=lb_meter, nnull=len(null),
             null_cost=null_cost, share=100.0 * null_cost / cost_all)
    cells.append(c)
if len({c["harvest"] for c in cells}) != len(cells):
    die(3, "two printed prices resolved to the same harvest")
print("matched  %d of %d printed prices to exactly one harvest, all distinct; the two lower-bound methods agree on %d of %d"
      % (len(cells), len(table), len(cells), len(cells)))

# ---- 3 + 4 ------------------------------------------------------------------------------------------------
def lifted(xs, u, form):
    return [(c["price"] * (1 + u) if form == "uplift" else c["price"] + u * c["null_cost"]) if c["lb"] else c["price"]
            for c in xs]

def prem(plain, diet, u, form, side):
    pl = lifted(plain, u, form) if side == "plain" else [c["price"] for c in plain]
    dt = lifted(diet, u, form) if side == "diet" else [c["price"] for c in diet]
    return statistics.median(dt) / statistics.median(pl)

def margin(plain, diet, target, form, side):
    big = 1000.0 if form == "uplift" else 1.0e7
    if side == "plain":
        reached = lambda u: prem(plain, diet, u, form, side) <= target
    else:
        reached = lambda u: prem(plain, diet, u, form, side) >= target
    if reached(0.0):
        return "already"
    if not reached(big):
        return "none"
    lo, hi = 0.0, big
    for _ in range(300):
        mid = (lo + hi) / 2
        if reached(mid): hi = mid
        else: lo = mid
    return ("+%.1f%%" % (100 * hi)) if form == "uplift" else ("%.0fx" % hi)

def both(plain, diet, target, side):
    return "%s | %s" % (margin(plain, diet, target, "uplift", side), margin(plain, diet, target, "factor", side))

def median_rests_on_bound(xs):
    s = sorted(xs, key=lambda c: c["price"]); n = len(s)
    mid = [s[n // 2]] if n % 2 else [s[n // 2 - 1], s[n // 2]]
    return any(c["lb"] for c in mid)

GROUPS = (("BARE MATRIX (the scoreboard; sign test over 5 problems)", "bare"),
          ("STATEMENT ARM (the paired reading at k=4, plus LZW from the matrix)", "statement"))
for gname, extras in GROUPS:
    has_smoke = any(c["smoke"] for c in cells if c["extras"] == extras)
    for rname, keep in (("A", lambda c: True), ("B", lambda c: not c["smoke"])):
        if rname == "B" and not has_smoke:
            continue
        pop = [c for c in cells if c["extras"] == extras and keep(c)]
        lbs = [c for c in pop if c["lb"]]
        print()
        print("%s -- READING %s%s" % (gname, rname, "" if has_smoke else " (no underlined cell in this group, so A = B)"))
        print("  printed prices %d  lower bounds %d  (plain %d, diet %d)" % (
            len(pop), len(lbs), sum(c["arm"] == "plain" for c in lbs), sum(c["arm"] == "diet" for c in lbs)))
        for c in lbs:
            print("  LB  %-8s %-5s $%6.2f  %-28s tex:%d  interrupted records %d  recorded share of cost %.4f%%"
                  % (c["task"], c["arm"], c["price"], c["harvest"], c["line"], c["nnull"], c["share"]))
        if lbs:
            print("  recorded share of cost over these %d cells: min %.4f%%  max %.4f%%"
                  % (len(lbs), min(c["share"] for c in lbs), max(c["share"] for c in lbs)))
        print("  %-8s %4s %4s  %-9s %-9s %-8s %-6s %-20s %-20s %-20s %-20s" % (
            "problem", "n_pl", "n_dt", "plain_med", "diet_med", "premium", "medLB",
            "plain side to 1.0x", "plain side to floor", "diet side to 1.0x", "diet side to floor"))
        for task in sorted({c["task"] for c in pop}):
            plain = [c for c in pop if c["task"] == task and c["arm"] == "plain"]
            diet = [c for c in pop if c["task"] == task and c["arm"] == "diet"]
            if not plain or not diet:
                continue
            pmed = statistics.median([c["price"] for c in plain]); dmed = statistics.median([c["price"] for c in diet])
            pr = dmed / pmed
            mb = {(False, False): "--", (True, False): "plain", (False, True): "diet", (True, True): "both"}[
                (median_rests_on_bound(plain), median_rests_on_bound(diet))]
            print("  %-8s %4d %4d  $%-8.2f $%-8.2f %.4fx %-6s %-20s %-20s %-20s %-20s" % (
                task, len(plain), len(diet), pmed, dmed, pr, mb,
                both(plain, diet, 1.0, "plain") if pr > 1.0 else "-",
                both(plain, diet, FLOOR, "plain") if pr > FLOOR else "-",
                both(plain, diet, 1.0, "diet") if pr < 1.0 else "-",
                both(plain, diet, FLOOR, "diet") if pr < FLOOR else "-"))

lbs = [c for c in cells if c["lb"]]
print()
print("ALL PRINTED PRICES  %d  lower bounds %d  (plain %d, diet %d)  recorded share of cost over them: min %.4f%%  max %.4f%%"
      % (len(cells), len(lbs), sum(c["arm"] == "plain" for c in lbs), sum(c["arm"] == "diet" for c in lbs),
         min(c["share"] for c in lbs), max(c["share"] for c in lbs)))
