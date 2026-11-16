#include <stdio.h>
#include <stdlib.h>


/* Sugestao de estrutura de dados para guardar a lista de programa
 * e os programas. Voce pode alterar essa estrutura como quiser,
 * mas deve implementar uma lista circular encadeada. 
 */
typedef struct programa Programa;
struct programa {
  char nome[81];
  int tempo_restante;
  Programa *ant;
  Programa *prox;
};


/* Sugestao de estrutura de dados para a lista ligada circular.
 * Observe que cada no' dessa lista e' um programa. O campo
 * num_programas pode ajudar a identificar quando a lista
 * estiver vazia.
 */
typedef struct lista Lista;
struct lista {
  Programa *prim;
  int num_programas;
};


/* Sugestao de funcao para criar uma lista. Voce pode
 * alterar, usar ou remover esta funcao.
 */
Lista *lst_criar(void)
{
  Lista *nova = malloc(sizeof(Lista));
  nova->prim = NULL;
  nova->num_programas = 0;
  return nova;
}


/* Sugestao de funcao para ler a descricao de um programa e
 * retornar um novo no' para ele. Voce pode usar, modificar
 * ou remover esta funcao.
 */
Programa *ler_programa(void)
{
  Programa *novo = malloc(sizeof(Programa));
  
  // Leitura do nome do programa
  scanf("%80s", novo->nome);
  
  // Leitura do tempo total de execucao do programa
  scanf("%d", &novo->tempo_restante);
  
  // Atribui valores iniciais para os ponteiro do no'
  novo->ant = NULL;
  novo->prox = NULL;
  
  return novo;
}


/* Sugestao de funcao para inserir um no' no fim da lista.
 * Voce deve primeiro criar um novo programa usando a funcao
 * ler_programa() e depois passar o no' para esta funcao, que
 * so' precisara' ajustar os ponteiros para inserir no fim
 */
void lst_insere_fim(Lista *lst, Programa *nodo)
{
  if (lst->num_programas == 0)
  {
    nodo->ant = nodo;
    nodo->prox = nodo; 
    lst->prim = nodo;
  }
  else
  {
    Programa *ultimo = lst->prim->ant;

    if (ultimo != NULL)
    {
      ultimo->prox = nodo;
    }
    
    nodo->ant = ultimo;
    nodo->prox = lst->prim; 
    lst->prim->ant = nodo;
    
  }

  lst->num_programas++;
  return;
}


/* Sugestao de funcao para remover um no' da lista. Use
 * esta funcao para remover um no' da lista duplamente
 * encadeada.
 */
Programa *lst_remove(Lista *lst, Programa *nodo)
{
  if (lst->num_programas == 1 && lst->prim == nodo)
  {
    free(lst->prim);
    lst->num_programas = 0;
    lst->prim = NULL;
    return NULL;;
  }
  
  int max_iteracoes = lst->num_programas;
  int iteracoes = 0;
  Programa *atual = lst->prim;
  
  while(iteracoes < max_iteracoes && atual != nodo)
  {
      atual = atual->prox;
      iteracoes++;
  }

  if (atual == NULL)
  {
    return NULL;
  }

  Programa *prox = atual->prox;

  if (lst->prim == nodo)
  {
    lst->prim = prox;
  }
  
  atual->ant->prox = prox;
  prox->ant = atual->ant;

  free(atual);
  lst->num_programas--;

  return prox;
}


int main(void)
{
  int currentTime = 0;
  int Q;
  int N;

  scanf("%d", &Q);
  scanf("%d", &N);

  Lista *lista = lst_criar();

  for (int i = 0; i < N; i++)
  {
    Programa * p = ler_programa();
    lst_insere_fim(lista, p);
  }

  Programa *atual = lista->prim;

  int loop = Q;

  while (atual != NULL)
  {
    if (loop == 0)
    {
      loop = Q;
    }
    
    int retirar = 0;
    
    if (atual->tempo_restante <= loop)
    {
      //printf("%d us: %s trabalhou por %d, restando: %d\n", currentTime, atual->nome, loop, atual->tempo_restante - loop);
      currentTime += atual->tempo_restante;
      loop = 0;
      atual->tempo_restante = 0;
      retirar = 1;

      printf("%d us: %s finalizou\n", currentTime, atual->nome);
    }
    else {
      //printf("%d us: %s trabalhou por %d, restando: %d\n", currentTime, atual->nome, loop, atual->tempo_restante - loop);
      currentTime += loop;
      atual->tempo_restante -= loop;
      loop = 0;
    }

    atual = atual->prox;
    
    if (retirar == 1)
    {
       atual = lst_remove(lista, atual->ant);  
    }
  }

  printf("%d us: shutdown\n", currentTime);  
}