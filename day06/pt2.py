# maps ftw
fishy = {}
for i in range(0, 9):
	fishy[i] = 0

for i in input().split(','):
	fishy[int(i)] += 1

for _ in range(256):
	prev = fishy[0]

	fishy[0] = fishy[1]
	fishy[1] = fishy[2]
	fishy[2] = fishy[3]
	fishy[3] = fishy[4]
	fishy[4] = fishy[5]
	fishy[5] = fishy[6]
	fishy[6] = fishy[7] + prev
	fishy[7] = fishy[8]
	fishy[8] = prev

print(sum(fishy.values()))