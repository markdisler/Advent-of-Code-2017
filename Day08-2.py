def evaluate(reg_val, comparison_op, cond_val):
	if comparison_op == '==':
		return reg_val == cond_val
	elif comparison_op == '<':
		return reg_val < cond_val
	elif comparison_op == '>':
		return reg_val > cond_val
	elif comparison_op == '<=':
		return reg_val <= cond_val
	elif comparison_op == '>=':
		return reg_val >= cond_val
	elif comparison_op == '!=':
		return reg_val != cond_val
	
maximum = 0
registers = dict()

line = input()
while line != '':
	tokens = line.split(' ')

	if tokens[0] not in registers:
		registers[tokens[0]] = 0
	if tokens[4] not in registers:
		registers[tokens[4]] = 0
			
	if evaluate(int(registers[tokens[4]]), tokens[5], int(tokens[6])):
		if tokens[1] == 'inc':
			registers[tokens[0]] += int(tokens[2])
		else:
			registers[tokens[0]] -= int(tokens[2])
		as_list = list(registers.values())
		as_list.append(maximum)
		maximum = max(as_list)

	line = input()

print(maximum)