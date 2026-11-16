#include <stdio.h>
#include <stdlib.h>

// ESCREVA SEU CÓDIGO AQUI!!!
typedef struct listano{
  unsigned valor;
  struct listano *prox;
} ListaNo;

typedef struct lista{
  ListaNo* prim;
} Lista;

Lista* lst_cria(){
  Lista* l = (Lista*) malloc(sizeof(Lista));
  if(l == NULL){
    exit(1);
  }
  l->prim = NULL;
  return l;
}

void lst_insere(Lista* l, unsigned valor){
  ListaNo* NovoNo = (ListaNo*) malloc(sizeof(ListaNo));
  NovoNo->valor = valor;
  NovoNo->prox = l->prim;
  l->prim = NovoNo;
}

int comprimento(Lista* l){
  int i = 0;
  ListaNo* p = l->prim;
  while(p != NULL){
    i++;
    p = p->prox;
  }
  return i;
}
int main(void){

  Lista *l = lst_cria();

  int valor;

  while(scanf("%d", &valor), valor >= 0) {

    lst_insere(l, valor);
    
  }

  printf("Comprimento: %d\n", comprimento(l));

  return 0;
  
}