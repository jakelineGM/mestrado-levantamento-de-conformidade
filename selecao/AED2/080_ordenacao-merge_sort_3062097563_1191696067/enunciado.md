# Ordenação por mesclagem (chave/valor)

Ordenação por intercalação
Implemente o algoritmo de ordenação por intercalação (merge sort).
Em seguida, use esse algoritmo para ordenar uma coleção do tipo (chave, valor). As chaves serão inteiros não negativos e os valores poderão ser quaisquer coisas imprimíveis em Python (inteiros, reais, strings etc.).

Entrada
A entrada será uma coleção de casos de teste.
Cada caso de teste será uma lista de tuplas (chave, valor). O valor será em notação Python. Use eval para ler o caso de teste.
A entrada termina quando aparecer uma lista vazia.

Saída
Para cada caso de teste, imprima primeiro a mensagem Caso {}, substituindo a sequência {} pelo número do caso de teste.
Em seguida imprima, linha por linha, os valores ordenados (não imprima as chaves).
Imprima uma linha em branco ao final do caso de teste.

Dicas
Faça uma classe para representar cada elemento da lista (exemplo: Elem ou Par). Sua lista deve ser composta por objetos dessa classe. Sobrecarregue o método __lt__ (operador <) para permitir que o algoritmo de ordenação compare apenas as chaves. Caso queira, você também pode sobrecarregar o operador __le__ (operador <=).
Não se esqueça que o Merge Sort é um algoritmo de ordenação estável. Tome cuidado na hora de intercalar elementos com chaves iguais.
Lembre-se que apenas as chaves devem ser ordenadas. Não considere o valor do elemento durante as comparações.
