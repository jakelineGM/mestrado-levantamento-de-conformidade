#include <stdio.h>

// BEGIN
char buscaBinaria (int vet[],int tamvet, int chave){
int ini = 0;
int fim = tamvet-1;
int meio;
while(ini <= fim){
meio = (ini+fim)/2;
if(chave > vet[meio]){
  ini = meio +1;
}else if(chave < vet[meio]){
  fim = meio-1;
}else{
if(chave != vet[meio +1] && chave != vet[meio-1]){
  return 1;
}
return 0;
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
  scanf("%u%*c",&size);
  int vet[size];
  ler(vet,size);
  if (buscaBinaria(vet, size, chave)) {
    printf("SIM");
  } else {
    printf("NAO");
  }
}