# `lane_identity.py` — the identity half of §Q3.4 item 2, and the check it replaces

bench, 2026-09-17.

## What it replaces, at the code
`clb_stage.sh` (the frozen export) checks the account like this:

    em=$(python3 -c '… .get("oauthAccount") … .get("emailAddress","")' "$CLB_CFG") || true
    [ -n "${em:-}" ] || die "account identity UNREADABLE for CLB_CFG — unreadable is not a pass"
    say "ACCOUNT identity read (not printed: the infra-name gate)"

**That is a READABILITY check.** Any non-empty value passes, **including the wrong account** — and an
all-whitespace value passes too, since `[ -n "   " ]` is true.
⇒ ***THE COMMENT ABOVE IT NAMES THE RIGHT LAW AND THE CODE IMPLEMENTS ONLY ITS WEAKER HALF.*** It says
*"identity by the account the dir authenticates as, never by its name"*: **"never by its name" is satisfied;
"the account it authenticates as" is read and compared to nothing.** The log line *"ACCOUNT identity read"* is
accurate, which is exactly why a lead reads it as *verified*.
⛔ **This campaign has already had a correctly-named config dir authenticate as a different account with a
21-arm preflight passing it**, and a lane that MOVES between accounts meets the hazard at every move.

## What it refuses
| rc | condition |
|---|---|
| 2 | no `.claude.json`, or unparsable — *absent is not empty, and neither is a pass* |
| 3 | no readable identity (including all-whitespace — **the shape the `-n` test above PASSES**) |
| 4 | **no `--expect` supplied** — *a missing expectation is not a pass*, which would be this tool's own defect one level up |
| 5 | digest mismatch — **both digests named, neither account named** |
| 6 | `--credential`: no credential file, or expired with no refresh token (**the client exits 0 on an auth failure**, so this must be caught before the fire) |

## Two limits, stated where the verdict is
1. ⛔ **The expectation cannot be taken from the box.** A digest read off the dir and compared to itself blesses
   whatever is there. `--print-digest` says so **loudly, in its own output**, and exits without checking anything.
   **The expected digest is recorded once by a human who knows the intended account** — for this lane, on the
   Captain's word after he performs the login — and is mechanical thereafter.
2. ⛔ **§Q3.4 item 2 also requires "a trivial authenticated read checked by its BODY".** That costs a call and is
   **NOT performed here**; `--credential` checks only the credential file's offline shape, and **prints that limit
   beside its own green**, because a limit must ride where its verdicts ride.

## `live-drive.out`
The self-test on the run box, then `--print-digest` against both config dirs (they authenticate as **different**
accounts, which is expected: the lane has moved), the `rc 4` refusal, an `rc 5` mismatch, and the `--credential`
path.
⚠️ **The `--credential` arm passes `--expect` a digest taken from the box itself.** That proves the OK path's
**mechanism** and verifies **no identity at all** — it is labelled as such here rather than left to be misread,
which is the same defect this whole tool is about.
⚠️ **The drive also caught one in my own harness:** `python3 … | head -2; echo rc=$?` reported **rc 0** for a
command that truly exits **4**. The pipeline's status is `head`'s. Both drives are kept: the first reads the pipe,
the second reads the command, and the difference is visible in the file.
📌 Digests and config-dir names are replaced by role words here. **The real expected digest belongs in the
untracked lane env** (A1.5: the values that identify an account or a host are untracked), never in this tree.
