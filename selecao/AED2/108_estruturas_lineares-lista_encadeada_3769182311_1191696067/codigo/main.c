#include <stdio.h>
#include <stdlib.h>


struct nodo {
  int elem;
  struct nodo *prox;
};


// Cria uma nova lista vazia. Nesta representação, a lista vazia
// deve ser apenas um ponteiro nulo.
struct nodo *lst_cria(void)
{
  struct nodo* lis = (struct nodo*)malloc(sizeof(struct nodo));
  lis = NULL;
  return lis;
}


// Cria um novo nó contendo como elemento o valor passado pelo
// parâmetro `elem' e insere este novo nó no começo da lista.
// Caso a alocação seja bem-sucedida, a função deve retornar
// um ponteiro para o início da lista.
struct nodo *lst_insere_inicio(struct nodo *lis, int elem)
{
 struct nodo *inicio = (struct nodo*)malloc(sizeof(struct nodo));
    if(inicio == NULL){
      printf("erro de alocação");
    }
  inicio->elem = elem;
  inicio->prox = lis;
  return inicio;
}


// Remove o primeiro nó da lista encadeada e retorna um
// ponteiro para o nvo início da lista
struct nodo *lst_remove_inicio(struct nodo *lis)
{
  struct nodo* novoInicio = NULL;
  
    if(lis->prox != NULL){
      novoInicio = lis->prox;
       free(lis);
    }
  return novoInicio;
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
  struct nodo* list = lst_cria();

    while(scanf("%d",&entrada), entrada!=0){
      if(entrada>0){
        list = lst_insere_inicio(list,entrada);
      }
      else if(entrada<0){
        int numeros = entrada*-1;
          for(int i=0;i<numeros;i++){
            if(list!=NULL){
             list = lst_remove_inicio(list);
            }
          }
      }
    }

  lst_imprime(list);
  
}