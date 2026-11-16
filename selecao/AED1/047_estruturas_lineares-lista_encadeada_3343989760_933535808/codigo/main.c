#include <stdio.h>
#include <stdlib.h>

typedef struct no {
    int val;
    struct no* prox;
} tipoNo;

typedef struct {
    tipoNo* prim;
} tipoLista;

tipoNo* criaNo(int val, tipoNo* prox) {
    tipoNo* novo = (tipoNo*)malloc(sizeof(tipoNo));
    novo->val = val;
    novo->prox = prox;
    return novo;
}

void iniciaLista(tipoLista* lista) {
    lista->prim = NULL;
}

void insere(tipoLista* lista, int val) {
    lista->prim = criaNo(val, lista->prim);
}

void populaLista(tipoLista* lista) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int val;
        scanf("%d", &val);
        insere(lista, val);
    }
}

int simetrica(tipoLista* lista) { 
    if (lista->prim==NULL) return 1;
  
    tipoNo*aux = lista->prim;
    int cc = 0;

  while(aux){
    cc++;
    aux  = aux->prox; //vai contar qnts elementos tem na lista
  }

  if (cc == 1) return 1; //eh simetrica
 
  int metade = cc/2; 
  int posInicioSegunda;
  
  if (cc % 2 == 0){ posInicioSegunda = metade;} //desconsidera o do meio se for impar
  else { posInicioSegunda = metade+1; }
  
  tipoNo *primMetade = lista->prim; // p cada elemento da primeira metade
    for (int i=0; i<metade; i++){
     tipoNo *segMetade = lista->prim;
      for (int j=0; j<posInicioSegunda; j++){
        segMetade = segMetade->prox;
      }
      int encontrado = 0;
      while(segMetade){
        if (segMetade->val == primMetade->val)
          encontrado = 1;
        segMetade = segMetade->prox;
    }
     if (!encontrado) return 0;
      primMetade = primMetade->prox;
  }
  return 1;
}
  
 
    



int main() {
    tipoLista lista;
    iniciaLista(&lista);

    populaLista(&lista);

    if (simetrica(&lista)) {
        printf("Simetrica\n");
    } else {
        printf("Nao simetrica\n");
    }
}