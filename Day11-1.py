import readline
from queue import Queue

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

def in_bounds(point, width, height):
	return point[0] >= 0 and point[1] >= 0 and point[0] < width and point[1] < height

class Node:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.n = None
		self.s = None
		self.nw = None
		self.ne = None
		self.sw = None
		self.se = None
		self.visited = False

class Vertex:
	def __init__(self, node, path_len):
		self.node = node
		self.path_len = path_len

input = input()

moves = input.split(',')
minPt = (0, 0)
maxPt = (0, 0)
endPt = (0, 0)

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

	minPt = (min(minPt[0], endPt[0]), min(minPt[1], endPt[1]))
	maxPt = (max(maxPt[0], endPt[0]), max(maxPt[1], endPt[1]))

# Normalize
x_origin = abs(minPt[0])
y_origin = abs(minPt[1])

altered_y = y_origin
if x_origin % 2 == 1:
	altered_y += 1

normalizedMaxPt = (maxPt[0] + x_origin, maxPt[1] + altered_y)
normalizedEndPt = (endPt[0] + x_origin, endPt[1] + altered_y)

# Make the grid
grid_w = normalizedMaxPt[0] + 1
grid_h = normalizedMaxPt[1] + 1
grid = [[Node(x, y) for x in range(grid_w)] for y in range(grid_h)] 

for y in range(0, normalizedMaxPt[1] + 1):
	for x in range(0, normalizedMaxPt[0] + 1):
		n_pt = move_n((x, y))
		s_pt = move_s((x, y))
		nw_pt = move_nw((x, y))
		ne_pt = move_ne((x, y))
		sw_pt = move_sw((x, y))
		se_pt = move_se((x, y))

		grid[y][x].n = grid[n_pt[1]][n_pt[0]] if in_bounds(n_pt, grid_w, grid_h) else None
		grid[y][x].s = grid[s_pt[1]][s_pt[0]] if in_bounds(s_pt, grid_w, grid_h) else None
		grid[y][x].nw = grid[nw_pt[1]][nw_pt[0]] if in_bounds(nw_pt, grid_w, grid_h) else None
		grid[y][x].ne = grid[ne_pt[1]][ne_pt[0]] if in_bounds(ne_pt, grid_w, grid_h) else None
		grid[y][x].sw = grid[sw_pt[1]][sw_pt[0]] if in_bounds(sw_pt, grid_w, grid_h) else None
		grid[y][x].se = grid[se_pt[1]][se_pt[0]] if in_bounds(se_pt, grid_w, grid_h) else None

# BFS
q = Queue()
q.put(Vertex(grid[y_origin][x_origin], 0))
grid[y_origin][x_origin].visited = True

def next_unvistited(n):
	neighbors = [n.n, n.s, n.nw, n.ne, n.sw, n.se]
	for neighbor in neighbors:
		if neighbor != None and not neighbor.visited:
			return neighbor
	return None

print("Start", (x_origin, y_origin))
print("Goal", normalizedEndPt)
while not q.empty():
	vertex = q.get()
	next = next_unvistited(vertex.node)

	while next != None and not (next.x == normalizedEndPt[0] and next.y == normalizedEndPt[1]):
		next.visited = True
		new_vert = Vertex(next, vertex.path_len + 1)
		q.put(new_vert)
		next = next_unvistited(vertex.node)

	if next != None and next.x == normalizedEndPt[0] and next.y == normalizedEndPt[1]:
		print(vertex.path_len + 1)
		break
