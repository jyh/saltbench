#!/usr/bin/env python3
"""meter.py — recover the METERED SUM and the audit facts from a Claude Code session jsonl.

    meter.py <session.jsonl> [--result result.json] [--pattern-file <regex file>] [--live]
    meter.py --self-test

THE UNIT (PRE-REG §9, unchanged): metered sum = input + cache_creation + cache_read + output, summed
over ALL calls in the episode. A CALL is one distinct `message.id` among `type=="assistant"` lines:
one API call lands as one line PER CONTENT BLOCK, each carrying the same usage (measured 08/28,
45 lines = 22 calls). Summing lines would overcount by the number of content blocks.
Classes named because a successor must state them (refuter distillation §7): SUBAGENT calls appear
as isSidechain=true lines — counted AND flagged (they VOID a stage-0 episode); COMPACTION lands as
a system/summary record — counted where its usage lands, and the count is reported; API-LEVEL
RETRIES (429/5xx) never land in the jsonl and are not billed — the metered sum is what LANDED.
`--live` tolerates a truncated last line (the watchdog reads a file being written).
"""
import argparse, collections, json, os, re, sys

CLASSES = ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")


def load(path, live=False):
    recs = []
    with open(path, "rb") as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            try:
                recs.append(json.loads(line))
            except Exception:
                if live:
                    continue  # a line still being written
                raise SystemExit("bad json at line %d" % (i + 1))
    return recs


def meter(recs, pattern=None):
    by_id = collections.OrderedDict()
    sidechain = 0; missing_class = []; models = collections.Counter(); tiers = collections.Counter()
    bash_cmds = []; tool_uses = collections.Counter(); thinking = 0; compactions = 0
    first_ts = None; last_ts = None; versions = set()
    for r in recs:
        t = r.get("type")
        if t == "system" and r.get("subtype") in ("compact_boundary", "compaction"):
            compactions += 1
        if t == "summary":
            compactions += 1
        if t != "assistant":
            continue
        if r.get("isSidechain"):
            sidechain += 1
        m = r.get("message") or {}
        mid = m.get("id") or r.get("requestId") or r.get("uuid")
        u = m.get("usage") or {}
        if mid not in by_id:
            for c in CLASSES:
                if c not in u:
                    missing_class.append((mid, c))
            by_id[mid] = {c: int(u.get(c, 0) or 0) for c in CLASSES}
            by_id[mid]["thinking"] = int(((u.get("output_tokens_details") or {}).get("thinking_tokens")) or 0)
            models[m.get("model")] += 1; tiers[u.get("service_tier")] += 1
            versions.add(r.get("version"))
            ts = r.get("timestamp")
            if ts:
                first_ts = first_ts or ts; last_ts = ts
        for c in m.get("content") or []:
            if isinstance(c, dict) and c.get("type") == "tool_use":
                tool_uses[c.get("name")] += 1
                if c.get("name") == "Bash":
                    bash_cmds.append(((c.get("input") or {}).get("command") or ""))
    calls = len(by_id)
    tot = {c: sum(v[c] for v in by_id.values()) for c in CLASSES}
    thinking = sum(v["thinking"] for v in by_id.values())
    metered = sum(tot.values())
    net_hits = []
    if pattern:
        rx = re.compile(pattern)
        net_hits = [c for c in bash_cmds if rx.search(c)]
    return {
        "calls": calls, "metered_sum": metered, "classes": tot, "thinking_tokens": thinking,
        "per_call_max": max((sum(v[c] for c in CLASSES) for v in by_id.values()), default=0),
        "models": dict(models), "service_tiers": dict(tiers), "claude_versions": sorted(x for x in versions if x),
        "sidechain_lines": sidechain, "compactions": compactions, "missing_usage_class": missing_class[:5],
        "tool_uses": dict(tool_uses), "bash_commands": len(bash_cmds), "network_hits": net_hits,
        "first_call_ts": first_ts, "last_call_ts": last_ts,
        "void": bool(sidechain or net_hits or missing_class),
    }


