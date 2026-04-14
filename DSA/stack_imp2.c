#include<stdio.h>

#define N 10

int push(int number,int *top, int* stack);
int pop(int* top, int* stack);
int seek(int* top,int* stack);
int print(int* top,int* stack);


int main()
{
    int choice;
    int stack[N];
    int top = -1;
    int * t = &top;

    while(1)
    {
        printf("Enter the choices:\n");;
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. print all element form stack\n");
        printf("4  seek\n");
        printf("5. quit\n");

        scanf("%d",&choice);

        if(choice == 5)
        {   
            break;
        }

        switch (choice)
        {
            case 1:
                int num;
                printf("Enter the number to Push:");
                scanf("%d",&num);
                if(push(num,t,stack) == 0)
                {
                    printf("Pushed %d successfully\n",num);
                }
                break;
            case 2:
                pop(t,stack);
                break;
            case 3:
                print(t,stack);
                break;   
            case 4:
                seek(t,stack);
                break;
            
        }

    }

    return 0;

}

int push(int number,int *top, int* stack)
{
    if(*top == N-1)
    {
        printf("Stack Overflow\n");
        return -1;
    }

    *top = *top + 1;
    stack[*top] = number;
    return 0;
}

int pop(int* top, int* stack)
{
    if(*top == -1)
    {
        printf("Stack Underflow\n");
        return -1;
    }
    
    *top = *top - 1;
    return 0;
}

int seek(int* top,int* stack)
{
    if(*top == -1)
    {
        printf("No element to seek\n");
        return -1;
    }
    
    printf("seek item: %d\n",stack[*top]);
    return 0;
}

int print(int* top,int* stack)
{
    if(*top == -1)
    {
        printf("Stack Underflow\n");
        return -1;
    }
    printf("{");
    for(int i = *top;i > -1; i--)
    {
        if(i==0)
        {
            printf("%d",stack[i]);
            break;
        }
        printf("%d,",stack[i]);
    }

    printf("}\n");
    return 0;
}

