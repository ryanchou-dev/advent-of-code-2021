# 7! is brute forceable 

import itertools

digits = {
	"acedgfb": 8,
	"cdfbe": 5,
	"gcdfa": 2,
	"fbcad": 3,
	"dab": 7,
	"cefabd": 9,
	"cdfgeb": 6,
	"eafb": 4,
	"cagedb": 0,
	"ab": 1
}

digits = {"".join(sorted(i)): digits[i] for i in digits}

ans = 0

for _ in range(200):
	sp, out = input().split(" | ")
	sp = sp.split(" ")
	out = out.split(" ")

	res = ""

	possible = [i for i in itertools.permutations("abcdefg")]

	for j in possible:
		a = {}
		
		for i in range(len("abcdefg")):
			a[j[i]] = "abcdefg"[i]
		
		sps = ["".join(a[d] for d in c) for c in sp]
		o = ["".join(a[d] for d in c) for c in out]
		
		flag = True

		for s in sps:
			if "".join(sorted(s)) not in digits:
				flag = False
		
		if (flag):
			output = ["".join(sorted(t)) for t in o]
			ans += int("".join(str(digits[t]) for t in output))
			break

print(ans)