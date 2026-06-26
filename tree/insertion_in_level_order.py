from node import Node
from inorder import BinaryTree
class Tree:
    def insertion(self,root,key):
        queue = [root]
        top = 1

        while len(queue)!=0:

            current = queue.pop(0)

            if current.left == None:
                n1 = Node(key)
                current.left = n1
                return root
            else:
                queue.append(current.left)
                top = top + 1

            if current.right == None:
                n1 = Node(key)
                current.right = n1
                return root
            else:
                queue.append(current.right)
                top = top + 1

        

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.right = Node(9)
    root.left.left = Node(7)
    root.right.left = Node(15)
    root.right.right = Node(8)

    key = 12

    bt = BinaryTree()
    bt.inorder_f(root)


    t = Tree()
    t.insertion(root,key)

    print()
    bt.inorder_f(root)