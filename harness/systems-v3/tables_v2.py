#!/usr/bin/env python3
"""tables_v2.py --map CELLMAP.tsv [--out RESULT.md] [--selftest]

The instrument registered by REGISTRATION-descriptive-tables-v2-2026-09-27.md: four descriptive tables over the complete
pilot matrix (T1 greenfield, T2 brownfield, T3 spec-change, T4 salt-diet / plain ratios), one median per condition, every
figure read from a TRACKED per-cell source named in the cell map. Nothing is typed: a cell whose source row or column
cannot be found prints `unmeasured`, and the 181 + 16 + 3 = 200 check then fails and the exit code is non-zero.

CELLMAP.tsv, one row per CELL (INEXPR conditions and DECLARED conditions without cells carry one row with cell `-`):
  model problem field arm extras status cell lower_bound lb_reason sources note
    status       DONE | INEXPR | DECLARED
    lower_bound  1 if the figure is a floor (CAP-COST · FLOOR meter · DEADLINE cut; registration ADDENDUM 1 A1.2)
    sources      entries separated by ' ; ' whose T values are SUMMED (a spec-change cell's phases, A1.1); NONE if none:
                   tsv|<path>|<k=v,k=v>|<T col>|<out col or ->     filters select exactly one data row ('#' lines are not data)
                   md|<path>|<line>|<T header>|<out header or ->    a markdown pipe-table row; the header row is found above it
                   json|<path>|<id>|<phase or ->|<T field>|<out field or ->   a list of records keyed by id (and phase)
                   fix|<path>|<line>|<T field #>|<out field # or ->  a whitespace-split line of a fenced table; the cell id must be on it
                   re|<path>|<line>|<regex, one group>              a prose figure; the regex must match exactly once; cell id on the line
                   re@<anchor>|<path>|<line>|<regex>               the same, the cell id on an ANCHOR line at most 5 lines above
rc 0 the check holds and every DONE cell was measured · 1 a check failed (named) · 2 usage."""
import argparse, csv, io, json, os, re, shutil, statistics, subprocess, sys

MODELS = ["claude-opus-5", "claude-sonnet-5", "gemini-3.1-pro-high", "gemini-3.8-flash-high"]
PROBLEMS = ["Crc32", "LRU", "FreeList", "LZW", "Paxos"]
EXCLUDED = []
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def _num(x):
    try:
        return float(str(x).replace(",", "").strip())
    except (TypeError, ValueError):
        return None


def _tsv(path, cache):
    if ("tsv", path) not in cache:
        full = os.path.join(REPO, path)
        header, rows = None, []
        if os.path.exists(full):
            for ln in open(full, encoding="utf-8").read().splitlines():
                if not ln.strip() or ln.startswith("#"):
                    continue
                if header is None:
                    header = ln.split("\t")
                else:
                    rows.append(ln.split("\t"))
        cache[("tsv", path)] = (header, rows)
    return cache[("tsv", path)]


