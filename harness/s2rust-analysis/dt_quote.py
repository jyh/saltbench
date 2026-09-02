#!/usr/bin/env python3
"""dt_quote.py — price the row-DT Sonnet read from the 3-id PAIRED probe, and apply gates G1/G2.

Council 09/02: "DT both arms at Sonnet". Helm gates, as RE-CUT 08:37 on this seat's denominator finding:
  G1 SPEND   the 13-id TWO-ARM read (26 episodes) PROCEEDS UNASKED if its quoted PER-EPISODE QUOTA
             <= 2x the Opus read's measured per-episode quota. Tokens are reported BESIDE quota, never
             as the gate. HARD CEILING regardless: <= 25 percentage points of the bench account's weekly.
  G2 CENSORING  report the censoring fraction beside the count; >=2 of 3 at the cap => the 13-id read at
             MAX_TURNS=40 is registered in its own header as PARTLY A CAP MEASUREMENT.

⭐ THE GATE IS A RATIO, SO IT NEEDS NO ABSOLUTE QUOTA READING — WHICH IS THE ONLY REASON THIS SEAT CAN
   IMPLEMENT IT. There is no non-invasive quota reader here (a standing refusal in this seat's bank), so an
   absolute "quota used" is not measurable. But G1 compares Sonnet's per-episode quota to OPUS's, and

       sonnet_quota/ep <= 2 x opus_quota/ep
   <=> (S_tok/ep x qpt_sonnet) <= 2 x (O_tok/ep x qpt_opus)
   <=> token_ratio <= 2 x (qpt_opus / qpt_sonnet)

   so everything cancels except the measured TOKEN ratio (this probe) and the tier's QUOTA-PER-TOKEN ratio.

⚠️ THE ONE IMPORTED CONSTANT, NAMED AS SUCH. qpt_opus/qpt_sonnet = 2.19 is measured on S2-LEAN, not here
   (stage B, same 60 episodes: Opus x0.24 tokens but x0.53 quota => 0.53/0.24 = 2.21 ~ the banked 2.19).
   Importing a number from an adjacent population is this seat's most-repeated defect, so it is imported
   only with the test of whether it TRANSFERS: quota-per-token is a weighted average over token CLASSES, so
   it transfers exactly insofar as the class mix matches. MEASURED: S2-Rust/Opus here is 93.20% cache_read;
   S2-Lean/Sonnet was 93.2%. The mixes agree to two decimals, so the weighting is the same and what remains
   is the tiers' per-class price ratio -- a property of the models, not of the substrate.
   ⛔ It is still an import. The report prints the gate's verdict at 2.19 AND the sensitivity band, so a
   reader who rejects the constant can still read the answer off the table.
"""
import sys, os, json, re, statistics, argparse

# ---- the Opus read, measured (draw ranks 1..10, in draw order) -------------------------------------------
OPUS_READ = [  # (draw_rank, episode, class, calls, metered)
    (1,  "ep-34aa0535", "VERIFY_FAIL", 40, 3255428),
    (2,  "ep-dd13ed30", "PASS",        23,  957722),
    (3,  "ep-a2f50c0e", "PASS",        26, 1366939),
    (4,  "ep-e3895808", "PASS",        32, 2150320),
    (5,  "ep-0e3ab1ab", "PASS",        27, 1106010),
    (6,  "ep-0951cdb5", "PASS",        40, 3132914),
    (7,  "ep-b6310c13", "PASS",        35, 2215679),
    (8,  "ep-3e844002", "PASS",        27, 1613737),
    (9,  "ep-99735220", "PASS",        39, 3524943),
    (10, "ep-651e86f2", "PASS",        35, 3101197),
]
QPT_OPUS_OVER_SONNET = 2.19   # imported, S2-Lean; transfer-tested by the class mix (see docstring)
G1_MULT   = 2.0               # "<= 2x the Opus read's measured per-episode quota"
N_IDS     = 13
N_ARMS    = 2
N_EPISODES = N_IDS * N_ARMS   # 26
CAP       = 40
WEEKLY_PT_PER_SONNET_TOK = 1.0 / 19_670_000   # S2-Lean anchor: 19.67M Sonnet tokens moved weekly 54%->55%
WEEKLY_CEILING_PTS = 25.0

def money(x):
    return "{:,}".format(int(round(x)))

