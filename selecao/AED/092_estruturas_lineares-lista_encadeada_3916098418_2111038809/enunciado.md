# Inserção e remoção na lista ligada (Python)

Inserção e remoção na lista ligada
Crie uma estrutura de lista ligada e implemente as funções de inserção no fim da lista e remoção de um nó da lista que contém um valor passado por parâmetro.
Em seguida, faça um programa que lê uma sequência de inteiros e os insere, em ordem, em uma lista ligada inicialmente vazia.
Depois, leia uma segunda sequência de números inteiros. Remova cada um desses elementos da lista. Se houver mais de um elemento com o mesmo valor, remova apenas a primeira ocorrência.
Por fim, imprima o conteúdo da lista, que poderá estar vazia. Separe corretamente os elementos com vírgulas e não se esqueça do ponto final.

## Dicas

Use dicionários para representar os nós da lista ligada. Você também pode usar um dicionário para guardar uma referência para o primeiro e o último elementos da lista.
Não se esqueça que, na remoção, você precisará de uma referência para o nó removido e seu antecessor. Para evitar casos especiais, você pode utilizar um nó sentinela no início da lista.
Na hora de imprimir, você pode manipular o argumento end da função print para imprimir as vírgulas e o ponto final. Ou você pode acumular cada elemento da saída em uma lista e imprimir com ', '.join().
