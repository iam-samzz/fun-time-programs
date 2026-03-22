class Node:
    def __init__(self,data):
        self.data = data
        self.next = None;
        

x = int(input("Enter the no.of element: "))


head = None
tail = None

for i in range(0,x):
    if i == 0:
        temp = Node(i)
        head = temp
        tail = temp
    else:
        temp = Node(i)
        tail.next = temp
        tail = temp 

current = head
while current!= None:
    print(current.data)
    current = current.next
