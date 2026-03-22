#include<stdio.h>
#include<stdlib.h>

typedef struct node
{
    int data;
    struct node* next;
}node;

void insert_pos(node* head, int pos, int value);

int main()
{
    node* head = malloc(sizeof(node));
    head->data = 10;
    node* tail = head;
    node* temp = NULL;
    for(int i= 0; i<5;i++)
    {
        temp = malloc(sizeof(node));
        tail->next  = temp;
        temp->data = i*10;
        tail = temp;
    }

    //before
    temp = head;
    while(temp!=NULL)
    {
        printf("%d ",temp->data);
        temp = temp->next;
    }
    //now we wil insert at a pos
    insert_pos(head,2,99);
    printf("\n");
    //after
    temp = head;
    while(temp!=NULL)
    {
        printf("%d ",temp->data);
        temp = temp->next;
    }

    free(head);

}

void insert_pos(node* head, int pos, int value)
{
    node* p = head;

    for(int i=1;i<pos;i++)
    {
        p = p->next;
    }

    //now p is in pos-1 element
    node* temp = malloc(sizeof(node));
    temp->data = value;
    temp->next = p->next;
    p->next = temp;
}

