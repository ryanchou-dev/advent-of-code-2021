bits = []
for i in range(1000):
	bits.append(input())

left = bits.copy()

for col in range(12):
	if (len(left) > 1):
		cnt1, cnt2 = 0, 0

		for i in left:
			if i[col] == "1":
				cnt1 += 1
			else:
				cnt2 += 1

		if cnt1 >= cnt2:
			left = [i for i in left if i[col] == "1"]
		else:
			left = [i for i in left if i[col] == "0"]
	
print(left[0])

left = bits.copy()

for col in range(12):
	if len(left) > 1:
		cnt1, cnt2 = 0, 0
		for i in left:
			if i[col] == "1":
				cnt1 += 1
			else:
				cnt2 += 1

		if cnt1 >= cnt2:
			left = [i for i in left if i[col] == "0"]
		else:
			left = [i for i in left if i[col] == "1"]
	
print(left[0])