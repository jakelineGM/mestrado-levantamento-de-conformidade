#include <stdio.h>
#include <stdlib.h>


struct nodo {
  int elem;
  struct nodo *prox;
};


// Cria uma nova lista vazia. Nesta representação, a lista vazia
// deve ser apenas um ponteiro nulo.
struct nodo *lst_cria(void)
{
  return NULL;
}


// Cria um novo nó contendo como elemento o valor passado pelo
// parâmetro `elem' e insere este novo nó no começo da lista.
// Caso a alocação seja bem-sucedida, a função deve retornar
// um ponteiro para o início da lista.
struct nodo *lst_insere_inicio(struct nodo *lis, int elem)
{
  struct nodo* novo = malloc(sizeof(struct nodo));

  if (novo == NULL)
  {
    exit(1);
  }

  novo->elem = elem;
  novo->prox = lis;

  return novo;
}


// Percorre a lista procurando um nó que contenha o elemento
// passado por parâmetro e o remove. Se esse elemento não existir,
// então nada deve ser feito. Retorna sempre um ponteiro para
// o primeiro nó da lista.
struct nodo *lst_remove_elem(struct nodo *lis, int elem)
{
  struct nodo *anterior = NULL;
  struct nodo *atual = lis;

  while(atual != NULL && atual->elem != elem)
  {
    anterior = atual;
    atual = atual->prox;
  }

  if (atual != NULL)
  {
    struct nodo *prox = atual->prox;
    free(atual);
    
    if (anterior == NULL)
    {
      return prox;
    }

    anterior->prox = prox;
  }

  return lis;
}


// Percorre a lista e imprime seu conteúdo.
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


// Programa principal. Verifique o enunciado.
int main(void)
{
  int N;
  struct nodo *lis = lst_cria();

  scanf("%d", &N);
  while (N != 0)
  {
    if (N > 0)
    {
      lis = lst_insere_inicio(lis, N);
    }
    else
    {
      lis = lst_remove_elem(lis, N * -1);
    }
    
    scanf("%d", &N);
  }

  lst_imprime(lis);
}