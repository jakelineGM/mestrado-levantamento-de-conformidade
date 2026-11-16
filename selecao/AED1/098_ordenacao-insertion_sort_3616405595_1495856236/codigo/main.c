#include <stdio.h>
#include <stdlib.h>

void imprime(int *vetor, int tam){
  printf("{");
  
  for(int i = 0; i < tam; i++){
    printf("%d", vetor[i]);
  
    if( i < tam - 1){
      printf(", ");
    }
  }   
  printf("}\n");
}

void insertion(int *vetor, int tam){

  imprime(vetor, tam);

  for(int i = 1; i < tam; i++){
    int chave = vetor[i];
    int j = i - 1;

    while( j >= 0 && vetor[j] > chave){
      if(vetor [j + 1] != vetor[j]){

        vetor [j + 1] = vetor[j];
        imprime(vetor, tam);
      } 
      else{
        vetor [j + 1] = vetor[j];
      }
      j--;
    }
     
    if(vetor [j + 1] != chave){
    
      vetor [j + 1] = chave;    
      imprime(vetor, tam);
  
    }
  }
}

int main(){
  int tam;
  scanf("%d", &tam);

  int *vetor = malloc(tam * sizeof(int));

  for(int i = 0; i < tam; i++){
    scanf("%d", &vetor[i]);
  }

  insertion(vetor, tam);
  free(vetor);
  return 0;
}