# Os primeiros serão os últimos

Os primeiros serão os últimos
Neste exercício você deve manipular uma lista duplamente encadeada da seguinte forma:
Leia um inteiro N e construa uma lista de N elementos em sequência, isto é 1, 2, 3, ..., N
Leia um inteiro x
Procure o elemento x na lista
Pegue todos os elementos desde o primeiro da lista até o elemento x e insira, na ordem inversa, no fim da lista
Repita as operações 2-4 tantas vezes quanto necessário
Imprima a lista resultante
Por exemplo, suponha que N=8, então a lista inicial será a seguinte:
1 ⇄ 2 ⇄ 3 ⇄ 4⇄ 5 ⇄ 6 ⇄ 7 ⇄ 8
Se x=4, então você deve pegar os elementos 1 ⇄ 2 ⇄ 3 ⇄ 4, invertê-los e inserir no final. A lista resultante ficará assim:
5 ⇄ 6 ⇄ 7 ⇄ 8 ⇄ 4 ⇄ 3 ⇄ 2 ⇄ 1
Depois você deverá ler o próximo x. Suponha que ele é x=7. Então você deve pegar os elementos 5 ⇄ 6 ⇄ 7, invertê-los e inserir no final. A lista ficará assim:
8 ⇄ 4 ⇄ 3 ⇄ 2 ⇄ 1 ⇄ 7 ⇄ 6 ⇄ 5
As inversões acabam quando x=0. Nesse momento você deverá parar de processar e imprimir o conteúdo da lista.
