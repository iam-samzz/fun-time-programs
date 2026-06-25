from node import Node

class Tree:
    def level_of_node(self,root,root_level,key):
        
        if root == None:
            return False
        #base case
        if root.data == key:
            print(f"the level of {key} is: {root_level}")
            return True
        
        #recursive case
        status_left = self.level_of_node(root.left,(root_level+1),key)

        status_right = self.level_of_node(root.right,(root_level+1),key)

        status =  status_left or status_right

        return status
        
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

    bt.level_of_node(root,0,17)
