class Node:
    def __init__(self,data):
        self.data = data
        self.next = None;


x = int(input("Enter no.of element: "))

head =  None
for i in range(0,x):
    temp = Node(i)
    temp.next = head
    head = temp


while head!=None:
    print(head.data)
    head = head.next


