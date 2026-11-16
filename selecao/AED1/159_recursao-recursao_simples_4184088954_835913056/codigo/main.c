#include <stdio.h>

int calcula_mdc(int a, int b) {

  int resposta;
  
  if (b == 0) {
    resposta = a;
  } else {
    resposta = calcula_mdc(b, a % b);
    }
  return resposta;
}

int main(void) {

  int a, b, resultado;

  while (scanf("%d %d", &a, &b) && (a != 0 || b != 0)) {
    resultado = calcula_mdc(a, b);
    printf("%d\n",resultado);
  }
}