#include <stdio.h>

// BEGIN

unsigned cont = 0;
unsigned buscaBinaria(int vet[], unsigned size, int chave){
  for(int x = 0; x < size;x++){
      if(vet[x] == chave){
        cont++;
      }
  }
  if(cont > 1){
    return 0;
  }
  else{
    return 1;
  }
  
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