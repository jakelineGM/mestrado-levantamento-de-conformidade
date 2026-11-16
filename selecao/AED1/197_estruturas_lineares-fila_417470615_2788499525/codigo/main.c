#include <stdlib.h>
#include <stdio.h>
#include<string.h>

typedef struct pessoa Pessoa;
typedef struct no No;
typedef struct fila Fila;

struct pessoa{
  char nome[101];
  int idade;
};

struct no{
  No *prox;
  Pessoa pessoa;
};

struct fila{
  No *prim;
  No *ult;
};

Fila * cria_fila(){
  Fila *f = malloc(sizeof(Fila));
  f->prim = NULL;
  f->ult = NULL;
  return f;
}
void insere_fila(Fila *f, Pessoa p){
  No *novo = malloc(sizeof(No));
  novo->pessoa.idade = p.idade;
  strcpy(novo->pessoa.nome, p.nome);
  novo->prox = NULL;
  if(f->ult != NULL){
    f->ult->prox = novo;
  }else{
    f->prim = novo;
  }
  f->ult = novo;
}
void imprime_fila(Fila *f){
  No *p;
  for(p = f->prim; p != NULL; p = p->prox){
    printf("%s - %d\n", p->pessoa.nome, p->pessoa.idade);
  }
}
void une_fila(Fila *normal, Fila *pref){
  if(pref->prim != NULL){
    pref->ult->prox = normal->prim;
    normal = pref;
  }
}
int main(){
  Fila *f = cria_fila();
  Fila *pref = cria_fila();
  Pessoa p;
  
  while(scanf("%[^\n]", p.nome) != EOF){
    scanf("%d", &p.idade);
    if(p.idade >= 80 && p.idade != 0){
      insere_fila(pref,p);
    }else if(p.idade != 0){
      insere_fila(f,p);
    }
    p.idade = 0;
  }
  imprime_fila(pref);
  imprime_fila(f);
  return 0;
}