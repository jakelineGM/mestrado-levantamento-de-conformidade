# O QuickSort do brasileira (E/S para Python)

O Quick Sort no Brasileirão
Futebol é o esporte mais popular do planeta, contando com milhares de times em campeonatos ao redor do mundo inteiro.
Com tantos times, é dura a tarefa manter registro dos jogos e dos placares de todos os campeonatos. Portanto, neste exercício você deve escrever um programa que recebe o nome de um campeonato, os nomes dos times e uma descrição de todos os jogos. Calcule e imprima a tabela do campeonato, em ordem do vencedor ao perdedor.
Cada jogo pode terminar em vitória de um dos times ou empate. Não há diferença entre jogos em casa ou como visitante. O time vencedor leva 3 pontos e, em caso de empate, ambos os times levam 1 ponto.
O placar geral do campeonato deve ser ordenado, com o método Quick Sort, pelos seguintes critérios:
O primeiro critério é o número de pontos. Um time que fez mais pontos, obviamente, estará melhor classificado que os times com menor número de pontos;
O segundo critério é o número de vitórias. Se dois times tiverem o mesmo número de pontos, então o time que tiver mais vitórias estará melhor classificado;
O terceiro critério é o saldo de gols. Se dois times empatarem nos critérios anteriores, então o time que tiver a maior diferença entre gols feitos e gols recebidos será melhor classificado;
O quarto critério é o número de gols marcados. Se dois times empatam em todos os critérios anteriores, então o time que marcou mais gols será melhor classificado;
O quinto critério é o número de partidas jogadas. Se dois times empatam em todos os critérios anteriores, então o time que realizou menos jogos até o momento será melhor classificado;
O último critério é o nome do time. Se dois times empatam em todos os critérios anteriores, então o time com nome de menor ordem lexicográfica estará melhor classificado.

Entrada
A entrada será uma descrição completa de vários campeonatos. Cada campeonato é um caso de teste.
O primeiro valor na entrada será um inteiro N indicando o número de campeonatos.
Cada campeonato é uma descrição dos times e de todos os jogos realizados. A descrição do campeonato começa com uma linha em branco (que você deve ler e descartar com um comando input). Na linha seguinte aparecerá o nome do campeonato, que é uma string sem espaços que você pode ler com input.
Em seguida, aparecerá um inteiro T indicando o número de times (1 < T ≤ 30), seguido de T palavras com os nomes dos times. Os nomes dos times podem conter letras maiúsculas e minúsculas, números, hífen e o caracter barra-baixa (_).
Após o nome do último time, haverá um inteiro G indicando o número de jogos realizados até agora.
Os G jogos serão descritos da seguinte forma: o nome de um time, o separador :, o número de gols marcados por esse time, o separador #, o nome do segundo time, o separador : e o número de gols marcados pelo segundo time. Por exemplo, a descrição Bananeiras:3#Sao_Pedro:2 indica que a equipe Bananeiras venceu o time do São Pedro por 3 a 2. Todos os gols são números não negativos menores que 20. Você pode presumir que todos os nomes que aparecem nos jogos são times que foram apresentados anteriormente. Nenhum time irá jogar contra si mesmo.

Saída
Para cada campeonato, imprima primeiramente o nome do campeonato em uma linha. As próximas T linhas devem descrever os T times do campeonato, ordenados de acordo com as regras apresentadas anteriormente.
Para cada time, imprima uma linha com o seguinte formato:
[a] - Nome_do_time: [b] pontos, [c] jogos ([d]-[e]-[f]), d.g. [g] ([h]-[i])
Substituindo:
[a] pela posição do time no placar
[b] pelo total de pontos que o time conseguiu
[c] pelo número de jogos que o time jogou
[d] pelo número de vitórias
[e] pelo número de empates
[f] pelo número de derrotas
[g] pela diferença de gols (marcados - sofridos)
[h] pelo número de gols marcados
[i] pelo número de gols sofridos
Imprima uma linha em branco após cada campeonato.
