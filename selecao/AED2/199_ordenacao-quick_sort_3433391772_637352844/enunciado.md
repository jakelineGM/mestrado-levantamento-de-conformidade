# Quick Sort (chave/valor)

Quick Sort
Faça um programa em Python que ordena uma lista de pares (chave, valor) utilizando o método Quick Sort com particionamento de Hoare.
O método da ordenação Quick Sort com particionamento de Hoare é baseado nos seguintes passos:
Selecione um pivô, que deverá ser a chave do elemento central. Se houver dois elementos centrais, escolha aquele que está mais à esquerda;
Particione a lista de modo que todas as chaves à esquerda do pivô sejam menores ou iguais a ele e todas as chaves à direita do pivô sejam maiores ou iguais a ele;
Ordene recursivamente as partes à esquerda e à direita do pivô.
Use seu método de ordenação um programa principal que lê uma série de listas contendo coleções de tuplas (chave, valor) e imprima as listas ordenadas. Pare quando a entrada contiver a lista vazia.

Entrada
A entrada será uma coleção de casos de teste.
Cada caso de teste será uma lista de tuplas (chave, valor). O valor será em notação Python e poderá conter qualquer tipo de dados. Use eval para ler o caso de teste.
A entrada termina quando aparecer uma lista vazia.

Saída
Para cada caso de teste, imprima primeiro a mensagem Caso {}, substituindo a sequência {} pelo número do caso de teste.
Em seguida imprima, linha por linha, os elementos ordenados (tanto a chave quanto o valor, separados por espaço).
Imprima uma linha em branco ao final do caso de teste.

Dica
Após a leitura do caso de teste, crie uma lista com elementos de uma classe na qual você sobrecarregou o método __lt__.
Lembre-se que você deve ordenar apenas pela chave.
