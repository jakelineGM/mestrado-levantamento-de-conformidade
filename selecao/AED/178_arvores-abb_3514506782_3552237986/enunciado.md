# Pesquisa na árvore binária de busca

Pesquisa na Árvore Binária
Escreva um programa que lê uma árvore binária de busca da entrada e faz pesquisa por um valor.
A árvore de busca será representada como um dicionário que contém três chaves:
'valor': guarda o valor da chave do nó
'esq': uma referência para o filho esquerdo do nó. Se a sub-árvore esquerda for vazia, então o valor associado a esta chave será None. Caso contrário, será um dicionário conténdo todos os campos de um nó.
'dir': uma referência para o filho direito do nó. Pode ser None ou um dicionário.
Veja nas dicas do exercício alguns exemplos de árvores e suas representações como dicionários.

Entrada
A entrada conterá vários casos de árvores que devem ser processadas separadamente.
Cada caso de começa com uma linha representando um dicionário em notação Python. Leia essa linha usando input e eval.
Em seguida, haverá uma linha contendo uma lista, em notação Python, contendo as chaves que você deve pesquisar. Cada chave será um número inteiro não negativo.
Depois da lista de chaves, pode haver uma próxima árvore ou um dicionário vazio ({}) indicando o fim da entrada.

Saída
Para cada chave pesquisada, você deverá imprimir uma das duas seguintes mensagens:
"Chave {} encontrada"
"Chave {} nao encontrada"
Sendo que a sequência de caracteres {} deve ser substituída pelo valor da chave pesquisa.
Após a última chave, você deverá imprimir a mensagem:
"Encontrei {} chaves"
sendo que você deve substituir as sequências de caracteres {} pelo número de chaves encontradas.
Imprima uma linha em branco ao final do caso para aumentar a legibilidade da saída.

## Dicas

Exemplo 1
Por exemplo, se a árvore contiver apenas a chave 5, então sua representação será a seguinte:
T = { 'valor': 5,
 'esq': None,
 'dir': None
 }

Ou, em uma única linha:
T = { 'valor': 5, 'esq': None, 'dir': None }

Exemplo 2
Se a árvore contiver a chave 5 na raiz e também a chave 2 em um dos filhos, então a representação será a seguinte:
T = { 'valor': 5,
 'esq': { 'valor': 2,
 'esq': None,
 'dir': None
 },
 'dir': None
 }

Ou, em uma única linha:
T = { 'valor': 5, 'esq': { 'valor': 2, 'esq': None, 'dir': None }, 'dir': None }

Exemplo 3
Se a árvore for a da figura abaixo...

Então sua representação como um dicionário será a seguinte:
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

É um pouco mais chato visualizar essa árvore em uma única linha, mas é assim que ela irá aparecer no caso de teste:
T = { 'valor': 5, 'esq': { 'valor': 3, 'esq': { 'valor': 2, 'esq': None, 'dir': None }, 'dir': None }, 'dir': { 'valor': 8, 'esq': None, 'dir': None } }
