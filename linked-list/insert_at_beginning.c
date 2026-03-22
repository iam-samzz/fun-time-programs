#include<stdio.h>
#include<stdlib.h>



typedef struct node
{
    int data;
    struct node* next;
}node;


node* insert_element(int n);


int main()
{   
    int n;
    printf("Enter the number of element:");
    scanf("%d",&n);

    
    printf("\n");
    printf("inserting...\n");

    node* head_p = insert_element(n);
    while(head_p != NULL)
    {
        printf("%d,",head_p->data);
        head_p = head_p->next;
    }

    free(head_p);
}

node* insert_element(int n)
{
    node * head = NULL;
    node * temp = NULL;

    for(int i=0;i<n;i++)
    {
        temp = (node*)malloc(1*sizeof(node));
        temp->data = i;
        temp->next = head;
        head = temp;
    }

    return head;
}