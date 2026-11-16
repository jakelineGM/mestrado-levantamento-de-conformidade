# Busca na árvore binária de busca

Busca na Árvore Binária de Busca
Em Python, podemos representar uma árvore como um dicionário contendo três chaves:
'valor': armazena o valor da chave na raiz da árvore;
'esq': uma referência para a sub-árvore esquerda da raiz (pode ser um dicionário ou None);
'dir': uma referência para a sub-árvore esquerda da raiz (pode ser um dicionário ou None).
Por exemplo, considere a árvore mostrada na figura a seguir:

A representação dessa árvore como um dicionário em Python é a seguinte:
T = { 'valor': 5,
 'esq': { 'valor': 3,
 'esq': { 'valor': 2,
 'esq': None,
 'dir': None
 },
 'dir': None
 },
 'dir': { 'valor': 8,
 'esq': None,
 'dir': None
 },
 }
Colocando tudo isso em uma única linha de código, fica assim:
{'valor': 5, 'esq': { 'valor': 3, 'esq': { 'valor': 2, 'esq': None, 'dir': None}, 'dir': None}, 'dir': { 'valor': 8, 'esq': None, 'dir': None},}
É desagradável de ler, mas, se essa linha estiver guardada em uma string, então é possível usar a função eval para montar rapidamente uma árvore a partir da entrada ao invés de montá-la por meio do algoritmo de inserção (que você irá elaborar em outro exercício).
Elabore uma função chamada arvore_busca(raiz, chave) para tentar encontrar uma chave em uma árvore binária de busca, ambas especificadas pelos parâmetros da função. A função deverá ser recursiva e retornar o nó que contém a chave desejada ou o objeto None.
Escreva também o corpo principal para ler a descrição de uma única árvore e uma lista de chaves a serem pesquisadas. Para cada chave, imprima uma linha indicando se a chave foi encontrada ou não, de acordo com os exemplos.
