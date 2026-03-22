class Node:
    
    def __init__(self):
        self.data = None
        self.next = None
def insert_f(n):
    temp = None
    head = None
    tail = None

    for i in range(0,n):
        temp = Node()
        
        d = int(input(""))
        temp.data = d


        if i==0:
            head = temp
            tail = temp
        else:
            tail.next = temp
            tail = temp
    return head

def traversal(head):
    print("-----------")
    p = head
    while p!= None:
        print(p.data,end="->")
        p = p.next




n = int(input("Enter the num:"))
h = insert_f(n)
traversal(h)