//insert at specific position
//[1,2,3,5,..]
//input = 2
// [1,"2",2,3,4...]
#include<stdio.h>
#include<ctype.h>

#define SIZE 11
int main(){
    int arr[SIZE] = {1,21,13,64,-5,9,10,11,7,-6,};

    int num;
    int index;
    printf("Enter an Number:");
    scanf("%d",&num);
    printf("Enter the index:");
    scanf("%d",&index);

    if(arr[SIZE-1]!=0)
    {
        printf("Array is full\n");
        return -1;
    }
    else
    {
        
        int temp;
        int paste = num;

        printf("Original Array:");
        for(int i=0;i<SIZE;i++)
        {
            printf("%d,",arr[i]);
        }

        for(int i=index;i<SIZE; i++)
        {
            

            temp = arr[i];
            arr[i] = paste;
            paste = temp;
        }

        
        printf("\nArray after inseted:");
        for(int i = 0;i<SIZE ; i++)
        {
            printf("%d,",arr[i]);

        }

        return 0;
    }


}