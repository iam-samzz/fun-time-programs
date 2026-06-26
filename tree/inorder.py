#in order usinig recursion in binary tree


class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None


class BinaryTree:

	def inorder_f(self,start_node):

		if start_node == None:
			return

		self.inorder_f(start_node.left)

		print(start_node.data,end=",")

		self.inorder_f(start_node.right)

		return



if __name__ == "__main__":

	n1 = Node(10)
	n2 = Node(5)
	n3 = Node(15)
	n4 = Node(7)

	n5 = Node(3)


	n1.left = n2
	n1.right = n3
	n2.right = n4
	n2.left = n5


	t1 = BinaryTree()

	t1.inorder_f(n1)
