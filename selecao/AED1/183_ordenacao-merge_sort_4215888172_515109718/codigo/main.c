#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct dados {
    char nome[20];
    char endereco[40];
    int id;
} tipoDados;

void mergeSortR(tipoDados vetor[], tipoDados aux[], int inicio, int fim){
  int a, b, k;
  if(inicio < fim){
    int meio = (inicio + fim)/2;
    mergeSortR(vetor, aux, inicio, meio);
    mergeSortR(vetor, aux, meio+1, fim);

    a = inicio; b = meio + 1; k = inicio;
    while((a<=meio)&&(b<=fim)){
      if(strcmp(vetor[a].nome,vetor[b].nome)<0){
        aux[k] = vetor[a];
        a++;
      }
      else{
        aux[k] = vetor[b];
        b++;
      } 
      k++;
    }
    while(a<=meio){
      aux[k] = vetor[a];
      a++; k++;
    }
    while(b<=fim){
      aux[k] = vetor[b];
      b++; k++;
    }
    for(k = inicio; k <= fim; k++){
      vetor[k] = aux[k];
    }
  }  
}
void mergeSortNome(tipoDados vet[], int tam){
  tipoDados *aux;
  aux = (tipoDados*) malloc (sizeof(tipoDados)*tam);
  mergeSortR(vet, aux, 0, tam-1);
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