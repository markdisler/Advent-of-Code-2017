count = 0

line = input()
while line != '':
	words = line.split(" ")
	word_set_sorted_letters = set()
	for word in words:
		word_set_sorted_letters.add(''.join(sorted(word)))

	if len(words) == len(word_set_sorted_letters):
		count += 1

	line = input()

print(count)