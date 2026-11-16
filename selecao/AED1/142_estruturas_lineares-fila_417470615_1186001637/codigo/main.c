#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef struct{
  char nome[101];
  int idade;
} Pessoa;

typedef struct No{
  struct No* prox;
  Pessoa pessoa;
} No;

typedef struct{
  No *prim;
  No* ult;
} Fila;

Fila* criar_fila() {
  Fila *fila = malloc(sizeof(Fila));
  fila->prim = NULL;
  fila->ult = NULL;
  return fila;
}

No* criar_no(Pessoa nova_pessoa) {
  No *novo_no = malloc(sizeof(No));
  strcpy(novo_no->pessoa.nome, nova_pessoa.nome);
  novo_no->pessoa.idade = nova_pessoa.idade;
  novo_no->prox = NULL;
  return novo_no;
}

void inserir_inicio(Fila *fila, Pessoa nova_pessoa) {
  No* novo_no = criar_no(nova_pessoa);
  if(fila->prim == NULL) {
    fila->prim = fila->ult = novo_no;
  } else {
    novo_no->prox = fila->prim;
    fila->prim = novo_no;
  }
}

void inserir_final(Fila *fila, Pessoa nova_pessoa) {
  No* novo_no = criar_no(nova_pessoa);
  if(fila->prim == NULL) {
    fila->prim = fila->ult = novo_no;
  } else {
    fila->ult->prox = novo_no;
    fila->ult = novo_no;
  }
}

void inserir_meio(Fila *fila, Pessoa nova_pessoa) {
  No* novo_no = criar_no(nova_pessoa);
  if(fila->prim == NULL) {
    fila->prim = fila->ult = novo_no;
  } else {
    No* atual = fila->prim;
    No* anterior = NULL;
    while(atual->prox != NULL && atual->pessoa.idade >= 80) {
      anterior = atual;
      atual = atual->prox;
    }
    if(anterior == NULL) {
      novo_no->prox = atual->prox;
      atual->prox = novo_no;
    } else {
      anterior->prox = novo_no;
      novo_no->prox = atual;
    }
  }
}

void inserir_pessoa_fila(Fila *fila, Pessoa nova_pessoa) {
  if(nova_pessoa.idade >= 80) {
    if(fila->prim == NULL || fila->prim->pessoa.idade >= 80) {
      inserir_meio(fila, nova_pessoa);
    } else {
      inserir_inicio(fila, nova_pessoa);
    }
  } else {
    inserir_final(fila, nova_pessoa);
  }
}

void imprimir_fila(Fila *fila) {
  No* atual = fila->prim;
  while(atual != NULL) {
    printf("%s - %d\n", atual->pessoa.nome, atual->pessoa.idade);
    atual = atual->prox;
  }
}

void limpar_fila(Fila *fila) {
  No* atual = fila->prim;
  while(atual != NULL) {
    No* aux = atual;
    atual = atual->prox;
    free(aux);
  }
  fila->prim = NULL;
  free(fila);
}



int main(void) {
  Pessoa pessoa;
  Fila *fila = criar_fila();
  while(scanf("%[^\n]%*c %d%*c", pessoa.nome, &pessoa.idade) != EOF) {
    inserir_pessoa_fila(fila, pessoa);
  }

  imprimir_fila(fila);


  limpar_fila(fila);

  return 0;
}