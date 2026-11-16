#include <stdio.h>
#include <stdlib.h>

/* Estrutura para guardar um elemento da lista.
 */
typedef struct nodo Nodo;
struct nodo {
  int carta;
  Nodo *ant;
  Nodo *prox;
};


/* Estrutura para a lista duplamente encadeada. O ponteiro fim
 * será importante para fazer inserções no fim sem precisar 
 * percorrer a lista.
 */
typedef struct lista Lista;
struct lista {
  Nodo *ini;
  Nodo *fim;
  int tamanho;
};


/* Cria uma nova lista vazia. Você pode modificar o código para
 * introduzir um nó cabeça sentinela (recomendado!)
 */
Lista *cria_lista(void)
{
  Lista *nova = malloc(sizeof *nova);

  nova->ini = NULL;
  nova->fim = NULL;
  nova->tamanho = 0;

  return nova;
}


/* Insere um elemento (carta) na lista. Não se esqueça de atualizar
 * o contador de nós para saber facilmente quando resta apenas uma
 * carta no monte.
 */
void insere_fim(Lista *lista, int carta) {
  Nodo *novo = malloc(sizeof *novo);

  novo->carta = carta;
  novo->prox = NULL;
  novo->ant = lista->fim;

  if (lista->fim != NULL) 
    lista->fim->prox = novo;
  else 
    lista->ini = novo;

  lista->fim = novo;
  lista->tamanho++;
}



/* Remove um elemento do início da lista e retorna o seu valor. Não
 * se esqueça de atualizar os ponteiros `ini' e `fim', nem de
 * atualizar o contador da lista.
 */
int retira(Lista *lista) {
  if (lista->ini == NULL)
    return -1;

  Nodo *removido = lista->ini;
  int valor = removido->carta;

  lista->ini = removido->prox;
  if (lista->ini != NULL) 
    lista->ini->ant = NULL;
  else 
    lista->fim = NULL;

  free(removido);
  lista->tamanho--;
  return valor;
}


/* Retorna o tamanho da lista. Use para saber quantas cartas ainda
 * existem no monte.
 */
int tamanho(Lista *lista) {
  return lista->tamanho;
}


int main(void) {
  int n;
  while (scanf("%d", &n) && n != 0) {
    Lista *monte = cria_lista();

    for (int i = 1; i <= n; i++) 
      insere_fim(monte, i);

    printf("Descartadas:");

    int primeiro = 1;
    while(monte->tamanho > 1) {
      int descartada = retira(monte);

      if (primeiro) {
        printf(" %d", descartada);
        primeiro = 0;
      } else {
        printf(" %d", descartada);
      }

      if (monte->tamanho > 1) {
        int mover = retira(monte);
        insere_fim(monte, mover);
      }
    }

    printf("\nRestou: %d\n", monte->ini->carta);
    free(monte->ini);
    free(monte);
  }

  return 0;
}