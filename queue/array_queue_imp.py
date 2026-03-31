#circular queue

class Queue:
    
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1
    #enqueue
    def enqueue(self,number):
        if self.front == -1:        
            self.front = 0
            self.rear = 0
            self.queue.append(number)

        else:
            self.rear = self.rear + 1
            self.queue.append(number)

    def dequeue(self):
        
        if self.front == -1:
            print("stack underflow")
            print()
        
        else:
            self.front = self.front + 1

            if self.front > self.rear:
                self.front = -1
                self.rear = -1
    
    def seek(self):
        if self.front == -1:
            print("Empty queue")
            print()
        
        else:
            print(f"Seek item: {self.queue[self.front]}")
            print()

    def print_all(self):
        if self.front == -1:
            print("Empty Queue")
            print()
        else:
            print(self.queue[self.front:self.rear+1])
            print()

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
                number = int(input("Eneter a Number to push:")) 
                q.enqueue(number)
            
            elif choice == 2:
                q.dequeue()
            elif choice == 3:
                q.seek()
            elif choice == 4:
                q.print_all()
            else:
                print("Enter Valid choice")
        except ValueError:
            print("Some Exception occured!! try entering Value again")

        




        

    