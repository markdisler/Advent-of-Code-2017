num_list = [i for i in range(256)]
cur_pos = 0
skip = 0
lengths = [int(i) for i in '34,88,2,222,254,93,150,0,199,255,39,32,137,136,1,167'.split(',')]

for length in lengths:
	start = cur_pos
	end = (cur_pos + length) % len(num_list) - 1

	for i in range(0, int(length / 2)):
		temp_start = num_list[start]
		num_list[start] = num_list[end]
		num_list[end] = temp_start
		start = (start + 1) % len(num_list)
		end = (((end - 1) % len(num_list)) + len(num_list)) % len(num_list)

	cur_pos = (cur_pos + length + skip) % len(num_list)
	skip += 1
	print(num_list, '\n')

print(num_list[0] * num_list[1])

