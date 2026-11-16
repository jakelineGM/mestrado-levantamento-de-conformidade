# Passos da busca binária

Passos da Busca Binária
A busca binária é um algoritmo bastante eficiente, com complexidade temporal O(log n) no pior caso.
Neste exercício, você deverá elaborar um programa que verifica essa eficiência. Para isso, você deverá implementar uma versão modificada do algoritmo de busca binária.
Tipicamente, a busca binária retorna o índice do elemento que possui a chave desejada ou -1, se não existir nenhum elemento assim na lista.
A modificação que você deverá fazer é a seguinte: ao invés de retornar -1 ou o índice do elemento encontrado, retorne uma lista contendo todas as chaves que foram verificadas durante a busca.
Por exemplo, se o conteúdo da lista for 
[2,3,5,7,11,13,17,19]
e a chave desejada for k=5, então primeiro será verificado o elemento central v3​=7. Depois será verificado o elemento central da metade esquerda, isto é, v1​=3. Finalmente, o elemento v2​=5, que é o desejado, será verificado.
Se estivéssemos procurando pela chave k=6, então verifricaríamos a mesma sequência de elementos, mas não encontraríamos a chave desejada.
Em ambos os casos, a função deveria retornar a lista [7, 3, 5].

Entrada e Saída
A entrada conterá duas linhas. A primeira será uma lista em notação Python com valores em ordem crescente. A segunda será uma lista de chaves.
Para cada chave da entrada, faça a busca binária e imprima as chaves que foram verificadas pelo algoritmo.
