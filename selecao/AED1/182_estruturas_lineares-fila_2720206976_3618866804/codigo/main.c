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
// SUAS FUNCOES DEVEM COMPLEMENTAR O PROGRAMA PRINCIPAL
// ELE JA TEM CHAMADAS PARA SUAS FUNCOES
void criaFila(tipoFila* fila){
  fila->inicio = NULL;
  fila->fim = NULL;
}

void enfileirar(tipoFila* fila, tipoDados dados){
  tipoNo* novo = (tipoNo*) malloc(sizeof(tipoNo));
  novo->dados = dados;
  novo->prox = NULL;
  if(fila->fim){
    fila->fim->prox = novo;
  }else{
    fila->inicio = novo;
  }
  fila->fim = novo;
}

tipoDados desenfileirar(tipoFila* fila){
  tipoNo* tmp = fila->inicio;
  fila->inicio = tmp->prox;
  tipoDados d = tmp->dados;
  free(tmp);
  return d;
}

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