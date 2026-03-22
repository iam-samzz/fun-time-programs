#include<stdio.h>
#include<stdlib.h>

typedef struct node
{
    int data;
    struct node* next;
}node;

//prototypes:
node* insert(int n);
void traverse(node* head);

int main()
{
    int n;
    printf("Enter the no.of element:");
    scanf("%d",&n);

    node* p = insert(n);

    traverse(p);

}

node* insert(int n)
{

    node* head = NULL;
    node* tail = NULL;
    node* temp = NULL;

    printf("enter the num:");
    int x;

    for(int i=0;i<n;i++)
    {
        scanf("%d",&x);

        temp = malloc(sizeof(node));
        if(temp==NULL)
        {
            printf("Mem Alloc not sucess");
            exit(1);
        }


        temp->data = x;
        temp->next = NULL;
        if(i==0)
        {
            head = temp;
            tail = temp;
        }
        else
        {
            tail->next = temp;
            tail = temp;
        }
    }

    return head;
}

void traverse(node* head)
{
    node* p = head;

    while(p!=NULL)
    {
        printf("%d->",p->data);
        p = p->next;
    }

}