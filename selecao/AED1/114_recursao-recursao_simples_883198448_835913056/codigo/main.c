#include <stdio.h> 

int recursiva(int numero, int quantRecursao) {

  int resposta;

  if (numero <= 0) {
    resposta = 1;
  } else {
    resposta = numero * recursiva(numero - quantRecursao, quantRecursao);
  }
return resposta;
}

int main(void) {
  int numero, quantRecursao, resultado, contador;
  scanf("%d %d", &numero, &quantRecursao);
  while (numero !=0 || quantRecursao !=0) {
    resultado = recursiva(numero, quantRecursao);
    printf("%d", numero);

    for (contador = 0; contador < quantRecursao; contador++) {
      printf("!");
    }
    printf(" = %d\n",resultado);
    scanf("%d %d", &numero, &quantRecursao);
  }  
}