#include<stdio.h>

int main()
{
    int arr[] = {1,3,4,5,6,7,20,7,8};
    int size = sizeof(arr)/sizeof(arr[0]);

    int index;
    printf("enter index:");
    scanf("%d",&index);

    if(index>size || index<0)
    {
        printf("Enter Valid Index\n");
        return 1;
    }

    printf("Enter Value:");
    scanf("%d",&arr[index]);

    printf("Updated list:");
    printf("\n[");
    for(int i=0; i<size; i++){
        printf("%d,",arr[i]);
    }
    printf("]\n");

    return 0;
}