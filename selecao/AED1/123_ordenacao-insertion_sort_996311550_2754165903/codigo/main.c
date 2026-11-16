// PARTE A MODIFICAR
// INICIOFUNCAOALUNO
// ESCREVA NESSA ÁREA  A FUNCAO questao07 que deve atender ao enunciado do exercício. 

//BEGINFUNCAOALUNO
void questao06(int vet[], unsigned tamVetor){
  int i, j;
  int auxiliar;
  int maior;
  for(i=0;i<tamVetor;i++){
    j = i;
    maior = i;
    for(j=i;j<tamVetor;j++){
      if (vet[j] > vet[maior]) {
        maior = j;
      }
    }
    auxiliar = vet[maior];
    vet[maior] = vet[i];
    vet[i] = auxiliar;
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