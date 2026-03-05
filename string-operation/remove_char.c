#include<stdio.h>
#include<string.h>

char* remove_char(char* word,int pos);

char* remove_char(char* word,int pos)
{
    int len = strlen(word);

    //"HELLO"
    for(int i=pos; i<len;i++)
    {
        
        word[i]=word[i+1];
    }

    return word;
}

int main()
{
    char word[] = "Hello";
    int pos = 2;

    printf("%s", remove_char(word,pos));

    return 0;
}