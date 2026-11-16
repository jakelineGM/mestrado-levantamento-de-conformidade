#include <stdio.h>
#include <stdlib.h>
#include <math.h>


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
  struct nodo *novo = malloc(sizeof(struct nodo));

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
  struct nodo *ant = NULL;
  struct nodo *p = lis;

  while(p != NULL && p->elem != elem) {
    ant = p;
    p = p->prox;
  }

  if(p == NULL) {
    return lis;
  }

  if(ant == NULL) {
    lis = p->prox;
  } else{
      ant->prox = p->prox;
    }

  free(p);
  
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
  int x;
  struct nodo *Lista = lst_cria();
  
  while(1) {
    scanf("%d", &x);

    if(x > 0){
      Lista = lst_insere_inicio(Lista, x);   
    } else {
        Lista = lst_remove_elem(Lista, abs(x));
      }

    if(x == 0) {
      break;
    }
    
  }

  lst_imprime(Lista);

  return 0;
  
}