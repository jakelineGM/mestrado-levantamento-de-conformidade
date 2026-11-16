#include <stdio.h>

int paridade (int numero) {

  int resposta;

  if (numero == 0) {
      resposta = 1;
    } else {
      resposta = !paridade(numero - 1);
      }
  return resposta;
}

int main (void) {

  int numero;

  while (scanf("%d", &numero) && numero >= 0) {
    if (paridade(numero)) {
      printf("%d eh par\n", numero);
    } else {
      printf("%d eh impar\n", numero);
      }
  }
}