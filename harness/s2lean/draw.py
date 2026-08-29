#!/usr/bin/env python3
"""draw.py — the frozen, arm-independent draw over CLEVER's REAL id set (repair round 1, D6).
Population: the 161 problem_* views = HumanEval ids 0..163 minus {22, 137, 162} (those three files do not exist in the
pinned CLEVER clone; 161 and 163 do). The order is sha256("problem_<id>" + SEED); the four pre-registered excluded ids
(32, 39, 123, 160 — flagged.json excluded_ids) are REMOVED before the first k are taken, so a k-draw is k scorable
problems and the F3 denominator is k by construction. The id list is a LITERAL (never a live `ls views/`).
usage: draw.py <k> [--bare]      prints the first k as `problem_<id>` (the driver's form); --bare prints bare ids
       draw.py --self-check      asserts the population, the exclusion list against flagged.json and the pinned k=30
import: draw.order() / draw.draw(k) / draw.IDS / draw.EXCLUDED for s2_morning_line.py (same code, no subprocess)."""
import hashlib, json, os, sys

SEED = "saltbench-s2lean-stage0-2026-08-29"
MISSING = (22, 137, 162)                 # HumanEval ids with no CLEVER file at the pinned commit
EXCLUDED = (32, 39, 123, 160)            # pre-registered, arm-independent (flagged.json excluded_ids)
IDS = [i for i in range(164) if i not in MISSING]
assert len(IDS) == 161, len(IDS)
PINNED_30 = [109, 34, 73, 90, 159, 12, 69, 0, 163, 146, 129, 16, 4, 81, 38, 142, 110, 96, 112, 141,
             31, 114, 75, 54, 127, 18, 74, 51, 82, 99]

def order():
    """the full 161-id order (excluded ids still present), `problem_<id>` strings"""
    ids = ["problem_%d" % i for i in IDS]
    ids.sort(key=lambda i: hashlib.sha256((i + SEED).encode()).hexdigest())
    return ids

def pid(t):
    return int(t.split("_")[1])

def draw(k):
    """the first k NON-excluded ids of the order, `problem_<id>` strings"""
    return [t for t in order() if pid(t) not in EXCLUDED][:k]

def self_check():
    here = os.path.dirname(os.path.abspath(__file__))
    fl = json.load(open(os.path.join(here, "flagged.json")))
    assert sorted(fl["excluded_ids"]) == sorted(EXCLUDED), ("flagged.json excluded_ids != draw.EXCLUDED", fl["excluded_ids"], EXCLUDED)
    got = [pid(t) for t in draw(30)]
    assert got == PINNED_30, ("draw(30) != pinned", got)
    assert len(order()) == 161 and len(set(order())) == 161
    assert not (set(pid(t) for t in draw(161)) & set(EXCLUDED)) and len(draw(161)) == 157
    return got

if __name__ == "__main__":
    if "--self-check" in sys.argv:
        got = self_check()
        print("PASS draw self-check: population 161 (0..163 minus %s), excluded %s removed, draw(30) == pinned: %s"
              % (list(MISSING), list(EXCLUDED), " ".join(map(str, got))))
        sys.exit(0)
    k = int(sys.argv[1])
    d = draw(k)
    print(" ".join(str(pid(t)) for t in d) if "--bare" in sys.argv else " ".join(d))
