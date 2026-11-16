#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct dados {
    char nome[20];
    char endereco[40];
    int id;
} tipoDados;

void merge(tipoDados v[], tipoDados aux[], int inicio, int meio, int fim){
  int i = inicio, j = meio+1, k = inicio;
  while((i<=meio) && (j<=fim)){
    if(strcmp(v[i].nome, v[j].nome) < 0){
      aux[k] = v[i];
      i++;
    }else {
      aux[k] = v[j];
      j++;
    }

    k++;
  }

  while(i<=meio){
    aux[k] = v[i];
    i++;
    k++;
  }

  while(j<=fim){
    aux[k] = v[j];
    j++;
    k++;
  }

  for(int x = inicio; x<=fim; x++){v[x] = aux[x];}
}

void mergeSort(tipoDados v[], tipoDados aux[], int inicio, int fim){
  
  if(inicio < fim){
    int meio = (inicio+fim)/2;
    mergeSort(v, aux, inicio, meio);
    mergeSort(v, aux, meio+1, fim);
    merge(v, aux, inicio, meio, fim);
  }
}

void mergeSortNome(tipoDados v[], int tam){
  tipoDados*aux = (tipoDados*)malloc(sizeof(tipoDados)*tam);
  mergeSort(v, aux, 0, tam-1);
  free(aux);
}




int main() {
    int n;
    scanf("%d", &n);
    tipoDados vetor[n];

    for (int i = 0; i < n; i++) {
        scanf(" %[^;]; %[^;]; %d", vetor[i].nome, vetor[i].endereco, &vetor[i].id);
    }

    mergeSortNome(vetor, n);

    for (int i = 0; i < n; i++) {
        printf("%s; %s; %d\n", vetor[i].nome, vetor[i].endereco, vetor[i].id);
    }
}