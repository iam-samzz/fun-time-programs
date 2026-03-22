#include<stdio.h>
#include<stdlib.h>

typedef struct node
{
    int data;
    struct node* next;
    struct node* prev;
}node;

node* insert_element(int n);

int main()
{
    int n = 10;

    node* p = insert_element(n);

    while(p!=NULL)
    {
        printf("%d\n",p->data);
        p = p->next;
    }
    
}

node* insert_element(int n)
{
    node* head = NULL;
    node* tail = NULL;
    node* temp = NULL;

    for(int i=0;i<n;i++)
    {
        temp = malloc(sizeof(node));
        if(temp == NULL)
        {
            printf("memory allocation failed!");
            exit(1);
        }

        if(i==0)
        {
            temp->data = i;

            head = temp;
            tail = temp;
            temp->prev = NULL;
            temp->next = NULL;
        }

        else{
            temp->data = i;

            temp->prev = tail;
            temp->next = NULL;

            tail->next = temp;

            tail = temp;
        }
    }

    return head;
}
