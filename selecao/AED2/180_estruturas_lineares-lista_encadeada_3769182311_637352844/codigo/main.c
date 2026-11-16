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


// Remove o primeiro nó da lista encadeada e retorna um
// ponteiro para o nvo início da lista
struct nodo *lst_remove_inicio(struct nodo *lis)
{
  if (lis == NULL) return NULL;
  struct nodo *p = lis;
  lis = p->prox;

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
  int x, i, tamanho = 0;

  struct nodo *Lista = lst_cria();
  
  while (1){
    scanf("%d", &x);
    
    if (x > 0){
      Lista = lst_insere_inicio(Lista, x);
      tamanho++;
    } else{
        if (abs(x) > tamanho){
          for (i = 0; i < tamanho; i++){
            Lista = lst_remove_inicio(Lista);
          }  
        } else{
            for (i = 0; i < abs(x); i++){
                Lista = lst_remove_inicio(Lista);
            } 
          }
      }

  if  (x == 0) {
    break;
  }
        
  }

  lst_imprime(Lista);  

  return 0;
}