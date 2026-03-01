#include<stdio.h>

int main()
{
    int num = 50;
    int *ptr = &num;
    printf("%d \n",num);
    printf("%d \n",&num);
    printf("%d \n",ptr);
    printf("%d",*ptr);
}