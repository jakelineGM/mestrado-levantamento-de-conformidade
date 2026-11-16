# Removendo Maior Elemento de uma Lista Encadeada

Faça uma função para remover o elemento com maior valor de uma lista encadeada do tipoLista. A função deve retornar o maior valor achado, retornando zero caso a lista seja vazia.
Considere que os valores da lista encadeada fornecida são todos positivos.

typedef struct tipoNo {
 int valor;
 struct tipoNo *prox;
} tipoNo;

typedef struct tipoLista {
 tipoNo *prim;
} tipoLista;
