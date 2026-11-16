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
void insere_fim(Lista *lista, int carta)
{
  Nodo *novo = malloc(sizeof(Nodo));

  novo->carta = carta;
  novo->prox = NULL;
  novo->ant = lista->fim;

  // complete o código para modificar o último elemento da lista
  // não se esqueça de modificar o início da lista quando ela estiver
  // vazia

  if (lista->ini == NULL)
  {
    lista->ini = novo;
  }
  else
  {
    lista->fim->prox = novo;
  }

  lista->fim = novo;

  lista->tamanho++;
}



/* Remove um elemento do início da lista e retorna o seu valor. Não
 * se esqueça de atualizar os ponteiros `ini' e `fim', nem de
 * atualizar o contador da lista.
 */
int retira(Lista *lista)
{
  int valor;

  if (lista->tamanho == 0)
  {
    return 0;
  }

  valor = lista->ini->carta;
  
  if (lista->tamanho == 1)
  { 
    free(lista->ini);
    
    lista->ini = NULL;
    lista->fim = NULL;
    lista->tamanho = 0;
  }
  else 
  {
    Nodo *prox = lista->ini->prox;

    free(lista->ini);
  
    lista->ini = prox;
  
    lista->tamanho--;
  }

  return valor;
}


/* Retorna o tamanho da lista. Use para saber quantas cartas ainda
 * existem no monte.
 */
int tamanho(Lista *lista)
{
  return lista->tamanho;
}


int main(void)
{
  int N;

  scanf("%d", &N);
  while (N != 0)
  {
    Lista *lis = cria_lista();
    
    for (int i = 0; i < N; i++)
    {
      insere_fim(lis, i + 1);
    }

    printf("Descartadas:");

    while(tamanho(lis) > 1)
    {
      int retirado = retira(lis);
      printf(" %d", retirado);
      retirado = retira(lis);
      insere_fim(lis, retirado);
    }

    int resto = retira(lis);
    printf("\nRestou: %d\n", resto);

    free(lis);
    
    scanf("%d", &N);
  }
}