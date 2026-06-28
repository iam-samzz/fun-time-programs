from node import Node
# problem from https://www.geeksforgeeks.org/dsa/deletion-binary-tree/

from inorder import BinaryTree

class Tree:
     #finding deepest node and right most node
    def find_right_most(self,root):
        queue = [(root,None,None)]

        top = 0

        #left = 0, right = 1

        while len(queue) != 0:
        
            last_removed = queue.pop(0)

            if last_removed[0].left != None:
                queue.append((last_removed[0].left,last_removed[0],0))
                top = top + 1
                
            if last_removed[0].right != None:
                queue.append((last_removed[0].right,last_removed[0],1))
                top = top + 1

             
        
        self.data = last_removed[0].data
        
        #print()
        #print(last_removed[1].data,last_removed[1].left.data,last_removed[1].right.data)
        #print()
        if last_removed[2] == 0:
            last_removed[1].left = None

        if last_removed[2] == 1:
            last_removed[1].right = None

        #print()


        #basically we are deleting the rightmost node and the deleting that node
        return self.data
    
    def find_key_node(self,root,key,original_root):

        #we want to find the key node and changes it data from the right most data4
        
        if root == None:
            return False
        if root.data == key:
            #print(root.data)
            root.data = self.find_right_most(original_root)
            return True
        
        status = self.find_key_node(root.left,key,original_root)
        if status != True:
            status = self.find_key_node(root.right,key,original_root)

        return status
    

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.right = Node(9)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right.left = Node(15)
    root.right.right = Node(8)

    original_root = root
    key = 11

    bt = BinaryTree()
    bt.inorder_f(root)



    t = Tree()
    t.find_key_node(root,key,original_root)

    print()
    bt.inorder_f(root)
 
    
        
        
            

