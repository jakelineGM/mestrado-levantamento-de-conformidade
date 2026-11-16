# Ordenação parcial com bubble sort

Ordenação parcial do vetor
Normalmente, a saída de um algoritmo de ordenação é uma permutação na qual todos os elementos de um vetor estão em alguma ordem específica. Por exemplo, se a entrada for a seguinte sequência:
6,2,7,1,5,4,3,8
Então a saída certa deve ser a seguinte:
1,2,3,4,5,6,7,8
Entretanto, existem situações nas quais não queremos ordenar todos os elementos. Uma ordenação parcial é uma permutação na qual apenas os K primeiros elementos de um vetor estão em ordem. Os demais podem permanecer em qualquer ordem. Por exemplo, se a entrada for a seguinte sequência:
6,2,7,1,5,4,3,8
Então uma ordenação parcial com K=3 pode produzir o seguinte resultado:
1,2,3,6,4,7,5,8
Note que apenas os três primeiros elementos do vetor estão em ordem. Os demais não estão necessariamente em ordem.
Escreva uma versão modificada do algoritmo Bubble Sort para fazer ordenação parcial do vetor. Sua função deverá percorrer o vetor da direita para a esquerda e parar após K passagens.

Entrada e saída
A entrada conterá várias linhas a serem processadas. Cada linha será uma tupla na forma (K,lis), sendo que K indica que você deve ordenar os K primeiros elementos e lis contém a lista a ser parcialmente ordenada.
Para cada linha da entrada, imprima a lista parcialmente ordenada em notação Python.
A entrada acaba quando aparecer uma tupla vazia. A leitura dos casos já está escrita no código inicial.
