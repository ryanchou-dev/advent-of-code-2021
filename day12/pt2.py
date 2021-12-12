# with the amount of bugs i got on this problem, 
# im surprised i still got 441
from collections import defaultdict

small = []
adj = defaultdict(list)

for _ in range(25):
	u, v = input().split('-')
	adj[u].append(v)
	adj[v].append(u)
	small += [i for i in (u, v) if i.islower() and i != "start"]

ans = 0

def dfs(node, visited, twiced):
	if (node == "end"):
		return 1

	if (node in small):
		visited.append(node)

	ans = 0
	for u in adj[node]:
		if u not in visited and u != "start":
			ans += dfs(u, visited.copy(), twiced)
		elif not twiced and u in visited and u != "start":
			ans += dfs(u, visited.copy(), True)

	return ans

print(dfs("start", ["start"], False))