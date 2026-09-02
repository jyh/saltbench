#!/usr/bin/env python3
"""screen_verus.py — the token screen over the agent's two BODIES. Importable and a CLI.

DEFENCE IN DEPTH, NOT THE GATE. The gate is check_verus.py's three integrity layers (statement immutability
by assembly, the benchmark's own count guard, lynette `additions`) plus the referee. The screen only refuses
bodies carrying constructs an honest Verus proof of these tasks never needs, so that they are not even
elaborated.

⛔ THE SET IS WRITTEN FROM THE CORPUS OF LEGITIMATE TOKENS, NOT FROM A LIST OF SCARY ONES — that inversion is
the defect the DD refuter caught, and each anchoring below is a measured count in the benchmark, not a taste:
  · the bare substring `axiom` is NOT refused. `axiom_max_phyaddr_width_facts();` is a legitimate call to a
    context fact (17 hits in 3 of 20 sampled files). Only the DECLARING form `axiom fn` is refused.
  · `#![trigger …]` and `#![auto]` are ALLOWED (51 hits in 7 of 20 files); every other inner attribute `#![`
    is refused.
  · `broadcast use <group>;` is ALLOWED — it is a proof statement and lynette whitelists Item::BroadcastUse.
    A line-start `use` NOT preceded by `broadcast` is a new import and IS refused.
  · `#[verifier::…]` is allowed ONLY for the five lynette itself classifies as "instructions about completing
    a proof" (additions.rs is_proof_attr): rlimit, integer_ring, memoize, loop_isolation, spinoff_prover.
    Every other `#[verifier::` / `#[verifier(` is REFUSED — a REGISTERED deliberate restriction, whose control
    is the ground-truth pass: a reference body this screen refuses is a SCREEN DEFECT, not a dead task.

Runs over the bodies AFTER blanking comments, string literals, raw strings and char literals (via rustspan, the
one structural reader), so a token inside a comment or a string cannot trip it. Newlines are preserved so line
numbers hold.

usage: screen_verus.py <bodies.json>   -> JSON list of violations "key: token@line"
       screen_verus.py --selftest      -> drives every red AND green arm, exit 0 iff all pass
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rustspan

PROOF_ATTRS = ("rlimit", "integer_ring", "memoize", "loop_isolation", "spinoff_prover")

# (name, compiled pattern). Order is cosmetic; all are reported.
RULES = [
    ("assume(",            re.compile(r"(?<![A-Za-z0-9_])assume\s*\(")),
    ("assume_specification", re.compile(r"(?<![A-Za-z0-9_])assume_specification(?![A-Za-z0-9_])")),
    ("admit(",             re.compile(r"(?<![A-Za-z0-9_])admit\s*\(")),
    ("external_body",      re.compile(r"(?<![A-Za-z0-9_])external_body(?![A-Za-z0-9_])")),
    ("verifier::external", re.compile(r"#\[\s*verifier\s*(?:::\s*external\b|\(\s*external\s*\))")),
    ("assume_termination", re.compile(r"(?<![A-Za-z0-9_])assume_termination(?![A-Za-z0-9_])")),
    ("exec_allows_no_decreases_clause",
                           re.compile(r"(?<![A-Za-z0-9_])exec_allows_no_decreases_clause(?![A-Za-z0-9_])")),
    ("axiom fn",           re.compile(r"(?<![A-Za-z0-9_])axiom\s+fn(?![A-Za-z0-9_])")),
    ("macro_rules",        re.compile(r"(?<![A-Za-z0-9_])macro_rules(?![A-Za-z0-9_])")),
    ("include!",           re.compile(r"(?<![A-Za-z0-9_])include\s*!")),
    ("include_str!",       re.compile(r"(?<![A-Za-z0-9_])include_str\s*!")),
    ("std::process",       re.compile(r"(?<![A-Za-z0-9_])std\s*::\s*process(?![A-Za-z0-9_])")),
    ("unsafe",             re.compile(r"(?<![A-Za-z0-9_])unsafe(?![A-Za-z0-9_])")),
    ("extern",             re.compile(r"(?<![A-Za-z0-9_])extern(?![A-Za-z0-9_])")),
    ("mod",                re.compile(r"(?<![A-Za-z0-9_])mod\s+[A-Za-z_]")),
    ("fn main",            re.compile(r"(?<![A-Za-z0-9_])fn\s+main(?![A-Za-z0-9_])")),
    ("#[cfg",              re.compile(r"#\[\s*cfg")),
    ("#[test]",            re.compile(r"#\[\s*test\s*\]")),
    ("unimplemented!",     re.compile(r"(?<![A-Za-z0-9_])unimplemented\s*!")),
    ("todo!",              re.compile(r"(?<![A-Za-z0-9_])todo\s*!")),
]
# inner attributes: everything but the two allowed trigger forms
_INNER = re.compile(r"#!\[\s*(?!trigger\b)(?!auto\b)(?!all_triggers\b)")
# a line-start `use` not preceded by `broadcast`
_USE = re.compile(r"(?m)^[ \t]*use[ \t]+")
_BROADCAST_USE = re.compile(r"(?m)^[ \t]*broadcast[ \t]+use[ \t]+")
# any #[verifier...] attribute, so the non-proof ones can be refused
_VERIFIER_ATTR = re.compile(r"#\[\s*verifier\s*(?:::\s*([A-Za-z_][A-Za-z0-9_]*)|\(\s*([A-Za-z_][A-Za-z0-9_]*))")
# helpers-region item shapes that are not a proof fn
_HELPER_BAD = [
    ("spec fn",         re.compile(r"(?<![A-Za-z0-9_])spec\s+fn(?![A-Za-z0-9_])")),
    ("exec fn",         re.compile(r"(?<![A-Za-z0-9_])exec\s+fn(?![A-Za-z0-9_])")),
    ("impl",            re.compile(r"(?m)^[ \t]*(?:pub[ \t]+)?impl(?![A-Za-z0-9_])")),
    ("trait",           re.compile(r"(?m)^[ \t]*(?:pub[ \t]+)?trait(?![A-Za-z0-9_])")),
    ("const",           re.compile(r"(?m)^[ \t]*(?:pub[ \t]+)?const(?![A-Za-z0-9_])")),
    ("broadcast proof", re.compile(r"(?m)^[ \t]*(?:pub[ \t]+)?broadcast[ \t]+proof(?![A-Za-z0-9_])")),
]


# ─────────────────────────────────────────────────────────────────────────────────────────────────────────
# ROW AV — WHAT THE CHECKER REFUSES, THE AGENT MUST HAVE BEEN TOLD.
#
# Row AV was opened against S2-Lean: `native_decide` is effectively out of bounds and NO PROMPT SAYS SO, so
# an episode can fail on a rule the agent was never given. The helm ruled it ripens at this regime boundary.
# MEASURED HERE BEFORE ANY REPAIR: of the 29 refusal rules this screen enforces, the S2-Rust prompts named
# 12 and left **17 unstated** — including two an agent would plausibly reach for while writing a legitimate
# helper lemma: a new `use` import (only `broadcast use` is allowed) and `todo!`/`unimplemented!`.
#
# ⛔⛔ AND THE UNSTATED SURFACE IS ARM-RELEVANT, WHICH IS WHY THIS IS NOT COSMETIC. The `use` rule bites in
# the HELPERS region, and the salt arm `a2` is the arm that ENCOURAGES helper lemmas. This is amendment 15's
# FATAL 3 wearing different clothes: an instrument that penalises the treatment for applying the treatment
# manufactures the opposite effect. Asking "which arm is likelier to trip this gate, and why" is now a
# standing question for every gate this campaign adds.
#
# ⇒ THE REPAIR IS NOT PROSE, IT IS A GATE. Stating the rules in a prompt fixes today and rots tomorrow: the
#   next rule added to RULES would be unstated again, and nothing would notice. This registry makes the
#   prompt a CONSUMER of the rule set: every entry below must name a phrase that literally appears in the
#   agent-visible prompt text, and `selftest_prompt_coverage.py` REFUSES a rule with no entry at all — so a
#   rule cannot be added to the checker without the same commit telling the agent about it.
#   📌 The value is the phrase the AGENT reads, not a restatement of the regex: a rule the prompt states in
#      different words than the code uses is still stated.
PROMPT_COVERAGE = {
    "assume(": "assume", "assume_specification": "assume_specification", "admit(": "admit",
    "external_body": "external_body", "verifier::external": "verifier::external",
    "assume_termination": "assume_termination",
    "exec_allows_no_decreases_clause": "exec_allows_no_decreases_clause",
    "axiom fn": "axiom fn", "macro_rules": "macro_rules", "include!": "include!",
    "include_str!": "include_str!", "std::process": "std::process", "unsafe": "unsafe",
    "extern": "extern", "mod": "mod", "fn main": "fn main", "#[cfg": "#[cfg",
    "#[test]": "#[test]", "unimplemented!": "unimplemented!", "todo!": "todo!",
    "#![ (non-trigger)": "inner attribute", "use (new import)": "new `use` import",
    "#[verifier::X] non-proof": "#[verifier::",
    "spec fn (helpers)": "spec fn", "exec fn (helpers)": "exec fn", "impl (helpers)": "impl",
    "trait (helpers)": "trait", "const (helpers)": "const",
    "broadcast proof (helpers)": "broadcast proof",
}


def rule_names():
    """Every refusal rule this screen enforces, by the name it reports — the gate's subject.

    Derived from the live tables rather than typed, so a rule added to RULES or _HELPER_BAD appears here
    automatically and the coverage gate goes red until the prompt names it.
    """
    return ([n for n, _ in RULES]
            + ["#![ (non-trigger)", "use (new import)", "#[verifier::X] non-proof"]
            + ["%s (helpers)" % n for n, _ in _HELPER_BAD])


def strip(src):
    """Blank comments, strings, raw strings and char literals; keep newlines so line numbers hold."""
    try:
        _, incode = rustspan.code_map(src)
    except rustspan.SpanError:
        return src          # unlexable: screen the raw text, which can only refuse MORE
    return "".join(c if (incode[i] or c == "\n") else " " for i, c in enumerate(src))


def helpers_shape(helpers_text):
    """WHITELIST the helpers region: every top-level item must be a `proof fn` / `pub proof fn`.

    ⛔ THIS IS A SEPARATE STRUCTURAL GATE, NOT PART OF THE TOKEN SCREEN, AND `--no-screen` DOES NOT DISABLE IT.
    Reason, measured: the helpers region is appended PAST the end of the original item list so that lynette
    `additions` accepts it (build_views_verus.py's docstring), and lynette's lockstep loop therefore never
    EXAMINES anything in that region — an added `axiom fn` there is invisible to layer 4. The end-of-block
    placement buys acceptance of legitimate helpers and pays for it in layer-4 coverage of that region, so
    the region needs a structural gate of its own. A whitelist, not a blacklist: the blacklist this replaces
    passed every named bad shape and would have admitted every unnamed one.
    """
    s = strip(helpers_text or "")
    out = []
    i, n, depth, start = 0, len(s), 0, None
    while i < n:
        c = s[i]
        if depth == 0 and start is None and not c.isspace():
            start = i
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0 and start is not None:
                out.append((start, s[start:i + 1])); start = None
        elif c == ";" and depth == 0 and start is not None:
            out.append((start, s[start:i + 1])); start = None
        i += 1
    if start is not None:
        out.append((start, s[start:]))
    bad = []
    for off, item in out:
        head = item
        while True:
            h = head.lstrip()
            if h.startswith("#["):
                d = 0
                for k, ch in enumerate(h):
                    if ch == "[":
                        d += 1
                    elif ch == "]":
                        d -= 1
                        if d == 0:
                            head = h[k + 1:]; break
                else:
                    break
                continue
            head = h
            break
        if not re.match(r"(?:pub\s+)?proof\s+fn\b", head):
            bad.append("helpers: item %d is not a `proof fn`@%d" % (len(bad) + 1, _line(s, off)))
    return bad


def _line(s, i):
    return s.count("\n", 0, i) + 1


def violations(bodies):
    out = []
    for key in ("proof", "helpers"):
        raw = bodies.get(key) or ""
        s = strip(raw)
        for name, pat in RULES:
            for m in pat.finditer(s):
                out.append("%s: %s@%d" % (key, name, _line(s, m.start())))
        for m in _INNER.finditer(s):
            out.append("%s: #![ (non-trigger)@%d" % (key, _line(s, m.start())))
        bcast = {m.end() for m in _BROADCAST_USE.finditer(s)}
        for m in _USE.finditer(s):
            if m.end() not in bcast:
                out.append("%s: use (new import)@%d" % (key, _line(s, m.start())))
        for m in _VERIFIER_ATTR.finditer(s):
            attr = m.group(1) or m.group(2)
            if attr not in PROOF_ATTRS:
                out.append("%s: #[verifier::%s]@%d" % (key, attr, _line(s, m.start())))
        if key == "helpers":
            for name, pat in _HELPER_BAD:
                for m in pat.finditer(s):
                    out.append("%s: %s (helpers must be proof fn)@%d" % (key, name, _line(s, m.start())))
    return out


# ---------------------------------------------------------------- selftest
CASES = [
    # (name, bodies, expect_violation)  — RED arms
    ("assume",            {"proof": "assume(false);"}, True),
    ("admit",             {"proof": "admit();"}, True),
    ("assume_specification", {"proof": "assume_specification foo;"}, True),
    ("external_body helper", {"helpers": "#[verifier::external_body]\nproof fn h() {}"}, True),
    ("axiom fn",          {"helpers": "pub axiom fn a() ensures false;"}, True),
    ("new import",        {"proof": "use std::collections::HashMap;"}, True),
    ("inner attr",        {"proof": "#![allow(unused)]"}, True),
    ("spec fn in helpers", {"helpers": "spec fn s() -> bool { true }"}, True),
    ("exec fn in helpers", {"helpers": "exec fn e() {}"}, True),
    ("impl in helpers",   {"helpers": "impl Foo { }"}, True),
    ("unimplemented",     {"proof": "unimplemented!()"}, True),
    ("std::process",      {"proof": "std::process::exit(0);"}, True),
    ("verifier attr not in the five", {"proof": "#[verifier::truncate] assert(true);"}, True),
    ("fn main",           {"helpers": "fn main() {}"}, True),
    # GREEN arms — WITHOUT THESE THE SCREEN ONLY PROVES IT REFUSES EVERYTHING
    ("trigger inner attr", {"proof": "assert forall|i: int, j: int| #![trigger f(i, j)] p(i, j) by { }"}, False),
    ("auto inner attr",   {"proof": "assert forall|i: int| #![auto] p(i) by { }"}, False),
    ("all_triggers inner attr",  # the form the screen's own control found; see the module docstring
                          {"proof": "assert forall |c1, c2| #![all_triggers] p(c1, c2) by { }"}, False),
    ("a NON-trigger inner attr is STILL refused",  # the control that keeps the widening narrow
                          {"proof": "#![allow(dead_code)] assert(true);"}, True),
    ("broadcast use",     {"proof": "broadcast use group_mul_properties;"}, False),
    ("axiom_ call",       {"proof": "axiom_max_phyaddr_width_facts();"}, False),
    ("by nonlinear_arith", {"proof": "assert(x * y >= 0) by (nonlinear_arith) requires x >= 0, y >= 0;"}, False),
    ("by(bit_vector) no space", {"proof": "assert(a & b == b & a) by(bit_vector);"}, False),
    ("reveal + decreases", {"proof": "reveal(f);\nreveal_with_fuel(f, 2);"}, False),
    ("trigger attr",      {"proof": "assert forall|i: int| #[trigger] f(i) by { }"}, False),
    ("proof fn helper",   {"helpers": "pub proof fn lemma_x(a: nat)\n  ensures a >= 0\n{ }"}, False),
    ("verifier::rlimit is allowed", {"proof": "#[verifier::rlimit(50)] assert(true);"}, False),
    ("calc!",             {"proof": "calc! { (==) a; { } b; }"}, False),
    # the token inside a COMMENT or a STRING must not trip the screen
    ("assume in a comment", {"proof": "// assume(false) is what we do NOT do\nassert(true);"}, False),
    ("assume in a string", {"proof": 'let s = "assume(false)"; assert(true);'}, False),
]


def selftest():
    bad = 0
    for name, bodies, expect in CASES:
        got = bool(violations(bodies))
        ok = got == expect
        bad += not ok
        print("%-4s %-34s expect=%-5s got=%-5s %s" % ("ok" if ok else "FAIL", name, expect, got,
                                                      "" if ok else violations(bodies)))
    print("\nscreen_verus selftest: %d arms, %d failed" % (len(CASES), bad))
    return 1 if bad else 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    print(json.dumps(violations(json.load(open(sys.argv[1])))))
