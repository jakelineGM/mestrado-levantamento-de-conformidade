#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct dados {
    char nome[20];
    char endereco[40];
    int id;
} tipoDados;

void insercao(tipoDados vetor[], int inicio, int fim){
  int i, j;
  tipoDados pivot;

  for(i=inicio+1; i<=fim; i++){
    pivot = vetor[i];
    j = i-1;
    while((j >= 0) && (vetor[j].id > pivot.id)){
      vetor[j+1] = vetor[j];
      j--;
    }
    vetor[j+1] = pivot;
  }
}

void quickSort(tipoDados vetor[], int inicio, int fim){
  if(inicio < fim){
    if(fim - inicio + 1 < 10){
      insercao(vetor, inicio, fim);
      return;
    }
    tipoDados pivot = vetor[fim];
    int i = inicio-1;

    for(int j=inicio; j<fim; j++){
      if(vetor[j].id <= pivot.id){
        i++;
        tipoDados temp = vetor[i];
        vetor[i] = vetor[j];
        vetor[j] = temp;
      }
    }
    tipoDados temp = vetor[i+1];
    vetor[i+1] = vetor[fim];
    vetor[fim] = temp;

    int p = i+1;

    quickSort(vetor, inicio, p-1);
    quickSort(vetor, p+1, fim);
  }
}

void quickSortID(tipoDados vetor[], int n){
  quickSort(vetor, 0, n-1);
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