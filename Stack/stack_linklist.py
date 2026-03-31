class Node:
    
    def __init__(self):
        self.data = None
        self.next = None

class Stack:
    def __init__(self):
            self.top = None
            self.count = 0

    def push_e(self,number):
        temp = Node()
        temp.data = number
        temp.next = self.top
        self.top = temp

        self.count = self.count+1

    def pop_e(self):

        if self.top == None:
            print("Stack Underflow")
            return False
        temp = self.top
        self.top = temp.next
        
        value = temp.data

        self.count = self.count - 1
        return value


    def seek(self):
        if self.top == None:
            print("Stack Underflow")
            return False

        print(self.top.data)

    def print_all(self):
        if self.top == None:
            print("Stack Underflow")
            return False
        temp = top

        while(temp!=None):
            print(temp.data)
            temp = temp.next



if __name__ == "__main__":
        st = Stack()

        while(True):
            print("1. push")
            print("2. pop")
            print("3. seek")
            print("4. print-all")
            
            choice = int(input("Enter the choice:"))
            
            if(choice == None):
                break

            if choice == 1:
                number = int(input("enter the num to push:"))
                st.push_e(number)
            elif choice == 2:
                st.pop_e()
            elif choice == 3:
                st.seek()
            elif choice == 4:
                st.print_all()
            else:
                break


