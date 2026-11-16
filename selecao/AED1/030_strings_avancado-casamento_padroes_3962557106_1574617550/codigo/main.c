#include <stdio.h>

int compara(char sub[], char string[]) {

  int posS = 0;
  int posZ = 0;

  while ((string[posS] != 0) && (sub[posZ] != 0)) {

    if(string[posS] == sub[posZ]) {
    posZ++;
    } else {

      posZ = 0;
      
    }
    
  posS++;
  }

  if(sub[posZ] == 0) {

    return 1;
    
  } else {

    return 0;
    
  }
  
}

int main(void) {

  char string[201];
  char sub[201];
  int comparacao = 0;

  while(scanf("%s", sub), sub[0] != 'F'){
    
    scanf("%s", string);
  
    comparacao = compara(sub, string);
  
    if(comparacao == 1) {
  
      printf("SIM\n");
      
    } else {
  
      printf("NAO\n");
      
    }
  }
  
}