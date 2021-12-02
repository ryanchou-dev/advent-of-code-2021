depth = 0
forwards = 0

for i in range(1000):
	s, e = map(str, input().split())
	if (s == "forward"):
		forwards += int(e)
	elif (s == "down"):
		depth += int(e)
	else:
		depth -= int(e)

print(forwards * depth)