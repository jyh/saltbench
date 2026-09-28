"""The agy /usage rows block NA logged (§H8), cut from the seat's QUOTA-LOG.tsv: every AGY-USAGE(gemini) row whose source names a
cells-na-* root. Kept: stamp · pool · 5-hour used % · weekly used % · the reset line as printed · the root. The account column is
NOT carried (it names an account by role, which a public tree does not need).   usage: python3 usage_rows.py <QUOTA-LOG.tsv>"""
import re, sys
print('\t'.join(['stamp', 'pool', 'used_5h_pct', 'used_weekly_pct', 'resets', 'root']))
for l in open(sys.argv[1]):
    c = l.rstrip('\n').split('\t')
    if len(c) >= 10 and c[8] == 'AGY-USAGE(gemini)':
        m = re.search(r'usage-at-dispatch\.txt of (cells-na-\S+)', c[9])
        if m:
            print('\t'.join([c[0], c[1], c[2], c[3], c[7], m.group(1)]))
