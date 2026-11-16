# Particionamento de Hoare (para QuickSort)

Particionamento de Hoare
Implemente, em Python, o algoritmo de particionamento de Hoare.
Selecione o elemento central como pivô. Se houver dois elementos centrais, escolha o que está mais à esquerda;
Percorra o vetor da esquerda para a direita com um contador, procurando um elemento que pode ser movido para a direita do pivô;
Percorra o vetor da direita para a esquerda com um segundo contador, procurando um elemento que pode ser movido para a esquerda do pivô;
Se os contadores não "cruzaram", troque os elementos sinalizados por eles de posição.
O algoritmo finaliza quando o segundo contador se encontra com o primeiro ou troca de lugar com ele. O contador que finaliza mais à esquerda marca o ponto de corte.

Entrada
A entrada será uma coleção de casos de teste.
Cada caso de teste será uma lista de tuplas (chave, valor). O valor será dado em notação Python e poderá ter qualquer tipo de dados imprimível. Use eval para ler o caso de teste.
A entrada termina quando aparecer uma lista vazia.

Saída
Para cada caso de teste, imprima primeiro a mensagem Caso {}, substituindo a sequência {} pelo número do caso de teste.
Em seguida imprima uma linha contendo a parte esquerda do vetor particionado e, em uma segunda linha, a parte direita do vetor particionado.
Imprima uma linha em branco depois de cada caso de teste.

Dica
Após a leitura do caso de teste, crie uma lista com elementos de uma classe na qual você sobrecarregou o método __lt__.
