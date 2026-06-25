from node import Node

class Tree:
    def search_a_node(self,root,key):
        
        status = False
        #base cases        
        if root == None:
            return False
        if root.data == key:
            status = True
            return status

        #recursive case

        left_status = self.search_a_node(root.left,key)

        right_status = self.search_a_node(root.right,key)
        
        status = left_status or right_status

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

    print(bt.search_a_node(root,17))
        