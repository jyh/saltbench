#!/usr/bin/env python3
"""cell_tokens.py — the ⑯ reading for a Claude-lane cell: TOKENS FIRST, USD DERIVED, VOIDS DECLARED.

    cell_tokens.py <cell-dir> [<cell-dir> ...] --meter <path to cell_meter.py> [--raw-dir <dir>]
    cell_tokens.py --self-test

THE RULING IT IMPLEMENTS (council 2026-09-17 ⑯, the Captain: "what we really want is the token cost, borken
down if possible. Dollars are secondary"): per cell, tokens by ROLE and by DIRECTION and by PHASE where the
harness logs it; a VOID stays a DECLARED ABSENCE; USD is derived from tokens, never the reverse.

⛔ WHY THIS EXISTS RATHER THAN A CALL TO `clb_harvest.py` (AMENDMENT-claude-lane-B ADDENDUM 3 §A3.5(e)).
`clb_harvest.py` derives a cell's session slug from `CLB_CFG` -- the lane env, a MUTABLE key. When the lane
moves, it prints `VOID(UNMETERED) no session dir for this cell` for cells whose sessions are on the same box.
Measured 2026-09-17 on three landed cells: 3 of 3 VOID by that path, 3 of 3 metered from the cfg the cell
records for itself. ⇒ A CELL IS METERED FROM THE `cfg` ITS OWN `ctl/run-cfg.tsv` RECORDS, NEVER FROM THE
AMBIENT ENV. The cell also records `phase` there, which is ⑯'s phase dimension for free.

⛔ WHAT IT REFUSES, RATHER THAN PRINTING A ZERO. An absence here is a manufactured one -- the numbers exist
and the path was wrong -- so every failure NAMES the path it looked at and exits non-zero:
    rc 2  no ctl/run-cfg.tsv, or no `cfg` row in it        rc 3  the recorded cfg has no slug dir
    rc 4  the meter produced no RECEIPT rows               rc 5  the meter could not be run
A cell whose meter declares a VOID is still PRINTED -- the void rides with the numbers, verbatim, because
"unmetered is not zero" and "understated is not a price" are different claims and both must reach the reader.
"""
import argparse, os, re, subprocess, sys

RECEIPT = re.compile(
    r"^RECEIPT (?P<bucket>\S+) (?P<model>\S+) records (?P<records>\d+) input (?P<input>\d+) "
    r"cache_creation (?P<cc>\d+) \((?P<w5>\d+)/(?P<w1>\d+)\) cache_read (?P<cr>\d+) output (?P<output>\d+) T (?P<T>\d+)")
DIRS = ("input", "cache_write_5m", "cache_write_1h", "cache_read", "output")  # FIVE: cache_creation is TWO rates


def run_cfg(cell):
    """The cfg rows and phases the CELL records for itself. Returns ([cfg,...], [phase,...])."""
    p = os.path.join(cell, "ctl", "run-cfg.tsv")
    if not os.path.exists(p):
        return None, None
    cfgs, phases = [], []
    for line in open(p):
        f = line.rstrip("\n").split("\t")
        if len(f) >= 2 and f[0] == "cfg" and f[1] not in cfgs:
            cfgs.append(f[1])
        if len(f) >= 2 and f[0] == "phase" and f[1] not in phases:
            phases.append(f[1])
    return (cfgs or None), phases


def slug_of(cfg, cell):
    cfg = os.path.expanduser(cfg)
    return os.path.join(cfg, "projects", os.path.realpath(os.path.join(cell, "repo")).replace("/", "-"))


def meter_text(meter, slug, launches):
    try:
        r = subprocess.run([sys.executable, meter, slug, "--launches", str(launches)],
                           capture_output=True, text=True)
    except OSError as e:
        return None, "cannot run the meter %s: %s" % (meter, e)
    return (r.stdout or "") + (r.stderr or ""), None


def parse(text):
    rows, voids, limits = [], [], []
    for line in text.splitlines():
        m = RECEIPT.match(line)
        if m:
            d = m.groupdict()
            rows.append({k: (int(v) if k not in ("bucket", "model") else v) for k, v in d.items()})
        elif line.startswith("VOID("):
            voids.append(line)
        elif line.startswith("LIMITATION "):
            limits.append(line)
    return rows, voids, limits


