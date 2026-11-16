#include <stdio.h>

void imprime_bin(int num){
  //int converter; 
  
  if (num < 2){
    printf("%d", num);
  }
  else{
    //converter = imprime_bin(num/ 2);
    imprime_bin(num/ 2);
    printf("%d", num%2);
  }
 //return converter;
}

int main(void){
  int num;

  scanf("%d", &num);

  imprime_bin(num);
}