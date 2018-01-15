samples = 0
matches = 0
prev_a = 277
prev_b = 349

while samples < 40000000:
	prev_a = (prev_a * 16807) % 2147483647
	prev_b = (prev_b * 48271) % 2147483647

	if prev_a & 0xFFFF == prev_b & 0xFFFF:
		matches += 1

	print(samples)
	samples += 1

print('Number of Matches:', matches)
