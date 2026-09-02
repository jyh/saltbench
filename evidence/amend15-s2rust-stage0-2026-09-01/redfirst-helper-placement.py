"""RED-FIRST PROOF for the helper-placement repair. Amendment 14's law: a gate must fail on the BROKEN
version EVERY time — reproducing a defect is not gating it. Runs the guard arm 3x under each placement."""
import json, subprocess, sys, tempfile, os
sys.path.insert(0,'/Users/jyh/projects/claude/saltbench/harness/s2rust')
import build_views_verus as B
L=os.path.expanduser("~/bench-src/verus-proof-synthesis/utils/lynette/source/target/release/lynette")
T='NR__impl_u__l1__impl2__lemma_empty_implies_interp_empty'
fz=json.load(open('vout2/views/%s/frozen.json'%T)); gt=json.load(open('vout2/gt/%s.json'%T))
HELPER="pub proof fn h_ok(n: nat)\n  ensures n >= 0\n{ }"
orig=B.assemble(fz,{},pristine=True)
def canon(placement):
    if placement=="FIXED":   # end of the verus! block (shipped)
        return B.assemble(fz,{"proof":gt["proof"],"helpers":HELPER})
    # BROKEN: the design's original placement — top level immediately before the enclosing item
    return (fz["prefix"] + "\n"+HELPER+"\n" + fz["enclosing_head"] + "\n"+gt["proof"]+"\n"
            + fz["suffix_head"] + fz["suffix_tail"])
for placement in ("BROKEN","FIXED"):
    verdicts=[]
    for _ in range(3):
        with tempfile.TemporaryDirectory() as d:
            o=os.path.join(d,"o.rs"); c=os.path.join(d,"c.rs")
            open(o,"w").write(orig); open(c,"w").write(canon(placement))
            p=subprocess.run([L,"additions",o,c],capture_output=True,text=True)
            verdicts.append("REFUSED" if p.returncode!=0 else "accepted")
    print(f"  helpers placement {placement:6s} -> lynette {verdicts}")
