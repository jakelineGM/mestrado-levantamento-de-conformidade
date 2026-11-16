#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct tipoDado {
char nome[50];
}tipoDado;

typedef struct tipoNo{
tipoDado dado;
struct tipoNo *prox;
}tipoNo;

typedef struct tipoFila{
tipoNo *prim, *ult;
}tipoFila;

void criarFila (tipoFila *f){

  f->prim = NULL;
  f->ult = NULL;
  
}

void inserirNaFila (tipoFila *f, tipoDado dado){
  tipoNo *aux;
  aux = (tipoNo*)malloc(sizeof(tipoNo));

  aux -> dado = dado;
  aux -> prox = NULL;

  if(f->prim == NULL){
    f->prim = aux;
  }
  else{
    f->ult->prox = aux;
  }

  f->ult = aux;

}

tipoNo * haElementos(tipoFila *f){
  return f->prim;
}

//Faça sua Função aqui:

void mostrarReverso(tipoFila*f){
  tipoNo *aux,*ultimo;
 
  ultimo = NULL;
  
  if(f->prim){
    while(ultimo != f->prim){
      aux = f->prim;
      while(aux->prox!=ultimo){
        aux = aux->prox;
      }
      printf("%s\n",aux->dado.nome);
      ultimo = aux;
    }
  }
}



int main (){
  tipoFila f;
  tipoDado d;
  int n;


  criarFila(&f);

  scanf("%d%*c",&n);

  while(n){
    scanf("%[^\n]%*c",d.nome);
    inserirNaFila(&f,d);
    n--;
  }
  mostrarReverso(&f);
}















