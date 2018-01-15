import readline

input = input()
all_group_score = 0
sub_group_score = 0
looking_at_garbage = False
i = 0

while i < len(input):
	if input[i] == '!':
		i += 1
	elif looking_at_garbage == True:
		if input[i] == '>':
			looking_at_garbage = False
	elif input[i] == '{':
		sub_group_score += 1
		all_group_score += sub_group_score
	elif input[i] == '}':
		sub_group_score -= 1
	elif input[i] == '<':
		looking_at_garbage = True
	i += 1

print(all_group_score)
