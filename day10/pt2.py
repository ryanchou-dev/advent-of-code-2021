# thank the cow gods for this func
from statistics import median

inp = []
switch = {'{': '}', '(': ')', '[':']', '<':'>'}
switch2 = {v: u for u, v in switch.items()}

for i in range(94):
	inp.append(input())

ans = []

for i in inp:
	needtoclose = []
	flag = True
	cur = 0

	for j in i:
		if j in switch2.keys():
			if (needtoclose[-1] == switch2[j]):
				needtoclose.pop()
			else:
				flag = False
		else:
			needtoclose.append(j)
	
	if (flag):
		needtoclose.reverse()
		
		for j in needtoclose:
			cur *= 5
			if (switch[j] == ')'):
				cur += 1
			elif (switch[j] == ']'):
				cur += 2
			elif (switch[j] == '}'):
				cur += 3
			elif (switch[j] == '>'):
				cur += 4
	
		ans.append(cur)

print(median(ans))