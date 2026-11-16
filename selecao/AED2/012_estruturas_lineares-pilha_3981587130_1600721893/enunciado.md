# Operadores balanceados

Operadores balanceados
Uma sequência de parênteses, colchetes e chaves é considerada bem-formada se para cada operador que "abre" existe um correspondente que "fecha". Por exemplo: A sequencia "{([])}" é bem-formada, pois todos os operadores fechados na ordem inversa que foram abertos. Por outro lado, a sequencia "([)]" não é bem formada, pois o operador ")" foi fechado no momento errado.
Faça um programa que lê várias sequências de operadores e imprime, para cada um deles, a palavra SIM ou a palavra NAO, indicando se a sequência está balanceada. Cada sequência de entrada terá no máximo 100 caracteres.
A entrada termina com uma linha contendo apenas um ponto final.

## Dicas

A resolução deste exercício consiste em verificar se cada operador de abertura ([, (, e {) tem um operador de fechamento correspondente.
Isso pode ser feito com uma pilha. Leia a sequência em uma string e depois processe essa sequência caracter por caracter:
Se o caracter for um operador de abertura, coloque-o no topo de uma pilha. Isso indica que existe um operador aberto que precisa ser fechado.
Se for um caracter de fechamento, verifique se ele é compatível com o operador que está no topo da pilha. Se for, então remova o operador do topo da pilha.
Esse processo só funcionará se a sequência de abrir e fechar operadores estiver correta. Se aparecer um operador de fechamento e a pilha estiver vazia ou o topo da pilha for incompatível, então a sequência não está balanceada.
Além disso, ao final da string a pilha deverá estar vazia. Caso contrário, algum operador foi aberto, mas não fechado.
Não é necessário usar uma lista encadeada para a pilha.
