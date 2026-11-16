#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct dados {
    char nome[20];
    char endereco[40];
    int id;
} tipoDados;

void merge(tipoDados v[], int inicio, int meio, int fim) {
  int i, j, k;
  int n1 = meio - inicio + 1;
  int n2 = fim - meio;

  tipoDados *L = (tipoDados *)malloc(n1 * sizeof(tipoDados));
  tipoDados *R = (tipoDados *)malloc(n2 * sizeof(tipoDados));

  for (i = 0; i < n1; i++)
      L[i] = v[inicio + i];
  for (j = 0; j < n2; j++)
      R[j] = v[meio + 1 + j];

    
  i = 0;
  j = 0;
  k = inicio;

  while (i < n1 && j < n2) {
      if (strcmp(L[i].nome, R[j].nome) <= 0) {
          v[k] = L[i];
          i++;
      } else {
          v[k] = R[j];
          j++;
      }
      k++;
  }

  while (i < n1) {
      v[k] = L[i];
      i++;
      k++;
  }

  while (j < n2) {
      v[k] = R[j];
      j++;
      k++;
  }

  free(L);
  free(R); 
}

void mergeSortRecursivo(tipoDados v[], int fim) {
  if(inicio < fim) {
    int meio = inicio + (fim - inicio) / 2;
  
    mergeSortRecursivo(v, inicio, meio);
    mergeSortRecursivo(v, meio + 1, fim);
  
    merge(v, inicio, meio, fim);
  }
}

void mergeSortNome(tipoDados v[], int n) {
  if(n > 1) mergeSortRecursivo(v, 0, n-1);
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