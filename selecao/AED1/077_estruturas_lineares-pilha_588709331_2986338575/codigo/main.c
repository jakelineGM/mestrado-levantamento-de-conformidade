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
Pilha* pilha_cria(void){
  Pilha* p = (Pilha*)malloc(sizeof(Pilha));
  p->prim = NULL;
    return p;
}
void pilha_push(Pilha* p, int v){
  PilhaNo* novo = (PilhaNo*)malloc(sizeof(PilhaNo));
  novo->info = v;
  novo->prox = p->prim;
  p->prim = novo;
}
int pilha_pop(Pilha* p){
  if(p->prim != NULL){
    PilhaNo* topo = p->prim;
    int valor = topo->info;
    p->prim = topo->prox;
    free(topo);
    return valor;
  }
  return 0;
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
  PilhaNo* atual = p->prim;
  while(atual != NULL){
    PilhaNo* temp = atual;
    atual = atual->prox;
    free(temp);
  }
  free(p);
}

int main() {
   // Seu código aqui!
  Pilha* p = pilha_cria();
  int comando, valor;

  while(scanf("%d", &comando) == 1){
    if(comando == -1){
      pilha_imprime(p);
      break;
    }else if (comando == 0){
      if(pilha_vazia(p)){
        printf("pilha vazia!\n");
      }else{
        pilha_pop(p);
      }
    } else if(comando == 1){
      if(scanf("%d", &valor) == 1){
        pilha_push(p, valor);
      }
    }
  }
    pilha_libera(p);
    return 0;
}