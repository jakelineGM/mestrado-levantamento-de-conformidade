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
void criaFila (tipoFila *f){
  f -> inicio = NULL;
  f -> fim = NULL;
}
void enfileirar (tipoFila *f,tipoDados pessoa ){
  tipoNo* aux;
  aux = (tipoNo*)malloc(sizeof(tipoNo));
  if (f -> inicio == NULL){
    f -> inicio = aux;
    f -> fim = aux;
    aux -> dados = pessoa;
    aux -> prox = NULL;
  }else{
    aux -> dados = pessoa;
    f -> fim -> prox = aux;
    f -> fim = aux;
    aux -> prox = NULL;
  }
}

tipoDados desenfileirar (tipoFila *f){
  tipoDados temp;
  tipoNo* aux;

  aux = f -> inicio;
  if (f -> inicio == NULL){
    strcpy(temp.nome,"");
    temp.id = 0;
    return temp;
  }else if(f -> inicio  == f -> fim){
    f -> inicio = NULL;
    f -> fim = NULL;
    temp = aux -> dados;
    free(aux);
    return temp;
  }else{
    f -> inicio = aux -> prox;
    temp = aux -> dados;
    free (aux);
    return temp;
  }
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