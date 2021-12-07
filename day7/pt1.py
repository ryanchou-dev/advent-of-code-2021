# optimal position is median
# pretty easy day, but i was still slow :')
# gj sans for ranking in the global leaderboard!!
crabs = [int(i) for i in input().split(',')]

crabs.sort()
trav = crabs[len(crabs) // 2]

ans = 0
for i in crabs:
	ans += abs(i - trav)
print(ans)