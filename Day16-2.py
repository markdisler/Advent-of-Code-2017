import readline

line = 'abcdefghijklmnop'
starting = line
dance_moves = input().split(',')

def run_dance(line):
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
	return line

line = run_dance(line)
count_for_cycle = 1
while line != starting:
	line = run_dance(line)
	count_for_cycle += 1
print('Cycle length', count_for_cycle)

for i in range(0, 1000000000 % count_for_cycle):
	line = run_dance(line)
print(line)