a = []
for i in range(2000):
	a.append(int(input()))

w = 0

for i in range(3):
	w += a[i]

ans = 0
prev = 10000000

for i in range(1997):
	if (w > prev):
		ans += 1
	
	prev = w
	w -= a[i]
	w += a[i + 3]

if (w > prev):
	ans += 1

print(ans)

