from level_order_traversal import Node


class Tree:
    def depth(self,root):
        if root == None:
            return [0,0]

        self.left = 0
        self.right = 0

        if root.left != None:
            self.left = 1
        
        if root.right != None:
            self.right = 1

        
        #basically for a node n, max we are adding the next left branch length(1) and the maximum length of the complete left branch
        max_left = self.left + max(self.depth(root.left))
        max_right = self.right + max(self.depth(root.right))

        max_list = [max_left,max_right]


        #this only returns the max length of left branch from the root and the right branch from the root. like , [4,2], here 4 is the length
        return max_list

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
    print(max(bt.depth(root)))