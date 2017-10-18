"""
	UHHHH, A TREE
"""
class Node(): 
	def __init__(self, data): 
		self.data = data
		self.left = None
		self.right = None

	def visit(self): 
		print(self.data)

def in_order(node): 
	if node is not None: 
		in_order(node.left)
		node.visit()
		in_order(node.right)

def pre_order(node): 
	if node is not None: 
		node.visit()
		pre_order(node.left)
		pre_order(node.right)

def post_order(node): 
	if node is not None: 
		post_order(node.left)
		post_order(node.right)
		node.visit()

if __name__ == '__main__':
	root = Node(10)
	root.left = Node(6)
	root.right = Node(16)
	root.left.left = Node(4)
	root.left.right = Node(8)
	root.right.left = Node(11)
	root.right.right = Node(20)
	print("IN ORDER")
	in_order(root)
	print("\n\n\nPRE ORDER")
	pre_order(root)
	print("\n\n\nPOST ORDER")
	post_order(root)