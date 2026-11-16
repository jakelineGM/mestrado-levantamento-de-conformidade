#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct dados {
    char nome[20];
    char endereco[40];
    int id;
} tipoDados;

void mergeSortNome(tipoDados v[],tipoDados vaux[], int n, int inicio, int fim){
  int meio, i, j, k, tam = n;
  if(inicio < fim){
    i = inicio;
    k = inicio;
    meio = (inicio + fim)/2;
    j = meio + 1;
    mergeSortNome(v, vaux,tam, inicio, meio);
    mergeSortNome(v,vaux,tam,meio + 1,fim);

    while((i<=meio)&&(j<=fim)){
      if(strcmp(v[i].nome, v[j].nome) < 0){vaux[k] = v[i]; i++;}
      else{vaux[k] = v[j]; j++;}
      k++;
    }
    while(i<=meio){vaux[k] = v[i]; i++;k++;}
    while(j<=fim){vaux[k] = v[j];j++;k++;}

    for(k = inicio;k<=fim;k++){v[k] = vaux[k];}
  }

  
}







int main() {
    int n;
    scanf("%d", &n);
    tipoDados v2[n];
    tipoDados vetor[n];

    for (int i = 0; i < n; i++) {
        scanf(" %[^;]; %[^;]; %d", vetor[i].nome, vetor[i].endereco, &vetor[i].id);
    }

    mergeSortNome(vetor,v2, n, 0, n -1);

    for (int i = 0; i < n; i++) {
        printf("%s; %s; %d\n", vetor[i].nome, vetor[i].endereco, vetor[i].id);
    }
}