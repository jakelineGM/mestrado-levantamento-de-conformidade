# Ordenação de Vetor com Quick Sort

Faça uma função que receba como parâmetro um vetor de pessoas do tipoPessoa, e seu número de elementos. A função deve ordenar o vetor recebido em ordem decrescente de altura utilizando o método quicksort.
typedef struct {
 char nome[30];
 char endereco[20];
 float altura; 
} tipoPessoa;

typedef struct tipoNo {
 tipoPessoa dado;
 struct tipoNo *prox;
} tipoNo;

typedef struct tipoLista {
 tipoNo *prim;
} tipoLista;
