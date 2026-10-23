#!/usr/bin/env python3
"""calls_to_green.py -- O90 [H3]: the calls an S2-Lean stage-B episode spends up to its FIRST GREEN compile of the task
file, read from the episode's own Claude Code transcript (session.jsonl) and the harness wrapper's log (rt.log).

DEFINITIONS (all derived from the episode's bytes; nothing typed per episode)
  tool call      every assistant `tool_use` block on the main thread (isSidechain false), in transcript order, 1-based
  API call       a distinct assistant `message.id` (the unit the meter's `calls` counts); `api` in the table counts
                 those that issued a tool call, `api_calls_total` all of them (compared with manifest `calls`)
  compile call   a Bash tool call whose command runs Lean on the task file:  [lake env] lean [-flags] [path/]task.lean
                 (direct, or through the episode's `rt` wrapper as ./rt, ../rt or <ep>/rt; a lean run on any OTHER
                 file -- scratch.lean, a copy of the task -- is NOT a compile call)
  rt rc          the wrapper logs START/END rc=N per invocation (rt.template). Each START is assigned to the last tool
                 call whose timestamp (floored to the second) is <= the START second. The rc of a task-file compile is
                 the rc of the matching rt END. Lean exits non-zero on an error; a `sorry` is only a WARNING (rc 0).
  diagnostics    in the call's tool_result text, for the task file only:
                   error : `task.lean:L:C: error:` and the tagged form `task.lean:L:C: error(lean.xxx):`, and lake's
                           marker-first form `error: ...task.lean:L:C:`; a bare line-initial `error:` is also counted
                   sorry : `task.lean:L:C: warning: declaration uses 'sorry'`
  visibility     the shell text after the lean invocation, up to the end of its pipeline, is classified:
                   OPAQUE   stdout redirected to a file or /dev/null; a `grep -c`/`grep -q`/`wc` stage; a positive
                            `grep PAT` whose PAT would not pass both an error line and the sorry line; any stage not
                            recognised below
                   TRUNC(N) `head -N`, `tail -N`, `sed -n 1,Np`: transparent only if the result holds < N lines
                   CLEAR    no stage, or `grep -v PAT` stages whose PAT matches neither an error nor the sorry line
  verdict        RED   a task-file error or sorry diagnostic is visible, or a task-file rt rc != 0
                 GREEN no such diagnostic, output CLEAR (or TRUNC that did not bite), AND rc evidence: an rt END rc=0
                       for the task file (GREEN), or -- no rt in the call -- the direct `lake env lean` form with a
                       clear output (GREEN_NORT, weaker: nothing proves the compile ran)
                 UNDET no diagnostic visible but the output was OPAQUE or possibly truncated
  first green    the 1-based tool-call index of the first GREEN/GREEN_NORT compile call; `first_maybe` is the first
                 GREEN or UNDET one, an optimistic bound -- where they differ the reading is ambiguous for that episode

usage:  calls_to_green.py --state <dir holding ep-*/> [--stage B] [--json out.json]
        calls_to_green.py --selftest      (synthetic fixtures; each detector driven red by a mutant)
exit: 0 ok · 1 a cross-check or selftest failed · 2 input error
"""
import argparse, glob, json, os, re, shlex, sys
from datetime import datetime, timezone

LEAN_TASK = re.compile(r"(?:^|[\s;&|('\"`])(?:lake\s+env\s+)?lean(?:\s+-{1,2}\S+)*\s+['\"]?(?:\S*/)?task\.lean(?![\w.])")
DIAG_ERR = [
    re.compile(r"(?:^|[\s/])task\.lean:\d+:\d+:\s*error(?:\([^)]*\))?:", re.M),
    re.compile(r"^error(?:\([^)]*\))?:.*task\.lean:\d+:\d+", re.M),
    re.compile(r"^error(?:\([^)]*\))?:", re.M),
]
DIAG_SORRY = re.compile(r"(?:^|[\s/])task\.lean:\d+:\d+:\s*warning:\s*declaration uses 'sorry'", re.M)
SAMPLE_ERR = "task.lean:12:3: error: unsolved goals"
SAMPLE_ERR_T = "task.lean:12:3: error(lean.unknownIdentifier): Unknown identifier `x`"
SAMPLE_SORRY = "task.lean:158:8: warning: declaration uses 'sorry'"
MUTANT = os.environ.get("CTG_MUTANT", "")  # selftest only: "nosorry" | "noerrtag" | "norc" | "nofilter"


