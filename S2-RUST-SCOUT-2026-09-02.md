# S2-RUST SCOUT — 2026-09-02 (bench seat). READ-ONLY. **ZERO MODEL TOKENS.**

**Standing work under the Captain's 09/01 14:1x word** ("at the CEILING: report, then default-if-silent the
§9.5 S2-Rust READ-ONLY scout"), i.e. amendment 11 §9 item 5: at the ceiling the fallback is **not a larger
`k`** but the commission's **PRIMARY treatment substrate, S2-Rust, on which there is still zero record.**

This does **not** re-do `S2-SOURCE-READ-2026-08-29.md`. It closes items that read left open by name, and it
**corrects two numbers that read got wrong** — in both cases *against* the benchmark, and in both cases from
the same cause.

---

## §1 · ⛔⛔ TWO OPEN COUNTS CLOSED — AND THE BENCHMARKS WERE RIGHT BOTH TIMES; **WE** WERE WRONG

The 08/29 read flagged, as open item (e): *"the two unaccounted Multilingual Rust instances (41 verified vs 43
stated) and the 238-vs-239 Multi-SWE-bench image/instance drift must be resolved from downloaded files."*
Both are now resolved **from primary data**, and both resolve in the benchmark's favour.

### 1a. SWE-bench Multilingual Rust = **43**, exactly as the dataset card says

`datasets-server /statistics` (the `/filter` endpoint still returns **HTTP 500**, four days on):

| repo | n |
|---|---|
| tokio-rs/tokio | 9 |
| tokio-rs/axum | **7** |
| astral-sh/ruff | 7 |
| sharkdp/bat | 8 |
| uutils/coreutils | 5 |
| nushell/nushell | 5 |
| burntsushi/ripgrep | 2 |
| **total** | **43** |

⇒ **The card's "Rust | 43" is CORRECT.** The 08/29 read's 41 was short by exactly the two it enumerated wrong:
it listed **axum as 5** (`682, 1119, 1730, 1934, 2096`) when axum is **7**. Split total: 300 examples, 41 repos.

### 1b. Multi-SWE-bench Rust = **239 PR images + 10 base = 249 tags**, matching paper Table 1 **repo by repo**

Counted **by exact image key** from `scripts/images_verified.txt` (1,679 lines, downloaded and counted
locally — not summarised):

| image | base | pr- | paper Table 1 #Num |
|---|---|---|---|
| `burntsushi_m_ripgrep` | 1 | 14 | 14 ✓ |
| `clap-rs_m_clap` | 1 | **132** | 132 ✓ |
| `nushell_m_nushell` | 1 | 14 | 14 ✓ |
| `rayon-rs_m_rayon` | 1 | 2 | 2 ✓ |
| `serde-rs_m_serde` | 1 | 2 | 2 ✓ |
| `sharkdp_m_bat` | 1 | 10 | 10 ✓ |
| `sharkdp_m_fd` | 1 | 14 | 14 ✓ |
| `tokio-rs_m_bytes` | 1 | 5 | 5 ✓ |
| `tokio-rs_m_tokio` | 1 | **25** | 25 ✓ |
| `tokio-rs_m_tracing` | 1 | 21 | 21 ✓ |
| **total** | **10** | **239** | **239 ✓** |

⇒ **Zero drift. Every repo matches exactly.** The 08/29 read reported `clap 137` and `tokio 22` and concluded
a "near-reconciled" 238-vs-239 discrepancy with "per-repo drift". **There is no drift. Both of its outlier
numbers were artefacts of its own counting method.**

### 1c. ⭐ THE CAUSE IS ONE THING, AND IT IS THE FAMILY THIS SEAT HAS BEEN FINDING ALL WEEK

Both errors came from **matching a SUBSTRING where an EXACT KEY was needed**, in a namespace where names
nest:
- **`tokio` is both an ORG and a REPO.** `grep tokio` over the image list returns **54** lines —
  `tokio-rs_m_tokio` **plus** `tokio-rs_m_bytes` **plus** `tokio-rs_m_tracing`. Counting `tokio` counts three
  repos.
- **`clap` matches `clap-rs_m_clap` AND the five per-PR override recipes** (`clap_2814_to_755.py` etc.),
  inflating 132 → 137.

