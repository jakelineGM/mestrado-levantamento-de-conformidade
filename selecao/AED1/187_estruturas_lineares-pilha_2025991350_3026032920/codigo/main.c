#include <stdio.h>
#include <stdlib.h>

typedef struct { 
    char nome[20];
    int id;
} tipoDados;

typedef struct no {
    tipoDados dados;
    struct no* prox;
} tipoNo;

typedef struct {
    tipoNo* topo;
} tipoPilha;

// Funcoes a serem feitas. 
// Coloque os includes necessários para seu para o seu 
// programa aqui
// SUAS FUNCOES DEVEM COMPLEMENTAR O PROGRAMA PRINCIPAL
// ELE JA TEM CHAMADAS PARA SUAS FUNCOES

void criaPilha(tipoPilha *p){
  p->topo = NULL;
}

void empilha(tipoPilha *p, tipoDados d){
  tipoNo *aux = (tipoNo*) malloc(sizeof(tipoNo));
  aux->dados = d;
  aux->prox = p->topo;
  p->topo = aux;
}

tipoDados desempilha(tipoPilha *p){
    tipoDados *aux = (tipoDados*) malloc(sizeof(tipoDados));
    if(p->topo){
      aux = &p->topo->dados;
      p->topo = p->topo->prox;}
      return *aux;
}



// FIM DO SEU CODIGO


void mostraPilha(tipoPilha* pilha) {
    tipoNo* aux= pilha->topo;	
    while(aux) {
	    printf("%s\n",aux->dados.nome);
	    printf("%d\n",aux->dados.id);
		aux = aux->prox;
	}
}

int main() {
	tipoDados pessoa;
	tipoPilha p1;
	tipoPilha p2;
	
	criaPilha(&p1);
	criaPilha(&p2);
	
	scanf("%[^\n]%*c",pessoa.nome);
	scanf("%d%*c",&pessoa.id);
	empilha(&p1,pessoa);
	
	scanf("%[^\n]%*c",pessoa.nome);
	scanf("%d%*c",&pessoa.id);
	empilha(&p1,pessoa);
	
	pessoa = desempilha(&p1);
	empilha(&p2,pessoa);
	
	scanf("%[^\n]%*c",pessoa.nome);
	scanf("%d%*c",&pessoa.id);
	empilha(&p1,pessoa);
	
	scanf("%[^\n]%*c",pessoa.nome);
	scanf("%d%*c",&pessoa.id);
	empilha(&p1,pessoa);
	
	pessoa = desempilha(&p1);
	empilha(&p2,pessoa);
	
	mostraPilha(&p1);
	mostraPilha(&p2);	
}