#include<stdio.h>
#include<stdlib.h>

typedef struct node
{
    int data;
    struct node* next;
}node;

int searching(int key,node* head);

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
    
    if(searching(10,head) == 0)
    {
        printf("Element Available");
    }
    else
    {
        printf("Not available");
    }
}

int searching(int key,node* head)
{
    node* p = head;
    
    while(p!=NULL)
    {
        if(p->data == key)
        {
            return 0;
        }
        
        p = p->next;
    }
    p = NULL;
    return 1;
}