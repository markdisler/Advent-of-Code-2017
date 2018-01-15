class SecScanner:
	def __init__(self, depth, location, range):
		self.depth = depth
		self.location = location
		self.range = range
		self.direction = 1

	def step(self):
		if self.location >= 0:
			self.location += self.direction
			if self.location == self.range - 1 or self.location == 0:
				self.direction *= -1

	def caught(self, pos):
		return self.depth == pos and self.location == 0

depth_range_dict = dict()
line = input()
last_depth = 0
while line != '':
	last_depth = int(line.split(': ')[0])
	depth_range_dict[last_depth] = int(line.split(': ')[1])
	line = input()

# Fill missing depths AND construct scanners
scanners = list()
for i in range(0, last_depth + 1):
	if not i in depth_range_dict:
		depth_range_dict[i] = 0
	scanners.append(SecScanner(i, 0 if depth_range_dict[i] > 0 else -1, depth_range_dict[i]))	

# Move through firewall	
me = -1 # start outside layer 0
severity = 0
while me < last_depth:
	me += 1
	for s in scanners:
		if s.caught(me):
			severity += (me * depth_range_dict[me])
		s.step()

print(severity)

