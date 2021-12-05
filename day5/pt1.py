# i messed up on this problem so bad...

mx = -1
my = -1

exists = [[0 for _ in range(1000)] for _ in range(1000)]

for i in range(500):
	# thank the programming gods for python's string parsing
	e = input().split()
	e.pop(1)
	
	x, y = map(int, e[0].split(','))
	x1, y1 = map(int, e[1].split(','))

	if x == x1:
		if y1 > y:
			for j in range(y, y1 + 1):
				exists[x][j] += 1
		else:
			for j in range(y, y1 - 1, -1):
				exists[x][j] += 1

	elif y == y1:
		if x1 > x:
			for j in range(x, x1 + 1):
				exists[j][y] += 1
		else:
			for j in range(x, x1 - 1, -1):
				exists[j][y] += 1


ans = 0

for i in range(1000):
	for j in range(1000):
		if exists[i][j] > 1:
			ans += 1

print(ans)