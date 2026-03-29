#include<stdio.h>

#define N 10
//using array

int dequeue();
int enqueue();
int isEmpty();
int isFull();
int seek();


int queue[N];
int front = -1;
int rear = -1;

int main()
{
    while(1)
    {
        int choice;

        printf("Enter the Choice:\n");
        printf("1. enqueue\n");
        printf("2. dequeue\n");
        printf("3. seek\n");
        printf("0. quit\n");
        scanf("%d",&choice);

        if(choice == 0)
        {
            printf("Thank You!");
            break;
        }

        switch(choice)
        {
            case 1:
                int number;
                printf("Enter number to add in Queue: ");
                scanf("%d",&number);
                enqueue(number);
                break;
            case 2:
                dequeue();
                break;
            case 3:
                seek();
                break;

        }
    }
    return 0;
}

int isEmpty()
{
    if(front == -1 && rear == -1)
    {
        //empty
        return 0;
    }

    //not empty
    return -1;
}

int isFull()
{
    if((rear+1) % N == front)
    {
        //full
        return 0;
    }

    //not full
    return -1;
}


int enqueue(int number)
{
    //1st check if its full
    if(isFull(front,rear) == 0)
    {
        printf("Queue if Full\n");
        return -1;
    }
    
    if(front == -1)
    {
        front = 0;
    }
    rear = (rear + 1) % N;
    queue[rear] = number;
    printf("enqueue Successful\n");
    return 0;
}

int dequeue()
{
    //check if its empt'y
    if(isEmpty(front,rear) == 0)
    {
        printf("Queue is Empty\n");
        return -1;
    }
    
    //front == rear means only one element in the queue
    if(front == rear)
    {
        front = -1;
        rear = -1;
    }
    else
    {
        front = (front+1) % N;
    }
    printf("Dequeue Successful\n");
    return 0;
}

int seek()
{
    if(isEmpty(front,rear) == 0)
    {
        printf("Empty queue\n");
        return -1;
    }

    printf("seek: %d\n",queue[front]);
    return queue[front];
}

