#!/usr/bin/env python3
"""lane_identity.py — §Q3.4 item 2, the half a tool can carry: DOES THIS CONFIG DIR AUTHENTICATE AS THE
ACCOUNT WE INTENDED? Compares a DIGEST of the identity against a recorded expectation. Never prints the value.

    lane_identity.py --cfg <dir> --expect <sha256/16>   [--credential]
    lane_identity.py --cfg <dir> --print-digest          (prints the digest; LOUDLY NOT A CHECK)
    lane_identity.py --self-test

⛔ WHY IT EXISTS. `clb_stage.sh` reads `oauthAccount.emailAddress` and refuses only when it is EMPTY:

      [ -n "${em:-}" ] || die "account identity UNREADABLE for CLB_CFG — unreadable is not a pass"
      say "ACCOUNT identity read (not printed: the infra-name gate)"

That is a READABILITY check. Any non-empty value passes, INCLUDING THE WRONG ACCOUNT -- and the log line
"ACCOUNT identity read" is what a lead reads as *verified*. The comment above that code names the right law
("identity by the account the dir authenticates as, never by its name") and the code implements only its
weaker half: "never by its name" is satisfied; "the account it authenticates as" is read and compared to
nothing. ⇒ A CORRECTLY-NAMED CONFIG DIR CAN AUTHENTICATE AS A DIFFERENT ACCOUNT, this campaign has already
had that happen with a 21-arm preflight passing it, and a lane that MOVES between accounts meets the hazard
every time it moves.

⛔ A MISSING EXPECTATION IS NOT A PASS (rc 4). Without --expect there is nothing to compare, and a tool that
returned 0 in that case would reproduce the defect it exists to fix, one level up.
⛔ THE EXPECTATION CANNOT BE TAKEN FROM THE BOX. A digest read off the dir and then compared to itself
blesses whatever is there. The expected digest is recorded ONCE by a human who knows the intended account
-- for this campaign, on the Captain's word after he performs the login -- and is mechanical thereafter.
⛔ WHAT IT DOES NOT DO: §Q3.4 item 2 also requires "a trivial authenticated read checked by its BODY". That
costs a call and is NOT performed here. --credential checks only the OFFLINE shape of the credential file,
and the report SAYS SO beside its verdict, because a limit must ride where the verdict rides.

THE VALUE NEVER LEAVES. Only sha256/16 is printed, per the tree's infra-name gate. Self-test arm 8 proves it.
"""
import argparse, hashlib, json, os, sys, time

def digest(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]

def identity(cfg, out):
    p = os.path.join(os.path.expanduser(cfg), ".claude.json")
    if not os.path.exists(p):
        out("REFUSE rc 2: no .claude.json under the config dir. Absent is not empty and neither is a pass."); return None, 2
    try:
        d = json.load(open(p))
    except Exception as e:
        out("REFUSE rc 2: .claude.json is unparsable (%s). Unparsable is not a pass." % type(e).__name__); return None, 2
    em = ((d.get("oauthAccount") or {}) or {}).get("emailAddress") or ""
    if not em.strip():
        out("REFUSE rc 3: the config dir has NO readable account identity. Unreadable is not a pass."); return None, 3
    return em.strip(), 0

def credential(cfg, out):
    """The OFFLINE half only. Never a substitute for the body-checked authenticated read."""
    p = os.path.join(os.path.expanduser(cfg), ".credentials.json")
    if not os.path.exists(p):
        out("REFUSE rc 6: no .credentials.json under the config dir — the client exits 0 on an auth failure,"
            " so an absent credential must be caught HERE, not at the fire."); return 6
    try:
        o = (json.load(open(p)).get("claudeAiOauth") or {})
    except Exception as e:
        out("REFUSE rc 6: .credentials.json is unparsable (%s)." % type(e).__name__); return 6
    has_refresh = bool(o.get("refreshToken"))
    exp = o.get("expiresAt")
    fresh = bool(exp) and (exp / 1000.0) > time.time()
    if not fresh and not has_refresh:
        out("REFUSE rc 6: the access token is expired or absent AND there is no refresh token."); return 6
    out("    credential: present · refresh token %s · access token %s" % (
        "present" if has_refresh else "ABSENT", "valid" if fresh else "expired (a refresh token is present)"))
    out("    ⛔ THIS IS THE OFFLINE SHAPE ONLY. §Q3.4 item 2's trivial AUTHENTICATED READ, checked by its")
    out("       BODY, is NOT performed here and is still owed at the preflight.")
    return 0

def run(cfg, expect, do_cred, print_digest, out):
    em, rc = identity(cfg, out)
    if rc:
        return rc
    got = digest(em)
    if print_digest:
        out("DIGEST %s" % got)
        out("⛔ THIS IS NOT A CHECK. It reports what the dir authenticates as, so a human who knows the")
        out("   intended account can record it as --expect. Comparing this to itself blesses whatever is there.")
        return 0
    if not expect:
        out("REFUSE rc 4: no --expect supplied. A MISSING EXPECTATION IS NOT A PASS — that is the same defect"
            " this tool exists to fix, one level up. Use --print-digest to obtain a value to record.")
        return 4
    if got != expect:
        out("REFUSE rc 5: IDENTITY MISMATCH. expected %s · got %s" % (expect, got))
        out("   (neither account is named: only digests cross this boundary, per the infra-name gate)")
        return 5
    out("IDENTITY OK: the config dir authenticates as the expected account (digest %s)." % got)
    return credential(cfg, out) if do_cred else 0

