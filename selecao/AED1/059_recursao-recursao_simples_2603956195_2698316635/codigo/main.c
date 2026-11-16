#include <stdio.h>
// representacao binaria
void imprime_bin(unsigned int num){
    if (num == 0){
        printf("0");
      return;
    }
    if (num > 1){
        imprime_bin(num / 2);
    }
  printf("%d", num % 2);
}

int main(){
    unsigned int num;
    scanf("%u", &num);
    imprime_bin(num);
    printf("\n");
    return 0;
}