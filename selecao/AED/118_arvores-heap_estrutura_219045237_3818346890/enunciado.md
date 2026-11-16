# Implementação do heapify

Operação max_heapify
Escreva uma função, chamada max_heapify, que recebe como entrada um vetor contendo uma “quase-heap” máxima e transforma esse vetor em uma heap máxima.
Uma “quase-heap” máxima é um vetor A=(a1​,a2​,a3​,…,an−1​) no qual todos os elementos respeitam a propriedade de heap máxima, com exceção do primeiro, que pode ou não respeitar a propriedade de heap máxima.
Para transformar essa “quase-heap” em uma heap, compare o elemento na posição a ser testada do vetor com os seus dois filhos (se houver). Caso ele viole a propriedade de heap com algum dos filhos, troque-o de posição com o filho mais promissor. Aplique max_heapify recursivamente até que a propriedade de heap não seja mais violada.
Para recordar, dado um elemento A[i] em uma heap...
O pai de A[i] pode ser encontrado no índice pai(i)=⌊2i−1​⌋;
O elemento A[0] não possui pai;
O filho esquerdo de A[i], se existir, pode ser encontrado no índice 2i+1 e o filho direito, se existir, em 2i+2;
A propriedade de heap máxima é A[pai(i)]⩾A[i].
Em seguida, faça um programa principal que lê várias listas em notação Python, representando “quase-heaps”. Para cada uma imprima a lista resultante da operação max_heapify. A entrada termina com a lista vazia ([]).
