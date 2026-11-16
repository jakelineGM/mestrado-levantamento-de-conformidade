#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{
  char nome[101];
  int idade;
} Pessoa;

typedef struct No{
  struct No* prox;
  Pessoa pessoa;
} No;

typedef struct{
  No* prim;
  No* ult;
} Fila;

Fila* cria_fila(){
  Fila* f=(Fila*)malloc(sizeof(Fila));
  f->prim=NULL;
  f->ult=NULL;
  return f;
}

No* novo_no(Pessoa p){
  No* n=(No*)malloc(sizeof(No));
  n->pessoa=p;
  n->prox=NULL;
  return n;
}

void insere_fila(Fila* f, Pessoa p){
  No* novo=novo_no(p);
  if(f->prim==NULL){
    f->prim=f->ult=novo;
    return;
  }
  if(p.idade < 80){
    f->ult->prox=novo;
    f->ult=novo;
  }else{
    No* atual=f->prim;
    No* ultimo_idoso=NULL;
    while(atual != NULL){
      if(atual->pessoa.idade >= 80){
        ultimo_idoso = atual;
      }
      atual =atual->prox;
    }
    if(ultimo_idoso==NULL){
      novo->prox=f->prim;
      f->prim=novo;
    }else{
      novo->prox=ultimo_idoso->prox;
      ultimo_idoso->prox=novo;
      if(ultimo_idoso==f->ult){
        f->ult=novo;
      }
    }
  }
}

void imprime_fila(Fila* f){
  No* atual=f->prim;
  while(atual!=NULL){
    printf("%s - %d\n", atual->pessoa.nome, atual->pessoa.idade);
    atual=atual->prox;
  }
}

void libera_fila(Fila* f){
  No* atual=f->prim;
  while(atual!=NULL){
    No* temp=atual;
    atual =atual->prox;
    free(temp);
  }
  free(f);
}

int main(){
  Fila* fila=cria_fila();
  Pessoa p;
  char linha[150];

  while(fgets(p.nome,sizeof(p.nome),stdin)!= NULL){
    p.nome[strcspn(p.nome,"\n")]='\0';
    if(fgets(linha,sizeof(linha),stdin)==NULL) break;
    p.idade = atoi(linha);
    insere_fila(fila,p);
  }

  imprime_fila(fila);
  libera_fila(fila);

  return 0;
}


