# Inundação!

Inundação
Codibentinho mora em uma cidadezinha no interior que é cortada por um rio. A casa dele fica em um terreno bastante acidentado e, de vez em quando, o rio transborda. Algumas vezes o rio chega até a casa de Codibentinho, mas outras vezes o terreno acidentado protege sua casa.
Para você entender melhor essa situação, veja a figura abaixo:

A casa de Cobidentinho está à esquerda e, entre a casa dele e o rio, existe um pequeno morro. Já o prédio onde vive Labiana, à direita, está quase na altura do rio. Observe como se o rio transbordar, então o prédio de Labiana certamente será atingido pelas águas, enquanto a casa de Codibentinho possivelmente estará protegida. Mas nem sempre! Se as chuvas forem muito pesadas, então o rio subirá o suficiente para avançar sobre o morro e alcançar a casa de Codibentinho.
Escreva um programa que lê a descrição de um terreno, as coordenadas da casa de Codibentinho e a altura que a água do rio irá atingir. Descubra se o rio chegará à casa de Codibentinho ou não.

Entrada
O terreno será descrito por uma matriz que representa a altura de cada posição da região onde Codibentinho vive.
A entrada começa com cinco valores inteiros, N, M, A, L e C, que correspondem ao seguinte:
N e M são as dimensões da matriz (quantidade de linhas e de colunas, respectivamente). A matriz terá tamanho mínimo 5×5 e máximo 30×30;
A indica a altura máxima que o rio atingirá durante a chuva;
L e C indicam as coordenadas da casa de Codibentinho (linha e coluna, respectivamente). Elas serão sempre valores válidos (isto é, contidos na matriz). As coordenadas da matriz começam em zero. A casa de Codibentinho ocupa uma única célula da matriz.
Finalmente, haverá N×M inteiros com o conteúdo da matriz (isto é, alturas do terreno). As alturas serão valores entre 0 e 9. As posições do terreno nas quais a altura é zero indicam onde o rio corre.
Observe que a entrada sempre conterá um único rio e ele será contínuo. Não haverá posições com água que não estejam diretamente conectadas do rio. Isto é, de qualquer posição da matriz com valor 0 (água), será possível encontrar pelo menos uma outra célula da matriz "à esquerda", "acima", "abaixo" ou "à direita" que também possui valor 0 (água) e todas essas posições farão parte do rio.

Saída
Você deverá calcular as posições da matriz que ficarão cobertas pelo rio quando ele transbordar.
Se o rio atingir a casa de Codibentinho, você deverá imprimir a mensagem "Deu ruim!". Caso contrário, você deverá imprimir o emoji ":)".

## Dicas

Este é um exercício de pilhas. Você pode resolver com uma estrutura de dados para pilhas ou então com recursão.
Primeiro, elabore uma estrutura de dados para guardar o terreno, que pode ser baseada em uma matriz de inteiros.
Para ilustrar, considere o seguinte caso de teste:
Entrada do caso de teste de exemplo:
9 8 1 8 0
0 0 1 2 2 1 1 1
0 0 0 1 2 2 1 1
1 0 0 0 1 1 2 2
1 1 0 0 0 1 1 1
2 1 1 0 0 0 1 0
2 2 1 1 0 0 0 0
1 2 2 1 1 0 0 1
1 1 2 2 1 0 0 1
1 1 2 2 1 1 0 1
Os números indicam um terreno que cabe em uma matriz com 9 linhas e 8 colunas. A água alcançará altura máxima 1 e a casa de Codibentinho fica nas coordenadas (8,0).
Podemos desenhar a matriz em cores para você visualizar tudo isso:

As células por onde o rio passa estão indicadas em azul e a casa de Codibentinho com o "C" em fundo vermelho.
Conforme a entrada, o rio atingirá altura máxima 1. Isso significa que as seguintes células, marcadas com fundo roxo, ficarão submersas:

Note que, embora a casa de Codibentinho esteja em uma região com altura 1, a água não conseguiu ultrapassar a barreira de altura 2 que fica entre entre o rio e a casa dele. Portanto ele se safou desta vez!
Para resolver este exercício você deverá implementar um algoritmo flood-fill.
Procure primeiro uma célula da matriz que contenha água. Ela será parte do rio;
Inicie uma busca por todas as células adjacentes que podem ser alcançadas pelo rio. Isto é, as células "acima", "abaixo", "à esquerda" e "à direita" que têm altura no máximo A;
Elabore um mecanismo para procurar as células adjacentes a essas quatro células. Você pode fazer isso com uma função recursiva ou então empilhando as coordenadas das células conforme você as encontra. É importante usar alguma estrutura para não fazer recursão/empilhar a mesma célula duas vezes;
Se as coordenadas da casa de Codibentinho forem encontradas, então ela será inundada. Se a recursão terminar ou se a pilha esvaziar antes da casa de Codibentinho ser encontrada, então ela estará protegida.
