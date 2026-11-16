#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int verifica_substring(char *substring, char*string){
  int contsub=0, i=0;

  while((substring[contsub] != 0) && (string[i] != 0)){
    if(string[i] == substring[contsub]){
      contsub++;
    }else{
      contsub=0;
    }
    i++;
  }
  
  return (substring[contsub] == 0);
}

int main(void){
  char s[201], z[201];

  while(scanf("%s%s", s, z), s[0] != 'F'){
    if(verifica_substring(s,z) == 1)
      printf("SIM\n");
    else
      printf("NAO\n");
  }
}