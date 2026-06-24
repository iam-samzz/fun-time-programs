from level_order_traversal import Node


class Tree:
    def depth(self,root):
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