def load_manifests(path):
    txt = open(path).read()
    blocks = re.split(r'^##### ', txt, flags=re.M)[1:]
    dec = json.JSONDecoder(); out = {}
    for b in blocks:
        ep, rest = b.split('\n', 1)
        try:
            m, _ = dec.raw_decode(rest.lstrip())
        except Exception:
            continue
        out[ep.strip()] = m
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe-manifests", required=True)
    ap.add_argument("--served", default=None, help="lines: <ep> <model>=<count>[,...]")
    ap.add_argument("--expect-model", default="claude-sonnet-5")
    a = ap.parse_args()

    mans = load_manifests(a.probe_manifests)
    if not mans:
        print("REFUSE: no probe manifests parsed from %s" % a.probe_manifests); return 4
    probe = sorted(mans.values(), key=lambda m: m["start_utc"])

    W = 110
    print("=" * W)
    print("ROW DT — THE SONNET QUOTE, FROM THE 3-ID PAIRED PROBE ON THE HARD BAND")
    print("gate G1 as re-cut 08:37: per-episode QUOTA <= %.1fx the Opus read's, over %d episodes" % (G1_MULT, N_EPISODES))
    print("=" * W)

    # ---- GATE 0: the tier actually served ----------------------------------------------------------------
    served = {}
    if a.served and os.path.exists(a.served):
        for line in open(a.served):
            p = line.split()
            if len(p) >= 2:
                served[p[0]] = p[1]
    print("\nGATE 0 — THE TIER THAT ACTUALLY SERVED (message.model; model_requested is a REQUEST)")
    bad = []
    for m in probe:
        ep = m["episode"]; s = served.get(ep, "UNREAD")
        ok = (a.expect_model in s) and ("opus" not in s)
        if not ok: bad.append(ep)
        print("  %-13s requested=%-18s served=%-40s %s" % (ep, m.get("model_requested"), s,
                                                           "ok" if ok else "*** MISMATCH ***"))
    if bad:
        print("  ⛔ REFUSE: a tier contrast whose tier is unverified is not one (%d mismatched)." % len(bad))
    else:
        print("  ✅ every probe episode served by %s" % a.expect_model)

    # ---- the pairing --------------------------------------------------------------------------------------
    print("\nTHE PAIRING — same task, same arm, same instrument; only MODEL differs")
    print("  %-4s %-13s %-14s %5s %11s | %-13s %-14s %5s %11s | %6s" % (
        "rank", "sonnet ep", "class", "calls", "tokens", "opus ep", "class", "calls", "tokens", "ratio"))
    rows = []
    for i, m in enumerate(probe):
        o = OPUS_READ[i]
        tok = m.get("metered_sum") or 0
        r = tok / o[4] if o[4] else float("nan")
        rows.append(dict(rank=i+1, ep=m["episode"], cls=m.get("check_class"), calls=m.get("calls") or 0,
                         tok=tok, o_tok=o[4], o_cls=o[2], o_calls=o[3], ratio=r,
                         term=m.get("termination"), classes=m.get("metered_classes") or {}))
        print("  %-4d %-13s %-14s %5s %11s | %-13s %-14s %5s %11s | %5.2fx" % (
            i+1, m["episode"], m.get("check_class"), m.get("calls"), money(tok),
            o[1], o[2], o[3], money(o[4]), r))
    s_sum = sum(r["tok"] for r in rows); o_sum = sum(r["o_tok"] for r in rows)
    ratio = s_sum / o_sum if o_sum else float("nan")
    print("  %-4s %-13s %-14s %5s %11s | %-13s %-14s %5s %11s | %5.2fx" % (
        "SUM", "", "", "", money(s_sum), "", "", "", money(o_sum), ratio))
    print("\n  AGGREGATE paired TOKEN ratio (the estimator that prices a run) : %.2fx" % ratio)
    print("  MEDIAN per-episode ratio (robust; reported, not used)          : %.2fx" %
          statistics.median([r["ratio"] for r in rows]))
    for r in rows:
        if r["cls"] != r["o_cls"]:
            print("  ⚠️  rank %d class MOVED %s (opus) -> %s (sonnet): its ratio carries an OUTCOME change,"
                  % (r["rank"], r["o_cls"], r["cls"]))
            print("      not only a tier price. A tier that fails where the other passed pays the cap, not the task.")

    # ---- the class mix, the transfer test for the imported constant ---------------------------------------
    tot = {}
    for r in rows:
        for k, v in r["classes"].items(): tot[k] = tot.get(k, 0) + v
    st = sum(tot.values())
    print("\n  TRANSFER TEST for the imported quota-per-token constant — the Sonnet probe's class mix")
    if st:
        for k, v in sorted(tot.items(), key=lambda x: -x[1]):
            print("    %-28s %13s  %6.2f%%" % (k, money(v), 100*v/st))
        cr = 100*tot.get("cache_read_input_tokens", 0)/st
        print("    cache_read here %.2f%%  vs  S2-Rust/Opus 93.20%%  vs  S2-Lean/Sonnet 93.2%%" % cr)
        print("    %s" % ("✅ mixes agree ⇒ the weighting transfers; what remains is the tiers' price ratio."
                          if abs(cr - 93.2) < 3 else
                          "⛔ MIX DIFFERS ⇒ the 2.19x import is NOT justified here; treat the gate as unmeasured."))

    # ---- G1 -----------------------------------------------------------------------------------------------
    o_per_ep = sum(o[4] for o in OPUS_READ) / len(OPUS_READ)
    s_per_ep = o_per_ep * ratio
    ratio_limit = G1_MULT * QPT_OPUS_OVER_SONNET
    quota_rel = ratio / QPT_OPUS_OVER_SONNET     # sonnet per-ep quota, in units of opus per-ep quota
    print("\nG1 — THE GATE, IN QUOTA UNITS, PER EPISODE")
    print("  Opus per-episode, measured        : %13s tokens  (22,424,889 / 10)" % money(o_per_ep))
    print("  Sonnet per-episode, quoted        : %13s tokens  (= Opus/ep x %.2fx)" % (money(s_per_ep), ratio))
    print("  tokens are BESIDE the gate, not the gate  ⇑")
    print("  Sonnet per-episode QUOTA          : %.2fx the Opus per-episode quota" % quota_rel)
    print("    (= token ratio %.2fx / quota-per-token %.2fx)" % (ratio, QPT_OPUS_OVER_SONNET))
    print("  G1 limit                          : %.2fx  ⇔ a token ratio of %.2fx" % (G1_MULT, ratio_limit))
    g1 = quota_rel <= G1_MULT
    print("  %s G1 %s (%.2f of the %.1fx allowance)" % ("✅" if g1 else "⛔", "PASSES ⇒ PROCEED UNASKED" if g1
                                                        else "FAILS ⇒ HOLD AND POST", quota_rel, G1_MULT))

    # ---- the hard weekly ceiling --------------------------------------------------------------------------
    tot_tok = s_per_ep * N_EPISODES
    pts = tot_tok * WEEKLY_PT_PER_SONNET_TOK
    print("\n  HARD CEILING — the bench account's weekly, %.0f points" % WEEKLY_CEILING_PTS)
    print("    read total, %d episodes          : %13s tokens (reported, not the gate)" % (N_EPISODES, money(tot_tok)))
    print("    weekly points, at the S2-Lean anchor (19.67M Sonnet tok = 1 pt) : %.1f of %.0f" % (pts, WEEKLY_CEILING_PTS))
    print("    %s" % ("✅ under the ceiling" if pts <= WEEKLY_CEILING_PTS else "⛔ OVER THE CEILING ⇒ HOLD"))
    print("    binding order: the ratio gate binds at %.2fx, the weekly ceiling at %.2fx ⇒ %s binds first"
          % (ratio_limit, WEEKLY_CEILING_PTS/(o_per_ep*N_EPISODES*WEEKLY_PT_PER_SONNET_TOK),
             "the RATIO GATE" if ratio_limit < WEEKLY_CEILING_PTS/(o_per_ep*N_EPISODES*WEEKLY_PT_PER_SONNET_TOK)
             else "the WEEKLY CEILING"))

    # ---- G2 -----------------------------------------------------------------------------------------------
    passes = sum(1 for r in rows if r["cls"] == "PASS")
    capped = [r for r in rows if r["calls"] >= CAP]
    print("\nG2 — CENSORING, REPORTED BESIDE THE COUNT")
    print("  passes            : %d of %d   (Opus on the same three: %d of 3)" %
          (passes, len(rows), sum(1 for o in OPUS_READ[:3] if o[2] == "PASS")))
    print("  at the cap (%d)    : %d of %d" % (CAP, len(capped), len(rows)))
    if len(capped) >= 2:
        print("  ⛔ the 13-id read at MAX_TURNS=40 must be headed PARTLY A CAP MEASUREMENT;")
        print("     the MAX_TURNS=120 arm is a SEPARATE row, never a re-cut of this one.")
    elif capped:
        print("  ⚠️  the cap binds on at least one episode — never report the count alone.")
    else:
        print("  ✅ no probe episode reached the cap.")

    # ---- sensitivity --------------------------------------------------------------------------------------
    print("\nSENSITIVITY — n=3, and the token ratio is the whole quote")
    print("  %-14s %-14s %-9s %-8s" % ("token ratio", "quota vs opus", "weekly pts", "G1"))
    for rr in sorted({ratio*0.5, ratio*0.75, ratio, ratio*1.25, ratio*1.5, ratio_limit}):
        q = rr / QPT_OPUS_OVER_SONNET
        p = o_per_ep * rr * N_EPISODES * WEEKLY_PT_PER_SONNET_TOK
        print("  %-14s %-14s %-9s %-8s" % ("%.2fx" % rr, "%.2fx" % q, "%.1f" % p,
                                           "PASS" if q <= G1_MULT else "FAIL"))
    print("=" * W)
    return 0

if __name__ == "__main__":
    sys.exit(main())
