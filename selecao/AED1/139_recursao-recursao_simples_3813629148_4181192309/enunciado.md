# ANDANDO NA MATRIZ RECURSIVAMENTE

ANDANDO NA MATRIZ RECURSIVAMENTE
Ande na matriz recursivamente dada uma posição X,Y e imprima todos os elementos acima dessa posição, abaixo dessa posição, a direita da posição e ao fim a esquerda da posição. Siga a ordem estabelecida.
Defina o tamanho N como 12 para inicializar a matriz, a matriz não será maior que 12x12;
Após a posição será definido o tamanho da matriz senho X(linha) <= N e Y(coluna) <= N;
Ao fim faça a leitura dos valores da matriz;

## Dicas

Faça uma Função recursiva para cada direção;
exemplo:
1 2 3
4 5 6
7 8 9
A posição 1,1 é 5 e eu quero todos os elementos a direita do 5 recursivamente tendo apenas o 6;
Estabeleça uma função que ande apenas para direita até o fim do tamanho inicial.
Faça uma função que valide que a posição é maior ou igual a zero e menor que o tamanho da matriz. ESSE SERÁ UM CASO DE PARADA.
