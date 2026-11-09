#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node * next;
}node;


int main(){

    node* head = NULL;

    for(int i = 0; i< 5; i++){

        node* temp = NULL;
        temp = malloc(sizeof(node));
        temp->data = 10;
        temp->next = head; //connecting to the prev head
        head = temp;
    };

    node* temp = head;
    while (temp != NULL){
        printf("%d", temp->data);
        printf("\n");
        temp = temp->next;
    };

}


