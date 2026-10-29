#!/usr/bin/env python3
"""attempts.py — read 1 as fired (O90 ADDENDUM 8 A8.1): one row per model attempt, derived from the reader's own records.

usage: attempts.py RUNDIR [--since ISO]   (RUNDIR holds run.log, out/meter.tsv and calls/*.json, as gemini's driver wrote them)

Joins meter.tsv (unit, session, ok) to calls/<stamp>-<session>.json (rc, status, tokens, duration, stderr) BY SESSION ID and
prints a TSV, then a summary. Read-only. A meter row with no call record, or a call record with no meter row, is printed as a
row with the missing half marked "-", and counted on the summary line: a join is never assumed complete.
"""
import collections, glob, json, os, sys

def main(rundir, since):
    meter = [l.rstrip("\n").split("\t") for l in open(os.path.join(rundir, "out", "meter.tsv"))][1:]
    calls = {}
    for f in glob.glob(os.path.join(rundir, "calls", "*.json")):
        if os.path.basename(f) < since: continue
        j = json.load(open(f)); calls[j["session"]] = j
    print("\t".join(["unit", "arm", "chunk", "session", "ok", "cause", "tokens", "seconds"]))
    seen, rows = set(), []
    for unit, session, _cost, ok, _served in meter:
        j = calls.get(session); seen.add(session)
        arm = unit.split("/")[1]; chunk = unit.split("#")[1]
        if j is None:
            rows.append((unit, arm, chunk, session, ok, "-", "-", "-")); continue
        t = j.get("turn") or {}; err = j.get("stderr_tail") or ""
        cause = ("ok" if j["ok"] else "print-timeout" if "print timeout after" in err
                 else "stream-interrupted" if "stream was interrupted" in (t.get("error") or "") else "other")
        rows.append((unit, arm, chunk, session, ok, cause, j["tokens"], round(t.get("duration_seconds") or 0)))
    orphans = [s for s in calls if s not in seen]
    for r in rows: print("\t".join(map(str, r)))
    by = collections.Counter((r[1], r[5]) for r in rows)
    tok = sum(r[6] for r in rows if r[6] != "-"); okn = sum(1 for r in rows if r[4] == "yes")
    chunks = collections.defaultdict(list)
    for r in rows: chunks[(r[0], r[1])].append(r[4] == "yes")
    unread = collections.Counter(arm for (u, arm), v in chunks.items() if not any(v))
    reached = collections.Counter(arm for (u, arm) in chunks)
    print(f"# attempts {len(rows)} · ok {okn} · tokens {tok} · tokens per ok read {tok // okn if okn else 'nan'}")
    print("# by arm x cause: " + " · ".join(f"{a} {c} {n}" for (a, c), n in sorted(by.items())))
    print("# chunks reached / UNREAD (every attempt failed): " + " · ".join(f"{a} {reached[a]}/{unread[a]}" for a in sorted(reached)))
    for c in sorted({r[5] for r in rows if r[5] != "-"}):
        cs = [r for r in rows if r[5] == c]
        print(f"# cause {c}: n {len(cs)} · mean tokens {sum(r[6] for r in cs) / len(cs):.0f} · mean seconds {sum(r[7] for r in cs) / len(cs):.0f}")
    print(f"# failed attempts' share of tokens: {sum(r[6] for r in rows if r[5] not in ('ok', '-')) / tok:.3f}")
    print(f"# join: meter rows with no call record {sum(1 for r in rows if r[5] == '-')} · call records with no meter row {len(orphans)}")

if __name__ == "__main__":
    a = sys.argv[1:]
    since = a[a.index("--since") + 1] if "--since" in a else ""
    main(a[0], since)
