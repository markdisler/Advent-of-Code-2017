day10 = __import__('Day10-2')

puzzle_input = 'ugkiagan'
used = 0
for i in range(128):
	knot_hash = day10.get_knot_hash(puzzle_input + '-' + str(i))
	as_bin = bin(int(knot_hash, 16))[2:]
	num_pad = 128 - len(as_bin)
	as_bin = ('0' * num_pad) + as_bin
	used += as_bin.count('1')
print(used)
