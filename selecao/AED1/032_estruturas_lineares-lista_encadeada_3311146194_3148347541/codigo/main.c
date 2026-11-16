#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct {
    char nome[30];
    char endereco[20];
    float altura;
} tipoPessoa;

typedef struct no tipoNo;
struct no {
    tipoPessoa dado;
    tipoNo* prox;
};

typedef struct {
    tipoNo* prim;
} tipoLista;

void iniciaLista(tipoLista* lista) {
    lista->prim = NULL;
}

void inserePessoas(tipoLista* lista) {
    tipoPessoa pessoa;
    scanf("%[^\n]%*c", pessoa.nome);
    while (strcmp(pessoa.nome, "FIM") != 0) {
        tipoNo* novo = (tipoNo*) malloc(sizeof(tipoNo));
        scanf("%[^\n]%*c", pessoa.endereco);
        scanf("%f%*c", &pessoa.altura);
        novo->dado = pessoa;
        novo->prox = lista->prim;
        lista->prim = novo;
        scanf("%[^\n]%*c", pessoa.nome);
    }
}



// COMPLETE A FUNCAO
void imprimeAlturaPosicaoPar(tipoLista* lista) {
  tipoNo*curr = lista->prim;
  int i = 1;
  while(curr->prox != NULL) {
    if(i%2==0){
      printf("%.2f\n", curr->dado.altura);
    }
    curr = curr->prox;
    i++;
  }
  
}


int main() {
    tipoLista lista;
    iniciaLista(&lista);
    inserePessoas(&lista);
    imprimeAlturaPosicaoPar(&lista);
    return 0;
}