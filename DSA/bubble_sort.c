#include<stdio.h>

int main()
{
      int len = 9;
    int arr[9] = {9,5,8,1,0,85,85,4,11};

    int temp;
    for(int i=0 ; i<len; i++)
    {
        for(int j = 0;j<(len-1-i);j++)
        {
            if(arr[j]>arr[j+1])
            {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }

    for(int i=0;i<len;i++)
    {
        printf("%d,",arr[i]);
    }
}



