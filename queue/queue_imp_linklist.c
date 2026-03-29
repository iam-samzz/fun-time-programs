#include<stdio.h>
#include<stdlib.h>


typedef struct node
{
    int data;
    struct node* next;
}node;

node* front = NULL;
node* rear = NULL;

void enqueue(int number)
{
    node* temp = malloc(sizeof(node));
    if(temp == NULL)
    {
        printf("Stack Overflow\n");
        exit(-1);
    }


    temp->data = number;
    temp->next = NULL;


    if(front == NULL)// checking if the queue is empty
    {
        front = temp;
        rear = temp;
        
    }
    else
    {
        rear->next = temp;
        rear = temp;
    }

}

int dequeue()
{
    if(front == NULL)
    {
        printf("Stack Underflow\n");
        return -1;
    }
    
    node* temp = front;
    front = temp->next;
    free(temp);

    if(front == NULL)
    {
        rear = NULL;
    }
    return 0;

}

int seek()
{
    if(front==NULL)
    {
        printf("No element to seek\n");
        return -1;
    }
    printf("%d\n",front->data); 
    return front->data;
}

int main()
{
    printf("hello\n");
    while(1)
    {
        int choice;

        printf("\nEnter the Choice:\n");
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