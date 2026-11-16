#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct {
  char nome[101];
  int idade;
} Pessoa;

typedef struct No {
  struct No* prox;
  Pessoa pessoa;
} No;

typedef struct {
  No *prim;
  No* ult;
} Fila;

Fila* cria_fila() {
  Fila* f = (Fila*) malloc(sizeof(Fila));
  f->prim = f->ult = NULL;
  return f;
}

void insere_fila(Fila* f, Pessoa p) {
  No* novo = (No*) malloc(sizeof(No));
  novo->pessoa = p;
  novo->prox = NULL;

  if(p.idade < 80) {
    if(f->prim == NULL) {
      f->prim = f->ult = novo;
    }
    else {
      f->ult->prox = novo;
      f->ult = novo;
    }
  }else{
    if(f->prim == NULL) {
      f-> prim = f->ult = novo;
    }else if (f->prim ->pessoa.idade < 80) {
      novo->prox = f->prim;
      f->prim = novo;
      
    }else {
      No* atual = f->prim;
      while (atual->prox != NULL && atual->prox->pessoa.idade >= 80) {
        atual = atual->prox;
      }
      novo->prox = atual->prox;
      atual->prox = novo;

      if(novo->prox == NULL) f->ult = novo;
    }
  }
} 

void imprime_fila(Fila* f){
  No* atual = f->prim;
  while(atual != NULL) {
    printf("%s - %d\n", atual->pessoa.nome, atual->pessoa.idade);
    atual = atual->prox;
  }
}

void destroi_fila(Fila* f) {
  No* atual = f->prim;
  while(atual != NULL) {
    No* temp = atual;
    atual = atual->prox;
    free(temp);
  }
  free(f);
}

int main() {
  Fila* fila = cria_fila();

  Pessoa p;

  while(scanf(" %[^\n]",p.nome) != EOF) {
    if (scanf("%d", &p.idade) != 1) break;
    insere_fila(fila, p);
  }
  imprime_fila(fila);
  destroi_fila(fila);

  return 0;
}