def _mdcells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def read_entry(e, cache, cell_id=None):
    """One source entry -> (T, out, provenance) or (None, None, reason).  Grammar: see the module docstring."""
    parts = e.strip().split("|")
    kind = parts[0]
    if kind == "tsv" and len(parts) == 5:
        _, path, filt, tcol, ocol = parts
        header, rows = _tsv(path, cache)
        if header is None:
            return None, None, "no such source %s" % path
        conds = [kv.split("=", 1) for kv in filt.split(",") if kv]
        if tcol not in header or any(k not in header for k, _ in conds):
            return None, None, "column missing in %s" % path
        hits = [r for r in rows if all(len(r) > header.index(k) and r[header.index(k)] == v for k, v in conds)]
        if len(hits) != 1:
            return None, None, "%d rows for %s in %s" % (len(hits), filt, path)
        r = hits[0]
        t = _num(r[header.index(tcol)]) if len(r) > header.index(tcol) else None
        o = _num(r[header.index(ocol)]) if ocol in header and len(r) > header.index(ocol) else None
        return (t, o, "%s [%s].%s" % (path, filt, tcol)) if t is not None else (None, None, "T not numeric in %s [%s]" % (path, filt))
    if kind == "md" and len(parts) == 5:
        _, path, lineno, tname, oname = parts
        full = os.path.join(REPO, path)
        if not os.path.exists(full):
            return None, None, "no such source %s" % path
        lines = open(full, encoding="utf-8").read().splitlines()
        i = int(lineno) - 1
        if not (0 <= i < len(lines)) or not lines[i].lstrip().startswith("|"):
            return None, None, "line %s of %s is not a table row" % (lineno, path)
        j = i
        while j > 0 and lines[j - 1].lstrip().startswith("|"):
            j -= 1
        header = _mdcells(lines[j])
        row = _mdcells(lines[i])
        if tname not in header:
            return None, None, "header %r not in the table at %s:%d" % (tname, path, j + 1)
        t = _num(row[header.index(tname)]) if len(row) > header.index(tname) else None
        o = _num(row[header.index(oname)]) if oname in header and len(row) > header.index(oname) else None
        return (t, o, "%s:%s col %r" % (path, lineno, tname)) if t is not None else (None, None, "T not numeric at %s:%s" % (path, lineno))
    if kind == "json" and len(parts) == 6:
        _, path, cid, phase, tf, of = parts
        full = os.path.join(REPO, path)
        if not os.path.exists(full):
            return None, None, "no such source %s" % path
        if ("json", path) not in cache:
            cache[("json", path)] = json.load(open(full, encoding="utf-8"))
        d = cache[("json", path)]
        hits = [x for x in d if isinstance(x, dict) and str(x.get("id")) == cid and (phase == "-" or str(x.get("phase")) == phase)]
        if len(hits) != 1:
            return None, None, "%d records for id=%s phase=%s in %s" % (len(hits), cid, phase, path)
        t, o = _num(hits[0].get(tf)), (_num(hits[0].get(of)) if of != "-" else None)
        return (t, o, "%s [id=%s,phase=%s].%s" % (path, cid, phase, tf)) if t is not None else (None, None, "T null at %s id=%s phase=%s" % (path, cid, phase))
    anchor = None
    if kind.startswith("re@"):
        kind, anchor = "re", int(kind[3:])
    if kind in ("fix", "re") and len(parts) >= 4:
        path, lineno = parts[1], parts[2]
        full = os.path.join(REPO, path)
        if not os.path.exists(full):
            return None, None, "no such source %s" % path
        lines = open(full, encoding="utf-8").read().splitlines()
        i = int(lineno) - 1
        if not (0 <= i < len(lines)):
            return None, None, "no line %s in %s" % (lineno, path)
        ln = lines[i]
        if anchor is not None:
            if not (i - 5 <= anchor - 1 <= i) or not cell_id or cell_id not in lines[anchor - 1].split():
                return None, None, "cell %s not on anchor line %s of %s (within 5 above %s)" % (cell_id, anchor, path, lineno)
        elif cell_id and cell_id not in ln:
            return None, None, "cell %s not on %s:%s" % (cell_id, path, lineno)
        if kind == "fix" and len(parts) == 5:
            f = ln.split()
            ti = int(parts[3]) - 1
            t = _num(f[ti]) if 0 <= ti < len(f) else None
            o = None
            if parts[4] != "-":
                oi = int(parts[4]) - 1
                o = _num(f[oi]) if 0 <= oi < len(f) else None
            return (t, o, "%s:%s field %s" % (path, lineno, parts[3])) if t is not None else (None, None, "field %s not numeric at %s:%s" % (parts[3], path, lineno))
        if kind == "re":
            rx = "|".join(parts[3:])
            ms = list(re.finditer(rx, ln))
            if len(ms) != 1 or ms[0].lastindex != 1:
                return None, None, "regex matched %d times at %s:%s" % (len(ms), path, lineno)
            t = _num(ms[0].group(1))
            return (t, None, "%s:%s /%s/" % (path, lineno, rx)) if t is not None else (None, None, "regex group not numeric at %s:%s" % (path, lineno))
    return None, None, "unparsed source entry %r" % e


def read_cell(r, cache):
    """Sum of the cell's source entries (registration ADDENDUM 1 A1.1). Any entry unresolved -> unmeasured."""
    if r["sources"].strip() in ("", "-", "NONE"):
        return None, None, "no tracked source"
    tt, oo, provs = 0.0, 0.0, []
    for e in r["sources"].split(" ; "):
        t, o, p = read_entry(e, cache, r.get("cell"))
        if t is None:
            return None, None, p
        tt += t
        oo = None if (o is None or oo is None) else oo + o
        provs.append(p)
    return tt, oo, " + ".join(provs)


