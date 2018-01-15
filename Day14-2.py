day10 = __import__('Day10-2')

class Square:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.used = False
		self.north = None
		self.south = None
		self.west = None
		self.east = None
		self.visited = False
		self.region = -1

puzzle_input = 'ugkiagan'
grid = [[Square(x, y) for x in range(128)] for y in range(128)]
for i in range(128):
	knot_hash = day10.get_knot_hash(puzzle_input + '-' + str(i))
	as_bin = bin(int(knot_hash, 16))[2:]
	num_pad = 128 - len(as_bin)
	as_bin = ('0' * num_pad) + as_bin
	print(as_bin)
	for x in range(len(as_bin)):
		if int(as_bin[x]) == 1:
			grid[i][x].used = True

def in_bounds(point):
	return point[0] >= 0 and point[1] >= 0 and point[0] < 128 and point[1] < 128

for y in range(128):
	for x in range(128):
		grid[y][x].north = grid[y - 1][x] if in_bounds((x, y - 1)) else None
		grid[y][x].south = grid[y + 1][x] if in_bounds((x, y + 1)) else None
		grid[y][x].west = grid[y][x - 1] if in_bounds((x - 1, y)) else None
		grid[y][x].east = grid[y][x + 1] if in_bounds((x + 1, y)) else None

def unvisited_used_square():
	for y in range(128):
		for x in range(128):
			if grid[y][x].used and not grid[y][x].visited:
				return (x, y)
		
num_regions = 1
node_point = unvisited_used_square()
while node_point != None:
	stack = []
	stack.append(grid[node_point[1]][node_point[0]])

	while len(stack) > 0:
		node = stack.pop()
		if not node.visited:
			node.visited = True
			node.region = num_regions
			for neighbor in [node.north, node.south, node.east, node.west]:
				if neighbor != None and not neighbor.visited and neighbor.used:
					stack.append(neighbor)


	num_regions += 1
	node_point = unvisited_used_square()
num_regions -= 1
print(num_regions)