#include<stdio.h>

int main()
{
    int arr[10];
    int * ptr;

    ptr = &arr[0]; //pointing the address to 1st element


    ptr[2] = 100;
    arr[3] = 200;

    printf("%d \n",ptr[2]);
    printf("%d",arr[3]);


    //so basically, the 'arr' itself is a pointer like ptr
    int (*b)[10]; //b is a pointer which pointer to entire array , not just one element

    int *c[10]; //there is an array of 10 elements each pointing to an integer, and as usual, c points to 1st element in the arr

}
