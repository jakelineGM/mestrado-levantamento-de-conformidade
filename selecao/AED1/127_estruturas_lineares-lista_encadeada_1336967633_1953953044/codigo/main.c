#include <stdlib.h>
#include <stdio.h>

typedef struct tipoNo {
	int valor;
	struct tipoNo *prox;
} tipoNo;

typedef struct tipoLista {
	tipoNo *prim;
} tipoLista;

void inserirNaLista(tipoLista *lista, int valor) {
    tipoNo *novo = (tipoNo *) malloc(sizeof(tipoNo));
    novo->valor = valor;
    novo->prox = lista->prim;
    lista->prim = novo;
}

// FACA SUA FUNCAO AQUI
int removerMaiorLista(tipoLista *l){
  if(!l->prim){
    return 0;
  }
  tipoNo*aux=l->prim;
  tipoNo*anterior = NULL;
  tipoNo*maior=l->prim;
  tipoNo*anteriormaior=NULL;
  while(aux){
    if(aux->valor>maior->valor){
      maior=aux;
      anteriormaior=anterior;
    }
    anterior = aux;
    aux= aux->prox;
  }
  if(maior==l->prim){
    l->prim=l->prim->prox;
  }
  else{
    anteriormaior->prox=maior->prox;
  }
  int v= maior-> valor;
  free(maior);
  return v;
  }
// END FUNCAO


void mostrarLista(tipoLista *lista) {
    tipoNo *atual = lista->prim;
    while(atual!=NULL) {
        printf("%d\n", atual->valor);
        
        atual=atual->prox;
    }
}


int main() {
    tipoLista lista;
    lista.prim = NULL;

    for(int i=0;i<10;i++) {
        int valor;
        scanf("%d", &valor);
        inserirNaLista(&lista, valor);
    }

    printf("%d\n", removerMaiorLista(&lista));
    mostrarLista(&lista);

}