#!/usr/bin/env python3
"""tables_v3.py --map CELLMAP.tsv --ev EVIDENCE_DIR [--out RESULT.md] [--selftest]

The instrument registered by REGISTRATION-cost-tables-v3-2026-09-29.md (§V1–§V6, ADDENDA 1–2): the complete pilot matrix in
DOLLARS and WALL SECONDS, one median per condition by v2's rule (tables_v2.median_mark, imported unchanged), over v2's cell map.
Tokens are not reprinted: the paper cites v2's T1–T4.

Inputs, all tracked: v2's cell map; in EVIDENCE_DIR the step a–e extractions (cellroots.tsv, claude-cost-raw.tsv,
claude-wall-raw.tsv, agy-steps-raw.tsv, opus-split-raw.tsv, rates-gemini-2026-09-29.tsv); v2's tracked Claude sources (for the
cost column of the row v2 read T from); level 8's phase_facts.json files (the second method for the aside walls).
Nothing is typed: a cell whose figure cannot be derived prints `unmeasured` with its reason.
rc 0 every table's check holds (numbers + — + declared + unmeasured = 200) and no second method disagreed · 1 otherwise · 2 usage."""
import argparse, csv, glob, json, os, statistics, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import tables_v2 as v2   # median_mark, ratio, sign, _tsv, MODELS, PROBLEMS: v2's rules, unchanged by registration §V3

REPO = v2.REPO
TIER = 200000
# the cost column of the row v2 read T from (ADDENDUM 2 A2.3: the tracked cost is the figure of record)
COST_COL = {"final_T": ["final_COST"], "p1_T": ["p1_COST"], "p2_T": ["p2_COST"], "T": ["cost", "cost_usd"]}


INPUTS = ["cellroots.tsv", "claude-cost-raw.tsv", "claude-wall-raw.tsv", "claude-wall-raw-allroots.tsv", "agy-steps-raw.tsv",
          "opus-split-raw.tsv", "rates-gemini-2026-09-29.tsv"]


def blob(path):
    return subprocess.run(["git", "hash-object", path], capture_output=True, text=True).stdout.strip()[:12] or "UNHASHED"


def repro_cause(f):
    """ADDENDUM 3 A3.2's two causes, per row, so the limit rides beside the figure; anything else is named UNEXPLAINED."""
    if f.get("wall_copy_root"):
        return "A3.1 copy root: the re-run metered the landing's slug (phase 1) only"
    if "p1_COST" in f.get("usd_src", "") and "p2_COST" in f.get("usd_src", ""):
        return "SC probe-separated: the tracked phases exclude the sandbox probe; the re-run includes it"
    return "UNEXPLAINED"


def tsv(path):
    rows = [l.rstrip("\n").split("\t") for l in open(path, encoding="utf-8") if l.strip() and not l.startswith("#")]
    return [dict(zip(rows[0], r)) for r in rows[1:]]


def load_ev(ev):
    E = {}
    E["root"] = {r["cell"]: r["root"] for r in tsv(os.path.join(ev, "cellroots.tsv"))}
    E["ccost"] = {(r["cell"], r["root"]): r for r in tsv(os.path.join(ev, "claude-cost-raw.tsv"))}
    E["cwall"] = {}
    for r in tsv(os.path.join(ev, "claude-wall-raw.tsv")):
        E["cwall"].setdefault((r["cell"], r["root"]), []).append(r)
    E["cwall_all"] = {}
    for r in tsv(os.path.join(ev, "claude-wall-raw-allroots.tsv")):
        E["cwall_all"].setdefault(r["cell"], {}).setdefault(r["root"], []).append(r)
    E["agy"] = {}
    for r in tsv(os.path.join(ev, "agy-steps-raw.tsv")):
        E["agy"].setdefault((r["cell"], r["root"]), []).append(r)
    E["split"] = {(r["cell"], r["root"]): r for r in tsv(os.path.join(ev, "opus-split-raw.tsv"))}
    E["rates"] = {}
    for r in tsv(os.path.join(ev, "rates-gemini-2026-09-29.tsv")):
        E["rates"].setdefault(r["lane_label"], {})[r["tier"]] = r
    E["facts"] = {}
    for p in sorted(glob.glob(os.path.join(REPO, "evidence", "l8-*", "phase_facts.json"))):
        for x in json.load(open(p)):
            E["facts"].setdefault((x["id"], int(x["phase"])), []).append((x.get("wall_seconds"), os.path.relpath(p, REPO)))
    return E


