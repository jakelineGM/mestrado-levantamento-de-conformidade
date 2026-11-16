#include <stdio.h>
#include <stdlib.h>

typedef struct no {
    int dado;
    struct no* prox;
} tipoNo;

typedef struct {
    tipoNo* topo;
} tipoPilha;

tipoNo* criaNo(int dado, tipoNo* topo) {
    tipoNo* novo = (tipoNo*) malloc(sizeof(tipoNo));
    novo->dado = dado;
    novo->prox = topo;
    return novo;
}

// ADICIONE AS IMPLEMENTAÇÕOES  DAS OPERAÇÕES DA PILHAS
// IMPLEMENTADAS NAS QUESTOES ANTERIORES

void criaPilha(tipoPilha* pilha) {
  pilha->topo = NULL;
  }
void empilha(tipoPilha* pilha, int dado) {
  tipoNo *aux ;
  aux = (tipoNo*) malloc(sizeof(tipoNo));
  aux->dado = dado;
  aux->prox = pilha->topo;
 pilha->topo = aux;
      
  }

 void desempilha(tipoPilha* pilha) {
  tipoNo *aux= pilha->topo;
   
if(pilha->topo){
  pilha->topo = aux->prox;

  free(aux);
}
   
}

// MODIFIQUE A SEGUINTE FUNÇÃO PARA FAZER O QUE FOI PEDIDO NA QUESTAO
void inserirElemVetorPilha(int vetor[], int k, tipoPilha* pilha){


  for(int i=0;i<k;i++){
    empilha(pilha, vetor[i]);
  }


  
}

// END FUNCAO DA QUESTAO


void mostraPilha(tipoPilha* pilha) {
    tipoNo* aux = pilha->topo;    
    while(aux) {
        printf("%d\n", aux->dado);
        aux = aux->prox;
    }
}

int main() {
    int k;
    tipoPilha p1;
    
    criaPilha(&p1);

    scanf("%d", &k);

    int vetor[k];

    for(int i = 0; i < k; i++) {
        scanf("%d", &vetor[i]);
    }

    inserirElemVetorPilha(vetor, k, &p1);

    mostraPilha(&p1);

    return 0;
}