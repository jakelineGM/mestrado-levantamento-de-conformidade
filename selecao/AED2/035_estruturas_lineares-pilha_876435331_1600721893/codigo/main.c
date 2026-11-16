#include <stdio.h>
#include <stdlib.h>


/* Estrutura para guardar um elemento da pilha.
 */
typedef struct nodo Nodo;
struct nodo {
  int valor;
  Nodo *prox;
};


/* Estrutura para a pilha, que deve ser uma lista ligada. O
 * primeiro elemento é o topo da pilha.
 */
typedef struct pilha Pilha;
struct pilha {
  Nodo *topo;
  int tamanho;
};


/* Insere um elemento no topo da pilha (ou seja, no início da
 * lista ligada)
 */
void push(Pilha *p, int valor)
{
  Nodo *novo = malloc(sizeof *novo);
  if (novo == NULL) return;

  novo->valor = valor;
  novo->prox = p->topo;
  p->topo = novo;
  p->tamanho++;
  
  printf("push %d\n", valor);
}


/* Retorna o valor do primeiro elemento da pilha, sem alterar
 * o conteúdo da pilha. Use para saber se o topo da pilha contém
 * o valor zero ou um valor negativo.
 */
int primeiro(Pilha *p) {
  return p->topo->valor;
}


/* Remove um elemento do topo da pilha (ou seja, retira o 
 * primeiro elemento da lista)
 */
void pop(Pilha *p) {
  if (p->topo != NULL) {
    Nodo *aux = p->topo;                             //rs
    int removido = aux->valor;

    p->topo = aux->prox;
    p->tamanho--;

    free(aux);
    printf("pop %d\n", removido);
  }
}


/* Retorna o tamanho da pilha. Use para saber se é possível
 * retirnar dois elementos da pilha quando o topo for
 * um valor negativo.
 */
int tamanho(Pilha *p) {
  return p->tamanho;
}


int main(void) {
  Pilha p;
  p.topo = NULL;
  p.tamanho = 0;

  int n;
  while(scanf("%d", &n) == 1) {
    push(&p, n);

    if (primeiro(&p) == 0) 
      break;

    while(tamanho(&p) >= 2 && primeiro(&p) < 0) {
      int v1 = primeiro(&p);
      pop(&p);

      int v2 = primeiro(&p);
      pop(&p);

      push(&p, v1 + v2);

      if (primeiro(&p) == 0) 
        return 0;
    }

    if (tamanho(&p) < 2 && primeiro(&p) < 0) break;
  }

  return 0;
}