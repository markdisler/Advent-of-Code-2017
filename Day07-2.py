class Node:
	def __init__(self, name, weight, children):
		self.name = name
		self.weight = weight
		self.children = children
	def __str__(self):
		return "{}, {}, {}".format(self.name, self.weight, self.children)
	def __repr__(self):
		return "{}, {}, {}".format(self.name, self.weight, self.children)

def build_from_root(root, child_dict):
	if root.name in child_dict:
		for child in child_dict[root.name]:
			print(child.name, "is child of", root.name)
			build_from_root(child, child_dict)
			root.children.append(child)

def weight_of_tower(root):
	total_weight = root.weight
	if len(root.children) > 0:
		for child in root.children:
			total_weight += weight_of_tower(child)
	return total_weight


def detect_outlier(node):
	if len(node.children) > 0:

		mini_set = set()
		mini_list = list()
		node_dict = dict()
		for n in node.children:
			w = weight_of_tower(n)
			mini_list.append(w)
			mini_set.add(w)
			node_dict[w] = n

		if len(mini_set) != 1:
			print(mini_list)
			for elem in mini_set:
				mini_list.remove(elem)

			actual = mini_list[0]
			mini_set.remove(actual)

			outlier = list(mini_set)[0]
			print("Outlier:", outlier)	

			outlier_node = node_dict[outlier]
			rest_of_weight = weight_of_tower(outlier_node) - outlier_node.weight
			print(rest_of_weight)

			print("Actual Value:", actual - rest_of_weight)


			detect_outlier(node_dict[outlier])		


#dict
parent_child_dict = dict()
name_weight_dict = dict()

# All disc names (regardless of whether they hold other discs)
nodes = set()

# Discs that are being held (ie: are pointed to by "->")
held_discs = set() 

line = input()
while line != '':
	basic_name = line[0:line.index('(') - 1]
	weight = int(line[line.index('(') + 1:line.index(')')])
	nodes.add(Node(basic_name, weight, list())) # remember the name
	name_weight_dict[basic_name] = weight;

	# If arrow found, the part following contains held discs
	if "->" in line:
		start_idx = line.index("->")

		# Name
		parent = line[0:line.index('(') - 1]

		# Children names
		sub = line[(start_idx + 3)::]
		children_names = sub.split(", ")
		children = [Node(i, 0, list()) for i in children_names]

		held_discs.update(children_names) # add held discs to set

		parent_child_dict[parent] = children

	line = input()

print(name_weight_dict)	

# Resolve child weights
for k,v in parent_child_dict.items():
	child_list = parent_child_dict[k]
	for i in range(0, len(child_list)):
		child_list[i].weight = name_weight_dict[child_list[i].name]

# Check all disc names to see if they are not held.
# The disc that is not held is the one at the bottom (it is doing the holding)
root = None
for n in nodes:
	if n.name not in held_discs:
		root = n
		print("Answer:", n.name)
		break

build_from_root(root, parent_child_dict)
detect_outlier(root)
