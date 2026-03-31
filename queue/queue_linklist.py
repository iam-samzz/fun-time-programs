class Node:
    def __init__(self):
        self.data = None
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,number):
        temp = Node()
        temp.data = number
        temp.next = None

        if self.front == None:
            self.front = temp
            self.rear = temp
            
        else:
            self.rear.next = temp
            self.rear = temp
    
    def dequeue(self):

        if self.front == None:
            print("Queue Underflow!")
            return None

        else:
            #before
            value = self.front.data

            #after
            self.front = self.front.next

            #if the front crosses the rear
            if self.front == None:
                self.front = None
                self.rear = None
        
            #return before value
            return value

    def seek(self):
        if self.front == None:
            print("Empty Queue")
        else:
            return self.front.data

    def print_all(self):
        if self.front == None:
            print("Empty Queue")

        else:

            temp = self.front

            print("[",end = "")
            while temp != None:
                print(temp.data,end = ",")
                temp = temp.next
            print("]")

        
if __name__ == "__main__":
    q = Queue()
    while(True):
        print()
        print("1. enqueue")
        print("2. dequeue")
        print("3. seek")
        print("4. print-all")
        print("0. exit")
        try:
            choice = int(input("Enter the choice:"))

            if choice == 0:
                print("exiting..")
                break
            elif choice == 1:
                #enqueue
                number = int(input("Eneter a Number to enqueue:")) 
                q.enqueue(number)
            
            
            elif choice == 2:
                value = q.dequeue()
                if value is not None:
                    print("Done!")
                    print(f"Dequeued item: {value}")
                
            elif choice == 3:
                print("seek item: ",q.seek())
            elif choice == 4:
                q.print_all()
            else:
                print("Enter Valid choice")
        except ValueError:
            print("Some Exception occured!! try entering Value again")



