#include <stdio.h>

int ehSubstring(char *stringInteresse, char *string){
  int i = 0;
  while (string[i] != 0){
  int j = 0;
    while ((stringInteresse[j] != 0) && ((string[i+j]) == stringInteresse[j])){
      j++;
    }
    if(stringInteresse[j] == 0){
      return 1;
    }
        i++;
  }
  return 0;
}
int main(void){
  char stringInteresse[202];
  char string[202];

  while((scanf("%s", stringInteresse)) != (stringInteresse[0] == 'F')){
    scanf("%s", string);
    if(ehSubstring(stringInteresse, string)){
      printf("SIM\n");
    } else printf("NAO\n");
  }
  return 0;
}