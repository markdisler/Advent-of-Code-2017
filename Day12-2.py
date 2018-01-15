def path_exists(start_id, goal_id, program_dict, seen):
	if start_id in seen:
		return False
	seen.append(start_id)

	if start_id == goal_id:
		return True

	for a in program_dict[start_id]:
		if path_exists(a, goal_id, program_dict, seen):
			return True
	return False


program_associates = dict()
program_set = set()
line = input()
while line != '':
	program_id = int(line[0:line.index('<') - 1])
	program_set.add(program_id)
	program_associates[program_id] = [int(i) for i in line[line.index('>') + 1 : len(line)].split(', ')]
	line = input()

# WARNING: Rather slow, but it works
groups = 0
while len(program_set) > 0:
	programs_in_group = list()
	for key, value in program_associates.items():
		if (path_exists(key, list(program_set)[0], program_associates, list())):
			programs_in_group.append(key)
	program_set = program_set - set(programs_in_group)
	print(len(program_set))
	groups += 1

print(groups)
	
