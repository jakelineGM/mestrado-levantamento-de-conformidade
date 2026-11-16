#include <stdio.h>
#include <stdlib.h>

typedef struct Elemento {
  int valor;
  struct Elemento* proximo;
} Elemento;

Elemento* criar_elemento(int valor) 
{
  Elemento* novo_elemento = (Elemento*)malloc(sizeof(Elemento));
  if (novo_elemento == NULL) {
    return NULL;
  }
  novo_elemento->valor = valor;
  novo_elemento->proximo = NULL;
  return novo_elemento;
}

Elemento* inserir_fim(Elemento* cabeca, int valor) 
{
  Elemento* novo_elemento = criar_elemento(valor);
  if (cabeca == NULL) {
    return novo_elemento;
  }
  Elemento* atual = cabeca;
  while(atual->proximo != NULL) {
    atual =  atual->proximo;
  }
  atual->proximo = novo_elemento;
  return cabeca;
}

Elemento* remocao_lista(Elemento* cabeca, int valor) 
{
  Elemento* atual = cabeca;
  Elemento* anterior = NULL;

    if (cabeca == NULL) {
      return NULL;
    }
    if (atual != NULL && atual->valor == valor) {
      cabeca = atual->proximo;
      free(atual);
      return cabeca;
    }
    while (atual != NULL && atual->valor != valor) {
      anterior = atual;
      atual = atual->proximo;
    }
    if (atual == NULL) {
      return cabeca;
    }
    anterior->proximo = atual->proximo;
    free(atual);
    return cabeca;
}

void imprime_lista(Elemento* cabeca)
{
  Elemento* atual = cabeca;
    if (atual == NULL) {
      printf(".\n");
      return;
    }
    printf("%d", atual->valor);
    atual = atual->proximo;

    while(atual != NULL) {
      printf(", %d", atual->valor);
      atual = atual->proximo;
    }
    printf(".\n");
}

void libera_lista(Elemento* cabeca)
{
  Elemento* atual = cabeca;
  Elemento* proximo;

    while(atual != NULL) {
      proximo = atual->proximo;
      free(atual);
      atual = proximo;
    }
}

int main() 
{
  Elemento* cabeca = NULL;
  int N, M;
  int valor;

    if (scanf("%d", &N) != 1) {
      return 1;
    }

    for (int i = 0; i < N; i++) {
      if (scanf("%d", &valor) != 1) {
        libera_lista(cabeca);
        return 1;
      }
      cabeca = inserir_fim(cabeca, valor);
    }

    if(scanf("%d", &M) != 1) {
      libera_lista(cabeca);
      return 1;
    }
    for (int i = 0; i < M; i++) {
        if (scanf("%d", &valor) != 1) {
          libera_lista(cabeca);
          return 1;
        }
      cabeca = remocao_lista(cabeca, valor);
    }
  imprime_lista(cabeca);

  libera_lista(cabeca);

return 0; 
}