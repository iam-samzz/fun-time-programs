#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAX_CHAR 30
int main()
{
    char *s1 = NULL;
    char *s2 = NULL;

    s1 = malloc(MAX_CHAR*sizeof(char));
    s2 = malloc(MAX_CHAR* sizeof(char));

    //getting input

    printf("Enter  s1:");
    scanf("%29s",s1); // The 'MAX_CHAR-1' ensures that even if the user types more, 
                                // only the first MAX_CHAR (+ plus the null terminator) are stored in s1.

    printf("Enter s2:");
    scanf("%29s",s2);

    if(strcmp(s1,s2) == 0)
        printf("Yes");
    else
        printf("No");

    return 0;


}