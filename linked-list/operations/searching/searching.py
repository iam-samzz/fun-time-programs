class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

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

def searching(key,head):
    temp = head
    while temp!= None:
        if temp.data == key:
            return True
        temp = temp.next
    
    return False

if searching(11,head):
    print("element available")
else:
    print("not available")