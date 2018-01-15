def index_in_bounds(x, y, size):
	return (x >= 0 and y >= 0 and x < size and y < size)

def sum_neighbors(grid, x, y):
	size = len(grid)
	n =  grid[y - 1][x] if index_in_bounds(x, y - 1, size) else 0
	s = grid[y + 1][x] if index_in_bounds(x, y + 1, size)  else 0
	e = grid[y][x + 1] if index_in_bounds(x + 1, y, size) else 0
	w = grid[y][x - 1] if index_in_bounds(x - 1, y, size) else 0
	ne = grid[y - 1][x + 1] if index_in_bounds(x + 1, y - 1, size) else 0
	nw = grid[y - 1][x - 1] if index_in_bounds(x - 1, y - 1, size) else 0
	se = grid[y + 1][x + 1] if index_in_bounds(x + 1, y + 1, size) else 0
	sw =  grid[y + 1][x - 1] if index_in_bounds(x - 1, y + 1, size) else 0
	return n + s + e + w + ne + nw + se + sw

# Puzzle input
input = 289326

# Calculate dimensions of the grid
row_count = 0
sqrIndex = 2
while pow(sqrIndex, 2) < input:
	if sqrIndex % 2 == 1:
		row_count += 1
	sqrIndex += 1

if pow((sqrIndex - 1), 2) < input and pow(sqrIndex, 2) >= input:
	row_count += 1

# Dimension for the grid
s = row_count * 2 + 1

# Make the grid
grid = [[0 for x in range(s)] for y in range(s)] 

# Start filling the grid
centerX = int((s - 1) / 2)
centerY = int((s - 1) / 2)
grid[centerY][centerX] = 1
ptX = centerX + 1
ptY = centerY

r = 1 				# distance/radius from center
numPlacedInRing = 0 # counter for values in ring
xMin = centerX  - r
xMax = centerX + r
yMin = centerY - r
yMax = centerY + r

dir = 0 # direction

while True:
	grid[ptY][ptX] = sum_neighbors(grid, ptX, ptY)
	
	# Puzzle answer is first value larger than input
	if grid[ptY][ptX] > input:
		print("Answer:", grid[ptY][ptX])
		break

	numPlacedInRing += 1

	# Number of values in ring 'r' distance from center is 8 * r
	if numPlacedInRing == 8*r:
		numPlacedInRing = 0
		r += 1
		xMin = centerX - r
		xMax = centerX + r
		yMin = centerY - r
		yMax = centerY + r
	
	# Update indicies based on direction and bounds
	if (dir == 0) and (ptX < xMax):
		ptX += 1
	elif (dir == 1) and (ptY > yMin):
		ptY -= 1
	elif (dir == 2) and (ptX > xMin):
		ptX -= 1
	elif (dir == 3) and (ptY < yMax):
		ptY += 1
	else:
		dir = (dir + 1) % 4
		if dir == 0:
			ptX += 1
		elif dir == 1:
			ptY -= 1
		elif dir == 2:
			ptX -= 1
		elif dir == 3:
			ptY += 1
