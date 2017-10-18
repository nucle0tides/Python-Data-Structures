"""
	Looking for myself, but I ended up in a cycle.
"""
class Graph(): 
	def __init__(self, nodes): 
		self.nodes = nodes
		self.root = nodes[0]

class Node(): 
	def __init__(self, data): 
		self.data = data
		self.visited = False
		self.neighbors = []

	def visit(self): 
		print(self.data)

	def set_neighbors(neighbors): 
		self.neighbors = neighbors

def depth_first_search(node):
	if node is None: 
		return 
	node.visit()
	node.visited = True
	for n in node.neighbors:
		if n.visited is False:
			depth_first_search(n)

