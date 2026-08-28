#!/usr/bin/env python3
"""meter.py — recover the METERED SUM and the audit facts from a Claude Code session jsonl.

    meter.py <session.jsonl> [--result result.json] [--ep <EP>] [--escape-file <regex>] [--url-file <regex>]
                             [--extra <other.jsonl> ...] [--live]
    meter.py --self-test

THE UNIT (PRE-REG §9, unchanged): metered sum = input + cache_creation + cache_read + output over ALL
calls in the episode. A CALL is one distinct `message.id` among `type=="assistant"` lines: one API call
lands as one line PER CONTENT BLOCK, each carrying the same usage (measured 08/28, 45 lines = 22
calls). Summing lines would overcount by the number of content blocks.

Rules the refuter pass (a03bd3c) forced, each a named field below:
  * no message.id and no requestId  -> `no_call_id_lines`, VOID (never a per-line uuid fallback — M6)
  * `isApiErrorMessage` / model `<synthetic>` lines -> excluded from calls, counted `api_error_lines` (M7)
  * compaction: `compact_boundary` records carry `compactMetadata.preTokens/postTokens` and NO usage —
    the summarising call lands NOWHERE, so its floor is reported separately and the CLI's larger
    figure governs UPWARD (`jsonl_undercount`) (M2, M8)
  * subagents: `isSidechain` lines OR spawn tool_uses (Agent/Task/Workflow/Skill) -> VOID(SUBAGENT) (M3)
  * a truncated last line is RECORDED (`truncated_last_line`), never silently skipped (M5)
  * ESCAPE audit over EVERY tool_use input (Bash command; Read/Edit/Write/Glob/Grep paths): a hit whose
    tool_result is the hook's BLOCKED text is an ATTEMPT (counted); an unblocked hit VOIDs (F1/L1/R4)
  * URL mentions are counted apart from escapes and never VOID on their own (L7)
"""
import argparse, collections, json, os, re, sys

CLASSES = ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")
SPAWN = {"Agent", "Task", "Workflow", "Skill"}
PATH_TOOLS = {"Read": ("file_path",), "Edit": ("file_path",), "Write": ("file_path",), "MultiEdit": ("file_path",),
              "NotebookEdit": ("notebook_path",), "Glob": ("path",), "Grep": ("path",), "LS": ("path",)}
BLOCKED_MARK = "BLOCKED by the episode harness"


def load(path, live=False):
    recs, truncated = [], 0
    with open(path, "rb") as f:
        lines = f.read().split(b"\n")
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        try:
            recs.append(json.loads(line))
        except Exception:
            if i == len(lines) - 1 or i == len(lines) - 2:
                truncated += 1  # a line still being (or never finished) written
            elif live:
                truncated += 1
            else:
                raise SystemExit("bad json at line %d (not the last line)" % (i + 1))
    return recs, truncated


def _tool_results(recs):
    """tool_use_id -> result text (first 400 chars) from user records."""
    out = {}
    for r in recs:
        if r.get("type") != "user":
            continue
        for c in (r.get("message") or {}).get("content") or []:
            if isinstance(c, dict) and c.get("type") == "tool_result":
                cc = c.get("content")
                txt = cc if isinstance(cc, str) else " ".join(x.get("text", "") for x in (cc or []) if isinstance(x, dict))
                out[c.get("tool_use_id")] = (txt or "")[:400]
    return out


