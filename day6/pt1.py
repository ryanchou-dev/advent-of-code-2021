# brute forced pt1
fishy = [int(i) for i in input().split(',')]

for j in range(80):
	for i in range(len(fishy)):
		fishy[i] -= 1
		if (fishy[i] == -1):
			fishy[i] = 6
			fishy.append(8)
	
print(len(fishy))
