#include <stdio.h>

// BEGIN
void binSearch(int vet[], int vSize, int key){
  int inicio = 0;
  int fim = vSize - 1;

  while(inicio <= fim){
    int meio = (inicio+fim)/2;

    if(key < vet[meio]){
      printf("%d ", vet[meio]);
      fim = meio - 1;
    }
    else if(key > vet[meio]){
      printf("%d ", vet[meio]);
      inicio = meio + 1;
    }
    else{
      printf("%d ", vet[meio]);
      fim = 0;
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