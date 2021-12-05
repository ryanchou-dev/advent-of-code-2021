a = []
for i in range(2000):
	a.append(int(input()))

prev = a[0]
ans = 0

for i in a[1:]:
	if i > prev:
		ans += 1
	
	prev = i

print(ans)