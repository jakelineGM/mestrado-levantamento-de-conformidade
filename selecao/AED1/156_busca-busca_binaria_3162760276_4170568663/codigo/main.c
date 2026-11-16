#include <stdio.h>

// BEGIN
char buscaBinaria(int v[], int size, int chave){
  unsigned i,j, meio;
  i=0;
  j=size-1;

  while(i<=j){
    meio=(i+j)/2;
    if(chave > v[meio]){
      i = meio+1;
    }else if(chave< v[meio]){
      j = meio-1;
    }else{
      if(v[meio+1] == chave || v[meio-1] == chave){
        return 0;
      }else {
        return 1;
      }
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