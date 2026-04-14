#include<stdio.h>
#include<stdlib.h>

typedef struct node
{
    int data;
    struct node* next;
}node;

//typecasting
int push(int num,node** top);
int print(node* top);

//push and print operation using singly linekd list
int main()
{
    //initialiING TOP as NULL
    node* top = NULL;


    while(1)
    {
        int choice;
        printf("Enter the Choice:\n");
        printf("1. Push\n");
        printf("2. Print\n");
        printf("0. quit\n");
        scanf("%d",&choice);

        if(choice == 0)
        {
            break;
        }

        switch(choice)
        {
            case 1:
                int num;
                printf("Enter the Num to push:");
                scanf("%d",&num);

                push(num,&top);
                break;
            case 2:
                print(top);
                break;
        }

    }

    return 0;
}

int push(int num,node** top_p)
{
    node* temp = malloc(sizeof(node));
    if(temp == NULL)
    {
        printf("Stack Overflow");
        return -1;
    }

    temp->data = num;
    temp->next = *top_p;
    *top_p = temp;

    printf("Pushed %d\n",num);
    return 0;
}

int print(node* top)
{
    if(top == NULL)
    {
        printf("No element to print!\n");
        return -1;
    }

    node* temp = top;
    while(temp!=NULL)
    {
        printf("%d,",temp->data);
        temp = temp->next;
    }

    printf("\n");
    return 0;
}