#include <stdio.h>

int buscaBinaria(int v[], int tam, int num){
  int i, j, meio, contador;
  i = 0;
  j = tam -1;
  contador = 0;
  while(i <= j){
    meio = i + (j - i)/2;
    if(v[meio] == num){
        contador++;
    }
    if (v[meio] < num){
      i = meio + 1;
    }
    else{
      j = meio - 1;
    }
  }
  if (contador == 1){
    return 1;
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