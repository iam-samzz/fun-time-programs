#include<stdio.h>

int main(){
    
    int arr[10];

    int size = sizeof(arr) / sizeof(arr[0]);

    printf("Enter the elements:");
    for(int i = 0 ; i<10; i++){
        scanf("%d,",&arr[i]);
    }

    for(int i = 0;i< 10; i++)
    {
        printf("Element at index %d: %d .",i,arr[i]);
    }

    return 0;
}