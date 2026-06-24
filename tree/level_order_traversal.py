class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def level_order_traversal(self,root):
        queue = []

        queue.append(root)
        top = 0
        node_printed= 0

        while(node_printed<=top):
            current = queue[node_printed]
            print(current.data)
            node_printed = node_printed+1

            if current.left != None:
                queue.append(current.left)
                top = top+1
            if current.right != None:
                queue.append(current.right)
                top = top+1
    def level_order_recursion(self,l):
            
        if len(l)<1:
            return
        self.queue = []
        self.top = 0
        for i in l:
            print(i.data,end=",")
                
            if i.left != None:
                self.queue.append(i.left)
                self.top = self.top + 1
            if i.right != None:
                self.queue.append(i.right)
                self.top = self.top + 1
        print()
        self.level_order_recursion(self.queue)
            



            
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

    bt.level_order_recursion([root])

            

            