⛔ **AND A TRAP FOR ANY TOOLING THE SCOUT BUILDS, FOUND HERE:** the harness's **recipe folders use
UNDERSCORES** (`multi_swe_bench/harness/repos/rust/clap_rs/`) while the **published image names use HYPHENS**
(`mswebench/clap-rs_m_clap`). My first exact-key tally returned **0** for six of the ten repos for precisely
this reason. ⇒ ***never derive an image name from a folder name in this benchmark.***

⇒ 🔑 **THE LAW, and it is the seventh instance of one shape this seat has met in five days:
AN INSTRUMENT THAT MATCHES A PROXY (a substring) FOR AN EXACT KEY KEEPS RETURNING A NUMBER, AND THE NUMBER IS
WRONG IN THE DIRECTION OF WHATEVER ELSE SHARES THE PREFIX.** `ship BC` on a DONE line · `c_dead` on
elaboration · the controls gate on a boolean · the F3 headline at a stage-C root · the Seatbelt fence on a
path · `STATEMENT_ALTERED` on a delimiter · **and now a benchmark census on a substring.**
📌 **And the correction runs the other way this time:** every previous member had us *trusting* a green light.
Here we **disbelieved a benchmark's own published count** on the strength of our own miscount. *A proxy
instrument does not only manufacture false confidence — it manufactures false suspicion, and the second is
harder to notice because it feels like rigour.*

## §2 · PINS ESTABLISHED (08/29 open item (b): *"neither brief nor sources give a commit hash… pin the harness
by git SHA and the datasets by HF revision SHA"*)

| artefact | pin | as of |
|---|---|---|
| SWE-bench harness | `08c82f46f3bec35596613fe88042e5a49128500f` | **2026-09-01T20:17:09Z** |
| Multi-SWE-bench harness | `24f493f8a103e72312ded4f6b9c89f081d69cb09` | 2025-12-18T06:27:09Z |
| `SWE-bench/SWE-bench_Multilingual` (HF) | `846e647b9f33c0b51b739d005d13d85493c9af09` | 2026-08-17T00:45:10Z |

⚠️ **THE SWE-BENCH HARNESS MOVED YESTERDAY** — 172 modifications, committed **2026-09-01**, the same day this
campaign was reading its layout. The 08/29 read's note that `swebench/harness/` has "no `test_spec/` or
`docker_build.py` at those paths" is a statement about a **tree that has since changed**, and must be re-read
at the pin, not inherited. Multi-SWE-bench by contrast has been **dormant ~8.5 months**.
⇒ *the two candidate harnesses have opposite staleness risks, and a scout that pins only one of them is
exposed on the other.*

## §3 · WHAT REMAINS OPEN, HONESTLY (unchanged or only partly advanced from 08/29)

Not touched by this pass, and still required before any S2-Rust design can be frozen:
- **(a) Rust toolchain pins.** Still unread — `/filter` 500s block reading `eval_script` for a Multilingual
  row, and Multi-SWE-bench recipes say `FROM rust:latest`, so the **only** pin is the Docker Hub image digest,
  which must be recorded at snapshot time. **A benchmark whose recipe is unpinned is pinned by its registry,
  and a registry tag is a moving target with a name that looks fixed.**
- **(c) Feasibility on the Studio.** Both harnesses are Docker-in-Linux, `linux/amd64`, no native-macOS path.
  Rosetta emulation is verified working on the Studio for `linux/amd64`, but **no Rust image has been pulled or
  run here** and disk cost is unmeasured. Rust-SWE-bench needs a 120 GB local build and is separately blocked
  on **(g) licence absent**.
- **(d) Arm content is undesigned** — whether `hints_text` (often quoting the fix) and `FAIL_TO_PASS` test
  names (which leak the fix's shape) are withheld is the single largest design question, and **no grader for a
  salt arm exists in either harness.**
- **(f) Contamination is unquantified**; no post-cutoff Rust pool exists in any of these sets.
- **(h)** whether Multilingual's 2026-08 `:latest` re-push changed image contents vs `v1`.

## §4 · WHAT THIS SCOUT DOES **NOT** DO

It does not choose a substrate, propose a design, or price a run. **No amendment follows from it** — it is a
source read, and the commission's order is *source read first*. Its whole product is: **two open counts
closed, three pins established, one live staleness risk named, and one method error corrected in our own
record.** The two Rust pools remain **~4× apart in difficulty** (Multilingual Rust is Claude 3.7 Sonnet's
*easiest* language at 58.14 %; Multi-SWE-bench Rust best is 15.90 %) and are **not interchangeable** — a fact
from the 08/29 read that this pass re-confirms as the most consequential thing known about S2-Rust.
