#include<stdio.h>
#include<stdlib.h>

//structure
typedef struct node
{
    int data;
    struct node * next;
}node;

//prototype
node* insert_at_end(int n);

int main()
{
    int n = 10;
    node* p = insert_at_end(n);
    
    while(p!=NULL)
    {
        printf("%d\n",p->data);
        p = p->next;    
    }
}

node* insert_at_end(int n)
{
    node* head;
    node* tail;
    node* temp;

    for(int i=0;i<n;i++)
    {
        temp = malloc(sizeof(node));
        if(i==0)
        {
            head = temp;
            tail = temp;
            temp->data = i;
            temp->next = NULL;
        }
        else{
            tail->next = temp;
            tail = temp;
            temp->data = i;
            temp->next = NULL;
        }
    }

    return head;
}
