#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct no {
    int dado;
    struct no* prox;
} tipoNo;

typedef struct {
    tipoNo* atual;
} tipoListaCircular;

void criaListaCircular(tipoListaCircular* lista) {
    lista->atual = NULL;
}

void inserirListaCircular(tipoListaCircular* lista, int dado) {
    tipoNo* aux;

    aux = (tipoNo*) malloc(sizeof(tipoNo));
    aux->dado = dado;

    if(lista->atual) {
        aux->prox = lista->atual->prox;
        lista->atual->prox = aux;
    } else {
        lista->atual=aux;
        aux->prox=aux;
    }
}

// FACA SUA FUCAO AQUI 
void removerSegundoElemento(tipoListaCircular *l){
  tipoNo *aux, *temp;
  if(l->atual){
    aux = l->atual;
    if(aux->prox){
      temp = aux->prox;
      aux->prox = temp->prox;
    }
  }
}

// END FUNCAO

void mostraLista(tipoListaCircular* lista) {
    if (lista->atual == NULL) {
        printf("Lista vazia!\n");
        return;
    }

    tipoNo* inicio = lista->atual->prox;
    tipoNo* aux = inicio;

    do {
        printf("%d\n", aux->dado);
        aux = aux->prox;
    } while (aux != inicio);
}

int main() {
    int dado;
    tipoListaCircular lista;

    criaListaCircular(&lista);


    scanf("%d%*c", &dado);
    inserirListaCircular(&lista, dado);

    scanf("%d%*c", &dado);
    inserirListaCircular(&lista, dado);

    scanf("%d%*c", &dado);
    inserirListaCircular(&lista, dado);

    scanf("%d%*c", &dado); 
    inserirListaCircular(&lista, dado);

    scanf("%d%*c", &dado);
    inserirListaCircular(&lista, dado);

    removerSegundoElemento(&lista);

    mostraLista(&lista); 

    return 0;
}