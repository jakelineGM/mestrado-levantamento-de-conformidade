# Algoritmo de euclides recursivo (maximo divisor comum)

Algoritmo de Euclides Recursivo
Elabore uma função recursiva que calcula o máximo divisor comum (mdc) de dois números a e b utilizando o Algoritmo de Euclides.
O algoritmo de Euclides pode ser descrito por meio das seguintes regras:
Se b = 0, então o mdc entre os dois números será a
Senão, então o mdc entre entre eles será o mdc entre b e o resto da divisão de a por b
Por exemplo, para encontrarmos o mdc entre 15 e 18, fazemos os seguintes passos:

Portanto, o máximo divisor comum entre 15 e 18 é 3.
Escreva um programa que lê uma porção de pares de números inteiros positivos e imprime o mdc entre eles. Todos os números serão maiores que zero, exceto o último par, que será 0 0 para indicar o fim do caso de teste.

## Dicas

Escreva primeiro uma relação de recorrência na forma

antes de começar a codificar. Em pelo menos um dos casos da relação, a função \text{mdc} aparecer ao lado direito, indicando a recursão.
