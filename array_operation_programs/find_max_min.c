//find the max and min in an array

#include<stdio.h>
#include<ctype.h>


int main()
{
    int arr[] = {9,10,4,6,8,4,2,1,0};

    int min;
    int max;

    int len = sizeof(arr) / sizeof(int);
    if(len == 0)
    {
        printf("Empty Array");
        return -1;
    }


    for(int i = 0; i< len; i++)
    {
        if(i == 0)
        {
            min = arr[i];
            max = arr[i];
        }
        else
        {
            if(arr[i]>max)
            {
                max = arr[i];
            }

            if(arr[i]<min)
            {
                min = arr[i];
            }
        }
    }

    printf("Min:%d \nMax:%d",min,max);

    return 0;
}
