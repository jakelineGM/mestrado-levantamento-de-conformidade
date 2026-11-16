#include <stdio.h>
#include <stdlib.h>

// Definição da estrutura do nó
typedef struct no {
    int valor;
    struct no *prox;
} No;

// Definição da estrutura da lista
typedef struct {
    No *inicio;
} Lista;

// Função para criar uma lista vazia
Lista* lst_cria() {
    Lista *l = (Lista*) malloc(sizeof(Lista));
    l->inicio = NULL;
    return l;
}

// Função para inserir elementos no início da lista
void lst_insere(Lista *l, int valor) {
    No *novo = (No*) malloc(sizeof(No));
    novo->valor = valor;
    novo->prox = l->inicio;
    l->inicio = novo;
}

// Função para retornar o último valor da lista
int ultimo(Lista* l) {
    if (l->inicio == NULL) {
        return -1; // Retorna -1 se a lista estiver vazia
    }
    
    No *atual = l->inicio;
    while (atual->prox != NULL) {
        atual = atual->prox;
    }
    return atual->valor;
}

int main(void) {
    Lista *l = lst_cria();

    int n, valor;
    scanf("%d", &n);

    for(int i = 0; i < n; i++) {
        scanf("%d", &valor);
        lst_insere(l, valor);
    }

    printf("Ultimo: %d\n", ultimo(l));

    return 0;
}