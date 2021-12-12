# standard dfs problem today

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

e = []
for i in range(5):
	e.append(input())

ans = 0
for i in range(5):
	for j in range(10):
		works = True
		for k in range(4):
			x = i + dx[k]
			y = j + dy[k]

			if x < 0 or x >= 5 or y < 0 or y >= 10:
				continue

			if int(e[x][y]) <= int(e[i][j]):
				works = False
				break

		if (works):
			ans += int(e[i][j]) + 1

print(ans)


