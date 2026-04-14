#include<stdio.h>

#define N 2



int push(int number,int* top, int* stack);
int pop(int* top, int* stack);


int main()
{
    int stack[N];

    int top = -1;
    int *t = &top;

    push(10,t,stack);
    push(20,t,stack);
    push(30,t,stack);
}

int push(int number,int* top, int* stack)
{   
    if(*top == N-1)
    {
        printf("Can't push %d-",number);
        printf("Stack Overflow");
        return -1;
    }

    *top = *top+1;
    stack[*top] = number;
    printf("Pushed %d\n",number);
    return 0;
}

int pop(int* top, int* stack)
{
    if(*top == -1)
    {
        printf("Stack Underflow");
        return -1;
    }

    int temp = stack[*top];
    *top = *top - 1;
    return temp;
}