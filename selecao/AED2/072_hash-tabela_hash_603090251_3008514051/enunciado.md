# Uma hash simples

Uma hash simples
Faça um programa que lê números inteiros não negativos e os insere em uma tabela de espalhamento usando o método da divisão e sondagem linear. Ao final, imprima o conteúdo da tabela.
Para uma chave k tal que k∈N0 e uma tabela com tamanho m∈N+, a função de espalhamento deve ser
h(k)≡k (mod m).
E a sondagem linear, em caso de colisão, deve ser
h′(k,i)≡(k+i) (mod m).

Entrada
A entrada começa com um valor inteiro 0 < m < 100.000 indicando o tamanho que sua tabela de espalhamento deve ter, seguida por um inteiro 0<n≤m indicando o número de valores que devem ser inseridos na tabela.
Após a configuração da tabela, aparecerão os inteiros x1​,x2​,x3​,…,xn​. Os valores a serem inseridos na tabela serão inteiros não negativos no intervalo 0≤xi​≤4×109.

Saída
Imprima apenas as posições não vazias da tabela usando a seguinte formatação:
Em C/C++: "%d: %d\n", índice, tabela[índice]
Em Python: "%d: %d" % (índice, tabela[índice])
