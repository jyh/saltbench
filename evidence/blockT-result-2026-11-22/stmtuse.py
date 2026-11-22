import sys, re
sec = open(sys.argv[1]).read(); src = open(sys.argv[2]).read()
names = sorted(set(re.findall(r'spec fn ([a-z_0-9]+)', sec)))
named = [n for n in names if re.search(r'\b' + re.escape(n) + r'\b', src)]
print(f"spec fns named {len(named)}/{len(names)}")
# control: a name that cannot be present must read 0
# positive control: the interface function every solution must define (from the section's own exec fn signatures)
iface = re.findall(r'\bfn ([a-z_0-9]+)', open(sys.argv[3]).read()) if len(sys.argv) > 3 else re.findall(r'pub fn ([a-z_0-9]+)', sec)
iface = [n for n in iface if n != 'main']
print("control absent-name hits:", len(re.findall(r'\bzz_not_a_spec_fn\b', src)), "· control interface fns present:", sum(1 for n in iface if re.search(r'\b' + n + r'\b', src)), "/", len(iface))
d = [l.rstrip() for l in sec.splitlines() if l.strip()]; s = set(l.rstrip() for l in src.splitlines())
print(f"section lines verbatim {sum(1 for l in d if l in s)}/{len(d)}")
print("named:", ", ".join(named)); print("not named:", ", ".join(n for n in names if n not in named))
