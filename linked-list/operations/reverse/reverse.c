#include<stdio.h>
#include<stdlib.h>

typedef struct node
{
    int data;
    struct node* next;
}node;

void reverse(node* head);


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

    
        temp = head;
    while(temp!=NULL)
    {
        printf("%d ",temp->data);
        temp = temp->next;
    }
    //now we wil insert at a pos
    reverse(head);
    printf("\n");
    //after
    temp = head;
    while(temp!=NULL)
    {
        printf("%d ",temp->data);
        temp = temp->next;
    }
    
}

void reverse(node* head)
{
    node* pre = NULL;
    node* current = head;
    node* nxt = head->next;

    while(current!=NULL)
    {

    }

}   