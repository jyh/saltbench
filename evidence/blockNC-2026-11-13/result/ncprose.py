    LIVE = ('⚠️ **EVERY LIVENESS FAILURE IS ONE CLAUSE TEST, `answer_is_the_count_honest_pair`, IN BOTH ARMS AND BOTH MODELS** (each failing '
            'cell: 0 regressions failed, 1 of 5 clause tests failed; the failing test named in each cell\'s B-suite output beside cells.tsv on '
            'the run box). The B suite\'s author (the lead) declared two readings of that card\'s count when building it (2026-11-09). Under '
            'NC §C6 item 4 a defect in a suite is a HARNESS finding, never an arm effect, so these failures are reported as they fell and the '
            'clause is put to a non-builder read; no arm reading rests on them.')
    if b == 'NCO':
        n1 = ('**Four condition-cells have no phase 2, all Opus LinearScan:** plain #3 and salt-diet #1–#3. Each source was a fresh phase 1 '
              '(block N\'s cells for those conditions were not eligible, `read_baselines.out`), and each ended CAP-COST at the fresh cap without landing. By §C2 they '
              'are REACH LOSSES: never re-run, never scored, never priced. So **Opus LinearScan salt-diet stands at n = 0** and plain at n = 2. '
              '**Two cells are scored at their WORKING TREE** (`clbfas02`, `clbfvs02`, both CAP-COST): their `solution.rs` was dirty at the cap, '
              'and score_claude_v3\'s rule reads the working tree. Their passes are floors.')
        n3 = ('⚠️ **Opus caps often in BOTH arms** (the CAP-COST counts above); a median at the cap is censored, and its ratio prints `>=`. '
              'The sign is the reading; the magnitudes are not, and the figures include the harness\'s own sandbox probe.')
        n4 = ('- **(ii) is a MISS for Opus:** in BinomialHeap and MaxFlow plain capped more often than salt-diet. LinearScan has no salt-diet '
              'phase-2 cell, so it gives no comparison. A miss is a result, reported as it fell.')
    else:
        n1 = ('**Five condition-cells have no phase 2.** Sonnet LinearScan salt-diet #1–#3: #1\'s fresh source LANDED but its G baseline read '
              '6 of 9 (REACH-LOSS-G: the code changed what the program computes), #2 and #3 ended CAP-COST. Sonnet MaxFlow salt-diet #2 and #3: '
              'both fresh sources ended CAP-COST. So **Sonnet LinearScan salt-diet stands at n = 0 and Sonnet MaxFlow salt-diet at n = 1**. '
              '**One cell ended EXIT-FORCED:** `clblvp03` (Liveness plain #3), the declared harness fault (the box reader under the C locale, '
              'fixed in the drivers on 11-15); its suite reads at HEAD. **Two cells are scored at their WORKING TREE** (`clblvs01`, `clblvs02`, '
              'both CAP-COST); their passes are floors.')
        n3 = ('⚠️ **Sonnet MaxFlow salt-diet is n = 1** (two reach losses), and that one cell (`clblxs01`) capped and fails 3 of 5 clause '
              'tests. The sign is the reading; the magnitudes are not, and the figures include the harness\'s own sandbox probe.')
        n4 = ('- **(ii) holds for Sonnet:** salt-diet capped strictly more often in Liveness and MaxFlow, and tied in three problems. '
              'LinearScan gives no comparison (no salt-diet phase-2 cell).')
    n1 = n1 + '\n' + LIVE
