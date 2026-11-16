# Inserção na árvore binária de busca

Inserção na Árvore Binária de Busca
Elabore uma função recursiva que realiza inserção de chaves em uma árvore binária de busca.
Escreva um programa principal que lê uma série de listas contendo valores inteiros. Cada lista representa os elementos que você deverá inserir em uma árvore binária de busca inicialmente vazia. Pare quando for lida uma lista vazia.
Como saída imprima, para cada árvore processada, o seguinte:
Uma linha contendo o padrão Arvore #, sendo # o número da árvore para facilitar os testes.
Três linhas contendo, respectivamente, as chaves encontradas durante os percursos pré-ordem, in-ordem e pós-ordem.
Uma linha em branco para separar os diferentes casos.

## Dicas

Represente a árvore como um dicionário, assim como nos exercícios anteriores.
Use a função cria_no(valor) para criar um novo nó com a chave valor e a função cria_arvore para criar uma árvore vazia.
Não é necessário preocupar-se com alocação/desalocação de memória, pois o Python possui coleta de lixo.
Se uma árvore T for vazia, a expressão T is None deve ser verdadeira. Use o operador is para verificar se você chegou a uma sub-árvore vazia no algoritmo de inserção.
