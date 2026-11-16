# Bubble ou Merge Sort?

Bubble ou Merge Sort?
Escreva um programa que lê um inteiro n e decide se é melhor utilizar o algoritmo Insertion Sort ou o algoritmo Merge Sort para ordenar um vetor de n elementos.
Considere que o tempo do Insertion Sort, no pior caso, é dado por Tb​(n) e o tempo do Merge Sort, em qualquer caso, é dado por Tm​(n).

 Tb​(n)=2n2−3n+1

 Tm​(n)=6nlog2​(n)+8n−6

## Dicas

Calcule o valor de Tb​(n) e Tm​(n) para o número lido do teclado e escolha o algoritmo cuja função de tempo tem o menor valor.
Para calcular um logaritmo em base 2, acrescente a seguinte linha no começo do seu código
from math import log2
Use a chamada log2(n) para calcular o valor de log2​(n).
