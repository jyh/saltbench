import json, re, os, subprocess, random, sys, time, shutil
SC="/private/tmp/claude-501/-Users-jyh-projects-claude-saltbench/e8874a3b-1986-465f-94d6-7f406589d989/scratchpad"
exec(open(SC+"/classify.py").read().split('recs=[json.loads')[0])
V=os.path.expanduser("~/bench-src/verus-release/verus-arm64-macos/verus")
P="/Users/jyh/bench-src/verus-proof-synthesis/benchmarks/VeruSAGE-Bench/tasks.jsonl"
recs=[json.loads(l) for l in open(P)]
pop=[r for r in recs if r["project"] in ("AC","NR")]
surv=[]
for r in pop:
    items=find_fn_items(r["task"], r["target_function"])
    cands=[it for it in items if it["body"] is not None and "unimplemented!()" not in it["body"]]
    if len(cands)==1 and cands[0]["mode"]=="proof" and cands[0]["body"][1:-1].strip()=="":
        surv.append(r)
surv.sort(key=lambda r: r["task_id"])
random.seed(20260902)
sample=random.sample(surv, 15)
work=SC+"/gtwork"; shutil.rmtree(work, ignore_errors=True); os.makedirs(work)
out=[]
for i,r in enumerate(sample,1):
    open(work+"/task.rs","w").write(r["ground_truth"])
    t0=time.time()
    # perl alarm timeout, 600s (macOS has no timeout(1))
    p=subprocess.run(["perl","-e","alarm 600; exec @ARGV", V,"--crate-type=lib","--rlimit","250",
                      "--smt-option","smt.random_seed=0","task.rs"],
                     cwd=work, capture_output=True, text=True)
    dt=time.time()-t0
    line=[l for l in p.stdout.splitlines() if l.startswith("verification results::")]
    line=line[0] if line else "(no results line)"
    m=re.search(r'(\d+) verified, (\d+) errors', line)
    verdict = "PASS" if (p.returncode==0 and m and int(m.group(2))==0 and int(m.group(1))>=1) else "FAIL"
    rl = "RLIMIT" if "Resource limit (rlimit) exceeded" in p.stderr else ""
    out.append((r["task_id"], verdict, p.returncode, line, round(dt,1), rl, len(r["ground_truth"])))
    print(f"{i:2d}/15 {verdict:4s} rc={p.returncode} {dt:7.1f}s {rl:6s} {line:45s} {r['task_id'][:60]}", flush=True)
n=sum(1 for x in out if x[1]=="PASS")
print(f"\nGT PASS at today's release, rlimit 250, seed 0:  {n}/15 = {100*n/15:.0f}%")
json.dump(out, open(SC+"/gtpass_result.json","w"), indent=1)
