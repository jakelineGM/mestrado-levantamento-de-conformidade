#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct dados {
    char nome[20];
    char endereco[40];
    int id;
} tipoDados;

void mergeSortNomeR(tipoDados v[], tipoDados aux[], int inicio, int fim) {
  int meio = (inicio + fim) / 2;
  int i = inicio, j = meio + 1;
  
  if(inicio < fim) {
    mergeSortNomeR(v, aux, inicio, meio);
    mergeSortNomeR(v, aux, meio + 1, fim);
    
    int k = inicio;
    while(i <= meio && j <= fim) {
      if(strcmp(v[i].nome, v[j].nome) < 0) {
        aux[k] = v[i];
        i++;
      } else {
        aux[k] = v[j];
        j++;
      }
      k++;
    }
  
    while(i <= meio) {
      aux[k] = v[i];
      i++;
      k++;
    }
    while(j <= fim) {
      aux[k] = v[j];
      j++;
      k++;
    }
    
    for(k = inicio; k <= fim; k++) {
      v[k] = aux[k];
    }
  }
  
}

void mergeSortNome(tipoDados vetor[], int tam) {
  tipoDados *aux;
  aux = (tipoDados*) malloc(sizeof(tipoDados) * tam);
  mergeSortNomeR(vetor, aux, 0, tam - 1);

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