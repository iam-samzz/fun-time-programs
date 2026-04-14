class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

def insert_At_pos(head,pos,value):

    for i in range(0,pos):
        if i == 0:
            p = head
        else:    
            p = p.next

    #now p is at pos-1

    temp = Node(value)
    temp.next = p.next
    p.next = temp

#main
for i in range(0,5):
    if i == 0:
        temp = Node(10)
        head = temp
        tail = temp
        
    else:
        temp = Node(i)
        tail.next = temp
        tail = temp


#before
temp = head
while(temp!=None):
    print(temp.data,end=" ")
    temp = temp.next

insert_At_pos(head,2,99)
print()
temp = head
while(temp!=None):
    print(temp.data, end=" ")
    temp = temp.next





