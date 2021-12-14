# any problem with coordinate points, im bad at

points = set()

for i in range(722):
	x, y = map(int, input().split(','))
	points.add((x, y))
	
input()

fold = int(input().split('=')[1])

after_fold = set()

# x-fold
for coord in points:
	if coord[0] > fold:
		after_fold.add((2 * fold - coord[0], coord[1]))
	else:
		after_fold.add((coord[0], coord[1]))

print(len(after_fold))