def report(cell, cfgs, phases, rows, voids, limits, out):
    T = sum(r["T"] for r in rows)
    out("=== %s   phases recorded: %s   cfg rows recorded: %d" % (
        os.path.basename(cell.rstrip("/")), ",".join(phases) if phases else "NONE", len(cfgs)))
    for v in voids:
        out("    VOID (declared, carried verbatim): " + v)
    for l in limits:
        out("    " + l)
    out("    TOKENS BY ROLE AND DIRECTION (the price of record):")
    out("    %-6s %-18s %8s %10s %12s %10s %10s %13s %11s %13s %7s" % (
        "role", "model", "records", "input", "cache_crea", "  5m_wr", "  1h_wr", "cache_read", "output", "T", "share"))
    for r in sorted(rows, key=lambda r: (r["bucket"], r["model"])):
        out("    %-6s %-18s %8d %10d %12d %10d %10d %13d %11d %13d %6.1f%%" % (
            r["bucket"], r["model"], r["records"], r["input"], r["cc"], r["w5"], r["w1"], r["cr"], r["output"], r["T"],
            100.0 * r["T"] / T if T else 0.0))
    out("    %-6s %-18s %8d %10d %12d %10d %10d %13d %11d %13d %6.1f%%" % (
        "ALL", "-", sum(r["records"] for r in rows), sum(r["input"] for r in rows), sum(r["cc"] for r in rows),
        sum(r["w5"] for r in rows), sum(r["w1"] for r in rows),
        sum(r["cr"] for r in rows), sum(r["output"] for r in rows), T, 100.0 if T else 0.0))
    out("    ⛔ cache_creation IS TWO DIRECTIONS AT DIFFERENT RATES (5-minute write vs 1-hour write, 6.25 vs 10.00")
    out("       per M for this model's row). A merged cache_creation cannot be priced, and a price derived from")
    out("       one that is merged is a BRACKET, not a figure. The split is carried because ⑯ says BY DIRECTION.")
    by_role = {}
    for r in rows:
        by_role[r["bucket"]] = by_role.get(r["bucket"], 0) + r["T"]
    out("    ROLE SHARE OF T: " + " · ".join(
        "%s %.1f%%" % (b, 100.0 * t / T) for b, t in sorted(by_role.items())) if T else "    ROLE SHARE: T is 0")
    out("    ⛔ ROLE IS head/exec/wf, THE MECHANISM CLASS. worker/designer/reviewer DO NOT SEPARATE: the meter")
    out("       keys the exec bucket by SERVED MODEL, not by executor. That is ⑯'s declared absence, not a zero.")
    out("    USD: DERIVED FROM THE TOKENS ABOVE, SECONDARY BY RULING — read it off the meter's own COST lines,")
    out("       which price each direction at its own rate and say 'modelled at list rates, not an invoice'.")
    return T


def one(cell, meter, launches, raw_dir, out):
    cfgs, phases = run_cfg(cell)
    if not cfgs:
        out("REFUSE rc 2: %s has no ctl/run-cfg.tsv with a cfg row. The cell does not say where its sessions"
            " are, and the ambient env is NOT a substitute." % cell)
        return 2
    rows, voids, limits, looked = [], [], [], []
    for cfg in cfgs:
        slug = slug_of(cfg, cell)
        looked.append(slug)
        if not os.path.isdir(slug):
            continue
        text, err = meter_text(meter, slug, launches)
        if err:
            out("REFUSE rc 5: " + err)
            return 5
        if raw_dir:
            os.makedirs(raw_dir, exist_ok=True)
            with open(os.path.join(raw_dir, os.path.basename(cell.rstrip("/")) + ".meter.txt"), "w") as f:
                f.write(text)
        r, v, l = parse(text)
        rows += r; voids += v; limits += l
    if not any(os.path.isdir(s) for s in looked):
        out("REFUSE rc 3: no slug dir at any cfg THE CELL RECORDS. Looked at: %s. This is an absence of a PATH,"
            " never of tokens." % "; ".join(looked))
        return 3
    if not rows:
        out("REFUSE rc 4: the meter produced no RECEIPT rows for %s. Unmetered is not zero." % cell)
        return 4
    report(cell, cfgs, phases, rows, voids, limits, out)
    return 0