def meter(recs, ep=None, escape_re=None, url_re=None, truncated=0):
    by_id = collections.OrderedDict()
    sidechain = 0; missing_class = []; models = collections.Counter(); tiers = collections.Counter()
    tool_uses = collections.Counter(); compactions = []; api_error = 0; no_call_id = 0
    escapes_blocked = []; escapes_unblocked = []; url_mentions = 0; spawn_uses = 0; dotdot = 0
    first_ts = None; last_ts = None; versions = set(); cost_state = None
    results = _tool_results(recs)
    rx_e = re.compile(escape_re) if escape_re else None
    rx_u = re.compile(url_re) if url_re else None
    for r in recs:
        t = r.get("type")
        if t == "system" and r.get("subtype") in ("compact_boundary", "compaction"):
            cm = r.get("compactMetadata") or {}
            compactions.append({"preTokens": cm.get("preTokens"), "postTokens": cm.get("postTokens")})
        if t == "summary":
            compactions.append({"preTokens": None, "postTokens": None, "kind": "summary-record"})
        if t == "cost-state":
            cost_state = r.get("modelUsage") or r.get("costState") or {k: v for k, v in r.items() if k != "type"}
        if t != "assistant":
            continue
        if r.get("isSidechain"):
            sidechain += 1
        m = r.get("message") or {}
        u = m.get("usage") or {}
        if r.get("isApiErrorMessage") or m.get("model") == "<synthetic>":
            api_error += 1
            continue
        mid = m.get("id") or r.get("requestId")
        if not mid:
            no_call_id += 1
            continue
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
            if not (isinstance(c, dict) and c.get("type") == "tool_use"):
                continue
            name = c.get("name"); inp = c.get("input") or {}
            tool_uses[name] += 1
            if name in SPAWN:
                spawn_uses += 1
            probe = None
            if name == "Bash":
                probe = inp.get("command") or ""
            elif name in PATH_TOOLS:
                probe = " ".join(str(inp.get(k) or "") for k in PATH_TOOLS[name])
            if probe is None:
                continue
            raw = probe.strip()
            if ".." in raw:
                dotdot += 1
            if name in PATH_TOOLS and ep and raw:
                # a file tool's path must be the episode's own tree (or /tmp); any other absolute path is an escape
                if raw.startswith(ep + "/") or raw == ep or not os.path.isabs(raw) or raw.startswith(("/tmp", "/private/tmp")):
                    continue
                escapes_unblocked.append("%s %s" % (name, probe))
                continue
            p2 = probe.replace(ep + "/", "/EP/") if ep else probe   # own-episode paths are neutral for the Bash regex
            if rx_e and rx_e.search(p2):
                res = results.get(c.get("id"), "")
                (escapes_blocked if BLOCKED_MARK in res else escapes_unblocked).append("%s %s" % (name, probe))
            elif rx_u and rx_u.search(probe):
                url_mentions += 1
    calls = len(by_id)
    tot = {c: sum(v[c] for v in by_id.values()) for c in CLASSES}
    thinking = sum(v["thinking"] for v in by_id.values())
    metered = sum(tot.values())
    comp_floor = sum(int(x.get("preTokens") or 0) + int(x.get("postTokens") or 0) for x in compactions)
    void_reasons = []
    if sidechain or spawn_uses: void_reasons.append("SUBAGENT")
    if escapes_unblocked: void_reasons.append("ESCAPE")
    if missing_class: void_reasons.append("USAGE_SCHEMA")
    if no_call_id: void_reasons.append("NO_CALL_ID")
    return {
        "calls": calls, "metered_sum": metered, "classes": tot, "thinking_tokens": thinking,
        "per_call_max": max((sum(v[c] for c in CLASSES) for v in by_id.values()), default=0),
        "models": dict(models), "service_tiers": dict(tiers), "claude_versions": sorted(x for x in versions if x),
        "sidechain_lines": sidechain, "spawn_tool_uses": spawn_uses, "api_error_lines": api_error, "no_call_id_lines": no_call_id,
        "compactions": len(compactions), "compaction_detail": compactions, "compaction_input_floor": comp_floor,
        "metered_sum_incl_compaction_floor": metered + comp_floor,
        "missing_usage_class": missing_class[:5], "truncated_last_line": bool(truncated),
        "tool_uses": dict(tool_uses), "bash_commands": tool_uses.get("Bash", 0),
        "escape_attempts_blocked": escapes_blocked, "escape_unblocked": escapes_unblocked,
        "url_mentions": url_mentions, "dotdot_paths": dotdot, "cost_state": cost_state,
        "first_call_ts": first_ts, "last_call_ts": last_ts,
        "void_reasons": void_reasons, "void": bool(void_reasons),
    }


