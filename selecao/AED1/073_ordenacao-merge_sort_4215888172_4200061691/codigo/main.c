#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct dados {
    char nome[20];
    char endereco[40];
    int id;
} tipoDados;


void mergeSortNomeM(tipoDados v[], tipoDados vaux[], int inicio, int fim){
  int meio = (inicio+fim)/2;
//  printf("MergeSort");
  if(inicio < fim){
    mergeSortNomeM(v, vaux, inicio, meio);
    mergeSortNomeM(v, vaux, meio+1, fim);
    int i = inicio, j = meio+1, k = inicio;
while(i <= meio || j<=fim){
  if(i <= meio && j <= fim && strcmp(v[i].nome,v[j].nome) < 1){
    vaux[k] = v[i];
    i++;  k++;
  }
  else if(j <= fim){
    vaux[k] = v[j];
    j++;  k++;
  }
  else {vaux[k] = v[i];
       k++;    i++;
       }
}

for(k = 0; k <= fim; k++){
  v[k] = vaux[k];
}
  }
}

void mergeSortNome (tipoDados v[], int tam){
  int inicio = 0, fim = tam-1;
  tipoDados vaux[tam];
  if(inicio < fim){mergeSortNomeM(v,vaux,inicio,fim);}
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