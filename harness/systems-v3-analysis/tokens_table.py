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

# ⛔⛔ THE FLOOR RULE, added 2026-09-10. The meter VOIDs a cell whose transcript carries an INTERRUPTED
# record, and it is right to: "the client stops writing usage where the interrupt lands, so this sum is
# a LOWER BOUND, not a price." But a VOID is not a gap -- the meter still computes T and COST from the
# 99%+ of records that ARE complete, and its own message says what that number is.
# ⇒ With --floors those cells are RETAINED and labelled FLOOR, never merged into the priced set.
# WHY IT MATTERS AND IS NOT BOOKKEEPING: dropping them is an ARM-CORRELATED exclusion (plain 44%
# priced, salt-diet 67%), so the strict aggregate compares two differently-selected subsets. Retaining
# them as floors is safe in the direction that matters -- a floor UNDERSTATES, the understatement
# falls more on the control arm, and a bias against the arm under test cannot MANUFACTURE a positive.
# ⛔ LIMIT: that argument licenses a NUMBER reported as a floor. It does NOT license a VERDICT.

HOME = os.path.expanduser("~")
BIN = os.path.join(HOME, "cells-specchange-1", "_bin", "cell_meter.py")
ARGS = [a for a in sys.argv[1:] if a != "--floors"]
FLOORS = "--floors" in sys.argv[1:]
ROOTS = ARGS or [os.path.join(HOME, "cells-matrix1")]

def cfg_dirs():
    return sorted(d for d in glob.glob(os.path.join(HOME, ".claude*")) if os.path.isdir(d))

def account_of(cfg):
    try:
        d = json.load(open(os.path.join(cfg, ".claude.json")))
        a = d["oauthAccount"]
        # the uuid PREFIX, never the account name or address: an infrastructure name may not sit
        # in the public tree, and a uuid prefix is an opaque, stable, auditable identifier.
        return a.get("accountUuid", "?")[:8], a.get("accountUuid", "?")[:8]
    except Exception:
        return ("UNREADABLE", "UNREADABLE")

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
        understated = m["void"] and all("UNDERSTATED" in v for v in m["void"])
        if m["void"] and not (FLOORS and understated and m.get("COST") is not None):
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
                         status=("FLOOR" if m["void"] else "OK"), models="+".join(sorted(models)),
                         records=m["records"], T=m["T"], cost=m["COST"], **tot))

hdr = ["root", "cell", "arm", "acct", "status", "models", "records",
       "input", "cache_write_5m", "cache_write_1h", "cache_read", "output", "T", "cost"]
print("\t".join(hdr))
for r in rows:
    print("\t".join(str(r.get(h, "-")) for h in hdr))
