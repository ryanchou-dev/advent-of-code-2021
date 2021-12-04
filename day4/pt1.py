import sys

start = [int(i) for i in input().split(',')]
board = []
input()

for i in range(99):
	b1 = []
	for j in range(5):
		b1.append(list(map(int, input().split())))
	board.append(b1)
	input()

def win(b1):
	for col in range(5):
		cnt = 0
		for i in range(5):
			if b1[i][col] == -1: 
				cnt += 1

		if (cnt == 5):
			return True
	
	for i in range(5):
		cnt = 0
		for j in range(5):
			if (b1[i][j] == -1):
				cnt += 1
		if (cnt == 5):
			return True


for i in start:
	for l in range(99):
		b1 = board[l]
		for j in range(5):
			for k in range(5):
				if b1[j][k] == i:
					b1[j][k] = -1
	
	for l in range(99):
		b1 = board[l]
		if win(b1):
			sume = 0
			for p in range(5):
				for m in range(5):
					if (b1[p][m] != - 1):
						sume += b1[p][m]

			sume *= i
			print(sume)
			sys.exit()

