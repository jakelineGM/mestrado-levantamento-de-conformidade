# Fila Banco

Em um certo banco sempre que um cliente chega ao local ele deve entrar no final da fila de atendimento. No entanto, caso o cliente tenha 80 anos ou mais ele deve entrar no início da fila. Além disso, se um cliente dessa faixa etária chegar no banco e houverem outros clientes da mesma faixa etária na fila, ele deve ficar atrás do último cliente dessa faixa etária. Implemente um programa que leia vários nomes de clientes e suas respectivas idades e ao final imprima a fila com essas restrições.

## Dicas

//Apenas uma ideia de como organizar as struct
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
