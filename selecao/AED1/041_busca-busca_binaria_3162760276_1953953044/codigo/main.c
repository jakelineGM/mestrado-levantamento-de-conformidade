#include <stdio.h>

// BEGIN
int buscaBinaria(int vet[],unsigned tam,int chave){
int n;
int z;
int a;
z = tam -1;
a = 0;
int meio;
meio = tam/2;
int cont;
cont = 0;
for (n=0;n<tam;n++){
  if (vet[n]==chave){
    cont ++;
  }
  if (chave > meio){
    vet[a] = meio +1;
  }
  if (chave < meio){
    vet[z] = meio - 1;
  }
}
  if (cont != 1){
    return 0;
  }
  return 1;
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