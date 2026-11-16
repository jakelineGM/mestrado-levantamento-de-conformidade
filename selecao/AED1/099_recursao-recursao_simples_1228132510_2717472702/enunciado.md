# Raiz quadrada recursiva

Raiz quadrada recursiva
O cálculo da raiz quadrada de um número real x pode ser feito através da seguinte relação de recorrência:
raiz(x,x0​,ε)=⎩⎨⎧​x0​,raiz(x,2x0​x02​+x​,ε),​se ∣x−x02​∣⩽εcaso contraˊrio​,
no qual x é o número cuja raiz queremos calcular, x0​ é uma aproximação inicial de x​ e ε é um erro aceitável.
Escreva uma função reucursiva para estimar a raiz quadrada x​. Em seguida, escreva um programa principal que lê várias configurações de x,x0​ e ε e imprime o valor estimado da raiz quadrada para cada configuração.
A entrada começará com inteiro N indicando o número de testes que você deverá realizar. Em seguida aparecerão N triplas contendo, respectivamente, os valores de x,x0​ e ε, sendo que x é um número inteiro e positivo, enquanto x0​ e ε são números reais.
Para cada tripla lida você deverá imprimir, com 5 casas decimais, o valor da raiz quadrada aproximada.

## Dicas

Use a função fabs() para encontrar o valor absoluto de uma expressão do tipo (double) ou fabfs() para encontrar o valor absoluto de uma expressão do tipo (float). Os protótipos das duas funções estão em <math.h>.
