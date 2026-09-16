#!/usr/bin/env python3
"""budget_read_column.py — the §3b disambiguating column, scored by ROUTE, never as a boolean.

WHY IT EXISTS (bench, 2026-09-15, relight 53):
  HC1-FIRE-ORDER.md's "three things a scorer must carry and cannot recover later" #1 says the NEAR-CAP
  band [$35.35, $37.21) is ITS OWN OUTCOME, because BUDGET.md is a live countdown the subject can read
  and a subject pacing itself to finish just under the cap produces exactly that band. The column that
  disambiguates it was specified as: "the authoritative read is a Read tool call in the session jsonl".

  ⛔ MEASURED AT THE OBJECT ON hc1fp01, AND THAT CRITERION IS WRONG IN A WAY THAT FAVOURS US:
        naive `grep -c BUDGET.md`          -> 3     (two are not reads at all)
        registered criterion (Read call)   -> 0     (a FALSE NEGATIVE)
        what the subject actually did      -> 1     `cat BUDGET.md 2>/dev/null`, inside a Bash call
    The two non-reads are the arm's OWN SEAT.md text describing budgets, and a source file listing
    "BUDGET.md" in a SKIP tuple. So the loose needle over-counts and the strict needle under-counts,
    in OPPOSITE directions, and neither is the quantity.

  ⇒ 🔑 A NEEDLE DEFECT GIVES YOU A ZERO WHERE YOUR WORDS ARE, NOT WHERE THE ANSWER IS. The file was
    read; the criterion could not see the route it was read by.

  ⇒ ⛔⛔ AND THE DIRECTION IS THE PART THAT MATTERS, BECAUSE IT IS ARM-CORRELATED AND IT FAVOURS OUR OWN
    REGISTERED PREDICTION. Under-counting budget reads pushes a NEAR-CAP cell out of "the subject paced
    itself to the cap" and into "the subject genuinely capped out" — which is the reading that makes
    §3a's cap-out prediction look CONFIRMED. A defect that biases a VERDICT toward the author's own
    hypothesis is not a footnote; it is the thing pre-registration exists to stop.

THE FORM: report every route SEPARATELY and let the scorer read them. Collapsing routes to a boolean is
what produced the defect; this tool refuses to collapse them.

⛔⛔ AND THE COLUMN WAS BROKEN THE OTHER WAY UNTIL 2026-09-16 (bench, relight 56) — IT COUNTED THE ACTION AND
NEVER LOOKED AT WHAT CAME BACK. Measured over all 42 ENDED HC1 cells (census:
~/bench-dry/budget-read-content-2026-09-16/census.out, two methods agreeing on 42/42):
      the column said READ                         42 of 42
      a read whose tool_result carried the countdown  10 of 42   (placebo 4 · plain 1 · salt-diet 5)
  The subject's opening `cat BUDGET.md 2>/dev/null` runs 7-56 s into the session, and the watcher first writes
  the file at its first tick (60 s). On hc1ps02 (NEAR-CAP, $36.76) the cat returned NOTHING and `ls BUDGET.md`
  8 s later printed "No such file or directory". It was scored READ.
  ⇒ 🔑 A CONSTANT READ IS THE SAME DEFECT AS THE CONSTANT NO-READ THIS TOOL WAS BUILT TO FIX, WITH THE SIGN REVERSED.
    Either way the criterion cannot vary with the data.
  ⇒ ⛔ AND THIS SIGN ALSO FLATTERS OUR PREDICTION: "READ" on a NEAR-CAP cell makes §3b's pacing exemption look
    load-bearing for a subject that never saw a number.
THE COLUMN NOW HAS THREE VALUES, decided by CONTENT, and the route counts above it are unchanged:
      READ-SAW        >= 1 read whose tool_result carries `cost (USD): cap <C> spent <S> remaining <R>`
      READ-NOT-SEEN   >= 1 read, and none of them returned the countdown (missing file, empty output)
      NO-READ         no read action at all
  A read is paired with its result BY tool_use_id over the WHOLE transcript, because a result carrying the
  file's content need not contain the string "BUDGET.md".
  SCOPE, printed with the verdict: the file given (the harvester passes the HEAD transcript); sub-agent
  transcripts are NOT in it.

  A read is an ACTION BY THE SUBJECT, so it is always a tool_use — never a tool_result (that is the
  file's content coming back), never assistant text (that is the subject talking about it), and never
  the arm's own instructions (that is the STATEMENT, identical in every arm by construction).
"""
import json, io, sys, os, re

