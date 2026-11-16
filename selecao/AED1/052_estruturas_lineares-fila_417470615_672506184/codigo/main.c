#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct No{
struct No* prox;
int idade;
char nome[101];
char sobrenome[101];
} No;

typedef struct{
No *prim;
No* ult;
} Fno;

Fno* cria_fila(){
  Fno *novo = malloc(sizeof(Fno));
  novo->prim = NULL;
  novo->ult = NULL;
  return novo;
}

void inserir_cliente(Fno *l, char *v, char *s, int num){
  No *novo = malloc(sizeof(No));
  strcpy(novo->nome, v);
  strcpy(novo->sobrenome, s);
  novo->idade = num;
  novo->prox = NULL;
  
  if(num >= 80){
    if(l->prim == NULL){
      //Fila vazia
      l -> prim = novo;
      l -> ult = novo;
    }
    else{
      //Fila não vazia. 
      //Temos 2 casos: mesma faixa etária ou não.

      //Para a mesma faixa etária:

      No* temp = l -> prim;
      No* ant = NULL;

      while(temp != NULL && temp ->idade >= 80){
        ant = temp;
        temp = temp -> prox;
      }

      if(ant == NULL){
        //Estamos no início da fila
        novo->prox = l->prim;
        l->prim = novo;
      }
      else{
        //Inserimos após o último cliente com a faixa etária
        ant -> prox = novo;
        novo -> prox = temp;
      }
    }
  }
  else{
    //Pessoa não idosa. Inserimos ao fim da fila, sem preferências.
    if(l -> ult == NULL){
      //Início da fila com ela vazia
      l -> prim = novo;
      l -> ult = novo;
    }
    else{
      //Fila não vazia
      l -> ult -> prox = novo;
      l -> ult = novo;
    }
  }
}

void imprimir_fila(Fno* l){
  No* q = l ->prim;

  while(q != NULL){
    printf("%s %s - %d \n", q -> nome, q -> sobrenome, q -> idade);
    q = q ->prox;
  }
}

void liberar_fila(Fno* l){
  No* q = l -> ult;
  while(q != NULL){
    No* t = q -> prox;
    free(q);
    q = t;
  }
  free(l);
}

int main(void){
  Fno* fila = cria_fila();

  char nome[101];
  char sobrenome[101];
  int idade;
  while(scanf("%s", nome) != EOF){
    scanf("%s", sobrenome);
    while(getchar() != '\n');
    scanf("%d", &idade);
    inserir_cliente(fila, nome, sobrenome, idade);
  }
  imprimir_fila(fila);
  liberar_fila(fila);
  return 0;
}