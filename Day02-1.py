 import readline

line = input()
sum = 0
while line != '':
    strVals = line.split("\t")
	intVals = [int(i) for i in strVals]
	sum += max(intVals) - min(intVals)
	line = input()

print(sum)
