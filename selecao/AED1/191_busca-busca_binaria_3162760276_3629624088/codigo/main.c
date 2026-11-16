#include <stdio.h>

int buscaBinaria(int *v, int size, int chave){
  int inicio =0;
  int fim = size-1;

  while(inicio<= fim){
    int meio= inicio+ (fim- inicio)/2;

    if(v[meio] == chave){
      return 1;
    }
    else if(v[meio]< chave){
      inicio = meio+1;
      
    }
    else{
      fim = meio -1;
    }
    }
  
  return 0;
}

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