def tracked_cost(sources, cache):
    """The sum of the cost columns of the tsv rows v2 read T from, or (None, why)."""
    if sources.strip() in ("", "-", "NONE"):
        return None, "no tracked source row"
    tot, prov = 0.0, []
    for e in sources.split(" ; "):
        parts = e.strip().split("|")
        if parts[0] != "tsv" or len(parts) != 5:
            return None, "a %s source carries no cost column" % parts[0]
        _, path, filt, tcol, _ = parts
        header, rows = v2._tsv(path, cache)
        col = next((c for c in COST_COL.get(tcol, []) if header and c in header), None)
        if col is None:
            return None, "no cost column beside %s in %s" % (tcol, path)
        conds = [kv.split("=", 1) for kv in filt.split(",") if kv]
        hits = [r for r in rows if all(len(r) > header.index(k) and r[header.index(k)] == v for k, v in conds)]
        if len(hits) != 1:
            return None, "%d rows for %s in %s" % (len(hits), filt, path)
        v = v2._num(hits[0][header.index(col)]) if len(hits[0]) > header.index(col) else None
        if v is None:
            return None, "%s not numeric in %s [%s]" % (col, path, filt)
        tot += v
        prov.append("%s [%s].%s" % (path, filt, col))
    return tot, " + ".join(prov)


def wall_num(s):
    """'wall 924/144000' -> (924.0, 144000.0)"""
    a, b = s.split()[1].split("/")
    return float(a), float(b)


def claude_cell(r, E, cache):
    """-> dict(usd, usd_b, usd_src, rerun, wall, wall_b, wall_src)"""
    cell, root = r["cell"], E["root"].get(r["cell"])
    lb = r["lower_bound"] == "1"
    out = {"usd": None, "usd_b": lb, "rerun": None, "wall": None, "wall_b": lb}
    x = E["ccost"].get((cell, root))
    if x:
        out["rerun"] = float(x["COST"])
    tc, why = tracked_cost(r["sources"], cache)
    if tc is not None:
        out["usd"], out["usd_src"] = tc, why
    elif out["rerun"] is not None:
        out["usd"], out["usd_src"] = out["rerun"], "claude-cost-raw.tsv (cell_meter re-run; %s)" % why
    else:
        out["usd_src"] = "unmeasured: %s; no re-run row" % why
    if x and "UNDERSTATED" in x["void"]:
        out["usd_b"] = True
    walls = E["cwall"].get((cell, root), [])
    if r["lb_reason"] == "CAP-COST" and out["usd"] is not None:
        capped = [w for w in walls if w["end_kind"] == "CAP-COST"]
        if len(capped) == 1 and x:
            cap = float(x["C1_USD"] if capped[0]["phase"] == "1" else x["C2_USD"])
            out["cap"] = cap
            if cap > out["usd"]:
                out["usd"], out["usd_src"] = cap, out["usd_src"] + " -> the cap %.2f entered (A1.3)" % cap
        else:
            out["cap"] = None
    phases = sorted(walls, key=lambda w: w["phase"])
    need = 2 if r["extras"] == "spec-change" else 1
    if need == 2 and len(phases) == 1 and phases[0]["phase"] == "1":
        # ADDENDUM 3: phase 2 ran in a COPY of this cell under another root. Take the ONE other root holding both phases, and only
        # if its phase-1 row is this root's phase-1 row (the copy check); anything else stays unmeasured.
        key = lambda w: (w["phase"], w["wall_last_meter"], w["held_s"], w["end_kind"])
        cand = [(rt, sorted(ws, key=lambda w: w["phase"])) for rt, ws in E.get("cwall_all", {}).get(cell, {}).items()
                if rt != root and sorted(w["phase"] for w in ws) == ["1", "2"]]
        if len(cand) == 1 and key(cand[0][1][0]) == key(phases[0]):
            phases = cand[0][1]
            out["wall_copy_root"] = cand[0][0]
        else:
            out["wall_src"] = "unmeasured: phase 2 not in this root and %d copy root(s) pass the copy check" % len(cand)
            return out
    if len(phases) != need or any(w["wall_last_meter"] == "NONE" for w in phases):
        out["wall_src"] = "unmeasured: %d end-marked phase(s) in this cell's own dir, %d needed" % (len(phases), need)
    else:
        ws = [wall_num(w["wall_last_meter"]) for w in phases]
        out["wall"] = sum(a for a, _ in ws)
        out["wall_src"] = ("claude-wall-raw-allroots.tsv, the copy at %s (ADDENDUM 3)" % out["wall_copy_root"]) if out.get("wall_copy_root") \
            else "claude-wall-raw.tsv phases %s" % ",".join(w["phase"] for w in phases)
        if any(a >= b - 60 for a, b in ws):
            out["wall_b"] = True
    return out


