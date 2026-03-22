#include<stdio.h>

int main()
{
    int arr1[3][3] = {
        {1,2,3},
        {4,5,6},
        {7,8,9}
    };
    
    int arr2[3][3] = {
        {9,10,10},
        {0,1,2},
        {5,6,9}
    };

    int size = sizeof(arr1)/sizeof(arr1[0]);
    int size2 = sizeof(arr1[0])/sizeof(arr1[0][0]);
    int arr3[3][3];


    for(int i=0; i<size;i++)
    {
        for(int j=0; j<size2; j++){
            arr3[i][j] = arr1[i][j] + arr2[i][j];
            printf("%d,",arr3[i][j]);
    }

        printf("\n");

    }

    
    return 0;


}