def median_mark(vals):
    """vals: [(value, capped)] -> (median, bounded).  Registration §D3: ≥ iff a capped cell sits at or below the median
    position in the ascending sort; ties conservative."""
    s = sorted(vals, key=lambda x: (x[0], -x[1]))
    n = len(s)
    med = statistics.median([v for v, _ in s])
    hi = n // 2  # index of the upper-middle element; for odd n it is the median element
    lo_bound = any(c for v, c in s[:hi + 1]) or any(c for v, c in s if v == med)
    return med, bool(lo_bound)


def fmt(v, bounded):
    if v is None:
        return "unmeasured"
    s = "{:,.0f}".format(v)
    return ("≥ " + s) if bounded else s


def ratio(num, den):
    """num, den: (value|None, bounded, mark) -> (value|None, mark) per §D4."""
    (nv, nb, nm), (dv, db, dm) = num, den
    if nm or dm:
        return None, "-"
    if nb and db:
        return nv / dv, "bounds only"
    if nb:
        return nv / dv, "≥"
    if db:
        return nv / dv, "≤"
    return nv / dv, ""


def sign(r):
    v, m = r
    if v is None or m == "bounds only":
        return None
    if m == "":
        return v > 1
    if m == "≥":
        return True if v > 1 else None
    if m == "≤":
        return False if v <= 1 else None
    return None


def build(map_path):
    allrows = list(csv.DictReader(open(map_path, encoding="utf-8"), delimiter="\t"))
    rows = [r for r in allrows if not r["model"].startswith("#")]
    EXCLUDED[:] = [r for r in allrows if r["model"].startswith("#")]
    cache, conds, prov = {}, {}, []
    for r in rows:
        k = (r["model"], r["problem"], r["field"], r["arm"], r["extras"])
        c = conds.setdefault(k, {"status": r["status"], "cells": []})
        if c["status"] != r["status"]:
            c["status"] = "CONFLICT"
        if r["status"] == "DONE" or (r["status"] == "DECLARED" and r["cell"] != "-"):
            t, o, p = read_cell(r, cache)
            c["cells"].append((r["cell"], t, o, r["lower_bound"] == "1", p))
            prov.append((k, r["cell"], t, o, r["lb_reason"] if r["lower_bound"] == "1" else "-", p))
    return conds, prov


def summarise(c):
    if c is None:
        return (None, False, "missing")
    if c["status"] == "INEXPR":
        return (None, False, "—")
    if c["status"] == "DECLARED":
        return (None, False, "declared")
    if c["status"] != "DONE":
        return (None, False, c["status"])
    if not c["cells"] or any(t is None for _, t, _, _, _ in c["cells"]):
        return (None, False, "unmeasured")
    med, b = median_mark([(t, cap) for _, t, _, cap, _ in c["cells"]])
    return (med, b, "")


def show(s):
    v, b, m = s
    return m if m else fmt(v, b)


