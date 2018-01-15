line = input()

cycles = 0
configurations = set()
blocks = [int(i) for i in line.split("\t")]
cur_config_str = " ".join(str(x) for x in blocks)

while cur_config_str not in configurations:
	print(cur_config_str)
	configurations.add(cur_config_str)

	# Redistribute blocks
	idx = blocks.index(max(blocks))
	num = blocks[idx]
	blocks[idx] = 0
	idx = (idx + 1) % len(blocks);
	while num > 0:
		blocks[idx] += 1
		num -= 1
		idx = (idx + 1) % len(blocks);

	cur_config_str = " ".join(str(x) for x in blocks)
	cycles += 1


print(cycles)


