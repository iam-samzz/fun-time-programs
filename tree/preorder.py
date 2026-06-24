class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
class BinaryTree:
	def preorder(self,root):

		if root == None:
			return

		print(root.data)

		self.preorder(root.left)

		self.preorder(root.right)

		return


if __name__ == "__main__":
	root_n1 = Node(5)
	n2 = Node(3)
	n3 = Node(8)
	n4 = Node(2)
	n5 = Node(9)

	root_n1.left = n2
	root_n1.right = n3

	n2.left = n4
	n3.right = n5


	bt = BinaryTree()

	bt.preorder(root_n1)



