#include <stdio.h>
#include <stdlib.h>

/* Estrutura para guardar um elemento da fila.
*/
typedef struct nodo Nodo;
struct nodo {
  int carta;
  Nodo *prox;
};


/* Estrutura para a fila, que deve ser uma lista ligada. Use uma
 * das pontas para representar o início da fila (de onde os
 * elementos devem ser retirados) e outra para representar o fim
 * da fila (onde os elementos devem ser inseridos).
 */
typedef struct fila Fila;
struct fila {
  Nodo *prim;
  Nodo *fim;
  int tamanho;
};


/* Cria uma nova fila vazia.
 */
Fila *cria_fila(void)
{
  Fila *nova = malloc(sizeof (Fila));

  nova->prim = NULL;
  nova->fim = NULL;
  nova->tamanho = 0;

  return nova;
}


/* Insere um elemento (carta) na fila. Não se esqueça de atualizar
 * o contador de nós para saber facilmente quando resta apenas uma
 * carta no monte.
 */
void insere(Fila *fila, int carta)
{
  Nodo *novo = malloc(sizeof(Nodo)); // complete o código!

  novo->carta = carta;
  novo->prox = NULL; // complete o código!

  if (fila->prim == NULL){
    fila->prim = novo;
    fila->fim = novo;
  } else {
    fila->fim->prox=novo;
    fila->fim = novo;
  }

  fila->tamanho++;
}



/* Remove um elemento da fila e retorna o seu valor. Não se esqueça
 * de atualizar o contador.
 */
int retira(Fila *fila)
{
  if (fila->prim == NULL){
    return -1;
  }

  Nodo *rem = fila->prim;
  int valor = rem->carta;

  fila->prim=rem->prox;
  if (fila->prim==NULL){
    fila->fim = NULL;
  }

  fila->tamanho--;
  free(rem);

  return valor;

}


/* Retorna o tamanho da fila. Use para saber quantas cartas ainda
 * existem no monte.
 */
int tamanho(Fila *fila)
{
  return fila->tamanho;
}


int main(void)
{
  int N;

  while (1){
    if (scanf("%d", &N) != 1){
      return 0;
    }
    if (N==0){
      break;
    }

    Fila *fila = cria_fila();
    
    for (int i= 1; i<= N; i++){
      insere(fila, i);
    }
    printf("Descartadas");

    int first = 1;

    while (tamanho(fila) > 1){
        int descartada = retira(fila);
        if (first){
          printf(" %d", descartada);
          first = 0;
        } else{
          printf(" %d", descartada);
        }
        int move = retira(fila);
        insere(fila, move);
    }
    int restante = retira(fila);
    printf("\nRestou: %d\n\n", restante);
    free(fila);
  }
  return 0;
}