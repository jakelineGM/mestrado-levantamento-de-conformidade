#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct dados {
    char nome[20];
    char endereco[40];
    int id;
} tipoDados;


void quickSortID(tipoDados v[], int tam){
  void quickSort(tipoDados v[], int inicio, int fim){
  int i = inicio; int j = fim;
  int pivot = v[(i+j)/2].id;

  while(i<=j){
    while(v[i].id < pivot) i++;
    while(v[j].id > pivot) j--;

    if(i<=j){
      tipoDados temp = v[i];
      v[i] = v[j];
      v[j] = temp;

      i++;
      j--;
      }
    }

  if(inicio < j) quickSort(v, inicio, j);
  if(i < fim) quickSort(v, i, fim);

  }

 
  quickSort(v, 0, tam-1);
}



int main() {
    int n;
    scanf("%d", &n);
    tipoDados vetor[n];

    for (int i = 0; i < n; i++) {
        scanf(" %[^;]; %[^;]; %d", vetor[i].nome, vetor[i].endereco, &vetor[i].id);
    }

    quickSortID(vetor, n);

    for (int i = 0; i < n; i++) {
        printf("%s; %s; %d\n", vetor[i].nome, vetor[i].endereco, vetor[i].id);
    }
}