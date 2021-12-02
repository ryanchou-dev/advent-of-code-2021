depth = 0
hor = 0
aim = 0

for i in range(1000):
	s, e = map(str, input().split())
	if (s == "forward"):
		hor += int(e)
		depth += int(e) * aim
	elif (s == "down"):
		aim += int(e)
	else:
		aim -= int(e)

print(hor * depth)