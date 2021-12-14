# counters are very cool
from collections import Counter

poly = input()
input()

subs = {}

for i in range(100):
	a, b = input().split(' -> ')
	subs[a] = b

# count pairs
g = Counter()

for i in range(len(poly) - 1):
	g[poly[i] + poly[i + 1]] += 1

for _ in range(40):
	nxt = Counter()

	for group, occ in g.items():
		l = group[0]
		r = group[1]
		sub = subs[group]
		
		nxt[l + sub] += occ
		nxt[sub + r] += occ

	g = nxt

ans = {}
for group, occ in g.items():
	if group[0] not in ans:
		ans[group[0]] = occ
	else:
		ans[group[0]] += occ

j = list(ans.values())
j.sort()

print(j[-1] - j[0] - 1)