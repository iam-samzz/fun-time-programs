//HELLO WORLD! THIS IS MY LINKED LIST PROBLEM BY ADDING DYNAMICALLY ELEMENTS TO END OF THE LIST!!  *_*


#include <stdio.h>
#include <stdlib.h>
typedef struct nodetype
{
    int data;
    struct nodetype *next;
}node;

typedef node *list; /*so this is ....type definition for " node* */
int main() {
    int n;
    char option;
    list tail,head,temp;
    head=tail=NULL;
    
    printf("WELCOME TO SAM'S LINKED LIST PROBLEM \n ----------------------------------------\n");
    printf("Enter element:");
    scanf("%d",&n);
    temp = (list)malloc(sizeof(node));
    temp->data = n;
    temp->next = NULL;
    tail=temp;
    head = temp;
    temp = NULL;
    printf("DON'T ENTER NUMBERS FOR y/n");
    printf("\nDo you want to continue(y/n):");
    scanf(" %c",&option);
    
    while(option !='n' && option!='N')
    {
            printf("\nEnter element:");
            scanf("%d",&n);
            temp = (list)malloc(sizeof(node));
            temp->data = n;
            temp->next = NULL;
            tail->next = temp;
            tail = temp;
            printf("\nDo you want to continue(y/n):");
            scanf(" %c",&option);
            if(option=='N' || option=='n')
            {
                break;
            }
    }

        //printing the elements of linked list..
        temp = head;
        printf("\nPRINTING THE ELEMENTS....PLEASE WAIT *_*\n \n \n");
        printf("LIST: [");
        while(temp!=NULL)
        {
            printf("%d",temp->data);
            if(temp->next!=NULL)
            {
                printf(",");
            }
            temp = temp->next;
        }
        printf("]");
    }
