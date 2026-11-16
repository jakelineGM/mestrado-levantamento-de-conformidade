#include <stdio.h>
#include <stdlib.h>

typedef struct lista{

  int capacidade;
  int tamanho;
  int *elementos;

} lst;

void remover(lst *lista, int num) {

  int pos = 0;
  
  while(lista->elementos[pos] != num){
    pos++;
  }

  for(int i = pos; i < lista->tamanho; i ++){
    lista->elementos[i] = lista->elementos[i+1];    
  }

  lista->tamanho--;
  
}

void inserir(lst *lista, int num){

  if(lista->tamanho == lista->capacidade){

    lista->capacidade *= 2;
    int *temp = realloc(lista->elementos, lista->capacidade);
    lista->elementos = temp;
    
  }
  
  lista->elementos[lista->tamanho] = num;
  lista->tamanho++;
  
}

lst *criar(int capacidade){

  lst *lista = malloc(sizeof(*lista));
  lista->capacidade = capacidade;
  lista->tamanho = 0;
  lista->elementos = malloc(capacidade * (sizeof *(lista->elementos)));

  return lista;

}

void liberar(lst *lista) {

    free(lista->elementos);
    free(lista);
  
}

void imprimeLista(lst *lista){

  printf("{");
  
  for(int i = 0; i < lista->tamanho - 1; i++){
    printf("%d, ", lista->elementos[i]);
  }
  printf("%d}\n", lista->elementos[lista->tamanho - 1]);
  
}

void insertionSort(lst *lista){

  for(int i = 1; i < lista->tamanho; i++){

    int prox = lista->elementos[i];
    int j = i - 1;
    
    while(j >= 0 && lista->elementos[j] > prox){

      if(lista->elementos[j + 1] != lista->elementos[j]){
        lista->elementos[j + 1] = lista->elementos[j];
        imprimeLista(lista);
      } else {
        lista->elementos[j + 1] = lista->elementos[j];
      }
      
      j--;  
    }
    
    if(lista->elementos[j + 1] != prox){
      lista->elementos[j + 1] = prox;
      imprimeLista(lista);
    } else {
      lista->elementos[j + 1] = prox;
    }
    
  }
  
}

int main(void){

  int capacidade;
  scanf("%d", &capacidade);
  lst *lista = criar(capacidade);

  for(int i = 0; i < lista->capacidade; i++){
    int temp;
    scanf("%d", &temp);
    inserir(lista, temp);
  }

  imprimeLista(lista);
  insertionSort(lista);

  liberar(lista);
  
}