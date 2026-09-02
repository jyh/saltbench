#!/usr/bin/env python3
"""build_views_verus.py — THE ONLY CODE THAT READS THE BENCHMARK. Runs on the SEAT, never on the Studio.

Per record it produces, for the drawn proof-fn tasks:
  views/<task_id>/task.rs      the VIEW the agent sees   (markers, empty regions)
  views/<task_id>/frozen.json  prefix / enclosing_head / suffix / the original interior   NO ground truth
  gt/<task_id>.json            the reference proof body                                   SEAT ONLY, never shipped

REFUSE CLASSES, each COUNTED and published with the draw (protocol §3, §8.1):
  EXEC_TARGET       the target is an exec/bare fn — the two-region model cannot express ghost insertions
  TARGET_ABSENT     `target_function` is not a proof-fn declaration in the file at all   (bench, amendment 15)
  TARGET_AMBIGUOUS  lynette's rule yields != 1 surviving candidate
  SHAPE             the stripped target body is not empty modulo whitespace
  UNFAITHFUL        the split does not reconstruct the original task byte-for-byte
  PARSE             the source could not be lexed unambiguously (rustspan refused)

⛔ The shape predicate is EMPTY MODULO WHITESPACE, not the literal `{\\n}`: measured over AC u NR, the literal
costs 44 tasks (21% of the recoverable population) to whitespace alone. The literal spelling is RECORDED per
task, never gated on.

⛔⛔ THE HELPERS REGION SITS AT THE END OF THE `verus!` BLOCK, AFTER EVERY ORIGINAL ITEM. Two independent
constraints collide and only this placement satisfies both:
  · rustc E0407 — a non-trait item inside a trait impl does not compile, so helpers cannot go inside the
    enclosing `impl`;
  · lynette `additions` — `check_items` (additions.rs:340-532) walks the two item lists in LOCKSTEP and skips
    an added `proof fn` ONLY in the `(Item::Fn, Item::Fn)` arm. A helper placed immediately before the
    enclosing item is compared against an `Item::Impl`, falls to the catch-all `(_, _)` arm and is REFUSED.
    Its loop is `while idx_orig < original.len() && idx_changed < changed.len()`, so items appended PAST the
    end of the original list are never examined and the final `idx_orig == original_items.len()` holds.
⛔ The design that this repairs placed helpers "at top level immediately before the item that encloses the
target" — the exact position lynette cannot accept for the 47 of 207 impl-enclosed views. MEASURED both ways:
before the `impl`, lynette rc=1 `Disallowed changes made to Verus macros`; at the end of the block, rc=0.
⚠️ AND THE REASON IT MATTERED MORE THAN ITS SIZE: the verdict would have been `STATEMENT_ALTERED` — a CHEATING
class — for doing exactly what the prompt invites, and the salt arm `a2` explicitly encourages helper lemmas.
An instrument that penalises the treatment for following the treatment manufactures its own effect.
Rust item order does not affect name resolution, so a target may call a helper declared after it.

usage: build_views_verus.py <tasks.jsonl> <outdir> [--projects AC,NR] [--only <task_id>[,...]]
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rustspan

HELPERS_VIEW = "\n// start_def helpers\n// end_def helpers\n"
PROOF_VIEW = "\n// start_def proof\n// end_def proof\n"


class Refuse(Exception):
    def __init__(self, cls, detail=""):
        super().__init__("%s: %s" % (cls, detail))
        self.cls = cls
        self.detail = detail


def _mode_before(src, start, fn_kw):
    """Classify the fn's mode from the tokens between the item's line start and the `fn` keyword."""
    head = src[start:fn_kw]
    if re.search(r"\bproof\s*$", head):
        return "proof"
    if re.search(r"\bspec(\s*\([^)]*\))?\s*$", head):
        return "spec"
    if re.search(r"\bexec\s*$", head):
        return "exec"
    return "bare"


def find_targets(src, name, incode):
    """Every `fn <name>` item in code position, with its mode and body span."""
    out = []
    for m in re.finditer(r"\bfn\s+" + re.escape(name) + r"\s*[<(]", src):
        if not incode[m.start()]:
            continue
        ls = src.rfind("\n", 0, m.start()) + 1
        mode = _mode_before(src, ls, m.start())
        # the body's opening brace: first code '{' after the signature, at paren/bracket depth 0
        j = m.end() - 1
        dp = db = 0
        body_open = None
        while j < len(src):
            ch = src[j]
            if incode[j]:
                if ch == "(":
                    dp += 1
                elif ch == ")":
                    dp -= 1
                elif ch == "[":
                    db += 1
                elif ch == "]":
                    db -= 1
                elif ch == "{" and dp == 0 and db == 0:
                    body_open = j
                    break
                elif ch == ";" and dp == 0 and db == 0:
                    break
            j += 1
        if body_open is None:
            continue
        body_close = rustspan.match_brace(src, body_open, incode)
        out.append(dict(mode=mode, fn_kw=m.start(), line_start=ls,
                        body_open=body_open, body_close=body_close,
                        body=src[body_open:body_close + 1]))
    return out


def _item_start(src, line_start):
    """Walk back over the item's contiguous attribute and doc-comment lines."""
    i = line_start
    while i > 0:
        prev_end = i - 1
        prev_start = src.rfind("\n", 0, prev_end) + 1
        line = src[prev_start:prev_end]
        s = line.strip()
        if s.startswith("#[") or s.startswith("#![") or s.startswith("//"):
            i = prev_start
            continue
        break
    return i


