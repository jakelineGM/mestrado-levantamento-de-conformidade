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

void criaFila(tipoFila *fila) {
  fila->inicio = NULL;
  fila->fim = NULL;
}

void enfileirar(tipoFila *fila, tipoDados dado) {
  tipoNo *no = (tipoNo *) malloc(sizeof(tipoNo));
  no->dados = dado;
  
  if (!fila->inicio) {
    fila->inicio = fila->fim = no;
  } else {
    fila->fim->prox = no;
  }
}

tipoDados desenfileirar(tipoFila *fila) {
  tipoNo* inicio = fila->inicio;
  tipoDados dado = inicio->dados;
  
  fila->inicio = fila->inicio->prox;
  free(inicio);
  
  return dado;
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