#include<stdio.h>
#include<stdlib.h>

//using char* method for string
int main()
{
      char *word = NULL; //creating a pointer

      word = malloc(6*sizeof(char)); //pointing a pointer to some memory location . 5 char +  '\0'

      if(word==NULL)
      {
        return -1;
      }

      printf("Enter input word: ");
      scanf("%5s",word); //can get only 5 char, saves the crash.

      int length = 0;
      while(*word !='\0') //*word means the actual word string, word means the address of 1st letter
      {
        length = length +1 ;
        word++;
      }

      printf("Length: %d\n",length);

      return 0;


}