def render(conds, prov):
    out, fails = [], []
    counts = {"num": 0, "—": 0, "declared": 0, "other": 0}
    def cell(k):
        s = summarise(conds.get(k))
        if s[2] == "":
            counts["num"] += 1
        elif s[2] in ("—", "declared"):
            counts[s[2]] += 1
        else:
            counts["other"] += 1
            fails.append("%s -> %s" % ("/".join(k), s[2]))
        return s
    def table(title, field, cols):
        out.append("\n## %s\n" % title)
        out.append("| model | problem | " + " | ".join(c[0] for c in cols) + " |")
        out.append("|---|---|" + "---|" * len(cols))
        grid = {}
        for m in MODELS:
            for p in PROBLEMS:
                vals = []
                for name, arm, extras in cols:
                    s = cell((m, p, field, arm, extras))
                    grid[(m, p, name)] = s
                    vals.append(show(s))
                out.append("| %s | %s | %s |" % (m, p, " | ".join(vals)))
        return grid
    four = [("bare-plain", "plain", "none"), ("bare-salt-diet", "salt-diet", "none"),
            ("statement-plain", "plain", "statement"), ("statement-salt-diet", "salt-diet", "statement")]
    g1 = table("T1 · greenfield — median total tokens per condition (n per condition in the output-token table below)", "greenfield", four)
    g2 = table("T2 · brownfield — median total tokens per condition (n per condition in the output-token table below)", "brownfield", four)
    g3 = table("T3 · spec-change (greenfield only) — median total tokens per condition (n per condition in the output-token table below)", "greenfield",
               [("plain", "plain", "spec-change"), ("salt-diet", "salt-diet", "spec-change")])
    total = counts["num"] + counts["—"] + counts["declared"] + counts["other"]
    check = "CHECK numbers %d + — %d + declared %d = %d (other %d) against 181 + 16 + 3 = 200" % (
        counts["num"], counts["—"], counts["declared"], total, counts["other"])
    ok = (counts["num"], counts["—"], counts["declared"], counts["other"], total) == (181, 16, 3, 0, 200)
    if not ok:
        fails.insert(0, check)
    # T4 (greenfield) + brownfield ratios in the file
    def rat(g, m, p, a, b):
        return ratio(g[(m, p, a)], g[(m, p, b)])
    out.append("\n## T4 · salt-diet ÷ plain, greenfield (registration §D4)\n")
    out.append("| model | problem | bare | statement | spec-change |")
    out.append("|---|---|---|---|---|")
    signs = {}
    for m in MODELS:
        for p in PROBLEMS:
            rs = [("bare", rat(g1, m, p, "bare-salt-diet", "bare-plain")),
                  ("statement", rat(g1, m, p, "statement-salt-diet", "statement-plain")),
                  ("spec-change", rat(g3, m, p, "salt-diet", "plain"))]
            cells = []
            for name, (v, mk) in rs:
                signs.setdefault((m, name), []).append((p, v, mk))
                cells.append("—" if v is None else (("%s %.2f" % (mk, v)).strip() if mk != "bounds only" else "bounds only (%.2f)" % v))
            out.append("| %s | %s | %s |" % (m, p, " | ".join(cells)))
    out.append("\n### T4 sign counts, per model per treatment (no p-value, by ruling)\n")
    out.append("| model | treatment | k of m ratios > 1 | indeterminate | median of the ratios | bounded among them |")
    out.append("|---|---|---|---|---|---|")
    for m in MODELS:
        for name in ("bare", "statement", "spec-change"):
            lst = signs[(m, name)]
            have = [(p, v, mk) for p, v, mk in lst if v is not None]
            sg = [(p, sign((v, mk))) for p, v, mk in have]
            k = sum(1 for _, s in sg if s is True)
            mm = sum(1 for _, s in sg if s is not None)
            ind = [p for p, s in sg if s is None]
            med = ("%.2f" % statistics.median([v for _, v, _ in have])) if have else "—"
            nb = sum(1 for _, v, mk in have if mk)
            out.append("| %s | %s | %d of %d | %s | %s | %d |" % (m, name, k, mm, ", ".join(ind) or "none", med, nb))
    out.append("\n### brownfield ratios (in the file, not in T4)\n")
    out.append("| model | problem | bare | statement |")
    out.append("|---|---|---|---|")
    for m in MODELS:
        for p in PROBLEMS:
            cs = []
            for a, b in (("bare-salt-diet", "bare-plain"), ("statement-salt-diet", "statement-plain")):
                v, mk = rat(g2, m, p, a, b)
                cs.append("—" if v is None else (("%s %.2f" % (mk, v)).strip() if mk != "bounds only" else "bounds only (%.2f)" % v))
            out.append("| %s | %s | %s |" % (m, p, " | ".join(cs)))
    # output tokens + per-cell provenance
    out.append("\n## Per-condition medians of OUTPUT tokens (same rule; not in the tables)\n")
    out.append("| model | problem | field | arm | extras | n | median output | bounded |")
    out.append("|---|---|---|---|---|---|---|---|")
    for k in sorted(conds):
        c = conds[k]
        if c["status"] != "DONE" or not c["cells"]:
            continue
        os_ = [(o, cap) for _, _, o, cap, _ in c["cells"]]
        if any(o is None for o, _ in os_):
            out.append("| %s | %d | unmeasured | - |" % (" | ".join(k), len(os_)))
            continue
        med, b = median_mark(os_)
        out.append("| %s | %d | %s | %s |" % (" | ".join(k), len(os_), "{:,.0f}".format(med), "≥" if b else ""))
    out.append("\n## Per-cell figures and their sources (every table number derives from these rows)\n")
    out.append("| model | problem | field | arm | extras | cell | T | output | lower bound | source |")
    out.append("|---|---|---|---|---|---|---|---|---|---|")
    for k, cell_id, t, o, cap, p in prov:
        out.append("| %s | %s | %s | %s | %s | %s |" % (" | ".join(k), cell_id, "unmeasured" if t is None else "{:,.0f}".format(t),
                   "-" if o is None else "{:,.0f}".format(o), cap, p))
    return out, check, ok, fails