READ_VERB = re.compile(
    r'\b(cat|head|tail|less|more|bat|sed|awk|grep|rg|wc|od|xxd|nl|cut|tr|sort|uniq|python3?|jq)\b')
COUNTDOWN = re.compile(r'cost \(USD\): cap ([0-9.]+) spent ([0-9.]+) remaining (-?[0-9.]+)')

def _result_text(b):
    c = b.get("content")
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        return "\n".join((x.get("text") or "") if isinstance(x, dict) else str(x) for x in c)
    return json.dumps(c)

def results_by_id(path):
    """Every tool_result's text, keyed by tool_use_id, over the WHOLE file (no BUDGET.md prefilter)."""
    out = {}
    for line in io.open(path, encoding="utf-8", errors="replace"):
        if '"tool_result"' not in line:
            continue
        try:
            r = json.loads(line)
        except Exception:
            continue
        c = (r.get("message") or {}).get("content")
        if isinstance(c, list):
            for b in c:
                if isinstance(b, dict) and b.get("type") == "tool_result":
                    out[b.get("tool_use_id")] = _result_text(b)
    return out

def classify(path):
    out = {"Read": 0, "Bash_read": 0, "Bash_mention_only": 0, "other_tool_use": 0,
           "wrote_budget": 0, "mention_in_payload": 0,
           "tool_result": 0, "assistant_text": 0, "user_or_system": 0,
           "unparsable": 0, "records_with_string": 0, "evidence": [], "read_uses": []}
    for ln, line in enumerate(io.open(path, encoding="utf-8", errors="replace"), 1):
        if "BUDGET.md" not in line:
            continue
        out["records_with_string"] += 1
        try:
            r = json.loads(line)
        except Exception:
            out["unparsable"] += 1
            continue
        msg = r.get("message") or {}
        content = msg.get("content")
        blocks = content if isinstance(content, list) else []
        saw_action = False
        for b in blocks:
            if not isinstance(b, dict):
                continue
            bt = b.get("type")
            if bt == "tool_use":
                inp = b.get("input") or {}
                s = json.dumps(inp)
                if "BUDGET.md" not in s:
                    continue
                saw_action = True
                name = b.get("name")
                if name == "Read":
                    out["Read"] += 1
                    out["read_uses"].append((b.get("id"), ln, r.get("timestamp")))
                    out["evidence"].append((ln, "Read", str(inp.get("file_path"))[:120]))
                elif name == "Bash":
                    cmd = inp.get("command", "")
                    # the discriminator: a read VERB applied to the file, not a bare mention
                    seg = ""
                    for part in re.split(r'[;&|\n]', cmd):
                        if "BUDGET.md" in part:
                            seg = part.strip()
                            break
                    if seg and READ_VERB.search(seg):
                        out["Bash_read"] += 1
                        out["read_uses"].append((b.get("id"), ln, r.get("timestamp")))
                        out["evidence"].append((ln, "Bash_read", seg[:120]))
                    else:
                        out["Bash_mention_only"] += 1
                        out["evidence"].append((ln, "Bash_mention_only", (seg or cmd)[:120]))
                else:
                    # ⛔ A TOOL THAT MERELY CARRIES THE STRING IS NOT A READ OF THE FILE, AND FOLDING
                    #   "other tool" INTO THE READ COUNT IS THE SAME OVER-COUNTING DEFECT THIS TOOL WAS
                    #   BUILT TO FIX, COMMITTED BY THE TOOL ITSELF. Measured on hc1cs03: a `Write` to
                    #   repo/memory/MEMORY.md whose CONTENT mentions BUDGET.md was scored a read, giving
                    #   2 where the truth is 1. Caught before the number was quoted.
                    #   ⇒ 🔑 THE DISCRIMINATOR IS THE TARGET, NOT THE MENTION: a read names BUDGET.md as
                    #     the thing it OPERATES ON. A Write naming it in a payload operates on something
                    #     else entirely, and a Write TO BudGET.md is a WRITE — its own finding, never a read.
                    tgt = str(inp.get("file_path") or inp.get("path") or "")
                    if name in ("Grep", "Glob") and "BUDGET.md" in json.dumps(
                            [inp.get("path"), inp.get("glob"), inp.get("pattern")]):
                        out["other_tool_use"] += 1
                        out["read_uses"].append((b.get("id"), ln, r.get("timestamp")))
                        out["evidence"].append((ln, "search:%s" % name, s[:120]))
                    elif name in ("Write", "Edit", "NotebookEdit") and "BUDGET.md" in tgt:
                        out["wrote_budget"] += 1
                        out["evidence"].append((ln, "WROTE-TO-BUDGET:%s" % name, tgt[:120]))
                    else:
                        out["mention_in_payload"] += 1
                        out["evidence"].append((ln, "mention_in_payload:%s" % name, tgt[:120] or s[:120]))
            elif bt == "tool_result":
                if "BUDGET.md" in json.dumps(b.get("content")):
                    out["tool_result"] += 1
            elif bt == "text":
                if "BUDGET.md" in (b.get("text") or ""):
                    out["assistant_text"] += 1
        if not blocks and isinstance(content, str) and "BUDGET.md" in content:
            out["user_or_system"] += 1
        elif not saw_action and r.get("type") == "user":
            pass
    return out

