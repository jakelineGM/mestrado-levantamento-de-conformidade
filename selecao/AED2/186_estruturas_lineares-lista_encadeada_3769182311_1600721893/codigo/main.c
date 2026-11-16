#include <stdio.h>
#include <stdlib.h>


struct nodo {
  int elem;
  struct nodo *prox;
};


// Cria uma nova lista vazia. Nesta representação, a lista vazia
// deve ser apenas um ponteiro nulo.
struct nodo *lst_cria(void) {
  return NULL;
}


// Cria um novo nó contendo como elemento o valor passado pelo
// parâmetro `elem' e insere este novo nó no começo da lista.
// Caso a alocação seja bem-sucedida, a função deve retornar
// um ponteiro para o início da lista.
struct nodo *lst_insere_inicio(struct nodo *lis, int elem) {
  struct nodo *novo = malloc(sizeof *novo);

  if (novo == NULL) 
    return NULL;

  novo->elem = elem;
  novo->prox = lis;
  lis = novo;

  return lis;
}


// Remove o primeiro nó da lista encadeada e retorna um
// ponteiro para o nvo início da lista
struct nodo *lst_remove_inicio(struct nodo *lis) {
  struct nodo *removido = lis;
  
  lis = lis->prox;
  free(removido);

  return lis;
}


// Percorre a lista e imprime seu conteúdo.
void lst_imprime(struct nodo *lis) {
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
int main(void) {
  int n;
  struct nodo *lis = lst_cria();

  scanf("%d", &n);
  
  while (n != 0) {
    if (n > 0) 
      lis = lst_insere_inicio(lis, n);
    else {
      n *= -1;
      int i = 0;
      while (lis != NULL && i < n) {
        lis = lst_remove_inicio(lis);
        i++;
      }
    }
    scanf("%d", &n);
  }

  lst_imprime(lis);
  return 0;
}