#include <stdlib.h>
#include <stdio.h>

typedef struct pilhano PilhaNo;
struct pilhano{
int info;
PilhaNo* prox;
};

typedef struct pilha Pilha;
struct pilha{
PilhaNo* prim;
};

// Implemente as funções:
Pilha* pilha_cria(void){
  Pilha* pilha = malloc(sizeof(Pilha));
  pilha->prim = NULL;
  return pilha;
}
void pilha_push(Pilha* p, int v){
  PilhaNo* novo = malloc(sizeof(PilhaNo));
  novo->info = v;
  novo->prox = p->prim;
  p->prim = novo;
}
int pilha_pop(Pilha* p){
  if(p->prim == NULL){
    printf("pilha vazia!\n");
    return -1;
  }
  PilhaNo* troca = p->prim;
  int valor = troca->info;
  p->prim = troca->prox;
  free(troca);
  return valor;
}
int pilha_vazia(Pilha* p){
  return p->prim == NULL;
}
void pilha_imprime(Pilha* p){
  if(pilha_vazia(p)){
    printf("pilha vazia!\n");
    return;
  }
  PilhaNo* atual = p->prim;
  while(atual != NULL){
    printf("%d\n", atual->info);
    atual = atual->prox;
  }
}
void pilha_libera(Pilha* p){
  while(!pilha_vazia(p)){
    pilha_pop(p);
  }
  free(p);
}

int main() {
  Pilha* pilha = pilha_cria();
  int comando, valor;

  while(scanf("%d", &comando), comando != -1){
    if(comando == 0){
      pilha_pop(pilha);
    }
    else if(comando == 1){
      scanf("%d", &valor);
      pilha_push(pilha, valor);
    }
  }

  pilha_imprime(pilha);

  pilha_libera(pilha);

  return 0;
}