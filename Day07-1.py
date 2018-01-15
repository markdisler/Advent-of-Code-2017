line = input()

# All disc names (regardless of whether they hold other discs)
all_names = set()

# Discs that are being held (ie: are pointed to by "->")
held_discs = set() 

while line != '':
	all_names.add(line) # remember the name

	# If arrow found, the part following contains held discs
	if "->" in line:
		start_idx = line.index("->")
		sub = line[(start_idx + 3)::]
		parts = sub.split(", ")
		held_discs.update(parts) # add held discs to set
	
	line = input()

# Check all disc names to see if they are not held.
# The disc that is not held is the one at the bottom (it is doing the holding)
for disc_name in all_names:
	basic_name = disc_name[0:disc_name.index('(') - 1]
	if basic_name not in held_discs:
		print("Answer:", basic_name)
		break

