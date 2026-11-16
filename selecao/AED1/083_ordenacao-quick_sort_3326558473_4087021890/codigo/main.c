#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define limiarInsercao 10

typedef struct dados {
    char nome[20];
    char endereco[40];
    int id;
} tipoDados;
void insertionSort(tipoDados vt[], int inicio, int fim){
int i,j;
  tipoDados pivot;

  for(i= inicio+1;i<=fim;i++ ){
    pivot = vt[i];
    j= i-1;

    while(j>=inicio && strcmp(vt[j].nome, pivot.nome)>0){
      vt[j+1]= vt[j];
      j--;
    }
    vt[j+1] = pivot;
  }
  
}

void quickSortNome(tipoDados vt[], int inicio, int fim){
int i,j;
tipoDados pivot;
  tipoDados tmp;

if((fim-inicio +1)<limiarInsercao){
  insertionSort(vt, inicio, fim);
  return;
}
  
i= inicio;
j= fim;
  pivot = vt[(inicio+fim)/2];
    while(i<=j){
while(strcmp(vt[i].nome,pivot.nome)<0 && i<fim)i++;
while(strcmp(vt[j].nome,pivot.nome)>0 && j>inicio)j--;

      if(j>=i){
     tmp=vt[i];
     vt[i]=vt[j];
        vt[j]= tmp;
        i++;
        j--;
        
        
      }
    }
    
     quickSortNome(vt, inicio, j);
    
  if(i<fim){
      
   quickSortNome(vt,i,fim);
  
  }

}
  


int main() {
    int n;
    scanf("%d", &n);
    tipoDados vetor[n];

    for (int i = 0; i < n; i++) {
        scanf(" %[^;]; %[^;]; %d", vetor[i].nome, vetor[i].endereco, &vetor[i].id);
    }

    quickSortNome(vetor,0, n-1);

    for (int i = 0; i < n; i++) {
        printf("%s; %s; %d\n", vetor[i].nome, vetor[i].endereco, vetor[i].id);
    }
}