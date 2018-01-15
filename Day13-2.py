depth_range_dict = dict()
line = input()
last_depth = 0
while line != '':
	last_depth = int(line.split(': ')[0])
	depth_range_dict[last_depth] = int(line.split(': ')[1])
	line = input()

for i in range(0, last_depth + 1):
	if not i in depth_range_dict:
		depth_range_dict[i] = 0

delay = 0
done = False
while not done:
	done = True

	for i in range(0, last_depth + 1):
		if depth_range_dict[i] != 0:
			if (i + delay) % (2 * (depth_range_dict[i] - 1)) == 0:
				done = False
				delay += 1
				print(delay)
				break
