# Radix Sort

Teste do RadixSort
Escreva um programa para testar o Radix Sort.
Seu programa deverá ler uma lista de números inteiros positivos e ordená-los pelo método RadixSort com a base 10.
Para fins de teste, imprima o resultado de cada ordenação parcial, isto é, a ordenação pelo último dígito mais significante, depois o penúltimo, o antepenúltimo etc.

## Dicas

Faça divisões por 1, 10, 100, 1000... e depois extraia o resto da divisão por 10 para saber o valor do dígito com o qual você precisa ordenar o vetor
Use uma variável que começa valendo 1 e vá multiplicando essa variável por 10 para encontrar os divisores 1, 10, 100, 1000...
Quando o divisor for maior que o maior valor da lista, a ordenação estrá finalizada