def crosscheck(m, result):
    out = {}
    if not result:
        return out
    out["cli_num_turns"] = result.get("num_turns")
    out["num_turns_matches_calls"] = (result.get("num_turns") == m["calls"]) if result.get("num_turns") is not None else None
    ru = result.get("usage") or {}
    out["cli_usage"] = {c: ru.get(c) for c in CLASSES}
    out["cli_minus_jsonl"] = {c: (int(ru[c]) - m["classes"][c]) for c in CLASSES if ru.get(c) is not None}
    out["cli_subtype"] = result.get("subtype"); out["cli_is_error"] = result.get("is_error")
    out["cli_total_cost_usd_REPORTED_NOT_USED"] = result.get("total_cost_usd")
    over = sum(max(0, d) for d in out["cli_minus_jsonl"].values())
    out["jsonl_undercount"] = over
    cli_sum = sum(int(ru.get(c) or 0) for c in CLASSES) if ru else 0
    out["metered_sum_governing"] = max(m["metered_sum"], cli_sum)  # the larger figure governs (M8)
    out["usage_matches_jsonl"] = all(d == 0 for d in out["cli_minus_jsonl"].values())
    return out


def self_test():
    ok = True
    def check(cond, msg):
        nonlocal ok
        print(("PASS " if cond else "FAIL ") + msg); ok = ok and cond
    ESC = "(^|[^A-Za-z0-9_./-])(curl|docker)([^A-Za-z0-9_-]|$)|/Users/[^ ]*/bench|/Users/[^ ]*/work/ep-"
    URL = "https?://"
    EP = "/Users/x/work/ep-own"
    u = {"input_tokens": 3, "cache_creation_input_tokens": 100, "cache_read_input_tokens": 1000, "output_tokens": 50, "output_tokens_details": {"thinking_tokens": 7}}
    def a(mid, content, **kw):
        return dict({"type": "assistant", "message": {"id": mid, "model": "claude-sonnet-5", "usage": u, "content": content}, "timestamp": "t"}, **kw)
    def tu(name, inp, tid): return {"type": "tool_use", "name": name, "input": inp, "id": tid}
    def tr(tid, text): return {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": tid, "content": text}]}}
    recs = [a("m1", [{"type": "thinking"}]), a("m1", [{"type": "text", "text": "x"}]), a("m1", [tu("Bash", {"command": "ls"}, "t1")]),
            a("m2", [tu("Read", {"file_path": EP + "/repo/a.py"}, "t2")]), {"type": "user"}]
    m = meter(recs, ep=EP, escape_re=ESC, url_re=URL)
    check(m["calls"] == 2, "3 lines of one message.id + 1 = 2 calls (dedupe by message.id)")
    check(m["metered_sum"] == 2 * 1153, "metered sum = 2 x (3+100+1000+50) = %d" % m["metered_sum"])
    check(m["thinking_tokens"] == 14 and m["tool_uses"] == {"Bash": 1, "Read": 1}, "thinking and tool counts")
    check(not m["void"], "clean transcript (own-episode Read) is not void")
    m2 = meter(recs + [a("m3", [], isSidechain=True)], ep=EP, escape_re=ESC)
    check(m2["void_reasons"] == ["SUBAGENT"], "a sidechain line voids as SUBAGENT")
    m2b = meter(recs + [a("m3b", [tu("Workflow", {}, "t9")])], ep=EP, escape_re=ESC)
    check("SUBAGENT" in m2b["void_reasons"], "a spawn tool_use voids as SUBAGENT")
    m3 = meter(recs + [a("m4", [tu("Bash", {"command": "curl x"}, "t4")])], ep=EP, escape_re=ESC)
    check(m3["escape_unblocked"] == ["Bash curl x"] and "ESCAPE" in m3["void_reasons"], "an unblocked escape voids")
    m3b = meter(recs + [a("m5", [tu("Bash", {"command": "curl x"}, "t5")]), tr("t5", BLOCKED_MARK + ": ...")], ep=EP, escape_re=ESC)
    check(m3b["escape_attempts_blocked"] == ["Bash curl x"] and not m3b["void"], "a hook-BLOCKED escape is an attempt, not a void")
    m3c = meter(recs + [a("m6", [tu("Read", {"file_path": "/Users/jyh/bench/harness/data/verified.json"}, "t6")])], ep=EP, escape_re=ESC)
    check(m3c["escape_unblocked"] and m3c["void"], "a Read of a host path outside the episode voids")
    m3d = meter(recs + [a("m7", [tu("Bash", {"command": "grep -rn http://x docs/"}, "t7")]), tr("t7", BLOCKED_MARK)], ep=EP, escape_re=ESC, url_re=URL)
    check(m3d["url_mentions"] == 1 and not m3d["void"], "a URL mention is counted, never a void")
    m3e = meter(recs + [a("m8", [tu("Bash", {"command": EP + "/rt python -m pytest"}, "t8")])], ep=EP, escape_re=ESC)
    check(not m3e["void"], "own rt (path under the episode) is not an escape")
    bad = a("m9", []); bad["message"]["usage"] = {"input_tokens": 1}
    m4 = meter(recs + [bad], ep=EP)
    check(m4["missing_usage_class"] and "USAGE_SCHEMA" in m4["void_reasons"], "a usage record missing a class voids (drift is a hole, not a zero)")
    noid = {"type": "assistant", "message": {"usage": u, "content": []}, "uuid": "u1"}
    m5 = meter(recs + [noid, noid], ep=EP)
    check(m5["calls"] == 2 and m5["no_call_id_lines"] == 2 and "NO_CALL_ID" in m5["void_reasons"], "no message.id: not counted per line, VOIDs")
    syn = {"type": "assistant", "isApiErrorMessage": True, "message": {"id": "uuid-x", "model": "<synthetic>", "usage": {c: 0 for c in CLASSES}, "content": []}}
    m6 = meter(recs + [syn], ep=EP)
    check(m6["calls"] == 2 and m6["api_error_lines"] == 1, "a synthetic API-error line is excluded from calls")
    comp = {"type": "system", "subtype": "compact_boundary", "compactMetadata": {"preTokens": 900000, "postTokens": 11000}}
    m7 = meter(recs + [comp], ep=EP)
    check(m7["compactions"] == 1 and m7["compaction_input_floor"] == 911000 and m7["metered_sum_incl_compaction_floor"] == 2306 + 911000, "compaction floor reported from compactMetadata")
    cc = crosscheck(m, {"num_turns": 2, "usage": {"input_tokens": 6, "cache_creation_input_tokens": 200, "cache_read_input_tokens": 2000, "output_tokens": 100}})
    check(cc["usage_matches_jsonl"] and cc["num_turns_matches_calls"] and cc["metered_sum_governing"] == 2306, "cli cross-check matches; jsonl governs when equal")
    cc2 = crosscheck(m, {"num_turns": 3, "usage": {"input_tokens": 900006, "cache_creation_input_tokens": 200, "cache_read_input_tokens": 2000, "output_tokens": 100}})
    check(cc2["jsonl_undercount"] == 900000 and cc2["metered_sum_governing"] == 902306 and cc2["num_turns_matches_calls"] is False, "the larger CLI figure governs upward; num_turns mismatch is flagged")
    import tempfile
    d = tempfile.mkdtemp(); p = os.path.join(d, "t.jsonl")
    with open(p, "w") as f:
        for r in recs: f.write(json.dumps(r) + "\n")
        f.write('{"type":"assistant","message":{"id":"m10","usage":{"input_tokens":1')
    recs2, tr2 = load(p)
    check(tr2 == 1 and len(recs2) == len(recs), "a truncated last line is recorded, not fatal")
    print("SELF-TEST", "OK" if ok else "FAILED")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl", nargs="?"); ap.add_argument("--result"); ap.add_argument("--ep")
    ap.add_argument("--escape-file"); ap.add_argument("--url-file"); ap.add_argument("--extra", nargs="*", default=[])
    ap.add_argument("--live", action="store_true"); ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    esc = open(a.escape_file).read().strip() if a.escape_file else None
    url = open(a.url_file).read().strip() if a.url_file else None
    recs, trunc = load(a.jsonl, live=a.live)
    m = meter(recs, ep=a.ep, escape_re=esc, url_re=url, truncated=trunc)
    if a.extra:
        m["extra_files"] = []
        for x in a.extra:
            r2, t2 = load(x, live=True)
            mm = meter(r2, ep=a.ep, escape_re=esc, url_re=url, truncated=t2)
            m["extra_files"].append({"file": x, "calls": mm["calls"], "metered_sum": mm["metered_sum"]})
    if a.result and os.path.exists(a.result):
        try:
            m["crosscheck"] = crosscheck(m, json.load(open(a.result)))
        except Exception as e:
            m["crosscheck"] = {"error": str(e)}
    print(json.dumps(m, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
