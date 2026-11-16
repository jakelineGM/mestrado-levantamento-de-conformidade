#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char nome[20];
    int id;
} tipoDados;

typedef struct no {
    tipoDados dados;
    struct no* prox;
} tipoNo;

typedef struct {
    tipoNo* inicio;
    tipoNo* fim;
} tipoFila;

// Funcoes a serem feitas. 
// Coloque os includes necessários para seu para o seu 
// programa aqui
void criaFila(tipoFila* x){
  x->inicio = NULL;
  x->fim = NULL;
}

void enfileirar(tipoFila* x,tipoDados y){
  tipoNo*novo = (tipoNo*) malloc(sizeof(tipoNo));
  novo->dados = y;
  novo->prox = NULL;
  if(x->inicio == NULL){
    x->inicio = novo;
    x->fim = novo;
  }
  else{
    tipoNo* aux = x->inicio;
    while(aux->prox){
      aux = aux->prox;
    }
    aux->prox = novo;
    x->fim = novo;
  }
}

tipoDados desenfileirar(tipoFila* x){
  tipoNo*aux = x->inicio;
  x->inicio = aux->prox;
  tipoDados d;
    d = aux->dados;
free(aux);
  return d;
}
// SUAS FUNCOES DEVEM COMPLEMENTAR O PROGRAMA PRINCIPAL
// ELE JA TEM CHAMADAS PARA SUAS FUNCOES





// FIM DO SEU CODIGO

void mostraFila(tipoFila* fila) {
    tipoNo* aux = fila->inicio;    
    while (aux != NULL) {
        printf("%s\n", aux->dados.nome);
        printf("%d\n", aux->dados.id);
        aux = aux->prox;
    }
}

int main() {
    tipoDados pessoa;
    tipoFila aliados,  imperio, garbage;

    criaFila(&aliados);
    criaFila(&imperio);
    criaFila(&garbage);

    scanf("%[^\n]%*c", pessoa.nome);
    scanf("%d%*c", &pessoa.id);

    enfileirar(&aliados, pessoa);

    scanf("%[^\n]%*c", pessoa.nome);
    scanf("%d%*c", &pessoa.id);

    enfileirar(&aliados, pessoa);

    scanf("%[^\n]%*c", pessoa.nome);
    scanf("%d%*c", &pessoa.id);

    enfileirar(&imperio, pessoa);

    scanf("%[^\n]%*c", pessoa.nome);
    scanf("%d%*c", &pessoa.id);

    enfileirar(&imperio, pessoa);

   
    mostraFila(&aliados);
    mostraFila(&imperio);

    pessoa = desenfileirar(&aliados);
    pessoa = desenfileirar(&imperio);

    mostraFila(&aliados);
    mostraFila(&imperio);

    return 0;
}