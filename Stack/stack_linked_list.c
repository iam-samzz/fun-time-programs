#include<stdio.h>
#include<stdlib.h>

typedef struct node
{
    int data;
    struct node* next;
}node;

node* push(int number, node* top);
int print(node* top);
int pop(node** top_l);
int seek(node* top);
int clear(node** top_l);

int main()
{
    //top_main
    node* top = NULL;


    //operarions: push,pop,print,seek,quit
    while(1)
    {
        int choice;
        printf("Enter the choice:\n");
        printf("1. push\n");
        printf("2. pop\n");
        printf("3. seek\n");
        printf("4. print all\n");
        printf("5. clear the list\n");
        printf("0. quit\n");
        scanf("%d",&choice);

        if(choice == 0)
        {
            break;
            return 0;
        }

        switch(choice)
        {
            case 1:
                int number;
                printf("Enter the number to push:");
                scanf("%d",&number);
                top = push(number,top);
                break;

            case 2:
                number = pop(&top);
                printf("Popped %d\n",number);
                break;
            case 3:
                seek(top);
                break;
            case 4:
                print(top);
                break;
            case 5:

                clear(&top);
                break;

        }
    }
}

//push the elements
node* push(int number, node* top)
{
    node* temp = malloc(sizeof(node));
    if(temp == NULL)
    {
        printf("Stack Overflow");
        exit(-1);
    }

    temp->data = number;
    temp->next = top;
    top = temp;
    printf("Pushed %d\n",number);
    return top;
}

//print all elements in the LL
int print(node* top)
{
    if(top == NULL)
    {
        printf("No element exits!\n");
        return -1;
    }

    printf("{");
    while(top!=NULL){
        printf("%d,",top->data);
        top = top->next;
    }
    printf("}\n");

    return 0;

}

//pop the element and return the popped element
int pop(node** top_l)
{
    

    if(*top_l == NULL)
    {
        printf("Stack Underflow!\n");
        exit(-1);
    }

    node* temp = *top_l;
    int d = temp->data;
    *top_l = temp->next;

    free(temp);

    return d;
}

//seek the top element

int seek(node* top)
{
    if(top == NULL)
    {
        printf("No element to seek.\n");
        return -1;
    }

    printf("%d\n",top->data);
    return 0;
}

//clear the whole Linked List
int clear(node** top_l)
{
    if(*top_l == NULL)
    {
        printf("Already empty set\n");
        return -1;
    }
    node* temp;
    while(*top_l!=NULL)
    {
        temp = *top_l;
        *top_l = temp->next;
        free(temp);
    }
    return 0;
}
