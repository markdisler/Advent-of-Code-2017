import readline

def divisible_values(list):
	for i in range(0, len(list)):
		for j in range(0, len(list)):
			if i != j:
				a = list[i]
				b = list[j]
				if a % b == 0:
					return [min(a, b), max(a, b)]
	return [0, 0]


line = input()
sum = 0

while line != '':
    strVals = line.split("\t")
	intVals = [int(z) for z in strVals]
	div_vals = divisible_values(intVals)
	sum += (div_vals[1] / div_vals[0])

	line = input()

print(int(sum))
