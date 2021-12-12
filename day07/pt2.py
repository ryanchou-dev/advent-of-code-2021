# optimal position is mean
crabs = [int(i) for i in input().split(',')]

trav = sum(crabs) // len(crabs)
ans = 0

for i in crabs:
	dist = abs(i - trav)
	ans += dist * (dist + 1) // 2
print(ans)