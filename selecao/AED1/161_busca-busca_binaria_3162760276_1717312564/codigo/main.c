#include <stdio.h>

// BEGIN
int buscaBinaria(int *vet, int size, int chave){
  int in = 0, fim = size-1, meio;
  int prim = -1, ult = -1;

  while(in <= fim){
    meio =(in+fim)/2;
    if(vet[meio]==chave){
      prim = meio;
      fim = meio - 1;
   
    }else if(vet[meio] < chave){
      in = meio + 1;
    }else{
      fim = meio - 1;
    }
  }
  if(prim == -1){
    return 0;
  }
  in = 0; 
  fim = size - 1;

  while (in <= fim){
    meio = (in+fim)/2;
    if(vet[meio] == chave){
      ult = meio;
      in = meio + 1;
      
    }else if(vet[meio]<chave){
      in = meio + 1;
      
    }else{
      fim = meio - 1;
      
    }
  }
  return prim == ult;
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
  scanf("%u%*c",&size);
  int vet[size];
  ler(vet,size);
  if (buscaBinaria(vet, size, chave)) {
    printf("SIM");
  } else {
    printf("NAO");
  }
}