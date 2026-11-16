#include <stdio.h>   // Para o printf, scanf, definicao do NULL e etc..
#include <stdlib.h> // precisa para usar o malloc
#include <string.h>  // USADA PARA STRCMP e outras funções

typedef struct tipoDado {
  char nome[50];
} tipoDado;

typedef struct tipoNo {
  tipoDado dado;
  struct tipoNo * prox;
} tipoNo;

typedef struct tipoFila {
  tipoNo *prim,*ult;
} tipoFila;

void criarFila(tipoFila *l) {
  l->prim = NULL;
  l->ult = NULL;

}


void inserirNaFila(tipoFila *l, tipoDado valor) {
  tipoNo *aux;
  aux = (tipoNo*) malloc(sizeof(tipoNo));
  aux-> dado = valor;
  aux->prox = NULL;
  if(l->prim == NULL) {
    l->prim = aux;
  }
  else {
    l->ult->prox = aux;
  }
  l->ult = aux;
}



tipoNo * haElementos(tipoFila *l) {
  return l->prim;

}

// FACAO SUA FUNCAO AQUI!

void mostrar(tipoNo *aux) {
  if (aux == NULL) {
    return;
  }
  mostrar(aux->prox);
  printf("%s\n", aux->dado.nome);
}

void mostrarReverso(tipoFila *f) {
  tipoNo *aux;
  aux = f->prim;
  mostrar(aux);
}

int main() {
tipoFila f;
  tipoDado d;
int n;

criarFila(&f);
scanf("%d%*c",&n);
while(n) {
 scanf("%[^\n]%*c",d.nome);
 inserirNaFila(&f,d);
 n--; 
}
mostrarReverso(&f);
}