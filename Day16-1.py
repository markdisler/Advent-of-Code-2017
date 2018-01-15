import readline

line = 'abcdefghijklmnop'
dance_moves = input().split(',')

for move in dance_moves:
	if move[0] == 's':
		split_idx = len(line) - int(move[1:])
		line = line[split_idx:] + line[0:split_idx]
	else:
		x_args = move[1:].split('/')
		if move[0] == 'x':
			x_args = [int(i) for i in x_args]
			x_args = [line[x_args[0]:x_args[0]+1], line[x_args[1]:x_args[1]+1]]
		line = line.replace(x_args[0], '*')
		line = line.replace(x_args[1], x_args[0])
		line = line.replace('*', x_args[1])
	
print(line)