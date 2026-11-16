# Árvore AVL 3: rotações simples

AVL 1: rotações simples
Neste exercício você deve escrever mais uma parte da solução para árvores AVL!
Você deverá elaborar funções para inserir chaves em uma árvore AVL e realizar rotações simples, isto é, rotações simples à esquerda (RR) ou rotações simples à direita (LL). Nos casos de teste deste exercício não haverá necessidade de realizar rotações duplas.
Você pode representar os nós da árvore como dicionários. Os nós podem ter as chaves 'valor', 'esq' e 'dir' e 'h', significando, respectivamente, o valor da chave no nó, uma referência para a raiz da sub-árvore esquerda, uma referência para a raiz da sub-árvore direita e a altura do nó.
Elabore uma função para realizar rotação simples à esquerda.
Elabore uma função para realizar rotação simples à dirita.
Elabore uma função para fazer inserção em árvore binária de busca, tomando o cuidado com as situações que exigem rotação simples.
Atualize a altura de cada nó quando fizer inserções e rotações na árvore. Não se esqueça de atualizar a altura de cada filho antes de atualizar a altura da raiz da sub-árvore.
Para este exercício, considere que a altura de uma sub-árvore vazia é 0. Então todos os nós folhas possuem altura 1.
Para este exercício, considere que o fator de balanceamento é calculado como a diferença entre a altura da sub-árvore direita e a sub-árvore esquerda (nessa ordem).
Escreva um programa principal que cria várias árvores, efetuando rotações para mantê-las simplesmente balanceadas.
Para cada árvore, imprima os resultados dos percursos pré-ordem e pós-ordem.
Entrada e Saída
A entrada conterá vários casos de teste. Cada caso de teste é uma lista contendo uma sequência de chaves que devem ser inseridas em uma árvore inicialmente vazia. A entrada termina quando aparecer a lista vazia (ela não é um caso de teste).
Como saída, imprima primeiro a frase 'Arvore {}', sendo que o especificador '{}' deve ser substituído pelo número da árvore que está sendo processada. Em seguida, imprima os percursos pré-ordem e pós-ordem da árvore obtida após a operação de rotação. Siga a formatação contida nos exemplos. Imprima uma linha em branco após cada caso de teste.
