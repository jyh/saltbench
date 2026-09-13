import re

with open("ScratchX.lean", "r") as f:
    scratch_lines = f.readlines()

with open("Salt/HB/Lemma10Seal.lean", "r") as f:
    seal_lines = f.readlines()

start_idx = 0
for i, line in enumerate(scratch_lines):
    if line.startswith("private lemma"):
        start_idx = i
        break

extracted = scratch_lines[start_idx:]

end_idx = len(seal_lines) - 1
while end_idx >= 0 and not seal_lines[end_idx].startswith("end Salt.N7"):
    end_idx -= 1

new_seal_lines = seal_lines[:end_idx] + ["\n"] + extracted + ["\n"] + seal_lines[end_idx:]

with open("Salt/HB/Lemma10Seal.lean", "w") as f:
    f.writelines(new_seal_lines)
