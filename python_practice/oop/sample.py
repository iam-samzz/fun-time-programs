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
        
        if last_removed[2] == 0:
            last_removed[1].left = None

        if last_removed[0].data == 1:
            last_removed[1].rigth = None

        #basically we are deleting the rightmost node and the deleting that node
        return self.data
