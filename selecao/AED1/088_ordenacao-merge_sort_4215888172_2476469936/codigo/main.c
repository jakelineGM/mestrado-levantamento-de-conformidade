#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct dados {
    char nome[20];
    char endereco[40];
    int id;
} tipoDados;

void intercala (tipoDados v[], tipoDados vaux[], int inicio, int meio, int fim) {
  int a = inicio;
  int b = meio + 1;
  int s = inicio;

  while ( (a<= meio) && (b <= fim)){
    if(strcmp(v[a].nome, v[b].nome) < 0) {
      vaux[s] = v[a];
      a++;
    } else {
      vaux[s] = v[b];
      b++;
    }
    s++;
  }

  while(a <= meio) {
    vaux[s] = v[a];
    a++;
    s++;
  }

  while(b <= fim) {
    vaux[s] = v[b];
    b++;
    s++;
  }

  for(a = inicio; a<=fim; a++){
    v[a] = vaux[a];
  }
}

void mergeSortI (tipoDados v[], tipoDados vaux[], int inicio, int fim) {
  int meio;

  if(inicio < fim) {
    meio = (inicio + fim)/2;
    mergeSortI(v, vaux, inicio, meio);
    mergeSortI(v, vaux, meio+1, fim);
    intercala(v, vaux, inicio, meio, fim);
  }
}

void mergeSortNome(tipoDados v[], int tam) {
  tipoDados *vaux;

  vaux = (tipoDados*) malloc(sizeof(tipoDados)*tam);
  mergeSortI(v, vaux, 0, tam - 1);
  free(vaux);
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