count = 0

line = input()
while line != '':
	words = line.split(" ")
	wordSet = set(words)
	if len(words) == len(wordSet):
		count += 1

	line = input()

print(count)