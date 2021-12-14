# brute force pt1
poly = input()
input()

subs = {}
for i in range(100):
	a, b = input().split(' -> ')
	subs[a] = b

def switch(nxt):
	new = ""
	for i in range(len(nxt) - 1):
		key = nxt[i] + nxt[i + 1]

		if key in subs:
			new += nxt[i]
			new += subs[key]
		else:
			new += nxt[i]

	new += nxt[-1]
	return new

for j in range(10): 
	poly = switch(poly)

occ = {}

for j in poly:
	if j in occ:
		occ[j] += 1
	else:
		occ[j] = 1

j = list(occ.values())
j.sort()
print(j[-1] - j[0])