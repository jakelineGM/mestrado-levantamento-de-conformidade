#include <stdio.h>
#include <stdlib.h>

// ESCREVA SEU CÓDIGO AQUI !!!

typedef struct no {
  int dado;
  struct no *prox;
} No;

typedef struct lista {
  No *inicio;
} Lista;

Lista* lst_cria(){
  Lista *l = (Lista*)malloc(sizeof(Lista));
  l->inicio = NULL;
  return l;
}

void lst_insere(Lista *l, int valor){
  No *novo = (No*)malloc(sizeof(No));
  novo->dado = valor;
  novo->prox = l->inicio;
  l->inicio = novo;
}

int ultimo(Lista *l){
  if(l->inicio == NULL){
    printf("Erro: Lista vazia!\n");
    exit(1);
  }
  No *atual = l->inicio;
  while (atual->prox != NULL){
      atual = atual->prox;
  }
  return atual->dado;
}

int main(void) {

  Lista *l = lst_cria();

  int n, valor;
  scanf("%d", &n);

  for(int i = 0; i < n; i++) {
    scanf("%d", &valor);
    lst_insere(l, valor);
  }

  printf("Ultimo: %d\n", ultimo(l));

  return 0;
  
}