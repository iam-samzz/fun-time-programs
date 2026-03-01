#include<stdio.h>

int main(){

    int arr[] = {1,10,30,60,2,4,22,10,-2,-15,0,-100,1000,2};

    int size = sizeof(arr) / sizeof(arr[0]);
    int number;
    printf("Enter a number for linear Search:");
    scanf("%d",&number);

    int status = 0;
    for(int i = 0;i<size; i++)
    {
        if(arr[i] == number)
        {
            printf("Element found at index:%d\n",i);
            status = 1;
        }

    }
    
    if(status == 0){
        printf("Element not found");
        return -1;
    }
    else
        return 0;
}