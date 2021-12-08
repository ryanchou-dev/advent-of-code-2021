# the problem statement was very weird

ans = 0
for i in range(200):
	line = input()
	_, out = line.split(" | ")
	out = out.split()
	for i in out:
		if len(i) in [2, 3, 4, 7]:
			ans += 1

print(ans)
