//get an input
//get postion
//get char to be inserted


//we can do this by creating a new string or manipulting the current string

// ['h','e','l','l','o']


//char* h = hello;
//h = address of 'h'
//*h = 'h'


/*
get all 3 values:

func(arr):

    temp = NULL
    pos = given
    char = given

    for iterate through (from pos to last value) from i - n:
        temp = arr[i]
        arr[i] = char
        char = temp

        i++
    */


#include<stdio.h>
#include<string.h>

char* insert_func(char* arr,int pos,char ch);

char* insert_func(char* arr,int pos,char ch)
{
    int temp = 0;
    
    int len = strlen(arr);
    for(int i = pos; i<=len ;i++)
    {

        temp = arr[i];
        arr[i] = ch;
        ch = temp;

    }

    return arr;
}
int main()
{
    char arr[20] = "Hello";
    int pos;
    char ch;
    printf("Enter pos");
    scanf("%d",&pos);

    printf("Enter ch:");
    scanf(" %c",&ch);


    printf("%s",insert_func(arr,pos,ch));

}