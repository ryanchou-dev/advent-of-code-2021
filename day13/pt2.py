points = set()

for i in range(722):
	x, y = map(int, input().split(','))
	points.add((x, y))

input()

def x(pos, rem):
	nxt = set()
	for coord in rem:
		if coord[0] > pos:
			nxt.add((2 * pos - coord[0], coord[1]))
		else:
			nxt.add((coord[0], coord[1]))
	return nxt

def y(pos, rem):
	nxt = set()
	for coord in rem:
		if coord[1] > pos:
			nxt.add((coord[0], 2 * pos - coord[1]))
		else:
			nxt.add((coord[0], coord[1]))
	return nxt

for instruct in range(12):
	line = input().split("=")
	direct, sep = line[0][-1], int(line[1])

	if (direct == "x"):
		points = x(sep, points)
	else:
		points = y(sep, points)

points = list(points)


xc = [i[0] for i in points]
yc = [i[1] for i in points]
xc.sort()
yc.sort()

for y in range(yc[0], yc[-1] + 1):
	for x in range(xc[0], xc[-1] + 1):
		if ((x, y) in points):
			print("#", end="")
		else:
			print(" ", end="")
	print()