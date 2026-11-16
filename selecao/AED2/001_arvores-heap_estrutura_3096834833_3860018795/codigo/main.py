def max_heapfy(A, i):
    tam = len(A)
    maior = i
    esquerda = 2*i + 1
    direita = 2*i + 2
    if esquerda < tam and A[esquerda] > A[maior]:
        maior = esquerda
    if direita <tam and A[direita] > A[maior]:
        maior = direita
    if maior != i:
        A[i], A[maior] = A[maior], A[i]
        A = max_heapfy(A, maior)
    return A
  
caso = eval(input())
while caso != []:
  quase_heap =  max_heapfy(caso, 0)
  print(quase_heap)
  caso = eval(input())