# Passos do Insertion Sort

Passos do Insertion Sort
Escreva uma função que implementa o algoritmo de ordenação Insertion Sort (método da inserção), mas com uma modificação:
Sua função deverá imprimir o conteúdo completo da lista antes de começar a ordenar;
Sua função deverá imprimir a lista completa sempre que algum valor da lista for modificado. Não imprima quando você fizer atribuições que não alterem valores da lista.
Veja os exemplos a seguir para entender como proceder.

Exemplo 1
Na entrada abaixo, apenas o valor 2 está fora de lugar, portanto os elementos 3 e 4 precisam ser copiados para a direita.
[1, 3, 4, 2, 5, 6]
A saída esperada é a seguinte:
[1, 3, 4, 2, 5, 6]
[1, 3, 4, 4, 5, 6]
[1, 3, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
A linha 1 da saída contém a lista original. As linhas subsequentes mostram os valores que foram modificados para inserção do elemento 2 na sua posição correta.

Exemplo 2:
Na entrada abaixo, apenas o valor 3 está fora de lugar e existem várias ocorrências do elemento 4, além de uma ocorrência do elemento 5, que precisam ser copiadas para a direita.
[1, 2, 4, 4, 4, 4, 5, 3, 6, 6]
Saída esperada:
[1, 2, 4, 4, 4, 4, 5, 3, 6, 6]
[1, 2, 4, 4, 4, 4, 5, 5, 6, 6]
[1, 2, 4, 4, 4, 4, 4, 5, 6, 6]
[1, 2, 3, 4, 4, 4, 4, 5, 6, 6]
A linha 1 da saída contém a lista original.
Na linha 2, o valor 5 foi copiado para a direita, substituindo o 3.
Na linha 3, o valor 4 foi copiado para a direita, substitutindo o 4. Observe que o Insertion Sort copia todas as ocorrências do valor 4 para a direita, como qualquer algoritmo de inserção em lista. Mas como essas cópias não alteram o conteúdo do vetor, nada é impresso.
A próxima impressão ocorrerá apenas quando o elemento 3 for inserido na sua posição correta, gerando a linha 4 da saída.
