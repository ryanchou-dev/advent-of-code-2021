# much less code than yesterday, 
# got a worse score :'(

inp = []
for i in range(94):
	inp.append(input())

switch = {'}': '{', ')': '(', ']': '[', '>': '<'}

tot = 0

for i in inp:
	needtoclose = []
	
	for j in i:
		if j in switch.keys() and needtoclose[-1] == switch[j]:
			needtoclose.pop()
		elif j in switch.keys() and needtoclose[-1] != switch[j]:
			if j == ')':
				tot += 3
			elif j == ']':
				tot += 57
			elif j == '}':
				tot += 1197
			else:
				tot += 25137
			break
		else:
			needtoclose.append(j)
	
print(tot)