def build_one(rec):
    src = rec["task"]
    name = rec["target_function"]
    try:
        depths, incode = rustspan.code_map(src)
    except rustspan.SpanError as e:
        raise Refuse("PARSE", str(e))

    items = find_targets(src, name, incode)
    if not items:
        raise Refuse("TARGET_ABSENT", "no `fn %s` item in code position" % name)
    cands = [it for it in items if "unimplemented!()" not in it["body"]]
    if len(cands) != 1:
        raise Refuse("TARGET_AMBIGUOUS", "%d of %d items survive lynette's rule" % (len(cands), len(items)))
    t = cands[0]
    if t["mode"] != "proof":
        raise Refuse("EXEC_TARGET" if t["mode"] in ("exec", "bare") else "TARGET_ABSENT",
                     "target is a %s fn" % t["mode"])

    interior = src[t["body_open"] + 1:t["body_close"]]
    if interior.strip() != "":
        raise Refuse("SHAPE", "stripped body is not empty modulo whitespace")

    # the ENCLOSING top-level item: the target itself at depth 1, else the impl block around it
    d = depths[t["fn_kw"]]
    if d == 1:
        enclosing_start = _item_start(src, t["line_start"])
    elif d == 2:
        open_idx = None
        for j in range(t["fn_kw"], -1, -1):
            if incode[j] and src[j] == "{" and depths[j] == 1:
                open_idx = j
                break
        if open_idx is None:
            raise Refuse("PARSE", "target at depth 2 with no enclosing item")
        ls = src.rfind("\n", 0, open_idx) + 1
        # the enclosing item may span lines before its brace; walk back to its first token line
        k = ls
        while k > 0:
            ps = src.rfind("\n", 0, k - 1) + 1
            if re.search(r"[;}]\s*$", src[ps:k - 1]) or src[ps:k - 1].strip() == "":
                break
            k = ps
        enclosing_start = _item_start(src, k)
    else:
        raise Refuse("PARSE", "target at unexpected brace depth %d" % d)

    if depths[enclosing_start] != 1:
        raise Refuse("PARSE", "helpers insertion point is at depth %d, not 1" % depths[enclosing_start])

    # the enclosing `verus!` block's closing brace: the helpers region goes immediately before it
    vm = None
    for m in re.finditer(r"\bverus\s*!\s*[\{\[\(]", src):
        if not incode[m.start()]:
            continue
        ob = m.end() - 1
        if src[ob] != "{":
            raise Refuse("PARSE", "verus! invoked with a non-brace delimiter")
        cb = rustspan.match_brace(src, ob, incode)
        if ob < t["fn_kw"] < cb:
            vm = (ob, cb)
            break
    if vm is None:
        raise Refuse("PARSE", "target is not inside a verus! block")
    vclose = vm[1]
    if not (t["body_close"] < vclose):
        raise Refuse("PARSE", "verus! close precedes the target body close")

    frozen = dict(
        task_id=rec["task_id"], project=rec["project"], target_function=name,
        prefix=src[:enclosing_start],
        enclosing_head=src[enclosing_start:t["body_open"] + 1],
        proof_interior_original=interior,
        suffix_head=src[t["body_close"]:vclose],
        suffix_tail=src[vclose:],
        interior_literal=repr(interior),
        enclosed_in_impl=(d == 2),
    )
    # ⛔ THE SCAFFOLD SELF-TEST, byte-exact, and the ONLY thing that certifies the split (§4 clause a)
    if assemble(frozen, {}, pristine=True) != src:
        raise Refuse("UNFAITHFUL", "pristine assembly does not reproduce the task byte-for-byte")

    view = (frozen["prefix"] + frozen["enclosing_head"] + PROOF_VIEW
            + frozen["suffix_head"] + HELPERS_VIEW + frozen["suffix_tail"])
    gt_body = None
    gt_items = find_targets(rec["ground_truth"], name, rustspan.code_map(rec["ground_truth"])[1])
    gt_c = [it for it in gt_items if "unimplemented!()" not in it["body"]]
    if len(gt_c) == 1:
        gt_body = rec["ground_truth"][gt_c[0]["body_open"] + 1:gt_c[0]["body_close"]]
    return frozen, view, gt_body


