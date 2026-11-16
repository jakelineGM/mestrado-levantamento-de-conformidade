'''
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
  Nodo *novo = malloc(sizeof (Nodo));

  novo->carta = carta;
  novo->prox = NULL;

  if (fila->tamanho == 0) {
    fila->prim = novo;
    fila->fim = novo;
    fila->tamanho++;
  } else {
      fila->fim->prox = novo;
      fila->fim = novo;
      fila->tamanho++;
  }
}



/* Remove um elemento da fila e retorna o seu valor. Não se esqueça
 * de atualizar o contador.
 */
int retira(Fila *fila)
{
  if (fila->tamanho > 1) {
    Node *aux_nodo = fila->prim;
    int carta = fila->prim->carta;
    fila->prim = fila->prim->prox;
    fila->tamanho--;
    free(aux_nodo);
    return carta;
  } else {
    return -1;
  }
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
   int *valores = calloc(1, sieof(int));
   int valor;
   int l = 1;

   while (scanf("%d", &valor)) {
     if (valor == 0) {
       break;
     }

     valores = (int *) realloc(valoes, l * sizeof(int));
     valores[l - 1] = valor;
     l++;
   }

  for (int i = 0; i < l - 1; i++) {
    Fila *fila = cria_fila();

    for (int j = 1; j <= valores[i]; j++) {
      
      insere(fila, j);
    }

    int *cartas = calloc(1, sizeof(int));
    int k = 1;
    int carta;

    while (fila->tamanho > 1) {
      carta = retira(fila);
      cartas = realloc(cartas, k * sizeof(int));
      cartas[k - 1] = carta;
      k++;
      
      if (fila->tamanho > 1) {
        carta = retira(fila);
        insere(fila, carta);
      }  
    }

    printf("Descartadas:");
    for (int t = 0; t < k - 1; t++) {
      printf(" %d", cartas[t]);
    }

    printf("Restou: &d\n", retira(fila));
    free(fila);
  }

}
'''
def create_node(data):
  node = dict()

  node['data'] = data
  node['next'] = None

  return node

def create_queue():
  queue = dict()

  queue['head'] = None
  queue['tail'] = None
  queue['length'] = 0

  return queue

def insert(queue, data):
  new_node = create_node(data)

  if queue['length'] == 0:
    queue['head'] = new_node
    queue['tail'] = new_node
    queue['length'] += 1
  else:
    queue['tail']['next'] = new_node
    queue['tail'] = new_node
    queue['length'] += 1

def remove(queue):
  node_data = queue['head']['data']

  queue['head'] = queue['head']['next']
  queue['length'] -= 1

  return node_data

lengths = [int(i) for i in input().split()]

for i in range(len(lengths) - 1):
  queue = create_queue()

  for j in range(1, lengths[i] + 1):
    insert(queue, j)

  removed = list()

  while queue['length'] > 1:
    value = remove(queue)
    removed.append(value)

    if queue['length'] > 1:
      value = remove(queue)
      insert(queue, value)

  print("Descartadas:", end='')
  for r in removed:
    print(f' {r}', end='')

  print()

  print(f'Restou: {remove(queue)}')
  print()
