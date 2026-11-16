# Manipulação do grafo

Manipulação do grafo
Implemente uma estrutura de grafos usando representação de listas de adjacências. Você pode criar uma classe chamada Grafo ou o seu grafo pode ser simplesmente uma lista de listas em Python.
Não é necessário implementar uma estrutura de lista ligada. Você pode usar a classe list tanto para a lista de vértices quanto para cada lista de arestas.
O seu grafo deve suportar as seguintes operações:
Iniciar um grafo não direcionado contendo N vértices (não será necessário criar novos vértices ou remover vértices).
Inserir uma aresta com peso (u,v,w).
Remover uma aresta (u,v). Se a aresta não existir, então sua implementação não deverá fazer nada (não imprima nada, não lance exceções).
Verificar o peso da aresta (u,v).
Em seguida, escreva um programa principal que lê uma série de comandos de inserção e remoção de arestas, seguido de uma série de consultas de pesos de arestas.

Entrada
A entrada consistirá de vários grafos.
Cada descrição de um novo grafo começa com um inteiro N indicando o número de vértices que o grafo deverá ter. O conjunto de vértices deverá ser V={v0​,v1​,…,vN−1​} e o conjunto inicial de arestas deverá ser E={}.
Em seguida aparece um valor M indicando quantas operações de inserção e remoção devem ser feitas. Isso é seguido de M linhas contendo tuplas u,v,w (sem parênteses). Se w=0, então você deve tentar remover a aresta (u,v) do grafo. Caso contrário você deverá inserir a aresta (u,v,w). Lembre-se que o grafo é não direcionado.
Após as arestas, aparece um inteiro Q indicando quantas consultas devem ser realizadas. Cada consulta será uma tupla u,v (sem parênteses). Se a aresta existir, você deverá imprimir o peso w((u,v)). Caso contrário você não deverá imprimir nada.
Ao final de cada caso de teste haverá uma linha com separadores, a qual você deverá descartar.
A entrada termina quando aparecer N=0.
Todos os valores na entrada serão números inteiros.
Para simplificar a realização desta atividade, a leitura do caso de teste já está no código inicial.

Saída
Antes de imprimir a saída de cada grafo, imprima a mensagem "Grafo {}", substituindo a sequência {} pelo número incremental do grafo.
Para cada consulta de uma aresta (u,v), se ela existir, imprima a string "{u},{v}: {w}", substituindo {u} e {v} pelas adjacências da aresta consultada e {w} pelo peso da aresta. Caso contrário não imprima nada.
Imprima uma linha em branco após a saída de cada grafo.
