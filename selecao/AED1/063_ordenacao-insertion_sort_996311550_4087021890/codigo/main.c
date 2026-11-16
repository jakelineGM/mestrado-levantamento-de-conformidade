// PARTE A MODIFICAR
// INICIOFUNCAOALUNO
// ESCREVA NESSA ÁREA  A FUNCAO questao07 que deve atender ao enunciado do exercício. 


//BEGINFUNCAOALUNO
void  questao06(int *vet, int tamanho){
  int i=1;

  while(i<tamanho){
    int pivot = vet[i];
    int j= i-1;
  

while(j>=0 && vet[j]<pivot){
  vet[j+1] = vet[j];
  j--;
}
vet[j+1] = pivot;
  i++;

  
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