#include <stdio.h>

// BEGIN
void binSearch(int vet[], int tam, int valor){
  int inicio, meio, fim;
  int iguais = 0;

  inicio = 0;
  fim = tam-1;

  while (inicio <= fim && iguais == 0){
    meio = (inicio + fim)/2;
    if (valor > vet[meio]){
      inicio = meio+1;
    }
    else if (valor < vet[meio]){
      fim = meio-1;
    }
    else{
      iguais = 1;
    }
    
    printf ("%d ", vet[meio]);
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