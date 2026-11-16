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

void lst_insere_fim(Lista *lst, int num) {
  Nodo *p = malloc(sizeof *p);
  p->num = num;
  p->prox = NULL;
  
  if(lst->prim == NULL) {
    lst->prim = p;
    lst->fim = p;
  } else {
    lst->fim->prox = p;
    lst->fim = p;
  }
}

void lst_insere_inicio(Lista *lst, int num) {
  Nodo *p = malloc(sizeof *p);
  p->num = num;
  p->prox = lst->prim;

  lst->prim = p;
  if (lst->fim == NULL)
    lst->fim = p;
  /* Faça uma função que cria um novo nó contendo o
   * valor `num'. Insira esse nó no começo da lista.
   */
}


Nodo *lst_busca(Lista *lst, int num) {
  Nodo *p = lst->prim;
  while (p != NULL) {
    if (p->num == num) 
      return p;
    p = p->prox;
  }
  /* Faça uma função que percorre a lista e procura um
   * nó que contem o número `num'. Devolva um ponteiro
   * para esse nó.
   */
  return NULL;
}

int main(void) {
  Lista *lst;
  int num;

  lst = lst_cria();
  /* Insere todos os números no início da lista, até aparecer
   * um sentinela zero.
   */
  while (scanf("%d", &num), num != 0) {
    lst_insere_fim(lst, num);
  }

  /* Procura por todos os números de consulta
   */
  while (scanf("%d", &num), num != 0) {
    Nodo *encontrado = lst_busca(lst, num);
    if (encontrado == NULL) {
      printf("%d: nao existe\n", num);
    } else if (encontrado == lst->prim) {
      printf("%d: inicio\n", encontrado->num);
    } else if (encontrado == lst->fim) {
      printf("%d: fim\n", encontrado->num);
    } else {
      printf("%d: existe\n", encontrado->num);
    }
    /* Continue o código... verifique se o ponteiro
     * `encontrado' é NULL ou se ele indica o endereço
     * de um nó que está no começo da lista, no fim
     * da lista ou em outro lugar da lista.
     */
  }
  return 0;
}