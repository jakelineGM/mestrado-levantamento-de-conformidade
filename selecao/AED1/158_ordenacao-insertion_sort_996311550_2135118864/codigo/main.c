// PARTE A MODIFICAR
// INICIOFUNCAOALUNO
// ESCREVA NESSA ÁREA  A FUNCAO questao06 que deve atender ao enunciado do exercício. 

//BEGINFUNCAOALUNO
void questao06 (int v[], unsigned tam) {
  int i = tam-1, j;
  while(i > 0) {
    j = i;
    while( (j < tam) && (v[j] > v[j-1]) ) {
      int temp = v[j];
      v[j] = v[j-1];
      v[j-1] = temp;
      j++;
    }
    i--;
  }
}
//ENDFUNCAOALUNO


// ABAIXO CODIGO USADO PARA TESTE DA FUNCAO. NÃO MOFIQUE!

#include <stdio.h>
#include <stdlib.h>

// mostra dados de um vetor

void mostraVetor(int vet[], unsigned n) {
  unsigned x;

  for(x = 0; x< n; x++) {
    printf("%d ",vet[x]);
  }
  printf("\n");
}

int main() {
   unsigned tamVetor;
   unsigned x;

   scanf("%u%*c",&tamVetor);
   int *vet = (int*) malloc(sizeof(int)*tamVetor);

   for(x = 0; x< tamVetor; x++) {
     scanf("%d%*c",&vet[x]);
   } 
   questao06(vet,tamVetor);
   mostraVetor(vet,tamVetor);
   free(vet);
}