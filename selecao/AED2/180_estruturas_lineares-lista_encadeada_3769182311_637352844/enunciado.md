# Remoção da lista encadeada

Remoção da lista encadeada
Complete as funções a seguir da estrutura de lista encadeada:
lst_cria(): cria uma nova lista encadeada vazia;
lst_insere_inicio(lis, elem): cria um novo nó com o valor do elemento passado por parâmetro e o insere no início da lista encadeada;
lst_remove_inicio(lis): remove o primeiro nó da lista encadeada.
Veja que já existe uma função chamada lst_imprime que percorre toda a lista encadeada e imprime seu conteúdo.
Elabore um programa principal que lê uma sequência de valores inteiros e faz uma das seguintes ações:
Se um número estritamente positivo for lido, ele deverá ser inserido no início da lista;
Se um número negativo for lido, tente remover do começo da lista uma quantidade de nós igual ao valor absoluto desse número. Por exemplo, se o número lido for -3, então tente remover 3 nós. Caso a lista tenha menos que 3 nós, remova até a lista ficar vazia;
Se o sentinela for lido, pare o processamento.
Ao final, chame a função lst_imprime para imprimir a lista resultante.
