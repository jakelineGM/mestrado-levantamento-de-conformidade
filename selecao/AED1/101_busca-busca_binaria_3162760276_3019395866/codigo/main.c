#include <stdio.h>

// BEGIN
int buscaBinaria(int vet[],int tam,int chave){
  int inicio=0,fim=tam;
  int meio;
  while(inicio<=fim){
    meio=(inicio+fim)/2;
    if(chave>vet[meio]){
      inicio=meio+1;
    }else if(chave<vet[meio]){
      fim=meio-1;
    }else{
      return 1;
    }
  }
  return 0;
}
// END

void ler(int *v, int size) {
  for (int i = 0; i < size; i++)
    scanf("%d%*c", &v[i]);
}

int main() {
  int chave;
  int size;
  scanf("%d%*c",&chave);
  scanf("%u%*c",&size); // tamanho do vetor
  int vet[size];
  ler(vet,size);
  if (buscaBinaria(vet, size, chave)) {
    printf("SIM");
  } else {
    printf("NAO");
  }
}