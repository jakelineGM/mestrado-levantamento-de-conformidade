#include <stdio.h>
#include <stdlib.h>


struct nodo {
  int elem;
  struct nodo *prox;
};


struct nodo *lst_cria(void)
{
  struct nodo*list = (struct nodo*)malloc(sizeof(struct nodo));
  list = NULL;
  return list;
}


struct nodo *lst_insere_inicio(struct nodo *lis, int elem)
{
  struct nodo* inicio = (struct nodo*)malloc(sizeof(struct nodo));
    if(inicio==NULL){
      printf("erro de alocação");
    }
  inicio->prox = lis;
  inicio->elem = elem;
  return inicio;
}


struct nodo *lst_remove_elem(struct nodo *lis, int elem)
{
  struct nodo* ant;
  struct nodo* atual;
  ant = NULL;
  atual = lis;

    if(lis->elem == elem){
      struct nodo* novoInicio;
      novoInicio = lis->prox;
      free(lis);
    return novoInicio;
    }

    while(atual != NULL && atual->elem!= elem){
      ant = atual;
      atual = atual->prox;
    }

    if(atual==NULL){
      return lis;
    }

  ant->prox = atual->prox;
  free(atual);

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
  int entrada;
  struct nodo* lista = lst_cria();

    while(scanf("%d",&entrada), entrada!=0){
      if(entrada>0){
        lista = lst_insere_inicio(lista,entrada);
      }
      else{
        int chave = entrada*-1;
        if(lista!=NULL){
        lista = lst_remove_elem(lista,chave);
        }
      }
    }

  lst_imprime(lista);
    
}