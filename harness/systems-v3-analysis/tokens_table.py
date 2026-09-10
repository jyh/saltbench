#!/usr/bin/env python3
"""tokens_table.py - the TOKEN figures beside the DOLLAR figures, per cell and per arm.

Standing order, the Captain 2026-09-10 09:3x: "please info bench to produce token costs (in
addition to dollar costs)."  Dollars are DERIVED - they move with list pricing and with which
model served the cell.  Tokens are the physical quantity the quota pools meter, and P1 is a
cross-model comparison, so a result expressed only in dollars cannot be compared across models.

Every number here comes from cell_meter.py's own JSON over the cell's transcripts.  Nothing is
retyped and nothing is derived backwards from a price.  A cell whose account cannot be resolved
is reported UNRESOLVED, never guessed; a cell the meter VOIDs is reported VOID, never 0.

The account is DERIVED by locating the transcript tree under <cfg>/projects/, because until
2026-09-10 no cell recorded the account it ran on.
"""
import json, os, subprocess, sys, glob

HOME = os.path.expanduser("~")
BIN = os.path.join(HOME, "cells-specchange-1", "_bin", "cell_meter.py")
ROOTS = sys.argv[1:] or [os.path.join(HOME, "cells-matrix1")]

def cfg_dirs():
    return sorted(d for d in glob.glob(os.path.join(HOME, ".claude*")) if os.path.isdir(d))

def account_of(cfg):
    try:
        d = json.load(open(os.path.join(cfg, ".claude.json")))
        a = d["oauthAccount"]
        return a.get("emailAddress", "?"), a.get("accountUuid", "?")[:8]
    except Exception:
        return ("?", "?")

def find_transcripts(cell_repo):
    """Return (path, cfg) for the transcript tree of this repo, or (None, None)."""
    slug = cell_repo.replace("/", "-")
    hits = []
    for cfg in cfg_dirs():
        p = os.path.join(cfg, "projects", slug)
        if os.path.isdir(p) and os.listdir(p):
            hits.append((p, cfg))
    if len(hits) > 1:
        return ("MULTI:" + ";".join(c for _, c in hits), None)
    return hits[0] if hits else (None, None)

rows = []
for root in ROOTS:
    for cell in sorted(glob.glob(os.path.join(root, "*"))):
        cid = os.path.basename(cell)
        if not os.path.isdir(os.path.join(cell, "ctl")):
            continue
        def ctl(name):
            p = os.path.join(cell, "ctl", name)
            return open(p).read().strip() if os.path.exists(p) else "-"
        arm = ctl("arm")
        path, cfg = find_transcripts(os.path.join(cell, "repo"))
        if path is None:
            rows.append(dict(root=os.path.basename(root), cell=cid, arm=arm, acct="UNRESOLVED",
                             status="NO-TRANSCRIPT")); continue
        if path.startswith("MULTI:"):
            rows.append(dict(root=os.path.basename(root), cell=cid, arm=arm, acct="MULTI",
                             status=path)); continue
        email, uuid8 = account_of(cfg)
        out = subprocess.run([sys.executable, BIN, path, "--json"],
                             capture_output=True, text=True)
        try:
            m = json.loads(out.stdout)
        except Exception:
            rows.append(dict(root=os.path.basename(root), cell=cid, arm=arm, acct=email,
                             status="METER-UNPARSABLE")); continue
        if m["void"]:
            rows.append(dict(root=os.path.basename(root), cell=cid, arm=arm, acct=email,
                             status="VOID:" + m["void"][0][:40])); continue
        tot = dict(input=0, cache_write_5m=0, cache_write_1h=0, cache_read=0, output=0)
        models = set()
        for lane in ("head", "exec"):
            for mdl, v in m["receipt"].get(lane, {}).items():
                models.add(mdl)
                for k in tot:
                    tot[k] += v.get(k, 0)
        rows.append(dict(root=os.path.basename(root), cell=cid, arm=arm, acct=email,
                         status="OK", models="+".join(sorted(models)),
                         records=m["records"], T=m["T"], cost=m["COST"], **tot))

hdr = ["root", "cell", "arm", "acct", "status", "models", "records",
       "input", "cache_write_5m", "cache_write_1h", "cache_read", "output", "T", "cost"]
print("\t".join(hdr))
for r in rows:
    print("\t".join(str(r.get(h, "-")) for h in hdr))
