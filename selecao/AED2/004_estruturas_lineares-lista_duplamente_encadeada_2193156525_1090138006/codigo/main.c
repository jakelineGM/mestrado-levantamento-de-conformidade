#include <stdio.h>
#include <stdlib.h>

struct lista
{
  struct nodo* prim;
  int tam;
};

struct nodo
{
  int elem;
  struct nodo* prox;
  struct nodo* ant;
};

struct lista * cria_lista(void)
{
  struct lista *nova = malloc(sizeof *nova);
  nova->prim = NULL;
  nova->tam = 0;
  return nova;
}

struct nodo * cria_nodo(int valor)
{
  struct nodo *novo = malloc(sizeof *novo);
  
  /* Leitura do elem do programa e leitura do
  tempo total de execucao do program */  

  novo->elem = valor;
  
  //printf("nodo inserido: %s %d\n", novo->elem, novo->tempo_restante);
  // Atribui valores iniciais para os ponteiro do no'
  novo->ant = NULL;
  novo->prox = NULL;
  
  return novo;
}

void insere_fim(struct lista* lst, struct nodo* nodo)
{
  if(lst->prim == NULL){
    lst->prim = nodo;
    nodo->prox = nodo;
    nodo->ant = nodo;
    lst->tam++;
    //printf("oi");
    return; 
  }
  struct nodo* organizaSentido = lst->prim;
  while(organizaSentido->prox != lst->prim){
    organizaSentido = organizaSentido->prox;
  }

  organizaSentido->prox = nodo;
  nodo->ant = organizaSentido;
  nodo->prox = lst->prim;
  lst->prim->ant = nodo;
  lst->tam++;

}

void insere_ate_N(struct lista* lst, int N){

  for(int i = 0; i<N;i++){
    struct nodo* novo_nodo = cria_nodo(i+1);
    insere_fim(lst,novo_nodo);
  }
  return;
}

void imprime_lista_valores(struct lista* lst){
  if(lst->prim == NULL) return;
  struct nodo * organizaSentido = lst->prim;
    printf("%d ", organizaSentido->elem);
    organizaSentido = organizaSentido->prox;
  while(organizaSentido !=lst->prim){
    printf("%d ", organizaSentido->elem);
    organizaSentido = organizaSentido->prox;
  }
  printf("\n");
  return; 
}

/*passos incriveis para inverter uma lista 
  1- Inverte todos os ponteiros prox pelo ant e
  vice-versa -> caso interno, sem contar ponta
  2- Ponta EsquerdaConserta Ponteiro recebido do Final e Conserta
*/

struct nodo* copia_nodo(struct nodo* copiado){
  struct nodo* copia;
  copia = (struct nodo*)malloc(sizeof(struct nodo*));
  if(copia == NULL){
    return NULL;
  }
  copia->elem = copiado->elem;
  copia->prox = copiado->prox;
  copia->ant = copiado->ant;
  return copia;
}

void organizarPonteirosAnt(struct lista* lst){
  struct nodo* anterior = lst->prim;
  struct nodo* atual = anterior->prox;
  while(atual != lst->prim){
    atual->ant = anterior; 
    
    anterior = atual;
    atual = atual->prox;
  }
  atual->ant = anterior; 
}

void listaInversaEmNPonto(struct lista* lst, int Ponto){
  if(lst == NULL || lst->prim == NULL || 
     lst->prim->prox == lst->prim || lst->tam < Ponto ) return;
  
  struct nodo* limiteInversao = lst->prim;
  struct nodo* ultimoNo = lst->prim->ant;
  struct nodo* novoComeco;
  int ultimoElemento = 1;
  struct nodo* organizaSentido;
  while(limiteInversao->elem != Ponto){ //Esse elemento também vai ser invertido
    limiteInversao = limiteInversao->prox; 
  } //limiteINverso é o novocomeco
  novoComeco = limiteInversao->prox;
  ultimoNo->prox = limiteInversao;  // ajeita o final pra apontar na ordem certa
  struct nodo* savePonteiroProXD = copia_nodo(limiteInversao); // so quero o ponteiro prox
  organizaSentido = limiteInversao;
  
  while(lst->prim != organizaSentido){
    organizaSentido->prox = organizaSentido->ant;
    ultimoElemento++;
    organizaSentido = organizaSentido->ant;
  }
  organizaSentido->prox = savePonteiroProXD->prox; 
  free(savePonteiroProXD);
 
  if(lst->tam == ultimoElemento){
    lst->prim = novoComeco->prox;
  }else{
    lst->prim = novoComeco;
  }

  organizarPonteirosAnt(lst);
  
}

int main(void){
  int ponto;
  int tamanho_lista;
  struct lista* lst;
  lst = cria_lista();
  scanf("%d\n", &tamanho_lista);
  insere_ate_N(lst,tamanho_lista);

  scanf("%d ", &ponto);
  listaInversaEmNPonto(lst, ponto); 
  while(scanf("%d",&ponto),ponto != 0){    
    listaInversaEmNPonto(lst, ponto);

  }
  
  imprime_lista_valores(lst);

}