#include<stdio.h>
int multiply(int a,int b);

int main()
{
    printf("multiply(10*20):%d",multiply(20,10));
}

int multiply(int a,int b)
{   
    //add a for b-times
    //base case 
    if(b == 1)
    {
        return a;
    }

    //recursive case
    return (a + multiply(a,b-1)); ///loop: a + a*b-1
}