def ts(s):
    return datetime.strptime(s[:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc).timestamp()


def result_text(c):
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        return "\n".join(b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text")
    return ""


def has_err(text):
    pats = DIAG_ERR if MUTANT != "noerrtag" else [re.compile(r"(?:^|[\s/])task\.lean:\d+:\d+:\s*error:", re.M)]
    return any(p.search(text) for p in pats)


def has_sorry(text):
    return False if MUTANT == "nosorry" else bool(DIAG_SORRY.search(text))


def grep_pattern_passes(stage_tokens, line):
    """would `grep [opts] PAT` print `line`? None if the stage cannot be parsed."""
    pats, i, invert, extended, fixed = [], 1, False, False, False
    while i < len(stage_tokens):
        t = stage_tokens[i]
        if t == "-e" and i + 1 < len(stage_tokens):
            pats.append(stage_tokens[i + 1]); i += 2; continue
        if t.startswith("-") and len(t) > 1:
            invert |= "v" in t; extended |= "E" in t; fixed |= "F" in t
            if "c" in t or "q" in t or "l" in t:
                return None
            i += 1; continue
        pats.append(t); i += 1
        break
    if i < len(stage_tokens):  # a file operand: grep is not filtering the pipe
        return None
    if not pats:
        return None
    hit = False
    for p in pats:
        if fixed:
            alts = [p]
            hit |= any(a in line for a in alts)
        else:
            rp = p if extended else p.replace(r"\|", "|").replace(r"\(", "(").replace(r"\)", ")").replace(r"\+", "+")
            try:
                hit |= bool(re.search(rp, line))
            except re.error:
                return None
    return (not hit) if invert else hit


def visibility(cmd, match_end, n_result_lines):
    """classify the pipeline after the lean invocation: CLEAR | OPAQUE:<why> | TRUNC_BIT:<n> """
    rest = cmd[match_end:]
    m = re.search(r"\n|;|&&|\|\||(?<![|>&])&(?![>&])", rest)
    rest = rest[: m.start()] if m else rest
    if MUTANT == "nofilter":
        return "CLEAR"
    # stdout redirections (2>&1 and 2>/dev/null touch stderr only)
    r2 = re.sub(r"\b2>&1\b|\b2>\s*/dev/null", " ", rest)
    if re.search(r"(?:^|[^2])>{1,2}\s*\S", r2) or "&>" in r2:
        return "OPAQUE:redirect"
    stages = [s.strip() for s in re.split(r"(?<!\|)\|(?!\|)", r2)][1:]
    trunc = None
    for st in stages:
        if not st:
            continue
        try:
            tok = shlex.split(st)
        except ValueError:
            return "OPAQUE:unparsed"
        if not tok:
            continue
        p = tok[0]
        if p == "grep":
            a = grep_pattern_passes(tok, SAMPLE_ERR)
            b = grep_pattern_passes(tok, SAMPLE_ERR_T)
            c = grep_pattern_passes(tok, SAMPLE_SORRY)
            if a is None or b is None or c is None:
                return "OPAQUE:grep(%s)" % st[:40]
            if not (a and b and c):
                return "OPAQUE:grep-drops-diag(%s)" % st[:40]
            continue
        if p in ("head", "tail"):
            n = 10
            for t in tok[1:]:
                mm = re.fullmatch(r"-n?(\d+)", t) or (re.fullmatch(r"\d+", t) and re.fullmatch(r"(\d+)", t))
                if mm:
                    n = int(mm.group(1))
            trunc = n if trunc is None else min(trunc, n)
            continue
        if p == "sed" and len(tok) >= 3 and tok[1] == "-n":
            mm = re.fullmatch(r"1,(\d+)p", tok[2])
            if mm:
                n = int(mm.group(1)); trunc = n if trunc is None else min(trunc, n); continue
            return "OPAQUE:sed"
        if p in ("cat", "sort", "uniq"):
            continue
        return "OPAQUE:stage(%s)" % p
    if trunc is not None and n_result_lines >= trunc:
        return "TRUNC_BIT:%d" % trunc
    return "CLEAR"


def read_rt(path):
    ev, open_ = [], []
    if not os.path.isfile(path):
        return ev
    for line in open(path, errors="replace"):
        f = line.rstrip("\n").split("\t")
        if len(f) >= 3 and f[1] == "START":
            open_.append({"start": ts(f[0]), "cmd": f[2], "rc": None})
        elif len(f) >= 4 and f[1] == "END":
            # ENDs close the most recent START with the same command (calls are sequential in practice)
            for e in reversed(open_):
                if e["cmd"] == f[3] and e["rc"] is None:
                    e["rc"] = int(f[2].split("=")[1]); e["end"] = ts(f[0]); break
    return open_


def analyse(epdir):
    man = json.load(open(os.path.join(epdir, "manifest.json")))
    calls, results, all_msgs, side = [], {}, set(), 0
    trunc_markers = 0
    for line in open(os.path.join(epdir, "session.jsonl")):
        o = json.loads(line)
        if o.get("isSidechain"):
            side += 1
            continue
        msg = o.get("message") or {}
        c = msg.get("content")
        if o.get("type") == "assistant" and msg.get("id"):
            all_msgs.add(msg["id"])
        if o.get("type") == "assistant" and isinstance(c, list):
            for b in c:
                if b.get("type") == "tool_use":
                    calls.append({"id": b["id"], "name": b["name"], "input": b.get("input") or {},
                                  "t": ts(o["timestamp"]), "msg": msg.get("id")})
        if o.get("type") == "user" and isinstance(c, list):
            for b in c:
                if b.get("type") == "tool_result":
                    txt = result_text(b.get("content"))
                    if "Output too large" in txt or "[... truncated" in txt or "<persisted-output>" in txt:
                        trunc_markers += 1
                    results[b["tool_use_id"]] = {"text": txt, "is_error": bool(b.get("is_error")), "t": ts(o["timestamp"])}
    rt = read_rt(os.path.join(epdir, "rt.log"))
    unassigned = 0
    for e in rt:
        idx = None
        for i, cl in enumerate(calls):
            if int(cl["t"]) <= e["start"]:
                idx = i
        if idx is None:
            unassigned += 1
        else:
            calls[idx].setdefault("rt", []).append(e)
    rows, first_green, first_maybe, ncomp, last_verdict = [], None, None, 0, None
    seen_msgs = []
    for i, cl in enumerate(calls, 1):
        if cl["msg"] not in seen_msgs:
            seen_msgs.append(cl["msg"])
        cl["api_calls_so_far"] = len(seen_msgs)
        if cl["name"] != "Bash":
            continue
        cmd = cl["input"].get("command", "")
        ms = list(LEAN_TASK.finditer(cmd))
        if not ms:
            continue
        ncomp += 1
        res = results.get(cl["id"])
        if res is None:
            v, why = "UNDET", "no tool_result"
        else:
            text = res["text"]
            nlines = len(text.splitlines())
            rts = [e for e in cl.get("rt", []) if LEAN_TASK.search(" " + e["cmd"])]
            rcs = [e["rc"] for e in rts]
            if MUTANT == "norc":
                rcs = [0 for _ in rcs]
            vis = [visibility(cmd, m.end(), nlines) for m in ms]
            if has_err(text) or has_sorry(text):
                v, why = "RED", "diag:" + ("error" if has_err(text) else "sorry")
            elif any(r is not None and r != 0 for r in rcs):
                v, why = "RED", "rt rc=%s" % [r for r in rcs if r]
            elif all(x == "CLEAR" for x in vis):
                via_rt = any(re.search(r"(?:^|[\s/.])rt\s", cmd[: m.start() + 1] + " ") for m in ms) or bool(rts)
                if rts and all(r == 0 for r in rcs):
                    v, why = "GREEN", "rt rc=0, clear"
                elif not via_rt or not rts:
                    v, why = "GREEN_NORT", "no rt record; clear output, no diagnostic"
                else:
                    v, why = "UNDET", "rt rc unknown"
            else:
                v, why = "UNDET", ",".join(x for x in vis if x != "CLEAR")
        rows.append({"idx": i, "verdict": v, "why": why, "api_calls_so_far": cl["api_calls_so_far"]})
        last_verdict = v
        if first_green is None and v in ("GREEN", "GREEN_NORT"):
            first_green = rows[-1]
        if first_maybe is None and v in ("GREEN", "GREEN_NORT", "UNDET"):
            first_maybe = rows[-1]
    return {
        "ep": os.path.basename(epdir), "problem": man.get("instance_id"), "arm": man.get("arm"),
        "stage": man.get("stage"), "passed": bool(man.get("passed")), "class": (man.get("check") or {}).get("class"),
        "manifest_calls": man.get("calls"), "tool_calls": len(calls), "tool_results": sum(1 for c in calls if c["id"] in results),
        "api_calls": len(seen_msgs), "api_calls_total": len(all_msgs), "compile_calls": ncomp,
        "first_green_idx": first_green["idx"] if first_green else None,
        "first_green_verdict": first_green["verdict"] if first_green else None,
        "first_green_api_calls": first_green["api_calls_so_far"] if first_green else None,
        "first_maybe_idx": first_maybe["idx"] if first_maybe else None,
        "last_compile_verdict": last_verdict, "sidechain_lines": side, "rt_unassigned": unassigned,
        "rt_invocations": len(rt), "truncated_results": trunc_markers,
        "compiles": rows,
    }


def run(a):
    eps = sorted(glob.glob(os.path.join(a.state, "ep-*")))
    out = []
    for d in eps:
        try:
            st = json.load(open(os.path.join(d, "manifest.json"))).get("stage")
        except Exception:
            continue
        if st != a.stage:
            continue
        out.append(analyse(d))
    if not out:
        print("FAIL: zero stage-%s episodes under %s" % (a.stage, a.state))
        return 1
    num = lambda r: (int(r["problem"].split("_")[-1]), r["arm"])
    out.sort(key=num)
    hdr = ("problem", "arm", "passed", "class", "tools", "api", "compiles", "1st_green", "kind", "api@1st", "1st_maybe", "last")
    print("%-12s %-3s %-6s %-16s %5s %4s %8s %9s %-10s %7s %9s %-10s" % hdr)
    fails = []
    for r in out:
        print("%-12s %-3s %-6s %-16s %5d %4d %8d %9s %-10s %7s %9s %-10s" % (
            r["problem"], r["arm"], r["passed"], r["class"], r["tool_calls"], r["api_calls"], r["compile_calls"],
            r["first_green_idx"] or "-", r["first_green_verdict"] or "-", r["first_green_api_calls"] or "-",
            r["first_maybe_idx"] or "-", r["last_compile_verdict"] or "-"))
        if r["passed"] and r["first_green_idx"] is None:
            fails.append("%s/%s passed but has no first green" % (r["problem"], r["arm"]))
    tot = dict(
        episodes=len(out), sidechain_lines=sum(r["sidechain_lines"] for r in out),
        missing_results=sum(r["tool_calls"] - r["tool_results"] for r in out),
        truncated_results=sum(r["truncated_results"] for r in out),
        rt_unassigned=sum(r["rt_unassigned"] for r in out),
        api_eq_manifest=sum(r["api_calls_total"] == r["manifest_calls"] for r in out),
        ambiguous=sum(r["first_green_idx"] != r["first_maybe_idx"] for r in out),
        passed_with_green=sum(1 for r in out if r["passed"] and r["first_green_idx"]),
        passed=sum(r["passed"] for r in out),
        failed_with_green=sum(1 for r in out if not r["passed"] and r["first_green_idx"]),
        failed=sum(not r["passed"] for r in out))
    print("\ncompleteness: sidechain lines %(sidechain_lines)d · tool calls without a tool_result %(missing_results)d · "
          "results carrying a truncation marker %(truncated_results)d · rt invocations unassigned %(rt_unassigned)d · "
          "transcript API calls == manifest calls in %(api_eq_manifest)d of %(episodes)d" % tot)
    print("cross-check: passed with a first green %(passed_with_green)d of %(passed)d · failed with a first green "
          "%(failed_with_green)d of %(failed)d · ambiguous (first_green != first_maybe) %(ambiguous)d" % tot)
    # paired view on the problems both arms passed (population derived from `passed`, arms read from the manifests)
    by = {}
    for r in out:
        by.setdefault(r["problem"], {})[r["arm"]] = r
    arms = sorted({r["arm"] for r in out})
    pairs = []
    if len(arms) == 2:
        x, y = arms
        for p in sorted(by, key=lambda q: int(q.split("_")[-1])):
            d = by[p]
            if x in d and y in d and d[x]["passed"] and d[y]["passed"] and d[x]["first_green_idx"] and d[y]["first_green_idx"]:
                pairs.append((p, d[x]["first_green_idx"], d[y]["first_green_idx"], d[x]["tool_calls"], d[y]["tool_calls"]))
        if pairs:
            print("\npaired, both passed (n = %d): first-green tool-call index %s vs %s, and total tool calls" % (len(pairs), y, x))
            for p, gx, gy, tx, ty in pairs:
                print("  %-12s %s %3d  %s %3d  ratio %5.2f   |  total %s %3d  %s %3d" % (p, x, gx, y, gy, gy / gx, x, tx, y, ty))
            rs = sorted(gy / gx for _, gx, gy, _, _ in pairs)
            n = len(rs); med = rs[n // 2] if n % 2 else (rs[n // 2 - 1] + rs[n // 2]) / 2
            print("  %s needs more calls than %s in %d of %d pairs, fewer in %d, equal in %d · median ratio %.3f" % (
                y, x, sum(gy > gx for _, gx, gy, _, _ in pairs), n, sum(gy < gx for _, gx, gy, _, _ in pairs),
                sum(gy == gx for _, gx, gy, _, _ in pairs), med))
            tot["paired"] = [dict(problem=p, **{x: gx, y: gy, x + "_total": tx, y + "_total": ty}) for p, gx, gy, tx, ty in pairs]
    if a.json:
        json.dump({"totals": tot, "episodes": out}, open(a.json, "w"), indent=1, sort_keys=True)
    print("CROSS-CHECK: %s" % ("every passed episode has a first green" if not fails else "FAILED: " + " | ".join(fails)))
    return 1 if fails else 0


# ---------------------------------------------------------------- selftest: fixtures built here, not typed verdicts
def _fixture(tmp, name, cmds_results, rt_lines, passed=True):
    d = os.path.join(tmp, "ep-" + name)
    os.makedirs(d, exist_ok=True)
    json.dump({"instance_id": "problem_1", "arm": "a0", "stage": "B", "passed": passed, "calls": len(cmds_results),
               "check": {"class": "PASS" if passed else "AXIOMS_FAIL"}}, open(os.path.join(d, "manifest.json"), "w"))
    with open(os.path.join(d, "session.jsonl"), "w") as f:
        for k, (cmd, res) in enumerate(cmds_results):
            t = "2026-01-01T00:00:%02d.500Z" % (2 * k)
            f.write(json.dumps({"type": "assistant", "timestamp": t, "isSidechain": False, "message": {"id": "m%d" % k,
                    "content": [{"type": "tool_use", "id": "t%d" % k, "name": "Bash", "input": {"command": cmd}}]}}) + "\n")
            t2 = "2026-01-01T00:00:%02d.900Z" % (2 * k + 1)
            f.write(json.dumps({"type": "user", "timestamp": t2, "isSidechain": False, "message": {
                    "content": [{"type": "tool_result", "tool_use_id": "t%d" % k, "content": res}]}}) + "\n")
    with open(os.path.join(d, "rt.log"), "w") as f:
        for k, cmd, rc in rt_lines:
            f.write("2026-01-01T00:00:%02dZ\tSTART\t%s\n2026-01-01T00:00:%02dZ\tEND\trc=%d\t%s\n" % (2 * k, cmd, 2 * k + 1, rc, cmd))
    return d


def selftest():
    import tempfile
    tmp = tempfile.mkdtemp(prefix="ctg-selftest-")
    EP = "/w/ep-x/rt"
    # each fixture: (name, calls, rt, expected first_green index derived from WHICH call carries the clean compile)
    F = []
    # F1 sorry at call 2, clean at call 3
    F.append(("sorry", [("cat task.lean", "x"), (EP + " lake env lean task.lean", SAMPLE_SORRY), (EP + " lake env lean task.lean", "")],
              [(1, "lake env lean task.lean ", 0), (2, "lake env lean task.lean ", 0)], 3))
    # F2 tagged error visible, rc=1, then green
    # (no rt: the direct form, so only the diagnostic text can make it RED)
    F.append(("errtag", [('PATH="$HOME/.elan/bin:$PATH" lake env lean task.lean 2>&1 | grep -v deprecated', SAMPLE_ERR_T),
                         ('PATH="$HOME/.elan/bin:$PATH" lake env lean task.lean', "")], [], 2))
    # F3 the wrapper's bound fired (rc=124) with a clean-looking output, then green
    F.append(("rc", [(EP + " lake env lean task.lean", ""), (EP + " lake env lean task.lean", "")],
              [(0, "lake env lean task.lean ", 124), (1, "lake env lean task.lean ", 0)], 2))
    # F4 a grep -v that would DROP the sorry line -> UNDET, then green
    F.append(("filter", [(EP + " lake env lean task.lean 2>&1 | grep -v sorry", ""), (EP + " lake env lean task.lean", "")],
              [(0, "lake env lean task.lean ", 0), (1, "lake env lean task.lean ", 0)], 2))
    # F5 a scratch file compile is not a compile call; a task.lean.bak mention is not either
    F.append(("scratch", [(EP + " lake env lean scratch.lean", ""), ("rm -f task.lean.bak", ""), (EP + " lake env lean task.lean", "")],
              [(0, "lake env lean scratch.lean ", 0), (2, "lake env lean task.lean ", 0)], 3))
    ok = True
    for mut in ("", "nosorry", "noerrtag", "norc", "nofilter"):
        global MUTANT
        MUTANT = mut
        bad = []
        for name, calls, rtl, want in F:
            d = _fixture(tmp, "%s-%s" % (name, mut or "pristine"), calls, rtl)
            r = analyse(d)
            if r["first_green_idx"] != want:
                bad.append("%s: first_green %s want %s" % (name, r["first_green_idx"], want))
        if mut == "":
            print("selftest pristine            %s" % ("PASS (5/5 fixtures)" if not bad else "FAIL " + "; ".join(bad)))
            ok &= not bad
        else:
            print("selftest mutant %-12s %s" % (mut, ("RED as required: " + "; ".join(bad)) if bad else "GREEN -- the mutant was NOT caught"))
            ok &= bool(bad)
    MUTANT = ""
    print("SELFTEST %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--state")
    ap.add_argument("--stage", default="B")
    ap.add_argument("--json")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())
    if not a.state:
        ap.error("--state required")
    sys.exit(run(a))


if __name__ == "__main__":
    main()
