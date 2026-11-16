# Descartando cartas (E/S simplificada)

Brincando com cartas
Neste exercício, você deverá simular uma brincadeira com cartas. A brincadeira é assim:
N cartas numeradas de 1 até N são colocadas em um monte com a carta 1 no topo e a carta N no fundo;
Quando o monte contiver uma única carta, a brincadeira terminou;
Senão, você deve retirar a carta que está no topo e descartá-la. Depois, pegue a carta seguinte e coloque-a no fundo do monte.
Os passos 2 e 3 devem ser repetidos até que reste uma única carta no monte.
Entrada
A entrada contém várias partidas. Cada partida é descrita por um inteiro N que diz o número de cartas no monte.
A entrada termina com N=0.
Saída
Ao final de cada partida você deverá imprimir duas linhas, de acordo com os seguintes formatos:
Descartadas: X Y Z W ...
Restou: Q
A primeira linha contém a lista de cartas que foram removidas do monte, na ordem em que elas foram removidas. A segunda é a carta que restou no monte.
Use uma estrutura de lista duplamente encadeada para representar o monte.
