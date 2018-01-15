import readline

def move_n(point):
	return (point[0], point[1] - 1)
def move_s(point):
	return (point[0], point[1] + 1)
def move_nw(point):
	if point[0] % 2 == 0:
		return (point[0] - 1, point[1] - 1)
	else:
		return (point[0] - 1, point[1])
def move_ne(point):
	if point[0] % 2 == 0:
		return (point[0] + 1, point[1] - 1)
	else:
		return (point[0] + 1, point[1])
def move_sw(point):
	if point[0] % 2 == 0:
		return (point[0] - 1, point[1])
	else:
		return (point[0] - 1, point[1] + 1)
def move_se(point):
	if point[0] % 2 == 0:
		return (point[0] + 1, point[1])
	else:
		return (point[0] + 1, point[1] + 1)

input = input()
moves = input.split(',')
endPt = (0, 0)
max_steps = 0

for move in moves:
	if move == 'n':
		endPt = move_n(endPt)
	elif move == 's':
		endPt = move_s(endPt)
	elif move == 'nw':
		endPt = move_nw(endPt)
	elif move == 'ne':
		endPt = move_ne(endPt)
	elif move == 'sw':
		endPt = move_sw(endPt)
	elif move == 'se':
		endPt = move_se(endPt)

	max_steps = max(abs(endPt[0]), max_steps)

print(max_steps)	
