steps = 0
instructions = list()

# Get instructions
line = input()
while line != '':
	instructions.append(int(line))
	line = input()

# Follow instructions
idx = 0
while idx >= 0 and idx < len(instructions):
	offset = instructions[idx]
	if offset >= 3:
		instructions[idx] -= 1
	else:
		instructions[idx] += 1

	idx += offset
	steps += 1

print(steps)