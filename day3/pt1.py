bits = []
for i in range(1000):
	bits.append(input())

bit1 = ""
for col in range(12):
	cnt1, cnt0 = 0, 0

	for i in range(1000):
		if (bits[i][col] == "1"):
			cnt1 += 1
		else:
			cnt0 += 1

	if (cnt1 > cnt0):
		bit1 += "1"
	else:
		bit1 += "0"

print(bit1)

bit2 = ""
for col in range(12):
	cnt1, cnt0 = 0, 0

	for i in range(1000):
		if (bits[i][col] == "1"):
			cnt1 += 1
		else:
			cnt0 += 1

	if (cnt1 < cnt0):
		bit2 += "1"
	else:
		bit2 += "0"

print(bit2)

# i manually converted the two bits in an online converter ^^