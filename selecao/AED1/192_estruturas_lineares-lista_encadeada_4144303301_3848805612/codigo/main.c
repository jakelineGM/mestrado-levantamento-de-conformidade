#include <stdio.h>
#include <stdlib.h>

typedef struct NO{
  int valor;
  struct NO* proximo;
}No;

typedef struct Lista{
  No* inicio;

}Lista;

Lista* lst_cria(){

  Lista* novaLista = (Lista*) malloc(sizeof(Lista));
  novaLista->inicio = NULL;
  return novaLista;
}

void lst_insere(Lista* l, int valor){
  No* novo = (No*) malloc(sizeof(Lista));
  novo->valor = valor;
  novo->proximo = l->inicio;
  l->inicio = novo;
}

void lst_imprime(Lista* l){
  No* atual = l->inicio;
  while(atual != NULL){
    printf("%d ", atual->valor);
    atual = atual->proximo;
  }
}

Lista *concatena(Lista* l1, Lista* l2){

  No* atual = l1->inicio;
  if(atual == NULL){
    l1->inicio = l2->inicio;
    
  }else{
    while(atual->proximo != NULL){
      atual = atual->proximo;
    }
    atual->proximo = l2->inicio;
  }
  l2->inicio = NULL;
  return l1;
  
}

int main(void) {

  Lista* l1 = lst_cria();
  Lista* l2 = lst_cria();

  int n, valor;
  scanf("%d", &n);

  for(int i = 0; i < n; i++) {
    scanf("%d", &valor);
    lst_insere(l1, valor);
  }

  scanf("%d", &n);

  for(int i = 0; i < n; i++) {
    scanf("%d", &valor);
    lst_insere(l2, valor);
  }

  lst_imprime(concatena(l1, l2));

  return 0;
  
}