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
line = input()
while line != '':
	program_id = int(line[0:line.index('<') - 1])
	program_associates[program_id] = [int(i) for i in line[line.index('>') + 1 : len(line)].split(', ')]
	line = input()

count = 0
for key, value in program_associates.items():
	if (path_exists(key, 0, program_associates, list())):
		count += 1

print(count)
	
