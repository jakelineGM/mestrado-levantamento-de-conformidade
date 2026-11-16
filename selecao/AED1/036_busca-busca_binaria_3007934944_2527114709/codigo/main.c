#include <stdio.h>

// BEGIN
void binSearch(int v[], int vSize, int value){
  int inicio, meio, fim;
  inicio = 0;
  fim = vSize - 1;
  while(inicio <= fim){
    meio = (inicio+fim)/2;
    printf("%d", v[meio]);
    if (value > v[meio]){
      inicio = meio+1;
    }
    else if (value < v[meio]){
      fim = meio - 1;
    }
    else {
      printf("\n");
      return;
    }

    if(inicio <= fim){
      printf(" ");
    }
  }
  printf("\n");
}

// END

int main() {
  int vet[] = {3,12,20,25,40,50,55,90,95,99};
  int vSize = sizeof(vet) / sizeof(vet[0]);
  int value;
 
  if(scanf("%d", &value) == 1){
     binSearch(vet, vSize, value);
  }
  return 0;
}