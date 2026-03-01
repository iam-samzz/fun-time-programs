#include<stdio.h>

int main()
{

        char * s = "hello";


        printf("%p\n",s); //address of pointer s, which is 1st letter 'h'
        printf("%s\n",s); //prints the whole string from 'h' to 'o'

        s = "world";

        printf("%p\n",s); 
        printf("%s\n",s); 

        char x[] = "Samaran";
        printf("%s\n",x);

        x[0] = 's';
        printf("%s\n",x);

        // x[] = "project"; -> this is not possible in x[] method of creating string in c

        return 0;


}