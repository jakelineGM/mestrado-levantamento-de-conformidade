#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct {
    float altura;
    char nome[30];
    char endereco[20];
} tipoPessoa;

typedef struct no tipoNo;
struct no {
    tipoPessoa dado;
    tipoNo* prox;
};

typedef struct {
    tipoNo* prim;
} tipoLista;

tipoLista* criaLista() {
    tipoLista* lista = (tipoLista*) malloc(sizeof(tipoLista));
    lista->prim = NULL;
    return lista;
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

// COMPLETE A FUNCAO A SEGUIR
void imprimeAlturasAoContrario(tipoNo* prim) {
  
  if(prim){
    imprimeAlturasAoContrario(prim->prox);
    printf("%.2f ",prim->dado.altura);
  }
}

int main() {
    tipoLista* lista = criaLista();
    inserePessoas(lista);
    imprimeAlturasAoContrario(lista->prim);
    return 0;
}