def crosscheck(m, result):
    out = {}
    if not result:
        return out
    out["cli_num_turns"] = result.get("num_turns")
    ru = result.get("usage") or {}
    out["cli_usage"] = {c: ru.get(c) for c in CLASSES}
    out["cli_subtype"] = result.get("subtype"); out["cli_is_error"] = result.get("is_error")
    out["cli_total_cost_usd_REPORTED_NOT_USED"] = result.get("total_cost_usd")
    out["usage_matches_jsonl"] = all(ru.get(c) is None or int(ru.get(c)) == m["classes"][c] for c in CLASSES)
    return out


def self_test():
    ok = True
    def check(cond, msg):
        nonlocal ok
        print(("PASS " if cond else "FAIL ") + msg); ok = ok and cond
    u = {"input_tokens": 3, "cache_creation_input_tokens": 100, "cache_read_input_tokens": 1000, "output_tokens": 50, "output_tokens_details": {"thinking_tokens": 7}}
    a = lambda mid, content, **kw: dict({"type": "assistant", "message": {"id": mid, "model": "claude-sonnet-5", "usage": u, "content": content}, "timestamp": "t"}, **kw)
    recs = [a("m1", [{"type": "thinking"}]), a("m1", [{"type": "text", "text": "x"}]), a("m1", [{"type": "tool_use", "name": "Bash", "input": {"command": "ls"}}]),
            a("m2", [{"type": "tool_use", "name": "Read", "input": {}}]), {"type": "user"}]
    m = meter(recs, pattern="curl")
    check(m["calls"] == 2, "3 lines of one message.id + 1 = 2 calls (dedupe by message.id)")
    check(m["metered_sum"] == 2 * 1153, "metered sum = 2 x (3+100+1000+50) = %d" % m["metered_sum"])
    check(m["thinking_tokens"] == 14 and m["tool_uses"] == {"Bash": 1, "Read": 1}, "thinking and tool counts")
    check(not m["void"], "clean transcript is not void")
    m2 = meter(recs + [a("m3", [], isSidechain=True)], pattern="curl")
    check(m2["sidechain_lines"] == 1 and m2["void"], "a sidechain line voids")
    m3 = meter(recs + [a("m4", [{"type": "tool_use", "name": "Bash", "input": {"command": "curl x"}}])], pattern="curl")
    check(m3["network_hits"] == ["curl x"] and m3["void"], "a network hit voids")
    bad = dict(a("m5", []))
    bad["message"]["usage"] = {"input_tokens": 1}
    m4 = meter(recs + [bad])
    check(m4["missing_usage_class"] and m4["void"], "a usage record missing a class voids (drift is a hole, not a zero)")
    cc = crosscheck(m, {"num_turns": 2, "usage": {"input_tokens": 6, "cache_creation_input_tokens": 200, "cache_read_input_tokens": 2000, "output_tokens": 100}})
    check(cc["usage_matches_jsonl"], "cli usage cross-check matches")
    cc2 = crosscheck(m, {"num_turns": 2, "usage": {"input_tokens": 7}})
    check(not cc2["usage_matches_jsonl"], "cli usage mismatch is reported, not smoothed")
    print("SELF-TEST", "OK" if ok else "FAILED")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl", nargs="?"); ap.add_argument("--result"); ap.add_argument("--pattern-file"); ap.add_argument("--live", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    pat = open(a.pattern_file).read().strip() if a.pattern_file else None
    m = meter(load(a.jsonl, live=a.live), pattern=pat)
    if a.result and os.path.exists(a.result):
        try:
            m["crosscheck"] = crosscheck(m, json.load(open(a.result)))
        except Exception as e:
            m["crosscheck"] = {"error": str(e)}
    print(json.dumps(m, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
