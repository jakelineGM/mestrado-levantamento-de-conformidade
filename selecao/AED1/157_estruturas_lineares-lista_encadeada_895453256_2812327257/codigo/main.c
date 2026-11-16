#include <stdio.h>
#include <stdlib.h>

typedef struct no tipoNo;
struct no {
    int val;
    tipoNo* prox;
};

typedef struct {
    tipoNo* prim;
} tipoLista;

tipoNo* criaNo(int val, tipoNo* prox) {
    tipoNo* novo = malloc(sizeof(tipoNo));
    novo->val = val;
    novo->prox = prox;
    return novo;
}


void iniciaLista(tipoLista* lista) {
    lista->prim = NULL;
}

void insereNums(tipoLista* lista) {
    int num;
    scanf("%d", &num);
    if (num == -1) return;
    lista->prim = criaNo(num, lista->prim);
    insereNums(lista);
}


// COMPLETE A FUNCAO
int somaValores(tipoLista* lista) {
  int s = 0;
  tipoNo *aux = lista->prim;
  while(aux){
    s = s + aux->val;
    aux = aux->prox;
  }
  return s;
}

int main() {
    tipoLista lista;
    iniciaLista(&lista);
    insereNums(&lista);
    printf("%d\n", somaValores(&lista));
    return 0;
}