def agy_phase_usd(p, rates):
    """One phase's modelled dollars (ADDENDUM 2 A2.1: output includes thinking and is priced once) -> (usd | None, why)."""
    rt = rates.get(p["served"])
    if not rt:
        return None, "no rate row for %s" % p["served"]
    def price(row, inp, cr, out):
        return (inp * float(row["input"]) + cr * float(row["cache_read"]) + out * float(row["output_incl_thinking"])) / 1e6
    one = rt.get("all")
    if p["coverage"] in ("COMPLETE", "EXCEEDS-METER"):
        lo = [int(p["lo_" + k]) for k in ("input", "cache_read", "output")]
        hi = [int(p["hi_" + k]) for k in ("input", "cache_read", "output")]
        if one:
            return price(one, *[a + b for a, b in zip(lo, hi)]), "per request (%s)" % p["coverage"]
        return price(rt["prompt<=200k"], *lo) + price(rt["prompt>200k"], *hi), "per request, tiered (%s)" % p["coverage"]
    if one:
        return price(one, int(p["meter_input"]), int(p["meter_cache_read"]), int(p["meter_output"])), "meter totals (one tier; %s)" % p["coverage"]
    return None, "a tiered price and %s per-request records" % p["coverage"]


def agy_cell(r, E, fails):
    cell, root = r["cell"], E["root"].get(r["cell"])
    lb = r["lower_bound"] == "1"
    out = {"usd": None, "usd_b": lb, "rerun": None, "wall": None, "wall_b": lb}
    ph = sorted(E["agy"].get((cell, root), []), key=lambda p: int(p["phase"]))
    if not ph:
        out["usd_src"] = out["wall_src"] = "unmeasured: no agy phase row"
        return out
    usd, whys, wall = 0.0, [], 0.0
    for p in ph:
        u, why = agy_phase_usd(p, E["rates"])
        whys.append("p%s %s" % (p["phase"], why))
        usd = None if (u is None or usd is None) else usd + u
        if p["wall_s"] in ("-", "", "None"):
            wall = None
        elif wall is not None:
            w = float(p["wall_s"])
            wall += w
            if p["max_wall"] not in ("-", "") and w >= float(p["max_wall"]) - float(p["turn_timeout"]):
                out["wall_b"] = True        # by timing (§V3; A2.5: this errs toward the floor)
            if "ASIDE" in p["note"]:        # A1.1's second method
                fx = E["facts"].get((cell, int(p["phase"])), [])
                if not fx:
                    out.setdefault("facts", []).append("p%s no phase_facts record" % p["phase"])
                for fw, src in fx:
                    if fw is None or abs(float(fw) - w) > 0.1:
                        fails.append("A1.1 wall disagreement %s p%s: turn loop %s vs %s %s" % (cell, p["phase"], w, src, fw))
                    else:
                        out.setdefault("facts", []).append("p%s = %s" % (p["phase"], src))
    out["usd"], out["usd_src"] = usd, "agy-steps-raw.tsv: " + "; ".join(whys)
    out["wall"], out["wall_src"] = wall, "agy-steps-raw.tsv wall_s" if wall is not None else "unmeasured: a phase without a turn-loop wall"
    return out


def build(map_path, ev):
    E = load_ev(ev)
    cache, conds, prov, fails = {}, {}, [], []
    for r in csv.DictReader(open(map_path, encoding="utf-8"), delimiter="\t"):
        if r["model"].startswith("#"):
            continue
        k = (r["model"], r["problem"], r["field"], r["arm"], r["extras"])
        c = conds.setdefault(k, {"status": r["status"], "cells": []})
        if c["status"] != r["status"]:
            c["status"] = "CONFLICT"
        if r["status"] == "DONE" or (r["status"] == "DECLARED" and r["cell"] != "-"):
            f = claude_cell(r, E, cache) if r["model"].startswith("claude") else agy_cell(r, E, fails)
            f["cell"], f["lb_reason"] = r["cell"], r["lb_reason"]
            sp = E["split"].get((r["cell"], E["root"].get(r["cell"])))
            if sp and float(sp["T"]) > 0 and float(sp["COST"]) > 0:
                f["share_T"] = 1 - float(sp["T_head"]) / float(sp["T"])
                f["share_usd"] = 1 - float(sp["COST_head"]) / float(sp["COST"])
            c["cells"].append(f)
            prov.append((k, f))
    return conds, prov, fails