def self_test():
    import tempfile
    ok = [True]
    def check(c, m):
        ok[0] = ok[0] and c
        print(("  PASS " if c else "  FAIL ") + m)
    MARK = "zzmarker-identity-value@example.invalid"   # a distinctive value that must NEVER be printed
    lines = []
    out = lines.append
    with tempfile.TemporaryDirectory() as t:
        def mk(name, claude=None, creds=None):
            d = os.path.join(t, name); os.makedirs(d)
            if claude is not None: open(os.path.join(d, ".claude.json"), "w").write(json.dumps(claude))
            if creds is not None: open(os.path.join(d, ".credentials.json"), "w").write(json.dumps(creds))
            return d
        good = mk("good", {"oauthAccount": {"emailAddress": MARK}})
        D = digest(MARK)
        lines.clear(); check(run(mk("none"), D, False, False, out) == 2 and any("rc 2" in l for l in lines),
                             "RED no .claude.json -> rc 2, 'absent is not empty and neither is a pass'")
        lines.clear(); check(run(mk("noacct", {"other": 1}), D, False, False, out) == 3,
                             "RED no oauthAccount -> rc 3, 'unreadable is not a pass'")
        lines.clear(); check(run(mk("empty", {"oauthAccount": {"emailAddress": "   "}}), D, False, False, out) == 3,
                             "RED an all-whitespace identity -> rc 3 (the shape clb_stage.sh's -n test would PASS)")
        lines.clear(); rc = run(good, None, False, False, out)
        check(rc == 4 and any("MISSING EXPECTATION IS NOT A PASS" in l for l in lines),
              "RED no --expect -> rc 4, refuses rather than passing")
        lines.clear(); rc = run(good, "0000000000000000", False, False, out)
        body_mm = "\n".join(lines)
        check(rc == 5 and "0000000000000000" in body_mm and D in body_mm,
              "RED a wrong expectation -> rc 5, and BOTH digests are named")
        lines.clear(); check(run(good, D, False, False, out) == 0, "GREEN the right expectation -> rc 0")
        lines.clear(); rc = run(good, None, False, True, out)
        check(rc == 0 and any("THIS IS NOT A CHECK" in l for l in lines),
              "--print-digest exits 0 and says LOUDLY that it is not a check")
        # arm 8 — THE VALUE NEVER LEAVES, proven with a positive control
        all_out = []
        for args in ((good, D, False, False), (good, "0000000000000000", False, False),
                     (good, None, False, False), (good, None, False, True)):
            lines.clear(); run(*args, out); all_out += lines
        body = "\n".join(all_out)
        check(MARK not in body and D in body,
              "the identity VALUE appears in NO output across four paths, while its DIGEST does (positive control)")
        # credential arms
        cred_none = mk("cnone", {"oauthAccount": {"emailAddress": MARK}})
        lines.clear(); check(run(cred_none, D, True, False, out) == 6,
                             "RED --credential with no .credentials.json -> rc 6 (the client exits 0 on auth failure)")
        past = int((time.time() - 3600) * 1000)
        cred_exp = mk("cexp", {"oauthAccount": {"emailAddress": MARK}},
                      {"claudeAiOauth": {"expiresAt": past, "refreshToken": "r"}})
        lines.clear(); rc = run(cred_exp, D, True, False, out)
        check(rc == 0 and any("refresh token is present" in l for l in lines),
              "an EXPIRED access token with a refresh token is a NOTE, not a refusal — and it is stated")
        cred_dead = mk("cdead", {"oauthAccount": {"emailAddress": MARK}},
                       {"claudeAiOauth": {"expiresAt": past}})
        lines.clear(); check(run(cred_dead, D, True, False, out) == 6,
                             "RED expired AND no refresh token -> rc 6")
        lines.clear(); run(cred_exp, D, True, False, out)
        check(any("NOT performed here and is still owed" in l for l in lines),
              "the limit rides WITH the verdict: the body-checked read is declared un-run, beside the green")
    print("lane_identity SELF-TEST: " + ("OK" if ok[0] else "FAILED"))
    return 0 if ok[0] else 1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cfg"); ap.add_argument("--expect"); ap.add_argument("--credential", action="store_true")
    ap.add_argument("--print-digest", action="store_true"); ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test: return self_test()
    if not a.cfg:
        print("usage: lane_identity.py --cfg <dir> --expect <sha256/16> [--credential] | --print-digest"); return 64
    return run(a.cfg, a.expect, a.credential, a.print_digest, print)

if __name__ == "__main__":
    sys.exit(main())
