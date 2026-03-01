#include<stdio.h>
#include<stdlib.h>
//so basically we define the total num of char that can enter by the user
#define MAX_CHAR 30

int main()
{
    char* str = NULL;
    char ch;
    str = malloc(MAX_CHAR*sizeof(char));
    if(str==NULL)
    {
        printf("Memory is not allocated.  :(");
        return -1;
    }

    //getting input
    printf("enter the string(<=29):");
    scanf("%29s",str);

    printf("enter the char to search:");
    scanf(" %c",&ch);

    //index will be 0,.. in for the 1st element
    int index = 0;
    //iterating through ..all the element by *str, which means '<char>', simply str points to the memory location
    while(*str != '\0')
    {
        if(*str == ch)
        {
            printf("At index: %d",index);
            return 0;
        }
        index++;
        str++;
    }
    
    printf("-1");
    return -1;
}

