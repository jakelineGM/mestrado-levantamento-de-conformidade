#include <stdio.h>

// BEGIN

// END

void ler(int *v, int size) {
  for (int i = 0; i < size; i++)
    scanf("%d%*c", &v[i]);
}

int buscaBinaria(int *v, int size, int chave){
  int left = 0, right = size - 1;
  int primeiro = -1, ultimo = -1;


  while(left <= right){
    int mid = (left + right) / 2;
    if(v[mid] == chave){
      primeiro = mid;
      right = mid - 1;
    } else if(v[mid] < chave){
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  if(primeiro == -1){
    return 0;
  }

  left = 0;
  right = size - 1;
  while(left <= right){
    int mid = (left + right) / 2;
    if(v[mid] == chave){
      ultimo = mid;
      left = mid + 1;
    } else if (v[mid] < chave){
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return primeiro == ultimo;
  
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