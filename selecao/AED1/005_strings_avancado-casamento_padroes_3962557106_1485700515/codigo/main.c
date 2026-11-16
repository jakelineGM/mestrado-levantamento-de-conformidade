#include <stdio.h>

int eh_substring(char s[], char z[]){

  int i = 0;
  int encontrou = 0;

  while(z[i] != 0 && encontrou == 0){
    int j = 0;
    while(s[j] != 0 && (z[i + j] == s[j])){
      j++;
    }
    if(s[j] == 0){
      encontrou = 1;
    }
    i++;
  }
  return encontrou;
}

int main(void){
  char s[201];
  char z[201];
  int continuar = 1;

  while(continuar){
    scanf("%s", s);

    if(s [0] == 'F'){
      continuar = 0;
    }else{
      scanf("%s", z);
      if(eh_substring(s, z)){
        printf("SIM\n");
      }else{
       printf("NAO\n");
      }
    }
  }
  return 0;
}