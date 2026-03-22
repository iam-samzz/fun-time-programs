class Node:
    def __init__(self):
        self.data = None
        self.nextn = None
        self.prevn = None


X = 10

for i in range(0,X):
    if(i==0):
        temp = Node()
        temp.data = i

        head = temp
        tail = temp
    else:
        temp = Node()
        temp.data = i

        temp.prevn = tail
        tail.nextn = temp

        tail = temp
    

# from head to tail print
current_p = head
while current_p != None:
    print(current_p.data,end= " ")
    current_p = current_p.nextn

print()
#from tail to head printing
current_p = tail
while current_p != None:
    print(current_p.data, end= " ")
    current_p = current_p.prevn


