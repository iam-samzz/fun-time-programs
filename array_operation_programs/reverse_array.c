//get an array
/*
no.of element can we odd or even

logical_len = len -1
for i in range int(len/2):
    temp = array[i]]
    temp2 = array[logical_length-i]
    array[i] = temp2;
    array[logical_length-i] = temp
print reversed array
*/

#include<stdio.h>

int main()
{
    //reversed Array
    int arr[] = {1,2,3,4,5,6,7};



    int size = sizeof(arr)/sizeof(arr[0]);
    int logical_size = size - 1;
    int temp1;
    int temp2;

    if(size==0)
    {
        printf("Array is empty!");
        return -1;
    }
    for(int i=0;i < size/2; i++)
    {
        temp1 = arr[i];
        arr[i] = arr[logical_size - i];
        arr[logical_size-i] = temp1; 
    }

    printf("Reversed Arr: [");
    for(int i=0; i < size; i++)
    {
        if(i == size-1)
        {
            printf("%d",arr[i]);
            break;
        }
        else
        {
            printf("%d,",arr[i]);
        }
    }
    printf("]");
    return 0;
}





