#include <stdio.h>

// BEGIN


void binSearch(int vet[],unsigned tamvet, int chave){
  int inicio;
  int meio;
  int fim;

  inicio = 0;
  fim = tamvet-1;

  while(inicio <= fim){
    meio = (inicio+fim)/2;
    printf("%d ",vet[meio]);

    if(chave < vet[meio]){
      fim = meio-1;
    }
    if(chave > vet[meio]){
      inicio = meio+1;
    }
    if(chave == vet[meio]){
      inicio = fim+1;
    }
  }
}
// END

int main() {
  int vet[] = {3,12,20,25,40,50,55,90,95,99};
  int vSize = sizeof(vet) / sizeof(vet[0]);
  int value;
  scanf("%d",&value);
  binSearch(vet,vSize, value);
}