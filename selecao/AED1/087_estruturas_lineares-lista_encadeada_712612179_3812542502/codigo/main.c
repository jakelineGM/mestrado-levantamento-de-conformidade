#include <stdio.h>
#include <stdlib.h>


typedef struct listano ListaNo;
typedef struct lista Lista;

struct listano{
  float valor;
  ListaNo* prox;
};

struct lista{
  ListaNo* prim;
};

Lista* lst_cria(){
  Lista* l = malloc(sizeof(Lista));
  if(l == NULL) exit(1);
  l->prim = NULL;
  return l;
}

void lst_insere(Lista* l, float valor){
  ListaNo* novo = malloc(sizeof(ListaNo));
  if(novo == NULL) exit(1);
  novo->valor = valor;
  novo->prox = l->prim;
  l->prim = novo;
}

Lista* merge(Lista* l1, Lista* l2){
  Lista* merged = lst_cria();
  ListaNo *p1 = l1->prim, *p2 = l2->prim;

  while(p1 != NULL || p2 != NULL){
    
    if(p1 != NULL){
      lst_insere(merged, p1->valor);
      ListaNo *temp = p1->prox;
      free(p1);
      p1 = temp;
    }
    
    if(p2 != NULL){
      lst_insere(merged, p2->valor);
      ListaNo *temp = p2->prox;
      free(p2);
      p2 = temp;
    }
  }

  free(l1);
  free(l2);

  return merged;
}

void lst_imprime(Lista* l){
  ListaNo* p;
  for(p = l->prim; p != NULL; p = p->prox){
    printf("%.2f ", p->valor);
  }
  printf("\n");
}

int main(void) {

  Lista *l1 = lst_cria();
  Lista *l2 = lst_cria();

  int n;
  float valor;

  scanf("%d", &n);
  for(int i = 0; i < n; i++) {
    scanf("%f", &valor);
    lst_insere(l1, valor);
  }

  scanf("%d", &n);
  for(int i = 0; i < n; i++) {
    scanf("%f", &valor);
    lst_insere(l2, valor);
  }

  lst_imprime(merge(l1, l2));

  return 0;
  
}