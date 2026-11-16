#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct dados {
    char nome[20];
    char endereco[40];
    int id;
} tipoDados;

void insertSort(tipoDados v[], unsigned tamVetor){
  tipoDados pivot;
  int i,j;
  for(i = 1; i < tamVetor; i++){
    j = i-1;
    pivot = v[i];
  while (j >= 0 && strcmp(v[j].nome,pivot.nome)> 0){
    v[j+1] = v[j];
    j--;
    }
  v[j+1] = pivot;
  }
}

void qSortR(tipoDados v[], unsigned inicio, unsigned fim){
  tipoDados aux;
  tipoDados pivot;
  unsigned i, j, meio;
  while(fim-inicio > 10){
    i = inicio;
    j = fim;
    meio = (inicio+fim)/2;
    pivot = v[meio];
    while(i<=j){
      while(strcmp(v[i].nome,pivot.nome)< 0){i++;}
      while(strcmp(v[j].nome,pivot.nome)> 0){j--;}
    if (i<= j){
      aux = v[i];
      v[i] = v[j];
      v[j] = aux;
      i++;
      j--;
      }
    }
  if(inicio<j){qSortR(v, inicio, j);inicio = i;}
   else{qSortR(v,i,fim); fim = j;} 
  }
}

void quickSortNome(tipoDados v[], unsigned tamVetor){
  qSortR(v, 0, tamVetor-1);
  insertSort(v,tamVetor);
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