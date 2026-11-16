#include <stdlib.h>
#include <stdio.h>

typedef struct pilhano PilhaNo;
struct pilhano {
    int info;
    PilhaNo* prox;
};

typedef struct pilha Pilha;
struct pilha {
    PilhaNo* prim;
};

// Implemente as funções:
Pilha* pilha_cria(void);
void pilha_push(Pilha* p, int v);
int pilha_pop(Pilha* p);
int pilha_vazia(Pilha* p);
void pilha_imprime(Pilha* p);
void pilha_libera(Pilha* p);

int main(){
  Pilha* p = pilha_cria();
   int n, v;
  while(scanf("%d" , &n)){
    if (n == -1){
      if (pilha_vazia(p)) printf("pilha vazia!\n");
      else pilha_imprime(p);
      break;
    }
    else if (n == 0){
      pilha_pop(p);
    }
    else if (n == 1){
      scanf("%d" , &v);
      pilha_push(p, v);
    }
  } 
  pilha_libera(p);

  return 0;
}

  Pilha* pilha_cria(){
    Pilha* p = malloc(sizeof(Pilha));
    if (p == NULL) exit(1);
    p->prim = NULL;
    return p;
  }

  int pilha_vazia(Pilha* p){
    int ok = 0;
    if (p->prim == NULL) ok = 1;
    return ok;
  }

  void pilha_imprime(Pilha* p){
    PilhaNo* p2;
    for (p2 = p->prim; p2 != NULL; p2 = p2->prox){
      printf("%d\n" , p2->info);
    }
  }

  int pilha_pop(Pilha* p){
    int v = 1;
    if (pilha_vazia(p)) {
      printf("pilha vazia!\n");
    }
    else {
    PilhaNo* n = p->prim;
    v = n->info;
    p->prim = n->prox;
    free(n);
    }
    return v;
  } 

  void pilha_push(Pilha* p, int v){
  PilhaNo* n = malloc(sizeof(PilhaNo));
  if (n == NULL) exit(1);
  n->info = v;
  n->prox = p->prim;
  p->prim = n;
  } 

  void pilha_libera(Pilha* p){
    PilhaNo* n = p->prim;
    while (n != NULL){
      PilhaNo* t = n->prox;
      free(n);
      n = t;
    }
    free(p);
  }
