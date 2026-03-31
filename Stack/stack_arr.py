N = 10

stack = []
top = -1


#push
#pop
#seek
#print


def push(number):
    stack.append(number)

while(True):
    print("1. push")
    print("2. pop")
    print("3. seek")
    print("3. print-all")

    choice = int(input("Enter the choice:"))
    
    if choice == 1:
        number = int(input("Enter the num to push:"))
        push(number)
        top = top + 1
    elif choice == 2:
        if top == -1:
            print("Empty stack")
        else:
            stack.pop()
            top = top - 1
            print("Popped successfully")
    elif choice == 3:
        if top == -1:
            print("Empty stack")
        else:
            print(stack[top])
    elif choice == 4:
        if(top == -1):
            print("Empty stack")
        else:
            print(stack[::-1])

    elif choice == 0:
        break
    else:
        print("Enter valid choice!")
