#include <stdio.h>
#include <stdlib.h>

typedef struct nodo Nodo;
struct nodo {
  int num;
  Nodo *prox;
};

typedef struct lista Lista;
struct lista {
  Nodo *prim;
  Nodo *fim;
};

Lista *lst_cria(void)
{
  Lista *novo;

  novo = malloc(sizeof (Lista));
  novo->prim = NULL;
  novo->fim = NULL;

  return novo;
}

void lst_insere_inicio(Lista *lst, int num)
{

  /* Faça uma função que cria um novo nó contendo o
   * valor `num'. Insira esse nó no começo da lista.
   */
  Nodo *novo = malloc(sizeof(Nodo));
  novo->num = num;
  
  if (lst->prim == NULL)
  {
    lst->prim = novo;
    lst->fim = novo;

    return;
  }

  novo->prox = lst->prim;
  lst->prim = novo;
  return;
}


Nodo *lst_busca(Lista *lst, int num)
{
  Nodo *atual = lst->prim;

  while (atual != NULL && atual->num != num)
  {
    atual = atual->prox;
  }

  return atual;
}

int main(void)
{
  Lista *lst;
  int num;

  lst = lst_cria();

  /* Insere todos os números no início da lista, até aparecer
   * um sentinela zero.
   */
  while (scanf("%d", &num), num != 0) {
    lst_insere_inicio(lst, num);
  }

  /* Procura por todos os números de consulta
   */
  while (scanf("%d", &num), num != 0) {
    Nodo *encontrado = lst_busca(lst, num);

    /* Continue o código... verifique se o ponteiro
     * `encontrado' é NULL ou se ele indica o endereço
     * de um nó que está no começo da lista, no fim
     * da lista ou em outro lugar da lista.
     */
    if (encontrado == NULL)
    {
      printf("%d: nao existe\n", num);
    }
    else if (lst->prim == encontrado)
    {
      printf("%d: inicio\n", num);
    }
    else if (lst->fim == encontrado)
    {
      printf("%d: fim\n", num);
    }
    else
    {
      printf("%d: existe\n", num);
    }
  }
}