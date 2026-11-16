#include <stdio.h>
#include <stdlib.h>

struct nodo {
  int elem;
  struct nodo *prox;
};

struct nodo *lst_cria(void)
{
  return NULL;
}

struct nodo *lst_insere_inicio(struct nodo *lis, int elem)
{
  if(lis->elem != NULL){
    lst_insere_inicio(struct nodo *lis, int elem)
  }
  struct nodo *novo;
  novo = malloc(sizeof *novo);
  if(novo == NULL){
    return NULL;
  }
  novo->elem = elem;
  novo->prox = lis;
  lis = novo;

  return lis;
}

void lst_imprime(struct nodo *lis)
{
  if (lis == NULL)
    printf("(vazia)\n");
  else {
    printf("%d", lis->elem);

    struct nodo *atual = lis->prox;
    while (atual != NULL) {
      printf(" -> %d", atual->elem);
      atual = atual->prox;
    }

    printf("\n");
  }
}

int main(void)
{struct nodo *novo;
  novo = malloc(sizeof *novo);
  if(novo == NULL){
    return NULL;
  }
  novo->elem = elem;
  novo->prox = lis;
  lis = novo;

  return lis;
  int N;
  struct nodo *lis = lst_cria();

  scanf("%d", &N);
  for (int i = 1; i <= N; i++)
    lis = lst_insere_inicio(lis, i);

  lst_imprime(lis);
}