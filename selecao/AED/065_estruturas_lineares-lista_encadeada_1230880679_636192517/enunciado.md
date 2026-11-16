# Triplas na lista ligada

Triplas
Escreva um programa que lê uma lista de inteiros x1​,x2​,x3​,…, que pode ser arbitrariamente longa. Em seguida, leia um único inteiro qi​, indicando que todas as ocorrências desse número devem ser removidas da lista. Se a lista resultante contiver uma sequência de no mínimo três elementos consecutivos de mesmo valor, a saída deverá ser a palavra "tripla". Caso contrário, a saída deve ser a palavra "nada".

Entrada e Saída
A entrada começa com um inteiro N, indicando o número de listas a serem processadas.
Em seguida aparecem N linhas indicando o conteúdo de cada lista e o número a ser removido. O conteúdo de cada lista é separado do número a ser removido pelo sentinela 0. Observe que, em alguns casos, o número a ser removido pode não existir na lista e, em outros, a lista pode começar ou ficar vazia depois da remoção.
Para cada lista, imprima "tripla" ou a palavra "nada" conforme explicado no enunciado.

Dicas
Para ilustrar, veja a seguinte entrada de exemplo, que contém duas listas.
2
1 2 3 4 3 4 3 4 0 3
1 2 3 0 1
O conteúdo da primeira lista é (1, 2, 3, 4, 3, 4, 3, 4) e o valor a ser removido é o 3. A lista resultante será (1, 2, 4, 4, 4), que possui três ocorrências consecutivas do elemento 4. Portanto você deve imprimir a palavra  "tripla".
A segunda lista é (1, 2, 3) e o elemento a ser removido é 1. A lista resultante será (2, 3), que não possui três ocorrências repetidas de nenhum elemento. Portanto a palavra "nada" deve ser impressa.