def main():
    if len(sys.argv) < 2:
        print("usage: budget_read_column.py <session.jsonl> [...]"); return 2
    rc = 0
    for p in sys.argv[1:]:
        if not os.path.exists(p):
            print("MISSING %s" % p); rc = 1; continue
        o = classify(p)
        any_read = o["Read"] + o["Bash_read"] + o["other_tool_use"]
        print("=== %s" % os.path.basename(p))
        print("  BUDGET.md READ BY THE SUBJECT : %d   (Read %d + Bash-with-a-read-verb %d + other tool %d)"
              % (any_read, o["Read"], o["Bash_read"], o["other_tool_use"]))
        print("  NOT reads, counted separately : mention-only-in-Bash %d · mention-in-a-payload %d · tool_result %d · assistant text %d · arm/system text %d"
              % (o["Bash_mention_only"], o["mention_in_payload"], o["tool_result"], o["assistant_text"], o["user_or_system"]))
        if o["wrote_budget"]:
            print("  ⛔ SUBJECT WROTE TO BUDGET.md %d time(s) — its own finding, and NOT a read." % o["wrote_budget"])
        print("  records containing the string : %d   unparsable %d" % (o["records_with_string"], o["unparsable"]))
        res = results_by_id(p)
        saw, unseen = [], []
        for uid, ln, ts in o["read_uses"]:
            m = COUNTDOWN.search(res.get(uid, ""))
            (saw).append((ln, ts, m.group(2) if m else None))
        assert len(saw) + len(unseen) == any_read, "paired reads must equal counted reads"
        col = "READ-SAW" if saw else ("READ-NOT-SEEN" if any_read else "NO-READ")
        print("  RETURNED THE COUNTDOWN         : %d of %d reads%s   (the rest returned no countdown: missing file / empty output)"
              % (len(saw), any_read, ("; last seen spent $%s at %s" % (saw[-1][2], saw[-1][1])) if saw else ""))
        print("  §3b COLUMN                    : %s   (scope: this transcript only; sub-agent transcripts are NOT read)" % col)
        if unseen:
            print("  ⚠️  %d read(s) returned NO countdown, at: %s" % (len(unseen), ", ".join("line %d %s" % (u[0], u[1]) for u in unseen)))
        if o["Read"] == 0 and o["Bash_read"] > 0:
            print("  ⚠️  THE REGISTERED CRITERION ('a Read tool call') WOULD SCORE THIS **NO-READ** AND BE WRONG.")
        for ln, kind, what in o["evidence"]:
            print("      line %-6d %-22s %s" % (ln, kind, what))
    return rc

sys.exit(main())
