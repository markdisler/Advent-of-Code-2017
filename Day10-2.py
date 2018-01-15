def get_knot_hash(puzzle_input):
	num_list = [i for i in range(256)]
	cur_pos = 0
	skip = 0
	lengths = list()
	for c in puzzle_input:
		lengths.append(ord(c))
	lengths.extend([17, 31, 73, 47, 23])

	for i in range(64):
		for length in lengths:
			start = cur_pos
			end = (cur_pos + length) % len(num_list) - 1

			for x in range(0, int(length / 2)):
				temp_start = num_list[start]
				num_list[start] = num_list[end]
				num_list[end] = temp_start
				start = (start + 1) % len(num_list)
				end = (((end - 1) % len(num_list)) + len(num_list)) % len(num_list)

			cur_pos = (cur_pos + length + skip) % len(num_list)
			skip += 1

	knot_hash = ''
	for i in range(16):
		block = num_list[i * 16: (i+1) * 16]
		dh = block[0]
		for x in range(1, 16):
			dh ^= block[x]
		knot_hash += "%0.2X" % dh	
	return knot_hash.lower()

puzzle_input = '34,88,2,222,254,93,150,0,199,255,39,32,137,136,1,167'
print(get_knot_hash(puzzle_input))


