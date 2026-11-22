import sys, re
def blocks(t):
    out = {}
    for m in re.finditer(r'(?:pub )?(?:open |closed )?spec fn ([a-z_0-9]+)', t):
        i = m.start(); depth = 0; j = t.index('{', i)
        k = j
        while True:
            if t[k] == '{': depth += 1
            elif t[k] == '}':
                depth -= 1
                if depth == 0: break
            k += 1
        out[m.group(1)] = ' '.join(t[i:k+1].split())
    return out
a = blocks(open(sys.argv[1]).read()); b = blocks(open(sys.argv[2]).read())
same = [n for n in a if n in b and a[n] == b[n]]; diff = [n for n in a if n in b and a[n] != b[n]]
print(f"provided spec fns {len(a)} · defined in solution {sum(1 for n in a if n in b)} · identical (whitespace-normalised) {len(same)} · DIFFERENT {len(diff)}")
for n in diff: print("  DIFF", n, "| provided:", a[n][:110], "| solution:", b[n][:110])
