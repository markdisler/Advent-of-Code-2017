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

# Start traversing the "grid"
centerX = int((s - 1) / 2)
centerY = int((s - 1) / 2)
ptX = centerX + 1
ptY = centerY

r = 1 				# distance/radius from center
numPlacedInRing = 0 # counter for values in ring
xMin = centerX  - r
xMax = centerX + r
yMin = centerY - r
yMax = centerY + r

dir = 0 # direction

for i in range(2, input + 1):

	numPlacedInRing += 1
	print(i, "placed at", ptX, ", ", ptY)

	# Number of values in ring 'r' distance from center is 8 * r
	if numPlacedInRing == 8*r:
		numPlacedInRing = 0
		r += 1
		xMin = centerX - r
		xMax = centerX + r
		yMin = centerY - r
		yMax = centerY + r

	if (i == input): # answer found
		break		 # exit here so ptX & ptY aren't changed

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

deltaX = abs(ptX - centerX)
deltaY = abs(ptY - centerY)
print("Distance:", (deltaX + deltaY))