#include <stdio.h>
#include <string.h>
#include <stdlib.h>




typedef int tipoDados;


typedef struct tipoNo {
  tipoDados d;
  struct tipoNo *prox;
} tipoNo;

typedef struct tipoList {
  tipoNo *prim;
} tipoLista;



void mostraLista(tipoLista *pLista) {
  tipoNo *aux;

  aux = pLista->prim;

  while(aux) {
    printf("%d\n",aux->d);
    aux = aux->prox;
  }
}



void insereNaLista(tipoLista *pLista, tipoDados *al) {

  tipoNo *aux;
  aux = (tipoNo *) malloc (sizeof(tipoNo) );
  aux->d = *al;
  aux->prox = pLista->prim;
  pLista->prim = aux;
}



void criaLista(tipoLista *pLista) {
  pLista->prim = NULL;
}


// FACA AQUI SUA FUNCAO
void removeDaLista(tipoLista *pLista, int k){
  if(k<1 || pLista->prim == NULL){
    return;
  }
  tipoNo *aux = pLista->prim;
  tipoNo *temp;
  
  if(k==1){
    temp = pLista->prim;
    pLista->prim = temp->prox;
    free(temp);
    return;
  }
  
  int cont;
  cont = 1;
  while(aux && aux->prox){
    if(cont == k-1){
      temp = aux->prox;
      aux->prox = temp->prox;
      free(temp);
      return;
    }
    aux = aux->prox;
    cont++;
  }
}
// FIM DA SUA FUNCAO

void lerValoresParaLista(tipoLista *p, int tam) {
  int val;
 
  for(int x = 0; x< tam; x++) {
    scanf("%d%*c",&val);
    insereNaLista(p,&val);
  }
}





int main() {
  tipoLista l1;
  int k;
  int tam;

  criaLista(&l1);
  scanf("%d%*c",&tam);
  lerValoresParaLista(&l1,tam);
  scanf("%d%*c",&k);

  mostraLista(&l1);
  printf("Removendo a posicao %d\n",k);
  removeDaLista(&l1,k);
  scanf("%d%*c",&k);
  mostraLista(&l1);
  printf("Removendo a posicao %d\n",k);
  removeDaLista(&l1,k);
  mostraLista(&l1);
}