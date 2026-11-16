# Remoção em árvore binária de busca (substit. pelo sucessor)

Remoção da árvore (2)
Elabore um programa capaz de fazer inserções e remoções em uma árvore binária de busca.
Lembre-se que o grau de um nó é o número de filhos. A remoção de um nó com grau zero (folha) consiste em simplesmente eliminar o nó da árvore; já a remoção de um nó com grau um exige que o nó removido seja substituído pelo seu filho esquerdo ou direito.
No caso do nó com grau 2, é necessário substituí-lo pelo seu ou sucessor. Geralmente essa escolha é arbitrária e pode gerar uma árvore diferente em cada caso. Como o Code Bench exige que a resposta para uma entrada seja única, neste exercício você deverá necessariamente trocar a chave pelo seu sucessor.
Em seguida, escreva um programa principal que lê duas listas. A primeira lista conterá as chaves que você deverá inserir em uma árvore binária de busca inicialmente vazia. A segunda conterá as chaves que você deverá remover da árvore.
Faça primeiro todas as operações de inserção e imprima o percurso pré-ordem da árvore inicial.
Em seguida, faça as operações de remoção. Após cada remoção, imprima o percurso pré-ordem da árvore.
As chaves deverão ser inseridas e removidas na ordem em que aparecerem nas listas.