def summarise(c, cur):
    if c is None:
        return (None, False, "missing")
    if c["status"] == "INEXPR":
        return (None, False, "—")
    if c["status"] == "DECLARED":
        return (None, False, "declared")
    if c["status"] != "DONE":
        return (None, False, c["status"])
    if not c["cells"] or any(f[cur] is None for f in c["cells"]):
        return (None, False, "unmeasured")
    med, b = v2.median_mark([(f[cur], f[cur + "_b"]) for f in c["cells"]])
    return (med, b, "")


def show(s, cur):
    v, b, m = s
    if m:
        return m
    t = ("$%s" % "{:,.2f}".format(v)) if cur == "usd" else "{:,.0f} s".format(v)
    return ("≥ " + t) if b else t


def render(conds, cur, tag, unit):
    out, counts, fails = [], {"num": 0, "—": 0, "declared": 0, "unmeasured": 0, "other": 0}, []
    def cell(k):
        s = summarise(conds.get(k), cur)
        key = "num" if s[2] == "" else (s[2] if s[2] in counts else "other")
        counts[key] += 1
        if key == "other":
            fails.append("%s %s -> %s" % (tag, "/".join(k), s[2]))
        return s
    def table(title, field, cols):
        out.append("\n## %s\n" % title)
        out.append("| model | problem | " + " | ".join(c[0] for c in cols) + " |")
        out.append("|---|---|" + "---|" * len(cols))
        grid = {}
        for m in v2.MODELS:
            for p in v2.PROBLEMS:
                vals = []
                for name, arm, extras in cols:
                    s = cell((m, p, field, arm, extras))
                    grid[(m, p, name)] = (s[0], s[1], s[2])
                    vals.append(show(s, cur))
                out.append("| %s | %s | %s |" % (m, p, " | ".join(vals)))
        return grid
    four = [("bare-plain", "plain", "none"), ("bare-salt-diet", "salt-diet", "none"),
            ("statement-plain", "plain", "statement"), ("statement-salt-diet", "salt-diet", "statement")]
    g1 = table("%s1 · greenfield — median %s per condition" % (tag, unit), "greenfield", four)
    g2 = table("%s2 · brownfield — median %s per condition" % (tag, unit), "brownfield", four)
    g3 = table("%s3 · spec-change (greenfield only) — median %s per condition" % (tag, unit), "greenfield",
               [("plain", "plain", "spec-change"), ("salt-diet", "salt-diet", "spec-change")])
    total = sum(counts.values())
    check = "%s CHECK numbers %d + — %d + declared %d + unmeasured %d = %d (other %d) against 200" % (
        tag, counts["num"], counts["—"], counts["declared"], counts["unmeasured"], total, counts["other"])
    if total != 200 or counts["other"] or counts["—"] != 16 or counts["declared"] != 3:
        fails.insert(0, check)
    out.append("\n## %s4 · salt-diet ÷ plain, greenfield, %s (v2 §D4's rule)\n" % (tag, unit))
    out.append("| model | problem | bare | statement | spec-change |")
    out.append("|---|---|---|---|---|")
    signs = {}
    def fr(v, mk):
        return "—" if v is None else (("%s %.2f" % (mk, v)).strip() if mk != "bounds only" else "bounds only (%.2f)" % v)
    for m in v2.MODELS:
        for p in v2.PROBLEMS:
            rs = [("bare", v2.ratio(g1[(m, p, "bare-salt-diet")], g1[(m, p, "bare-plain")])),
                  ("statement", v2.ratio(g1[(m, p, "statement-salt-diet")], g1[(m, p, "statement-plain")])),
                  ("spec-change", v2.ratio(g3[(m, p, "salt-diet")], g3[(m, p, "plain")]))]
            for name, (v, mk) in rs:
                signs.setdefault((m, name), []).append((p, v, mk))
            out.append("| %s | %s | %s |" % (m, p, " | ".join(fr(v, mk) for _, (v, mk) in rs)))
    out.append("\n### %s4 sign counts, per model per treatment (no p-value)\n" % tag)
    out.append("| model | treatment | k of m ratios > 1 | indeterminate | median of the ratios | bounded among them |")
    out.append("|---|---|---|---|---|---|")
    for m in v2.MODELS:
        for name in ("bare", "statement", "spec-change"):
            have = [(p, v, mk) for p, v, mk in signs[(m, name)] if v is not None]
            sg = [(p, v2.sign((v, mk))) for p, v, mk in have]
            k = sum(1 for _, s in sg if s is True)
            mm = sum(1 for _, s in sg if s is not None)
            ind = [p for p, s in sg if s is None]
            med = ("%.2f" % statistics.median([v for _, v, _ in have])) if have else "—"
            out.append("| %s | %s | %d of %d | %s | %s | %d |" % (m, name, k, mm, ", ".join(ind) or "none", med,
                                                                   sum(1 for _, _, mk in have if mk)))
    out.append("\n### %s brownfield ratios (in the file, not in %s4)\n" % (tag, tag))
    out.append("| model | problem | bare | statement |")
    out.append("|---|---|---|---|")
    for m in v2.MODELS:
        for p in v2.PROBLEMS:
            cs = [fr(*v2.ratio(g2[(m, p, a)], g2[(m, p, b)])) for a, b in (("bare-salt-diet", "bare-plain"), ("statement-salt-diet", "statement-plain"))]
            out.append("| %s | %s | %s |" % (m, p, " | ".join(cs)))
    return out, check, fails


