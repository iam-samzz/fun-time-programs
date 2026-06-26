from node import Node

class Tree:
    def find_parent_node(self,root,key):

        if root == None:
            return False
        
        if root.data == key:
            return True
        
        self.left = self.find_parent_node(root.left,key)
        if self.left == True:
            print(f"the parent node of the key is {root.data}")

        self.right = self.find_parent_node(root.right,key)
        if self.right == True:
            print(f"the parent node of the key is {root.data}")


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(12)
    root.right = Node(13)

    root.left.left = Node(7)
    root.left.right = Node(14)

    root.right.right = Node(2)

    root.left.left.left = Node(17)
    root.left.left.right = Node(23)

    root.left.right.left = Node(27)
    root.left.right.right = Node(3)

    root.right.right.left = Node(8)
    root.right.right.right = Node(11)

    bt = Tree()

    bt.find_parent_node(root,17)
    


        