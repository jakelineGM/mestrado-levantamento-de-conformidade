#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct dados {
    char nome[20];
    char endereco[40];
    int id;
} tipoDados;

void merge(tipoDados v[], tipoDados vaux[], int inicio,int meio, int fim){
  int a = inicio, b= meio+1, c=inicio; 
  while((a<=meio) && (b<=fim)){
    if(strcmp(v[a].nome,v[b].nome)<0){vaux[c] = v[a]; a++;}
    else{vaux[c] = v[b]; b++;}
    c++;
  }
  while(a<=meio){vaux[c]=v[a]; a++; c++;}
  while(b<=fim){vaux[c]=v[b]; b++; c++;}

  for(int a= inicio; a<=fim; a++){v[a] = vaux[a];}
}

void mergeSortI(tipoDados v[],tipoDados vaux[], int inicio, int fim){
  if(inicio<fim){
    int meio = (inicio + fim)/2;
    mergeSortI(v,vaux,inicio,meio);
    mergeSortI(v,vaux,meio+1,fim);
    merge(v,vaux,inicio,meio,fim);
  }
  
}

void mergeSortNome(tipoDados v[], int tam){
  tipoDados* vaux = (tipoDados*)malloc(sizeof(tipoDados)*tam);
   mergeSortI(v,vaux,0,tam-1);
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