def render_split(conds):
    out = ["\n## S1 · Opus: the share of each cell's T and dollars OUTSIDE the head session (median over the condition's cells)\n",
           "| problem | field | arm | extras | n | median share of T | median share of $ |", "|---|---|---|---|---|---|---|"]
    for k in sorted(conds):
        if k[0] != "claude-opus-5" or conds[k]["status"] != "DONE":
            continue
        fs = conds[k]["cells"]
        st = [f["share_T"] for f in fs if "share_T" in f]
        if len(st) != len(fs) or not fs:
            out.append("| %s | %d | unmeasured | unmeasured |" % (" | ".join(k[1:]), len(fs)))
            continue
        out.append("| %s | %d | %.1f %% | %.1f %% |" % (" | ".join(k[1:]), len(fs), 100 * statistics.median(st),
                                                      100 * statistics.median(f["share_usd"] for f in fs)))
    return out


def selftest():
    n = 0
    def ok(c, msg):
        nonlocal n
        n += 1
        if not c:
            raise AssertionError(msg)
    rates = {"F": {"all": {"input": "1", "cache_read": "0.1", "output_incl_thinking": "10"}},
             "P": {"prompt<=200k": {"input": "2", "cache_read": "0.2", "output_incl_thinking": "12"},
                   "prompt>200k": {"input": "4", "cache_read": "0.4", "output_incl_thinking": "18"}}}
    z = {"lo_input": "0", "lo_cache_read": "0", "lo_output": "0", "hi_input": "0", "hi_cache_read": "0", "hi_output": "0",
         "meter_input": "0", "meter_cache_read": "0", "meter_output": "0", "lo_thinking": "0", "hi_thinking": "0"}
    p = dict(z, served="P", coverage="COMPLETE", lo_input="1000000", lo_output="1000000", lo_thinking="900000")
    ok(abs(agy_phase_usd(p, rates)[0] - 14.0) < 1e-9, "Pro low tier: 1M in x 2 + 1M out x 12 = 14; thinking is NOT priced again (A2.1)")
    p = dict(z, served="P", coverage="COMPLETE", hi_input="1000000", hi_cache_read="1000000", hi_output="1000000")
    ok(abs(agy_phase_usd(p, rates)[0] - 22.4) < 1e-9, "Pro upper tier: 4 + 0.4 + 18 (A2.4: only this arm drives it)")
    p = dict(z, served="P", coverage="PARTIAL", meter_input="1000000")
    ok(agy_phase_usd(p, rates)[0] is None, "Pro with PARTIAL records is unmeasured, never priced at one tier (§V2)")
    p = dict(z, served="F", coverage="PARTIAL", meter_input="1000000", meter_output="1000000", lo_input="5")
    ok(abs(agy_phase_usd(p, rates)[0] - 11.0) < 1e-9, "Flash PARTIAL falls back to the meter totals (one tier)")
    p = dict(z, served="F", coverage="EXCEEDS-METER", lo_input="1000000", hi_input="1000000", meter_input="1")
    ok(abs(agy_phase_usd(p, rates)[0] - 2.0) < 1e-9, "Flash EXCEEDS prices the per-request records, both tiers at its one rate")
    ok(agy_phase_usd(dict(z, served="X", coverage="COMPLETE"), rates)[0] is None, "an unknown served label has no price")
    ok(wall_num("wall 924/144000") == (924.0, 144000.0), "wall parse")
    # the Claude cell rules, on a fixture evidence set
    E = {"root": {"c1": "r", "c2": "r", "c3": "r"},
         "ccost": {("c1", "r"): {"COST": "40.10", "void": "-", "C1_USD": "37.21", "C2_USD": "18.60"},
                   ("c2", "r"): {"COST": "24.29", "void": "-", "C1_USD": "37.21", "C2_USD": "18.60"},
                   ("c3", "r"): {"COST": "5.00", "void": "VOID(UNDERSTATED)", "C1_USD": "37.21", "C2_USD": "18.60"}},
         "cwall": {("c1", "r"): [{"phase": "1", "wall_last_meter": "wall 100/144000", "end_kind": "CAP-COST"}],
                   ("c2", "r"): [{"phase": "1", "wall_last_meter": "wall 50/144000", "end_kind": "LANDED"},
                                 {"phase": "2", "wall_last_meter": "wall 80/72000", "end_kind": "CAP-COST"}],
                   ("c3", "r"): [{"phase": "1", "wall_last_meter": "wall 143950/144000", "end_kind": "LANDED"}]}}
    row = lambda c, lb, why, ex: {"cell": c, "lower_bound": lb, "lb_reason": why, "sources": "NONE", "extras": ex}
    f = claude_cell(row("c1", "1", "CAP-COST", "none"), E, {})
    ok(f["usd"] == 40.10 and f["usd_b"], "A1.3: metered above the cap -> the metered figure, >=")
    E["ccost"][("c1", "r")]["COST"] = "36.00"
    f = claude_cell(row("c1", "1", "CAP-COST", "none"), E, {})
    ok(f["usd"] == 37.21 and f["usd_b"], "A1.3: metered below the cap -> the cap its end marker names")
    f = claude_cell(row("c2", "1", "CAP-COST", "spec-change"), E, {})
    ok(f["usd"] == 24.29, "A1.3: a cumulative phase-2 cut enters at its metered 24.29, never the 18.60 below its own spend")
    ok(f["wall"] == 130.0, "a spec-change cell's wall is the sum of its two phases")
    E["cwall"][("c4", "r")] = [{"phase": "1", "wall_last_meter": "wall 10/144000", "held_s": "0", "end_kind": "LANDED"}]
    E["root"]["c4"] = "r"
    E["cwall_all"] = {"c4": {"r": E["cwall"][("c4", "r")], "copy": [dict(E["cwall"][("c4", "r")][0]),
                             {"phase": "2", "wall_last_meter": "wall 5/72000", "held_s": "0", "end_kind": "LANDED"}]}}
    ok(claude_cell(row("c4", "0", "-", "spec-change"), E, {})["wall"] == 15.0, "ADDENDUM 3: phase 2 from the one copy root that passes the copy check")
    E["cwall_all"]["c4"]["copy"][0]["wall_last_meter"] = "wall 11/144000"
    ok(claude_cell(row("c4", "0", "-", "spec-change"), E, {})["wall"] is None, "ADDENDUM 3: a copy whose phase 1 differs is refused")
    f = claude_cell(row("c2", "0", "-", "none"), E, {})
    ok(f["wall"] is None, "a one-phase condition whose cell holds two phases is unmeasured, never a silent pick")
    f = claude_cell(row("c3", "0", "-", "none"), E, {})
    ok(f["usd_b"] and f["wall_b"], "VOID(UNDERSTATED) marks dollars >=; a wall within one tick of its cap marks wall >=")
    ok(claude_cell(row("c9", "0", "-", "none"), E, {})["usd"] is None, "no tracked row and no re-run -> unmeasured")
    # summarise and the checks
    c = {"status": "DONE", "cells": [{"usd": 1.0, "usd_b": False}, {"usd": 2.0, "usd_b": False}, {"usd": None, "usd_b": False}]}
    ok(summarise(c, "usd")[2] == "unmeasured", "any cell unmeasured -> the condition is unmeasured")
    c = {"status": "DONE", "cells": [{"usd": 1.0, "usd_b": True}, {"usd": 2.0, "usd_b": False}, {"usd": 3.0, "usd_b": False}]}
    ok(summarise(c, "usd") == (2.0, True, ""), "v2's median rule, imported unchanged")
    ok(summarise({"status": "INEXPR", "cells": []}, "usd")[2] == "—" and summarise({"status": "DECLARED", "cells": []}, "usd")[2] == "declared", "marks")
    ok(show((2.0, True, ""), "usd") == "≥ $2.00" and show((61.4, False, ""), "wall") == "61 s", "formatting")
    ok(repro_cause({"wall_copy_root": "x"}).startswith("A3.1") and repro_cause({"usd_src": "a.p1_COST + b.p2_COST"}).startswith("SC")
       and repro_cause({"usd_src": "a.final_COST"}) == "UNEXPLAINED", "every reproduction row carries its cause, or UNEXPLAINED")
    print("selftest OK (%d arms)" % n)
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--map")
    ap.add_argument("--ev")
    ap.add_argument("--out")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not (a.map and a.ev):
        ap.error("--map and --ev are required")
    conds, prov, fails = build(a.map, a.ev)
    head = subprocess.run(["git", "-C", REPO, "rev-parse", "--short=12", "HEAD"], capture_output=True, text=True).stdout.strip()
    body, checks = [], []
    for cur, tag, unit in (("usd", "$", "modelled list-price dollars"), ("wall", "W", "wall seconds")):
        b, ck, fl = render(conds, cur, tag, unit)
        body += b
        checks.append(ck)
        fails += fl
    body += render_split(conds)
    repro = [(k, f) for k, f in prov if f.get("rerun") is not None and f.get("usd_src", "").startswith(("evidence", "harness"))]
    dis = [(k, f) for k, f in repro if abs(f["rerun"] - f["usd"]) >= 0.01 and "cap" not in f.get("usd_src", "")]
    capped = [(k, f) for k, f in prov if f.get("lb_reason") == "CAP-COST"]
    body.append("\n## Rule 1's reproduction (ADDENDUM 2 A2.3): tracked cost of record against the cell_meter re-run\n")
    unexpl = sum(1 for k, f in dis if repro_cause(f) == "UNEXPLAINED")
    body.append("%d cells carry both; %d differ by a cent or more (listed; they do NOT stop the run); %d of them have no registered cause." % (
        len(repro), len(dis), unexpl))
    body.append("\n| cell | tracked (of record) | re-run | difference | cause (ADDENDUM 3 A3.2) |\n|---|---|---|---|---|")
    body += ["| %s | %.4f | %.4f | %+.4f | %s |" % (f["cell"], f["usd"], f["rerun"], f["rerun"] - f["usd"], repro_cause(f)) for k, f in dis]
    if unexpl:
        fails.append("%d reproduction difference(s) with no registered cause" % unexpl)
    body.append("\n## The CAP-COST cells (A1.3): the cap, the metered dollars and which entered\n")
    body.append("| cell | condition | cap named by its end marker | figure entered | source |\n|---|---|---|---|---|")
    body += ["| %s | %s | %s | %s | %s |" % (f["cell"], "/".join(k), "-" if f.get("cap") is None else "%.2f" % f["cap"],
             "unmeasured" if f["usd"] is None else "%.4f" % f["usd"], f["usd_src"]) for k, f in capped]
    body.append("\n## Per-cell figures and their sources (every table number derives from these rows)\n")
    body.append("| model | problem | field | arm | extras | cell | dollars | wall s | lower bound | dollar source | wall source |")
    body.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for k, f in prov:
        body.append("| %s | %s | %s | %s | %s | %s | %s |" % (" | ".join(k), f["cell"],
            "unmeasured" if f["usd"] is None else ("≥ " if f["usd_b"] else "") + "%.4f" % f["usd"],
            "unmeasured" if f["wall"] is None else ("≥ " if f["wall_b"] else "") + "%.1f" % f["wall"],
            f["lb_reason"], f.get("usd_src", "-"), f.get("wall_src", "-") + ("; second method: " + ", ".join(f["facts"]) if f.get("facts") else "")))
    hdr = ["# RESULT: THE COMPLETE PILOT MATRIX IN DOLLARS AND WALL TIME (arXiv v3)",
           "## Printed by `harness/systems-v3/tables_v3.py` over the working tree at repo head `%s`, from `%s` and `%s`. Registered in "
           "`REGISTRATION-cost-tables-v3-2026-09-29.md` (§V1–§V6, ADDENDA 1–3), committed before this ran. The instrument and its "
           "inputs may be newer than that head, so they are named by CONTENT (git blob ids, checkable at any commit with "
           "`git hash-object <file>`): %s." % (head, os.path.relpath(os.path.abspath(a.map), REPO), os.path.relpath(os.path.abspath(a.ev), REPO),
               " · ".join("`%s` %s" % (os.path.basename(f), blob(f)) for f in [os.path.abspath(__file__), os.path.abspath(a.map)] +
                          [os.path.join(a.ev, n) for n in INPUTS])), ""]
    hdr += ["**%s**" % c for c in checks] + ["**Second methods: %d disagreement(s)%s.**" % (len(fails) - sum(1 for f in fails if "CHECK" in f),
            "" if not fails else "; " + "; ".join(fails[:6]))]
    exceeds = sorted({f["cell"] for k, f in prov if "EXCEEDS-METER" in f.get("usd_src", "")})
    unm = [(cur, k, f["cell"], f[cur + "_src"] if cur == "wall" else f["usd_src"]) for cur in ("usd", "wall") for k, f in prov
           if f[cur] is None and conds[k]["status"] == "DONE"]
    hdr += ["",
        "⛔ **A descriptive reading over the complete matrix: no test, no p-value, no verdict on the arms; the registered tests remain §4's.** "
        "A cheaper arm is cheaper, not better.",
        "",
        "- **Dollars are MODELLED at list prices, not invoices** (every cell ran on a subscription): one schedule per vendor, both pages read "
        "2026-09-29 (`rates-gemini-2026-09-29.tsv`; Claude `rates.tsv` rows re-read and agreeing). Claude: every record at its served "
        "model's rates, so an Opus cell's Sonnet subagents are priced at Sonnet's. agy: per request at the tier of its prompt "
        "(input + cache read), thinking inside output and priced once (ADDENDUM 2 A2.1). Context-caching STORAGE is not priced.",
        "- **The Pro upper price tier (prompts over 200k) is selected by NO request in these data** (largest Pro prompt 144,717); only the "
        "selftest exercises that arm (A2.4).",
        "- **Wall includes the box.** It depends on what else the run box was doing and on the vendor's service at that hour. Not extracted "
        "per cell here: the records that carry the concurrency (`claude_live_at_fire` in the Claude fire logs, the agy concurrency column, "
        "the one-heavy-job lock). A wall `≥` set by timing (within one turn timeout of the wall cap) errs toward the floor (A2.5).",
        "- **`≥`** a floor (CAP-COST, FLOOR, DEADLINE by the record; a meter `VOID(UNDERSTATED)`; a wall at its cap). A CAP-COST cell's dollars "
        "are the larger of its metered cost and the cap its end marker names (A1.3). **`—`** inexpressible. **`declared`** unreached at the cap.",
        "- **Priced from per-request records larger than the meter's fold (EXCEEDS-METER, flagged):** %s." % (", ".join(exceeds) or "none"),
        "- Rule 1's reproduction differences have two causes, both shown at the object (ADDENDUM 3 A3.2): the SC cells' probe-separated "
        "tracked columns, and the copy-root cells' re-run of the landing's slug alone.",
        "",
        "## Unmeasured cells in DONE conditions, per currency",
        "| currency | model | problem | field | arm | extras | cell | why |", "|---|---|---|---|---|---|---|---|"] + [
        "| %s | %s | %s | %s |" % (cur, " | ".join(k), c, why) for cur, k, c, why in unm] + ([] if unm else ["| none | | | | | | | |"])
    txt = "\n".join(hdr + body) + "\n"
    if a.out:
        open(a.out, "w", encoding="utf-8").write(txt)
    else:
        sys.stdout.write(txt)
    for c in checks:
        print(c, file=sys.stderr)
    for f in fails[:40]:
        print("FAIL " + f, file=sys.stderr)
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
