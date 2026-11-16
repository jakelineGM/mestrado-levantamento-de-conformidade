# Elemento no início ou no fim da lista ligada?

Início, meio ou fim?
Crie uma estrutura de lista ligada e implemente a operação de inserção no início. Em seguida, faça um programa principal que lê uma lista e depois uma série de consultas. Cada consulta será um número e você deverá dizer, de maneira bem aproximada, onde o elemento se encontra na lista.

Entrada
Inicialmente, haverá uma sequência de valores inteiros positivos x1​,x2​,…,0. Cada valor xi​ é um elemento que deve ser inserido no início da lista. O zero é apenas um sentinela para indicar o fim dos elementos a serem inseridos.
Em seguida, haverá uma série de consultas q1​,q2​,q3​,…,0. O zero é um sentinela e indica que as consultas terminaram.

Saída
Para cada consulta, imprima uma das seguintes mensagens:
%d: inicio: se o elemento é o primeiro da lista
%d: fim: se o elemento é o último da lista
%d: existe: se o elemento está na lista, mas não é o primeiro, nem o último
%d: nao existe: se o elemento não está na lista
Se o elemento for o primeiro e o último ao mesmo tempo, imprima %d: inicio.

## Dicas

O código inicial possui uma definição de estrutura de lista ligada que inclui os tipos Nodo, para representar nós da lista ligada, e Lista. A estrutura do tipo Lista guarda um ponteiro para o primeiro e para o último nós da lista ligada.
A função para criar uma lista vazia já está pronta.
Você pode completar o código da função lst_insere_inicio para criar e inserir um nó no começo da lista. Manipule cuidadosamente os ponteiros prim e fim da lista ligada.
Você pode completar o código da função lst_busca para buscar na lista ligada um nó que contém um certo valor. Se esse nó for encontrado, a função deverá retornar seu endereço. Caso contrário, a função pode retornar NULL.
Na função main, você pode usar as funções que você completou. Para cada valor de consulta, pesquise na lista a existência de um nó. Se o nó for encontrado, você poderá compará-lo com os ponteiros prim e fim da lista ligada para saber se esse nó está no início ou no fim da lista.
Você pode reutilizar as partes do código que quiser, incluindo apagar todo o código inicial e escrever o seu próprio.
