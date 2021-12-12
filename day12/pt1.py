# what i would do without defaultdict
from collections import defaultdict

small = []
adj = defaultdict(list)

for _ in range(25):
	u, v = input().split('-')
	adj[u].append(v)
	adj[v].append(u)
	small += [i for i in (u, v) if i.islower()]

ans = 0

# i originally did this day iteratively, but i redid it recursively cuz it's neater
def dfs(node, visited):
	if (node == "end"):
		global ans
		ans += 1
	
	# only care about small caves
	if (node in small):
		visited.add(node)
	elif (node in small and node in visited):
		return
	
	for u in adj[node]:
		if u not in visited:
			# ran into a bit of trouble with the .copy() thing
			dfs(u, visited.copy())

dfs("start", {"start"})
print(ans)