def selftest():
    assert median_mark([(1, 0), (2, 0), (3, 1)]) == (2, False)      # cap above the median cannot move it
    assert median_mark([(1, 1), (2, 0), (3, 0)]) == (2, True)       # cap below: the median is a floor
    assert median_mark([(1, 0), (2, 1), (3, 0)]) == (2, True)
    assert median_mark([(2, 0), (2, 1), (3, 0)]) == (2, True)       # tie with a capped value: conservative
    assert ratio((2.0, True, ""), (1.0, False, "")) == (2.0, "≥")
    assert ratio((2.0, False, ""), (1.0, True, "")) == (2.0, "≤")
    assert ratio((2.0, True, ""), (1.0, True, ""))[1] == "bounds only"
    assert ratio((None, False, "—"), (1.0, False, "")) == (None, "-")
    assert sign((1.5, "")) is True and sign((0.5, "")) is False
    assert sign((1.5, "≥")) is True and sign((0.9, "≥")) is None
    assert sign((0.9, "≤")) is False and sign((1.2, "≤")) is None
    import tempfile
    global REPO
    old, d = REPO, tempfile.mkdtemp(prefix="tables_v2.")
    try:
        REPO = d
        open(os.path.join(d, "a.tsv"), "w").write("# c\tx\ncell\troot\tT\tout\nx1\tr1\t100\t7\nx1\tr2\t200\t8\n")
        open(os.path.join(d, "b.md"), "w").write("text\n| cell | T (tokens) | out |\n|---|---|---|\n| y1 | 1,500 | 9 |\n")
        json.dump([{"id": "z1", "phase": 1, "T": 10}, {"id": "z1", "phase": 2, "T": 5}], open(os.path.join(d, "c.json"), "w"))
        c = {}
        assert read_entry("tsv|a.tsv|cell=x1,root=r2|T|out", c)[:2] == (200.0, 8.0)
        assert read_entry("tsv|a.tsv|cell=x1|T|out", c)[0] is None          # two rows: refuse, never pick one
        assert read_entry("md|b.md|4|T (tokens)|out", c)[:2] == (1500.0, 9.0)
        assert read_entry("md|b.md|3|T (tokens)|out", c)[0] is None          # the separator row is not a figure
        r = {"sources": "json|c.json|z1|1|T|- ; json|c.json|z1|2|T|-"}
        assert read_cell(r, c)[0] == 15.0                                     # phases sum (A1.1)
        assert read_cell({"sources": "json|c.json|z1|1|T|- ; json|c.json|z9|2|T|-"}, c)[0] is None   # one missing phase
        assert read_cell({"sources": "NONE"}, c)[0] is None
        open(os.path.join(d, "f.md"), "w").write("```\n  q1   LANDED  3,400   120\n  q2   LANDED  9   1\n```\nthe tripwire cell q3 spent 12,345 tokens in all\n")
        assert read_entry("fix|f.md|2|3|4", c, "q1")[:2] == (3400.0, 120.0)
        assert read_entry("fix|f.md|2|3|4", c, "q2")[0] is None                # the wrong cell's line: refuse
        assert read_entry(r"re|f.md|5|spent ([0-9,]+) tokens", c, "q3")[0] == 12345.0
        assert read_entry(r"re|f.md|5|([0-9,]+)", c, "q3")[0] is None          # two matches: refuse
        assert read_entry(r"re@2|f.md|3|LANDED  ([0-9,]+)", c, "q1")[0] == 9.0  # continuation line, id on the anchor
        assert read_entry(r"re@2|f.md|3|LANDED  ([0-9,]+)", c, "q2")[0] is None # anchor names another cell: refuse
    finally:
        REPO = old
        shutil.rmtree(d, ignore_errors=True)
    print("selftest OK (24 arms)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--map")
    ap.add_argument("--out")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.map:
        ap.error("--map is required")
    conds, prov = build(a.map)
    body, check, ok, fails = render(conds, prov)
    head = subprocess.run(["git", "-C", REPO, "rev-parse", "--short=12", "HEAD"], capture_output=True, text=True).stdout.strip()
    unmeasured = []
    for k in sorted(conds):
        c = conds[k]
        if c["status"] == "DONE" and (not c["cells"] or any(t is None for _, t, _, _, _ in c["cells"])):
            miss = [cid for cid, t, _, _, _ in c["cells"] if t is None]
            unmeasured.append("| %s | %s |" % (" | ".join(k), ", ".join(miss)))
    hdr = [
        "# RESULT: FOUR DESCRIPTIVE TABLES OVER THE COMPLETE PILOT MATRIX (arXiv v2)",
        "## Printed by `harness/systems-v3/tables_v2.py` at repo head `%s` from the cell map `%s`. Registered in "
        "`REGISTRATION-descriptive-tables-v2-2026-09-27.md` (§D1–§D6 and ADDENDUM 1), which was committed before this ran." % (head, os.path.relpath(os.path.abspath(a.map), REPO)),
        "",
        "**%s ⇒ %s.**" % (check, "THE CHECK HOLDS" if ok else "THE CHECK FAILS, AS REGISTERED (§D2): a DONE condition with any cell lacking a tracked figure prints `unmeasured`, and nothing is recovered by hand"),
        "",
        "⛔ **A descriptive reading over the complete matrix: no test, no p-value, no verdict on the arms. The registered tests "
        "remain §4's.** Every number below is a median of total tokens over a condition's cells of record (n = 3 for most; the n of each condition is printed in the output-token table).",
        "",
        "- **`T` differs between lanes, so compare arms WITHIN a row.** Claude lane: input + cache writes + cache reads + output, "
        "from the session meter; the block cells include the harness's sandbox probe in both arms (ADDENDUM 1 A1.3). agy lane "
        "(both Gemini models): input + output + cache read, with thinking inside output, as the vendor reports it.",
        "- **`≥`** the median is a floor, because a cell at or below the median position stopped at the cost cap (CAP-COST), "
        "carries a meter that records an under-read (FLOOR), or was cut off by a registered turn or wall deadline (DEADLINE). "
        "The reason is named per cell at the foot of this file. The cap binds the salt-diet arm more often (census §T3, §U2, §V3).",
        "- **`—`** inexpressible: Paxos × statement, both task forms, all four models (an arm-neutral formal statement cannot "
        "exist for a proof-obligation task). **`declared`** unreached at the cap (census ADDENDUM 19). **`unmeasured`** a DONE "
        "condition some of whose cells have no tracked token figure (listed next).",
        "- A spec-change cell's figure is phase 1 + phase 2 (ADDENDUM 1 A1.1). For the Opus spec-change cells, phase 1 is the "
        "reused matrix-1 landing, so the same phase-1 figure also appears in that landing's own row.",
        "",
        "## The %d unmeasured conditions and the cells with no tracked figure" % len(unmeasured),
        "| model | problem | field | arm | extras | cells with no tracked T |",
        "|---|---|---|---|---|---|",
    ] + unmeasured + [
        "",
        "## Cells in the map but OUTSIDE a condition's population (the result of record's scored cells govern, ADDENDUM 1 A1.4)",
        "| map row | cell | why |",
        "|---|---|---|",
    ] + ["| %s | %s | %s |" % (" / ".join([r["model"].replace("#EXCLUDED-BY-RECORD ", ""), r["problem"], r["field"], r["arm"], r["extras"]]),
                              r["cell"], r["note"].split(". ")[0]) for r in EXCLUDED]
    txt = "\n".join(hdr + body) + "\n"
    if a.out:
        open(a.out, "w", encoding="utf-8").write(txt)
    else:
        sys.stdout.write(txt)
    print(check, file=sys.stderr)
    print("instrument at repo head %s; map %s" % (head, a.map), file=sys.stderr)
    for f in fails[:40]:
        print("FAIL " + f, file=sys.stderr)
    if len(fails) > 40:
        print("... %d more" % (len(fails) - 40), file=sys.stderr)
    return 0 if ok and not fails else 1


if __name__ == "__main__":
    sys.exit(main())
