#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct dados {
    char nome[20];
    char endereco[40];
    int id;
} tipoDados;


void quicksort (tipoDados v[], int inicio, int fim){
  int i=inicio,j=fim, pivo=v[(inicio+fim)/2].id;
  while(i<=j){
    while(v[i].id<pivo){
      i++;
    }
    while(v[j].id>pivo){
      j--;
    }
    if(i<=j){
      tipoDados temp=v[i];
      v[i]=v[j];
      v[j]=temp;
      i++;
      j--;
    }
  }
  if(inicio<j){
    quicksort(v,inicio,j);
  }
  if(i<fim){
    quicksort(v,i,fim);
  }
}

void quickSortID(tipoDados v[],int tam){
  quicksort(v,0,tam-1);
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