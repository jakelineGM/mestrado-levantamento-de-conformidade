# Passos do Insertion Sort (E/S para C)

Passos do Insertion Sort
Escreva uma versão modificada do algoritmo de ordenação Insertion Sort (método da inserção) que mostra os passos que são realizados. Para isso, imprima o conteúdo do vetor assim que a função for chamada e cada vez que algum elemento do vetor for modificado. Não imprima nada quando você fizer atribuições que não alterem valores do vetor.

## Dicas

Exemplo 1
Entrada:
6
1 3 4 2 5 6
Saída esperada:
{1, 3, 4, 2, 5, 6}
{1, 3, 4, 4, 5, 6}
{1, 3, 3, 4, 5, 6}
{1, 2, 3, 4, 5, 6}
Explicação:
Na primeira linha foi feita a impressão da lista original. As linhas subsequentes mostram os valores que foram modificados para inserção do elemento 2 na sua posição correta.

Exemplo 2:
Entrada:
10
1 2 4 4 4 4 5 3 6 6
Saída esperada:
{1, 2, 4, 4, 4, 4, 5, 3, 6, 6}
{1, 2, 4, 4, 4, 4, 5, 5, 6, 6}
{1, 2, 4, 4, 4, 4, 4, 5, 6, 6}
{1, 2, 3, 4, 4, 4, 4, 5, 6, 6}
Explicação:
Na primeira linha foi feita a impressão da lista original. As linhas subsequentes mostram os valores que foram modificados para inserção do elemento 3 na sua posição correta. Observe que, para encontrar essa posição, o algoritmo faz vários passos nos quais uma posição que já contém o valor 4 recebe novamente o valor 4, mas nenhuma impressão é realizada nesses casos.