def assemble(fz, bodies, pristine=False):
    """canonical = prefix + helpers + enclosing_head + proof body + suffix.

    Statement immutability BY ASSEMBLY: nothing the agent wrote outside the two regions can reach the
    referee, because only the two bodies are read. Pristine restores the original interior, which is what
    makes the self-test byte-exact for the 44 whitespace-variant tasks the literal `{\\n}` would refuse.
    """
    bodies = {} if pristine else (bodies or {})
    helpers = "" if pristine else (bodies.get("helpers") or "").strip()
    hblock = ("\n" + helpers + "\n") if helpers else ""
    if pristine:
        body = fz["proof_interior_original"]
    else:
        p = (bodies.get("proof") or "").strip("\n")
        body = ("\n" + p + "\n") if p.strip() else fz["proof_interior_original"]
    return (fz["prefix"] + fz["enclosing_head"] + body
            + fz["suffix_head"] + hblock + fz["suffix_tail"])


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 2:
        sys.exit(__doc__)
    jsonl, outdir = args
    projects = "AC,NR"
    only = None
    for a in sys.argv[1:]:
        if a.startswith("--projects"):
            projects = a.split("=", 1)[1] if "=" in a else sys.argv[sys.argv.index(a) + 1]
        if a.startswith("--only"):
            only = (a.split("=", 1)[1] if "=" in a else sys.argv[sys.argv.index(a) + 1]).split(",")
    keep = set(projects.split(","))
    os.makedirs(os.path.join(outdir, "views"), exist_ok=True)
    os.makedirs(os.path.join(outdir, "gt"), exist_ok=True)
    counts, built, gt_missing = {}, 0, []
    for line in open(jsonl, encoding="utf-8"):
        rec = json.loads(line)
        if rec["project"] not in keep:
            continue
        if only and rec["task_id"] not in only:
            continue
        try:
            frozen, view, gt_body = build_one(rec)
        except Refuse as r:
            counts[r.cls] = counts.get(r.cls, 0) + 1
            continue
        d = os.path.join(outdir, "views", rec["task_id"])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "task.rs"), "w", encoding="utf-8").write(view)
        json.dump(frozen, open(os.path.join(d, "frozen.json"), "w"), indent=1)
        if gt_body is None:
            gt_missing.append(rec["task_id"])
        else:
            json.dump({"proof": gt_body, "helpers": ""},
                      open(os.path.join(outdir, "gt", rec["task_id"] + ".json"), "w"), indent=1)
        built += 1
    report = dict(built=built, refused=counts, gt_body_missing=gt_missing, projects=sorted(keep))
    json.dump(report, open(os.path.join(outdir, "draw_report.json"), "w"), indent=1)
    print(json.dumps(report, indent=1))


if __name__ == "__main__":
    main()
