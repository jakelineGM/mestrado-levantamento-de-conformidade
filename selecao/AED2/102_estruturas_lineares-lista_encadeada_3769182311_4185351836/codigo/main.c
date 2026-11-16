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
  struct nodo *novo;
  novo = malloc(sizeof(*novo));
  if (novo == NULL) {
    printf ("Erro ao realizar a alocação de memória.\n");
    return NULL;
  }

  novo->elem = elem;
  novo->prox = lis;
  lis = novo;

  return lis;
}


// Remove o primeiro nó da lista encadeada e retorna um
// ponteiro para o nvo início da lista
struct nodo *lst_remove_inicio(struct nodo *lis)
{
  struct nodo *removido;
  
  removido = lis;
  lis = removido->prox;
  free(removido);

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
  int num;
  struct nodo *lis = lst_cria();
  
  while(scanf("%d", &num) && num != 0) {
    if (num > 0) {
      lis = lst_insere_inicio(lis, num);
    }
    else if (num < 0) {
      int remover = abs(num);
      for(int cont = 0; cont < remover; cont++) {
          if (lis != NULL) {
            lis = lst_remove_inicio(lis);
          }
        }
    }
  }
  lst_imprime(lis);

  return 0;
}