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
    tipoNo* topo;
} tipoPilha;

// Funcoes a serem feitas. 
// Coloque os includes necessários para seu para o seu 
// programa aqui
// SUAS FUNCOES DEVEM COMPLEMENTAR O PROGRAMA PRINCIPAL
// ELE JA TEM CHAMADAS PARA SUAS FUNCOES

void criaPilha(tipoPilha *p){
  p -> topo = NULL;
}
tipoDados desempilha(tipoPilha *p){
  tipoNo*aux, *temp;
  tipoDados pessoa;
  aux = p->topo;
  if(aux){
    pessoa = aux -> dados;
    if(aux -> prox == NULL){ // se o elemento tiver so um 
      p -> topo = NULL;
      free(aux);
    } else{ // se o elemento for >= 2
      temp = aux;
      p -> topo = aux -> prox;
      free(temp);
    }
  }
  return pessoa;
}
void empilha(tipoPilha *p, tipoDados dado){
  tipoNo *aux;
  aux = malloc(sizeof(tipoNo));
  strcpy(aux -> dados.nome, dado.nome);
  aux -> dados.id = dado.id;

  if(p-> topo == NULL){

    p -> topo = aux;
    aux -> prox = NULL;
  } else{
      aux -> prox = p -> topo;
      p -> topo = aux;
  }
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