def self_test():
    import tempfile, textwrap
    ok = [True]
    def check(c, m):
        ok[0] = ok[0] and c
        print(("  PASS " if c else "  FAIL ") + m)
    lines = []
    out = lines.append
    with tempfile.TemporaryDirectory() as t:
        # a stub meter that prints whatever fixture it is pointed at
        stub = os.path.join(t, "stub_meter.py")
        fixture = os.path.join(t, "fixture.txt")
        open(stub, "w").write(textwrap.dedent("""\
            import sys
            sys.stdout.write(open(%r).read())
        """ % fixture))
        good = ("heads 1 sidechains 1 workflows 0 records 5 unparsable 0\n"
                "RECEIPT bucket model records input cache_creation(5m/1h) cache_read output T share_T COST share_COST\n"
                "RECEIPT head m1 records 3 input 10 cache_creation 100 (0/100) cache_read 1000 output 40 T 1150 70% COST $1 70%\n"
                "RECEIPT exec m1 records 2 input 5 cache_creation 50 (50/0) cache_read 400 output 30 T 485 30% COST $0.5 30%\n")
        def cell_at(name, cfgname, make_slug=True, with_cfg=True):
            c = os.path.join(t, name); os.makedirs(os.path.join(c, "ctl")); os.makedirs(os.path.join(c, "repo"))
            if with_cfg:
                open(os.path.join(c, "ctl", "run-cfg.tsv"), "w").write(
                    "cfg\t%s\nrun_at\t2026-09-17T00:00:00Z\nphase\t1\n" % os.path.join(t, cfgname))
            if make_slug:
                os.makedirs(slug_of(os.path.join(t, cfgname), c))
            return c

        # RED 1 — no run-cfg.tsv at all
        lines.clear(); c = cell_at("nocfg", "cfgA", make_slug=False, with_cfg=False)
        check(one(c, stub, 1, None, out) == 2 and any("rc 2" in l for l in lines), "RED no ctl/run-cfg.tsv -> rc 2, names the cell")
        # RED 2 — the cfg is recorded but its slug dir does not exist (THE LIVE DEFECT)
        lines.clear(); c = cell_at("noslug", "cfgB", make_slug=False)
        rc = one(c, stub, 1, None, out)
        check(rc == 3 and any("rc 3" in l and "never of tokens" in l for l in lines),
              "RED recorded cfg with no slug dir -> rc 3, names the path, refuses to print 0")
        # RED 3 — the meter runs but emits no RECEIPT rows
        lines.clear(); open(fixture, "w").write("heads 0 sidechains 0 workflows 0 records 0 unparsable 0\n")
        c = cell_at("norec", "cfgC")
        check(one(c, stub, 1, None, out) == 4 and any("Unmetered is not zero" in l for l in lines),
              "RED meter emits no RECEIPT rows -> rc 4, 'unmetered is not zero'")
        # RED 4 — a VOID must be CARRIED, not swallowed, and the cell still prints
        lines.clear(); open(fixture, "w").write("VOID(UNDERSTATED) 1 record(s) carry stop_reason=null\n" + good)
        c = cell_at("void", "cfgD")
        rc = one(c, stub, 1, None, out)
        check(rc == 0 and any("VOID(UNDERSTATED)" in l for l in lines) and any("T" in l for l in lines),
              "a VOID rides WITH the numbers, verbatim, and the cell still reports")
        # GREEN — every expected value DERIVED FROM THE FIXTURE'S BYTES, never typed (idiom law clause 1)
        lines.clear(); open(fixture, "w").write(good)
        c = cell_at("green", "cfgE")
        rc = one(c, stub, 1, None, out)
        body = "\n".join(lines)
        fx_rows, _, _ = parse(good)
        exp_T = sum(r["T"] for r in fx_rows)
        exp_head = 100.0 * sum(r["T"] for r in fx_rows if r["bucket"] == "head") / exp_T
        # ⛔ each arm is a single conjunction: an `and ... or ...` arm passes on the OR alone and tests nothing
        check(rc == 0, "GREEN a complete cell exits 0")
        check(str(exp_T) in body, "GREEN the ALL row carries T derived from the fixture (= %d), summed not typed" % exp_T)
        check(("head %.1f%%" % exp_head) in body,
              "GREEN role share recomputed from T (= %.1f%%), not copied from the meter's own share column" % exp_head)
        # and the arm that proves the arm above can FAIL: a different fixture must move the number
        lines.clear(); open(fixture, "w").write(good.replace("T 485 30%", "T 9485 30%"))
        c2 = cell_at("green2", "cfgF"); one(c2, stub, 1, None, out)
        check(str(exp_T) not in "\n".join(lines),
              "MUTANT a changed fixture moves the total, so the two arms above are not vacuous")
        check("phases recorded: 1" in body, "GREEN the phase the CELL records is reported (⑯'s phase dimension)")
        check("worker/designer/reviewer DO NOT SEPARATE" in body, "the declared absence is printed BESIDE the numbers, never left to a document")
        # ⛔ THE TTL SPLIT — cache_creation is TWO directions at DIFFERENT rates, and a merged one cannot be priced
        fx_head = [r for r in fx_rows if r["bucket"] == "head"][0]
        check(str(fx_head["w1"]) in body and str(fx_head["w5"]) in body,
              "the cache_creation 5m/1h SPLIT is carried (fixture: %d/%d), not merged away" % (fx_head["w5"], fx_head["w1"]))
        # and the mutant: move the split WITHOUT moving the total, and the output must change
        lines.clear(); open(fixture, "w").write(good.replace("cache_creation 100 (0/100)", "cache_creation 100 (100/0)"))
        c3 = cell_at("green3", "cfgG"); one(c3, stub, 1, None, out)
        moved = "\n".join(lines)
        check(str(exp_T) in moved and moved != body,
              "MUTANT moving cache_creation between TTLs leaves T unchanged and CHANGES the report — a merged column could not tell them apart")
    print("cell_tokens SELF-TEST: " + ("OK" if ok[0] else "FAILED"))
    return 0 if ok[0] else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cells", nargs="*")
    ap.add_argument("--meter", default=None)
    ap.add_argument("--launches", type=int, default=1)
    ap.add_argument("--raw-dir", default=None)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not a.cells or not a.meter:
        print("usage: cell_tokens.py <cell-dir> ... --meter <cell_meter.py> [--raw-dir <dir>]"); return 64
    worst = 0
    for c in a.cells:
        rc = one(c, a.meter, a.launches, a.raw_dir, print)
        worst = worst or rc
        print("")
    return worst


if __name__ == "__main__":
    sys.exit(main())
