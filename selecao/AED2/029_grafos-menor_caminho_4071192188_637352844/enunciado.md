# Buraco de minhoca (Floyd-Warshall)

Buracos de Minhoca!
O Sr. Floyd é um renomado cientista do Grafoverso, onde buracos de minhoca são dobras do espaço-tempo que permitem a um viajante deslocar-se nas quatro dimensões (incluindo tempo).
Recentemente, o Sr. Floyd finalizou um mapa bastante completo dos buracos de minhoca do Grafoverso. A figura abaixo é uma pequena amostra. Nela, as setas indicam deslocamento no espaço e os números indicam deslocamento no tempo (em anos).

Observe que os buracos de minhoca são unidirecionais, mas em alguns casos existem buracos de ida e de volta, como entre Starboundia e Ad 42.
Observe também que alguns buracos levam o viajante para o futuro e, outros, para o passado. Por exemplo, ao viajar de Nox 16 até Dabu, um astronauta seria levado 0,17 ano para o futuro (aproximadamente 62 dias). Por outro lado, ao viajar de Nox 16 para Ad 42, o viajante se encontraria 0,2 ano no passado (cerca de 73 dias).
Mais interessante, a combinação de alguns buracos de minhoca permite viajar quase livremente no tempo. Por exemplo, uma viagem completa de Lux 138, passando por Nox 16 e Ad 42, para enfim retornar ao ponto de origem, deslocaria um astronauta aproximadamente um mês para o passado. Teoricamente, um astronauta poderia repetir essa viagem indefinidamente e viajar para o passado quantos meses quisesse!
Seu objetivo neste exercício é analisar um mapa do Grafoverso e decidir se é ou não possível viajar arbitrariamente para o passado.

Entrada
A entrada consistirá de apenas um grafo.
A primeira linha conterá uma lista de nomes de estrelas e planetas que podem abrigar buracos de minhoca. Cada nome será uma string contendo letras, números e hífens. Os nomes serão separados por espaços e a linha será terminada por um ponto final (separado do último nome por espaço).
Em seguida, haverá um número arbitrário de linhas descrevendo buracos de minhoca. Cada buraco será descrito por três itens: o nome da origem, o nome do destino e um número de ponto flutuante indicando o deslocamento temporal do buraco.
A entrada será finalizada pela string . . 0.

Saída
Após analisar o mapa, verifique se é possível viajar arbitrariamente para o passado. Ou seja, verifique se existem buracos de minhoca em uma disposição que permita sair de uma estrela ou planeta e retornar ao ponto de origem voltando no tempo em qualquer quantidade de dias, meses ou anos.
Caso seja possível, imprima o texto Great Scott!!, exatamente.
Se não for possível, imprima o texto Pesado..., exatamente.

Restrições
O nome de cada estrela ou planeta terá no máximo 80 caracteres;
O número de estrelas e planetas será no máximo 20;
O número de buracos de minhocas será no máximo 400;
A origem de um buraco pode ser igual ao destino;
Não haverá buracos com mesmas origens e destinos (buracos "paralelos");
O deslocamento temporal de qualquer buraco será no máximo 10 anos;
Não se preocupe com erros de aproximação de ponto flutuante (não haverá nenhum número tão próximo de zero que possa causar essa situação).

## Dicas

Usar matriz de adjacências levará ao resultado mais facilmente...
