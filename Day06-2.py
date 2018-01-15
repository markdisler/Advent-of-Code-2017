line = input()

cycles = 0
configurations = set()
blocks = [int(i) for i in line.split("\t")]
cur_config_str = " ".join(str(x) for x in blocks)
seen = False
repeating_distrib = "";

while cur_config_str not in configurations or seen:
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

	# Once seen, start counting cycles
	if seen:
		cycles += 1

	# Update config string
	cur_config_str = " ".join(str(x) for x in blocks)
	
	# If we come across the repeated config again, we can stop
	if cur_config_str == repeating_distrib:
		break

	# Save the configuration that is being repeated
	if cur_config_str in configurations and not seen:
		seen = True
		repeating_distrib = cur_config_str

print(cycles)


