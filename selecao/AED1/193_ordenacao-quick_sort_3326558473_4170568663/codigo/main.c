#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct dados {
    char nome[20];
    char endereco[40];
    int id;
} tipoDados;


void qSort(tipoDados v[], int inicio, int fim){
  int i, j;
  tipoDados aux, meio;

  while(fim-inicio >= 10){
    i = inicio; j = fim;
    meio = v[(inicio+fim)/2];
    while(i<=j){
      while(strcmp(v[i].nome, meio.nome) < 0) i++;
      while(strcmp(v[j].nome, meio.nome) > 0) j--;
      if(i<=j){
        aux = v[j];
        v[j] = v[i];
        v[i] = aux;
        i++;
        j--;
      }
    }
    if(j-inicio > fim-i){ 
      qSort(v, i, fim);
      fim = j;
    }else{
      qSort(v, inicio, j);
      inicio = i;
    }
  }
}
void insertionSort(tipoDados v[], int inicio, int fim){
  int i, j;
  tipoDados pivo;
  i = 1;
  while(i<fim){
    j=i-1; pivo =  v[i];

    while(j>=0 && strcmp(pivo.nome, v[j].nome)<0){
      v[j+1] = v[j];
      j--;
    }
    v[j+1] = pivo;
    i++;
  }
}

void quickSortNome(tipoDados v[], int n){
  qSort(v, 0, n-1);
  insertionSort(v, 0, n);
}




int main() {
    int n;
    scanf("%d", &n);
    tipoDados vetor[n];

    for (int i = 0; i < n; i++) {
        scanf(" %[^;]; %[^;]; %d", vetor[i].nome, vetor[i].endereco, &vetor[i].id);
    }

    quickSortNome(vetor, n);

    for (int i = 0; i < n; i++) {
        printf("%s; %s; %d\n", vetor[i].nome, vetor[i].endereco, vetor[i].id);
    }
}