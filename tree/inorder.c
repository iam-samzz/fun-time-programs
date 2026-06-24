#include<stdio.h>
#include<stdlib.h>


typedef struct node
{
	int data;
	struct node * left;
	struct node * right;

}node;

int inorder(node* node)
{

	if(node == NULL)
	{
		return 0;
	}


	inorder(node->left);

	printf("%d,",node->data);

	inorder(node->right);

	return 0;
}

int main()
{
	node* n1 = malloc(sizeof(node));
	n1->data = 10;

	node* n2 = malloc(sizeof(node));
	n2->data = 5;

	node* n3 = malloc(sizeof(node));
	n3->data = 15;

	node* n4 = malloc(sizeof(node));
	n4->data = 3;

	node* n5 = malloc(sizeof(node));
	n5->data = 7;


	n1->left = n2;
	n1->right = n3;

	n2->left = n4;
	n2->right = n5;


	inorder(n1);
}